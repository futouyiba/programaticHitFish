# 剑旗鱼（Swordfish｜Xiphias gladius）｜昼夜垂直迁移四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | FISH-R02-S23｜剑旗鱼｜昼夜垂直迁移与深层猎物追击（census CENSUS-B2 快照全文在案）。文件名 _diel 后缀＝Story 限定（本文件只表达 S23 昼夜垂直迁移面；同种其它 Story 若存在另立） |
| 冻结 Pattern | P05（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 5–27℃、最适 16℃、pelagic-oceanic、深 0–2878m、全天活跃、肉食性、追猎、oceanodromous、海水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-SWO-BAKE（SINGLE 族成员：昼夜垂直迁移水层因子，diel 绑定切换）+ P-B2-SWO-RESP（TYPED 族标准成员，水层匹配=呈现参数） |

## 0. 上游语义与洄游形态

- 洄游形态：昼夜垂直迁移（diel vertical migration——夜间上浮表层↔昼间下潜深层追击猎物）；FishModePressure=Candidate 不购买（census Group 面判语原样：NO_SURFACE_EFFECT）。
- Bake 面：水层因子单链 diel premise 绑定（census P-B2-SWO-BAKE：昼夜垂直迁移水层因子，SINGLE 族成员）。
- **coverage delta #24 登记项（NEEDS_REGRESSION_SAMPLE，本批原样携带）**：剑旗鱼是 #24 的 2D 定向样本——迁移驱动未闭合（Story 正文无「迁移驱动」节），census 骨架按 premise 绑定处理，**2D 判据留 representation 线**（若迁移定向语义要求 2D 表达能力=表达层回归样本，本批不闭合）。
- Response 面：TYPED 族标准成员（水层匹配=呈现参数——census 判语原样）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围；2D 回归登记为 OPEN 不在本批闭合）。

Profile 引用清单：@SwordfishDielSpatialProfile @SwordfishPreyFields @SwordfishDietClasses @SwordfishSizeWindow @SwordfishNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——FishModePressure=Candidate 不购买）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| SwordfishDiel_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | habitat_factor：昼夜垂直迁移水层因子（表层↔深层；typed 实例，diel 驱动——census P-B2-SWO-BAKE 实例常量） |
| FactorBinding | lifecycle premise：diel 配置级切换（夜间表层↔昼间深层；值域由 Profile 层定值；不建 body 分支——迁移驱动语义未闭合，coverage #24 登记） |
| SpatialSlotProfile | @SwordfishDielSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@SwordfishPreyFields；diet_classes=@SwordfishDietClasses；size_window=@SwordfishSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@SwordfishDielSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的水层事实（昼夜垂直迁移轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@SwordfishPreyFields 绑定的头足类/深海鱼类 prey class 生物量，
      经 diet_classes=@SwordfishDietClasses 食性过滤
      与 size_window=@SwordfishSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（diel——上游昼夜事实，配置级切换因子集）

EVAL_TYPED_FIELD_OR_FACTOR：
    用水层事实查询 @SwordfishDielSpatialProfile
    得到 DielSpatialFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 DielSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；迁移驱动 2D 判据=coverage #24 回归登记，本批不闭合）
```

### 2.3 live 层投影声明

live BA 句型层无昼夜垂直迁移专用句型；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；coverage delta #24 NEEDS_REGRESSION_SAMPLE 原样携带（2D 定向判据留 representation 线）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @SwordfishNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @SwordfishNormalFeedingProfile（水层匹配=呈现参数——census 判语原样）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（昼夜垂直迁移水层 diel 绑定——census 冻结实例常量）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 2D 定向表达能力（coverage #24 NEEDS_REGRESSION_SAMPLE——迁移驱动未闭合，回归样本归 representation 线，本批按 premise 绑定骨架表达）；(2) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。
- 跨层登记：R08 摘要「旗鱼喙击打保守降 Open 留 FR3」＝旗鱼科喙击打捕获段判例（Capture Boundary 域）——与剑旗鱼 S23 昼夜垂直迁移面不同面别（post-instantiation owner），不在本文件承载。

BATCH_ID: REP-FULL-MIGRA-001
