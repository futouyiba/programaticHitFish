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
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @DiscusLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | fry_school（稚鱼群；移动锚，位置由上游 Resolver 解析） |
| GuardAnchorRelationProfile | @DiscusGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @DiscusBroodHabitatSuitabilityProfile |
| LocalTemperatureProfile | @DiscusGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 BroodCare Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 掩体 / 深度
读取 当前稚鱼群锚点位置（上游 Fry / Brood Field Resolver 产出）
读取 当前目标与稚鱼群锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @DiscusLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与稚鱼群的关系查询 @DiscusGuardRelationProfile
得到 RelationFit

用当前目标的掩体结构查询 @DiscusBroodHabitatSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @DiscusGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 BroodCare SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| StructureProfile | @DiscusNormalStructureProfile（掩体结构因子） |
| StillwaterProfile | @DiscusStillwaterProfile（静水偏好因子） |
| PreyResourceProfile | @DiscusPreyResourceProfile（猎物资源因子） |
| TimeProfile | @DiscusNormalTimeProfile（早晨活跃方向） |
| ExtremeTemperatureGate | @DiscusNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前结构（掩体 / 倒木根区）
读取 当前点静水 / 流速事实
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

用结构查询 @DiscusNormalStructureProfile 得到 StructureFit
用静水事实查询 @DiscusStillwaterProfile 得到 StillwaterFit
用猎物资源查询 @DiscusPreyResourceProfile 得到 PreyFit
用时段查询 @DiscusNormalTimeProfile 得到 TimeFit

如果 当前点水温 < @DiscusNormalTempFloor：
    返回 极低空间权重（early return）

合并 StructureFit / StillwaterFit / PreyFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
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

评价 @DiscusGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

边界注记：幼鱼贴附取食黏液＝照护关系（允许贴附），不得进入本 Group 的任何 Feeding / 评价通道（census 语义边界逐字遵守）。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

用这些输入评价 @DiscusNormalFeedingProfile
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

- 使用的自由度：V1 四原子（稚鱼群存在事实）+ R1；BA-T2 锚实例=fry_school（§11.2 Fry Guard 泛化）；R-T1 Profile 重绑定；QT-1；两 Story 一文件（S12 色型不分裂判定）。
- 放弃的自由度：(1) census 双路径 body（DUAL_PATH 第 4 成员，HIGH）→ live V0 Defense-only，分歧待机制侧；(2) 黏液喂养的照护关系——永不进入 Feeding 通道；(3) 色型分裂（橙 / 白同构，不建两套表达）；(4) 合并算子数学 OPERATOR UNDEFINED ×2。
- [需核对] 育幼掩体结构集合成员（倒木根区 / 静水掩体方向来自物种属性锚，具体成员 [需正文]）；窗口 / 阈值数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
