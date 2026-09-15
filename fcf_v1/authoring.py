"""Constrained current-contract Authoring Data -> compiled pre-generation bundle."""
from dataclasses import dataclass
import re
from typing import Any, List, Mapping, Optional, Tuple
from .pre_generation import CandidateContribution

ALLOWED_BANDS = {"NONE", "LOW", "NORMAL", "HIGH"}
ALLOWED_RESPONSE_INTENTS = {"SET_RESPONSE_BAND", "CAP_RESPONSE_BAND"}
ALLOWED_OVERLAP = {"ALLOW_PARALLEL", "REQUIRE_DISJOINT_ELIGIBILITY"}
ALLOWED_PARAM_OWNERS = {
    "SPECIES_SHARED", "ENGAGEMENT_MODE", "FISH_QUALITY",
    "SHARED_PROFILE", "ENVIRONMENT_FACT", "PROGRAM_CONST",
}
ALLOWED_PARAM_TYPES = {"float", "int", "string", "bool"}
PARAM_SCHEMA_CONTROL_FLOW_KEYS = {"step_order", "next", "branch", "jump"}
SURFACES = ("bake", "response", "quality_selection")


@dataclass(frozen=True)
class CompiledContentBundle:
    species_slow_facts: Mapping[str, Any]
    engagement_mode_routing_snapshot: Mapping[str, Any]
    surface_program_bundle: Mapping[str, Any]
    resolved_bake_subjects: Mapping[str, Any]
    contributions: Tuple[CandidateContribution, ...]


class AuthoringError(ValueError):
    pass


def _ids(items):
    return [x.get("id") for x in items]


def _by_id(items, item_id):
    return next((x for x in items if x.get("id") == item_id), None)


def _dedupe(items):
    return list(dict.fromkeys(items))


def _typed(value: Any, type_name: str) -> bool:
    if type_name == "float":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if type_name == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    if type_name == "string":
        return isinstance(value, str)
    if type_name == "bool":
        return isinstance(value, bool)
    return False


def _value_error(key: str, value: Any, definition: Mapping[str, Any]) -> Optional[str]:
    type_name = definition.get("type")
    if type_name not in ALLOWED_PARAM_TYPES:
        return f"invalid component type: {key}/{type_name}"
    if not _typed(value, type_name):
        return f"invalid typed value: {key} expected {type_name}"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "min" in definition and value < definition["min"]:
            return f"value below min: {key}"
        if "max" in definition and value > definition["max"]:
            return f"value above max: {key}"
    return None


def _validate_expr(expr: str, lineno: int) -> None:
    if "???" in expr or not expr.strip():
        raise AuthoringError(f"Bake DSL line {lineno}: invalid expression")
    if not re.fullmatch(r"[A-Za-z0-9_ .,+\-*/<>=!()\[\]]+", expr):
        raise AuthoringError(f"Bake DSL line {lineno}: unsupported expression token")


def compile_bake_dsl(source: str) -> Mapping[str, Any]:
    """Validate the approved prototype vocabulary and derive a read-only Structure Lens."""
    if not isinstance(source, str) or not source.strip():
        raise AuthoringError("Bake DSL line 1: empty source")
    depth = 0
    saw_top_return = False
    lens = []
    for lineno, raw in enumerate(source.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue
        if line == "}":
            depth -= 1
            if depth < 0:
                raise AuthoringError(f"Bake DSL line {lineno}: unmatched closing brace")
            continue
        m = re.fullmatch(r"rule\s+([A-Za-z_][A-Za-z0-9_]*)\s*\{", line)
        if m:
            lens.append({"line": lineno, "kind": "RULE", "name": m.group(1)})
            depth += 1
            continue
        m = re.fullmatch(r"if\s+(.+):\s*return\s+(.+)", line)
        if m:
            _validate_expr(m.group(1), lineno)
            _validate_expr(m.group(2), lineno)
            lens.append({"line": lineno, "kind": "GATE"})
            lens.append({"line": lineno, "kind": "EARLY_RETURN"})
            continue
        m = re.fullmatch(r"if\s+(.+)\s*\{", line)
        if m:
            _validate_expr(m.group(1), lineno)
            lens.append({"line": lineno, "kind": "GATE"})
            depth += 1
            continue
        m = re.fullmatch(r"let\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)", line)
        if m:
            _validate_expr(m.group(2), lineno)
            lens.append({"line": lineno, "kind": "ASSIGN", "name": m.group(1)})
            continue
        m = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)", line)
        if m:
            _validate_expr(m.group(2), lineno)
            lens.append({"line": lineno, "kind": "ASSIGN", "name": m.group(1)})
            continue
        m = re.fullmatch(r"return\s+(.+)", line)
        if m:
            _validate_expr(m.group(1), lineno)
            kind = "EARLY_RETURN" if depth > 0 else "RETURN"
            lens.append({"line": lineno, "kind": kind})
            if depth == 0:
                saw_top_return = True
            continue
        raise AuthoringError(f"Bake DSL line {lineno}: unsupported statement")
    if depth != 0:
        raise AuthoringError("Bake DSL: unclosed brace")
    if not saw_top_return:
        raise AuthoringError("Bake DSL: missing final return")
    return {"structure_lens": tuple(lens)}


def _resolve_profile_param(doc, species, mode, key):
    profiles = {p.get("id"): p for p in doc.get("shared_profiles", [])}
    refs = list(mode.get("shared_profile_refs", [])) + list(species.get("shared_profile_refs", []))
    for ref in refs:
        profile = profiles.get(ref)
        if profile and key in profile.get("params", {}):
            return profile["params"][key], ref
    return None, None


def resolve_bake_subject(
    doc: Mapping[str, Any],
    quality_ref: str,
    mode_ref: str,
    environment_facts: Optional[Mapping[str, Any]] = None,
) -> Mapping[str, Any]:
    """Resolve one Species x FishQuality x EngagementMode subject with provenance."""
    species = doc.get("species", {})
    mode = _by_id(species.get("engagement_modes", []), mode_ref)
    quality = _by_id(doc.get("fish_qualities", []), quality_ref)
    if mode is None:
        raise AuthoringError(f"missing EngagementMode: {mode_ref}")
    if quality is None:
        raise AuthoringError(f"missing FishQuality: {quality_ref}")
    program = _by_id(doc.get("surface_programs", {}).get("bake", []), mode.get("bake_program_ref"))
    if program is None:
        raise AuthoringError(f"missing Bake Program: {mode.get('bake_program_ref')}")

    compiled_logic = compile_bake_dsl(program.get("dsl", ""))
    schema = program.get("required_params", [])
    schema_keys = {p.get("key") for p in schema}
    mode_params = mode.get("bake_params", {})
    orphaned = tuple(
        {"key": key, "status": "ORPHANED", "source": "ENGAGEMENT_MODE", "value": value}
        for key, value in sorted(mode_params.items())
        if key not in schema_keys
    )

    resolved = {}
    for spec in schema:
        key = spec.get("key")
        owners = spec.get("owner_policy", [])
        found = False
        entry = {
            "key": key,
            "type": spec.get("type"),
            "required": bool(spec.get("required", True)),
        }
        for owner in owners:
            if owner == "ENGAGEMENT_MODE" and key in mode_params:
                entry.update(status="OVERRIDE", source=owner, value=mode_params[key])
                found = True
                break
            if owner == "FISH_QUALITY" and key in quality.get("narrow_param_overrides", {}):
                entry.update(status="OVERRIDE", source=owner, value=quality["narrow_param_overrides"][key])
                found = True
                break
            if owner == "SPECIES_SHARED" and key in species.get("shared_params", {}):
                entry.update(status="INHERITED", source=owner, value=species["shared_params"][key])
                found = True
                break
            if owner == "SHARED_PROFILE":
                value, profile_ref = _resolve_profile_param(doc, species, mode, key)
                if profile_ref is not None:
                    entry.update(status="INHERITED", source=owner, source_ref=profile_ref, value=value)
                    found = True
                    break
            if owner == "ENVIRONMENT_FACT":
                if environment_facts is None:
                    entry.update(status="RUNTIME_FACT_REQUIRED", source=owner, value=None)
                    found = True
                    break
                if key in environment_facts:
                    entry.update(status="FACT", source=owner, value=environment_facts[key])
                    found = True
                    break
            if owner == "PROGRAM_CONST" and "const_value" in spec:
                entry.update(status="PROGRAM", source=owner, value=spec["const_value"])
                found = True
                break
        if not found:
            entry.update(status="MISSING" if entry["required"] else "OPTIONAL_UNSET", source=None, value=None)
        resolved[key] = entry

    return {
        "identity": {
            "species": species.get("species_id"),
            "fish_quality": quality_ref,
            "engagement_mode": mode_ref,
        },
        "program_ref": program["id"],
        "params": resolved,
        "orphaned": orphaned,
        "program_logic": {
            "source": "PROGRAM_OWNED_LOGIC",
            "program_ref": program["id"],
            "dsl": program.get("dsl", ""),
            "structure_lens": compiled_logic["structure_lens"],
        },
    }


def lint_authoring(doc: Mapping[str, Any]) -> List[str]:
    errors = []
    required = {
        "schema_version", "species", "fish_qualities", "engagement_mode_routing",
        "spatial_opportunities", "surface_programs", "component_definitions", "shared_profiles",
    }
    allowed = required | {"meanings", "templates", "template_ref"}
    errors += [f"unknown field: {k}" for k in doc if k not in allowed]
    errors += [f"missing field: {k}" for k in required if k not in doc]

    templates = doc.get("templates", {})
    for t in templates.values():
        if isinstance(t, Mapping) and ("template_ref" in t or "extends" in t):
            errors.append("deep or runtime template inheritance is forbidden")

    component_defs = doc.get("component_definitions", {})
    for key, definition in component_defs.items():
        if definition.get("type") not in ALLOWED_PARAM_TYPES:
            errors.append(f"invalid component type: {key}/{definition.get('type')}")
        owners = definition.get("allowed_owners", [])
        if not owners or any(o not in ALLOWED_PARAM_OWNERS for o in owners):
            errors.append(f"invalid ComponentDefinition owner policy: {key}")

    species = doc.get("species", {})
    if not species.get("species_id"):
        errors.append("missing species_id")

    modes = species.get("engagement_modes", [])
    mode_ids = _ids(modes)
    if not mode_ids:
        errors.append("missing engagement_modes")
    if len(mode_ids) != len(set(mode_ids)):
        errors.append("duplicate EngagementMode id")

    default_mode = species.get("default_engagement_mode_ref")
    if default_mode not in set(mode_ids):
        errors.append("DefaultEngagementModeRef must reference one EngagementMode")

    routing_ref = species.get("engagement_mode_routing_program_ref")
    if not routing_ref:
        errors.append("missing EngagementModeRoutingProgramRef")

    profiles = doc.get("shared_profiles", [])
    profile_ids = _ids(profiles)
    if len(profile_ids) != len(set(profile_ids)):
        errors.append("duplicate SharedProfile id")

    def validate_param_map(param_map, owner, label):
        for key, value in param_map.items():
            definition = component_defs.get(key)
            if definition is None:
                errors.append(f"unknown ComponentDefinition: {label}/{key}")
                continue
            if owner not in definition.get("allowed_owners", []):
                errors.append(f"illegal param owner: {label}/{key}/{owner}")
            err = _value_error(key, value, definition)
            if err:
                errors.append(f"{label}: {err}")

    validate_param_map(species.get("shared_params", {}), "SPECIES_SHARED", "Species Shared")
    for ref in species.get("shared_profile_refs", []):
        if ref not in set(profile_ids):
            errors.append(f"Species references missing SharedProfile: {ref}")
    for profile in profiles:
        validate_param_map(profile.get("params", {}), "SHARED_PROFILE", f"SharedProfile {profile.get('id')}")

    qualities = doc.get("fish_qualities", [])
    quality_ids = _ids(qualities)
    if not quality_ids:
        errors.append("missing FishQuality")
    if len(quality_ids) != len(set(quality_ids)):
        errors.append("duplicate FishQuality id")
    for q in qualities:
        try:
            if float(q.get("base_weight", -1)) < 0:
                errors.append(f"invalid FishQualityBaseWeight: {q.get('id')}")
        except (TypeError, ValueError):
            errors.append(f"invalid FishQualityBaseWeight: {q.get('id')}")
        if any(k in q for k in ("bake_program_ref", "response_program_ref", "quality_selection_program_ref", "program_ref")):
            errors.append(f"FishQuality cannot bind Surface Program: {q.get('id')}")
        validate_param_map(q.get("narrow_param_overrides", {}), "FISH_QUALITY", f"FishQuality {q.get('id')}")

    surface_programs = doc.get("surface_programs", {})
    program_ids = {}
    for surface in SURFACES:
        programs = surface_programs.get(surface, [])
        ids = _ids(programs)
        program_ids[surface] = set(ids)
        if len(ids) != len(set(ids)):
            errors.append(f"duplicate {surface} Program id")

    for p in surface_programs.get("bake", []):
        try:
            compile_bake_dsl(p.get("dsl", ""))
        except AuthoringError as exc:
            errors.append(f"{p.get('id')}: {exc}")
        schema = p.get("required_params", [])
        keys = [x.get("key") for x in schema]
        if len(keys) != len(set(keys)):
            errors.append(f"duplicate RequiredParamSchema key in {p.get('id')}")
        for spec in schema:
            key = spec.get("key")
            if any(k in spec for k in PARAM_SCHEMA_CONTROL_FLOW_KEYS):
                errors.append(f"RequiredParamSchema control flow forbidden: {p.get('id')}/{key}")
            if key not in component_defs:
                errors.append(f"RequiredParamSchema missing ComponentDefinition: {p.get('id')}/{key}")
            type_name = spec.get("type")
            if type_name not in ALLOWED_PARAM_TYPES:
                errors.append(f"invalid RequiredParamSchema type: {p.get('id')}/{key}")
            elif key in component_defs and component_defs[key].get("type") != type_name:
                errors.append(f"RequiredParamSchema type mismatch: {p.get('id')}/{key}")
            owners = spec.get("owner_policy", [])
            if not owners or any(o not in ALLOWED_PARAM_OWNERS for o in owners):
                errors.append(f"invalid Owner Policy: {p.get('id')}/{key}")
            if key in component_defs and any(o not in component_defs[key].get("allowed_owners", []) for o in owners):
                errors.append(f"Owner Policy exceeds ComponentDefinition: {p.get('id')}/{key}")
            if "PROGRAM_CONST" in owners and "const_value" in spec:
                err = _value_error(key, spec["const_value"], component_defs.get(key, {"type": type_name}))
                if err:
                    errors.append(f"{p.get('id')}: {err}")

    for m in modes:
        refs = {
            "bake": m.get("bake_program_ref"),
            "response": m.get("response_program_ref"),
            "quality_selection": m.get("quality_selection_program_ref"),
        }
        for surface, ref in refs.items():
            if ref not in program_ids.get(surface, set()):
                errors.append(f"EngagementMode {m.get('id')} references missing {surface} Program: {ref}")
        for ref in m.get("shared_profile_refs", []):
            if ref not in set(profile_ids):
                errors.append(f"EngagementMode {m.get('id')} references missing SharedProfile: {ref}")
        validate_param_map(m.get("bake_params", {}), "ENGAGEMENT_MODE", f"EngagementMode {m.get('id')}")

    for p in surface_programs.get("response", []):
        rules = p.get("rules", [])
        ids = _ids(rules)
        if len(ids) != len(set(ids)):
            errors.append(f"duplicate response rule ID in {p.get('id')}")
        for r in rules:
            if r.get("intent") not in ALLOWED_RESPONSE_INTENTS:
                errors.append(f"invalid Response intent: {r.get('intent')}")
            if r.get("band") not in ALLOWED_BANDS:
                errors.append(f"invalid ResponseBand: {r.get('band')}")

    routing = doc.get("engagement_mode_routing", {})
    if routing.get("program_ref") != routing_ref:
        errors.append("Routing program_ref must match Species EngagementModeRoutingProgramRef")

    allocations = routing.get("allocations", [])
    seen = set()
    totals = {q: 0.0 for q in quality_ids}
    for a in allocations:
        q, m = a.get("quality_ref"), a.get("mode_ref")
        key = (q, m)
        if key in seen:
            errors.append(f"duplicate ModeAllocation: {q}/{m}")
        seen.add(key)
        if q not in set(quality_ids):
            errors.append(f"ModeAllocation references missing FishQuality: {q}")
        if m not in set(mode_ids):
            errors.append(f"ModeAllocation references missing EngagementMode: {m}")
        if m == default_mode:
            errors.append("Default Mode share is derived remainder, not authored allocation")
        try:
            share = float(a.get("share"))
        except (TypeError, ValueError):
            errors.append(f"invalid EngagementModeShare: {q}/{m}")
            continue
        if not 0 <= share <= 1:
            errors.append(f"invalid EngagementModeShare: {q}/{m}")
        if q in totals:
            totals[q] += share

    for q, total in totals.items():
        if total > 1 + 1e-9:
            errors.append(f"OVERALLOCATED: {q} SpecialShareTotal={total}")

    overlap = routing.get("overlap_contract", "ALLOW_PARALLEL")
    if overlap not in ALLOWED_OVERLAP:
        errors.append(f"invalid AllocationOverlapContract: {overlap}")

    for s in doc.get("spatial_opportunities", []):
        m = s.get("mode_ref")
        if m not in set(mode_ids):
            errors.append(f"SpatialOpportunity references missing EngagementMode: {m}")
        try:
            if float(s.get("spatial_weight", -1)) < 0:
                errors.append(f"invalid SpatialOpportunity weight: {s.get('support_ref')}")
        except (TypeError, ValueError):
            errors.append(f"invalid SpatialOpportunity weight: {s.get('support_ref')}")

    # Authoring completeness resolves per Species x FishQuality x EngagementMode.
    valid_bake_refs = program_ids.get("bake", set())
    for m in modes:
        if m.get("bake_program_ref") not in valid_bake_refs:
            continue
        for q in qualities:
            try:
                resolved = resolve_bake_subject(doc, q.get("id"), m.get("id"), environment_facts=None)
            except AuthoringError as exc:
                errors.append(str(exc))
                continue
            for entry in resolved["params"].values():
                if entry["status"] == "MISSING" and entry["required"]:
                    errors.append(f"MISSING_PARAM: {m.get('id')}/{q.get('id')}/{entry['key']}")
            for orphan in resolved["orphaned"]:
                errors.append(f"ORPHANED_PARAM: {m.get('id')}/{orphan['key']}")

    return _dedupe(errors)


def compile_authoring(doc: Mapping[str, Any]) -> CompiledContentBundle:
    errors = lint_authoring(doc)
    if errors:
        raise AuthoringError("; ".join(errors))

    species = doc["species"]
    default_mode = species["default_engagement_mode_ref"]
    qualities = {q["id"]: q for q in doc["fish_qualities"]}
    mode_ids = {m["id"] for m in species["engagement_modes"]}

    explicit = {(q, m): 0.0 for q in qualities for m in mode_ids if m != default_mode}
    for a in doc["engagement_mode_routing"]["allocations"]:
        explicit[(a["quality_ref"], a["mode_ref"])] = float(a["share"])

    shares = {}
    for q in qualities:
        special_total = sum(share for (quality, _), share in explicit.items() if quality == q)
        shares[(q, default_mode)] = 1.0 - special_total
        for m in mode_ids:
            if m != default_mode:
                shares[(q, m)] = explicit[(q, m)]

    spatial_by_mode = {}
    for s in doc["spatial_opportunities"]:
        spatial_by_mode.setdefault(s["mode_ref"], []).append(s)

    contributions = []
    for qid, q in qualities.items():
        base = float(q["base_weight"])
        for mode in mode_ids:
            share = shares[(qid, mode)]
            if share <= 0 or base <= 0:
                continue
            for s in spatial_by_mode.get(mode, ()):
                weight = base * share * float(s["spatial_weight"])
                if weight > 0:
                    contributions.append(CandidateContribution(species["species_id"], qid, mode, s["support_ref"], weight))

    surface_bundle = {}
    for surface in SURFACES:
        programs = []
        for p in doc["surface_programs"].get(surface, []):
            cp = dict(p)
            if surface == "response":
                cp["rules"] = tuple(sorted(p.get("rules", []), key=lambda r: r["id"]))
            if surface == "bake":
                cp["structure_lens"] = compile_bake_dsl(p.get("dsl", ""))["structure_lens"]
            programs.append(cp)
        surface_bundle[surface] = tuple(programs)

    routing_snapshot = {
        "program_ref": doc["engagement_mode_routing"]["program_ref"],
        "default_mode_ref": default_mode,
        "overlap_contract": doc["engagement_mode_routing"].get("overlap_contract", "ALLOW_PARALLEL"),
        "shares": tuple(sorted((
            {"quality_ref": q, "mode_ref": m, "share": share}
            for (q, m), share in shares.items()
        ), key=lambda x: (x["quality_ref"], x["mode_ref"]))),
    }

    resolved_subjects = {}
    for m in species["engagement_modes"]:
        for q in doc["fish_qualities"]:
            key = f"{q['id']}::{m['id']}"
            resolved_subjects[key] = resolve_bake_subject(doc, q["id"], m["id"], environment_facts=None)

    return CompiledContentBundle(
        species.get("slow_facts", {}),
        routing_snapshot,
        surface_bundle,
        resolved_subjects,
        tuple(contributions),
    )
