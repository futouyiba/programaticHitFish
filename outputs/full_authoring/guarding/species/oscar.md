# 地图鱼（Oscar｜Astronotus ocellatus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R05-地图鱼-Biparental-Guard-Quiet-Water-Ambush（Story 页 3d7a4137d2368196abfff3130d97773c；CENSUS-B0 全四面判定快照在案） |
| 冻结 Pattern | P01 + P04（r05-input-summary 表：Existing / Default / None） |
| census 程序 | P-OSC-RESP-GUARD（Response，GUARD_CONFLICT_DUAL_PATH_RESPONSE 族 canonical_source，HIGH）+ P-OSC-BAKE / P-OSC-RESP-FEEDING |
| 物种属性锚 | fish-reference-20260908：水温 22–25℃、最适 23.5℃、benthopelagic、全天活跃、躲藏（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；census CENSUS-B0 归档） |
| 证据档 | Tier A（census 快照含 premise 常量：清巢产卵→护卵 3–4 天→迁仔 6–7 天） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding，掩体伏击 context） |

## 0. 上游语义与护巢形态

- 护巢形态：双亲护巢（BIPARENTAL_GUARD，persistent condition）——清巢产卵 → 护卵（nest，约 3–4 天）→ 迁仔（fry，约 6–7 天）（census premise 常量，照录；天数为 Story 证据常量，不是本文件配置数值）。双亲可同时执行（两个体同 body，不影响 body 结构）。
- 锚点：nest_anchor（平坦石面 / 浅坑）｜fry_anchor（迁仔期稚鱼群）——guard 期 relation object（census）；GuardAnchor Resolver 实例切换（§11.2 泛化）。
- P04 消费方式：guard_state 是 persistent condition premise（presentation 前已存在且持续）；census Bake 判例：护巢期 anchor 邻近因子激活且权重主导，按 condition 配置级因子切换处理，body 不设分支（CENSUS-B0 open_semantics 原样保留：若 review 判需 body 内 IF，本面结构结论需复核）。
- census ↔ live 表达分歧（显式登记，本文件表达 live Working V0）：census Response canonical body 为双路径（EVAL_TARGET_AS_FOOD_TYPED ∥ EVAL_TARGET_AS_INTRUDER_TYPED → COMBINE_DUAL_PATH → DECIDE，可出 TargetFeeding 或 RelationalConflict）；live V0 取舍为 Guarding Group 只评 Defense（例 1C）。本文件按 live V0 表达；双路径族真值登记在 census registry（GUARD_CONFLICT_DUAL_PATH_RESPONSE，本鱼为 canonical_source），其 COMBINE_DUAL_PATH 合并算子数学 OPERATOR UNDEFINED——待机制侧裁决两线 reconciliation。见 §5 放弃自由度 (1)。
- 互斥状态：guard_state ∈ {NONE, BIPARENTAL_GUARD}（census premise 枚举）。

Profile 引用清单：@OscarSpawnWindowStart @OscarSpawnWindowEnd @OscarGuardWarmupDays @OscarGuardTempThreshold @OscarNestStructureSet @OscarGuardingShare @OscarLocalGuardAnchorEligibility @OscarNestSuitabilityProfile @OscarGuardRelationProfile @OscarGuardAnchorDominanceProfile @OscarGuardLocalTemperatureProfile @OscarGuardThreatProfile @OscarStillwaterProfile @OscarSubstrateStructureProfile @OscarPreyResourceProfile @OscarNormalTimeProfile @OscarNormalTempFloor @OscarNormalFeedingProfile @OscarGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| OS1 | C1 | 当前日期 | — | BETWEEN | @OscarSpawnWindowStart | @OscarSpawnWindowEnd |
| OS1 | C2 | 连续均温 | @OscarGuardWarmupDays | >= | @OscarGuardTempThreshold | — |
| OS1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @OscarNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| OscarGuardEligible | AND | 1 | Condition | OS1.C1 |
| OscarGuardEligible | AND | 2 | Condition | OS1.C2 |
| OscarGuardEligible | AND | 3 | Condition | OS1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Oscar_Guard_Route | @OscarGuardEligible | Guarding | Species 内行为份额 | @OscarGuardingShare |
| Oscar_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@OscarGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@OscarSpawnWindowStart, @OscarSpawnWindowEnd]
    并且 连续均温 >= @OscarGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @OscarNestStructureSet

则：
    GuardingShare = @OscarGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：Species 当前基础供给权重的无量纲分配比例（live §7 契约）。双亲组成不逐个体表达：护巢份额覆盖双亲整体（份额粒度，非个体分类）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化 + Anchor 主导权重槽）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @OscarLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest_anchor（护卵段）｜fry_anchor（迁仔段；随 guard 阶段事实配置级切换，body 不设分支） |
| GuardAnchorRelationProfile | @OscarGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @OscarNestSuitabilityProfile |
| AnchorDominanceProfile | @OscarGuardAnchorDominanceProfile（护巢期 anchor 邻近因子权重主导——census 判例的 Profile 化） |
| LocalTemperatureProfile | @OscarGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前 guard 阶段事实，选择 GuardAnchorResolver 实例：
    护卵段 → 锚=nest_anchor（当前场内清巢石面 / 浅坑位置）
    迁仔段 → 锚=fry_anchor（当前稚鱼群位置）
读取 当前目标与锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @OscarLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与锚点的关系查询 @OscarGuardRelationProfile
得到 RelationFit

用当前目标的底质查询 @OscarNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @OscarGuardLocalTemperatureProfile
得到 LocalTempFit

用当前 guard 阶段事实查询 @OscarGuardAnchorDominanceProfile
得到各因子权重（护巢期 anchor 因子主导）

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit（按 @OscarGuardAnchorDominanceProfile 权重）
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 加权合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set；因子集=census P-OSC-BAKE 常态因子）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| StillwaterProfile | @OscarStillwaterProfile（静水偏好因子） |
| SubstrateStructureProfile | @OscarSubstrateStructureProfile（泥沙底浅沟塘结构掩体因子） |
| PreyResourceProfile | @OscarPreyResourceProfile（小鱼 / 螯虾 / 虫 / 幼虫资源因子） |
| TimeProfile | @OscarNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @OscarNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧；census open_semantics：因子间业务顺序未由冻结证据裁决，按 unordered typed factor set 处理） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前点静水 / 流速事实
读取 当前结构（泥沙底浅沟塘 / 掩体）
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

用静水事实查询 @OscarStillwaterProfile 得到 StillwaterFit
用结构查询 @OscarSubstrateStructureProfile 得到 StructureFit
用猎物资源查询 @OscarPreyResourceProfile 得到 PreyFit
用时段查询 @OscarNormalTimeProfile 得到 TimeFit

如果 当前点水温 < @OscarNormalTempFloor：
    返回 极低空间权重（early return）

合并 StillwaterFit / StructureFit / PreyFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @OscarGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；伏击 context） | @OscarNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与卵床 / 稚鱼群锚点的关系（按当前锚实例）
读取 侵入距离、持续时间、威胁 Cue

评价 @OscarGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前掩体 / 静水 context（伏击 typed context）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @OscarNormalFeedingProfile
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @OscarGuardingEligibilityByQuality | @NeutralAffinity | 成熟双亲护巢组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @OscarGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 泛化 + AnchorDominanceProfile（census「anchor 权重主导」判例的 Profile 化，body 不设分支）；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) **census 双路径（TargetFeeding ∥ RelationalConflict 并行评估 + COMBINE_DUAL_PATH）**——live V0 只表达 Defense-only；双路径真值在 census registry（本鱼为 canonical_source，HIGH）；两线 reconciliation 待机制侧，本文件不冒充已闭合；(2) BA-T1 / Guard 合并算子 OPERATOR UNDEFINED；(3) 双亲个体角色分工（雌雄谁迁仔）——份额粒度不表达；(4) guard 阶段天数值（3–4 天 / 6–7 天）为 Story 证据常量照录于 §0，不进配置。
- census open_semantics 原样保留：因子间顺序未由证据裁决（unordered 处理）；「若 review 判需 body 内 IF，本面结构结论需复核」。
- [需核对] 无（Tier A）；窗口 / 阈值数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
