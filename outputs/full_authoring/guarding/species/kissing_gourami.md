# 接吻鲷（Kissing Gourami｜Helostoma temminckii）｜Guarding 系四面表达——骨架占位档（P04 归属待 Story 正文）

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED
**SKELETON_PLACEHOLDER——本文件为 P04 标准骨架占位：本地快照对这条 Story 只有批注名「接吻鲷」（R09 P04×6 名单），护巢形态（巢型 / 亲鱼组成 / 守护对象）零本地证据。若 Story 正文判无护巢关系（P04 归属不成立），本文件整体撤回。**

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 接吻鲷（R09 P04×6「慈鲷+岩礁护卵系内部多样性」名单成员；triage 批注仅「接吻鲷」三字；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（R09 P04×6 名单转述；护巢形态细节 [需正文]） |
| 物种属性锚 | fish-reference-20260908：水温 22–28℃、最适 25℃、benthopelagic、深 2m–、全天活跃、躲藏、杂食（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | **Tier C（仅名单成员资格；零形态证据）** |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：**未知（本地零证据）**——本节所有语义要素全部待 Story 正文：产卵基质（巢型）、亲鱼组成（单亲 / 双亲）、守护对象（卵 / 稚鱼）、守护期窗口。
- 骨架占位策略：以下四面按 P04 标准骨架（例 1 + BA-T2 + Defense-only + QT-1）给出**全 @ 化零数值形态**——每一条具体语义都显式挂 [需正文]；这保证「结构可装、语义未装」，Story 正文到达后只填 Profile 语义，不改结构。
- 互斥状态：ReproductionState ∈ {NONE, …}（成员待正文）。
- 撤回条件：Story 正文若判「无护巢关系」（如开放水域播撒产卵、无守护行为），则本 Story 不属 P04，本文件整体撤回（R06 停食洄游判例同款纪律：guard relation 未证实即归属=False FIT）。

Profile 引用清单：@KissingGouramiSpawnWindowStart @KissingGouramiSpawnWindowEnd @KissingGouramiGuardWarmupDays @KissingGouramiGuardTempThreshold @KissingGouramiSpawnStructureSet @KissingGouramiGuardingShare @KissingGouramiLocalGuardAnchorEligibility @KissingGouramiSpawnSuitabilityProfile @KissingGouramiGuardRelationProfile @KissingGouramiGuardLocalTemperatureProfile @KissingGouramiGuardThreatProfile @KissingGouramiNormalLayerProfile @KissingGouramiNormalStructureProfile @KissingGouramiNormalTemperatureProfile @KissingGouramiNormalTimeProfile @KissingGouramiNormalTempFloor @KissingGouramiNormalFeedingProfile @KissingGouramiGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2；三原子语义全待正文）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| KG1 | C1 | 当前日期 | — | BETWEEN | @KissingGouramiSpawnWindowStart | @KissingGouramiSpawnWindowEnd |
| KG1 | C2 | 连续均温 | @KissingGouramiGuardWarmupDays | >= | @KissingGouramiGuardTempThreshold | — |
| KG1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @KissingGouramiSpawnStructureSet | — |

[需正文] C1 窗口、C2 阈值语义、C3 结构集合成员（产卵基质类型）全部由 Story 正文 + Profile 层定值；C3 若正文判「无结构依赖产卵」（开放水面播撒），本原子删除而非置空集。

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| KissingGouramiGuardEligible | AND | 1 | Condition | KG1.C1 |
| KissingGouramiGuardEligible | AND | 2 | Condition | KG1.C2 |
| KissingGouramiGuardEligible | AND | 3 | Condition | KG1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| KissingGourami_Guard_Route | @KissingGouramiGuardEligible | Guarding | Species 内行为份额 | @KissingGouramiGuardingShare |
| KissingGourami_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@KissingGouramiGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@KissingGouramiSpawnWindowStart, @KissingGouramiSpawnWindowEnd]
    并且 连续均温 >= @KissingGouramiGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @KissingGouramiSpawnStructureSet

则：
    GuardingShare = @KissingGouramiGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。本脚本为骨架形态——其成立以 Story 正文确认护巢关系为前提。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化；锚实例待正文）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @KissingGouramiLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | 待正文（nest / surface_spawn / fry_school 之一，视守护对象而定） |
| GuardAnchorRelationProfile | @KissingGouramiGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @KissingGouramiSpawnSuitabilityProfile |
| LocalTemperatureProfile | @KissingGouramiGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（骨架展开；锚点类型占位）

```plain text
读取 当前目标的结构 / 底质 / 水深
读取 当前守护对象锚点位置（上游 GuardAnchor Resolver 产出；实例待正文）
读取 当前目标与锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @KissingGouramiLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与锚点的关系查询 @KissingGouramiGuardRelationProfile
得到 RelationFit

用当前目标的结构查询 @KissingGouramiSpawnSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @KissingGouramiGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @KissingGouramiNormalLayerProfile |
| StructureProfile | @KissingGouramiNormalStructureProfile |
| TemperatureProfile | @KissingGouramiNormalTemperatureProfile |
| TimeProfile | @KissingGouramiNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @KissingGouramiNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @KissingGouramiNormalLayerProfile 得到 LayerFit
用当前结构查询 @KissingGouramiNormalStructureProfile 得到 StructureFit
用当前水温查询 @KissingGouramiNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @KissingGouramiNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @KissingGouramiNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @KissingGouramiGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @KissingGouramiNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与守护对象锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @KissingGouramiGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @KissingGouramiNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @KissingGouramiGuardingEligibilityByQuality | @NeutralAffinity | 成熟护巢组成（亲鱼组成待正文）；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @KissingGouramiGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：仅 P04 标准骨架（V1 三原子 + R1 + BA-T2 + Defense-only + QT-1）——**零物种级语义自由度被使用**（全部 [需正文]）。
- 放弃的自由度：无实质取舍可记录（骨架不装语义）。
- 撤回条件（重申）：Story 正文判无护巢关系 ⇒ 本文件整体撤回，R09 P04×6 计数随 Story DB 对账修正。
- [需正文] 产卵基质类型、亲鱼组成、守护对象、窗口——本文件唯一目标是把「结构可装」先钉住。

BATCH_ID: REP-FULL-GUARD-001
