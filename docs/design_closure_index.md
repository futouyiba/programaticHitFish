# FCF V1 Design Closure Index

这是一份设计导航，不替代各机制的详细 contract。阅读顺序应从事实与
identity 开始，再到解释、状态和终结结算。所有机制先完成语义闭合，才
进入 prototype/production implementation。

中文概念与链路入口：

- [fcf_v1_overview_cn.md](fcf_v1_overview_cn.md) — 概念、整体机制、配置示例、中文术语与主链路图示。
- [temperature_profile_configuration.md](temperature_profile_configuration.md) — 温度世界数据的完整字段表、YAML 示例、烘焙和查询输出。
- [Ogre Lake 使用说明](ogre_lake_visualization_user_guide.md) — 如何阅读逐层空间切块可视化。
- [Ogre Lake companion experiment](ogre_lake_manual_region_companion_experiment.md) — Manual Region 的作者成本证据；不参与主机制 promotion/reject。
- [RF4 Old Burg Lake estimate](rf4_old_burg_spatial_authoring_estimate.md) — 用公开地图与截图复测空间交叉切割；明确区分可见事实与 FCF 假设。
- [Ogre Lake reproducible overlay](ogre_lake_reproducible_overlay_experiment.md) — 以明确 Layer、状态向量与连通分量复算 2D Patch，并单独报告 3D Habitat Volume。

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

## 2. 机制 closure matrix

| 机制 | 详细设计 | 主要 owner | 当前 review |
|---|---|---|---|
| 温度 | `temperature_mechanism_design.md` | Occupancy / Conversion / Lifecycle-Safety（按不同 consequence） | APPROVE_WITH_MINOR |
| 溶解氧 | `dissolved_oxygen_mechanism_design.md` | Occupancy / Conversion / Safety | APPROVE |
| 流速/流向 | `flow_mechanism_design.md` | Occupancy / task-budget / Arrival / Safety | APPROVE_WITH_MINOR |
| 光照/浑浊度 | `light_turbidity_mechanism_design.md` | Perception / TaskCapability / Occupancy | APPROVE |
| 深度/结构 | `depth_structure_mechanism_design.md` | Spatial/Geometry / Occupancy / Arrival | APPROVE |
| 资源/历史 | `resource_history_mechanism_design.md` | History/Future、Motive、Settlement | APPROVE |
| Motive/Program | `motive_behavior_program_design.md` | deterministic motive resolver / Program | APPROVE |
| Encounter | `encounter_conversion_mechanism_design.md` | Encounter task / Commit boundary | APPROVE_WITH_MINOR |
| Contact/Hook | `contact_hook_mechanism_design.md` | Contact capacity / Hook compatibility | APPROVE |

`APPROVE_WITH_MINOR` 表示没有具体 V1 blocker，但保留 operational clarity
或 production-adapter follow-up；不表示可跳过设计 contract。

实体与编辑边界：

- [fish_entity_variant_design.md](fish_entity_variant_design.md) — Species capability、PopulationSlice、BehaviorProgram、Variant、Candidate、History 的统一契约。
- [editor_interaction_design.md](editor_interaction_design.md) — 字段控件、继承、变更分类、preview、review/publish 状态机与 migration。
- [implementation_readiness_matrix.md](implementation_readiness_matrix.md) — 设计、reference evidence、独立 review 与 production gate 的完成性矩阵。

## 3. 不可越过的 V1 边界

- World Fact 不携带 fish-specific interpretation；
- Species = capability，BehaviorProgram = current policy；
- 普通鱼默认为 exchangeable mass，不引入 persistent individual identity；
- 一个 physical consequence 只有一个 authoritative owner；
- Candidate 只能在 atomic reservation 后产生；
- Pending 不占 PSU、不运行 AI、不重掷 Entry；
- Motive 与 Encounter Conversion 默认确定性；
- 随机性只在明确声明的 Entry/Commit/Contact tie 边界；
- A/T/E 不是万能 bonus lane；
- 所有 replay identity 必须含 scope、semantic fingerprint 与相关 revision；
- 所有 terminal mutation 以唯一 transaction ID 幂等。

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

编辑器只编辑 schema、profile、policy、初值和 migration；不直接修改运行中
Candidate。Capability/scale change 必须触发 recalibration 与 reviewer sign-off。

## 5. 当前明确延期与外部必需 gate（两者不可混同）

V1.1/deferred（可延期）：

- 新增未声明 Species capability 或新 motive 类型；
- 更复杂生态、AI 行为或“更真实”的 bonus。

External V1 gate（不可延期，必须在 Freeze 前完成）：

- 在真实 production runtime/storage 上运行完整 fixture、replay、concurrency、
  property 套件；
- 最终 V1 Freeze promotion。

`APPROVE_WITH_MINOR` 只表示当前没有设计 blocker；相应 operational clarity
仍需落实。External gate 不是 V1.1 backlog，也不能由当前 reference oracle
自行宣称完成。production runtime 接入后，
必须按 [verification_report.md](verification_report.md) 的 handoff acceptance
contract 重新审查。

## 6. 设计完成判据

只有同时满足以下条件，某机制才可从 Design 进入实现：

1. 输入事实、snapshot 和 revision 有明确定义；
2. 输出字段、单位、边界和 UNKNOWN 行为有明确定义；
3. 每个 consequence 有唯一 owner；
4. 状态转换、失败路径、重放和并发语义唯一；
5. 至少一个 adversarial counterexample 已被推理驳回；
6. 独立 reviewer 给出 `APPROVE` 或 `APPROVE_WITH_MINOR`；
7. 没有把 V1.1 扩展偷偷引入当前 contract。
