# FCF V1 设计闭合索引（Design Closure Index）

这是一份设计导航，不替代各机制的详细契约（contract）。阅读顺序应从事实与
身份（identity）开始，再到解释、状态和终结结算。所有机制先完成语义闭合，才
进入原型/生产实现（prototype/production implementation）。

中文概念与链路入口：

- [fcf_v1_overview_cn.md](fcf_v1_overview_cn.md) — 概念、整体机制、配置示例、中文术语与主链路图示。
- [glossary_cn.md](glossary_cn.md) — 全仓库机制英文术语、中文主标签、定义与适用边界。
- [temperature_profile_configuration.md](temperature_profile_configuration.md) — 温度世界数据的完整字段表、YAML 示例、烘焙和查询输出。
- [scoped_review_protocol.md](scoped_review_protocol.md) — PATCH / ARTIFACT / MILESTONE 分级审核与禁止结论越权规则（试行）。
- [fcf_v0_document_governance.md](fcf_v0_document_governance.md) — Simplified V0 文档台账、重复/冲突/过时内容处置规则。
- [fcf_v0_conflict_register.md](fcf_v0_conflict_register.md) — V0 冲突登记与 V0→V1 差异（delta）分类。
- [response_scheme_1.md](response_scheme_1.md) — Simplified V0 Response 方案一提案（Pathway × FactorFit × MAX），Working，未 Promotion 为 Current Authority。
- [response_design_explained_cn.md](response_design_explained_cn.md) — 方案一的解释层讲解；公式与数值以方案一为准。
- [Ogre Lake 使用说明](ogre_lake_visualization_user_guide.md) — 如何阅读逐层空间切块可视化。
- [Ogre Lake companion experiment](archive/fcf_v0/ogre_lake_manual_region_companion_experiment.md) — 初版历史假设，已由可复核实验替代。
- [RF4 Old Burg Lake estimate](archive/fcf_v0/rf4_old_burg_spatial_authoring_estimate.md) — 历史外部证据，保留用于追溯，不作为当前测算入口。
- [Ogre Lake reproducible overlay](ogre_lake_reproducible_overlay_experiment.md) — 以明确的层（Layer）、状态向量与连通分量复算 2D Patch，并单独报告 3D 栖息体积（Habitat Volume）。
- [Ogre Lake complete HTML explainer](ogre-lake-spatial-authoring-explainer.html) — 面向评审与投屏的完整图文页面，包含逐层交互演示、RF4 参照和高层讲解脚本。

## 1. 总体因果图

```text
World Fact snapshots + Species capability + Slice policy + History snapshot
  → local semantic interpretations (each consequence has one owner)
  → Opportunity / finite Entry
  → atomic reservation
  → Candidate snapshot
  → Encounter Conversion
  → Commit
  → Contact arbitration
  → Hook compatibility
  → one Settlement transaction
  → END-CUT History delta
```

## 2. 机制闭合矩阵（closure matrix）

| 机制 | 详细设计 | 主要归属方（owner） | 当前审查（review） |
|---|---|---|---|
| 温度 | `temperature_mechanism_design.md` | 栖息占位（Occupancy）/ 转化（Conversion）/ 生命周期安全（Lifecycle-Safety），按不同后果（consequence） | APPROVE_WITH_MINOR |
| 溶解氧 | `dissolved_oxygen_mechanism_design.md` | 栖息占位 / 转化 / 安全（Safety） | APPROVE |
| 流速/流向 | `flow_mechanism_design.md` | 栖息占位 / 任务预算（task-budget）/ 到达（Arrival）/ 安全（Safety） | APPROVE_WITH_MINOR |
| 光照/浑浊度 | `light_turbidity_mechanism_design.md` | 感知（Perception）/ 任务能力（TaskCapability）/ 栖息占位 | APPROVE |
| 深度/结构 | `depth_structure_mechanism_design.md` | 空间/几何（Spatial/Geometry）/ 栖息占位 / 到达 | APPROVE |
| 资源/历史 | `resource_history_mechanism_design.md` | 历史/未来（History/Future）、动机（Motive）、终结结算（Settlement） | APPROVE |
| 动机/策略程序（Motive/Program） | `motive_behavior_program_design.md` | 确定性动机解析器（deterministic motive resolver）/ 策略程序（Program） | APPROVE |
| 遭遇（Encounter） | `encounter_conversion_mechanism_design.md` | 遭遇任务 / 承诺边界（Commit boundary） | APPROVE_WITH_MINOR |
| 接触/挂钩（Contact/Hook） | `contact_hook_mechanism_design.md` | 接触容量 / 挂钩兼容性 | APPROVE |

`APPROVE_WITH_MINOR` 表示没有具体 V1 阻塞项（blocker），但保留运营清晰性（operational clarity）
或生产适配器跟进（production-adapter follow-up）；不表示可跳过设计契约。

实体与编辑边界：

- [fish_entity_variant_design.md](fish_entity_variant_design.md) — 物种能力（Species capability）、种群切片（PopulationSlice）、行为策略程序（BehaviorProgram）、变体（Variant）、遭遇候选（Candidate）、历史（History）的统一契约。
- [editor_interaction_design.md](editor_interaction_design.md) — 字段控件、继承、变更分类、预览（preview）、审查/发布（review/publish）状态机与迁移（migration）。
- [implementation_readiness_matrix.md](implementation_readiness_matrix.md) — 设计、参考证据（reference evidence）、独立审查（review）与生产闸门（production gate）的完成性矩阵。

## 3. 不可越过的 V1 边界

- 世界事实（World Fact）不携带针对具体鱼的语义解释（fish-specific interpretation）；
- 物种（Species）= 能力（capability），行为策略程序（BehaviorProgram）= 当前策略（current policy）；
- 普通鱼默认为可交换质量（exchangeable mass），不引入持久个体身份（persistent individual identity）；
- 一个物理后果（physical consequence）只有一个权威归属方（authoritative owner）；
- 遭遇候选（Candidate）只能在原子保留（atomic reservation）后产生；
- Pending 不占 PSU、不运行 AI、不重掷进入（Entry）；
- 动机（Motive）与遭遇转化（Encounter Conversion）默认确定性；
- 随机性只在明确声明的进入/承诺判定/接触平局（Entry/Commit/Contact tie）边界；
- A/T/E 不是万能加成通道（bonus lane）；
- 所有重放身份（replay identity）必须含作用域（scope）、语义指纹（semantic fingerprint）与相关修订版本（revision）；
- 所有终态变更（terminal mutation）以唯一交易 ID（transaction ID）幂等。

## 4. 统一编辑器视图

任何环境或鱼类属性编辑，都必须能显示：

```text
input fact/state
→ derived interpretation
→ consequence_id
→ semantic owner
→ downstream stage
→ trace/revision
```

编辑器只编辑结构模式（schema）、剖面（profile）、策略（policy）、初值和迁移（migration）；不直接修改运行中
遭遇候选。能力/规模变更（Capability/scale change）必须触发重新校准（recalibration）与审查者签署（reviewer sign-off）。

## 5. 当前明确延期与外部必需 gate（两者不可混同）

V1.1/deferred（可延期）：

- 新增未声明物种能力（Species capability）或新动机（motive）类型；
- 更复杂生态、AI 行为或“更真实”的加成（bonus）。

External V1 gate（不可延期，必须在 Freeze 前完成）：

- 在真实生产运行时/存储上运行完整固定样例（fixture）、重放（replay）、并发（concurrency）、
  性质（property）套件；
- 最终 V1 Freeze 晋升（promotion）。

`APPROVE_WITH_MINOR` 只表示当前没有设计阻塞项（blocker）；相应运营清晰性
仍需落实。External gate 不是 V1.1 待办清单（backlog），也不能由当前参考预言机（reference oracle）
自行宣称完成。生产运行时接入后，
必须按 [verification_report.md](verification_report.md) 的移交验收契约（handoff acceptance
contract）重新审查。

## 6. 设计完成判据

只有同时满足以下条件，某机制才可从 Design 进入实现：

1. 输入事实、快照（snapshot）和修订版本（revision）有明确定义；
2. 输出字段、单位、边界和 UNKNOWN 行为有明确定义；
3. 每个后果（consequence）有唯一归属方（owner）；
4. 状态转换、失败路径、重放和并发语义唯一；
5. 至少一个对抗性反例（adversarial counterexample）已被推理驳回；
6. 独立审查者（reviewer）给出 `APPROVE` 或 `APPROVE_WITH_MINOR`；
7. 没有把 V1.1 扩展偷偷引入当前契约。
