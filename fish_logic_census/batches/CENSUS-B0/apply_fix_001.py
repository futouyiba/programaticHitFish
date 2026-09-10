# -*- coding: utf-8 -*-
"""CENSUS-B0-FIX-001：独立审 REVISE 修复轮的 jsonl 级修改。

F-1（blocker）：补录 EEL S6（泡沫巢雄护）/S9（幼成切换）两个程序——修复轮非盲
（registry_seen_at_creation=true，形状影响风险声明见 provenance）；engine 实跑
对新 body 的判同，不手填结果。
F-2（blocker）：MGC FieldFeeding channel 与 potamodromous 洄游补分类注记。
"""
import hashlib
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from census_engine import structural_diff  # noqa: E402

BATCH = Path(__file__).parent
EEL_STORY = "FISH-R05-电鳗-Electrogenic-Remote-Prey-Control"
EEL_URL = "https://app.notion.com/p/3d7a4137d23681c9a5a3dcc1c7ddd4fc"  # R2 勘误：envelope 原文尾部多一个"4"（33 位无效 ID），此为 32 位规范 ID（与 blind_programs/stories.jsonl 一致）
FIX = "CENSUS-B0-FIX-001"

BIAS_DECL = ("修复轮非盲补录：创建时 registry 与族 canonical 已知（F-1 目标即覆盖缺口，"
             "同构预期本身是被审对象）；程序形状自冻结 Story 证据（S6 雄鱼筑泡沫巢护幼 / "
             "S9 幼体食无脊椎、成体食鱼及小哺乳）重建，由 reviewer 复检覆盖 fit 风险")

EEL_GUARD = {
    "program_id": "P-EEL-RESP-GUARD", "story_id": EEL_STORY, "species_id": "EEL",
    "surface": "Response",
    "incoming_premises": [
        "guard_state = MALE_FOAM_NEST_GUARD（雄鱼筑泡沫巢护幼，persistent condition）",
        "nest_anchor = foam_nest（泡沫巢 relation object）",
    ],
    "human_readable_sketch": (
        "护幼期双路径：path A 食物路径（typed food evaluator，成体食鱼及小哺乳）与 "
        "path B 入侵者路径（对泡沫巢 anchor 的距离/威胁 typed evaluator）并行评估 → "
        "双路径合并 → 决定响应（TargetFeeding 或 RelationalConflict）。guard 为 "
        "persistent premise（P04 语义），双路径评估与合并是 Response 自有程序。"
        "与 OSC（canonical）/LUN 同构，intruder_evaluator_context=foam_nest。"
    ),
    "ordered_steps": [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
        {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
        {"op": "DECIDE_RESPONSE", "deps": [2]},
    ],
    "branches": [], "combine": "DUAL_PATH_MERGE",
    "return_type": "Response(TargetFeeding | RelationalConflict)",
    "instance_noise": {"species": "Electric Eel", "profile": "MaleFoamNestGuard",
                       "constants": {}},
    "helpers": [], "source_evidence_ids": [EEL_URL],
    "open_semantics": ["护幼行为实证；conflict 响应为 P04 语义映射（同 LUN 判例）"],
    "confidence": "MEDIUM",
}
EEL_FEEDING = {
    "program_id": "P-EEL-RESP-FEEDING", "story_id": EEL_STORY, "species_id": "EEL",
    "surface": "Response",
    "incoming_premises": [
        "lifecycle_stage = JUVENILE | ADULT（幼体食无脊椎→成体食鱼及小型哺乳，上游决定 evaluator 绑定）",
    ],
    "human_readable_sketch": (
        "离散目标 → 随 lifecycle stage 绑定的 typed food evaluator（幼=无脊椎评估；"
        "成=鱼/小哺乳评估）→ 决定响应。TYPED_TARGET_RESPONSE 成员；evaluator_binding "
        "轴第二 premise 实例（首个=湄公鲶）。与感知段（P-EEL-RESP-SENSE，EXPOSURE 通道）"
        "是同一 ResponseProgram 的不同 evaluator 面；完整组合语义属 Representation 层。"
    ),
    "ordered_steps": [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "DECIDE_RESPONSE", "deps": [0]},
    ],
    "branches": [], "combine": "NONE",
    "return_type": "Response(TargetFeeding)",
    "instance_noise": {"species": "Electric Eel", "profile": None,
                       "constants": {"diet": "juv_invertebrate→adult_fish/small_mammal"}},
    "helpers": [], "source_evidence_ids": [EEL_URL],
    "open_semantics": [],
    "confidence": "HIGH",
}

# 判同对象（与 run_merge_tests.py 的 canonical 一致）
DUAL_CANONICAL = {
    "program_id": "TEMPLATE::GUARD_CONFLICT_DUAL_PATH_RESPONSE", "surface": "Response",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
        {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
        {"op": "DECIDE_RESPONSE", "deps": [2]},
    ],
    "branches": [], "combine": "DUAL_PATH_MERGE",
    "return_type": "Response(TargetFeeding | RelationalConflict)",
    "instance_noise": {"species": None, "profile": None, "constants": {}},
}
TYPED_CANONICAL = {
    "program_id": "TEMPLATE::TYPED_TARGET_RESPONSE", "surface": "Response",
    "incoming_premises": [],
    "ordered_steps": [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "DECIDE_RESPONSE", "deps": [0]},
    ],
    "branches": [], "combine": "NONE",
    "return_type": "Response(TargetFeeding)",
    "instance_noise": {"species": None, "profile": None, "constants": {}},
}

def fix_hash(record):
    body = {k: v for k, v in record.items() if k != "program_hash"}
    return hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()[:16]

def load(name):
    return [json.loads(l) for l in (BATCH / name).read_text(encoding="utf-8")
            .splitlines() if l.strip()]

def dump(name, rows):
    (BATCH / name).write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8")

def main():
    # --- F-1: merge_tests 追加（engine 实跑） ---
    mt = load("merge_tests.jsonl")
    for prog, canon, tpl, axis, reason in [
        (EEL_GUARD, DUAL_CANONICAL, "GUARD_CONFLICT_DUAL_PATH_RESPONSE", None,
         "第三成员直验（修复轮补录）：engine 无字面差异，骨架/op/deps/combine/return "
         "与 canonical 全同构；intruder_evaluator_context=foam_nest 在族轴内；"
         "PREMISE 差异按 F02 不计入。"),
        (EEL_FEEDING, TYPED_CANONICAL, "TYPED_TARGET_RESPONSE",
         "evaluator_binding(随 lifecycle premise 切换)",
         "engine 无字面差异；evaluator_binding 第二 premise 实例（首个=MGC），"
         "body 单态，绑定随 premise 配置切换。"),
    ]:
        diffs = sorted(structural_diff(prog, canon))
        verdict = "MERGE_CONFIDENT" if not [d for d in diffs if d != "PREMISE"] \
            else "NEW_TEMPLATE_CANDIDATE"
        assert verdict == "MERGE_CONFIDENT", (prog["program_id"], diffs)
        mt.append({
            "program_id": prog["program_id"], "template_id": tpl, "verdict": verdict,
            "same": True, "param_only": axis is not None,
            "structural_diffs": [], "engine_raw_diffs": diffs,
            "proposed_parameter_axis": axis,
            "reasoning": reason + "（" + BIAS_DECL + "）",
            "provenance": {"batch": FIX, "engine": "census_engine.structural_diff",
                           "driver": "independent review CENSUS-B0-REV-001 F-1"},
        })
    dump("merge_tests.jsonl", mt)

    # --- F-1: programs 追加 ---
    progs = load("programs.jsonl")
    for prog, family in [(EEL_GUARD, "GUARD_CONFLICT_DUAL_PATH_RESPONSE"),
                         (EEL_FEEDING, "TYPED_TARGET_RESPONSE")]:
        progs.append({
            "program_id": prog["program_id"], "story_id": prog["story_id"],
            "species_id": prog["species_id"], "surface": prog["surface"],
            "consequence": "NEW_PROGRAM_CANDIDATE", "family_membership": family,
            "review_or_tar_ref": "HRQ-06" if "GUARD" in prog["program_id"] else "HRQ-05",
            "blind_hash": None,
            "blind_hash_note": "created in " + FIX + "（非盲补录，无盲冻结 hash）；program_hash="
                               + fix_hash(prog) + " 为修复轮创建内容指纹",
            "program_hash": fix_hash(prog),
            "original_program_body_unchanged": True,
            "comparison_body_note": "修复轮创建即终态；未再改写",
            "registry_seen_at_creation": True, "post_registry_mutations": [],
            "provenance": {"batch": FIX,
                           "driver": "independent review CENSUS-B0-REV-001 F-1 (EEL S6/S9 coverage gap)",
                           "bias_declaration": BIAS_DECL},
        })
    # --- F-2: MGC 两条补注记 ---
    for p in progs:
        if p["program_id"] == "P-MGC-RESP-FEEDING":
            p["fix_notes"] = [{
                "round": FIX, "item": "F-2",
                "note": ("ResponseChannel FieldFeeding（幼体肉食期，story properties）按 "
                         "TYPED 族 evaluator_channel/binding 轴 premise 实例处理；幼体程序"
                         "证据不足不建体（TAR-02）。语义层 P0x 对应指针待 coordinator 确认"
                         "（coordinator 修复信中『P03 轴』引用未核实，census 侧不引用未读 pattern）")}]
        if p["program_id"] == "P-MGC-BAKE-ADULT":
            p["fix_notes"] = [{
                "round": FIX, "item": "F-2",
                "note": ("potamodromous 洄游照 CHB 先例按 P05 配置级处理（Bake 因子集随 "
                         "lifecycle premise 配置切换）；洄游细节少知，不展开 spawn 因子集")}]
    dump("programs.jsonl", progs)

    # --- F-1/F-2: stories.jsonl 的 EEL/MGC 条目更新 ---
    stories = load("stories.jsonl")
    for s in stories:
        if s["species_id"] if "species_id" in s else s["story_id"].startswith("FISH-R05-电鳗"):
            pass
    for s in stories:
        if s["story_id"].startswith("FISH-R05-电鳗"):
            resp = s["surfaces"]["Response"]
            resp["program_ids"] = ["P-EEL-RESP-SENSE", "P-EEL-RESP-FEEDING", "P-EEL-RESP-GUARD"]
            resp["reason"] += ("。FIX-001 补录（独立审 F-1）：S6 泡沫巢雄护=DUAL_PATH 第三成员"
                               "（intruder_evaluator_context=foam_nest）；S9 幼成切换=TYPED 族"
                               " evaluator_binding 第二 premise 实例；两程序为修复轮非盲补录"
                               "（registry_seen_at_creation=true，bias 声明见 provenance）")
            s["fix_round"] = {"id": FIX, "items": ["F-1"]}
        if s["story_id"].startswith("FISH-R05-湄公鲶"):
            s["surfaces"]["Response"]["reason"] += (
                "。FIX-001 补注（F-2）：ResponseChannel FieldFeeding（幼体肉食期）按 TYPED 族"
                " evaluator_channel/binding 轴 premise 实例处理；幼体程序证据不足不建体（TAR-02）")
            s["surfaces"]["Bake"]["reason"] += (
                "。FIX-001 补注（F-2）：potamodromous 洄游照 CHB 先例按 P05 配置级处理"
                "（因子集随 lifecycle premise 配置切换，细节少知不展开）")
            s["fix_round"] = {"id": FIX, "items": ["F-2"]}
    dump("stories.jsonl", stories)

    # --- F-1: program_revisions 留痕 ---
    revs = [
        {"program_id": "P-EEL-RESP-GUARD", "action": "ADDED_IN_FIX_ROUND",
         "revision_recorded": True, "round": FIX,
         "reason": "independent review CENSUS-B0-REV-001 F-1: EEL S6 foam-nest guard story coverage gap",
         "before": None, "after": "GUARD_CONFLICT_DUAL_PATH_RESPONSE third member (direct test pass)"},
        {"program_id": "P-EEL-RESP-FEEDING", "action": "ADDED_IN_FIX_ROUND",
         "revision_recorded": True, "round": FIX,
         "reason": "independent review CENSUS-B0-REV-001 F-1: EEL S9 ontogenetic diet switch coverage gap",
         "before": None, "after": "TYPED_TARGET_RESPONSE member (evaluator_binding second premise instance)"},
    ]
    dump("program_revisions.jsonl", revs)

    # --- F-1: discovery_curve B0 行更新（sketches 13→15, merge_confident 12→14） ---
    csv = (BATCH.parent.parent / "discovery_curve.csv").read_text(encoding="utf-8")
    csv = csv.replace("CENSUS-B0,5,13,12,2,5,1,0,3,2,0,0,0,0",
                      "CENSUS-B0,5,15,14,2,5,1,0,3,2,0,0,0,0")
    (BATCH.parent.parent / "discovery_curve.csv").write_text(csv, encoding="utf-8")
    print("FIX-001 applied: merge_tests +2, programs +2(+2 notes), stories EEL/MGC updated,")
    print("program_revisions 2, discovery_curve B0 row -> sketches=15 merge_confident=14")

if __name__ == "__main__":
    main()
