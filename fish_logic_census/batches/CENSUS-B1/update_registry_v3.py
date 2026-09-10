# -*- coding: utf-8 -*-
"""CENSUS-B1 registry v2→v3 更新（脚本化 mutation，可审计）。"""
import io

P = "fish_logic_census/template_registry.yaml"
t = io.open(P, encoding="utf-8").read()

t = t.replace("""version: 2
mutation_provenance:
  batch: CENSUS-B0""", """version: 3
mutation_provenance:
  batch: CENSUS-B1
  date: 2026-09-10
  previous_version: 2
  b1_summary: "CRR known_non_matches +9（B1 全部 Bake 非 RelativeRank 形）；PLAIN+BRT / PATCH+ONS / TYPED+13 / DUAL+DIS；新立 SINGLE_FACTOR_NORMALIZED_WEIGHT（7 成员）与 CUE_GUIDED_APPROACH_AVOID（1 成员 PROVISIONAL+product_deferred）——HRQ-B1-01..05"

v2_provenance:
  batch: CENSUS-B0""")

t = t.replace("""    merge_candidate_status:""", """      - batch: CENSUS-B1
        program_id: [P-B1-GRB-BAKE, P-B1-BRT-BAKE, P-B1-DRU-BAKE, P-B1-COD-BAKE, P-B1-PAD34-BAKE, P-B1-BLU-BAKE, P-B1-SMA-BAKE, P-B1-LAM-BAKE, P-B1-ONS-BAKE]
        reason: B1 全部 9 个 Bake 程序非匹配（单因子/patch/梯度/因子组合形态，无 RelativeRank 结构）；CRR 本批仍无新成员（B1 选样无低温 refuge 类故事）
    merge_candidate_status:""")

t = t.replace("""      - {batch: CENSUS-B0, program_id: P-CHB-BAKE, blind_hash: 7a45a474788ede01}""",
"""      - {batch: CENSUS-B0, program_id: P-CHB-BAKE, blind_hash: 7a45a474788ede01}
      - {batch: CENSUS-B1, program_id: P-B1-BRT-BAKE, blind_hash: a871643093aeb6b4, note: "第 3 成员：patch+rank_position 2 槽；槽位数伸缩+rank 因子类型准入待 HRQ-B1-04"}""")

t = t.replace("""    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）]""",
"""    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）, HRQ-B1-04（槽位数伸缩+rank 因子类型）]""")

t = t.replace("""      - {batch: CENSUS-B0, program_id: P-MGC-BAKE-ADULT, blind_hash: 2b560452df77643f}
    known_non_matches: []
    provisional_note: 单成员 PROVISIONAL_CASE_SPECIFIC；与 P06 Compression Candidate（FR 线压回 P02 测试）联动，族稳定性待后续 P06 成员；helper 同为 PROVISIONAL 待第二跨 case 实例（resolver_tests.jsonl）""",
"""      - {batch: CENSUS-B0, program_id: P-MGC-BAKE-ADULT, blind_hash: 2b560452df77643f}
      - {batch: CENSUS-B1, program_id: P-B1-ONS-BAKE, blind_hash: 4e782a2e8b2440a4, note: "第 2 成员：context_type=current（急流石底绑定）；行为链 Evidence Open（confidence LOW）"}
    known_non_matches: []
    provisional_note: 双成员（湄公鲶成体 zone + 准白甲鱼 current）均 P06 域；PROVISIONAL 维持待 P06 压缩测试；context_type 轴（zone|current）待批；与 SINGLE 族的 optional_context 边界交 HRQ-B1-02；helper SubstrateResourcePatchEvaluator 同 PROVISIONAL""")

t = t.replace("""      - {batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-FEEDING, blind_hash: null, note: "修复轮非盲补录（EEL S9 幼成切换）：evaluator_binding 轴第二 premise 实例（首个=P-MGC-RESP-FEEDING）"}
    known_non_matches: []""",
"""      - {batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-FEEDING, blind_hash: null, note: "修复轮非盲补录（EEL S9 幼成切换）：evaluator_binding 轴第二 premise 实例（首个=P-MGC-RESP-FEEDING）"}
      - {batch: CENSUS-B1, program_id: [P-B1-GRB-RESP, P-B1-BRT-RESP, P-B1-TIL-RESP, P-B1-PAD35-RESP, P-B1-DRU-RESP, P-B1-COD-RESP, P-B1-PIK-RESP, P-B1-GAR-RESP, P-B1-BLU-RESP, P-B1-SMA-RESP, P-B1-RAI-RESP, P-B1-ONS-RESP], note: "12 标准成员（engine 无字面差异）；binding 新实例：TIL 口孵 cap / PAD35 cue_history 输入 / BLU 窄接受"}
      - {batch: CENSUS-B1, program_id: P-B1-PAD34-RESP-SENSE, blind_hash: 448a1b0d61629f96, note: "evaluator_channel 新实例 PASSIVE_ELECTROSENSE（被动电感受；对照 B0 电鳗 ACTIVE_ELECTROLOCATION）；产品电呈现契约未定（TAR-07）"}
    known_non_matches:
      - {batch: CENSUS-B1, template_id: CUE_GUIDED_APPROACH_AVOID, reason: evaluand=环境梯度场+RETURN=Approach|Avoid（真结构差异立新族）}""")

t = t.replace("""      - {batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-GUARD, blind_hash: null, note: "修复轮非盲补录（EEL S6 泡沫巢雄护）：第三成员，engine 直验与 canonical 无字面差异；intruder_evaluator_context=foam_nest"}""",
"""      - {batch: CENSUS-B0-FIX-001, program_id: P-EEL-RESP-GUARD, blind_hash: null, note: "修复轮非盲补录（EEL S6 泡沫巢雄护）：第三成员，engine 直验与 canonical 无字面差异；intruder_evaluator_context=foam_nest"}
      - {batch: CENSUS-B1, program_id: P-B1-DIS-RESP-GUARD, blind_hash: 585905b944bd66d6, note: "第 4 成员（七彩神仙育幼黏液喂养）：engine 无字面差异；fry_anchor=幼鱼群；色型不分裂（S12 对照不建体）"}""")

t = t.rstrip() + """
  - template_id: SINGLE_FACTOR_NORMALIZED_WEIGHT
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-B1
      seeded: 2026-09-10
      review_queue: HRQ-B1-01
    canonical_program_body: |
      EVAL_TYPED_FIELD_OR_FACTOR(typed 场/因子)
      -> NORMALIZE_WEIGHT
    ir_pointer: batches/CENSUS-B1/run_merge_tests.py::CANONICALS.SINGLE_FACTOR_NORMALIZED_WEIGHT
    allowed_parameter_axes:
      - factor_type(typed：resource_patch | habitat_factor(depth/layer/…) | chemical_gradient_field | …；轴宽度待 HRQ-B1-01)
      - factor_binding(随 lifecycle/season/sex premise 切换)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 多因子 combine（那是 PLAIN 域）, typed context 中间步（那是 PATCH 域）, gate（那是 HARD_GATED/CRR 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-B1, program_id: P-B1-GRB-BAKE, blind_hash: 7386b661fbf0c696}
      - {batch: CENSUS-B1, program_id: P-B1-DRU-BAKE, blind_hash: be9208df5d4b38aa}
      - {batch: CENSUS-B1, program_id: P-B1-PAD34-BAKE, blind_hash: 94902290bfe32ec4}
      - {batch: CENSUS-B1, program_id: P-B1-SMA-BAKE, blind_hash: 15cf1c61b86be3ad}
      - {batch: CENSUS-B1, program_id: P-B1-COD-BAKE, blind_hash: f78b761e75ef034f}
      - {batch: CENSUS-B1, program_id: P-B1-BLU-BAKE, blind_hash: 780566f2df78e5d7}
      - {batch: CENSUS-B1, program_id: P-B1-LAM-BAKE, blind_hash: dc12005c1ccc5a14, note: "最宽 factor_type 实例：chemical_gradient_field（非资源场）"}
    known_non_matches:
      - {batch: CENSUS-B1, template_id: PATCH_RESOURCE_FOLLOWING, reason: 缺 typed context 步（optional_context 边界 HRQ-B1-02）}
      - {batch: CENSUS-B1, template_id: CONSTRAINED_RELATIVE_REFUGE, reason: 无 RelativeRank 结构}
    open_precedents: [HRQ-B1-01（factor_type 轴宽度）, HRQ-B1-02（与 PATCH 的 optional_context 边界）]
  - template_id: CUE_GUIDED_APPROACH_AVOID
    surface: Response
    status: CANDIDATE
    provenance:
      batch: CENSUS-B1
      seeded: 2026-09-10
      review_queue: HRQ-B1-03
      related_precedent: "Semantic Review Context §10 环境场 evaluand 判例（Field Channel OPEN）；FR 线 Non-feeding cue-guided approach 组合 Semantic Open"
    canonical_program_body: |
      EVAL_AMBIENT_CUE_GRADIENT_TYPED(环境梯度场 evaluand，非离散目标)
      -> DECIDE_APPROACH_OR_AVOID
      -> Response(Approach | Avoid)
    ir_pointer: batches/CENSUS-B1/run_merge_tests.py::CANONICALS.CUE_GUIDED_APPROACH_AVOID
    allowed_parameter_axes:
      - cue_field_type(typed: pheromone | alarm | 其它具名化学/物理梯度)
      - direction(attract | avoid)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 离散目标 evaluand（那是 TYPED 族域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-B1, program_id: P-B1-LAM-RESP-APPROACH, blind_hash: e6963e25c39f0bd4}
    known_non_matches:
      - {batch: CENSUS-B1, template_id: TYPED_TARGET_RESPONSE, reason: "OPERATOR+RETURN 真差异（环境梯度场 evaluand + Approach|Avoid 返回 vs 离散目标 + TargetFeeding）"}
    provisional_note: 单成员 PROVISIONAL_CASE_SPECIFIC + product_deferred（TAR-06：产品不纳诱捕/化学趋向则候选冻结归档）
"""

io.open(P, "w", encoding="utf-8").write(t)

import yaml
reg = yaml.safe_load(io.open(P, encoding="utf-8"))
assert reg["version"] == 3, reg["version"]
ids = [x["template_id"] for x in reg["templates"]]
assert set(ids) == {"CONSTRAINED_RELATIVE_REFUGE", "PLAIN_FACTOR_COMBINE",
                    "HARD_GATED_FACTOR_COMBINE", "PATCH_RESOURCE_FOLLOWING",
                    "TYPED_TARGET_RESPONSE", "GUARD_CONFLICT_DUAL_PATH_RESPONSE",
                    "SINGLE_FACTOR_NORMALIZED_WEIGHT", "CUE_GUIDED_APPROACH_AVOID"}, ids
for x in reg["templates"]:
    assert "helper_dependencies" in x and "resolver_dependencies" in x, x["template_id"]
print("registry v3 OK: 8 templates, deps complete")
