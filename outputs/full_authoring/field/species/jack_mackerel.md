# 日本竹荚鱼（Japanese Jack Mackerel｜Trachurus japonicus）｜滤食浮游场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批：滤食/食物场组） |
| Story | CSV 滤食锚（selective plankton feeding）行；Story 行 [需正文]（P03 主 relation 待核——鲹科成体混合捕食张力登记） |
| 冻结 Pattern | P03 [需核对]（CSV 方向锚；行级标签 Story DB 核对） |
| 物种属性锚 | fish-reference-20260908：pelagic-neritic、全天活跃、滤食性（selective plankton feeding）、温和、oceanodromous、营养级 3.4（行级 AI 审核状态=待人工审核；仅作方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型：Channel=Feeding，evaluand 换为食物场浓度、换 Profile/Facts，live §13.3 Forage-Coupled Feeding 读法；Reaction 槽 OFF） |
| 亚结构组 | 滤食型（persistent filter feeding）——plankton 场参数差异化 |

## 0. 上游语义与食物场形态

- 食物场形态：滤食浮游场（场 evaluand——分布式浓度场，水柱分布；CSV 滤食性方向锚）。滤食与钩饵响应并非同一现实机制（鳙鱼 Story 判语同款——本组 Tier A 样板语义）。
- 混合食性张力登记：CSV 摄食类型=selective plankton feeding（滤食锚）与鲹科（Carangidae）成体混合捕食（浮游+小鱼）常识方向冲突——结构上不冲突（场跟随结构容纳 prey class 构成差异），构成裁决归 Story 正文（README §4 登记项 3）。
- Bake 面：食物场浓度单链（照 bighead_carp.md 骨架——BHC canonical；场实例 prey class 构成按本鱼 Profile 值域差异化）。
- Response 面：FOOD_FIELD_FEEDING_RESPONSE 投影（intake_semantics=持续滤食；接受窗参数差异进 Profile 值域）。
- Group 面：无路由（无供给拆分证据；handoff「鱼群供给路由候选」仅点名鲢/鳙系——本鱼不在其中）。
- Quality 面：无程序证据。
- 表达超集说明：骨架参数化表达；未超出 BHC canonical 族域。
- **判断顺序（REP-ORDER-FIX-005 顺序还原，handoff 判序+CSV 方向锚推导）**：判断链＝滤食水层定位（沿岸表层/中上层滤食带三档——pelagic-neritic 方向锚 [需核对]）→ 场浓度判定（浮游浓度三档——浮游+小鱼混合构成张力归第 3 步构成判定；水流输送调制并入 Profile 值域）→ 个体大小口径判定（鳃耙/口裂口径三档——鲹科成体混合捕食张力 [需正文]）→ 归一化（族常量终点步——SINGLE 族域无 combine 步）。推导来源＝handoff 判序指令（滤食型：先判水层位置（上层/中层）→水流/食物场密度→个体大小口径→合并）+ BHC canonical 同型骨架参数差异化（链形照 bighead_carp.md 顺序还原链，水层锚换沿岸表层）；与 census canonical 两步判语的拓扑分歧登记 README §7。分级命中：每步三档（偏好=全额/可接受=削减×衰减不清零/不接受=出局 EARLY_RETURN）；early return 的对象=格子。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@JmkPlanktonFieldEvaluatorProfile @JmkPlanktonPreyFields @JmkDietClasses @JmkSizeWindow @JmkFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Jmk_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化；bighead_carp.md Tier A 样板骨架；**§2.2 已顺序还原（REP-ORDER-FIX-005）：水层定位→场浓度→口径链+early return，分歧登记 README §7**） |
| FieldType(typed) | food_field：plankton 场（场 evaluand——浮游浓度场，沿岸表层水柱分布（CSV selective plankton feeding 方向锚；鲹科成体浮游+小鱼混合构成 [需正文]）） |
| FieldEvaluatorProfile | @JmkPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |
| FactorBinding | lifecycle premise：季节相位配置级切换（因子集随上游 premise 配置切换，不建 body 分支） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@JmkPlanktonPreyFields 绑定的 plankton prey class 生物量——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@JmkDietClasses；size_window=@JmkSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）；场耦合 live 参照读法=§10 BA-T5 Forage Field Coupling——两层 reconciliation OPEN，README §3 |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-005】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝滤食水层定位 → 场浓度判定 → 个体大小口径判定 → 归一化（族常量终点步）；
三步均为同一场评估（FieldSuitability）的顺序判定（非多因子并联——SINGLE 族域），
每步分级命中（偏好=全额/可接受=削减×衰减不清零/不接受=出局 EARLY_RETURN）；
early return 的对象=格子。推导来源与 census 判语分歧登记 README §7
（census 侧族重跑=work standards §5.4 行动项）；档位成员=Profile 值域不冻结。

读取 当前格子的水层/深度带事实（滤食水层判定输入——顺序还原链第一判定步的事实读取）
读取 当前格子的食物场事实（浮游浓度场——水柱分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@JmkPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@JmkDietClasses 食性过滤
      与 size_window=@JmkSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（季节相位——lifecycle premise 配置级切换；不在本 body 内分支）

第 1 步 滤食水层定位（场评估的前置顺序判定，分级命中）：
    用水层/深度带事实查询 @JmkPlanktonFieldEvaluatorProfile 的水层分档槽
    （沿岸表层/中上层滤食带——pelagic-neritic 方向锚 [需核对]；
      滤食型先判水层位置（上层/中层）；档位成员与阈值=Profile 值域不冻结 [需正文]）
    如果 ∈ 偏好滤食水层（preferred 槽——沿岸表层浮游富集带）：
        不折减，进入第 2 步
    否则如果 ∈ 可接受邻层（tolerated 槽）：
        携削减标记进入第 2 步（× Profile 衰减参数——削减但不清零）
    否则（远离滤食水层，滤食位不在场）：
        返回 0（EARLY_RETURN：格子不在滤食水层范围，出局）

第 2 步 EVAL_FOOD_FIELD_CONCENTRATION（canonical 步的档位化展开——场浓度三档）：
    用食物场浓度事实查询 @JmkPlanktonFieldEvaluatorProfile
    （水流对浮游分布的输送调制并入 Profile 值域；
      场适应性——场浓度评估，非离散 patch、非结构因子）
    如果 ∈ 高浓度带（preferred 槽——场浓度在偏好带）：
        FieldSuitability = 全额
    否则如果 ∈ 边际浓度带（tolerated 槽）：
        FieldSuitability = 削减（× Profile 衰减参数叠加——削减但不清零）
    否则（空场/浓度低于起始阈值）：
        返回 0（EARLY_RETURN：场不可用，格子出局）

第 3 步 个体大小口径判定（口径三档——契约口径过滤维度的链位化）：
    用口径过滤前后的构成对比（食物场浓度事实 vs diet_classes=@JmkDietClasses
      与 size_window=@JmkSizeWindow 过滤后的在场可食构成）查询 @JmkPlanktonFieldEvaluatorProfile
      的口径分档槽（口径=个体大小决定的鳃耙间距/口裂——鲹科成体混合捕食张力
      （浮游+小鱼构成按 Story 正文定 [需正文]）；@JmkSizeWindow 值域）
    如果 口径内构成为主（preferred 槽——场构成与本鱼口径匹配）：
        FieldSuitability 保持（本步不折减）
    否则如果 仅部分构成在口径内（tolerated 槽）：
        FieldSuitability = 削减（× Profile 衰减参数叠加——部分可食）
    否则（场构成全部超出本鱼口径——浓度高亦不可食）：
        返回 0（EARLY_RETURN：口径不匹配，格子出局）

    多步命中档的折减合成算子标注：OPERATOR UNDEFINED —— 待机制侧
    （SINGLE 族 forbidden_freedoms 无 combine 步；三步为同一场评估的顺序判定非并联，
     步间折减合成=族重跑后的规格动作，本文件不静默定义）

第 4 步 NORMALIZE_WEIGHT（canonical；链终点步——handoff 判序「合并」的族域读法：
    SINGLE 族域单场因子链的合并=归一化终点，非多因子 COMBINE）：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族 canonical
两步「无 gate 判语」的拓扑分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；本鱼 census 未建体（B2 选样未含）——本投影按 BHC canonical 骨架参数差异化，Story 正文到达后 census 侧判同可能改判（换标签/换族＝结构变更需重审）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @JmkFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游浓度场——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @JmkFieldIntakeProfile
    （场摄入评估——持续滤食摄入语义（混合食性张力：CSV 滤食锚 vs 鲹科成体 piscivore 倾向——prey class 构成按 Story 正文定 [需正文]）；
      intake_semantics=持续滤食——FOOD_FIELD_FEEDING_RESPONSE 族参数轴实例）
    得到 FieldIntakeEvaluation

DECIDE_FIELD_FEEDING（分级命中，REP-ORDER-FIX-005 展开）：
    按三档判定 FieldIntakeEvaluation（档位成员=@JmkFieldIntakeProfile 值域不冻结）：
    如果 FieldIntakeEvaluation ∈ 接受档（preferred 槽——场浓度足够启动摄入）：
        返回 Response(FieldFeeding)（全额响应）
    否则如果 ∈ 边际档（tolerated 槽——低浓度场仍维持低摄入）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(FieldFeeding)

Reaction 槽 OFF
（evaluand=食物场非离散目标——与 TYPED 族通道轴不可互吞（B1-LAM 判例同型）；
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

- 使用的自由度：census SINGLE 族 food_field 轴投影标签与场实例语义（plankton 场——CSV 方向锚）；FOOD_FIELD 族投影（intake_semantics=持续滤食）；Profile 命名；伪脚本步序（canonical 两步固定；**§2.2/§3.2 已顺序还原（REP-ORDER-FIX-005）：链序与档位结构（照 BHC 样板链，水层锚换沿岸表层）——推导依据 §0 判断顺序行**）。
- 放弃的自由度：census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate」判语拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；离散钩饵捕获通道表达（产品捕获方式 TAR-09 Open——不预购买）；合并算子（单场因子链无 combine 步；步间折减合成 OPERATOR UNDEFINED）；数值与 Profile 值域不冻结。
- [需正文] P03 主 relation 行级标签、prey class 构成（混合食性张力消解）、群游集聚值域（若有）。

BATCH_ID: REP-FULL-FIELD-001
顺序还原修复批次：REP-ORDER-FIX-005（§0/§2/§3/§5 修改；Bake 水层定位→场浓度→口径链+early return，Response 档位展开）
