# 复杂度记账｜呈现 Cue 轴模态扩充表达 R1

`Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED`

- 批次：REP-CUE-AXIS-001（B0 REPRESENTATION_RUNNING 首轮）
- 记账对象：`config/cue_axis.config.json`（Config 主路径表达，schema `cue_axis.config.r1`）+ `dsl/cue_axis.dsl.txt`（对照，NOT ADMITTED）
- 输入来源：立项规格 REP-COVERAGE-DELTA-001 report §2.3（K8 列级规格）；FR3 前提闭合 CD-R05-01（FISH-R05-FR3-001R）；结构参照 live 主页转录（REP-CLARITY-FIX-001 后版本）§17.2/§17.3/§5.1；机制约束 KNIFE-READ-001 §11 / §15.6 / §16.5 / §16.7（归档版 2026-09-10T03:49:56Z，本批未 re-fetch）
- 数值示例为占位，不最终定值（与 Knife「不定死数值，只定死 Representation Boundary」一致——措辞避开守卫词干，见 README §5 注记）

## 1. §15.6 指标逐项

| 指标 | 本批增量 | 说明 |
|---|---|---|
| N_2D_Profile_Bindings | +0 | 两轴均为 P0 阶 Unary Profile lookup，无任何 2D 绑定（validator AXIS 检查族强制 arity=unary、拒绝第二轴键形态）。 |
| N_Unique_Axis_Pair_Families | +0 | 同上；scent×水流、electro×传导不构成本批的轴对（归感知/环境 Resolver owner）。 |
| 2D_Profile_ControlPoint_Volume | +0 | 同上。 |
| N_Fixed_Composite_Slot_Kinds | +0 | 未引入任何 composite slot。两个 Profile 槽位是 §17.2 既有 Reaction Profile 表的普通行（同款两列结构加两行），不是新构件种类；合并复用既有 RR-T1 通道 FIXED_COMBINE，不新增合并结构。 |
| N_Distinct_Dependency_Graphs | **+0（新增图种类）** | 两轴不产生新依赖图拓扑：每轴 = 「呈现侧计算事实 → unary Profile lookup → Fit」一条平行叶子，挂在**既有** RR-T1 通道依赖图（呈现/饵/姿态事实 → @FeedingProfile → … → FIXED_COMBINE → FinalResponse）上，图形状不变。新增的是叶子**实例** 2 条，不是图**种类**。 |

### 为什么不需要 2D Profile（Knife §16.5 / §10.3 判据对照）

- §16.5 Pairwise Breaker 判据是**不可分离交互**（一个因素的效果随另一因素取值系统性反转 / 最优区间迁移）。scent×水流、electro×水体传导是**输运/传导物理计算**，不是「物种对双环境轴的响应面」——规格明文该耦合归感知/环境 Resolver owner。
- §10.3（Light × Turbidity 反例）已裁定：2D Profile 用于「Species/Group 真正需要配置的双变量 Response Surface」，不用于替代本应由稳定 Resolver 负责的物理/感知计算。本批两轴按 Primitive Admission Ladder 落 **P0**（Knife §11），P1（typed 2D）都不需要。
- 除非未来出现 §16.5 型不可分离样本（如「味型强度的最优响应区间随流速系统性迁移」且有物种级证据），否则不开 2D——该重开条件与规格 §2.3(2) 一致。

## 2. 新增槽位 / 事实 / 表 / 控制点

| 项 | 数量 | 性质 |
|---|---|---|
| 新增 Profile 槽位 | **2**（@ScentCueProfile、@ElectroFieldProfile） | §17.2 Reaction Profile 表同款两列结构加两行；纯数据槽位（数值面为 per-population 实例），无计算结构 |
| 新增事实枚举值 | **2**（BaitScentIntensity、LureElectricField） | Grammar 5.1 条件原子「事实/计算项」枚举扩充，V2/V3 形态复用，**零新列**（validator FACT 检查族强制 columns_added=0） |
| 新增表 | 0 | 槽位挂 §17.2 既有表加行；事实挂 Grammar 5.1 既有枚举列；不新增任何表 |
| 新增通道 / 模板 | 0 | 并入既有 RR-T1 Feeding/Reaction 通道 FIXED_COMBINE；RR 模板计数不变（不推翻 §17.5 压缩结论） |
| 新增中间输出 | 2 个 Fit（ScentCueFit、ElectroFieldCueFit） | 通道并列输入；**不是**新依赖图、不是作者可编辑中间依赖（合并拓扑与算子钉死） |
| 作者可编辑逻辑控制点 | **0** | 作者能改的只有：Profile 数值表（示例 lookup table）、实例绑定（population × slot × profile instance）、RuleSet 条件行引用两条新事实（V2/V3 既有列内）；算子 / 顺序 / 嵌套 / 通道拓扑全部常量（validator TOP / AXIS / COMBINE 检查族） |

## 2b. 输入侧义务（对上游呈现侧的要求）

- **量**：上游呈现侧必须为每条呈现状态产出 2 条计算事实（BaitScentIntensity、LureElectricField 各 1）⇒ 字段量义务 = **2 × N_presentations**。本批只声明枚举名与口径语义（上游呈现侧计算事实），**不定义取值域与档位**——那是呈现侧 Resolver 的产出契约，不在本批输入内。
- **边界**：输运（气味×水流）、传导衰减（电场×水体）的计算义务在感知/环境 Resolver owner，不因本轴设立而转移到 Response 面；本轴消费的是**已计算好的呈现侧强度/特征事实**。
- **含义**：将来若呈现侧把「修正后的可感知强度」（例如按水体传导衰减折算后的电场特征）作为事实口径交付，属于上游口径变化，应走上游事实族登记（类比 forage 契约 R1 README §6 的 SNAP allowlist 收窄义务），不在本轴配置内自行折算。

## 3. L_response 影响

1. **不新增 Response 模板数量**：RR-T1/T2/T3 计数不变；两个新轴只给既有通道加两个并列 Fit 输入，不新增 Channel、不新增汇总结构（§17.5「Reaction 的发现降低 template fragmentation」的结论不被本批推翻）。
2. **不推高 L_response**：无新控制拓扑、无顺序语义、无 DSL 结构；全部落在声明式 Config 主路径（声明式槽位行 + 数据行 + 钉死常量）。
3. **诚实成本（不隐藏）**：每 population 每呈现状态要多算 2 次 unary lookup（或按实现缓存复用）——这是两条新轴真实的运行成本，随 population × presentation 状态数线性增长；作为并列输入并入既有合并，无额外结算拓扑成本。

## 4. 复杂度迁移自检（§15.6 的立法意图）

Knife 攻击的假简化是「L 变小但复杂度迁移成大量独特 2D Surface / case-specific Resolver / 隐蔽 slot 词汇表」。逐项自检：

- 无 case-specific Resolver 引入（配置内没有任何 Resolver 调用；两轴只做 lookup）；
- 无隐蔽 slot 词汇表（没有新增 slot kind；两个 @Profile 是 §17.2 既有表的行，不是新构件类型）；
- 无 operator 词汇表（作者侧零算子可选；合并算子是常量且数学保持 UNDEFINED 显式状态）；
- 复杂度全部留在**数据行**里（Profile 数值表 + 实例绑定行 + 两条枚举行）——这正是该刀期望的位置。

结论：无复杂度迁移迹象。

## 5. DSL 对照的 L_observed

见 `dsl/cue_axis.dsl.txt` §L_observed：同一契约 DSL 表达长度 ≈ Config；DSL 买进的自由度（可换算子、可嵌套、可按实例改写算子树）恰是本契约要拒绝的，且 DSL 形状会主动打开「输运/传导耦合项」的表达缺口（Config 的封闭枚举 + unary 准入在表达层杜绝）。本扩充不构成 Expression Gate 正证据；Config 主路径表达占优。

## 6. 验证状态

- 结构 + 边界守卫：PASS（命令与输出原样记录于 `README.md` §5；守卫自测 69 用例全触发——含 18 条英文词干、17 条中文关键词逐条 probe，及行级键白名单 / 封闭枚举 / unary 准入 / FIXED_COMBINE 钉死各反例）。
- 本记账为表达成本核算，**不是**机制 promotion，**不是** Freeze，不构成对 Knife 页或 live 主页任何 Verdict 的覆盖；合并算子数学保持 OPERATOR UNDEFINED 待机制侧，本批只冻结表达边界。
