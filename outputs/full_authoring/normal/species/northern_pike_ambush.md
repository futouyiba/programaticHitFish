# 白斑狗鱼（Northern Pike｜Esox lucius）｜植被伏击四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：伏击组） |
| Story | B01-S18｜白斑狗鱼｜植被伏击（**Story 名与语义由批内互指标定**：census CENSUS-B1-PIK Bake 判语「植被伏击属 S18 另一条 Story」+ migration 批 northern_pike_spawn.md §5「S18 植被伏击（另 Story）不在此承载」双源互指；S18 本身无 census 快照） |
| 冻结 Pattern | P01（批内互指标定；[需核对] Story DB 行级标签） |
| 物种属性锚 | fish-reference-20260908：水温 10–28℃、最适 19℃、pelagic、晨昏活跃、肉食性、追猎、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B+（批内双源互指标定 Story 身份；结构按伏击组 Tier A 样板参数化；条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| 亚结构组 | 伏击型（ambush/structure typed）＋鱼食性/体型分级维度（piscivore） |
| Story 限定 | 文件名 _ambush 后缀＝Story 限定：S19（P05，migration 批）/S20（捕获边界，本批 northern_pike_strike.md）不属本文件范围 |

## 0. 上游语义与摄食形态

- 摄食形态：植被伏击（掩体贴近等待→短程出击）。空间语义＝植被结构单因子（S18 侧），与 S20 的 Static Habitat（无空间新证据）是同种两条 Story 的两个 Bake 读法（census 判语互指原样）。
- 证据边界：S18 无 census 快照——本文件结构为伏击组样板（florida_gar.md 骨架）的表达层选择；Story 正文到达后若判多因子/带硬约束＝换 BakeTemplate 值 + 增/删行＝**结构变更需重审**（validator 族边界拦截静默改写），不是 Profile 重绑定。
- Response 面：TYPED 族伏击参数（轮廓/停顿/结构贴近 context——组样板语义）。
- Group 面 / Quality 面：按组样板 NO_SURFACE_EFFECT。
- 表达超集说明：本文件为骨架参数化表达（Tier B+）；未超出组样板族域。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier B+）**：判断链＝GATE_VEGETATION_COVER 门（沉水植被/草洞掩体存在，不成立=EARLY_RETURN） → 掩体结构档位（三档分级命中） → 归一化。水温/光照/时段等通用因子未入链（CSV 锚无 Story 空间程序证据——§5.1 例序是模板示例不是证据，不冒充）。

Profile 引用清单：@PikVegetationAmbushProfile @PikPreyFields @PikDietClasses @PikSizeWindow @PikAmbushFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| PikA_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；**§2.2 已顺序还原（REP-ORDER-FIX-004）：early return 链+分级命中，登记 README §7**） |
| FactorType(typed) | structure_factor：植被掩体结构轴（沉水植被缘/草洞贴近；typed 实例——S18 植被伏击语义，批内互指标定） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@PikPreyFields；diet_classes=@PikDietClasses；size_window=@PikSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed structure factor（B-T1 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝GATE_VEGETATION_COVER 门（沉水植被/草洞掩体存在） → 掩体结构档位 → 归一化；掩体档分级命中
（最适伏击=全额/次级掩体=削减不清零/暴露=出局 EARLY_RETURN），门不成立直接
EARLY_RETURN。伏击型第一判断＝结构掩体（无掩体不伏击），与追击型（猎物场+
栖息双槽）、机会型（食物丰度先行）、夜行型（底板+光照槽）的顺序差异本身=
LogicTemplate 判据。顺序来源＝批内互指/点名锚方向级推导（[需正文]）——Story 正文到达后校准（census 侧 SINGLE
族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的植被结构轴事实（沉水植被缘/草洞贴近）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@PikPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@PikDietClasses 食性过滤
      与 size_window=@PikSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 GATE_VEGETATION_COVER（沉水植被/草洞掩体存在——伏击型第一判断：无可用掩体不伏击）：
    用该 typed 因子轴事实查询 @PikVegetationAmbushProfile 的掩体存在分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 格子存在沉水植被缘/草洞掩体结构：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：格子无植被掩体结构——伏击型结构掩体先行判据）

第 2 步 掩体结构档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用该 typed 因子轴事实查询 @PikVegetationAmbushProfile 的掩体伏击分档槽
    （植被掩体贴近质量：掩体内/植被缘开阔侧；档位成员=Profile 值域不冻结 [需正文]）
    如果 掩体结构 ∈ 最适伏击档（preferred 槽）：
        VegetationAmbushFit = 全额
    否则如果 ∈ 次级掩体档（tolerated 槽）：
        VegetationAmbushFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（暴露无掩体档）：
        返回 0（EARLY_RETURN：暴露格子不承载伏击分布）

第 3 步 NORMALIZE_WEIGHT：
    对 VegetationAmbushFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @PikAmbushFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（轮廓/停顿/植被边缘贴近 context——伏击组样板参数）评价 @PikAmbushFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@PikAmbushFeedingProfile 值域不冻结）：
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

- 使用的自由度：SINGLE 族投影标签与 typed 因子实例语义（植被掩体结构轴）；Profile 命名；顺序还原链序与档位结构（REP-ORDER-FIX-004：门先行 EARLY_RETURN+掩体档三档分级命中）。
- 放弃的自由度：(1) 归族裁决权移交（S18 无 census 快照——Story 正文到达后 census 判同可能改判 PLAIN/GATED，结构变更需重审）；(2) 合并算子（无 combine 步；OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。
- 同种三 Story 分工（S18/S19/S20 三文件三批）互指闭合（README §3 登记 6）。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 门先行 EARLY_RETURN+掩体档三档分级命中，Response DECIDE 档位展开）
