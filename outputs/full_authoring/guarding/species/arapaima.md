# 巨骨舌鱼（Arapaima｜Arapaima gigas）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R06 巨骨舌鱼（R06 P04×3 护巢组之一；FR3 抽验名单：「巨骨舌鱼洪水护幼」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（R06 FR3 抽验名单转述：洪水护幼——雄鱼环护稚鱼群关系） |
| 物种属性锚 | fish-reference-20260908：水温 25–29℃、最适 27℃、demersal、晨昏活跃、追猎（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R06 FR3 归档摘要在 tmp/triage_r06.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding(BroodCare)=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护幼形态：洪水护幼——高水位期雄鱼环护稚鱼群（洪泛漫滩上的 fry school 移动锚；R06 FR3 抽验名单一句）。
- 洪水耦合：guard 与洪水位相耦合（低水位不触发护幼路由）——位相事实是路由条件原子，不是 Bake 因子（防双重结算：Group 面读位相做路由，Bake 面不重复读位相做惩罚）。
- 洪泛漫滩空间：漫滩槽位 = DynamicSpatialSlot 消费上游洪泛可及性事实（REP-COVERAGE-DELTA-001 K1/K14 洪泛漫滩先例——#36 革胡子鲶同构）；洪泛区锚解析归上游 Fry / Brood Field Resolver。
- 互斥状态：洪水位相 ∈ {LOW_WATER, RISING, HIGH_WATER, FALLING}（typed 枚举；本 Story 冻结高水位护幼行）× guard_state ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；位相成员、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@ArapaimaHighWaterPhases @ArapaimaSpawnWindowStart @ArapaimaSpawnWindowEnd @ArapaimaGuardWarmupDays @ArapaimaGuardTempThreshold @ArapaimaBroodStructureSet @ArapaimaGuardingShare @ArapaimaLocalGuardAnchorEligibility @ArapaimaBroodHabitatSuitabilityProfile @ArapaimaGuardRelationProfile @ArapaimaGuardLocalTemperatureProfile @ArapaimaGuardThreatProfile @ArapaimaNormalLayerProfile @ArapaimaNormalStructureProfile @ArapaimaNormalTemperatureProfile @ArapaimaNormalTimeProfile @ArapaimaNormalTempFloor @ArapaimaNormalFeedingProfile @ArapaimaGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| AR1 | C1 | 洪水位相事实 | — | IN | @ArapaimaHighWaterPhases | — |
| AR1 | C2 | 当前日期 | — | BETWEEN | @ArapaimaSpawnWindowStart | @ArapaimaSpawnWindowEnd |
| AR1 | C3 | 连续均温 | @ArapaimaGuardWarmupDays | >= | @ArapaimaGuardTempThreshold | — |
| AR1 | C4 | 场内结构集合 | — | CONTAINS_ANY | @ArapaimaBroodStructureSet | — |
| AR1 | C5 | 稚鱼群存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| ArapaimaBroodCareEligible | AND | 1 | Condition | AR1.C1 |
| ArapaimaBroodCareEligible | AND | 2 | Condition | AR1.C2 |
| ArapaimaBroodCareEligible | AND | 3 | Condition | AR1.C3 |
| ArapaimaBroodCareEligible | AND | 4 | Condition | AR1.C4 |
| ArapaimaBroodCareEligible | AND | 5 | Condition | AR1.C5 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Arapaima_BroodCare_Route | @ArapaimaBroodCareEligible | BroodCare | Species 内行为份额 | @ArapaimaGuardingShare |
| Arapaima_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 洪水位相事实
读取 当前日期
读取 连续均温（窗口=@ArapaimaGuardWarmupDays 天）
读取 当前钓场结构集合
读取 稚鱼群存在事实（上游 Fry / Brood Field Resolver：洪泛漫滩稚鱼群）

如果：
    洪水位相事实 IN @ArapaimaHighWaterPhases
    并且 当前日期处于 [@ArapaimaSpawnWindowStart, @ArapaimaSpawnWindowEnd]
    并且 连续均温 >= @ArapaimaGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @ArapaimaBroodStructureSet
    并且 稚鱼群存在事实 == 存在

则：
    BroodCareShare = @ArapaimaGuardingShare

否则：
    BroodCareShare = 0

SpecialShareTotal = BroodCareShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 BroodCareShare / NormalFeedingShare
```

Share 语义：live §7 契约。位相原子只在 Group 面结算一次（§8.5 anti-double-counting）。

## 2. Bake

### 2.1 BroodCare Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化 + 洪泛漫滩 DynamicSpatialSlot）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE + DynamicSpatialSlot（洪泛漫滩） |
| GuardAnchorEligibilityRule | @ArapaimaLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | fry_school（洪泛漫滩稚鱼群；移动锚） |
| GuardAnchorRelationProfile | @ArapaimaGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @ArapaimaBroodHabitatSuitabilityProfile |
| LocalTemperatureProfile | @ArapaimaGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 BroodCare Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 水深 / 漫滩可及性事实（上游洪泛事实）
读取 当前稚鱼群锚点位置（上游 Fry / Brood Field Resolver 产出）
读取 当前目标与稚鱼群锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @ArapaimaLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与稚鱼群的关系查询 @ArapaimaGuardRelationProfile
得到 RelationFit

用当前目标的漫滩掩体查询 @ArapaimaBroodHabitatSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @ArapaimaGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 BroodCare SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @ArapaimaNormalLayerProfile |
| StructureProfile | @ArapaimaNormalStructureProfile |
| TemperatureProfile | @ArapaimaNormalTemperatureProfile |
| TimeProfile | @ArapaimaNormalTimeProfile（晨昏活跃方向） |
| ExtremeTemperatureGate | @ArapaimaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @ArapaimaNormalLayerProfile 得到 LayerFit
用当前结构查询 @ArapaimaNormalStructureProfile 得到 StructureFit
用当前水温查询 @ArapaimaNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @ArapaimaNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @ArapaimaNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| BroodCare | 顺序响应规则（Defense-only） | @ArapaimaGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @ArapaimaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

BroodCare Group：

```plain text
读取 当前 Presentation 与稚鱼群锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @ArapaimaGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @ArapaimaNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| BroodCare | QT-1 | @ArapaimaGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼护幼组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（BroodCare 行查 @ArapaimaGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（洪水位相 IN + 稚鱼群存在）+ R1；BA-T2 锚实例=fry_school + 漫滩 DynamicSpatialSlot；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0）；(2) Guard 合并算子数学 OPERATOR UNDEFINED；(3) 洪水位相的 Bake 面重复惩罚（anti-double-counting：位相只在 Group 面结算）。
- [需正文] 高水位位相成员（RISING/HIGH_WATER/FALLING 归属）；窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
