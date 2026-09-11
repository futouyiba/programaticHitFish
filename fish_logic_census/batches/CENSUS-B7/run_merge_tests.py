# -*- coding: utf-8 -*-
"""CENSUS-B7 判同段：盲程序 219 × registry v8 canonical（engine raw；
语义裁决在 build_census_outputs.py）。

canonical IR 来源（逐字不重造）：
- CRR / SINGLE v1 / TYPED / GUARD / STATE_GATED / FOOD_FIELD：B2/B4
  run_merge_tests.py 物化版转写（B5/B6 同源；FOOD_FIELD 为 B2 HRQ-B2-01
  立族 canonical，2 实例 BHC/HER）。
- RS1 9 新族 + RP1 2 新族：../CENSUS-RERUN-SINGLE-001 与 ../CENSUS-
  RERUN-PLAIN-001 blind_programs.jsonl 源成员冻结体直读（RP1 跨批复用范式）。
- C9 ORDERED_QUAD_TIER_COMBINE_CHAIN：../CENSUS-RERUN-SINGLE-001/
  blind_programs.jsonl P-RS1-BLU-HAB-BAKE（REV-001 修复轮冻结体）——
  **pending 候选族不在 registry v8（HRQ-RS1-05 待裁）**：同构时判 NEW/AMB
  引用 HRQ-RS1-05 联动（B6 范式 template_status 标注）。

测试矩阵（110 bake / 86 typed / 14 field / 9 guard）：
  Bake 110 vs SINGLE v1 → raw（语义 AMBIGUOUS：v1 证伪待裁 HRQ-RS1-01
       ——B5-①/B6 同态，三层联动链 +B7）
  Bake 110 vs CRR → raw（NEW non-match 第 7 批）
  Bake 110 vs 11 新族 → raw（NEW 分组）
  Bake 110 vs C9（pending）→ raw（NEW 分组+HRQ-RS1-05 联动）
  RESP 86 vs TYPED → raw（预期 MC）
  FIELD 14 vs FOOD_FIELD → raw（预期 MC——B2 族首批扩容；骨架同构单步
       场评估链，op 名字面差异）
  FIELD 14 vs TYPED → raw（族域边界互证：RETURN 硬判据——B1-LAM/B2
       BHC-RESP-FIELD 判例链）
  guard 9 vs GUARD → raw（预期 EXT——anchor 轴 7 新值候选 + 2 复现值）
  guard 9 vs STATE_GATED / TYPED → 分组互证（§9.2 拓扑边界）
  SOK2 vs STATE_GATED → 单条互证（P05 洄游停食状态门 vs 动机未定
       typed 占位——本批无 STATE_GATED 新成员的记录）
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

# ---- B2/B4 物化 canonical（B5/B6 同源逐字转写）----
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
    "FOOD_FIELD_FEEDING_RESPONSE": tpl(
        "FOOD_FIELD_FEEDING_RESPONSE", "Response", [
            ("EVAL_FOOD_FIELD_INTAKE", []), ("DECIDE_FIELD_FEEDING", [0])],
        "NONE", "Response(FieldFeeding)"),
}

# ---- RS1/RP1 新族 canonical：源成员冻结体直读（跨批复用范式）----
NEW_FAMILY_SOURCE = {
    "TIERED_SINGLE_FACTOR_CHAIN": (RS1, "P-RS1-COD-BAKE"),
    "LAYER_AXIS_DUAL_TIER_CHAIN": (RS1, "P-RS1-CHU-BAKE"),
    "GATED_COVER_TIER_CHAIN": (RS1, "P-RS1-FGA-BAKE"),
    "NOCTURNAL_LIGHTSLOT_CHAIN": (RS1, "P-RS1-WEL-BAKE"),
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": (RS1, "P-RS1-GRH-BAKE"),
    "SOFT_TRIPLE_TIER_CHAIN": (RS1, "P-RS1-BSK-BAKE"),
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": (RS1, "P-RS1-SMB-BAKE"),
    "FILTER_FIELD_ACCUMULATE_CHAIN": (RS1, "P-RS1-BHC-BAKE"),
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": (RS1, "P-RS1-BLU-BAKE"),
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": (RP1, "P-RP1-OSC-BAKE"),
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN": (RP1, "P-RP1-BRT-BAKE"),
}
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

# ---- B7 程序分组（从 blind_programs.jsonl 实测分组，不硬编码清单）----
PROGRAMS = {p["program_id"]: p for p in (
    json.loads(line) for line in
    (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip())}
BAKE_ORDER = sorted([pid for pid, p in PROGRAMS.items()
                     if p["surface"] == "Bake"])
TYPED_PIDS = sorted([pid for pid, p in PROGRAMS.items()
                     if p["return_type"] == "Response(TargetFeeding)"])
FIELD_PIDS = sorted([pid for pid, p in PROGRAMS.items()
                     if p["return_type"] == "Response(FieldFeeding)"])
GUARD_PIDS = sorted([pid for pid, p in PROGRAMS.items()
                     if "RelationalConflict" in p["return_type"]])
assert len(BAKE_ORDER) == 110 and len(TYPED_PIDS) == 86 \
    and len(FIELD_PIDS) == 14 and len(GUARD_PIDS) == 9, (
    len(BAKE_ORDER), len(TYPED_PIDS), len(FIELD_PIDS), len(GUARD_PIDS))
NEW_FAMILIES = list(NEW_FAMILY_SOURCE.keys())
C9 = "ORDERED_QUAD_TIER_COMBINE_CHAIN"


def main():
    report = {"vs_CRR": [], "vs_SINGLE": [], "vs_new_families": [],
              "vs_c9_candidate": [], "family": [], "field_vs_foodfield": [],
              "field_vs_typed": [], "guard_cross": [], "sok2_vs_state_gated": []}
    # 1) Bake 110 vs CRR
    for pid in BAKE_ORDER:
        report["vs_CRR"].append({"program_id": pid,
                                 "structural_diffs": sorted(
                                     structural_diff(PROGRAMS[pid], CRR_IR))})
    # 2) Bake 110 vs SINGLE v1
    for pid in BAKE_ORDER:
        report["vs_SINGLE"].append({
            "program_id": pid,
            "engine_structural_diff": sorted(
                structural_diff(
                    PROGRAMS[pid],
                    CANONICALS["SINGLE_FACTOR_NORMALIZED_WEIGHT"]))})
    # 3) Bake 110 vs 11 新族
    for fam in NEW_FAMILIES:
        rows = [{"program_id": pid,
                 "engine_structural_diff": sorted(
                     structural_diff(PROGRAMS[pid], CANONICALS[fam]))}
                for pid in BAKE_ORDER]
        report["vs_new_families"].append({"family": fam, "rows": rows})
    # 4) Bake 110 vs C9（pending 候选族——HRQ-RS1-05 联动）
    rows = [{"program_id": pid,
             "engine_structural_diff": sorted(
                 structural_diff(PROGRAMS[pid], CANONICALS[C9]))}
            for pid in BAKE_ORDER]
    report["vs_c9_candidate"].append({"family": C9, "rows": rows,
                                      "note": "pending candidate family "
                                              "(HRQ-RS1-05) not in registry v8"})
    # 5) typed 86 vs TYPED
    for pid in TYPED_PIDS:
        report["family"].append({
            "program_id": pid, "family": "TYPED_TARGET_RESPONSE",
            "engine_structural_diff": sorted(
                structural_diff(PROGRAMS[pid],
                                CANONICALS["TYPED_TARGET_RESPONSE"]))})
    # 6) field 14 vs FOOD_FIELD
    for pid in FIELD_PIDS:
        report["field_vs_foodfield"].append({
            "program_id": pid, "family": "FOOD_FIELD_FEEDING_RESPONSE",
            "engine_structural_diff": sorted(
                structural_diff(PROGRAMS[pid],
                                CANONICALS["FOOD_FIELD_FEEDING_RESPONSE"]))})
    # 7) field 14 vs TYPED（族域边界互证）
    rows = [{"program_id": pid,
             "engine_structural_diff": sorted(
                 structural_diff(PROGRAMS[pid],
                                 CANONICALS["TYPED_TARGET_RESPONSE"]))}
            for pid in FIELD_PIDS]
    report["field_vs_typed"].append({"family": "TYPED_TARGET_RESPONSE",
                                     "rows": rows})
    # 8) guard 9 vs GUARD
    for pid in GUARD_PIDS:
        report["family"].append({
            "program_id": pid,
            "family": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
            "engine_structural_diff": sorted(
                structural_diff(PROGRAMS[pid],
                                CANONICALS["GUARD_CONFLICT_DUAL_PATH_RESPONSE"]))})
    # 9) guard 9 跨族互证
    for fam in ("STATE_GATED_MULTI_PATH_RESPONSE", "TYPED_TARGET_RESPONSE"):
        rows = [{"program_id": pid,
                 "engine_structural_diff": sorted(
                     structural_diff(PROGRAMS[pid], CANONICALS[fam]))}
                for pid in GUARD_PIDS]
        report["guard_cross"].append({"family": fam, "rows": rows})
    # 10) SOK2 vs STATE_GATED（单条互证）
    report["sok2_vs_state_gated"].append({
        "program_id": "P-B7-SOK2-RESP",
        "engine_structural_diff": sorted(
            structural_diff(PROGRAMS["P-B7-SOK2-RESP"],
                            CANONICALS["STATE_GATED_MULTI_PATH_RESPONSE"]))})

    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"engine report: vs_CRR={len(report['vs_CRR'])} "
          f"vs_SINGLE={len(report['vs_SINGLE'])} "
          f"vs_new_families={len(report['vs_new_families'])}x110 "
          f"vs_c9=1x110 family={len(report['family'])} "
          f"field_vs_foodfield={len(report['field_vs_foodfield'])} "
          f"field_vs_typed=1x14 guard_cross=2x9 sok2=1")
    # 摘要
    for r in report["vs_SINGLE"][:2]:
        print(f"  SINGLE {r['program_id']}: {r['engine_structural_diff']}")
    for grp in report["vs_new_families"]:
        ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
        print(f"  NEWFAM {grp['family']:<40} "
              f"distinct_diff_sets={len(ds)} sample={sorted(ds)[0]}")
    grp = report["vs_c9_candidate"][0]
    ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
    print(f"  C9CAND distinct_diff_sets={len(ds)} sample={sorted(ds)[0]}")
    for r in report["family"]:
        print(f"  FAM {r['program_id']:<20} vs {r['family']:<36} "
              f"{r['engine_structural_diff']}")
    ds = {tuple(r["engine_structural_diff"])
          for r in report["field_vs_foodfield"]}
    print(f"  FIELD vs FOOD_FIELD distinct_diff_sets={len(ds)} "
          f"samples={sorted(ds)[:3]}")
    for grp in report["field_vs_typed"]:
        ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
        print(f"  FIELD vs {grp['family']:<36} distinct={len(ds)} "
              f"sample={sorted(ds)[0]}")
    for grp in report["guard_cross"]:
        ds = {tuple(r["engine_structural_diff"]) for r in grp["rows"]}
        print(f"  CROSS {grp['family']:<36} distinct_diff_sets={len(ds)} "
              f"sample={sorted(ds)[0]}")
    print(f"  SOK2 vs STATE_GATED: "
          f"{report['sok2_vs_state_gated'][0]['engine_structural_diff']}")


if __name__ == "__main__":
    main()
