# 蓝鳃太阳鱼（Bluegill Sunfish｜Lepomis macrochirus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | C06｜蓝鳃太阳鱼·护巢（15-Case 已审冻结故事，Evidence 页 3d6a4137d23681ff8ea6d954a69f7385） |
| 冻结 Pattern | P04 语义（C06 转述：护巢与摄食可在同一阶段出现；不能证明固定 Defense-first → DESIGN_POLICY）；Story DB 行级 Pattern 标签未在本地快照 [需核对] |
| 相邻故事 | B01-S39 小饵低阻呈现与吐饵（R01 CoverageDelta）＝摄食面故事，非护巢故事；其表达落点=Response 窄接受 Profile + Conversion owner（REP-COVERAGE-DELTA-001 #10 已判定），本文件不重复展开 |
| 物种属性锚 | fish-reference-20260908：水温 1–36℃、最适 18.5℃、benthopelagic、晨昏活跃（行级 AI 审核状态=待人工审核；本文件不引用其数值做阈值，仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，REP-CLARITY-FIX-001 后版本，2026-09-10） |
| 证据档 | Tier A（C06 冻结故事快照全文在 outputs/fcf_authoring_concrete_r2/baseline_mapping.md） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：殖民地巢群——部分雄鱼预先建立并持续照护巢区；入侵者与小拟饵可引发防御响应（C06 已审主张）。
- C06 未决维度 R01（多动机同时成立的输出/优先策略）：live V0 Working 已显式取舍为「Defense-only + Feeding evaluator 不进入该 Group Program」（例 1C + §8.8 结构性关闭，Program Binding 可验证，不写数值 Feeding=0）；这是主动复杂度取舍，不是已闭合裁决（见 §5）。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}（§13.1 先例）；蓝鳃护巢行＝PARENTAL_GUARD。本鱼仅一个 Special Group（Guarding），不触发跨 Special Group 的重叠约束。
- 「部分雄鱼」语义：只有部分成熟雄鱼进入护巢组成——由 GuardingShare 表达（供给份额），不需要逐个体属性事实（REP-COVERAGE-DELTA-001 §2.1 share-vector 先例；不触发 Sex/Maturity 个体属性 TODO）。
- 表达超集说明：无（本文件未超出 C06 冻结语义主张范围）。

Profile 引用清单：@BluegillSpawnWindowStart @BluegillSpawnWindowEnd @BluegillGuardWarmupDays @BluegillGuardTempThreshold @BluegillColonyNestStructureSet @BluegillGuardingShare @BluegillLocalGuardAnchorEligibility @BluegillColonyNestSuitabilityProfile @BluegillGuardRelationProfile @BluegillGuardLocalTemperatureProfile @BluegillGuardThreatProfile @BluegillNormalLayerProfile @BluegillNormalStructureProfile @BluegillNormalTemperatureProfile @BluegillNormalTimeProfile @BluegillNormalTempFloor @BluegillNormalFeedingProfile @BluegillGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| GB1 | C1 | 当前日期 | — | BETWEEN | @BluegillSpawnWindowStart | @BluegillSpawnWindowEnd |
| GB1 | C2 | 连续均温 | @BluegillGuardWarmupDays | >= | @BluegillGuardTempThreshold | — |
| GB1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @BluegillColonyNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| BluegillGuardEligible | AND | 1 | Condition | GB1.C1 |
| BluegillGuardEligible | AND | 2 | Condition | GB1.C2 |
| BluegillGuardEligible | AND | 3 | Condition | GB1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Bluegill_Guard_Route | @BluegillGuardEligible | Guarding | Species 内行为份额 | @BluegillGuardingShare |
| Bluegill_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@BluegillGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@BluegillSpawnWindowStart, @BluegillSpawnWindowEnd]
    并且 连续均温 >= @BluegillGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @BluegillColonyNestStructureSet

则：
    GuardingShare = @BluegillGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：Species 当前基础供给权重的无量纲分配比例（live §7 契约）；不是最终中鱼概率，不是 Response 质量，不是额外生成容量。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化「Parental Guard Anchor Template」，live §11.2 MERGE_SUPPORTED 版）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @BluegillLocalGuardAnchorEligibility |
| GuardAnchorRelationProfile | @BluegillGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @BluegillColonyNestSuitabilityProfile |
| LocalTemperatureProfile | @BluegillGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前目标与最近殖民地巢群锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @BluegillLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与巢群锚点的关系查询 @BluegillGuardRelationProfile
得到 RelationFit

用当前目标的巢床结构查询 @BluegillColonyNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @BluegillGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @BluegillNormalLayerProfile |
| StructureProfile | @BluegillNormalStructureProfile |
| TemperatureProfile | @BluegillNormalTemperatureProfile |
| TimeProfile | @BluegillNormalTimeProfile |
| ExtremeTemperatureGate | @BluegillNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段（蓝鳃晨昏活跃方向由 @BluegillNormalTimeProfile 值域承载）

用当前水层查询 @BluegillNormalLayerProfile 得到 LayerFit
用当前结构查询 @BluegillNormalStructureProfile 得到 StructureFit
用当前水温查询 @BluegillNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @BluegillNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @BluegillNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @BluegillGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；Reaction 槽 OFF） | @BluegillNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与巢区 / 护幼对象的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @BluegillGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @BluegillNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1 PARALLEL QUALITY WEIGHT MODIFIERS）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @BluegillGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼护巢组成（「部分雄鱼」）；资格与 Response 分开（§12.6：不写「大鱼 Bonus」，brood aggression 留在 Response） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier（LureSize / BaitSize / HookSize 等）属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @BluegillGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：条件原子 V1 三原子 + R1 规则集；BA-T2 泛化模板的 Profile 绑定；R-T1 单通道 Profile 重绑定；QT-1 Eligibility/Affinity 绑定；Share 契约语义（§7）。
- 放弃的自由度（显式记录）：(1) Defense / Feeding arbitration——live V0 取舍（例 1C），C06 未决维度 R01 的优先策略不在本表达内闭合；(2) Guard Bake 多 Factor 合并算子——OPERATOR UNDEFINED 待机制侧；(3) 巢群殖民地的巢间社会结构（巢群内个体互动）——无 Story 证据，不表达。
- 与 R0 四面补齐包的差异：four-surface-completion-r1 曾记 C06 Bake=明确不适用（当时 Story 为 Response 面故事）；本批按 live §15.3 M1（Bass BA-GUARD-NEST-GATE）生产先例给出 Guarding Group Bake。该差异已在 README 登记，不是机制裁决。
- [需核对] Story DB 行级 Pattern 标签；巢床结构集合成员与窗口数值由 Profile 层定值（本文件不冻结）。

BATCH_ID: REP-FULL-GUARD-001
