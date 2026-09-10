# -*- coding: utf-8 -*-
"""CENSUS-B0 判同阶段：加载冻结盲程序 + template_registry，跑 census_engine
structural_diff / merge_verdict / family_admit，输出 engine_report.json。

引擎只出结构事实；四态 verdict 的语义裁决由 worker reasoning 给出
（见 merge_tests.jsonl）。Registry 原文保持不动，CRR 的 IR 形式仅为
comparison view（provenance 记录于 merge_tests）。
"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff, merge_verdict, family_admit  # noqa: E402

BATCH = Path(__file__).parent

# --- registry v0 唯一种子 → comparison IR（顺序/deps 依 registry canonical 文本） ---
CRR_IR = {
    "program_id": "TEMPLATE::CONSTRAINED_RELATIVE_REFUGE",
    "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
        {"op": "GATE_HARD_VIABILITY", "deps": [0]},      # Apply Hard Viability Constraint(s) -> FeasibleSet
        {"op": "EVAL_RELATIVE_RANK", "deps": [1]},       # RelativeRank(target, reference_set=FeasibleSet)
        {"op": "EVAL_SECONDARY_HABITAT", "deps": [2]},   # Secondary Refuge / Habitat Evaluation
        {"op": "COMBINE_FIXED", "deps": [3]},
    ],
    "branches": [{"kind": "GATE", "guard": "hard_viability", "else": "exclude_from_feasible"}],
    "combine": "FIXED",
    "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}},
}

# --- 本批新立候选族 canonical（candidate_canonical_body，IR 形式） ---
CANONICALS = {
    "PLAIN_FACTOR_COMBINE": {
        "program_id": "TEMPLATE::PLAIN_FACTOR_COMBINE",
        "surface": "Bake",
        "incoming_premises": [],
        "ordered_steps": [
            {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": []},
            {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": []},
            {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": []},
            {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": []},
            {"op": "COMBINE_WEIGHTED", "deps": [0, 1, 2, 3]},
        ],
        "branches": [],
        "combine": "WEIGHTED_FACTORS",
        "return_type": "SpatialDistributionWeight",
        "instance_noise": {"species": None, "profile": None, "constants": {}},
    },
    "HARD_GATED_FACTOR_COMBINE": {
        "program_id": "TEMPLATE::HARD_GATED_FACTOR_COMBINE",
        "surface": "Bake",
        "incoming_premises": [],
        "ordered_steps": [
            {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
            {"op": "GATE_HARD_VIABILITY", "deps": [0]},
            {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": [1]},
            {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": [1]},
            {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": [1]},
            {"op": "COMBINE_WEIGHTED", "deps": [2, 3, 4]},
        ],
        "branches": [{"kind": "GATE", "guard": "hard_viability", "else": "exclude_from_feasible"}],
        "combine": "WEIGHTED_FACTORS",
        "return_type": "SpatialDistributionWeight",
        "instance_noise": {"species": None, "profile": None, "constants": {}},
    },
    "PATCH_RESOURCE_FOLLOWING": {
        "program_id": "TEMPLATE::PATCH_RESOURCE_FOLLOWING",
        "surface": "Bake",
        "incoming_premises": [],
        "ordered_steps": [
            {"op": "EVAL_RESOURCE_PATCH", "deps": []},
            {"op": "CONSTRAIN_ZONE", "deps": [0]},
            {"op": "NORMALIZE_WEIGHT", "deps": [1]},
        ],
        "branches": [],
        "combine": "NONE_SINGLE_CHAIN",
        "return_type": "SpatialDistributionWeight",
        "instance_noise": {"species": None, "profile": None, "constants": {}},
    },
    "TYPED_TARGET_RESPONSE": {
        "program_id": "TEMPLATE::TYPED_TARGET_RESPONSE",
        "surface": "Response",
        "incoming_premises": [],
        "ordered_steps": [
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        "branches": [],
        "combine": "NONE",
        "return_type": "Response(TargetFeeding)",
        "instance_noise": {"species": None, "profile": None, "constants": {}},
    },
    "GUARD_CONFLICT_DUAL_PATH_RESPONSE": {
        "program_id": "TEMPLATE::GUARD_CONFLICT_DUAL_PATH_RESPONSE",
        "surface": "Response",
        "incoming_premises": ["guard_state = ACTIVE (persistent condition premise)"],
        "ordered_steps": [
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
            {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
            {"op": "DECIDE_RESPONSE", "deps": [2]},
        ],
        "branches": [],
        "combine": "DUAL_PATH_MERGE",
        "return_type": "Response(TargetFeeding | RelationalConflict)",
        "instance_noise": {"species": None, "profile": None, "constants": {}},
    },
}

# program -> (template, 轴) 检索计划：仅同 surface 比较
PLAN_VS_CRR = ["P-MGC-BAKE-ADULT", "P-LUN-BAKE-WET", "P-LUN-BAKE-AESTIVATION",
               "P-OSC-BAKE", "P-EEL-BAKE", "P-CHB-BAKE"]
FAMILY_TESTS = [
    ("P-OSC-BAKE", "PLAIN_FACTOR_COMBINE"),
    ("P-CHB-BAKE", "PLAIN_FACTOR_COMBINE"),
    ("P-LUN-BAKE-WET", "HARD_GATED_FACTOR_COMBINE"),
    ("P-EEL-BAKE", "HARD_GATED_FACTOR_COMBINE"),
    ("P-LUN-BAKE-WET", "PLAIN_FACTOR_COMBINE"),        # extension 判例：gate 轴
    ("P-EEL-BAKE", "PLAIN_FACTOR_COMBINE"),            # extension 判例：gate 轴
    ("P-MGC-BAKE-ADULT", "PATCH_RESOURCE_FOLLOWING"),
    ("P-MGC-BAKE-ADULT", "PLAIN_FACTOR_COMBINE"),      # 单链 vs 多因子：确证不并入
    ("P-MGC-RESP-FEEDING", "TYPED_TARGET_RESPONSE"),
    ("P-LUN-RESP-FEEDING", "TYPED_TARGET_RESPONSE"),
    ("P-OSC-RESP-FEEDING", "TYPED_TARGET_RESPONSE"),
    ("P-CHB-RESP-FEEDING", "TYPED_TARGET_RESPONSE"),
    ("P-EEL-RESP-SENSE", "TYPED_TARGET_RESPONSE"),     # evaluator_channel 轴判例
    ("P-OSC-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"),
    ("P-LUN-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"),
    ("P-LUN-BAKE-AESTIVATION", "PLAIN_FACTOR_COMBINE"),   # ambiguous 程序的 raw 记录
    ("P-LUN-BAKE-AESTIVATION", "HARD_GATED_FACTOR_COMBINE"),
    # FIX-001 补录两条（R2 顺带项：engine_report 重生成到 25 条）
    ("P-EEL-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"),
    ("P-EEL-RESP-FEEDING", "TYPED_TARGET_RESPONSE"),
]


def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
                 if line.strip())}
    # FIX-001 补录程序 body（非盲，provenance 见 programs.jsonl）
    sys.path.insert(0, str(BATCH))
    from apply_fix_001 import EEL_GUARD, EEL_FEEDING  # noqa: E402
    programs[EEL_GUARD["program_id"]] = EEL_GUARD
    programs[EEL_FEEDING["program_id"]] = EEL_FEEDING
    report = {"vs_CRR": [], "family": []}
    for pid in PLAN_VS_CRR:
        p = programs[pid]
        diffs = sorted(structural_diff(p, CRR_IR))
        report["vs_CRR"].append({"program_id": pid, "structural_diffs": diffs})
    for pid, fam in FAMILY_TESTS:
        p = programs[pid]
        fam_body = CANONICALS[fam]
        fam_dict = {"canonical_program_body": fam_body,
                    "allowed_parameter_axes": ["factor_set(typed,bounded)",
                                               "factor_weights",
                                               "evaluator_channel(typed)",
                                               "hard_constraint_gate: NONE|typed"],
                    "version": 1}
        report["family"].append({
            "program_id": pid, "family": fam,
            "engine_family_admit": family_admit(fam_dict, p),
            "engine_structural_diff": sorted(structural_diff(p, fam_body)),
        })
    out = BATCH / "engine_report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report -> {out}")
    print("\n-- vs CRR --")
    for r in report["vs_CRR"]:
        print(f"  {r['program_id']}: {r['structural_diffs']}")
    print("\n-- family direct tests --")
    for r in report["family"]:
        print(f"  {r['program_id']} vs {r['family']}: "
              f"{r['engine_family_admit'].get('direct_test', r['engine_family_admit']).get('verdict', 'ADMITTED')} "
              f"diffs={r['engine_structural_diff']}")


if __name__ == "__main__":
    main()
