# 准白甲鱼（White Amur-like Barb｜Onychostoma simum）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| Story | FISH-R02-S22｜准白甲鱼｜急流底质刮食资源（census CENSUS-B1 快照全文在案；Story 页 3d6a4137d23681e7a651c3b1b67ae84f） |
| 冻结 Pattern | P06（census B1 stories.jsonl 快照；pattern_status=Compression Candidate 压回 P02 待测） |
| 物种属性锚 | 无 fish-reference-20260908 行（CSV 未收录该鱼；身份锚＝census instance_noise species=Onychostoma simum） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体 blind_programs.jsonl 冻结；confidence LOW——行为链 Evidence Open 原样携带） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-ONS-BAKE（PATCH_RESOURCE_FOLLOWING 第 2 成员，context_type=current 侧）+ P-B1-ONS-RESP（TYPED_TARGET_RESPONSE 标准成员，刮食口径窗参数） |
| 收录说明 | coordinator 分批名单（R05 六条+R06 四条）外增补：本地快照可证的 P06-labeled Story（R02-S22）——照 guarding 批「全部本地快照可证 Story」同口径收录，且为 PATCH 族 context 轴 current 侧唯一本地实例；若 coordinator 裁定名单封闭，本文件独立可撤（结构零耦合） |

## 0. 上游语义与底质处理形态

- 底质处理形态：急流底质刮食——附着资源 patch 评估 → 流速 context 应用（急流石底绑定）→ 归一化权重（census 盲程序体冻结判语）。
- 行为链 Evidence Open：急流—石底—附着—刮食行为链仅身份确认，食性/口器行为/实钓均缺直接闭合证据（census confidence LOW 原样携带；P06 压缩测试联动）。
- Pattern 状态：P06 Compression Candidate（可能压回 P02，merge key 四元组裁决归 Cross-Batch/FR 线）——本文件按 P06 现标签表达，压缩裁决不改本面结构（Bake 程序体与 Pattern 归属正交）。
- Group 面：无供给拆分（census Group consequence=NO_SURFACE_EFFECT 原样）。
- Quality 面：无 Quality 程序证据（census Quality consequence=NO_SURFACE_EFFECT 原样）。
- 表达超集说明：无（未超出 census 冻结程序语义范围；confidence LOW 状态全程可见）。
- **判断顺序（REP-ORDER-FIX-001 顺序还原）**：判断链按 census 行为链原文「急流—石底—附着—刮食」四环顺序还原＝流速档 → 石底档 → 附着资源档 → 归一化。census context 常量 fast_flow_stone（单绑定）拆为流速档＋石底档两步——拆步即结构差异（登记 README §7）。分级命中：每步三档（最适应=全额/可接受=削减不清零/排除=出局），档位成员与阈值全 Profile 值域不冻结；行为链 Evidence Open（confidence LOW）原样携带——档位成员待正文/证据闭合。

Profile 引用清单：@OnychostomaSubstratePatchProfile @OnychostomaCurrentConstraintProfile @OnychostomaSubstrateSpatialProfile @OnychostomaSubstratePreyFields @OnychostomaDietClasses @OnychostomaSizeWindow @OnychostomaScrapeFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件（census Group consequence=NO_SURFACE_EFFECT「无供给拆分」）。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Onychostoma_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生底质程序｜配置表（NormalFeeding Group）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-SUBSTRATE-PATCH（本批投影标签＝census PATCH_RESOURCE_FOLLOWING，registry v4，双成员 PROVISIONAL——HRQ-04/HRQ-B1-02 PENDING；3 步带 typed context；**§2.2 已顺序还原（REP-ORDER-FIX-001）：行为链四环原序+early return 链+分级命中，分歧登记 README §7**） |
| PatchResourceType(typed) | 石底附着藻/碎屑资源（attached_algae_detritus；census P-B1-ONS-BAKE 实例常量，confidence LOW） |
| ContextConstraint(typed) | current=fast_flow_stone 急流石底绑定（census context_type 轴 current 侧；轴宽度 zone/current 两值待批；行为链 Evidence Open） |
| CurrentContextProfile | @OnychostomaCurrentConstraintProfile |
| SubstratePatchProfile | @OnychostomaSubstratePatchProfile（typed substrate evaluator 实例） |
| FactorBinding | 常年绑定（census incoming_premises：current_context/attached_resource_field 均为上游 fact，无 premise 切换主张） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@OnychostomaSubstratePreyFields；diet_classes=@OnychostomaDietClasses；size_window=@OnychostomaSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@OnychostomaSubstrateSpatialProfile + 流速 Factor（coverage delta K3/#25 吸收读法：流速 Factor+附着 benthic prey class；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-001】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝census 行为链原文「急流—石底—附着—刮食」四环原序＝流速档 → 石底档 →
附着资源档 → 归一化；每步分级命中（全额/削减/出局），出局即 EARLY_RETURN。
census context 常量 fast_flow_stone（单绑定）拆为流速档＋石底档两步——
顺序与拆步差异本身=LogicTemplate 判据，与 census canonical body
（EVAL_RESOURCE_PATCH → APPLY_CURRENT_CONTEXT → NORMALIZE_WEIGHT，无 gate 判语）的
拓扑分歧登记 README §7（census 侧受影响族重跑=work standards §5.4 行动项）。

读取 当前格子的流速事实（current_context，上游 fact）
读取 当前格子的底质类型
读取 当前格子的附着资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@OnychostomaSubstratePreyFields 绑定的附着藻/碎屑 prey class 生物量，
      经 diet_classes=@OnychostomaDietClasses 食性过滤
      与 size_window=@OnychostomaSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 流速档（GATE_CURRENT——census op APPLY_CURRENT_CONTEXT 的顺序还原形）：
    用流速事实查询 @OnychostomaCurrentConstraintProfile
    （急流石底绑定方向，census 实例常量；档位成员=Profile 值域不冻结 [需正文]）
    如果 流速 ∈ 急流档（preferred 槽）：
        进入第 2 步
    否则如果 流速 ∈ 过渡档（tolerated 槽）：
        CurrentTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（缓流/静水档）：
        返回 0（EARLY_RETURN：急流种不入缓静水分布）

第 2 步 石底档（分级命中）：
    用底质类型查询 @OnychostomaSubstratePatchProfile 的基质分档槽
    如果 底质 ∈ 石底档（preferred 槽——附着面可得）：
        SubstrateTier = 全额保留
    否则如果 底质 ∈ 硬质非石档（tolerated 槽——附着面有限）：
        SubstrateTier = 削减（削减但不清零）
    否则（软底无附着面档）：
        返回 0（EARLY_RETURN：无附着面底质出局）

第 3 步 附着资源档（EVAL_RESOURCE_PATCH，分级命中）：
    用附着资源事实查询 @OnychostomaSubstratePatchProfile
    （typed substrate evaluator 实例；三档分档槽=Profile 值域不冻结）
    如果 附着生物量 ∈ 丰档（preferred 槽）：
        SubstratePatchIntensity = 全额强度
    否则如果 附着生物量 ∈ 贫档（tolerated 槽）：
        SubstratePatchIntensity = 削减强度（削减但不清零）
    否则（无附着资源档）：
        返回 0（EARLY_RETURN：无附着资源的格子出局）

第 4 步 NORMALIZE_WEIGHT：
    对 CurrentTier × SubstrateTier × SubstratePatchIntensity 执行模板固定归一化
    （族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census PATCH 族
canonical 三步的分歧登记 README §7；行为链 Evidence Open，confidence LOW 全程可见）
```

### 2.3 live 层投影声明

live 侧吸收读法＝BA-T1 底板 + DynamicSpatialSlot=@OnychostomaSubstrateSpatialProfile + 流速 Factor（REP-COVERAGE-DELTA-001 #25：流速 Factor（LowEnergyRefugeProfile 流速轴先例——live §7 冷锋 Overlay 资产名，非本鱼绑定）+ 附着 benthic prey class）。census PATCH 族（PROVISIONAL）context_type 轴（zone/current 两值）待批；与 SINGLE 族的 optional_context 边界交 HRQ-B1-02——本文件按 census 判同结果（MERGE，context 槽轴内）表达，族裁决归机制侧。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；刮食口径窗参数） | @OnychostomaScrapeFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 scrape_context（口径窗/附着生物量上游 fact）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实与 scrape_context 评价 @OnychostomaScrapeFeedingProfile
    （刮食取向 typed food evaluator：mouth_gape_window 口径窗）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-001 展开）：
    按三档判定 FoodEvaluation（档位成员=@OnychostomaScrapeFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（连续刮食机会在本表达仍落离散钩饵 target——P02/P06 域待检验判语，census 原样携带）
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

- 使用的自由度：census PATCH 族投影标签与 typed 轴实例值（attached_algae_detritus / current=fast_flow_stone——census 冻结实例常量）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-001：行为链四环原序、fast_flow_stone 单绑定拆两步、三档分级命中、early return 链——推导依据 §0 判断顺序行）**；Bake 输入契约字段复用。
- 放弃的自由度：(1) BakeTemplate 晋升（同湄公鲶——投影标签非 live 句型）；(2) census canonical 步序与单 context 绑定的服从（顺序还原后链与 canonical 三步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(3) 合并算子（本程序无 combine 步；live 层组合算子 OPERATOR UNDEFINED 待机制侧）；(4) 行为链闭合（Evidence Open 状态原样携带——本文件不假装急流—石底—附着—刮食链已证实；档位成员 [需正文]）；(5) P06 压缩裁决（压回 P02 与否归 FR/Cross-Batch，不改本面结构）；(6) 数值与 Profile 值域不冻结（含三档档位成员与阈值）。
- 跨层登记：P-B1-ONS-RESP 的刮食口径窗参数属 census「标准成员+参数实例」（engine 无字面差异）；confidence LOW 全程可见。

BATCH_ID: REP-FULL-GRAZE-001
顺序还原修复批次：REP-ORDER-FIX-001（§0/§2/§3/§5 修改；Bake 伪脚本行为链四环原序+early return 链+分级命中，Response 档位展开）
