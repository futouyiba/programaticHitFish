# 短扁口鲶（Piraiba｜Brachyplatystoma filamentosum）｜食物场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批：食物场组——顶级 piscivore 场跟随型） |
| Story | FISH-R10 批成员（handoff 点名「Piraiba 鲶顶级（R10）」；R10 收官批 49 行之一——本地摘要无 per-fish 明细，Story 行 [需正文]） |
| 冻结 Pattern | P03 [需核对]（handoff 点名归 P03 主 relation 样本；行级标签 Story DB 核对——README §4 登记项 1） |
| 物种属性锚 | fish-reference-20260908：短扁口鲶行——早晨活跃、活泼、Pimelodidae/Brachyplatystoma（食性/摄食类型/栖息带列空——行级 AI 审核状态=待人工审核；仅作身份锚，食性方向按属级 piscivore 顶级方向 [需核对]） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B+（handoff 批次点名先例——同 migration 批 atlantic_tarpon「handoff 点名 [需正文]」档；条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型，live §13.3 Forage-Coupled Feeding 读法；Reaction 槽 OFF） |
| 亚结构组 | 场跟随型（field_type=饵鱼场；intake_semantics=脉冲摄入——顶级 piscivore 食物场跟随） |

## 0. 上游语义与食物场形态

- 食物场形态：顶级 piscivore 的**食物场跟随**（handoff 口径「Piraiba 鲶顶级（R10）」归 P03 主 relation——饵鱼/猎物群场浓度驱动的空间跟随，非滤食 plankton 场、非离散伏击）。CSV 行食性/摄食类型列空—— piscivore 方向为属级常识方向锚 [需核对]，结构以「具名食物场（bait-fish 场）」表达，piscivore 与否不改变场跟随结构（只改 prey class 构成——Profile 值域）。
- 与滤食系的区别（同族不同参数轴实例）：FOOD_FIELD_FEEDING_RESPONSE 族参数轴 field_type＝「plankton_field 或其它具名食物场」（registry allowed_parameter_axes 原文）——本鱼取**饵鱼场**实例；intake_semantics＝**脉冲摄入**（捕获式进食 vs 滤食的持续摄入）。结构（场 evaluand + FieldFeeding RETURN）不变。
- Group 面：无路由（无供给拆分证据；[需正文] 若 Story 证实洪泛期/夜移供给拆分＝升级重审）。
- Quality 面：无程序证据。
- 表达超集说明：骨架参数化表达；未超出 FOOD_FIELD 族域（field_type/intake_semantics 两参数轴都是族声明轴）。

Profile 引用清单：@PrbBaitfishFieldEvaluatorProfile @PrbBaitfishPreyFields @PrbDietClasses @PrbSizeWindow @PrbFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Prb_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化） |
| FieldType(typed) | food_field：饵鱼场（bait-fish 场——猎物鱼群/大型无脊椎的分布浓度场；handoff P03 主 relation 方向。构成 [需正文]） |
| FieldEvaluatorProfile | @PrbBaitfishFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性；深槽/河道结构对场分布的调制并入值域） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@PrbBaitfishPreyFields 绑定的饵鱼/大型无脊椎 prey class 生物量——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@PrbDietClasses；size_window=@PrbSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）；场耦合 live 参照读法=§10 **BA-T5 Forage Field Coupling**（ForageSchoolIntensity 场事实——本批最贴句型；两层 reconciliation OPEN，README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（饵鱼场浓度——猎物鱼群分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@PrbBaitfishPreyFields 绑定的饵鱼/大型无脊椎 prey class 生物量，
      经 diet_classes=@PrbDietClasses 食性过滤
      与 size_window=@PrbSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_FOOD_FIELD_CONCENTRATION：
    用饵鱼场浓度事实查询 @PrbBaitfishFieldEvaluatorProfile
    得到 FieldSuitability（场适应性——场浓度评估，非离散 patch、非结构因子）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；本鱼 Bake 场耦合与 live §10 BA-T5（ForageSchoolIntensity + VerticalAlignment + 温氧可行性固定乘）句型同域——BA-T5 是多因子固定乘形态而本投影是单场因子链，两层等价性归机制侧，本文件不冒充 BA-T5 实例。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=脉冲摄入） | @PrbFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（饵鱼场浓度——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用饵鱼场浓度评价 @PrbFieldIntakeProfile
    （场摄入评估——顶级 piscivore 的脉冲摄入语义（捕获式进食）；
      intake_semantics=脉冲摄入——FOOD_FIELD_FEEDING_RESPONSE 族参数轴实例；
      field_type=饵鱼场——族 field_type 轴「其它具名食物场」实例）
    得到 FieldIntakeEvaluation

DECIDE_FIELD_FEEDING：
    按 FieldIntakeEvaluation 决定场摄食响应档位

返回 Response(FieldFeeding)

Reaction 槽 OFF
（evaluand=食物场非离散目标——与 TYPED 族通道轴不可互吞（B1-LAM 判例同型）；
 单次捕获的 Encounter/Conversion 语义归捕获边界 owner，不进本响应程序；
 离散钩饵捕获通道属产品捕获方式 Product Scope——TAR-09 Open，本文件不表达）
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

- 使用的自由度：FOOD_FIELD 族参数轴实例选取（field_type=饵鱼场、intake_semantics=脉冲摄入——两轴都是族声明参数轴非新结构）；Profile 命名；伪脚本步序（canonical 两步固定）；BA-T5 参照读法选择。
- 放弃的自由度：(1) piscivore 独立建组（CSV 行食性列空——piscivore 方向是属级方向锚，prey class 构成进 Profile 值域不建独立结构）；(2) 单次捕获 Encounter/Conversion 语义（捕获边界 owner——不在 Response 程序内折算）；(3) 离散钩饵捕获通道表达（TAR-09 Open）；(4) 合并算子（OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结。
- [需正文] Story 行（R10 批 P03 主 relation 行级标签）、食性/场构成、晨昏水层切换（若有）。

BATCH_ID: REP-FULL-FIELD-001
