# 银鲫（Prussian Carp｜Carassius gibelio）｜繁殖状态非持久性四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：阶段/状态组） |
| Story | FISH-R09 普通层（handoff 点名银鲫雌核；R09-FR3 摘要「银鲫判例（§6 四问非持久性）」+ R09-FR2「银鲫保守度接受」；Story 正文 [需正文]） |
| 冻结 Pattern | P05（handoff 点名；R09 FR3 判例载体；行级 Pattern 标签 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 10–20℃、最适 15℃、benthopelagic、早晨活跃、植食性（grazing on aquatic plants）、温和、potamodromous、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier B（handoff 点名 + R09 FR3 判例批注一行 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）——繁殖状态=非持久性 condition，无 Response 拓扑差异 |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与状态形态

- 状态形态：雌核生殖种群（gynogenesis——雌核发育，种群繁殖状态）+ 繁殖期行为；R09-FR3 判例「银鲫判例（§6 四问非持久性）」——**繁殖状态未通过持久性四问，判非持久性 condition**：不购买 FishGroup、不拆供给、不进 Response 拓扑（R09-FR2「银鲫保守度接受」=保守表达被接受）。判例原文细节（§6 四问逐条）未在本地快照，[需正文]。
- Group 面：繁殖状态非持久性 → 单一 NormalFeeding Group；种群繁殖组成（雌核种群雌性占比等）=世界侧事实/Profile 值域，不程序化。
- Bake 面：植食性底质处理（CSV：grazing on aquatic plants）——SINGLE 骨架容纳方向；繁殖期若有空间偏好差异，落 premise 值域。
- Response 面：R-T1 骨架（植食取向接受窗参数方向——CSV 锚）；繁殖期响应强度若变化=Profile 参数（Cap 形态若产品要求），无拓扑差异证据。
- 表达超集说明：Tier B 骨架按非持久性状态单因子形给出；正文到达后若判持久性状态（升级 FishGroup）＝结构变更需重审；正文判无程序语义即撤回本文件。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，CSV 方向级推导 [需正文]）**：判断链＝premise 读取（繁殖状态配置级——非持久性 condition 落值域不落结构）→ 植食资源带档位归属三档 → 归一化。推导来源＝CSV grazing on aquatic plants 方向锚（Tier B 无行级证据，链序为样板语义方向级还原，档位成员 [需正文]）。分级命中：资源带三档（水草/附着带充分=全额/稀草过渡带=削减不清零/无草带=出局 EARLY_RETURN）；early return 的对象=格子，不是繁殖状态（PREMBIND 不变量维持；繁殖期空间偏好差异若有=落 premise 值域）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@PrussianCarpReproductiveStateSpatialProfile @PrussianCarpPreyFields @PrussianCarpDietClasses @PrussianCarpSizeWindow @PrussianCarpNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；R09-FR3 判例：繁殖状态四问未过持久性门槛=非持久性 condition，不购买 FishGroup）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| PrussianCarp_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（繁殖状态未通过持久性四问＝非持久性 condition——R09-FR3 判例：
不购买 FishGroup、不拆供给；种群繁殖组成=世界侧事实，不进本面）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影骨架）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——归族裁决归 census 侧判同；**§2.2 已顺序还原（REP-ORDER-FIX-003）：资源带档位归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：植食资源位置轴（水草/底质附着带——CSV grazing on aquatic plants 方向；具体构成 [需正文]） |
| FactorBinding | lifecycle premise：繁殖状态配置级切换（非繁殖/繁殖期值域切换——非持久性 condition 落值域不落结构；值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @PrussianCarpReproductiveStateSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@PrussianCarpPreyFields；diet_classes=@PrussianCarpDietClasses；size_window=@PrussianCarpSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@PrussianCarpReproductiveStateSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（繁殖状态配置级——非持久性 condition 落值域）→ 植食资源带
档位归属三档 → 归一化；档位判定分级命中（水草带充分=全额/稀草过渡带=削减不清零/
无草带=出局 EARLY_RETURN）。繁殖状态切换本身不进 body 分支（PREMBIND 不变量维持：
非持久性 condition 落值域不落结构，R09-FR3 判例读法）；early return 的对象是格子，
不是繁殖状态。推导来源=CSV grazing on aquatic plants 方向锚（方向级，
档位成员 [需正文]）；档位成员=Profile 值域不冻结。与 census SINGLE 族 canonical
两步（无 gate 判语）的拓扑分歧登记 README §7（census 侧受影响族重跑=work
standards §5.4 行动项）。

读取 当前格子的位置轴事实（植食资源带位置轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@PrussianCarpPreyFields 绑定的水草/附着 prey class 生物量，
      经 diet_classes=@PrussianCarpDietClasses 食性过滤
      与 size_window=@PrussianCarpSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（繁殖状态——上游事实，配置级切换因子值域；
    本 body 只按 premise 取 Profile 值域，不含状态分支）

第 1 步 植食资源带档位归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @PrussianCarpReproductiveStateSpatialProfile 的资源带分档槽
    （水草/底质附着带构成 [需正文]；档位成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 水草带充分档（preferred 槽——植食资源充分）：
        ReproductiveStateSpatialFit = 全额
    否则如果 ∈ 稀草过渡带（tolerated 槽）：
        ReproductiveStateSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（无草带——无植食资源）：
        返回 0（EARLY_RETURN：无草带的格子出局——CSV 锚方向级推导 [需正文]，
        若正文证实底栖无脊椎等替代资源带则档位成员调整，结构变更需重审）

第 2 步 NORMALIZE_WEIGHT：
    对 ReproductiveStateSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live 吸收读法=BA-T1 底板 + DynamicSpatialSlot=@PrussianCarpReproductiveStateSpatialProfile（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影骨架）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @PrussianCarpNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @PrussianCarpNormalFeedingProfile（植食取向接受窗——CSV 方向锚；
    繁殖期强度若变化=Profile 参数，无拓扑差异证据）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@PrussianCarpNormalFeedingProfile 值域不冻结；
    繁殖状态非持久性——档位结构不随繁殖状态切换，R09-FR3 判例保守读法）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（繁殖状态非持久性——无 Response 拓扑差异购买，R09-FR3 判例保守读法）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；种群繁殖组成不进品质程序体（世界侧事实） |

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

- 使用的自由度：SINGLE 族投影标签；typed 因子实例语义（植食资源带方向）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：资源带档位归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) 雌核生殖种群状态程序化（=世界侧事实/Profile 值域，不进任何面程序体）；(3) 繁殖状态 FishGroup 升级（R09-FR3 判例非持久性——若正文证实持久性状态，结构变更需重审）；(4) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结（含资源带/档位成员）。
- [需正文] R09 判例 §6 四问逐条（本地仅摘要一行）、繁殖期空间偏好（若有）、Response 接受窗参数方向、植食资源带构成。
- [需核对] Story DB 行级 Pattern 标签。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 资源带档位归属三档+early return 链，Response 档位展开）
