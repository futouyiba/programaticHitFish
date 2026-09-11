# 黑鮰（Black Bullhead Catfish｜Ameiurus melas）｜夜行低光四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（P01 普通层＝全库最大 Pattern 群 第 6 批：第二轮全量闭合——夜行组） |
| Story | R 系批成员（批归属未在本地 [需核对]；CSV 行 258） |
| 冻结 Pattern | P01 [需核对]（CSV 方向锚归层） |
| 物种属性锚 | fish-reference-20260908：孤僻、夜间活跃、肉食性、营养级 3.81、demersal（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照；第一轮交付包 outputs/full_authoring/normal/） |
| 证据档 | Tier B（CSV 方向锚；[需核对]） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；光照/低光 cue 参数并入；Reaction 槽 OFF） |
| 亚结构组 | 夜行/低光型（nocturnal/low-light typed） |

## 0. 上游语义与摄食形态

- 摄食形态：黑鮰（植被池沼夜行）。
- 证据边界：Story 行级 Pattern 标签不在本地 [需核对]；本文件结构为夜行组样板（第一轮 Tier A 样板骨架）的表达层选择——Story 正文到达后 census 判同可能改判（换组/换 BakeTemplate/换 Response 拓扑＝**结构变更需重审**，validator 族边界拦截静默改写），不是 Profile 重绑定。
- 附加注记：同属云斑鮰（第一轮夜行组）互指——判例不继承。
- Response 面：R-T1 Feeding-only + 光照/低光 Cue 参数（live §11.5 判例原样：RR-1 Feeding-only + LightAvailability / Cue Profile——低光不另开通道）；TYPED 族参数差异（夜相底栖贴近/气味饵呈现——组样板参数）。
- Group 面 / Quality 面：组样板 NO_SURFACE_EFFECT。
- 表达超集说明：骨架参数化表达；未超出组样板族域。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier B）**：判断链＝夜行底板栖息档位（三档，无底板=EARLY_RETURN） → 低光/夜相槽档位（槽内三档，槽位置=§11.5 判例固定原位） → 归一化。光照/时段先行语义由槽内档位与 Response 面 LightAvailability cue 双承载（槽位置提前=改判例结构需重审，张力登记 README §7）。

Profile 引用清单：@BBHNightHabitatProfile @BBHLowLightSpatialProfile @BBHPreyFields @BBHDietClasses @BBHSizeWindow @BBHNormalFeedingProfile @BBHLightCueProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| BBH_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-NOCTURNAL-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT 低光侧；live §11.5 判例：MERGE_SUPPORTED → BA-T1 + 低光空间槽，BakeTemplate +0——第一轮定型，本批零新族；**§2.2 已顺序还原（REP-ORDER-FIX-004）：底板档三档+低光槽内三档（槽位置按 §11.5 判例原位），登记 README §7**） |
| FactorType(typed) | habitat_factor：泥底植被池沼夜行底板轴（小型须系夜行方向） |
| SpatialSlotProfile | @BBHLowLightSpatialProfile（低光空间槽——live §11.5 DynamicSpatialSlot 判例） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BBHPreyFields；diet_classes=@BBHDietClasses；size_window=@BBHSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@BBHLowLightSpatialProfile（live §11.5 原样判例读法；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝夜行底板栖息档位 → 低光/夜相槽档位 → 归一化。光照+时段＝夜行型第一
环境判据（夜行组方向锚）；表达层槽位置＝live §11.5 判例固定（DynamicSpatialSlot
槽位由判例固定合入，非作者可选）——光照先行语义由槽内三档与 Response 面
LightAvailability cue 双承载，槽位置提前＝改判例结构需重审（张力登记 README §7）。
族域边界：槽＝调整器非 gate——亮水档落极低削减不清零，出局语义落 typed 因子
（无夜行底板=EARLY_RETURN）。推导来源＝CSV 方向锚级推导（[需正文]）；档位成员=Profile 值域不冻结 [需正文]。

读取 当前格子的habitat_factor事实（泥底植被池沼夜行底板轴（小型须系夜行方向））
读取 当前格子的低光空间事实（低光/夜相空间槽——DynamicSpatialSlot）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BBHPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@BBHDietClasses 食性过滤
      与 size_window=@BBHSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 夜行底板栖息档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用habitat_factor事实查询 @BBHNightHabitatProfile 的夜行底板分档槽
    （泥底植被池沼夜行底板轴·小型须系夜行方向；档位成员=Profile 值域不冻结 [需正文]）
    如果 栖息 ∈ 夜行底板档（preferred 槽）：
        WeedyNightHabitatFit = 全额
    否则如果 ∈ 次级夜栖档（tolerated 槽）：
        WeedyNightHabitatFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（无夜行底板档）：
        返回 0（EARLY_RETURN：无夜行底板的格子出局——夜行型栖息底板判据）

第 2 步 低光/夜相槽档位（APPLY_DYNAMIC_SPATIAL_SLOT 槽内三档——光照+时段判据；
  槽位置=live §11.5 判例固定原位，非作者可选）：
    用低光空间事实查询 @BBHLowLightSpatialProfile 的低光分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 光照/时段 ∈ 夜相低光档（preferred 槽）：
        低光槽全额合入（槽位＝判例固定）
    否则如果 ∈ 晨昏过渡档（tolerated 槽）：
        低光槽削减合入（× Profile 衰减参数——削减但不清零）
    否则（亮水日间档）：
        低光槽极低削减合入（削减但不清零——槽=调整器非 gate，
        出局语义不落槽内）

第 3 步 NORMALIZE_WEIGHT：
    对 WeedyNightHabitatFit（含低光槽合入调整）执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live §11.5 判例原样（MERGE_SUPPORTED → BA-T1 + DynamicSpatialSlot，BakeTemplate +0；VISIBILITY-LIMITED-FEEDING 家族候选成员）；census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @BBHNormalFeedingProfile + @BBHLightCueProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前低光可用性 / 光照 cue 事实（LightAvailability——§11.5 判例的 Cue Profile 输入，参数级并入 Feeding 评价）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（夜相底栖贴近/气味饵呈现——组样板参数）评价 @BBHNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@BBHNormalFeedingProfile 值域不冻结）：
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

- 使用的自由度：SINGLE/PLAIN 族投影标签与 typed 因子实例语义；Profile 命名；顺序还原链序与档位结构（REP-ORDER-FIX-004：夜行底板档三档+低光槽内三档——槽位置按 §11.5 判例原位）。
- 放弃的自由度：(1) 归族裁决权移交（无 census 快照——Story 正文到达后判同可能改判，结构变更需重审）；(2) 合并算子（无 combine 步或 OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。
- 放弃的自由度：(4) 名单身份/口径张力项的裁决权（见 §0 附加注记与 README 排除表——登记在案不冒充）。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM2-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 夜行底板档三档+低光槽内三档——槽位置按 §11.5 判例原位，Response DECIDE 档位展开）
