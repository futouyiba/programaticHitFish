# 欧鲢（Common Chub｜Squalius cephalus）｜体型分级机会主义与产卵洄游四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：个体发生切换组） |
| Story | FISH-R05-欧鲢-Size-Graded-Opportunism-Spawning-Run（Story 页 3d7a4137d236817c8f4ee128d2269970；census CENSUS-B0 快照全文在案） |
| 冻结 Pattern | P01 + P05（census B0 stories.jsonl 快照；本批承载 P05 侧语义——体型分级 premise 与产卵洄游配置级切换；P01 侧=机会主义宽谱 TYPED 实例） |
| 物种属性锚 | fish-reference-20260908：水温 4–20℃、最适 12℃、benthopelagic、早晨活跃、杂食性（variable）、撕鳍性格标注、potamodromous、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B0 全四面判定快照 + 盲程序体 blind_programs.jsonl 冻结；阴性对照样本——EXISTING_PROGRAM_INSTANCE + absence_claim NO_NEW_PROGRAM_CURRENT_EVIDENCE） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；evaluator 参数宽度随 size_class premise 切换（body 单态） |
| census 程序 | P-CHB-BAKE（PLAIN 族成员，registry v4 在案：4 槽流速/深潭结构/猎物/水面机会→COMBINE_WEIGHTED）+ P-CHB-RESP-FEEDING（TYPED 族标准成员，机会主义宽谱） |

## 0. 上游语义与生活史形态

- 个体发生形态：体型分级机会主义（size_class=SMALL/LARGE 上游 trait——小个体=杂食宽谱，大个体=鱼食偏好收窄；全部落因子权重与 prey 谱参数，无结构差异——census 冻结判语原样）。
- 洄游形态：产卵洄游（spawn_run=INACTIVE/ACTIVE lifecycle 状态，上游决定）——**P05 判例本鱼为配置级切换先例源**：洄游期因子集切换为快水/砾石繁殖因子（spawn_factors={fast_water, gravel} 冻结常量），配置级处理 body 不分支；census open_semantics 原样携带：「若 review 判需 body 内 IF，本面结构结论需复核」。
- Group 面：体型分级=trait/condition（成/幼不并存互斥）、洄游=P05 时序状态，均不拆供给（census Group 面 NO_SURFACE_EFFECT 原样）。
- Response 面：TYPED 标准成员（机会主义宽谱 evaluator——多种饵/拟饵可钓 FishBase 原文佐证；size_class premise 决定参数宽度：小=宽谱、大=偏窄鱼食）。
- Quality 面：census NO_SURFACE_EFFECT（S3=EO 不影响结构判断）。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围；本鱼是 P05×multi-path 判例链的阴性对照——洄游不停食、无 Reaction 路径）。

Profile 引用清单：@CommonChubFlowFactorProfile @CommonChubPoolStructureProfile @CommonChubPreyFactorProfile @CommonChubSurfaceFilmProfile @CommonChubPreyFields @CommonChubDietClasses @CommonChubSizeWindow @CommonChubNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——体型分级=trait/condition、洄游=P05 时序状态，均不拆供给）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| CommonChub_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（size_class 与 spawn_run premise 由上游 trait/lifecycle 决定，不构成本面路由输入——
体型分级与产卵洄游均为配置级，census 判语原样）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census PLAIN 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；typed 因子集→固定组合；本鱼为族早期成员 4 槽——与地图鱼 P-OSC-BAKE factor_set 轴内直验同构，census 阴性对照） |
| Factor1Type(typed) | habitat_factor：流速（急流-深潭 mosaic 轴；typed 实例——census P-CHB-BAKE 槽 1 EVAL_HABITAT_FACTOR_FLOW） |
| Factor2Type(typed) | habitat_factor：深潭结构（typed 实例——census P-CHB-BAKE 槽 2） |
| Factor3Type(typed) | resource_factor：猎物资源（杂食宽谱，大个体鱼食权重升——size_class premise 落本槽参数；census 槽 3） |
| Factor4Type(typed) | resource_factor：陆生猎物水面机会（typed 实例——census 槽 4 EVAL_RESOURCE_FACTOR_SURFACE_FILM） |
| FactorBinding | lifecycle premise：spawn_run 配置级切换（INACTIVE=常态 4 槽因子集 / ACTIVE=快水+砾石繁殖因子集 {fast_water, gravel} 冻结常量——P05 判例配置级，body 不分支；size_class 同为上游 premise，落槽 3 参数） |
| CombineRule | Template-fixed COMBINE_WEIGHTED（族常量拓扑；数学 OPERATOR UNDEFINED 待机制侧——census open_semantics 因子间顺序 unordered 原样携带） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@CommonChubPreyFields；diet_classes=@CommonChubDietClasses；size_window=@CommonChubSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set（§13.2 结构族：4 槽因子集；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的流速事实
读取 当前格子的深潭结构事实
读取 当前格子的猎物资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@CommonChubPreyFields 绑定的杂食谱 prey class 生物量，
      经 diet_classes=@CommonChubDietClasses 食性过滤
      与 size_window=@CommonChubSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前格子的陆生猎物水面机会事实
读取 当前 premise（spawn_run 与 size_class——上游 lifecycle trait/体型 trait，
    配置级切换因子集与参数，body 不分支）

第 1 槽 EVAL_HABITAT_FACTOR_FLOW：
    用流速事实查询 @CommonChubFlowFactorProfile
    得到 FlowFit

第 2 槽 EVAL_HABITAT_FACTOR_POOL_STRUCTURE：
    用深潭结构事实查询 @CommonChubPoolStructureProfile
    得到 PoolStructureFit

第 3 槽 EVAL_RESOURCE_FACTOR_PREY：
    用猎物资源事实查询 @CommonChubPreyFactorProfile（size_class premise：大个体鱼食权重升——参数）
    得到 PreyFit

第 4 槽 EVAL_RESOURCE_FACTOR_SURFACE_FILM：
    用水面机会事实查询 @CommonChubSurfaceFilmProfile
    得到 SurfaceFilmFit

COMBINE_WEIGHTED：
    按模板固定组合规则合并 FlowFit / PoolStructureFit / PreyFit / SurfaceFilmFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（census PLAIN 族 COMBINE_WEIGHTED 数学未冻结；
    因子间顺序未由证据裁决，unordered 处理——open_semantics 原样携带）

返回 SpatialDistributionWeight（因子集结束：无 gate、无 early return、无相对寻优
——族 forbidden_freedoms 边界；产卵洄游期因子集切换在 premise 配置层完成，本 body 不含 IF 分支
——若 review 判需 body 内 IF，结构结论需复核，census open_semantics 原样）
```

### 2.3 live 层投影声明

live 结构族 B-T1 Independent Factor Set + Optional Gate（§13.2）覆盖 4 槽形态；census PLAIN 族与 live B-T1 对齐（HRQ-01 factor_set 轴 + HRQ-07 unordered）归两层 reconciliation（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；evaluator 参数宽度随 size_class premise 切换） | @CommonChubNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前 size_class premise（决定 evaluator 参数宽度：
    SMALL=杂食宽谱接受窗；LARGE=鱼食偏好收窄——census 冻结判语，
    body 单态无分支）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @CommonChubNormalFeedingProfile（机会主义宽谱 typed food evaluator——
    多种饵/拟饵可钓，FishBase 原文佐证；diet_breadth=wide_opportunist 冻结常量）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
（产卵洄游期不停食——本鱼是停食洄游判例族的阴性对照：洄游改配置不改 Response 拓扑，
无 Reaction Path 购买）
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

- 使用的自由度：census PLAIN 族投影标签与 4 槽 typed 因子实例语义（census 冻结槽序/常量 spawn_factors/diet_breadth）；Profile 命名；伪脚本步序（槽序 unordered、Combine 拓扑族固定）。
- 放弃的自由度：(1) 产卵洄游 body 内分支（P05 判例配置级——若 review 改判需 IF，结构结论复核，census open_semantics 原样）；(2) 体型分级 Group 化（trait/condition 不拆供给）；(3) 合并算子数学（OPERATOR UNDEFINED 待机制侧）；(4) 数值与 Profile 值域不冻结。
- 跨批关系：本鱼 P01+P05 双 Pattern——P01 侧（机会主义宽谱）与 P05 侧（体型分级+洄游配置切换）已在本文件一体表达（census 单 Story 快照承载四面，不拆两文件）；本鱼 potamodromous 配置级处理是湄公鲶（MGC）/grazing 批引用的 CHB 先例源，两批读法一致。

BATCH_ID: REP-FULL-MIGRA-001
