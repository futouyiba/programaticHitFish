# -*- coding: utf-8 -*-
"""HRQ-MUTATION-001: registry v8 -> v9 mutation executor（HRQ 裁决执行批）.

授权来源（唯一依据）：fish_logic_census/hrq_decision_log.md @ commit b5088ab
（HRQ-ADJUDICATION-2026-09-11：七项裁决+两组语义裁定——本批零新增裁决，
逐条执行决策日志文末「mutation 批执行清单」）。

产出：
  1. fish_logic_census/template_registry.yaml  v8 -> v9（全部替换锚点断言唯一）
  2. fish_logic_census/truth_rebuild_queue.jsonl（234 AMB + 14 slot_tiering = 248 行）
  3. 批目录 manifest.yaml + 空 jsonl（validate_batch 形式要求，manifest 声明非普查批）

幂等守卫：registry 已是 v9 -> exit 1（防重放回退；RS1 判例⑧⑨）。
历史内容零删除：SINGLE/PLAIN/PATCH 的 v8 known_instances 原文整体保留为历史层。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = ROOT / "fish_logic_census" / "template_registry.yaml"
QUEUE = ROOT / "fish_logic_census" / "truth_rebuild_queue.jsonl"
BATCH = ROOT / "fish_logic_census" / "batches" / "HRQ-MUTATION-001"

text = REG.read_text(encoding="utf-8")
if "\nversion: 9\n" in text:
    sys.exit("GUARD: registry already at v9 — refusing to re-apply (idempotency)")

extracted = json.loads((BATCH / "_extracted.json").read_text(encoding="utf-8"))


def blind_hashes(batch_dir: str) -> dict:
    out = {}
    for line in (ROOT / "fish_logic_census" / "batches" / batch_dir / "blind_programs.jsonl") \
            .read_text(encoding="utf-8").splitlines():
        if line.strip():
            p = json.loads(line)
            out[p["program_id"]] = p.get("blind_hash")
    return out


BH5 = blind_hashes("CENSUS-B5")
BH6 = blind_hashes("CENSUS-B6")
BH7 = blind_hashes("CENSUS-B7")


# ===========================================================================
# 替换列表（每个锚点断言在原文中恰好出现 count 次）
# ===========================================================================
patches: list[tuple[str, str, int, str]] = []


def rep(old, new, count, tag):
    patches.append((old, new, count, tag))


def fmt_ids(ids):
    return "[" + ", ".join(ids) + "]"


TYPED_B5 = fmt_ids(extracted["CENSUS-B5"]["mc_typed"])
TYPED_B6 = fmt_ids(extracted["CENSUS-B6"]["mc_typed"])
TYPED_B7 = fmt_ids(extracted["CENSUS-B7"]["mc_typed"])
FIELD_B7 = fmt_ids(extracted["CENSUS-B7"]["mc_field"])
CRR_B5 = fmt_ids(extracted["CENSUS-B5"]["crr_nonmatch"])
CRR_B6 = fmt_ids(extracted["CENSUS-B6"]["crr_nonmatch"])
CRR_B7 = fmt_ids(extracted["CENSUS-B7"]["crr_nonmatch"])

DEC = "HRQ-ADJUDICATION-2026-09-11（决策日志 commit b5088ab）"

# ---------------------------------------------------------------------------
# A. version 8 -> 9 + mutation_provenance 头块（旧块整体挪入 v8_mutation_history）
# ---------------------------------------------------------------------------
rep("version: 8\n", "version: 9\n", 1, "version bump")

HEAD_NEW = """mutation_provenance:
  batch: HRQ-MUTATION-001
  kind: HRQ_ADJUDICATION_EXECUTION（registry mutation 批——非普查批：无新盲程序/无新判同；人类裁决已完成，本批逐条落表）
  date: 2026-09-14
  previous_version: 8
  authorization: "%s"
  ruling_scope: "七项裁决（1 SINGLE 拆分/2 顺序=族判据/3 C9 缓立并入重跑/4 anchor 四形式/5 HARD_GATED v2/6 目录卫生三件套/7 CRR+簿记打包）+两组语义裁定（1 无合并步——渐进累积+×0.01 软出局；2 措辞对齐/逐鱼顺序推导必做）"
  previous_state: "v8：21 族条目全 CANDIDATE；SINGLE 66 名义（61 moved_pending_review 过渡双列+5 无文件成员）；9 链族 CANDIDATE-pending-HRQ-RS1-01；GUARD anchor 轴 6+1 值+18 候选挂账（B5 9+B6 2+B7 7）+RSB 复现+DIS2 对照；TYPED 74 名义；FOOD_FIELD 2 名义；HARD_GATED canonical v1+v2 提案 pending（EEL AMBIGUOUS）；PLAIN 5 名义（0/5 证伪后 3 slot_tiering+OSC/BRT 出族挂账）；PATCH 2 名义（MGC/ONS 重指派挂账）；CRR known_non_matches 75（B0-B4）；Bake 名义程序 162+RS1 REV-001 4 HAB=166 pending"
  ruling_to_mutation_map:
    ruling_1_SINGLE_split: "SINGLE_FACTOR_NORMALIZED_WEIGHT status CANDIDATE->RETIRED（v1 canonical 证伪注记：RS1 61/61 全 body 结构差异+渐进累积语义）；61 moved 成员＝47 转正 9 链族（链族 known_instances 已载：B1 6+B2 8+B3 16+B4 17）+14 slot_tiering（C8 追击型：B3 9+B4 5）经裁决 6-③ 转 truth_rebuild_queue（不在任何链族——HRQ-MUTATION-REV-001 F2 补正）；SINGLE 原 66 条清单保留为 v8 历史快照层；5 无文件成员（LAM/PIN/ASR/RVS/RDS）evidence_insufficient_held 归 FR/表达线；234 AMB（B4 25+B5 52+B6 47+B7 110）-> truth_rebuild_queue.jsonl"
    semantic_1_progressive_accumulation: "9 链族+HARD_GATED v2+EXTREME_TEMP+PATCH_GATED_DUAL canonical 全部重写：无终步合并算子（NORMALIZE_WEIGHT/COMBINE_* 终步与 OPERATOR UNDEFINED 占位关闭），每步 EVAL 三档（preferred=全额乘入/tolerated=×衰减乘入/excluded=×0.01 软出局乘入——非零、仍可参与下游，对齐 0.3.4.0 Bake DSL）-> 乘入 running weight；GATE 硬门 EARLY_RETURN 语义保留（门非三档出局）"
    semantic_2_wording_alignment: "原『排除档=出局/EARLY_RETURN』措辞全部对齐为 ×0.01 软出局（B 系列表达文件措辞对齐待办记批报告；work standards §5.1 表述更新归文档线）"
    ruling_2_order_as_family_criterion: "9 链族全部加 order_provisional: true（基础序=模板约定；成员真实序待终局逐鱼推导，序差异=族移动）"
    ruling_3_C9_deferred_to_rerun: "C9/PROGRESSIVE_TIERED_FUNNEL 不入 registry（缓立）；truth_rebuild_queue 为其重跑基准载体——157 对 PENDING_CANDIDATE 比较材料悬置；HRQ-RS1-05 关闭"
    ruling_4_anchor_four_forms: "GUARD（Response 面）anchor 轴重写为四形式（nest/egg_mass/fry_school/host_brood）+brooded 退化边界（不入本族待重跑：ARO 银龙口哺/TIL3 罗非退化链）；guard_participant 轴（male|biparental）新立；fan/黏液喂养->guard_action_notes 注记字段；GUARD_ANCHOR（Bake 面）anchor_type 轴同源对齐；原 6+1 值与 18 候选+RSB/DIS2 按落位表逐一 reassign（见 GUARD 族 v9 四形式重排块）；pebble_mound 18-vs-19 口径关闭（->nest）；discus_mucus vs fry_anchor 关闭（->fry_school+注记）"
    ruling_5_HARD_GATED_v2: "canonical v2 落表（BUILD+双硬门->EXIT 档因子集 unordered×4，渐进累积）；LUN canonical_source_v2+EEL 第 2 成员（AMBIGUOUS 清除）；电感知分层注记 REP-CUE-AXIS-001（主动放电/远程麻痹归 Encounter/Conversion、被动电感知归 Response cue——不进 Bake）"
    ruling_6_directory_hygiene: "PATCH_RESOURCE_FOLLOWING status->VACATED（MGC->GATED_COVER gate_axis bottom_zone 第 3 实例转正/ONS->SOFT_TRIPLE 第 2 成员转正）；PLAIN_FACTOR_COMBINE status->FALSIFIED（0/5 自有成员证伪证据随册；14 slot_tiering -> truth_rebuild_queue）；活族 21->19 条目（Bake 空壳移除——PROVISIONAL 新族不受影响）"
    ruling_7_CRR_ledger_plus_bookkeeping: "CRR 保留+negative_evidence_ledger（284 non-match=live 侧资产；known_non_matches 补 B5/B6/B7 三行对账闭环 75+52+47+110=284）；TYPED known_instances 74->248（B5 43+B6 45+B7 86）；FOOD_FIELD 2->16（B7 14）；GUARD 四形式重排+participant 轴；Bake 名义程序数 166（v8 pending 转 v9 正式）；LOCAL_SATURATION_CANDIDATE 正式撤销（B4 立案前提证伪——裁决 1 联动）；MGC 旧口径 reconciliation-note（B0 TYPED premise 处理 vs FOOD_FIELD 族——待重跑对齐）"
  closed_hrqs: "RS1-01/RS1-04⑥/RS1-05/RS1-03、B4-01（饱和撤销）/B4-02、B5-01/B5-02、B6-01/B6-02、B7-01/B7-02、B2-02（CRR）"
  handed_to_rerun: "truth_rebuild_queue.jsonl 248 行（234 AMB+14 slot_tiering）——终局全库顺序还原重跑输入清单（逐鱼顺序推导必做；C9 与 brooded[ARO/TIL3] 由重跑证据终裁）"
  review_gate: "本批 status=INDEPENDENT_REVIEW_REQUIRED——mutation 不自我批准；独立审通过前不推远端"

v8_mutation_history:"""

HEAD_NEW = HEAD_NEW % DEC

rep(
    "mutation_provenance:\n  batch: CENSUS-RERUN-PLAIN-001",
    HEAD_NEW + "\n  batch: CENSUS-RERUN-PLAIN-001",
    1,
    "provenance head",
)

# ---------------------------------------------------------------------------
# B. CRR：known_non_matches 补 B5/B6/B7 + negative_evidence_ledger
# ---------------------------------------------------------------------------
rep(
    "        reason: B4 边界层 25 程序全部非匹配（premise 绑定切换[洄游/季节/潮汐/盐度/阶段]与静态结构/因子绑定形态，无 RelativeRank）；CRR 连续第 4 批 0 成员（HRQ-B2-02 维持）\n",
    "        reason: B4 边界层 25 程序全部非匹配（premise 绑定切换[洄游/季节/潮汐/盐度/阶段]与静态结构/因子绑定形态，无 RelativeRank）；CRR 连续第 4 批 0 成员（HRQ-B2-02 维持）\n"
    "      - batch: CENSUS-B5\n"
    f"        program_id: {CRR_B5}\n"
    "        reason: B5（R08+R09 双包）52 Bake 程序全部非匹配（平铺因子/静态结构形态，无 RelativeRank）——累计 127 仍 0 成员；v9 名义入册（裁决 7-A）\n"
    "      - batch: CENSUS-B6\n"
    f"        program_id: {CRR_B6}\n"
    "        reason: B6（FISH-R10 收官批）47 Bake 程序全部非匹配——累计 174 仍 0 成员；v9 名义入册（裁决 7-A）\n"
    "      - batch: CENSUS-B7\n"
    f"        program_id: {CRR_B7}\n"
    "        reason: B7（R01-R05 残余基线收尾）110 Bake 程序全部非匹配——累计 284 仍 0 成员；HRQ-B2-02 经裁决 7-A 关闭（negative_evidence_ledger 保留）\n",
    1,
    "CRR non-match ledger B5-B7",
)

rep(
    """    merge_candidate_status:
      pike_winter_vs_pike_summer: STRONG_MERGE_CANDIDATE
      bass_coldslow_vs_pike: PLAUSIBLE_MERGE_CANDIDATE""",
    """    merge_candidate_status:
      pike_winter_vs_pike_summer: STRONG_MERGE_CANDIDATE
      bass_coldslow_vs_pike: PLAUSIBLE_MERGE_CANDIDATE
    negative_evidence_ledger:
      ruling: "裁决 7-A（%s）：CRR 负证据台账保留——live 侧资产不撤；284 条 non-match 反对票继续记，作 census<->live 对账弹药；HRQ-B2-02 关闭（输入通道问题非结构缺失——重跑批对账输入）"
      ledger_size: 284   # B0 5 + B1 9 + B2 10 + B3 26 + B4 25 + B5 52 + B6 47 + B7 110（v8 册内 75 + v9 补录 209）""" % DEC,
    1,
    "CRR negative_evidence_ledger",
)

# ---------------------------------------------------------------------------
# C. PLAIN_FACTOR_COMBINE -> FALSIFIED
# ---------------------------------------------------------------------------
rep(
    """  - template_id: PLAIN_FACTOR_COMBINE
    surface: Bake
    status: CANDIDATE""",
    """  - template_id: PLAIN_FACTOR_COMBINE
    surface: Bake
    status: FALSIFIED""",
    1,
    "PLAIN status FALSIFIED",
)

rep(
    """    canonical_program_body: |
      EVAL_HABITAT_FACTOR_TYPED (槽1)
      EVAL_HABITAT_FACTOR_TYPED (槽2)
      EVAL_RESOURCE_FACTOR_TYPED (槽3)
      EVAL_RESOURCE_FACTOR_TYPED (槽4)
      -> COMBINE_WEIGHTED
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-B0/run_merge_tests.py::CANONICALS.PLAIN_FACTOR_COMBINE""",
    """    canonical_program_body: |
      EVAL_HABITAT_FACTOR_TYPED (槽1)
      EVAL_HABITAT_FACTOR_TYPED (槽2)
      EVAL_RESOURCE_FACTOR_TYPED (槽3)
      EVAL_RESOURCE_FACTOR_TYPED (槽4)
      -> COMBINE_WEIGHTED
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-B0/run_merge_tests.py::CANONICALS.PLAIN_FACTOR_COMBINE
    v1_falsification:
      ruling: "裁决 6-②（%s）：PLAIN_FACTOR_COMBINE v1 废止——0/5 自有成员重跑证伪（CENSUS-RERUN-PLAIN-001：CHB/WAL/MDF=slot_tiering 受限还原轨[HRQ-RS1-03 关闭]+OSC/BRT 出族）——『因子集无序』读法正式关闭（与裁决 2-B 一致：顺序=族判据）"
      evidence: "batches/CENSUS-RERUN-PLAIN-001/merge_tests.jsonl（38 条=8 MC+3 EXT+25 NEW+2 AMB）；OSC->EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN / BRT->PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN（单成员 PROVISIONAL 沿革）；canonical v2（slot_tiering）唯一存活读法随 v1 一并废止——slot_tiering 归属由终局重跑重判"
      member_disposition: "known_instances 5 条（OSC/CHB/BRT/WAL/MDF 原体）=历史层保留（v1 时代 MC 判同产物，证伪后不计正式成员）；OSC/BRT 以 RS1/RP1 重跑体入新族；14 追击型 slot_tiering（P-RS1-TAI 等）-> truth_rebuild_queue.jsonl（裁决 6-③）"
      status_note: FALSIFIED 保留全部历史字段（known_instances/open_precedents/rerun 注记=历史层不删）""" % DEC,
    1,
    "PLAIN falsification block",
)

rep(
    """      - {batch: CENSUS-B0, program_id: P-OSC-BAKE, blind_hash: 49c23a9d14d8205f}
      - {batch: CENSUS-B0, program_id: P-CHB-BAKE, blind_hash: 7a45a474788ede01}""",
    """      # —— v8 历史快照层（v1 证伪后全部移出正式成员——裁决 6-②；重跑体归属见 v1_falsification.member_disposition）——
      - {batch: CENSUS-B0, program_id: P-OSC-BAKE, blind_hash: 49c23a9d14d8205f}
      - {batch: CENSUS-B0, program_id: P-CHB-BAKE, blind_hash: 7a45a474788ede01}""",
    1,
    "PLAIN historical layer note",
)

rep(
    "slot_tiering(FLAT|IF3_SLOT_VALUE) 轴提案 pending HRQ-RS1-03——批准前不计正式成员（HNC extension 挂账先例）；证据分层（表达文件 Tier B vs story 单因子）待裁决\"",
    "slot_tiering(FLAT|IF3_SLOT_VALUE) 轨道经裁决 6-③ 关闭——14 成员转 truth_rebuild_queue.jsonl 与 234 AMB 同队同流程（逐鱼顺序推导后重判归属）；证据分层（表达文件 Tier B vs story 单因子）随重跑消解\"",
    1,
    "PLAIN pending_members note update",
)

# ---------------------------------------------------------------------------
# D. HARD_GATED v2
# ---------------------------------------------------------------------------
rep(
    """  - template_id: HARD_GATED_FACTOR_COMBINE
    surface: Bake
    status: CANDIDATE""",
    """  - template_id: HARD_GATED_FACTOR_COMBINE
    surface: Bake
    status: CANDIDATE   # v9：canonical v2 经裁决 5-A 确认落表（族定义保持——硬门前置+因子组合）""",
    1,
    "HARD_GATED status note",
)

rep(
    """    canonical_program_body: |
      BUILD_ACCESSIBLE_SET
      -> GATE_HARD_VIABILITY(typed, e.g. surface_access)
      -> EVAL_HABITAT_FACTOR_TYPED (槽)
      -> EVAL_HABITAT_FACTOR_TYPED (槽)
      -> EVAL_RESOURCE_FACTOR_TYPED (槽)
      -> COMBINE_WEIGHTED
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-B0/run_merge_tests.py::CANONICALS.HARD_GATED_FACTOR_COMBINE""",
    """    canonical_program_body: |
      BUILD_ACCESSIBLE_SET
      -> GATE_HARD_VIABILITY(typed, e.g. surface_access)（硬生存门：不过=EARLY_RETURN——门语义保留）
      -> GATE_EXTREME_TEMP(第二道极值水温硬门——v2 新增[裁决 5-A 确认]：极值带=EARLY_RETURN)
      -> EVAL 因子×4 unordered（EXIT 档因子集——时段槽=v2 新增；各三档分级命中：
         preferred=全额乘入 / tolerated=×衰减乘入 / EXIT 档=×0.01 软出局乘入[非零、仍可参与下游——
         语义裁定 1/2：原『排除档=出局』措辞对齐渐进累积语义]）
      -> [渐进累积：weight = weight × step_fit 逐步累积——无终步 COMBINE_WEIGHTED（语义裁定 1 关闭合并算子占位）]
      -> SpatialDistributionWeight
    canonical_version: v2   # v1（平铺因子+COMBINE 终步）经 RP1 2/2 成员重跑证伪——裁决 5-A 确认 v2；v1 文本见 git b5088ab^
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL（canonical=P-RP1-LUN-BAKE 冻结体；v1 指针 batches/CENSUS-B0/run_merge_tests.py::CANONICALS.HARD_GATED_FACTOR_COMBINE 历史保留）
    order_provisional: true   # 裁决 2-B：因子判断顺序=族判据；因子集 unordered 为 v2 提案证据态（RP1 重跑证据未裁决序）——终局逐鱼推导后若序有据则分化""",
    1,
    "HARD_GATED canonical v2",
)

rep(
    """    known_instances:
      - {batch: CENSUS-B0, program_id: P-LUN-BAKE-WET, blind_hash: f752b5fe225edd86}
      - {batch: CENSUS-B0, program_id: P-EEL-BAKE, blind_hash: 611e70f2cd5fd260}""",
    """    known_instances:
      # —— v9（裁决 5-A）：双成员经 v2 canonical 确认（LUN 源+EEL AMBIGUOUS 清除）——原体为 v1 时代判同产物，v2 成员资格由 RP1 重跑体承载 ——
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-LUN-BAKE, role: canonical_source_v2, note: "LUN 顺序还原重跑体=canonical v2 源（BUILD+双硬门+EXIT 档因子集）；B0 原体 P-LUN-BAKE-WET blind_hash f752b5fe225edd86（v1 历史层）"}
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-EEL-BAKE, note: "EEL 顺序还原重跑体——AMBIGUOUS 清除（裁决 5-A）：Tier A story 证据确认 BUILD 存在，直验并入 v2；电感知分层按 REP-CUE-AXIS-001（主动放电/远程麻痹归 Encounter/Conversion、被动电感知归 Response cue——不进 Bake）；B0 原体 P-EEL-BAKE blind_hash 611e70f2cd5fd260（v1 历史层）"}
    electroception_layering_note: "REP-CUE-AXIS-001 裁定（裁决 5-A 引用）：电感知表征分层——主动放电/远程麻痹归 Encounter/Conversion 层、被动电感知归 Response cue 层，不进 Bake 面（TYPED evaluator_channel=PASSIVE_ELECTROSENSE 实例为 Response 侧对应）\"""",
    1,
    "HARD_GATED membership v2",
)

rep(
    """      review: HRQ-RP1-01
  - template_id: PATCH_RESOURCE_FOLLOWING""",
    """      review: HRQ-RP1-01（已裁决 2026-09-11：裁决 5-A 确认 v2+双成员——commit b5088ab）
  - template_id: PATCH_RESOURCE_FOLLOWING""",
    1,
    "HARD_GATED review closed",
)

# ---------------------------------------------------------------------------
# E. PATCH_RESOURCE_FOLLOWING -> VACATED
# ---------------------------------------------------------------------------
rep(
    """  - template_id: PATCH_RESOURCE_FOLLOWING
    surface: Bake
    status: CANDIDATE""",
    """  - template_id: PATCH_RESOURCE_FOLLOWING
    surface: Bake
    status: VACATED""",
    1,
    "PATCH status VACATED",
)

rep(
    """      outcome: "2/2 成员 vs canonical 评估先行三步 body 证伪：MGC zone=bottom 还原为首道二元定位门（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE=门先行）→GATED_COVER_TIER_CHAIN 重指派提案（gate_axis bottom_zone 第 3 实例，AST/SNS 同值；deps 位形全同语义 MC）；ONS current 侧展开为流速三档+石底档两步（三档×3 链无二元门——首档含过渡削减带）→SOFT_TRIPLE_TIER_CHAIN 重指派提案（族 1→2，单成员 PROVISIONAL 升格候选；deps 位形全同语义 MC）——重指派批准后本族空置（P06 压缩候选联动 HRQ-04/HRQ-B1-02 PENDING 不受影响，归并裁决一并处置）"
      review: HRQ-RP1-02""",
    """      outcome: "2/2 成员 vs canonical 评估先行三步 body 证伪：MGC zone=bottom 还原为首道二元定位门（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE=门先行）→GATED_COVER_TIER_CHAIN 重指派提案（gate_axis bottom_zone 第 3 实例，AST/SNS 同值；deps 位形全同语义 MC）；ONS current 侧展开为流速三档+石底档两步（三档×3 链无二元门——首档含过渡削减带）→SOFT_TRIPLE_TIER_CHAIN 重指派提案（族 1→2，单成员 PROVISIONAL 升格候选；deps 位形全同语义 MC）——重指派批准后本族空置（P06 压缩候选联动 HRQ-04/HRQ-B1-02 PENDING 不受影响，归并裁决一并处置）"
      review: HRQ-RP1-02（重指派部分已裁决 2026-09-11：裁决 6-① 空置撤销——commit b5088ab）
    vacated_provenance:
      ruling: "裁决 6-①（%s）：PATCH_RESOURCE_FOLLOWING 空置撤销——双成员重指派批准落表"
      disposition: "MGC（原体 P-MGC-BAKE-ADULT/RP1 重跑体 P-RP1-MGC-BAKE）-> GATED_COVER_TIER_CHAIN gate_axis bottom_zone 第 3 实例（v9 转正正式成员）；ONS（原体 P-B1-ONS-BAKE/RP1 重跑体 P-RP1-ONS-BAKE）-> SOFT_TRIPLE_TIER_CHAIN 第 2 成员（v9 转正，单成员 PROVISIONAL 升格）；known_instances 2 条原体记录=历史层保留（不删）"
      p06_deferred: "P06 压缩候选联动（HRQ-04/HRQ-B1-02 PENDING）不受影响——归并裁决另行处置（裁决 6-① 原文）"
      status_note: VACATED（活族计数移出——裁决 6：21->19 条目；后续重跑增减另计）""" % DEC,
    1,
    "PATCH vacated provenance",
)

rep(
    """    known_instances:
      - {batch: CENSUS-B0, program_id: P-MGC-BAKE-ADULT, blind_hash: 2b560452df77643f}
      - {batch: CENSUS-B1, program_id: P-B1-ONS-BAKE, blind_hash: 4e782a2e8b2440a4, note: "第 2 成员：context_type=current（急流石底绑定）；行为链 Evidence Open（confidence LOW）"}""",
    """    known_instances:
      # —— v8 历史快照层（裁决 6-① 空置：两成员经 RP1 重跑体转正他族——GATED_COVER_TIER_CHAIN/SOFT_TRIPLE_TIER_CHAIN）——
      - {batch: CENSUS-B0, program_id: P-MGC-BAKE-ADULT, blind_hash: 2b560452df77643f, note: "v9 已转正 GATED_COVER_TIER_CHAIN（gate_axis bottom_zone 第 3 实例）——RP1 重跑体 P-RP1-MGC-BAKE 承载成员资格"}
      - {batch: CENSUS-B1, program_id: P-B1-ONS-BAKE, blind_hash: 4e782a2e8b2440a4, note: "v9 已转正 SOFT_TRIPLE_TIER_CHAIN（第 2 成员）——RP1 重跑体 P-RP1-ONS-BAKE 承载成员资格；原注记：context_type=current（急流石底绑定）；行为链 Evidence Open（confidence LOW）"}""",
    1,
    "PATCH membership historical layer",
)

# ---------------------------------------------------------------------------
# F. SINGLE -> RETIRED
# ---------------------------------------------------------------------------
rep(
    """  - template_id: SINGLE_FACTOR_NORMALIZED_WEIGHT
    surface: Bake
    status: CANDIDATE""",
    """  - template_id: SINGLE_FACTOR_NORMALIZED_WEIGHT
    surface: Bake
    status: RETIRED""",
    1,
    "SINGLE status RETIRED",
)

rep(
    """    ir_pointer: batches/CENSUS-B1/run_merge_tests.py::CANONICALS.SINGLE_FACTOR_NORMALIZED_WEIGHT""",
    """    ir_pointer: batches/CENSUS-B1/run_merge_tests.py::CANONICALS.SINGLE_FACTOR_NORMALIZED_WEIGHT
    retired_provenance:
      ruling: "裁决 1-A（%s）：SINGLE v1 canonical 正式退役——RS1 61/61 有输入成员全 body 结构差异（0 匹配）+B4 饱和伪影根因在案（LOCAL_SATURATION_CANDIDATE 前提证伪——裁决 7 撤销）+渐进累积语义（语义裁定 1：无终步合并算子，NORMALIZE_WEIGHT 终步读法废止）"
      member_disposition: "61 moved 成员（RS1 重跑体 P-RS1-*）＝47 转正 9 链族（计数层面移出本族——链族 known_instances 已载：B1 6+B2 8+B3 16+B4 17）+14 slot_tiering（C8 追击型）经裁决 6-③ 转 truth_rebuild_queue（不在任何链族——HRQ-MUTATION-REV-001 F2 补正）；5 无 B 系列表达文件成员 evidence_insufficient_held：LAM[P-B1]/PIN[P-B3]/ASR+RVS+RDS[P-B4]——归 FR/表达线补证，不并入任何族（裁决 1-④）；本族 known_instances 原 66 条清单=v8 历史快照层（git b5088ab^ 可溯全文）"
      amb_chain: "B4 25+B5 52+B6 47+B7 110=234 AMB 四层链 -> truth_rebuild_queue.jsonl（终局全库顺序还原重跑输入清单；裁决 1-③）"
      status_note: RETIRED（非删除——证伪留册；重跑若复活单步平铺形需新证据新裁决）""" % DEC,
    1,
    "SINGLE retired provenance",
)

rep(
    """    known_instances:
      - {batch: CENSUS-B1, program_id: P-B1-GRB-BAKE, blind_hash: 7386b661fbf0c696}""",
    """    known_instances:
      # —— v8 历史快照层（66 名义：61 成员 v9 转正 9 链族[RS1 重跑体承载]+5 无文件成员 evidence_insufficient_held——裁决 1-A；SINGLE v1 证伪后本清单不计任何族的正式成员）——
      - {batch: CENSUS-B1, program_id: P-B1-GRB-BAKE, blind_hash: 7386b661fbf0c696}""",
    1,
    "SINGLE historical layer note",
)

rep(
    """      review: HRQ-RS1-01
  - template_id: CUE_GUIDED_APPROACH_AVOID""",
    """      review: HRQ-RS1-01（已裁决 2026-09-11：裁决 1-A 拆分确认+234 AMB 转重验队列——commit b5088ab）
  - template_id: CUE_GUIDED_APPROACH_AVOID""",
    1,
    "SINGLE review closed",
)

# ---------------------------------------------------------------------------
# G. 9 链族：review_queue 转正注记 + canonical 渐进累积重写 + order_provisional
#    + MGC/ONS 转正 + GUARD_ANCHOR 轴四形式对齐
# ---------------------------------------------------------------------------
rep(
    "      review_queue: HRQ-RS1-01/02\n",
    "      review_queue: HRQ-RS1-01/02（已裁决 2026-09-11：裁决 1-A 转正 CANDIDATE 确认+裁决 2-B 顺序=族判据——commit b5088ab）\n",
    7,
    "chain families review_queue closed (x7: TIERED/LAYER/GATED_COVER/NOCTURNAL/ZONE_SUBSTRATE/FILTER_FIELD/GUARD_ANCHOR)",
)
rep(
    "      review_queue: HRQ-RS1-02\n",
    "      review_queue: HRQ-RS1-02（已裁决 2026-09-11：裁决 1-A 转正 CANDIDATE 确认+裁决 2-B 顺序=族判据——commit b5088ab）\n",
    2,
    "chain families review_queue closed (x2)",
)

ORDER_PROV = """    order_provisional: true   # 裁决 2-B：因子判断顺序=族判据；本基础序为模板约定（B 系列表达文件序），成员真实序待终局逐鱼顺序推导（解析载体=重跑批范围声明：HRQ-MUTATION-001 batch_report §5-③；truth_rebuild_queue 仅为其 AMB/C8 输入子集，链族在册成员的入队属新裁决 HRQ-REBUILD-SCOPE-01 候选待裁——HRQ-MUTATION-REV-001 F5 补正）——真实序差异=族移动
"""

# TIERED_SINGLE
rep(
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(typed 因子三档分级命中：preferred=全额/tolerated=削减不清零/excluded=出局 EARLY_RETURN)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.TIERED_SINGLE_FACTOR_CHAIN""",
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(typed 因子三档分级命中——渐进累积语义[语义裁定 1]：
        preferred=全额乘入 running weight / tolerated=×衰减乘入 / excluded=×0.01 软出局乘入
        [非零、仍可参与下游——对齐 0.3.4.0 Bake DSL『return 0.01 * weight』；语义裁定 2：原『出局 EARLY_RETURN』措辞废止])
      -> [无终步合并算子：weight = weight × StepFit 逐步累积——单步链即终值（NORMALIZE_WEIGHT 终步经语义裁定 1 关闭）]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.TIERED_SINGLE_FACTOR_CHAIN
""" + ORDER_PROV,
    1,
    "TIERED_SINGLE canonical rewrite",
)

# LAYER_AXIS
rep(
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(水层带软三档定位)
      -> EVAL_TYPED_FIELD_OR_FACTOR(premise 绑定轴段归属三档)
      -> NORMALIZE_WEIGHT(LayerTier × AxisFit 积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.LAYER_AXIS_DUAL_TIER_CHAIN""",
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(水层带软三档定位——渐进累积语义：preferred=全额/tolerated=×衰减/excluded=×0.01 软出局，乘入 running weight)
      -> EVAL_TYPED_FIELD_OR_FACTOR(premise 绑定轴段归属三档——同上乘入)
      -> [渐进累积：weight = weight × LayerTierFit × AxisFit——无终步合并算子（原『积内归一化』读法经语义裁定 1 关闭）]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.LAYER_AXIS_DUAL_TIER_CHAIN
""" + ORDER_PROV,
    1,
    "LAYER_AXIS canonical rewrite",
)

# GATED_COVER
rep(
    """    canonical_program_body: |
      GATE_STRUCTURE_COVER_PRESENT(结构掩体存在门：不成立直接 EARLY_RETURN)
      -> EVAL_TYPED_FIELD_OR_FACTOR(掩体/质量档三档)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GATED_COVER_TIER_CHAIN""",
    """    canonical_program_body: |
      GATE_STRUCTURE_COVER_PRESENT(结构掩体存在门：不成立直接 EARLY_RETURN——门语义保留[二元门前出局，非三档出局])
      -> EVAL_TYPED_FIELD_OR_FACTOR(掩体/质量档三档——渐进累积语义：preferred=全额乘入/tolerated=×衰减乘入/excluded=×0.01 软出局乘入)
      -> [渐进累积：weight = weight × CoverTierFit——无终步合并算子]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GATED_COVER_TIER_CHAIN
""" + ORDER_PROV,
    1,
    "GATED_COVER canonical rewrite",
)

# NOCTURNAL
rep(
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(夜行底板栖息档三档：无夜行底板=出局 EARLY_RETURN)
      -> APPLY_DYNAMIC_SPATIAL_SLOT(低光/夜相槽三档：调整器语义——亮水=极低削减不清零，出局语义不落槽内；槽位=live §11.5 判例固定)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.NOCTURNAL_LIGHTSLOT_CHAIN""",
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(夜行底板栖息档三档——渐进累积语义[语义裁定 1/2]：preferred=全额乘入/tolerated=×衰减乘入/无夜行底板=×0.01 软出局乘入[原『出局 EARLY_RETURN』措辞对齐])
      -> APPLY_DYNAMIC_SPATIAL_SLOT(低光/夜相槽三档：调整器语义——亮水=极低削减不清零，出局语义不落槽内；槽位=live §11.5 判例固定；槽值乘入 running weight)
      -> [渐进累积：weight = weight × NightHabitatFit × LowlightSlotMod——无终步合并算子]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.NOCTURNAL_LIGHTSLOT_CHAIN
""" + ORDER_PROV,
    1,
    "NOCTURNAL canonical rewrite",
)

# ZONE_SUBSTRATE
rep(
    """    canonical_program_body: |
      GATE_ZONE(底层水层硬定位：非底层=EARLY_RETURN)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底栖资源档三档)
      -> NORMALIZE_WEIGHT(SubstrateTier × ResourceIntensity 积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_SUBSTRATE_RESOURCE_CHAIN""",
    """    canonical_program_body: |
      GATE_ZONE(底层水层硬定位：非底层=EARLY_RETURN——门语义保留)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档——渐进累积语义乘入 running weight)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底栖资源档三档——同上乘入)
      -> [渐进累积：weight = weight × SubstrateTierFit × ResourceIntensityFit——无终步合并算子（原『积内归一化』读法经语义裁定 1 关闭）]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_SUBSTRATE_RESOURCE_CHAIN
""" + ORDER_PROV,
    1,
    "ZONE_SUBSTRATE canonical rewrite",
)

# SOFT_TRIPLE
rep(
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(近底带水层软三档——无硬门)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(资源档三档)
      -> NORMALIZE_WEIGHT(三档积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.SOFT_TRIPLE_TIER_CHAIN""",
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(近底带水层软三档——无硬门；渐进累积语义乘入 running weight)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底质栖境档三档——同上乘入)
      -> EVAL_TYPED_FIELD_OR_FACTOR(资源档三档——同上乘入)
      -> [渐进累积：weight = weight × LayerTierFit × SubstrateTierFit × ResourceTierFit——无终步合并算子（原『三档积内归一化』读法经语义裁定 1 关闭）]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.SOFT_TRIPLE_TIER_CHAIN
""" + ORDER_PROV,
    1,
    "SOFT_TRIPLE canonical rewrite",
)

# ZONE_DEPTH
rep(
    """    canonical_program_body: |
      GATE_ZONE(底层水层硬定位)
      -> EVAL_TYPED_FIELD_OR_FACTOR(深度带档三档——本鱼独有步)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥栖境档三档)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥资源档三档)
      -> NORMALIZE_WEIGHT(三档积内归一化)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN""",
    """    canonical_program_body: |
      GATE_ZONE(底层水层硬定位：非底层=EARLY_RETURN——门语义保留)
      -> EVAL_TYPED_FIELD_OR_FACTOR(深度带档三档——本鱼独有步；渐进累积语义乘入 running weight)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥栖境档三档——同上乘入)
      -> EVAL_TYPED_FIELD_OR_FACTOR(底泥资源档三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子（原『三档积内归一化』读法经语义裁定 1 关闭）]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN
""" + ORDER_PROV,
    1,
    "ZONE_DEPTH canonical rewrite",
)

# FILTER_FIELD
rep(
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(滤食水层定位三档——携削减标记)
      -> EVAL_FOOD_FIELD_CONCENTRATION(场浓度三档：FieldSuitability 叠加衰减)
      -> EVAL_SIZE_GAUGE_MATCH(个体口径三档：口径不匹配=出局)
      -> NORMALIZE_WEIGHT(步间折减合成算子 OPERATOR UNDEFINED 待机制侧)
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.FILTER_FIELD_ACCUMULATE_CHAIN""",
    """    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(滤食水层定位三档——携削减标记；渐进累积语义乘入 running weight)
      -> EVAL_FOOD_FIELD_CONCENTRATION(场浓度三档：FieldSuitability 叠加衰减——乘入 running weight)
      -> EVAL_SIZE_GAUGE_MATCH(个体口径三档：口径不匹配=×0.01 软出局乘入[原『出局』措辞对齐语义裁定 1/2]——乘入 running weight)
      -> [渐进累积：weight 逐步乘入——『步间折减合成算子 OPERATOR UNDEFINED』占位经语义裁定 1 关闭：乘法逐步进行，无终点合并步骤]
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.FILTER_FIELD_ACCUMULATE_CHAIN
""" + ORDER_PROV,
    1,
    "FILTER_FIELD canonical rewrite",
)

# GUARD_ANCHOR（Bake 面）：canonical 重写 + anchor_type 轴四形式对齐
rep(
    """    canonical_program_body: |
      GATE_ANCHOR_EXISTENCE(锚存在门：锚域外=EARLY_RETURN 非「算出低值」)
      -> EVAL_ANCHOR_SUITABILITY(锚适配三档)
      -> EVAL_ANCHOR_RELATION(守卫关系三档)
      -> EVAL_LOCAL_TEMPERATURE(局部温度三档)
      -> COMBINE_GUARD_FACTORS(算子 OPERATOR UNDEFINED 待机制侧)
      -> Guarding SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GUARD_ANCHOR_TIERED_COMBINE_CHAIN
    allowed_parameter_axes:
      - anchor_type(typed: colony_nest | floodplain_fry_school | root_spawn_eggs | pebble_mound——与 Response 面 GUARD anchor 轴同源第 4-7 值；HRQ-RS1-02 待批)""",
    """    canonical_program_body: |
      GATE_ANCHOR_EXISTENCE(锚存在门：锚域外=EARLY_RETURN 非「算出低值」——门语义保留)
      -> EVAL_ANCHOR_SUITABILITY(锚适配三档——渐进累积语义乘入 running weight)
      -> EVAL_ANCHOR_RELATION(守卫关系三档——同上乘入)
      -> EVAL_LOCAL_TEMPERATURE(局部温度三档——同上乘入)
      -> [渐进累积：weight = weight × SuitabilityFit × RelationFit × TempFit——COMBINE_GUARD_FACTORS 终步合并算子经语义裁定 1 关闭（无终点合并步骤）]
      -> Guarding SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.GUARD_ANCHOR_TIERED_COMBINE_CHAIN
""" + ORDER_PROV + """    allowed_parameter_axes:
      - anchor_type(typed: nest | egg_mass | fry_school | host_brood——四形式[裁决 4-A]；v8 原值映射：colony_nest->nest / floodplain_fry_school->fry_school / root_spawn_eggs->egg_mass / pebble_mound->nest；与 Response 面 GUARD anchor 轴同源对齐[18-vs-19 口径经裁决 4 关闭])""",
    1,
    "GUARD_ANCHOR canonical rewrite + axis four-forms",
)

# GUARD_ANCHOR known_instances 转正注记
rep(
    """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-ARA-BAKE, P-RS1-RBP-BAKE, P-RS1-HNC-BAKE], note: "engine 零差异（4 锚型）；HNC pebble_mound 与 HRQ-B4-01 Response 面提案同值"}""",
    """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-ARA-BAKE, P-RS1-RBP-BAKE, P-RS1-HNC-BAKE], note: "engine 零差异（4 锚型）；v9 四形式对齐：colony_nest[BLU]->nest / floodplain_fry_school[ARA]->fry_school / root_spawn_eggs[RBP]->egg_mass / pebble_mound[HNC]->nest（pebble_mound 口径经裁决 4 关闭；HNC 与 HRQ-B4-01 Response 面提案同源）"}""",
    1,
    "GUARD_ANCHOR members four-forms note",
)

# GATED_COVER：MGC 转正
rep(
    """      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-MGC-BAKE, note: "重指派提案 pending HRQ-RP1-02：PATCH 族 canonical 源成员 MGC 顺序还原门先行形（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE）；gate_axis=bottom_zone 第 3 实例（AST/SNS 同值）；engine raw=门/tier 字面（B/O/P），语义 MC——伏击门 9 例同型；批准前不计正式成员"}""",
    """      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-MGC-BAKE, note: "v9 转正正式成员（裁决 6-① 批准重指派）：PATCH 族 canonical 源成员 MGC 顺序还原门先行形（GATE_ZONE→EVAL_RESOURCE_PATCH→渐进累积）；gate_axis=bottom_zone 第 3 实例（AST/SNS 同值）；engine raw=门/tier 字面（B/O/P），语义 MC——伏击门 9 例同型；原体 P-MGC-BAKE-ADULT 见 PATCH 族历史层"}""",
    1,
    "GATED_COVER MGC promoted",
)

# SOFT_TRIPLE：ONS 转正 + provisional_note 升格
rep(
    """      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-ONS-BAKE, note: "重指派提案 pending HRQ-RP1-02：PATCH 族 ONS 顺序还原三档×3 链（流速档[含过渡削减带]/石底档/附着资源档+三值积归一化；deps 位形全同语义 MC——GATE_CURRENT 为文件原标签、分支语义=IF3 非二元门）；族 1→2 跨科独立重复（BSK 吸口形 vs ONS 急流刮食形）——单成员 PROVISIONAL 升格候选；批准前不计正式成员"}""",
    """      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-ONS-BAKE, note: "v9 转正正式成员（裁决 6-① 批准重指派）：PATCH 族 ONS 顺序还原三档×3 链（流速档[含过渡削减带]/石底档/附着资源档——渐进累积；deps 位形全同语义 MC——GATE_CURRENT 为文件原标签、分支语义=IF3 非二元门）；族 1→2 跨科独立重复（BSK 吸口形 vs ONS 急流刮食形）；原体 P-B1-ONS-BAKE 见 PATCH 族历史层"}""",
    1,
    "SOFT_TRIPLE ONS promoted",
)

rep(
    """    provisional_note: 单成员 PROVISIONAL（Tier B CSV benthopelagic 软定位推导，硬定位与否 [需正文]——正文证实硬定位则并入 ZONE_SUBSTRATE 族）；RP1 后 2 成员候选（+ONS pending HRQ-RP1-02）——批准后升格""",
    """    provisional_note: v9 升格双成员族（裁决 6-① 批准 ONS 重指派）：BSK 单成员 PROVISIONAL 沿革（Tier B CSV benthopelagic 软定位推导，硬定位与否 [需正文]——正文证实硬定位则并入 ZONE_SUBSTRATE 族，待终局重跑）；ONS 转正第 2 成员（跨科独立重复）——成员真实序 order_provisional 复核归重跑""",
    1,
    "SOFT_TRIPLE provisional note update",
)

# ZONE_DEPTH 单成员 provisional_note 保留（RS1-02 已裁决转正，正文核证仍归重跑）——不动

# EXTREME_TEMP：语义裁定 1 canonical 对齐（status/HRQ-RP1-02 保持 pending——决策日志未裁，仅语义裁定适用）
rep(
    """    canonical_program_body: |
      GATE_EXTREME_TEMP(极值水温硬门：末位算术门还原为前置出局——极值带=EARLY_RETURN)
      -> EVAL 因子×4 unordered（静水/结构/猎物/时段——因子间顺序=证据未裁决 unordered 原样；
         各三档分级命中，排除档=EARLY_RETURN——EXIT 语义非 PLAIN 槽值出局）
      -> COMBINE_WEIGHTED(算子 OPERATOR UNDEFINED 待机制侧)
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN""",
    """    canonical_program_body: |
      GATE_EXTREME_TEMP(极值水温硬门：末位算术门还原为前置出局——极值带=EARLY_RETURN[门语义保留])
      -> EVAL 因子×4 unordered（静水/结构/猎物/时段——因子间顺序=证据未裁决 unordered 原样；
         各三档分级命中——渐进累积语义[语义裁定 1/2]：preferred=全额乘入/tolerated=×衰减乘入/
         排除档=×0.01 软出局乘入[非零、仍可参与下游——原『EARLY_RETURN』措辞对齐；EXIT 档语义非 PLAIN 槽值出局])
      -> [渐进累积：weight 逐步乘入四因子——无终步 COMBINE_WEIGHTED（合并算子占位经语义裁定 1 关闭）]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN
    order_provisional: true   # 因子集 unordered=证据态；终局逐鱼推导后若序有据则分化（裁决 2-B）""",
    1,
    "EXTREME_TEMP canonical semantic alignment",
)

# PATCH_GATED_DUAL：同上语义对齐
rep(
    """    canonical_program_body: |
      GATE_PATCH_PRESENCE(patch 存在性门：无 patch=EARLY_RETURN——竞争占位对象存在性先行)
      -> EVAL_RESOURCE_PATCH(patch 强度档三档：近零档=出局 EARLY_RETURN)
      -> EVAL_RANK_POSITION_PREFERENCE(core-vs-edge 三档：优势=中心全额/中间=削减/次级=边缘带占位
         更低削减不清零——出局落槽值非 EARLY_RETURN)
      -> COMBINE_WEIGHTED(算子 OPERATOR UNDEFINED 待机制侧)
      -> SpatialDistributionWeight（无归一化步——族边界）
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN""",
    """    canonical_program_body: |
      GATE_PATCH_PRESENCE(patch 存在性门：无 patch=EARLY_RETURN——竞争占位对象存在性先行[门语义保留])
      -> EVAL_RESOURCE_PATCH(patch 强度档三档——渐进累积语义[语义裁定 1/2]：近零档=×0.01 软出局乘入[原『出局 EARLY_RETURN』措辞对齐]，乘入 running weight)
      -> EVAL_RANK_POSITION_PREFERENCE(core-vs-edge 三档：优势=中心全额乘入/中间=×衰减乘入/次级=边缘带占位
         更低削减不清零——槽值乘入[出局不落槽内，族域边界保持])
      -> [渐进累积：weight = weight × PatchIntensityFit × RankPositionFit——无终步 COMBINE_WEIGHTED（合并算子占位经语义裁定 1 关闭）；无归一化步（族边界保留）]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN
    order_provisional: true   # 双槽序=RP1 重跑证据态；终局逐鱼推导复核（裁决 2-B）""",
    1,
    "PATCH_GATED_DUAL canonical semantic alignment",
)

print(f"patch count: {len(patches)}")

# ---------------------------------------------------------------------------
# H. TYPED：known_instances 名义入册 74->248 + MGC reconciliation note
# ---------------------------------------------------------------------------
rep(
    '''      - {batch: CENSUS-B4, program_id: [P-B4-POR-RESP, P-B4-SDG-RESP, P-B4-TSK-RESP, P-B4-ASR-RESP, P-B4-RVS-RESP, P-B4-GPF-RESP, P-B4-RKB-RESP, P-B4-SSL-RESP, P-B4-BSK-RESP, P-B4-RRH-RESP, P-B4-GRH-RESP, P-B4-SMB-RESP, P-B4-GDE-RESP, P-B4-WIT-RESP, P-B4-WIN-RESP, P-B4-YTF-RESP, P-B4-SMF-RESP, P-B4-BST-RESP, P-B4-FDR-RESP, P-B4-BSB-RESP, P-B4-CBM-RESP, P-B4-SAI-RESP, P-B4-MOO-RESP, P-B4-RDS-RESP], note: "24 标准成员；强实例：SDG+TSK evaluator_channel=PASSIVE_ELECTROSENSE 第 2/3 例（FR3 判例① K8 感知端）/ POR 温血第 2 例 / GDE+CBM 夜行+WIN 日间低光 typed context（R03 教训不买 Mode）/ SMB 咽喉骨板磿碎机制 typed 事实（草鱼 R02 先例）/ RDS 贝食偏好原文；MEDIUM 推算 6 例（RVS+MOO=P01 冻结主张承载 / GPF+RKB=齿板喙齿形态 / BSK=吸口形态 / SMF=掘穴栖息）"}''',
    '''      - {batch: CENSUS-B4, program_id: [P-B4-POR-RESP, P-B4-SDG-RESP, P-B4-TSK-RESP, P-B4-ASR-RESP, P-B4-RVS-RESP, P-B4-GPF-RESP, P-B4-RKB-RESP, P-B4-SSL-RESP, P-B4-BSK-RESP, P-B4-RRH-RESP, P-B4-GRH-RESP, P-B4-SMB-RESP, P-B4-GDE-RESP, P-B4-WIT-RESP, P-B4-WIN-RESP, P-B4-YTF-RESP, P-B4-SMF-RESP, P-B4-BST-RESP, P-B4-FDR-RESP, P-B4-BSB-RESP, P-B4-CBM-RESP, P-B4-SAI-RESP, P-B4-MOO-RESP, P-B4-RDS-RESP], note: "24 标准成员；强实例：SDG+TSK evaluator_channel=PASSIVE_ELECTROSENSE 第 2/3 例（FR3 判例① K8 感知端）/ POR 温血第 2 例 / GDE+CBM 夜行+WIN 日间低光 typed context（R03 教训不买 Mode）/ SMB 咽喉骨板磿碎机制 typed 事实（草鱼 R02 先例）/ RDS 贝食偏好原文；MEDIUM 推算 6 例（RVS+MOO=P01 冻结主张承载 / GPF+RKB=齿板喙齿形态 / BSK=吸口形态 / SMF=掘穴栖息）"}
      # —— v9 名义入册（裁决 7-A 簿记打包）：B5-B7 MC[typed] 174 例挂账转正 74->248；判同细节权威=各批 merge_tests.jsonl ——
      - {batch: CENSUS-B5, program_id: TYPED_B5_PLACEHOLDER, note: "43 标准成员（R08+R09 普通层双包合批；R09 身份层 4 例处理见 B5 批档）"}
      - {batch: CENSUS-B6, program_id: TYPED_B6_PLACEHOLDER, note: "45 标准成员（FISH-R10 全库收官批——十节压缩四节形消费）"}
      - {batch: CENSUS-B7, program_id: TYPED_B7_PLACEHOLDER, note: "86 标准成员（R01-R05 残余基线收尾）——field-vs-typed 14 对经 RETURN 硬判据分流入 FOOD_FIELD"}''',
    1,
    "TYPED membership B5-B7",
)

rep(
    '''      - {batch: CENSUS-B3, template_id: STATE_GATED_MULTI_PATH_RESPONSE, reason: "反向互记：BRANCH（状态 IF 门）+COMBINE+RETURN（TargetFeeding|NonFeedingStrike）真差异——停食洄游双 Path（FR3 判例①）"}''',
    '''      - {batch: CENSUS-B3, template_id: STATE_GATED_MULTI_PATH_RESPONSE, reason: "反向互记：BRANCH（状态 IF 门）+COMBINE+RETURN（TargetFeeding|NonFeedingStrike）真差异——停食洄游双 Path（FR3 判例①）"}
    v9_notes:
      nominal_membership: "74->248（B5 43+B6 45+B7 86——裁决 7-A 名义入册；batch_report 计数对账）"
      mgc_reconciliation_note: "reconciliation-note（待重跑对齐——HRQ-B7-03 谱系/裁决 7 打包小项）：B0 MGC（P-MGC-RESP-FEEDING）以 TYPED evaluator_channel 轴处理 food-field 型行为（B0 旧口径=FieldFeeding 按 TYPED premise/通道处理）；B2 起 FOOD_FIELD_FEEDING_RESPONSE 立族（field evaluand+FieldFeeding RETURN 硬判据，B2/B7 两批独立复证）——两口径不一致；MGC 真形待终局重跑重判（可能移族，不预判）"''',
    1,
    "TYPED v9 notes + MGC reconciliation",
)

# ---------------------------------------------------------------------------
# I. FOOD_FIELD：known_instances 2->16
# ---------------------------------------------------------------------------
rep(
    '''      - {batch: CENSUS-B2, program_id: P-B2-HER-RESP-FIELD, blind_hash: 9d8f33094b9b4afe}
    known_non_matches:''',
    '''      - {batch: CENSUS-B2, program_id: P-B2-HER-RESP-FIELD, blind_hash: 9d8f33094b9b4afe}
      # —— v9 名义入册（裁决 7-A）：B7 MC[field] 14 例挂账转正 2->16 ——
      - {batch: CENSUS-B7, program_id: FIELD_B7_PLACEHOLDER, note: "14 标准成员（field evaluand+FieldFeeding RETURN 硬判据——B2 立族判例第 2 批独立复证[field-vs-typed 分组 14 对]；R01/R02 残余移动/近岸潮流/繁殖窗等饵场形态——实例注记见 B7 批档 FIELD_DETAIL）"}
    known_non_matches:''',
    1,
    "FOOD_FIELD membership B7",
)

# ---------------------------------------------------------------------------
# J. GUARD（Response 面）：anchor 四形式轴 + participant 轴 + 28 名义重排
# ---------------------------------------------------------------------------
GUARD_OLD = """    allowed_parameter_axes:
      - intruder_evaluator_context(typed：nest_anchor | fry_anchor | foam_nest[B0-FIX] | sand_nest[B3, pending HRQ-B3-02] | tree_root_eggs[B3, pending HRQ-B3-02] | male_built_nest[B3, pending HRQ-B3-02] | pebble_mound[B4 提案, pending HRQ-B4-01])   # B3-F-3 修正（CENSUS-B4）：原声明仅 2 值与 known_instances 6 anchor 实例漂移，现对齐并标注审批态
      - guard_target_specificity(typed：species_typed_intruder[B4 提案, pending HRQ-B4-01] | any_intruder[B0-B3 默认未显式分型])   # NEW 轴提案（HRQ-B4-01）
      - path_strength_weights
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-B0, program_id: P-OSC-RESP-GUARD, blind_hash: 50945342e27abd5c, role: canonical_source}
      - {batch: CENSUS-B0, program_id: P-LUN-RESP-GUARD, blind_hash: b2594d9e1eefa015}
      - {batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-GUARD, blind_hash: null, note: "修复轮非盲补录（EEL S6 泡沫巢雄护）：第三成员，engine 直验与 canonical 无字面差异；intruder_evaluator_context=foam_nest"}
      - {batch: CENSUS-B1, program_id: P-B1-DIS-RESP-GUARD, blind_hash: 585905b944bd66d6, note: "第 4 成员（七彩神仙育幼黏液喂养）：engine 无字面差异；fry_anchor=幼鱼群；色型不分裂（S12 对照不建体）"}
      - {batch: CENSUS-B3, program_id: P-B3-ARA-RESP, blind_hash: 5f3f40e142fffa81, note: "第 5 成员（巨骨舌鱼洪水护巢）：anchor=沙巢+护卵护幼；换气暴露 runtime premise（TAR-11）；engine raw 仅槽名/合并步标名字面差异"}
      - {batch: CENSUS-B3, program_id: P-B3-RBP-RESP, blind_hash: cf001f79596b2729, note: "第 6 成员（红腹食人鱼树根护卵）：anchor=tree_root_eggs；群游=防御 Negative Knowledge（FR3 判例②）已排除 Group"}
      - {batch: CENSUS-B3, program_id: P-B3-WEL-RESP, blind_hash: 2b938a5ca14665e4, note: "第 7 成员（欧洲巨鲶雄巢守护）：anchor=male_built_nest；听嗅主导+夜行 typed context premise"}
      - {batch: CENSUS-B4, program_id: P-B4-HNC-RESP, blind_hash: fb17fdf2f57dbadf, note: "第 8 成员（双点美鱥石巢守护）extension 候选挂账：anchor=pebble_mound（轴值提案）+guard_target_specificity=species_typed_intruder（NEW 轴提案——『defend…from other N. biguttatus males but not other species』逐字；异种借巢被容忍）；骨架同构（engine raw 仅槽名/合并步标名字面）；TEMPLATE_EXTENSION_CANDIDATE pending HRQ-B4-01——批准前不计正式成员"}"""


def h(d, pid):
    v = d.get(pid)
    return "null" if v is None else str(v)


GUARD_NEW = f"""    allowed_parameter_axes:
      - anchor(typed：后代空间存在形式——四值+一边界[裁决 4-A 四形式方案]：nest[构建型巢体：石巢/砾脊合一/pebble_mound/泡沫巢/殖民巢/清巢] | egg_mass[利用型附着：岩缝/洞顶/岩面/树根——底质差异归 suitability] | fry_school[移动稚鱼群] | host_brood[蚌宿主]；brooded[口孵/体内携带]=结构级退化链不入本族——待真形重跑终裁[ARO 银龙口哺/TIL3 罗非退化链先例])   # v9 重写：原 intruder_evaluator_context 6+1 值与 18 候选收敛为四形式（轴膨胀根因=四维度塞一轴——关注项经裁决 4 关闭）
      - guard_participant(typed：male | biparental——谁守独立成轴[裁决 4-A 配套拆解规则]；未记录成员不虚构——终局重跑补全)
      - guard_target_specificity(typed：species_typed_intruder[B4 提案, pending HRQ-B4-01] | any_intruder[B0-B3 默认未显式分型])   # NEW 轴提案（HRQ-B4-01）——anchor 四形式裁决未涉及，维持 pending
      - path_strength_weights
      - guard_action_notes(注记字段非分支轴[裁决 4-A 配套拆解规则]：怎么守->Response 动作[fan 扇护/黏液喂养]；位相->DynamicSpatialSlot；停食->premise[fasting]；底质->@NestStructureSet 路由 C3+suitability Profile——轴不重复记账；GuardAnchorResolverInstance 字段保留细名：实例管场内定位，轴值管语义分类)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next]
    helper_dependencies: []
    resolver_dependencies: []
    four_form_disposition:
      ruling: "裁决 4-A（{DEC}）：落位表点名成员照录（石巢脊->nest/洪水->fry_school+slot/洞顶->egg_mass+suitability/卵块->egg_mass/岩缝扇护->egg_mass+fan/双亲巢->nest+participant/狼鱼->egg_mass+premise[fasting]/贝内->host_brood/口孵->待重跑/pebble_mound->nest/discus_mucus->fry_school+注记）；未点名成员（CSL/ROB/CRA2/SMA1/BLU2/CCF2/CSN1/BBR1）按四形式定义直接分类——独立审复核点"
      counts: "28 名义=既有 8（含 HNC 挂账转正）+挂账 20（B5 9+B6 2+B7 9）；四形式正式 24[nest 12/egg_mass 7/fry_school 3/host_brood 2]+brooded 挂起 2[ARO/TIL3——结构级退化链边界成员不计四形式轴值，待真形重跑终裁]+form-hold 挂起 2[CSL/CSN1——冻结证据无巢/构建判别词（HRQ-MUTATION-REV-001 F1），待真形重跑终裁]"
    known_instances:
      # —— v9 四形式重排（裁决 4-A）：anchor=语义分类；原细名保留于 note（GuardAnchorResolverInstance 场内定位）——
      - {{batch: CENSUS-B0, program_id: P-OSC-RESP-GUARD, blind_hash: 50945342e27abd5c, role: canonical_source, anchor: nest, participant: biparental, note: "地图鱼双亲护巢（B0 story Biparental-Guard 标题直证）；细名 nest_anchor->nest"}}
      - {{batch: CENSUS-B0, program_id: P-LUN-RESP-GUARD, blind_hash: b2594d9e1eefa015, anchor: nest, note: "南美肺鱼守巢；B0 v1 轴声明 2 值时代未逐成员记录细名——nest_anchor->nest 按四形式映射（独立审可核）"}}
      - {{batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-GUARD, blind_hash: null, anchor: nest, participant: male, note: "修复轮非盲补录（EEL S6 泡沫巢雄护）：第三成员，engine 直验与 canonical 无字面差异；细名 foam_nest->nest（泡沫巢=构建型）"}}
      - {{batch: CENSUS-B1, program_id: P-B1-DIS-RESP-GUARD, blind_hash: 585905b944bd66d6, anchor: fry_school, participant: biparental, note: "第 4 成员（七彩神仙育幼黏液喂养）：细名 fry_anchor（幼鱼群）->fry_school；黏液喂养=guard_action_notes（Response 动作）；色型不分裂（S12 对照不建体）——DIS2 白色型并入本值"}}
      - {{batch: CENSUS-B3, program_id: P-B3-ARA-RESP, blind_hash: 5f3f40e142fffa81, anchor: nest, participant: male, note: "第 5 成员（巨骨舌鱼洪水护巢）：细名 sand_nest（沙巢）->nest（构建型底质巢）；换气暴露 runtime premise（TAR-11）保留；engine raw 仅槽名/合并步标名字面差异"}}
      - {{batch: CENSUS-B3, program_id: P-B3-RBP-RESP, blind_hash: cf001f79596b2729, anchor: egg_mass, note: "第 6 成员（红腹食人鱼树根护卵）：细名 tree_root_eggs->egg_mass（利用型附着：树根）；群游=防御 Negative Knowledge（FR3 判例②）已排除 Group"}}
      - {{batch: CENSUS-B3, program_id: P-B3-WEL-RESP, blind_hash: 2b938a5ca14665e4, anchor: nest, participant: male, note: "第 7 成员（欧洲巨鲶雄巢守护）：细名 male_built_nest->nest+participant(male)；听嗅主导+夜行 typed context premise 保留"}}
      - {{batch: CENSUS-B4, program_id: P-B4-HNC-RESP, blind_hash: fb17fdf2f57dbadf, anchor: nest, note: "第 8 成员（双点美鱥石巢守护）：细名 pebble_mound->nest（裁决 4：18-vs-19 口径关闭——构建型）；guard_target_specificity=species_typed_intruder 维持 HRQ-B4-01 pending（『defend…from other N. biguttatus males but not other species』逐字；异种借巢被容忍）；骨架同构（engine raw 仅槽名/合并步标名字面）"}}
      # —— B5 挂账 9 例转正（裁决 4-A 落位；HRQ-B5-02 关闭）——
      - {{batch: CENSUS-B5, program_id: P-B5-ARO-RESP, blind_hash: {h(BH5, 'P-B5-ARO-RESP')}, anchor: brooded, membership: pending_truth_rebuild, note: "银龙雄口哺携带卵/幼近 6 周——落位表『口孵->待重跑（退化链候选）』+裁决 4 brooded 边界（结构级退化链不入本族）：anchor 轴值挂起不计四形式，待真形重跑终裁；水面跳捕 P01 面另行"}}
      - {{batch: CENSUS-B5, program_id: P-B5-CSL-RESP, blind_hash: {h(BH5, 'P-B5-CSL-RESP')}, anchor: form_hold, membership: pending_truth_rebuild, note: "细名 nest_pelagic_larvae（雄护卵+浮游幼体跨两发育阶段）——冻结 premise/story 无巢/构建判别词，四形式证据不足不虚构（HRQ-MUTATION-REV-001 F1）：anchor 形式挂起，待真形重跑以 B 系列证据终裁；浮游幼体期 fry_school 语义注记保留"}}
      - {{batch: CENSUS-B5, program_id: P-B5-CRC-RESP, blind_hash: {h(BH5, 'P-B5-CRC-RESP')}, anchor: nest, participant: male, note: "细名 gravel_ridge（雄砾巢脊连续建造：挖坑->覆石->紧邻下游再挖成脊）——落位表『石巢脊->nest』（stone_nest/gravel_ridge 合一）"}}
      - {{batch: CENSUS-B5, program_id: P-B5-ROB-RESP, blind_hash: {h(BH5, 'P-B5-ROB-RESP')}, anchor: nest, participant: male, note: "细名 rock_nest_fan（雄岩巢扇护+防御复合约 14 天）——岩巢构建型->nest；fan 供氧子动作=guard_action_notes（Response 动作注记，裁决 4 拆解规则）"}}
      - {{batch: CENSUS-B5, program_id: P-B5-MDC-RESP, blind_hash: {h(BH5, 'P-B5-MDC-RESP')}, anchor: egg_mass, note: "细名 cave_ceiling（洞顶产卵——产卵位垂直面选择）——落位表『洞顶->egg_mass+suitability』（底质差异归 suitability Profile）"}}
      - {{batch: CENSUS-B5, program_id: P-B5-JGC-RESP, blind_hash: {h(BH5, 'P-B5-JGC-RESP')}, anchor: nest, participant: biparental, note: "细名 nest_biparental（浊水湖巢）——落位表『双亲巢->nest+participant(biparental)』（guard_participant 轴首批实例之一，跨属双亲例）"}}
      - {{batch: CENSUS-B5, program_id: P-B5-JDP-RESP, blind_hash: {h(BH5, 'P-B5-JDP-RESP')}, anchor: fry_school, participant: male, note: "细名 flood_spawn_male_guard（洪水事件机会繁殖+雄护卵复合）——落位表『洪水护卵群->fry_school+slot』：洪水位相=DynamicSpatialSlot 注记（guard_action_notes）"}}
      - {{batch: CENSUS-B5, program_id: P-B5-LMP-RESP, blind_hash: {h(BH5, 'P-B5-LMP-RESP')}, anchor: egg_mass, note: "细名 egg_mass_rock（附着卵块激进守护——非巢结构型无建造行为）——落位表『卵块->egg_mass』"}}
      - {{batch: CENSUS-B5, program_id: P-B5-AMK-RESP, blind_hash: {h(BH5, 'P-B5-AMK-RESP')}, anchor: egg_mass, participant: male, note: "细名 rock_crevice_fan（岩缝产卵+胸鳍连续扇护 40-45 天）——落位表『岩缝扇护->egg_mass+Response(fan)』：fan=guard_action_notes"}}
      # —— B6 挂账 2 例转正（裁决 4-A 落位；HRQ-B6-02 关闭）——
      - {{batch: CENSUS-B6, program_id: P-B6-AWF-RESP, blind_hash: {h(BH6, 'P-B6-AWF-RESP')}, anchor: egg_mass, participant: male, note: "细名 wolf_egg_mass_fasting_guard（雄鱼守护卵块直至孵化+护卵期几乎不进食）——落位表『狼鱼->egg_mass+premise(fasting)』：停食=premise 注记（guard_action_notes）；硬壳碾压摄食并行"}}
      - {{batch: CENSUS-B6, program_id: P-B6-LFB-RESP, blind_hash: {h(BH6, 'P-B6-LFB-RESP')}, anchor: host_brood, note: "细名 mussel_brood（产卵管贝内产卵+幼贝内发育）——落位表『贝内产卵->host_brood』；鳑鲏 R03 先例；RSB（B7）为跨属复现实证"}}
      # —— B7 挂账 9 例转正（裁决 4-A 落位；HRQ-B7-02 关闭）——
      - {{batch: CENSUS-B7, program_id: P-B7-BBR1-RESP, blind_hash: {h(BH7, 'P-B7-BBR1-RESP')}, anchor: egg_mass, note: "细名 bullhead_cave_night_guard（洞巢护卵+夜间底栖嗅觉取食）——四形式直接分类：洞巢=利用型洞穴->egg_mass+suitability（洞巢）[未点名成员，独立审复核点]；昼夜时窗=premise 非结构；P01+P04 组合注记保留"}}
      - {{batch: CENSUS-B7, program_id: P-B7-BLU2-RESP, blind_hash: {h(BH7, 'P-B7-BLU2-RESP')}, anchor: nest, participant: male, note: "细名 bluegill_nest_guard_forage_overlap（护巢+父本食卵+巢区小饵双意义并存）——巢守护构建型->nest[未点名成员，独立审复核点]；filial cannibalism 双意义结算政策未定注记保留"}}
      - {{batch: CENSUS-B7, program_id: P-B7-CCF2-RESP, blind_hash: {h(BH7, 'P-B7-CCF2-RESP')}, anchor: egg_mass, participant: male, note: "细名 channel_cave_guard（洞巢雄鱼照护+受扰食卵）——洞巢=利用型->egg_mass+suitability（洞巢）[未点名成员，独立审复核点]；Semantic Open 置信如实保留（照护->lure-defense 映射无可靠证据）"}}
      - {{batch: CENSUS-B7, program_id: P-B7-CRA2-RESP, blind_hash: {h(BH7, 'P-B7-CRA2-RESP')}, anchor: nest, participant: male, note: "细名 black_crappie_nest_guard（雄鱼筑巢护卵至孵化——本种证据实证不再同科猜测）——筑巢构建型->nest[未点名成员，独立审复核点]；Semantic Open 保留（对玩家饵的冲突路径尚待行为证据）"}}
      - {{batch: CENSUS-B7, program_id: P-B7-CSN1-RESP, blind_hash: {h(BH7, 'P-B7-CSN1-RESP')}, anchor: form_hold, membership: pending_truth_rebuild, note: "细名 snakehead_brood_guard（繁殖期亲鱼守护卵幼+植被伏击捕食双语境）——冻结 premise/story 无浮巢/筑巢判别词，『浮巢构建型』系册外知识注入（HRQ-MUTATION-REV-001 F1）：anchor 形式挂起，待真形重跑以 B 系列证据终裁；护幼期 fry_school 语义注记保留；P01 伏击+P04 组合注记保留"}}
      - {{batch: CENSUS-B7, program_id: P-B7-DIS2-RESP, blind_hash: {h(BH7, 'P-B7-DIS2-RESP')}, anchor: fry_school, participant: biparental, note: "白神仙色型（色型不分裂——并入 B1-DIS 同值）；提案 discus_mucus_brood 与 fry_anchor 覆盖关系经裁决 4 关闭->fry_school+guard_action_notes（黏液喂养=Response 动作）；Low 证据（色型压缩）注记保留"}}
      - {{batch: CENSUS-B7, program_id: P-B7-RSB-RESP, blind_hash: {h(BH7, 'P-B7-RSB-RESP')}, anchor: host_brood, note: "细名 bitterling_mussel_brood（卵产入活蚌鳃腔+贝内发育）——host_brood（mussel_brood 语义并入 B6 LFB 同值）：鳑鲏科跨属第 2 实证；Relation Object 语义（非新捕食/资源程序）；产卵管=产卵工具行为变量非 branch"}}
      - {{batch: CENSUS-B7, program_id: P-B7-SMA1-RESP, blind_hash: {h(BH7, 'P-B7-SMA1-RESP')}, anchor: nest, note: "细名 smallmouth_nest_fry_guard（巢与幼鱼守护+营养竞争语境）——按初始存在形式落 nest+跨阶段注记[稚鱼期 fry_school 语义；主形式待终局重跑——未点名成员，独立审复核点]；2009 饱食/2016 补食实验注记保留"}}
      - {{batch: CENSUS-B7, program_id: P-B7-TIL3-RESP, blind_hash: {h(BH7, 'P-B7-TIL3-RESP')}, anchor: brooded, membership: pending_truth_rebuild, note: "细名 tilapia_territory（雄鱼繁殖领地——雌鱼取卵离巢口孵，领地与幼体非同一关系对象）——裁决 4 brooded 边界点名『罗非退化链先例』：结构级退化链待真形重跑终裁，anchor 轴值挂起不计四形式；Semantic Open（领地 vs 护巢轴内一致性）随重跑重审"}}"""

rep(GUARD_OLD, GUARD_NEW, 1, "GUARD four-forms rewrite")

# 占位符替换（超长 id 列表注入）
patches_final = []
for old, new, count, tag in patches:
    new = new.replace("TYPED_B5_PLACEHOLDER", TYPED_B5)
    new = new.replace("TYPED_B6_PLACEHOLDER", TYPED_B6)
    new = new.replace("TYPED_B7_PLACEHOLDER", TYPED_B7)
    new = new.replace("FIELD_B7_PLACEHOLDER", FIELD_B7)
    patches_final.append((old, new, count, tag))

# ---------------------------------------------------------------------------
# 应用（锚点断言唯一 -> 依序替换）
# ---------------------------------------------------------------------------
new_text = text
for old, new, count, tag in patches_final:
    n = new_text.count(old)
    assert n == count, "ANCHOR FAIL [%s]: expected %d occurrence(s), found %d" % (tag, count, n)
    new_text = new_text.replace(old, new)
    print("  ok  " + tag)

# YAML 语法自检（通过后才写盘——防半成品落盘）
import yaml
data = yaml.safe_load(new_text)
assert data["version"] == 9, "version must be 9 after mutation"
tpl_ids = [t["template_id"] for t in data["templates"]]
assert len(tpl_ids) == len(set(tpl_ids)) == 21, "template count changed: %d" % len(tpl_ids)
status_map = {t["template_id"]: t["status"] for t in data["templates"]}
assert status_map["SINGLE_FACTOR_NORMALIZED_WEIGHT"] == "RETIRED"
assert status_map["PLAIN_FACTOR_COMBINE"] == "FALSIFIED"
assert status_map["PATCH_RESOURCE_FOLLOWING"] == "VACATED"
active = [k for k, v in status_map.items() if v == "CANDIDATE"]
print("  yaml validated: 21 entries, CANDIDATE active=%d, RETIRED/FALSIFIED/VACATED=3" % len(active))
REG.write_text(new_text, encoding="utf-8", newline="\n")

# ---------------------------------------------------------------------------
# truth_rebuild_queue.jsonl（234 AMB + 14 slot_tiering = 248 行）
# ---------------------------------------------------------------------------
B4_25 = ["POR", "SDG", "ASR", "GPF", "RKB", "SSL", "GDE", "CBM", "SAI", "BSK",
         "RRH", "GRH", "BST", "MOO", "TSK", "RVS", "SMB", "WIT", "WIN", "YTF",
         "SMF", "FDR", "BSB", "HNC", "RDS"]
HELD3 = {"ASR", "RVS", "RDS"}
RS1_MAP = {
    "BST": "TIERED_SINGLE_FACTOR_CHAIN", "CBM": "TIERED_SINGLE_FACTOR_CHAIN",
    "SDG": "TIERED_SINGLE_FACTOR_CHAIN", "TSK": "TIERED_SINGLE_FACTOR_CHAIN",
    "GPF": "GATED_COVER_TIER_CHAIN", "SSL": "GATED_COVER_TIER_CHAIN",
    "WIT": "GATED_COVER_TIER_CHAIN", "YTF": "GATED_COVER_TIER_CHAIN",
    "FDR": "GATED_COVER_TIER_CHAIN", "BSB": "GATED_COVER_TIER_CHAIN",
    "GDE": "NOCTURNAL_LIGHTSLOT_CHAIN", "MOO": "NOCTURNAL_LIGHTSLOT_CHAIN",
    "GRH": "ZONE_SUBSTRATE_RESOURCE_CHAIN", "RRH": "ZONE_SUBSTRATE_RESOURCE_CHAIN",
    "BSK": "SOFT_TRIPLE_TIER_CHAIN", "SMB": "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN",
    "HNC": "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
}
C8 = ["TAI", "BLP", "GW", "RFP", "DS", "PBF", "GT", "HAL", "GG",
      "POR", "RKB", "WIN", "SMF", "SAI"]

rows = []
REF = "HRQ-ADJUDICATION-2026-09-11（hrq_decision_log.md @ commit b5088ab）"
ENTERED = {"batch": "HRQ-MUTATION-001", "date": "2026-09-14"}

for code in B4_25:
    pid = "P-B4-%s-BAKE" % code
    if code in HELD3:
        rows.append({
            "queue_id": "", "program_id": pid, "surface": "Bake",
            "source_batch": "CENSUS-B4",
            "layer": "AMB 四层链第 1 层（B4 25）",
            "reason": "B4 批 SINGLE v1 MC 成员——v1 canonical 经 RS1 61/61 证伪（0 匹配）+渐进累积语义（裁决 1-A）",
            "pending_work": "evidence_insufficient_held（裁决 1-④）：无 B 系列表达文件，归 FR/表达线补证——补齐后方可进入终局重跑；不并入任何族",
            "ruling_ref": REF, "entered_queue": ENTERED,
        })
    elif code in RS1_MAP:
        fam = RS1_MAP[code]
        rerun = "P-RS1-%s-BAKE" % code
        rows.append({
            "queue_id": "", "program_id": pid, "surface": "Bake",
            "source_batch": "CENSUS-B4",
            "layer": "AMB 四层链第 1 层（B4 25）",
            "reason": "B4 批 SINGLE v1 MC 成员——v1 canonical 经 RS1 61/61 证伪（0 匹配）+渐进累积语义（裁决 1-A）；RS1 重跑体 %s 已 moved %s（order_provisional）" % (rerun, fam),
            "pending_work": "终局顺序还原重跑：逐鱼判断顺序推导（§5 纪律）->真形判同（顺序=族判据，裁决 2-B；PROGRESSIVE_TIERED_FUNNEL 为重跑基准之一，裁决 3-A）；真实序差异=族移动",
            "ruling_ref": REF, "entered_queue": ENTERED,
        })
    else:
        # C8 轨 5 例（POR/RKB/WIN/SMF/SAI）：RS1 重跑体在 slot_tiering 追击轨（同队第 5 层另有条目）
        rows.append({
            "queue_id": "", "program_id": pid, "surface": "Bake",
            "source_batch": "CENSUS-B4",
            "layer": "AMB 四层链第 1 层（B4 25）",
            "reason": "B4 批 SINGLE v1 MC 成员——v1 canonical 经 RS1 61/61 证伪（0 匹配）；RS1 重跑体 P-RS1-%s-BAKE 已入 C8 slot_tiering 追击轨（HRQ-RS1-03->裁决 6-③ 关闭，同队第 5 层另有条目）" % code,
            "pending_work": "两轨合并处理（同鱼 C8 轨重跑体条目互引），以最新真形为准：逐鱼判断顺序推导->重判归属（顺序=族判据，裁决 2-B）",
            "ruling_ref": REF, "entered_queue": ENTERED,
        })

for b, layer_no in (("CENSUS-B5", 2), ("CENSUS-B6", 3), ("CENSUS-B7", 4)):
    n_amb = len(extracted[b]["amb"])
    for pid in extracted[b]["amb"]:
        rows.append({
            "queue_id": "", "program_id": pid, "surface": "Bake",
            "source_batch": b,
            "layer": "AMB 四层链第 %d 层（%s %d）" % (layer_no, b.split("-")[1], n_amb),
            "reason": "AMB vs SINGLE v1（HRQ 挂账：不对被证伪 canonical 制造确信合并——B5 判例①）——v1 经裁决 1-A 正式退役，AMB 转真形重验",
            "pending_work": "终局顺序还原重跑：逐鱼判断顺序推导（§5 纪律）->真形判同（顺序=族判据，裁决 2-B；PROGRESSIVE_TIERED_FUNNEL 为重跑基准之一，裁决 3-A）",
            "ruling_ref": REF, "entered_queue": ENTERED,
        })

for code in C8:
    extra = "；同鱼 B4 层另有原体条目（P-B4-*-BAKE）——两轨合并处理" if code in ("POR", "RKB", "WIN", "SMF", "SAI") else ""
    rows.append({
        "queue_id": "", "program_id": "P-RS1-%s-BAKE" % code, "surface": "Bake",
        "source_batch": "CENSUS-RERUN-SINGLE-001",
        "layer": "slot_tiering 追击轨（14——裁决 6-③ 并队）",
        "reason": "C8 重归族提案（slot_tiering extension）——PLAIN v1 证伪+slot_tiering 轨道关闭（裁决 6-②③）；表达文件自投影受限还原（Tier B vs story 证据分层待消解）",
        "pending_work": "并入真形重验队列同队同流程（裁决 6-③）：逐鱼顺序推导后重判归属%s" % extra,
        "ruling_ref": REF, "entered_queue": ENTERED,
    })

assert len(rows) == 248, "queue rows = %d != 248" % len(rows)
for i, row in enumerate(rows, 1):
    row["queue_id"] = "TRB-%04d" % i
QUEUE.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                 encoding="utf-8", newline="\n")
print("  truth_rebuild_queue.jsonl: 248 rows (B4 25=22 rerun-linkage+3 held; B5 52; B6 47; B7 110; slot_tiering 14)")

# ---------------------------------------------------------------------------
# 批目录 manifest + 空 jsonl（validate_batch 形式要求）
# ---------------------------------------------------------------------------
MANIFEST = """batch_id: HRQ-MUTATION-001
kind: REGISTRY_MUTATION_EXECUTION
date: 2026-09-14
status: INDEPENDENT_REVIEW_REQUIRED
authorization:
  source: fish_logic_census/hrq_decision_log.md
  commit: b5088ab
  adjudication: HRQ-ADJUDICATION-2026-09-11（七项裁决+两组语义裁定）
  scope: "本批零新增裁决——仅逐条落表；不超出决策日志文末 mutation 批执行清单范围"
no_blind_input: true
blind_discipline: "非普查批：无冻结 Story/无新盲程序/无判同——盲纪律不适用（无新 sketch 故无 registry_seen 风险面）"
registry_mutation:
  file: fish_logic_census/template_registry.yaml
  version: 8 -> 9
  script: batches/HRQ-MUTATION-001/apply_hrq_mutation.py（幂等守卫：检测 v9 即拒绝重放）
  previous_state_snapshot: "mutation_provenance.previous_state + v8_mutation_history + git b5088ab^（权威文件不删历史）"
new_artifacts:
  - "fish_logic_census/truth_rebuild_queue.jsonl（248 行=234 AMB[B4 25+B5 52+B6 47+B7 110]+14 slot_tiering——终局全库顺序还原重跑输入清单）"
counts_reconciliation: "见 batch_report.md（逐条裁决->落表对照与计数对账）"
validator_note: "programs/stories/blind_programs/merge_tests 为空文件（validate_batch 形式要求——本批无新程序）；受影响程序 248 条清单见 truth_rebuild_queue.jsonl；registry 归属变更见 mutation_provenance.ruling_to_mutation_map"
"""
(BATCH / "manifest.yaml").write_text(MANIFEST, encoding="utf-8", newline="\n")
for name in ("programs.jsonl", "stories.jsonl", "blind_programs.jsonl", "merge_tests.jsonl"):
    (BATCH / name).write_text("", encoding="utf-8", newline="\n")

print("DONE: registry v9 + truth_rebuild_queue.jsonl + batch scaffolding")
