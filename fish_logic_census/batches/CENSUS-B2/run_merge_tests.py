# -*- coding: utf-8 -*-
"""CENSUS-B2 判同段：盲程序 20 × registry v3（engine raw；语义裁决在 build_census_outputs.py）。"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent

CRR_IR = {
    "program_id": "TEMPLATE::CONSTRAINED_RELATIVE_REFUGE", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
        {"op": "GATE_HARD_VIABILITY", "deps": [0]},
        {"op": "EVAL_RELATIVE_RANK", "deps": [1]},
        {"op": "EVAL_SECONDARY_HABITAT", "deps": [2]},
        {"op": "COMBINE_FIXED", "deps": [3]}],
    "branches": [{"kind": "GATE", "guard": "hard_viability", "else": "exclude_from_feasible"}],
    "combine": "FIXED", "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}

def tpl(pid, surface, steps, combine, rtype):
    return {"program_id": f"TEMPLATE::{pid}", "surface": surface,
            "incoming_premises": [],
            "ordered_steps": [{"op": op, "deps": d} for op, d in steps],
            "branches": [], "combine": combine, "return_type": rtype,
            "instance_noise": {"species": None, "profile": None, "constants": {}}}

CANONICALS = {
    "SINGLE_FACTOR_NORMALIZED_WEIGHT": tpl("SINGLE_FACTOR_NORMALIZED_WEIGHT", "Bake", [
        ("EVAL_TYPED_FIELD_OR_FACTOR", []), ("NORMALIZE_WEIGHT", [0])],
        "NONE_SINGLE_CHAIN", "SpatialDistributionWeight"),
    "PLAIN_FACTOR_COMBINE": tpl("PLAIN_FACTOR_COMBINE", "Bake", [
        ("EVAL_HABITAT_FACTOR_TYPED", []), ("EVAL_HABITAT_FACTOR_TYPED", []),
        ("EVAL_RESOURCE_FACTOR_TYPED", []), ("EVAL_RESOURCE_FACTOR_TYPED", []),
        ("COMBINE_WEIGHTED", [0, 1, 2, 3])], "WEIGHTED_FACTORS", "SpatialDistributionWeight"),
    "TYPED_TARGET_RESPONSE": tpl("TYPED_TARGET_RESPONSE", "Response", [
        ("EVAL_TARGET_AS_FOOD_TYPED", []), ("DECIDE_RESPONSE", [0])],
        "NONE", "Response(TargetFeeding)"),
    "CUE_GUIDED_APPROACH_AVOID": tpl("CUE_GUIDED_APPROACH_AVOID", "Response", [
        ("EVAL_AMBIENT_CUE_GRADIENT_TYPED", []), ("DECIDE_APPROACH_OR_AVOID", [0])],
        "NONE", "Response(Approach | Avoid)"),
    "FOOD_FIELD_FEEDING_RESPONSE": tpl("FOOD_FIELD_FEEDING_RESPONSE", "Response", [
        ("EVAL_FOOD_FIELD_INTAKE", []), ("DECIDE_FIELD_FEEDING", [0])],
        "NONE", "Response(FieldFeeding)"),
}

VS_CRR = ["P-B2-PIK19-BAKE", "P-B2-WAL-BAKE", "P-B2-BRT12-BAKE", "P-B2-ARC-BAKE",
          "P-B2-VEN-BAKE", "P-B2-FGA-BAKE", "P-B2-SWO-BAKE", "P-B2-BHC-BAKE",
          "P-B2-HER-BAKE", "P-B2-MDF-BAKE"]
FAMILY = [
    ("P-B2-PIK19-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-BRT12-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-ARC-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-VEN-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-FGA-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-SWO-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-BHC-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-HER-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B2-WAL-BAKE", "PLAIN_FACTOR_COMBINE"),
    ("P-B2-MDF-BAKE", "PLAIN_FACTOR_COMBINE"),
    ("P-B2-PIK19-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-WAL-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-BRT12-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-ARC-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-VEN-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-FGA-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-SWO-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-MDF-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B2-BHC-RESP-FIELD", "FOOD_FIELD_FEEDING_RESPONSE"),
    ("P-B2-HER-RESP-FIELD", "FOOD_FIELD_FEEDING_RESPONSE"),
    ("P-B2-BHC-RESP-FIELD", "TYPED_TARGET_RESPONSE"),
    ("P-B2-HER-RESP-FIELD", "CUE_GUIDED_APPROACH_AVOID"),
]

def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
                 if line.strip())}
    report = {"vs_CRR": [], "family": []}
    for pid in VS_CRR:
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(structural_diff(programs[pid], CRR_IR))})
    for pid, fam in FAMILY:
        report["family"].append({
            "program_id": pid, "family": fam,
            "engine_structural_diff": sorted(structural_diff(programs[pid], CANONICALS[fam]))})
    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report: vs_CRR={len(report['vs_CRR'])} family={len(report['family'])}")
    for r in report["vs_CRR"]:
        print(f"  CRR {r['program_id']}: {r['structural_diffs']}")
    for r in report["family"]:
        print(f"  {r['program_id']:<22} vs {r['family']:<32} {r['engine_structural_diff']}")

if __name__ == "__main__":
    main()
