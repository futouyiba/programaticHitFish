# 小口黑鲈（Smallmouth Bass｜Micropterus dolomieu）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | C07｜小口黑鲈·护巢 / 护幼（15-Case 已审冻结故事，Evidence 页 3d6a4137d23681759b0fff070b2f0e4c）；Story DB B01 行＝P04 Mode Candidate + P0x（FISH-R06-FR2 F-1 复核记载） |
| 冻结 Pattern | P04（雄鱼照护巢与幼鱼；照护状态支持区别于普通猎物获取的关系性响应） |
| 审核禁用项 | Suski 2003 钓放 / 窝内损失效应：第二轮审核明确不证明该效应，本文件不使用它构造任何时间反馈（C07 裁决，逐字遵守） |
| 相邻故事 | B01-S32 跟随翻底动物获取被惊出的猎物（R01 CoverageDelta）＝摄食面故事；其表达落点=上游扰动事实 + DynamicSpatialSlot + Reaction 通道（REP-COVERAGE-DELTA-001 #11 已判定），本文件不重复展开 |
| 物种属性锚 | fish-reference-20260908：水温 8.5–29.5℃、最适 19℃、benthopelagic、深 1–7m、晨昏活跃、好斗（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版） |
| 证据档 | Tier A（C07 冻结故事快照全文在 outputs/fcf_authoring_concrete_r2/baseline_mapping.md） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼照护巢与幼鱼（C07 已审主张）——覆盖护卵（nest）与护幼（fry）两阶段；冻结的是护巢 / 护幼压力，不含扰底跟随故事（C07 明示）。
- 锚点两阶段：GuardAnchor Resolver 实例 ∈ {nest_bed（卵床）, fry_school（稚鱼群）}——live §11.2 Fry Guard 泛化判例：同一 BA-T2 模板，锚差异=上游 Resolver 实例切换，不新增 BakeTemplate、不设 body 分支。
- C07 未决维度 R01 / R02（重叠 / 默认值策略、跨面程序包身份）：live V0 已取舍为 Defense-only 结构性关闭（例 1C + §8.8）；记录于 §5。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}（§13.1）；本鱼仅 Guarding 一个 Special Group。
- 同属对照纪律（FISH-R06-FR2 F-1 教训）：Micropterus 4 行中仅本行有 P04 护巢 Story（大口黑鲈双行均 0 Story / Identity 隔离）；同属泛化不成立，不做属级推广。

Profile 引用清单：@SmallmouthSpawnWindowStart @SmallmouthSpawnWindowEnd @SmallmouthGuardWarmupDays @SmallmouthGuardTempThreshold @SmallmouthNestStructureSet @SmallmouthGuardStages @SmallmouthGuardingShare @SmallmouthLocalGuardAnchorEligibility @SmallmouthNestSuitabilityProfile @SmallmouthGuardRelationProfile @SmallmouthGuardLocalTemperatureProfile @SmallmouthGuardThreatProfile @SmallmouthNormalLayerProfile @SmallmouthNormalStructureProfile @SmallmouthNormalTemperatureProfile @SmallmouthNormalTimeProfile @SmallmouthNormalTempFloor @SmallmouthNormalFeedingProfile @SmallmouthGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| SM1 | C1 | 当前日期 | — | BETWEEN | @SmallmouthSpawnWindowStart | @SmallmouthSpawnWindowEnd |
| SM1 | C2 | 连续均温 | @SmallmouthGuardWarmupDays | >= | @SmallmouthGuardTempThreshold | — |
| SM1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @SmallmouthNestStructureSet | — |
| SM1 | C4 | 繁殖阶段事实 | — | IN | @SmallmouthGuardStages | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| SmallmouthGuardEligible | AND | 1 | Condition | SM1.C1 |
| SmallmouthGuardEligible | AND | 2 | Condition | SM1.C2 |
| SmallmouthGuardEligible | AND | 3 | Condition | SM1.C3 |
| SmallmouthGuardEligible | AND | 4 | Condition | SM1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Smallmouth_Guard_Route | @SmallmouthGuardEligible | Guarding | Species 内行为份额 | @SmallmouthGuardingShare |
| Smallmouth_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@SmallmouthGuardWarmupDays 天）
读取 当前钓场结构集合
读取 繁殖阶段事实

如果：
    当前日期处于 [@SmallmouthSpawnWindowStart, @SmallmouthSpawnWindowEnd]
    并且 连续均温 >= @SmallmouthGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @SmallmouthNestStructureSet
    并且 繁殖阶段事实 IN @SmallmouthGuardStages（卵床守护 / 稚鱼守护两段）

则：
    GuardingShare = @SmallmouthGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：Species 当前基础供给权重的无量纲分配比例（live §7 契约）。阶段事实（C4）不重复结算 C1–C3 的因果：C1–C3 判资格（窗口 / 适温 / 合法巢区），C4 判当前处于照护阶段（PARENTAL_GUARD 型状态，上游 typed 枚举）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例随阶段切换）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @SmallmouthLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest_bed｜fry_school（随繁殖阶段事实配置级切换；body 不设分支） |
| GuardAnchorRelationProfile | @SmallmouthGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @SmallmouthNestSuitabilityProfile |
| LocalTemperatureProfile | @SmallmouthGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前繁殖阶段事实，选择 GuardAnchorResolver 实例：
    卵床守护阶段 → 锚=nest_bed（当前场内卵床位置）
    稚鱼守护阶段 → 锚=fry_school（当前稚鱼群位置）
读取 当前目标与该锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @SmallmouthLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与锚点的关系查询 @SmallmouthGuardRelationProfile
得到 RelationFit

用当前目标的底质 / 结构查询 @SmallmouthNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @SmallmouthGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @SmallmouthNormalLayerProfile |
| StructureProfile | @SmallmouthNormalStructureProfile |
| TemperatureProfile | @SmallmouthNormalTemperatureProfile |
| TimeProfile | @SmallmouthNormalTimeProfile |
| ExtremeTemperatureGate | @SmallmouthNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段（晨昏活跃方向由 @SmallmouthNormalTimeProfile 值域承载）

用当前水层查询 @SmallmouthNormalLayerProfile 得到 LayerFit
用当前结构查询 @SmallmouthNormalStructureProfile 得到 StructureFit
用当前水温查询 @SmallmouthNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @SmallmouthNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @SmallmouthNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @SmallmouthGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；Reaction 槽 OFF） | @SmallmouthNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与巢区 / 稚鱼群的关系（按当前锚实例）
读取 侵入距离、持续时间、威胁 Cue

评价 @SmallmouthGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @SmallmouthNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @SmallmouthGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼照护组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @SmallmouthGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（阶段事实作第四原子）+ R1；BA-T2 锚实例切换（nest_bed / fry_school，§11.2 MERGE_SUPPORTED）；R-T1 Profile 重绑定；QT-1 Eligibility/Affinity。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0，例 1C）；(2) Guard Bake 合并算子 OPERATOR UNDEFINED；(3) Suski 2003 钓放损失时间反馈——审核禁用项，永不进入本表达；(4) 护巢雄鱼个体的巢位领地史（逐个体状态）——无 Story 证据。
- [需核对] Story DB 行级 Pattern 标签（B01=P04 Mode Candidate + P0x 已由 F-1 复核记载，以 Story DB 为准）；巢床结构集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
