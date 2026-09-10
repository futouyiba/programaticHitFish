# 玻璃梭鲈（Walleye｜Sander vitreus）｜繁殖浅滩季节位置重排四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | B01-S02｜玻璃梭鲈｜繁殖浅滩与季节位置重排（census CENSUS-B2 快照全文在案） |
| 冻结 Pattern | P05（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 1.1–29℃、最适 15.05℃、benthopelagic、深 0–27m、夜间活跃、肉食性、追猎、potamodromous、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-WAL-BAKE（PLAIN 族第 4 成员：温度+食物 2 因子，registry v4 在案）+ P-B2-WAL-RESP（TYPED 族标准成员） |

## 0. 上游语义与洄游形态

- 洄游形态：季节位置重排（繁殖浅滩↔深水结构，temp/season+食物驱动）；鱼群聚集≠互斥 FishGroup（census Group 面判语原样：NO_SURFACE_EFFECT）。
- Bake 面：温度+食物 2 因子组合（census P-B2-WAL-BAKE：PLAIN 族第 4 成员，槽位轴 2–6 内）——**本 Story 是本批 PLAIN 投影唯一 Tier A 成员**（与 census B0 欧鲢 P-CHB-BAKE 同族）。
- Response 面：TYPED 族标准成员（产卵聚集不证明更强取食——census 判语原样）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@WalleyeSpawnTemperatureProfile @WalleyeSpawnPreyFactorProfile @WalleyePreyFields @WalleyeDietClasses @WalleyeSizeWindow @WalleyeNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——鱼群聚集≠互斥 FishGroup）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| WalleyeSpawn_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-MIGRATION-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；typed 因子集→固定组合；本鱼为族第 4 成员温度+食物 2 槽） |
| Factor1Type(typed) | habitat_factor：温度（繁殖浅滩↔深水温度梯度；typed 实例——census P-B2-WAL-BAKE 因子 1） |
| Factor2Type(typed) | resource_factor：食物（猎物可得性；typed 实例——census P-B2-WAL-BAKE 因子 2） |
| FactorBinding | lifecycle premise：spawning_stage 配置级切换（繁殖浅滩期↔散后深水结构期因子值域切换；值域由 Profile 层定值；不建 body 分支） |
| TemperatureProfile | @WalleyeSpawnTemperatureProfile |
| PreyFactorProfile | @WalleyeSpawnPreyFactorProfile |
| CombineRule | Template-fixed COMBINE_WEIGHTED（族常量拓扑；数学 OPERATOR UNDEFINED 待机制侧——census open_semantics 因子间顺序 unordered） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@WalleyePreyFields；diet_classes=@WalleyeDietClasses；size_window=@WalleyeSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set（§13.2 结构族：2 槽温度+食物；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的温度事实
读取 当前格子的猎物资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@WalleyePreyFields 绑定的鱼类 prey class 生物量，
      经 diet_classes=@WalleyeDietClasses 食性过滤
      与 size_window=@WalleyeSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（spawning_stage——上游繁殖事实，配置级切换因子值域）

第 1 槽 EVAL_HABITAT_FACTOR_TYPED：
    用温度事实查询 @WalleyeSpawnTemperatureProfile
    得到 TemperatureFit

第 2 槽 EVAL_RESOURCE_FACTOR_TYPED：
    用猎物资源事实查询 @WalleyeSpawnPreyFactorProfile
    得到 PreyFit

COMBINE_WEIGHTED：
    按模板固定组合规则合并 TemperatureFit 与 PreyFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（census PLAIN 族 COMBINE_WEIGHTED 数学未冻结；
    因子间顺序 unordered，Factor 展示顺序不改变结果）

返回 SpatialDistributionWeight（因子集结束：无 gate、无 early return、无相对寻优
——族 forbidden_freedoms 边界；单因子属 SINGLE 族域，硬约束属 HARD_GATED 族域）
```

### 2.3 live 层投影声明

live 结构族 B-T1 Independent Factor Set + Optional Gate（§13.2）天然覆盖 2 槽温度+食物形态（Normal Habitat 吸收先例）；census PLAIN 族与 live B-T1 的槽位/顺序对齐（HRQ-01 factor_set 轴 + HRQ-07 unordered 提案）归两层 reconciliation（README §3 登记 1），本文件不闭合。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @WalleyeNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @WalleyeNormalFeedingProfile（产卵聚集不证明更强取食——census 判语原样；夜间活跃=时段参数方向）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
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

- 使用的自由度：census PLAIN 族投影标签与 typed 因子实例语义（温度+食物 2 槽——census 冻结实例常量）；Profile 命名；伪脚本步序（槽序 unordered、Combine 拓扑族固定）。
- 放弃的自由度：(1) 合并算子数学（COMBINE_WEIGHTED 数学 OPERATOR UNDEFINED 待机制侧）；(2) 鱼群聚集 Group 化（census 判语：聚集≠互斥 FishGroup）；(3) 数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-MIGRA-001
