# FCF V1 Implementation Readiness Matrix

本矩阵用于完成性审计：设计项必须同时有权威 contract、reference evidence 和
独立 reviewer 结论，才可交给工程师实现。`APPROVE_WITH_MINOR` 表示没有
机制 blocker，但不替代 production adapter gate。

| 要求域 | 权威设计 | Reference evidence | 独立 review | 当前状态 |
|---|---|---|---|---|
| DSL 类型、namespace、revision、owner、随机边界 | `dsl_semantic_design.md`, `fcf_v1_engineering_spec.md` | `fcf_v1/dsl.py`, `schemas/fcf_v1.schema.json` | APPROVE | 设计闭合 |
| 温度 | `temperature_mechanism_design.md` | trace/owner 纸面 contract | APPROVE_WITH_MINOR（措辞已修正） | 设计闭合 |
| 溶解氧 | `dissolved_oxygen_mechanism_design.md` | resolver/trace contract | APPROVE | 设计闭合 |
| 环境因子组合 | `environment_factor_composition_design.md` | owner/profile contract | APPROVE_WITH_MINOR | 设计闭合 |
| 流速/流向 | `flow_mechanism_design.md` | vector/task/safety contract | APPROVE_WITH_MINOR | 设计闭合 |
| 光照/浑浊度 | `light_turbidity_mechanism_design.md` | actionability/trace contract | APPROVE | 设计闭合 |
| 深度/结构 | `depth_structure_mechanism_design.md` | geometry revision/gate contract | APPROVE | 设计闭合 |
| 资源/历史 | `resource_history_mechanism_design.md` | transaction/idempotency contract | APPROVE | 设计闭合 |
| Motive/BehaviorProgram | `motive_behavior_program_design.md` | deterministic enum/rule contract | APPROVE | 设计闭合 |
| Encounter Conversion | `encounter_conversion_mechanism_design.md` | COMMIT boundary contract | APPROVE_WITH_MINOR | 设计闭合 |
| Contact/Hook | `contact_hook_mechanism_design.md` | capacity/replay contract | APPROVE | 设计闭合 |
| Fish entity / Variant | `fish_entity_variant_design.md` | model/editor snapshot contract | APPROVE | 设计闭合 |
| Editor / authoring | `editor_contract.md`, `editor_interaction_design.md` | `fcf_v1/editor.py`, transactional tests | APPROVE | 设计闭合 |
| Candidate/ledger/conservation | `fcf_v1_engineering_spec.md` | `fcf_v1/engine.py`, `tests/test_fcf_v1.py` | checklist + review | reference 已验证 |
| Replay/concurrency/journal | `verification_report.md` | journal/conformance tests | checklist + review | reference 已验证 |
| Flagship traces | `flagship_traces.md` | three reference tests | review checklist | reference 已验证 |
| Production runtime/storage | `verification_report.md` handoff contract | 需要真实 factory/runtime | 尚无 production evidence | 外部 V1 gate |

## 完成判据

“设计与原型完成”不能仅由测试绿色推出。最终审计必须确认：

1. 每一行的 design contract、owner、revision、UNKNOWN 和失败路径明确；
2. reference tests 覆盖该行声明的 identity、conservation、replay 或并发性质；
3. reviewer 结论没有未处理的 blocker/semantic ambiguity；
4. production runtime/storage 的证据单独列为 V1 Freeze gate，不冒充已完成。
