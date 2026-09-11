# 大马哈鱼（Chum Salmon｜Oncorhynchus keta）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | FISH-R06 鲑系洄游层（停食洄游判例族首例：R06 摘要原文「Adults cease feeding in freshwater」；FR3 裁=停食判例族分支化未证实侧→P05 状态 × Response multi-path，拒 P04——R06 FR3/Guarding 批 README 排除表判例链；Story 正文 [需正文]） |
| 冻结 Pattern | P05（R06 FR3 分支化判例：洄游型 relation 未证实→P05×multi-path；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 0–23.7℃、最适 11.85℃、benthopelagic、深 0–250m、晨昏活跃、肉食性、追猎、anadromous、淡水/半咸水/海水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（R06 摘要停食证据原文一行 + G2/C12 表达样板；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子 V2（G2 同款）；条件组合 R2；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；MigrationReaction=R-T1 单通道（Reaction；非摄食 Provocation，Feeding 强抑制或关闭——停食首例判语） |
| census 程序 | 无（Story 未入 census 归档；本批照 G2/C12 样板 + census SINGLE 族先例投影表达，census 侧 ΔL=0） |

## 0. 上游语义与洄游形态

- 洄游形态：anadromous 溯河产卵型（秋季溯河典型；阶段枚举 @ 化不冻结）。洄游相位=上游 lifecycle premise（world/生命周期事实），非 FishGroup 内自有状态机。
- 停食判例（本鱼为族首例）：R06 高价值发现原文「Adults cease feeding in freshwater」——成体入淡水后停食；洄游期咬钩=非摄食攻击/挑衅响应的独立证据。FR3 裁定：guard relation 未证实→不属 P04，归 P05 状态 × Response multi-path（大马哈/美洲西鲱双例首裁，白北鲑/高首鲑跨科重复确认，狼鱼 relation 证实侧归 P04——判例族五例，本鱼为洄游侧首例）。
- 空间重排：海洋觅食区↔河口↔产卵河段位置轴——premise 配置级因子集切换（CHB/MGC 先例）。
- MigrationReaction Group 无独立 Bake 程序（C12/§17.1 先例）；空间分布由 Normal 面 premise 绑定切换承载。
- 表达超集说明：Tier B 骨架照 G2/C12 样板 + census SINGLE 族投影给出；Story 正文到达后若判 PLAIN（多因子）或 GATED＝换 BakeTemplate 值 + 增/删行＝结构变更需重审（validator 族边界拦截静默改写），不是 Profile 重绑定。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，CSV 方向级推导 [需正文]）**：判断链＝premise 读取（OCEAN/MIGRATION/SPAWN 配置级）→ 近底水层带定位（CSV benthopelagic 软定位三档）→ 阶段绑定轴段归属三档 → 归一化。与样板基准链（atlantic_salmon 两步）的差异＝近底水层带定位步（Tier B 无样板步序约束，CSV 栖息带锚入链；A- 档样板鱼样板链优先不入——差异来源=推导证据层不同，本身=LogicTemplate 判据）。停食触点差异（Response 面）：R06 原文「Adults cease feeding in freshwater」——停食触点=入淡水（淡水轴段=停食窗口方向），与美洲西鲱「洄游全程停食」触点不同（atlantic_salmon 按样板鱼处理无此细读）。分级命中：各步三档（全额/削减不清零/出局 EARLY_RETURN）；early return 的对象=格子，不是阶段——阶段切换永远 premise 配置级（PREMBIND 不变量维持），非洄游阶段程序仍运行；「非洄游阶段不进入洄游 Response 程序」由 §1 路由承载。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@ChumSalmonMigrationReactionEligible @ChumSalmonMigrationStages @ChumSalmonMigrationWaterTypes @ChumSalmonMigrationReactionShare @ChumSalmonMigrationSpatialProfile @ChumSalmonPreyFields @ChumSalmonDietClasses @ChumSalmonSizeWindow @ChumSalmonNormalFeedingProfile @ChumSalmonMigrationReactionProfile @ChumSalmonMigrationEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 条件原子（变体 V2：条件组/条件/事实·计算项/参数/比较符/比较值；G2 原样形态）

| 条件组 | 条件 | 事实 / 计算项 | 参数 | 比较符 | 比较值 |
|---|---|---|---|---|---|
| CS1 | C1 | 当前洄游 / 繁殖阶段事实 | — | IN | @ChumSalmonMigrationStages |
| CS1 | C2 | 当前水体类型 | — | IN | @ChumSalmonMigrationWaterTypes |

### 1.2 条件组合（变体 R2：规则集/组合方式/引用）

| 规则集 | 组合方式 | 引用 |
|---|---|---|
| ChumSalmonMigrationReactionEligible | AND | CS1.C1, CS1.C2 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| ChumSalmon_Migration_Route | @ChumSalmonMigrationReactionEligible | MigrationReaction | 按配置分流 | @ChumSalmonMigrationReactionShare |
| ChumSalmon_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前洄游 / 繁殖阶段事实
读取 当前水体类型

如果 阶段事实 IN @ChumSalmonMigrationStages
并且 水体类型 IN @ChumSalmonMigrationWaterTypes：

    从普通摄食机会中分出 @ChumSalmonMigrationReactionShare
    放入 MigrationReaction Group

否则：
    不生成 MigrationReaction Group

MigrationReactionShare = 命中 ? @ChumSalmonMigrationReactionShare : 0
SpecialShareTotal = MigrationReactionShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——Share 契约（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 MigrationReactionShare / NormalFeedingShare
（分群本身仍是 Predicate + 权重路由；不为此购买任何阶段选择器——G2 读数原样）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 NormalFeeding Group｜配置表（洄游空间重排；阶段配置级因子集切换）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；照 census B2 北极红点鲑位置因子先例投影；**§2.2 已顺序还原（REP-ORDER-FIX-003）：近底软定位+轴段归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：洄游阶段位置轴（海洋觅食区↔河口↔产卵河段；typed 实例，随 premise 取轴段） |
| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支——CHB/MGC 先例） |
| SpatialSlotProfile | @ChumSalmonMigrationSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@ChumSalmonPreyFields；diet_classes=@ChumSalmonDietClasses；size_window=@ChumSalmonSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@ChumSalmonMigrationSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（阶段配置级）→ 近底水层带定位（软三档）→ 阶段绑定轴段归属三档
→ 归一化；各步分级命中（全额/削减不清零/出局 EARLY_RETURN）。阶段切换本身不进 body
分支（PREMBIND 不变量维持）；early return 的对象是格子，不是阶段（非洄游阶段程序仍
运行、按海洋段轴取值）。推导来源=CSV benthopelagic 栖息带锚+G2/C12 样板空间重排语义
（方向级，段成员 [需正文]）；档位成员=Profile 值域不冻结。与 census SINGLE 族 canonical
两步（无 gate 判语）的拓扑分歧登记 README §7（census 侧受影响族重跑=work standards
§5.4 行动项）。

读取 当前格子的水层带位置事实
读取 当前格子的位置轴事实（洄游阶段绑定的空间轴段）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@ChumSalmonPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@ChumSalmonDietClasses 食性过滤
      与 size_window=@ChumSalmonSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（OCEAN/MIGRATION/SPAWN——上游 lifecycle trait，配置级切换因子集；
    本 body 只按 premise 取 Profile 轴段值，不含阶段分支）

第 1 步 近底水层带定位（CSV benthopelagic 软定位，分级命中）：
    用水层带位置查询 @ChumSalmonMigrationSpatialProfile 的水层分档槽
    （近底中上带=CSV 栖息带锚；档位成员=Profile 值域不冻结 [需正文]）
    如果 水层 ∈ 近底中上带（preferred 槽）：
        LayerTier = 全额保留
    否则如果 ∈ 过渡带（tolerated 槽）：
        LayerTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（远带）：
        返回 0（EARLY_RETURN：远离近底带的格子出局——CSV 锚方向级推导 [需正文]，
        若正文证实深层/底层带活动则档位成员调整，结构变更需重审）

第 2 步 阶段绑定轴段归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @ChumSalmonMigrationSpatialProfile 的阶段轴段分档槽
    （轴=海洋觅食区↔河口↔产卵河段三段；段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 当前 premise 偏好轴段（preferred 槽）：
        MigrationSpatialFit = 全额
    否则如果 ∈ 过渡带（tolerated 槽——河口/近口混交带方向）：
        MigrationSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（当前阶段绑定轴段外——非本阶段空间）：
        返回 0（EARLY_RETURN：格子不在当前阶段空间重排范围，出局）

第 3 步 NORMALIZE_WEIGHT：
    对 LayerTier × MigrationSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 MigrationReaction Group｜无独立 Bake 程序（显式声明）

Reaction 不要求独立 Bake（live §17.1 先例；C12 Bake=明确不适用）。洄游期空间重排由 Normal 面 premise 配置切换承载（§2.1 FactorBinding），MigrationReaction Group 的供给空间分布沿用该输出。

### 2.4 live 层投影声明

live BA 句型层无洄游专用句型（§11.6 判 NEW_TEMPLATE_NOT_PROVEN）；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（双 Group 双 Path；R06/R10 FR3 停食判例：P05 状态 × Response multi-path）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @ChumSalmonNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |
| MigrationReaction | R-T1 单通道（Reaction；非摄食 Provocation） | @ChumSalmonMigrationReactionProfile | 返回 ReactionResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本（双 Path 结构完全展开）

NormalFeeding Group：

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @ChumSalmonNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@ChumSalmonNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

MigrationReaction Group：

```plain text
第 0 步 程序级门（非洄游阶段不进入本 Program——§1 路由承载）：
    阶段事实 ∉ @ChumSalmonMigrationStages 或 水体类型 ∉ @ChumSalmonMigrationWaterTypes
    时本 Group 不成立（§1.4 分群），本 Program 整体不激活——
    程序级出局（EARLY_RETURN：非洄游阶段的鱼不进入洄游 Response 程序，
    归 NormalFeeding Path 处理；阶段判定在路由层完成，本 body 不含阶段分支——
    PREMBIND 不变量维持）

第 1 步 状态门控（STATE_GATE_FEEDING，停食判例族首例——判断链最先）：
    本 Group 停食语义成立——普通 Feeding 强抑制或关闭
    （停食判例族首例证据：R06 摘要原文「Adults cease feeding in freshwater」——
    成体入淡水后停食；停食触点=入淡水（淡水轴段=停食窗口方向，与美洲西鲱
    「洄游全程停食」触点不同——触点窗口成员=@ChumSalmonMigrationStages 值域内
    Profile 层定值）；Typed Result=档位关闭而非数值归零。若产品要求保留残值则
    Cap 形态，档位与残值由 Profile 层定值；正文细读 [需正文]）：
    普通 Feeding 评价 在本 Program 出局（EARLY_RETURN——停食成立时 Feeding 通道
    最先关闭，后续步骤不再评价任何摄食响应）

读取 当前离散目标的非摄食 Provocation 事实（入侵/挑衅 Cue：突然性、贴近度、侵扰持续性、产卵地侵扰语义）

第 2 步 EVAL_TARGET_AS_INTRUDER_TYPED：
    用 Provocation 事实评价 @ChumSalmonMigrationReactionProfile
    得到 ProvocationEvaluation

第 3 步 DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 ProvocationEvaluation（档位成员=@ChumSalmonMigrationReactionProfile 值域不冻结）：
    如果 ProvocationEvaluation ∈ 激惹档（preferred 槽）：
        返回 Response(Reaction)（全额响应）
    否则如果 ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(Reaction)

不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program——
live §8.8 Typed Result 先例；本行=第 1 步状态门控的拓扑语义，状态门控=其在
判断链中的位置，两读法同义）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |
| MigrationReaction | QT-1 | @ChumSalmonMigrationEligibilityByQuality | @NeutralAffinity | 洄游期成熟个体组成方向（值域由 Profile 层定值） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（NormalFeeding 或 MigrationReaction）

对每个品质：
    读取该品质的 GroupEligibilityFactor（NormalFeeding 行查 @NeutralEligibility；MigrationReaction 行查 @ChumSalmonMigrationEligibilityByQuality）
    读取该品质的 GroupAffinityFactor（查 @NeutralAffinity）
    读取当前 lure / bait / hook / context 等原始事实
    评价所有适用的 Presentation Modifier / Context Modifier（只读原始事实）

    原始品质权重 =
        基础品质权重
        × GroupEligibilityFactor
        × GroupAffinityFactor
        × 所有适用 Modifier

汇总所有品质的原始权重

如果总权重 > 0：
    统一归一化
    输出 QualityWeightVector
否则：
    当前 FishQuality × FishGroup 不产生可实现候选
```

## 5. 自由度、边界与放弃项

- 使用的自由度：G2 MigrationReaction share-vector 路由样板；SINGLE 族投影标签与 typed 因子实例语义；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：近底软定位步（CSV 锚）、轴段归属三档+early return 链、Response 状态门控显式化+程序级门+档位展开——推导依据 §0 判断顺序行）**；停食判例双 Path Response 结构。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) R-T2 折叠候选（归机制侧）；(3) BA-T7 ROUTE/TRANSITION 洄游句型（NEW_TEMPLATE_NOT_PROVEN）；(4) 阶段选择器（G2 明确不购买；程序级门/状态门控不构成 body 内阶段分支）；(5) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(6) 数值与 Profile 值域不冻结（含水层/轴段/档位成员）。
- [需正文] 洄游阶段枚举成员、水体类型集合、MigrationShare 档位、Provocation Cue 构成、停食起止相位细读（摘要一行证据的正文级确认）。
- [需核对] Story DB 行级 Pattern 标签。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 近底软定位+轴段归属三档+early return 链，Response 状态门控显式化+程序级门+停食触点语义+双 Path 档位展开）
