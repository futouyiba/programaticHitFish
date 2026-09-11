# 高首鲟（White Sturgeon｜Acipenser transmontanus）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | FISH-R09 普通层（停食洄游判例族第 4 例：R09 摘要「停食第 4 例（鲟科）」——停食语义首次进入鲟形目；handoff 点名高首鲟；Story 正文 [需正文]） |
| 冻结 Pattern | P05（R06→R08→R09 判例链洄游侧；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 0–23.3℃、最适 11.65℃、demersal、深 1–122m、晨昏活跃、肉食性、孤僻、anadromous、淡水/半咸水/海水；CSV 双行在案（高首鲟=White Sturgeon 01 与白化高首鲟=White Sturgeon 02——种级同种白化变体行，R10-FR2 双行 4 对口径相关；本文件按 01 行锚定，白化行不另建文件）（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（R09 摘要停食批注一行 + G2/C12 表达样板；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子 V2（G2 同款）；条件组合 R2；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；MigrationReaction=R-T1 单通道（Reaction；非摄食 Provocation，Feeding 强抑制或关闭——停食第 4 例判语） |
| census 程序 | 无（Story 未入 census 归档；本批照 G2/C12 样板 + census SINGLE 族先例投影表达，census 侧 ΔL=0） |

## 0. 上游语义与洄游形态

- 洄游形态：anadromous 溯河产卵型（鲟科大个体型；春季溯河典型，阶段枚举 @ 化不冻结）。洄游相位=上游 lifecycle premise，非 FishGroup 内自有状态机。
- 停食判例（族第 4 例，鲟科首例）：R09 摘要「停食第 4 例（鲟科）」——停食洄游语义在鲟形目的重复；行级细节 [需正文]。
- 空间重排：海洋/河口觅食区↔产卵河段深潭位置轴——premise 配置级因子集切换（CHB/MGC 先例）；demersal 底栖取向为空间 Profile 值域方向（CSV 锚），不构成独立结构。
- MigrationReaction Group 无独立 Bake 程序（C12/§17.1 先例）。
- 表达超集说明：Tier B 骨架照 G2/C12 样板 + census SINGLE 族投影给出；正文到达后换族=结构变更需重审。
- 种级区分：白化高首鲟（White Sturgeon 02）为同种白化变体行（CSV 行级在案），不另建机制文件；白化体色属资产/品质维度（coverage #22 色型判例：色型不分裂），若产品启用白化资产归呈现层而非机制层。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，CSV 方向级推导 [需正文]）**：判断链＝premise 读取（OCEAN/MIGRATION/SPAWN 配置级）→ 底层水层定位（CSV demersal 硬定位——非底层=出局）→ 阶段绑定轴段归属三档 → 产卵段深潭终段档（§0 既有「产卵河段深潭位置轴」——SPAWN 段内的深潭偏好终段判定，本鱼独有终段步）→ 归一化。停食触点差异（Response 面）：R09 证据仅「第 4 例（鲟科）」一行——停食触点未细读，窗口成员 [需正文]。分级命中：各步三档（全额/削减不清零/出局 EARLY_RETURN）；early return 的对象=格子，不是阶段（PREMBIND 不变量维持；非洄游阶段程序仍运行；「非洄游阶段不进入洄游 Response 程序」由 §1 路由承载）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@WhiteSturgeonMigrationReactionEligible @WhiteSturgeonMigrationStages @WhiteSturgeonMigrationWaterTypes @WhiteSturgeonMigrationReactionShare @WhiteSturgeonMigrationSpatialProfile @WhiteSturgeonPreyFields @WhiteSturgeonDietClasses @WhiteSturgeonSizeWindow @WhiteSturgeonNormalFeedingProfile @WhiteSturgeonMigrationReactionProfile @WhiteSturgeonMigrationEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 条件原子（变体 V2：条件组/条件/事实·计算项/参数/比较符/比较值；G2 原样形态）

| 条件组 | 条件 | 事实 / 计算项 | 参数 | 比较符 | 比较值 |
|---|---|---|---|---|---|
| WS1 | C1 | 当前洄游 / 繁殖阶段事实 | — | IN | @WhiteSturgeonMigrationStages |
| WS1 | C2 | 当前水体类型 | — | IN | @WhiteSturgeonMigrationWaterTypes |

### 1.2 条件组合（变体 R2：规则集/组合方式/引用）

| 规则集 | 组合方式 | 引用 |
|---|---|---|
| WhiteSturgeonMigrationReactionEligible | AND | WS1.C1, WS1.C2 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| WhiteSturgeon_Migration_Route | @WhiteSturgeonMigrationReactionEligible | MigrationReaction | 按配置分流 | @WhiteSturgeonMigrationReactionShare |
| WhiteSturgeon_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前洄游 / 繁殖阶段事实
读取 当前水体类型

如果 阶段事实 IN @WhiteSturgeonMigrationStages
并且 水体类型 IN @WhiteSturgeonMigrationWaterTypes：

    从普通摄食机会中分出 @WhiteSturgeonMigrationReactionShare
    放入 MigrationReaction Group

否则：
    不生成 MigrationReaction Group

MigrationReactionShare = 命中 ? @WhiteSturgeonMigrationReactionShare : 0
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
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；照 census B2 北极红点鲑位置因子先例投影；**§2.2 已顺序还原（REP-ORDER-FIX-003）：底层硬定位+轴段归属三档+深潭终段档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：洄游阶段位置轴（河口/下游觅食区↔产卵河段深潭；typed 实例，随 premise 取轴段） |
| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支——CHB/MGC 先例） |
| SpatialSlotProfile | @WhiteSturgeonMigrationSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@WhiteSturgeonPreyFields；diet_classes=@WhiteSturgeonDietClasses；size_window=@WhiteSturgeonSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@WhiteSturgeonMigrationSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（阶段配置级）→ 底层水层定位（硬判定）→ 阶段绑定轴段归属三档
→ 产卵段深潭终段档 → 归一化；各步分级命中（全额/削减不清零/出局 EARLY_RETURN）。
阶段切换本身不进 body 分支（PREMBIND 不变量维持）；early return 的对象是格子，
不是阶段（非洄游阶段程序仍运行、按河口/下游段轴取值）。推导来源=CSV demersal
栖息带锚+§0 既有产卵河段深潭位置轴语义+G2/C12 样板空间重排语义（方向级，
段成员 [需正文]）；档位成员=Profile 值域不冻结。与 census SINGLE 族 canonical
两步（无 gate 判语）的拓扑分歧登记 README §7（census 侧受影响族重跑=work
standards §5.4 行动项）。

读取 当前格子的水层带位置事实
读取 当前格子的位置轴事实（洄游阶段绑定的空间轴段）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@WhiteSturgeonPreyFields 绑定的底栖/鱼类 prey class 生物量，
      经 diet_classes=@WhiteSturgeonDietClasses 食性过滤
      与 size_window=@WhiteSturgeonSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（OCEAN/MIGRATION/SPAWN——上游 lifecycle trait，配置级切换因子集；
    本 body 只按 premise 取 Profile 轴段值，不含阶段分支）

第 1 步 底层水层定位（CSV demersal 底栖特化硬定位）：
    用水层带位置查询 @WhiteSturgeonMigrationSpatialProfile 的水层分档槽
    （底层带=CSV 栖息带锚；档位成员=Profile 值域不冻结 [需正文]）
    如果 水层 ∈ 底层带（preferred 槽）：
        LayerTier = 全额保留
    否则如果 ∈ 近底过渡带（tolerated 槽）：
        LayerTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（中上远带）：
        返回 0（EARLY_RETURN：demersal 底栖特化不在非底层分布——
        硬判定；CSV 锚方向级推导 [需正文]，若正文证实离底取食
        则档位化=结构变更需重审）

第 2 步 阶段绑定轴段归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @WhiteSturgeonMigrationSpatialProfile 的阶段轴段分档槽
    （轴=河口/下游觅食区↔产卵河段；段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 当前 premise 偏好轴段（preferred 槽）：
        MigrationSpatialFit = 全额
    否则如果 ∈ 过渡带（tolerated 槽——河口/近口混交带方向）：
        MigrationSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（当前阶段绑定轴段外——非本阶段空间）：
        返回 0（EARLY_RETURN：格子不在当前阶段空间重排范围，出局）

第 3 步 产卵段深潭终段档（本鱼独有终段步——SPAWN 段内深潭偏好）：
    仅当 premise ∈ SPAWN 段时执行（段内子档判定，不是阶段分支——
    premise 取值已由第 2 步读取）：
    用深潭结构事实查询 @WhiteSturgeonMigrationSpatialProfile 的深潭分档槽
    （深潭成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子 ∈ 深潭结构档（preferred 槽）：
        DeepPoolTier = 全额保留
    否则如果 ∈ 深潭邻近档（tolerated 槽）：
        DeepPoolTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（产卵段内无深潭结构档）：
        返回 0（EARLY_RETURN：产卵段内非深潭格出局——
        §0 既有深潭轴语义的方向级推导 [需正文]）

第 4 步 NORMALIZE_WEIGHT：
    对 LayerTier × MigrationSpatialFit × DeepPoolTier 执行模板固定归一化
    （族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 MigrationReaction Group｜无独立 Bake 程序（显式声明）

Reaction 不要求独立 Bake（live §17.1 先例；C12 Bake=明确不适用）。洄游期空间重排由 Normal 面 premise 配置切换承载（§2.1 FactorBinding），MigrationReaction Group 的供给空间分布沿用该输出。

### 2.4 live 层投影声明

live BA 句型层无洄游专用句型（§11.6 判 NEW_TEMPLATE_NOT_PROVEN）；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（双 Group 双 Path；R06–R10 FR3 停食判例：P05 状态 × Response multi-path）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @WhiteSturgeonNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |
| MigrationReaction | R-T1 单通道（Reaction；非摄食 Provocation） | @WhiteSturgeonMigrationReactionProfile | 返回 ReactionResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本（双 Path 结构完全展开）

NormalFeeding Group：

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @WhiteSturgeonNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@WhiteSturgeonNormalFeedingProfile 值域不冻结）：
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
    阶段事实 ∉ @WhiteSturgeonMigrationStages 或 水体类型 ∉ @WhiteSturgeonMigrationWaterTypes
    时本 Group 不成立（§1.4 分群），本 Program 整体不激活——
    程序级出局（EARLY_RETURN：非洄游阶段的鱼不进入洄游 Response 程序，
    归 NormalFeeding Path 处理；阶段判定在路由层完成，本 body 不含阶段分支——
    PREMBIND 不变量维持）

第 1 步 状态门控（STATE_GATE_FEEDING，停食判例族第 4 例——判断链最先）：
    本 Group 停食语义成立——普通 Feeding 强抑制或关闭
    （停食判例族第 4 例证据：R09 摘要「停食第 4 例（鲟科）」——
    停食语义首次进入鲟形目；停食触点未细读（证据仅一行——触点窗口成员=
    @WhiteSturgeonMigrationStages 值域内 Profile 层定值 [需正文]）；
    Typed Result=档位关闭而非数值归零。若产品要求保留残值则 Cap 形态，
    档位与残值由 Profile 层定值；行级停食细节 [需正文]）：
    普通 Feeding 评价 在本 Program 出局（EARLY_RETURN——停食成立时 Feeding 通道
    最先关闭，后续步骤不再评价任何摄食响应）

读取 当前离散目标的非摄食 Provocation 事实（入侵/挑衅 Cue：突然性、贴近度、侵扰持续性、深潭/产卵床侵扰语义）

第 2 步 EVAL_TARGET_AS_INTRUDER_TYPED：
    用 Provocation 事实评价 @WhiteSturgeonMigrationReactionProfile
    得到 ProvocationEvaluation

第 3 步 DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 ProvocationEvaluation（档位成员=@WhiteSturgeonMigrationReactionProfile 值域不冻结）：
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
| MigrationReaction | QT-1 | @WhiteSturgeonMigrationEligibilityByQuality | @NeutralAffinity | 洄游期成熟个体组成方向（值域由 Profile 层定值；白化变体不分裂——色型不建体判例） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（NormalFeeding 或 MigrationReaction）

对每个品质：
    读取该品质的 GroupEligibilityFactor（NormalFeeding 行查 @NeutralEligibility；MigrationReaction 行查 @WhiteSturgeonMigrationEligibilityByQuality）
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

- 使用的自由度：G2 MigrationReaction share-vector 路由样板；SINGLE 族投影标签与 typed 因子实例语义；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：底层硬定位步+深潭终段档（本鱼独有，CSV+§0 深潭轴语义锚）、轴段归属三档+early return 链、Response 状态门控显式化+程序级门+档位展开——推导依据 §0 判断顺序行）**；停食判例双 Path Response 结构。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) R-T2 折叠候选（归机制侧）；(3) BA-T7 ROUTE/TRANSITION 洄游句型（NEW_TEMPLATE_NOT_PROVEN）；(4) 白化变体行分裂（色型不建体判例，资产维度归呈现层）；(5) 阶段选择器（程序级门/状态门控不构成 body 内阶段分支）；(6) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(7) 数值与 Profile 值域不冻结（含水层/轴段/深潭/档位成员）。
- [需正文] 洄游阶段枚举成员、水体类型集合、MigrationShare 档位、Provocation Cue 构成、停食行级细节（鲟科第 4 例正文级确认）。
- [需核对] Story DB 行级 Pattern 标签；鲟系其它行（俄罗斯鲟/尖吻鲟/短吻鲟/闪光鲟/小体鲟）是否另有 P05 Story——不在本批冒充覆盖（README §4 登记 4）。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 底层硬定位+轴段归属三档+深潭终段档+early return 链，Response 状态门控显式化+程序级门+双 Path 档位展开）
