# 单鳍多线鱼（Atka Mackerel｜Pleurogrammus monopterygius）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 单鳍多线鱼（R09 P04×6「慈鲷+岩礁护卵系内部多样性」之一；triage 批注：「单鳍多线鱼（岩缝胸鳍扇卵 40-45 天）」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（岩缝产卵 + 长期扇护——雄鱼岩礁岩缝卵块守护型，R09 P04 内部多样性样本） |
| 物种属性锚 | fish-reference-20260908：水温 2.7–4.7℃、最适 3.7℃、demersal、深 0–720m、全天活跃、海水（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | Tier B（triage 批注一行——含守护期常量「40–45 天」；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼岩缝产卵 + 胸鳍扇卵守护（R09 triage 批注「岩缝胸鳍扇卵 40-45 天」）——卵产于岩礁岩缝 / 平台，雄鱼以胸鳍扇水供氧并守护，守护期约 40–45 天（**Story 证据常量，照录于此**；它是 persistent condition 的证据描述，不是本文件配置数值）。
- 扇卵的归属边界：扇卵（fanning）是朝向卵块的照护行为（对卵，不对呈现）——属 guard premise 的持续性证据，**不进 Response 面**（Response 只评价对呈现的关系性响应；防「照护行为走私成 Response 通道」）。
- 海水场景：population 绑定海水钓场（venue 级属性，非路由条件）。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}（PARENTAL_GUARD 行在本鱼持续约 40–45 天——窗口期长度事实归 Story 正文层）。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；岩缝结构集合成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@AtkaSpawnWindowStart @AtkaSpawnWindowEnd @AtkaGuardWarmupDays @AtkaGuardTempThreshold @AtkaSpawningStructureSet @AtkaGuardingShare @AtkaLocalGuardAnchorEligibility @AtkaCreviceSpawnSuitabilityProfile @AtkaGuardRelationProfile @AtkaGuardLocalTemperatureProfile @AtkaGuardThreatProfile @AtkaNormalLayerProfile @AtkaNormalStructureProfile @AtkaNormalTemperatureProfile @AtkaNormalTimeProfile @AtkaNormalTempFloor @AtkaNormalFeedingProfile @AtkaGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| AK1 | C1 | 当前日期 | — | BETWEEN | @AtkaSpawnWindowStart | @AtkaSpawnWindowEnd |
| AK1 | C2 | 连续均温 | @AtkaGuardWarmupDays | >= | @AtkaGuardTempThreshold | — |
| AK1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @AtkaSpawningStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| AtkaGuardEligible | AND | 1 | Condition | AK1.C1 |
| AtkaGuardEligible | AND | 2 | Condition | AK1.C2 |
| AtkaGuardEligible | AND | 3 | Condition | AK1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Atka_Guard_Route | @AtkaGuardEligible | Guarding | Species 内行为份额 | @AtkaGuardingShare |
| Atka_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@AtkaGuardWarmupDays 天；冷水系阈值方向由 Profile 层承载）
读取 当前钓场结构集合

如果：
    当前日期处于 [@AtkaSpawnWindowStart, @AtkaSpawnWindowEnd]
    并且 连续均温 >= @AtkaGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @AtkaSpawningStructureSet（岩缝 / 礁石平台产卵面）

则：
    GuardingShare = @AtkaGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。守护期 40–45 天的持续性由繁殖窗口事实的上游口径承载（窗口长度=Story 事实层），不进路由原子。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=岩缝卵块）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @AtkaLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | crevice_spawn（岩缝 / 礁石平台卵块 [需正文]） |
| GuardAnchorRelationProfile | @AtkaGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @AtkaCreviceSpawnSuitabilityProfile |
| LocalTemperatureProfile | @AtkaGuardLocalTemperatureProfile（冷水轴：2.7–4.7℃ 方向由 Profile 值域承载） |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的岩礁结构 / 岩缝分布 / 深度
读取 当前目标与卵块锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @AtkaLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与卵块锚点的关系查询 @AtkaGuardRelationProfile
得到 RelationFit

用当前目标的岩缝结构查询 @AtkaCreviceSpawnSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @AtkaGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @AtkaNormalLayerProfile |
| StructureProfile | @AtkaNormalStructureProfile |
| TemperatureProfile | @AtkaNormalTemperatureProfile（冷水轴） |
| TimeProfile | @AtkaNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @AtkaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @AtkaNormalLayerProfile 得到 LayerFit
用当前结构查询 @AtkaNormalStructureProfile 得到 StructureFit
用当前水温查询 @AtkaNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @AtkaNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @AtkaNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @AtkaGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @AtkaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与岩缝卵块锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @AtkaGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

边界注记：胸鳍扇卵（朝向卵块的照护行为）不进本 Response 面——它由 guard premise 的持续性事实承载（§0）；把扇卵写成 Response 通道会造成「照护行为」与「对呈现响应」双重结算。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @AtkaNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @AtkaGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼扇护组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @AtkaGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=crevice_spawn；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) 扇卵行为进 Response 面（拒——照护行为属 premise 持续性证据）；(2) 守护期天数作配置数值（40–45 天是 Story 事实常量，窗口口径归上游事实层）；(3) Defense / Feeding arbitration（live V0）；(4) Guard 合并算子数学 OPERATOR UNDEFINED。
- [需正文] 岩缝结构集合成员、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
