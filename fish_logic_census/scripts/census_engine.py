"""Census engine: mechanical invariants for LogicTemplate merge discipline.

Implements the code-checkable core of Method R0 / Orchestrator Prompt R2 and
Golden Fixtures F01-F17. Semantic judgments (premise-vs-owned attribution,
evidence sufficiency) remain LLM/reviewer work — this module never decides
business meaning, only structural and bookkeeping invariants.

Program IR (dict):
  {
    "program_id": str,
    "surface": str,
    "incoming_premises": [str, ...],          # decided upstream, read-only here
    "ordered_steps": [{"op": str, "deps": [step_index_or_name, ...]}, ...],
    "branches": [{"kind": "IF|GATE", "guard": str, "else": str|None}, ...],
    "combine": str|None,
    "return_type": str,
    "instance_noise": {"species": str|None, "profile": str|None,
                       "constants": {str: any}},   # erased by deinstantiate()
    "helpers": [{"name": str, "body_has_control_flow": bool, "case_specific": bool}],
  }
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional, Set

# ---------------------------------------------------------------------------
# Structural diff (F01, F03, F04, F07, F11)
# ---------------------------------------------------------------------------

def structural_diff(a: Dict[str, Any], b: Dict[str, Any]) -> Set[str]:
    """Return the set of structural differences between two program bodies.

    Order comparison uses op SEQUENCES (positions matter); identical multisets
    in different order => ORDER diff even if mathematically commutable (F01).
    Feature/IO similarity is never consulted (F07).
    """
    diffs: Set[str] = set()
    ops_a = [s["op"] for s in a["ordered_steps"]]
    ops_b = [s["op"] for s in b["ordered_steps"]]
    if ops_a != ops_b:
        if sorted(ops_a) == sorted(ops_b):
            diffs.add("ORDER")            # same ops, different sequence (F01/F11)
        else:
            diffs.add("OPERATOR")
    deps_a = {frozenset(d) for d in _dep_sets(a)}
    deps_b = {frozenset(d) for d in _dep_sets(b)}
    if deps_a != deps_b:
        diffs.add("DEPENDENCY")           # covers F04 flattening: FeasibleSet->Rank edge lost
    if _branch_shape(a) != _branch_shape(b):
        diffs.add("BRANCH")               # F03: surface-owned CHECK/GATE difference
    if a.get("combine") != b.get("combine"):
        diffs.add("COMBINE")
    if a.get("return_type") != b.get("return_type"):
        diffs.add("RETURN")
    if [p for p in a["incoming_premises"]] != [p for p in b["incoming_premises"]]:
        diffs.add("PREMISE")              # informational; activation diffs stay premises (F02)
    return diffs


def _dep_sets(p: Dict[str, Any]) -> List[Set[str]]:
    return [set(s.get("deps", [])) for s in p["ordered_steps"]]


def _branch_shape(p: Dict[str, Any]) -> List[str]:
    return [f"{b['kind']}:{b['guard']}" for b in p.get("branches", [])]


# ---------------------------------------------------------------------------
# Merge verdict (F01, F03, F05, F14, F15)
# ---------------------------------------------------------------------------

ARBITRARY_FREEDOM = {"arbitrary policy", "arbitrary steps", "arbitrary expression",
                     "arbitrary next", "policy = arbitrary"}

def merge_verdict(program: Dict[str, Any], template: Dict[str, Any],
                  allowed_axes: Optional[List[str]] = None) -> Dict[str, Any]:
    """Four-state pairwise verdict. MERGE_CONFIDENT requires EMPTY structural
    diffs on the body (premise diffs are excluded per F02)."""
    body_diffs = structural_diff(program, template) - {"PREMISE"}
    axis_ok = all(axis in (allowed_axes or []) for axis in _axis_demand(program, template))
    record = {"program_id": program["program_id"], "same": not body_diffs,
              "structural_diffs": sorted(body_diffs),
              "axis_demand": sorted(_axis_demand(program, template))}
    if not body_diffs:
        record.update(verdict="MERGE_CONFIDENT",
                      param_only=not _axis_demand(program, template))
    elif not body_diffs - {"COMBINE"} and axis_ok and "OPERATOR" not in body_diffs:
        # only a bounded, typed axis is demanded
        record.update(verdict="TEMPLATE_EXTENSION_CANDIDATE",
                      param_only=True,
                      requires=("extension_complexity_cost",
                                "new_template_complexity_cost",
                                "recommended_shape"))   # F14: never a plain merge
    elif body_diffs <= {"AMBIGUOUS_PARTS"}:
        record.update(verdict="AMBIGUOUS_NEEDS_EXPANSION", param_only=False)
    else:
        record.update(verdict="NEW_TEMPLATE_CANDIDATE", param_only=False)
    return record


def _axis_demand(program: Dict[str, Any], template: Dict[str, Any]) -> Set[str]:
    """Bounded, named axes the program needs beyond the template body."""
    demand: Set[str] = set()
    for s in program["ordered_steps"]:
        op = s["op"]
        if "(" in op and op.split("(", 1)[0] + ".*" not in (
                t["op"] for t in template["ordered_steps"]):
            demand.add(op)
    return demand


# ---------------------------------------------------------------------------
# De-instantiation (F13): comparison view only, original immutable
# ---------------------------------------------------------------------------

def deinstantiate(program: Dict[str, Any]) -> Dict[str, Any]:
    """Erase instance noise; NEVER reorder/merge/abstract semantics."""
    view = deepcopy(program)
    view["instance_noise"] = {"species": None, "profile": None, "constants": {}}
    view["comparison_body"] = True
    view["original_program_body"] = {"hash": program.get("blind_hash"),
                                     "unchanged": True}
    return view


# ---------------------------------------------------------------------------
# Helper admission (F06): complexity laundering interceptor
# ---------------------------------------------------------------------------

def helper_admission(helper: Dict[str, Any]) -> Dict[str, Any]:
    fail_reasons: List[str] = []
    if helper.get("body_has_control_flow"):
        fail_reasons.append("Authoring-visible control flow inside helper")
    if helper.get("case_specific"):
        fail_reasons.append("Case-specific program hiding")
    return {"admitted": not fail_reasons, "reasons": fail_reasons,
            "verdict": "PASS" if not fail_reasons else "HELPER_ADMISSION_FAIL"}


# ---------------------------------------------------------------------------
# Candidate family integrity (F15): no chained similarity
# ---------------------------------------------------------------------------

def family_admit(family: Dict[str, Any], program: Dict[str, Any]) -> Dict[str, Any]:
    """Every member must be tested DIRECTLY against the canonical body."""
    direct = merge_verdict(program, family["canonical_program_body"],
                           family.get("allowed_parameter_axes", []))
    if direct["verdict"] in ("MERGE_CONFIDENT",):
        return {"admitted": True, "canonical_version": family["version"],
                "regression_recheck_required": False}
    # joining would require canonical change => extension/new + version bump (F15)
    return {"admitted": False, "direct_test": direct,
            "canonical_version_next": family["version"] + 1,
            "regression_recheck_required": True,
            "verdict": direct["verdict"]}


# ---------------------------------------------------------------------------
# Counting rules (F10, F11)
# ---------------------------------------------------------------------------

def census_count(instances: List[Dict[str, Any]], templates: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Program instances != templates; schema reuse != body identity."""
    return {"n_program_instances": len(instances),
            "n_logic_templates": len(templates),
            "note": "schema count is a Representation-side statistic; never merge "
                    "bodies because one DSL schema can express both (F11)"}
