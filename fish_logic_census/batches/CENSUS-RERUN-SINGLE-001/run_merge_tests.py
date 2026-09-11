# -*- coding: utf-8 -*-
"""CENSUS-RERUN-SINGLE-001 判同段（engine 层）——原批 61 程序测试矩阵。

【REV-001 注记 2026-09-11】本脚本描述原批 engine 矩阵（A-E 段，engine_report.json）。
REV-001 修复轮（B1 面错配）新增的 4 条栖息面补录程序（P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE）
engine 判同在 apply_fix_rev001.py（engine_report_rev001.json）——不回写本脚本与本报告
（原批 61 条冻结体与测试产物零改动）。

输入：blind_programs.jsonl 61 条（已冻结 2026-09-11T04:39:22Z，registry_seen=false）。
registry v6 canonical 逐字取自各批 ir_pointer：
- SINGLE_FACTOR_NORMALIZED_WEIGHT = batches/CENSUS-B1/run_merge_tests.py::CANONICALS（B4 转写同文）
- PLAIN / HARD_GATED / PATCH = batches/CENSUS-B0/run_merge_tests.py::CANONICALS
- CRR = B4 物化文本（IR 同 v0 种子）
新簇 canonical = 本批冻结盲体的 canonical-source 成员 body 逐字（STATE_GATED 物化先例：
canonical 即源成员程序体；instance_noise 擦除为 comparison view）。

测试矩阵：
 A) 61 × SINGLE v1（受影响族重验）
 B) 61 × 自簇 canonical（F15 直验，含 10 canonical-source 自测）
 C) 14（C8）× PLAIN（重归族评估）
 D) 12（C3 门形）× HARD_GATED；2（GRB/SMA）× PATCH（族域边界证据）
 E) 61 × CRR（non-match 证据续存；重跑程序不重复登记 CRR non-match 名单——
    同物种原程序 B1-B4 已登记，registry mutation 注记）
语义裁决（四态）在 build_census_outputs.py。
"""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent

SINGLE_IR = {
    "program_id": "TEMPLATE::SINGLE_FACTOR_NORMALIZED_WEIGHT", "surface": "Bake",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "EVAL_TYPED_FIELD_OR_FACTOR", "deps": []},
        {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
    "branches": [], "combine": "NONE_SINGLE_CHAIN",
    "return_type": "SpatialDistributionWeight",
    "instance_noise": {"species": None, "profile": None, "constants": {}}}

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

# 新候选族（9 Bake 新族 + C8 归 PLAIN 提案）：canonical-source 成员（冻结盲体逐字）
NEW_FAMILY_SOURCE = {
    "TIERED_SINGLE_FACTOR_CHAIN": "P-RS1-COD-BAKE",        # C1 (17)
    "LAYER_AXIS_DUAL_TIER_CHAIN": "P-RS1-CHU-BAKE",        # C2 (2)
    "GATED_COVER_TIER_CHAIN": "P-RS1-FGA-BAKE",            # C3 (12)
    "NOCTURNAL_LIGHTSLOT_CHAIN": "P-RS1-WEL-BAKE",         # C4 (5)
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": "P-RS1-GRH-BAKE",     # C5a (3)
    "SOFT_TRIPLE_TIER_CHAIN": "P-RS1-BSK-BAKE",            # C5b (1, PROVISIONAL)
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": "P-RS1-SMB-BAKE",  # C5c (1, PROVISIONAL)
    "FILTER_FIELD_ACCUMULATE_CHAIN": "P-RS1-BHC-BAKE",     # C6 (2)
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": "P-RS1-BLU-BAKE", # C7 (4)
    "PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL": "P-RS1-TAI-BAKE",  # C8 (14) 归 PLAIN 提案载体
}

CLUSTER_OF = {}  # program_id -> cluster hint（自冻结盲体的 cluster_hint_blind 字段）
progs = {p["program_id"]: p for p in
         (json.loads(line) for line in
          (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
          if line.strip())}
for p in progs.values():
    CLUSTER_OF[p["program_id"]] = p["cluster_hint_blind"]

CLUSTER_TO_FAMILY = {
    "C1_TIERED_SINGLE": "TIERED_SINGLE_FACTOR_CHAIN",
    "C2_DUAL_TIER": "LAYER_AXIS_DUAL_TIER_CHAIN",
    "C3_GATED_TIER": "GATED_COVER_TIER_CHAIN",
    "C4_NOCTURNAL": "NOCTURNAL_LIGHTSLOT_CHAIN",
    "C5a_ZONE_SUBSTRATE": "ZONE_SUBSTRATE_RESOURCE_CHAIN",
    "C5b_TRIPLE_SOFT": "SOFT_TRIPLE_TIER_CHAIN",
    "C5c_ZONE_DEPTH": "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN",
    "C6_FILTER_FIELD": "FILTER_FIELD_ACCUMULATE_CHAIN",
    "C7_GUARD_ANCHOR": "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
    "C8_PLAIN_DUALSLOT": "PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL",
}


def canon_of(source_pid):
    body = {k: progs[source_pid][k] for k in (
        "program_id", "surface", "incoming_premises", "ordered_steps",
        "branches", "combine", "return_type", "instance_noise")}
    body["program_id"] = "TEMPLATE::" + CLUSTER_OF[source_pid] + "::CANONICAL_SOURCE"
    return body


def main():
    report = {"family_vs_single": [], "cluster_membership": [], "c8_vs_plain": [],
              "boundary_vs_hard_gated": [], "boundary_vs_patch": [], "vs_crr": []}
    for pid, p in progs.items():
        report["family_vs_single"].append(
            {"program_id": pid, "structural_diffs": sorted(structural_diff(p, SINGLE_IR))})
        report["vs_crr"].append(
            {"program_id": pid, "structural_diffs": sorted(structural_diff(p, CRR_IR))})
    # 簇 canonical 直验（F15：每成员直验 canonical，禁链式）
    canonical_bodies = {}
    for fam, src in NEW_FAMILY_SOURCE.items():
        canonical_bodies[fam] = canon_of(src)
        report["cluster_membership"].append({
            "program_id": src, "family": fam, "role": "canonical_source_selftest",
            "engine_structural_diff": sorted(
                structural_diff(progs[src], canonical_bodies[fam]))})
    for pid, p in progs.items():
        fam = CLUSTER_TO_FAMILY[CLUSTER_OF[pid]]
        if pid in NEW_FAMILY_SOURCE.values():
            continue  # source 自测已录
        report["cluster_membership"].append({
            "program_id": pid, "family": fam, "role": "member_direct_test",
            "engine_structural_diff": sorted(
                structural_diff(p, canonical_bodies[fam]))})
    # C8 × PLAIN
    for pid, p in progs.items():
        if CLUSTER_OF[pid] == "C8_PLAIN_DUALSLOT":
            report["c8_vs_plain"].append({
                "program_id": pid,
                "engine_structural_diff": sorted(structural_diff(p, PLAIN_IR))})
    # 边界：C3 门形 × HARD_GATED；GRB/SMA × PATCH
    for pid, p in progs.items():
        if CLUSTER_OF[pid] == "C3_GATED_TIER":
            report["boundary_vs_hard_gated"].append({
                "program_id": pid,
                "engine_structural_diff": sorted(structural_diff(p, HARD_GATED_IR))})
            if pid in ("P-RS1-GRB-BAKE", "P-RS1-SMA-BAKE"):
                report["boundary_vs_patch"].append({
                    "program_id": pid,
                    "engine_structural_diff": sorted(structural_diff(p, PATCH_IR))})
    (BATCH / "engine_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print("engine report:",
          f"vs_single={len(report['family_vs_single'])}",
          f"cluster={len(report['cluster_membership'])}",
          f"c8_vs_plain={len(report['c8_vs_plain'])}",
          f"vs_hard_gated={len(report['boundary_vs_hard_gated'])}",
          f"vs_patch={len(report['boundary_vs_patch'])}",
          f"vs_crr={len(report['vs_crr'])}")
    # 汇总打印
    from collections import Counter
    for key in ("family_vs_single", "cluster_membership", "c8_vs_plain",
                "boundary_vs_hard_gated", "boundary_vs_patch"):
        c = Counter(tuple(sorted(r.get("engine_structural_diffs",
                                       r.get("engine_structural_diff", []))))
                    for r in report[key])
        print(f"-- {key}: {dict(c)}")


if __name__ == "__main__":
    main()
