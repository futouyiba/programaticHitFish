# 帝王鲑（Chinook Salmon｜Oncorhynchus tshawytscha）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | FISH-R06 鲑系洄游层（handoff 分批名单「鲑科四」之二；R06 摘要 28 鱼=鲑系洄游 10+淡水掠食 14+海水掠食 4；Story 正文 [需正文]） |
| 冻结 Pattern | P05（handoff 点名；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 0–24.9℃、最适 12.45℃、benthopelagic、深 0–375m、晨昏活跃、肉食性、追猎、anadromous、淡水/半咸水/海水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（handoff 点名 + R06 摘要批注 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）——非停食洄游骨架（停食证据未证实；若正文证实停食→升级 MigrationReaction 双 Path 结构，属结构变更需重审） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与洄游形态

- 洄游形态：anadromous 溯河产卵型（大型鲑；海洋肥育↔深河产卵，阶段枚举 @ 化不冻结）；洄游相位=上游 lifecycle premise，非 FishGroup 内自有状态机。
- 停食判例对齐：帝王鲑未列入停食判例族（R06/R08/R09/R10 摘要停食五例=大马哈/美洲西鲱/白北鲑/高首鲟/狼鱼——无本鱼）；本骨架按非停食洄游表达（Normal 摄食维持）。若正文证实洄游期停食→照 G2/C12 判例升级 MigrationReaction 双 Path 结构（结构变更需重审，validator 族边界拦截静默改写）。
- 空间重排：海洋觅食区↔河口↔深河产卵段位置轴——premise 配置级因子集切换（CHB/MGC 先例）。
- 表达超集说明：Tier B 骨架按 P05 洄游单因子形（census SINGLE 族）给出，仅容纳 handoff 点名+CSV 方向；正文到达后换族=结构变更需重审；正文判无程序语义即撤回本文件。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，CSV 方向级推导 [需正文]）**：判断链＝premise 读取（OCEAN/MIGRATION/SPAWN 配置级）→ 阶段绑定轴段归属三档 → 归一化。推导来源＝G2/C12 样板空间重排语义+CSV anadromous 方向锚（Tier B 无行级证据，链序为样板语义方向级还原，段成员 [需正文]）。分级命中：轴段三档（当前阶段偏好轴段=全额——海洋觅食区↔河口↔深河产卵段随 premise 取段/过渡带=削减不清零/轴段外=出局 EARLY_RETURN）；early return 的对象=格子，不是阶段（PREMBIND 不变量维持；非洄游阶段程序仍运行、按海洋段轴取值）。CSV benthopelagic 锚未入链（样板链优先）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@ChinookSalmonMigrationSpatialProfile @ChinookSalmonPreyFields @ChinookSalmonDietClasses @ChinookSalmonSizeWindow @ChinookSalmonNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；P05 判例：洄游相位=lifecycle premise 层，不购买 Migration Group——停食未证实侧）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| ChinookSalmon_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（lifecycle premise：OCEAN/MIGRATION/SPAWN 由上游决定，不构成本面路由输入——
停食未证实，洄游改配置不改供给拓扑）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影骨架）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——照 census B2 北极红点鲑位置因子先例投影；**§2.2 已顺序还原（REP-ORDER-FIX-003）：轴段归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：洄游阶段位置轴（海洋觅食区↔河口↔深河产卵段；typed 实例，随 premise 取轴段） |
| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支——CHB/MGC 先例） |
| SpatialSlotProfile | @ChinookSalmonMigrationSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@ChinookSalmonPreyFields；diet_classes=@ChinookSalmonDietClasses；size_window=@ChinookSalmonSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@ChinookSalmonMigrationSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（阶段配置级）→ 阶段绑定轴段归属三档 → 归一化；轴段判定分级命中
（当前阶段偏好轴段=全额/过渡带=削减不清零/轴段外=出局 EARLY_RETURN）。阶段切换本身
不进 body 分支（PREMBIND 不变量维持）；early return 的对象是格子，不是阶段（非洄游
阶段程序仍运行、按海洋段轴取值）。推导来源=G2/C12 样板空间重排语义+CSV anadromous
方向锚（方向级，段成员 [需正文]）；档位成员=Profile 值域不冻结。与 census SINGLE 族
canonical 两步（无 gate 判语）的拓扑分歧登记 README §7（census 侧受影响族重跑=
work standards §5.4 行动项）。

读取 当前格子的位置轴事实（洄游阶段绑定的空间轴段）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@ChinookSalmonPreyFields 绑定的鱼类 prey class 生物量，
      经 diet_classes=@ChinookSalmonDietClasses 食性过滤
      与 size_window=@ChinookSalmonSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（OCEAN/MIGRATION/SPAWN——上游 lifecycle trait，配置级切换因子集；
    本 body 只按 premise 取 Profile 轴段值，不含阶段分支）

第 1 步 阶段绑定轴段归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @ChinookSalmonMigrationSpatialProfile 的阶段轴段分档槽
    （轴=海洋觅食区↔河口↔深河产卵段；段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 当前 premise 偏好轴段（preferred 槽）：
        MigrationSpatialFit = 全额
    否则如果 ∈ 过渡带（tolerated 槽——河口/近口混交带方向）：
        MigrationSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（当前阶段绑定轴段外——非本阶段空间）：
        返回 0（EARLY_RETURN：格子不在当前阶段空间重排范围，出局）

第 2 步 NORMALIZE_WEIGHT：
    对 MigrationSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live BA 句型层无洄游专用句型（§11.6 判 NEW_TEMPLATE_NOT_PROVEN）；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影骨架）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @ChinookSalmonNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @ChinookSalmonNormalFeedingProfile（大型鲑取向参数——CSV 方向锚）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@ChinookSalmonNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（非停食骨架：洄游期摄食维持；停食若正文证实→MigrationReaction 双 Path 升级需重审）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（恒为 NormalFeeding——无 Special Group）

对每个品质：
    读取该品质的 GroupEligibilityFactor（查 @NeutralEligibility）
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

- 使用的自由度：SINGLE 族投影标签；typed 因子实例语义（洄游位置轴，取自 handoff 点名+CSV）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：轴段归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) 归族裁决权（SINGLE 骨架是表达层选择，census 侧判同可能改判 PLAIN/GATED——结构变更需重审）；(3) MigrationReaction 双 Path（停食未证实——若正文证实，升级=结构变更需重审）；(4) BA-T7 ROUTE/TRANSITION 洄游句型（NEW_TEMPLATE_NOT_PROVEN）；(5) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(6) 数值与 Profile 值域不冻结（含轴段/档位成员）。
- [需正文] 洄游阶段枚举、空间轴构成、Response 接受窗参数方向、洄游期摄食是否维持（停食证实即升级）。
- [需核对] Story DB 行级 Pattern 标签（「鲑科四」名单读法——本文件按 handoff 字面收录，粉鲑/硬头鳟/细鳞鲑等未入批登记 README §4）。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 轴段归属三档+early return 链，Response 档位展开）
