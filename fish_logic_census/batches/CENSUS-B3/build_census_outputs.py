# -*- coding: utf-8 -*-
"""CENSUS-B3 判同产物 + registry v4→v5 + discovery_curve（一体化脚本）。
语义裁决依据：engine_report.json（raw）+ worker reasoning；B0-B2 判例链。"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"state": "HRQ-B3-01", "guard": "HRQ-B3-02", "members": "HRQ-B3-03"}
AXIS = "轴属立族/扩容提案（HRQ 待批）；engine raw diff 为槽名/合并步标名字面差异，骨架同构"

BAKES = ["CHU", "CHN", "COH", "PIN", "BRO", "SHA", "ALE", "AST", "SNS", "TAR",
         "TAI", "ARA", "PB", "RBP", "BLP", "WEL", "FLA", "BUR", "GW", "SGA",
         "RFP", "DS", "PBF", "GT", "HAL", "GG"]
POSITION_BAKES = ["CHU", "CHN", "COH", "PIN", "BRO", "SHA", "ALE", "AST", "SNS",
                  "TAR", "ARA", "BUR", "PBF", "GT", "HAL"]   # P05 阶段/周期/季节绑定
STRUCTURE_BAKES = ["TAI", "PB", "RBP", "BLP", "WEL", "FLA", "GW", "SGA", "RFP",
                   "DS", "GG"]                                # 静态结构 anchor
TYPED_RESP = ["CHN", "COH", "PIN", "BRO", "ALE", "AST", "SNS", "TAR", "TAI",
              "PB", "BLP", "FLA", "BUR", "GW", "PAY", "SGA", "SHO", "RFP",
              "DS", "PBF", "GT", "HAL", "GG"]
GUARD_RESP = ["ARA", "RBP", "WEL"]
FASTING = ["CHU", "SHA"]

BLIND = {p["program_id"]: p for p in (
    json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(
        encoding="utf-8").splitlines() if l.strip())}

M = []
# --- 1) 26 Bake vs CRR：non-match（CRR 累计 24→50） ---
for sid in BAKES:
    M.append({"program_id": f"P-B3-{sid}-BAKE",
              "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "PREMISE"],
              "engine_raw_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "PREMISE"],
              "reasoning": "CRR 判别结构（BUILD→GATE→RelativeRank(reference_set="
                           "FeasibleSet)→secondary→FIXED）不存在：premise 绑定切换/"
                           "静态结构因子形态。归 SINGLE 候选族。CRR 本批仍零成员"
                           "（B3 选样=洄游/掠食层，无 refuge 类故事；HRQ-B2-02 输入"
                           "通道问题维持人类裁决）。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B3"}})
# --- 2) 26 Bake vs SINGLE：MERGE_CONFIDENT ---
for sid in POSITION_BAKES:
    M.append({"program_id": f"P-B3-{sid}-BAKE",
              "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": ["OPERATOR", "PREMISE"],
              "proposed_parameter_axis":
                  "factor_type(typed: habitat_factor(position/layer/depth))"
                  "+factor_binding(随 lifecycle/season/flood premise 切换)",
              "reasoning": f"骨架同构（单 typed 因子→归一化）；槽名字面在 factor_type 轴内"
                           f"（B1 HRQ-B1-01 声明域）。实例={sid}：P05 阶段/周期/季节绑定位置因子"
                           f"（洄游系/洪水周期/季节重排）。{AXIS}",
              "provenance": {"batch": "CENSUS-B3"}})
for sid in STRUCTURE_BAKES:
    M.append({"program_id": f"P-B3-{sid}-BAKE",
              "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": ["OPERATOR", "PREMISE"],
              "proposed_parameter_axis":
                  "factor_type(typed: habitat_factor(structure))",
              "reasoning": f"骨架同构；静态结构 anchor 因子（深潭/植被/急流/洞穴/倒木/"
                           f"逆流/洄湾/底栖/礁洞）——B2 FGA（植被结构）同型第 2-11 例。"
                           f"{AXIS}",
              "provenance": {"batch": "CENSUS-B3"}})
# --- 3) 23 Response vs TYPED：MERGE_CONFIDENT ---
TYPED_NOTES = {
    "AST": "须探底质 substrate relation（鲟科第三例）", "SNS": "夜行+软底质插探",
    "TAR": "群游猎物取向+上翘口水面呈现（气呼吸=runtime 条件 premise 非分支）",
    "TAI": "陆生猎物水面呈现（欧鲢 R05 同构）",
    "GW": "逆流+黄昏夜+水面呈现",
    "BUR": "颏须底探+低光（产卵球=繁殖集群排除）",
    "FLA": "底质+个体发生 premise", "PBF": "温血=热生理 typed fact（FR3 §7 admission 击穿点全不成立）",
    "GT": "夜间低光+礁沙岩结构（R03 教训不买 Night Mode）",
    "HAL": "深度+底质", "PAY": "獠牙鱼食形态推断（Confidence MEDIUM）",
    "SHO": "同属黑鲈同构推算（属内 2/4 先例，Confidence MEDIUM）",
    "DS": "同科笋壳鱼先例同构（Confidence MEDIUM）"}
for sid in TYPED_RESP:
    note = TYPED_NOTES.get(sid, "标准")
    M.append({"program_id": f"P-B3-{sid}-RESP",
              "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": (["PREMISE"]
                                   if BLIND[f"P-B3-{sid}-RESP"]["incoming_premises"]
                                   else []),
              "reasoning": f"engine 仅 PREMISE（F02 不计）或无差异。实例注记：{note}。",
              "provenance": {"batch": "CENSUS-B3"}})
# --- 4) 3 Response vs GUARD：MERGE_CONFIDENT（族扩容） ---
GUARD_NOTES = {
    "ARA": "沙巢+护卵护幼（Obligate air-gulp 换气暴露记 runtime premise，TAR-11）",
    "RBP": "树根卵团（群游=防御 Negative Knowledge 已在 S3 排除——FR3 判例②）",
    "WEL": "雄巢守护至幼虫孵出（听嗅主导+夜行=typed context premise）"}
for sid in GUARD_RESP:
    M.append({"program_id": f"P-B3-{sid}-RESP",
              "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": ["COMBINE", "OPERATOR", "PREMISE"],
              "proposed_parameter_axis":
                  "intruder_evaluator_context(typed: nest_anchor 新实例"
                  " sand_nest|tree_root_eggs|male_built_nest)",
              "reasoning": f"骨架同构：并行双 evaluator（deps 位形 [ [],[],[0,1],[2] ] 与 "
                           f"canonical 完全一致、branches 空、RETURN 同）→ combine → decide。"
                           f"engine raw 差异全为字面：intruder evaluator 槽名"
                           f"（EVAL_NEST_INTRUDER_RELATION vs EVAL_TARGET_AS_INTRUDER_TYPED，"
                           f"intruder_evaluator_context 轴内）与合并步标名"
                           f"（COMBINE_CONFLICT_AWARE vs COMBINE_DUAL_PATH——同一结构步命名）。"
                           f"第 5-7 成员：{GUARD_NOTES[sid]}。{AXIS}",
              "provenance": {"batch": "CENSUS-B3"}})
# --- 5) 2 fasting vs TYPED + vs GUARD：NEW_TEMPLATE_CANDIDATE（新族提案） ---
FASTING_NOTES = {"CHU": "『Adults cease feeding in freshwater』（判例①源例，L3 双源）",
                 "SHA": "『Feeding ceases during upstream spawning migration』（判例①跨科重复例）"}
for sid in FASTING:
    M.append({"program_id": f"P-B3-{sid}-RESP-FASTING",
              "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "RETURN"],
              "engine_raw_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "PREMISE", "RETURN"],
              "reasoning": "停食洄游双 Path（FR3 判例①）：状态 IF 门（migration_stage=="
                           "FASTING_RUN）互斥切换摄食 Path/非摄食攻击 Path——BRANCH（canonical "
                           "无门）+OPERATOR（4 步 vs 2 步）+DEPENDENCY+COMBINE+RETURN"
                           "（Response(TargetFeeding | NonFeedingStrike)）真结构差异，"
                           "非轴内。立 STATE_GATED_MULTI_PATH_RESPONSE 候选族（HRQ-B3-01）。",
              "human_review_queued": HRQ["state"],
              "provenance": {"batch": "CENSUS-B3"}})
    M.append({"program_id": f"P-B3-{sid}-RESP-FASTING",
              "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "RETURN"],
              "engine_raw_diffs": ["BRANCH", "COMBINE", "DEPENDENCY",
                                   "OPERATOR", "PREMISE", "RETURN"],
              "reasoning": "与 GUARD 族互证独立：GUARD=∥ 并行双 evaluator（无分支、同刻竞争"
                           "→COMBINE）；本程序=IF 状态门互斥（不同刻、状态抑制一条 Path）+"
                           "RETURN 语义不同（RelationalConflict vs NonFeedingStrike）。"
                           "两族 multi-path 拓扑不同（§9.2 同为 one-program-multi-path 但"
                           "结构元素不同）——双向互记 non-match。",
              "human_review_queued": HRQ["state"],
              "provenance": {"batch": "CENSUS-B3"}})

FAMILY_OF = {}
for sid in BAKES:
    FAMILY_OF[f"P-B3-{sid}-BAKE"] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT",
                                     HRQ["members"])
for sid in TYPED_RESP:
    FAMILY_OF[f"P-B3-{sid}-RESP"] = ("TYPED_TARGET_RESPONSE", HRQ["members"])
for sid in GUARD_RESP:
    FAMILY_OF[f"P-B3-{sid}-RESP"] = ("GUARD_CONFLICT_DUAL_PATH_RESPONSE",
                                     HRQ["guard"])
for sid in FASTING:
    FAMILY_OF[f"P-B3-{sid}-RESP-FASTING"] = ("STATE_GATED_MULTI_PATH_RESPONSE",
                                             HRQ["state"])


def main():
    # merge_tests
    (BATCH / "merge_tests.jsonl").write_text(
        "\n".join(json.dumps(m, ensure_ascii=False) for m in M) + "\n",
        encoding="utf-8")
    # programs
    out = []
    for p in BLIND.values():
        fam, ref = FAMILY_OF[p["program_id"]]
        out.append({"program_id": p["program_id"], "story_id": p["story_id"],
                    "species_id": p["species_id"], "surface": p["surface"],
                    "consequence": "NEW_PROGRAM_CANDIDATE",
                    "family_membership": fam, "review_ref": ref,
                    "blind_hash": p["blind_hash"],
                    "original_program_body_unchanged": True,
                    "registry_seen_at_creation": False,
                    "post_registry_mutations": [],
                    "provenance": {"batch": "CENSUS-B3"}})
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n",
        encoding="utf-8")
    # revisions / resolver / absence / coverage
    (BATCH / "program_revisions.jsonl").write_text("", encoding="utf-8")
    (BATCH / "resolver_tests.jsonl").write_text(json.dumps({
        "resolver_id": "NO_NEW_RESOLVER_FAMILY",
        "note": "B3 未新增 resolver family；洄游阶段/洪水触发/温血/气呼吸/听嗅/护巢 anchor "
                "均为世界侧 fact 或 premise 供给义务（上游 SNAP 登记同 B1/B2）；换气暴露 "
                "opportunity 语义压力记 TAR-11（与 HRQ-B2-01 opportunity lifecycle 同域）",
        "provenance": {"batch": "CENSUS-B3"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (BATCH / "absence_claims.jsonl").write_text("", encoding="utf-8")
    (BATCH / "coverage.jsonl").write_text("", encoding="utf-8")
    # HRQ
    hrq = [
        {"queue_id": HRQ["state"], "batch": "CENSUS-B3",
         "kind": "NEW_TEMPLATE_CANDIDATE", "surface": "Response",
         "template_id": "STATE_GATED_MULTI_PATH_RESPONSE",
         "canonical_summary":
             "EVAL_MIGRATION_FASTING_STATE -> IF(migration_stage==FASTING_RUN) "
             "{EVAL_STRIKE_NON_FEEDING | ELSE EVAL_TARGET_AS_FOOD_TYPED} -> "
             "DECIDE_MULTI_PATH_RESPONSE -> Response(TargetFeeding | NonFeedingStrike)",
         "members": [
             {"program_id": "P-B3-CHU-RESP-FASTING",
              "blind_hash": BLIND["P-B3-CHU-RESP-FASTING"]["blind_hash"],
              "role": "canonical_source",
              "note": FASTING_NOTES["CHU"]},
             {"program_id": "P-B3-SHA-RESP-FASTING",
              "blind_hash": BLIND["P-B3-SHA-RESP-FASTING"]["blind_hash"],
              "direct_test": "与 canonical 源 engine 无字面差异（同构骨架）",
              "note": FASTING_NOTES["SHA"]}],
         "proposed_parameter_axes": [
             "fasting_state_binding(typed: migration_stage premise)",
             "strike_path_semantics(动机归因 open——FR3 判例①升级三条件之①闭合前为最小骨架)"],
         "pending_review_questions": [
             "与 P05 判例①的两层登记：FR3 已裁『停食→P05 状态抑制 Feeding Path；非摄食可钓性→Response multi-path(§9.2)』——census 族独立性不自动 promote 任何 Grammar/Mode",
             "与 GUARD_CONFLICT_DUAL_PATH 的家族关系：同为 §9.2 one-program-multi-path 但拓扑不同（IF 状态门互斥 vs ∥ 同刻并行竞争）——已双向互记 non-match，是否维持两级并列待 review",
             "NonFeedingStrike Path 语义最小骨架的合法边界：动机归因（攻击/领地/护巢）未闭合前 strike evaluator 不得细化（升级三条件之①；TAR-10 同源）",
             "FR3 判例①升级三条件之③（产品需停食/摄食群互斥预分供给）若触发，本族与 FishGroup 层的边界重开"],
         "known_non_matches": [
             "TYPED_TARGET_RESPONSE（BRANCH+OPERATOR+COMBINE+RETURN 真差异——单路径 vs 状态门控双路径）",
             "GUARD_CONFLICT_DUAL_PATH_RESPONSE（IF 互斥 vs ∥ 并行；NonFeedingStrike vs RelationalConflict）"],
         "status": "CANDIDATE"},
        {"queue_id": HRQ["guard"], "batch": "CENSUS-B3",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Response",
         "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
         "question": "P04 护巢组 3 例（ARA 沙巢/RBP 树根卵/WEL 雄巢）判族：envelope 压力点"
                     "『GUARD_CONFLICT_DUAL_PATH 扩容 or PLAIN 族』——worker 裁定扩容（骨架"
                     "同构直验：并行双 evaluator→combine→decide，deps 位形与 canonical 一致）；"
                     "intruder_evaluator_context 轴新实例 sand_nest|tree_root_eggs|"
                     "male_built_nest（原 nest_anchor|fry_anchor 域扩展）",
         "pending_review_questions": [
             "anchor 类型轴扩展（卵/幼/巢三种 relation 对象）是否在原轴内（worker 倾向轴内：guard_state 单 premise 承载）",
             "FR3 P04 三问抽验（真 guard 状态/误拆双 supply/竞争留痕）已转 Cross-Batch——抽验结论若翻转则本 3 成员回归复检",
             "P04 语义层（Candidate，Design Authority Accepted）与 census 族两层登记维持"],
         "related": ["FR3 FISH-R06 判例（P04×3 抽验框架）", "HRQ-06(B0)"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["members"], "batch": "CENSUS-B3",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Bake+Response",
         "question": "SINGLE +26（41 名义成员：factor_type 新实例 position/layer/depth 阶段"
                     "绑定 15 + structure 静态 11）；TYPED +23（50 名义）；CRR +26 non-match"
                     "（累计 50 non-match 仍 0 成员——HRQ-B2-02 维持人类裁决）",
         "pending_review_questions": [
             "SINGLE 名义 41 成员的族完整性：本批 26 条全部 engine raw 仅 OPERATOR+PREMISE（骨架同构）——canonical 未变更，无需全族回归复检（F15）",
             "TYPED evaluator_binding 轴新实例：PBF 温血 typed fact / TAR 气呼吸 runtime 条件（binding 型 premise 第 4/5 例）"],
         "status": "PENDING_REVIEW"},
    ]
    (BATCH / "human_review_queue.jsonl").write_text(
        "\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n",
        encoding="utf-8")
    # registry v4 -> v5
    p = ROOT / "template_registry.yaml"
    t = io.open(p, encoding="utf-8").read()
    t = t.replace("""version: 4
mutation_provenance:
  batch: CENSUS-B2
  date: 2026-09-10
  previous_version: 3""", """version: 5
mutation_provenance:
  batch: CENSUS-B3
  date: 2026-09-11
  previous_version: 4
  b3_summary: "R06 洄游/掠食批 28 Story 54 程序：SINGLE +26（41，P05 阶段绑定 position 15+structure 11）；TYPED +23（50）；GUARD +3（7，intruder_evaluator_context 新实例）；CRR +26 non-match（累计 50 仍 0 成员）；新立 STATE_GATED_MULTI_PATH_RESPONSE（2，停食洄游双 Path——FR3 判例① §9.2 multi-path）——ΔL_bake=0 / ΔL_response=+1；HRQ-B3-01..03"

v4_provenance:
  batch: CENSUS-B2
  date: 2026-09-10
  previous_version: 3""")
    # CRR non-match 追加
    t = t.replace(
        """        reason: B2 thermal/季节/场类 10 程序全部非匹配（premise 绑定切换/因子组合形态）；CRR 真首考的结构性输入问题转 HRQ-B2-02（人类裁决）""",
        """        reason: B2 thermal/季节/场类 10 程序全部非匹配（premise 绑定切换/因子组合形态）；CRR 真首考的结构性输入问题转 HRQ-B2-02（人类裁决）
      - batch: CENSUS-B3
        program_id: [P-B3-CHU-BAKE, P-B3-CHN-BAKE, P-B3-COH-BAKE, P-B3-PIN-BAKE, P-B3-BRO-BAKE, P-B3-SHA-BAKE, P-B3-ALE-BAKE, P-B3-AST-BAKE, P-B3-SNS-BAKE, P-B3-TAR-BAKE, P-B3-TAI-BAKE, P-B3-ARA-BAKE, P-B3-PB-BAKE, P-B3-RBP-BAKE, P-B3-BLP-BAKE, P-B3-WEL-BAKE, P-B3-FLA-BAKE, P-B3-BUR-BAKE, P-B3-GW-BAKE, P-B3-SGA-BAKE, P-B3-RFP-BAKE, P-B3-DS-BAKE, P-B3-PBF-BAKE, P-B3-GT-BAKE, P-B3-HAL-BAKE, P-B3-GG-BAKE]
        reason: B3 洄游/掠食层 26 程序全部非匹配（premise 绑定切换/静态结构因子形态，无 RelativeRank）；CRR 仍 0 成员（HRQ-B2-02 维持）""")
    # SINGLE instances 追加
    t = t.replace(
        """      - {batch: CENSUS-B2, program_id: [P-B2-BHC-BAKE, P-B2-HER-BAKE], note: "factor_type 轴 +food_field（场实例第 2/3 个，继 LAM chemical_gradient）"}""",
        """      - {batch: CENSUS-B2, program_id: [P-B2-BHC-BAKE, P-B2-HER-BAKE], note: "factor_type 轴 +food_field（场实例第 2/3 个，继 LAM chemical_gradient）"}
      - {batch: CENSUS-B3, program_id: [P-B3-CHU-BAKE, P-B3-CHN-BAKE, P-B3-COH-BAKE, P-B3-PIN-BAKE, P-B3-BRO-BAKE, P-B3-SHA-BAKE, P-B3-ALE-BAKE, P-B3-AST-BAKE, P-B3-SNS-BAKE, P-B3-TAR-BAKE, P-B3-ARA-BAKE, P-B3-BUR-BAKE, P-B3-PBF-BAKE, P-B3-GT-BAKE, P-B3-HAL-BAKE], note: "factor_type=habitat_factor(position/layer/depth)：P05 阶段/周期/季节绑定 15 例（洄游系+洪水周期+季节重排）；factor_binding 轴批量实例"}
      - {batch: CENSUS-B3, program_id: [P-B3-TAI-BAKE, P-B3-PB-BAKE, P-B3-RBP-BAKE, P-B3-BLP-BAKE, P-B3-WEL-BAKE, P-B3-FLA-BAKE, P-B3-GW-BAKE, P-B3-SGA-BAKE, P-B3-RFP-BAKE, P-B3-DS-BAKE, P-B3-GG-BAKE], note: "factor_type=habitat_factor(structure)：静态结构 anchor 11 例（深潭/植被/急流/洞穴/倒木/逆流/洄湾/底栖/礁洞——B2 FGA 同型）"}""")
    # TYPED instances 追加
    t = t.replace(
        """      - {batch: CENSUS-B2, program_id: [P-B2-PIK19-RESP, P-B2-WAL-RESP, P-B2-BRT12-RESP, P-B2-ARC-RESP, P-B2-VEN-RESP, P-B2-FGA-RESP, P-B2-SWO-RESP, P-B2-MDF-RESP], note: "8 标准成员（MDF=motion-triggered 强实例：静止不触发/移动触发追捕）"}""",
        """      - {batch: CENSUS-B2, program_id: [P-B2-PIK19-RESP, P-B2-WAL-RESP, P-B2-BRT12-RESP, P-B2-ARC-RESP, P-B2-VEN-RESP, P-B2-FGA-RESP, P-B2-SWO-RESP, P-B2-MDF-RESP], note: "8 标准成员（MDF=motion-triggered 强实例：静止不触发/移动触发追捕）"}
      - {batch: CENSUS-B3, program_id: [P-B3-CHN-RESP, P-B3-COH-RESP, P-B3-PIN-RESP, P-B3-BRO-RESP, P-B3-ALE-RESP, P-B3-AST-RESP, P-B3-SNS-RESP, P-B3-TAR-RESP, P-B3-TAI-RESP, P-B3-PB-RESP, P-B3-BLP-RESP, P-B3-FLA-RESP, P-B3-BUR-RESP, P-B3-GW-RESP, P-B3-PAY-RESP, P-B3-SGA-RESP, P-B3-SHO-RESP, P-B3-RFP-RESP, P-B3-DS-RESP, P-B3-PBF-RESP, P-B3-GT-RESP, P-B3-HAL-RESP, P-B3-GG-RESP], note: "23 标准成员；强实例：TAR 水面取向+气呼吸 runtime premise / TAI+GW 陆生猎物水面呈现 / PBF 温血 typed fact（FR3 §7）/ AST 鲟科须探第 3 例 / GT 夜礁缘（不买 Night Mode——R03 教训）；PAY/SHO/DS 为形态/同属/同科推算（Confidence MEDIUM）"}""")
    # TYPED non-match 追加（双向互记：vs STATE_GATED）
    t = t.replace(
        """      - {batch: CENSUS-B2, template_id: FOOD_FIELD_FEEDING_RESPONSE, reason: "反向互记（B2-FIX-001 F-1）：evaluand=食物场+RETURN=FieldFeeding（真结构差异立新族）"}""",
        """      - {batch: CENSUS-B2, template_id: FOOD_FIELD_FEEDING_RESPONSE, reason: "反向互记（B2-FIX-001 F-1）：evaluand=食物场+RETURN=FieldFeeding（真结构差异立新族）"}
      - {batch: CENSUS-B3, template_id: STATE_GATED_MULTI_PATH_RESPONSE, reason: "反向互记：BRANCH（状态 IF 门）+COMBINE+RETURN（TargetFeeding|NonFeedingStrike）真差异——停食洄游双 Path（FR3 判例①）"}""")
    # GUARD instances 追加
    t = t.replace(
        """      - {batch: CENSUS-B1, program_id: P-B1-DIS-RESP-GUARD, blind_hash: 585905b944bd66d6, note: "第 4 成员（七彩神仙育幼黏液喂养）：engine 无字面差异；fry_anchor=幼鱼群；色型不分裂（S12 对照不建体）"}""",
        """      - {batch: CENSUS-B1, program_id: P-B1-DIS-RESP-GUARD, blind_hash: 585905b944bd66d6, note: "第 4 成员（七彩神仙育幼黏液喂养）：engine 无字面差异；fry_anchor=幼鱼群；色型不分裂（S12 对照不建体）"}
      - {batch: CENSUS-B3, program_id: P-B3-ARA-RESP, blind_hash: 5f3f40e142fffa81, note: "第 5 成员（巨骨舌鱼洪水护巢）：anchor=沙巢+护卵护幼；换气暴露 runtime premise（TAR-11）；engine raw 仅槽名/合并步标名字面差异"}
      - {batch: CENSUS-B3, program_id: P-B3-RBP-RESP, blind_hash: cf001f79596b2729, note: "第 6 成员（红腹食人鱼树根护卵）：anchor=tree_root_eggs；群游=防御 Negative Knowledge（FR3 判例②）已排除 Group"}
      - {batch: CENSUS-B3, program_id: P-B3-WEL-RESP, blind_hash: 2b938a5ca14665e4, note: "第 7 成员（欧洲巨鲶雄巢守护）：anchor=male_built_nest；听嗅主导+夜行 typed context premise"}""")
    # GUARD non-match 追加（vs STATE_GATED）
    t = t.replace(
        """    known_non_matches:
      - {batch: CENSUS-B0, template_id: TYPED_TARGET_RESPONSE, reason: 单路径 vs 双路径并行+combine}""",
        """    known_non_matches:
      - {batch: CENSUS-B0, template_id: TYPED_TARGET_RESPONSE, reason: 单路径 vs 双路径并行+combine}
      - {batch: CENSUS-B3, template_id: STATE_GATED_MULTI_PATH_RESPONSE, reason: "反向互记：∥ 同刻并行竞争 vs IF 状态门互斥；RelationalConflict vs NonFeedingStrike——同为 §9.2 multi-path 但拓扑不同"}""")
    # 尾部新族
    t = t.rstrip() + """
  - template_id: STATE_GATED_MULTI_PATH_RESPONSE
    surface: Response
    status: CANDIDATE
    provenance:
      batch: CENSUS-B3
      seeded: 2026-09-11
      review_queue: HRQ-B3-01
      semantic_pattern_correspondence: P05（FR3 FISH-R06 判例①：停食→状态抑制 Feeding Path；非摄食可钓性→Response multi-path §9.2；P01 摄食 Path 内嵌——两层登记待 review）
    canonical_program_body: |
      EVAL_MIGRATION_FASTING_STATE
      -> IF (migration_stage==FASTING_RUN) { EVAL_STRIKE_NON_FEEDING } ELSE { EVAL_TARGET_AS_FOOD_TYPED }
      -> DECIDE_MULTI_PATH_RESPONSE
      -> Response(TargetFeeding | NonFeedingStrike)
    ir_pointer: batches/CENSUS-B3/build_blind_programs.py::P-B3-CHU-RESP-FASTING
    allowed_parameter_axes:
      - fasting_state_binding(typed: migration_stage premise)
      - strike_path_semantics(动机归因 open——FR3 判例①升级三条件之①闭合前为最小骨架)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 同刻并行双 evaluand（那是 GUARD 族域——本族为状态门互斥）, 场 evaluand]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-B3, program_id: P-B3-CHU-RESP-FASTING, blind_hash: 59501cd2ba4234f3, role: canonical_source}
      - {batch: CENSUS-B3, program_id: P-B3-SHA-RESP-FASTING, blind_hash: 04e9019822c483c5, note: "判例①跨科重复例（『Feeding ceases during upstream spawning migration』）"}
    known_non_matches:
      - {batch: CENSUS-B3, template_id: TYPED_TARGET_RESPONSE, reason: "BRANCH+OPERATOR+COMBINE+RETURN 真差异（状态门控双路径 vs 单路径）"}
      - {batch: CENSUS-B3, template_id: GUARD_CONFLICT_DUAL_PATH_RESPONSE, reason: "IF 状态门互斥 vs ∥ 同刻并行；NonFeedingStrike vs RelationalConflict"}
    open_precedents: [HRQ-B3-01（strike 动机归因引文=升级三条件之①；TAR-10 同源；条件③触发时与 FishGroup 边界重开）]
    provisional_note: 双成员（跨科独立重复——FR3 判例①）；strike Path 语义为最小骨架（动机归因 open）
"""
    io.open(p, "w", encoding="utf-8").write(t)
    import yaml
    reg = yaml.safe_load(io.open(p, encoding="utf-8"))
    assert reg["version"] == 5 and len(reg["templates"]) == 10, (
        reg["version"], len(reg["templates"]))
    counts = {x["template_id"]: len(x["known_instances"]) for x in reg["templates"]}
    print("registry v5:", counts)
    # discovery curve
    c = ROOT / "discovery_curve.csv"
    t = io.open(c, encoding="utf-8").read().rstrip() + \
        "\nCENSUS-B3,28,54,52,0,1,0,0,0,1,0,0,0,0\n"
    io.open(c, "w", encoding="utf-8").write(t)
    n_mc = sum(1 for m in M if m["verdict"] == "MERGE_CONFIDENT")
    print(f"merge_tests={len(M)} (MERGE_CONFIDENT={n_mc}) programs={len(out)}")


if __name__ == "__main__":
    main()
