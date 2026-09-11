# -*- coding: utf-8 -*-
"""CENSUS-B6 判同产物一体化脚本（merge_tests/programs/HRQ/absence/resolver/
coverage/revisions + discovery_curve 追加一行）。

registry 不动（章程：registry mutation 由独立审通过后另批处理——本批全部
归族/扩容提案进 HRQ）。

语义裁决依据：engine_report.json（raw）+ worker reasoning + B0-B5/RS1/RP1
判例链。核心裁决：
1) Bake 47 vs SINGLE v1 → AMBIGUOUS_NEEDS_EXPANSION：engine raw 仅 op 名
   字面（OPERATOR）+PREMISE，骨架同构——但 SINGLE v1 canonical 已被 RS1
   全体成员证伪（61/61，HRQ-RS1-01 pending；B5 52 AMB 同态先例）。
   本批输入层与 B1-B5 同源（Story 正文压缩模板——表达层更薄，档位/门形
   同样被抹平）。归族裁决 blocked：不 MC 不 NEW 单独立族。→ HRQ-B6-01。
2) Bake 47 vs CRR → NEW non-match（B0-B5 连续回落测试第 6 批，累计 174）。
3) Bake 47 vs 11 新族 → NEW non-match 分组（每族 47 程序 engine diff
   完全一致——distinct_diff_sets=1）。
4) Bake 47 vs C9（ORDERED_QUAD_TIER_COMBINE_CHAIN，pending 候选族）→
   NEW non-match 分组 + HRQ-RS1-05 联动注记（envelope 指示：非 registry
   族，C9 立族裁决时本批 47 对为其第 6 批 non-match 素材）。
5) RESP 45 vs TYPED → MERGE_CONFIDENT（raw 仅 PREMISE 或空——F02）。
6) guard 2 vs GUARD → TEMPLATE_EXTENSION_CANDIDATE（骨架同构：deps 位形
   [ [],[],[0,1],[2] ]/branches 空/RETURN 同；raw 仅槽名/合并步标名字面
   ——B4-HNC/B5-② 同型）。新内容=AWF 狼鱼卵块守护+护卵停食语境 / LFB
   贝宿主繁殖关系（anchor 轴第 16-17 值候选——与 HRQ-B5-02 轴系联动）
   → HRQ-B6-02。
7) guard 2 vs STATE_GATED/TYPED → NEW 分组互证（§9.2 两拓扑边界 B5 后
   再证 / 单路径边界）。
"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"bake_membership": "HRQ-B6-01",
       "guard_ext": "HRQ-B6-02",
       "members": "HRQ-B6-03"}

BAKE_ORDER = ["SUK", "GRK", "KHK", "OGK", "LCP", "AMC", "HFC", "ASC",
              "WCC", "AGC", "WS2", "WAG", "HYS", "ACA", "ATC", "AWF",
              "PSH", "LFB", "BMB", "PLC", "SSM", "CGD", "GDB", "RBD",
              "RUF", "DBC", "JSB", "ASB", "DCL", "BHM", "WHC", "PRB",
              "RSS", "PCC", "STS", "PKC", "BCF", "TGS", "EUP", "BTS",
              "GDS", "SLM", "PKS", "BLT", "RSC", "BBH", "AMN"]
GUARD_2 = ["AWF", "LFB"]
TYPED_45 = [s for s in BAKE_ORDER if s not in GUARD_2]
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
C9 = "ORDERED_QUAD_TIER_COMBINE_CHAIN"

GUARD_DETAIL = {
    "AWF": {
        "anchor": "wolf_egg_mass_fasting_guard（雄鱼守护卵块直至孵化+护卵期"
                  "几乎不进食——硬壳碾压摄食并行）",
        "extra": "护卵期停食语境（停食判例第 5 例·护卵型首例——FR3 R10 关系"
                 "证实分支=P04 语境；与 P05 洄游停食 4 例的判例族关系留"
                 "review）；雄性单亲持续守护（参与形态=male，B0-B5 默认型）；"
                 "硬壳碾压齿系=typed context 非结构",
        "note": "大西洋狼鱼岩底硬壳碾压+雄护卵块停食"},
    "LFB": {
        "anchor": "mussel_brood（产卵管贝内产卵+幼贝内发育——贝宿主繁殖关系，"
                  "鳑鲏 R03 先例第 2 例跨属重复）",
        "extra": "贝宿主=繁殖对象依赖（Relation Object 语义——FR 层明言非新"
                 "捕食/资源程序）；守护对象在贝体内（隐蔽载体型 vs 巢/穴/"
                 "卵块附着型）；雌鱼产卵管=产卵工具行为变量非 branch",
        "note": "大鳍𫚪低营养杂食+贝内产卵幼贝发育"},
}

TYPED_NOTES = {
    "SUK": "锦鲤品系复用推算（Identity Deferred，Low——story 字段如实携带）",
    "GRK": "锦鲤品系复用推算（Identity Deferred，Low）",
    "KHK": "锦鲤品系复用推算（Identity Deferred，Low）",
    "OGK": "锦鲤品系复用推算（Identity Deferred，Low）",
    "LCP": "镜鲤品系复用推算（Identity Deferred，Low）",
    "AMC": "镜鲤白化品系复用推算（Identity Deferred，Low）",
    "HFC": "鳞鲤人面鲤品系复用推算（Identity Deferred，Low）",
    "ASC": "鳞鲤白化品系复用推算（Identity Deferred，Low）",
    "WCC": "叉尾鮰品系复用推算（Identity Deferred，Low）",
    "AGC": "草鱼品系复用推算+P02 grazing 背景（Identity Deferred，Low）",
    "WS2": "高首鲟白化品系复用（Identity Deferred，Low；与 B5 WST 同种"
           "同 URL——Cross-Batch 去重联动）",
    "WAG": "鳄雀鳝白化品系复用推算（Identity Deferred，Low）",
    "HYS": "杂交飼系复用推算（Identity Deferred，High——库锚即杂交式学名，"
           "判例第 3 例）",
    "ACA": "Silurus 同属第 2 例（『Adults feed on all types of fish』引文）"
           "+夜行同属推断（S7 EO）",
    "ATC": "小型底栖食标准+P05 溯河 premise（微型溯河鳕）",
    "PSH": "巨型鱼食标准（幼-成同食性）+P05 potamodromous；名实分离（库锚"
           "学名从——中文名大青鲨错位非 Identity Deferred）",
    "BMB": "杂食标准+P05 半溯河 premise",
    "PLC": "急流杂食标准（马口鱼系同构）",
    "SSM": "马鲛系第 3 例（同属同构）+P05 oceanodromous premise",
    "CGD": "沙底小型底栖标准；群游 S3 excluded（群结构事实）",
    "GDB": "鲂系同属推算（MEDIUM——S1 EO）",
    "RBD": "急流微底栖 typed（镖鲈科首例 darter 型）；卵埋底质=产卵行为"
           "变量非 guard（story FR 层明言，P04 假说不预立）",
    "RUF": "富营湖底栖标准；沿海鱼食=生境分化记录（S9）非分支；入侵供给="
           "OPS 注记",
    "DBC": "黄颡鱼系同属推算（MEDIUM——S1/S8 双 EO）",
    "JSB": "花鲈属同属参照（MEDIUM——maculatus 专项数据薄+历史同物异名；"
           "与 ASB 同 URL 同源——批内去重联动注记）",
    "ASB": "掠食标准（幼浮游→成鱼虾 ontogeny premise）+P05 降海+雄先熟"
           "性转换=繁殖系统变量 premise（降海型首例——洄游方向对照）",
    "DCL": "同唇䱌系同属推算（MEDIUM——薄资料同属替代，FishBase 公开版无页）",
    "BHM": "虫幼 typed（MEDIUM）",
    "WHC": "鮰系第 3 例杂食标准；story『鲿科』科名宽泛用法注记",
    "PRB": "巨型鱼食顶级掠食（MEDIUM——按 story 字段）+P05 potamodromous"
           " premise；猴/人胃含物=猎物谱记录",
    "RSS": "底栖无脊椎标准（太阳鱼系第 6 例）",
    "PCC": "毛鼻鲶科同属推算（MEDIUM——食性无述薄资料）",
    "STS": "深礁夜行甲壳/小鱼标准（夜行=昼夜时窗 premise）；V3 英文名"
           " Grouper 泛指错位注记（非 Identity Deferred）",
    "PKC": "慈鲷掠食型推算（MEDIUM——trophic 3.6，食性细节 EO）",
    "BCF": "无脊椎/贝/鱼标准+夜间摄食时窗 premise（深潭主河道）",
    "TGS": "夜行鱼食+蟹标准（夜间捕食时窗 premise；洪泛林栖息绑定）",
    "EUP": "昼间机会食标准（日出日落峰=昼夜时窗 premise；12cm 起鱼食="
           "ontogeny premise——非分级命中链）；名实分离（欧洲鲈，库锚"
           "学名从）",
    "BTS": "水面昆虫 typed（MEDIUM；水面呈现 S7——B5 ARG 同型）",
    "GDS": "浮游/虫/贝杂食标准；饵鱼 S10 excluded（产品面；B5 RVC 同属）",
    "SLM": "草食 typed（Serrasalmid 植食第 3 例——RHM/RBP 反差系延续）+"
           "P02 洪泛资源背景 premise",
    "PKS": "太阳鱼系第 7 例小鱼/无脊椎标准（无信封转写——正文承载为准）",
    "BLT": "P01 冻结主张承载（食性 EO，MEDIUM）；名实分离（Bull Trout，"
           "库锚学名从）；potamodromous premise",
    "RSC": "腐屑-无脊椎标准（MEDIUM）；群游 S3 excluded（群结构事实）",
    "BBH": "夜行杂食标准（昼夜时窗 premise；无信封转写——正文承载为准；"
           "story『鲿科』科名宽泛用法注记）",
    "AMN": "同属推算（MEDIUM——食性无述 trophic 3.5）",
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
RAW_C9 = {r["program_id"]: r["engine_structural_diff"]
          for r in ENGINE["vs_c9_candidate"][0]["rows"]}
RAW_FAM = {(r["program_id"], r["family"]): r["engine_structural_diff"]
           for r in ENGINE["family"]}
RAW_CROSS = {g["family"]: {r["program_id"]: r["engine_structural_diff"]
                           for r in g["rows"]}
             for g in ENGINE["guard_cross"]}

M = []
# --- 1) Bake 47 vs SINGLE v1：AMBIGUOUS_NEEDS_EXPANSION（归族 blocked by HRQ-RS1-01）---
for sid in BAKE_ORDER:
    pid = f"P-B6-{sid}-BAKE"
    M.append({"program_id": pid,
              "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "AMBIGUOUS_NEEDS_EXPANSION", "same": None,
              "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": RAW_SINGLE[pid],
              "blocked_by": "HRQ-RS1-01（SINGLE v1 canonical 证伪待裁决）",
              "reasoning": "engine raw 仅 op 名字面（OPERATOR=EVAL_HABITAT_"
                           "FACTOR_POSITION vs EVAL_TYPED_FIELD_OR_FACTOR，B4/B5 "
                           "同型槽名差异）+PREMISE——骨架同构。但 SINGLE v1 "
                           "canonical 已被 RS1 全体成员证伪（61/61 body 结构差异、"
                           "0 匹配；HRQ-RS1-01 pending）：本批输入层与 B1-B5 同源"
                           "（Story 正文——R10 更为压缩模板四节形，表达层更薄），"
                           "RS1 已证明该层平铺形相对顺序还原形系统性收敛。归族"
                           "两难：不 MC（不对被证伪 canonical 制造确信合并——"
                           "B4 25 成员已陷 moved_pending_review 同态，B5 52 AMB "
                           "同态先例）；不 NEW 立族（平铺输入立族=RS1 反例）。"
                           "裁决=v1 保留则本批按 B4 先例 MC 入族；拆分批准则本批"
                           "对 9 新族+C9 重裁（全 non-match 已实测，真形需 B 表达"
                           "顺序还原输入另批）。挂 HRQ-B6-01。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B6"}})
# --- 2) Bake 47 vs CRR：NEW non-match（第 6 批连续 0 成员）---
for sid in BAKE_ORDER:
    pid = f"P-B6-{sid}-BAKE"
    M.append({"program_id": pid,
              "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(RAW_CRR[pid]) - {"PREMISE"}),
              "engine_raw_diffs": RAW_CRR[pid],
              "reasoning": "CRR 判别结构（BUILD→GATE→RelativeRank(reference_set="
                           "FeasibleSet)→secondary→FIXED）不存在：收官批为 premise "
                           "绑定切换（品系复用/洄游/降海/昼夜/ontogeny）与静态"
                           "结构/因子绑定形态。CRR 连续第 6 批 0 成员（B0-B6 累计 "
                           "174 non-match；HRQ-B2-02 维持人类裁决）。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B6"}})
# --- 3) Bake 47 vs 11 新族：NEW 分组 non-match ---
for fam in NEW_FAMILIES:
    rows = RAW_NEWFAM[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": [f"P-B6-{sid}-BAKE" for sid in BAKE_ORDER],
              "n_programs": len(BAKE_ORDER),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": f"47 程序 engine diff 完全一致（distinct_diff_sets=1）。"
                           f"{NEW_FAM_REASON[fam]}——本批 Story 层（压缩模板）无"
                           f"面内判断链/档位/门证据（顺序扫描结论，manifest "
                           f"order_discipline），与该族档位形真结构差异。注意："
                           f"non-match 对平铺输入成立的含义受 RS1 教训限定"
                           f"（Story 层平链本身是收敛形——真形待顺序还原），"
                           f"与条目 1 的 AMBIGUOUS 同源挂账。",
              "human_review_queued": HRQ["bake_membership"],
              "provenance": {"batch": "CENSUS-B6"}})
# --- 4) Bake 47 vs C9（pending 候选族）：NEW 分组 + HRQ-RS1-05 联动 ---
rows = RAW_C9
diff_sets = {tuple(v) for v in rows.values()}
assert len(diff_sets) == 1, diff_sets
M.append({"program_id": [f"P-B6-{sid}-BAKE" for sid in BAKE_ORDER],
          "n_programs": len(BAKE_ORDER),
          "template_id": C9,
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
          "param_only": False,
          "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
          "engine_raw_diffs": sorted(next(iter(rows.values()))),
          "engine_uniform": True,
          "template_status": "PENDING_CANDIDATE_NOT_IN_REGISTRY（HRQ-RS1-05 待裁"
                             "——REV-001 修复轮 C9=无门有序四步档位链 4 HAB 成员）",
          "reasoning": "47 程序 engine diff 完全一致（distinct_diff_sets=1）。"
                       "BRANCH+COMBINE+DEPENDENCY+OPERATOR（无门有序四步档位链"
                       "+终步扇入 vs 本批平链两步）。**C9 联动注记（envelope "
                       "指示）**：C9 是 HRQ-RS1-05 的 pending 候选族、不在 "
                       "registry v8——本条 non-match 不构成 registry 族归并"
                       "记录；C9 立族裁决（HRQ-RS1-05）时本批 47 对为第 6 批"
                       "平铺输入 non-match 素材（真形待 B 表达顺序还原），与 "
                       "HRQ-RS1-01/B5-01/B6-01 三层挂账链同源。",
          "human_review_queued": HRQ["bake_membership"],
          "related_review": "HRQ-RS1-05（C9 立族+成员归宿裁决联动）",
          "provenance": {"batch": "CENSUS-B6"}})
# --- 5) RESP 45 vs TYPED：MERGE_CONFIDENT ---
for sid in TYPED_45:
    pid = f"P-B6-{sid}-RESP"
    M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")],
              "reasoning": f"engine 仅 PREMISE（F02 不计）。实例注记："
                           f"{TYPED_NOTES[sid]}。",
              "provenance": {"batch": "CENSUS-B6"}})
# --- 6) guard 2 vs GUARD：TEMPLATE_EXTENSION_CANDIDATE ---
for sid in GUARD_2:
    pid = f"P-B6-{sid}-RESP"
    d = GUARD_DETAIL[sid]
    M.append({"program_id": pid,
              "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
              "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False,
              "param_only": True, "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "GUARD_CONFLICT_DUAL_PATH_RESPONSE")],
              "extension_complexity_cost":
                  "+anchor 轴新值（第 16-17 值候选——B5 已提案 9 值待批，本批"
                  f"追加 {d['anchor']}）挂既有 intruder evaluator 槽；canonical "
                  "body 零改动（deps 位形 [ [],[],[0,1],[2] ]/branches 空/"
                  "RETURN 同）；护卵期停食/产卵管/贝宿主关系为 premise+语义"
                  "注记非新增 branch",
              "new_template_complexity_cost":
                  "为守护对象/语境差异复制整条 ∥ 并行双路径拓扑为独立族——与 "
                  "GUARD 既有 7+1+B5 候选 9 成员全部骨架同构（仅守护对象/"
                  "语境 typed 不同），各自立族=家族数爆炸，违反 F10/F14 节俭",
              "recommended_shape":
                  "扩展 GUARD：2 例入族为 B5 提案后第 18-19 名义成员（anchor 轴"
                  "第 16-17 值候选）——HRQ-B6-02 与 HRQ-B5-02 轴系合并裁决联动；"
                  "批前按 extension 候选挂账（HNC 第 8 名义先例）",
              "proposed_parameter_axis":
                  f"intruder_evaluator_context 新值候选（{d['anchor']}）"
                  "——B5 HRQ-B5-02 已提案 9 值（第 7-15）待批，本批追加形成"
                  "第 16-17 值候选；无 NEW 轴提案（guard_participant=male 为"
                  "既有默认型；贝宿主=Relation Object 语义非轴）",
              "reasoning": f"骨架同构：并行双 evaluator（deps 位形与 canonical 一致、"
                           f"branches 空、RETURN 同）→ combine → decide；engine raw "
                           f"差异全为字面（intruder 槽名 EVAL_NEST_INTRUDER_RELATION "
                           f"vs EVAL_TARGET_AS_INTRUDER_TYPED；合并步标名 "
                           f"COMBINE_CONFLICT_AWARE vs COMBINE_DUAL_PATH——B4-HNC/"
                           f"B5-② 同型字面，B3 判同经验）。实例={sid}：{d['note']}；"
                           f"新内容={d['extra']}。守护对象/语境 typing 非新增 "
                           f"branch/gate（拓扑不变）→ 有限 typed 新参数轴 → "
                           f"TEMPLATE_EXTENSION_CANDIDATE（F14 非 plain merge）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B6"}})
# --- 7) guard 2 跨族互证（分组）---
for fam, reason in (
    ("STATE_GATED_MULTI_PATH_RESPONSE",
     "§9.2 两拓扑边界再证（2 例同型）：∥ 同刻并行竞争（无分支）vs IF "
     "状态门互斥；RelationalConflict vs NonFeedingStrike——双向 non-match 维持"
     "（B3/B4/B5 判例链）。注：AWF 护卵停食与 STATE_GATED 洄游停食的语境"
     "对照（护卵型 vs 洄游型——FR3 R10 分支化）留 review，不改变本条拓扑"
     "判据"),
    ("TYPED_TARGET_RESPONSE",
     "单路径边界互证（2 例同型）：单 evaluator vs ∥ 双 evaluator+combine+"
     "双值 RETURN——GUARD 族域判据维持（B0 OSC 先例同型）")):
    rows = RAW_CROSS[fam]
    diff_sets = {tuple(v) for v in rows.values()}
    assert len(diff_sets) == 1, (fam, diff_sets)
    M.append({"program_id": [f"P-B6-{sid}-RESP" for sid in GUARD_2],
              "n_programs": len(GUARD_2),
              "template_id": fam,
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(next(iter(rows.values()))) - {"PREMISE"}),
              "engine_raw_diffs": sorted(next(iter(rows.values()))),
              "engine_uniform": True,
              "reasoning": reason + "。2 程序 engine diff 完全一致"
                           "（distinct_diff_sets=1）。",
              "human_review_queued": HRQ["guard_ext"],
              "provenance": {"batch": "CENSUS-B6"}})

FAMILY_OF = {}
for sid in BAKE_ORDER:
    FAMILY_OF[f"P-B6-{sid}-BAKE"] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT",
                                     HRQ["bake_membership"], "PENDING_SPLIT_RULING")
for sid in TYPED_45:
    FAMILY_OF[f"P-B6-{sid}-RESP"] = ("TYPED_TARGET_RESPONSE", HRQ["members"], None)
for sid in GUARD_2:
    FAMILY_OF[f"P-B6-{sid}-RESP"] = ("GUARD_CONFLICT_DUAL_PATH_RESPONSE",
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
               "provenance": {"batch": "CENSUS-B6"}}
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
        "note": "B6 未新增 resolver family；品系复用/杂交身份/洄游（溯河/半溯"
                "河/降海/potamodromous/oceanodromous）/昼夜时窗/夜行/ontogeny/"
                "性转换/护卵期停食/低氧耐热/洪泛依赖/入侵种/保护边界/名实分离"
                "均为世界侧 fact、premise 供给义务或 evaluator typed context"
                "（上游 SNAP 登记同 B1-B5）",
        "provenance": {"batch": "CENSUS-B6"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # absence claims：非强宣称——Bake 归族挂起说明（与 HRQ-RS1-01 联动）
    (BATCH / "absence_claims.jsonl").write_text(json.dumps({
        "story_id": "CENSUS-B6-AGGREGATE",
        "claim": "BAKE_MEMBERSHIP_PENDING_SPLIT_RULING",
        "scope": "Bake 47 程序对 SINGLE v1 归族 = AMBIGUOUS_NEEDS_EXPANSION"
                 "（非 non-match 亦非 MC）：v1 canonical 证伪待裁决"
                 "（HRQ-RS1-01），本批 Story 层平链与 B1-B5 成员同层同态"
                 "（B4 25 成员已 moved_pending_review；B5 52 AMB 同态）",
        "evidence_basis": "engine raw 仅 op 名字面（骨架同构）；RS1 61/61 证伪"
                          "记录；本批顺序扫描无面内判断链（manifest "
                          "order_discipline）",
        "does_not_claim": "非 NO_NEW_PROGRAM_PROVEN / LOCAL_SATURATION——47 AMB "
                          "是归族挂起不是饱和证据；真形需 B 表达顺序还原输入"
                          "（独立 envelope 同 B0-B2 重跑范式）；R10 为全库收官"
                          "批——后续无普通层新输入，顺序还原重跑为唯一补证通道",
        "provenance": {"batch": "CENSUS-B6"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # HRQ
    hrq = [
        {"queue_id": HRQ["bake_membership"], "batch": "CENSUS-B6",
         "kind": "AMBIGUOUS_MEMBERSHIP_BLOCKED_BY_SPLIT_RULING",
         "surface": "Bake",
         "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
         "question": "B6 Bake 47 程序（FISH-R10 全库收官批）对 SINGLE v1 归族"
                     "裁决=AMBIGUOUS_NEEDS_EXPANSION：engine raw 仅 op 名字面"
                     "（骨架同构平链），但 v1 canonical 已被 RS1 全体成员证伪"
                     "（61/61）且 HRQ-RS1-01 裁决 pending。本批输入层与 B1-B5 "
                     "同源且更薄（R10 压缩模板四节形——FISH-R10-FIX-001 F-B "
                     "已声明）——RS1 已证明 Story 层平铺形系统性收敛。",
         "verdict_branches": [
             "若 HRQ-RS1-01 裁 SINGLE v1 保留（拆分不批准）：本批 47 按 B4 先例"
             "升 MC 入族（名义 66→118+52+47=217），随之继承 moved_pending_"
             "review 风险",
             "若裁拆分批准（9 新族成立）：本批 47 对新族全 non-match（engine "
             "BRANCH 等真差异已实测）——真形判定需 B 表达顺序还原输入（独立 "
             "envelope，B0-B2 重跑范式）后重裁；本批挂账态不变"],
         "pending_review_questions": [
             "本批与 B4 25 成员+B5 52 AMB 同态三层联动——HRQ-RS1-01 裁决时"
             "三批成员一并处置",
             "vs 11 新族+C9 分组 non-match 的含义限定（Story 层平链是收敛形——"
             "non-match 真对象是『平链』不是『鱼的真实程序』），merge_tests "
             "条目已注记",
             "C9（ORDERED_QUAD_TIER_COMBINE_CHAIN，pending 候选族）联动：本批 "
             "47 对 C9 non-match 为 HRQ-RS1-05 立族裁决的第 6 批素材（envelope "
             "指示登记；不当 registry 族处理）",
             "CRR 连续第 6 批 0 成员（累计 174 non-match）——HRQ-B2-02 维持",
             "R10 收官批特殊性：后续无普通层新输入，Bake 真形补证唯一通道="
             "B 表达顺序还原重跑（全库 R01-R10 平链输入的系统性问题）"],
         "related": ["HRQ-RS1-01（SINGLE 拆分总裁决）", "HRQ-B5-01（B5 52 AMB "
                    "同态）", "HRQ-B4-02（B4 25 成员备案）", "HRQ-RS1-05（C9 "
                    "候选族联动）",
                    "absence_claims.jsonl BAKE_MEMBERSHIP_PENDING_SPLIT_RULING"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["guard_ext"], "batch": "CENSUS-B6",
         "kind": "TEMPLATE_EXTENSION_CANDIDATE", "surface": "Response",
         "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
         "question": "B6 P04 guard 2 例（AWF 大西洋狼鱼雄护卵块+护卵期停食"
                     "/LFB 大鳍𫚪贝内产卵+幼贝发育）入 GUARD 族：2/2 骨架同构"
                     "直验（∥ 双 evaluator→combine→decide；deps 位形/branches/"
                     "RETURN 与 canonical 一致；engine raw 仅槽名/合并步标名字面"
                     "——B4-HNC/B5-② 同型）。",
         "proposed_axes": [
             "intruder_evaluator_context 第 16-17 值候选（wolf_egg_mass_fasting_"
             "guard[狼鱼卵块守护+护卵停食语境]/mussel_brood[贝宿主繁殖关系——"
             "鳑鲏 R03 先例第 2 例跨属重复]）——与 HRQ-B5-02 已提案 9 值（第 "
             "7-15）合并裁决（anchor 轴累计 11 候选值）",
             "护卵期停食语境（AWF）：停食判例第 5 例·护卵型首例——FR3 R10 "
             "关系证实分支=P04 语境（guard premise 注记）；与 P05 洄游停食 "
             "4 例（INC/WST/HBW/BAS 系）的判例族关系（语境分支化是否需要"
             "结构承载）留 review",
             "贝宿主关系语义（LFB）：贝=繁殖对象依赖（Relation Object——FR 层"
             "明言非新捕食/资源程序）；守护对象在载体体内（隐蔽载体型 vs 巢/"
             "穴/卵块附着型）的轴内一致性；雌鱼产卵管=产卵工具行为变量"],
         "complexity_comparison": {
             "extension": "+anchor 轴 2 值候选挂既有 evaluator 槽；canonical "
                          "零改动；不触发全族回归复检（F15）",
             "new_template": "2 例按守护对象/语境差异各自立族——与既有 7+1+"
                             "B5 候选 9 成员全部骨架同构，家族数爆炸违反节俭"
                             "（F10/F14）",
             "recommended": "extension（worker 裁定；与 HRQ-B5-02 合并批准后 "
                            "anchor 轴值正式入声明，2 例入族为第 18-19 名义"
                            "成员）"},
         "pending_review_questions": [
             "与 HRQ-B5-02 的合并裁决（anchor 轴 9+2=11 候选值+participant 轴+"
             "fan 语义一并批）还是分批批",
             "护卵停食语境的 P04/P05 判例族分支化结构承载（FR3 relation 证实"
             "分支已裁 P04 语境——census 侧维持 premise 注记是否充分）",
             "mussel_brood 隐蔽载体型 anchor 与建造型/附着型/携带型（B5 提案）"
             "的轴内一致性",
             "P04 pattern 页 Mechanism Stories 清单是否已含本批 2 例 URL"
             "（FR 层索引先于 census——无盲纪律影响）"],
         "related": ["HRQ-B5-02（anchor 轴 9 值+participant 轴提案——合并裁决"
                     "联动）", "HRQ-06(B0)", "HRQ-B3-02（anchor 轴扩容先例）",
                     "HRQ-B4-01（HNC extension 先例）"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["members"], "batch": "CENSUS-B6",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Response",
         "template_id": "TYPED_TARGET_RESPONSE",
         "question": "TYPED +45 MC（B5 后名义 117→162 pending review）：R10 "
                     "收官批 45 标准 typed 成员（品系复用 11+杂交 1+普通层 "
                     "33）；GUARD +2 extension 候选（HRQ-B6-02）；Bake 47 "
                     "AMBIGUOUS 挂账（HRQ-B6-01）；ΔL 全零"
                     "（group/bake/response/quality）",
         "pending_review_questions": [
             "TYPED 14 例 MEDIUM 成员证据分层（GDB/DBC/JSB/DCL/PCC/PKC/BLT/"
             "AMN=同属推算或 P01 承载；BHM/BTS/RSC=story 字段 Medium；LFB "
             "guard MEDIUM）——是否全部入族 or 部分降 EO 待 FR 线引文",
             "身份层 13 例处理（品系 12 Low+杂交鲟 1 High，Verdict 全 Deferred）："
             "机制复用推算承载（B5-⑤ 判例——TMU/TGT/HYC 先例），身份裁决归 FR "
             "线；WS2 与 B5 WST 同种同 URL（Acipenser transmontanus）——"
             "Cross-Batch 去重联动（CMR/LKR 同型第 2 例）；JSB 与 ASB 同 URL "
             "同源（Lateolabrax japonicus 页）——批内去重联动注记",
             "R10 强实例注记：ASB 降海+雄先熟首例（洄游方向对照——P05 premise "
             "值差异非结构）；EUP 日升日落峰+12cm ontogeny（premise 配置级）；"
             "RBD 镖鲈科首例（卵埋底质 P04 假说不预立——story FR 层明言）",
             "packet 口径差异 4 项（manifest packet_count_reconciliation："
             "Confidence 24/11/12 vs 实测 23/12/12；P04×3 vs 正文 2[RBD 只记 "
             "P01]；P05×7 vs 正文 8[+WS2 品系继承]；DB Semantic Pattern 字段"
             "多数单值登记）——按 story 字段处理记档",
             "名实分离 3 例（PSH/EUP/BLT）=库锚学名从（非 Identity Deferred，"
             "中文名错位注记）——与品系 12 的 Identity Deferred 分型处理",
             "顺序推导纪律执行确认（§5.1）：47 Story 逐条顺序扫描，无一面内 "
             "early-return 判断链；时序均为 lifecycle/洄游/昼夜/ontogeny/guard "
             "期 premise 配置级（判例④/P05 状态抑制/FR3 R10 停食分支化）"],
         "status": "PENDING_REVIEW"},
    ]
    (BATCH / "human_review_queue.jsonl").write_text(
        "\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n",
        encoding="utf-8")
    # discovery curve（只追加一行；registry 不动）
    c = ROOT / "discovery_curve.csv"
    t = io.open(c, encoding="utf-8").read().rstrip() + \
        "\nCENSUS-B6,47,94,45,2,0,47,0,0,0,0,0,0,0\n"
    io.open(c, "w", encoding="utf-8").write(t)
    n_mc = sum(1 for m in M if m["verdict"] == "MERGE_CONFIDENT")
    n_ext = sum(1 for m in M if m["verdict"] == "TEMPLATE_EXTENSION_CANDIDATE")
    n_new = sum(1 for m in M if m["verdict"] == "NEW_TEMPLATE_CANDIDATE")
    n_amb = sum(1 for m in M if m["verdict"] == "AMBIGUOUS_NEEDS_EXPANSION")
    print(f"merge_tests={len(M)} (MC={n_mc} EXT={n_ext} NEWC={n_new} AMB={n_amb}) "
          f"programs={len(out)}")
    print("note: NEW records = 47 CRR singles + 11 grouped new-family + 1 "
          "grouped C9-candidate + 2 grouped guard-cross (program-family "
          "pairs: 47 + 47*12 + 2*2 = 615)")


if __name__ == "__main__":
    main()
