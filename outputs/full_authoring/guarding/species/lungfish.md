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
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：Guard 面＝锚存在性判定 → 锚适配（巢穴锚面三档） → 关系评估（三档） → 局部温度 → 合成；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier A）：census premise「湿季筑巢、护卵并以血管化腹鳍供氧」——筑巢=构建选址（锚适配先行）→ 护卵=巢穴占位（关系在后）；WET 季节资格已在路由面结算（C1），Bake 不重复结算。Normal 面＝水面可达硬门（OBLIGATE 气呼吸——第一出局条件） → 水温极值硬门 → 静水/结构/猎物/时段各三档——**因子间顺序不排序**（census open_semantics「未裁决 unordered」原样保留）。分级命中：三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2 模板平铺读法的分歧登记 README §7。

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
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @LungfishLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest（雄鱼巢穴，单一实例） |
| GuardAnchorRelationProfile | @LungfishGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @LungfishNestSuitabilityProfile |
| LocalTemperatureProfile | @LungfishGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配 → 关系评估 → 局部温度 → 合并；出局即 EARLY_RETURN（返回 0，
不进入后续评估），不做「先全算再减」。推导来源（Tier A）：census premise「湿季筑巢、护卵」——
筑巢=构建选址（锚适配先行）→ 护卵=巢穴占位（关系评估在后）；WET 季节资格已在路由面结算（C1），
本程序不重复结算季节 premise。步序与档位成员的正文级校准 [需正文]。与 live BA-T2 模板平铺读法的
分歧登记 README §7。

读取 当前目标的结构 / 底质 / 深度
读取 当前目标与巢穴锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @LungfishLocalGuardAnchorEligibility
    （锚=雄鱼巢穴；WET 与繁殖资格已在路由面判定，本步不重复结算 premise，
      只判「当前目标是否处于该巢穴的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的底质 / 巢穴结构查询 @LungfishNestSuitabilityProfile
    （巢穴锚面三档分档槽=Profile 值域——档位成员与阈值不冻结）
    如果 锚面 ∈ 最适应档（preferred 锚面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 锚面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0（EARLY_RETURN：排除锚面出局——湿季筑巢的选址适配先行）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与巢穴锚点的关系（距离 / 朝向）查询 @LungfishGuardRelationProfile
    （守卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @LungfishGuardLocalTemperatureProfile
    （护巢期局部温度三档=Profile 值域不冻结）
    如果 局部温度 ∈ 适温档：
        LocalTempFit = 全额
    否则如果 ∈ 边际档：
        LocalTempFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        返回 0（EARLY_RETURN：护巢期排除温度带出局）

第 5 步 合并：
    合并 AnchorSuitabilityFit / RelationFit / LocalTempFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

### 2.3 NormalFeeding Group｜配置表（HARD_GATED_FACTOR_COMBINE 族成员——水面可达硬门 + 因子组合；census P-LUN-BAKE-WET 判例）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-LUN-WET-GATED-FACTORS（census 族成员：硬门前置 + 因子组合；非相对寻优）（**§2.4 已顺序还原（REP-ORDER-FIX-002）：双硬门先行＋分级命中；因子间顺序按 census open_semantics unordered 原样保留——分歧登记 README §7**） |
| SurfaceAccessGate | @LungfishSurfaceAccessGate（专性气呼吸：水面不可达即剔除，HARD GATE 而非排序） |
| StillwaterProfile | @LungfishStillwaterProfile（静水偏好因子） |
| PondStructureProfile | @LungfishPondStructureProfile（塘体结构因子） |
| PreyResourceProfile | @LungfishPreyResourceProfile（猎物资源因子：鱼虾螺蚌藻） |
| TimeProfile | @LungfishNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @LungfishNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧；census open_semantics：因子间顺序未裁决，unordered 处理） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水面可达硬门（第一出局条件——OBLIGATE
气呼吸：无水面通道即剔除，census HARD GATE 判例「硬门前置」的判断序形态） → 水温极值硬门 →
因子评价（各三档分级命中）。**因子间顺序不排序**：census open_semantics「因子间顺序未裁决，
unordered 处理」原样保留——强行排序=冒充证据（§5 放弃项 (5)，分歧登记 README §7）。
末位算术门（水温<floor 返回极低）还原为前置出局判定。

读取 水文季节事实（本 Bake 仅 WET 态激活）
构建 当前水域可访问集
读取 当前点水面可达事实
读取 当前点静水 / 流速事实
读取 当前结构
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

第 1 步 水面可达硬门（GATE_SURFACE_ACCESS——第一出局条件）：
    用当前点水面可达事实查询 @LungfishSurfaceAccessGate
    （专性气呼吸：水面不可达即剔除——硬门，非相对排序）
    如果 水面不可达：
        从可访问集中剔除该目标，返回 0（EARLY_RETURN：OBLIGATE 气呼吸出局——
        生存硬门先于一切因子评价）
    否则：
        进入第 2 步

第 2 步 水温极值硬门（GATE_EXTREME_TEMP）：
    用当前点水温对照排除档边界（@LungfishNormalTempFloor 为边界参考）
    如果 当前点水温 ∈ 排除档（极值带）：
        返回 0（EARLY_RETURN：极值温度带出局）

因子评价（因子间顺序=census unordered 原样，不排序；各因子分级命中，三档=Profile 值域不冻结）：
    用静水事实查询 @LungfishStillwaterProfile：
        最适应档=StillwaterFit 全额 / 可接受档=削减（× Profile 衰减参数，不清零）/ 排除档=返回 0（EARLY_RETURN）
    用结构查询 @LungfishPondStructureProfile：
        最适应档=StructureFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0（EARLY_RETURN）
    用猎物资源查询 @LungfishPreyResourceProfile：
        最适应档=PreyFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0（EARLY_RETURN）
    用时段查询 @LungfishNormalTimeProfile（夜间活跃方向）：
        活跃档=TimeFit 全额 / 一般档=削减（不清零）/ 排除档=返回 0（EARLY_RETURN）

合并步：
    合并 StillwaterFit / StructureFit / PreyFit / TimeFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（census WEIGHTED_FACTORS 的权重数学未冻结——因子顺序与合并数学均待机制侧，不因分级命中展开而隐式定义）

返回 SpatialDistributionWeight（顺序还原链结束：双硬门 early return、因子分级命中；因子间顺序=证据未裁决，不冒充）
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

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @LungfishGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@LungfishGuardThreatProfile 值域不冻结——
    强度上限待证：census caveat「攻击性直接证据开放」原样携带，值域方向与上限由 Profile 层
    在证据闭合后定值，本文件不预设强度）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

注意：conflict 响应**强度**为 P04 语义映射，攻击性直接证据开放（census caveat 原样保留）——@LungfishGuardThreatProfile 值域方向与上限由 Profile 层在证据闭合后定值，本文件不预设强度。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

EVAL_TARGET_AS_FOOD（吸吮式 typed food evaluator）：
    用这些输入评价 @LungfishNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@LungfishNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 ∈ 边际档：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

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

- 使用的自由度：V1 四原子（水文季节 typed 字面量 WET）+ R1；HARD_GATED Bake 族绑定（census 判例）；R-T1 Profile 重绑定；QT-1；**顺序还原链序与档位结构（REP-ORDER-FIX-002：Guard 面锚存在性→锚适配→关系→温度 early return 链、三档分级命中；Normal 面水面可达硬门第一→水温极值门；Response DECIDE 三档——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census 双路径 body（DUAL_PATH，MEDIUM）→ live V0 Defense-only，分歧待机制侧；(2) DRY 蛰伏态 Bake（P05 故事 + S10=EO playable 存疑，本批不表达）；(3) 腹鳍供氧行为本身（照护行为事实，属 premise 证据，不进 Response 面）；(4) 合并算子数学 OPERATOR UNDEFINED ×2；(5) Normal 面因子间顺序的强行排序（census open_semantics「unordered 未裁决」原样保留——顺序还原只到双硬门先行+分级命中，不冒充因子顺序证据；登记 README §7）；(6) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- P04 映射 caveat（F-9）原样携带：LUN→P04 为 census 新增跨层映射，FR 冻结侧仅 P05，未经 FR3 语义侧确认；若 FR3 侧改判，本文件 Group/Response 表达需复核。
- [需核对] 巢穴结构集合成员、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；Guard Bake 锚存在性 early return 链＋分级命中，Normal Bake 双硬门先行＋因子 unordered 原样，Response DECIDE 档位展开）
