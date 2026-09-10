# 褐鳟（Brown Trout｜Salmo trutta）｜普通摄食季节脉冲四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：机会组） |
| Story | B01-S12｜褐鳟｜普通摄食与季节猎物脉冲（census CENSUS-B2 快照全文在案）。同种另 Story B01-S14（P02 摄食位置竞争，census CENSUS-B1-BRT）不属本文件——归后续场/位置竞争批 |
| 冻结 Pattern | P01（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：追猎、晨昏活跃、肉食性、营养级 3.36（行级 AI 审核状态=待人工审核；仅作方向锚——CSV 性格列与本组（机会）归属的张力见 §5） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-BRT12-BAKE（SINGLE 族成员：季节脉冲猎物 patch——Story Competing 明言 ResourcePatch 描述足够）+ P-B2-BRT12-RESP（TYPED 标准成员：季节 context 参数） |
| 亚结构组 | 机会组（opportunistic）——本组 Tier A 样板 |

## 0. 上游语义与摄食形态

- 摄食形态：普通摄食+季节猎物脉冲（季节性猎物丰度脉冲驱动位置与响应——Story Competing 明言 ResourcePatch 描述足够，census 原样）。
- Group 面：census NO_SURFACE_EFFECT（Hatch Mode 无独立持续身份证据——Story 判语原样）。
- Response 面：TYPED 标准成员（季节 context 参数——参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。
- 本文件为机会组 Tier A 样板：同组其余文件按此骨架参数差异化。

Profile 引用清单：@BrtSeasonalPulsePatchProfile @BrtPreyFields @BrtDietClasses @BrtSizeWindow @BrtSeasonContextProfile @BrtNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：Hatch Mode 无独立持续身份证据）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Brt_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-OPPORTUNE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；机会组 Tier A 样板文件） |
| FactorType(typed) | resource_patch：季节脉冲猎物 patch 轴（猎物丰度季节脉冲——census P-B2-BRT12-BAKE 实例常量；Story Competing 明言 ResourcePatch 描述足够） |
| FactorBinding | season premise：季节脉冲窗口配置级切换（值域由 Profile 层定值；不建 body 分支） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BrtPreyFields；diet_classes=@BrtDietClasses；size_window=@BrtSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed resource factor（B-T1 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的季节脉冲猎物 patch 轴事实（猎物丰度脉冲）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BrtPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@BrtDietClasses 食性过滤
      与 size_window=@BrtSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（季节脉冲窗口——配置级切换因子）

EVAL_TYPED_FIELD_OR_FACTOR：
    用猎物 patch 轴事实查询 @BrtSeasonalPulsePatchProfile
    得到 SeasonalPulseFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 SeasonalPulseFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）；本文件 = 机会组样板（同组其余文件按此骨架参数差异化）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @BrtNormalFeedingProfile + @BrtSeasonContextProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前季节 context premise（季节猎物构成——evaluator 参数级，非独立通道）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @BrtNormalFeedingProfile
    （季节 context 并入评价参数——census 判语原样：季节 context 参数，参数级无新拓扑）
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（季节脉冲猎物 patch——census 冻结实例常量）；Profile 命名；伪脚本步序（canonical 两步固定）；季节 context 的参数归层（census 判语照录）。
- 放弃的自由度：(1) Hatch Mode 的 Group 化（census 判语：无独立持续身份证据）；(2) 同种 S14（P02 位置竞争面）的表达（归后续批，本文件不冒充）；(3) 合并算子（无 combine 步；OPERATOR UNDEFINED）；(4) 数值与 Profile 值域不冻结。
- CSV 性格锚「追猎」与本组（机会）归属的张力已登记：census 冻结程序（季节脉冲猎物 patch 机会响应）优先于 CSV 习性行（README §4 登记项 5）。

BATCH_ID: REP-FULL-NORM-001
