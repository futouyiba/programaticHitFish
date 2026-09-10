# 溪鲦＝黑斑须雅罗鱼（Common Creek Chub｜Semotilus atromaculatus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R08 溪鲦（R08：「溪鲦（石巢第 3 例跨属）」；Story 页 URL 未在本地快照） |
| 名称映射 | triage 批注名「溪鲦」＝fish-reference-20260908 行「黑斑须雅罗鱼 Common Creek Chub Semotilus atromaculatus」（俄 4 映射=青蛙/近似种类比）——同一物（石巢系第 3 例跨属判据即基于此行），实例绑定时以 DB 行身份为准 |
| 冻结 Pattern | P04（石巢守护——同 R07 双点美鱥石巢系第 3 例，跨属重复确认） |
| 物种属性锚 | fish-reference-20260908：水温 0–30.3℃、最适 15.15℃、demersal、早晨活跃、撕鳍（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R08 FR3 归档摘要在 tmp/triage_r08.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：石巢守护——雄鱼筑砾石巢并守护（R08「石巢第 3 例跨属」：与 R07 双点美鱥（Nocomis 属）跨属重复确认同形处置——同一 BA-T2 锚模板 + Profile 重绑定，不新增结构）。
- 跨属重复的计数意义：石巢系第 3 例＝DiscoveryBatch 重复确认样本（同形处置一致性），不是新模板证据（R07/R08 FR3 口径）。
- 筑巢者语义：同双点美鱥——巢体存在事实（guard premise）与筑巢基质资格（路由原子）分开判。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；结构集合成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@CreekChubSpawnWindowStart @CreekChubSpawnWindowEnd @CreekChubGuardWarmupDays @CreekChubGuardTempThreshold @CreekChubNestSiteStructureSet @CreekChubGuardingShare @CreekChubLocalGuardAnchorEligibility @CreekChubStoneNestSuitabilityProfile @CreekChubGuardRelationProfile @CreekChubGuardLocalTemperatureProfile @CreekChubGuardThreatProfile @CreekChubNormalLayerProfile @CreekChubNormalStructureProfile @CreekChubNormalTemperatureProfile @CreekChubNormalTimeProfile @CreekChubNormalTempFloor @CreekChubNormalFeedingProfile @CreekChubGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| CC1 | C1 | 当前日期 | — | BETWEEN | @CreekChubSpawnWindowStart | @CreekChubSpawnWindowEnd |
| CC1 | C2 | 连续均温 | @CreekChubGuardWarmupDays | >= | @CreekChubGuardTempThreshold | — |
| CC1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @CreekChubNestSiteStructureSet | — |
| CC1 | C4 | 巢体存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| CreekChubGuardEligible | AND | 1 | Condition | CC1.C1 |
| CreekChubGuardEligible | AND | 2 | Condition | CC1.C2 |
| CreekChubGuardEligible | AND | 3 | Condition | CC1.C3 |
| CreekChubGuardEligible | AND | 4 | Condition | CC1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| CreekChub_Guard_Route | @CreekChubGuardEligible | Guarding | Species 内行为份额 | @CreekChubGuardingShare |
| CreekChub_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@CreekChubGuardWarmupDays 天）
读取 当前钓场结构集合
读取 石巢存在事实（上游 GuardAnchor Resolver 产出）

如果：
    当前日期处于 [@CreekChubSpawnWindowStart, @CreekChubSpawnWindowEnd]
    并且 连续均温 >= @CreekChubGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @CreekChubNestSiteStructureSet
    并且 巢体存在事实 == 存在

则：
    GuardingShare = @CreekChubGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。C3（基质资格）与 C4（石巢已筑成）不重复结算。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化；与双点美鱥同模板跨属复用）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @CreekChubLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | stone_nest（雄鱼所筑砾石巢 [需正文]） |
| GuardAnchorRelationProfile | @CreekChubGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @CreekChubStoneNestSuitabilityProfile |
| LocalTemperatureProfile | @CreekChubGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的底质 / 砾石滩结构 / 水深
读取 当前目标与石巢锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @CreekChubLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与石巢锚点的关系查询 @CreekChubGuardRelationProfile
得到 RelationFit

用当前目标的砾石底质查询 @CreekChubStoneNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @CreekChubGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @CreekChubNormalLayerProfile |
| StructureProfile | @CreekChubNormalStructureProfile |
| TemperatureProfile | @CreekChubNormalTemperatureProfile |
| TimeProfile | @CreekChubNormalTimeProfile（早晨活跃方向） |
| ExtremeTemperatureGate | @CreekChubNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @CreekChubNormalLayerProfile 得到 LayerFit
用当前结构查询 @CreekChubNormalStructureProfile 得到 StructureFit
用当前水温查询 @CreekChubNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @CreekChubNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @CreekChubNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @CreekChubGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @CreekChubNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与石巢锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @CreekChubGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @CreekChubNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @CreekChubGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼筑巢守护组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @CreekChubGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子 + R1；BA-T2 锚实例=stone_nest（与双点美鱥同模板跨属复用——石巢系第 3 例的同形处置）；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0）；(2) Guard 合并算子数学 OPERATOR UNDEFINED；(3) 属级差异的模板分化（跨属重复＝Profile 重绑定，不建新模板——R08 同形处置口径）。
- [需核对] 名称映射（溪鲦 ↔ 黑斑须雅罗鱼 DB 行）在实例绑定前核对 Story DB 行身份；石巢基质集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
