# 大西洋大海鲢（Atlantic Tarpon｜Megalops atlanticus）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | handoff 分批名单点名（大海鲢——amphidromous 型；Story 行未在本地快照 [需正文]；批次归属待核对） |
| 冻结 Pattern | P05（handoff 点名；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 10–40℃、最适 25℃、reef-associated、深 0–40m、晨昏活跃、肉食性、追猎、**amphidromous**（非繁殖驱动的海河洄游）、淡水/半咸水/海水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（handoff 点名 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）——非停食骨架（amphidromous 非繁殖洄游，停食语义默认不适用） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与洄游形态

- 洄游形态：**amphidromous 两向洄游**（幼体逆流入河/沼泽发育肥育↔亚成体/成体降海沿岸礁带生活；繁殖产卵在近海——洄游相位与繁殖相位非同一，**与 anadromous「洄游=繁殖前奏」语义轴不同**）；洄游相位=上游 lifecycle premise，非 FishGroup 内自有状态机。
- 状态轴差异登记：本鱼 premise 枚举按发育阶段（LARVA/JUVENILE_RIVER/SUBADULT_SEA/ADULT_COASTAL 方向）而非繁殖阶段（SPAWN 前置型）——amphidromous 与 anadromous 的阶段语义差异落在 premise 值域（@ 化），不改任何面结构；正文到达后按实际枚举定值。
- 停食判例对齐：停食判例族五例均为繁殖洄游型（R06–R10）；本鱼 amphidromous 非繁殖洄游——停食语义默认不适用；若正文证实阶段性停食（如越冬或幼体变态期），按判例族另行评估。
- 空间重排：沿岸礁带↔河口↔河沼幼体发育带位置轴——premise 配置级因子集切换（CHB/MGC 先例）。
- 表达超集说明：Tier B 骨架按 P05 洄游单因子形给出；正文到达后换族=结构变更需重审；正文判无程序语义即撤回本文件。

Profile 引用清单：@TarponAmphidromousSpatialProfile @TarponPreyFields @TarponDietClasses @TarponSizeWindow @TarponNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；P05 判例：洄游相位=lifecycle premise 层，不购买 Migration Group——非繁殖洄游侧无停食证据）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Tarpon_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（lifecycle premise：发育阶段枚举由上游决定，不构成本面路由输入——
amphidromous 洄游改配置不改供给拓扑）

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
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——照 census B2 北极红点鲑位置因子先例投影） |
| FactorType(typed) | habitat_factor：发育阶段位置轴（沿岸礁带↔河口↔河沼幼体带；typed 实例，随 premise 取轴段） |
| FactorBinding | lifecycle premise：发育阶段配置级切换（amphidromous 发育枚举——LARVA/JUVENILE_RIVER/SUBADULT_SEA/ADULT_COASTAL 方向；值域由 Profile 层定值；不建 body 分支——CHB/MGC 先例） |
| SpatialSlotProfile | @TarponAmphidromousSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TarponPreyFields；diet_classes=@TarponDietClasses；size_window=@TarponSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@TarponAmphidromousSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的位置轴事实（发育阶段绑定的空间轴段）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@TarponPreyFields 绑定的鱼类/无脊椎 prey class 生物量，
      经 diet_classes=@TarponDietClasses 食性过滤
      与 size_window=@TarponSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（发育阶段——上游 lifecycle trait，配置级切换因子集）

EVAL_TYPED_FIELD_OR_FACTOR：
    用位置轴事实查询 @TarponAmphidromousSpatialProfile
    得到 AmphidromousSpatialFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 AmphidromousSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，硬约束属 HARD_GATED 族域）
```

### 2.3 live 层投影声明

live BA 句型层无洄游专用句型（§11.6 判 NEW_TEMPLATE_NOT_PROVEN）；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影骨架）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TarponNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @TarponNormalFeedingProfile（积极追击取向参数——CSV 追猎方向锚）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
（非停食骨架：amphidromous 非繁殖洄游，停食语义默认不适用）
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

- 使用的自由度：SINGLE 族投影标签；typed 因子实例语义（发育阶段位置轴——amphidromous 状态轴）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 归族裁决权（结构变更需重审）；(2) MigrationReaction 双 Path（非繁殖洄游无停食证据——若正文证实阶段性停食按判例族另行评估）；(3) BA-T7 ROUTE/TRANSITION 句型；(4) 合并算子（OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结。
- [需正文] 发育阶段枚举（amphidromous 相位）、空间轴构成（reef-associated↔河沼）、Response 接受窗参数方向、幼体发育带空间事实供给（世界侧义务）。
- [需核对] Story DB 行级 Pattern 标签。

BATCH_ID: REP-FULL-MIGRA-001
