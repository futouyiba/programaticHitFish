# 乌鳢（Northern Snakehead｜Channa argus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | R02-S15 乌鳢｜伏击捕食与护幼关系切换（R02 CoverageDelta，REP-COVERAGE-DELTA-001 #26 已判定） |
| 冻结 Pattern | P04 语义（K4 繁殖/育幼锚判定转述：伏击↔护幼切换=类型化状态互斥路由 + BA-T1/BA-T2 各绑 + R-T2 反应主导）；Story DB 行级 Pattern 标签未在本地快照 [需核对] |
| 物种属性锚 | fish-reference-20260908：水温 4–22℃、最适 13℃、benthopelagic、晨昏活跃、孤僻（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；coverage report 归档） |
| 证据档 | Tier A（coverage #26 四面判定在案；Story 正文细节 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding(BroodCare)=Defense-only（live V0）；NormalFeeding=R-T2 固定双通道（Feeding + Reaction，反应主导——coverage #26 判定） |

## 0. 上游语义与护巢形态

- 护幼形态：植被浮巢育幼——伏击捕食（常态）与护幼关系（PARENTAL_GUARD 态）随繁殖状态互斥切换（coverage #26：类型化状态互斥路由，§13.1 ReproductionState 先例）。
- 锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）；GuardAnchor Resolver 实例 = Fry / Brood Field（§11.2 泛化）。
- 常态面（NONE）：植被结构伏击（BA-T1 植被结构 Factor + 低光先例 K14 同构）；Response 反应主导（R-T2：Feeding + Reaction 双通道——伏击型对 deflection / 振动 / erratic 轨迹的反应通道主导）。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}（天然互斥——同一时刻的种群份额只进一个 Group；§13.1）。
- 表达超集说明：无（coverage #26 判定映射展开，未超出标题语义）。

Profile 引用清单：@SnakeheadSpawnWindowStart @SnakeheadSpawnWindowEnd @SnakeheadGuardWarmupDays @SnakeheadGuardTempThreshold @SnakeheadBroodStructureSet @SnakeheadGuardingShare @SnakeheadLocalGuardAnchorEligibility @SnakeheadBroodHabitatSuitabilityProfile @SnakeheadGuardRelationProfile @SnakeheadGuardLocalTemperatureProfile @SnakeheadGuardThreatProfile @SnakeheadVegetationStructureProfile @SnakeheadLowLightSpatialProfile @SnakeheadPreyResourceProfile @SnakeheadNormalTimeProfile @SnakeheadNormalTempFloor @SnakeheadNormalFeedingProfile @SnakeheadNormalReactionProfile @ReactionCap @SnakeheadGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| SN1 | C1 | 当前日期 | — | BETWEEN | @SnakeheadSpawnWindowStart | @SnakeheadSpawnWindowEnd |
| SN1 | C2 | 连续均温 | @SnakeheadGuardWarmupDays | >= | @SnakeheadGuardTempThreshold | — |
| SN1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @SnakeheadBroodStructureSet | — |
| SN1 | C4 | 稚鱼群存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| SnakeheadBroodCareEligible | AND | 1 | Condition | SN1.C1 |
| SnakeheadBroodCareEligible | AND | 2 | Condition | SN1.C2 |
| SnakeheadBroodCareEligible | AND | 3 | Condition | SN1.C3 |
| SnakeheadBroodCareEligible | AND | 4 | Condition | SN1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Snakehead_BroodCare_Route | @SnakeheadBroodCareEligible | BroodCare | Species 内行为份额 | @SnakeheadGuardingShare |
| Snakehead_Default | 默认 | NormalFeeding（植被伏击） | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@SnakeheadGuardWarmupDays 天）
读取 当前钓场结构集合
读取 稚鱼群存在事实（上游 GuardAnchor Resolver：Fry / Brood Field 实例）

如果：
    当前日期处于 [@SnakeheadSpawnWindowStart, @SnakeheadSpawnWindowEnd]
    并且 连续均温 >= @SnakeheadGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @SnakeheadBroodStructureSet
    并且 稚鱼群存在事实 == 存在

则：
    BroodCareShare = @SnakeheadGuardingShare

否则：
    BroodCareShare = 0

SpecialShareTotal = BroodCareShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 BroodCareShare / NormalFeedingShare
```

Share 语义：live §7 契约。「伏击↔护幼切换」＝份额级互斥路由（同一时刻份额只进一组），不建逐个体状态机。

## 2. Bake

### 2.1 BroodCare Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=fry school）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @SnakeheadLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | fry_school（浮巢稚鱼群；植被区移动锚） |
| GuardAnchorRelationProfile | @SnakeheadGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @SnakeheadBroodHabitatSuitabilityProfile |
| LocalTemperatureProfile | @SnakeheadGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 BroodCare Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的植被结构 / 水深
读取 当前稚鱼群锚点位置（上游 Fry / Brood Field Resolver 产出）
读取 当前目标与稚鱼群锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @SnakeheadLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与稚鱼群的关系查询 @SnakeheadGuardRelationProfile
得到 RelationFit

用当前目标的植被掩体查询 @SnakeheadBroodHabitatSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @SnakeheadGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 BroodCare SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 + 低光 / 植被伏击 DynamicSpatialSlot，K14 先例）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot |
| VegetationStructureProfile | @SnakeheadVegetationStructureProfile（植被结构 Factor） |
| LowLightSpatialProfile | @SnakeheadLowLightSpatialProfile（低光槽位；§11.5 先例） |
| PreyResourceProfile | @SnakeheadPreyResourceProfile（猎物资源因子） |
| TimeProfile | @SnakeheadNormalTimeProfile（晨昏活跃方向） |
| ExtremeTemperatureGate | @SnakeheadNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前植被结构
读取 当前光照事实
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

用植被结构查询 @SnakeheadVegetationStructureProfile 得到 StructureFit
用光照事实查询 @SnakeheadLowLightSpatialProfile 得到 LowLightFit
用猎物资源查询 @SnakeheadPreyResourceProfile 得到 PreyFit
用时段查询 @SnakeheadNormalTimeProfile 得到 TimeFit

如果 当前点水温 < @SnakeheadNormalTempFloor：
    返回 极低空间权重（early return）

合并 StructureFit / LowLightFit / PreyFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态 + live §17.2 RR-T1 双通道形态）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| BroodCare | 顺序响应规则（Defense-only） | @SnakeheadGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T2 固定双通道（Feeding + Reaction，反应主导） | @SnakeheadNormalFeedingProfile + @SnakeheadNormalReactionProfile + @ReactionCap | 返回 FinalResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

BroodCare Group：

```plain text
读取 当前 Presentation 与浮巢 / 稚鱼群锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @SnakeheadGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group（R-T2，反应主导）：

```plain text
评价 Feeding Channel：
    读取当前饵 / 姿态 / 手法
    使用 @SnakeheadNormalFeedingProfile
    得到 FeedingResponse

评价 Reaction Channel：
    读取突然加速 / 变向 / 下落（abruptness）
    读取 deflection（撞植被后偏转）
    读取振动 / 闪光
    读取 PresentationProximity
    读取持续追逐要求
    读取 CueFamiliarity
    使用 @SnakeheadNormalReactionProfile
    得到 ReactionResponse

FinalResponse = MAX(FeedingResponse, ReactionResponse)
如启用 @ReactionCap：FinalResponse = MIN(FinalResponse, @ReactionCap)

算子标注：MAX 为 live §17.3 Bass Reaction Working Algorithm Candidate（§13.3 注记：Multi-channel Aggregate Semantics 是 Signature 字段，未冻结）；@ReactionCap 为可选固定 Cap 槽（R-T1 结构），不是任意后处理脚本

返回 FinalResponse
```

反应主导语义：Reaction Profile 值域承载（伏击型对 deflection / erratic 的反应权重高），不是控制流差异。

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| BroodCare | QT-1 | @SnakeheadGuardingEligibilityByQuality | @NeutralAffinity | 成熟亲鱼育幼组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（BroodCare 行查 @SnakeheadGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
    读取该品质的 GroupAffinityFactor（@NeutralAffinity）
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

- 使用的自由度：V1 四原子 + R1；BA-T1+LowLightSlot / BA-T2 锚实例双模板各绑一组；R-T2 固定双通道（coverage #26 反应主导判定）；QT-1。
- 放弃的自由度：(1) 逐个体「伏击↔护幼」状态机（份额级互斥路由替代）；(2) Guard 合并算子 / R-T2 Aggregate 数学（MAX 为 Working Candidate、Cap 数学 OPERATOR UNDEFINED）；(3) 双亲分工（份额粒度）。
- [需正文] 浮巢结构集合成员（植被浮巢区方向来自判定句，具体成员待 Story 正文）；R-T2 Reaction Profile 的主导强度值域。

BATCH_ID: REP-FULL-GUARD-001
