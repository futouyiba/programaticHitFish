# 南美肺鱼（South American Lungfish｜Lepidosiren paradoxa）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R05-南美肺鱼-Aestivation-State-Switch（Story 页 3d7a4137d23681f9b62bdd65f610ffb4；CENSUS-B0 全四面判定快照在案） |
| 冻结 Pattern | P05（主）；护巢段＝**P04 语义映射（census 显式 caveat：跨层映射，FR 冻结 patterns 仅 P05，未经 FR3 语义侧确认——F-9 登记）**，confidence MEDIUM |
| census 程序 | P-LUN-RESP-GUARD（Response，GUARD_CONFLICT_DUAL_PATH_RESPONSE 族成员，MEDIUM）+ P-LUN-BAKE-WET / P-LUN-RESP-FEEDING |
| census 开放语义 | 「护巢行为实证；conflict 响应强度为 P04 语义映射（Bluegill/Smallmouth 先例），攻击性直接证据开放」（原样保留） |
| 物种属性锚 | fish-reference-20260908：水温 24–28℃、最适 26℃、demersal、夜间活跃、孤僻（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；census CENSUS-B0 归档） |
| 证据档 | Tier A（census 快照）；护巢强度证据=开放（MEDIUM） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0；强度上限待证——攻击性直接证据开放）；NormalFeeding=R-T1 单通道（Feeding，吸吮 typed） |

## 0. 上游语义与护巢形态

- 生命周期 premise（census）：season_regime = WET｜DRY（干湿由 world 水文状态上游决定，个体不同时双态）；air_breathing = OBLIGATE（物种常量：无水面通道不可存活）。
- 护巢形态：雄鱼巢穴守护（MALE_NEST_GUARD，persistent condition）——湿季筑巢、护卵并以血管化腹鳍供氧（census premise 常量：oxygenation_organ=vascularized_pelvic_fins）。
- 非护巢期 Response：单路径 P01 吸吮 typed food evaluator（P-LUN-RESP-FEEDING）；护巢期 guard body 激活（census：「非护巢期该 body 不激活」）。
- 干季（DRY）：蛰伏态＝独立 P05 故事（burrow anchor 退化体，playable 存疑 S10=EO，census AMBIGUOUS / TAR-01）——**不属于本批 Guarding 表达范围**，本文件只在 WET premise 下表达 Guarding。
- census ↔ live 表达分歧（同 oscar.md §0 条目，显式登记）：census 护巢期 body 为双路径（DUAL_PATH，MEDIUM）；live V0 为 Defense-only。本文件表达 live V0；分歧与 COMBINE_DUAL_PATH 数学（OPERATOR UNDEFINED）待机制侧。
- 互斥状态：season_regime ∈ {WET, DRY}（上游 world 水文）× guard_state ∈ {NONE, MALE_NEST_GUARD}。

Profile 引用清单：@LungfishSpawnWindowStart @LungfishSpawnWindowEnd @LungfishGuardWarmupDays @LungfishGuardTempThreshold @LungfishNestStructureSet @LungfishGuardingShare @LungfishLocalGuardAnchorEligibility @LungfishNestSuitabilityProfile @LungfishGuardRelationProfile @LungfishGuardLocalTemperatureProfile @LungfishGuardThreatProfile @LungfishStillwaterProfile @LungfishPondStructureProfile @LungfishPreyResourceProfile @LungfishSurfaceAccessGate @LungfishNormalTimeProfile @LungfishNormalTempFloor @LungfishNormalFeedingProfile @LungfishGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：WET

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| LU1 | C1 | 水文季节事实 | — | == | WET | — |
| LU1 | C2 | 当前日期 | — | BETWEEN | @LungfishSpawnWindowStart | @LungfishSpawnWindowEnd |
| LU1 | C3 | 连续均温 | @LungfishGuardWarmupDays | >= | @LungfishGuardTempThreshold | — |
| LU1 | C4 | 场内结构集合 | — | CONTAINS_ANY | @LungfishNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| LungfishGuardEligible | AND | 1 | Condition | LU1.C1 |
| LungfishGuardEligible | AND | 2 | Condition | LU1.C2 |
| LungfishGuardEligible | AND | 3 | Condition | LU1.C3 |
| LungfishGuardEligible | AND | 4 | Condition | LU1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Lungfish_Guard_Route | @LungfishGuardEligible | Guarding | Species 内行为份额 | @LungfishGuardingShare |
| Lungfish_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 水文季节事实
读取 当前日期
读取 连续均温（窗口=@LungfishGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    水文季节事实 == WET
    并且 当前日期处于 [@LungfishSpawnWindowStart, @LungfishSpawnWindowEnd]
    并且 连续均温 >= @LungfishGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @LungfishNestStructureSet

则：
    GuardingShare = @LungfishGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。DRY 蛰伏态不在本批表达（P05 独立故事；GuardingShare 路由只在 WET 下评价）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @LungfishLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest（雄鱼巢穴，单一实例） |
| GuardAnchorRelationProfile | @LungfishGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @LungfishNestSuitabilityProfile |
| LocalTemperatureProfile | @LungfishGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 底质 / 深度
读取 当前目标与巢穴锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @LungfishLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与巢穴锚点的关系查询 @LungfishGuardRelationProfile
得到 RelationFit

用当前目标的底质 / 巢穴结构查询 @LungfishNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @LungfishGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（HARD_GATED_FACTOR_COMBINE 族成员——水面可达硬门 + 因子组合；census P-LUN-BAKE-WET 判例）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-LUN-WET-GATED-FACTORS（census 族成员：硬门前置 + 因子组合；非相对寻优） |
| SurfaceAccessGate | @LungfishSurfaceAccessGate（专性气呼吸：水面不可达即剔除，HARD GATE 而非排序） |
| StillwaterProfile | @LungfishStillwaterProfile（静水偏好因子） |
| PondStructureProfile | @LungfishPondStructureProfile（塘体结构因子） |
| PreyResourceProfile | @LungfishPreyResourceProfile（猎物资源因子：鱼虾螺蚌藻） |
| TimeProfile | @LungfishNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @LungfishNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧；census open_semantics：因子间顺序未裁决，unordered 处理） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 水文季节事实（本 Bake 仅 WET 态激活）
构建 当前水域可访问集
读取 当前点水面可达事实
读取 当前点静水 / 流速事实
读取 当前结构
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

如果 当前点水面不可达（@LungfishSurfaceAccessGate 不成立）：
    从可访问集中剔除该目标（硬门，非相对排序；early return 极低 / 0）

用静水事实查询 @LungfishStillwaterProfile 得到 StillwaterFit
用结构查询 @LungfishPondStructureProfile 得到 StructureFit
用猎物资源查询 @LungfishPreyResourceProfile 得到 PreyFit
用时段查询 @LungfishNormalTimeProfile 得到 TimeFit

如果 当前点水温 < @LungfishNormalTempFloor：
    返回 极低空间权重（early return）

合并 StillwaterFit / StructureFit / PreyFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（census WEIGHTED_FACTORS 的权重数学未冻结）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @LungfishGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；吸吮 typed evaluator） | @LungfishNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与巢穴锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @LungfishGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

注意：conflict 响应**强度**为 P04 语义映射，攻击性直接证据开放（census caveat 原样保留）——@LungfishGuardThreatProfile 值域方向与上限由 Profile 层在证据闭合后定值，本文件不预设强度。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @LungfishNormalFeedingProfile（吸吮式 typed food evaluator）
返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @LungfishGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼护巢组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @LungfishGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（水文季节 typed 字面量 WET）+ R1；HARD_GATED Bake 族绑定（census 判例）；R-T1 Profile 重绑定；QT-1。
- 放弃的自由度：(1) census 双路径 body（DUAL_PATH，MEDIUM）→ live V0 Defense-only，分歧待机制侧；(2) DRY 蛰伏态 Bake（P05 故事 + S10=EO playable 存疑，本批不表达）；(3) 腹鳍供氧行为本身（照护行为事实，属 premise 证据，不进 Response 面）；(4) 合并算子数学 OPERATOR UNDEFINED ×2。
- P04 映射 caveat（F-9）原样携带：LUN→P04 为 census 新增跨层映射，FR 冻结侧仅 P05，未经 FR3 语义侧确认；若 FR3 侧改判，本文件 Group/Response 表达需复核。
- [需核对] 巢穴结构集合成员、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
