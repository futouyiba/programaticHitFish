# 褐鳟·摄食位置竞争（Brown Trout｜Salmo trutta）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| Story | B01-S14｜褐鳟｜摄食位置竞争与中心—边缘资源分配（census CENSUS-B1-BRT 快照全文在案；Story 页 3d6a4137d236812dadf2c2e5d3260f47；受控异种配对实验证据，census confidence=MEDIUM 原样携带）。同种另 Story B01-S12（P01 普通摄食季节脉冲）已由 normal 批 brown_trout.md 承载——双文件分工互指（白斑狗鱼三 Story 三文件先例），本文件不重复 S12 面 |
| 冻结 Pattern | P02（census B1 stories.jsonl 快照 frozen_patterns） |
| 物种属性锚 | fish-reference-20260908 行 262：pelagic-neritic、肉食性、晨昏活跃、追猎、anadromous、营养级 3.36（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结 P-B1-BRT-BAKE/P-B1-BRT-RESP） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-BRT-BAKE（PLAIN 族第 3 成员：patch+rank 2 槽，combine=WEIGHTED_FACTORS；依赖 HRQ-B1-04 双轴扩容——槽位数伸缩+EVAL_RANK_POSITION_PREFERENCE 新具名 typed 因子类型准入）+ P-B1-BRT-RESP（TYPED 标准成员） |

## 0. 上游语义与位置竞争形态

- 摄食形态：食物 patch 强度评估 + 个体 rank 位置偏好因子加权组合——优势个体偏向 patch 中心，次级个体边缘化（core-vs-edge，census 盲体实例常量原样）；竞争性占位以个体属性因子表达，不是独立争食 Mode（census owner 推论）。
- rank premise：individual_rank=优势等级（个体 Condition/Relation fact，上游）；持久写回为 Open Question（TAR-05 未定——census open_semantics 原样：若产品不实现 rank 状态，程序体退化为纯 patch 形，族归属翻案）。
- conflict path：Story 明言「明显攻击并不多」，conflict 路径证据不足不建（census 判语原样）。
- **两层登记（rank 因子 vs share-vector）**：中心—边缘分配的 Group 侧替代读法=同条件多路由 Share Vector（coverage_delta report §2.1；live §7 契约+§15.1）；census 判定选 Bake 侧 rank 因子（Group 面 NO_SURFACE_EFFECT）。两层是同一现实的两个表达层，HRQ-B1-04 联合裁决 OPEN——本文件按 census 表达，不在表达层闭合。
- Group 面：census NO_SURFACE_EFFECT（个体 Condition/Relation 而非独立争食 Mode——owner 推论；GroupPressure=None）。
- Response 面：TYPED 标准成员（位置背景影响可及食物——position_context premise，参数级无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@BrtPatchCompetitorProfile @BrtRankPositionProfile @BrtPreyFields @BrtDietClasses @BrtSizeWindow @BrtNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：个体 Condition/Relation 而非独立争食 Mode，GroupPressure=None；Group 侧 share-vector 替代读法见 §0 两层登记——裁决归机制侧）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Brt_Position_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P02-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；typed 因子集→组合——本标签本批唯一使用文件＝census 在案 PLAIN 第 3 成员） |
| Factor1Type(typed) | resource_patch：食物位置分布轴（census premise resource_patch=食物位置分布；盲体槽1 op=EVAL_RESOURCE_PATCH——族判同实例化名） |
| Factor2Type(typed) | individual_rank：优势等级→patch 中心-边缘位置偏好轴（census 盲体槽2 op=EVAL_RANK_POSITION_PREFERENCE——新具名 typed 因子类型，首个个体属性调制因子，**准入待批 HRQ-B1-04**；rank fact 产品持久写回未定 TAR-05） |
| FactorBinding | 常年绑定（rank premise 为个体 Condition/Relation 上游 fact，非 lifecycle/season 切换） |
| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BrtPreyFields；diet_classes=@BrtDietClasses；size_window=@BrtSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set 双因子形态（§13.2 结构族读法）+ Group 侧 share-vector 替代读法（§7/§15.1，HRQ-B1-04 联合裁决 OPEN——README §3 登记 4） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物位置分布轴事实（食物 patch 强度）
读取 当前个体 rank premise（individual_rank=优势等级——上游个体 Condition/Relation fact）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BrtPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@BrtDietClasses 食性过滤
      与 size_window=@BrtSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR（槽1）：
    用食物 patch 强度事实查询 @BrtPatchCompetitorProfile
    得到 PatchFit

EVAL_RANK_POSITION_PREFERENCE（槽2）：
    用个体 rank premise 查询 @BrtRankPositionProfile
    得到 RankPositionFit
    （优势个体偏向 patch 中心、次级个体边缘化——core-vs-edge；
      具名 op 待批 HRQ-B1-04：首个个体属性调制因子，factor 轴语义边界扩展）

COMBINE_WEIGHTED：
    合并 PatchFit 与 RankPositionFit
算子标注：OPERATOR UNDEFINED — 待机制侧（多因子合并算子；live §15.3 同款占位声明）

返回 SpatialDistributionWeight（因子集链结束：无 gate、无归一化步——族边界）
退化条款：若产品不实现 rank 状态（TAR-05 未定），槽2 退化为常量——
程序体退化为纯 patch 形，族归属翻案（census open_semantics 原样，结构变更需重审）
```

### 2.3 live 层投影声明

census PLAIN 族与 live 句型层（B-T1 双因子形态）reconciliation OPEN（README §3 登记 1）；rank 因子（Bake 侧）与 share-vector（Group 侧）的同一现实两层表达联合裁决 OPEN（HRQ-B1-04 related 原样）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @BrtNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 所占位置 premise（position_context 上游 fact——位置背景影响可及食物）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @BrtNormalFeedingProfile
    （位置背景并入评价参数——census 盲体 sketch 原样，参数级无新拓扑）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
（conflict 路径不建：Story 明言「明显攻击并不多」，证据不足——census 判语原样；
  RelationalConflict 双路径属 GUARD 族域，本鱼不消费）
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

- 使用的自由度：census PLAIN 族投影标签与双槽 typed 因子实例语义（resource_patch + individual_rank——census 冻结槽序与实例常量原样）；Profile 命名；伪脚本步序（canonical 槽1→槽2→组合固定）。
- 放弃的自由度：(1) 争食 Mode 的 Group 化（census 判语：个体 Condition/Relation 而非独立争食 Mode，GroupPressure=None——Group 侧 share-vector 替代读法两层裁决 OPEN）；(2) conflict 路径（「明显攻击并不多」证据不足不建——census 判语原样）；(3) 合并算子数学（OPERATOR UNDEFINED）；(4) rank fact 持久写回（TAR-05 未定——退化条款见 §2.2，翻案=结构变更需重审）；(5) 数值与 Profile 值域不冻结。
- HRQ-B1-04 双轴待批（槽位数伸缩 2 槽 vs canonical 4 槽轴声明 2–6 + rank 因子类型准入）——本文件按 census 判定表达；裁决翻案=换 BakeTemplate 值+增/删行=结构变更需重审（validator 族边界拦截静默改写）。

BATCH_ID: REP-FULL-P02-001
