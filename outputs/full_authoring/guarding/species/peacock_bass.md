# 孔雀鲈＝金目丽鱼属（Cichla spp.）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 Cichla（R09 P04×6「慈鲷+岩礁护卵系内部多样性」之一；triage 批注：「Cichla 第 3 金目」；Story 页 URL 未在本地快照） |
| 种级身份待定 | fish-reference-20260908 含 3 行 Cichla：金目丽鱼（C. temensis，27–29℃）、奥里诺科孔雀鲈（C. orinocensis，27–29℃）、眼点丽鱼（C. ocellaris，24–27℃）——triage「第 3 金目」未指明具体行 [需正文核对 DB 行身份]；三行表达同构（属级共享骨架 + per-instance Profile 重绑定，K13 先例） |
| 冻结 Pattern | P04（双亲护幼——卵床守护与稚鱼群环护两段） |
| 物种属性锚 | fish-reference-20260908（三行见上；benthopelagic、全天活跃、好斗、肉食；行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | Tier B（triage 批注一行；种级身份与 Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护幼形态：双亲护幼——产卵床守护与稚鱼群环护（R09 P04×6 批注的 Cichla 护幼形态；具体巢型 [需正文]，按浅水卵石床方向 @ 化）。
- 两段锚：卵床守护（nest）→ 稚鱼群环护（fry school）——同小口黑鲈两段锚形态（GuardAnchor Resolver 实例切换，§11.2 泛化）。
- 种级身份：三行 Cichla 共用本骨架；实例绑定（哪个 DB 行承载本 Story）待 Story DB 核对；Profile 全部 per-instance 可重绑定（温度轴差异由各 Profile 值域承载）。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；巢床结构集合成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@CichlaSpawnWindowStart @CichlaSpawnWindowEnd @CichlaGuardWarmupDays @CichlaGuardTempThreshold @CichlaNestStructureSet @CichlaGuardStages @CichlaGuardingShare @CichlaLocalGuardAnchorEligibility @CichlaNestSuitabilityProfile @CichlaGuardRelationProfile @CichlaGuardLocalTemperatureProfile @CichlaGuardThreatProfile @CichlaNormalLayerProfile @CichlaNormalStructureProfile @CichlaNormalTemperatureProfile @CichlaNormalTimeProfile @CichlaNormalTempFloor @CichlaNormalFeedingProfile @CichlaGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| CI1 | C1 | 当前日期 | — | BETWEEN | @CichlaSpawnWindowStart | @CichlaSpawnWindowEnd |
| CI1 | C2 | 连续均温 | @CichlaGuardWarmupDays | >= | @CichlaGuardTempThreshold | — |
| CI1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @CichlaNestStructureSet | — |
| CI1 | C4 | 繁殖阶段事实 | — | IN | @CichlaGuardStages | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| CichlaGuardEligible | AND | 1 | Condition | CI1.C1 |
| CichlaGuardEligible | AND | 2 | Condition | CI1.C2 |
| CichlaGuardEligible | AND | 3 | Condition | CI1.C3 |
| CichlaGuardEligible | AND | 4 | Condition | CI1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Cichla_Guard_Route | @CichlaGuardEligible | Guarding | Species 内行为份额 | @CichlaGuardingShare |
| Cichla_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@CichlaGuardWarmupDays 天）
读取 当前钓场结构集合
读取 繁殖阶段事实

如果：
    当前日期处于 [@CichlaSpawnWindowStart, @CichlaSpawnWindowEnd]
    并且 连续均温 >= @CichlaGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @CichlaNestStructureSet
    并且 繁殖阶段事实 IN @CichlaGuardStages（卵床守护 / 稚鱼环护两段）

则：
    GuardingShare = @CichlaGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。双亲护幼由份额整体表达；种级身份未定不影响路由结构（三行同构）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例随阶段切换）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @CichlaLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest（卵床守护段）｜fry_school（稚鱼群环护段；随繁殖阶段事实配置级切换，body 不设分支） |
| GuardAnchorRelationProfile | @CichlaGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @CichlaNestSuitabilityProfile |
| LocalTemperatureProfile | @CichlaGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的底质 / 浅水结构 / 水深
读取 当前繁殖阶段事实，选择 GuardAnchorResolver 实例：
    卵床守护段 → 锚=nest（当前场内卵床位置）
    稚鱼环护段 → 锚=fry_school（当前稚鱼群位置）
读取 当前目标与该锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @CichlaLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与锚点的关系查询 @CichlaGuardRelationProfile
得到 RelationFit

用当前目标的底质结构查询 @CichlaNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @CichlaGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @CichlaNormalLayerProfile |
| StructureProfile | @CichlaNormalStructureProfile |
| TemperatureProfile | @CichlaNormalTemperatureProfile（种级温度轴差异由此 Profile per-instance 承载） |
| TimeProfile | @CichlaNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @CichlaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @CichlaNormalLayerProfile 得到 LayerFit
用当前结构查询 @CichlaNormalStructureProfile 得到 StructureFit
用当前水温查询 @CichlaNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @CichlaNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @CichlaNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @CichlaGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @CichlaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与卵床 / 稚鱼群锚点的关系（按当前锚实例）
读取 侵入距离、持续时间、威胁 Cue

评价 @CichlaGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @CichlaNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @CichlaGuardingEligibilityByQuality | @NeutralAffinity | 成熟双亲护幼组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @CichlaGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子 + R1；BA-T2 两段锚切换（nest / fry_school）；R-T1 Profile 重绑定；QT-1；属级三行共享骨架 + per-instance 重绑定。
- 放弃的自由度：(1) 种级模板分化（三 Cichla 行同构——K13 per-instance 重绑定先例）；(2) Defense / Feeding arbitration（live V0）；(3) Guard 合并算子数学 OPERATOR UNDEFINED。
- [需核对] triage「Cichla 第 3 金目」对应的 DB 行（temensis / orinocensis / ocellaris）与 Story 页身份；[需正文] 卵床结构集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
