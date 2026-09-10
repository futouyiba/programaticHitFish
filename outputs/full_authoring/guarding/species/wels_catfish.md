# 欧洲巨鲶（Wels Catfish｜Silurus glanis）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R06 欧洲巨鲶（R06 P04×3 护巢组之一；FR3 抽验名单：「欧洲巨鲶雄鱼守巢」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（R06 FR3 抽验名单转述：雄鱼守巢——洞巢守卵关系） |
| 物种属性锚 | fish-reference-20260908：水温 4–20℃、最适 12℃、benthopelagic、深 0–30m、夜间活跃、孤僻（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R06 FR3 归档摘要在 tmp/triage_r06.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding，夜行低光 context） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼守巢（洞巢守卵——河岸洞窟 / 树根盘下巢穴中的卵体守护；R06 FR3 抽验名单一句）。
- 常态面：夜间活跃底栖掠食（物种属性锚方向；夜行低光由 TimeProfile 值域承载，不建独立 Group）。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；巢洞结构集合成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@WelsSpawnWindowStart @WelsSpawnWindowEnd @WelsGuardWarmupDays @WelsGuardTempThreshold @WelsNestStructureSet @WelsGuardingShare @WelsLocalGuardAnchorEligibility @WelsNestSuitabilityProfile @WelsGuardRelationProfile @WelsGuardLocalTemperatureProfile @WelsGuardThreatProfile @WelsNormalLayerProfile @WelsNormalStructureProfile @WelsNormalTemperatureProfile @WelsNormalTimeProfile @WelsNormalTempFloor @WelsNormalFeedingProfile @WelsGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| WE1 | C1 | 当前日期 | — | BETWEEN | @WelsSpawnWindowStart | @WelsSpawnWindowEnd |
| WE1 | C2 | 连续均温 | @WelsGuardWarmupDays | >= | @WelsGuardTempThreshold | — |
| WE1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @WelsNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| WelsGuardEligible | AND | 1 | Condition | WE1.C1 |
| WelsGuardEligible | AND | 2 | Condition | WE1.C2 |
| WelsGuardEligible | AND | 3 | Condition | WE1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Wels_Guard_Route | @WelsGuardEligible | Guarding | Species 内行为份额 | @WelsGuardingShare |
| Wels_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@WelsGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@WelsSpawnWindowStart, @WelsSpawnWindowEnd]
    并且 连续均温 >= @WelsGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @WelsNestStructureSet

则：
    GuardingShare = @WelsGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。「雄鱼守巢」的雄性组成由 Eligibility / share 表达，不引入逐个体性别属性。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @WelsLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | burrow_nest（河岸洞窟 / 树根盘洞巢 [需正文]） |
| GuardAnchorRelationProfile | @WelsGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @WelsNestSuitabilityProfile |
| LocalTemperatureProfile | @WelsGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前目标与洞巢锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @WelsLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与洞巢锚点的关系查询 @WelsGuardRelationProfile
得到 RelationFit

用当前目标的洞窟 / 树根盘结构查询 @WelsNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @WelsGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @WelsNormalLayerProfile（底栖方向） |
| StructureProfile | @WelsNormalStructureProfile |
| TemperatureProfile | @WelsNormalTemperatureProfile |
| TimeProfile | @WelsNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @WelsNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @WelsNormalLayerProfile 得到 LayerFit
用当前结构查询 @WelsNormalStructureProfile 得到 StructureFit
用当前水温查询 @WelsNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @WelsNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @WelsNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @WelsGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @WelsNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与洞巢锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @WelsGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @WelsNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @WelsGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼守巢组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @WelsGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=burrow_nest；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0）；(2) Guard 合并算子数学 OPERATOR UNDEFINED；(3) 雄性个体识别（Eligibility / share 粒度）。
- [需正文] 洞巢结构集合成员与窗口数值由 Profile 层定值。
- [需正文·结构级] C4（巢体存在原子）有无取决于正文是否判「洞巢为雄鱼挖掘/清理建造」——若建造语义成立则需补 C4 原子（改结构），与「只填 Profile 不改结构」承诺冲突；本文件按场地利用型处理（无 C4）为当前判断（REV-001 F4）。

BATCH_ID: REP-FULL-GUARD-001
