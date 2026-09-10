# 圆鳍鱼（Lumpfish｜Cyclopterus lumpus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 圆鳍鱼（R09 P04×6「慈鲷+岩礁护卵系内部多样性」之一；triage 批注：「圆鳍鱼（吸盘+雄激进护卵）」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（雄鱼浅水岩礁护卵——雄性激进守护型，R09 P04 内部多样性样本） |
| 物种属性锚 | fish-reference-20260908：水温 3–11℃、最适 7℃、benthopelagic、深 0–868m、全天活跃、海水（行级 AI 审核状态=待人工审核；仅作方向锚；吸盘为底面附着结构属性） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0；「雄激进」=Threat Profile 值域方向，不冻结强度）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼浅水岩礁护卵（R09 triage 批注「吸盘+雄激进护卵」）——雄鱼守护岩礁 / 卵块附着基上的卵体，守护强度方向=激进（Profile 值域方向，数值不冻结）。
- 吸盘归属：吸盘（底面附着结构）＝物种形态属性，属资产 / 感知面方向锚——**不进四面任何条件原子或通道**（无 Story 语义把它变成机制轴）。
- 「雄激进」的表达纪律：R09 批注词「激进」是强度方向描述——落 @LumpfishGuardThreatProfile 值域方向（不冻结数值）；**不**升格为 Response 面新通道 / 新模板（防「强度词走私结构」）。
- 海水场景：population 绑定海水钓场（venue 级 population 属性，非路由条件——不写「水体类型 IN」原子，防与 population 绑定双重结算）。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；附着基结构集合成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@LumpfishSpawnWindowStart @LumpfishSpawnWindowEnd @LumpfishGuardWarmupDays @LumpfishGuardTempThreshold @LumpfishSpawningStructureSet @LumpfishGuardingShare @LumpfishLocalGuardAnchorEligibility @LumpfishSpawnSurfaceSuitabilityProfile @LumpfishGuardRelationProfile @LumpfishGuardLocalTemperatureProfile @LumpfishGuardThreatProfile @LumpfishNormalLayerProfile @LumpfishNormalStructureProfile @LumpfishNormalTemperatureProfile @LumpfishNormalTimeProfile @LumpfishNormalTempFloor @LumpfishNormalFeedingProfile @LumpfishGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| LF1 | C1 | 当前日期 | — | BETWEEN | @LumpfishSpawnWindowStart | @LumpfishSpawnWindowEnd |
| LF1 | C2 | 连续均温 | @LumpfishGuardWarmupDays | >= | @LumpfishGuardTempThreshold | — |
| LF1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @LumpfishSpawningStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| LumpfishGuardEligible | AND | 1 | Condition | LF1.C1 |
| LumpfishGuardEligible | AND | 2 | Condition | LF1.C2 |
| LumpfishGuardEligible | AND | 3 | Condition | LF1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Lumpfish_Guard_Route | @LumpfishGuardEligible | Guarding | Species 内行为份额 | @LumpfishGuardingShare |
| Lumpfish_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@LumpfishGuardWarmupDays 天；冷水系阈值方向由 Profile 层承载）
读取 当前钓场结构集合

如果：
    当前日期处于 [@LumpfishSpawnWindowStart, @LumpfishSpawnWindowEnd]
    并且 连续均温 >= @LumpfishGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @LumpfishSpawningStructureSet（浅水岩礁 / 卵块附着基）

则：
    GuardingShare = @LumpfishGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。雄性组成由 Eligibility / share 表达；海水 population 绑定不进路由原子。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=岩礁卵块）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @LumpfishLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | rock_spawn（浅水岩礁卵块 / 附着基 [需正文]） |
| GuardAnchorRelationProfile | @LumpfishGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @LumpfishSpawnSurfaceSuitabilityProfile |
| LocalTemperatureProfile | @LumpfishGuardLocalTemperatureProfile（冷水轴） |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的岩礁结构 / 底质 / 深度
读取 当前目标与卵块锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @LumpfishLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与卵块锚点的关系查询 @LumpfishGuardRelationProfile
得到 RelationFit

用当前目标的岩礁附着面查询 @LumpfishSpawnSurfaceSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @LumpfishGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @LumpfishNormalLayerProfile |
| StructureProfile | @LumpfishNormalStructureProfile |
| TemperatureProfile | @LumpfishNormalTemperatureProfile（冷水轴：3–11℃ 方向由 Profile 值域承载） |
| TimeProfile | @LumpfishNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @LumpfishNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @LumpfishNormalLayerProfile 得到 LayerFit
用当前结构查询 @LumpfishNormalStructureProfile 得到 StructureFit
用当前水温查询 @LumpfishNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @LumpfishNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @LumpfishNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @LumpfishGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @LumpfishNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与卵块锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @LumpfishGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

强度方向注记：「雄激进护卵」（R09 批注词）＝@LumpfishGuardThreatProfile 值域方向声明（同方向高、阈值低的 Profile 形态候选）；数值不冻结，不升格新通道。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @LumpfishNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @LumpfishGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼护卵组成；资格与 Response 分开（§12.6——「激进」留在 Response，不写品质 Bonus） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @LumpfishGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=rock_spawn；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) 吸盘机制轴（无 Story 语义，不进四面）；(2) 「激进」强度数值（Profile 值域方向，不冻结）；(3) Defense / Feeding arbitration（live V0）；(4) Guard 合并算子数学 OPERATOR UNDEFINED。
- [需正文] 附着基结构集合成员、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
