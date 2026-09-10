# 江鳕（Burbot｜Lota lota）｜夜行低光四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（P01 普通层＝全库最大 Pattern 群 第 6 批：第二轮全量闭合——夜行组） |
| Story | REV-001 F1 跳行点名（REP-FULL-NORM2-001 handoff 转录；CSV 行 245） |
| 冻结 Pattern | P01 [需核对]（CSV 方向锚归层） |
| 物种属性锚 | fish-reference-20260908：追猎、夜间活跃、肉食性、营养级 3.84、demersal（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照；第一轮交付包 outputs/full_authoring/normal/） |
| 证据档 | Tier B+（点名锚；[需核对]） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；光照/低光 cue 参数并入；Reaction 槽 OFF） |
| 亚结构组 | 夜行/低光型（nocturnal/low-light typed） |

## 0. 上游语义与摄食形态

- 摄食形态：江鳕（石底深潭冬夜伏击）。
- 证据边界：Story 行级 Pattern 标签不在本地 [需核对]；本文件结构为夜行组样板（第一轮 Tier A 样板骨架）的表达层选择——Story 正文到达后 census 判同可能改判（换组/换 BakeTemplate/换 Response 拓扑＝**结构变更需重审**，validator 族边界拦截静默改写），不是 Profile 重绑定。
- Response 面：R-T1 Feeding-only + 光照/低光 Cue 参数（live §11.5 判例原样：RR-1 Feeding-only + LightAvailability / Cue Profile——低光不另开通道）；TYPED 族参数差异（夜相底栖贴近/振动呈现——组样板参数）。
- Group 面 / Quality 面：组样板 NO_SURFACE_EFFECT。
- 表达超集说明：骨架参数化表达；未超出组样板族域。

Profile 引用清单：@BRBNightHabitatProfile @BRBLowLightSpatialProfile @BRBPreyFields @BRBDietClasses @BRBSizeWindow @BRBNormalFeedingProfile @BRBLightCueProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| BRB_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族低光侧投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-NOCTURNAL-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT 低光侧；live §11.5 判例：MERGE_SUPPORTED → BA-T1 + 低光空间槽，BakeTemplate +0——第一轮定型，本批零新族） |
| FactorType(typed) | habitat_factor：石底深潭冬夜底板轴（鳕科淡水低温夜行方向） |
| SpatialSlotProfile | @BRBLowLightSpatialProfile（低光空间槽——live §11.5 DynamicSpatialSlot 判例） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BRBPreyFields；diet_classes=@BRBDietClasses；size_window=@BRBSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@BRBLowLightSpatialProfile（live §11.5 原样判例读法；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的habitat_factor事实（石底深潭冬夜底板轴（鳕科淡水低温夜行方向））
读取 当前格子的低光空间事实（低光/夜相空间槽——DynamicSpatialSlot）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BRBPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@BRBDietClasses 食性过滤
      与 size_window=@BRBSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用habitat_factor事实查询 @BRBNightHabitatProfile
    得到 RockNightDeepPoolFit

APPLY_DYNAMIC_SPATIAL_SLOT：
    用低光空间事实调整分布权重（低光槽——§11.5 判例形态，非作者可选算子）

NORMALIZE_WEIGHT：
    对调整后权重执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子+低光槽链结束：无 gate、无 combine 步——族边界）
```

### 2.3 live 层投影声明

live §11.5 判例原样（MERGE_SUPPORTED → BA-T1 + DynamicSpatialSlot，BakeTemplate +0；VISIBILITY-LIMITED-FEEDING 家族候选成员）；census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @BRBNormalFeedingProfile + @BRBLightCueProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前低光可用性 / 光照 cue 事实（LightAvailability——§11.5 判例的 Cue Profile 输入，参数级并入 Feeding 评价）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（夜相底栖贴近/振动呈现——组样板参数）评价 @BRBNormalFeedingProfile
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

- 使用的自由度：SINGLE/PLAIN 族投影标签与 typed 因子实例语义；Profile 命名；伪脚本步序（canonical 固定）。
- 放弃的自由度：(1) 归族裁决权移交（无 census 快照——Story 正文到达后判同可能改判，结构变更需重审）；(2) 合并算子（无 combine 步或 OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-NORM2-001
