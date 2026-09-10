# 罗非鱼（Nile Tilapia｜Oreochromis niloticus）｜Guarding 系四面生产级表达（口孵型）

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | B01-S44 罗非鱼｜雌性口孵期间摄食减少与幼鱼回口（R01 CoverageDelta，REP-COVERAGE-DELTA-001 #3 已判定：口孵=类型化繁殖状态路由 + BA-T2 育幼锚 + R-T1 Cap；雌性专属由 share 表达） |
| 冻结 Pattern | P04 语义（K4 繁殖/育幼锚判定转述）；Story DB 行级 Pattern 标签未在本地快照 [需核对] |
| 相邻故事 | C08 尼罗罗非鱼｜刮食与悬浮颗粒摄食混合（15-Case）＝NormalFeeding 面既有表达（live 例 3 双通道），本文件 NormalFeeding Response 直接绑定该结构，不重复展开 |
| 物种属性锚 | fish-reference-20260908：水温 13.5–33℃、最适 23.25℃、benthopelagic、深 0–20m、全天活跃、温和（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；coverage report 归档） |
| 证据档 | Tier A（coverage #3 四面判定在案；Story 正文细节 [需正文]） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Brooding=Feeding-with-Cap（R-T1 单通道 + 固定 Cap；**非 Defense-only**——口孵亲鱼无守巢防御语义，判定句为「摄食减少」）；NormalFeeding=R-T2 固定双通道（刮食 + 悬浮颗粒） |

## 0. 上游语义与护巢形态

- 口孵形态：雌性口孵（typed 繁殖状态）——口孵期间摄食减少（Feeding Cap）；幼鱼回口（受惊时稚鱼返回亲鱼口腔）。
- 幼鱼回口的归属边界：回口是稚鱼侧对威胁的世界侧行为（brood anchor 世界模拟），**不是亲鱼对呈现的 Response**——不进入亲鱼 Response 面（防双重结算：稚鱼群锚已由 BroodCare 型 anchor 语义承载）。
- 雌性专属：由 share 表达（@TilapiaBroodingFemaleShare 路由雌性份额），不引入逐个体性别属性事实（coverage #3 判定 + §2.1 share-vector 先例；不触发 Sex/Maturity 个体属性 TODO）。
- 锚点：口孵群（brood-in-mouth，与个体绑定的锚）——GuardAnchor Resolver 实例 = 口孵群；空间锚=育幼期雌鱼常驻区 [需正文：口孵期雌鱼空间偏好无本地正文]。
- 互斥状态：繁殖阶段 ∈ {NONE, BROODING（口孵期）, …}（typed 枚举；本 Story 冻结 BROODING 行）。
- 与例 3 双通道的关系：NormalFeeding Group 的双通道摄食（刮食 + 悬浮颗粒）已由 live 例 3 表达（汇总算子 OPERATOR UNDEFINED 标注在案）；本文件只做绑定引用。

Profile 引用清单：@TilapiaSpawnWindowStart @TilapiaSpawnWindowEnd @TilapiaBroodingWarmupDays @TilapiaBroodingTempThreshold @TilapiaBroodingStages @TilapiaBroodingFemaleShare @TilapiaBroodAnchorEligibility @TilapiaBroodCareSuitabilityProfile @TilapiaBroodingFeedingCap @ResponseCap @TilapiaNormalLayerProfile @TilapiaNormalStructureProfile @TilapiaNormalTemperatureProfile @TilapiaNormalTimeProfile @TilapiaNormalTempFloor @GrazingProfile @SuspendedFeedingProfile @TilapiaBroodingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| TI1 | C1 | 当前日期 | — | BETWEEN | @TilapiaSpawnWindowStart | @TilapiaSpawnWindowEnd |
| TI1 | C2 | 连续均温 | @TilapiaBroodingWarmupDays | >= | @TilapiaBroodingTempThreshold | — |
| TI1 | C3 | 繁殖阶段事实 | — | IN | @TilapiaBroodingStages | — |

条件原子化说明：口孵无巢体 / 巢区结构语义，故无 CONTAINS_ANY 原子；「处于口孵期」原子化为繁殖阶段事实 IN @TilapiaBroodingStages（typed 枚举集，Profile 层定义成员）。

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| TilapiaBroodingEligible | AND | 1 | Condition | TI1.C1 |
| TilapiaBroodingEligible | AND | 2 | Condition | TI1.C2 |
| TilapiaBroodingEligible | AND | 3 | Condition | TI1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Tilapia_Brooding_Route | @TilapiaBroodingEligible | Brooding | Species 内雌性份额路由 | @TilapiaBroodingFemaleShare |
| Tilapia_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@TilapiaBroodingWarmupDays 天）
读取 繁殖阶段事实

如果：
    当前日期处于 [@TilapiaSpawnWindowStart, @TilapiaSpawnWindowEnd]
    并且 连续均温 >= @TilapiaBroodingTempThreshold
    并且 繁殖阶段事实 IN @TilapiaBroodingStages

则：
    BroodingShare = @TilapiaBroodingFemaleShare（雌性专属由份额表达）

否则：
    BroodingShare = 0

SpecialShareTotal = BroodingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 BroodingShare / NormalFeedingShare
```

Share 语义：live §7 契约；份额是供给比例，不是逐个体性别分类。

## 2. Bake

### 2.1 Brooding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化，锚实例=口孵群）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @TilapiaBroodAnchorEligibility |
| GuardAnchorResolverInstance | brood_in_mouth（口孵群；锚与个体绑定，空间表现=育幼期雌鱼常驻区） |
| GuardAnchorSuitabilityProfile | @TilapiaBroodCareSuitabilityProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

注：本组无独立 RelationProfile / LocalTemperatureProfile 行——口孵锚与个体绑定（无「目标点 vs 固定锚位」关系轴）；空间收缩由 @TilapiaBroodCareSuitabilityProfile 单 Factor 承载 [需正文：口孵期雌鱼空间偏好]。这是 BA-T2 的退化绑定，不是新模板。

### 2.2 Brooding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 水层 / 深度
读取 育幼期雌鱼常驻区事实（口孵群锚的空间投影，上游 Resolver 产出）

如果当前目标不满足 @TilapiaBroodAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标的常驻区适配查询 @TilapiaBroodCareSuitabilityProfile
得到 BroodCareFit

返回 Brooding SpatialDistributionWeight（单 Factor，无合并步）
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT |
| LayerProfile | @TilapiaNormalLayerProfile |
| StructureProfile | @TilapiaNormalStructureProfile |
| TemperatureProfile | @TilapiaNormalTemperatureProfile |
| TimeProfile | @TilapiaNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @TilapiaNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

用当前水层查询 @TilapiaNormalLayerProfile 得到 LayerFit
用当前结构查询 @TilapiaNormalStructureProfile 得到 StructureFit
用当前水温查询 @TilapiaNormalTemperatureProfile 得到 TemperatureFit
用当前时段查询 @TilapiaNormalTimeProfile 得到 TimeFit

如果 TemperatureFit < @TilapiaNormalTempFloor：
    返回 极低空间权重（early return）

合并 LayerFit / StructureFit / TemperatureFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子；live §15.2 M0 同款占位声明）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（R-T1 结构族 + 固定 Cap 槽；NormalFeeding=live 例 3 双通道绑定）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Brooding | R-T1 单通道 + 固定 Cap（Feeding-with-Cap） | @GrazingProfile/@SuspendedFeedingProfile 继承 + @TilapiaBroodingFeedingCap | 返回 Cap 后 FeedingResponse | 返回低 / 无响应 |
| NormalFeeding | R-T2 固定双通道（刮食 + 悬浮颗粒；live 例 3） | @GrazingProfile + @SuspendedFeedingProfile | 返回 FinalResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Brooding Group（Feeding-with-Cap——「口孵期间摄食减少」的表达）：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前动态 Feeding / Pursuit 相关事实

评价 BaseResponse（复用 NormalFeeding 双通道评价结构，见下节）

Response = MIN(BaseResponse, @TilapiaBroodingFeedingCap)

返回 Response
```

Cap 语义：模板固定 Cap 槽（live §13.3 R-T1：`Response = MIN(BaseResponse, @ResponseCap)`）；「摄食减少」被表达为 Cap 上限，不是攻击 / 防御通道，不是任意后处理脚本。

NormalFeeding Group（live 例 3 原样绑定）：

```plain text
评价 刮食 Channel：
    使用 @GrazingProfile

评价 悬浮颗粒摄食 Channel：
    使用 @SuspendedFeedingProfile

按模板固定规则合并两个 Channel
算子标注：OPERATOR UNDEFINED — 待机制侧（同一摄食 evaluator 内双 Feeding Channel 的汇总算子未闭合；live 例 3 同款占位声明）

返回 最终 Response
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Brooding | QT-1 | @TilapiaBroodingEligibilityByQuality | @NeutralAffinity | 成熟雌鱼口孵组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Brooding 行查 @TilapiaBroodingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 三原子（无结构原子——口孵无巢语义）+ R1；BA-T2 退化绑定（单 Factor）；R-T1 + Cap 槽；R-T2 双通道绑定（例 3 既有）；QT-1。
- 放弃的自由度：(1) 幼鱼回口行为——世界侧 brood anchor 行为，不进亲鱼 Response 面；(2) 雌性个体识别——份额表达；(3) 口孵期 Cap 之下的进一步摄食动态（Story 只冻结「减少」，强度由 Profile 层）；(4) 双通道汇总数学 OPERATOR UNDEFINED。
- [需正文] 口孵期雌鱼空间偏好（常驻区方向）；@TilapiaBroodingStages 枚举成员。

BATCH_ID: REP-FULL-GUARD-001
