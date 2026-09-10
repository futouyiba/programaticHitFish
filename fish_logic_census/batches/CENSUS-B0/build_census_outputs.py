# -*- coding: utf-8 -*-
"""CENSUS-B0 判同产物生成：merge_tests.jsonl / programs.jsonl / resolver_tests.jsonl /
absence_claims.jsonl。

引擎（engine_report.json）只提供结构事实；本脚本写入 worker 的语义裁决与
reasoning。typed 槽名 / guard 名 / 通道名的字面差异在族定义声明的有限参数轴
（factor_set / hard_constraint_gate / evaluator_channel，均 HRQ 待批）下吸收；
引擎 raw diff 原样保留供 review 复核。
"""
import json
from pathlib import Path

BATCH = Path(__file__).parent

HRQ = {
    "plain": "HRQ-01", "hard": "HRQ-02", "ext": "HRQ-03", "patch": "HRQ-04",
    "typed": "HRQ-05", "dual": "HRQ-06", "order": "HRQ-07",
}
AXIS_NOTE = ("轴属立族提案（HRQ 待批）；引擎 raw diff 为槽名/guard/通道字面差异，"
             "body 骨架（步序/依赖形状/branch 位/combine/return）同构")

EXT_COST = {
    "extension_complexity_cost": (
        "PLAIN canonical 增加一个可选 hard_constraint_gate 槽（NONE|typed）：既有成员 "
        "OSC/CHB 多一项恒 NONE 配置（低）；但 canonical body 出现可选结构位，gate 必须"
        "前置于全部因子的不变式进入族定义，后续所有 PLAIN 成员与 Trace 都要解释 gate "
        "适用性，族 canonical 复杂度上升，开始接近『带开关的万能组合器』"
    ),
    "new_template_complexity_cost": (
        "registry Bake 族 +1（两族仅差一个前置 gate）：每族 canonical 保持纯净"
        "（纯因子组合 vs 门控因子组合），成员无重复归属（LUN/EEL 只属 HARD_GATED）；"
        "代价是登记条目 +1 与『两族差异仅一个结构元素』的知识维护"
    ),
    "recommended_shape": "HUMAN_DECISION",
}

QUEUE_REF = {  # 显式映射：verdict 为 NEW/EXTENSION 的 merge_test → human review 条目
    ("P-MGC-BAKE-ADULT", "CONSTRAINED_RELATIVE_REFUGE"): HRQ["patch"],
    ("P-LUN-BAKE-WET", "CONSTRAINED_RELATIVE_REFUGE"): HRQ["hard"],
    ("P-OSC-BAKE", "CONSTRAINED_RELATIVE_REFUGE"): HRQ["plain"],
    ("P-EEL-BAKE", "CONSTRAINED_RELATIVE_REFUGE"): HRQ["hard"],
    ("P-CHB-BAKE", "CONSTRAINED_RELATIVE_REFUGE"): HRQ["plain"],
    ("P-LUN-BAKE-WET", "PLAIN_FACTOR_COMBINE"): HRQ["ext"],
    ("P-EEL-BAKE", "PLAIN_FACTOR_COMBINE"): HRQ["ext"],
    ("P-MGC-BAKE-ADULT", "PLAIN_FACTOR_COMBINE"): HRQ["patch"],
}

def mt(pid, tpl, verdict, engine_diffs, reasoning, axis=None, freedom=None,
       same=False, param_only=False, ext=False):
    r = {
        "program_id": pid, "template_id": tpl, "verdict": verdict,
        "same": same, "param_only": param_only,
        "structural_diffs": [] if verdict == "MERGE_CONFIDENT" else engine_diffs,
        "engine_raw_diffs": engine_diffs,
        "reasoning": reasoning,
        "provenance": {"batch": "CENSUS-B0", "engine": "census_engine.structural_diff",
                       "report": "engine_report.json"},
    }
    if axis:
        r["proposed_parameter_axis"] = axis
    if freedom:
        r["required_new_freedom"] = freedom
    if verdict in ("NEW_TEMPLATE_CANDIDATE", "TEMPLATE_EXTENSION_CANDIDATE"):
        r["human_review_queued"] = QUEUE_REF[(pid, tpl)]
    if ext:
        r.update(EXT_COST)
    return r

CRR_NO_RANK = ("CRR 的判别结构（FeasibleSet→RelativeRank(reference_set)→Secondary Refuge"
               "→Fixed Combine）在本程序不存在：无相对排序、无约束内寻优")

MERGE_TESTS = [
    # --- vs registry v0 唯一种子 CRR ---
    mt("P-MGC-BAKE-ADULT", "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "单资源链（patch→zone→weight）与 CRR 完全不同构；" + CRR_NO_RANK +
       "。归 PATCH_RESOURCE_FOLLOWING 单成员族（HRQ-04）。"),
    mt("P-LUN-BAKE-WET", "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "有 hard gate 但 gate 之后是因子加权组合；" + CRR_NO_RANK +
       "。水面可达是绝对约束（无通道即不可存活）而非相对最优，故非 CRR 变体；"
       "归 HARD_GATED_FACTOR_COMBINE（HRQ-02）。"),
    mt("P-LUN-BAKE-AESTIVATION", "CONSTRAINED_RELATIVE_REFUGE", "AMBIGUOUS_NEEDS_EXPANSION",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "anchor 退化体与 CRR 结构差异真实，但 playable scope 未决（干季穴捕 S10=EO），"
       "结构裁决悬置；见 TARGETED_AUDIT_REQUEST TAR-01。"),
    mt("P-OSC-BAKE", "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "无 gate 的因子组合体；" + CRR_NO_RANK + "。归 PLAIN_FACTOR_COMBINE（HRQ-01）。"),
    mt("P-EEL-BAKE", "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "门控因子组合体，同 P-LUN-BAKE-WET 判据；" + CRR_NO_RANK +
       "。归 HARD_GATED_FACTOR_COMBINE（HRQ-02）。"),
    mt("P-CHB-BAKE", "CONSTRAINED_RELATIVE_REFUGE", "NEW_TEMPLATE_CANDIDATE",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "无 gate 因子组合体，同 P-OSC-BAKE 判据；" + CRR_NO_RANK +
       "。归 PLAIN_FACTOR_COMBINE（HRQ-01）。"),
    # --- 族内直验（candidate canonical body） ---
    mt("P-OSC-BAKE", "PLAIN_FACTOR_COMBINE", "MERGE_CONFIDENT",
       ["OPERATOR", "PREMISE"],
       "body 骨架同构（4 typed 因子槽→COMBINE_WEIGHTED，deps/combine/return 全同）；"
       "OPERATOR 仅为具体因子名字面（STILLWATER/SUBSTRATE_STRUCTURE/PREY/ANCHOR_PROXIMITY），"
       "在 factor_set(typed,bounded) 轴内。PREMISE 差异按 F02 不计入 body。" + AXIS_NOTE,
       axis="factor_set(typed,bounded)", same=True, param_only=False),
    mt("P-CHB-BAKE", "PLAIN_FACTOR_COMBINE", "MERGE_CONFIDENT",
       ["OPERATOR", "PREMISE"],
       "骨架同构；因子字面（FLOW/POOL_STRUCTURE/PREY/SURFACE_FILM）在 factor_set 轴内；"
       "spawn 因子集切换按 P05 配置级处理（body 无 IF）。" + AXIS_NOTE,
       axis="factor_set(typed,bounded)", same=True, param_only=False),
    mt("P-LUN-BAKE-WET", "HARD_GATED_FACTOR_COMBINE", "MERGE_CONFIDENT",
       ["BRANCH", "OPERATOR", "PREMISE"],
       "canonical 源；BRANCH 为 guard 命名字面（surface_access_available vs generic），"
       "在 hard_constraint_gate(typed) 轴内；因子字面在 factor_set 轴内。" + AXIS_NOTE,
       axis="factor_set(typed,bounded)+hard_constraint_gate(typed)", same=True, param_only=False),
    mt("P-EEL-BAKE", "HARD_GATED_FACTOR_COMBINE", "MERGE_CONFIDENT",
       ["BRANCH", "OPERATOR", "PREMISE"],
       "直验通过：与 canonical 同为 BUILD→GATE→3 因子→COMBINE_WEIGHTED，依赖形状相同；"
       "SUBSTRATE_STRUCTURE 与 STRUCTURE 为同一 typed 结构因子槽命名差异；guard 同为"
       "水面可达。" + AXIS_NOTE,
       axis="factor_set(typed,bounded)+hard_constraint_gate(typed)", same=True, param_only=False),
    mt("P-LUN-BAKE-WET", "PLAIN_FACTOR_COMBINE", "TEMPLATE_EXTENSION_CANDIDATE",
       ["BRANCH", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "对 PLAIN canonical 的真结构差异：前置 hard gate（BUILD_ACCESSIBLE_SET+GATE 步骤、"
       "branch 条目、因子 deps 全部改指 gate 输出）。不能 MERGE（F03/F14）。两条路："
       "a) PLAIN 增加有限 typed 轴 hard_constraint_gate: NONE|typed；b) 独立立 "
       "HARD_GATED_FACTOR_COMBINE 族。Extension 非天然优于 New，输出 Total Complexity "
       "Compare 供 review 裁决（HRQ-03）。",
       axis="hard_constraint_gate: NONE | typed_hard_viability", ext=True),
    mt("P-EEL-BAKE", "PLAIN_FACTOR_COMBINE", "TEMPLATE_EXTENSION_CANDIDATE",
       ["BRANCH", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "同 P-LUN-BAKE-WET 的 gate 轴判例（同一差异形状，两成员一致）。（HRQ-03）",
       axis="hard_constraint_gate: NONE | typed_hard_viability", ext=True),
    mt("P-MGC-BAKE-ADULT", "PATCH_RESOURCE_FOLLOWING", "MERGE_CONFIDENT",
       ["PREMISE"],
       "canonical 源（单成员族，engine 无字面差异）。单成员 PROVISIONAL：与 P06 "
       "Compression Candidate 联动（FR 线待测压回 P02），族升级等后续 P06 成员（HRQ-04）。",
       same=True, param_only=True),
    mt("P-MGC-BAKE-ADULT", "PLAIN_FACTOR_COMBINE", "NEW_TEMPLATE_CANDIDATE",
       ["COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "确证不并入：单资源链无 combine 语义、无多因子依赖扇入，与因子组合体结构真差异。"
       "作为 PATCH 族与 PLAIN 族的相互 non-match 证据记录。"),
    mt("P-MGC-RESP-FEEDING", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "canonical 源；engine 无字面差异（EVAL_TYPED→DECIDE）。evaluator 类型随 lifecycle "
       "premise 切换（参数绑定），body 单态。",
       same=True, param_only=True),
    mt("P-LUN-RESP-FEEDING", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "直验通过：吸吮 typed evaluator 槽位差异在 evaluator_channel 轴内，骨架同构。",
       axis="evaluator_channel(typed)", same=True, param_only=False),
    mt("P-OSC-RESP-FEEDING", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "直验通过：伏击 typed（掩体/静水 context）槽位差异在 evaluator_channel 轴内。",
       axis="evaluator_channel(typed)", same=True, param_only=False),
    mt("P-CHB-RESP-FEEDING", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "直验通过：机会主义宽谱 evaluator 槽位差异在 evaluator_channel 轴内；"
       "体型分级仅改参数宽度。",
       axis="evaluator_channel(typed)", same=True, param_only=False),
    mt("P-EEL-RESP-SENSE", "TYPED_TARGET_RESPONSE", "MERGE_CONFIDENT",
       ["OPERATOR", "PREMISE"],
       "感知段：EVAL_TARGET_EXPOSURE_TYPED（电场扰动通道+夜行弱光）与 AS_FOOD 通道字面"
       "差异在 evaluator_channel 轴内；骨架同构（typed evaluator→DECIDE）。主动发电场"
       "是持续背景行为，非目标程序分支。" + AXIS_NOTE + "。攻击段 OUT_OF_SCOPE（envelope）。",
       axis="evaluator_channel(typed)", same=True, param_only=False),
    mt("P-OSC-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "canonical 源（证据最全：双亲护卵+迁仔）；guard_state 为 persistent condition "
       "premise（F02），双路径并行评估+合并是 Response 自有程序。",
       same=True, param_only=True),
    mt("P-LUN-RESP-GUARD", "GUARD_CONFLICT_DUAL_PATH_RESPONSE", "MERGE_CONFIDENT", ["PREMISE"],
       "直验通过（engine 无字面差异）：雄鱼护巢（腹鳍供氧）同构双路径体；confidence "
       "MEDIUM（conflict 响应为 P04 语义映射，攻击性直接证据开放）。",
       same=True, param_only=True),
    mt("P-LUN-BAKE-AESTIVATION", "PLAIN_FACTOR_COMBINE", "AMBIGUOUS_NEEDS_EXPANSION",
       ["COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "anchor 退化体（评估链空置）与因子组合体结构真差异，但 playable scope 未决"
       "（S10=EO）→ 不立新族，悬置待 TAR-01。"),
    mt("P-LUN-BAKE-AESTIVATION", "HARD_GATED_FACTOR_COMBINE", "AMBIGUOUS_NEEDS_EXPANSION",
       ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"],
       "同上：结构差异真实，裁决悬置（TAR-01）。"),
]

CONSEQUENCE = {
    "P-MGC-BAKE-ADULT": ("NEW_PROGRAM_CANDIDATE", "PATCH_RESOURCE_FOLLOWING", HRQ["patch"]),
    "P-MGC-RESP-FEEDING": ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE", HRQ["typed"]),
    "P-LUN-BAKE-WET": ("NEW_PROGRAM_CANDIDATE", "HARD_GATED_FACTOR_COMBINE", HRQ["hard"]),
    "P-LUN-BAKE-AESTIVATION": ("AMBIGUOUS", None, "TAR-01"),
    "P-LUN-RESP-FEEDING": ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE", HRQ["typed"]),
    "P-LUN-RESP-GUARD": ("NEW_PROGRAM_CANDIDATE", "GUARD_CONFLICT_DUAL_PATH_RESPONSE", HRQ["dual"]),
    "P-OSC-BAKE": ("NEW_PROGRAM_CANDIDATE", "PLAIN_FACTOR_COMBINE", HRQ["plain"]),
    "P-OSC-RESP-FEEDING": ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE", HRQ["typed"]),
    "P-OSC-RESP-GUARD": ("NEW_PROGRAM_CANDIDATE", "GUARD_CONFLICT_DUAL_PATH_RESPONSE", HRQ["dual"]),
    "P-EEL-BAKE": ("NEW_PROGRAM_CANDIDATE", "HARD_GATED_FACTOR_COMBINE", HRQ["hard"]),
    "P-EEL-RESP-SENSE": ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE", HRQ["typed"]),
    "P-CHB-BAKE": ("NEW_PROGRAM_CANDIDATE", "PLAIN_FACTOR_COMBINE", HRQ["plain"]),
    "P-CHB-RESP-FEEDING": ("NEW_PROGRAM_CANDIDATE", "TYPED_TARGET_RESPONSE", HRQ["typed"]),
}

RESOLVER_TESTS = [
    {"resolver_id": "SubstrateResourcePatchEvaluator",
     "kind": "typed_evaluator_helper", "admission_checks": {
         "semantic_stability": "PASS（P06 语义：ResourcePatch + typed substrate）",
         "cross_case_reuse": "PASS（P06 机制故事多成员，B0 仅湄公鲶成体 1 实例）",
         "no_author_edited_control_flow": "PASS（无内部控制流）",
         "typed_output": "PASS（patch 强度场）",
         "owner_boundary": "PASS（Bake 内 evaluator，非独立程序）"},
     "engine_helper_admission": {"admitted": True, "reasons": [], "verdict": "PASS"},
     "provisional": "PROVISIONAL_CASE_SPECIFIC 直到第二个跨 case 实例",
     "provenance": {"batch": "CENSUS-B0"}},
    {"resolver_id": "NO_NEW_RESOLVER_FAMILY",
     "note": ("B0 未新增 semantic resolver family：hard_viability gate 与 typed factor "
              "evaluators 均为模板内 op；GATE/anchor 等复杂度未外移（n_case_specific=0）"),
     "provenance": {"batch": "CENSUS-B0"}},
]

ABSENCE = [{
    "story_id": "FISH-R05-欧鲢-Size-Graded-Opportunism-Spawning-Run",
    "claim": "NO_NEW_PROGRAM_CURRENT_EVIDENCE",
    "scope": ("无超出本批已识别族（PLAIN_FACTOR_COMBINE / TYPED_TARGET_RESPONSE）的独有"
              "程序结构：阴性对照预期成立"),
    "basis": ("Bake 与 P-OSC-BAKE 在 factor_set 轴内直验同构；Response 为 TYPED 族标准"
              "成员；体型分级落因子权重/prey 谱参数，产卵洄游落 P05 配置级因子集切换；"
              "四面无 Group 拆分、无 Quality 程序差异。基于 FISH-R05 冻结证据"
              "（S3=EO 不影响程序结构判断；非 NO_NEW_PROGRAM_PROVEN）"),
    "provenance": {"batch": "CENSUS-B0"},
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
        c, family, ref = CONSEQUENCE[p["program_id"]]
        out.append({
            "program_id": p["program_id"], "story_id": p["story_id"],
            "species_id": p["species_id"], "surface": p["surface"],
            "consequence": c, "family_membership": family,
            "review_or_tar_ref": ref,
            "blind_hash": p["blind_hash"], "original_program_body_unchanged": True,
            "comparison_body_note": "deinstantiate() 派生视图；原 body 冻结于 blind_programs.jsonl",
            "registry_seen_at_creation": False, "post_registry_mutations": [],
            "provenance": {"batch": "CENSUS-B0"},
        })
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n", encoding="utf-8")
    (BATCH / "resolver_tests.jsonl").write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in RESOLVER_TESTS) + "\n",
        encoding="utf-8")
    (BATCH / "absence_claims.jsonl").write_text(
        "\n".join(json.dumps(a, ensure_ascii=False) for a in ABSENCE) + "\n",
        encoding="utf-8")
    for name in ("coverage.jsonl", "program_revisions.jsonl"):
        (BATCH / name).write_text("", encoding="utf-8")
    print(f"merge_tests={len(MERGE_TESTS)} programs={len(out)} -> {BATCH}")


if __name__ == "__main__":
    main()
