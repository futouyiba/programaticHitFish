"""0.3.4.0-B fixed Bake template prototype.

B-current runtime contract only. The module intentionally exposes no author-editable
DSL or per-subject program picker. Static authoring resolves to a fish-side subject
and a pond-side opportunity seed; environment evaluation consumes those two objects
plus one canonical ConditionGroup.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any, Mapping, Sequence


FIXED_BAKE_TEMPLATE_PROGRAM_ID = "FCF_BAKE_TEMPLATE_V1"
BAKE_ALGORITHM_CONTRACT_VERSION = "AFLA_R2_1"

SOFT_FACTOR_MIN = 0.05
SOFT_FACTOR_MAX = 1.0
CORE_SUBOPTIMAL_FIT = 0.60
SECONDARY_LOSS_SCALE = 1.0 / 6.0
SECONDARY_LOSS_BUDGET = 0.5 * (-math.log(CORE_SUBOPTIMAL_FIT))

AGGREGATION_ROLES = frozenset({"CORE", "SECONDARY", "EXCLUDED"})
GATE_FAILURE_CAPS = {
    "NONE": None,
    "HARD_EXCLUDE": 0.00,
    "TRACE_RESIDUAL": 0.01,
    "LOW_RESIDUAL": 0.05,
}


class BakeConfigError(ValueError):
    pass


@dataclass(frozen=True)
class ConditionGroup:
    condition_group_id: str
    structure_type: str
    water_temperature_range: tuple[float, float]
    feeding_ecology_layers: tuple[str, ...]
    time_period: str


@dataclass(frozen=True)
class BakeEvaluationResult:
    env_coeff: float
    spatial_opportunity_intensity: float
    trace: Mapping[str, Any]


def migrate_legacy_binding(binding: Mapping[str, Any]) -> Mapping[str, str]:
    """Normalize legacy ConditionRole into current AggregationRole.

    OFF + NONE is losslessly equivalent to EXCLUDED + NONE. Legacy OFF with an
    active Gate is *not* losslessly representable under the current contract and
    therefore requires an explicit content decision instead of silent coercion.
    """
    if "aggregationRole" in binding:
        role = str(binding["aggregationRole"])
    elif "conditionRole" in binding:
        role = str(binding["conditionRole"])
    else:
        raise BakeConfigError("missing AggregationRole")
    gate_policy = str(binding.get("gatePolicy", "NONE"))

    if role == "OFF":
        if gate_policy != "NONE":
            raise BakeConfigError(
                "legacy OFF + non-NONE GatePolicy requires explicit content migration"
            )
        role = "EXCLUDED"

    _validate_role_gate(role, gate_policy)
    return {"aggregationRole": role, "gatePolicy": gate_policy}


def migrate_legacy_bindings(bindings: Mapping[str, Mapping[str, Any]]) -> Mapping[str, Mapping[str, str]]:
    return {key: migrate_legacy_binding(value) for key, value in bindings.items()}


def _validate_role_gate(role: str, gate_policy: str) -> None:
    if role not in AGGREGATION_ROLES:
        raise BakeConfigError(f"invalid AggregationRole: {role}")
    if gate_policy not in GATE_FAILURE_CAPS:
        raise BakeConfigError(f"invalid GatePolicy: {gate_policy}")
    if role != "CORE" and gate_policy != "NONE":
        raise BakeConfigError("GatePolicy must be NONE/absent unless AggregationRole=CORE")


def _clamp_computed_soft_fit(value: float) -> float:
    if not math.isfinite(value):
        raise BakeConfigError("computed factor fit is not finite")
    return min(SOFT_FACTOR_MAX, max(SOFT_FACTOR_MIN, value))


def _authored_affinity(value: Any, label: str) -> float:
    result = float(value)
    if not math.isfinite(result) or not (SOFT_FACTOR_MIN <= result <= SOFT_FACTOR_MAX):
        raise BakeConfigError(
            f"{label} authored affinity must be within [{SOFT_FACTOR_MIN}, {SOFT_FACTOR_MAX}]"
        )
    return result


def _temperature_params(profile: Mapping[str, Any]) -> tuple[float, float, float, float, str]:
    accept_min = float(profile["acceptMin"])
    preferred_min = float(profile["preferredMin"])
    preferred_max = float(profile["preferredMax"])
    accept_max = float(profile["acceptMax"])
    shape = str(profile.get("falloffShape", "LINEAR")).upper()
    if not all(math.isfinite(x) for x in (accept_min, preferred_min, preferred_max, accept_max)):
        raise BakeConfigError("temperature boundaries must be finite")
    if not (accept_min <= preferred_min <= preferred_max <= accept_max):
        raise BakeConfigError("invalid temperature boundaries")
    if shape not in {"LINEAR", "SMOOTHSTEP"}:
        raise BakeConfigError(f"unsupported temperature falloffShape: {shape}")
    return accept_min, preferred_min, preferred_max, accept_max, shape


def _falloff_value(x: float, shape: str) -> float:
    x = min(1.0, max(0.0, x))
    if shape == "LINEAR":
        return x
    return x * x * (3.0 - 2.0 * x)


def _point_temperature_fit(t: float, profile: Mapping[str, Any]) -> float:
    accept_min, preferred_min, preferred_max, accept_max, shape = _temperature_params(profile)
    if t <= accept_min or t >= accept_max:
        return 0.0
    if preferred_min <= t <= preferred_max:
        return 1.0
    if t < preferred_min:
        width = preferred_min - accept_min
        x = 1.0 if width == 0 else (t - accept_min) / width
    else:
        width = accept_max - preferred_max
        x = 1.0 if width == 0 else (accept_max - t) / width
    return _falloff_value(x, shape)


def _representative_temperature(temp_range: Sequence[Any]) -> tuple[float, float, float]:
    if not isinstance(temp_range, (list, tuple)) or len(temp_range) != 2:
        raise BakeConfigError("TEMPERATURE requires waterTemperatureRange [min,max]")
    t_min, t_max = float(temp_range[0]), float(temp_range[1])
    if not math.isfinite(t_min) or not math.isfinite(t_max):
        raise BakeConfigError("temperature range must be finite")
    if t_min > t_max:
        raise BakeConfigError("temperature range min > max")
    return t_min, t_max, (t_min + t_max) / 2.0


def _require_quality_ref(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise BakeConfigError(f"{label} fishQualityRef must be a mapping")
    if not value.get("fishQualityId"):
        raise BakeConfigError(f"{label} fishQualityRef missing fishQualityId")
    return value


class FixedBakeTemplateProgram:
    """System-owned fixed topology for the 0.3.4.0-B vertical slice."""

    condition_slots = ("TEMPERATURE", "STRUCTURE", "FEEDING_LAYER", "TIME_PERIOD")
    gate_capable = frozenset({"TEMPERATURE"})

    def evaluate(
        self,
        resolved_subject: Mapping[str, Any],
        resolved_seed: Mapping[str, Any],
        condition_group: ConditionGroup,
    ) -> BakeEvaluationResult:
        if any(key in resolved_subject for key in ("fishPondRef", "baseOpportunityIntensity", "backgroundPolicy")):
            raise BakeConfigError("ResolvedSpatialOpportunitySubject must not contain Pond-owned opportunity truth")
        if any(key in resolved_seed for key in ("resolvedComponentProfiles", "resolvedSpatialOpportunityBindings")):
            raise BakeConfigError("ResolvedOpportunitySeed must not contain fish-side profile/binding truth")

        subject_quality = _require_quality_ref(resolved_subject.get("fishQualityRef"), "subject")
        seed_quality = _require_quality_ref(resolved_seed.get("fishQualityRef"), "seed")
        if dict(subject_quality) != dict(seed_quality):
            raise BakeConfigError("subject/seed fishQualityRef mismatch")
        if not resolved_seed.get("fishPondRef"):
            raise BakeConfigError("ResolvedOpportunitySeed missing fishPondRef")

        base = float(resolved_seed["baseOpportunityIntensity"])
        if not math.isfinite(base) or base < 0:
            raise BakeConfigError("invalid BaseOpportunityIntensity")

        bindings = resolved_subject.get("resolvedSpatialOpportunityBindings", {})
        components = resolved_subject.get("resolvedComponentProfiles", {})
        unknown_conditions = set(bindings) - set(self.condition_slots)
        if unknown_conditions:
            raise BakeConfigError(f"unknown fixed-template condition(s): {sorted(unknown_conditions)}")

        gate_results = []
        factor_results = []
        failed_caps = []
        core_loss = 0.0
        secondary_loss_unscaled = 0.0

        for condition_key in self.condition_slots:
            if condition_key not in bindings:
                raise BakeConfigError(f"missing AggregationRole/GatePolicy: {condition_key}")
            binding = bindings[condition_key]
            if "conditionRole" in binding:
                raise BakeConfigError("legacy ConditionRole must be migrated before B-current evaluation")
            role = str(binding.get("aggregationRole", ""))
            gate_policy = str(binding.get("gatePolicy", "NONE"))
            _validate_role_gate(role, gate_policy)
            if gate_policy != "NONE" and condition_key not in self.gate_capable:
                raise BakeConfigError(f"GatePolicy unsupported for {condition_key}")

            if role == "EXCLUDED":
                continue

            raw_fit: float
            raw_inputs: Mapping[str, Any]
            is_computed_continuous_fit = False
            gate_passed = True

            if condition_key == "TEMPERATURE":
                profile = components.get("temperature")
                if profile is None:
                    raise BakeConfigError("active TEMPERATURE missing profile")
                t_min, t_max, representative = _representative_temperature(
                    condition_group.water_temperature_range
                )
                raw_fit = _point_temperature_fit(representative, profile)
                raw_inputs = {
                    "waterTemperatureRange": [t_min, t_max],
                    "representativeTemp": representative,
                }
                is_computed_continuous_fit = True
                if gate_policy != "NONE":
                    threshold = float(profile["tempThreshold"])
                    if not math.isfinite(threshold) or not (0.0 <= threshold <= 1.0):
                        raise BakeConfigError("tempThreshold must be within [0,1]")
                    gate_passed = raw_fit >= threshold

            elif condition_key == "STRUCTURE":
                profile = components.get("structure", {}).get("affinity", {})
                structure_type = condition_group.structure_type
                if not profile or structure_type not in profile:
                    raise BakeConfigError(f"STRUCTURE missing affinity for {structure_type}")
                raw_fit = _authored_affinity(profile[structure_type], f"STRUCTURE/{structure_type}")
                raw_inputs = {"structureType": structure_type}

            elif condition_key == "FEEDING_LAYER":
                profile = components.get("feedingLayer", {}).get("affinity", {})
                layers = tuple(condition_group.feeding_ecology_layers)
                if not layers:
                    raise BakeConfigError("FEEDING_LAYER requires at least one FeedingEcologyLayer")
                missing = [layer for layer in layers if layer not in profile]
                if not profile or missing:
                    raise BakeConfigError(f"FEEDING_LAYER missing affinity for {missing or layers}")
                layer_fits = {
                    layer: _authored_affinity(profile[layer], f"FEEDING_LAYER/{layer}")
                    for layer in layers
                }
                raw_fit = max(layer_fits.values())
                raw_inputs = {
                    "feedingEcologyLayers": list(layers),
                    "layerFits": layer_fits,
                }

            elif condition_key == "TIME_PERIOD":
                profile = components.get("timePeriod", {}).get("affinity", {})
                period = condition_group.time_period
                if not profile or period not in profile:
                    raise BakeConfigError(f"TIME_PERIOD missing affinity for {period}")
                raw_fit = _authored_affinity(profile[period], f"TIME_PERIOD/{period}")
                raw_inputs = {"timePeriod": period}

            else:  # pragma: no cover
                raise BakeConfigError(f"unknown condition slot: {condition_key}")

            applied_fit = _clamp_computed_soft_fit(raw_fit) if is_computed_continuous_fit else raw_fit
            loss = -math.log(applied_fit)
            factor_results.append(
                {
                    "conditionKey": condition_key,
                    "aggregationRole": role,
                    "rawInputs": dict(raw_inputs),
                    "rawFit": raw_fit,
                    "appliedFit": applied_fit,
                    "loss": loss,
                }
            )
            if role == "CORE":
                core_loss += loss
            elif role == "SECONDARY":
                secondary_loss_unscaled += loss

            if gate_policy != "NONE":
                cap = GATE_FAILURE_CAPS[gate_policy]
                gate_results.append(
                    {
                        "conditionKey": condition_key,
                        "policy": gate_policy,
                        "passed": gate_passed,
                        "failureCap": cap,
                    }
                )
                if not gate_passed:
                    failed_caps.append(float(cap))

        secondary_loss_raw = SECONDARY_LOSS_SCALE * secondary_loss_unscaled
        secondary_loss_applied = min(secondary_loss_raw, SECONDARY_LOSS_BUDGET)
        raw_env_coeff = math.exp(-(core_loss + secondary_loss_applied))

        gate_failure_cap = min(failed_caps) if failed_caps else None
        background_policy = resolved_seed.get("backgroundPolicy", {"enabled": False})
        background_enabled = bool(background_policy.get("enabled", False))
        if not background_enabled and "envCoeffMin" in background_policy:
            raise BakeConfigError("envCoeffMin requires backgroundPolicy.enabled=true")

        floor_applied = False
        if gate_failure_cap is not None:
            final_env_coeff = min(raw_env_coeff, gate_failure_cap)
        elif background_enabled:
            floor = float(background_policy["envCoeffMin"])
            if not math.isfinite(floor) or not (0.0 < floor <= 0.30):
                raise BakeConfigError("invalid envCoeffMin")
            final_env_coeff = max(raw_env_coeff, floor)
            floor_applied = final_env_coeff > raw_env_coeff
        else:
            final_env_coeff = raw_env_coeff

        intensity = base * final_env_coeff
        trace = {
            "programId": FIXED_BAKE_TEMPLATE_PROGRAM_ID,
            "algorithmContractVersion": BAKE_ALGORITHM_CONTRACT_VERSION,
            "fishQualityRef": dict(subject_quality),
            "fishPondRef": resolved_seed["fishPondRef"],
            "conditionGroupId": condition_group.condition_group_id,
            "baseOpportunityIntensity": base,
            "gateResults": tuple(gate_results),
            "factorResults": tuple(factor_results),
            "coreLoss": core_loss,
            "secondaryLossRaw": secondary_loss_raw,
            "secondaryLossApplied": secondary_loss_applied,
            "rawEnvCoeff": raw_env_coeff,
            "gateFailureCap": gate_failure_cap,
            "backgroundFloorApplied": floor_applied,
            "finalEnvCoeff": final_env_coeff,
            "spatialOpportunityIntensity": intensity,
        }
        return BakeEvaluationResult(final_env_coeff, intensity, trace)
