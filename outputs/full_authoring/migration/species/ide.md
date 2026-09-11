# 圆腹雅罗鱼（Ide｜Leuciscus idus）｜个体发生食性切换四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：个体发生切换组） |
| Story | handoff 分批名单点名（Ide 鱼食性随龄——个体发生切换型）；Story 行未在本地快照 [需正文]；live FISH-R05 Ide 页在案（REV-001 minor-2 闭合）（R05–R10 摘要无 Ide per-fish 明细） |
| 冻结 Pattern | P05（handoff 点名个体发生切换型；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 4–20℃、最适 12℃、benthopelagic、早晨活跃、杂食性（variable）、撕鳍性格标注、potamodromous、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（handoff 点名 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；evaluator 参数随生命周期 premise 切换（body 单态） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与生活史形态

- 个体发生形态（方向）：食性随龄切换——幼体杂食/无脊椎取向→成体鱼食/宽谱取向（handoff 点名方向；具体切换轴与 prey 谱 [需正文]）。
- 判例对齐：个体发生切换属 **lifecycle premise 层**（P05 判例不购买 FishGroup；切换既非 Group 路由程序亦非 Bake body 内分支——湄公鲶 MGC/欧鲢 CHB/电鳗 S9 先例链）。本鱼与欧鲢同科（Leuciscidae）同 potamodromous 方向——配置级处理先例直接适用。
- Group 面：按分批口径无供给拆分（单一 NormalFeeding Group）；若正文出现互斥供给证据则升级重审。
- 表达超集说明：Tier B 骨架按 P05 个体发生单因子形（census SINGLE 族）给出，仅容纳 handoff 点名方向；Story 正文到达后若判 PLAIN（多因子）/GATED（硬约束）＝换 BakeTemplate 值 + 增/删行＝结构变更需重审，不是静默改写；正文判无程序语义即撤回本文件。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，handoff 点名方向级推导 [需正文]）**：判断链＝premise 读取（JUVENILE/ADULT 配置级）→ 阶段绑定空间轴段归属三档 → 归一化。推导来源＝handoff 点名「食性随龄」方向+CSV benthopelagic 方向锚（Tier B 无行级证据，链序为样板语义方向级还原，段成员 [需正文]）。分级命中：轴段三档（当前阶段偏好带=全额——幼体沿岸浅水带↔成体开阔深水带随 premise 取段/过渡带=削减不清零/对侧带=出局 EARLY_RETURN）；early return 的对象=格子，不是发育阶段（PREMBIND 不变量维持——个体发生切换属 premise 层，MGC/CHB/S9 先例链）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@IdeOntogeneticSpatialProfile @IdePreyFields @IdeDietClasses @IdeSizeWindow @IdeNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；P05 判例：个体发生切换属 lifecycle premise 层，不购买 FishGroup——MGC/CHB/S9 先例链）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Ide_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（lifecycle premise 由上游体型/年龄 trait 决定，不构成本面路由输入——
食性随龄切换属 premise 层，MGC/CHB 先例）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影骨架）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——归族裁决归 census 侧判同；**§2.2 已顺序还原（REP-ORDER-FIX-003）：轴段归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：生活史阶段空间轴（幼体沿岸浅水↔成体开阔深水方向——CSV benthopelagic+杂食方向锚；具体轴构成 [需正文]） |
| FactorBinding | lifecycle premise：JUVENILE/ADULT 配置级切换（值域由 Profile 层定值；不建 body 分支——MGC/CHB 先例） |
| SpatialSlotProfile | @IdeOntogeneticSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@IdePreyFields；diet_classes=@IdeDietClasses；size_window=@IdeSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@IdeOntogeneticSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（发育阶段配置级）→ 阶段绑定空间轴段归属三档 → 归一化；
轴段判定分级命中（当前阶段偏好带=全额/过渡带=削减不清零/对侧带=出局
EARLY_RETURN）。发育阶段切换本身不进 body 分支（PREMBIND 不变量维持：
JUVENILE/ADULT=上游体型/年龄 trait，配置级切换因子集——MGC/CHB 先例）；
early return 的对象是格子，不是发育阶段。推导来源=handoff 点名方向+CSV
benthopelagic 方向锚（方向级，段成员 [需正文]）；档位成员=Profile 值域不冻结。
与 census SINGLE 族 canonical 两步（无 gate 判语）的拓扑分歧登记 README §7
（census 侧受影响族重跑=work standards §5.4 行动项）。

读取 当前格子的位置轴事实（生活史阶段空间轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@IdePreyFields 绑定的杂食/鱼类 prey class 生物量，
      经 diet_classes=@IdeDietClasses 食性过滤
      与 size_window=@IdeSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（JUVENILE/ADULT——上游体型/年龄 trait，配置级切换因子集；
    本 body 只按 premise 取 Profile 轴段值，不含发育阶段分支）

第 1 步 阶段绑定空间轴段归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @IdeOntogeneticSpatialProfile 的阶段轴段分档槽
    （轴=幼体沿岸浅水带↔成体开阔深水带（方向——具体构成 [需正文]）；
    段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 当前 premise 偏好带（preferred 槽——幼体沿岸带/成体深水带方向）：
        OntogeneticSpatialFit = 全额
    否则如果 ∈ 过渡带（tolerated 槽）：
        OntogeneticSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（对侧带——当前阶段不取的轴段）：
        返回 0（EARLY_RETURN：格子不在当前发育阶段空间范围，出局）

第 2 步 NORMALIZE_WEIGHT：
    对 OntogeneticSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live 吸收读法=BA-T1 底板 + DynamicSpatialSlot=@IdeOntogeneticSpatialProfile（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影骨架）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；evaluator 参数随生命周期 premise 切换） | @IdeNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前 lifecycle premise（决定 food evaluator 参数方向：
    幼体=无脊椎/杂食取向接受窗；成体=宽谱/鱼食取向——census evaluator_binding 轴
    premise 实例读法（MGC 先例），body 单态）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @IdeNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@IdeNormalFeedingProfile 值域不冻结；
    幼体=无脊椎/杂食取向接受窗、成体=宽谱/鱼食取向——参数随 premise 切换，
    档位结构不随 premise 切换）：
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

- 使用的自由度：SINGLE 族投影标签；typed 因子实例语义（个体发生方向，取自 handoff 点名+CSV）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：轴段归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) 归族裁决权（SINGLE 骨架是表达层选择，census 侧判同可能改判 PLAIN/GATED——结构变更需重审）；(3) 个体发生切换 Group 化/Response 分支（P05 判例 premise 层，MGC/CHB/S9 先例链）；(4) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结（含轴段/档位成员）。
- [需正文] 食性切换轴（幼→成 prey 谱具体构成）、空间轴构成、Response 接受窗参数方向、批次归属（R05–R10 摘要无 per-fish 明细）。
- [需核对] Story DB 行级 Pattern 标签。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 轴段归属三档+early return 链，Response 档位展开）
