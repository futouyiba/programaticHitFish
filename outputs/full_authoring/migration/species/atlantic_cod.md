# 大西洋鳕（Atlantic Cod｜Gadus morhua）｜繁殖期性别相关水深四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | B01-S52｜大西洋鳕鱼｜繁殖期性别相关水深与未确认产卵潜水（Story 页 3d7a4137d23681879692c6ae73dd9798；census CENSUS-B1 快照全文在案） |
| 冻结 Pattern | P05（census B1 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 0–15℃、最适 7.5℃、benthopelagic、深 0–600m、全天活跃、肉食性、追猎、oceanodromous、半咸水/海水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-COD-BAKE（SINGLE 族成员：深度因子 sex/stage premise 绑定）+ P-B1-COD-RESP（TYPED 族标准成员，遥测深度不判定当下 FeedingMatch） |

## 0. 上游语义与洄游形态

- 洄游形态：繁殖期水深调整（性别相关：雄雌个体随繁殖阶段占据不同水深带）；Spatial 随阶段/性别调整，先不购买互斥 FishGroup（census Group 面判语原样：GroupPressure=Possible 未证实）。
- **share-vector 替代读法（coverage delta #6 判例，显式登记）**：「性别相关水深=GR 同条件双路由 share-vector 拆分（male/female 两 Group 各绑不同深度 BA Profile）；share 是供给比例不是逐个体分类」（coverage delta report §2.1/#6/K6 原文）。census 侧按配置级因子绑定处理（深度因子随 sex/stage premise 绑定，不拆 Group）——**两读法都是 G-T1 域内表达层选择**（share-vector 多路由是 §7/§15.1 既有能力），census 主判定=配置级，本文件按 census 判定表达，share-vector 读法登记于 §2.3（取舍归两层 reconciliation，非结构分歧）。
- Bake 面：深度因子单链 sex/stage premise 绑定（census P-B1-COD-BAKE：SINGLE 族成员）。
- Response 面：TYPED 族标准成员（遥测深度不判定当下 FeedingMatch——census 判语原样）。
- Quality 面：census NO_SURFACE_EFFECT。
- 证据分级标注：「未确认产卵潜水」为 Story 原文证据分级标注（未证实行为），不建体（coverage #6 判语）。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，census 冻结语义层推导）**：判断链＝premise 读取（sex/stage 个体事实配置级）→ 性别阶段绑定深度带归属三档 → 归一化。推导来源＝census P-B1-COD-BAKE 冻结实例常量（深度因子随 sex/stage premise 绑定——盲体 sketch 语义的档位化还原；Tier A 骨架在案，档位成员不在快照——段成员 [需正文]）。分级命中：深度带三档（当前 sex/stage 偏好深度带=全额——繁殖期雄/雌/未繁殖个体深度带值域随 premise 取段/相邻深度带=削减不清零/远带=出局 EARLY_RETURN）；early return 的对象=格子，不是性别阶段（PREMBIND 不变量维持——sex/stage 不构成路由输入，§1.3 判语原样）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@CodSexStageDepthProfile @CodPreyFields @CodDietClasses @CodSizeWindow @CodNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——GroupPressure=Possible 未证实，先不购买互斥 FishGroup；性别 share-vector 替代读法见 §2.3 登记）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| CodSexStage_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（sex/stage premise 由上游 lifecycle trait 决定，不构成本面路由输入——
性别相关水深按配置级因子绑定处理，census 主判定）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例；share 是供给比例不是逐个体分类）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；**§2.2 已顺序还原（REP-ORDER-FIX-003）：深度带归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：繁殖期深度因子（性别相关水深带；typed 实例，sex/stage 驱动——census P-B1-COD-BAKE 实例常量） |
| FactorBinding | lifecycle premise：sex/stage 配置级切换（繁殖期雄/雌/未繁殖个体深度带值域切换；值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @CodSexStageDepthProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@CodPreyFields；diet_classes=@CodDietClasses；size_window=@CodSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@CodSexStageDepthProfile（handoff 指定读法；share-vector 替代读法见 §2.3；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（性别阶段配置级）→ 性别阶段绑定深度带归属三档 → 归一化；
深度带判定分级命中（当前偏好深度带=全额/相邻深度带=削减不清零/远带=出局
EARLY_RETURN）。性别阶段切换本身不进 body 分支（PREMBIND 不变量维持：
sex/stage=上游个体事实，配置级切换因子集——不构成路由输入，§1.3 判语原样）；
early return 的对象是格子，不是性别阶段。推导来源=census P-B1-COD-BAKE 冻结实例
常量（盲体 sketch 语义的档位化还原——Tier A 骨架在案、档位成员不在快照，
段成员 [需正文]）；档位成员=Profile 值域不冻结。与 census SINGLE 族 canonical
两步（无 gate 判语）的拓扑分歧登记 README §7（census 侧受影响族重跑=
work standards §5.4 行动项）。

读取 当前格子的深度带事实（繁殖期性别相关水深轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@CodPreyFields 绑定的鱼类/无脊椎 prey class 生物量，
      经 diet_classes=@CodDietClasses 食性过滤
      与 size_window=@CodSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（sex/stage——上游个体事实，配置级切换因子集；
    本 body 只按 premise 取 Profile 深度带值，不含性别阶段分支）

第 1 步 性别阶段绑定深度带归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用深度带事实查询 @CodSexStageDepthProfile 的阶段深度分档槽
    （轴=繁殖期雄/雌/未繁殖个体深度带随 sex/stage 取段；段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子深度 ∈ 当前 sex/stage 偏好深度带（preferred 槽）：
        SexStageDepthFit = 全额
    否则如果 ∈ 相邻深度带（tolerated 槽）：
        SexStageDepthFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（远带——当前 sex/stage 不取的深度带）：
        返回 0（EARLY_RETURN：格子不在当前性别阶段深度范围，出局）

第 2 步 NORMALIZE_WEIGHT：
    对 SexStageDepthFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明与 share-vector 替代读法登记

live 吸收读法=BA-T1 底板 + DynamicSpatialSlot=@CodSexStageDepthProfile。**share-vector 替代读法（coverage delta #6/K6 判例原文）**：「性别相关水深=GR 同条件双路由 share-vector 拆分（male/female 两 Group 各绑不同深度 BA Profile）」——share 是供给比例不是逐个体分类，G-T1 域内既有能力（§7 契约+§15.1 多路由先例）。census 主判定=配置级因子绑定（不拆 Group）；两读法取舍归 census↔live 两层 reconciliation（README §3 登记 2），本文件按 census 判定表达不闭合。「未确认产卵潜水」为证据分级标注（未证实行为不建体）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @CodNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @CodNormalFeedingProfile（遥测深度不判定当下 FeedingMatch——census 判语原样）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@CodNormalFeedingProfile 值域不冻结；
    遥测深度不进 Response 档位判定——census 判语在档位层的读法）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；census Quality 面 NO_SURFACE_EFFECT |

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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（深度因子 sex/stage 绑定——census 冻结实例常量）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：深度带归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) 性别 share-vector 双路由表达（coverage #6 判例读法，census 主判定=配置级；取舍归两层 reconciliation 登记不闭合）；(3) 「产卵潜水」行为建体（Story 证据分级=未确认，不建体）；(4) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结（含深度带/档位成员）。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 深度带归属三档+early return 链，Response 档位展开）
