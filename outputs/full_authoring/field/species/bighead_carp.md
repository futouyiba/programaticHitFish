# 鳙鱼（Bighead Carp｜Hypophthalmichthys nobilis）｜滤食浮游场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批：滤食/食物场组） |
| Story | FISH-R02-S09｜鳙鱼｜滤食浮游场与水层机会（census CENSUS-B2 全四面判定快照 + 盲程序体冻结在案） |
| 冻结 Pattern | P03（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：benthopelagic、早晨活跃、杂食性名义行、potamodromous、营养级 2.83（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值——CSV 食性列与本 Story 滤食语义的口径差以 census 快照为准） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结——**FOOD_FIELD_FEEDING_RESPONSE 族 canonical source**） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型：Channel=Feeding，evaluand 换为食物场浓度、换 Profile/Facts，live §13.3 Forage-Coupled Feeding 读法；Reaction 槽 OFF） |
| census 程序 | P-B2-BHC-BAKE（SINGLE 族 factor_type 轴 +food_field 场实例）+ P-B2-BHC-RESP-FIELD（FOOD_FIELD_FEEDING_RESPONSE canonical source） |
| 亚结构组 | 滤食型（persistent filter feeding）——**本组 Tier A 样板** |

## 0. 上游语义与食物场形态

- 食物场形态：滤食浮游场（场 evaluand——分布式浓度场：浮游动物/浮游植物/悬浮颗粒浓度，水柱分布；census incoming premise 原样）。滤食与钩饵响应并非同一现实机制（Story 明言——census 判语原样）。
- Bake 面：食物场浓度单链（census P-B2-BHC-BAKE：EVAL_FOOD_FIELD_CONCENTRATION → NORMALIZE_WEIGHT；SINGLE 族 factor_type 轴 +food_field——场实例第 2/3 例继 B1 七鳃鳗 chemical_gradient 场系）。高生产力水层定位＝场评估的自然输出（census sketch 原样）。
- Response 面：FOOD_FIELD_FEEDING_RESPONSE 族 canonical source（evaluand=食物场浓度非离散目标 + RETURN=FieldFeeding；与 TYPED 通道轴不可互吞——B1-LAM 判例同型）。产品捕获方式＝Product Scope TAR-09 Open。
- Group 面：census NO_SURFACE_EFFECT（FishMode Weak）——无供给拆分；handoff「鱼群供给路由候选」Story DB 行级 [需核对]（README §4 登记项 1）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@BhcPlanktonFieldEvaluatorProfile @BhcPlanktonPreyFields @BhcDietClasses @BhcSizeWindow @BhcFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT（FishMode Weak）原样）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Bhc_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族 food_field 场投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化；本组 Tier A 样板文件） |
| FieldType(typed) | food_field：plankton 场（场 evaluand——浮游动物/浮游植物/悬浮颗粒浓度场，水柱分布；census P-B2-BHC-BAKE 实例常量） |
| FieldEvaluatorProfile | @BhcPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BhcPlanktonPreyFields 绑定的 plankton prey class 生物量——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@BhcDietClasses；size_window=@BhcSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 Independent Factor Set 单因子退化形；场耦合 live 参照读法=§10 BA-T5 Forage Field Coupling 句型——两层 reconciliation OPEN，README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（浮游浓度场——水柱分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BhcPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@BhcDietClasses 食性过滤
      与 size_window=@BhcSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_FOOD_FIELD_CONCENTRATION：
    用食物场浓度事实查询 @BhcPlanktonFieldEvaluatorProfile
    得到 FieldSuitability（场适应性——场浓度评估，非离散 patch、非结构因子）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；场耦合句型的 live 参照＝BA-T5（ForageSchoolIntensity 类场事实 + Profile 评估——live 侧尚未按 plankton 场实例化，本文件不冒充句型晋升）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @BhcFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游浓度场——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @BhcFieldIntakeProfile
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

- 使用的自由度：census SINGLE 族 food_field 轴投影标签与场实例语义（plankton 场——census 冻结实例常量）；FOOD_FIELD_FEEDING_RESPONSE 族投影（canonical source）；intake_semantics 参数轴取值（持续滤食）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 离散钩饵捕获通道表达（产品捕获方式 TAR-09 Open——census open_semantics 原样携带，不预购买）；(2) 合并算子（单场因子链无 combine 步；OPERATOR UNDEFINED）；(3) 鱼群供给路由（census 判 NO_SURFACE_EFFECT，handoff 候选 Story DB 行级 [需核对]）；(4) 数值与 Profile 值域不冻结。
- 同型对照：鲢鱼 R02-S07 与本鱼同型（census 判语「同型对照不建体」）——silver_carp.md 按本骨架参数差异化。
- 本文件为本批滤食组 Tier A 样板：同组其余文件按此骨架参数差异化，不重复引用本文件。

BATCH_ID: REP-FULL-FIELD-001
