# 红腹食人鱼（Red-bellied Piranha｜Pygocentrus nattereri）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R06 红腹食人鱼（R06 P04×3 护巢组之一；FR3 抽验名单：「红腹食人鱼树根护卵」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（R06 FR3 抽验名单转述：树根护卵——护卵关系） |
| 姊妹判例 | R06 FR3 frenzy 校正：群游=防御性替代解释（Wikipedia 无证据形态），不买 frenzy Group Mode（Negative Knowledge 入 Registry note）——本文件不建 frenzy 组 |
| 物种属性锚 | fish-reference-20260908：水温 23–27℃、最适 25℃、pelagic、全天活跃（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R06 FR3 归档摘要在 tmp/triage_r06.md + outputs/batches/FISH-R06-FR3-001.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：树根护卵（沉水树根 / 水草丛间的卵体守护；R06 FR3 抽验名单一句）——亲鱼组成（单亲 / 双亲）与守护强度未在本地快照 [需正文]。
- Negative Knowledge 边界（R06 FR3 判例转述）：frenzy 群游行为**无证据支持**（no investigation shows 形态 + 防御性替代解释），不买 Group Mode——本文件只有 Guarding / NormalFeeding 两组，不建 Frenzy 组；evidence-shows 翻转条件在 Registry note。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；结构集合成员、亲鱼组成、窗口数值全部 @ 化或标注 [需正文]，不冒充 Story 正文。

Profile 引用清单：@PiranhaSpawnWindowStart @PiranhaSpawnWindowEnd @PiranhaGuardWarmupDays @PiranhaGuardTempThreshold @PiranhaNestStructureSet @PiranhaGuardingShare @PiranhaLocalGuardAnchorEligibility @PiranhaNestSuitabilityProfile @PiranhaGuardRelationProfile @PiranhaGuardLocalTemperatureProfile @PiranhaGuardThreatProfile @PiranhaNormalLayerProfile @PiranhaNormalStructureProfile @PiranhaNormalTemperatureProfile @PiranhaNormalTimeProfile @PiranhaNormalTempFloor @PiranhaNormalFeedingProfile @PiranhaGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| PI1 | C1 | 当前日期 | — | BETWEEN | @PiranhaSpawnWindowStart | @PiranhaSpawnWindowEnd |
| PI1 | C2 | 连续均温 | @PiranhaGuardWarmupDays | >= | @PiranhaGuardTempThreshold | — |
| PI1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @PiranhaNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| PiranhaGuardEligible | AND | 1 | Condition | PI1.C1 |
| PiranhaGuardEligible | AND | 2 | Condition | PI1.C2 |
| PiranhaGuardEligible | AND | 3 | Condition | PI1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Piranha_Guard_Route | @PiranhaGuardEligible | Guarding | Species 内行为份额 | @PiranhaGuardingShare |
| Piranha_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@PiranhaGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@PiranhaSpawnWindowStart, @PiranhaSpawnWindowEnd]
    并且 连续均温 >= @PiranhaGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @PiranhaNestStructureSet

则：
    GuardingShare = @PiranhaGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。无 Frenzy 组（Negative Knowledge 判例）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @PiranhaLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | root_spawn（沉水树根 / 水草丛卵体锚 [需正文]） |
| GuardAnchorRelationProfile | @PiranhaGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @PiranhaNestSuitabilityProfile |
| LocalTemperatureProfile | @PiranhaGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 水深 / 沉水植被关系
读取 当前目标与树根卵体锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @PiranhaLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与卵体锚点的关系查询 @PiranhaGuardRelationProfile
得到 RelationFit

用当前目标的沉水结构查询 @PiranhaNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @PiranhaGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @PiranhaNormalLayerProfile（pelagic 方向） |
| StructureProfile | @PiranhaNormalStructureProfile |
| TemperatureProfile | @PiranhaNormalTemperatureProfile |
| TimeProfile | @PiranhaNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @PiranhaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @PiranhaNormalLayerProfile 得到 LayerFit
用当前结构查询 @PiranhaNormalStructureProfile 得到 StructureFit
用当前水温查询 @PiranhaNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @PiranhaNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @PiranhaNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @PiranhaGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @PiranhaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与树根卵体锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @PiranhaGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @PiranhaNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @PiranhaGuardingEligibilityByQuality | @NeutralAffinity | 成熟亲鱼护卵组成（单亲 / 双亲待正文）；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @PiranhaGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=root_spawn；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) Frenzy Group Mode（R06 Negative Knowledge 判例——无证据不建组）；(2) Defense / Feeding arbitration（live V0）；(3) Guard 合并算子数学 OPERATOR UNDEFINED。
- [需正文] 亲鱼组成（Quality Eligibility 成员）；树根护卵结构集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
