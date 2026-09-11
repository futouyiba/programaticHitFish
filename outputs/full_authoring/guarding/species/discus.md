# 七彩神仙（橙／白两色型｜Orange/White Discus｜Symphysodon aequifasciatus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | R02-S11 七彩神仙鱼(橙)｜亲鱼体表黏液喂养幼鱼；R02-S12 七彩神仙鱼(白)｜亲鱼护幼关系（色型不分裂）——两条 Story 一套表达（S12 判定：与 S11 同一表达；外观色型属资产/品质维度） |
| 冻结 Pattern | P04（CENSUS-B1 stories.jsonl：CENSUS-B1-DIS frozen_patterns=[P04]） |
| census 程序 | P-B1-DIS-RESP-GUARD（Response，GUARD_CONFLICT_DUAL_PATH_RESPONSE 族第 4 成员，HIGH；fry_anchor=幼鱼群；色型不分裂——S12 白色型同构对照，不重复建体） |
| 物种属性锚 | fish-reference-20260908：水温 26–31℃、最适 28.5℃、早晨活跃、警惕（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；census CENSUS-B1 归档；REP-COVERAGE-DELTA-001 #16/#22 判定） |
| 证据档 | Tier A（census 快照） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding(BroodCare)=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding） |

## 0. 上游语义与护巢形态

- 育幼形态：双亲育幼（BIPARENTAL_CARE，persistent condition，P04）；fry_anchor = 幼鱼群（贴附取食亲鱼体表黏液的幼鱼群 relation object）。幼鱼贴附取食黏液是**照护关系（允许贴附），非捕食**（census 原文）——该关系语义禁止被表达成 Feeding 通道。
- 色型不分裂：橙 / 白两色型同一 Species 表达；色型差异只在资产 / 外观维度，不分裂 Group、Profile 绑定或 Quality 结构（S12 判定逐字遵守）。
- census ↔ live 表达分歧（同 oscar.md §0 条目）：census 育幼期 body 为双路径（DUAL_PATH，HIGH）；live V0 为 Defense-only（RR-T2）。本文件表达 live V0；COMBINE_DUAL_PATH 数学 OPERATOR UNDEFINED，待机制侧。
- 互斥状态：guard_state ∈ {NONE, BIPARENTAL_CARE}。
- 表达超集说明：无。
- **判断顺序（REP-ORDER-FIX-002 顺序还原）**：BroodCare 面＝锚存在性判定 → 锚适配（**群栖境**三档——移动锚的适配判「稚鱼群所在栖境」而非固定巢址） → 关系评估（贴群三档） → 局部温度 → 合并；锚不存在格 EARLY_RETURN 出局（非「返回低值」）。推导来源（Tier A）：census P-B1-DIS premise「幼鱼贴附取食亲鱼体表黏液」——贴附=贴群关系；稚鱼群存在已在路由面结算（C4），Bake 不重复结算。Normal 面＝水温极值硬门（暖水窄温方向锚） → 掩体结构定位 → 静水 → 猎物 → 时段（早晨） → 合并——物种属性锚方向级 [需正文]。分级命中：各步三档（最适应=全额 / 可接受=削减不清零 / 排除=出局），档位成员与阈值全 Profile 值域不冻结。与 live BA-T2/BA-T1 模板平铺读法的分歧登记 README §7。

Profile 引用清单：@DiscusSpawnWindowStart @DiscusSpawnWindowEnd @DiscusGuardWarmupDays @DiscusGuardTempThreshold @DiscusBroodStructureSet @DiscusGuardingShare @DiscusLocalGuardAnchorEligibility @DiscusBroodHabitatSuitabilityProfile @DiscusGuardRelationProfile @DiscusGuardLocalTemperatureProfile @DiscusGuardThreatProfile @DiscusNormalStructureProfile @DiscusStillwaterProfile @DiscusPreyResourceProfile @DiscusNormalTimeProfile @DiscusNormalTempFloor @DiscusNormalFeedingProfile @DiscusGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| DI1 | C1 | 当前日期 | — | BETWEEN | @DiscusSpawnWindowStart | @DiscusSpawnWindowEnd |
| DI1 | C2 | 连续均温 | @DiscusGuardWarmupDays | >= | @DiscusGuardTempThreshold | — |
| DI1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @DiscusBroodStructureSet | — |
| DI1 | C4 | 稚鱼群存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| DiscusBroodCareEligible | AND | 1 | Condition | DI1.C1 |
| DiscusBroodCareEligible | AND | 2 | Condition | DI1.C2 |
| DiscusBroodCareEligible | AND | 3 | Condition | DI1.C3 |
| DiscusBroodCareEligible | AND | 4 | Condition | DI1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Discus_BroodCare_Route | @DiscusBroodCareEligible | BroodCare | Species 内行为份额 | @DiscusGuardingShare |
| Discus_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

Group 命名注记：目标 Group 记 BroodCare（育幼组）而非 Guarding——本鱼 relation object 是稚鱼群（Fry Guard 型），与巢守型（Nest Guard）共用同一模板族（§11.2 泛化），组名差异只影响绑定表，不影响结构。

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@DiscusGuardWarmupDays 天）
读取 当前钓场结构集合
读取 稚鱼群存在事实（上游 GuardAnchor Resolver：Fry / Brood Field 实例）

如果：
    当前日期处于 [@DiscusSpawnWindowStart, @DiscusSpawnWindowEnd]
    并且 连续均温 >= @DiscusGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @DiscusBroodStructureSet
    并且 稚鱼群存在事实 == 存在

则：
    BroodCareShare = @DiscusGuardingShare

否则：
    BroodCareShare = 0

SpecialShareTotal = BroodCareShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 BroodCareShare / NormalFeedingShare
```

Share 语义：live §7 契约。双亲育幼由份额整体表达（份额粒度，非个体分类）；橙 / 白色型共用本路由（色型不分裂）。

## 2. Bake

### 2.1 BroodCare Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=fry school）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @DiscusLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | fry_school（稚鱼群；移动锚，位置由上游 Resolver 解析） |
| GuardAnchorRelationProfile | @DiscusGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @DiscusBroodHabitatSuitabilityProfile |
| LocalTemperatureProfile | @DiscusGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 BroodCare Group｜中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配（群栖境） → 关系评估（贴群） → 局部温度 → 合并；出局即
EARLY_RETURN（返回 0，不进入后续评估），不做「先全算再减」。推导来源（Tier A）：census
P-B1-DIS premise「幼鱼贴附取食亲鱼体表黏液＝照护关系」——贴附=亲鱼贴群；稚鱼群存在已在
路由面判定（C4），本程序不重复结算该 premise。移动锚语义：锚适配判「稚鱼群所在栖境」
（群位置由上游 Resolver 解析），非固定巢址选址。步序与档位成员的正文级校准 [需正文]。
与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的结构 / 掩体 / 深度
读取 当前稚鱼群锚点位置（上游 Fry / Brood Field Resolver 产出）
读取 当前目标与稚鱼群锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @DiscusLocalGuardAnchorEligibility
    （锚=稚鱼群移动锚；稚鱼群存在已在路由面判定（C4），本步不重复结算 premise，
      只判「当前目标是否处于稚鱼群的合法护卫锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与育幼分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中——群栖境语义）：
    用当前目标的掩体结构查询 @DiscusBroodHabitatSuitabilityProfile
    （稚鱼群所在栖境的适配三档分档槽=Profile 值域——档位成员与阈值不冻结；
      移动锚：栖境质量随群位置整体评价）
    如果 群栖境 ∈ 最适应档（preferred 掩体栖境）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 栖境）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除栖境档）：
        返回 0（EARLY_RETURN：排除栖境出局——稚鱼群不驻留的栖境无育幼分布）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中——贴群语义）：
    用当前目标与稚鱼群的关系（距离 / 朝向）查询 @DiscusGuardRelationProfile
    （贴群护卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 贴群核档：
        RelationFit = 全额（贴群护卫——黏液喂养关系的空间形态）
    否则如果 ∈ 护卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0（EARLY_RETURN：护卫圈外无育幼占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @DiscusGuardLocalTemperatureProfile
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

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT（**§2.4 已顺序还原（REP-ORDER-FIX-002）：early return 链＋分级命中；与 live BA-T1 Independent Factor Set 无序语义的分歧登记 README §7**） |
| StructureProfile | @DiscusNormalStructureProfile（掩体结构因子） |
| StillwaterProfile | @DiscusStillwaterProfile（静水偏好因子） |
| PreyResourceProfile | @DiscusPreyResourceProfile（猎物资源因子） |
| TimeProfile | @DiscusNormalTimeProfile（早晨活跃方向） |
| ExtremeTemperatureGate | @DiscusNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水温极值硬门 → 掩体结构定位 → 静水 → 猎物 →
时段 → 合并。推导来源：物种属性锚方向级（暖水窄温 26–31℃→极值门先行；掩体结构栖境——
CSV 行级方向，[需正文] 校准；无 Story 空间程序证据的因子顺序不冒充）。水温门从「末位算术门」
还原为前置出局判定（@DiscusNormalTempFloor 为排除档边界参考）。与 live BA-T1 Independent Factor
Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前结构（掩体 / 倒木根区）
读取 当前点静水 / 流速事实
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

第 1 步 水温极值硬门（GATE_EXTREME_TEMP）：
    用当前点水温对照排除档边界（@DiscusNormalTempFloor 为边界参考）
    如果 当前点水温 ∈ 排除档（极值带）：
        返回 0（EARLY_RETURN：极值温度带出局——暖水窄温种的生存出局条件先行）

第 2 步 掩体结构定位（分级命中）：
    用当前结构查询 @DiscusNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（× Profile 衰减参数——不清零）
    否则：
        返回 0（EARLY_RETURN：排除结构档出局）

第 3 步 静水（分级命中）：
    用静水事实查询 @DiscusStillwaterProfile（三档=Profile 值域不冻结）
    如果 静水 ∈ 最适应档：
        StillwaterFit = 全额
    否则如果 ∈ 可接受档：
        StillwaterFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除流态档出局）

第 4 步 猎物（分级命中）：
    用猎物资源查询 @DiscusPreyResourceProfile（三档=Profile 值域不冻结）
    如果 猎物资源 ∈ 最适应档：
        PreyFit = 全额
    否则如果 ∈ 可接受档：
        PreyFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：无猎物资源档出局）

第 5 步 时段（分级命中）：
    用当前时段查询 @DiscusNormalTimeProfile（早晨三档=Profile 值域不冻结）
    如果 时段 ∈ 活跃档：
        TimeFit = 全额
    否则如果 ∈ 一般档：
        TimeFit = 削减（不清零）
    否则：
        返回 0（EARLY_RETURN：排除时段档出局 [需正文：非活跃时段是否出局归 Profile 值域]）

第 6 步 合并：
    合并 StructureFit / StillwaterFit / PreyFit / TimeFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明——合并数学待机制侧，不因链序还原而隐式定义）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| BroodCare | 顺序响应规则（Defense-only） | @DiscusGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @DiscusNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

BroodCare Group：

```plain text
读取 当前 Presentation 与稚鱼群锚点的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @DiscusGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@DiscusGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

边界注记：幼鱼贴附取食黏液＝照护关系（允许贴附），不得进入本 Group 的任何 Feeding / 评价通道（census 语义边界逐字遵守）。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

EVAL_TARGET_AS_FOOD：
    用这些输入评价 @DiscusNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→返回」为平铺占位；
与 §3.1 配置表「命中 / 未命中」两列语义对齐）：
    按三档判定 FoodEvaluation（档位成员=@DiscusNormalFeedingProfile 值域不冻结）：
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
| BroodCare | QT-1 | @DiscusGuardingEligibilityByQuality | @NeutralAffinity | 成熟双亲育幼组成；资格与 Response 分开（§12.6）；橙 / 白色型同表 |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。色型（橙 / 白）不产生品质分裂：外观差异属资产维度（S12 判定）。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（BroodCare 行查 @DiscusGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（稚鱼群存在事实）+ R1；BA-T2 锚实例=fry_school（§11.2 Fry Guard 泛化）；R-T1 Profile 重绑定；QT-1；两 Story 一文件（S12 色型不分裂判定）；**顺序还原链序与档位结构（REP-ORDER-FIX-002：BroodCare 面锚存在性→群栖境适配→贴群关系→温度 early return 链、三档分级命中；Normal 面极值门→掩体定位→静水→猎物→时段链；Response DECIDE 三档——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census 双路径 body（DUAL_PATH 第 4 成员，HIGH）→ live V0 Defense-only，分歧待机制侧；(2) 黏液喂养的照护关系——永不进入 Feeding 通道；(3) 色型分裂（橙 / 白同构，不建两套表达）；(4) 合并算子数学 OPERATOR UNDEFINED ×2；(5) live BA-T1 Independent Factor Set 无序因子语义的服从（Normal 面顺序还原链与无序合并语义拓扑分歧——登记 README §7，裁决归机制侧）；(6) 数值与 Profile 值域不冻结（含各步三档档位成员与阈值）。
- [需核对] 育幼掩体结构集合成员（倒木根区 / 静水掩体方向来自物种属性锚，具体成员 [需正文]）；窗口 / 阈值数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
顺序还原修复批次：REP-ORDER-FIX-002（§0/§2/§3/§5 修改；BroodCare Bake 锚存在性 early return 链＋分级命中，Normal Bake 链还原，Response DECIDE 档位展开）
