# 草鱼（Grass Carp｜Ctenopharyngodon idella）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| Story | B01-S53｜草鱼｜植食资源与预投饵斑块（census CENSUS-B1-GRB 快照全文在案；Story 页 3d6a4137d23681168a18f10342e09a94） |
| 冻结 Pattern | P02（census B1 stories.jsonl 快照 frozen_patterns；handoff 要求核对的行级 Pattern relation——快照层冻结在案，live 行级 SNAPSHOT_ONLY 见 README §4） |
| 物种属性锚 | fish-reference-20260908 行 185：benthopelagic、植食性、早晨活跃、温和、potamodromous、营养级 2（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结 P-B1-GRB-BAKE/P-B1-GRB-RESP） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-GRB-BAKE（SINGLE 族首成员：resource_patch 轴首实例，factor=resource_patch(plant+prebait)；盲体首步 op=EVAL_RESOURCE_PATCH，族判同实例化名）+ P-B1-GRB-RESP（TYPED 标准成员：面包/玉米取向参数） |
| 相邻文件 | field 批 albino_grass_carp.md（白化草鱼 L1 等效层）以本文件为本体——本文件建立后其重绑定清单随本体更新（单向从属，见该文件 §5） |

## 0. 上游语义与资源斑块形态

- P02 判别轴（本批口径）：食物载体=**离散资源斑块**（Resource Patch→Discrete Target→TargetFeeding），对照 P06=连续基质处理——判别轴=食物载体（离散斑块 vs 连续基质），非栖息带或食性。
- 资源构成：植食资源+预投饵斑块双构成（census 盲体实例常量 resource="aquatic_plant+bait_patch"，原样）。
- **关键判别（预投饵斑块 vs 自然资源斑块——handoff 点名）**：census 判定两者为**同一 Bake 形态**——同族（SINGLE）同轴（factor_type=resource_patch）同一因子实例；差异不在鱼程序结构，而在**世界侧事实供给层**：prebait_patches（玩家预投饵行为产生的资源斑块）是世界侧事实供给义务（环境资源 owner 保存；census resolver_tests 登记，与 coverage_delta report §5b 同源），自然资源斑块（水草植食资源）同为上游事实。玩家行为产生资源斑块不购买新 Bake 结构、不购买 Mode/Group。
- Group 面：census NO_SURFACE_EFFECT 原样（Story Competing 明言：饵区鱼多不证明必须 Group；P02：Patch 不自动购买 Mode/Group）。
- Response 面：TYPED 标准成员（P02 语义=patch 背景下离散 TargetFeeding；面包/玉米取向参数——参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。
- **判断顺序（REP-ORDER-FIX-001 顺序还原）**：判断链＝斑块存在性 → 斑块质量档位 → 归一化。顺序推导来源：census 盲体 sketch「分布跟随植食资源与预投饵斑块」＋P02 判别轴（食物载体=离散资源斑块——**斑块追随程序的先验是斑块存在**：无斑块格不产生追随分布，存在性先行）；质量评估展开为三档分级命中（最适应=全额/可接受=削减不清零/排除=出局），档位成员与阈值全 Profile 值域不冻结。斑块双构成（水生植物/预投饵）同源评估——来源差异在世界侧事实供给层（§0 关键判别），不购买档位分叉。CSV 时段（早晨活跃）锚未入链（无 Story 空间程序证据）。

Profile 引用清单：@GrbHerbivorePatchProfile @GrbPreyFields @GrbDietClasses @GrbSizeWindow @GrbNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：饵区鱼多不证明必须 Group，P02 Patch 不自动购买 Mode/Group）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Grb_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——本标签本批 4 文件之一；**§2.2 已顺序还原（REP-ORDER-FIX-001）：early return 链+分级命中，分歧登记 README §7**） |
| FactorType(typed) | resource_patch：植食资源+预投饵斑块轴（census P-B1-GRB-BAKE 实例常量 resource="aquatic_plant+bait_patch"；预投饵斑块 prebait_patches=世界侧事实供给义务，resolver_tests 登记非鱼程序结构） |
| FactorBinding | 常年绑定（无 lifecycle/season premise 切换证据） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@GrbPreyFields；diet_classes=@GrbDietClasses；size_window=@GrbSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot（live §11.4 预投饵先例——玩家投放资源斑块的槽位语义；两层 reconciliation OPEN——README §3 登记 1） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-001】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝斑块存在性 → 斑块质量档位 → 归一化；分级命中（全额/削减/出局），
出局即 EARLY_RETURN。P02 斑块追随程序的先验=斑块存在（无斑块格不产生追随分布）；
存在性先行是 census sketch「分布跟随植食资源与预投饵斑块」的行为判断序还原
（canonical 计算序 EVAL_TYPED_FIELD_OR_FACTOR 单步在此展开为存在门+质量档两步）。
顺序差异本身=LogicTemplate 判据，与 census canonical body（无 gate 判语）的拓扑分歧
登记 README §7（census 侧 SINGLE 族重跑=work standards §5.4 行动项）。

读取 当前格子的植食资源+预投饵斑块轴事实
    （双构成：水生植物资源事实 + prebait_patches 玩家预投饵斑块事实——
      两者同为世界侧上游事实；预投饵斑块的保存与衰减归环境资源 owner；
      双构成同源评估——来源差异在世界侧事实供给层，不购买档位分叉）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@GrbPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@GrbDietClasses 食性过滤
      与 size_window=@GrbSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 斑块存在性（GATE_PATCH_PRESENCE）：
    用斑块轴事实查询 @GrbHerbivorePatchProfile 的存在分档槽
    如果 本格无植食资源斑块且无预投饵斑块（excluded 槽——零斑块）：
        返回 0（EARLY_RETURN：无斑块格不参与斑块追随分布）
    否则：
        进入第 2 步

第 2 步 斑块质量档位（EVAL_TYPED_FIELD_OR_FACTOR，分级命中）：
    用斑块质量事实查询 @GrbHerbivorePatchProfile
    （census 盲体首步 op=EVAL_RESOURCE_PATCH——族判同的实例化名，同构；
      单 typed 因子评估展开为三档分档槽=Profile 值域不冻结）
    如果 斑块质量 ∈ 最适应档（preferred 槽）：
        HerbivorePatchFit = 全额强度
    否则如果 斑块质量 ∈ 可接受档（tolerated 槽）：
        HerbivorePatchFit = 削减强度（× Profile 衰减参数——削减但不清零）
    否则（斑块存在但质量近零档）：
        返回 0（EARLY_RETURN：质量排除档出局）

第 3 步 NORMALIZE_WEIGHT：
    对 HerbivorePatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本程序。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，BakeTemplate 投影标签
不因此静默改写——换标签/改结构=census 族重跑裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层（BA-T1+DynamicSpatialSlot）reconciliation OPEN（README §3 登记 1）；预投饵斑块的 §11.4 先例是 live 侧槽位语义，不是 census 族晋升。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @GrbNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 局部食物背景 premise（resource_context 上游 fact——patch 背景参数）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @GrbNormalFeedingProfile
    （面包/玉米等饵取向参数——census 盲体实例常量 bait="bread/corn"；
      P02 语义：patch 背景下的离散目标食物评价，参数级无新拓扑）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-001 展开）：
    按三档判定 FoodEvaluation（档位成员=@GrbNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档：
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（resource_patch(plant+prebait)——census 冻结实例常量原样）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-001：斑块存在性先行、质量三档分级命中、early return 链——推导依据 §0 判断顺序行）**；预投饵资源的世界侧归属层选择（census 判语照录——事实供给义务非鱼程序结构）；Bake 输入契约字段复用。
- 放弃的自由度：(1) 饵区聚集的 Group 化（census 判语：饵区鱼多不证明必须 Group，Patch 不自动购买 Mode/Group）；(2) 预投饵斑块的鱼侧程序化（世界侧事实供给义务——玩家投放语义不进鱼 Bake/Response 结构；live §11.4 槽位归属两层 reconciliation OPEN）；(3) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(4) 双构成（水草/预投饵）的档位分叉（同源评估——来源差异在世界侧事实供给层）；(5) 水温/时段因子入链（CSV 锚无 Story 空间程序证据）；(6) 数值与 Profile 值域不冻结（含档位成员与阈值）；(7) PATCH↔SINGLE optional_context 边界（HRQ-B1-02）与 census↔live 两层 reconciliation 的裁决权（归机制侧）。
- CSV 习性锚（早晨活跃/温和/potamodromous）仅方向锚；potamodromous 若 Story 正文证实洄游期因子切换，照 MGC/CHB 先例按 lifecycle premise 配置级处理，不购买 Migration Group。

BATCH_ID: REP-FULL-P02-001
顺序还原修复批次：REP-ORDER-FIX-001（§0/§2/§3/§5 修改；Bake 伪脚本 early return 链+分级命中，Response 档位展开）
