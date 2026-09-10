# 大西洋鲱（Atlantic Herring｜Clupea harengus）｜浮游食场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批：滤食/食物场组） |
| Story | FISH-R02-S02｜大西洋鲱鱼｜群游产卵与浮游食场（census CENSUS-B2 全四面判定快照 + 盲程序体冻结在案） |
| 冻结 Pattern | P03（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：benthopelagic、全天活跃、滤食性（selective plankton feeding）、活泼、oceanodromous、营养级 3.38（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结——FOOD_FIELD_FEEDING_RESPONSE 第 2 成员；**库内首个 GroupPressure=Strong/Group-only verdict**） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型：Channel=Feeding，evaluand 换为食物场浓度、换 Profile/Facts，live §13.3 Forage-Coupled Feeding 读法；Reaction 槽 OFF） |
| census 程序 | P-B2-HER-BAKE（SINGLE 族 factor_type 轴 +food_field 场实例）+ P-B2-HER-RESP-FIELD（FOOD_FIELD_FEEDING_RESPONSE 第 2 成员，engine 无字面差异） |
| 亚结构组 | 滤食型（persistent filter feeding；群游集聚承载） |

## 0. 上游语义与食物场形态

- 食物场形态：浮游食场跟随（场 evaluand——浮游食场浓度；找鱼=定位饵鱼层/群体边缘——玩家策略，census sketch 原样）。
- 群游集聚：由空间 Factor 值域承载（coverage #17 判——群游集聚是空间 Factor 值域，不单独购买结构）；群游集聚与 plankton 场评估的关系＝场适应性 Profile 的值域维度，非独立程序步。
- Group 面（本文件最特殊面）：census 判语原样——**库内首个 GroupPressure=Strong/Group-only verdict**：census 层无 routing body 证据（摄食群与产卵群重叠非同态、无统一触发器——Story 自述「产卵群体≠摄食群体（不可统一全年群体触发器）」）；语义层判定与 census 正交。本文件按 census 判语＝无路由程序，Group 语义压力登记不闭合（README §3 登记 2）。
- Bake 面：浮游食场因子单链（census P-B2-HER-BAKE：EVAL_FOOD_FIELD_CONCENTRATION → NORMALIZE_WEIGHT；SINGLE 族 food_field 轴场实例）；季节产卵迁移为 lifecycle premise（配置级）。
- Response 面：FOOD_FIELD_FEEDING_RESPONSE 第 2 成员（engine 与 canonical 无字面差异——census 判语）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无。

Profile 引用清单：@HerPlanktonFieldEvaluatorProfile @HerPlanktonPreyFields @HerDietClasses @HerSizeWindow @HerFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 verdict 原样：GroupPressure=Strong 但 census 层无 routing body 证据——摄食群与产卵群重叠非同态、无统一触发器，语义层判定与 census 正交，README §3 登记 2）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Her_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（群游语义压力 GroupPressure=Strong 登记——census 层无 routing body 证据：
  摄食群与产卵群重叠非同态、无统一触发器，本程序不建群游路由）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族 food_field 场投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化） |
| FieldType(typed) | food_field：plankton 场（浮游食场——census P-B2-HER-BAKE 实例常量；群游集聚由场适应性值域承载，coverage #17 判） |
| FieldEvaluatorProfile | @HerPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性；群游集聚值域并入本 Profile） |
| FactorBinding | lifecycle premise：季节产卵迁移配置级切换（产卵期因子集由上游 premise 配置切换——世界侧事实；不建 body 分支。产卵群体≠摄食群体，不可统一全年群体触发器——Story 判语原样） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@HerPlanktonPreyFields 绑定的 plankton prey class 生物量——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@HerDietClasses；size_window=@HerSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）；场耦合 live 参照读法=§10 BA-T5 Forage Field Coupling（ForageSchoolIntensity 类场事实）——两层 reconciliation OPEN，README §3 |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（浮游食场浓度——水柱分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@HerPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@HerDietClasses 食性过滤
      与 size_window=@HerSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（季节产卵迁移——lifecycle premise，配置级切换因子集；不在本 body 内分支）

EVAL_FOOD_FIELD_CONCENTRATION：
    用食物场浓度事实查询 @HerPlanktonFieldEvaluatorProfile
    得到 FieldSuitability（场适应性——含群游集聚值域承载，非独立程序步）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；BA-T5 Forage Field Coupling（饵鱼群强度 + 垂直对齐 + 温氧可行性固定乘）是 live 侧最接近的场耦合句型——本鱼 plankton 场与 BA-T5 的对象（饵鱼群场）不同，句型类比不等于晋升。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @HerFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游食场浓度——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @HerFieldIntakeProfile
    （场摄入评估——持续滤食摄入语义；
      intake_semantics=持续滤食——FOOD_FIELD_FEEDING_RESPONSE 族参数轴实例）
    得到 FieldIntakeEvaluation

DECIDE_FIELD_FEEDING：
    按 FieldIntakeEvaluation 决定场摄食响应档位

返回 Response(FieldFeeding)

Reaction 槽 OFF
（evaluand=食物场非离散目标——与 TYPED 族通道轴不可互吞（B1-LAM 判例同型）；
 离散钩饵捕获通道属产品捕获方式 Product Scope——TAR-09 Open，本文件不表达）
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

- 使用的自由度：census SINGLE 族 food_field 轴投影标签与场实例语义；FOOD_FIELD_FEEDING_RESPONSE 族投影；intake_semantics 取值（持续滤食）；群游集聚的 Profile 值域承载读法（coverage #17 判）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 群游 Group 路由（census Group-only verdict：无 routing body 证据——摄食群/产卵群重叠非同态；语义层 GroupPressure=Strong 登记不闭合，README §3 登记 2）；(2) 产卵洄游 Group（P05 面=oceanodromous 季节产卵迁移 premise 配置级；不购买 Migration Group）；(3) 离散钩饵捕获通道表达（TAR-09 Open）；(4) 合并算子（OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-FIELD-001
