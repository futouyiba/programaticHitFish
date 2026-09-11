# -*- coding: utf-8 -*-
"""CENSUS-B6 判同段：盲程序 94 × registry v8 canonical（engine raw；
语义裁决在 build_census_outputs.py）。

canonical IR 来源（逐字不重造）：
- CRR / SINGLE v1 / TYPED / GUARD / STATE_GATED：B4 run_merge_tests.py
  CANONICALS 物化版转写（B5 同源转写；STATE_GATED 为 B3-F-2 物化）。
- RS1 9 新族：../CENSUS-RERUN-SINGLE-001/blind_programs.jsonl 源成员冻结体
  直读（RP1 跨批复用范式）。
- RP1 2 新族：../CENSUS-RERUN-PLAIN-001/blind_programs.jsonl 源成员直读。
- C9 ORDERED_QUAD_TIER_COMBINE_CHAIN：../CENSUS-RERUN-SINGLE-001/
  blind_programs.jsonl P-RS1-BLU-HAB-BAKE（REV-001 修复轮冻结体；RS1 merge_
  tests canonical_source_selftest 角色）——**pending 候选族不在 registry v8
  （HRQ-RS1-05 待裁）**：envelope 指示 R10 程序与其链形同构时判 NEW/AMB 需
  引用 HRQ-RS1-05 联动，不当成 registry 族。

测试矩阵：
  Bake  47 vs SINGLE v1 → raw（语义 AMBIGUOUS：v1 canonical 经 RS1 61/61 证伪
       待裁决 HRQ-RS1-01——B5-① 范式沿用）
  Bake  47 vs CRR → raw（NEW non-match，B0-B5 连续回落测试第 6 批）
  Bake  47 vs 11 新族（RS1 9+RP1 2）→ raw（NEW 分组：平链 vs 档位/门/链形）
  Bake  47 vs C9（pending 候选族）→ raw（NEW 分组+HRQ-RS1-05 联动）
  RESP  45 vs TYPED → raw（预期 MC）
  RESP  2 guard vs GUARD → raw（预期 EXT——AWF/LFB 守护对象新值与 B5 anchor
       轴系联动）
  guard  2 vs STATE_GATED → 分组互证（§9.2 两拓扑边界）
  guard  2 vs TYPED → 分组互证（单路径边界）
"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent
RS1 = BATCH.parent / "CENSUS-RERUN-SINGLE-001"
RP1 = BATCH.parent / "CENSUS-RERUN-PLAIN-001"

# ---- B4 物化 canonical（B5 同源逐字转写）----
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
    "SINGLE_FACTOR_NORMALIZED_WEIGHT": tpl(
        "SINGLE_FACTOR_NORMALIZED_WEIGHT", "Bake", [
            ("EVAL_TYPED_FIELD_OR_FACTOR", []), ("NORMALIZE_WEIGHT", [0])],
        "NONE_SINGLE_CHAIN", "SpatialDistributionWeight"),
    "TYPED_TARGET_RESPONSE": tpl(
        "TYPED_TARGET_RESPONSE", "Response", [
            ("EVAL_TARGET_AS_FOOD_TYPED", []), ("DECIDE_RESPONSE", [0])],
        "NONE", "Response(TargetFeeding)"),
    "GUARD_CONFLICT_DUAL_PATH_RESPONSE": tpl(
        "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "Response", [
            ("EVAL_TARGET_AS_FOOD_TYPED", []),
            ("EVAL_TARGET_AS_INTRUDER_TYPED", []),
            ("COMBINE_DUAL_PATH", [0, 1]),
            ("DECIDE_RESPONSE", [2])],
        "DUAL_PATH_MERGE", "Response(TargetFeeding | RelationalConflict)",
        premises=["guard_state = ACTIVE (persistent condition premise)"]),
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

# ---- RS1/RP1 新族 canonical：源成员冻结体直读（跨批复用范式）----
NEW_FAMILY_SOURCE = {
    # RS1（batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE）
    "TIERED_SINGLE_FACTOR_CHAIN": (RS1, "P-RS1-COD-BAKE"),
    "LAYER_AXIS_DUAL_TIER_CHAIN": (RS1, "P-RS1-CHU-BAKE"),
    "GATED_COVER_TIER_CHAIN": (RS1, "P-RS1-FGA-BAKE"),
    "NOCTURNAL_LIGHTSLOT_CHAIN": (RS1, "P-RS1-WEL-BAKE"),
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": (RS1, "P-RS1-GRH-BAKE"),
    "SOFT_TRIPLE_TIER_CHAIN": (RS1, "P-RS1-BSK-BAKE"),
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": (RS1, "P-RS1-SMB-BAKE"),
    "FILTER_FIELD_ACCUMULATE_CHAIN": (RS1, "P-RS1-BHC-BAKE"),
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": (RS1, "P-RS1-BLU-BAKE"),
    # RP1（batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE）
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": (RP1, "P-RP1-OSC-BAKE"),
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN": (RP1, "P-RP1-BRT-BAKE"),
}
# C9 pending 候选族（HRQ-RS1-05；不在 registry v8）——源=P-RS1-BLU-HAB-BAKE
# （REV-001 修复轮冻结体，RS1 canonical_source_selftest 角色）
C9_CANDIDATE_SOURCE = (RS1, "P-RS1-BLU-HAB-BAKE")


def load_source(batch_dir, src_pid):
    pool = {p["program_id"]: p for p in (
        json.loads(l) for l in (batch_dir / "blind_programs.jsonl")
        .read_text(encoding="utf-8").splitlines() if l.strip())}
    body = {k: v for k, v in pool[src_pid].items()
            if k in ("program_id", "surface", "incoming_premises",
                     "ordered_steps", "branches", "combine", "return_type",
                     "instance_noise")}
    return body


for fam, (batch_dir, src_pid) in NEW_FAMILY_SOURCE.items():
    body = load_source(batch_dir, src_pid)
    body["program_id"] = f"TEMPLATE::{fam}"
    CANONICALS[fam] = body

_c9 = load_source(*C9_CANDIDATE_SOURCE)
_c9["program_id"] = "TEMPLATE::ORDERED_QUAD_TIER_COMBINE_CHAIN"
CANONICALS["ORDERED_QUAD_TIER_COMBINE_CHAIN"] = _c9

BAKE_ORDER = ["SUK", "GRK", "KHK", "OGK", "LCP", "AMC", "HFC", "ASC",
              "WCC", "AGC", "WS2", "WAG", "HYS", "ACA", "ATC", "AWF",
              "PSH", "LFB", "BMB", "PLC", "SSM", "CGD", "GDB", "RBD",
              "RUF", "DBC", "JSB", "ASB", "DCL", "BHM", "WHC", "PRB",
              "RSS", "PCC", "STS", "PKC", "BCF", "TGS", "EUP", "BTS",
              "GDS", "SLM", "PKS", "BLT", "RSC", "BBH", "AMN"]  # 47
GUARD_2 = ["AWF", "LFB"]
TYPED_45 = [s for s in BAKE_ORDER if s not in GUARD_2]  # 45
NEW_FAMILIES = list(NEW_FAMILY_SOURCE.keys())  # 11
C9 = "ORDERED_QUAD_TIER_COMBINE_CHAIN"


def main():
    programs = {p["program_id"]: p for p in
                (json.loads(line) for line in
                 (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8")
                 .splitlines() if line.strip())}
    report = {"vs_CRR": [], "vs_SINGLE": [], "vs_new_families": [],
              "vs_c9_candidate": [], "family": [], "guard_cross": []}
    # 1) Bake 47 vs CRR
    for sid in BAKE_ORDER:
        pid = f"P-B6-{sid}-BAKE"
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(
                                     structural_diff(programs[pid], CRR_IR))})
    # 2) Bake 47 vs SINGLE v1
    for sid in BAKE_ORDER:
        pid = f"P-B6-{sid}-BAKE"
        report["vs_SINGLE"].append({
            "program_id": pid,
            "engine_structural_diff": sorted(
                structural_diff(programs[pid],
                                CANONICALS["SINGLE_FACTOR_NORMALIZED_WEIGHT"]))})
    # 3) Bake 47 vs 11 新族（逐程序实测；分组条目在 build_census_outputs）
    for fam in NEW_FAMILIES:
        rows = []
        for sid in BAKE_ORDER:
            pid = f"P-B6-{sid}-BAKE"
            rows.append({"program_id": pid,
                         "engine_structural_diff": sorted(
                             structural_diff(programs[pid], CANONICALS[fam]))})
        report["vs_new_families"].append({"family": fam, "rows": rows})
    # 4) Bake 47 vs C9（pending 候选族——HRQ-RS1-05 联动）
    rows = []
    for sid in BAKE_ORDER:
        pid = f"P-B6-{sid}-BAKE"
        rows.append({"program_id": pid,
                     "engine_structural_diff": sorted(
                         structural_diff(programs[pid], CANONICALS[C9]))})
    report["vs_c9_candidate"].append({"family": C9, "rows": rows,
                                      "note": "pending candidate family "
                                              "(HRQ-RS1-05) not in registry v8"})
    # 5) RESP 45 vs TYPED + guard 2 vs GUARD
    for sid in TYPED_45:
        pid = f"P-B6-{sid}-RESP"
        report["family"].append({
            "program_id": pid, "family": "TYPED_TARGET_RESPONSE",
            "engine_structural_diff": sorted(
                structural_diff(programs[pid],
                                CANONICALS["TYPED_TARGET_RESPONSE"]))})
    for sid in GUARD_2:
        pid = f"P-B6-{sid}-RESP"
        report["family"].append({
            "program_id": pid, "family": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
            "engine_structural_diff": sorted(
                structural_diff(programs[pid],
                                CANONICALS["GUARD_CONFLICT_DUAL_PATH_RESPONSE"]))})
    # 6) guard 2 跨族互证（STATE_GATED / TYPED）
    for fam in ("STATE_GATED_MULTI_PATH_RESPONSE", "TYPED_TARGET_RESPONSE"):
        rows = []
        for sid in GUARD_2:
            pid = f"P-B6-{sid}-RESP"
            rows.append({"program_id": pid,
                         "engine_structural_diff": sorted(
                             structural_diff(programs[pid], CANONICALS[fam]))})
        report["guard_cross"].append({"family": fam, "rows": rows})

    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report: vs_CRR={len(report['vs_CRR'])} "
          f"vs_SINGLE={len(report['vs_SINGLE'])} "
          f"vs_new_families={len(report['vs_new_families'])}x47 "
          f"vs_c9=1x47 family={len(report['family'])} "
          f"guard_cross={len(report['guard_cross'])}x2")
    # 摘要
    for r in report["vs_SINGLE"][:2] + report["vs_SINGLE"][-1:]:
        print(f"  SINGLE {r['program_id']}: {r['engine_structural_diff']}")
    for grp in report["vs_new_families"]:
        ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
        print(f"  NEWFAM {grp['family']:<40} "
              f"distinct_diff_sets={len(ds)} sample={sorted(ds)[0]}")
    grp = report["vs_c9_candidate"][0]
    ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
    print(f"  C9CAND {grp['family']:<40} "
          f"distinct_diff_sets={len(ds)} sample={sorted(ds)[0]}")
    for r in report["family"]:
        print(f"  {r['program_id']:<16} vs {r['family']:<36} "
              f"{r['engine_structural_diff']}")
    for grp in report["guard_cross"]:
        ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
        print(f"  CROSS {grp['family']:<36} distinct_diff_sets={len(ds)} "
              f"sample={sorted(ds)[0]}")


if __name__ == "__main__":
    main()
