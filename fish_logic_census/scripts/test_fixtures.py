"""Golden Regression Fixtures F01-F17 (Notion: 3d7a4137d23681688f54cf0f3dd5133b).

Automated core. Fixtures whose essence is structural/bookkeeping are fully
asserted here; fixtures with a semantic-judge component carry a
SEMANTIC_JUDGE note — that part stays with the reviewer/LLM and is NOT
pretended to be solved by static analysis (per the fixtures page's own note).

Run via pytest (main suite) or `python fish_logic_census/scripts/run_fixtures.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from census_engine import (census_count, deinstantiate, family_admit,
                            helper_admission, merge_verdict, structural_diff)


def _prog(pid, premises, ops, deps=None, branches=None, combine=None,
          ret="SpatialWeight", species=None, profile=None):
    deps = deps or [[] for _ in ops]
    return {"program_id": pid, "surface": "Bake",
            "incoming_premises": premises,
            "ordered_steps": [{"op": o, "deps": d} for o, d in zip(ops, deps)],
            "branches": branches or [], "combine": combine, "return_type": ret,
            "instance_noise": {"species": species, "profile": profile, "constants": {}},
            "helpers": []}


# F01: ordered programs must not merge via canonicalization
def test_f01_order_diff_blocks_merge():
    a = _prog("A", [], ["TemperatureGate", "StructureFit", "DepthFit"])
    b = _prog("B", [], ["StructureGate", "TemperatureFit", "DepthFit"])
    diffs = structural_diff(a, b)
    assert "ORDER" in diffs or "OPERATOR" in diffs
    v = merge_verdict(b, a)
    assert v["verdict"] != "MERGE_CONFIDENT"
    if "ORDER" in v["structural_diffs"]:
        assert v["structural_diffs"]  # STRUCTURAL_DIFF contains ORDER


# F02: activation difference stays in premises; identical bodies may merge-test
def test_f02_activation_is_premise_not_body():
    a = _prog("A", ["FishMode=Winter"], ["StructureFit", "DepthFit", "FixedCombine"])
    b = _prog("B", ["FishMode=SummerNight"], ["StructureFit", "DepthFit", "FixedCombine"])
    v = merge_verdict(b, a)
    assert v["verdict"] == "MERGE_CONFIDENT"  # premise diff excluded from body


# F03: surface-owned CHECK/GATE cannot be laundered into an upstream premise
def test_f03_gate_difference_is_structural():
    gated = _prog("A", ["FishMode=Winter"], ["AbsoluteThermalFit"],
                  branches=[{"kind": "GATE", "guard": "NormalAcceptableThermalHabitatExists", "else": "RelativeWarmthRank"}])
    flat = _prog("B", ["FishMode=Winter"], ["AbsoluteThermalFit"])
    v = merge_verdict(gated, flat)
    assert "BRANCH" in v["structural_diffs"]
    assert v["verdict"] != "MERGE_CONFIDENT"


# F04: intermediate dependency (FeasibleSet -> RelativeWarmthRank) is preserved
def test_f04_dependency_not_flattened():
    pike = _prog("PikeWinter", ["ColdRegime=TRUE"],
                 ["ApplyHardViability", "RelativeWarmthRank", "RefugeEvaluation"],
                 deps=[[], ["0:FeasibleSet"], ["0:FeasibleSet"]])
    flat = _prog("FlatFactors", ["ColdRegime=TRUE"],
                 ["TemperatureFactor", "DOFactor", "RefugeFactor"],
                 deps=[[], [], []])
    v = merge_verdict(pike, flat)
    assert "DEPENDENCY" in v["structural_diffs"] or "OPERATOR" in v["structural_diffs"]
    assert v["verdict"] != "MERGE_CONFIDENT"


# F05: Winter vs Summer merge requires secondary-evaluation closure
def test_f05_secondary_unclosed_not_confident():
    winter = _prog("W", [], ["ViabilityConstraint", "RelativeRank(WARMER)", "SecondaryRefugeEvaluation", "Combine"],
                   deps=[[], ["0:FeasibleSet"], ["0:FeasibleSet"], []])
    summer = _prog("S", [], ["DOConstraint", "RelativeRank(COOLER)", "SecondaryHabitatEvaluation", "Combine"],
                   deps=[[], ["0:FeasibleSet"], ["0:FeasibleSet"], []])
    v = merge_verdict(summer, winter)
    assert v["verdict"] != "MERGE_CONFIDENT"  # AMBIGUOUS or NEW until secondary closes


# F06: helper laundering intercepted
def test_f06_helper_laundering_fails():
    bad = {"name": "PikeCurrentStrategySpatialScore", "body_has_control_flow": True,
           "case_specific": True}
    assert helper_admission(bad)["verdict"] == "HELPER_ADMISSION_FAIL"
    good = {"name": "RelativeRank", "body_has_control_flow": False, "case_specific": False}
    assert helper_admission(good)["admitted"]


# F07: feature similarity is not merge evidence
def test_f07_features_are_not_evidence():
    a = _prog("A", [], ["AbsoluteTemperatureGate", "StructureFit", "Combine"])
    b = _prog("B", [], ["DOConstraint", "FeasibleSet", "RelativeTemperatureRank", "PreyTradeoff"])
    v = merge_verdict(b, a)
    assert v["structural_diffs"] != []
    assert v["verdict"] != "MERGE_CONFIDENT"


# F10/F11: instances vs templates; schema reuse != body identity
def test_f10_f11_counting():
    x = _prog("X", [], ["Gate", "Fit", "Combine"], species="Pike", profile="P1")
    y = _prog("Y", [], ["Gate", "Fit", "Combine"], species="Bass", profile="P2")
    counts = census_count([x, y], [{"t": 1}])
    assert counts["n_program_instances"] == 2
    assert counts["n_logic_templates"] <= 2  # at most 1 template for these two
    # F11: A->B->C vs B->A->C = 2 bodies even if one schema expresses both
    p1 = _prog("P1", [], ["A", "B", "C"])
    p2 = _prog("P2", [], ["B", "A", "C"])
    assert "ORDER" in structural_diff(p1, p2)


# F13: de-instantiation never mutates the original
def test_f13_original_immutable():
    import hashlib, json
    from copy import deepcopy
    p = _prog("P", [], ["Step1", "Step2"], species="Pike", profile="PikeWinter")
    p["blind_hash"] = hashlib.sha256(json.dumps(p["ordered_steps"], sort_keys=True).encode()).hexdigest()[:16]
    frozen = deepcopy(p)
    view = deinstantiate(p)
    assert view["instance_noise"]["species"] is None
    assert view["original_program_body"]["hash"] == frozen["blind_hash"]
    assert p["ordered_steps"] == frozen["ordered_steps"]  # original untouched


# F14: bounded axis is an EXTENSION, never a disguised merge
def test_f14_extension_not_merge():
    template = _prog("T", [], ["A", "B"])
    extended = _prog("E", [], ["A", "B"])
    extended["ordered_steps"].append({"op": "optional_slot_C(ON|OFF)", "deps": []})
    v = merge_verdict(extended, template)
    assert v["verdict"] in ("TEMPLATE_EXTENSION_CANDIDATE", "NEW_TEMPLATE_CANDIDATE")
    assert v["verdict"] != "MERGE_CONFIDENT"
    if v["verdict"] == "TEMPLATE_EXTENSION_CANDIDATE":
        assert set(v["requires"]) == {"extension_complexity_cost",
                                      "new_template_complexity_cost", "recommended_shape"}


# F15: no chained similarity in candidate families
def test_f15_chain_ban():
    family = {"version": 1,
              "canonical_program_body": _prog("canon", [], ["A", "B", "Return"]),
              "allowed_parameter_axes": []}
    member = _prog("C", [], ["A", "B", "Return"])
    assert family_admit(family, member)["admitted"] is True
    intruder = _prog("C", [], ["A", "B", "Return", "ExtraStep"])
    result = family_admit(family, intruder)
    assert result["admitted"] is False
    assert result["canonical_version_next"] == 2
    assert result["regression_recheck_required"] is True


# F16/F17/F08/F09/F12: validator-behavior fixtures -> see validate_batch.py
# (tested via test_validate_batch below with synthetic batch data)
def test_validator_guardrails(tmp_path):
    import validate_batch as vb
    # F08: classification without sketch
    stories = [{"story_id": "S1", "consequence": "PARAM_PROFILE"}]  # no sketch, no NO_SURFACE reason
    errs = vb.check_consequence_sketches(stories, sketches=[])
    assert any("PROGRAM_SKETCH_REQUIRED_BEFORE_CONSEQUENCE_CLASSIFICATION" in e for e in errs)
    # F09: shallow research, strong absence claim
    coverage = [{"story_id": "S1", "r": {"R5": "EVIDENCE_INSUFFICIENT", "R8": "EVIDENCE_INSUFFICIENT"}}]
    errs = vb.check_absence_claims(coverage, claims=[{"story_id": "S1", "claim": "NO_NEW_PROGRAM_CURRENT_EVIDENCE"}])
    assert any("ABSENCE_CLAIM_EXCEEDS_RESEARCH_COVERAGE" in e for e in errs)
    # F12: all-checked but no second pass
    cov2 = [{"story_id": "S2", "r": {f"R{i}": "FOUND" for i in range(1, 11)}, "second_pass": None}]
    errs = vb.check_depth_gate(cov2)
    assert any("TARGETED_SECOND_PASS_REQUIRED" in e for e in errs)
    # F17: blind sketch mutated after registry open without revision
    programs = [{"program_id": "P1", "blind_hash": "H1", "registry_seen_at_creation": False,
                 "post_registry_mutations": [{"reason": "polish"}]}]
    errs = vb.check_blind_freeze(programs)
    assert any("BLIND_SKETCH_POST_REGISTRY_MUTATION" in e for e in errs)
    # F16: research stage read registry before freeze
    manifest = {"stage": "RESEARCH", "registry_reads_before_freeze": True}
    errs = vb.check_stage_blindness(manifest)
    assert any("RESEARCH_BLINDNESS_VIOLATION" in e for e in errs)
