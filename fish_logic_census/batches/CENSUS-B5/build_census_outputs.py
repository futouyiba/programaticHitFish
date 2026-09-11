# -*- coding: utf-8 -*-
"""CENSUS-B5 判同产物一体化脚本（merge_tests/programs/HRQ/absence/resolver/
coverage/revisions + discovery_curve 追加一行）。

registry 不动（章程：registry mutation 由独立审通过后另批处理——本批全部
归族/扩容提案进 HRQ）。

语义裁决依据：engine_report.json（raw）+ worker reasoning + B0-B4/RS1/RP1
判例链。核心裁决：
1) Bake 52 vs SINGLE v1 → AMBIGUOUS_NEEDS_EXPANSION：engine raw 仅 op 名
   字面（OPERATOR）+PREMISE，骨架同构——但 SINGLE v1 canonical 已被 RS1
   全体成员证伪（61/61 body 结构差异、0 匹配，HRQ-RS1-01 pending）。本批
   输入层与 B1-B4 同源（Story 正文十节），RS1 已证明该层平铺形相对顺序
   还原形系统性收敛（表达文件档位/门形在 Story 层被抹平）。故归族裁决
   blocked：不 MC（不对被证伪 canonical 制造确信合并记录）；不 NEW 单独
   立族（平铺输入立族=RS1 反例「平铺输入→伪结构收敛」）。→ HRQ-B5-01。
2) Bake 52 vs CRR → NEW non-match（B0-B4 连续回落测试第 5 批）。
3) Bake 52 vs 11 新族 → NEW non-match 分组（每族 52 程序 engine diff
   完全一致——distinct_diff_sets=1，分组记录无损）。
4) RESP 43 vs TYPED → MERGE_CONFIDENT（raw 仅 PREMISE 或空——F02）。
5) guard 9 vs GUARD → TEMPLATE_EXTENSION_CANDIDATE（骨架同构：deps 位形
   [ [],[],[0,1],[2] ]/branches 空/RETURN 同；raw 仅槽名/合并步标名字面
   ——B4-HNC 同型）。新内容=anchor 9 新值 + guard_participant(biparental)
   NEW 轴提案 + fan 扇护子动作语义 → HRQ-B5-02。
6) guard 9 vs STATE_GATED/TYPED → NEW 分组互证（§9.2 两拓扑边界第 5 例
   互证 / 单路径边界）。
"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"bake_membership": "HRQ-B5-01",
       "guard_ext": "HRQ-B5-02",
       "members": "HRQ-B5-03"}

BAKE_ORDER = ["SAF", "ARO", "CSL", "AKB", "MHS", "SPM", "YFT", "STM", "ALB",
              "STL", "ARG", "LKT", "RHM", "RBP", "TMU", "SPK", "DTN", "GAJ",
              "HAD", "BPB", "RVC", "CRC", "INC", "HBW", "CLC", "RTC",
              "WST", "ROB", "KGO", "LMD", "MDC", "JGC", "SPC", "TGT", "HYC",
              "PRC", "CCR", "APA", "GOT", "GIT", "SVT", "PEL", "CMR", "LKR",
              "ASP", "BIA", "HLL", "BAS", "JDP", "LMP", "AMK", "GSF"]
GUARD_9 = ["ARO", "CSL", "CRC", "ROB", "MDC", "JGC", "JDP", "LMP", "AMK"]
TYPED_43 = [s for s in BAKE_ORDER if s not in GUARD_9]
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
        "BRANCH（typed 因子三档分级命中+EARLY_RETURN）vs 本批平链无档位",
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

GUARD_DETAIL = {
    "ARO": {
        "anchor": "mouthbrooding_male（雄口哺携带卵/幼近 6 周——携带型 anchor："
                  "守护对象随身携带 vs 结构型巢/穴）",
        "extra": "携带型 vs 结构型 anchor 语义域问题（Story Open Question：口哺"
                 " guard 与巢 guard 的 P04 表达差异）",
        "note": "银龙鱼水面跳捕+雄口哺"},
    "CSL": {
        "anchor": "nest_pelagic_larvae（雄护卵+浮游幼体——守护对象跨两发育阶段）",
        "extra": "守护对象阶段扩展（卵+浮游幼）",
        "note": "葛氏鲈塘鳢静水伏击+护卵幼"},
    "CRC": {
        "anchor": "gravel_ridge（雄砾巢脊连续建造——挖坑→覆石→紧邻下游再挖成脊）",
        "extra": "石巢系第 3 例异属独立演化（Nocomis R07 + Semotilus 本例）；"
                 "脊形连续建造 vs 丘形单体（HNC pebble_mound 邻近值）",
        "note": "黑斑须雅罗鱼头源掠食+砾巢脊"},
    "ROB": {
        "anchor": "rock_nest_fan（雄岩巢扇护+防御复合约 14 天——fan 供氧子动作）",
        "extra": "fan 扇护子动作语义（供氧+御敌复合）；一巢多雌 mating system "
                 "premise",
        "note": "岩钝鲈岩区浅水+雄巢扇护"},
    "MDC": {
        "anchor": "cave_ceiling（洞顶产卵——产卵位垂直面选择）",
        "extra": "guard_participant=biparental（双亲参与——NEW 轴提案值）",
        "note": "米达斯慈鲷岩壁运河+洞顶双亲护"},
    "JGC": {
        "anchor": "nest_biparental（浊水湖巢）",
        "extra": "guard_participant=biparental（双亲——NEW 轴提案值，与 MDC "
                 "同型跨属重复）",
        "note": "淡水石斑浊水湖掠食+双亲护卵幼"},
    "JDP": {
        "anchor": "flood_spawn_male_guard（洪水事件机会繁殖+雄护卵复合）",
        "extra": "P05 洪水系×P04 guard 复合 anchor（洪水事件触发繁殖 premise + "
                 "守护持续）",
        "note": "宝石鲈洪水机会繁殖+雄护卵"},
    "LMP": {
        "anchor": "egg_mass_rock（附着卵块激进守护——非巢结构型：无建造行为）",
        "extra": "非建造 anchor 类（附着卵块）；雌雄二态呈现变量 typed context "
                 "候选",
        "note": "圆鳍鱼吸盘底栖+雄护卵块"},
    "AMK": {
        "anchor": "rock_crevice_fan（岩缝产卵+胸鳍连续扇护 40-45 天）",
        "extra": "fan 扇护子动作语义（与 ROB 同型跨科重复——供氧子动作）；"
                 "一年两产 lifecycle 节奏 premise",
        "note": "单鳍多线鱼岩礁+岩缝扇护"},
}

TYPED_NOTES = {
    "SAF": "喙击打=攻击工具行为 typed（Story 明言改造目标可捕获性非生成机会；"
           "FishMode=Weak Open）；帆展开=攻击姿态 overlay",
    "AKB": "P01 冻结主张承载（食性 EO，MEDIUM）",
    "MHS": "杂食原文承载；头下位姿态假说 EO 不构程序输入（posture grain 内变量）",
    "SPM": "单独猎击 typed（负知识：非群游协作）",
    "YFT": "体型分级群游+FAD 关联=群结构事实 premise 排除",
    "STM": "鱼/甲壳/鱿标准；喙击打本种 EO（SAF 属例不外推）",
    "ALB": "混群+马尾藻=同场供给群结构事实排除",
    "STL": "海期食性标准；同种双型不拆 Group（P05）",
    "ARG": "水面昆虫+旅鼠 typed（水面呈现——S7 MSF）；背鳍求偶=繁殖信号排除",
    "LKT": "夜行低光 typed context（R03 先例）；夜产+清岩=lifecycle premise",
    "RHM": "植物叶取食 typed（离散善件型植物目标；草鱼 grazing 先例不买 Mode；"
           "食人鱼科植食反差例）",
    "RBP": "虫+腐植杂食 typed；幼体拟态=反捕食排除",
    "TMU": "狗鱼系伏击复用推算（Identity-Deferred，MEDIUM）",
    "SPK": "狗鱼型掠食 typed（名实分离——鲤科掠食，鳡鱼 R03 同型）；相食 premise",
    "DTN": "礁栖反差+小群鱼/鱿 typed；ciguatoxic CB 轴排除",
    "GAJ": "深礁鱼食 typed；ciguatera CB 轴排除",
    "HAD": "底栖小生物标准（鳕科第 2 例）",
    "BPB": "纯鱼食标准（Cichla 第 2 例）",
    "RVC": "P01 承载（食性 EO，MEDIUM）；石巢假说 EO 不预立 P04",
    "INC": "成鱼食小鱼 typed；停食洄游=P05 状态抑制 premise（第 3 例）——"
           "停食咬钩动机归因 open（STATE_GATED 升级三条件之①未闭合，维持 "
           "TYPED 最小骨架）",
    "HBW": "底栖软体/甲壳/摇蚊标准；双型 premise",
    "CLC": "同属 Silurus 推算伏击（MEDIUM）",
    "RTC": "鱼/蟹/果杂食 typed（果实=沉水植物果实输入，暹罗巨鲤同型）",
    "WST": "体型分级鱼食 typed；产卵前停食=P05 状态抑制 premise（第 4 例）——"
           "与 INC 同型 open 注记",
    "KGO": "静水植被杂食标准；接吻器功能假说 EO",
    "LMD": "同属鳜属推算伏击（MEDIUM）",
    "SPC": "characid 鱼食标准（Cichla 第 3 例）；护巢 EO 不预立 P04",
    "TGT": "亲本鲑鳟系复用推算（Identity-Deferred，MEDIUM）",
    "HYC": "鲫系底栖杂食复用推算（Identity-Deferred，MEDIUM）",
    "PRC": "底栖杂食标准；雌核发育=繁殖系统变量 premise",
    "CCR": "夜行底栖杂食 typed（夜行=低光 context R03 先例）；干冬钻泥=蛰伏 "
           "premise（第 5 例）",
    "APA": "山地溪流食性栖息推断承载（S1 MSF 无食性引文，MEDIUM）",
    "GOT": "P01 冻结主张承载（食性 EO，MEDIUM；稀有鳟系同构推断）",
    "GIT": "P01 冻结主张承载（食性 EO，MEDIUM）",
    "SVT": "端足类专食 typed（exclusively 原文）；双种群分离 premise",
    "PEL": "三态食性 breadth typed（浮游/底栖/水面——非分级门）；三型 premise",
    "CMR": "底栖/浮游/植物/腐屑杂食标准（双行 A）",
    "LKR": "同种杂食复用（双行 B——同种同 URL 引文同源，非跨种推算）",
    "ASP": "结构伏击鱼食 typed（桥墩/堰坝位点；鲤科罕见 piscivore）+水面呈现",
    "BIA": "獠牙掠食形态推断（MEDIUM）",
    "HLL": "trophic 2.3 植食倾向推算（MEDIUM）",
    "BAS": "植食 typed；洪水周期 premise+气呼吸 runtime premise",
    "GSF": "幼食未成熟虫/微型甲壳 typed（ontogeny premise）；巢产 EO 不预立 P04",
}

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
RAW_FAM = {(r["program_id"], r["family"]): r["engine_structural_diff"]
           for r in ENGINE["family"]}
RAW_CROSS = {g["family"]: {r["program_id"]: r["engine_structural_diff"]
                           for r in g["rows"]}
             for g in ENGINE["guard_cross"]}

M = []
# --- 1) Bake 52 vs SINGLE v1：AMBIGUOUS_NEEDS_EXPANSION（归族 blocked by HRQ-RS1-01）---
for sid in BAKE_ORDER:
    pid = f"P-B5-{sid}-BAKE"
    M.append({"program_id": pid,
              "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "AMBIGUOUS_NEEDS_EXPANSION", "same": None,
              "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": RAW_SINGLE[pid],
              "blocked_by": "HRQ-RS1-01（SINGLE v1 canonical 证伪待裁决）",
              "reasoning": "engine raw 仅 op 名字面（OPERATOR=EVAL_HABITAT_"
                           "FACTOR_POSITION vs EVAL_TYPED_FIELD_OR_FACTOR，B4 "
                           "同型槽名差异）+PREMISE——骨架同构。但 SINGLE v1 "
                           "canonical 已被 RS1 全体成员证伪（61/61 body 结构差异、"
                           "0 匹配；HRQ-RS1-01 pending）：本批输入层与 B1-B4 同源"
                           "（Story 正文），RS1 已证明该层平铺形相对顺序还原形系统"
                           "性收敛。归族两难：不 MC（不对被证伪 canonical 制造确信"
                           "合并——B4 25 成员已陷 moved_pending_review 同态）；不 NEW "
                           "立族（平铺输入立族=RS1 反例）。裁决=v1 保留则本批按 B4 "
                           "先例 MC 入族；拆分批准则本批对 9 新族重裁（全 non-match，"
                           "真形需 B 表达顺序还原输入另批）。挂 HRQ-B5-01。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B5"}})
# --- 2) Bake 52 vs CRR：NEW non-match（第 5 批连续 0 成员）---
for sid in BAKE_ORDER:
    pid = f"P-B5-{sid}-BAKE"
    M.append({"program_id": pid,
              "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(RAW_CRR[pid]) - {"PREMISE"}),
              "engine_raw_diffs": RAW_CRR[pid],
              "reasoning": "CRR 判别结构（BUILD→GATE→RelativeRank(reference_set="
                           "FeasibleSet)→secondary→FIXED）不存在：普通层批为 premise "
                           "绑定切换（洄游/季节/洪水/温升/停食）与静态结构/因子绑定"
                           "形态。CRR 连续第 5 批 0 成员（B0-B5 累计 127 non-match；"
                           "HRQ-B2-02 维持人类裁决）。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B5"}})
# --- 3) Bake 52 vs 11 新族：NEW 分组 non-match ---
for fam in NEW_FAMILIES:
    rows = RAW_NEWFAM[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": [f"P-B5-{sid}-BAKE" for sid in BAKE_ORDER],
              "n_programs": len(BAKE_ORDER),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": f"52 程序 engine diff 完全一致（distinct_diff_sets=1）。"
                           f"{NEW_FAM_REASON[fam]}——本批 Story 层无面内判断链/"
                           f"档位/门证据（顺序扫描结论，manifest order_discipline），"
                           f"与该族档位形真结构差异。注意：non-match 对平铺输入"
                           f"成立的含义受 RS1 教训限定（Story 层平链本身是收敛形——"
                           f"真形待顺序还原），与条目 1 的 AMBIGUOUS 同源挂账。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B5"}})
# --- 4) RESP 43 vs TYPED：MERGE_CONFIDENT ---
for sid in TYPED_43:
    pid = f"P-B5-{sid}-RESP"
    M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")],
              "reasoning": f"engine 仅 PREMISE（F02 不计）或无差异。实例注记："
                           f"{TYPED_NOTES[sid]}。",
              "provenance": {"batch": "CENSUS-B5"}})
# --- 5) guard 9 vs GUARD：TEMPLATE_EXTENSION_CANDIDATE ---
for sid in GUARD_9:
    pid = f"P-B5-{sid}-RESP"
    d = GUARD_DETAIL[sid]
    M.append({"program_id": pid,
              "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
              "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False,
              "param_only": True, "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "GUARD_CONFLICT_DUAL_PATH_RESPONSE")],
              "extension_complexity_cost":
                  "+anchor 轴新值（intruder_evaluator_context 第 7 值起——"
                  f"{d['anchor']}）挂既有 intruder evaluator 槽；canonical body "
                  "零改动（deps 位形 [ [],[],[0,1],[2] ]/branches 空/RETURN 同）；"
                  "fan 扇护/双亲参与为 evaluator/守护行为 typing 非新增 branch",
              "new_template_complexity_cost":
                  "为 anchor 值/参与者/扇护子动作差异复制整条 ∥ 并行双路径拓扑为"
                  "独立族——与 GUARD 既有 7+1 成员全部骨架同构（仅 anchor/参与者/"
                  "子动作 typed 不同），9 例将各自立族=家族数爆炸，违反 F10/F14 节俭",
              "recommended_shape":
                  "扩展 GUARD：9 例入族为第 9-17 名义成员（anchor 轴 9 新值提案+"
                  "guard_participant(biparental) NEW 轴提案+fan 子动作语义 open）"
                  "——HRQ-B5-02 待批；批前按 extension 候选挂账（HNC 第 8 名义"
                  "先例）",
              "proposed_parameter_axis":
                  f"intruder_evaluator_context 新值提案（{d['anchor']}）"
                  "+guard_participant(typed: male | biparental——NEW 轴提案，"
                  "MDC/JGC 双亲例跨属重复）",
              "reasoning": f"骨架同构：并行双 evaluator（deps 位形与 canonical 一致、"
                           f"branches 空、RETURN 同）→ combine → decide；engine raw "
                           f"差异全为字面（intruder 槽名 EVAL_NEST_INTRUDER_RELATION "
                           f"vs EVAL_TARGET_AS_INTRUDER_TYPED；合并步标名 "
                           f"COMBINE_CONFLICT_AWARE vs COMBINE_DUAL_PATH——B4-HNC "
                           f"同型字面，B3 判同经验）。实例={sid}：{d['note']}；"
                           f"新内容={d['extra']}。谓词/子动作/参与者 typing 非新增 "
                           f"branch/gate（拓扑不变）→ 有限 typed 新参数轴 → "
                           f"TEMPLATE_EXTENSION_CANDIDATE（F14 非 plain merge）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B5"}})
# --- 6) guard 9 跨族互证（分组）---
for fam, reason in (
    ("STATE_GATED_MULTI_PATH_RESPONSE",
     "§9.2 两拓扑边界第 5 例互证（9 例同型）：∥ 同刻并行竞争（无分支）vs IF "
     "状态门互斥；RelationalConflict vs NonFeedingStrike——双向 non-match 维持"
     "（B3/B4 判例）"),
    ("TYPED_TARGET_RESPONSE",
     "单路径边界互证（9 例同型）：单 evaluator vs ∥ 双 evaluator+combine+双值 "
     "RETURN——GUARD 族域判据维持（B0 OSC 先例同型）")):
    rows = RAW_CROSS[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": [f"P-B5-{sid}-RESP" for sid in GUARD_9],
              "n_programs": len(GUARD_9),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": reason + "。9 程序 engine diff 完全一致"
                           "（distinct_diff_sets=1）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B5"}})

FAMILY_OF = {}
for sid in BAKE_ORDER:
    FAMILY_OF[f"P-B5-{sid}-BAKE"] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT",
                                     HRQ["bake_membership"], "PENDING_SPLIT_RULING")
for sid in TYPED_43:
    FAMILY_OF[f"P-B5-{sid}-RESP"] = ("TYPED_TARGET_RESPONSE", HRQ["members"], None)
for sid in GUARD_9:
    FAMILY_OF[f"P-B5-{sid}-RESP"] = ("GUARD_CONFLICT_DUAL_PATH_RESPONSE",
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
               "provenance": {"batch": "CENSUS-B5"}}
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
        "note": "B5 未新增 resolver family；洄游/季节/洪水周期/温升触发/停食状态/"
                "蛰伏/气呼吸/雌核发育/三倍体/杂交身份/保护边界/喙击打工具/扇护子"
                "动作/雌雄二态均为世界侧 fact、premise 供给义务或 evaluator typed "
                "context（上游 SNAP 登记同 B1-B4）",
        "provenance": {"batch": "CENSUS-B5"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # absence claims：非强宣称——Bake 归族挂起说明（与 HRQ-RS1-01 联动）
    (BATCH / "absence_claims.jsonl").write_text(json.dumps({
        "story_id": "CENSUS-B5-AGGREGATE",
        "claim": "BAKE_MEMBERSHIP_PENDING_SPLIT_RULING",
        "scope": "Bake 52 程序对 SINGLE v1 归族 = AMBIGUOUS_NEEDS_EXPANSION"
                 "（非 non-match 亦非 MC）：v1 canonical 证伪待裁决（HRQ-RS1-01），"
                 "本批 Story 层平链与 B1-B4 成员同层同态（B4 25 成员已 "
                 "moved_pending_review）",
        "evidence_basis": "engine raw 仅 op 名字面（骨架同构）；RS1 61/61 证伪"
                          "记录；本批顺序扫描无面内判断链（manifest "
                          "order_discipline）",
        "does_not_claim": "非 NO_NEW_PROGRAM_PROVEN / LOCAL_SATURATION——52 AMB "
                          "是归族挂起不是饱和证据；真形需 B 表达顺序还原输入"
                          "（独立 envelope 同 B0-B2 重跑范式）",
        "provenance": {"batch": "CENSUS-B5"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # HRQ
    hrq = [
        {"queue_id": HRQ["bake_membership"], "batch": "CENSUS-B5",
         "kind": "AMBIGUOUS_MEMBERSHIP_BLOCKED_BY_SPLIT_RULING",
         "surface": "Bake",
         "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
         "question": "B5 Bake 52 程序（普通层 R08+R09 双包）对 SINGLE v1 归族裁决="
                     "AMBIGUOUS_NEEDS_EXPANSION：engine raw 仅 op 名字面（骨架同构"
                     "平链），但 v1 canonical 已被 RS1 全体成员证伪（61/61 body 结构"
                     "差异、0 匹配）且 HRQ-RS1-01 裁决 pending。本批输入层与 B1-B4 "
                     "同源（Story 正文十节，非顺序还原表达文件）——RS1 已证明该层"
                     "平铺形系统性收敛（档位/门形在 Story 层被抹平）。",
         "verdict_branches": [
             "若 HRQ-RS1-01 裁 SINGLE v1 保留（拆分不批准）：本批 52 按 B4 先例"
             "升 MC 入族（名义 66→118），随之继承 moved_pending_review 风险",
             "若裁拆分批准（9 新族成立）：本批 52 对新族全 non-match（engine "
             "BRANCH 等真差异已实测）——真形判定需 B 表达顺序还原输入（独立 "
             "envelope，B0-B2 重跑范式）后重裁；本批挂账态不变"],
         "pending_review_questions": [
             "本批与 B4 25 成员（已 moved_pending_review）同态联动——HRQ-RS1-01 "
             "裁决时两批成员一并处置",
             "vs 11 新族分组 non-match 的含义限定（Story 层平链是收敛形——"
             "non-match 真对象是『平链』不是『鱼的真实程序』），merge_tests 条目"
             "已注记",
             "CRR 连续第 5 批 0 成员（累计 127 non-match）——HRQ-B2-02 维持"],
         "related": ["HRQ-RS1-01（SINGLE 拆分总裁决）", "HRQ-B4-02（B4 25 成员备案）",
                     "absence_claims.jsonl BAKE_MEMBERSHIP_PENDING_SPLIT_RULING"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["guard_ext"], "batch": "CENSUS-B5",
         "kind": "TEMPLATE_EXTENSION_CANDIDATE", "surface": "Response",
         "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
         "question": "B5 P04 guard 9 例（R08 3+R09 6——ARO 口哺/CSL 护卵幼/"
                     "CRC 砾巢脊/ROB 雄巢扇护/MDC 洞顶双亲/JGC 浊水双亲/JDP 洪水"
                     "护卵/LMP 卵块激进/AMK 岩缝扇护）入 GUARD 族：9/9 骨架同构"
                     "直验（∥ 双 evaluator→combine→decide；deps 位形/branches/"
                     "RETURN 与 canonical 一致；engine raw 仅槽名/合并步标名字面"
                     "——B4-HNC 同型）。",
         "proposed_axes": [
             "intruder_evaluator_context 9 新值提案（第 7-15 值：mouthbrooding_male"
             "[携带型]/nest_pelagic_larvae/gravel_ridge/rock_nest_fan/cave_ceiling/"
             "nest_biparental/flood_spawn_male_guard/egg_mass_rock/rock_crevice_fan）",
             "guard_participant(typed: male | biparental)——NEW 轴提案（MDC+JGC "
             "双亲例跨属重复；B0-B4 成员默认 male 未显式分型）",
             "fan 扇护子动作（ROB+AMK 跨科重复）——guard Path 内供氧子动作语义："
             "typed 子步 vs 结构元素，当前证据（『fan and defend』/『continuously "
             "fans』单句）只支撑行为修饰 typing，不支撑面内 branch"],
         "complexity_comparison": {
             "extension": "+anchor 轴 9 值+1 有限 typed 轴挂既有 evaluator/守护槽；"
                          "canonical 零改动；不触发全族回归复检（F15）",
             "new_template": "9 例按 anchor/参与者差异各自立族——与既有 7+1 成员"
                             "全部骨架同构，家族数爆炸违反节俭（F10/F14）",
             "recommended": "extension（worker 裁定；HRQ 批准后 anchor 轴值+新轴"
                            "正式入声明，9 例入族为第 9-17 名义成员）"},
         "pending_review_questions": [
             "携带型 anchor（ARO 口哺）语义域：守护对象随身携带 vs 结构型巢/穴——"
             "anchor 轴内值 vs 新轴（Story Open Question：口哺 guard 与巢 guard 的 "
             "P04 表达差异）",
             "fan 扇护是否需结构化（IF 供氧门→扇护分支）——当前证据不足，若 FR 线"
             "给出扇护行为序列证据则重开",
             "非建造 anchor 类（LMP 附着卵块无建造行为；MDC 洞顶=自然结构选择）"
             "与建造型（CRC 砾脊/ROB 岩巢）的轴内一致性",
             "guard_participant 轴与 P04 语义层『双亲 vs 雄性』两层登记维持（P04="
             "Candidate；census 扩容不自动 promote）",
             "P04 pattern 页 Mechanism Stories 清单已含本批 9 例 URL（FR 层索引先"
             "于 census——无盲纪律影响，pattern 页非 census registry）"],
         "related": ["HRQ-06(B0)", "HRQ-B3-02（anchor 轴扩容先例）",
                     "HRQ-B4-01（HNC extension 先例+guard_target_specificity 轴）"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["members"], "batch": "CENSUS-B5",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Response",
         "template_id": "TYPED_TARGET_RESPONSE",
         "question": "TYPED +43 MC（74→117 名义 pending review）：R08+R09 普通层"
                     "43 标准 typed 成员；GUARD +9 extension 候选（HRQ-B5-02）；"
                     "Bake 52 AMBIGUOUS 挂账（HRQ-B5-01）；ΔL 全零"
                     "（group/bake/response/quality）",
         "pending_review_questions": [
             "TYPED 13 例 MEDIUM 推算成员证据分层（AKB/APA/GOT/GIT/LMD/HLL/AMK="
             "P01 冻结主张或栖息推断承载；TMU/TGT/HYC=亲本/鲫系复用推算"
             "[Identity-Deferred]；BIA=獠牙形态推断；RVC=同属推算；CLC=同属推算）"
             "——是否全部入族 or 部分降 EO 待 FR 线引文（S1 EO 面）",
             "停食洄游第 3/4 例（INC 白北鲑/WST 高首鲟）：Story 层停食事实=P05 状态"
             "抑制 premise（判例维持），停食咬钩动机归因 open——STATE_GATED 升级"
             "三条件之①未闭合，成员保持 TYPED 最小骨架；与 HRQ-B3-01 联动",
             "同种双行 2 例（CMR/LKR 同 Rutilus rutilus 双行同批）：程序体同源"
             "（同 URL FishBase 页）——Cross-Batch 合并处置时两程序去重联动",
             "身份层 4 例（TMU/TGT/HYC=杂交/工程 Identity-Deferred；LKR=双行 "
             "Deferred）：机制复用推算 MEDIUM——身份裁决归 FR 线",
             "packet 计数口径差异：R08 packet 声明 P04×4 而 story Semantic Pattern "
             "字段实际 3 例（ARO/CSL/CRC）——疑 packet 将 CSL 护卵+护浮游幼分开计"
             "或含同属注记；本批按 story 字段 9 例处理（manifest 已记）",
             "顺序推导纪律执行确认（§5.1）：52 Story 逐条顺序扫描，无一面内 "
             "early-return 判断链；时序均为 lifecycle/季节/洪水/昼夜 premise 配置"
             "级（判例④/P05 状态抑制）"],
         "status": "PENDING_REVIEW"},
    ]
    (BATCH / "human_review_queue.jsonl").write_text(
        "\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n",
        encoding="utf-8")
    # discovery curve（只追加一行；registry 不动）
    c = ROOT / "discovery_curve.csv"
    t = io.open(c, encoding="utf-8").read().rstrip() + \
        "\nCENSUS-B5,52,104,43,9,0,52,0,0,0,0,0,0,0\n"
    io.open(c, "w", encoding="utf-8").write(t)
    n_mc = sum(1 for m in M if m["verdict"] == "MERGE_CONFIDENT")
    n_ext = sum(1 for m in M if m["verdict"] == "TEMPLATE_EXTENSION_CANDIDATE")
    n_new = sum(1 for m in M if m["verdict"] == "NEW_TEMPLATE_CANDIDATE")
    n_amb = sum(1 for m in M if m["verdict"] == "AMBIGUOUS_NEEDS_EXPANSION")
    print(f"merge_tests={len(M)} (MC={n_mc} EXT={n_ext} NEWC={n_new} AMB={n_amb}) "
          f"programs={len(out)}")
    print("note: NEW records = 52 CRR singles + 11 grouped new-family + 2 grouped "
          "guard-cross (program-family pairs: 52 + 572 + 18 = 642)")


if __name__ == "__main__":
    main()
