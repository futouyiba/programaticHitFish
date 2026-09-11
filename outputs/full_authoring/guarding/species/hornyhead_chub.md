# 双点美鱥（Hornyhead Chub｜Nocomis biguttatus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R07 双点美鱥（R07 P04：「石巢共生 guard target specificity=Open Question 不立 Candidate」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（石巢守护——筑石巢并守护的关系语义） |
| Registry Open Question | guard target specificity（对共生对象的特异性分辨）＝Open，不立 Candidate——本文件按「无特异性分辨」表达，特异性槽位留白（见 §3 注记） |
| 物种属性锚 | fish-reference-20260908：水温 11–19℃、最适 15℃、demersal、早晨活跃、撕鳍（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R07 FR3 归档摘要在 tmp/triage_r07.md） |
| 证据档 | Tier B（triage 批注一行 + Open Question 判定；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0；目标特异性分辨不表达）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：石巢守护——雄鱼筑砾石巢（石巢）并守护；石巢共生（其它鱼种在石巢上产卵的共生现象）构成 target specificity Open Question（R07 FR3：不立 Candidate，记 Open）。
- 筑巢者语义：巢体由本鱼建造——巢体存在事实是 guard premise（上游 GuardAnchor Resolver 产出），与「场内有合法筑巢基质」（资格原子）分开判（防双重结算）。
- 特异性边界：R07 判定「guard target specificity=Open Question 不立 Candidate」——本表达**不含**「对共生产卵者 / 对入侵者」的分辨逻辑；@HornyheadGuardThreatProfile 对一切逼近锚点的呈现统一评价。若未来特异性立项，走 Response Profile 重绑定（REP-COVERAGE-DELTA-001 K13 先例），不是新结构。
- 互斥状态：ReproductionState ∈ {NONE, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；石巢基质集合成员、窗口数值全部 @ 化或标注 [需正文]。
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：Guard 面＝锚存在性判定 → 锚适配（砾石基质三档——**构建型**：雄鱼筑巢=选址适配先行） → 关系评估（三档） → 局部温度 → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier B）：R07 FR3 抽验名单「石巢筑造+守护」（构筑型锚——方向级）；巢体存在事实已在路由面结算（C4），Bake 不重复结算；步序与档位成员 [需正文] 校准。Normal 面＝水层硬定位（demersal——非底层出局） → 结构 → 水温（排除档=极值出局） → 时段（早晨） → 合并——物种属性锚方向级 [需正文]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

Profile 引用清单：@HornyheadSpawnWindowStart @HornyheadSpawnWindowEnd @HornyheadGuardWarmupDays @HornyheadGuardTempThreshold @HornyheadNestSiteStructureSet @HornyheadGuardingShare @HornyheadLocalGuardAnchorEligibility @HornyheadStoneNestSuitabilityProfile @HornyheadGuardRelationProfile @HornyheadGuardLocalTemperatureProfile @HornyheadGuardThreatProfile @HornyheadNormalLayerProfile @HornyheadNormalStructureProfile @HornyheadNormalTemperatureProfile @HornyheadNormalTimeProfile @HornyheadNormalTempFloor @HornyheadNormalFeedingProfile @HornyheadGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| HC1 | C1 | 当前日期 | — | BETWEEN | @HornyheadSpawnWindowStart | @HornyheadSpawnWindowEnd |
| HC1 | C2 | 连续均温 | @HornyheadGuardWarmupDays | >= | @HornyheadGuardTempThreshold | — |
| HC1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @HornyheadNestSiteStructureSet | — |
| HC1 | C4 | 巢体存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| HornyheadGuardEligible | AND | 1 | Condition | HC1.C1 |
| HornyheadGuardEligible | AND | 2 | Condition | HC1.C2 |
| HornyheadGuardEligible | AND | 3 | Condition | HC1.C3 |
| HornyheadGuardEligible | AND | 4 | Condition | HC1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Hornyhead_Guard_Route | @HornyheadGuardEligible | Guarding | Species 内行为份额 | @HornyheadGuardingShare |
| Hornyhead_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@HornyheadGuardWarmupDays 天）
读取 当前钓场结构集合
读取 石巢存在事实（上游 GuardAnchor Resolver 产出）

如果：
    当前日期处于 [@HornyheadSpawnWindowStart, @HornyheadSpawnWindowEnd]
    并且 连续均温 >= @HornyheadGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @HornyheadNestSiteStructureSet
    并且 巢体存在事实 == 存在

则：
    GuardingShare = @HornyheadGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。C3（基质资格）与 C4（石巢已筑成）不重复结算。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @HornyheadLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | stone_nest（雄鱼所筑砾石巢 [需正文]） |
| GuardAnchorRelationProfile | @HornyheadGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @HornyheadStoneNestSuitabilityProfile |
| LocalTemperatureProfile | @HornyheadGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配（构建型选址） → 关系评估 → 局部温度 → 合并；出局即
EARLY_RETURN（返回 0，不进入后续评估），不做「先全算再减」。推导来源（Tier B）：R07 FR3
「石巢筑造+守护」——雄鱼筑砾石巢（构筑型锚：选址适配先于守位）；巢体存在事实已在路由面
判定（C4），本程序不重复结算该 premise；步序与档位成员 [需正文] 校准（顺序/档位变化=
census 判同输入，结构变更需重审）。与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的底质 / 砾石滩结构 / 水深
读取 当前目标与石巢锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @HornyheadLocalGuardAnchorEligibility
    （锚=雄鱼所筑石巢；巢体存在已在路由面判定（C4），本步不重复结算 premise，
      只判「当前目标是否处于石巢锚的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中——构建型选址语义）：
    用当前目标的砾石底质查询 @HornyheadStoneNestSuitabilityProfile
    （筑巢基质三档分档槽=Profile 值域——档位成员与阈值不冻结 [需正文]）
    如果 基质 ∈ 最适应档（preferred 筑巢基质）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 基质）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除基质档）：
        返回 0（EARLY_RETURN：排除基质出局——不可筑巢底质无石巢分布，构建型选址先行）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与石巢锚点的关系（距离 / 朝向）查询 @HornyheadGuardRelationProfile
    （守卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @HornyheadGuardLocalTemperatureProfile
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

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT（**§2.4 已顺序还原（REP-ORDER-FIX-002）：early return 链＋分级命中；与 live BA-T1 Independent Factor Set 无序语义的分歧登记 README §7**） |
| LayerProfile | @HornyheadNormalLayerProfile |
| StructureProfile | @HornyheadNormalStructureProfile |
| TemperatureProfile | @HornyheadNormalTemperatureProfile |
| TimeProfile | @HornyheadNormalTimeProfile（早晨活跃方向） |
| ExtremeTemperatureGate | @HornyheadNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水层定位（**硬定位**——demersal：非底层
出局） → 结构 → 水温 → 时段 → 合并。推导来源：物种属性锚方向级（demersal 硬定位＋早晨活跃
——CSV 行级方向，[需正文] 校准；无 Story 空间程序证据的因子顺序不冒充）。水温从「末位算术门」
还原为链中档位判定（排除档=EARLY_RETURN，@HornyheadNormalTempFloor 为排除档边界参考）。
与 live BA-T1 Independent Factor Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

第 1 步 水层定位（硬定位，分级命中）：
    用当前水层查询 @HornyheadNormalLayerProfile
    （demersal 硬定位三档=Profile 值域不冻结）
    如果 水层 ∈ 底层档：
        LayerFit = 全额
    否则如果 ∈ 近底带档：
        LayerFit = 削减（× Profile 衰减参数——不清零）
    否则（远底层档）：
        返回 0（EARLY_RETURN：非底层格出局——demersal 硬判定）

第 2 步 结构（分级命中）：
    用当前结构查询 @HornyheadNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除结构档出局 [需正文：排除档成员]）

第 3 步 水温（分级命中）：
    用当前水温查询 @HornyheadNormalTemperatureProfile（三档=Profile 值域不冻结）
    如果 水温 ∈ 适温档：
        TemperatureFit = 全额
    否则如果 ∈ 边际档：
        TemperatureFit = 削减（不清零）
    否则（排除档——@HornyheadNormalTempFloor 为边界参考）：
        返回 0（EARLY_RETURN：极值温度带出局）

第 4 步 时段（分级命中）：
    用当前时段查询 @HornyheadNormalTimeProfile（早晨三档=Profile 值域不冻结）
    如果 时段 ∈ 活跃档：
        TimeFit = 全额
    否则如果 ∈ 一般档：
        TimeFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除时段档出局 [需正文：非活跃时段是否出局归 Profile 值域]）

第 5 步 合并：
    合并 LayerFit / StructureFit / TemperatureFit / TimeFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明——合并数学待机制侧，不因链序还原而隐式定义）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @HornyheadGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @HornyheadNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与石巢锚点的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @HornyheadGuardThreatProfile
    得到 ThreatEvaluation
    （无特异性形态：@HornyheadGuardThreatProfile 不区分威胁对象身份——R07 Open Question，
      对一切逼近锚点的呈现统一评价）

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@HornyheadGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

特异性注记（R07 Open Question）：@HornyheadGuardThreatProfile 当前**不区分**威胁对象身份（共生产卵者 / 掠食者 / 杂项入侵者）——target specificity 未冻结；本 Profile 是「无特异性」形态。特异性若立项＝Profile 重绑定（K13 先例），不新增通道或结构。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

EVAL_TARGET_AS_FOOD：
    用这些输入评价 @HornyheadNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@HornyheadNormalFeedingProfile 值域不冻结）：
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
| Guarding | QT-1 | @HornyheadGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼筑巢守护组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @HornyheadGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（巢体存在事实）+ R1；BA-T2 锚实例=stone_nest；R-T1 Profile 重绑定；QT-1；**顺序还原链序与档位结构（REP-ORDER-FIX-002：Guard 面锚存在性→构建型基质适配→关系→温度 early return 链、三档分级命中；Normal 面 demersal 硬定位→结构→水温→时段链；Response DECIDE 三档——推导依据 §0 判断顺序行，全部 [需正文] 校准）**。
- 放弃的自由度：(1) **guard target specificity**（R07 Open Question——对共生产卵者的分辨不表达，Profile 无特异性形态）；(2) Defense / Feeding arbitration（live V0）；(3) Guard 合并算子数学 OPERATOR UNDEFINED；(4) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(5) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需正文] 砾石基质集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；Guard Bake 锚存在性 early return 链＋分级命中，Normal Bake 硬定位链还原，Response DECIDE 档位展开）
