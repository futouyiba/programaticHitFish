# 红鲑（Sockeye Salmon｜Oncorhynchus nerka）｜滤食浮游场系四面生产级表达（P03 面，双批分工）

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批：滤食/食物场组） |
| Story | FISH-R06 鲑科四之三（migration 批 sockeye_salmon.md 承载 P05 面：非停食洄游+湖沼生活史 premise [需正文]）；本文件为其 **P03 摄食面**——migration 批「滤食取向 P03 复核登记」兑现线（双批分工，[需正文]） |
| 冻结 Pattern | P05 [需核对]（migration 批承载）+ P03 摄食面（CSV 滤食锚 [需核对]——双面双批分工） |
| 物种属性锚 | fish-reference-20260908：pelagic-oceanic、晨昏活跃、滤食性（selective plankton feeding）、追猎、anadromous、营养级 3.54（行级 AI 审核状态=待人工审核；仅作方向锚，数值不做阈值——海洋期浮游+幼鱼混合构成 [需正文]） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（CSV 滤食锚 + migration 批复核线点名；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型：Channel=Feeding，evaluand 换为食物场浓度、换 Profile/Facts，live §13.3 Forage-Coupled Feeding 读法；Reaction 槽 OFF） |
| 亚结构组 | 滤食型（persistent filter feeding）——plankton 场参数差异化 |

## 0. 上游语义与食物场形态

- 食物场形态：滤食浮游场（场 evaluand——分布式浓度场，水柱分布；CSV 滤食性方向锚）。滤食与钩饵响应并非同一现实机制（鳙鱼 Story 判语同款——本组 Tier A 样板语义）。
- 双批分工互指：P05 面（洄游单链）＝migration 批 species/sockeye_salmon.md；P03 面（本文件）。红鲑溯河产卵期是否停食 [需正文]——停食判例族（大马哈/美洲西鲱 R06→白北鲑 R08→高首鲟 R09）不默认继承（migration 批同属不继承判语原样）；若 Story 证实停食＝Response 挂起形态升级重审（停食面归 migration 批双 Path 先例承载，本文件摄食期表达不预购买）。
- Bake 面：食物场浓度单链（照 bighead_carp.md 骨架——BHC canonical；场实例 prey class 构成按本鱼 Profile 值域差异化）。
- Response 面：FOOD_FIELD_FEEDING_RESPONSE 投影（intake_semantics=持续滤食；接受窗参数差异进 Profile 值域）。
- Group 面：无路由（无供给拆分证据；handoff「鱼群供给路由候选」仅点名鲢/鳙系——本鱼不在其中）。
- Quality 面：无程序证据。
- 表达超集说明：骨架参数化表达；未超出 BHC canonical 族域。

Profile 引用清单：@SckPlanktonFieldEvaluatorProfile @SckPlanktonPreyFields @SckDietClasses @SckSizeWindow @SckFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Sck_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化；bighead_carp.md Tier A 样板骨架） |
| FieldType(typed) | food_field：plankton 场（场 evaluand——浮游浓度场，海洋期表层水柱分布（CSV selective plankton feeding 方向锚；浮游/幼鱼混合构成 [需正文]）） |
| FieldEvaluatorProfile | @SckPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |
| FactorBinding | lifecycle premise：溯河洄游相位配置级切换（摄食期海域因子集 ↔ 溯河产卵期因子集由上游 premise 配置切换，不建 body 分支——MGC/CHB 先例） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@SckPlanktonPreyFields 绑定的 plankton prey class 生物量——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@SckDietClasses；size_window=@SckSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）；场耦合 live 参照读法=§10 BA-T5 Forage Field Coupling——两层 reconciliation OPEN，README §3 |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（浮游浓度场——水柱分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@SckPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@SckDietClasses 食性过滤
      与 size_window=@SckSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（溯河洄游相位——lifecycle premise 配置级切换；不在本 body 内分支）

EVAL_FOOD_FIELD_CONCENTRATION：
    用食物场浓度事实查询 @SckPlanktonFieldEvaluatorProfile
    得到 FieldSuitability（场适应性——场浓度评估，非离散 patch、非结构因子）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；本鱼 census 未建体（B2 选样未含）——本投影按 BHC canonical 骨架参数差异化，Story 正文到达后 census 侧判同可能改判（换标签/换族＝结构变更需重审）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @SckFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游浓度场——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @SckFieldIntakeProfile
    （场摄入评估——持续滤食摄入语义（海洋期摄食构成随生命周期 premise 切换——湖沼幼体期/海洋成体期的场构成差异进值域）；
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

- 使用的自由度：census SINGLE 族 food_field 轴投影标签与场实例语义；FOOD_FIELD 族投影（intake_semantics=持续滤食）；Profile 命名；伪脚本步序（canonical 两步固定）；双批分工面划分。
- 放弃的自由度：P05 洄游面/停食面表达（归 migration 批资产；停食判例族不默认继承）；离散钩饵捕获通道表达（产品捕获方式 TAR-09 Open——不预购买）；合并算子（单场因子链无 combine 步；OPERATOR UNDEFINED）；数值与 Profile 值域不冻结。
- [需正文] P03 主 relation 行级标签、海洋期场构成、溯河停食与否。

BATCH_ID: REP-FULL-FIELD-001
