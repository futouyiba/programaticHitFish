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
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：Guard 面＝锚存在性判定 → 锚适配（岩缝产卵面三档） → 关系评估（三档） → 局部温度（冷水轴三档） → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier B）：R09 triage 批注一句「单鳍多线鱼（岩缝胸鳍扇卵 40-45 天）」（岩缝卵块锚——方向级；扇卵=premise 证据不进 Response/Bake 判断步；40–45 天=Story 证据常量照录 §0）；步序与档位成员 [需正文] 校准。Normal 面＝水层硬定位（demersal——非底层出局） → 结构 → 水温（冷水轴——排除档出局） → 时段（全天） → 合成——物种属性锚方向级 [需正文]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

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
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @AtkaLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | crevice_spawn（岩缝 / 礁石平台卵块 [需正文]） |
| GuardAnchorRelationProfile | @AtkaGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @AtkaCreviceSpawnSuitabilityProfile |
| LocalTemperatureProfile | @AtkaGuardLocalTemperatureProfile（冷水轴：2.7–4.7℃ 方向由 Profile 值域承载） |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配 → 关系评估 → 局部温度 → 合并；出局即 EARLY_RETURN（返回 0，
不进入后续评估），不做「先全算再减」。推导来源（Tier B）：R09 triage 批注一句「岩缝胸鳍扇卵
40-45 天」——雄鱼岩缝卵块守护（锚型方向级；胸鳍扇卵=朝向卵块的照护行为，属 premise 持续性
证据，不进本判断链）；步序与档位成员 [需正文] 校准（顺序/档位变化=census 判同输入，结构变更
需重审）。与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的岩礁结构 / 岩缝分布 / 深度
读取 当前目标与卵块锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @AtkaLocalGuardAnchorEligibility
    （锚=crevice_spawn 岩缝卵块；护巢资格已在路由面判定，本步不重复结算 premise，
      只判「当前目标是否处于卵块锚的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的岩缝结构查询 @AtkaCreviceSpawnSuitabilityProfile
    （岩缝/礁石平台产卵面三档分档槽=Profile 值域——档位成员与阈值不冻结 [需正文]）
    如果 锚面 ∈ 最适应档（preferred 产卵面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 产卵面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0（EARLY_RETURN：排除产卵面出局——无可用岩缝无卵块分布）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与卵块锚点的关系（距离 / 朝向）查询 @AtkaGuardRelationProfile
    （守卫位三档=Profile 值域不冻结——扇护型守卫位=卵块邻近占位 [需正文]）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（扇护占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中——冷水轴）：
    用当前点局部温度查询 @AtkaGuardLocalTemperatureProfile
    （护巢期局部温度三档=Profile 值域不冻结——冷水轴 2.7–4.7℃ 方向由 Profile 值域承载）
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
| LayerProfile | @AtkaNormalLayerProfile |
| StructureProfile | @AtkaNormalStructureProfile |
| TemperatureProfile | @AtkaNormalTemperatureProfile（冷水轴） |
| TimeProfile | @AtkaNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @AtkaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水层定位（**硬定位**——demersal：非底层
出局） → 结构 → 水温 → 时段 → 合并。推导来源：物种属性锚方向级（demersal 硬定位＋冷水轴
2.7–4.7℃＋全天活跃——CSV 行级方向，[需正文] 校准；无 Story 空间程序证据的因子顺序不冒充）。
水温从「末位算术门」还原为链中档位判定（排除档=EARLY_RETURN，@AtkaNormalTempFloor 为排除档
边界参考——冷水轴值域由 Profile 承载）。与 live BA-T1 Independent Factor Set（因子无序合并）
模板语义的分歧登记 README §7。

读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

第 1 步 水层定位（硬定位，分级命中）：
    用当前水层查询 @AtkaNormalLayerProfile
    （demersal 硬定位三档=Profile 值域不冻结）
    如果 水层 ∈ 底层档：
        LayerFit = 全额
    否则如果 ∈ 近底带档：
        LayerFit = 削减（× Profile 衰减参数——不清零）
    否则（远底层档）：
        返回 0（EARLY_RETURN：非底层格出局——demersal 硬判定）

第 2 步 结构（分级命中）：
    用当前结构查询 @AtkaNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除结构档出局 [需正文：排除档成员]）

第 3 步 水温（分级命中——冷水轴）：
    用当前水温查询 @AtkaNormalTemperatureProfile（三档=Profile 值域不冻结——冷水轴方向由值域承载）
    如果 水温 ∈ 适温档：
        TemperatureFit = 全额
    否则如果 ∈ 边际档：
        TemperatureFit = 削减（不清零）
    否则（排除档——@AtkaNormalTempFloor 为边界参考）：
        返回 0（EARLY_RETURN：极值温度带出局）

第 4 步 时段（分级命中）：
    用当前时段查询 @AtkaNormalTimeProfile（全天三档=Profile 值域不冻结）
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
| Guarding | 顺序响应规则（Defense-only） | @AtkaGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @AtkaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与岩缝卵块锚点的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @AtkaGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@AtkaGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

边界注记：胸鳍扇卵（朝向卵块的照护行为）不进本 Response 面——它由 guard premise 的持续性事实承载（§0）；把扇卵写成 Response 通道会造成「照护行为」与「对呈现响应」双重结算。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

EVAL_TARGET_AS_FOOD：
    用这些输入评价 @AtkaNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@AtkaNormalFeedingProfile 值域不冻结）：
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=crevice_spawn；R-T1 Profile 重绑定；QT-1；**顺序还原链序与档位结构（REP-ORDER-FIX-002：Guard 面锚存在性→锚适配→扇护关系→温度 early return 链、三档分级命中；Normal 面 demersal 硬定位→结构→水温（冷水轴）→时段链；Response DECIDE 三档——推导依据 §0 判断顺序行，全部 [需正文] 校准）**。
- 放弃的自由度：(1) 扇卵行为进 Response 面（拒——照护行为属 premise 持续性证据）；(2) 守护期天数作配置数值（40–45 天是 Story 事实常量，窗口口径归上游事实层）；(3) Defense / Feeding arbitration（live V0）；(4) Guard 合并算子数学 OPERATOR UNDEFINED；(5) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(6) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需正文] 岩缝结构集合成员、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；Guard Bake 锚存在性 early return 链＋分级命中，Normal Bake 硬定位链还原，Response DECIDE 档位展开）
