# -*- coding: utf-8 -*-
"""CENSUS-RERUN-SINGLE-REV-001 B1 修复轮（apply_fix_rev001）。

driver: independent review CENSUS-RERUN-SINGLE-REV-001（verdict=ARTIFACT_REVISE）B1 blocker
——C7 GUARD_ANCHOR_TIERED_COMBINE_CHAIN 4 成员面错配（栖息面原程序被 §2.2 护巢面新程序
顶替 + 零披露 + 守恒破坏）；修复指令=Coordinator。链形论证本身经独立审确认无瑕，零改动。

修复内容（三件事 + 记账 + 披露）：
 1) 从 4 个表达文件 §2.4 NormalFeeding（栖息面）补录正确面重跑盲体 ×4
    （P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE；FIX 非盲补录范式 CENSUS-B0-FIX-001：
    registry_seen_at_creation=true + program_revisions 留痕 + manifest bias_declaration 补段），
    并 engine 实跑判同（vs registry v8 各相关族 canonical + C9 新簇直验）。
 2) §2.2 护巢面 4 程序（P-RS1-BLU/ARA/RBP/HNC-BAKE）改记新增（+4 名义）：rerun_of=null
    + program_revisions PROVENANCE_REWRITTEN；B1-B4 栖息面原程序维持 SINGLE
    moved_pending_review（归宿挂 §2.4 重跑结果，HRQ-RS1-01/05 联动）。
 3) 记账：名义 162 -> 162+4=166 pending HRQ；HRQ-RS1-01 拆分名单补正；curve RS1 行按实修正
    （dL_bake=+9 按修复指令冻结——C9 候选计入挂 HRQ-RS1-05 开放问题）。
 4) 披露：manifest bias_declaration 补「C7 面错配修复轮」全段（含对照表）；M2 同步
    build_census_outputs.py 内嵌 manifest 模板（registry_opened_at 声明性弱化版，
    文本自本模块 MANIFEST_FINAL 导入，防幂等重跑回退）。

幂等性：blind/merge_tests/stories 为 guarded append；programs/HRQ/manifest/curve/
program_revisions 为确定性重写（重复执行结果不变，除首次落盘的 date_applied 时间戳沿用）。
"""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent
CENSUS = BATCH.parents[1]
CURVE = CENSUS / "discovery_curve.csv"
RP1_BLIND = BATCH.parent / "CENSUS-RERUN-PLAIN-001" / "blind_programs.jsonl"

FIX_ID = "CENSUS-RERUN-SINGLE-REV-001"

# ---------------------------------------------------------------------------
# 面错配对照表（独立审 B1 blocker 实证；manifest bias_declaration 全段引用）
# ---------------------------------------------------------------------------
FACE_MISMATCH_TABLE = [
    # rerun 体（实取 §2.2 护巢面）, rerun_of 原程序（栖息面）, 正确对应面（本修复轮补录）
    ("P-RS1-BLU-BAKE", "P-B1-BLU-BAKE", "「季节性水层变化：水层因子评估→归一化」（CENSUS-B1/blind_programs.jsonl 行 15）",
     "bluegill.md §2.4 NormalFeeding（行 171）", "P-RS1-BLU-HAB-BAKE"),
    ("P-RS1-ARA-BAKE", "P-B3-ARA-BAKE", "「洪水周期阶段重排：低产卵场→洪泛平原→干季湖」（CENSUS-B3 行 23）",
     "arapaima.md §2.4（行 182）", "P-RS1-ARA-HAB-BAKE"),
    ("P-RS1-RBP-BAKE", "P-B3-RBP-BAKE", "「植被区结构因子（静态）→归一化」（CENSUS-B3 行 27）",
     "red_bellied_piranha.md §2.4（行 170）", "P-RS1-RBP-HAB-BAKE"),
    ("P-RS1-HNC-BAKE", "P-B4-HNC-BAKE", "「岩池小河清水静态分布。静态栖息单因子，无判断链」（CENSUS-B4 行 45）",
     "hornyhead_chub.md §2.4（行 176）", "P-RS1-HNC-HAB-BAKE"),
]

# rerun_of 正确映射（栖息面原程序 -> 补录承载），及护巢面新增注记用物种事实
HAB_SPECIES = {
    "BLU": {
        "orig": "P-B1-BLU-BAKE", "species": "Bluegill Sunfish（蓝鳃太阳鱼）",
        "profile": "@BluegillNormalLayerProfile", "anchor": "benthopelagic 软定位（近底带/中间水层/远底带——[需正文：硬定位与否]）",
        "phase": "晨昏活跃（@BluegillNormalTimeProfile 值域承载）", "file": "bluegill.md", "guard_group": "Guarding"},
    "ARA": {
        "orig": "P-B3-ARA-BAKE", "species": "Arapaima（巨骨舌鱼）",
        "profile": "@ArapaimaNormalLayerProfile", "anchor": "demersal 硬定位（底层/近底带/远底层）",
        "phase": "晨昏活跃（@ArapaimaNormalTimeProfile 值域承载）", "file": "arapaima.md", "guard_group": "BroodCare"},
    "RBP": {
        "orig": "P-B3-RBP-BAKE", "species": "Red-bellied Piranha（红腹食人鱼）",
        "profile": "@PiranhaNormalLayerProfile", "anchor": "pelagic 软定位（中上开阔水层/近结构沿岸/排除——[需正文：定位档成员]）",
        "phase": "全天活跃（@PiranhaNormalTimeProfile 值域承载）", "file": "red_bellied_piranha.md", "guard_group": "Guarding"},
    "HNC": {
        "orig": "P-B4-HNC-BAKE", "species": "Hornyhead Chub（双点美鱥）",
        "profile": "@HornyheadNormalLayerProfile", "anchor": "demersal 硬定位（底层/近底带/远底层）",
        "phase": "早晨活跃（@HornyheadNormalTimeProfile 值域承载）", "file": "hornyhead_chub.md", "guard_group": "Guarding"},
}

C9_FAMILY = "ORDERED_QUAD_TIER_COMBINE_CHAIN"
C9_CLUSTER = "C9_NORMAL_QUAD_TIER"
HAB_PREMISE = ("普通摄食期 NormalFeeding Group 激活（与 Guarding/BroodCare Group 的切换="
               "condition premise，路由面判定——body 不设分支）")

# 4 个 §2.4 链形全部同构：水层定位三档（IF3_EXIT）→ 结构三档 → 水温三档 → 时段三档
# → 合并（COMBINE_WEIGHTED 算子 UNDEFINED 待机制侧——live §15.2 M0 占位声明原样，
#   与 RP1 P-RP1-OSC-BAKE 同源 BA-T1 终步处理一致）→ SpatialDistributionWeight。
# 软/硬定位差异=Profile 档位成员归属（instance_noise/open_semantics），非 branch 结构差异
# （BSK C5b 注记同型）；活动节律=TimeProfile 值域承载非 branch。
C9_STEPS = [
    {"op": "EVAL_TYPED_FIELD_OR_FACTOR", "deps": []},
    {"op": "EVAL_TYPED_FIELD_OR_FACTOR", "deps": []},
    {"op": "EVAL_TYPED_FIELD_OR_FACTOR", "deps": []},
    {"op": "EVAL_TYPED_FIELD_OR_FACTOR", "deps": []},
    {"op": "COMBINE_WEIGHTED", "deps": [0, 1, 2, 3]},
]
C9_BRANCHES = [
    {"kind": "IF3_EXIT", "guard": "layer_position_tier"},
    {"kind": "IF3_EXIT", "guard": "structure_tier"},
    {"kind": "IF3_EXIT", "guard": "temperature_tier"},
    {"kind": "IF3_EXIT", "guard": "time_of_day_tier"},
]


def hab_blind_entry(code, sp):
    sketch = (
        "【修复轮补录盲体｜REV-001 B1｜§2.4 NormalFeeding 栖息面重跑】判断链=水层定位三档（" +
        sp["anchor"] + "）→ 结构三档 → 水温三档（排除档边界参考 TempFloor——「末位算术门」还原为链中档位判定）"
        "→ 时段三档（" + sp["phase"] + "）→ 合并（COMBINE_WEIGHTED 算子 OPERATOR UNDEFINED 待机制侧——"
        "BA-T1 因子合并算子，live §15.2 M0 同款占位声明，不因链序还原而隐式定义）。"
        "实例注记：本条为面错配修复（独立审 REV-001 B1）——原重跑（P-RS1-" + code + "-BAKE）误取同文件 §2.2 " +
        sp["guard_group"] + " 护巢面；本条为 " + sp["orig"] + "（栖息面原程序）的正确面重跑承载。"
        "链形转写自 guarding/species/" + sp["file"] + " §2.4（REP-ORDER-FIX-002；文件冻结输入，"
        "WORKING/NOT AUTHORITY；档位成员=Profile 值域不冻结 [需正文]，Story 正文到达后校准——"
        "顺序/档位差异本身=LogicTemplate 判据）。修复轮创建时 registry 已读（FIX 非盲补录——"
        "manifest bias_declaration 补段声明）。")
    body = {
        "program_id": f"P-RS1-{code}-HAB-BAKE",
        "story_id": f"CENSUS-RERUN-SINGLE-001-{code}-HAB",
        "species_id": code,
        "surface": "Bake",
        "incoming_premises": [HAB_PREMISE],
        "human_readable_sketch": sketch,
        "ordered_steps": C9_STEPS,
        "branches": C9_BRANCHES,
        "combine": "WEIGHTED_UNDEFINED",
        "return_type": "SpatialDistributionWeight",
        "instance_noise": {"species": sp["species"], "profile": sp["profile"], "constants": {}},
        "helpers": [],
        "source_evidence_ids": [f"outputs/full_authoring/guarding/species/{sp['file']}#REP-ORDER-FIX-002 §2.4 NormalFeeding"],
        "open_semantics": [
            "档位成员与阈值=Profile 值域不冻结 [需正文]（水层定位档成员含软/硬定位归属 [需正文：硬定位与否]——C5b BSK 同型注记）",
            "顺序还原=物种属性锚方向级推导（Tier B：水层定位软/硬与活动节律由 CSV 属性锚承载），Story 正文到达后校准",
            "证据分层：表达文件 §2.4 投影（四因子有序链）vs census B1-B4 story 证据（栖息单因子 SINGLE）来源分歧——挂 HRQ-RS1-01/05（C8 同型不静默归并）",
        ],
        "cluster_hint_blind": C9_CLUSTER,
        "registry_seen": True,
        "registry_seen_at_creation": True,   # FIX 非盲补录范式（B0-FIX-001）
        "fix_round": FIX_ID,
    }
    body["blind_hash"] = hashlib.sha256(
        json.dumps({k: body[k] for k in ("ordered_steps", "branches", "combine",
                                         "return_type", "incoming_premises")},
                   ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:16]
    return body


# ---------------------------------------------------------------------------
# registry v8 相关族 canonical IR（比较用逐字来源：run_merge_tests.py 内嵌 canonical
# 或各批冻结体直读——RP1 跨批复用范式）
# ---------------------------------------------------------------------------
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


def canon_of(source, cluster_label):
    """canonical = 源成员冻结体逐字（program_id 改写；STATE_GATED 物化先例）。"""
    body = {k: source[k] for k in ("program_id", "surface", "incoming_premises",
                                   "ordered_steps", "branches", "combine",
                                   "return_type", "instance_noise")}
    body["program_id"] = f"TEMPLATE::{cluster_label}::CANONICAL_SOURCE"
    return body


def load_blind(path):
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def write_jsonl(path, rows):
    path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                    encoding="utf-8")


def main():
    applied_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # 已应用则沿用原 date_applied（幂等重入；剥离 YAML 引号防双重引号损坏）
    existing_manifest = (BATCH / "manifest.yaml").read_text(encoding="utf-8")
    if "date_applied:" in existing_manifest and "@APPLIED_AT@" not in existing_manifest:
        for line in existing_manifest.splitlines():
            if line.strip().startswith("date_applied:"):
                applied_at = line.split(":", 1)[1].strip().strip('"')
                break

    # ---------------- 1) blind_programs.jsonl：guarded append ×4 ----------------
    blind = load_blind(BATCH / "blind_programs.jsonl")
    assert len(blind) in (61, 65), len(blind)
    hab_bodies = {code: hab_blind_entry(code, sp) for code, sp in HAB_SPECIES.items()}
    if len(blind) == 61:
        blind.extend(hab_bodies[c] for c in ("BLU", "ARA", "RBP", "HNC"))
        write_jsonl(BATCH / "blind_programs.jsonl", blind)
        print("blind_programs: 61 -> 65 (append P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE)")
    else:
        # 幂等重入：以磁盘上已冻结的补录体为准（不重写，保 frozen 语义）
        hab_bodies = {p["species_id"]: p for p in blind if p.get("fix_round") == FIX_ID}
        assert len(hab_bodies) == 4
        print("blind_programs: already 65 (idempotent re-entry)")
    progs_idx = {p["program_id"]: p for p in blind}

    # ---------------- 2) engine 实跑（修复轮判同） ----------------
    soft_triple_canon = canon_of(progs_idx["P-RS1-BSK-BAKE"], "SOFT_TRIPLE_TIER_CHAIN")
    rp1 = {p["program_id"]: p for p in load_blind(RP1_BLIND)}
    extreme_temp_canon = canon_of(rp1["P-RP1-OSC-BAKE"], "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN")
    guard_anchor_canon = canon_of(progs_idx["P-RS1-BLU-BAKE"], "GUARD_ANCHOR_TIERED_COMBINE_CHAIN")
    c9_canon = canon_of(hab_bodies["BLU"], C9_CLUSTER)

    hab_order = ["BLU", "ARA", "RBP", "HNC"]
    report = {
        "fix_round": FIX_ID,
        "canon": {
            C9_FAMILY: "P-RS1-BLU-HAB-BAKE（本修复轮冻结体）",
            "SOFT_TRIPLE_TIER_CHAIN": "P-RS1-BSK-BAKE（RS1 冻结体直读）",
            "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": "P-RP1-OSC-BAKE（RP1 冻结体跨批直读）",
            "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": "P-RS1-BLU-BAKE（RS1 冻结体直读）",
            "SINGLE_FACTOR_NORMALIZED_WEIGHT / PLAIN_FACTOR_COMBINE / CRR": "run_merge_tests.py 内嵌 canonical 同文",
        },
        "hab_vs_single": [], "c9_cluster_membership": [],
        "hab_vs_soft_triple": [], "hab_vs_extreme_temp": [],
        "hab_vs_guard_anchor": [], "hab_vs_plain": [], "hab_vs_crr": [],
    }
    for code in hab_order:
        p = hab_bodies[code]
        report["hab_vs_single"].append(
            {"program_id": p["program_id"], "structural_diffs": sorted(structural_diff(p, SINGLE_IR))})
        report["c9_cluster_membership"].append(
            {"program_id": p["program_id"],
             "role": "canonical_source_selftest" if code == "BLU" else "member_direct_test",
             "engine_structural_diff": sorted(structural_diff(p, c9_canon))})
        for key, canon in (("hab_vs_soft_triple", soft_triple_canon),
                           ("hab_vs_extreme_temp", extreme_temp_canon),
                           ("hab_vs_guard_anchor", guard_anchor_canon),
                           ("hab_vs_plain", PLAIN_IR), ("hab_vs_crr", CRR_IR)):
            report[key].append(
                {"program_id": p["program_id"], "structural_diffs": sorted(structural_diff(p, canon))})
    (BATCH / "engine_report_rev001.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    for key in ("hab_vs_single", "c9_cluster_membership", "hab_vs_soft_triple",
                "hab_vs_extreme_temp", "hab_vs_guard_anchor", "hab_vs_plain", "hab_vs_crr"):
        print(f"-- {key}:", dict(Counter(tuple(r["structural_diffs"] if "structural_diffs" in r
                                               else r["engine_structural_diff"])
                                         for r in report[key])))
    # 分组条目 uniform 断言（B5 判例③：distinct_diff_sets==1）
    for key in ("hab_vs_soft_triple", "hab_vs_extreme_temp", "hab_vs_guard_anchor",
                "hab_vs_plain", "hab_vs_crr"):
        assert len({tuple(r["structural_diffs"]) for r in report[key]}) == 1, key

    body_diff = lambda d: sorted(x for x in d if x != "PREMISE")

    # ---------------- 3) programs.jsonl：4 条护巢面改记新增 + 4 条 HAB 补录 ----------------
    programs = [json.loads(l) for l in
                (BATCH / "programs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    by_pid = {p["program_id"]: p for p in programs}
    for guard_pid, orig_pid, _orig_desc, _face, hab_pid in FACE_MISMATCH_TABLE:
        code = guard_pid.split("-")[2]
        e = by_pid[guard_pid]
        e["rerun_of"] = None
        e["fix_round"] = {
            "id": FIX_ID, "item": "B1",
            "change": ("rerun_of 链接改写：原误指 " + orig_pid + "（栖息/洄游分布面原程序）——"
                       "本程序实为表达文件 §2.2 " + HAB_SPECIES[code]["guard_group"] +
                       " 护巢面新程序（输入映射=物种名级文件扫描无面信息）；按修复指令改记新增程序"
                       "（+4 名义），不再声称继承栖息面原程序；正确面重跑承载=" + hab_pid +
                       "（§2.4）；" + orig_pid + " 维持 SINGLE moved_pending_review"
                       "（归宿挂 §2.4 重跑结果，HRQ-RS1-01/05 联动）"),
            "provenance_rewrite_recorded": "program_revisions.jsonl#" + guard_pid,
        }
        e["provenance"]["input"] = ("顺序还原后 B 系列表达文件 §2.2（REP-ORDER-FIX-001..005；"
                                    "REV-001 改记：护巢 Guard 面——面错配修复，见 fix_round）")
    if "P-RS1-BLU-HAB-BAKE" not in by_pid:
        for code in hab_order:
            sp = HAB_SPECIES[code]
            hb = hab_bodies[code]
            programs.append({
                "program_id": hb["program_id"], "story_id": hb["story_id"],
                "species_id": code, "surface": "Bake",
                "consequence": "NEW_PROGRAM_CANDIDATE",
                "family_membership": C9_FAMILY,
                "membership_status": "CANDIDATE_NEW_FAMILY",
                "review_ref": "HRQ-RS1-05",
                "blind_hash": hb["blind_hash"],
                "original_program_body_unchanged": True,
                "registry_seen_at_creation": True,
                "post_registry_mutations": [],
                "rerun_of": sp["orig"],
                "fix_round": {"id": FIX_ID, "item": "B1",
                              "change": "栖息面（§2.4 NormalFeeding）正确面重跑补录——FIX 非盲补录范式"},
                "provenance": {
                    "batch": FIX_ID,
                    "driver": "independent review CENSUS-RERUN-SINGLE-REV-001 B1（面错配）",
                    "input": f"顺序还原后表达文件 §2.4 NormalFeeding 栖息面（guarding/species/{sp['file']}#REP-ORDER-FIX-002）",
                    "bias_declaration": ("修复轮非盲补录（B0-FIX-001 范式）：创建时 registry v8 与 REV-001 结论"
                                         "已知——同构落族预期本身是被审对象；程序形状自 §2.4 伪脚本机械转写"
                                         "（四文件 §2.4 结构同构先于 registry 读取即已确立），由 reviewer 复检"),
                },
            })
        write_jsonl(BATCH / "programs.jsonl", programs)
        print(f"programs.jsonl: {len(programs)} entries（4 护巢面改记新增 + 4 HAB 补录）")
    else:
        print("programs.jsonl: fix entries already present (idempotent re-entry)")

    # ---------------- 4) merge_tests.jsonl：guarded append ×13 ----------------
    tests = [json.loads(l) for l in
             (BATCH / "merge_tests.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    if not any(isinstance(t.get("program_id"), str) and t["program_id"] == "P-RS1-BLU-HAB-BAKE"
               for t in tests):
        new_tests = []
        # A) 4 × SINGLE v1（栖息面正确重跑——61/61 论证对 4 原成员经补录后成立）
        for r in report["hab_vs_single"]:
            code = r["program_id"].split("-")[2]
            new_tests.append({
                "program_id": r["program_id"], "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
                "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
                "structural_diffs": body_diff(r["structural_diffs"]),
                "engine_raw_diffs": r["structural_diffs"],
                "reasoning": ("REV-001 B1 栖息面正确重跑承载（" + HAB_SPECIES[code]["orig"] +
                              " 的 §2.4 重跑体）：四因子有序档位链 vs v1 canonical 两步平铺 body 结构差异"
                              "（BRANCH=四步 IF3_EXIT 三档分级命中+early return；附加 OPERATOR[步数 5 vs 2]/"
                              "COMBINE[WEIGHTED_UNDEFINED vs NONE_SINGLE_CHAIN]/DEPENDENCY[终步扇入 deps]）。"
                              "SINGLE forbidden_freedoms 显式禁多因子 combine——族域违例佐证拆分非轴内差异。"
                              "原栖息面程序维持 SINGLE moved_pending_review，归宿=本重跑结果联动"
                              "（" + C9_FAMILY + " 候选）——HRQ-RS1-01 总裁决"),
                "human_review_queued": "HRQ-RS1-01",
                "provenance": {"batch": FIX_ID}})
        # B) C9 簇直验（F15：每成员直验 canonical，禁链式）
        for r in report["c9_cluster_membership"]:
            new_tests.append({
                "program_id": r["program_id"], "template_id": C9_FAMILY,
                "verdict": "MERGE_CONFIDENT", "same": True,
                "param_only": False, "structural_diffs": [],
                "engine_raw_diffs": r["engine_structural_diff"],
                "role": r["role"],
                "proposed_parameter_axis": (
                    "layer_anchor(typed: benthopelagic_soft | pelagic_soft | demersal_hard——"
                    "定位软/硬=档位成员归属轴非结构；LAYER_AXIS_DUAL_TIER 同名轴先例)"
                    "+factor_type(typed: layer_position|structure|temperature|time_of_day——"
                    "HRQ-B1-01 轴延续)+activity_phase(晨昏|全天|早晨——TimeProfile 值域承载非 branch)"),
                "reasoning": ("F15 直验（禁链式合并）：engine 零差异（四成员 body 同构——软/硬定位与"
                              "活动节律差异落 Profile 值域/instance_noise 轴非 branch/op）；跨科独立重复"
                              "（Centrarchidae/Arapaimidae/Serrasalmidae/Leuciscidae 四科四属）。"
                              "修复轮非盲（registry_seen_at_creation=true）——同构预期本身是被审对象，"
                              "由 reviewer 复检（B0-FIX-001 范式）"),
                "provenance": {"batch": FIX_ID}})
        # C) 边界证据（分组条目范式 B5 判例③：4 程序 engine diff 全一致 distinct_diff_sets=1）
        grouped = [
            ("hab_vs_soft_triple", "SOFT_TRIPLE_TIER_CHAIN",
             ("族域边界证据：三步软档链+NORMALIZE 积内归一化 vs 四步有序链+COMBINE WEIGHTED_UNDEFINED——"
              "链长差异=真结构差异（C5c ZONE_DEPTH 判例同型：步数非轴内）+终步算子差异（NORMALIZE vs COMBINE）。"
              "extend-vs-split：并入 SOFT_TRIPLE 需 +1 步并改终步=canonical 拓扑双改（F15 版本升级+全成员"
              "回归复检，含 RP1 ONS 重指派联动）；独立立族仅登记新 canonical（本批 C9 源成员冻结体），"
              "复杂度更低且与 OSC/PLAIN 边界已隔离——worker 裁 NEW"),
             "HRQ-RS1-05"),
            ("hab_vs_extreme_temp", "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN",
             ("族域边界证据：前置极值水温硬门+因子间 unordered 因子集 vs 无门有序链（水温=链中第 3 步档位"
              "判定非前置出局门）——GATE 有无=结构元素非 typed 轴；ORDER：OSC 因子序=census open_semantics "
              "unordered 原样保留 vs 本形四文件 §2.4 显式判断链序（水层→结构→水温→时段）——顺序有业务"
              "意义（early return 链先出先判）不 MERGE（F01/F11）。EXTREME_TEMP forbidden_freedoms 自声明"
              "『无门因子组合=PLAIN 域』——本形有序无门，两域均不覆盖，立 C9"),
             "HRQ-RS1-05"),
            ("hab_vs_guard_anchor", "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
             ("面级边界直证（同物种对侧）：BLU §2.2 护巢 Guard 面（锚存在门→锚适配/关系/温度档×3→合并→"
              "Guarding SpatialDistributionWeight）vs BLU §2.4 栖息面（本形：无门四因子链→分布权重）——"
              "GATE/RETURN/COMBINE/OPERATOR/DEPENDENCY 五类真差异；REV-001 B1 修复的两面即两个程序"
              "（+4 新增护巢面成员 + 4 栖息面重跑承载），面错配本身=本条边界证据的反面教训"),
             "HRQ-RS1-05"),
            ("hab_vs_plain", "PLAIN_FACTOR_COMBINE",
             ("族域边界证据：无序双槽+槽值档（slot_tiering 轨：excluded=出局槽值非 EARLY_RETURN）vs 有序"
              "四步链+EXIT 档（excluded=EARLY_RETURN）——槽间 unordered 契约（HRQ-07）与 SEQUENCE 链序为"
              "不同拓扑；C8 slot_tiering extension 轨不承载本形（C8 文件自投影维持无序，本形文件显式链序）。"
              "BRANCH（EXIT vs 无档/槽值）+OPERATOR+COMBINE 真差异"),
             "HRQ-RS1-05"),
            ("hab_vs_crr", "CONSTRAINED_RELATIVE_REFUGE",
             ("CRR non-match 续存（栖息面重跑链形仍无 RelativeRank(reference_set=FeasibleSet) 判别结构）。"
              "registry 决定沿用 RS1：同物种原程序 B1-B4 已登记 CRR known_non_matches，补录程序不重复"
              "追加名单（HRQ-RS1-04 记档）"),
             "HRQ-RS1-04"),
        ]
        for key, tpl, reasoning, hrq in grouped:
            diffs = report[key][0]["structural_diffs"]
            new_tests.append({
                "program_id": [r["program_id"] for r in report[key]],
                "n_programs": 4,
                "template_id": tpl,
                "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
                "structural_diffs": body_diff(diffs),
                "engine_raw_diffs": diffs,
                "engine_uniform": True, "distinct_diff_sets": 1,
                "reasoning": "REV-001 B1 修复轮分组条目（4 程序 engine diff 全一致）。" + reasoning,
                "human_review_queued": hrq,
                "provenance": {"batch": FIX_ID}})
        tests.extend(new_tests)
        write_jsonl(BATCH / "merge_tests.jsonl", tests)
        print(f"merge_tests.jsonl: {len(tests)} entries（+13 修复轮）")
    else:
        print("merge_tests.jsonl: fix entries already present (idempotent re-entry)")

    # ---------------- 5) stories.jsonl：guarded append ×4 + 护巢面 4 条注记 ----------------
    stories = [json.loads(l) for l in
               (BATCH / "stories.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    story_idx = {s["story_id"]: s for s in stories}
    for guard_pid, orig_pid, _d, _f, _h in FACE_MISMATCH_TABLE:
        code = guard_pid.split("-")[2]
        s = story_idx[f"CENSUS-RERUN-SINGLE-001-{code}"]
        if "fix_round" not in s:
            s["source_story"] = ("CENSUS-RERUN 单元｜REV-001 B1 改记新增（原误记 " + orig_pid +
                                 " 重跑——实为 §2.2 护巢 Guard 面新程序，非栖息面原程序重跑）｜"
                                 "输入=outputs/full_authoring/guarding/species/" +
                                 HAB_SPECIES[code]["file"] + "#REP-ORDER-FIX-002 §2.2")
            s["fix_round"] = {"id": FIX_ID, "item": "B1",
                              "change": "护巢面新程序（+4 名义）；正确面重跑单元见 CENSUS-RERUN-SINGLE-001-" + code + "-HAB"}
    if "CENSUS-RERUN-SINGLE-001-BLU-HAB" not in story_idx:
        for code in hab_order:
            sp = HAB_SPECIES[code]
            stories.append({
                "story_id": f"CENSUS-RERUN-SINGLE-001-{code}-HAB",
                "source_story": ("CENSUS-RERUN 单元｜" + sp["orig"] + " 正确面（§2.4 NormalFeeding 栖息面）"
                                 "重跑｜REV-001 B1 补录｜输入=outputs/full_authoring/guarding/species/" +
                                 sp["file"] + "#REP-ORDER-FIX-002 §2.4"),
                "frozen_patterns": ["work-standards-§5.1", "work-standards-§5.4"],
                "surfaces": {"Bake": {
                    "consequence": "NEW_PROGRAM_CANDIDATE",
                    "program_ids": [f"P-RS1-{code}-HAB-BAKE"],
                    "reason": "顺序还原链形重跑（栖息面正确承载；" + C9_FAMILY + " 候选）"}},
                "consequence": "NEW_PROGRAM_CANDIDATE",
                "fix_round": {"id": FIX_ID, "item": "B1"},
                "provenance": {"batch": FIX_ID}})
        write_jsonl(BATCH / "stories.jsonl", stories)
        print(f"stories.jsonl: {len(stories)} entries（+4 HAB 单元，4 护巢面单元注记改记）")
    else:
        print("stories.jsonl: fix entries already present (idempotent re-entry)")

    # ---------------- 6) program_revisions.jsonl（确定性重写 ×8） ----------------
    revisions = []
    for guard_pid, orig_pid, orig_desc, face, hab_pid in FACE_MISMATCH_TABLE:
        revisions.append({
            "program_id": guard_pid, "action": "PROVENANCE_REWRITTEN",
            "revision_recorded": True, "round": FIX_ID,
            "reason": ("independent review CENSUS-RERUN-SINGLE-REV-001 B1：rerun_of 面错配——原指 " +
                       orig_pid + " 为栖息面程序 " + orig_desc + "，本程序实取 §2.2 护巢 Guard 面；"
                       "改记新增程序（+4 名义），rerun_of=null"),
            "before": "rerun_of=" + orig_pid + "（重指派语义）",
            "after": ("rerun_of=null（新增程序 +4 名义）；GUARD_ANCHOR_TIERED_COMBINE_CHAIN 成员维持 4 个="
                      "本程序等 4 条护巢面程序；正确面重跑承载=" + hab_pid + "；" + orig_pid +
                      " 维持 SINGLE moved_pending_review（HRQ-RS1-01/05 联动）")})
    for code in hab_order:
        sp = HAB_SPECIES[code]
        revisions.append({
            "program_id": f"P-RS1-{code}-HAB-BAKE", "action": "ADDED_IN_FIX_ROUND",
            "revision_recorded": True, "round": FIX_ID,
            "reason": ("independent review CENSUS-RERUN-SINGLE-REV-001 B1：面错配修复——" + sp["orig"] +
                       "（栖息面）未被原重跑承载，从 " + sp["file"] + " §2.4 NormalFeeding 补录正确面重跑"),
            "before": None,
            "after": (C9_FAMILY + " 候选族成员（FIX 非盲补录 registry_seen_at_creation=true；"
                      "engine 直验簇内 4/4 零差异，vs registry v8 相关族全 body 结构差异——HRQ-RS1-05）")})
    write_jsonl(BATCH / "program_revisions.jsonl", revisions)
    print("program_revisions.jsonl: 8 entries")

    # ---------------- 7) human_review_queue.jsonl（确定性重写：RS1-01 补正 + RS1-05 新增） ----------------
    write_jsonl(BATCH / "human_review_queue.jsonl", [
        {"id": "HRQ-RS1-01",
         "topic": "SINGLE_FACTOR_NORMALIZED_WEIGHT 族拆分总裁决（受影响成员重跑）",
         "facts": ("61/66 有重跑输入成员 vs v1 canonical 全 body 结构差异（最小集 BRANCH=三档分级命中+"
                   "early return；45 例附加 GATE/OPERATOR/DEPENDENCY/COMBINE/RETURN）；SINGLE "
                   "forbidden_freedoms 显式禁 gate 与多因子 combine——族域违例佐证；5 无文件成员"
                   "（LAM/PIN/ASR/RVS/RDS）留 SINGLE pending。【REV-001 B1 补正 2026-09-11】原拆分"
                   "名单中 C7 的 4 席（BLU/ARA/RBP/HNC）作废——该 4 成员重跑体实取 §2.2 护巢面"
                   "（面错配，独立审 REV-001 实证），4 个原栖息面程序（P-B1-BLU-BAKE/P-B3-ARA-BAKE/"
                   "P-B3-RBP-BAKE/P-B4-HNC-BAKE）的正确面重跑已补录（P-RS1-*-HAB-BAKE，§2.4）——"
                   "61/61 body 差异论断经补录后对全 61 原成员成立（57 原重跑体+4 补录体）；4 原成员"
                   "归宿改为「§2.4 重跑结果联动」（" + C9_FAMILY + " 候选，HRQ-RS1-05）"),
         "decision_needed": ("①拆分处置批准：61 成员去向（9 新候选族+14 PLAIN 重归族提案——其中 4 席"
                             "由 C7 改挂 C9 联动）；②SINGLE v2 alternative：C1 TIERED_SINGLE（17 成员）"
                             "是否视为 SINGLE canonical 结构升级（v2=档位化两步）而非新族——worker 倾向 "
                             "SPLIT（45/61 非单档形，升级无法覆盖）+ C1 独立（BRANCH 真差异不 MERGE）；"
                             "③SINGLE v1 canonical 与 5 pending 成员的最终态；④REV-001 补正处置：+4 名义"
                             "（护巢面 4 程序改记新增——名义 162+4=166 pending）与 C9 联动归属批准"),
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001", "amended_by": FIX_ID}},
        {"id": "HRQ-RS1-02",
         "topic": "9 个新 Bake 候选族立族备案",
         "facts": ("TIERED_SINGLE(17)/LAYER_AXIS_DUAL_TIER(2)/GATED_COVER_TIER(12)/NOCTURNAL_"
                   "LIGHTSLOT(5)/ZONE_SUBSTRATE_RESOURCE(3)/SOFT_TRIPLE_TIER(1 PROVISIONAL)/"
                   "ZONE_DEPTH_SUBSTRATE_RESOURCE(1 PROVISIONAL)/FILTER_FIELD_ACCUMULATE(2)/"
                   "GUARD_ANCHOR_TIERED_COMBINE(4)；canonical=源成员冻结体（STATE_GATED 物化先例）；"
                   "边界证据：GATED_COVER vs HARD_GATED/PATCH、GUARD_ANCHOR vs PLAIN（RETURN/COMBINE）、"
                   "C5b/C5c vs C5a（首步软硬/链长真差异）。【REV-001 注记】GUARD_ANCHOR 4 成员 provenance "
                   "已改记新增（+4 名义；成员构成不变=4 条 §2.2 护巢面程序；链形论证经独立审确认无瑕）"),
         "decision_needed": ("①9 族立族批准（含 2 单成员 PROVISIONAL 的 extend-vs-split：C5b/C5c 对 "
                             "C5a 为 ORDER/OPERATOR 真差异，worker 裁 NEW 单成员候选非 extension）；"
                             "②gate_axis/anchor_type/factor_type 轴声明；③GUARD_ANCHOR 与 Response 面 "
                             "GUARD 族的 surface 边界确认（Bake 护巢分布 vs Response 双 Path）+ REV-001 "
                             "改记新增的 +4 名义入册"),
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001", "amended_by": FIX_ID}},
        {"id": "HRQ-RS1-03",
         "topic": "C8 14 成员 PLAIN 重归族 + slot_tiering extension 轴提案",
         "facts": ("14 追击型成员表达文件自投影=PLAIN（双槽+COMBINE_WEIGHTED，槽间 unordered 契约维持，"
                   "槽内三档=受限还原 excluded 槽值非 EARLY_RETURN）；engine raw=BRANCH/COMBINE/"
                   "DEPENDENCY/OPERATOR（槽 arity 2 在 factor_set 轴域内 B1-BRT 先例；槽名=factor_type "
                   "字面；真差异=槽内 IF3 档位）"),
         "decision_needed": ("①slot_tiering 轴批准与 PLAIN canonical v2（全库 PLAIN 投影文件已被顺序还原"
                             "统一槽内档位化——族形状问题同 SINGLE）；②证据分层裁决：表达文件投影（Tier B "
                             "[需正文]）vs census B1-B4 story 证据（单因子 SINGLE）来源分歧（14 例）；"
                             "③批准前 14 成员不计 PLAIN 正式成员（挂账）"),
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}},
        {"id": "HRQ-RS1-04",
         "topic": "重跑输入层治理与范围备案",
         "facts": ("①输入=顺序还原后 B 系列表达文件（WORKING/NOT AUTHORITY，档位成员 [需正文] 未校准"
                   "——Tier B 方向级推导）；②envelope 列 5 目录，实际受影响成员文件分布 7 目录"
                   "（guarding[FIX-002]/patch[FIX-001] 各承载 4+3 成员，已纳入——envelope URL 不全先例"
                   "记档）；③2 例文件名≠内容标题（labeo_barbel=唇䱻、northern_whiting=沙鮻）；"
                   "④CRR non-match 不重复登记决定；⑤ASR/RVS 身份待澄清（thorny_skate README §4）。"
                   "【REV-001 B1 追加】⑥guarding 目录多面承载的输入定位缺陷：物种名级文件扫描无面信息"
                   "（§2.2 护巢 vs §2.4 栖息）致 4 例面错配——修复=面显式定位（§ 节号入 source_evidence_"
                   "ids）+ 本 HRQ 治理项（RP1 HRQ-RP1-04 目录约定同源升级：节级定位约定固化）"),
         "decision_needed": "输入层缺陷修复路由（Story 正文到达后的档位校准回写机制；文件名-标题一致性清理；guarding 目录节级面定位约定固化）",
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001", "amended_by": FIX_ID}},
        {"id": "HRQ-RS1-05",
         "topic": "REV-001 修复轮备案：C9 候选族立族 + C7 面错配 provenance 改记 + 名义记账修正",
         "facts": ("①C7 面错配（独立审 REV-001 B1 实证）：GUARD_ANCHOR 4 成员 rerun_of 误指栖息面原程序"
                   "（实取 §2.2 护巢面；对照表见 manifest bias_declaration 补段）——已修复：4 程序改记"
                   "新增（+4 名义，rerun_of=null，program_revisions PROVENANCE_REWRITTEN），链形论证"
                   "无瑕维持；②栖息面正确重跑补录 4 条（P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE，§2.4，"
                   "FIX 非盲补录 registry_seen_at_creation=true）：链形=水层定位三档（软/硬定位=档位成员"
                   "归属轴）→结构三档→水温三档→时段三档→合并（UNDEFINED）——四成员 engine 零差异跨科"
                   "独立重复；③判同实测（engine_report_rev001.json）：vs SINGLE/PLAIN/CRR/SOFT_TRIPLE/"
                   "EXTREME_TEMP/GUARD_ANCHOR 全 body 结构差异→" + C9_FAMILY + " 新候选族（第 10 个，"
                   "worker 裁 NEW：vs SOFT_TRIPLE 链长+终步双差 [C5c 判例]；vs EXTREME_TEMP 门有无+"
                   "有序/无序 [GATE=结构元素非轴]；vs PLAIN/C8 有序链+EXIT vs 无序槽+槽值；vs "
                   "GUARD_ANCHOR 同物种对侧面级边界直证）；④名义 162+4=166 pending（原『162 不变』对"
                   "4 条不成立）；⑤证据分层：4 例 §2.4 投影（Tier B 四因子链）vs story 证据（栖息单因子）"
                   "来源分歧（C8 同型）"),
         "decision_needed": ("①C9 " + C9_FAMILY + " 立族批准（canonical=P-RS1-BLU-HAB-BAKE 修复轮冻结体；"
                             "layer_anchor/factor_type/activity_phase 轴声明；4 原栖息面程序重指派联动"
                             "HRQ-RS1-01）；②+4 名义（护巢面新程序入 GUARD_ANCHOR known_instances——"
                             "registry v8 现零改动，批准后另批入册）；③dL_bake 计入：修复指令冻结 RS1 行 "
                             "+9，C9 若立族则 +1 于何处计入（本行修正为 +10 或批准批次）需裁决；"
                             "④extend-vs-split 复核（vs SOFT_TRIPLE/EXTREME_TEMP 复杂度对比见 merge_tests）"),
         "provenance": {"batch": FIX_ID}},
    ])
    print("human_review_queue.jsonl: 5 entries（RS1-01/02/04 补正 + RS1-05 新增）")

    # ---------------- 8) manifest.yaml（确定性全量重写，M2 同步源） ----------------
    manifest = MANIFEST_FINAL.replace("@APPLIED_AT@", applied_at)
    (BATCH / "manifest.yaml").write_text(manifest, encoding="utf-8")
    print(f"manifest.yaml: rewritten（fix_round {FIX_ID}, applied_at={applied_at}）")

    # ---------------- 9) discovery_curve.csv：RS1 行按实修正 ----------------
    txt = CURVE.read_text(encoding="utf-8")
    lines = txt.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("CENSUS-RERUN-SINGLE-001,"):
            # 不加行内注释（保持纯 CSV）；修复说明见 manifest fix_round 与 batch_report
            lines[i] = "CENSUS-RERUN-SINGLE-001,65,65,65,14,9,0,0,9,0,0,0,0,0"
            break
    else:
        raise SystemExit("curve RS1 row not found")
    CURVE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("discovery_curve.csv: RS1 row -> 65/65/65/14/9/0/0/9 (dL_bake frozen per directive; note in manifest/report)")

    # ---------------- 对账打印 ----------------
    n_prog = len([json.loads(l) for l in
                  (BATCH / "programs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()])
    n_tests = len([json.loads(l) for l in
                   (BATCH / "merge_tests.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()])
    n_stories = len([json.loads(l) for l in
                     (BATCH / "stories.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()])
    n_blind = len(load_blind(BATCH / "blind_programs.jsonl"))
    print(f"reconcile: programs={n_prog} stories={n_stories} merge_tests={n_tests} blind={n_blind} "
          f"(expect 65/65/224/65)")


MANIFEST_FINAL = """batch_id: CENSUS-RERUN-SINGLE-001
role: FCF-CENSUS-WORKER
status: INDEPENDENT_REVIEW_REQUIRED
trigger: 用户 2026-09-11 反馈 §5.4 行动项（B 系列顺序还原 211/213 完成后，census 受影响族重跑）
scope:
  family: SINGLE_FACTOR_NORMALIZED_WEIGHT（66 成员）
  rerun_with_input: 61（B1:6 B2:8 B3:25 B4:22）
  rerun_input_unavailable: 5（LAM/PIN/ASR/RVS/RDS——absence_claims 登记）
  input_layer: 顺序还原后 B 系列表达文件 §2.2（REP-ORDER-FIX-001..005；WORKING/NOT AUTHORITY）
  input_dirs: 7（grazing/migration/normal/normal2/field/guarding/patch——envelope 列 5，
    guarding/patch 经全库 FIX 标记扫描确认纳入，HRQ-RS1-04 记档）
execution_mode: B3-F-0（fresh spawn 单轮，双时间戳+内容 hash 自证；program_revisions 原空——
  REV-001 修复轮后 8 条）
blind_discipline:
  blind_programs_frozen_at: "2026-09-11T04:39:22Z"   # 原批 61 条首冻（文件系统精确时刻，本地 12:39:22+0800）——append-only 未改写
  blind_programs_fix_appended_at: "@APPLIED_AT@"   # REV-001 追加 4 条栖息面补录（registry_seen_at_creation=true）
  n_programs: 65   # 61 原冻 + 4 修复轮补录（HAB）
  registry_opened_at: ">=2026-09-11T04:39:22Z（冻结后；权威锚=blind 文件 mtime"
    # + 本 manifest 生成时刻 git 工作树差异——opened_at 为声明性下界，不作精确时序主张）"
  post_registry_mutations: 0   # 原 61 条冻结体零改动；修复轮 4 条为新增创建（program_revisions 留痕）非 mutation
  bias_declaration: |
    事前暴露：SINGLE v1 canonical 两步形在角色记忆与 B4 批档（run_merge_tests.py
    CANONICALS——流程范式恢复时读取）中已知；本批骨架不从 canonical 反推，全部
    61 条为各文件 §2.2 顺序还原伪脚本的机械 IR 转写（文件自身即声明与 canonical
    的分歧并要求 census 侧重跑裁决——work standards §5.4）。盲重建顺序：读 61 份
    §2.2 → 转写冻结 → 开 registry。重跑语义：输入为表达文件（非 Story DB 快照），
    与 B0-B4 批的 Story 输入层不同——envelope 明示授权（ARTIFACT_URL=顺序还原后
    表达文件）。
    【REV-001 修复轮补段｜C7 面错配，2026-09-11】独立审 CENSUS-RERUN-SINGLE-REV-001
    （verdict=ARTIFACT_REVISE）B1 blocker 实证：GUARD_ANCHOR_TIERED_COMBINE_CHAIN 4 成员
    （P-RS1-BLU/ARA/RBP/HNC-BAKE）的 rerun_of 所指原 SINGLE 成员，直读 B1-B4 原盲体证实
    全部为栖息/洄游分布面程序；重跑体实际取自各表达文件 §2.2 护巢 Guard 面（返回 Guarding
    SpatialDistributionWeight）——行为面不同。佐证：tmp_chain_dump.txt 行 193（输入映射=物种名级
    文件扫描无面信息）；4 物种 census 侧原无护巢 Bake 面程序。面错配对照表（rerun 体｜误指
    原程序｜正确对应面）：
      P-RS1-BLU-BAKE（§2.2 护巢面）｜P-B1-BLU-BAKE「季节性水层变化：水层因子评估→归一化」
        （CENSUS-B1 blind 行 15）｜bluegill.md §2.4 NormalFeeding（行 171）→ P-RS1-BLU-HAB-BAKE
      P-RS1-ARA-BAKE（§2.2 护巢面）｜P-B3-ARA-BAKE「洪水周期阶段重排：低产卵场→洪泛平原→干季湖」
        （CENSUS-B3 行 23）｜arapaima.md §2.4（行 182）→ P-RS1-ARA-HAB-BAKE
      P-RS1-RBP-BAKE（§2.2 护巢面）｜P-B3-RBP-BAKE「植被区结构因子（静态）→归一化」
        （CENSUS-B3 行 27）｜red_bellied_piranha.md §2.4（行 170）→ P-RS1-RBP-HAB-BAKE
      P-RS1-HNC-BAKE（§2.2 护巢面）｜P-B4-HNC-BAKE「岩池小河清水静态分布。静态栖息单因子，无判断链」
        （CENSUS-B4 行 45）｜hornyhead_chub.md §2.4（行 176）→ P-RS1-HNC-HAB-BAKE
    修复处置（Coordinator 修复指令）：①4 个护巢面程序改记新增（+4 名义，rerun_of=null，
    program_revisions PROVENANCE_REWRITTEN ×4）；②4 个栖息面正确重跑补录（§2.4 →
    P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE；FIX 非盲补录范式 CENSUS-B0-FIX-001：创建时 registry v8
    与 REV-001 结论已知——同构落族预期本身是被审对象；程序形状自 §2.4 伪脚本机械转写，
    四文件 §2.4 结构同构事实先于 registry 读取即已确立，由 reviewer 复检）；③B1-B4 原栖息面
    程序维持 SINGLE moved_pending_review，归宿挂 §2.4 重跑结果（HRQ-RS1-01/05 联动）；
    ④名义 162 → 162+4=166 pending HRQ（原「重指派非新增」对 4 条不成立——守恒破坏修正）。
    C7 族链形同构论证经独立审确认真实无瑕（4 文件 Guard 面直验成立），本修复轮对 4 条
    护巢面盲体零改动；对照 C8 同面分歧显式挂 HRQ-RS1-03——处理梯度倒挂由本补段归零。
order_discipline: 全 61 链形按 §5.1 顺序还原形转写（ordered_steps 顺序=文件判断链顺序；
  early return/分级命中/槽语义=branches+return topology；分级命中展开为 IF3 非
  单一布尔——2026-09-11 用户新标准）；修复轮 4 条同纪律（§2.4 判断链序逐字转写，
  软/硬定位=Profile 档位成员归属非 branch 结构）
fix_round:
  id: CENSUS-RERUN-SINGLE-REV-001
  driver: independent review CENSUS-RERUN-SINGLE-REV-001 B1（verdict=ARTIFACT_REVISE；修复指令=Coordinator）
  date_applied: "@APPLIED_AT@"
  artifacts: "program_revisions 8 / merge_tests 211->224（+4 ×SINGLE、+4 C9 簇直验、+5 分组边界）/
    programs 61->65（4 护巢面改记新增+4 HAB 补录）/ stories 61->65 / blind_programs 61->65
    （append-only）/ HRQ 4->5（RS1-01/02/04 补正+RS1-05 新增）/ engine_report_rev001.json /
    batch_report+worker_self_qa 修复轮段落"
  registry: v8 零改动（+4 名义与 C9 候选族归 HRQ 批准后另批入册——章程：mutation 由独立审另批）
  m2_sync: "build_census_outputs.py 内嵌 manifest 模板 registry_opened_at 同步为磁盘声明性弱化版
    （原精确版 04:41:30Z 漂移——M2）；原批生成器加 REV-001 守卫（检测到修复已应用即拒绝执行，
    防幂等重跑回退），修复后批档终态（含本 manifest）由 apply_fix_rev001.py::MANIFEST_FINAL 持有"
verdict_counts:
  merge_confident: 65          # 61 簇内直验（原批，含 10 canonical 源自测）+ 4 C9 簇直验（修复轮）
  extension_candidate: 14      # C8 × PLAIN（slot_tiering 轴）——不变
  new_template_candidate_families: 9   # 原批 distinct 新候选族（registry template 级）
  new_template_candidate_fix_addendum: "C9 ORDERED_QUAD_TIER_COMBINE_CHAIN（修复轮实测产生，HRQ-RS1-05）——按修复指令不计入本批 dL_bake/curve RS1 行"
  ambiguous: 0
  fix_round_addendum:
    merge_confident_add: 4
    new_family_candidate_add: 1   # C9（挂 HRQ-RS1-05；dL 计入待裁决）
    nominal_programs_add: 4      # 护巢面 4 程序改记新增（162→166 pending HRQ）
deltas:
  dL_group: 0
  dL_bake: 9    # 按修复指令冻结 +9；C9 候选 +1 的计入位置挂 HRQ-RS1-05 裁决
  dL_response: 0
  dL_quality: 0
registry: v6 -> v7（原批）——REV-001 修复轮 v8 零改动（+4 名义/C9/provenance 改写均挂 HRQ 批准后另批入册）
"""


if __name__ == "__main__":
    main()
