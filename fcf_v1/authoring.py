"""Constrained Authoring Data -> compiled pre-generation content bundle."""
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Tuple
from .pre_generation import CandidateContribution

ALLOWED_GRADES = {"NONE", "LOW", "NORMAL", "HIGH"}
ALLOWED_OPS = {"SET", "CEILING"}

@dataclass(frozen=True)
class CompiledContentBundle:
    species_slow_facts: Mapping[str, Any]
    response_content_bundle: Mapping[str, Any]
    contributions: Tuple[CandidateContribution, ...]
    materialization_profiles: Mapping[str, Any]

class AuthoringError(ValueError): pass

def lint_authoring(doc: Mapping[str, Any]) -> List[str]:
    errors=[]
    required={"schema_version","species","lifecycles","spatial_opportunities","pathways","response_slices","materialization_profiles","rules"}
    allowed = required | {"meanings", "templates", "template_ref"}
    errors += [f"unknown field: {k}" for k in doc if k not in allowed]
    errors += [f"missing field: {k}" for k in required if k not in doc]
    species=doc.get("species",{})
    templates=doc.get("templates", {})
    for tid, t in templates.items():
        if isinstance(t, Mapping) and ("template_ref" in t or "extends" in t): errors.append("deep or runtime template inheritance is forbidden")
    rules=doc.get("rules",[])
    rule_ids=[r.get("id") for r in rules]
    if len(rule_ids)!=len(set(rule_ids)): errors.append("duplicate semantic rule ID")
    if rules and not any(r.get("fallback") for r in rules): errors.append("missing required fallback")
    # A missing condition is a wildcard. Same-priority wildcards or equal
    # condition sets are provably overlapping; ordering must never break ties.
    for i, a in enumerate(rules):
        for b in rules[i+1:]:
            if a.get("priority") == b.get("priority") and (not a.get("conditions") or not b.get("conditions") or a.get("conditions")==b.get("conditions")):
                errors.append(f"same-priority overlapping rules: {a.get('id')}, {b.get('id')}")
    if not species.get("species_id"): errors.append("missing species_id")
    lifecycles=doc.get("lifecycles",[])
    ids=[x.get("id") for x in lifecycles]
    if len(ids)!=len(set(ids)): errors.append("duplicate lifecycle id")
    if abs(sum(float(x.get("supply_share",0)) for x in lifecycles)-1)>1e-9: errors.append("Lifecycle share != 1")
    paths={x.get("id") for x in doc.get("pathways",[])}
    for mode in species.get("fish_modes",[]):
        for p in mode.get("pathways",[]):
            if p not in paths: errors.append(f"FishMode references missing pathway: {p}")
    for r in rules:
        if r.get("grade") not in ALLOWED_GRADES: errors.append(f"invalid ResponseGrade: {r.get('grade')}")
        if r.get("operation", "SET") not in ALLOWED_OPS: errors.append(f"illegal ResponseSlice operation: {r.get('operation')}")
    profiles=doc.get("materialization_profiles",[])
    pids={p.get("id") for p in profiles}
    for l in lifecycles:
        if l.get("materialization_profile") not in pids: errors.append("missing materialization profile")
        if l.get("mode")=="SPAWN_GUARD" and not any(p.get("id")==l.get("materialization_profile") and p.get("requires_anchor") for p in profiles): errors.append("Guard without anchor-compatible materialization profile")
    return errors

def compile_authoring(doc: Mapping[str, Any]) -> CompiledContentBundle:
    errors=lint_authoring(doc)
    if errors: raise AuthoringError("; ".join(errors))
    species=doc["species"]; slow=species.get("slow_facts",{})
    profiles={p["id"]:p for p in doc["materialization_profiles"]}
    contributions=[]
    for l in doc["lifecycles"]:
        profile=profiles[l["materialization_profile"]]
        for s in doc["spatial_opportunities"]:
            if s.get("cohort") != l["id"]: continue
            contributions.append(CandidateContribution(species["species_id"], l["id"], l["mode"], l.get("response_slice",""), profile.get("behavior_anchor_ref"), s["support_ref"], l["materialization_profile"], float(l["supply_share"])*float(s.get("engagement_mass",1))))
    # Canonical rule ordering makes file ordering semantically irrelevant.
    canonical_rules=tuple(sorted(doc["rules"], key=lambda r:(-int(r.get("priority",0)), r["id"])))
    return CompiledContentBundle(slow, {"pathways":doc["pathways"],"rules":canonical_rules,"meanings":doc.get("meanings",[]),"template_ref":doc.get("template_ref")}, tuple(contributions), profiles)
