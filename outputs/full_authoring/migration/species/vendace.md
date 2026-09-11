# 欧白鲑（Vendace｜Coregonus albula）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：洄游组） |
| Story | FISH-R02-S04｜欧白鲑｜冷水湖泊的底层/水层切换（census CENSUS-B2 快照全文在案） |
| 冻结 Pattern | P05（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 1.6–3.6℃、最适 2.6℃、benthopelagic、深 30m+、晨昏活跃、滤食性（selective plankton feeding）、撕鳍性格标注、anadromous 名义行（本鱼经典分布为冷水湖泊群——湖泊种群水层切换为主语义；行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照 + 盲程序体冻结） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B2-VEN-BAKE（SINGLE 族成员：水层因子 temp/season 绑定，与 B1 蓝鳃水层同型）+ P-B2-VEN-RESP（TYPED 族标准成员） |

## 0. 上游语义与洄游形态

- 洄游形态：冷水湖泊水层切换（底层↔水层，temp/season 驱动）；水层差异先作 Spatial/Condition（census Group 面判语原样：NO_SURFACE_EFFECT，不购买 FishGroup）。
- Bake 面：水层因子单链（census P-B2-VEN-BAKE：水层因子 temp/season 绑定；SINGLE 族成员，与 B1 蓝鳃季节水层同型先例）。
- Response 面：TYPED 族标准成员（离散钩饵 target）；CSV 滤食性（浮游选择摄食）与 Story 判定「水层切换」共存——摄食取向参数归 @VendaceNormalFeedingProfile 值域；若后续 Story 证实场摄食（滤食浮游场语义），Response 族判定需 P03 域复核（census FOOD_FIELD_FEEDING_RESPONSE 族先例：鳙鱼/大西洋鲱），本文件不预购买。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，census 冻结语义层推导）**：判断链＝premise 读取（temp/season 配置级）→ 季节绑定水层归属三档 → 归一化。推导来源＝census P-B2-VEN-BAKE 冻结实例常量（水层因子 temp/season 绑定，与 B1 蓝鳃季节水层同型——盲体 sketch 语义的档位化还原；Tier A 骨架在案，档位成员不在快照——段成员 [需正文]）。与北极红点鲑链同构但轴类型不同（垂直水层轴 vs 水平近岸↔深水轴——同族成员同构正常，轴语义差异归 Profile 值域）。分级命中：水层三档（当前季节偏好水层=全额——冷水期底层↔暖季水层随 premise 取段/过渡层=削减不清零/对侧水层=出局 EARLY_RETURN）；early return 的对象=格子，不是季节（PREMBIND 不变量维持）。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@VendaceLayerSpatialProfile @VendacePreyFields @VendaceDietClasses @VendaceSizeWindow @VendaceNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——水层差异先作 Spatial/Condition）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Vendace_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；**§2.2 已顺序还原（REP-ORDER-FIX-003）：水层归属三档+early return 链，分歧登记 README §7**） |
| FactorType(typed) | habitat_factor：水层因子（底层↔水层；typed 实例，temp/season 驱动——census P-B2-VEN-BAKE 实例常量；与 B1 蓝鳃季节水层同型） |
| FactorBinding | lifecycle premise：temp/season 配置级切换（冷水期底层↔暖季水层；值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @VendaceLayerSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@VendacePreyFields；diet_classes=@VendaceDietClasses；size_window=@VendaceSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@VendaceLayerSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝premise 读取（季节配置级）→ 季节绑定水层归属三档 → 归一化；水层判定分级命中
（当前季节偏好水层=全额/过渡层=削减不清零/对侧水层=出局 EARLY_RETURN）。季节切换本身
不进 body 分支（PREMBIND 不变量维持：temp/season=上游 premise，配置级切换因子集）；
early return 的对象是格子，不是季节。推导来源=census P-B2-VEN-BAKE 冻结实例常量
（盲体 sketch 语义的档位化还原——Tier A 骨架在案、档位成员不在快照，段成员 [需正文]）；
档位成员=Profile 值域不冻结。与 census SINGLE 族 canonical 两步（无 gate 判语）的拓扑
分歧登记 README §7（census 侧受影响族重跑=work standards §5.4 行动项）。

读取 当前格子的水层事实（底层↔水层冷水季节轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@VendacePreyFields 绑定的浮游/无脊椎 prey class 生物量，
      经 diet_classes=@VendaceDietClasses 食性过滤
      与 size_window=@VendaceSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（temp/season——上游事实，配置级切换因子集；
    本 body 只按 premise 取 Profile 水层段值，不含季节分支）

第 1 步 季节绑定水层归属（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用水层事实查询 @VendaceLayerSpatialProfile 的季节水层分档槽
    （垂直水层轴=底层↔水层两态随季节取段；档位成员与阈值=Profile 值域不冻结 [需正文]）
    如果 水层 ∈ 当前季节偏好水层（preferred 槽——冷水期底层/暖季水层方向）：
        LayerSpatialFit = 全额
    否则如果 ∈ 过渡层（tolerated 槽）：
        LayerSpatialFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（对侧水层——当前季节不取的水层）：
        返回 0（EARLY_RETURN：格子不在当前季节水层范围，出局）

第 2 步 NORMALIZE_WEIGHT：
    对 LayerSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步的分歧登记 README §7；换标签/改结构=census 判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live BA 句型层无水层切换专用句型；吸收读法=BA-T1 底板 + DynamicSpatialSlot（§11.4 先例）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @VendaceNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @VendaceNormalFeedingProfile（摄食取向参数——滤食性方向的接受窗值域由 Profile 层定值）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@VendaceNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（滤食浮游场语义若后续 Story 证实为场摄食——Response 族判定需 P03 域复核
（census FOOD_FIELD 族先例），本文件按 census TYPED 判定表达不预购买）
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（水层 temp/season 绑定——census 冻结实例常量）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-003：水层归属三档+early return 链、Response 档位展开——推导依据 §0 判断顺序行）**。
- 放弃的自由度：(1) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(2) 场摄食 Response 族（FOOD_FIELD）——census 判 TYPED 标准，滤食语义若升级=族判定变更需重审；(3) 合并算子（SINGLE 链无 combine 步；OPERATOR UNDEFINED）；(4) 数值与 Profile 值域不冻结（含水层/档位成员）。
- [需核对] CSV 迁徙类型=anadromous 名义行与本 Story 湖泊水层切换语义的口径（湖封种群 vs 溯河种群——行级标签待人工核对；Whitefish 通名系行级区分见 inconnu.md §0）。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 水层归属三档+early return 链，Response 档位展开）
