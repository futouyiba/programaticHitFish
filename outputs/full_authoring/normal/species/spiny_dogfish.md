# 白斑角鲨（Spiny Dogfish｜Squalus acanthias）｜被动电感受摄食四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：特殊感官组） |
| Story | FISH-R07 批成员（R07 Delta Candidate ①被动电感知双例之一：**角鲨**——R07 摘要点名「被动电感知双例（角鲨+鳐——与电鳗发电端构成电场轴双向语义）」；Story 页正文与行级 Pattern 标签不在本地 [需核对]） |
| 冻结 Pattern | P01 [需核对]（R07 摘要 Delta Candidate 归层；行级标签未在本地快照） |
| 物种属性锚 | fish-reference-20260908：追猎、全天活跃、肉食性、营养级 4.37、海水（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；cue 轴资产 outputs/cue_axis_r1/） |
| 证据档 | Tier B+（R07 摘要点名锚 + cue 轴资产在案；结构按特殊感官组样板参数化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；被动电感知 cue 轴并入；Reaction 槽 OFF） |
| cue 轴资产 | @ElectroFieldProfile（REP-CUE-AXIS-001 轴；被动侧消费——与鸭嘴鲟 S34 PASSIVE_ELECTROSENSE 同侧，对照电鳗 ACTIVE 侧） |
| 亚结构组 | 特殊感官 typed（电感知——K8 cue 轴并入）＋鱼食性/体型分级维度（营养级 4.37） |
| 待裁项携带 | R07 Delta Candidate ① 的 census 判同未做（B3+ 归档后判同；本文件为表达层骨架） |

## 0. 上游语义与摄食形态

- 摄食形态：被动电感受摄食（鲨鱼洛伦兹壶腹群被动感知猎物生物电场——R07 Delta Candidate 双例之一；与电鳗发电端构成电场轴双向语义，R07 摘要原话方向）。
- 证据边界：Story 正文不在本地——本文件结构为特殊感官组样板参数化（paddlefish_electro.md 被动侧骨架）；R07 Delta 的 census 判同（B3+）到达前，本文件是表达层骨架，EEG 侧（被动电感受通道实例名）以 @ElectroFieldProfile 轴资产承载。
- Response 面：TYPED 族电感知通道（被动侧——cue 轴并入 Feeding 通道，REP-CUE-AXIS-001 同款）。
- Group 面 / Quality 面：组样板 NO_SURFACE_EFFECT。
- 表达超集说明：骨架参数化表达（Tier B+）；未超出组样板族域与 cue 轴规格范围。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier B+）**：判断链＝感官信号场档位（可探测=全额/弱信号=削减/无信号=EARLY_RETURN）→ 归一化。感官通道绑定 premise（若有）保持配置级。

Profile 引用清单：@DogBenthicForagePatchProfile @DogPreyFields @DogDietClasses @DogSizeWindow @DogElectroFeedingProfile @ElectroFieldProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Dog_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-SENSE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——感官 patch 轴实例；**§2.2 已顺序还原（REP-ORDER-FIX-004）：early return 链+分级命中，登记 README §7**） |
| FactorType(typed) | resource_patch：底层猎物 patch 轴（底层鱼类/无脊椎猎物场——方向锚 [需正文]） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@DogPreyFields；diet_classes=@DogDietClasses；size_window=@DogSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed resource factor（B-T1 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝感官信号场档位 → 归一化。感官型第一判断＝猎物信号场可探测性
（可探测丰档=全额/弱信号=削减不清零/无信号=出局 EARLY_RETURN）——感官梯度
先行是本组与机会型（丰度先行）的判据差异。顺序来源＝批内互指/点名锚方向级推导（[需正文]）——Story 正文到达后
校准（census 侧 SINGLE 族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的底层猎物 patch 轴事实
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@DogPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@DogDietClasses 食性过滤
      与 size_window=@DogSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 感官信号场档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中——
  感官型第一判断：信号场可探测性先行）：
    用该轴事实查询 @DogBenthicForagePatchProfile 的信号场分档槽
    （底层猎物 patch 轴·底层鱼类/无脊椎猎物场——方向锚 [需正文]；档位成员=Profile 值域不冻结 [需正文]）
    如果 信号场 ∈ 可探测丰档（preferred 槽）：
        BenthicForageFit = 全额
    否则如果 ∈ 弱信号档（tolerated 槽）：
        BenthicForageFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（无信号档）：
        返回 0（EARLY_RETURN：无可探测猎物信号的格子出局——感官型信号先行判据）

第 2 步 NORMALIZE_WEIGHT：
    对 BenthicForageFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；被动电感知 cue 轴并入）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；被动电感知 cue 轴并入） | @DogElectroFeedingProfile + @ElectroFieldProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前拟饵 / 环境电场特征（LureElectricField——REP-CUE-AXIS-001 轴事实；
  被动感知侧——与鸭嘴鲟 S34 同侧，对照电鳗主动放电侧；
  产品电呈现输入契约未定 TAR-07——按轴占位消费）

EVAL_TARGET_AS_FOOD_TYPED（被动电感受通道并入 Feeding）：
    用目标事实与电场特征评价 @DogElectroFeedingProfile
    与 @ElectroFieldProfile 的评价结果按模板固定规则合并
    算子标注：OPERATOR UNDEFINED — 待机制侧（FIXED_COMBINE 数学；REP-CUE-AXIS-001 §1 同款声明）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@DogElectroFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（恒为 NormalFeeding——无 Special Group）

对每个品质：
    读取该品质的 GroupEligibilityFactor（查 @NeutralEligibility）
    读取该品质的 GroupAffinityFactor（查 @NeutralAffinity）
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

- 使用的自由度：SENSE-SINGLE 投影标签与 typed 因子实例语义（底层猎物 patch——方向锚）；@ElectroFieldProfile cue 轴资产被动侧消费（REP-CUE-AXIS-001）。
- 放弃的自由度：(1) 归族裁决权移交（R07 Delta ① 的 census 判同 B3+ 未做——判同到达可能改判/补充通道实例名，结构变更需重审）；(2) Story 正文语义（[需正文]——猎物构成/电感知细节到达后只填 Profile 值域）；(3) 产品电呈现契约定义（TAR-07）；(4) 合并算子数学（OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 信号场可探测档三档分级命中 EARLY_RETURN，Response DECIDE 档位展开）
