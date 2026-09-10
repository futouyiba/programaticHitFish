# -*- coding: utf-8 -*-
"""CENSUS-B2 判同产物 + registry v3→v4 + discovery_curve（一体化脚本）。
R03 裁决（coordinator 2026-09-10）：MDF 可用，frozen_status_confirmed，
引注 FISH-R03-RECON-001 + FISH-MAINT-FIX-001。"""
import io
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[1]
HRQ = {"field": "HRQ-B2-01", "crr": "HRQ-B2-02", "members": "HRQ-B2-03"}
AXIS = "轴属立族/扩容提案（HRQ 待批）；engine raw diff 为槽名字面差异，骨架同构"
CRR_DIFFS = ["BRANCH", "COMBINE", "DEPENDENCY", "OPERATOR", "PREMISE"]
NO_RANK = "CRR 判别结构（FeasibleSet→RelativeRank(reference_set)）不存在：premise 绑定切换/因子组合形态"

SINGLE_N = {"P-B2-PIK19-BAKE": "位置因子（spawning_stage 绑定）", "P-B2-BRT12-BAKE": "季节脉冲猎物 patch",
            "P-B2-ARC-BAKE": "近岸↔深水位置因子（temp/season）", "P-B2-VEN-BAKE": "水层因子（temp/season）",
            "P-B2-FGA-BAKE": "植被结构栖息因子（静态）", "P-B2-SWO-BAKE": "昼夜垂直迁移水层因子（diel 绑定；2D 判据 open）",
            "P-B2-BHC-BAKE": "食物场浓度（food_field——场实例）", "P-B2-HER-BAKE": "浮游食场（food_field+群体 overlay）"}
TYPED_N = {"P-B2-PIK19-RESP": "标准", "P-B2-WAL-RESP": "标准", "P-B2-BRT12-RESP": "季节 context 参数",
           "P-B2-ARC-RESP": "入口条件较强参数", "P-B2-VEN-RESP": "浮游取向参数", "P-B2-FGA-RESP": "轮廓/停顿/结构 context",
           "P-B2-SWO-RESP": "水层匹配呈现参数", "P-B2-MDF-RESP": "motion-triggered 强实例（静止不触发/移动触发追捕）"}

M = []
for pid, note in SINGLE_N.items():
    M.append({"program_id": pid, "template_id": "SINGLE_FACTOR_NORMALIZED_WEIGHT",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": ["OPERATOR", "PREMISE"],
              "proposed_parameter_axis": "factor_type(typed: +habitat_factor(position/structure/…) +food_field)",
              "reasoning": f"骨架同构（单 typed 因子→归一化）；槽名字面在 factor_type 轴内。实例={note}。{AXIS}",
              "provenance": {"batch": "CENSUS-B2", "engine": "engine_report.json"}})
for pid, note in [("P-B2-WAL-BAKE", "温度+食物 2 因子"), ("P-B2-MDF-BAKE", "结构+深度(低温绑定) 2 因子")]:
    M.append({"program_id": pid, "template_id": "PLAIN_FACTOR_COMBINE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
              "structural_diffs": [], "engine_raw_diffs": ["DEPENDENCY", "OPERATOR", "PREMISE"],
              "proposed_parameter_axis": "factor_set(typed,bounded 2–6 槽)",
              "reasoning": f"第 {4 if pid=='P-B2-WAL-BAKE' else 5} 成员直验：2 因子+COMBINE_WEIGHTED 骨架同构，"
                           f"槽位数（2 vs canonical 4）在 factor_set 轴 2–6 内（HRQ-01/B1-04 链）。实例={note}。{AXIS}",
              "provenance": {"batch": "CENSUS-B2"}})
for pid, note in TYPED_N.items():
    M.append({"program_id": pid, "template_id": "TYPED_TARGET_RESPONSE",
              "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
              "structural_diffs": [], "engine_raw_diffs": ["PREMISE"] ,
              "reasoning": f"engine 仅 PREMISE（F02 不计）/或无差异。实例注记：{note}。",
              "provenance": {"batch": "CENSUS-B2"}})
M.append({"program_id": "P-B2-BHC-RESP-FIELD", "template_id": "FOOD_FIELD_FEEDING_RESPONSE",
          "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
          "structural_diffs": [], "engine_raw_diffs": ["PREMISE"],
          "reasoning": "canonical 源（鳙鱼滤食：场浓度驱动持续摄入，无离散目标 evaluator——"
                       "滤食与钩饵响应非同一机制，Story 明言）",
          "provenance": {"batch": "CENSUS-B2"}})
M.append({"program_id": "P-B2-HER-RESP-FIELD", "template_id": "FOOD_FIELD_FEEDING_RESPONSE",
          "verdict": "MERGE_CONFIDENT", "same": True, "param_only": True,
          "structural_diffs": [], "engine_raw_diffs": ["PREMISE"],
          "reasoning": "第 2 成员直验（鲱鱼浮游食场；engine 无字面差异）；产卵群≠摄食群",
          "provenance": {"batch": "CENSUS-B2"}})
M.append({"program_id": "P-B2-BHC-RESP-FIELD", "template_id": "TYPED_TARGET_RESPONSE",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
          "structural_diffs": ["OPERATOR", "PREMISE", "RETURN"], "engine_raw_diffs": ["OPERATOR", "PREMISE", "RETURN"],
          "reasoning": "B1-LAM 判例同型：evaluand=食物场（非离散目标）+RETURN=FieldFeeding（非 TargetFeeding）"
                       "——真结构差异立 FOOD_FIELD_FEEDING_RESPONSE 族（HRQ-B2-01）",
          "human_review_queued": HRQ["field"], "provenance": {"batch": "CENSUS-B2"}})
M.append({"program_id": "P-B2-HER-RESP-FIELD", "template_id": "CUE_GUIDED_APPROACH_AVOID",
          "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
          "structural_diffs": ["OPERATOR", "PREMISE", "RETURN"], "engine_raw_diffs": ["OPERATOR", "PREMISE", "RETURN"],
          "reasoning": "两个场族互为 non-match 确证：食物场摄入决策（DECIDE_FIELD_FEEDING）vs 化学梯度趋向"
                       "（DECIDE_APPROACH_OR_AVOID）——同为场 evaluand 但程序目的与 RETURN 不同，不得互并",
          "human_review_queued": HRQ["field"], "provenance": {"batch": "CENSUS-B2"}})
for pid in ["P-B2-PIK19-BAKE", "P-B2-WAL-BAKE", "P-B2-BRT12-BAKE", "P-B2-ARC-BAKE",
            "P-B2-VEN-BAKE", "P-B2-FGA-BAKE", "P-B2-SWO-BAKE", "P-B2-BHC-BAKE",
            "P-B2-HER-BAKE", "P-B2-MDF-BAKE"]:
    M.append({"program_id": pid, "template_id": "CONSTRAINED_RELATIVE_REFUGE",
              "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
              "structural_diffs": CRR_DIFFS, "engine_raw_diffs": CRR_DIFFS,
              "reasoning": NO_RANK + "。归 SINGLE/PLAIN 候选族。CRR 本批仍零成员（结构性原因见 HRQ-B2-02）。",
              "human_review_queued": HRQ["members"], "provenance": {"batch": "CENSUS-B2"}})

FAMILY_OF = {}
for pid in SINGLE_N: FAMILY_OF[pid] = ("SINGLE_FACTOR_NORMALIZED_WEIGHT", HRQ["members"])
for pid in ["P-B2-WAL-BAKE", "P-B2-MDF-BAKE"]: FAMILY_OF[pid] = ("PLAIN_FACTOR_COMBINE", HRQ["members"])
for pid in TYPED_N: FAMILY_OF[pid] = ("TYPED_TARGET_RESPONSE", HRQ["members"])
for pid in ["P-B2-BHC-RESP-FIELD", "P-B2-HER-RESP-FIELD"]: FAMILY_OF[pid] = ("FOOD_FIELD_FEEDING_RESPONSE", HRQ["field"])

def main():
    # merge_tests
    (BATCH / "merge_tests.jsonl").write_text(
        "\n".join(json.dumps(m, ensure_ascii=False) for m in M) + "\n", encoding="utf-8")
    # programs（含 MDF 状态澄清）
    blind = [json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    out = []
    for p in blind:
        fam, ref = FAMILY_OF[p["program_id"]]
        rec = {"program_id": p["program_id"], "story_id": p["story_id"],
               "species_id": p["species_id"], "surface": p["surface"],
               "consequence": "NEW_PROGRAM_CANDIDATE", "family_membership": fam,
               "review_ref": ref, "blind_hash": p["blind_hash"],
               "original_program_body_unchanged": True,
               "registry_seen_at_creation": False, "post_registry_mutations": [],
               "provenance": {"batch": "CENSUS-B2"}}
        if p["program_id"].startswith("P-B2-MDF"):
            rec["input_status"] = {
                "frozen_status": "confirmed",
                "adjudication": "coordinator 2026-09-10：R03 最终 FR2=ARTIFACT_APPROVE（四轮链 03:01→03:39Z）+FR3 AUTO_CONTINUE 完成；FISH-R03-RECON-001 确认终审真实；DB 属性 Independent PASS 为权威（正文 REVISE 为历史残留，转 researcher 队列清理）",
                "references": ["FISH-R03-RECON-001", "FISH-MAINT-FIX-001"],
                "blind_note": "blind_programs.jsonl 冻结时标 disputed（hash 内）；本澄清记录于 program_revisions.jsonl"}
        out.append(rec)
    (BATCH / "programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in out) + "\n", encoding="utf-8")
    # revisions（状态澄清留痕，body 未动）
    (BATCH / "program_revisions.jsonl").write_text(json.dumps({
        "program_id": "P-B2-MDF-BAKE/P-B2-MDF-RESP", "action": "STATUS_FIELD_CLARIFIED",
        "revision_recorded": True, "round": "CENSUS-B2（判同段）",
        "reason": "input_status: frozen_status_disputed -> confirmed（coordinator adjudication；blind hash 未变，仅状态标注澄清）",
        "before": "disputed（页属性 PASS vs 正文 REVISE 矛盾）",
        "after": "confirmed（FISH-R03-RECON-001 + FISH-MAINT-FIX-001）"}, ensure_ascii=False) + "\n", encoding="utf-8")
    (BATCH / "resolver_tests.jsonl").write_text(json.dumps({
        "resolver_id": "NO_NEW_RESOLVER_FAMILY",
        "note": "B2 未新增 resolver family；food_field 浓度场/猎物脉冲/季节水温均为世界侧事实供给义务（上游 SNAP 登记同 B1）；opportunity lifecycle/dedup 压力记 HRQ-B2-01（P03 Notes 同源）",
        "provenance": {"batch": "CENSUS-B2"}}, ensure_ascii=False) + "\n", encoding="utf-8")
    (BATCH / "absence_claims.jsonl").write_text("", encoding="utf-8")
    (BATCH / "coverage.jsonl").write_text("", encoding="utf-8")
    # registry v3 -> v4
    p = ROOT / "template_registry.yaml"
    t = io.open(p, encoding="utf-8").read()
    t = t.replace("""version: 3
mutation_provenance:
  batch: CENSUS-B1""", """version: 4
mutation_provenance:
  batch: CENSUS-B2
  date: 2026-09-10
  previous_version: 3
  b2_summary: "CRR +10 non-match 仍 0 成员（HRQ-B2-02 输入通道问题）；SINGLE +8（15 成员，factor_type 轴 +food_field）；PLAIN +2（5）；TYPED +8（27）；新立 FOOD_FIELD_FEEDING_RESPONSE（2 成员）——ΔL_bake=0 / ΔL_response=+1；MDF（R03）frozen_status_confirmed（RECON-001）"

v3_provenance:
  batch: CENSUS-B1""")
    t = t.replace("""        reason: B1 全部 9 个 Bake 程序非匹配（单因子/patch/梯度/因子组合形态，无 RelativeRank 结构）；CRR 本批仍无新成员（B1 选样无低温 refuge 类故事）""",
"""        reason: B1 全部 9 个 Bake 程序非匹配（单因子/patch/梯度/因子组合形态，无 RelativeRank 结构）；CRR 本批仍无新成员（B1 选样无低温 refuge 类故事）
      - batch: CENSUS-B2
        program_id: [P-B2-PIK19-BAKE, P-B2-WAL-BAKE, P-B2-BRT12-BAKE, P-B2-ARC-BAKE, P-B2-VEN-BAKE, P-B2-FGA-BAKE, P-B2-SWO-BAKE, P-B2-BHC-BAKE, P-B2-HER-BAKE, P-B2-MDF-BAKE]
        reason: B2 thermal/季节/场类 10 程序全部非匹配（premise 绑定切换/因子组合形态）；CRR 真首考的结构性输入问题转 HRQ-B2-02（人类裁决）""")
    t = t.replace("""      - {batch: CENSUS-B1, program_id: P-B1-BRT-BAKE, blind_hash: a871643093aeb6b4, note: "第 3 成员：patch+rank_position 2 槽；槽位数伸缩+rank 因子类型准入待 HRQ-B1-04"}""",
"""      - {batch: CENSUS-B1, program_id: P-B1-BRT-BAKE, blind_hash: a871643093aeb6b4, note: "第 3 成员：patch+rank_position 2 槽；槽位数伸缩+rank 因子类型准入待 HRQ-B1-04"}
      - {batch: CENSUS-B2, program_id: P-B2-WAL-BAKE, blind_hash: 41c2972d04f4dfae, note: "第 4 成员：温度+食物 2 因子"}
      - {batch: CENSUS-B2, program_id: P-B2-MDF-BAKE, blind_hash: 12d75c2a13f7b08e, note: "第 5 成员：结构+深度(低温绑定)；R03 frozen_status_confirmed（FISH-R03-RECON-001）"}""")
    t = t.replace("""      - {batch: CENSUS-B1, program_id: P-B1-LAM-BAKE, blind_hash: dc12005c1ccc5a14, note: "最宽 factor_type 实例：chemical_gradient_field（非资源场）"}""",
"""      - {batch: CENSUS-B1, program_id: P-B1-LAM-BAKE, blind_hash: dc12005c1ccc5a14, note: "最宽 factor_type 实例：chemical_gradient_field（非资源场）"}
      - {batch: CENSUS-B2, program_id: [P-B2-PIK19-BAKE, P-B2-BRT12-BAKE, P-B2-ARC-BAKE, P-B2-VEN-BAKE, P-B2-FGA-BAKE, P-B2-SWO-BAKE], blind_hash: "见 blind_programs.jsonl", note: "habitat/resource 因子 6 例（position/patch/layer/structure/diel-layer）"}
      - {batch: CENSUS-B2, program_id: [P-B2-BHC-BAKE, P-B2-HER-BAKE], note: "factor_type 轴 +food_field（场实例第 2/3 个，继 LAM chemical_gradient）"}""")
    t = t.replace("""      - {batch: CENSUS-B1, program_id: P-B1-PAD34-RESP-SENSE, blind_hash: 448a1b0d61629f96, note: "evaluator_channel 新实例 PASSIVE_ELECTROSENSE（被动电感受；对照 B0 电鳗 ACTIVE_ELECTROLOCATION）；产品电呈现契约未定（TAR-07）"}""",
"""      - {batch: CENSUS-B1, program_id: P-B1-PAD34-RESP-SENSE, blind_hash: 448a1b0d61629f96, note: "evaluator_channel 新实例 PASSIVE_ELECTROSENSE（被动电感受；对照 B0 电鳗 ACTIVE_ELECTROLOCATION）；产品电呈现契约未定（TAR-07）"}
      - {batch: CENSUS-B2, program_id: [P-B2-PIK19-RESP, P-B2-WAL-RESP, P-B2-BRT12-RESP, P-B2-ARC-RESP, P-B2-VEN-RESP, P-B2-FGA-RESP, P-B2-SWO-RESP, P-B2-MDF-RESP], note: "8 标准成员（MDF=motion-triggered 强实例：静止不触发/移动触发追捕）"}""")
    t = t.rstrip() + """
  - template_id: FOOD_FIELD_FEEDING_RESPONSE
    surface: Response
    status: CANDIDATE
    provenance:
      batch: CENSUS-B2
      seeded: 2026-09-10
      review_queue: HRQ-B2-01
      semantic_pattern_correspondence: P03（Food Field → FieldFeeding / Field Opportunity，New Candidate；两层登记待 review）
    canonical_program_body: |
      EVAL_FOOD_FIELD_INTAKE(食物场浓度 evaluand，非离散目标)
      -> DECIDE_FIELD_FEEDING
      -> Response(FieldFeeding)
    ir_pointer: batches/CENSUS-B2/run_merge_tests.py::CANONICALS.FOOD_FIELD_FEEDING_RESPONSE
    allowed_parameter_axes:
      - field_type(typed: plankton_field | 其它具名食物场)
      - intake_semantics(持续滤食 | 脉冲摄入)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 离散目标 evaluand（那是 TYPED 族域）, 趋向/避让决策（那是 CUE_GUIDED 族域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-B2, program_id: P-B2-BHC-RESP-FIELD, blind_hash: 8f3c897d68152a74, role: canonical_source}
      - {batch: CENSUS-B2, program_id: P-B2-HER-RESP-FIELD, blind_hash: 9d8f33094b9b4afe}
    known_non_matches:
      - {batch: CENSUS-B2, template_id: TYPED_TARGET_RESPONSE, reason: "evaluand=食物场+RETURN=FieldFeeding（B1-LAM 判例同型真差异）"}
      - {batch: CENSUS-B2, template_id: CUE_GUIDED_APPROACH_AVOID, reason: "同为场 evaluand 但程序目的（摄入 vs 趋向/避让）与 RETURN 不同"}
    open_precedents: [HRQ-B2-01（opportunity identity/lifetime/dedup 压力——P03 Notes 同源；产品捕获方式 TAR-09）]
    provisional_note: 双成员；P03 语义层为 New Candidate——census 族独立性不自动 promote Grammar
"""
    io.open(p, "w", encoding="utf-8").write(t)
    import yaml
    reg = yaml.safe_load(io.open(p, encoding="utf-8"))
    assert reg["version"] == 4 and len(reg["templates"]) == 9, (reg["version"], len(reg["templates"]))
    counts = {x["template_id"]: len(x["known_instances"]) for x in reg["templates"]}
    print("registry v4:", counts)
    # discovery curve
    c = ROOT / "discovery_curve.csv"
    t = io.open(c, encoding="utf-8").read().rstrip() + "\nCENSUS-B2,10,20,20,0,1,0,0,0,1,0,0,0,0\n"
    io.open(c, "w", encoding="utf-8").write(t)
    print(f"merge_tests={len(M)} programs={len(out)}")

if __name__ == "__main__":
    main()
