# 米达斯慈鲷（Midas Cichlid｜Amphilophus citrinellus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R09 米达斯慈鲷（R09 P04×6「慈鲷+岩礁护卵系内部多样性」之一；triage 批注：「洞穴顶产卵米达斯」；Story 页 URL 未在本地快照） |
| 冻结 Pattern | P04（洞穴顶产卵 + 双亲守护——产卵面位置型护卵变体，R09 P04 内部多样性样本） |
| 物种属性锚 | fish-reference-20260908：水温 23–33℃、最适 28℃、benthopelagic、全天活跃、好斗（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；R09 FR3 归档摘要在 tmp/triage_r09.md） |
| 证据档 | Tier B（triage 批注一行；Story 正文 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 护巢形态：洞穴顶产卵——洞穴顶壁 / 岩洞内壁产卵并守护（R09 triage 批注「洞穴顶产卵米达斯」）；亲鱼组成（双亲判读 [需正文]）。
- P04 内部多样性意义（R09 FR3 待裁口径）：护卵变体（洞穴顶 / 浊水双亲 / 岩缝扇卵 / 雄巢扇护 / 吸盘雄护）按「P04 样本累计 or 内部 typed variant 边界」记录——表达侧当前一律落同模板（BA-T2）+ Profile 重绑定，变体差异由锚实例 / Profile 承载，不建新模板（同 R07 石巢判例方向）。
- 互斥状态：ReproductionState ∈ {NONE, ACTIVE_SPAWNING, PARENTAL_GUARD}。
- 表达超集说明：Tier B 文件的条件原子结构与集名按 P04 标准骨架给出；洞穴结构集合成员、亲鱼组成、窗口数值全部 @ 化或标注 [需正文]。
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：Guard 面＝锚存在性判定 → 锚适配（洞穴产卵面三档） → 关系评估（三档） → 局部温度 → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier B）：R09 triage 批注一句「洞穴顶产卵米达斯」（锚型方向级）；步序与档位成员 [需正文] 校准。Normal 面＝水层软定位（benthopelagic） → 结构 → 水温（排除档=极值出局） → 时段（全天） → 合并——物种属性锚方向级 [需正文]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

Profile 引用清单：@MidasSpawnWindowStart @MidasSpawnWindowEnd @MidasGuardWarmupDays @MidasGuardTempThreshold @MidasSpawnSurfaceSet @MidasGuardingShare @MidasLocalGuardAnchorEligibility @MidasCaveSpawnSuitabilityProfile @MidasGuardRelationProfile @MidasGuardLocalTemperatureProfile @MidasGuardThreatProfile @MidasNormalLayerProfile @MidasNormalStructureProfile @MidasNormalTemperatureProfile @MidasNormalTimeProfile @MidasNormalTempFloor @MidasNormalFeedingProfile @MidasGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| MD1 | C1 | 当前日期 | — | BETWEEN | @MidasSpawnWindowStart | @MidasSpawnWindowEnd |
| MD1 | C2 | 连续均温 | @MidasGuardWarmupDays | >= | @MidasGuardTempThreshold | — |
| MD1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @MidasSpawnSurfaceSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| MidasGuardEligible | AND | 1 | Condition | MD1.C1 |
| MidasGuardEligible | AND | 2 | Condition | MD1.C2 |
| MidasGuardEligible | AND | 3 | Condition | MD1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Midas_Guard_Route | @MidasGuardEligible | Guarding | Species 内行为份额 | @MidasGuardingShare |
| Midas_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@MidasGuardWarmupDays 天）
读取 当前钓场结构集合

如果：
    当前日期处于 [@MidasSpawnWindowStart, @MidasSpawnWindowEnd]
    并且 连续均温 >= @MidasGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @MidasSpawnSurfaceSet（含洞穴顶壁类结构）

则：
    GuardingShare = @MidasGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。双亲守护由份额整体表达（份额粒度，非个体分类）。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=洞穴产卵面）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @MidasLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | cave_ceiling_spawn（洞穴顶壁 / 岩洞内壁产卵面 [需正文]） |
| GuardAnchorRelationProfile | @MidasGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @MidasCaveSpawnSuitabilityProfile |
| LocalTemperatureProfile | @MidasGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配 → 关系评估 → 局部温度 → 合并；出局即 EARLY_RETURN（返回 0，
不进入后续评估），不做「先全算再减」。推导来源（Tier B）：R09 triage 批注一句「洞穴顶产卵
米达斯」（洞穴顶壁/岩洞内壁产卵面——锚型方向级）；步序与档位成员 [需正文] 校准（顺序/档位
变化=census 判同输入，结构变更需重审）。与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的岩洞结构 / 深度 / 遮蔽关系
读取 当前目标与洞穴产卵面锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @MidasLocalGuardAnchorEligibility
    （锚=cave_ceiling_spawn 洞穴产卵面；护巢资格已在路由面判定，本步不重复结算 premise，
      只判「当前目标是否处于产卵面锚的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的洞穴结构查询 @MidasCaveSpawnSuitabilityProfile
    （洞穴产卵面三档分档槽=Profile 值域——档位成员与阈值不冻结 [需正文]）
    如果 锚面 ∈ 最适应档（preferred 产卵面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 产卵面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0（EARLY_RETURN：排除产卵面出局——无可用洞穴结构无产卵面分布）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与产卵面锚点的关系（距离 / 朝向）查询 @MidasGuardRelationProfile
    （守卫位三档=Profile 值域不冻结——洞穴型守卫位=洞内/洞口占位 [需正文]）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @MidasGuardLocalTemperatureProfile
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
| LayerProfile | @MidasNormalLayerProfile |
| StructureProfile | @MidasNormalStructureProfile |
| TemperatureProfile | @MidasNormalTemperatureProfile |
| TimeProfile | @MidasNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @MidasNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水层定位（软定位） → 结构 → 水温 → 时段 → 合并。
推导来源：物种属性锚方向级（benthopelagic 软定位＋全天活跃——CSV 行级方向，[需正文] 校准；
无 Story 空间程序证据的因子顺序不冒充）。水温从「末位算术门」还原为链中档位判定（排除档=
EARLY_RETURN，@MidasNormalTempFloor 为排除档边界参考）。与 live BA-T1 Independent Factor
Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

第 1 步 水层定位（软定位，分级命中）：
    用当前水层查询 @MidasNormalLayerProfile
    （benthopelagic 软定位三档=Profile 值域不冻结 [需正文：硬定位与否]）
    如果 水层 ∈ 近底带档：
        LayerFit = 全额
    否则如果 ∈ 中间水层档：
        LayerFit = 削减（× Profile 衰减参数——不清零）
    否则（远底带档）：
        返回 0（EARLY_RETURN：远离底带格出局）

第 2 步 结构（分级命中）：
    用当前结构查询 @MidasNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除结构档出局 [需正文：排除档成员]）

第 3 步 水温（分级命中）：
    用当前水温查询 @MidasNormalTemperatureProfile（三档=Profile 值域不冻结）
    如果 水温 ∈ 适温档：
        TemperatureFit = 全额
    否则如果 ∈ 边际档：
        TemperatureFit = 削减（不清零）
    否则（排除档——@MidasNormalTempFloor 为边界参考）：
        返回 0（EARLY_RETURN：极值温度带出局）

第 4 步 时段（分级命中）：
    用当前时段查询 @MidasNormalTimeProfile（全天三档=Profile 值域不冻结）
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
| Guarding | 顺序响应规则（Defense-only） | @MidasGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @MidasNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与洞穴产卵面锚点的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @MidasGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@MidasGuardThreatProfile 值域不冻结）：
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
    用这些输入评价 @MidasNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@MidasNormalFeedingProfile 值域不冻结）：
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
| Guarding | QT-1 | @MidasGuardingEligibilityByQuality | @NeutralAffinity | 成熟亲鱼护卵组成（双亲 [需正文]）；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @MidasGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子 + R1；BA-T2 锚实例=cave_ceiling_spawn（P04 内部多样性由锚实例 / Profile 承载）；R-T1 Profile 重绑定；QT-1；**顺序还原链序与档位结构（REP-ORDER-FIX-002：Guard 面锚存在性→锚适配→关系→温度 early return 链、三档分级命中；Normal 面定位→结构→水温→时段链；Response DECIDE 三档——推导依据 §0 判断顺序行，全部 [需正文] 校准）**。
- 放弃的自由度：(1) Defense / Feeding arbitration（live V0）；(2) Guard 合并算子数学 OPERATOR UNDEFINED；(3) 洞穴内微地形（顶壁朝向 / 洞深梯度）——无 Story 证据，不表达；(4) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(5) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需正文] 洞穴产卵面结构集合成员、亲鱼组成（双亲判读）、窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；Guard Bake 锚存在性 early return 链＋分级命中，Normal Bake 链还原，Response DECIDE 档位展开）
