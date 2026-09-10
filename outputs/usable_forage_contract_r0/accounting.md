# 复杂度记账｜UsableForageAvailability 表达 R1

`Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED`

- 批次：FORAGE-CONTRACT-REP-001（B2 REPRESENTATION_REVIEW_RUNNING，R1 修复轮；FORAGE-CONTRACT-REV-001 F4 处置增量）
- 记账对象：`config/usable_forage.config.json`（Config 主路径表达，schema `usable_forage.config.r1`）+ `dsl/usable_forage.dsl.txt`（对照，NOT ADMITTED）
- 输入来源：Design Owner 经 Coordinator 批准的契约边界（handoff 原文）；KNIFE-READ-001 §15.6 / §15.2 / §15.7 / §16（live 读取归档版 2026-09-10T03:49:56Z，本批未 re-fetch）
- 数值示例为占位，不冻结（与 Knife「不冻结数值，只冻结 Representation Boundary」一致）

## 1. §15.6 指标逐项

| 指标 | 本契约增量 | 说明 |
|---|---|---|
| N_2D_Profile_Bindings | +0 | 契约内无任何 2D Profile 绑定。 |
| N_Unique_Axis_Pair_Families | +0 | 同上。 |
| 2D_Profile_ControlPoint_Volume | +0 | 同上。 |
| N_Fixed_Composite_Slot_Kinds | +0 | 未引入任何 composite slot。`FILTERED_SUM` 是契约内部的固定聚合常量（`author_selectable=false`），不是作者可配的 slot kind。 |
| N_Distinct_Dependency_Graphs | **1**（不 >1） | 全契约唯一依赖图：`Resolved Snapshot → 食性过滤 → 口径过滤 → 固定求和 → usable_forage_availability`。所有 population 共用同一图，只有数据行不同（diet 列表、size 窗、代表尺寸）。 |

### 为什么不需要 2D Profile（对应 Knife §16.5 Pairwise Breaker 判据）

diet eligibility × size eligibility 是两个**互相独立**的静态谓词的合取（AND），完全可分离——不存在「一个过滤的方向随另一个过滤的取值系统性反转」的非分离交互。且 diet / size 是 population 的静态属性，不是 cell 环境轴；2D Response Surface 的形状（物种对双环境轴的响应面）与本内容不匹配。按 §16.5 判据，这不构成 2D Profile 证据，连 P1 都不需要，落在 P0 事实表达层。

## 2. 新增表 / 绑定 / 控制点

| 项 | 数量 | 性质 |
|---|---|---|
| 新增数据表 | 2（prey field 绑定表；population eligibility 表） | 纯数据行，无计算结构、无新表「种类」语义（就是绑定表 + 过滤条件表） |
| 新增快照绑定 | N_prey_classes 条（示例 4 条：fish / crayfish / insect_larvae / zooplankton） | 引用，非逻辑；每条强制 `resolved_snapshot.` 前缀（validator SNAP 检查） |
| 作者可编辑逻辑控制点 | **0** | 作者能改的只有数据值（diet 列表、size 窗、代表尺寸、绑定键）；聚合算子与依赖形状是常量（validator COMBINE / TOP 检查） |
| 新增输出事实 | 1：`usable_forage_availability` @ grain population × cell | 见 §3 诚实成本 |

## 2b. 输入侧义务（对上游 Snapshot 的字段量要求；R1 / F4 新增）

本契约不是免费的：它在输入侧对上游 Resolved Snapshot 施加明确的**字段量义务**——

- **量**：契约声明 N_prey_classes 条 prey field 绑定（本示例实例 4 条：fish / crayfish / insect_larvae / zooplankton），上游 Snapshot 必须在**每个 cell** 为每条绑定提供独立的原始 prey 生物量字段 ⇒ 字段量义务 = **N_prey_classes × N_cells**（示例实例即 4 × N_cells），随 prey 分类粒度与格子数线性增长。
- **口径**：这些字段必须是**原始生物量口径**（机器可读声明 `contract.prey_field_semantics = "raw_biomass_uncorrected"`）。上游若提供的是修正口径（perceived / visible / adjusted / corrected 族键），validator SNAP 检查族直接 fail——上游的义务是交原始值，修正是其它 owner 的结算内容。
- **含义**：收紧 prey 分类粒度（更大的 N_prey_classes）不只放大本契约自己的绑定表，还把等比例的字段量义务转嫁给 Snapshot 生产侧；本记账把这个外部性显式化，不隐藏在「读一下快照」的措辞后面。

## 3. L_bake 影响

1. **不新增 Logic Signature**（**external gate，本批未闭合**：该结论依赖 §15.7 边界页——page id `3d6a4137d23681049e3dc602d9e784c4`——对「什么算新增 Logic Signature」的边界主张；该页在本批输入中未展开（仅经 KNIFE-READ-001 转述获得），主张本身待后续批次裁决，本条不预支该裁决）。在假设该主张成立的前提下：本契约不改变控制拓扑、不改既有 IO 契约形状（只声明式地新增一个事实）、不引入作者可见中间依赖 → Forage 仍是 §16.7 最小句型里的 **unary 因子**（`lookup(usable_forage, @ForageProfile)`），与本事实契约解耦。
2. **不推高 L_bake**：契约完全落在声明式 Config 主路径内，未购买 Template / composite slot / DSL 任何一项结构。
3. **诚实成本（不隐藏）**：因为 eligibility 是 per-population 的，`usable_forage_availability` 不能做成 population 中立的单一标量场——Bake 输出面按 **O(N_populations × N_cells)** 增长。这是本契约真实的输出记账成本，随种群数线性增长。

## 4. 复杂度迁移自检（§15.6 的立法意图）

 Knife 攻击的假简化是「L_bake 变小但复杂度迁移成大量独特 2D Surface / case-specific Resolver / 隐蔽 slot 词汇表」。逐项自检：

- 无 case-specific Resolver 引入（契约内没有任何 Resolver 调用）；
- 无隐蔽 slot 词汇表（没有新增任何 slot kind，`AlternativeSupportSlot` 类构件为零）；
- 无 operator 词汇表（作者侧零算子可选）；
- 复杂度全部留在**数据表**里——这正是该刀期望的位置。

结论：无复杂度迁移迹象。

## 5. DSL 对照的 L_observed

见 `dsl/usable_forage.dsl.txt` §L_observed：同一契约 DSL 表达长度 ≈ Config，且 DSL 买进的自由度（可换算子、可嵌套、可按实例改写算子树）恰是本契约要拒绝的。本契约不构成 Expression Gate 正证据；Config 主路径表达占优。

## 6. 验证状态

- 结构 + 边界守卫：PASS（R1 重跑；命令与输出原样记录于 `README.md` §5；守卫自测 66 用例全触发——含 25 条英文词干、18 条中文关键词逐条 probe，及行级键白名单 / SNAP 事实族 allowlist / 空 diet_classes 正例）。
- 本记账为表达成本核算，**不是**机制 promotion，**不是** Freeze，不构成对 Knife 页任何 Verdict 的覆盖；§3.1 的「不新增 Logic Signature」为 external gate，待后续批次裁决（见该条标注）。
