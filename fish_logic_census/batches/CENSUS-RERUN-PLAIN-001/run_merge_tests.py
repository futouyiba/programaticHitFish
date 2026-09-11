# -*- coding: utf-8 -*-
"""CENSUS-RERUN-PLAIN-001 判同段（engine 层）。

输入：blind_programs.jsonl 9 条（已冻结 2026-09-11T05:25:21Z，registry_seen=false）。
registry v7 canonical 逐字取自各批 ir_pointer：
- PLAIN / HARD_GATED / PATCH / CRR = batches/CENSUS-B0/run_merge_tests.py::CANONICALS
  （RS1 批转写同文，v7 在案）
- GATED_COVER_TIER_CHAIN = P-RS1-FGA-BAKE / ZONE_SUBSTRATE = P-RS1-GRH-BAKE /
  ZONE_DEPTH = P-RS1-SMB-BAKE / SOFT_TRIPLE_TIER_CHAIN = P-RS1-BSK-BAKE /
  C8 归 PLAIN 提案载体 = P-RS1-TAI-BAKE ——均取自 RS1 冻结盲体逐字
新 canonical = 本批冻结盲体的 canonical-source 成员 body 逐字（STATE_GATED 物化先例）：
- HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL = P-RP1-LUN-BAKE（canonical v2 升级提案）
- EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN = P-RP1-OSC-BAKE（新候选族）
- PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN = P-RP1-BRT-BAKE（新候选族）

测试矩阵：
 A) PLAIN 原始 5（OSC/CHB/BRT/WAL/MDF）× PLAIN v1
 B) HARD_GATED 2（LUN/EEL）× HARD_GATED v1
 C) PATCH 2（MGC/ONS）× PATCH v1
 D) 直验/重归（F15）：P1 三成员（CHB/WAL/MDF）× C8 提案载体（TAI）；
    LUN × HG v2 自测；EEL × HG v2；OSC/BRT × 自族自测；
    MGC × GATED_COVER（FGA）；ONS × SOFT_TRIPLE（BSK）
 E) 边界：OSC × {HG v2, GATED_COVER, C8 载体}；BRT × {GATED_COVER, C8 载体, OSC 源}；
    LUN × GATED_COVER（v2 方向）；MGC × {HARD_GATED v1, ZONE_SUBSTRATE}；
    ONS × {ZONE_SUBSTRATE, ZONE_DEPTH}
 F) 9 × CRR（non-match 证据续存；重跑程序不重复登记 CRR 名单——HRQ-RS1-04 判例延续）
语义裁决（四态）在 build_census_outputs.py。
"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent
RS1 = BATCH.parent / "CENSUS-RERUN-SINGLE-001"

PLAIN_IR = {
    "program_id": "TEMPLATE::PLAIN_FACTOR_COMBINE", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": []},
        {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": []},
        {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": []},
        {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": []},
        {"op": "COMBINE_WEIGHTED", "deps": [0, 1, 2, 3]}],
    "branches": [], "combine": "WEIGHTED_FACTORS",
    "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}

HARD_GATED_IR = {
    "program_id": "TEMPLATE::HARD_GATED_FACTOR_COMBINE", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
        {"op": "GATE_HARD_VIABILITY", "deps": [0]},
        {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": [1]},
        {"op": "EVAL_HABITAT_FACTOR_TYPED", "deps": [1]},
        {"op": "EVAL_RESOURCE_FACTOR_TYPED", "deps": [1]},
        {"op": "COMBINE_WEIGHTED", "deps": [2, 3, 4]}],
    "branches": [{"kind": "GATE", "guard": "hard_viability",
                  "else": "exclude_from_feasible"}],
    "combine": "WEIGHTED_FACTORS", "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}

PATCH_IR = {
    "program_id": "TEMPLATE::PATCH_RESOURCE_FOLLOWING", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "EVAL_RESOURCE_PATCH", "deps": []},
        {"op": "CONSTRAIN_ZONE", "deps": [0]},
        {"op": "NORMALIZE_WEIGHT", "deps": [1]}],
    "branches": [], "combine": "NONE_SINGLE_CHAIN",
    "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}

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

# RS1 冻结盲体（canonical=源成员逐字；ir_pointer v7 在案）
rs1_progs = {p["program_id"]: p for p in
             (json.loads(line) for line in
              (RS1 / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
              if line.strip())}

# 本批冻结盲体
progs = {p["program_id"]: p for p in
         (json.loads(line) for line in
          (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
          if line.strip())}

# 本批 canonical-source 物化（STATE_GATED 物化先例：canonical 即源成员程序体；
# instance_noise 擦除为 comparison view）
NEW_FAMILY_SOURCE = {
    "HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL": "P-RP1-LUN-BAKE",
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": "P-RP1-OSC-BAKE",
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN": "P-RP1-BRT-BAKE",
}


def canon_of(source_pid, pool, cluster_key="cluster_hint_blind"):
    body = {k: pool[source_pid][k] for k in (
        "program_id", "surface", "incoming_premises", "ordered_steps",
        "branches", "combine", "return_type", "instance_noise")}
    body["program_id"] = "TEMPLATE::" + pool[source_pid][cluster_key] + "::CANONICAL_SOURCE"
    return body


def main():
    report = {"vs_plain_v1": [], "vs_hard_gated_v1": [], "vs_patch_v1": [],
              "membership": [], "boundary": [], "vs_crr": []}
    d = lambda p, t: sorted(structural_diff(p, t))

    # A/B/C) 受影响族 v1 canonical 重验
    for pid in ("P-RP1-OSC-BAKE", "P-RP1-CHB-BAKE", "P-RP1-BRT-BAKE",
                "P-RP1-WAL-BAKE", "P-RP1-MDF-BAKE"):
        report["vs_plain_v1"].append(
            {"program_id": pid, "engine_structural_diff": d(progs[pid], PLAIN_IR)})
    for pid in ("P-RP1-LUN-BAKE", "P-RP1-EEL-BAKE"):
        report["vs_hard_gated_v1"].append(
            {"program_id": pid, "engine_structural_diff": d(progs[pid], HARD_GATED_IR)})
    for pid in ("P-RP1-MGC-BAKE", "P-RP1-ONS-BAKE"):
        report["vs_patch_v1"].append(
            {"program_id": pid, "engine_structural_diff": d(progs[pid], PATCH_IR)})

    # D) 直验/重归（F15：每成员直验 canonical，禁链式）
    v2 = canon_of("P-RP1-LUN-BAKE", progs)
    report["membership"].append({
        "program_id": "P-RP1-LUN-BAKE", "family": "HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL",
        "role": "canonical_source_selftest",
        "engine_structural_diff": d(progs["P-RP1-LUN-BAKE"], v2)})
    report["membership"].append({
        "program_id": "P-RP1-EEL-BAKE", "family": "HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL",
        "role": "member_direct_test",
        "engine_structural_diff": d(progs["P-RP1-EEL-BAKE"], v2)})
    for fam, src in NEW_FAMILY_SOURCE.items():
        if src == "P-RP1-LUN-BAKE":
            continue  # 上方已录
        body = canon_of(src, progs)
        report["membership"].append({
            "program_id": src, "family": fam, "role": "canonical_source_selftest",
            "engine_structural_diff": d(progs[src], body)})
    # P1 三成员 × C8 提案载体（TAI RS1 冻结体）
    tai = canon_of("P-RS1-TAI-BAKE", rs1_progs)
    for pid in ("P-RP1-CHB-BAKE", "P-RP1-WAL-BAKE", "P-RP1-MDF-BAKE"):
        report["membership"].append({
            "program_id": pid, "family": "PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL",
            "role": "member_direct_test_vs_rs1_carrier",
            "engine_structural_diff": d(progs[pid], tai)})
    # MGC × GATED_COVER（FGA）；ONS × SOFT_TRIPLE（BSK）
    fga = canon_of("P-RS1-FGA-BAKE", rs1_progs)
    bsk = canon_of("P-RS1-BSK-BAKE", rs1_progs)
    report["membership"].append({
        "program_id": "P-RP1-MGC-BAKE", "family": "GATED_COVER_TIER_CHAIN",
        "role": "member_direct_test",
        "engine_structural_diff": d(progs["P-RP1-MGC-BAKE"], fga)})
    report["membership"].append({
        "program_id": "P-RP1-ONS-BAKE", "family": "SOFT_TRIPLE_TIER_CHAIN",
        "role": "member_direct_test",
        "engine_structural_diff": d(progs["P-RP1-ONS-BAKE"], bsk)})

    # E) 边界证据
    osc_src = canon_of("P-RP1-OSC-BAKE", progs)
    grh = canon_of("P-RS1-GRH-BAKE", rs1_progs)
    smb = canon_of("P-RS1-SMB-BAKE", rs1_progs)
    for pid, tpl, label in (
            ("P-RP1-OSC-BAKE", v2, "vs_HARD_GATED_V2"),
            ("P-RP1-OSC-BAKE", fga, "vs_GATED_COVER"),
            ("P-RP1-OSC-BAKE", tai, "vs_C8_CARRIER"),
            ("P-RP1-BRT-BAKE", fga, "vs_GATED_COVER"),
            ("P-RP1-BRT-BAKE", tai, "vs_C8_CARRIER"),
            ("P-RP1-BRT-BAKE", osc_src, "vs_OSC_SOURCE"),
            ("P-RP1-LUN-BAKE", fga, "vs_GATED_COVER"),
            ("P-RP1-MGC-BAKE", HARD_GATED_IR, "vs_HARD_GATED_V1"),
            ("P-RP1-MGC-BAKE", grh, "vs_ZONE_SUBSTRATE"),
            ("P-RP1-ONS-BAKE", grh, "vs_ZONE_SUBSTRATE"),
            ("P-RP1-ONS-BAKE", smb, "vs_ZONE_DEPTH")):
        report["boundary"].append({
            "program_id": pid, "template": label,
            "engine_structural_diff": d(progs[pid], tpl)})

    # F) 9 × CRR
    for pid in progs:
        report["vs_crr"].append(
            {"program_id": pid, "engine_structural_diff": d(progs[pid], CRR_IR)})

    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print("engine report:",
          f"plain={len(report['vs_plain_v1'])}",
          f"hg={len(report['vs_hard_gated_v1'])}",
          f"patch={len(report['vs_patch_v1'])}",
          f"membership={len(report['membership'])}",
          f"boundary={len(report['boundary'])}",
          f"crr={len(report['vs_crr'])}")
    for key in ("vs_plain_v1", "vs_hard_gated_v1", "vs_patch_v1",
                "membership", "boundary"):
        c = Counter(tuple(r["engine_structural_diff"]) for r in report[key])
        print(f"-- {key}: {dict(c)}")


if __name__ == "__main__":
    main()
