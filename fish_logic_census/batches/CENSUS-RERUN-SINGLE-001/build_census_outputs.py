# -*- coding: utf-8 -*-
"""CENSUS-RERUN-SINGLE-001 语义裁决与产物装配（build_census_outputs）。

产物：programs.jsonl / merge_tests.jsonl / stories.jsonl /
absence_claims.jsonl / human_review_queue.jsonl / manifest.yaml +
仓库级 template_registry.yaml v6→v7 + discovery_curve.csv 追加行。

语义裁决（四态，worker 层）依据 engine_report.json + 判同经验判例：
- 61 × SINGLE v1：body 结构差异（BRANCH 为最小集）→ NEW_TEMPLATE_CANDIDATE
  （SINGLE forbidden_freedoms 显式禁 gate/多因子 combine——带门/多步链为族域违例，
   非轴内差异；HRQ-RS1-01）
- 簇内直验：engine PREMISE-only（F02 不计 body）或门轴字面（C3 gate_axis，
  GUARD anchor 判例）→ MERGE_CONFIDENT（语义层）
- C8 14 × PLAIN：槽 arity/槽名在 factor_set 轴内（HRQ-B1-04 先例）；
  槽内 IF3 三档=有界 typed 新轴 slot_tiering → TEMPLATE_EXTENSION_CANDIDATE
  （F14 非 plain merge；复杂度对比入条目；HRQ-RS1-03）
- C3 12 × HARD_GATED、GRB/SMA × PATCH：族域边界 non-match 证据 →
  NEW_TEMPLATE_CANDIDATE（HRQ-RS1-02 边界注记）
- 61 × CRR：non-match 续存（同物种原程序 B1-B4 已登记 CRR known_non_matches，
  重跑程序不重复追加名单——registry mutation 注记；HRQ-RS1-04）
"""
import json
import shutil
from pathlib import Path

BATCH = Path(__file__).parent
CENSUS = BATCH.parents[1]
REG = CENSUS / "template_registry.yaml"
CURVE = CENSUS / "discovery_curve.csv"

engine = json.loads((BATCH / "engine_report.json").read_text(encoding="utf-8"))
progs = {p["program_id"]: p for p in
         (json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(
             encoding="utf-8").splitlines() if l.strip())}
CLUSTER = {pid: p["cluster_hint_blind"] for pid, p in progs.items()}
FAMILY_OF = {
    "C1_TIERED_SINGLE": "TIERED_SINGLE_FACTOR_CHAIN",
    "C2_DUAL_TIER": "LAYER_AXIS_DUAL_TIER_CHAIN",
    "C3_GATED_TIER": "GATED_COVER_TIER_CHAIN",
    "C4_NOCTURNAL": "NOCTURNAL_LIGHTSLOT_CHAIN",
    "C5a_ZONE_SUBSTRATE": "ZONE_SUBSTRATE_RESOURCE_CHAIN",
    "C5b_TRIPLE_SOFT": "SOFT_TRIPLE_TIER_CHAIN",
    "C5c_ZONE_DEPTH": "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN",
    "C6_FILTER_FIELD": "FILTER_FIELD_ACCUMULATE_CHAIN",
    "C7_GUARD_ANCHOR": "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
    "C8_PLAIN_DUALSLOT": "PLAIN_FACTOR_COMBINE",
}
RERUN_OF = {  # code -> 原 SINGLE 成员程序
    "GRB": "P-B1-GRB-BAKE", "DRU": "P-B1-DRU-BAKE", "COD": "P-B1-COD-BAKE",
    "PAD34": "P-B1-PAD34-BAKE", "BLU": "P-B1-BLU-BAKE", "SMA": "P-B1-SMA-BAKE",
    "PIK19": "P-B2-PIK19-BAKE", "BRT12": "P-B2-BRT12-BAKE", "ARC": "P-B2-ARC-BAKE",
    "VEN": "P-B2-VEN-BAKE", "FGA": "P-B2-FGA-BAKE", "SWO": "P-B2-SWO-BAKE",
    "BHC": "P-B2-BHC-BAKE", "HER": "P-B2-HER-BAKE",
    "CHU": "P-B3-CHU-BAKE", "CHN": "P-B3-CHN-BAKE", "COH": "P-B3-COH-BAKE",
    "BRO": "P-B3-BRO-BAKE", "SHA": "P-B3-SHA-BAKE", "ALE": "P-B3-ALE-BAKE",
    "AST": "P-B3-AST-BAKE", "SNS": "P-B3-SNS-BAKE", "TAR": "P-B3-TAR-BAKE",
    "TAI": "P-B3-TAI-BAKE", "ARA": "P-B3-ARA-BAKE", "PB": "P-B3-PB-BAKE",
    "RBP": "P-B3-RBP-BAKE", "BLP": "P-B3-BLP-BAKE", "WEL": "P-B3-WEL-BAKE",
    "FLA": "P-B3-FLA-BAKE", "BUR": "P-B3-BUR-BAKE", "GW": "P-B3-GW-BAKE",
    "SGA": "P-B3-SGA-BAKE", "RFP": "P-B3-RFP-BAKE", "DS": "P-B3-DS-BAKE",
    "PBF": "P-B3-PBF-BAKE", "GT": "P-B3-GT-BAKE", "HAL": "P-B3-HAL-BAKE",
    "GG": "P-B3-GG-BAKE",
    "POR": "P-B4-POR-BAKE", "SDG": "P-B4-SDG-BAKE", "TSK": "P-B4-TSK-BAKE",
    "GPF": "P-B4-GPF-BAKE", "RKB": "P-B4-RKB-BAKE", "SSL": "P-B4-SSL-BAKE",
    "BSK": "P-B4-BSK-BAKE", "RRH": "P-B4-RRH-BAKE", "GRH": "P-B4-GRH-BAKE",
    "SMB": "P-B4-SMB-BAKE", "GDE": "P-B4-GDE-BAKE", "WIT": "P-B4-WIT-BAKE",
    "WIN": "P-B4-WIN-BAKE", "YTF": "P-B4-YTF-BAKE", "SMF": "P-B4-SMF-BAKE",
    "BST": "P-B4-BST-BAKE", "FDR": "P-B4-FDR-BAKE", "BSB": "P-B4-BSB-BAKE",
    "CBM": "P-B4-CBM-BAKE", "SAI": "P-B4-SAI-BAKE", "HNC": "P-B4-HNC-BAKE",
    "MOO": "P-B4-MOO-BAKE",
}
NO_FILE = {  # 5 个无重跑输入成员（原批 story 证据维持 SINGLE，flagged）
    "LAM": ("P-B1-LAM-BAKE", "海七鳃鳗——全库无表达文件（B 系列未承载）"),
    "PIN": ("P-B3-PIN-BAKE", "粉鲑——无表达文件（migration README §4 登记 3：名单未入批）"),
    "ASR": ("P-B4-ASR-BAKE", "大西洋黄貂鱼——身份待澄清（normal/thorny_skate README §4：R07『鳐』按棘背钝头鳐承载，ASR/RVS 为候选未建文件）"),
    "RVS": ("P-B4-RVS-BAKE", "眼斑河魟——同上"),
    "RDS": ("P-B4-RDS-BAKE", "小冠太阳鱼——无表达文件"),
}

CLUSTER_REASON = {
    "C1_TIERED_SINGLE": "单 typed 因子三档链（canonical 两步的档位化还原形：EVAL 展开为 IF3_EXIT 三档+early return）。17 成员三亚群（premise 轴段 10/机会 4/感官 3）IR 同构——因子维度差异落 factor_type 轴（HRQ-B1-01 轴延续）",
    "C2_DUAL_TIER": "双档链：水层带软三档→premise 轴段三档→积内归一化。与 C1 的差异=前置水层定位步（OPERATOR/DEPENDENCY 真差异，非轴内）——大马哈鱼（benthopelagic 锚）与美洲西鲱（pelagic-neritic 锚）跨科独立重复",
    "C3_GATED_TIER": "结构存在门（二元 EARLY_RETURN）+掩体/质量档三档+归一化。12 成员门轴 8 值（vegetation_edge/weedy_slack/bottom_zone×2/buryable_substrate×4/pool_structure/reef_edge/patch_presence/disturbance_window）——门轴差异=gate_axis 参数轴（GUARD anchor 判例同型），非结构差异。envelope『伏击 26 门形』在本 SINGLE 成员集内落此簇 10+patch 门 2",
    "C4_NOCTURNAL": "夜行底板档（出局）+低光槽三档（调整器语义：亮水=极低削减不清零，出局语义不落槽内）+归一化。槽位=live §11.5 判例固定。与 C1 差异=第二槽步+槽无出局语义（branch kind 真差异）",
    "C5a_ZONE_SUBSTRATE": "底带硬门+底质栖境档+资源档+积内归一化（四步）。envelope grazing 链形",
    "C5b_TRIPLE_SOFT": "近底带软三档（无硬门）+底质档+资源档（四步但首步软档非 GATE——与 C5a 结构差异）。单成员 PROVISIONAL（CSV benthopelagic 软定位推导，硬定位与否 [需正文]）",
    "C5c_ZONE_DEPTH": "底带硬门+深度档（本鱼独有步）+底质档+资源档（五步）。单成员 PROVISIONAL（CSV 深≥4m 锚；链长差异=ORDER/OPERATOR 真差异非轴内）",
    "C6_FILTER_FIELD": "滤食场三步累积链：水层档→场浓度档→个体口径档（同一场评估顺序判定，线性叠加 deps；步间折减合成算子 OPERATOR UNDEFINED 待机制侧）。与 C5b 差异=op 语义（场浓度/口径 vs 底质/资源）+线性累积 deps vs 扇入积",
    "C7_GUARD_ANCHOR": "护巢锚四评估链：锚存在门→锚适配档→关系档→温度档→合并（UNDEFINED）→Guarding SpatialDistributionWeight。返回类型与合并步=真差异（Bake 面护巢分布程序——与 Response 面 GUARD 族（∥ 双 evaluand）不同 surface 不同拓扑）。4 成员锚型=colony_nest/floodplain_fry_school/root_spawn_eggs/pebble_mound（anchor 轴第 4-7 值；pebble_mound 与 HRQ-B4-01 提案同值）",
    "C8_PLAIN_DUALSLOT": "追击型双槽+终合并（槽间 unordered 按 PLAIN 族契约）：槽内三档受限还原（excluded=出局槽值非 EARLY_RETURN——槽无 gate 语义族域边界维持）。表达文件自投影=PLAIN_FACTOR_COMBINE；与 census B1-B4 story 证据（单因子 SINGLE）来源分歧→重归族提案走 extension 轨（HRQ-RS1-03）",
}


def write_jsonl(name, rows):
    (BATCH / name).write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8")


def main():
    # ---------------- programs.jsonl ----------------
    programs = []
    for pid, p in progs.items():
        code = p["species_id"]
        fam = FAMILY_OF[CLUSTER[pid]]
        entry = {
            "program_id": pid, "story_id": p["story_id"],
            "species_id": code, "surface": "Bake",
            "consequence": "NEW_PROGRAM_CANDIDATE",
            "family_membership": fam,
            "membership_status": ("PROPOSED_PENDING_REVIEW"
                                  if fam == "PLAIN_FACTOR_COMBINE" or
                                  CLUSTER[pid] in ("C5b_TRIPLE_SOFT", "C5c_ZONE_DEPTH")
                                  else "CANDIDATE_NEW_FAMILY"),
            "review_ref": ("HRQ-RS1-03" if fam == "PLAIN_FACTOR_COMBINE"
                           else "HRQ-RS1-02"),
            "blind_hash": p["blind_hash"],
            "original_program_body_unchanged": True,
            "registry_seen_at_creation": False,
            "post_registry_mutations": [],
            "rerun_of": RERUN_OF[code],
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001",
                           "input": "顺序还原后 B 系列表达文件 §2.2（REP-ORDER-FIX-001..005）"},
        }
        programs.append(entry)
    write_jsonl("programs.jsonl", programs)

    # ---------------- merge_tests.jsonl（语义四态） ----------------
    tests = []
    body_diff = lambda d: sorted(x for x in d if x != "PREMISE")
    # A) 61 × SINGLE v1
    for r in engine["family_vs_single"]:
        pid = r["program_id"]
        fam = FAMILY_OF[CLUSTER[pid]]
        dest = ("PLAIN_FACTOR_COMBINE（重归族提案，extension 轨 HRQ-RS1-03）"
                if fam == "PLAIN_FACTOR_COMBINE" else fam + "（新候选族 HRQ-RS1-02）")
        tests.append({
            "program_id": pid, "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["structural_diffs"]),
            "engine_raw_diffs": r["structural_diffs"],
            "reasoning": ("顺序还原重跑：链形（" + CLUSTER_REASON[CLUSTER[pid]].split("。")[0] +
                          "）与 v1 canonical 两步平铺形存在 body 结构差异（最小集=BRANCH：三档分级命中+"
                          "early return 为 canonical 无有的控制流）。SINGLE forbidden_freedoms 显式禁 "
                          "gate 与多因子 combine——带门/多步/合并链为族域违例非轴内差异，不得 MERGE。"
                          "重跑处置提案：" + dest + "（HRQ-RS1-01 总裁决）"),
            "human_review_queued": "HRQ-RS1-01",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    # B) 簇内直验（F15）——C8 的簇 canonical 为提案载体（PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL，
    # canonical 源=TAI 冻结体）；与 14 × registry PLAIN v1 canonical 的 extension 评估（C 段）分记
    for r in engine["cluster_membership"]:
        pid = r["program_id"]
        fam = FAMILY_OF[CLUSTER[pid]]
        test_tpl = ("PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL"
                    if CLUSTER[pid] == "C8_PLAIN_DUALSLOT" else fam)
        raw = r["engine_structural_diff"]
        raw_note = ("canonical 源自测（engine 零差异）" if not raw else
                    ("engine raw=PREMISE（F02 activation 差异留 premise 不计 body）" if raw == ["PREMISE"] else
                     "engine raw=门轴字面（OPERATOR/BRANCH=gate_axis 值差异，GUARD anchor 判例同型；PREMISE 同前）"))
        tests.append({
            "program_id": pid, "template_id": test_tpl,
            "verdict": "MERGE_CONFIDENT", "same": True,
            "param_only": False, "structural_diffs": [], "engine_raw_diffs": raw,
            "role": r["role"],
            "proposed_parameter_axis": (
                "gate_axis(typed: vegetation_edge|weedy_slack|bottom_zone|buryable_substrate|"
                "pool_structure|reef_edge|patch_presence|disturbance_window)+factor_type(typed)+"
                "factor_binding(随 premise 切换)" if CLUSTER[pid] == "C3_GATED_TIER" else
                "factor_type(typed: premise_bound_axis|opportunity_field|sensory_signal)+"
                "factor_binding(随 premise 切换)" if CLUSTER[pid] == "C1_TIERED_SINGLE" else
                "anchor_type(typed: colony_nest|floodplain_fry_school|root_spawn_eggs|pebble_mound)"
                if CLUSTER[pid] == "C7_GUARD_ANCHOR" else
                "night_habitat_axis(typed)+lowlight_slot(live §11.5 判例原位)"
                if CLUSTER[pid] == "C4_NOCTURNAL" else
                "factor_type(typed)+factor_binding(随 premise 切换)"),
            "reasoning": ("F15 直验（禁链式合并）：" + raw_note + "；骨架同构（" +
                          CLUSTER_REASON[CLUSTER[pid]] + "）"),
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    # C) 14 × PLAIN
    for r in engine["c8_vs_plain"]:
        tests.append({
            "program_id": r["program_id"], "template_id": "PLAIN_FACTOR_COMBINE",
            "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False, "param_only": True,
            "structural_diffs": ["BRANCH"],
            "engine_raw_diffs": r["engine_structural_diff"],
            "extension_complexity_cost": (
                "+1 有界 typed 参数轴 slot_tiering(FLAT | IF3_SLOT_VALUE)（顺序还原 §5.1 对 PLAIN 槽的"
                "受限档位化：excluded=出局槽值非 EARLY_RETURN——槽无 gate 语义族域边界维持）；"
                "canonical body 拓扑零改动（槽间 unordered/终合并不变）；槽 arity 2 在 factor_set 轴声明域"
                "（2–6 槽，B1-BRT 2 槽先例 HRQ-B1-04）；槽名 EVAL_TYPED_FIELD_OR_FACTOR= factor_type 字面"),
            "new_template_complexity_cost": (
                "为槽内档位化复制整条 PLAIN 槽-组合拓扑为独立族——与 PLAIN 既有 5 成员仅差槽内 branch，"
                "且顺序还原已对全库 PLAIN 投影文件统一施加同款受限还原（族规模将全量翻倍），违反 F10/F14 节俭"),
            "recommended_shape": (
                "扩展 PLAIN：slot_tiering 轴提案挂 HRQ-RS1-03；14 重跑成员以重归族提案入账（批准前不计"
                "正式成员——HNC extension 挂账先例）。注意：本 extension 的证据源=表达文件投影（Tier B "
                "[需正文]），与 census B1-B4 story 证据（单因子 SINGLE）来源分歧——裁决时需先定证据分层"),
            "proposed_parameter_axis": "slot_tiering(FLAT | IF3_SLOT_VALUE)（NEW 轴提案）",
            "human_review_queued": "HRQ-RS1-03",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    # D) 边界证据
    for r in engine["boundary_vs_hard_gated"]:
        tests.append({
            "program_id": r["program_id"], "template_id": "HARD_GATED_FACTOR_COMBINE",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["engine_structural_diff"]),
            "engine_raw_diffs": r["engine_structural_diff"],
            "reasoning": ("族域边界证据：结构存在门+单档+归一化 vs BUILD_ACCESSIBLE_SET→hard "
                          "viability gate→多槽→COMBINE——无 accessible-set 构建、无多槽合并、门语义="
                          "结构掩体存在非硬生存约束。GATED_COVER_TIER_CHAIN 独立于 HARD_GATED 立族"),
            "human_review_queued": "HRQ-RS1-02",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    for r in engine["boundary_vs_patch"]:
        tests.append({
            "program_id": r["program_id"], "template_id": "PATCH_RESOURCE_FOLLOWING",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["engine_structural_diff"]),
            "engine_raw_diffs": r["engine_structural_diff"],
            "reasoning": ("族域边界证据：patch 存在门先行（GATE→EVAL→NORM）vs PATCH 评估先行"
                          "（EVAL_RESOURCE_PATCH→CONSTRAIN_ZONE→NORM）——判断顺序相反（顺序有业务"
                          "意义=ORDER 判据），且无 typed context 中间步。门形 patch 追随不并入 PATCH 族"),
            "human_review_queued": "HRQ-RS1-02",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    # E) 61 × CRR（non-match 续存）
    for r in engine["vs_crr"]:
        tests.append({
            "program_id": r["program_id"], "template_id": "CONSTRAINED_RELATIVE_REFUGE",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["structural_diffs"]),
            "engine_raw_diffs": r["structural_diffs"],
            "reasoning": ("CRR non-match 续存（重跑链形仍无 RelativeRank(reference_set=FeasibleSet) "
                          "判别结构）。registry 决定：同物种原程序 B1-B4 已登记 CRR known_non_matches，"
                          "重跑程序不重复追加名单（HRQ-RS1-04 记档）"),
            "human_review_queued": "HRQ-RS1-04",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    write_jsonl("merge_tests.jsonl", tests)

    # ---------------- stories.jsonl ----------------
    stories = []
    for pid, p in progs.items():
        code = p["species_id"]
        fam = FAMILY_OF[CLUSTER[pid]]
        stories.append({
            "story_id": p["story_id"],
            "source_story": ("CENSUS-RERUN 单元｜" + RERUN_OF[code] +
                             " 重跑｜输入=" + p["source_evidence_ids"][0]),
            "frozen_patterns": ["work-standards-§5.1", "work-standards-§5.4"],
            "surfaces": {"Bake": {
                "consequence": "NEW_PROGRAM_CANDIDATE", "program_ids": [pid],
                "reason": "顺序还原链形重跑（" + fam + "）"}},
            "consequence": "NEW_PROGRAM_CANDIDATE",
            "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}})
    write_jsonl("stories.jsonl", stories)

    # ---------------- absence_claims / HRQ ----------------
    write_jsonl("absence_claims.jsonl", [
        {"story_id": f"CENSUS-RERUN-SINGLE-001-{code}",
         "claim": "RERUN_INPUT_UNAVAILABLE",
         "program_id": orig, "reason": reason + "——顺序还原重跑输入缺失；原批 story 证据维持 "
         "SINGLE v1 归族（平铺两步），标记 pending_restored_input，不入拆分处置",
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}}
        for code, (orig, reason) in NO_FILE.items()])
    write_jsonl("human_review_queue.jsonl", [
        {"id": "HRQ-RS1-01",
         "topic": "SINGLE_FACTOR_NORMALIZED_WEIGHT 族拆分总裁决（受影响成员重跑）",
         "facts": ("61/66 有重跑输入成员 vs v1 canonical 全 body 结构差异（最小集 BRANCH=三档分级命中+"
                   "early return；45 例附加 GATE/OPERATOR/DEPENDENCY/COMBINE/RETURN）；SINGLE "
                   "forbidden_freedoms 显式禁 gate 与多因子 combine——族域违例佐证；5 无文件成员"
                   "（LAM/PIN/ASR/RVS/RDS）留 SINGLE pending"),
         "decision_needed": ("①拆分处置批准：61 成员去向（9 新候选族+14 PLAIN 重归族提案）；"
                             "②SINGLE v2 alternative：C1 TIERED_SINGLE（17 成员）是否视为 SINGLE "
                             "canonical 结构升级（v2=档位化两步）而非新族——worker 倾向 SPLIT"
                             "（45/61 非单档形，升级无法覆盖）+ C1 独立（BRANCH 真差异不 MERGE）；"
                             "③SINGLE v1 canonical 与 5 pending 成员的最终态"),
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}},
        {"id": "HRQ-RS1-02",
         "topic": "9 个新 Bake 候选族立族备案",
         "facts": ("TIERED_SINGLE(17)/LAYER_AXIS_DUAL_TIER(2)/GATED_COVER_TIER(12)/NOCTURNAL_"
                   "LIGHTSLOT(5)/ZONE_SUBSTRATE_RESOURCE(3)/SOFT_TRIPLE_TIER(1 PROVISIONAL)/"
                   "ZONE_DEPTH_SUBSTRATE_RESOURCE(1 PROVISIONAL)/FILTER_FIELD_ACCUMULATE(2)/"
                   "GUARD_ANCHOR_TIERED_COMBINE(4)；canonical=源成员冻结体（STATE_GATED 物化先例）；"
                   "边界证据：GATED_COVER vs HARD_GATED/PATCH、GUARD_ANCHOR vs PLAIN（RETURN/COMBINE）、"
                   "C5b/C5c vs C5a（首步软硬/链长真差异）"),
         "decision_needed": ("①9 族立族批准（含 2 单成员 PROVISIONAL 的 extend-vs-split：C5b/C5c 对 "
                             "C5a 为 ORDER/OPERATOR 真差异，worker 裁 NEW 单成员候选非 extension）；"
                             "②gate_axis/anchor_type/factor_type 轴声明；③GUARD_ANCHOR 与 Response 面 "
                             "GUARD 族的 surface 边界确认（Bake 护巢分布 vs Response 双 Path）"),
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}},
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
                   "④CRR non-match 不重复登记决定；⑤ASR/RVS 身份待澄清（thorny_skate README §4）"),
         "decision_needed": "输入层缺陷修复路由（Story 正文到达后的档位校准回写机制；文件名-标题一致性清理）",
         "provenance": {"batch": "CENSUS-RERUN-SINGLE-001"}}])

    # ---------------- manifest.yaml ----------------
    manifest = """batch_id: CENSUS-RERUN-SINGLE-001
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
execution_mode: B3-F-0（fresh spawn 单轮，双时间戳+内容 hash 自证；program_revisions 空）
blind_discipline:
  blind_programs_frozen_at: "2026-09-11T04:39:22Z"   # 文件系统精确时刻（本地 12:39:22+0800）
  n_programs: 61
  registry_opened_at: "2026-09-11T04:41:30Z"          # 冻结后（read template_registry.yaml v6）
  post_registry_mutations: 0
  bias_declaration: |
    事前暴露：SINGLE v1 canonical 两步形在角色记忆与 B4 批档（run_merge_tests.py
    CANONICALS——流程范式恢复时读取）中已知；本批骨架不从 canonical 反推，全部
    61 条为各文件 §2.2 顺序还原伪脚本的机械 IR 转写（文件自身即声明与 canonical
    的分歧并要求 census 侧重跑裁决——work standards §5.4）。盲重建顺序：读 61 份
    §2.2 → 转写冻结 → 开 registry。重跑语义：输入为表达文件（非 Story DB 快照），
    与 B0-B4 批的 Story 输入层不同——envelope 明示授权（ARTIFACT_URL=顺序还原后
    表达文件）。
order_discipline: 全 61 链形按 §5.1 顺序还原形转写（ordered_steps 顺序=文件判断链顺序；
  early return/分级命中/槽语义=branches+return topology；分级命中展开为 IF3 非
  单一布尔——2026-09-11 用户新标准）
verdict_counts:
  merge_confident: 61          # 簇内直验（含 10 canonical 源自测；语义层）
  extension_candidate: 14      # C8 × PLAIN（slot_tiering 轴）
  new_template_candidate_families: 9   # distinct 新候选族（registry template 级）
  ambiguous: 0
deltas:
  dL_group: 0
  dL_bake: 9
  dL_response: 0
  dL_quality: 0
registry: v6 -> v7（SINGLE 拆分注记 + 9 新候选族 + PLAIN 重归族挂账）
"""
    (BATCH / "manifest.yaml").write_text(manifest, encoding="utf-8")

    # ---------------- discovery curve ----------------
    row = ("CENSUS-RERUN-SINGLE-001,61,61,61,14,9,0,0,9,0,0,0,0,0\n")
    txt = CURVE.read_text(encoding="utf-8")
    if not txt.endswith("\n"):
        txt += "\n"
    if "CENSUS-RERUN-SINGLE-001" not in txt:  # 幂等重入
        CURVE.write_text(txt + row, encoding="utf-8")

    # ---------------- registry v6 -> v7 ----------------
    reg = REG.read_text(encoding="utf-8")
    reg = reg.replace(
        "version: 6\n",
        "version: 7\n", 1)
    reg = reg.replace(
        "mutation_provenance:\n",
        """mutation_provenance:
  batch: CENSUS-RERUN-SINGLE-001
  date: 2026-09-11
  previous_version: 6
  rerun_summary: "SINGLE 族受影响成员重跑（用户反馈 §5.4 行动项；顺序还原后 B 系列表达文件为盲重建输入）：61/66 成员 vs v1 canonical 全 body 结构差异（最小集 BRANCH；SINGLE forbidden_freedoms 禁 gate/多因子佐证）→ 拆分提案：+9 新 Bake 候选族（TIERED_SINGLE 17/LAYER_AXIS_DUAL_TIER 2/GATED_COVER_TIER 12/NOCTURNAL_LIGHTSLOT 5/ZONE_SUBSTRATE_RESOURCE 3/SOFT_TRIPLE_TIER 1 PROV/ZONE_DEPTH_SUBSTRATE_RESOURCE 1 PROV/FILTER_FIELD_ACCUMULATE 2/GUARD_ANCHOR_TIERED_COMBINE 4）+14 追击型 PLAIN 重归族提案（slot_tiering 轴 extension HRQ-RS1-03）；5 无文件成员留 SINGLE pending（LAM/PIN/ASR/RVS/RDS）；拆分待 HRQ-RS1-01 人类裁决——61 成员在 SINGLE known_instances 标注 moved_pending_review 不删除；CRR non-match 不重复登记（原程序 B1-B4 已录）；dL_bake=+9"
""", 1)
    # SINGLE 条目追加重跑注记（open_precedents 行后）
    reg = reg.replace(
        "    open_precedents: [HRQ-B1-01（factor_type 轴宽度）, HRQ-B1-02（与 PATCH 的 optional_context 边界）]\n",
        """    open_precedents: [HRQ-B1-01（factor_type 轴宽度）, HRQ-B1-02（与 PATCH 的 optional_context 边界）, HRQ-RS1-01（族拆分总裁决）]
    rerun_2026_09_11:
      batch: CENSUS-RERUN-SINGLE-001
      outcome: "61/66 有输入成员 vs v1 canonical 全 body 结构差异（0 匹配）；5 无文件成员（LAM/PIN/ASR/RVS/RDS）维持原归族 pending_restored_input"
      split_proposal: "61 成员 moved_pending_review：C1 17→TIERED_SINGLE_FACTOR_CHAIN / C2 2→LAYER_AXIS_DUAL_TIER_CHAIN / C3 12→GATED_COVER_TIER_CHAIN / C4 5→NOCTURNAL_LIGHTSLOT_CHAIN / C5a 3→ZONE_SUBSTRATE_RESOURCE_CHAIN / C5b 1→SOFT_TRIPLE_TIER_CHAIN / C5c 1→ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN / C6 2→FILTER_FIELD_ACCUMULATE_CHAIN / C7 4→GUARD_ANCHOR_TIERED_COMBINE_CHAIN / C8 14→PLAIN_FACTOR_COMBINE 重归族提案（slot_tiering extension）——批准后 SINGLE 名义成员=5 pending 或 0（视 v1 canonical 最终态裁决）"
      review: HRQ-RS1-01
""", 1)
    # PLAIN 追加重归族挂账注记
    reg = reg.replace(
        "    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）, HRQ-B1-04（槽位数伸缩+rank 因子类型）]\n",
        """    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）, HRQ-B1-04（槽位数伸缩+rank 因子类型）, HRQ-RS1-03（slot_tiering 轴+14 重归族挂账）]
    rerun_2026_09_11_pending_members: "CENSUS-RERUN-SINGLE-001：14 追击型成员（TAI/BLP/GW/RFP/DS/PBF/GT/HAL/GG/POR/RKB/WIN/SMF/SAI——P-RS1-*-BAKE）表达文件自投影 PLAIN 双槽+槽内三档受限还原；slot_tiering(FLAT|IF3_SLOT_VALUE) 轴提案 pending HRQ-RS1-03——批准前不计正式成员（HNC extension 挂账先例）；证据分层（表达文件 Tier B vs story 单因子）待裁决"
""", 1)
    # 9 个新族条目（STATE_GATED 条目之后追加）
    new_templates = """
  - template_id: TIERED_SINGLE_FACTOR_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族顺序还原重跑拆分（用户反馈 §5.4）；canonical=源成员 P-RS1-COD-BAKE 冻结体
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(typed 因子三档分级命中：preferred=全额/tolerated=削减不清零/excluded=出局 EARLY_RETURN)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.TIERED_SINGLE_FACTOR_CHAIN
    allowed_parameter_axes:
      - factor_type(typed: premise_bound_axis | opportunity_field | sensory_signal | …；HRQ-B1-01 轴延续)
      - factor_binding(随 lifecycle/season/sex/diel premise 切换)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 多因子 combine（PLAIN 域）, 前置 gate（GATED_COVER/HARD_GATED 域）, 第二判定步（LAYER_AXIS_DUAL_TIER 域）, 无档位平铺（那是 SINGLE v1 域——BRANCH 真差异）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-COD-BAKE, role: canonical_source, note: "premise 轴段亚群（10）之一：sex/stage 深度带"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-PIK19-BAKE, P-RS1-ARC-BAKE, P-RS1-VEN-BAKE, P-RS1-SWO-BAKE, P-RS1-CHN-BAKE, P-RS1-COH-BAKE, P-RS1-BRO-BAKE, P-RS1-ALE-BAKE, P-RS1-TAR-BAKE], note: "premise 轴段亚群其余 9（繁殖轴段/季节轴/季节水层/DVM 相位/洄游轴段×4/发育轴段）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-BRT12-BAKE, P-RS1-PB-BAKE, P-RS1-BST-BAKE, P-RS1-CBM-BAKE], note: "机会亚群（4）：食物丰度先行"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-PAD34-BAKE, P-RS1-SDG-BAKE, P-RS1-TSK-BAKE], note: "感官亚群（3）：信号场可探测性先行"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: SINGLE_FACTOR_NORMALIZED_WEIGHT, reason: "BRANCH 真差异（三档分级命中+early return 为 v1 平铺 canonical 无有的控制流；档位化=canonical 结构变更非轴内）"}
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: LAYER_AXIS_DUAL_TIER_CHAIN, reason: "OPERATOR/DEPENDENCY（前置水层定位步）"}
  - template_id: LAYER_AXIS_DUAL_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分；canonical=P-RS1-CHU-BAKE（大马哈鱼 benthopelagic 锚）+美洲西鲱（pelagic-neritic 锚）跨科独立重复
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(水层带软三档定位)
      -> EVAL_TYPED_FIELD_OR_FACTOR(premise 绑定轴段归属三档)
      -> NORMALIZE_WEIGHT(LayerTier × AxisFit 积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.LAYER_AXIS_DUAL_TIER_CHAIN
    allowed_parameter_axes:
      - layer_anchor(typed: benthopelagic | pelagic_neritic | …)
      - premise_axis_binding(lifecycle/阶段轴段)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 单档链（TIERED_SINGLE 域）, 三档链（C5 域）, 硬门首步（GATED_COVER/C5a 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-CHU-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SHA-BAKE}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: TIERED_SINGLE_FACTOR_CHAIN, reason: "前置水层定位步（OPERATOR/DEPENDENCY 真差异）——双判断序 vs 单判断序，顺序有业务意义不 MERGE"}
  - template_id: GATED_COVER_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分（envelope『伏击门形』承载族）；canonical=P-RS1-FGA-BAKE
    canonical_program_body: |
      GATE_STRUCTURE_COVER_PRESENT(结构掩体存在门：不成立直接 EARLY_RETURN)
      -> EVAL_TYPED_FIELD_OR_FACTOR(掩体/质量档三档)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GATED_COVER_TIER_CHAIN
    allowed_parameter_axes:
      - gate_axis(typed: vegetation_edge | weedy_slack | bottom_zone | buryable_substrate | pool_structure | reef_edge | patch_presence | disturbance_window；HRQ-RS1-02 待批)
      - factor_type(typed)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 无门单档（TIERED_SINGLE 域）, 多槽 combine（PLAIN/HARD_GATED 域）, BUILD_ACCESSIBLE_SET 前置（HARD_GATED 域）, 评估先行的 zone 约束（PATCH 域——门先行=ORDER 真差异）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-FGA-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-SGA-BAKE, P-RS1-AST-BAKE, P-RS1-SNS-BAKE, P-RS1-GPF-BAKE, P-RS1-SSL-BAKE, P-RS1-WIT-BAKE, P-RS1-YTF-BAKE, P-RS1-FDR-BAKE, P-RS1-BSB-BAKE], note: "伏击门 9 例（engine raw=gate_axis 字面，语义 MC——GUARD anchor 判例同型）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-GRB-BAKE, P-RS1-SMA-BAKE], note: "patch/扰动门 2 例（vs PATCH 族 ORDER 真差异——门先行 vs 评估先行；merge_tests 边界证据）"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: HARD_GATED_FACTOR_COMBINE, reason: "无 accessible-set 构建/多槽合并；门语义=结构掩体存在非硬生存约束（OPERATOR/DEPENDENCY/COMBINE 真差异）"}
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: PATCH_RESOURCE_FOLLOWING, reason: "门先行 vs 评估先行（ORDER）+无 typed context 中间步（OPERATOR）"}
  - template_id: NOCTURNAL_LIGHTSLOT_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分（live §11.5 判例槽位原位维持）；canonical=P-RS1-WEL-BAKE
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(夜行底板栖息档三档：无夜行底板=出局 EARLY_RETURN)
      -> APPLY_DYNAMIC_SPATIAL_SLOT(低光/夜相槽三档：调整器语义——亮水=极低削减不清零，出局语义不落槽内；槽位=live §11.5 判例固定)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.NOCTURNAL_LIGHTSLOT_CHAIN
    allowed_parameter_axes:
      - night_habitat_axis(typed: 洞穴深潭 | 木石结构 | 石底深潭 | 开阔水面 | …)
      - lowlight_slot(live §11.5 判例原位——槽位置非作者可选)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 槽内出局语义（出局落 typed 因子步非槽——族域边界）, 单档无槽（TIERED_SINGLE 域）, 槽位置提前（改 §11.5 判例结构需重审）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-WEL-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-FLA-BAKE, P-RS1-BUR-BAKE, P-RS1-GDE-BAKE, P-RS1-MOO-BAKE], note: "engine 零差异（含 PREMISE raw）"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: TIERED_SINGLE_FACTOR_CHAIN, reason: "第二槽步+槽无出局语义（branch kind 真差异）"}
  - template_id: ZONE_SUBSTRATE_RESOURCE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分（grazing 底质链形）；canonical=P-RS1-GRH-BAKE
    canonical_program_body: |
      GATE_ZONE(底层水层硬定位：非底层=EARLY_RETURN)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底栖资源档三档)
      -> NORMALIZE_WEIGHT(SubstrateTier × ResourceIntensity 积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_SUBSTRATE_RESOURCE_CHAIN
    allowed_parameter_axes:
      - substrate_tier_axis(typed: 无脊椎栖境 | 大型无脊椎 | 可翻性 | 底泥)
      - factor_binding(常年绑定/随 premise 切换)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 单/双档链（TIERED_SINGLE/DUAL_TIER 域）, 软首档无门（SOFT_TRIPLE 域）, 深度档步（ZONE_DEPTH 域）, 多槽 combine（PLAIN 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-GRH-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-RRH-BAKE, P-RS1-DRU-BAKE], note: "engine 零差异（同属同构+翻底可翻性轴值）"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: SOFT_TRIPLE_TIER_CHAIN, reason: "首步 GATE 硬门 vs 软三档（OPERATOR/BRANCH 真差异）"}
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN, reason: "深度档步有无（OPERATOR 真差异——步数 4 vs 5）"}
  - template_id: SOFT_TRIPLE_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-02
      origin: SINGLE 族拆分（BSK 独有链形）
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(近底带水层软三档——无硬门)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(资源档三档)
      -> NORMALIZE_WEIGHT(三档积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.SOFT_TRIPLE_TIER_CHAIN
    allowed_parameter_axes:
      - layer_tier_axis(typed)
      - substrate_tier_axis(typed)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 硬门首步（ZONE_SUBSTRATE 域）, 二步链]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BSK-BAKE, role: canonical_source}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: ZONE_SUBSTRATE_RESOURCE_CHAIN, reason: "首步软档 vs GATE（结构差异）；extend-vs-split 见 HRQ-RS1-02"}
    provisional_note: 单成员 PROVISIONAL（Tier B CSV benthopelagic 软定位推导，硬定位与否 [需正文]——正文证实硬定位则并入 ZONE_SUBSTRATE 族）
  - template_id: ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-02
      origin: SINGLE 族拆分（SMB 独有五步链——CSV 深≥4m 锚）
    canonical_program_body: |
      GATE_ZONE(底层水层硬定位)
      -> EVAL_TYPED_FIELD_OR_FACTOR(深度带档三档——本鱼独有步)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥资源档三档)
      -> NORMALIZE_WEIGHT(三档积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN
    allowed_parameter_axes:
      - depth_tier_axis(typed)
      - substrate_tier_axis(typed)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 无深度档步（ZONE_SUBSTRATE 域——步数=ORDER/OPERATOR 真差异非轴内）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SMB-BAKE, role: canonical_source}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: ZONE_SUBSTRATE_RESOURCE_CHAIN, reason: "深度档步有无（步数 5 vs 4——链长差异=真结构差异）；extend-vs-split 见 HRQ-RS1-02"}
    provisional_note: 单成员 PROVISIONAL（Tier B CSV 深度锚推导 [需正文]）
  - template_id: FILTER_FIELD_ACCUMULATE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分（滤食场链形）；canonical=P-RS1-BHC-BAKE；与 Response 面 FOOD_FIELD_FEEDING_RESPONSE 不同 surface（Bake 分布 vs Response 摄入）
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(滤食水层定位三档——携削减标记)
      -> EVAL_FOOD_FIELD_CONCENTRATION(场浓度三档：FieldSuitability 叠加衰减)
      -> EVAL_SIZE_GAUGE_MATCH(个体口径三档：口径不匹配=出局)
      -> NORMALIZE_WEIGHT(步间折减合成算子 OPERATOR UNDEFINED 待机制侧)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.FILTER_FIELD_ACCUMULATE_CHAIN
    allowed_parameter_axes:
      - field_type(typed: plankton_field | …；P03 轴 Bake 侧对应)
      - gauge_semantics(个体大小口径——鱼侧状态评估步)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 并联多因子（PLAIN 域——本族=同一场评估顺序判定线性累积）, 二步场链（TIERED_SINGLE 域）, 扇入积拓扑（C5 域——deps 线性 vs 扇入）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BHC-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-HER-BAKE, note: "engine 零差异；群游集聚并入槽值域（coverage #17）"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: SOFT_TRIPLE_TIER_CHAIN, reason: "op 语义（场浓度/口径 vs 底质/资源）+deps 线性累积 vs 扇入积（OPERATOR/DEPENDENCY 真差异）"}
  - template_id: GUARD_ANCHOR_TIERED_COMBINE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-SINGLE-001
      seeded: 2026-09-11
      review_queue: HRQ-RS1-01/02
      origin: SINGLE 族拆分（护巢 Bake 面分布程序）；canonical=P-RS1-BLU-BAKE；与 GUARD_CONFLICT_DUAL_PATH_RESPONSE（Response 面 ∥ 双 evaluand）不同 surface 不同拓扑
    canonical_program_body: |
      GATE_ANCHOR_EXISTENCE(锚存在门：锚域外=EARLY_RETURN 非「算出低值」)
      -> EVAL_ANCHOR_SUITABILITY(锚适配三档)
      -> EVAL_ANCHOR_RELATION(守卫关系三档)
      -> EVAL_LOCAL_TEMPERATURE(局部温度三档)
      -> COMBINE_GUARD_FACTORS(算子 OPERATOR UNDEFINED 待机制侧)
      -> Guarding SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GUARD_ANCHOR_TIERED_COMBINE_CHAIN
    allowed_parameter_axes:
      - anchor_type(typed: colony_nest | floodplain_fry_school | root_spawn_eggs | pebble_mound——与 Response 面 GUARD anchor 轴同源第 4-7 值；HRQ-RS1-02 待批)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 分布权重返回类型外的 return（其余 Bake 域）, BUILD_ACCESSIBLE_SET/hard_viability（HARD_GATED 域）, ∥ 并行双 evaluand（Response 面 GUARD 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BLU-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-ARA-BAKE, P-RS1-RBP-BAKE, P-RS1-HNC-BAKE], note: "engine 零差异（4 锚型）；HNC pebble_mound 与 HRQ-B4-01 Response 面提案同值"}
    known_non_matches:
      - {batch: CENSUS-RERUN-SINGLE-001, template_id: PLAIN_FACTOR_COMBINE, reason: "RETURN（Guarding vs 分布）+COMBINE（UNDEFINED 多评估合并 vs WEIGHTED 终合并）+前置锚门——真差异"}
"""
    reg = reg.rstrip("\n") + "\n" + new_templates
    REG.write_text(reg, encoding="utf-8")

    print("outputs written:")
    print(f"  programs={len(programs)} stories={len(stories)} "
          f"merge_tests={len(tests)}")
    from collections import Counter
    print("  verdicts:", dict(Counter(t["verdict"] for t in tests)))
    print("  registry: v7 written; curve row appended")


if __name__ == "__main__":
    main()
