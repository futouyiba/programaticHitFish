# -*- coding: utf-8 -*-
"""CENSUS-B4 判同段：盲程序 50 × registry v5 canonical（engine raw；
语义裁决在 build_census_outputs.py）。canonical IR 形状逐字取自各批
run_merge_tests.py 的 ir_pointer（B0/B1/B2），不重造。

【B3-F-2 修正】STATE_GATED_MULTI_PATH_RESPONSE canonical 此前仅指向
batches/CENSUS-B3/build_blind_programs.py::P-B3-CHU-RESP-FASTING（盲程序本体），
未物化为 run_merge_tests 可测的 CANONICALS 条目——本批物化（IR 逐字转写，
无改写）并执行：①canonical 源自测（CHU 零差异验证物化忠实性）②SHA 成员
直验回归复检（F15 族完整性）。registry v6 的 ir_pointer 同步指向本物化。"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent
B3 = BATCH.parent / "CENSUS-B3"

CRR_IR = {
    "program_id": "TEMPLATE::CONSTRAINED_RELATIVE_REFUGE", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
        {"op": "GATE_HARD_VIABILITY", "deps": [0]},
        {"op": "EVAL_RELATIVE_RANK", "deps": [1]},
        {"op": "EVAL_SECONDARY_HABITAT", "deps": [2]},
        {"op": "COMBINE_FIXED", "deps": [3]}],
    "branches": [{"kind": "GATE", "guard": "hard_viability",
                  "else": "exclude_from_feasible"}],
    "combine": "FIXED", "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}


def tpl(pid, surface, steps, combine, rtype, premises=None, branches=None):
    return {"program_id": f"TEMPLATE::{pid}", "surface": surface,
            "incoming_premises": premises or [],
            "ordered_steps": [{"op": op, "deps": d} for op, d in steps],
            "branches": branches or [], "combine": combine,
            "return_type": rtype,
            "instance_noise": {"species": None, "profile": None, "constants": {}}}


CANONICALS = {
    # B1 run_merge_tests.py::CANONICALS.SINGLE_FACTOR_NORMALIZED_WEIGHT
    "SINGLE_FACTOR_NORMALIZED_WEIGHT": tpl(
        "SINGLE_FACTOR_NORMALIZED_WEIGHT", "Bake", [
            ("EVAL_TYPED_FIELD_OR_FACTOR", []), ("NORMALIZE_WEIGHT", [0])],
        "NONE_SINGLE_CHAIN", "SpatialDistributionWeight"),
    # B0 ...::TYPED_TARGET_RESPONSE
    "TYPED_TARGET_RESPONSE": tpl(
        "TYPED_TARGET_RESPONSE", "Response", [
            ("EVAL_TARGET_AS_FOOD_TYPED", []), ("DECIDE_RESPONSE", [0])],
        "NONE", "Response(TargetFeeding)"),
    # B0 ...::GUARD_CONFLICT_DUAL_PATH_RESPONSE（premises 依 registry canonical）
    "GUARD_CONFLICT_DUAL_PATH_RESPONSE": tpl(
        "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "Response", [
            ("EVAL_TARGET_AS_FOOD_TYPED", []),
            ("EVAL_TARGET_AS_INTRUDER_TYPED", []),
            ("COMBINE_DUAL_PATH", [0, 1]),
            ("DECIDE_RESPONSE", [2])],
        "DUAL_PATH_MERGE", "Response(TargetFeeding | RelationalConflict)",
        premises=["guard_state = ACTIVE (persistent condition premise)"]),
    # B3-F-2 物化：batches/CENSUS-B3/build_blind_programs.py::P-B3-CHU-RESP-FASTING
    # IR 逐字转写（ordered_steps/branches/combine/return_type 不改写）
    "STATE_GATED_MULTI_PATH_RESPONSE": tpl(
        "STATE_GATED_MULTI_PATH_RESPONSE", "Response", [
            ("EVAL_MIGRATION_FASTING_STATE", []),
            ("EVAL_TARGET_AS_FOOD_TYPED", [0]),
            ("EVAL_STRIKE_NON_FEEDING", [0]),
            ("DECIDE_MULTI_PATH_RESPONSE", [1, 2])],
        "STATE_GATED_MULTI_PATH", "Response(TargetFeeding | NonFeedingStrike)",
        branches=[{"kind": "IF", "guard": "migration_stage==FASTING_RUN",
                   "else": "OCEAN_FEEDING"}]),
}

BAKES = ["POR", "SDG", "TSK", "ASR", "RVS", "GPF", "RKB", "SSL", "BSK",
         "RRH", "GRH", "SMB", "GDE", "WIT", "WIN", "YTF", "SMF", "BST",
         "FDR", "BSB", "CBM", "SAI", "HNC", "MOO", "RDS"]            # 25（BFS 0 程序）
TYPED_RESP = ["POR", "SDG", "TSK", "ASR", "RVS", "GPF", "RKB", "SSL", "BSK",
              "RRH", "GRH", "SMB", "GDE", "WIT", "WIN", "YTF", "SMF", "BST",
              "FDR", "BSB", "CBM", "SAI", "MOO", "RDS"]              # 24 标准
GUARD_RESP = ["HNC"]                                                 # 1（extension 候选）

FAMILY = []
for sid in BAKES:
    FAMILY.append((f"P-B4-{sid}-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"))
for sid in TYPED_RESP:
    FAMILY.append((f"P-B4-{sid}-RESP", "TYPED_TARGET_RESPONSE"))
# HNC：族直验（GUARD）+ 两跨族互证（TYPED 单路径 / STATE_GATED 门控——§9.2 边界）
FAMILY.append(("P-B4-HNC-RESP", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"))
FAMILY.append(("P-B4-HNC-RESP", "TYPED_TARGET_RESPONSE"))
FAMILY.append(("P-B4-HNC-RESP", "STATE_GATED_MULTI_PATH_RESPONSE"))
# B3-F-2：物化忠实性自测（canonical 源）+ SHA 成员直验回归复检（F15）
F2_TESTS = [("P-B3-CHU-RESP-FASTING", "STATE_GATED_MULTI_PATH_RESPONSE"),
            ("P-B3-SHA-RESP-FASTING", "STATE_GATED_MULTI_PATH_RESPONSE")]


def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8")
                 .splitlines() if line.strip())}
    b3_programs = {p["program_id"]: p for p in
                   (json.loads(line) for line in
                    (B3 / "blind_programs.jsonl").read_text(encoding="utf-8")
                    .splitlines() if line.strip())}
    report = {"vs_CRR": [], "family": [], "b3_f2_state_gated_materialization": []}
    for sid in BAKES:
        pid = f"P-B4-{sid}-BAKE"
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(
                                     structural_diff(programs[pid], CRR_IR))})
    for pid, fam in FAMILY:
        report["family"].append({
            "program_id": pid, "family": fam,
            "engine_structural_diff": sorted(
                structural_diff(programs[pid], CANONICALS[fam]))})
    for pid, fam in F2_TESTS:
        report["b3_f2_state_gated_materialization"].append({
            "program_id": pid, "family": fam, "role": (
                "canonical_source_selftest" if pid.endswith("CHU-RESP-FASTING")
                else "member_regression_recheck"),
            "engine_structural_diff": sorted(
                structural_diff(b3_programs[pid], CANONICALS[fam]))})
    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report: vs_CRR={len(report['vs_CRR'])} "
          f"family={len(report['family'])} "
          f"b3_f2={len(report['b3_f2_state_gated_materialization'])}")
    for r in report["vs_CRR"]:
        print(f"  CRR {r['program_id']}: {r['structural_diffs']}")
    for r in report["family"]:
        print(f"  {r['program_id']:<16} vs {r['family']:<36} "
              f"{r['engine_structural_diff']}")
    for r in report["b3_f2_state_gated_materialization"]:
        print(f"  F2 {r['program_id']:<24} vs {r['family']:<36} "
              f"{r['engine_structural_diff']} ({r['role']})")


if __name__ == "__main__":
    main()
