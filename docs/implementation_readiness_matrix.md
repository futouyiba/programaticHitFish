# FCF V1 实现就绪矩阵（Implementation Readiness Matrix）

本矩阵用于完成性审计：设计项必须同时有权威契约（contract）、参考证据（reference evidence）和
独立审查者（reviewer）结论，才可交给工程师实现。`APPROVE_WITH_MINOR` 表示没有
机制级阻塞项（blocker），但不替代生产适配器闸门（production adapter gate）。

| 要求域 | 权威设计 | 参考证据（Reference evidence） | 独立审查（review） | 当前状态 |
|---|---|---|---|---|
| DSL 类型、命名空间（namespace）、修订版本（revision）、归属方（owner）、随机边界 | `dsl_semantic_design.md`, `fcf_v1_engineering_spec.md` | `fcf_v1/dsl.py`, `schemas/fcf_v1.schema.json` | APPROVE | 设计闭合 |
| 温度 | `temperature_mechanism_design.md` | 追踪样例/归属方纸面契约 | APPROVE_WITH_MINOR（措辞已修正） | 设计闭合 |
| 溶解氧 | `dissolved_oxygen_mechanism_design.md` | 解析器/追踪样例契约 | APPROVE | 设计闭合 |
| 环境因子组合 | `environment_factor_composition_design.md` | 归属方/剖面契约 | APPROVE_WITH_MINOR | 设计闭合 |
| 流速/流向 | `flow_mechanism_design.md` | 矢量/任务/安全契约 | APPROVE_WITH_MINOR | 设计闭合 |
| 光照/浑浊度 | `light_turbidity_mechanism_design.md` | 可执行性/追踪样例契约 | APPROVE | 设计闭合 |
| 深度/结构 | `depth_structure_mechanism_design.md` | 几何修订版本/闸门契约 | APPROVE | 设计闭合 |
| 资源/历史 | `resource_history_mechanism_design.md` | 交易/幂等性契约 | APPROVE | 设计闭合 |
| 动机/行为策略程序（Motive/BehaviorProgram） | `motive_behavior_program_design.md` | 确定性枚举/规则契约 | APPROVE | 设计闭合 |
| 遭遇转化（Encounter Conversion） | `encounter_conversion_mechanism_design.md` | COMMIT 边界契约 | APPROVE_WITH_MINOR | 设计闭合 |
| 接触/挂钩（Contact/Hook） | `contact_hook_mechanism_design.md` | 容量/重放契约 | APPROVE | 设计闭合 |
| 鱼实体/变体（Fish entity / Variant） | `fish_entity_variant_design.md` | 模型/编辑器快照契约 | APPROVE | 设计闭合 |
| 编辑器/配置编写（Editor / authoring） | `editor_contract.md`, `editor_interaction_design.md` | `fcf_v1/editor.py`，事务性测试 | APPROVE | 设计闭合 |
| 遭遇候选/账本/守恒（Candidate/ledger/conservation） | `fcf_v1_engineering_spec.md` | `fcf_v1/engine.py`, `tests/test_fcf_v1.py` | checklist + review | 参考实现已验证 |
| 重放/并发/日志（Replay/concurrency/journal） | `verification_report.md` | 日志/一致性测试 | checklist + review | 参考实现已验证 |
| 旗舰追踪样例（Flagship traces） | `flagship_traces.md` | 三个参考测试 | review checklist | 参考实现已验证 |
| 生产运行时/存储（Production runtime/storage） | `verification_report.md` 移交契约 | 需要真实 factory/runtime | 尚无生产证据（production evidence） | 外部 V1 闸门（gate） |

## 完成判据

“设计与原型完成”不能仅由测试绿色推出。最终审计必须确认：

1. 每一行的设计契约（design contract）、归属方、修订版本、UNKNOWN 和失败路径明确；
2. 参考测试覆盖该行声明的身份（identity）、守恒（conservation）、重放（replay）或并发性质；
3. 审查者结论没有未处理的阻塞项/语义歧义（blocker/semantic ambiguity）；
4. 生产运行时/存储的证据单独列为 V1 冻结闸门（Freeze gate），不冒充已完成。
