# 电鳗（Electric Eel｜Electrophorus electricus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| Story | FISH-R05-电鳗-Electrogenic-Remote-Prey-Control 的 S6 段（雄鱼筑泡沫巢护幼）；Story 主 Pattern=无 registry 关系（New Pattern Candidate「Attacker-Generated Opportunity」已残核化）——护巢程序由 CENSUS-B0-REV-001 F-1 补录驱动 |
| census 程序 | P-EEL-RESP-GUARD（Response，GUARD_CONFLICT_DUAL_PATH_RESPONSE 族第三成员；**CENSUS-B0-FIX-001 非盲补录**——创建时 registry/canonical 已知，同构预期本身是被审对象，bias_declaration 在案） |
| 冻结 Pattern | P04 语义（S6 泡沫巢雄护；同 Bluegill/Smallmouth 先例受理） |
| 物种属性锚 | fish-reference-20260908：水温 23–28℃、最适 25.5℃、benthopelagic、夜间活跃、孤僻（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录，2026-09-10 版；census CENSUS-B0 / CENSUS-B0-FIX-001 归档） |
| 证据档 | Tier A（census 补录程序在案；非盲补录声明照录） |
| 变体声明 | 条件原子 V1；条件组合 R1；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | Guarding=Defense-only（live V0）；NormalFeeding=R-T1 单通道（Feeding，电感知 cue 轴并入） |

## 0. 上游语义与护巢形态

- 护巢形态：雄鱼筑泡沫巢护幼（MALE_FOAM_NEST_GUARD，persistent condition）；nest_anchor = foam_nest（泡沫巢 relation object）（census FIX-001 补录 premise）。
- 补录纪律声明（原样照录）：本程序为修复轮非盲补录（driver：独立审 F-1 EEL S6/S9 覆盖缺口）；程序形状自冻结 Story 证据重建，由 reviewer 复检覆盖 fit 风险。
- 非护巢期：S9 幼成食性切换（幼体食无脊椎、成体食鱼及小哺乳）＝P01 typed 摄食故事（P-EEL-RESP-FEEDING，TYPED 族），不在本批主题内；本文件 NormalFeeding 面直接绑定该 typed evaluator。
- 电感知轴（跨批资产）：电鳗对呈现的电场感知 cue 轴已由 REP-CUE-AXIS-001 立项（@ElectroFieldProfile，unary + FIXED_COMBINE 并入既有通道）；本文件 NormalFeeding Response 消费该轴，不重复规格。
- census ↔ live 表达分歧（同 oscar.md §0 条目）：census S6 body 为双路径（DUAL_PATH）；live V0 为 Defense-only。本文件表达 live V0；COMBINE_DUAL_PATH 数学 OPERATOR UNDEFINED，待机制侧。
- 互斥状态：guard_state ∈ {NONE, MALE_FOAM_NEST_GUARD}。

Profile 引用清单：@EelSpawnWindowStart @EelSpawnWindowEnd @EelGuardWarmupDays @EelGuardTempThreshold @EelFoamNestSiteStructureSet @EelGuardingShare @EelLocalGuardAnchorEligibility @EelFoamNestSuitabilityProfile @EelGuardRelationProfile @EelGuardLocalTemperatureProfile @EelGuardThreatProfile @EelStillwaterProfile @EelStructureProfile @EelPreyResourceProfile @EelNormalTimeProfile @EelNormalTempFloor @EelNormalFeedingProfile @ElectroFieldProfile @EelGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：存在

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| EE1 | C1 | 当前日期 | — | BETWEEN | @EelSpawnWindowStart | @EelSpawnWindowEnd |
| EE1 | C2 | 连续均温 | @EelGuardWarmupDays | >= | @EelGuardTempThreshold | — |
| EE1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @EelFoamNestSiteStructureSet | — |
| EE1 | C4 | 巢体存在事实 | — | == | 存在 | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| EelGuardEligible | AND | 1 | Condition | EE1.C1 |
| EelGuardEligible | AND | 2 | Condition | EE1.C2 |
| EelGuardEligible | AND | 3 | Condition | EE1.C3 |
| EelGuardEligible | AND | 4 | Condition | EE1.C4 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Eel_Guard_Route | @EelGuardEligible | Guarding | Species 内行为份额 | @EelGuardingShare |
| Eel_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
读取 连续均温（窗口=@EelGuardWarmupDays 天）
读取 当前钓场结构集合
读取 泡沫巢存在事实（上游 GuardAnchor Resolver 产出）

如果：
    当前日期处于 [@EelSpawnWindowStart, @EelSpawnWindowEnd]
    并且 连续均温 >= @EelGuardTempThreshold
    并且 场内结构集合 CONTAINS_ANY @EelFoamNestSiteStructureSet
    并且 巢体存在事实 == 存在

则：
    GuardingShare = @EelGuardingShare

否则：
    GuardingShare = 0

SpecialShareTotal = GuardingShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）

NormalFeedingShare = 1 - SpecialShareTotal

返回 GuardingShare / NormalFeedingShare
```

Share 语义：live §7 契约。C3（筑巢基质资格）与 C4（巢体已建成）不重复结算：C3 判场内是否有合法泡沫巢位结构，C4 判雄鱼泡沫巢这一 guard premise 已持续存在。

## 2. Bake

### 2.1 Guarding Group｜配置表（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorEligibilityRule | @EelLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | foam_nest（泡沫巢，单一实例） |
| GuardAnchorRelationProfile | @EelGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @EelFoamNestSuitabilityProfile |
| LocalTemperatureProfile | @EelGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

### 2.2 Guarding Group｜中文伪脚本（完全展开）

```plain text
读取 当前目标的结构 / 水深 / 岸缘关系
读取 当前目标与泡沫巢锚点的关系（距离 / 朝向）
读取 当前点局部温度

如果当前目标不满足 @EelLocalGuardAnchorEligibility：
    返回 极低 / 0 空间权重（early return）

用当前目标与泡沫巢锚点的关系查询 @EelGuardRelationProfile
得到 RelationFit

用当前目标的静水浅洼结构查询 @EelFoamNestSuitabilityProfile
得到 AnchorSuitabilityFit

用当前点局部温度查询 @EelGuardLocalTemperatureProfile
得到 LocalTempFit

合并 RelationFit / AnchorSuitabilityFit / LocalTempFit
算子标注：OPERATOR UNDEFINED — 待机制侧（Guard 模式 Bake 多 Factor 合并算子；live §15.3 同款占位声明）

返回 Guarding SpatialDistributionWeight
```

### 2.3 NormalFeeding Group｜配置表（BA-T1 Independent Factor Set；HARD_GATED 族成员——P-EEL-BAKE 判例：必要硬门 + 因子组合）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-EEL-GATED-FACTORS（census HARD_GATED_FACTOR_COMBINE 族成员；门语义=水面可达型硬约束，HRQ-02 队列在案） |
| StructureProfile | @EelStructureProfile（静水 / 沼泽结构因子） |
| StillwaterProfile | @EelStillwaterProfile（静水偏好因子） |
| PreyResourceProfile | @EelPreyResourceProfile（猎物资源因子：成体食鱼及小哺乳方向） |
| TimeProfile | @EelNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @EelNormalTempFloor |
| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED — 待机制侧） |

注：census P-EEL-BAKE 的具体硬门内容（水面可达 / 气呼吸约束）属该程序本体；本表按族绑定并保留 HRQ-02 引用，硬门槽位语义以 census 归档为准 [需核对：P-EEL-BAKE 硬门字段名]。

### 2.4 NormalFeeding Group｜中文伪脚本

```plain text
读取 当前结构（静水 / 沼泽掩体）
读取 当前点静水 / 流速事实
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

用结构查询 @EelStructureProfile 得到 StructureFit
用静水事实查询 @EelStillwaterProfile 得到 StillwaterFit
用猎物资源查询 @EelPreyResourceProfile 得到 PreyFit
用时段查询 @EelNormalTimeProfile 得到 TimeFit

如果 当前点水温 < @EelNormalTempFloor：
    返回 极低空间权重（early return）

合并 StructureFit / StillwaterFit / PreyFit / TimeFit
算子标注：OPERATOR UNDEFINED — 待机制侧（BA-T1 因子合并算子，无顺序依赖）

返回 SpatialDistributionWeight
```

## 3. Response

### 3.1 配置表（例 1C 形态；模板=RR-DEFENSE-01 / live §17.5 RR-T2 Defense-only，结构族 R-T1 单通道 Channel=Defense）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @EelGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；电感知 cue 轴并入） | @EelNormalFeedingProfile + @ElectroFieldProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

Guarding Group：

```plain text
读取 当前 Presentation 与泡沫巢锚点的关系
读取 侵入距离、持续时间、威胁 Cue

评价 @EelGuardThreatProfile
得到 DefenseResponse

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

边界注记：主动放电 / 远程麻痹＝Encounter / Conversion owner（REP-CUE-AXIS-001 §2 排除表 + FISH-R05-FR3-001R owner 分解）；Defense Response 只承载「对侵入者的关系性响应」，不承载放电捕获结果语义。

NormalFeeding Group：

```plain text
读取 当前饵 / Presentation Cue（尺寸、速度、轨迹、水层与相对位置）
读取 当前拟饵 / 环境电场特征（LureElectricField——REP-CUE-AXIS-001 轴事实）
读取 当前动态 Feeding / Pursuit 相关事实

用 LureElectricField 查询 @ElectroFieldProfile 得到 ElectroFieldCueFit
与 @EelNormalFeedingProfile 的评价结果按模板固定规则合并
算子标注：OPERATOR UNDEFINED — 待机制侧（FIXED_COMBINE 数学；REP-CUE-AXIS-001 §1 同款声明）

返回 FeedingResponse
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @EelGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼护巢组成；资格与 Response 分开（§12.6） |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；S9 幼成食性切换属 typed evaluator 参数，非品质结构 |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup

对每个品质：
    读取该品质的 GroupEligibilityFactor（Guarding 行查 @EelGuardingEligibilityByQuality；NormalFeeding 行查 @NeutralEligibility）
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

- 使用的自由度：V1 四原子（巢体存在事实==存在）+ R1；HARD_GATED 族绑定；R-T1 + 电感知轴消费（REP-CUE-AXIS-001 资产）；QT-1。
- 放弃的自由度：(1) census 双路径 body（DUAL_PATH 第三成员）→ live V0 Defense-only，分歧待机制侧；(2) 主动放电攻击语义（Encounter/Conversion owner，永不进入 Response 面）；(3) 合并算子数学 OPERATOR UNDEFINED ×2。
- 补录偏差声明（census bias_declaration）原样携带：非盲补录、同构预期本身是被审对象；本文件消费该程序时保留其 provenance。
- [需核对] P-EEL-BAKE 硬门字段名（HRQ-02 队列）；泡沫巢位结构集合成员与窗口数值由 Profile 层定值。

BATCH_ID: REP-FULL-GUARD-001
