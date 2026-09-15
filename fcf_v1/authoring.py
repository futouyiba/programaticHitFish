"""Constrained current-contract Authoring Data -> compiled pre-generation bundle."""
from dataclasses import dataclass
from typing import Any, List, Mapping, Tuple
from .pre_generation import CandidateContribution

ALLOWED_BANDS = {"NONE", "LOW", "NORMAL", "HIGH"}
ALLOWED_RESPONSE_INTENTS = {"SET_RESPONSE_BAND", "CAP_RESPONSE_BAND"}
ALLOWED_OVERLAP = {"ALLOW_PARALLEL", "REQUIRE_DISJOINT_ELIGIBILITY"}
SURFACES = ("bake", "response", "quality_selection")


@dataclass(frozen=True)
class CompiledContentBundle:
    species_slow_facts: Mapping[str, Any]
    engagement_mode_routing_snapshot: Mapping[str, Any]
    surface_program_bundle: Mapping[str, Any]
    contributions: Tuple[CandidateContribution, ...]


class AuthoringError(ValueError):
    pass


def _ids(items):
    return [x.get("id") for x in items]


def lint_authoring(doc: Mapping[str, Any]) -> List[str]:
    errors = []
    required = {"schema_version", "species", "fish_qualities", "engagement_mode_routing", "spatial_opportunities", "surface_programs"}
    allowed = required | {"meanings", "templates", "template_ref"}
    errors += [f"unknown field: {k}" for k in doc if k not in allowed]
    errors += [f"missing field: {k}" for k in required if k not in doc]

    templates = doc.get("templates", {})
    for t in templates.values():
        if isinstance(t, Mapping) and ("template_ref" in t or "extends" in t):
            errors.append("deep or runtime template inheritance is forbidden")

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

    surface_programs = doc.get("surface_programs", {})
    program_ids = {}
    for surface in SURFACES:
        programs = surface_programs.get(surface, [])
        ids = _ids(programs)
        program_ids[surface] = set(ids)
        if len(ids) != len(set(ids)):
            errors.append(f"duplicate {surface} Program id")

    for m in modes:
        refs = {"bake": m.get("bake_program_ref"), "response": m.get("response_program_ref"), "quality_selection": m.get("quality_selection_program_ref")}
        for surface, ref in refs.items():
            if ref not in program_ids.get(surface, set()):
                errors.append(f"EngagementMode {m.get('id')} references missing {surface} Program: {ref}")

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

    return errors


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
            programs.append(cp)
        surface_bundle[surface] = tuple(programs)

    routing_snapshot = {
        "program_ref": doc["engagement_mode_routing"]["program_ref"],
        "default_mode_ref": default_mode,
        "overlap_contract": doc["engagement_mode_routing"].get("overlap_contract", "ALLOW_PARALLEL"),
        "shares": tuple(sorted(({"quality_ref": q, "mode_ref": m, "share": share} for (q, m), share in shares.items()), key=lambda x: (x["quality_ref"], x["mode_ref"]))),
    }

    return CompiledContentBundle(species.get("slow_facts", {}), routing_snapshot, surface_bundle, tuple(contributions))
