# 鳜鱼（Mandarin Fish｜Siniperca chuatsi）｜结构伏击追捕四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：伏击组） |
| Story | FISH-R03｜鳜鱼｜Mandarin Fish｜Discrete Target（census CENSUS-B2 快照全文在案；input_status=frozen_status_confirmed——FISH-R03-RECON-001 + FISH-MAINT-FIX-001） |
| 冻结 Pattern | P01 + P02（census B2 stories.jsonl 快照；本文件表达 P01 主面，P02 侧归后续场摄食批） |
| 物种属性锚 | fish-reference-20260908：追猎、全天活跃、肉食性、营养级 4.45（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-MDF-BAKE（**PLAIN 族第 5 成员**：结构+深度(低温绑定) 2 因子）+ P-B2-MDF-RESP（TYPED 族强实例：motion-triggered——静止不触发/移动触发追捕，FAO 实证） |
| 亚结构组 | 伏击型（ambush/structure typed）＋鱼食性/体型分级维度（营养级 4.45 piscivore——size_window 参数组标记） |

## 0. 上游语义与摄食形态

- 摄食形态：结构+深度双因子伏击（census P-B2-MDF-BAKE：结构+深度(低温绑定) 2 因子，PLAIN 第 5 成员——本批唯一 PLAIN 标签伏击文件，其余伏击组文件为 SINGLE 单因子形态）。
- 夜间摄食的处理：census 判语原样——夜间摄食＝活性 condition（非空间分支）。本文件不建夜行低光槽（那是 NOCTURNAL 组族域），活性/时段并入 Response 参数。
- Response 面：TYPED 族强实例 motion-triggered（静止不触发/移动触发追捕——FAO 实证，census 判语原样）。这是 TYPED 族 evaluator 参数的强差异实例，不是新拓扑（census 判同在案）。
- Group 面：census NO_SURFACE_EFFECT（无足够物种级证据升级 FishMode——census 判语原样）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围；P02 侧不在本文件表达）。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier A）**：判断链＝受限还原——因子槽间顺序按 census PLAIN 族 unordered 契约不主张（改槽序=结构变更需重审）；每槽三档分级命中（excluded=出局槽值进 COMBINE 非 EARLY_RETURN——族域边界）。槽间先后不在本文件主张（HRQ-07 unordered 提案维持）；水温/时段等通用因子未入链。

Profile 引用清单：@MdfStructureFactorProfile @MdfDepthColdFactorProfile @MdfPreyFields @MdfDietClasses @MdfSizeWindow @MdfNightActivityProfile @MdfNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Mdf_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census PLAIN 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；因子集→组合；本标签本批唯一使用文件＝census 在案 PLAIN 第 5 成员；**§2.2 已顺序还原（REP-ORDER-FIX-004）：槽内三档分级命中——槽间顺序按族契约 unordered 不还原，登记 README §7**） |
| Factor1Type(typed) | structure_factor：结构掩体轴（岩礁/沉木/结构贴近；typed 实例——census P-B2-MDF-BAKE 实例常量） |
| Factor2Type(typed) | habitat_factor：深度轴·低温绑定（census 实例常量：深度因子带低温 premise 绑定；值域由 Profile 层定值） |
| FactorBinding | season premise：低温期深度偏好偏移（premise 配置级；不建 body 分支） |
| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@MdfPreyFields；diet_classes=@MdfDietClasses；size_window=@MdfSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set 双因子形态（§13.2 结构族读法；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按 authoring_work_standards §5.1 做受限顺序
还原：census PLAIN 族 open_semantics 判语＝因子槽间顺序 unordered（HRQ-07 提案）——
不把双槽改成 early return 链（改槽间顺序＝结构变更需重审，不发明）。还原内容＝
每槽因子评估展开为三档分档槽判定（preferred=全额/tolerated=削减不清零/
excluded=出局槽值）。**族域边界：PLAIN 槽的 excluded 档落槽值出局而非
EARLY_RETURN**——槽无 gate 语义（族边界禁 gate），出槽值仍进 COMBINE。
追击型判断主体＝猎物场+栖息双槽（vs 伏击型掩体先行/机会型食物丰度先行/
夜行型底板+光照槽——组间顺序差异本身=LogicTemplate 判据）。档位成员=Profile
值域不冻结 [需正文]。

读取 当前格子的结构掩体轴事实（岩礁/沉木/结构贴近）
读取 当前格子的深度轴事实（低温 premise 绑定的深度偏好）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@MdfPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@MdfDietClasses 食性过滤
      与 size_window=@MdfSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（低温期——深度因子绑定的 premise，配置级）

槽 1 EVAL_TYPED_FIELD_OR_FACTOR（structure_factor，分级命中）：
    用structure_factor事实查询 @MdfStructureFactorProfile 的结构分档槽
    （结构掩体轴·岩礁/沉木/结构贴近；typed 实例——census P-B2-MDF-BAKE 实例常量；档位成员=Profile 值域不冻结 [需正文]）
    如果 结构 ∈ 最适档（preferred 槽）：
        StructureFit = 全额
    否则如果 ∈ 次级档（tolerated 槽）：
        StructureFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        StructureFit = 出局槽值（excluded——非 EARLY_RETURN，出槽值仍进 COMBINE；
        PLAIN 族域内槽无 gate 语义）

槽 2 EVAL_TYPED_FIELD_OR_FACTOR（habitat_factor，分级命中）：
    用habitat_factor事实查询 @MdfDepthColdFactorProfile 的栖息分档槽
    （深度轴·低温绑定·census 实例常量：深度因子带低温 premise 绑定；值域由 Profile 层定值；档位成员=Profile 值域不冻结 [需正文]）
    如果 栖息 ∈ 适配档（preferred 槽）：
        DepthColdFit = 全额
    否则如果 ∈ 过渡档（tolerated 槽）：
        DepthColdFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        DepthColdFit = 出局槽值（excluded——非 EARLY_RETURN，同上族域边界）

COMBINE_WEIGHTED：
    合并两个 FactorFit
算子标注：OPERATOR UNDEFINED — 待机制侧（多因子合并算子；live §15.3 同款占位声明；
census PLAIN 族因子间顺序 unordered，槽展示顺序不改变结果）

返回 SpatialDistributionWeight（受限还原结束：槽内有分级命中；无链序、无 gate、
无 early return——族 forbidden_freedoms 边界（census open_semantics unordered 判语维持）；
单因子属 SINGLE 族域，硬约束属 HARD_GATED 族域）
```

### 2.3 live 层投影声明

census PLAIN 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；B-T1 Independent Factor Set 双因子读法（§13.2）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影——motion-triggered 强实例）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；motion-triggered 强实例） | @MdfNormalFeedingProfile + @MdfNightActivityProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 目标运动状态事实（静止/移动——motion-triggered 评价输入）
读取 当前活性 premise（夜间摄食＝活性 condition——census 判语原样，参数级）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @MdfNormalFeedingProfile
    （motion-triggered：静止目标不触发追捕档位，移动目标触发追捕——
      FAO 实证，census 判语原样；作为 evaluator 参数宽度，不是新通道）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@MdfNormalFeedingProfile 值域不冻结）：
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

- 使用的自由度：census PLAIN 族投影标签（本批唯一，census 在案第 5 成员）；typed 因子实例语义（结构+深度低温绑定——census 冻结实例常量）；motion-triggered evaluator 参数；Profile 命名。
- 放弃的自由度：(1) 夜间摄食的空间槽化（census 判语：活性 condition 非空间分支——低光槽形态归 NOCTURNAL 组族域，本文件不使用）；(2) 合并算子数学（OPERATOR UNDEFINED）；(3) P02 侧场摄食面（归后续场摄食批，本文件不冒充）；(4) 数值与 Profile 值域不冻结。
- CSV 性格锚「追猎」与本组（伏击）归属的张力已登记：census 冻结程序（结构+深度伏击因子、motion-triggered 追捕）优先于 CSV 习性行（README §4 登记项 5）。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 槽内三档分级命中——槽间顺序按族契约 unordered 不还原，Response DECIDE 档位展开）
