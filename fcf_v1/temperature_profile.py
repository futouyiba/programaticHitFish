"""Fail-closed semantic compiler for TemperatureProfile authoring artifacts."""

from copy import deepcopy
from datetime import datetime
import json
import math
import re
from typing import Any, Dict, List, Set

from .dsl import Diagnostic, DSLCompileError


_SOURCE_KINDS = {"SENSOR", "HYDRO_MODEL", "MANUAL_CALIBRATION"}
_SHA256 = re.compile(r"^sha256:[0-9a-fA-F]{64}$")


def _number(value: Any) -> bool:
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value))


def compile_temperature_profile(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Validate cross-field TemperatureProfile invariants and return a copy.

    JSON Schema owns field shape. This semantic pass owns relationships that
    JSON Schema cannot express portably: ranges, containment, identity,
    source-policy coverage and layer overlap.
    """
    d: List[Diagnostic] = []
    if raw.get("schema_version") != "fcf.temperature_profile.v1":
        d.append(Diagnostic("TEMPERATURE_SCHEMA_VERSION", "schema_version", "expected fcf.temperature_profile.v1"))

    digest = raw.get("source_manifest_hash")
    if not isinstance(digest, str) or not _SHA256.fullmatch(digest):
        d.append(Diagnostic("SOURCE_MANIFEST_HASH", "source_manifest_hash", "expected sha256 plus 64 hexadecimal digits"))

    clock = raw.get("temporal_clock") or {}
    epoch = clock.get("epoch")
    if epoch != "SIMULATION_START":
        try:
            if not isinstance(epoch, str):
                raise ValueError
            datetime.fromisoformat(epoch.replace("Z", "+00:00"))
        except (TypeError, ValueError):
            d.append(Diagnostic("CLOCK_EPOCH", "temporal_clock.epoch", "epoch must be SIMULATION_START or ISO-8601"))

    source_policy = raw.get("source_policy") or {}
    accepted = source_policy.get("accepted_source_kinds") or []
    accepted_set = set(accepted)
    if len(accepted) != len(accepted_set) or not accepted_set or not accepted_set <= _SOURCE_KINDS:
        d.append(Diagnostic("SOURCE_ALLOWLIST", "source_policy.accepted_source_kinds", "source kinds must be unique and known"))
    freshness = source_policy.get("freshness_by_source_s") or {}
    missing_freshness = accepted_set - set(freshness)
    if missing_freshness:
        d.append(Diagnostic("SOURCE_FRESHNESS_MISSING", "source_policy.freshness_by_source_s", f"missing freshness for {sorted(missing_freshness)}"))
    maximum_uncertainty = source_policy.get("maximum_uncertainty_c")
    if not _number(maximum_uncertainty) or maximum_uncertainty < 0:
        d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", "source_policy.maximum_uncertainty_c", "value must be finite and >= 0"))
    for source_kind, seconds in freshness.items():
        if not _number(seconds) or seconds < 0:
            d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", f"source_policy.freshness_by_source_s.{source_kind}", "freshness must be finite and >= 0"))

    interpolation = raw.get("interpolation_policy") or {}
    for field in ("maximum_spatial_gap_m", "maximum_depth_gap_m", "maximum_time_gap_s"):
        value = interpolation.get(field)
        if not _number(value) or value < 0:
            d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", f"interpolation_policy.{field}", "gap must be finite and >= 0"))

    layers = raw.get("depth_layers") or []
    mode = raw.get("profile_mode")
    if mode == "SINGLE_LAYER" and len(layers) != 1:
        d.append(Diagnostic("SINGLE_LAYER_COUNT", "depth_layers", "SINGLE_LAYER requires exactly one layer"))
    if not layers:
        d.append(Diagnostic("DEPTH_LAYERS_REQUIRED", "depth_layers", "at least one depth layer is required"))

    layer_ids: Set[str] = set()
    sample_ids: Set[str] = set()
    numeric_layers = []
    for i, layer in enumerate(layers):
        path = f"depth_layers[{i}]"
        if not isinstance(layer, dict):
            d.append(Diagnostic("DEPTH_LAYER_SHAPE", path, "layer must be an object"))
            continue
        layer_id = layer.get("layer_id")
        if not isinstance(layer_id, str) or not layer_id or layer_id in layer_ids:
            d.append(Diagnostic("DUPLICATE_LAYER_ID", path + ".layer_id", "layer ID must be non-empty and unique"))
        layer_ids.add(layer_id)
        lower, upper = layer.get("depth_min_m"), layer.get("depth_max_m")
        if not _number(lower) or not _number(upper) or lower < 0 or upper <= lower:
            d.append(Diagnostic("DEPTH_LAYER_RANGE", path, "layer must satisfy 0 <= depth_min_m < depth_max_m"))
        else:
            numeric_layers.append((float(lower), float(upper), path))
        for j, sample in enumerate(layer.get("samples") or []):
            sample_path = f"{path}.samples[{j}]"
            if not isinstance(sample, dict):
                d.append(Diagnostic("TEMPERATURE_SAMPLE_SHAPE", sample_path, "sample must be an object"))
                continue
            sample_id = sample.get("sample_id")
            if not isinstance(sample_id, str) or not sample_id or sample_id in sample_ids:
                d.append(Diagnostic("DUPLICATE_SAMPLE_ID", sample_path + ".sample_id", "sample ID must be globally unique"))
            sample_ids.add(sample_id)
            depth = sample.get("depth_m")
            if not _number(depth) or depth < 0:
                d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", sample_path + ".depth_m", "depth must be finite and >= 0"))
            if (_number(lower) and _number(upper) and _number(depth)
                    and not (lower <= depth < upper)):
                d.append(Diagnostic("SAMPLE_OUTSIDE_LAYER", sample_path + ".depth_m", "sample depth must be inside its half-open layer"))
            value_c = sample.get("value_c")
            uncertainty_c = sample.get("uncertainty_c")
            if not _number(value_c):
                d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", sample_path + ".value_c", "temperature must be finite"))
            if not _number(uncertainty_c) or uncertainty_c < 0:
                d.append(Diagnostic("NONFINITE_PHYSICAL_VALUE", sample_path + ".uncertainty_c", "uncertainty must be finite and >= 0"))
            valid_from, valid_to = sample.get("valid_from_ms"), sample.get("valid_to_ms")
            observed = sample.get("observed_at_ms")
            if not all(isinstance(x, int) and not isinstance(x, bool) for x in (valid_from, valid_to, observed)) or valid_from >= valid_to:
                d.append(Diagnostic("SAMPLE_VALIDITY_RANGE", sample_path, "sample requires integer valid_from < valid_to"))
            elif not (valid_from <= observed < valid_to):
                d.append(Diagnostic("SAMPLE_OBSERVED_OUTSIDE_VALIDITY", sample_path + ".observed_at_ms", "observed time must be inside validity interval"))
            if sample.get("source_kind") not in accepted_set:
                d.append(Diagnostic("SAMPLE_SOURCE_NOT_ALLOWED", sample_path + ".source_kind", "sample source is outside accepted_source_kinds"))
            calibration = sample.get("calibration_revision")
            if calibration is not None and (not isinstance(calibration, str) or not calibration):
                d.append(Diagnostic("CALIBRATION_REVISION", sample_path + ".calibration_revision", "revision must be null or non-empty"))

    numeric_layers.sort()
    for left, right in zip(numeric_layers, numeric_layers[1:]):
        if right[0] < left[1]:
            d.append(Diagnostic("DEPTH_LAYER_OVERLAP", f"{left[2]},{right[2]}", "depth layers must not overlap"))

    boundary_ids: Set[str] = set()
    for i, boundary in enumerate(raw.get("thermocline_boundaries") or []):
        path = f"thermocline_boundaries[{i}]"
        if not isinstance(boundary, dict):
            d.append(Diagnostic("THERMOCLINE_SHAPE", path, "boundary must be an object"))
            continue
        boundary_id = boundary.get("boundary_id")
        if not isinstance(boundary_id, str) or not boundary_id or boundary_id in boundary_ids:
            d.append(Diagnostic("DUPLICATE_BOUNDARY_ID", path + ".boundary_id", "boundary ID must be unique"))
        boundary_ids.add(boundary_id)
        top, bottom = boundary.get("top_depth_m"), boundary.get("bottom_depth_m")
        if not _number(top) or not _number(bottom) or top < 0 or bottom <= top:
            d.append(Diagnostic("THERMOCLINE_RANGE", path, "boundary must satisfy 0 <= top_depth_m < bottom_depth_m"))
        valid_from, valid_to = boundary.get("valid_from_ms"), boundary.get("valid_to_ms")
        if (not isinstance(valid_from, int) or isinstance(valid_from, bool)
                or not isinstance(valid_to, int) or isinstance(valid_to, bool)
                or valid_from >= valid_to):
            d.append(Diagnostic("THERMOCLINE_VALIDITY_RANGE", path, "boundary requires valid_from < valid_to"))

    if d:
        raise DSLCompileError(d)
    try:
        return json.loads(json.dumps(deepcopy(raw), sort_keys=True, allow_nan=False))
    except ValueError as exc:
        raise DSLCompileError([Diagnostic("NONFINITE_JSON_VALUE", "$", str(exc))]) from exc
