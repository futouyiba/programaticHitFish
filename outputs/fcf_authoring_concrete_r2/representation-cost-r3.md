# Representation Cost Ledger R3｜同一修改的实际编辑量

**范围：** C03、C06、C08、C09、C12 的已冻结样本；基于 R2 的实际表列、行与中文脚本。这里统计的是“作者需要触碰的最小声明单元”，不是工程工时，也不是最终选型结论。

## 1. 计算口径

- **PT 单元**：一个 ProfilePoint 的一个数值或一个 Parameter value；如果 PT 不能表达所需语义，记为 `—`，并单独说明缺失的结构。
- **Table 行**：一个新增/修改的完整数据行；共享行只算一次。固定 TemplateStep 改动算一行，但它属于模板治理，不是普通鱼种调参。
- **Step Table 行**：一个有序步骤声明；只计算本绑定需要改变的步骤，Profile/Predicate 外表另列。
- **Narrow DSL 行**：一个连续声明行或条件行；共享参数改变只改 Profile/Parameter 表，不改脚本行。

## 2. 同一修改的单元级账本

| 修改 | PT | Table | Step Table | Narrow DSL | 真实语义影响 |
| --- | --- | --- | --- | --- | --- |
| C06 Defense 曲线 x=.5：y=.60→.65 | 1 个 CurvePoint 数值 | 1 行的 y 单元 | 0 行 | 0 行 | 只改 Profile；仍是 Defense-only |
| C03 高响应阈值 match=.7、drift=.6 | 2 个 Parameter value | 2 个 Parameter 行（已有 Predicate 行不变） | 0 行 | 0 行 | 只改条件数据；FIRST_MATCH 不变 |
| C03 新增 AND 条件 `water_flow≥.4` | `—`（PT 无条件树） | 1 Parameter + 1 Predicate + 1 PredicateMember = 3 行 | 1 条条件引用行 + 外部参数 | 1 条条件表达式行 + 1 Parameter | 不购买 Drift Mode；需白名单输入 |
| C08 MAX→平均 | `—`（PT 不承载聚合拓扑） | 1 TemplateStep 行 + 模板实现/验证 | 1 step 行 | 1 聚合声明行 | 改变固定聚合候选，触发模板治理 |
| C09 两 frame 共享一个 RootOccurrence | `—` | 0 新行；复用既有 Identity Contract | 0 新行；Scope 输入不变 | 0 必需行；注释可选 | 不创建 FieldOpportunity 或第二时钟 |
| C12 Migration 关闭普通 Feeding | `—`（PT 不能表达上游分群） | 1 Group Binding 行（若尚无） | 1 Group route 选择行 | 1 分群/调用声明行 | 上游分流；不写 Stage Selector |
| C08 增加第三个固定 Channel | 1 Profile（仅数值）但不足以完成 | 1 Slot + ProfilePoint 行组 + TemplateStep 行 | 至少1 read step + 1 merge 输入 | 至少2声明行 | 真正改变拓扑；需重新 Review |

`—` 不是“免费”：它表示 PT 只能继续保存数值，不能独立表达这个语义；作者必须转到 Table/Step Table/DSL 或固定 Runtime 合同。C03 的两个阈值虽然都可能是 PT 单元，但 `AND` 关系仍在 Predicate Table/DSL 中定义，不能被两个数值行隐式推出。

## 3. 绑定级总量（来自当前 R2 样本）

| 代表绑定 | 依赖的作者表 | 配置闭包行数 | 中文脚本行数（空行不计） | 主要差异 |
| --- | --- | ---: | ---: | --- |
| C03_R | Binding、Slot、Parameter、Predicate、Member、ResponseBand | 14 | 10 | Table 把 FIRST_MATCH、条件树和 Default 拆行；DSL 连续呈现 |
| C06_R | Binding、Slot、CurvePoint | 5 | 8 | 两边都只读 Defense；普通 Feeding 没有空占位 |
| C08_R | Binding、Slot、CurvePoint | 7 | 10 | 两个 Slot 同时存在；MAX 是固定步骤，不是 Selector |
| C09_R | Binding、Slot、CurvePoint | 10 | 13 | Opportunity 身份不在本闭包生成；FoodField 是输入 |
| C12_N + C12_M | 2 Binding、2×Slot、CurvePoint | 15 | 22（12+10） | 两个上游 Group 调用不同 Binding，不在单 Runtime 内切换 Stage |

行数用于观察可读性和引用分散程度，不表示 Table 行越少越好：固定模板目录、类型检查、冲突检查和回放 trace 仍然是共享工程成本。DSL 行越少也不表示它自动更简单，因为同一引用闭包和编译约束仍必须存在。

## 4. 三个读者场景的选择信息

**调参作者**只想把 C06 的 0.60 改成 0.65：PT 和 Table 都是一格，Step Table/DSL 不必动。**机制作者**要让 C03 多一个 AND：PT 无法独立完成，Table 需要三行 FK 结构，DSL 需要一条可读条件但仍要新增参数。**Runtime 作者**要把 C08 MAX 换平均：四种表达都不能靠普通 Profile 单元完成，必须改固定聚合步骤与验证。

这三个场景说明比较应按“参数、条件、拓扑”分层：参数差异不应被误报成 Template 差异；条件树差异不应被误报成 Runtime Order；Gate/合并/身份顺序变化才是真正的 Step/Template 变化。

## 5. 验证与边界

账本中的闭包行数由 R2 `tables.json` 的实际引用关系抽取；脚本行数由 `scripts.json` 去除空行后统计。C03 阈值与 R2 参数行一致：`match≥0.7`、`drift≥0.6`；C08 两固定 Channel 与 R2 的 `R_DUAL_FIXED` 一致；C09–C11 仍没有新 Opportunity 表；C12 没有 Stage Selector。本文不测量作者工时，不宣称 PT/Table/Step Table/DSL 任一方案已被正式选定，也不覆盖尚未 FR3 的候选 Story。
