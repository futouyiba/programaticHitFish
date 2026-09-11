# 白斑狗鱼（Northern Pike｜Esox lucius）｜淹水草地繁殖位移四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | B01-S19｜白斑狗鱼｜淹水草地繁殖与回深水（census CENSUS-B2 快照全文在案）。文件名 _spawn 后缀＝Story 限定：同种另两条 census Story（B01-S20 捕获段 P01 / B01-S18 植被伏击）不属本文件范围 |
| 冻结 Pattern | P05（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 10–28℃、最适 19℃、pelagic、深 0–30m、晨昏活跃、肉食性、追猎、potamodromous、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-PIK19-BAKE（SINGLE 族成员：位置因子随 spawning_stage premise 配置切换）+ P-B2-PIK19-RESP（TYPED 族标准成员） |

## 0. 上游语义与洄游形态

- 洄游形态：繁殖位移（早春淹水草地浅滩产卵↔回深水，spawning_stage 驱动）；Spawning aggregation≠Guard≠互斥 Group（census Group 面判语原样：NO_SURFACE_EFFECT——聚集语义不购买供给拆分）。
- Bake 面：位置因子单链 spawning_stage premise 绑定（census P-B2-PIK19-BAKE：位置因子随 spawning_stage premise 配置切换；SINGLE 族成员）。
- Response 面：TYPED 族标准成员（产卵聚集不证明更强取食——census 判语原样：参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 与 Active Spawning 投影先例的关系：live「Active Spawning Representation Projection R0」给出产卵 Group 的 R-T1 Cap Slot（live 先例的 ActiveSpawningFeedingCap 槽）形态——**该投影的大口黑鲈产卵语义（Active Spawning Group+摄食 Cap）与本 Story 的白斑狗鱼判定（无 Group，位置因子 premise 切换）不同判定层**；census 侧判本 Story 无供给拆分，本文件按 census 判定表达，Active Spawning Group 形态作为表达层替代读法登记（§2.3），不冒充本 Story 判定。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，census 冻结语义层推导）**：判断链＝premise 读取（spawning_stage 配置级）→ 繁殖阶段绑定位置轴段归属三档 → 归一化。推导来源＝census P-B2-PIK19-BAKE 冻结实例常量（位置因子随 spawning_stage premise 配置切换——盲体 sketch 语义的档位化还原；Tier A 骨架在案，档位成员不在快照——段成员 [需正文]）。分级命中：轴段三档（当前阶段偏好带=全额——PRESPAWN 淹水草地浅滩带↔POSTSPAWN 深水结构带随 premise 取段/近岸过渡带=削减不清零/对侧带=出局 EARLY_RETURN）；early return 的对象=格子，不是繁殖阶段（PREMBIND 不变量维持——产卵聚集语义不购买供给拆分，census Group 面判语原样）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@PikeSpawnStageSpatialProfile @PikePreyFields @PikeDietClasses @PikeSizeWindow @PikeNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——Spawning aggregation≠Guard≠互斥 Group）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| PikeSpawn_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；**§2.2 已顺序还原（REP-ORDER-FIX-003）：繁殖轴段归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：繁殖位置轴（淹水草地浅滩↔深水；typed 实例，spawning_stage 驱动——census P-B2-PIK19-BAKE 实例常量） |
| FactorBinding | lifecycle premise：spawning_stage 配置级切换（PRESPAWN 淹水草地↔POSTSPAWN 回深水；值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @PikeSpawnStageSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@PikePreyFields；diet_classes=@PikeDietClasses；size_window=@PikeSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@PikeSpawnStageSpatialProfile（handoff 指定读法；Active Spawning Group+Cap 替代读法见 §2.3；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（繁殖阶段配置级）→ 繁殖阶段绑定位置轴段归属三档 → 归一化；
轴段判定分级命中（当前阶段偏好带=全额/近岸过渡带=削减不清零/对侧带=出局
EARLY_RETURN）。繁殖阶段切换本身不进 body 分支（PREMBIND 不变量维持：
spawning_stage=上游繁殖事实，配置级切换因子集）；early return 的对象是格子，
不是繁殖阶段。推导来源=census P-B2-PIK19-BAKE 冻结实例常量（盲体 sketch 语义的
档位化还原——Tier A 骨架在案、档位成员不在快照，段成员 [需正文]）；档位成员=
Profile 值域不冻结。与 census SINGLE 族 canonical 两步（无 gate 判语）的拓扑分歧
登记 README §7（census 侧受影响族重跑=work standards §5.4 行动项）。

读取 当前格子的位置轴事实（淹水草地浅滩↔深水繁殖轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@PikePreyFields 绑定的鱼类 prey class 生物量，
      经 diet_classes=@PikeDietClasses 食性过滤
      与 size_window=@PikeSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（spawning_stage——上游繁殖事实，配置级切换因子集；
    本 body 只按 premise 取 Profile 轴段值，不含繁殖阶段分支）

第 1 步 繁殖阶段绑定轴段归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用位置轴事实查询 @PikeSpawnStageSpatialProfile 的阶段轴段分档槽
    （轴=淹水草地浅滩↔深水两态随 spawning_stage 取段；段成员与阈值=Profile 值域不冻结 [需正文]）
    如果 格子位置 ∈ 当前阶段偏好带（preferred 槽——PRESPAWN 淹水草地浅滩带/
        POSTSPAWN 深水结构带方向）：
        SpawnStageSpatialFit = 全额
    否则如果 ∈ 近岸过渡带（tolerated 槽）：
        SpawnStageSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（对侧带——当前阶段不取的轴段）：
        返回 0（EARLY_RETURN：格子不在当前繁殖阶段空间范围，出局）

第 2 步 NORMALIZE_WEIGHT：
    对 SpawnStageSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live 吸收读法=BA-T1 底板 + DynamicSpatialSlot=@PikeSpawnStageSpatialProfile（§11.4/§11.6 Prespawn Staging 先例：MERGE_PLAUSIBLE→BA-T1，NEW_TEMPLATE_NOT_PROVEN）。**替代读法登记**：live「Active Spawning Projection R0」的产卵 Group（GR 分流+R-T1 Cap Slot，即 live 先例的 ActiveSpawningFeedingCap 槽）是同语义的 Group 面表达层选择（coverage #3 罗非鱼判例同构）——census 侧判本 Story 无供给拆分，两读法的取舍归 census↔live 两层 reconciliation（README §3 登记 1/2），本文件不闭合。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @PikeNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @PikeNormalFeedingProfile（产卵聚集不证明更强取食——census 判语原样；档位参数级）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@PikeNormalFeedingProfile 值域不冻结；
    产卵聚集不改变档位结构——census 判语在档位层的读法）：
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
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；census Quality 面 NO_SURFACE_EFFECT |

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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（繁殖位置轴 spawning_stage 绑定——census 冻结实例常量）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：繁殖轴段归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) Active Spawning Group+Cap 表达层选择（census 判无供给拆分；替代读法登记 §2.3，取舍归两层 reconciliation）；(3) Spawning aggregation Group 化（census 判语：≠Guard≠互斥 Group）；(4) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(5) 数值与 Profile 值域不冻结（含轴段/档位成员）。
- Story 限定：本文件只表达 S19；S20 横咬捕获段（P01，post-instantiation OUT_OF_SCOPE）与 S18 植被伏击（另 Story）不在此承载。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 繁殖轴段归属三档+early return 链，Response 档位展开）
