# 黑鼓鱼（Black Drum｜Pogonias cromis）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| Story | B01-S46｜黑鼓鱼｜翻底坑与泥云作为持续觅食痕迹（census CENSUS-B1-DRU 快照全文在案；Story 页 3d6a4137d236815b9313c3005b469749） |
| 冻结 Pattern | P02（census B1 stories.jsonl 快照 frozen_patterns） |
| 物种属性锚 | fish-reference-20260908 行 66：demersal、肉食性、晨昏活跃、孤僻、oceanodromous、营养级 3.38（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结 P-B1-DRU-BAKE/P-B1-DRU-RESP；REP-COVERAGE-DELTA-001 #5 四面吸收判定在案） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-DRU-BAKE（SINGLE 族成员：factor=resource_patch(benthic_prey)；盲体首步 op=EVAL_RESOURCE_PATCH）+ P-B1-DRU-RESP（TYPED 标准成员：P02 底栖取向） |
| 防混淆注记 | 黑鼓鱼（Black Drum，Sciaenidae）≠ 乌鳢/黑鱼（Snakehead——normal2 批排除表类 0 另行登记的鱼）≠ 红鼓鱼（red_drum.md，normal2 批，同科不同种）；三鱼名近，判定不互推 |

## 0. 上游语义与底栖斑块形态

- 摄食形态：分布跟随底栖猎物资源 patch（翻底觅食）→ 归一化权重（census 盲体 sketch 原样）；P02 判别轴：食物载体=离散底栖猎物斑块。
- **痕迹三层归属（泥云/翻底凹痕——本鱼种行为产物）**：(1) 对玩家=搜索线索（可见痕迹提示此处有翻底活动）；(2) 对鱼程序=痕迹可见性，环境 owner 保存与呈现；(3) 对分布程序=不改鱼程序——鱼仍对局部实际猎物响应，**痕迹≠必有鱼**（census owner 推论原样：痕迹持续不必变成 Mode 或 FieldFeeding）。
- Group 面：census NO_SURFACE_EFFECT 原样（Story Competing：痕迹持续不必变成 Mode 或 FieldFeeding）。
- Response 面：TYPED 标准成员（P02 底栖取向——参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT（**存在痕迹不能保底生成个体**——Story 判语原样，见 §4）。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@DruBottomForagerProfile @DruPreyFields @DruDietClasses @DruSizeWindow @DruNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：痕迹持续不必变成 Mode 或 FieldFeeding）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Dru_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——本标签本批 4 文件之一） |
| FactorType(typed) | resource_patch：底栖猎物 patch 轴（census P-B1-DRU-BAKE 实例常量 resource="benthic_prey"；benthic prey class 绑定——REP-COVERAGE-DELTA-001 #5 吸收读法） |
| FactorBinding | 常年绑定（无 lifecycle/season premise 切换证据） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@DruPreyFields；diet_classes=@DruDietClasses；size_window=@DruSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot + 痕迹可见性事实 feeding_traces（世界侧；§11.4 浑水先例——REP-COVERAGE-DELTA-001 #5 吸收读法；两层 reconciliation OPEN——README §3 登记 1） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的底栖猎物 patch 轴事实（底栖无脊椎分布——benthic_prey_field 上游 fact）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@DruPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@DruDietClasses 食性过滤
      与 size_window=@DruSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用底栖猎物 patch 轴事实查询 @DruBottomForagerProfile
    得到 BottomForagerFit（单 typed 因子评估；
      census 盲体首步 op=EVAL_RESOURCE_PATCH——族判同的实例化名，同构）

NORMALIZE_WEIGHT：
    对 BottomForagerFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；typed context 中间步属 PATCH 族域，多因子组合属 PLAIN 族域）

痕迹边界：翻底凹痕/泥云（feeding_traces）由环境 owner 保存并呈现给玩家——
不进入本分布程序的读取集（鱼对局部实际猎物响应，痕迹≠必有鱼）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层（BA-T1+DynamicSpatialSlot+痕迹可见性事实）reconciliation OPEN（README §3 登记 1）；痕迹的玩家可见性是 live §11.4 浑水先例的槽位语义，不是 census 族晋升。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @DruNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 底质/猎物背景 premise（benthic_context 上游 fact）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @DruNormalFeedingProfile
    （P02 底栖取向——底栖/泥底呈现的接受窗参数，参数级无新拓扑）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；census Quality 面 NO_SURFACE_EFFECT——存在痕迹不能保底生成个体（Story 判语：痕迹是行为产物不是个体密度凭证） |

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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（resource_patch(benthic_prey)——census 冻结实例常量原样）；Profile 命名；伪脚本步序（canonical 两步固定）；痕迹归属的三层拆分（census owner 推论照录）。
- 放弃的自由度：(1) 痕迹驱动的 Mode/FieldFeeding 化（census 判语：痕迹持续不必变成 Mode 或 FieldFeeding）；(2) 痕迹进鱼分布程序的读取集（世界侧可见性事实——玩家搜索信息不改鱼程序）；(3) 痕迹保底生成个体（Quality 判语：存在痕迹≠个体密度凭证）；(4) 数值与 Profile 值域不冻结；(5) PATCH↔SINGLE optional_context 边界（HRQ-B1-02）与 census↔live 两层 reconciliation 的裁决权（归机制侧）。

BATCH_ID: REP-FULL-P02-001
