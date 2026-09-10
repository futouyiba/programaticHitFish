# 小口黑鲈·跟随翻底觅食（Smallmouth Bass｜Micropterus dolomieu）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| Story | B01-S32｜小口黑鲈｜跟随翻底动物获取被惊出的猎物（census CENSUS-B1-SMA 快照全文在案；Story 页 3d6a4137d23681deb3a9c69b5ed3d5ad）。同种另 Story C07 护巢/护幼已由 guarding 批 smallmouth.md 承载（该文件相邻故事行显式留位本 Story 摄食面）——双文件分工互指，本文件不重复护巢面 |
| 冻结 Pattern | P02（census B1 stories.jsonl 快照 frozen_patterns） |
| 物种属性锚 | fish-reference-20260908 行 119：benthopelagic、肉食性、晨昏活跃、好斗、营养级 3.56（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结 P-B1-SMA-BAKE/P-B1-SMA-RESP；REP-COVERAGE-DELTA-001 #11 四面吸收判定在案） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）——census 程序体无 Reaction 步；coverage delta #11 的 Reaction 通道读法两层登记见 §3/§5 |
| census 程序 | P-B1-SMA-BAKE（SINGLE 族成员：factor=resource_patch(disturbance_revealed)；盲体首步 op=EVAL_RESOURCE_PATCH）+ P-B1-SMA-RESP（TYPED 标准成员：被惊出猎物取向，P02） |

## 0. 上游语义与扰动跟随形态

- 摄食形态：跟随扰动觅食——动态机会 patch 评估（它鱼/它动物翻底扰动暴露的猎物区）→ 归一化权重（census 盲体 sketch 原样）；P02 判别轴：食物载体=离散猎物斑块（扰动暴露的动态机会斑块）。
- 扰动事件归属：disturbance_events=它鱼/它动物翻底扰动事件与暴露猎物区（世界侧 fact，环境 owner 产生——扰动者改变局部猎物可达性，鱼对实际猎物响应；census owner 推论原样）；resolver_tests 登记（世界侧事实供给义务，与 coverage_delta report §5b 同源）。
- **跟随的否定判定（census Group 判语原样）**：跟随≠RelationalConflict、动物翻底不自动购买 Field Mode（Story Competing）。
- 两层登记（Response 面）：coverage delta #11 的吸收读法含「Reaction 通道（erratic 触发，§17.2）」——live 层 RR-T1 的 Optional Reaction 槽读法；census 程序体（P-B1-SMA-RESP，TYPED 12 标准成员之一）无 Reaction 步。本文件按 census 程序体表达（R-T1 OFF），两层 reconciliation OPEN——README §3 登记 2。
- Group 面：census NO_SURFACE_EFFECT。
- Response 面：TYPED 标准成员（被惊出猎物取向——参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围；Reaction 通道读法作为 live 层投影登记，未程序化）。

Profile 引用清单：@SmaDisturbanceFollowerProfile @SmaPreyFields @SmaDietClasses @SmaSizeWindow @SmaNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：跟随≠RelationalConflict、动物翻底不自动购买 Field Mode）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Sma_Follow_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| FactorType(typed) | resource_patch：扰动暴露猎物动态机会 patch 轴（census P-B1-SMA-BAKE 实例常量 resource="disturbance_revealed_prey"；disturbance_events=世界侧事实供给义务，resolver_tests 登记） |
| FactorBinding | 常年绑定（无 lifecycle/season premise 切换证据） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@SmaPreyFields；diet_classes=@SmaDietClasses；size_window=@SmaSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot + 上游扰动事件/斑块事实（coverage delta #11 吸收读法；两层 reconciliation OPEN——README §3 登记 1） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的扰动暴露猎物动态机会 patch 轴事实
    （disturbance_events——它鱼/它动物翻底扰动事件与暴露猎物区；
      世界侧 fact，环境 owner 产生：扰动者改变局部猎物可达性）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@SmaPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@SmaDietClasses 食性过滤
      与 size_window=@SmaSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用扰动暴露猎物机会轴事实查询 @SmaDisturbanceFollowerProfile
    得到 DisturbanceFollowerFit（单 typed 因子评估；
      census 盲体首步 op=EVAL_RESOURCE_PATCH——族判同的实例化名，同构）

NORMALIZE_WEIGHT：
    对 DisturbanceFollowerFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；typed context 中间步属 PATCH 族域，多因子组合属 PLAIN 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层（BA-T1+DynamicSpatialSlot+扰动事件事实）reconciliation OPEN（README §3 登记 1）；跟随≠RelationalConflict（无关系性 Group/Response 购买）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @SmaNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 暴露猎物背景 premise（revealed_prey_context 上游 fact）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @SmaNormalFeedingProfile
    （被惊出猎物取向——扰动背景下的食物评价参数：
      被惊出猎物的暴露/逃窜呈现特征并入食物评价输入，参数级无新拓扑）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
（census 程序体（P-B1-SMA-RESP，TYPED 标准成员）无 Reaction 步——按 census 表达；
  coverage delta #11 的 live 层 Reaction 通道读法（erratic 触发，live §17.2 RR-T1
  Optional Reaction 槽）两层 reconciliation OPEN——本文件不静默选择任一层，见 §5）
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（resource_patch(disturbance_revealed)——census 冻结实例常量原样）；Profile 命名；伪脚本步序（canonical 两步固定）；扰动事件的世界侧归属（census owner 推论照录）。
- 放弃的自由度：(1) 跟随的 RelationalConflict 化与 Field Mode 购买（census 判语：跟随≠RelationalConflict、动物翻底不自动购买 Field Mode）；(2) Reaction 通道的程序化（census 程序体无 Reaction 步——coverage delta #11 的 live 层 erratic 读法两层 reconciliation OPEN，不在本文件闭合）；(3) 数值与 Profile 值域不冻结；(4) PATCH↔SINGLE optional_context 边界（HRQ-B1-02）与两层 reconciliation 的裁决权（归机制侧）。
- 与 guarding 批 smallmouth.md（C07 护巢，P04 GUARD 族域）零耦合：本文件只表达 B01-S32 摄食面（P02），Group/Response 程序不共享；两文件判定不互推。

BATCH_ID: REP-FULL-P02-001
