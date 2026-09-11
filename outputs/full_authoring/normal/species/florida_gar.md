# 佛罗里达雀鳝（Florida Gar｜Lepisosteus platyrhincus）｜植被边缘伏击四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：伏击组） |
| Story | FISH-R02-S17｜佛罗里达雀鳝｜植被边缘伏击与浅水季节窗口（census CENSUS-B2 快照全文在案） |
| 冻结 Pattern | P01（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：孤僻、晨昏活跃、肉食性、营养级 3.72（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-FGA-BAKE（SINGLE 族成员：植被结构栖息因子，静态）+ P-B2-FGA-RESP（TYPED 族标准成员：轮廓/停顿/结构 context） |
| 亚结构组 | 伏击型（ambush/structure typed）——本组 Tier A 样板 |

## 0. 上游语义与摄食形态

- 摄食形态：植被边缘伏击（植被结构栖息因子，静态）。census Bake 面判语原样：植被结构栖息因子（静态；季节水温窗口＝活性 condition premise 非空间分支；SINGLE 成员）。
- 季节水温窗口的处理：浅水季节窗口是活性 condition（premise），不是空间分支——本文件按 census 判语将其表达为 Response/活性层 premise 参数，不建 Bake 分支（结构因子不随季节换轴）。
- Response 面：TYPED 族标准成员（轮廓/停顿/结构 context——census 判语原样）。伏击形态的 typed evaluator 差异（对静止/轮廓呈现的接受窗）全部是 Profile 参数宽度，不是新拓扑。
- Group 面：census NO_SURFACE_EFFECT（无供给拆分）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier A）**：判断链＝GATE_VEGETATION_EDGE 门（植被缘掩体存在，不成立=EARLY_RETURN） → 掩体结构档位（三档分级命中） → 归一化。水温/光照/时段等通用因子未入链（CSV 锚无 Story 空间程序证据——§5.1 例序是模板示例不是证据，不冒充）。

Profile 引用清单：@FgaVegetationStructureProfile @FgaPreyFields @FgaDietClasses @FgaSizeWindow @FgaShallowSeasonActivityProfile @FgaNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Fga_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；本组 Tier A 样板文件；**§2.2 已顺序还原（REP-ORDER-FIX-004）：early return 链+分级命中，登记 README §7**） |
| FactorType(typed) | structure_factor：植被边缘结构轴（植被缘/掩体贴近；typed 实例——census P-B2-FGA-BAKE 实例常量） |
| FactorBinding | season premise：浅水季节窗口＝活性 condition premise（值域由 Profile 层定值；不建 body 分支——census 判语：非空间分支） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@FgaPreyFields；diet_classes=@FgaDietClasses；size_window=@FgaSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed structure factor（B-T1 Independent Factor Set 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝GATE_VEGETATION_EDGE 门（植被缘掩体存在） → 掩体结构档位 → 归一化；掩体档分级命中
（最适伏击=全额/次级掩体=削减不清零/暴露=出局 EARLY_RETURN），门不成立直接
EARLY_RETURN。伏击型第一判断＝结构掩体（无掩体不伏击），与追击型（猎物场+
栖息双槽）、机会型（食物丰度先行）、夜行型（底板+光照槽）的顺序差异本身=
LogicTemplate 判据。顺序来源＝census 冻结全四面判定快照（Tier A 骨架在案、档位成员不在快照，段成员 [需正文]）——Story 正文到达后校准（census 侧 SINGLE
族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的植被结构轴事实（植被缘/掩体贴近）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@FgaPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@FgaDietClasses 食性过滤
      与 size_window=@FgaSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（浅水季节窗口——活性 condition premise，非空间分支）

第 1 步 GATE_VEGETATION_EDGE（植被缘掩体存在——伏击型第一判断：无可用掩体不伏击）：
    用该 typed 因子轴事实查询 @FgaVegetationStructureProfile 的掩体存在分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 格子存在植被缘/掩体结构（植被线/草缘贴近）：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：格子无植被掩体结构——伏击型结构掩体先行判据）

第 2 步 掩体结构档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用该 typed 因子轴事实查询 @FgaVegetationStructureProfile 的掩体伏击分档槽
    （植被缘伏击质量：掩体内侧/植被缘/结构边缘；档位成员=Profile 值域不冻结 [需正文]）
    如果 掩体结构 ∈ 最适伏击档（preferred 槽）：
        VegetationEdgeFit = 全额
    否则如果 ∈ 次级掩体档（tolerated 槽）：
        VegetationEdgeFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（暴露无掩体档）：
        返回 0（EARLY_RETURN：暴露格子不承载伏击分布）

第 3 步 NORMALIZE_WEIGHT：
    对 VegetationEdgeFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；本文件 = 伏击组样板（同组其余文件按此骨架参数差异化）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @FgaNormalFeedingProfile + @FgaShallowSeasonActivityProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前季节窗口 premise（活性 condition——浅水季节窗口，参数级）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（轮廓/停顿/结构 context——census 判语原样）评价 @FgaNormalFeedingProfile
    得到 FoodEvaluation
    （季节窗口作为活性 premise 并入评价参数，不是独立通道）

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@FgaNormalFeedingProfile 值域不冻结）：
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（植被边缘结构轴——census 冻结实例常量）；Profile 命名；顺序还原链序与档位结构（REP-ORDER-FIX-004：门先行 EARLY_RETURN+掩体档三档分级命中）；季节窗口的 premise 归层（census 判语照录）。
- 放弃的自由度：(1) 季节窗口的 Bake 分支化（census 判语：活性 condition premise 非空间分支）；(2) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。
- 本文件为本批伏击组 Tier A 样板：同组 Tier B 文件的骨架由此参数差异化，不重复引用本文件。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 门先行 EARLY_RETURN+掩体档三档分级命中，Response DECIDE 档位展开）
