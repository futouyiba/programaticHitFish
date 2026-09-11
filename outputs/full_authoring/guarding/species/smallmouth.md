# 小口黑鲈（Smallmouth Bass｜Micropterus dolomieu）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | C07｜小口黑鲈·护巢 / 护幼（15-Case 已审冻结故事，Evidence 页 3d6a4137d23681759b0fff070b2f0e4c）；Story DB B01 行＝P04 Mode Candidate + P0x（FISH-R06-FR2 F-1 复核记载） |
| 冻结 Pattern | P04（雄鱼照护巢与幼鱼；照护状态支持区别于普通猎物获取的关系性响应） |
| 审核禁用项 | Suski 2003 钓放 / 窝内损失效应：第二轮审核明确不证明该效应，本文件不使用它构造任何时间反馈（C07 裁决，逐字遵守） |
| 相邻故事 | B01-S32 跟随翻底动物获取被惊出的猎物（R01 CoverageDelta）＝摄食面故事；其表达落点=上游扰动事实 + DynamicSpatialSlot + Reaction 通道（REP-COVERAGE-DELTA-001 #11 已判定），本文件不重复展开 |
| 物种属性锚 | fish-reference-20260908：水温 8.5–29.5℃、最适 19℃、benthopelagic、深 1–7m、晨昏活跃、好斗（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版） |
| 证据档 | Tier A（C07 冻结故事快照全文在 outputs/fcf_authoring_concrete_r2/baseline_mapping.md） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼照护巢与幼鱼（C07 已审主张）——覆盖护卵（nest）与护幼（fry）两阶段；冻结的是护巢 / 护幼压力，不含扰底跟随故事（C07 明示）。
- 锚点两阶段：GuardAnchor Resolver 实例 ∈ {nest_bed（卵床）, fry_school（稚鱼群）}——live §11.2 Fry Guard 泛化判例：同一 BA-T2 模板，锚差异=上游 Resolver 实例切换，不新增 BakeTemplate、不设 body 分支。
- C07 未决维度 R01 / R02（重叠 / 默认值策略、跨面程序包身份）：live V0 已取舍为 Defense-only 结构性关闭（例 1C + §8.8）；记录于 §5。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}（§13.1）；本鱼仅 Guarding 一个 Special Group。
- 同属对照纪律（FISH-R06-FR2 F-1 教训）：Micropterus 4 行中仅本行有 P04 护巢 Story（大口黑鲈双行均 0 Story / Identity 隔离）；同属泛化不成立，不做属级推广。
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：Guard 面＝繁殖阶段 premise 读取（锚实例配置级切换，body 不设分支） → 锚存在性判定 → 锚适配（三档） → 关系评估（三档） → 局部温度 → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier A）：C07 雄鱼照护巢与幼鱼——两段锚（§11.2 判例：先锚实例后空间判断）；链内步序推导=护巢空间判断序 [需正文 校准]。Normal 面＝水层软定位（benthopelagic） → 结构 → 水温（排除档=极值出局） → 时段（晨昏） → 合并——物种属性锚方向级 [需正文]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

Profile 引用清单：@SmallmouthSpawnWindowStart @SmallmouthSpawnWindowEnd @SmallmouthGuardWarmupDays @SmallmouthGuardTempThreshold @SmallmouthNestStructureSet @SmallmouthGuardStages @SmallmouthGuardingShare @SmallmouthLocalGuardAnchorEligibility @SmallmouthNestSuitabilityProfile @SmallmouthGuardRelationProfile @SmallmouthGuardLocalTemperatureProfile @SmallmouthGuardThreatProfile @SmallmouthNormalLayerProfile @SmallmouthNormalStructureProfile @SmallmouthNormalTemperatureProfile @SmallmouthNormalTimeProfile @SmallmouthNormalTempFloor @SmallmouthNormalFeedingProfile @SmallmouthGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| SM1 | C1 | 当前日期 | — | BETWEEN | @SmallmouthSpawnWindowStart | @SmallmouthSpawnWindowEnd |
| SM1 | C2 | 连续均温 | @SmallmouthGuardWarmupDays | >= | @SmallmouthGuardTempThreshold | — |
| SM1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @SmallmouthNestStructureSet | — |
| SM1 | C4 | 繁殖阶段事实 | — | IN | @SmallmouthGuardStages | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| SmallmouthGuardEligible | AND | 1 | Condition | SM1.C1 |
| SmallmouthGuardEligible | AND | 2 | Condition | SM1.C2 |
| SmallmouthGuardEligible | AND | 3 | Condition | SM1.C3 |
| SmallmouthGuardEligible | AND | 4 | Condition | SM1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Smallmouth_Guard_Route | @SmallmouthGuardEligible | Guarding | Species 内行为份额 | @SmallmouthGuardingShare |
| Smallmouth_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@SmallmouthGuardWarmupDays 天）
读取 当前钓场结构集合
读取 繁殖阶段事实

如果：
    当前日期处于 [@SmallmouthSpawnWindowStart, @SmallmouthSpawnWindowEnd]
    并且 连续均温 >= @SmallmouthGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @SmallmouthNestStructureSet
    并且 繁殖阶段事实 IN @SmallmouthGuardStages（卵床守护 / 稚鱼守护两段）

则：
    GuardingShare = @SmallmouthGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：Species 当前基础供给权重的无量纲分配比例（live §7 契约）。阶段事实（C4）不重复结算 C1–C3 的因果：C1–C3 判资格（窗口 / 适温 / 合法巢区），C4 判当前处于照护阶段（PARENTAL_GUARD 型状态，上游 typed 枚举）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例随阶段切换）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @SmallmouthLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest_bed｜fry_school（随繁殖阶段事实配置级切换；body 不设分支） |
| GuardAnchorRelationProfile | @SmallmouthGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @SmallmouthNestSuitabilityProfile |
| LocalTemperatureProfile | @SmallmouthGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝（premise：繁殖阶段事实→锚实例配置级切换，body 不设分支） → 锚存在性判定 → 锚适配 →
关系评估 → 局部温度 → 合并；出局即 EARLY_RETURN（返回 0，不进入后续评估），不做「先全算再减」。
推导来源（Tier A）：C07 雄鱼照护巢与幼鱼——两段锚形态（§11.2 判例：锚实例先行，空间判断随后）；
链内步序推导=护巢空间判断序，正文级校准 [需正文]。与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的结构 / 底质 / 深度
读取 当前繁殖阶段事实，选择 GuardAnchorResolver 实例：
    卵床守护阶段 → 锚=nest_bed（当前场内卵床位置）
    稚鱼守护阶段 → 锚=fry_school（当前稚鱼群位置）
读取 当前目标与该锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @SmallmouthLocalGuardAnchorEligibility
    （锚=当前阶段锚实例；繁殖阶段资格已在路由面判定（C4），本步不重复结算 premise，
      只判「当前目标是否处于该锚的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的底质 / 结构查询 @SmallmouthNestSuitabilityProfile
    （两段共用 Profile，锚面语义随锚实例切换：卵床期=巢床底质结构 / 稚鱼期=稚鱼群所在结构；
      三档分档槽=Profile 值域——档位成员与阈值不冻结）
    如果 锚面 ∈ 最适应档（preferred 锚面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 锚面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0（EARLY_RETURN：排除锚面出局）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与锚点的关系（距离 / 朝向）查询 @SmallmouthGuardRelationProfile
    （守卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @SmallmouthGuardLocalTemperatureProfile
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
| LayerProfile | @SmallmouthNormalLayerProfile |
| StructureProfile | @SmallmouthNormalStructureProfile |
| TemperatureProfile | @SmallmouthNormalTemperatureProfile |
| TimeProfile | @SmallmouthNormalTimeProfile |
| ExtremeTemperatureGate | @SmallmouthNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水层定位（软定位） → 结构 → 水温 → 时段 → 合并。
推导来源：物种属性锚方向级（benthopelagic 软定位＋晨昏活跃——CSV 行级方向，[需正文] 校准；
无 Story 空间程序证据的因子顺序不冒充）。水温从「末位算术门」还原为链中档位判定（排除档=
EARLY_RETURN，@SmallmouthNormalTempFloor 为排除档边界参考）。与 live BA-T1 Independent Factor
Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段（晨昏活跃方向由 @SmallmouthNormalTimeProfile 值域承载）

第 1 步 水层定位（软定位，分级命中）：
    用当前水层查询 @SmallmouthNormalLayerProfile
    （benthopelagic 软定位三档=Profile 值域不冻结 [需正文：硬定位与否]）
    如果 水层 ∈ 近底带档：
        LayerFit = 全额
    否则如果 ∈ 中间水层档：
        LayerFit = 削减（× Profile 衰减参数——不清零）
    否则（远底带档）：
        返回 0（EARLY_RETURN：远离底带格出局）

第 2 步 结构（分级命中）：
    用当前结构查询 @SmallmouthNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除结构档出局 [需正文：排除档成员]）

第 3 步 水温（分级命中）：
    用当前水温查询 @SmallmouthNormalTemperatureProfile（三档=Profile 值域不冻结）
    如果 水温 ∈ 适温档：
        TemperatureFit = 全额
    否则如果 ∈ 边际档：
        TemperatureFit = 削减（不清零）
    否则（排除档——@SmallmouthNormalTempFloor 为边界参考）：
        返回 0（EARLY_RETURN：极值温度带出局）

第 4 步 时段（分级命中）：
    用当前时段查询 @SmallmouthNormalTimeProfile（晨昏三档=Profile 值域不冻结）
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
| Guarding | 顺序响应规则（Defense-only） | @SmallmouthGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；Reaction 槽 OFF） | @SmallmouthNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与巢区 / 稚鱼群的关系（按当前锚实例）
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @SmallmouthGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@SmallmouthGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

EVAL_TARGET_AS_FOOD：
    用这些输入评价 @SmallmouthNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@SmallmouthNormalFeedingProfile 值域不冻结）：
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
| Guarding | QT-1 | @SmallmouthGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼照护组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @SmallmouthGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（阶段事实作第四原子）+ R1；BA-T2 锚实例切换（nest_bed / fry_school，§11.2 MERGE_SUPPORTED）；R-T1 Profile 重绑定；QT-1 Eligibility/Affinity；**顺序还原链序与档位结构（REP-ORDER-FIX-002：premise 锚实例前置＋锚存在性→锚适配→关系→温度 early return 链、三档分级命中；Normal 面定位→结构→水温→时段链；Response DECIDE 三档——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0，例 1C）；(2) Guard Bake 合并算子 OPERATOR UNDEFINED；(3) Suski 2003 钓放损失时间反馈——审核禁用项，永不进入本表达；(4) 护巢雄鱼个体的巢位领地史（逐个体状态）——无 Story 证据；(5) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(6) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需核对] Story DB 行级 Pattern 标签（B01=P04 Mode Candidate + P0x 已由 F-1 复核记载，以 Story DB 为准）；巢床结构集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；Guard Bake 锚存在性 early return 链＋分级命中，Normal Bake 链还原，Response DECIDE 档位展开）
