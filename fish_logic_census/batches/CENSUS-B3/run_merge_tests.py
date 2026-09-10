# -*- coding: utf-8 -*-
"""CENSUS-B3 判同段：盲程序 54 × registry v4 canonical（engine raw；
语义裁决在 build_census_outputs.py）。canonical IR 形状逐字取自各批
run_merge_tests.py 的 ir_pointer（B0/B1/B2），不重造。"""
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
}

BAKES = ["CHU", "CHN", "COH", "PIN", "BRO", "SHA", "ALE", "AST", "SNS", "TAR",
         "TAI", "ARA", "PB", "RBP", "BLP", "WEL", "FLA", "BUR", "GW", "SGA",
         "RFP", "DS", "PBF", "GT", "HAL", "GG"]                      # 26（PAY/SHO 无 Bake）
TYPED_RESP = ["CHN", "COH", "PIN", "BRO", "ALE", "AST", "SNS", "TAR", "TAI",
              "PB", "BLP", "FLA", "BUR", "GW", "PAY", "SGA", "SHO", "RFP",
              "DS", "PBF", "GT", "HAL", "GG"]                        # 23 标准
GUARD_RESP = ["ARA", "RBP", "WEL"]                                   # 3
FASTING = ["CHU", "SHA"]                                             # 2

FAMILY = []
for sid in BAKES:
    FAMILY.append((f"P-B3-{sid}-BAKE", "SINGLE_FACTOR_NORMALIZED_WEIGHT"))
for sid in TYPED_RESP:
    FAMILY.append((f"P-B3-{sid}-RESP", "TYPED_TARGET_RESPONSE"))
for sid in GUARD_RESP:
    FAMILY.append((f"P-B3-{sid}-RESP", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"))
for sid in FASTING:
    FAMILY.append((f"P-B3-{sid}-RESP-FASTING", "TYPED_TARGET_RESPONSE"))
    FAMILY.append((f"P-B3-{sid}-RESP-FASTING", "GUARD_CONFLICT_DUAL_PATH_RESPONSE"))


def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8")
                 .splitlines() if line.strip())}
    report = {"vs_CRR": [], "family": []}
    for sid in BAKES:
        pid = f"P-B3-{sid}-BAKE"
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(
                                     structural_diff(programs[pid], CRR_IR))})
    for pid, fam in FAMILY:
        report["family"].append({
            "program_id": pid, "family": fam,
            "engine_structural_diff": sorted(
                structural_diff(programs[pid], CANONICALS[fam]))})
    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report: vs_CRR={len(report['vs_CRR'])} "
          f"family={len(report['family'])}")
    for r in report["vs_CRR"]:
        print(f"  CRR {r['program_id']}: {r['structural_diffs']}")
    for r in report["family"]:
        print(f"  {r['program_id']:<26} vs {r['family']:<36} "
              f"{r['engine_structural_diff']}")


if __name__ == "__main__":
    main()
