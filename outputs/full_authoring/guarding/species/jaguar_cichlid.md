# 淡水石斑＝珍珠虎鲷（Jaguar Cichlid｜Parachromis managuensis）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 淡水石斑（R09 P04×6「慈鲷+岩礁护卵系内部多样性」之一；triage 批注：「浊水双亲淡水石斑」；Story 页 URL 未在本地快照） |
| 名称映射 | fish-reference-20260908 行「淡水石斑｜Jaguar Cichlid｜Parachromis managuensis」（好斗，肉食，水温 25–36℃）——triage 名与 DB 行名一致 |
| 冻结 Pattern | P04（浊水双亲护幼——浊水语境下的双亲育幼关系，R09 P04 内部多样性样本） |
| 物种属性锚 | fish-reference-20260908：水温 25–36℃、最适 30.5℃、benthopelagic、深 3–10m、全天活跃、好斗（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护幼形态：浊水双亲护幼——浊水语境下双亲育幼（R09 triage 批注「浊水双亲淡水石斑」）；巢型 / 产卵基质未在本地快照 [需正文]。
- 浊度的落面：浊水＝**Bake 语境因子（unary 轴实例）**，不是 Group 路由条件——「浊水双亲」描述该 Story 的环境语境（Knife §10 盐度先例：轴实例而非新结构；REP-COVERAGE-DELTA-001 #27 同构）。浊度既不改变护幼路由资格，也不重复结算（Bake 面只读一次浊度事实）。
- P04 内部多样性意义（R09 FR3 待裁口径）：护卵变体一律落同模板（BA-T2）+ Profile 重绑定，不建新模板。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；巢面结构集合成员、浊度档位、窗口数值全部 @ 化或标注 [需正文]。

Profile 引用清单：@JaguarSpawnWindowStart @JaguarSpawnWindowEnd @JaguarGuardWarmupDays @JaguarGuardTempThreshold @JaguarNestStructureSet @JaguarGuardingShare @JaguarLocalGuardAnchorEligibility @JaguarNestSuitabilityProfile @JaguarGuardRelationProfile @JaguarGuardLocalTemperatureProfile @JaguarTurbidityProfile @JaguarGuardThreatProfile @JaguarNormalLayerProfile @JaguarNormalStructureProfile @JaguarNormalTemperatureProfile @JaguarNormalTimeProfile @JaguarNormalTempFloor @JaguarNormalFeedingProfile @JaguarGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| JA1 | C1 | 当前日期 | — | BETWEEN | @JaguarSpawnWindowStart | @JaguarSpawnWindowEnd |
| JA1 | C2 | 连续均温 | @JaguarGuardWarmupDays | >= | @JaguarGuardTempThreshold | — |
| JA1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @JaguarNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| JaguarGuardEligible | AND | 1 | Condition | JA1.C1 |
| JaguarGuardEligible | AND | 2 | Condition | JA1.C2 |
| JaguarGuardEligible | AND | 3 | Condition | JA1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Jaguar_Guard_Route | @JaguarGuardEligible | Guarding | Species 内行为份额 | @JaguarGuardingShare |
| Jaguar_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@JaguarGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@JaguarSpawnWindowStart, @JaguarSpawnWindowEnd]
    并且 连续均温 >= @JaguarGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @JaguarNestStructureSet

则：
    GuardingShare = @JaguarGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。浊水不进路由条件（Bake 语境因子，见 §2）；双亲护幼由份额整体表达。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化 + 浊度语境轴）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @JaguarLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest（巢型待正文 [需正文]） |
| GuardAnchorRelationProfile | @JaguarGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @JaguarNestSuitabilityProfile |
| LocalTemperatureProfile | @JaguarGuardLocalTemperatureProfile |
| TurbidityContextProfile | @JaguarTurbidityProfile（浊水语境 unary 轴实例；「浊水双亲」语境的落面，非路由条件 [需正文：浊度档位]） |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前目标与巢锚点的关系（距离 / 朝向）
读取 当前点局部温度
读取 当前点浊度事实

如果当前目标不满足 @JaguarLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与巢锚点的关系查询 @JaguarGuardRelationProfile
得到 RelationFit

用当前目标的底质结构查询 @JaguarNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @JaguarGuardLocalTemperatureProfile
得到 LocalTempFit

用当前点浊度查询 @JaguarTurbidityProfile
得到 TurbidityContextFit（浊水语境适配；unary，无第二轴）

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit / TurbidityContextFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @JaguarNormalLayerProfile |
| StructureProfile | @JaguarNormalStructureProfile |
| TemperatureProfile | @JaguarNormalTemperatureProfile |
| TimeProfile | @JaguarNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @JaguarNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @JaguarNormalLayerProfile 得到 LayerFit
用当前结构查询 @JaguarNormalStructureProfile 得到 StructureFit
用当前水温查询 @JaguarNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @JaguarNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @JaguarNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @JaguarGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @JaguarNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与巢 / 护幼对象锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @JaguarGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @JaguarNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @JaguarGuardingEligibilityByQuality | @NeutralAffinity | 成熟双亲护幼组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @JaguarGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 + 浊度 unary 语境轴（Knife §10 先例：轴实例非新结构）；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) 浊度作 Group 路由条件或 2D 交互（不立——unary 语境因子；若正文出现 §16.5 型不可分离样本再升级）；(2) Defense / Feeding arbitration（live V0）；(3) Guard 合并算子数学 OPERATOR UNDEFINED。
- [需正文] 巢型 / 产卵基质结构集合成员（「浊水双亲」未含巢型信息）；浊度档位取值域；窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
