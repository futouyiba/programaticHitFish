# -*- coding: utf-8 -*-
"""CENSUS-B7 判同产物一体化脚本（merge_tests/programs/HRQ/absence/resolver/
coverage/revisions + discovery_curve 追加一行）。

registry 不动（章程：registry mutation 由独立审通过后另批处理——本批全部
归族/扩容提案进 HRQ）。

语义裁决依据：engine_report.json（raw）+ worker reasoning + B0-B6/RS1/RP1
判例链。核心裁决：
1) Bake 110 vs SINGLE v1 → AMBIGUOUS_NEEDS_EXPANSION：engine raw 仅 op 名
   字面（OPERATOR）+PREMISE，骨架同构——但 SINGLE v1 canonical 已被 RS1
   全体成员证伪（61/61，HRQ-RS1-01 pending；B5 52+B6 47 AMB 同态先例）。
   本批输入层与 B1-B6 同源（Story 正文——R01-R05 十节形表达层同样无
   档位/门形结构声明）。归族裁决 blocked：不 MC 不 NEW 单独立族。→ HRQ-B7-01
   （B4 25+B5 52+B6 47+B7 110 四层联动链）。
2) Bake 110 vs CRR → NEW non-match（B0-B6 连续回落测试第 7 批，累计 284）。
3) Bake 110 vs 11 新族 → NEW non-match 分组（distinct_diff_sets=1 断言）。
4) Bake 110 vs C9（pending 候选族）→ NEW non-match 分组 + HRQ-RS1-05 联动
   （B7 110 对为第 7 批平铺输入 non-match 素材）。
5) RESP 86 vs TYPED → MERGE_CONFIDENT（raw 仅 PREMISE——F02）。
6) FIELD 14 vs FOOD_FIELD → MERGE_CONFIDENT：engine raw 仅 OPERATOR（场
   评估 op 名字面）+PREMISE——骨架同构（单步场评估链+NONE+RETURN=
   Response(FieldFeeding) 同）。B2 立族（HRQ-B2-01，2 实例 BHC/HER）后
   首批族扩容（2→16 名义 pending）。B1-LAM/B2 判例链：evaluand=场 +
   RETURN=FieldFeeding 是 FOOD_FIELD 族域判据（vs TYPED 见条目 7）。
7) FIELD 14 vs TYPED → NEW non-match 分组（族域边界互证：OPERATOR+
   PREMISE+RETURN——RETURN=FieldFeeding vs TargetFeeding 硬判据，
   B2 BHC-RESP-FIELD 判例同型第 2 批素材）。
8) guard 9 vs GUARD → TEMPLATE_EXTENSION_CANDIDATE：骨架同构（deps 位形
   [ [],[],[0,1],[2] ]/branches 空/RETURN 同）；raw 仅槽名/合并步标名
   字面（B4-HNC/B5-②/B6 同型）。新内容=7 个 anchor 新值候选（第 18-24）
   + 2 个已提案候选值跨批复现实证（DIS2 discus_mucus[vs B5 MDC]/
   RSB mussel_brood[vs B6 LFB]）→ HRQ-B7-02。
9) guard 9 vs STATE_GATED/TYPED → NEW 分组互证（§9.2 两拓扑边界）。
10) SOK2 vs STATE_GATED → NEW 单条互证（P05 洄游停食状态门 vs 动机未定
    typed 占位——本批无 STATE_GATED 新成员记录）。

计数声明（self-QA 对账基）：merge_tests 条目数 345 = MC 100[typed 86 +
field 14] + EXT 9 + NEW 126[CRR 110 单条 + 新族分组 11 + C9 分组 1 +
field-vs-typed 分组 1 + guard 跨族分组 2 + SOK2 1 条] + AMB 110；
程序×族对数 1683 = 110[CRR] + 110[SINGLE] + 110×11[新族] + 110[C9] +
86[TYPED] + 9[GUARD] + 14[FOOD_FIELD] + 14[field-vs-typed] + 9×2[guard
cross] + 1[SOK2]。
"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"bake_membership": "HRQ-B7-01",
       "guard_ext": "HRQ-B7-02",
       "members": "HRQ-B7-03"}

BLIND = {p["program_id"]: p for p in (
    json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(
        encoding="utf-8").splitlines() if l.strip())}
ENGINE = json.loads((BATCH / "engine_report.json").read_text(encoding="utf-8"))
RAW_CRR = {r["program_id"]: r["structural_diffs"] for r in ENGINE["vs_CRR"]}
RAW_SINGLE = {r["program_id"]: r["engine_structural_diff"]
              for r in ENGINE["vs_SINGLE"]}
RAW_NEWFAM = {g["family"]: {r["program_id"]: r["engine_structural_diff"]
                            for r in g["rows"]}
              for g in ENGINE["vs_new_families"]}
RAW_C9 = {r["program_id"]: r["engine_structural_diff"]
          for r in ENGINE["vs_c9_candidate"][0]["rows"]}
RAW_FAM = {(r["program_id"], r["family"]): r["engine_structural_diff"]
           for r in ENGINE["family"]}
RAW_FOODFIELD = {r["program_id"]: r["engine_structural_diff"]
                 for r in ENGINE["field_vs_foodfield"]}
RAW_FIELD_TYPED = {r["program_id"]: r["engine_structural_diff"]
                   for r in ENGINE["field_vs_typed"][0]["rows"]}
RAW_CROSS = {g["family"]: {r["program_id"]: r["engine_structural_diff"]
                           for r in g["rows"]}
             for g in ENGINE["guard_cross"]}
RAW_SOK2 = ENGINE["sok2_vs_state_gated"][0]["engine_structural_diff"]

BAKE_ORDER = sorted([pid for pid, p in BLIND.items()
                     if p["surface"] == "Bake"])
TYPED_PIDS = sorted([pid for pid, p in BLIND.items()
                     if p["return_type"] == "Response(TargetFeeding)"])
FIELD_PIDS = sorted([pid for pid, p in BLIND.items()
                     if p["return_type"] == "Response(FieldFeeding)"])
GUARD_PIDS = sorted([pid for pid, p in BLIND.items()
                     if "RelationalConflict" in p["return_type"]])

NEW_FAMILIES = [
    "TIERED_SINGLE_FACTOR_CHAIN", "LAYER_AXIS_DUAL_TIER_CHAIN",
    "GATED_COVER_TIER_CHAIN", "NOCTURNAL_LIGHTSLOT_CHAIN",
    "ZONE_SUBSTRATE_RESOURCE_CHAIN", "SOFT_TRIPLE_TIER_CHAIN",
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN", "FILTER_FIELD_ACCUMULATE_CHAIN",
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN",
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN"]
NEW_FAM_REASON = {
    "TIERED_SINGLE_FACTOR_CHAIN":
        "BRANCH+OPERATOR（typed 因子三档分级命中+EARLY_RETURN）vs 本批平链无档位",
    "LAYER_AXIS_DUAL_TIER_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（前置水层定位步+双档链）vs 平链单步",
    "GATED_COVER_TIER_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（结构掩体存在门先行）vs 平链无门",
    "NOCTURNAL_LIGHTSLOT_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（夜行底板档+低光槽调整器）vs 平链无槽",
    "ZONE_SUBSTRATE_RESOURCE_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（底层硬门+底质/资源双档）vs 平链",
    "SOFT_TRIPLE_TIER_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（三档×3 软链）vs 平链两步",
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN":
        "BRANCH+DEPENDENCY+OPERATOR（五步链含深度档）vs 平链两步",
    "FILTER_FIELD_ACCUMULATE_CHAIN":
        "BRANCH+COMBINE+DEPENDENCY+OPERATOR（滤食场浓度+口径评估线性累积）"
        "vs 平链单因子",
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN":
        "BRANCH+COMBINE+DEPENDENCY+OPERATOR+RETURN（锚存在门+Guarding 返回）"
        "vs 平链 SpatialDistributionWeight 返回",
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN":
        "BRANCH+COMBINE+DEPENDENCY+OPERATOR（极值水温硬门+EXIT 档因子集）"
        "vs 平链无门",
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN":
        "BRANCH+COMBINE+DEPENDENCY+OPERATOR（patch 存在门+双槽+无归一化）"
        "vs 平链",
}
C9 = "ORDERED_QUAD_TIER_COMBINE_CHAIN"

GUARD_DETAIL = {
    "CRA2": {
        "anchor": "black_crappie_nest_guard（雄鱼筑巢护卵至孵化——本种证据"
                  "实证，不再同科猜测）",
        "extra": "Semantic Open 置信如实携带（story：对玩家饵的冲突路径尚待"
                 "行为证据）；守巢事实确立+双意义候选",
        "note": "黑斑刺盖太阳鱼雄鱼筑巢护卵"},
    "SMA1": {
        "anchor": "smallmouth_nest_fry_guard（巢与幼鱼守护+营养竞争语境——"
                  "2009 饱食/2016 补食实验注记）",
        "extra": "story 层『并行可用候选不等于必须共同结算』——双 Path 候选"
                 "语义如实；Guard Mode bundle 必要性待证（story 竞争解释）",
        "note": "小口黑鲈巢幼守护与营养竞争"},
    "BLU2": {
        "anchor": "bluegill_nest_guard_forage_overlap（护巢+父本食卵+巢区"
                  "小饵双意义并存）",
        "extra": "父本食卵非『外部食物+守护』并发的证明（story 竞争解释）——"
                 "结算政策未定如实注记",
        "note": "蓝鳃太阳鱼护巢觅食食卵边界"},
    "CCF2": {
        "anchor": "channel_cave_guard（洞巢雄鱼照护+受扰食卵）",
        "extra": "Semantic Open 置信（story：照护→lure-defense 映射无可靠"
                 "证据）；洞巢=隐蔽结构型载体",
        "note": "斑点叉尾鮰洞巢照护受扰食卵"},
    "TIL3": {
        "anchor": "tilapia_territory（雄鱼繁殖领地——雌鱼取卵离巢口孵，"
                  "领地与幼体非同一关系对象）",
        "extra": "Semantic Open（story：P04 仅竞争参照，先区分领地与护卵）"
                 "——领地型 anchor 与守巢型的轴内一致性留 review",
        "note": "罗非鱼巢区领地与雌鱼离巢"},
    "CSN1": {
        "anchor": "snakehead_brood_guard（繁殖期亲鱼守护卵幼+植被伏击捕食"
                  "双语境）",
        "extra": "story 层『普通捕食仍可落 P01』——伏击 typed 与护幼 guard "
                 "的并存结构（P01+P04 组合）",
        "note": "乌鳢伏击捕食与护幼切换"},
    "BBR1": {
        "anchor": "bullhead_cave_night_guard（洞巢护卵+夜间底栖嗅觉取食）",
        "extra": "P01+P04 组合（R02 packet：乌鳢、云斑鮰护幼/洞巢进入 P04）；"
                 "昼夜时窗=premise 非结构",
        "note": "云斑鮰夜间底栖嗅觉与洞巢护卵"},
    "DIS2": {
        "anchor": "discus_mucus_brood（亲鱼护幼+幼鱼体表黏液摄食）——"
                  "**B5 MDC（橙型）已提案 anchor 候选值的跨批复现实证**",
        "extra": "色型不分裂（story FR 层 Compression Candidate：白橙同语义"
                 "两物种关联）——同 anchor 值复现为 B5 提案值提供第 2 实证",
        "note": "七彩神仙鱼（白）亲鱼护幼（色型不分裂）"},
    "RSB": {
        "anchor": "bitterling_mussel_brood（卵产入活蚌鳃腔+贝内发育）——"
                  "**B6 LFB（大鳍𫚪）已提案 anchor 候选值的跨批复现实证**",
        "extra": "鳑鲏科跨属第 2 实证（R03 高体鳑鲏 vs B6 大鳍𫚪）；"
                 "Relation Object 语义（FR 层明言非新捕食/资源程序）；"
                 "产卵管=产卵工具行为变量非 branch",
        "note": "高体鳑鲏贝内产卵幼贝发育"},
}

FIELD_DETAIL = {
    "MAC1": "R02 鲭鱼移动饵场（季节沿陆架+群体=找鱼线索）",
    "JCK1": "R02 竹荚鱼近岸潮流场（水温潮流改变分布）",
    "CAP1": "R02 毛鳞鱼近岸繁殖窗场（短窗+潮位时间）",
    "SIL1": "R02 鲢鱼水柱滤食场（+B02 接触捕获边界注记）",
    "BON1": "R02 东方狐鲣开放水层追猎场（FieldFeeding+下游离散目标）",
    "MDC2": "R03 鲮藻类/附着/碎屑连续场（P03——FR3 2 条 P03 之一）",
    "XCD": "R03 黄尾鲴附着资源场（P03——薄资料 Medium 推算）",
    "ROH": "R05 泰鲮季风洪泛植物场（P06 连续基质处理候选）",
    "MRC": "R05 印度鲮底中场（拾取 vs 滤机制开放）",
    "SPR": "R05 巴西鲷有机泥层场（illiophagous+800-1000km 洄游 premise）",
    "CHM": "R05 美洲锐唇鲷附着藻层场（下颌硬板刮食+幼成切换 premise）",
    "SHB": "R05 白条鱼上层悬浮场（虫拾取含次级离散目标）",
    "GTB": "R05 暹罗巨鲤洪泛果实窗场（阶段栖息分异 premise）",
    "WCB": "R05 团头鲂沉水草床场（选择性放牧控草——与草鱼 grazing 前例同构）",
}

TYPED_NOTES = {}
for pid in TYPED_PIDS:
    p = BLIND[pid]
    prem = p["incoming_premises"][0] if p["incoming_premises"] else ""
    conf = p.get("confidence")
    note = prem[:60] + ("｜conf=" + conf if conf else "")
    TYPED_NOTES[pid] = note

M = []
# --- 1) Bake 110 vs SINGLE v1：AMBIGUOUS ---
for pid in BAKE_ORDER:
    M.append({"program_id": pid,
              "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "AMBIGUOUS_NEEDS_EXPANSION", "same": None,
              "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": RAW_SINGLE[pid],
              "blocked_by": "HRQ-RS1-01（SINGLE v1 canonical 证伪待裁决）",
              "reasoning": "engine raw 仅 op 名字面（OPERATOR="
                           "EVAL_HABITAT_FACTOR_POSITION vs EVAL_TYPED_FIELD_"
                           "OR_FACTOR，B4-B6 同型槽名差异）+PREMISE——骨架"
                           "同构。但 SINGLE v1 canonical 已被 RS1 全体成员"
                           "证伪（61/61 body 结构差异、0 匹配；HRQ-RS1-01 "
                           "pending）：本批输入层与 B1-B6 同源（Story 正文"
                           "十节形——R01-R05 均无面内档位/门形结构声明，"
                           "顺序扫描结论见 manifest order_discipline），RS1 "
                           "已证明该层平铺形相对顺序还原形系统性收敛。归族"
                           "两难：不 MC（不对被证伪 canonical 制造确信合并"
                           "——B4 25 成员已陷 moved_pending_review 同态，"
                           "B5 52+B6 47 AMB 同态先例）；不 NEW 立族（平铺"
                           "输入立族=RS1 反例）。裁决=v1 保留则本批按 B4 先例"
                           " MC 入族；拆分批准则本批对 9 新族+C9 重裁（全 "
                           "non-match 已实测，真形需 B 表达顺序还原输入另批）。"
                           "挂 HRQ-B7-01（四层联动链第 4 层）。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 2) Bake 110 vs CRR：NEW non-match（第 7 批）---
for pid in BAKE_ORDER:
    M.append({"program_id": pid,
              "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(RAW_CRR[pid]) - {"PREMISE"}),
              "engine_raw_diffs": RAW_CRR[pid],
              "reasoning": "CRR 判别结构（BUILD→GATE→RelativeRank"
                           "(reference_set=FeasibleSet)→secondary→FIXED）不"
                           "存在：本批为 premise 绑定切换（洄游/昼夜/阶段/"
                           "品系复用/身份隔离）与静态结构/因子绑定形态。CRR "
                           "连续第 7 批 0 成员（B0-B7 累计 284 non-match；"
                           "HRQ-B2-02 维持人类裁决）。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 3) Bake 110 vs 11 新族：NEW 分组 ---
for fam in NEW_FAMILIES:
    rows = RAW_NEWFAM[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": list(BAKE_ORDER),
              "n_programs": len(BAKE_ORDER),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": f"110 程序 engine diff 完全一致（distinct_diff_sets=1）。"
                           f"{NEW_FAM_REASON[fam]}——本批 Story 层无面内判断链/"
                           f"档位/门证据（顺序扫描结论，manifest order_"
                           f"discipline），与该族档位形真结构差异。注意：non-match "
                           f"对平铺输入成立的含义受 RS1 教训限定（Story 层平链"
                           f"本身是收敛形——真形待顺序还原），与条目 1 的 "
                           f"AMBIGUOUS 同源挂账。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 4) Bake 110 vs C9（pending 候选族）---
rows = RAW_C9
diff_sets = {tuple(v) for v in rows.values()}
assert len(diff_sets) == 1, diff_sets
M.append({"program_id": list(BAKE_ORDER),
          "n_programs": len(BAKE_ORDER),
          "template_id": C9,
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
          "param_only": False,
          "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
          "engine_raw_diffs": sorted(next(iter(rows.values()))),
          "engine_uniform": True,
          "template_status": "PENDING_CANDIDATE_NOT_IN_REGISTRY（HRQ-RS1-05 "
                             "待裁——REV-001 修复轮 C9=无门有序四步档位链 "
                             "4 HAB 成员）",
          "reasoning": "110 程序 engine diff 完全一致（distinct_diff_sets=1）。"
                       "BRANCH+COMBINE+DEPENDENCY+OPERATOR（无门有序四步档位"
                       "链+终步扇入 vs 本批平链两步）。**C9 联动注记（envelope "
                       "指示）**：C9 是 HRQ-RS1-05 的 pending 候选族、不在 "
                       "registry v8——本条 non-match 不构成 registry 族归并"
                       "记录；C9 立族裁决（HRQ-RS1-05）时本批 110 对为第 7 批"
                       "平铺输入 non-match 素材（真形待 B 表达顺序还原），与 "
                       "HRQ-RS1-01/B5-01/B6-01/B7-01 四层挂账链同源。",
          "human_review_queued": HRQ["bake_membership"],
          "related_review": "HRQ-RS1-05（C9 立族+成员归宿裁决联动）",
          "provenance": {"batch": "CENSUS-B7"}})
# --- 5) RESP 86 vs TYPED：MERGE_CONFIDENT ---
for pid in TYPED_PIDS:
    M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")],
              "reasoning": f"engine 仅 PREMISE（F02 不计）。实例注记："
                           f"{TYPED_NOTES[pid]}。",
              "provenance": {"batch": "CENSUS-B7"}})
# --- 6) FIELD 14 vs FOOD_FIELD：MERGE_CONFIDENT（族扩容）---
for pid in FIELD_PIDS:
    code = pid.split("-")[2]
    M.append({"program_id": pid, "template_id": "FOOD_FIELD_FEEDING_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_FOODFIELD[pid],
              "reasoning": f"骨架同构：单步场评估→决策（deps 位形 [ [],[0] ]/"
                           f"branches 空/combine NONE/RETURN=Response"
                           f"(FieldFeeding) 与 B2 canonical 一致）；engine raw "
                           f"仅场评估 op 名字面（EVAL_FIELD_AS_FOOD_TYPED vs "
                           f"EVAL_FOOD_FIELD_INTAKE / DECIDE_RESPONSE vs "
                           f"DECIDE_FIELD_FEEDING）+PREMISE——B3 判同经验"
                           f"（槽名字面+骨架同构→语义 MC）。族域判据维持："
                           f"evaluand=场+RETURN=FieldFeeding（vs TYPED 的 "
                           f"RETURN 硬判据见 field_vs_typed 分组条目——"
                           f"B1-LAM/B2 BHC-RESP-FIELD 判例链第 2 批素材）。"
                           f"实例={code}：{FIELD_DETAIL[code]}。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 7) FIELD 14 vs TYPED：族域边界互证（分组 NEW）---
rows = RAW_FIELD_TYPED
diff_sets = {tuple(v) for v in rows.values()}
assert len(diff_sets) == 1, diff_sets
M.append({"program_id": list(FIELD_PIDS),
          "n_programs": len(FIELD_PIDS),
          "template_id": "TYPED_TARGET_RESPONSE",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
          "param_only": False,
          "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
          "engine_raw_diffs": sorted(next(iter(rows.values()))),
          "engine_uniform": True,
          "reasoning": "族域边界互证（14 例同型）：单目标评估+RETURN="
                       "Response(TargetFeeding) vs 场评估+RETURN=Response"
                       "(FieldFeeding)——OPERATOR+RETURN 真差异（B1-LAM "
                       "判例：evaluand/return 硬判据）。FOOD_FIELD 与 TYPED "
                       "两族边界维持（B2 HRQ-B2-01 立族判据第 2 批独立"
                       "复证）。14 程序 engine diff 完全一致"
                       "（distinct_diff_sets=1）。",
          "human_review_queued": HRQ["members"],
          "provenance": {"batch": "CENSUS-B7"}})
# --- 8) guard 9 vs GUARD：TEMPLATE_EXTENSION_CANDIDATE ---
for pid in GUARD_PIDS:
    code = pid.split("-")[2]
    d = GUARD_DETAIL[code]
    M.append({"program_id": pid,
              "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
              "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False,
              "param_only": True, "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "GUARD_CONFLICT_DUAL_PATH_RESPONSE")],
              "extension_complexity_cost":
                  "+anchor 轴新值候选（第 18-24 值——B4 +1→B5 +9→B6 +2 后"
                  f"本批 +7）挂既有 intruder evaluator 槽；2 例为已提案候选值"
                  "跨批复现实证（DIS2=discus_mucus vs B5 MDC / RSB="
                  "mussel_brood vs B6 LFB）；canonical body 零改动（deps 位形 "
                  "[ [],[],[0,1],[2] ]/branches 空/RETURN 同）；Semantic Open "
                  "置信 3 例如实携带",
              "new_template_complexity_cost":
                  "为守护对象/语境差异复制整条 ∥ 并行双路径拓扑为独立族——与 "
                  "GUARD 既有 7+1+B5 候选 9+B6 候选 2 成员全部骨架同构（仅"
                  "守护对象/语境 typed 不同），各自立族=家族数爆炸，违反 "
                  "F10/F14 节俭",
              "recommended_shape":
                  "扩展 GUARD：9 例入族（7 新值候选为第 18-24 名义成员提案+"
                  "2 复现实证并入既有候选值）——HRQ-B7-02 与 HRQ-B5-02/"
                  "HRQ-B6-02 轴系合并裁决联动（anchor 轴累计 18 候选值）；"
                  "批前按 extension 候选挂账（HNC 第 8 名义先例）",
              "proposed_parameter_axis":
                  f"intruder_evaluator_context：7 新值候选（{d['anchor']}）"
                  "——与 HRQ-B5-02 已提案 9 值+HRQ-B6-02 已提案 2 值合并裁决；"
                  "无 NEW 轴提案（领地型 TIL3 的轴内一致性留 review）",
              "reasoning": f"骨架同构：并行双 evaluator（deps 位形与 canonical 一致、"
                           f"branches 空、RETURN 同）→ combine → decide；engine raw "
                           f"差异全为字面（intruder 槽名 EVAL_NEST_INTRUDER_RELATION "
                           f"vs EVAL_TARGET_AS_INTRUDER_TYPED；合并步标名 "
                           f"COMBINE_CONFLICT_AWARE vs COMBINE_DUAL_PATH——B4-HNC/"
                           f"B5-②/B6 同型字面，B3 判同经验）。实例={code}：{d['note']}；"
                           f"新内容={d['extra']}。守护对象/语境 typing 非新增 "
                           f"branch/gate（拓扑不变）→ 有限 typed 新参数轴 → "
                           f"TEMPLATE_EXTENSION_CANDIDATE（F14 非 plain merge）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 9) guard 9 跨族互证（分组）---
for fam, reason in (
    ("STATE_GATED_MULTI_PATH_RESPONSE",
     "§9.2 两拓扑边界再证（9 例同型）：∥ 同刻并行竞争（无分支）vs IF "
     "状态门互斥；RelationalConflict vs NonFeedingStrike——双向 non-match "
     "维持（B3/B4/B5/B6 判例链）"),
    ("TYPED_TARGET_RESPONSE",
     "单路径边界互证（9 例同型）：单 evaluator vs ∥ 双 evaluator+combine+"
     "双值 RETURN——GUARD 族域判据维持（B0 OSC 先例同型）")):
    rows = RAW_CROSS[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": list(GUARD_PIDS),
              "n_programs": len(GUARD_PIDS),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": reason + "。9 程序 engine diff 完全一致"
                           "（distinct_diff_sets=1）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B7"}})
# --- 10) SOK2 vs STATE_GATED：单条互证 ---
M.append({"program_id": "P-B7-SOK2-RESP",
          "template_id": "STATE_GATED_MULTI_PATH_RESPONSE",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
          "param_only": False,
          "structural_diffs": sorted(set(RAW_SOK2) - {"PREMISE"}),
          "engine_raw_diffs": RAW_SOK2,
          "reasoning": "P05 洄游语境边界互证（单条）：S29 红鲑返河捕获动机"
                       "未定（story Semantic Open：『既不能默认 TargetFeeding "
                       "也不能归 B02』）——typed 单步占位 vs STATE_GATED 洄游"
                       "停食状态门（IF branch+四步）真结构差异。本批无 "
                       "STATE_GATED 新成员的记录（P05 停食状态门系 B3-B5 成员"
                       "之外无新增；S29 动机未定语境与停食状态门不同构——"
                       "SOK2 归 TYPED MC+Semantic Open 注记）。",
          "human_review_queued": HRQ["members"],
          "provenance": {"batch": "CENSUS-B7"}})

FAMILY_OF = {}
for pid in BAKE_ORDER:
    FAMILY_OF[pid] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT",
                      HRQ["bake_membership"], "PENDING_SPLIT_RULING")
for pid in TYPED_PIDS:
    FAMILY_OF[pid] = ("TYPED_TARGET_RESPONSE", HRQ["members"], None)
for pid in FIELD_PIDS:
    FAMILY_OF[pid] = ("FOOD_FIELD_FEEDING_RESPONSE", HRQ["members"],
                      "MEMBER_EXPANSION_PENDING_REVIEW")
for pid in GUARD_PIDS:
    FAMILY_OF[pid] = ("GUARD_CONFLICT_DUAL_PATH_RESPONSE",
                      HRQ["guard_ext"], "EXTENSION_CANDIDATE")


def main():
    # merge_tests
    (BATCH / "merge_tests.jsonl").write_text(
        "\n".join(json.dumps(m, ensure_ascii=False) for m in M) + "\n",
        encoding="utf-8")
    # programs
    out = []
    for p in BLIND.values():
        fam, ref, pending = FAMILY_OF[p["program_id"]]
        rec = {"program_id": p["program_id"], "story_id": p["story_id"],
               "species_id": p["species_id"], "surface": p["surface"],
               "consequence": "NEW_PROGRAM_CANDIDATE",
               "family_membership": fam, "review_ref": ref,
               "membership_status": pending or "MEMBER_EXPANSION_PENDING_REVIEW",
               "blind_hash": p["blind_hash"],
               "original_program_body_unchanged": True,
               "registry_seen_at_creation": False,
               "post_registry_mutations": [],
               "provenance": {"batch": "CENSUS-B7"}}
        if p.get("confidence"):
            rec["confidence"] = p["confidence"]
        out.append(rec)
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n",
        encoding="utf-8")
    # revisions / coverage（空）
    (BATCH / "program_revisions.jsonl").write_text("", encoding="utf-8")
    (BATCH / "coverage.jsonl").write_text("", encoding="utf-8")
    # resolver tests
    (BATCH / "resolver_tests.jsonl").write_text(json.dumps({
        "resolver_id": "NO_NEW_RESOLVER_FAMILY",
        "note": "B7 未新增 resolver family；洄游（溯河/降海/potamodromous/"
                "oceanodromous/半溯河/生态型对/三阶段）/昼夜时窗/夜行/"
                "ontogeny（幼成切换/食谱差异）/繁殖期（守巢/护幼/领地/求偶/"
                "色型）/品系杂交身份/身份隔离（Blocked-by-Identity 行）/"
                "低氧洪泛/广盐性/保护边界/捕获边界（B02 锚挂/B01 实例化后"
                "寄生）均为世界侧 fact、premise 供给义务或 evaluator typed "
                "context（上游 SNAP 登记同 B1-B6）",
        "provenance": {"batch": "CENSUS-B7"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # absence claims：非强宣称——Bake 归族挂起 + 基线终态
    (BATCH / "absence_claims.jsonl").write_text(json.dumps({
        "story_id": "CENSUS-B7-AGGREGATE",
        "claim": "BAKE_MEMBERSHIP_PENDING_SPLIT_RULING",
        "scope": "Bake 110 程序对 SINGLE v1 归族 = AMBIGUOUS_NEEDS_EXPANSION"
                 "（非 non-match 亦非 MC）：v1 canonical 证伪待裁决"
                 "（HRQ-RS1-01），本批 Story 层平链与 B1-B6 成员同层同态"
                 "（B4 25+B5 52+B6 47 已挂账；B7 110 为四层联动第 4 层）",
        "evidence_basis": "engine raw 仅 op 名字面（骨架同构）；RS1 61/61 证伪"
                          "记录；本批顺序扫描无面内判断链（manifest "
                          "order_discipline）",
        "does_not_claim": "非 NO_NEW_PROGRAM_PROVEN / LOCAL_SATURATION——110 AMB "
                          "是归族挂起不是饱和证据；真形需 B 表达顺序还原输入"
                          "（独立 envelope 同 B0-B2 重跑范式）。基线终态注记："
                          "本批后 census 基线 295/295=100% 消费（R01-R10 全库）"
                          "——普通层输入通道关闭，Bake 真形补证唯一通道=B 表达"
                          "顺序还原重跑（全库系统性）",
        "provenance": {"batch": "CENSUS-B7"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # HRQ
    hrq = [
        {"queue_id": HRQ["bake_membership"], "batch": "CENSUS-B7",
         "kind": "AMBIGUOUS_MEMBERSHIP_BLOCKED_BY_SPLIT_RULING",
         "surface": "Bake",
         "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
         "question": "B7 Bake 110 程序（census 基线收尾批：R01-R05 残余）对 "
                     "SINGLE v1 归族裁决=AMBIGUOUS_NEEDS_EXPANSION：engine raw "
                     "仅 op 名字面（骨架同构平链），但 v1 canonical 已被 RS1 "
                     "全体成员证伪（61/61）且 HRQ-RS1-01 裁决 pending。本批"
                     "输入层与 B1-B6 同源（R01-R05 十节 story——较 R10 压缩形"
                     "厚但同样无面内档位/门形结构声明）。",
         "verdict_branches": [
             "若 HRQ-RS1-01 裁 SINGLE v1 保留（拆分不批准）：本批 110 按 B4 "
             "先例升 MC 入族（名义随 B4 25+B5 52+B6 47 联动重算），随之继承 "
             "moved_pending_review 风险",
             "若裁拆分批准（9 新族成立）：本批 110 对新族全 non-match（engine "
             "BRANCH 等真差异已实测）——真形判定需 B 表达顺序还原输入（独立 "
             "envelope，B0-B2 重跑范式）后重裁；本批挂账态不变"],
         "pending_review_questions": [
             "四层联动：B4 25+B5 52+B6 47+B7 110=234 成员/AMB 待 HRQ-RS1-01 "
             "一并处置",
             "vs 11 新族+C9 分组 non-match 的含义限定（Story 层平链是收敛形——"
             "non-match 真对象是『平链』不是『鱼的真实程序』）",
             "C9（pending 候选族）联动：本批 110 对 C9 non-match 为 HRQ-RS1-05 "
             "立族裁决的第 7 批素材",
             "CRR 连续第 7 批 0 成员（累计 284 non-match）——HRQ-B2-02 维持",
             "基线终态：本批后 295/295=100% 消费，普通层输入通道关闭——Bake "
             "真形补证唯一通道=B 表达顺序还原重跑（R01-R10 全库系统性）"],
         "related": ["HRQ-RS1-01（SINGLE 拆分总裁决）", "HRQ-B5-01",
                    "HRQ-B6-01（三层前联）", "HRQ-B4-02", "HRQ-RS1-05",
                    "absence_claims.jsonl BAKE_MEMBERSHIP_PENDING_SPLIT_RULING"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["guard_ext"], "batch": "CENSUS-B7",
         "kind": "TEMPLATE_EXTENSION_CANDIDATE", "surface": "Response",
         "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
         "question": "B7 P04 guard 9 例入 GUARD 族：9/9 骨架同构直验（∥ 双 "
                     "evaluator→combine→decide；deps 位形/branches/RETURN 与 "
                     "canonical 一致；engine raw 仅槽名/合并步标名字面——"
                     "B4-HNC/B5-②/B6 同型）。7 个 anchor 新值候选（黑斑刺盖"
                     "巢守卫/小口黑鲈巢幼+营养竞争/蓝鳃护巢+食卵并存/斑点"
                     "叉尾鮰洞巢+受扰食卵/罗非鱼领地/乌鳢护幼/云斑鮰洞巢护卵）"
                     "+2 个已提案候选值跨批复现实证（白神仙鱼黏液喂养 vs B5 "
                     "MDC 橙型——色型不分裂；高体鳑鲏贝宿主 vs B6 LFB——鳑鲏"
                     "科跨属）。",
         "proposed_axes": [
             "intruder_evaluator_context 第 18-24 值候选（7 新值）+2 复现实证"
             "——与 HRQ-B5-02 已提案 9 值+HRQ-B6-02 已提案 2 值合并裁决"
             "（anchor 轴累计 18 候选值）",
             "TIL3 领地型 anchor（territory vs 护巢/护幼）的轴内一致性：story "
             "FR 层明言『先区分领地与护卵』——Semantic Open 置信如实携带，"
             "领地驱逐与守巢防御的关系路径同构性留 review",
             "Semantic Open 3 例（CRA2/CCF2/TIL3）：守巢/领地事实确立但冲突"
             "路径行为证据待验证——入 EXT 轨 vs 降 EO 待裁（与 B5 JGC『P04 "
             "语境记 guard premise 注记』判例族关系）",
             "BLU2 父本食卵语境（filial cannibalism）：『外部食物+守护』并发"
             "的证明边界（story 竞争解释）——双意义结算政策未定"],
         "complexity_comparison": {
             "extension": "+anchor 轴 7 值候选+2 复现实证挂既有 evaluator 槽；"
                          "canonical 零改动；不触发全族回归复检（F15）",
             "new_template": "9 例按守护对象/语境差异各自立族——与既有 7+1+"
                             "B5 候选 9+B6 候选 2 成员全部骨架同构，家族数"
                             "爆炸违反节俭（F10/F14）",
             "recommended": "extension（worker 裁定；与 HRQ-B5-02/HRQ-B6-02 "
                            "合并批准后 anchor 轴值正式入声明，9 例入族为"
                            "第 18-26 名义成员[含 2 复现并入]）"},
         "pending_review_questions": [
             "与 HRQ-B5-02+HRQ-B6-02 的合并裁决（anchor 轴 9+2+7=18 候选值+"
             "participant 轴+fan 语义一并批）还是分批批",
             "R01/R02 守巢系 7 例与 B5 9 例+B6 2 例的 anchor 值去重合并清单",
             "P04 pattern 页 Mechanism Stories 索引是否已含本批 9 例 URL"
             "（FR 层索引先于 census——无盲纪律影响）"],
         "related": ["HRQ-B5-02", "HRQ-B6-02（anchor 轴系联动）",
                     "HRQ-06(B0)", "HRQ-B3-02", "HRQ-B4-01"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["members"], "batch": "CENSUS-B7",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Response",
         "template_id": "TYPED_TARGET_RESPONSE + FOOD_FIELD_FEEDING_RESPONSE",
         "question": "TYPED +86 MC（B6 后名义 162+86=248 pending review）+ "
                     "FOOD_FIELD +14 MC（B2 立族后首批扩容：2→16 名义——"
                     "HRQ-B2-01 族域判据第 2 批独立复证：field vs TYPED "
                     "RETURN 硬判据 non-match 14 对）；GUARD +9 extension "
                     "候选（HRQ-B7-02）；Bake 110 AMBIGUOUS 挂账（HRQ-B7-01）；"
                     "ΔL 全零（本批零新族——基线收尾批全部同构入既有族）",
         "pending_review_questions": [
             "FOOD_FIELD 首批扩容（R02 5+R03 2+R05 7）：P03/P06 语境的场评估"
             "Response 统一进 FOOD_FIELD（vs B0 MGC『FieldFeeding 按 TYPED "
             "evaluator_channel 轴 premise 实例』旧处理）——两口径的族域"
             "重审（MGC-RESP-FEEDING 是否应重指派 FOOD_FIELD——B2 立族后"
             "的追溯一致性问题）",
             "MEDIUM 4 例（LWF1 身份隔离推算/SBS1/SBH1 Evidence Open 推算/"
             "LJB 薄资料）+ Low 6 例（品系 5+TNS 稀疏占位+DIS2 色型）证据"
             "分层——全部入族 or 部分降 EO 待 FR 线引文",
             "身份层处理（品系/杂交 6 例 RTL/WRC/KOI/MIR/GCR/DIS2+野生边界 "
             "WCR2+身份隔离 LWF1）：机制复用推算承载（B5-⑤/B6-⑥ 判例），"
             "身份裁决归 FR 线；R02-S06 Lake Whitefish=Blocked-by-Identity "
             "行但 story 属 FR3 25/25 PASS 范围——消费+隔离注记 Medium 的"
             "合法性留 review",
             "同种双 story 跨批：R02-S17 佛罗里达雀鳝 vs R04-FGA4（内容近似"
             "Vegetated Ambush）——各自消费+去重联动注记（B5 CMR/LKR、B6 "
             "WS2 同型第 3 例；typed MC 各计一条的口径确认）",
             "0 程序 story 2 例（PAD4 S36 锚挂=B02 边界 / SEA1 S47 附着寄生="
             "B01 实例化后边界）：顶层 no_surface_reason——与 B6『3 Blocked "
             "无 Story 不入』的对照（本批为有 Story 但捕获边界型 0 程序，"
             "原因分类≠identity blocked）",
             "WBL（R04 西方七鳃鳗）boundary-only/Product Scope Deferred："
             "Response 无程序+Bake 保留——FR3『不强并入 Target/Field 直至 "
             "product scope 显式』的 census 侧对应处理确认",
             "SOK2（S29 红鲑返河动机未定 Semantic Open）：typed MC 占位+"
             "STATE_GATED 互证 non-match——P05 停食门系无新增的记录口径",
             "顺序推导纪律执行确认（§5.1）：112 Story 逐条顺序扫描无面内 "
             "early-return 判断链；策略层『先找位置再选呈现』为面间顺序"],
         "status": "PENDING_REVIEW"},
    ]
    (BATCH / "human_review_queue.jsonl").write_text(
        "\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n",
        encoding="utf-8")
    # discovery curve（只追加一行；registry 不动；幂等守卫防重复 append）
    c = ROOT / "discovery_curve.csv"
    current = io.open(c, encoding="utf-8").read()
    if "CENSUS-B7," in current:
        print("curve: CENSUS-B7 row already present (idempotent skip)")
    else:
        io.open(c, "w", encoding="utf-8").write(
            current.rstrip() + "\nCENSUS-B7,112,219,100,9,0,110,0,0,0,0,0,0,0\n")
    n_mc = sum(1 for m in M if m["verdict"] == "MERGE_CONFIDENT")
    n_ext = sum(1 for m in M if m["verdict"] == "TEMPLATE_EXTENSION_CANDIDATE")
    n_new = sum(1 for m in M if m["verdict"] == "NEW_TEMPLATE_CANDIDATE")
    n_amb = sum(1 for m in M if m["verdict"] == "AMBIGUOUS_NEEDS_EXPANSION")
    print(f"merge_tests={len(M)} (MC={n_mc} EXT={n_ext} NEWC={n_new} AMB={n_amb}) "
          f"programs={len(out)}")
    print("note: NEW records = 110 CRR singles + 11 grouped new-family + 1 "
          "grouped C9-candidate + 1 grouped field-vs-typed + 2 grouped "
          "guard-cross + 1 SOK2; program-family pairs total 1683 = "
          "110[CRR]+110[SINGLE]+110*11[newfam]+110[C9]+86[TYPED]+9[GUARD]"
          "+14[FOOD_FIELD]+14[field-vs-typed]+9*2[guard-cross]+1[SOK2]")


if __name__ == "__main__":
    main()
