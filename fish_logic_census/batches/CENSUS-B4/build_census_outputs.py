# -*- coding: utf-8 -*-
"""CENSUS-B4 判同产物 + registry v5→v6 + discovery_curve（一体化脚本）。
语义裁决依据：engine_report.json（raw）+ worker reasoning；B0-B3 判例链。
含 B3-F-2/F-3 修正落 registry。"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"guard_ext": "HRQ-B4-01", "members": "HRQ-B4-02", "hygiene": "HRQ-B4-03"}
AXIS = "轴属扩容提案（HRQ 待批）；engine raw diff 为槽名/合并步标名字面差异，骨架同构"

BAKES = ["POR", "SDG", "TSK", "ASR", "RVS", "GPF", "RKB", "SSL", "BSK",
         "RRH", "GRH", "SMB", "GDE", "WIT", "WIN", "YTF", "SMF", "BST",
         "FDR", "BSB", "CBM", "SAI", "HNC", "MOO", "RDS"]
POSITION_BAKES = ["POR", "SDG", "ASR", "GPF", "RKB", "SSL", "GDE", "CBM", "SAI",
                  "BSK", "RRH", "GRH", "BST", "MOO"]   # premise 绑定切换（洄游/季节/潮汐/盐度/阶段）
STRUCTURE_BAKES = ["TSK", "RVS", "SMB", "WIT", "WIN", "YTF", "SMF", "FDR",
                   "BSB", "HNC", "RDS"]                # 静态结构/因子绑定
TYPED_RESP = ["POR", "SDG", "TSK", "ASR", "RVS", "GPF", "RKB", "SSL", "BSK",
              "RRH", "GRH", "SMB", "GDE", "WIT", "WIN", "YTF", "SMF", "BST",
              "FDR", "BSB", "CBM", "SAI", "MOO", "RDS"]
GUARD_RESP = ["HNC"]

BLIND = {p["program_id"]: p for p in (
    json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(
        encoding="utf-8").splitlines() if l.strip())}
ENGINE = json.loads((BATCH / "engine_report.json").read_text(encoding="utf-8"))
RAW_CRR = {r["program_id"]: r["structural_diffs"] for r in ENGINE["vs_CRR"]}
RAW_FAM = {(r["program_id"], r["family"]): r["engine_structural_diff"]
           for r in ENGINE["family"]}
RAW_F2 = {r["program_id"]: r for r in ENGINE["b3_f2_state_gated_materialization"]}

M = []
# --- 1) 25 Bake vs CRR：non-match（CRR 累计 50→75） ---
for sid in BAKES:
    pid = f"P-B4-{sid}-BAKE"
    M.append({"program_id": pid,
              "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False,
              "param_only": False,
              "structural_diffs": sorted(set(RAW_CRR[pid]) - {"PREMISE"}),
              "engine_raw_diffs": RAW_CRR[pid],
              "reasoning": "CRR 判别结构（BUILD→GATE→RelativeRank(reference_set="
                           "FeasibleSet)→secondary→FIXED）不存在：边界层为 premise 绑定切换"
                           "（洄游/季节/潮汐/盐度）与静态结构/因子绑定形态。归 SINGLE 候选族。"
                           "CRR 连续第 4 批零成员（B0-B4 累计 75 non-match；HRQ-B2-02 输入"
                           "通道问题维持人类裁决）。",
              "human_review_queued": HRQ["members"],
              "provenance": {"batch": "CENSUS-B4"}})
# --- 2) 25 Bake vs SINGLE：MERGE_CONFIDENT（骨架同构，槽名字面在 factor_type 轴内） ---
POSITION_NOTE = {
    "POR": "产仔洄游阶段绑定（2000km 南下；鲑系 P05 判例④同型）",
    "SDG": "高洄游+温度相关移动（双 premise）",
    "ASR": "咸淡水广适 runtime overlay+河口上溯（SGA 气呼吸 runtime 同型）",
    "GPF": "潮汐窗周期绑定（高潮上岸产卵→返水；洪水周期 P05 同型）",
    "RKB": "幼鱼流藻阶段绑定", "SSL": "幼浮游-底栖阶段绑定",
    "GDE": "春上溯/秋下行季节绑定", "CBM": "冬深水不活跃季节重排",
    "SAI": "春岸/冬深+南北洄游季节绑定",
    "BSK": "potamodromous 绑定", "RRH": "potamodromous 绑定",
    "GRH": "potamodromous 绑定", "BST": "potamodromous 绑定",
    "MOO": "potamodromous 绑定"}
STRUCT_NOTE = {
    "TSK": "深冷泥底 25-440m/-1~14°C", "RVS": "纯淡水河底 pH 绑定",
    "SMB": "河湾潭果", "WIT": "深冷泥底 45-366m/2-6°C（HAL 不同深度带）",
    "WIN": "近岸泥-中硬底", "YTF": "中深沙泥 37-82m/3-5°C",
    "SMF": "硬沙底掘穴（底质偏好绑定）", "FDR": "河湖底层",
    "BSB": "湾内岩礁咸淡水", "HNC": "岩池清水", "RDS": "温水静水植被"}
for sid in POSITION_BAKES:
    pid = f"P-B4-{sid}-BAKE"
    M.append({"program_id": pid, "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": RAW_FAM[(pid, "SINGLE_FACTOR_NORMALIZED_WEIGHT")],
              "proposed_parameter_axis":
                  "factor_type(typed: habitat_factor(position/binding))"
                  "+factor_binding(随 lifecycle/season/tide/salinity premise 切换)",
              "reasoning": f"骨架同构（单 typed 因子→归一化）；槽名字面在 factor_type 轴内"
                           f"（HRQ-B1-01 声明域）。实例={sid}：{POSITION_NOTE[sid]}。"
                           f"顺序推导注记：正文时序均为 premise 配置级（判例④），无面内判断链。{AXIS}",
              "provenance": {"batch": "CENSUS-B4"}})
for sid in STRUCTURE_BAKES:
    pid = f"P-B4-{sid}-BAKE"
    M.append({"program_id": pid, "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": RAW_FAM[(pid, "SINGLE_FACTOR_NORMALIZED_WEIGHT")],
              "proposed_parameter_axis": "factor_type(typed: habitat_factor(structure/substrate/depth))",
              "reasoning": f"骨架同构；静态结构/底质/深度因子——B3 structure 11 例同型"
                           f"第 12-22 例。实例={sid}：{STRUCT_NOTE[sid]}。{AXIS}",
              "provenance": {"batch": "CENSUS-B4"}})
# --- 3) 24 Response vs TYPED：MERGE_CONFIDENT ---
TYPED_NOTES = {
    "POR": "温血=热生理 typed fact（PBF 同型第 2 例；Story 明言不买 Mode）",
    "SDG": "evaluator_channel=PASSIVE_ELECTROSENSE 第 2 例（B1 PAD34 后；FR3 判例①感知端并入 K8）",
    "TSK": "evaluator_channel=PASSIVE_ELECTROSENSE 第 3 例+自发电场；食腐=食物类型；体型食性=premise",
    "ASR": "底栖无脊椎标准", "RVS": "P01 冻结主张承载（食性 EO，Confidence MEDIUM）",
    "GPF": "齿板形态事实承载（S1 磯食 EO，MEDIUM——PAY 推断同型）",
    "RKB": "喙齿形态事实承载（S1/S2 EO，MEDIUM）",
    "SSL": "多毛/小甲壳标准（潜沙=反捕食 runtime 排除）",
    "BSK": "吸口形态事实承载（S1 EO，MEDIUM）",
    "RRH": "双壳贝专食（磿贝机制 EO）", "GRH": "昆虫幼生（Moxostoma 属内对照）",
    "SMB": "咽喉骨板磿碎机制 typed 事实（草鱼 R02 先例不买 Mode）",
    "GDE": "夜行低光 typed context（R03 先例）+水面/落水猎物（欧鲢 R05 同构）",
    "WIT": "深冷泥底标准", "WIN": "日间×底栖复合 typed context（GDE 夜行对偶；表述顺序非程序门）",
    "YTF": "多毛主食", "SMF": "掘穴栖息事实推断伏击（S1 EO，MEDIUM；WEL/SGA 伏击 context 先例）",
    "BST": "底栖无脊椎标准（颏须 typed context 候选引文开放）",
    "FDR": "广食含同类幼鱼（premise）；产声=声学观察排除",
    "BSB": "贝/多毛标准（性转换 lifecycle premise EO）",
    "CBM": "夜捕 typed context（同属大西洋鲭 R02 无 filter 记录对照）",
    "SAI": "体型分级食性 ontogeny premise（TAI 同型）",
    "MOO": "P01 冻结主张承载（食性 EO，MEDIUM）",
    "RDS": "贝食偏好 FishBase 原文（磿螺机制 EO）"}
for sid in TYPED_RESP:
    pid = f"P-B4-{sid}-RESP"
    M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")],
              "reasoning": f"engine 仅 PREMISE（F02 不计）或无差异。实例注记：{TYPED_NOTES[sid]}。",
              "provenance": {"batch": "CENSUS-B4"}})
# --- 4) HNC vs GUARD：TEMPLATE_EXTENSION_CANDIDATE（guard_target_specificity 新轴提案） ---
pid = "P-B4-HNC-RESP"
M.append({"program_id": pid, "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
          "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False,
          "param_only": True, "structural_diffs": [],
          "engine_raw_diffs": RAW_FAM[(pid, "GUARD_CONFLICT_DUAL_PATH_RESPONSE")],
          "extension_complexity_cost":
              "+1 有限 typed 参数轴 guard_target_specificity(species_typed_intruder | "
              "any_intruder) 挂在既有 intruder evaluator 槽上；canonical body 零改动"
              "（deps 位形 [ [],[],[0,1],[2] ]/branches 空/RETURN 同）；anchor 轴第 6 值 "
              "pebble_mound（B3 扩容同型轴值）",
          "new_template_complexity_cost":
              "为单一 evaluator 谓词 typing 复制整条 ∥ 并行双路径拓扑为独立族——家族数翻倍"
              "且与 GUARD 7 成员全部结构同构（仅谓词 typed 不同），违反 F10/F14 节俭",
          "recommended_shape":
              "扩展 GUARD：HNC 入族为第 8 成员（anchor=pebble_mound；"
              "guard_target_specificity=species_typed_intruder 新轴提案）——HRQ-B4-01 待批；"
              "批前按 extension 候选挂账",
          "proposed_parameter_axis":
              "guard_target_specificity(typed: species_typed_intruder | any_intruder——NEW 轴"
              "提案) + intruder_evaluator_context 第 6 值 pebble_mound（既有轴值扩展）",
          "reasoning": "骨架同构：并行双 evaluator（deps 位形与 canonical 完全一致、branches 空、"
                       "RETURN 同）→ combine → decide；engine raw 差异全为字面（intruder 槽名"
                       "EVAL_NEST_INTRUDER_RELATION vs EVAL_TARGET_AS_INTRUDER_TYPED；合并步标名"
                       "COMBINE_CONFLICT_AWARE vs COMBINE_DUAL_PATH——B3 判同经验同型）。"
                       "超出 B3 成员的实质新内容=物种型 intruder 谓词：『defend the nest mounds "
                       "from other N. biguttatus males but not other species』逐字——防御触发"
                       "按目标物种分型（同种雄性竞争者触发，异种借巢者被容忍且借巢产卵发生）。"
                       "谓词 typing 非新增 branch/gate（拓扑不变）→ 有限 typed 新参数轴 → "
                       "TEMPLATE_EXTENSION_CANDIDATE（F14 非 plain merge）；Story 自记『P04 内部"
                       "结构变量 guard target specificity』Open Question，轴属裁决进 HRQ-B4-01。",
          "human_review_queued": HRQ["guard_ext"],
          "provenance": {"batch": "CENSUS-B4"}})
M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
          "structural_diffs": sorted(set(RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")]) - {"PREMISE"}),
          "engine_raw_diffs": RAW_FAM[(pid, "TYPED_TARGET_RESPONSE")],
          "reasoning": "互证独立：单路径 vs ∥ 并行双 evaluator+combine+双值 RETURN"
                       "（TargetFeeding | RelationalConflict）——GUARD 族域判据维持"
                       "（B0 OSC 先例同型 non-match）。",
          "human_review_queued": HRQ["guard_ext"],
          "provenance": {"batch": "CENSUS-B4"}})
M.append({"program_id": pid, "template_id": "STATE_GATED_MULTI_PATH_RESPONSE",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
          "structural_diffs": sorted(set(RAW_FAM[(pid, "STATE_GATED_MULTI_PATH_RESPONSE")]) - {"PREMISE"}),
          "engine_raw_diffs": RAW_FAM[(pid, "STATE_GATED_MULTI_PATH_RESPONSE")],
          "reasoning": "§9.2 两拓扑边界第 4 例互证：HNC=∥ 同刻并行竞争（无分支）vs "
                       "STATE_GATED=IF 状态门互斥（有分支）；RelationalConflict vs "
                       "NonFeedingStrike——双向 non-match 维持（B3 判例§9.2）。",
          "human_review_queued": HRQ["guard_ext"],
          "provenance": {"batch": "CENSUS-B4"}})
# --- 5) B3-F-2 修正验证：物化自测 + SHA 成员回归复检 ---
for b3pid, role, note in [
    ("P-B3-CHU-RESP-FASTING", "canonical_source_selftest",
     "B3-F-2 物化忠实性：canonical IR 逐字转写自本盲程序（body 零差异，PREMISE 信息性除外）"),
    ("P-B3-SHA-RESP-FASTING", "member_regression_recheck",
     "B3-F-2 族完整性回归复检（F15）：SHA 对物化 canonical 直验 body 零差异——成员资格维持")]:
    M.append({"program_id": b3pid,
              "template_id": "STATE_GATED_MULTI_PATH_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [],
              "engine_raw_diffs": RAW_F2[b3pid]["engine_structural_diff"],
              "reasoning": note + "（canonical 源自测计入 n_merge_confident——B1 教训）。",
              "provenance": {"batch": "CENSUS-B4", "fix": "B3-F-2"}})

FAMILY_OF = {}
for sid in BAKES:
    FAMILY_OF[f"P-B4-{sid}-BAKE"] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT", HRQ["members"])
for sid in TYPED_RESP:
    FAMILY_OF[f"P-B4-{sid}-RESP"] = ("TYPED_TARGET_RESPONSE", HRQ["members"])
FAMILY_OF["P-B4-HNC-RESP"] = ("GUARD_CONFLICT_DUAL_PATH_RESPONSE", HRQ["guard_ext"])


def main():
    # merge_tests
    (BATCH / "merge_tests.jsonl").write_text(
        "\n".join(json.dumps(m, ensure_ascii=False) for m in M) + "\n",
        encoding="utf-8")
    # programs
    out = []
    for p in BLIND.values():
        fam, ref = FAMILY_OF[p["program_id"]]
        rec = {"program_id": p["program_id"], "story_id": p["story_id"],
               "species_id": p["species_id"], "surface": p["surface"],
               "consequence": "NEW_PROGRAM_CANDIDATE",
               "family_membership": fam, "review_ref": ref,
               "blind_hash": p["blind_hash"],
               "original_program_body_unchanged": True,
               "registry_seen_at_creation": False,
               "post_registry_mutations": [],
               "provenance": {"batch": "CENSUS-B4"}}
        if p.get("confidence"):
            rec["confidence"] = p["confidence"]
        out.append(rec)
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n",
        encoding="utf-8")
    # revisions / resolver / coverage
    (BATCH / "program_revisions.jsonl").write_text("", encoding="utf-8")
    (BATCH / "resolver_tests.jsonl").write_text(json.dumps({
        "resolver_id": "NO_NEW_RESOLVER_FAMILY",
        "note": "B4 未新增 resolver family；电感知（K8 轴 FR 线）/潮汐窗/季节移动/盐度广适/"
                "温血/夜行/日间/产声观察/物种型 guard 谓词均为世界侧 fact、premise 供给义务"
                "或 evaluator typed context（上游 SNAP 登记同 B1-B3）",
        "provenance": {"batch": "CENSUS-B4"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (BATCH / "coverage.jsonl").write_text("", encoding="utf-8")
    # absence claims：LOCAL_SATURATION_CANDIDATE（第 3 个连续 ΔL_bake=0 批——candidate 不宣称 proven）
    (BATCH / "absence_claims.jsonl").write_text(json.dumps({
        "story_id": "CENSUS-B4-AGGREGATE",
        "claim": "LOCAL_SATURATION_CANDIDATE",
        "scope": "Bake 族宽度层：B2（thermal/季节 10）+B3（洄游/掠食 26）+B4（边界层 25）"
                 "连续 3 批 ΔL_bake=0（66 程序全 SINGLE 吸收）；B4 同时 ΔL_response=0"
                 "（边界层 24 typed 吸收+1 extension 候选）",
        "evidence_basis": "累计 75 CRR non-match（0 成员）；无超出已识别族独有结构的样本；"
                          "B4 顺序扫描（authoring_work_standards §5.1）确认边界层无面内"
                          "判断链样本",
        "does_not_claim": "非 NO_NEW_PROGRAM_PROVEN；SINGLE 41+B4 25 成员的顺序还原复检"
                          "（B0-B2 旧成员重跑）仍待独立 envelope；HRQ-B2-02（CRR 输入通道）"
                          "未决",
        "provenance": {"batch": "CENSUS-B4"}}, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # HRQ
    hrq = [
        {"queue_id": HRQ["guard_ext"], "batch": "CENSUS-B4",
         "kind": "TEMPLATE_EXTENSION_CANDIDATE", "surface": "Response",
         "template_id": "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
         "question": "HNC 双点美鱥（P04 石巢）入 GUARD 族：骨架同构直验（∥ 双 evaluator→"
                     "combine→decide；deps 位形/branches/RETURN 与 canonical 一致；engine raw "
                     "仅槽名/合并步标名字面）——但 intruder evaluator 携带物种型谓词"
                     "（『defend…from other N. biguttatus males but not other species』逐字："
                     "同种雄性触发防御，异种借巢者被容忍且借巢产卵+杂交发生）。",
         "proposed_axes": [
             "guard_target_specificity(typed: species_typed_intruder | any_intruder)——NEW 轴"
             "提案（B0-B3 成员默认 any_intruder 未显式分型）",
             "intruder_evaluator_context 第 6 值 pebble_mound（雄建石巢丘+产后覆砾——WEL "
             "male_built_nest 邻近但建造材质/覆砾行为不同，按轴值非新轴）"],
         "complexity_comparison": {
             "extension": "+1 有限 typed 轴挂既有 evaluator 槽；canonical 零改动；"
                          "不触发全族回归复检（F15）",
             "new_template": "复制整条 ∥ 双路径拓扑独立成族——与 7 成员结构同构仅谓词 typed "
                             "不同，违反节俭（F10/F14）",
             "recommended": "extension（worker 裁定；HRQ 批准后 anchor 轴值+新轴正式入声明）"},
         "pending_review_questions": [
             "物种型谓词是否可能进一步结构化（如 IF 物种门→防御/容忍两分支）——当前证据"
             "（Story Open Question+『not other species』单句）只支撑 evaluator 谓词 typing，"
             "不支撑面内 branch；若 FR 线后续给出借巢者容忍的行为序列证据则重开",
             "异种借巢产卵（nest associates）在产品供给中的语义（Story Open Question）——"
             "不影响 ResponseOwner 判定（FR 冻结），供给语义归 Representation 线",
             "FR3 P04 三问抽验（Cross-Batch 挂账）对本新成员同样适用——抽验结论翻转则回归复检",
             "P04 语义层与 census 族两层登记维持（P04=Candidate/Design Authority Accepted；"
             "census 扩容不自动 promote）"],
         "related": ["HRQ-06(B0)", "HRQ-B3-02（anchor 轴扩容先例）", "FR3 FISH-R07 判例（P04×HNC）"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["members"], "batch": "CENSUS-B4",
         "kind": "FAMILY_MEMBER_EXPANSION", "surface": "Bake+Response",
         "question": "SINGLE +25（66 名义：premise 绑定切换 14[洄游/季节/潮汐/盐度/阶段]"
                     "+静态结构 11）；TYPED +24（74 名义）；CRR +25 non-match（累计 75 仍 0 "
                     "成员——HRQ-B2-02 维持）；GUARD +1 extension 候选（HRQ-B4-01）；"
                     "ΔL 全零（group/bake/response/quality）",
         "pending_review_questions": [
             "顺序推导纪律执行确认（authoring_work_standards §5.1/用户反馈）：26 Story 逐条"
             "顺序扫描，无一面内 early-return 判断链；时序均为 premise 配置级（判例④）——"
             "B4 新成员 SINGLE 吸收为顺序诚实；SINGLE 41 旧成员复检风险（平铺化）属 B0-B2 "
             "重跑 envelope，本批不执行（manifest order_discipline 已记）",
             "TYPED 6 例 MEDIUM 推算成员的证据基础分层（RVS/MOO=P01 冻结主张承载；GPF/RKB="
             "齿板/喙齿形态事实；BSK=吸口形态事实；SMF=掘穴栖息事实+游钓事实）——是否全部"
             "入族 or 部分降 EO 待 FR 线引文（S1 EO 面）",
             "evaluator_channel=PASSIVE_ELECTROSENSE 第 2/3 例（SDG/TSK，B1 PAD34 后）——"
             "FR3 判例①并入 K8 的两层登记维持；电感知不改变机会生成结构（判例①证伪条款）",
             "LOCAL_SATURATION_CANDIDATE 首次立案（absence_claims.jsonl）：连续 3 批 "
             "ΔL_bake=0+本批 ΔL_response=0——candidate 非宣称，成立性归 review"],
         "status": "PENDING_REVIEW"},
        {"queue_id": HRQ["hygiene"], "batch": "CENSUS-B4",
         "kind": "REGISTRY_HYGIENE_FIX", "surface": "n/a",
         "question": "B3 审后两项修正的执行记录（envelope CENSUS-B4 指令）：F-2 STATE_GATED "
                     "canonical 物化进 run_merge_tests（IR 逐字转写自 P-B3-CHU-RESP-FASTING；"
                     "canonical 源自测+SHA 成员回归复检双 PASS——body 零差异）；F-3 GUARD "
                     "anchor 轴声明漂移修正（声明域 2 值→6 值对齐 known_instances：nest_anchor"
                     "|fry_anchor|foam_nest|sand_nest|tree_root_eggs|male_built_nest；B3 三值"
                     "标注 pending HRQ-B3-02；B4 pebble_mound 标注 HRQ-B4-01 提案）",
         "pending_review_questions": [
             "F-2 物化的 canonical 与 B3 盲程序 body 一致性（自测留痕 merge_tests 末 2 条）",
             "F-3 修正后轴声明含 pending 值是否合规（worker 倾向：声明对齐实例并标注审批态，"
             "优于声明与实例漂移）"],
         "status": "PENDING_REVIEW"},
    ]
    (BATCH / "human_review_queue.jsonl").write_text(
        "\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n",
        encoding="utf-8")
    # registry v5 -> v6
    p = ROOT / "template_registry.yaml"
    t = io.open(p, encoding="utf-8").read()
    t = t.replace("""version: 5
mutation_provenance:
  batch: CENSUS-B3
  date: 2026-09-11
  previous_version: 4""", """version: 6
mutation_provenance:
  batch: CENSUS-B4
  date: 2026-09-11
  previous_version: 5
  b4_summary: "R07 边界层批 26 Story 50 程序：SINGLE +25（66，premise 绑定切换 14+静态结构 11）；TYPED +24（74，PASSIVE_ELECTROSENSE 第 2/3 例+温血第 2 例）；GUARD +1 extension 候选（8 名义，guard_target_specificity 新轴提案 HRQ-B4-01）；CRR +25 non-match（累计 75 仍 0 成员）——ΔL 全零+LOCAL_SATURATION_CANDIDATE 首立案；B3-F-2（STATE_GATED canonical 物化）+B3-F-3（GUARD 轴声明对齐）修正落库；HRQ-B4-01..03"

v5_provenance:
  batch: CENSUS-B3
  date: 2026-09-11
  previous_version: 4""")
    # CRR non-match 追加
    t = t.replace(
        """        reason: B3 洄游/掠食层 26 程序全部非匹配（premise 绑定切换/静态结构因子形态，无 RelativeRank）；CRR 仍 0 成员（HRQ-B2-02 维持）""",
        """        reason: B3 洄游/掠食层 26 程序全部非匹配（premise 绑定切换/静态结构因子形态，无 RelativeRank）；CRR 仍 0 成员（HRQ-B2-02 维持）
      - batch: CENSUS-B4
        program_id: [P-B4-POR-BAKE, P-B4-SDG-BAKE, P-B4-TSK-BAKE, P-B4-ASR-BAKE, P-B4-RVS-BAKE, P-B4-GPF-BAKE, P-B4-RKB-BAKE, P-B4-SSL-BAKE, P-B4-BSK-BAKE, P-B4-RRH-BAKE, P-B4-GRH-BAKE, P-B4-SMB-BAKE, P-B4-GDE-BAKE, P-B4-WIT-BAKE, P-B4-WIN-BAKE, P-B4-YTF-BAKE, P-B4-SMF-BAKE, P-B4-BST-BAKE, P-B4-FDR-BAKE, P-B4-BSB-BAKE, P-B4-CBM-BAKE, P-B4-SAI-BAKE, P-B4-HNC-BAKE, P-B4-MOO-BAKE, P-B4-RDS-BAKE]
        reason: B4 边界层 25 程序全部非匹配（premise 绑定切换[洄游/季节/潮汐/盐度/阶段]与静态结构/因子绑定形态，无 RelativeRank）；CRR 连续第 4 批 0 成员（HRQ-B2-02 维持）""")
    # SINGLE instances 追加
    t = t.replace(
        """      - {batch: CENSUS-B3, program_id: [P-B3-TAI-BAKE, P-B3-PB-BAKE, P-B3-RBP-BAKE, P-B3-BLP-BAKE, P-B3-WEL-BAKE, P-B3-FLA-BAKE, P-B3-GW-BAKE, P-B3-SGA-BAKE, P-B3-RFP-BAKE, P-B3-DS-BAKE, P-B3-GG-BAKE], note: "factor_type=habitat_factor(structure)：静态结构 anchor 11 例（深潭/植被/急流/洞穴/倒木/逆流/洄湾/底栖/礁洞——B2 FGA 同型）"}""",
        """      - {batch: CENSUS-B3, program_id: [P-B3-TAI-BAKE, P-B3-PB-BAKE, P-B3-RBP-BAKE, P-B3-BLP-BAKE, P-B3-WEL-BAKE, P-B3-FLA-BAKE, P-B3-GW-BAKE, P-B3-SGA-BAKE, P-B3-RFP-BAKE, P-B3-DS-BAKE, P-B3-GG-BAKE], note: "factor_type=habitat_factor(structure)：静态结构 anchor 11 例（深潭/植被/急流/洞穴/倒木/逆流/洄湾/底栖/礁洞——B2 FGA 同型）"}
      - {batch: CENSUS-B4, program_id: [P-B4-POR-BAKE, P-B4-SDG-BAKE, P-B4-ASR-BAKE, P-B4-GPF-BAKE, P-B4-RKB-BAKE, P-B4-SSL-BAKE, P-B4-GDE-BAKE, P-B4-CBM-BAKE, P-B4-SAI-BAKE, P-B4-BSK-BAKE, P-B4-RRH-BAKE, P-B4-GRH-BAKE, P-B4-BST-BAKE, P-B4-MOO-BAKE], note: "factor_type=habitat_factor(position/binding)：premise 绑定切换 14 例（产仔洄游[POR]/高洄游+温度[SDG]/咸淡水 runtime 上溯[ASR]/潮汐窗周期[GPF——洪水周期同型]/幼流藻[RKB]/幼浮游[SSL]/季节洄游[GDE]/冬深水[CBM]/春岸冬深[SAI]/potamodromous×5）；顺序推导纪律执行（§5.1）——无面内判断链"}
      - {batch: CENSUS-B4, program_id: [P-B4-TSK-BAKE, P-B4-RVS-BAKE, P-B4-SMB-BAKE, P-B4-WIT-BAKE, P-B4-WIN-BAKE, P-B4-YTF-BAKE, P-B4-SMF-BAKE, P-B4-FDR-BAKE, P-B4-BSB-BAKE, P-B4-HNC-BAKE, P-B4-RDS-BAKE], note: "factor_type=habitat_factor(structure/substrate/depth)：静态结构/底质/深度 11 例（深冷泥底×2/河底/河湾/近岸/中深/掘穴底质/河湖底/湾礁/岩池/温水植被——B3 structure 同型第 12-22 例）"}""")
    # TYPED instances 追加
    t = t.replace(
        """      - {batch: CENSUS-B3, program_id: [P-B3-CHN-RESP, P-B3-COH-RESP, P-B3-PIN-RESP, P-B3-BRO-RESP, P-B3-ALE-RESP, P-B3-AST-RESP, P-B3-SNS-RESP, P-B3-TAR-RESP, P-B3-TAI-RESP, P-B3-PB-RESP, P-B3-BLP-RESP, P-B3-FLA-RESP, P-B3-BUR-RESP, P-B3-GW-RESP, P-B3-PAY-RESP, P-B3-SGA-RESP, P-B3-SHO-RESP, P-B3-RFP-RESP, P-B3-DS-RESP, P-B3-PBF-RESP, P-B3-GT-RESP, P-B3-HAL-RESP, P-B3-GG-RESP], note: "23 标准成员；强实例：TAR 水面取向+气呼吸 runtime premise / TAI+GW 陆生猎物水面呈现 / PBF 温血 typed fact（FR3 §7）/ AST 鲟科须探第 3 例 / GT 夜礁缘（不买 Night Mode——R03 教训）；PAY/SHO/DS 为形态/同属/同科推算（Confidence MEDIUM）"}""",
        """      - {batch: CENSUS-B3, program_id: [P-B3-CHN-RESP, P-B3-COH-RESP, P-B3-PIN-RESP, P-B3-BRO-RESP, P-B3-ALE-RESP, P-B3-AST-RESP, P-B3-SNS-RESP, P-B3-TAR-RESP, P-B3-TAI-RESP, P-B3-PB-RESP, P-B3-BLP-RESP, P-B3-FLA-RESP, P-B3-BUR-RESP, P-B3-GW-RESP, P-B3-PAY-RESP, P-B3-SGA-RESP, P-B3-SHO-RESP, P-B3-RFP-RESP, P-B3-DS-RESP, P-B3-PBF-RESP, P-B3-GT-RESP, P-B3-HAL-RESP, P-B3-GG-RESP], note: "23 标准成员；强实例：TAR 水面取向+气呼吸 runtime premise / TAI+GW 陆生猎物水面呈现 / PBF 温血 typed fact（FR3 §7）/ AST 鲟科须探第 3 例 / GT 夜礁缘（不买 Night Mode——R03 教训）；PAY/SHO/DS 为形态/同属/同科推算（Confidence MEDIUM）"}
      - {batch: CENSUS-B4, program_id: [P-B4-POR-RESP, P-B4-SDG-RESP, P-B4-TSK-RESP, P-B4-ASR-RESP, P-B4-RVS-RESP, P-B4-GPF-RESP, P-B4-RKB-RESP, P-B4-SSL-RESP, P-B4-BSK-RESP, P-B4-RRH-RESP, P-B4-GRH-RESP, P-B4-SMB-RESP, P-B4-GDE-RESP, P-B4-WIT-RESP, P-B4-WIN-RESP, P-B4-YTF-RESP, P-B4-SMF-RESP, P-B4-BST-RESP, P-B4-FDR-RESP, P-B4-BSB-RESP, P-B4-CBM-RESP, P-B4-SAI-RESP, P-B4-MOO-RESP, P-B4-RDS-RESP], note: "24 标准成员；强实例：SDG+TSK evaluator_channel=PASSIVE_ELECTROSENSE 第 2/3 例（FR3 判例① K8 感知端）/ POR 温血第 2 例 / GDE+CBM 夜行+WIN 日间低光 typed context（R03 教训不买 Mode）/ SMB 咽喉骨板磿碎机制 typed 事实（草鱼 R02 先例）/ RDS 贝食偏好原文；MEDIUM 推算 6 例（RVS+MOO=P01 冻结主张承载 / GPF+RKB=齿板喙齿形态 / BSK=吸口形态 / SMF=掘穴栖息）"}""")
    # GUARD：F-3 轴声明对齐 + HNC 成员追加（extension 候选挂账）
    t = t.replace(
        """    allowed_parameter_axes:
      - intruder_evaluator_context(typed：nest_anchor | fry_anchor)
      - path_strength_weights""",
        """    allowed_parameter_axes:
      - intruder_evaluator_context(typed：nest_anchor | fry_anchor | foam_nest[B0-FIX] | sand_nest[B3, pending HRQ-B3-02] | tree_root_eggs[B3, pending HRQ-B3-02] | male_built_nest[B3, pending HRQ-B3-02] | pebble_mound[B4 提案, pending HRQ-B4-01])   # B3-F-3 修正（CENSUS-B4）：原声明仅 2 值与 known_instances 6 anchor 实例漂移，现对齐并标注审批态
      - guard_target_specificity(typed：species_typed_intruder[B4 提案, pending HRQ-B4-01] | any_intruder[B0-B3 默认未显式分型])   # NEW 轴提案（HRQ-B4-01）
      - path_strength_weights""")
    t = t.replace(
        """      - {batch: CENSUS-B3, program_id: P-B3-WEL-RESP, blind_hash: 2b938a5ca14665e4, note: "第 7 成员（欧洲巨鲶雄巢守护）：anchor=male_built_nest；听嗅主导+夜行 typed context premise"}""",
        """      - {batch: CENSUS-B3, program_id: P-B3-WEL-RESP, blind_hash: 2b938a5ca14665e4, note: "第 7 成员（欧洲巨鲶雄巢守护）：anchor=male_built_nest；听嗅主导+夜行 typed context premise"}
      - {batch: CENSUS-B4, program_id: P-B4-HNC-RESP, blind_hash: fb17fdf2f57dbadf, note: "第 8 成员（双点美鱥石巢守护）extension 候选挂账：anchor=pebble_mound（轴值提案）+guard_target_specificity=species_typed_intruder（NEW 轴提案——『defend…from other N. biguttatus males but not other species』逐字；异种借巢被容忍）；骨架同构（engine raw 仅槽名/合并步标名字面）；TEMPLATE_EXTENSION_CANDIDATE pending HRQ-B4-01——批准前不计正式成员"}""")
    # GUARD open_precedents 追加
    t = t.replace(
        """    open_precedents: [HRQ-03（与 PLAIN 的 extend-vs-split）]""",
        """    open_precedents: [HRQ-03（与 PLAIN 的 extend-vs-split）, HRQ-B4-01（guard_target_specificity 新轴+anchor pebble_mound 提案）]""")
    # STATE_GATED：F-2 ir_pointer 物化指向
    t = t.replace(
        """    ir_pointer: batches/CENSUS-B3/build_blind_programs.py::P-B3-CHU-RESP-FASTING""",
        """    ir_pointer: batches/CENSUS-B4/run_merge_tests.py::CANONICALS.STATE_GATED_MULTI_PATH_RESPONSE（B3-F-2 修正物化：IR 逐字转写自 origin batches/CENSUS-B3/build_blind_programs.py::P-B3-CHU-RESP-FASTING；物化自测+SHA 成员回归复检双 PASS 留痕 CENSUS-B4/merge_tests.jsonl）""")
    io.open(p, "w", encoding="utf-8").write(t)
    import yaml
    reg = yaml.safe_load(io.open(p, encoding="utf-8"))
    assert reg["version"] == 6 and len(reg["templates"]) == 10, (
        reg["version"], len(reg["templates"]))
    counts = {x["template_id"]: len(x["known_instances"]) for x in reg["templates"]}
    print("registry v6:", counts)
    # discovery curve
    c = ROOT / "discovery_curve.csv"
    t = io.open(c, encoding="utf-8").read().rstrip() + \
        "\nCENSUS-B4,26,50,51,1,0,0,0,0,0,0,0,0,0\n"
    io.open(c, "w", encoding="utf-8").write(t)
    n_mc = sum(1 for m in M if m["verdict"] == "MERGE_CONFIDENT")
    n_ext = sum(1 for m in M if m["verdict"] == "TEMPLATE_EXTENSION_CANDIDATE")
    n_new = sum(1 for m in M if m["verdict"] == "NEW_TEMPLATE_CANDIDATE")
    print(f"merge_tests={len(M)} (MC={n_mc} EXT={n_ext} NEWC={n_new}) "
          f"programs={len(out)}")


if __name__ == "__main__":
    main()
