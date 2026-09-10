# -*- coding: utf-8 -*-
"""CENSUS-B1 判同阶段：盲程序（24）× template_registry v2，census_engine 出
结构事实；四态语义裁决见 merge_tests.jsonl（本批生成于 build_census_outputs.py）。
"""
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
        {"op": "COMBINE_FIXED", "deps": [3]},
    ],
    "branches": [{"kind": "GATE", "guard": "hard_viability", "else": "exclude_from_feasible"}],
    "combine": "FIXED", "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}},
}

def tpl(pid, surface, steps, combine, rtype, premises=None, branches=None):
    return {"program_id": f"TEMPLATE::{pid}", "surface": surface,
            "incoming_premises": premises or [],
            "ordered_steps": [{"op": op, "deps": d} for op, d in steps],
            "branches": branches or [], "combine": combine, "return_type": rtype,
            "instance_noise": {"species": None, "profile": None, "constants": {}}}

CANONICALS = {
    # B0 既有族（canonical 与 B0 run_merge_tests.py 一致）
    "PLAIN_FACTOR_COMBINE": tpl("PLAIN_FACTOR_COMBINE", "Bake", [
        ("EVAL_HABITAT_FACTOR_TYPED", []), ("EVAL_HABITAT_FACTOR_TYPED", []),
        ("EVAL_RESOURCE_FACTOR_TYPED", []), ("EVAL_RESOURCE_FACTOR_TYPED", []),
        ("COMBINE_WEIGHTED", [0, 1, 2, 3])], "WEIGHTED_FACTORS",
        "SpatialDistributionWeight"),
    "PATCH_RESOURCE_FOLLOWING": tpl("PATCH_RESOURCE_FOLLOWING", "Bake", [
        ("EVAL_RESOURCE_PATCH", []), ("CONSTRAIN_ZONE", [0]),
        ("NORMALIZE_WEIGHT", [1])], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight"),
    "TYPED_TARGET_RESPONSE": tpl("TYPED_TARGET_RESPONSE", "Response", [
        ("EVAL_TARGET_AS_FOOD_TYPED", []), ("DECIDE_RESPONSE", [0])],
        "NONE", "Response(TargetFeeding)"),
    "GUARD_CONFLICT_DUAL_PATH_RESPONSE": tpl(
        "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "Response", [
            ("EVAL_TARGET_AS_FOOD_TYPED", []), ("EVAL_TARGET_AS_INTRUDER_TYPED", []),
            ("COMBINE_DUAL_PATH", [0, 1]), ("DECIDE_RESPONSE", [2])],
        "DUAL_PATH_MERGE", "Response(TargetFeeding | RelationalConflict)"),
    # B1 新候选族 canonical
    "SINGLE_FACTOR_NORMALIZED_WEIGHT": tpl("SINGLE_FACTOR_NORMALIZED_WEIGHT", "Bake", [
        ("EVAL_TYPED_FIELD_OR_FACTOR", []), ("NORMALIZE_WEIGHT", [0])],
        "NONE_SINGLE_CHAIN", "SpatialDistributionWeight"),
    "CUE_GUIDED_APPROACH_AVOID": tpl("CUE_GUIDED_APPROACH_AVOID", "Response", [
        ("EVAL_AMBIENT_CUE_GRADIENT_TYPED", []), ("DECIDE_APPROACH_OR_AVOID", [0])],
        "NONE", "Response(Approach | Avoid)"),
}

PLAN_VS_CRR = [p for p in ["P-B1-GRB-BAKE", "P-B1-BRT-BAKE", "P-B1-DRU-BAKE",
                           "P-B1-COD-BAKE", "P-B1-PAD34-BAKE", "P-B1-BLU-BAKE",
                           "P-B1-SMA-BAKE", "P-B1-LAM-BAKE", "P-B1-ONS-BAKE"]]
FAMILY_TESTS = [
    # SINGLE 族（7 成员直验）
    ("P-B1-GRB-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-DRU-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-PAD34-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-SMA-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-COD-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-BLU-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    ("P-B1-LAM-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"),
    # PATCH 族第二成员 + SINGLE patch 成员 vs PATCH（optional_context extension 判例）
    ("P-B1-ONS-BAKE", "PATCH_RESOURCE_FOLLOWING"),
    ("P-B1-GRB-BAKE", "PATCH_RESOURCE_FOLLOWING"),
    ("P-B1-DRU-BAKE", "PATCH_RESOURCE_FOLLOWING"),
    ("P-B1-PAD34-BAKE", "PATCH_RESOURCE_FOLLOWING"),
    ("P-B1-SMA-BAKE", "PATCH_RESOURCE_FOLLOWING"),
    # PLAIN 族第 3 成员（rank 因子）
    ("P-B1-BRT-BAKE", "PLAIN_FACTOR_COMBINE"),
    # TYPED 族 13 个 B1 成员
    ("P-B1-GRB-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-BRT-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-TIL-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-PAD35-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-DRU-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-COD-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-PAD34-RESP-SENSE", "TYPED_TARGET_RESPONSE"),
    ("P-B1-PIK-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-GAR-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-BLU-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-SMA-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-RAI-RESP", "TYPED_TARGET_RESPONSE"),
    ("P-B1-ONS-RESP", "TYPED_TARGET_RESPONSE"),
    # DUAL 族第 4 成员
    ("P-B1-DIS-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"),
    # LAM approach vs TYPED（evaluand/return 边界判例）
    ("P-B1-LAM-RESP-APPROACH", "TYPED_TARGET_RESPONSE"),
    ("P-B1-LAM-RESP-APPROACH", "CUE_GUIDED_APPROACH_AVOID"),
]


def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
                 if line.strip())}
    report = {"vs_CRR": [], "family": []}
    for pid in PLAN_VS_CRR:
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(structural_diff(programs[pid], CRR_IR))})
    for pid, fam in FAMILY_TESTS:
        report["family"].append({
            "program_id": pid, "family": fam,
            "engine_structural_diff": sorted(structural_diff(programs[pid], CANONICALS[fam]))})
    out = BATCH / "engine_report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report -> {out}")
    print("\n-- vs CRR --")
    for r in report["vs_CRR"]:
        print(f"  {r['program_id']}: {r['structural_diffs']}")
    print("\n-- family --")
    for r in report["family"]:
        print(f"  {r['program_id']:<24} vs {r['family']:<34} diffs={r['engine_structural_diff']}")


if __name__ == "__main__":
    main()
