# 乌鳢（Northern Snakehead｜Channa argus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | R02-S15 乌鳢｜伏击捕食与护幼关系切换（R02 CoverageDelta，REP-COVERAGE-DELTA-001 #26 已判定） |
| 冻结 Pattern | P04 语义（K4 繁殖/育幼锚判定转述：伏击↔护幼切换=类型化状态互斥路由 + BA-T1/BA-T2 各绑 + R-T2 反应主导）；Story DB 行级 Pattern 标签未在本地快照 [需核对] |
| 物种属性锚 | fish-reference-20260908：水温 4–22℃、最适 13℃、benthopelagic、晨昏活跃、孤僻（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；coverage report 归档） |
| 证据档 | Tier A（coverage #26 四面判定在案；Story 正文细节 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding(BroodCare)=Defense-only（live V0）；NormalFeeding=R-T2 固定双通道（Feeding + Reaction，反应主导——coverage #26 判定） |

## 0. 上游语义与护巢形态

- 护幼形态：植被浮巢育幼——伏击捕食（常态）与护幼关系（PARENTAL_GUARD 态）随繁殖状态互斥切换（coverage #26：类型化状态互斥路由，§13.1 ReproductionState 先例）。
- 锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）；GuardAnchor Resolver 实例 = Fry / Brood Field（§11.2 泛化）。
- 常态面（NONE）：植被结构伏击（BA-T1 植被结构 Factor + 低光先例 K14 同构）；Response 反应主导（R-T2：Feeding + Reaction 双通道——伏击型对 deflection / 振动 / erratic 轨迹的反应通道主导）。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}（天然互斥——同一时刻的种群份额只进一个 Group；§13.1）。
- 表达超集说明：无（coverage #26 判定映射展开，未超出标题语义）。
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：BroodCare 面＝锚存在性判定 → 锚适配（植被掩体群栖境三档——浮巢稚鱼群所在植被栖境） → 关系评估（环护三档） → 局部温度 → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier A）：coverage #26 判定「植被浮巢育幼——伏击↔护幼类型化状态互斥」；稚鱼群存在已在路由面结算（C4），Bake 不重复结算。Normal 面＝水温极值硬门 → 植被结构定位（**伏击掩体先行**——coverage #26 常态面=植被伏击） → 低光（K14 低光槽三档） → 猎物 → 时段（晨昏） → 合并 [需正文 校准]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

Profile 引用清单：@SnakeheadSpawnWindowStart @SnakeheadSpawnWindowEnd @SnakeheadGuardWarmupDays @SnakeheadGuardTempThreshold @SnakeheadBroodStructureSet @SnakeheadGuardingShare @SnakeheadLocalGuardAnchorEligibility @SnakeheadBroodHabitatSuitabilityProfile @SnakeheadGuardRelationProfile @SnakeheadGuardLocalTemperatureProfile @SnakeheadGuardThreatProfile @SnakeheadVegetationStructureProfile @SnakeheadLowLightSpatialProfile @SnakeheadPreyResourceProfile @SnakeheadNormalTimeProfile @SnakeheadNormalTempFloor @SnakeheadNormalFeedingProfile @SnakeheadNormalReactionProfile @ReactionCap @SnakeheadGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| SN1 | C1 | 当前日期 | — | BETWEEN | @SnakeheadSpawnWindowStart | @SnakeheadSpawnWindowEnd |
| SN1 | C2 | 连续均温 | @SnakeheadGuardWarmupDays | >= | @SnakeheadGuardTempThreshold | — |
| SN1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @SnakeheadBroodStructureSet | — |
| SN1 | C4 | 稚鱼群存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| SnakeheadBroodCareEligible | AND | 1 | Condition | SN1.C1 |
| SnakeheadBroodCareEligible | AND | 2 | Condition | SN1.C2 |
| SnakeheadBroodCareEligible | AND | 3 | Condition | SN1.C3 |
| SnakeheadBroodCareEligible | AND | 4 | Condition | SN1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Snakehead_BroodCare_Route | @SnakeheadBroodCareEligible | BroodCare | Species 内行为份额 | @SnakeheadGuardingShare |
| Snakehead_Default | 默认 | NormalFeeding（植被伏击） | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@SnakeheadGuardWarmupDays 天）
读取 当前钓场结构集合
读取 稚鱼群存在事实（上游 GuardAnchor Resolver：Fry / Brood Field 实例）

如果：
    当前日期处于 [@SnakeheadSpawnWindowStart, @SnakeheadSpawnWindowEnd]
    并且 连续均温 >= @SnakeheadGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @SnakeheadBroodStructureSet
    并且 稚鱼群存在事实 == 存在

则：
    BroodCareShare = @SnakeheadGuardingShare

否则：
    BroodCareShare = 0

SpecialShareTotal = BroodCareShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 BroodCareShare / NormalFeedingShare
```

Share 语义：live §7 契约。「伏击↔护幼切换」＝份额级互斥路由（同一时刻份额只进一组），不建逐个体状态机。

## 2. Bake

### 2.1 BroodCare Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=fry school）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @SnakeheadLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | fry_school（浮巢稚鱼群；植被区移动锚） |
| GuardAnchorRelationProfile | @SnakeheadGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @SnakeheadBroodHabitatSuitabilityProfile |
| LocalTemperatureProfile | @SnakeheadGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 BroodCare Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配（植被掩体群栖境） → 关系评估（环护） → 局部温度 → 合并；出局即
EARLY_RETURN（返回 0，不进入后续评估），不做「先全算再减」。推导来源（Tier A）：coverage #26
判定「植被浮巢育幼」；稚鱼群存在已在路由面判定（C4），本程序不重复结算该 premise。
步序与档位成员的正文级校准 [需正文]。与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的植被结构 / 水深
读取 当前稚鱼群锚点位置（上游 Fry / Brood Field Resolver 产出）
读取 当前目标与稚鱼群锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @SnakeheadLocalGuardAnchorEligibility
    （锚=浮巢稚鱼群移动锚（植被区）；稚鱼群存在已在路由面判定（C4），本步不重复结算 premise，
      只判「当前目标是否处于稚鱼群的合法护卫锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与育幼分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中——植被掩体群栖境语义）：
    用当前目标的植被掩体查询 @SnakeheadBroodHabitatSuitabilityProfile
    （稚鱼群所在植被栖境的适配三档分档槽=Profile 值域——档位成员与阈值不冻结）
    如果 群栖境 ∈ 最适应档（preferred 植被掩体栖境）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 栖境）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除栖境档）：
        返回 0（EARLY_RETURN：排除栖境出局——稚鱼群不驻留的栖境无育幼分布）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中——环护语义）：
    用当前目标与稚鱼群的关系（距离 / 朝向）查询 @SnakeheadGuardRelationProfile
    （环护位三档=Profile 值域不冻结）
    如果 关系 ∈ 环护核档：
        RelationFit = 全额（环护占位）
    否则如果 ∈ 环护缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：环护圈外无育幼占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @SnakeheadGuardLocalTemperatureProfile
    （育幼期局部温度三档=Profile 值域不冻结）
    如果 局部温度 ∈ 适温档：
        LocalTempFit = 全额
    否则如果 ∈ 边际档：
        LocalTempFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        返回 0（EARLY_RETURN：育幼期排除温度带出局）

第 5 步 合并：
    合并 AnchorSuitabilityFit / RelationFit / LocalTempFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 BroodCare SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 + 低光 / 植被伏击 DynamicSpatialSlot，K14 先例）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot（**§2.4 已顺序还原（REP-ORDER-FIX-002）：early return 链＋分级命中；与 live BA-T1 Independent Factor Set 无序语义的分歧登记 README §7**） |
| VegetationStructureProfile | @SnakeheadVegetationStructureProfile（植被结构 Factor） |
| LowLightSpatialProfile | @SnakeheadLowLightSpatialProfile（低光槽位；§11.5 先例） |
| PreyResourceProfile | @SnakeheadPreyResourceProfile（猎物资源因子） |
| TimeProfile | @SnakeheadNormalTimeProfile（晨昏活跃方向） |
| ExtremeTemperatureGate | @SnakeheadNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水温极值硬门 → 植被结构定位 → 低光 → 猎物 →
时段 → 合并。推导来源（Tier A 方向）：coverage #26 常态面=植被结构伏击（BA-T1 植被结构 Factor
＋低光先例 K14）——伏击型定位=掩体先行，低光为第二定位修饰；[需正文] 校准（Story 正文细节
[需正文]）。水温门从「末位算术门」还原为前置出局判定（@SnakeheadNormalTempFloor 为排除档边界
参考）。与 live BA-T1 Independent Factor Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前植被结构
读取 当前光照事实
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

第 1 步 水温极值硬门（GATE_EXTREME_TEMP）：
    用当前点水温对照排除档边界（@SnakeheadNormalTempFloor 为边界参考）
    如果 当前点水温 ∈ 排除档（极值带）：
        返回 0（EARLY_RETURN：极值温度带出局）

第 2 步 植被结构定位（分级命中——伏击掩体先行）：
    用植被结构查询 @SnakeheadVegetationStructureProfile（三档=Profile 值域不冻结）
    如果 植被结构 ∈ 最适应档（伏击掩体）：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（× Profile 衰减参数——不清零）
    否则：
        返回 0（EARLY_RETURN：无伏击掩体档出局——伏击型定位先行）

第 3 步 低光（分级命中——K14 低光槽）：
    用光照事实查询 @SnakeheadLowLightSpatialProfile（低光三档=Profile 值域不冻结）
    如果 光照 ∈ 低光档：
        LowLightFit = 全额（伏击低光偏好）
    否则如果 ∈ 中光档：
        LowLightFit = 削减（不清零）
    否则（强光档）：
        返回 0（EARLY_RETURN：排除光照档出局 [需正文：强光是否出局归 Profile 值域]）

第 4 步 猎物（分级命中）：
    用猎物资源查询 @SnakeheadPreyResourceProfile（三档=Profile 值域不冻结）
    如果 猎物资源 ∈ 最适应档：
        PreyFit = 全额
    否则如果 ∈ 可接受档：
        PreyFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：无猎物资源档出局）

第 5 步 时段（分级命中）：
    用当前时段查询 @SnakeheadNormalTimeProfile（晨昏三档=Profile 值域不冻结）
    如果 时段 ∈ 活跃档：
        TimeFit = 全额
    否则如果 ∈ 一般档：
        TimeFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除时段档出局 [需正文：非活跃时段是否出局归 Profile 值域]）

第 6 步 合并：
    合并 StructureFit / LowLightFit / PreyFit / TimeFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明——合并数学待机制侧，不因链序还原而隐式定义）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 3. Response

### 3.1 配置表（例 1C 形态 + live §17.2 RR-T1 双通道形态）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| BroodCare | 顺序响应规则（Defense-only） | @SnakeheadGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T2 固定双通道（Feeding + Reaction，反应主导） | @SnakeheadNormalFeedingProfile + @SnakeheadNormalReactionProfile + @ReactionCap | 返回 FinalResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

BroodCare Group：

```plain text
读取 当前 Presentation 与浮巢 / 稚鱼群锚点的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @SnakeheadGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@SnakeheadGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group（R-T2，反应主导）：

```plain text
评价 Feeding Channel：
    读取当前饵 / 姿态 / 手法
    使用 @SnakeheadNormalFeedingProfile
    分级命中（REP-ORDER-FIX-002 展开；档位成员=@SnakeheadNormalFeedingProfile 值域不冻结）：
        接受档=全额 FeedingResponse / 边际档=低响应（削减不清零）/ 排除档=本通道 0
    得到 FeedingResponse

评价 Reaction Channel：
    读取突然加速 / 变向 / 下落（abruptness）
    读取 deflection（撞植被后偏转）
    读取振动 / 闪光
    读取 PresentationProximity
    读取持续追逐要求
    读取 CueFamiliarity
    使用 @SnakeheadNormalReactionProfile
    得到 ReactionResponse
    （本通道不展开档位控制流——「反应主导语义=Reaction Profile 值域承载，不是控制流差异」
      声明维持：反应权重在 Profile 值域内承载，不建通道内分支）

FinalResponse = MAX(FeedingResponse, ReactionResponse)
如启用 @ReactionCap：FinalResponse = MIN(FinalResponse, @ReactionCap)

算子标注：MAX 为 live §17.3 Bass Reaction Working Algorithm Candidate（§13.3 注记：Multi-channel Aggregate Semantics 是 Signature 字段，未冻结）；@ReactionCap 为可选固定 Cap 槽（R-T1 结构），不是任意后处理脚本

返回 FinalResponse
```

反应主导语义：Reaction Profile 值域承载（伏击型对 deflection / erratic 的反应权重高），不是控制流差异。

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| BroodCare | QT-1 | @SnakeheadGuardingEligibilityByQuality | @NeutralAffinity | 成熟亲鱼育幼组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（BroodCare 行查 @SnakeheadGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子 + R1；BA-T1+LowLightSlot / BA-T2 锚实例双模板各绑一组；R-T2 固定双通道（coverage #26 反应主导判定）；QT-1；**顺序还原链序与档位结构（REP-ORDER-FIX-002：BroodCare 面锚存在性→植被群栖境适配→环护关系→温度 early return 链、三档分级命中；Normal 面极值门→植被伏击定位先行→低光链；Feeding 通道 DECIDE 三档——Reaction 通道值域承载声明维持；推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) 逐个体「伏击↔护幼」状态机（份额级互斥路由替代）；(2) Guard 合并算子 / R-T2 Aggregate 数学（MAX 为 Working Candidate、Cap 数学 OPERATOR UNDEFINED）；(3) 双亲分工（份额粒度）；(4) Reaction Channel 的档位控制流展开（「值域承载非控制流」声明维持——展开=走私控制流，与本文件 §3.2 语义声明冲突）；(5) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(6) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需正文] 浮巢结构集合成员（植被浮巢区方向来自判定句，具体成员待 Story 正文）；R-T2 Reaction Profile 的主导强度值域。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；BroodCare Bake 锚存在性 early return 链＋分级命中，Normal Bake 伏击定位链还原，Feeding 通道 DECIDE 档位展开——Reaction 通道值域承载维持）
