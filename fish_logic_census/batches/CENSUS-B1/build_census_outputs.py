# -*- coding: utf-8 -*-
"""CENSUS-B1 判同产物：merge_tests.jsonl / programs.jsonl / resolver_tests.jsonl /
absence_claims.jsonl。语义裁决（worker reasoning）+ engine raw 留痕。
"""
import json
from pathlib import Path

BATCH = Path(__file__).parent
FIX = None  # 本批无修复轮补录

HRQ = {"single": "HRQ-B1-01", "ctx": "HRQ-B1-02", "cue": "HRQ-B1-03",
       "plain_axis": "HRQ-B1-04", "members": "HRQ-B1-05"}
CRR_DIFFS = ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"]
CRR_NO_RANK = ("CRR 判别结构（FeasibleSet→RelativeRank(reference_set)→Secondary Refuge"
               "→Fixed Combine）不存在于本程序：无相对寻优、无约束内寻优")
AXIS_NOTE = "轴属立族/扩容提案（HRQ 待批）；engine raw diff 为槽名字面差异，body 骨架同构"

EXT_CTX_COST = {
    "extension_complexity_cost": (
        "PATCH canonical 增加可选 context 槽（NONE|typed）：既有成员湄公鲶多一项 "
        "context=zone 已占槽（无扩散）；但 2 步成员并入后族内出现『有无 context 步』"
        "两种 body 形状，canonical 定义与 Trace 语义复杂化；context 步的业务意义"
        "（typed 环境调制）被降格为开关"
    ),
    "new_template_complexity_cost": (
        "SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）与 PATCH（3 步带 typed context）并存："
        "各 canonical 纯净；成员归属唯一（GRB/DRU/PAD34/SMA 归 SINGLE）；代价是 "
        "registry Bake 族 +1 与两族边界知识维护"
    ),
    "recommended_shape": "HUMAN_DECISION",
}

def mt(pid, tpl_id, verdict, engine_diffs, reasoning, axis=None, same=False,
       param_only=False, ext=False, queue=None):
    r = {"program_id": pid, "template_id": tpl_id, "verdict": verdict,
         "same": same, "param_only": param_only,
         "structural_diffs": [] if verdict == "MERGE_CONFIDENT" else engine_diffs,
         "engine_raw_diffs": engine_diffs, "reasoning": reasoning,
         "provenance": {"batch": "CENSUS-B1", "engine": "census_engine.structural_diff",
                        "report": "engine_report.json"}}
    if axis:
        r["proposed_parameter_axis"] = axis
    if queue:
        r["human_review_queued"] = queue
    if ext:
        r.update(EXT_CTX_COST)
    return r

BAKE_CRR = ["P-B1-GRB-BAKE", "P-B1-BRT-BAKE", "P-B1-DRU-BAKE", "P-B1-COD-BAKE",
            "P-B1-PAD34-BAKE", "P-B1-BLU-BAKE", "P-B1-SMA-BAKE", "P-B1-LAM-BAKE",
            "P-B1-ONS-BAKE"]
BAKE_CRR_TGT = {"P-B1-GRB-BAKE": "SINGLE", "P-B1-DRU-BAKE": "SINGLE",
                "P-B1-PAD34-BAKE": "SINGLE", "P-B1-SMA-BAKE": "SINGLE",
                "P-B1-COD-BAKE": "SINGLE", "P-B1-BLU-BAKE": "SINGLE",
                "P-B1-LAM-BAKE": "SINGLE", "P-B1-ONS-BAKE": "PATCH",
                "P-B1-BRT-BAKE": "PLAIN"}
TYPED_STD = ["P-B1-GRB-RESP", "P-B1-BRT-RESP", "P-B1-TIL-RESP", "P-B1-PAD35-RESP",
             "P-B1-DRU-RESP", "P-B1-COD-RESP", "P-B1-PIK-RESP", "P-B1-GAR-RESP",
             "P-B1-BLU-RESP", "P-B1-SMA-RESP", "P-B1-RAI-RESP", "P-B1-ONS-RESP"]
SINGLE_NOTE = {
    "P-B1-GRB-BAKE": "植食/预投饵资源 patch（P02）",
    "P-B1-DRU-BAKE": "底栖猎物 patch（P02）",
    "P-B1-PAD34-BAKE": "浮游猎物 patch（幼体限定）",
    "P-B1-SMA-BAKE": "扰动暴露猎物动态机会 patch（P02）",
    "P-B1-COD-BAKE": "深度 habitat 因子（sex/stage 绑定）",
    "P-B1-BLU-BAKE": "季节水层 habitat 因子",
    "P-B1-LAM-BAKE": "化学梯度场（信息素/警报；非资源场——factor_type 轴最宽实例，轴边界交 HRQ）",
}

MERGE_TESTS = []
# --- vs CRR（9）---
for pid in BAKE_CRR:
    tgt = BAKE_CRR_TGT[pid]
    MERGE_TESTS.append(mt(
        pid, "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE", CRR_DIFFS,
        f"{CRR_NO_RANK}。归 {tgt} 候选族（B1 判同）。",
        queue=HRQ["single"] if tgt == "SINGLE" else
        (HRQ["ctx"] if tgt == "PATCH" else HRQ["plain_axis"])))
# --- SINGLE 族 7 成员直验 ---
for pid, note in SINGLE_NOTE.items():
    MERGE_TESTS.append(mt(
        pid, "SINGLE_FACTOR_NORMALIZED_WEIGHT", "MERGE_CONFIDENT",
        ["OPERATOR", "PREMISE"],
        f"骨架同构（单 typed 场/因子评估→归一化，无 combine、无 gate）；槽名字面在 "
        f"factor_type(typed) 轴内。实例={note}。" + AXIS_NOTE,
        axis="factor_type(typed: resource_patch | habitat_factor | chemical_gradient_field)",
        same=True, param_only=False))
# --- PATCH 第 2 成员（ONS）---
MERGE_TESTS.append(mt(
    "P-B1-ONS-BAKE", "PATCH_RESOURCE_FOLLOWING", "MERGE_CONFIDENT",
    ["OPERATOR", "PREMISE"],
    "第二成员直验：3 步同构（patch→typed context→normalize）；APPLY_CURRENT_CONTEXT "
    "与 CONSTRAIN_ZONE 为同一 typed context 槽命名差异（context_type 轴：zone|current）。"
    "P06 域第二实例，PROVISIONAL 维持待 P06 压缩测试。" + AXIS_NOTE,
    axis="context_type(typed: zone | current)", same=True, param_only=False))
# --- 4 patch 成员 vs PATCH（optional_context extension 判例）---
for pid in ["P-B1-GRB-BAKE", "P-B1-DRU-BAKE", "P-B1-PAD34-BAKE", "P-B1-SMA-BAKE"]:
    MERGE_TESTS.append(mt(
        pid, "PATCH_RESOURCE_FOLLOWING", "TEMPLATE_EXTENSION_CANDIDATE",
        ["DEPENDENCY", "OPERATOR", "PREMISE"],
        "对 PATCH canonical 的真结构差异：缺 typed context 中间步（依赖链 2 段 vs 3 段）。"
        "不能 MERGE（F14）。两条路：a) PATCH 加 optional_context 槽吸收；b) 归 "
        "SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步族）。本批以 SINGLE 族承接（7 成员直验），"
        "族间边界（context 步是结构元素还是退化）交 review（HRQ-B1-02）。",
        axis="optional_context: NONE | typed", ext=True, queue=HRQ["ctx"]))
# --- PLAIN 第 3 成员（BRT）---
MERGE_TESTS.append(mt(
    "P-B1-BRT-BAKE", "PLAIN_FACTOR_COMBINE", "MERGE_CONFIDENT",
    ["DEPENDENCY", "OPERATOR", "PREMISE"],
    "第 3 成员直验：patch 因子 + rank_position 因子 → COMBINE_WEIGHTED，骨架同构；"
    "与 canonical 差异=因子槽位数（2 vs 4，factor_set 轴槽位数 2–6 内）+ rank 为新具名 "
    "typed 因子类型（EVAL_RANK_POSITION_PREFERENCE，个体属性因子——factor_set 轴的新类型"
    "准入，关联 B0 HRQ-01 轴边界）+ combine 语义相同。" + AXIS_NOTE,
    axis="factor_set(typed,bounded 2–6 槽；新因子类型 rank_position 待批)", same=True,
    param_only=False, queue=HRQ["plain_axis"]))
# --- TYPED 12 标准成员 ---
TYPED_STD_NOTE = {
    "P-B1-GRB-RESP": "植食/饵取向（P02 背景下离散 TargetFeeding）",
    "P-B1-BRT-RESP": "位置竞争背景下的食物评估（conflict path 证据不足不建——「明显攻击并不多」）",
    "P-B1-TIL-RESP": "口孵期 cap 抑制（premise 参数，body 单态）",
    "P-B1-PAD35-RESP": "cue_history 输入扩展（evaluator 输入 fact，body 单态；状态契约 Input Contract Open→TAR-07）",
    "P-B1-DRU-RESP": "底栖取向（P02）",
    "P-B1-COD-RESP": "遥测深度不判定当下 FeedingMatch，标准成员",
    "P-B1-PIK-RESP": "初次接受 only（取饵后阶段 OUT_OF_SCOPE）",
    "P-B1-GAR-RESP": "最初接受 only（携行/吞咽/Hook OUT_OF_SCOPE）",
    "P-B1-BLU-RESP": "窄接受参数宽度（小饵低阻；吐饵 OUT_OF_SCOPE）",
    "P-B1-SMA-RESP": "被惊出猎物取向（P02）",
    "P-B1-RAI-RESP": "表面鼠形饵 context + 地域 Profile 重绑定（纯参数阴性样本）",
    "P-B1-ONS-RESP": "刮食口径窗（P02/P06 域，confidence LOW）",
}
for pid in TYPED_STD:
    MERGE_TESTS.append(mt(
        pid, "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
        f"engine 无字面差异（PREMISE 按 F02 不计入）。实例注记：{TYPED_STD_NOTE[pid]}。",
        same=True, param_only=True))
# --- PAD34 sense（通道轴）---
MERGE_TESTS.append(mt(
    "P-B1-PAD34-RESP-SENSE", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT",
    ["OPERATOR", "PREMISE"],
    "感知段：EVAL_TARGET_EXPOSURE_TYPED（被动电感受通道）与 AS_FOOD 字面差异在 "
    "evaluator_channel 轴内（B0 电鳗主动电定位同款通道槽；PASSIVE_ELECTROSENSE 为新通道"
    "实例）。产品电呈现契约未定（Product Scope Deferred→TAR-07）。" + AXIS_NOTE,
    axis="evaluator_channel(typed: +PASSIVE_ELECTROSENSE)", same=True, param_only=False))
# --- DUAL 第 4 成员（DIS）---
MERGE_TESTS.append(mt(
    "P-B1-DIS-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "MERGE_CONFIDENT",
    ["PREMISE"],
    "第 4 成员直验：engine 无字面差异；fry_anchor=幼鱼群（intruder_evaluator_context "
    "轴新实例：贴附取食的幼鱼群 relation object）；色型不分裂（S12 白色型同构对照不重复建体）。"
    "与 Semantic Review Context §9.2 判例及 P04 语义一致。",
    axis="intruder_evaluator_context(typed: +fry_school)", same=True, param_only=False))
# --- LAM approach 边界判例 ---
MERGE_TESTS.append(mt(
    "P-B1-LAM-RESP-APPROACH", "TYPED_TARGET_RESPONSE", "NEW_TEMPLATE_CANDIDATE",
    ["OPERATOR", "PREMISE", "RETURN"],
    "与 typed-target 族的真差异：①central evaluand=环境化学梯度场（非离散钩饵目标，"
    "PrimaryEvaluand=Other）；②RETURN 语义=Approach|Avoid（非 TargetFeeding——信息素"
    "吸引不是 Feeding，Story 明言）。RETURN 差异是四态判据真结构差异，不 MERGE。"
    "立 CUE_GUIDED_APPROACH_AVOID 候选族（关联 Semantic Review Context §10 环境场 "
    "evaluand 判例：Field Channel 的 OPEN 边界——census 累计 Candidate 不自动 promote "
    "Grammar）。Product Scope Deferred（TAR-06）。",
    queue=HRQ["cue"]))
MERGE_TESTS.append(mt(
    "P-B1-LAM-RESP-APPROACH", "CUE_GUIDED_APPROACH_AVOID", "MERGE_CONFIDENT",
    ["PREMISE"],
    "canonical 源（单成员 PROVISIONAL：产品范围未定+FR 线 Non-feeding cue-guided "
    "approach 组合待检验；若产品不纳趋向/诱捕，候选冻结归档）。",
    same=True, param_only=True))

CONSEQUENCE = {}
for pid in BAKE_CRR:
    CONSEQUENCE[pid] = ("NEW_PROGRAM_CANDIDATE", BAKE_CRR_TGT[pid] + (
        "_FACTOR_NORMALIZED_WEIGHT" if BAKE_CRR_TGT[pid] == "SINGLE" else
        ("_RESOURCE_FOLLOWING" if BAKE_CRR_TGT[pid] == "PATCH" else "_FACTOR_COMBINE")))
for pid in TYPED_STD + ["P-B1-PAD34-RESP-SENSE"]:
    CONSEQUENCE[pid] = ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE")
CONSEQUENCE["P-B1-DIS-RESP-GUARD"] = ("NEW_PROGRAM_CANDIDATE", "GUARD_CONFLICT_DUAL_PATH_RESPONSE")
CONSEQUENCE["P-B1-LAM-RESP-APPROACH"] = ("NEW_PROGRAM_CANDIDATE", "CUE_GUIDED_APPROACH_AVOID")
QUEUE_REF = {"SINGLE": HRQ["single"], "PATCH": HRQ["ctx"], "PLAIN": HRQ["plain_axis"],
             "TYPED": HRQ["members"], "DUAL": HRQ["members"],
             "CUE": HRQ["cue"]}

RESOLVER_TESTS = [
    {"resolver_id": "NO_NEW_RESOLVER_FAMILY",
     "note": ("B1 未新增 semantic resolver family：patch/梯度场评估与 typed evaluator 均"
              "为模板内 op；扰动事件/化学梯度场/预投饵斑块/痕迹可见性均为世界侧事实供给"
              "义务（登记：disturbance_events、chemical_gradient_field、prebait_patches、"
              "feeding_traces——触发上游 SNAP 事实清单登记，与 coverage_delta report §5b 同源）"),
     "provenance": {"batch": "CENSUS-B1"}},
]

ABSENCE = [{
    "story_id": "CENSUS-B1-RAI",
    "claim": "NO_NEW_PROGRAM_CURRENT_EVIDENCE",
    "scope": "虹鳟鼠形表面饵地域变体：纯 Profile/参数重绑定样本，无新程序结构",
    "basis": ("B0/B1 已识别族内完全吸收（TYPED 标准成员，engine 无字面差异）；"
              "地域变体=per-instance Profile 重绑定、表面 context=呈现参数。"
              "基于 B01-S24 冻结证据（Stable/L2）"),
    "provenance": {"batch": "CENSUS-B1"},
}]


def main():
    (BATCH / "merge_tests.jsonl").write_text(
        "\n".join(json.dumps(m, ensure_ascii=False) for m in MERGE_TESTS) + "\n",
        encoding="utf-8")
    programs = [json.loads(line) for line in
                (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()]
    out = []
    for p in programs:
        c, family = CONSEQUENCE[p["program_id"]]
        key = ("SINGLE" if "SINGLE" in family else
               "PATCH" if "PATCH" in family else
               "PLAIN" if "PLAIN" in family else
               "TYPED" if "TYPED" in family else
               "DUAL" if "DUAL" in family else "CUE")
        out.append({
            "program_id": p["program_id"], "story_id": p["story_id"],
            "species_id": p["species_id"], "surface": p["surface"],
            "consequence": c,
            "family_membership": family.replace("_FACTOR_NORMALIZED_WEIGHT", "_FACTOR_NORMALIZED_WEIGHT"),
            "review_ref": QUEUE_REF[key],
            "blind_hash": p["blind_hash"], "original_program_body_unchanged": True,
            "registry_seen_at_creation": False, "post_registry_mutations": [],
            "provenance": {"batch": "CENSUS-B1"}})
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n", encoding="utf-8")
    (BATCH / "resolver_tests.jsonl").write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in RESOLVER_TESTS) + "\n",
        encoding="utf-8")
    (BATCH / "absence_claims.jsonl").write_text(
        "\n".join(json.dumps(a, ensure_ascii=False) for a in ABSENCE) + "\n",
        encoding="utf-8")
    (BATCH / "coverage.jsonl").write_text("", encoding="utf-8")
    (BATCH / "program_revisions.jsonl").write_text("", encoding="utf-8")
    print(f"merge_tests={len(MERGE_TESTS)} programs={len(out)}")


if __name__ == "__main__":
    main()
