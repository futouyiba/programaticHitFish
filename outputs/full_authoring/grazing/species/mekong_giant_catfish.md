# 湄公鲶（Mekong Giant Catfish｜Pangasianodon gigas）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| Story | FISH-R05-湄公鲶-Ontogenetic-Feeding-Rebuild（census CENSUS-B0 快照全文在案；Story 页 3d7a4137d23681309e29fd03798c1214） |
| 冻结 Pattern | P05 + P06（census B0 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 20–32℃、最适 26℃、benthopelagic、夜间活跃、植食性、暖水、potamodromous、孤僻（行级 AI 审核状态=待人工审核；本文件不引用其数值做阈值，仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B0 全四面判定快照 + 盲程序体 blind_programs.jsonl 冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；evaluator 类型随 lifecycle premise 切换（body 单态） |
| census 程序 | P-MGC-BAKE-ADULT（PATCH_RESOURCE_FOLLOWING 创始成员，canonical 源）+ P-MGC-RESP-FEEDING（TYPED_TARGET_RESPONSE 创始成员） |

## 0. 上游语义与底质处理形态

- 底质处理形态：成体＝底部碎屑/藻资源 patch 强度场评估（typed substrate evaluator，P06 语义）→ 底带区域约束 → 归一化。单资源链，无 hard gate、无相对排序、无 combine（census 盲程序体冻结判语）。
- 个体发生切换（幼肉食→成植食）：体型驱动的缓慢单调单向发育，同时刻单态、无并存互斥供给——P05 判例不购买 FishGroup；切换属 **lifecycle premise 层**，既非 Group 路由程序亦非 Bake body 内分支（census Group 面判语原样携带）。
- potamodromous 洄游：照欧鲢（CHB）先例按 P05 配置级处理（Bake 因子集随 lifecycle premise 配置切换）；洄游细节少知，不展开 spawn 因子集（census FIX-001 F-2 补注原样携带）。
- 幼体（肉食期）：Bake 程序无空间行为证据，未建体（TAR-02）；其 Response 面 FieldFeeding 通道按 TYPED 族 evaluator_binding 轴 premise 实例处理。
- Quality 面：齿系重塑改变 prey 处理能力与食性偏好＝encounter/conversion 层 typed 参数，无 Quality Selection 程序体结构差异证据（census Quality 面判语原样携带）。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@MekongCatfishSubstratePatchProfile @MekongCatfishZoneConstraintProfile @MekongCatfishSubstrateSpatialProfile @MekongCatfishSubstratePreyFields @MekongCatfishDietClasses @MekongCatfishSizeWindow @MekongCatfishAdultFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件（census Group consequence=NO_SURFACE_EFFECT：同时刻单态、无并存互斥供给，个体发生切换归 lifecycle premise 层）。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| MekongCatfish_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（lifecycle premise＝JUVENILE | ADULT 由上游决定，不构成本面路由输入）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例；非中鱼概率、非 Response 质量、非额外生成容量）。

## 2. Bake

### 2.1 Story 派生底质程序｜配置表（NormalFeeding Group，成体绑定）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-SUBSTRATE-PATCH（本批投影标签＝census PATCH_RESOURCE_FOLLOWING，registry v4，双成员 PROVISIONAL——HRQ-04/HRQ-B1-02 PENDING；3 步带 typed context） |
| PatchResourceType(typed) | 底部碎屑+藻资源（detritus+algae；census P-MGC-BAKE-ADULT 实例常量，registry patch_resource_type 轴） |
| ContextConstraint(typed) | zone=bottom 底带约束（census context_type 轴 zone 侧；轴宽度 zone/current 两值待批） |
| ZoneConstraintProfile | @MekongCatfishZoneConstraintProfile |
| SubstratePatchProfile | @MekongCatfishSubstratePatchProfile（helper SubstrateResourcePatchEvaluator 实例——helper 同 PROVISIONAL） |
| FactorBinding | lifecycle premise：ADULT（幼体肉食期 Bake 无空间证据不建体，TAR-02；potamodromous 因子集随 premise 配置切换，CHB 先例，细节少知不展开） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@MekongCatfishSubstratePreyFields；diet_classes=@MekongCatfishDietClasses；size_window=@MekongCatfishSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@MekongCatfishSubstrateSpatialProfile + 底带 Factor（coverage delta K3 吸收读法；census 族与 live 句型两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前 lifecycle premise（JUVENILE | ADULT——上游 lifecycle trait，体型/年龄驱动，缓慢单向）
如果 premise = JUVENILE：
    幼体 Bake 程序无空间行为证据，不建体（TAR-02）——不进入本程序
否则（premise = ADULT，本程序绑定实例）：

读取 当前格子的底质组成
读取 当前格子的底部资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@MekongCatfishSubstratePreyFields 绑定的碎屑/藻类 prey class 生物量，
      经 diet_classes=@MekongCatfishDietClasses 食性过滤
      与 size_window=@MekongCatfishSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前格子的底带位置（zone 轴事实）

第 1 步 EVAL_RESOURCE_PATCH：
    用底部碎屑/藻资源事实查询 @MekongCatfishSubstratePatchProfile
    （SubstrateResourcePatchEvaluator 实例，typed substrate evaluator）
    得到 SubstratePatchIntensity

第 2 步 CONSTRAIN_ZONE：
    用当前格子的底带位置应用 @MekongCatfishZoneConstraintProfile（zone=bottom）
    得到 ZoneConstrainedWeight

第 3 步 NORMALIZE_WEIGHT：
    对 ZoneConstrainedWeight 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单资源链结束：无 gate、无 early return、无 combine、
无相对排序——族 forbidden_freedoms 边界；硬约束证据若出现属 HARD_GATED 族域另立）
```

### 2.3 live 层投影声明

live BA 句型层（BA-T1..T6）现无底质单链句型；live 侧吸收读法＝BA-T1 底板 + DynamicSpatialSlot=@MekongCatfishSubstrateSpatialProfile + 底带 Factor（REP-COVERAGE-DELTA-001 K3 判 NO_ACTION 的吸收结构）。census PATCH 族（PROVISIONAL）与 live 句型层的等价性归机制侧，本批不闭合（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；evaluator 类型随 lifecycle premise 切换，body 单态） | @MekongCatfishAdultFeedingProfile（成体绑定实例） | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前 lifecycle premise（决定 food evaluator 的类型绑定：
    幼体=肉食取向评估；成体=植食/碎屑取向评估——census evaluator_binding 轴，
    饵与藻食偏好为参数）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @MekongCatfishAdultFeedingProfile（成体绑定实例）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
（连续刮食机会在本表达仍落离散钩饵 target——P02/P06 待检验判语原样携带，census 侧不闭合）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；齿系重塑的 prey 处理能力差异归 encounter/conversion 层 typed 参数，不进品质程序体 |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier（LureSize / BaitSize / HookSize 等）属 live §12.3 跨鱼资产，不在本文件重复。

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

- 使用的自由度：census PATCH 族投影标签与 typed 轴实例值（detritus+algae / zone=bottom——census 冻结实例常量）；Profile 命名；伪脚本步序（canonical 三步固定，不可重排）；Bake 输入契约字段复用（UsableForageAvailability 的 prey_fields/diet_classes/size_window）。
- 放弃的自由度：(1) BakeTemplate 晋升——BA-SUBSTRATE-PATCH 是 census 族投影标签，不是 live 句型晋升（两层 reconciliation OPEN）；(2) 合并算子——本程序无 combine 步（族域边界），live 层 DynamicSpatialSlot 与 BA-T1 底板的组合算子 OPERATOR UNDEFINED 待机制侧；(3) 幼体 Bake 建体（无空间证据，TAR-02）；(4) potamodromous spawn 因子集展开（细节少知，CHB 先例配置级处理）；(5) 数值与 Profile 值域不冻结。
- 跨层登记：幼体 Response FieldFeeding 通道的 P0x 语义层对应指针待 coordinator 确认（census fix_notes 原样携带——coordinator 修复信中「P03 轴」引用未核实，表达侧不引用未读 pattern）。

BATCH_ID: REP-FULL-GRAZE-001
