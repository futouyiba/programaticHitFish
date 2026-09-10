# 鲤（Common Carp｜Cyprinus carpio）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| Story | FISH-R02-S08｜鲤鱼｜底质翻拱与资源斑块（REP-COVERAGE-DELTA-001 #23 四面吸收判定在案：benthic prey class 绑定 + 基质/结构 Factor；翻拱扰动事实族义务同 #5/#11；Story 页正文不在本地快照 [需正文]） |
| 冻结 Pattern | P02 [需核对]（handoff 分批判别轴读法：食物载体=底泥中离散底栖猎物斑块→P02 侧，非 P06 连续基质；行级 Pattern relation 未在本地快照——live 不可达 SNAPSHOT_ONLY，README §4 登记） |
| 物种属性锚 | fish-reference-20260908 行 165：benthopelagic、肉食性（底栖无脊椎取向方向）、早晨活跃、撕鳍、potamodromous、营养级 3.06（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier B（handoff 点名 + coverage delta #23 吸收判定 + CSV 方向锚；无 census 快照、Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出——同批 Tier A 三成员（草鱼/黑鼓鱼/小口黑鲈）同形；归族裁决归 census 侧判同（README §3 登记 2） |
| 相邻文件 | field 批鲤复合体品系 L1 等效层 6 文件（koi / koi_kohaku / koi_ogon / koi_shiro_utsuri / koi_goromo / albino_mirror_carp / albino_scale_carp / leather_carp / human_face_carp——以 field 批 README 品系表为准）以本文件为本体——本文件建立后其重绑定清单随本体更新 |

## 0. 上游语义与底质翻拱形态

- 底质翻拱形态（方向）：底泥中离散底栖猎物（无脊椎）的斑块追随取食——翻拱取食行为改变局部底质并把猎物暴露于可取位置（CSV：benthopelagic、肉食性底栖取向；coverage delta #23：benthic prey class 绑定 + 基质/结构 Factor）；具体猎物构成/翻拱深度/斑块密度 [需正文]。
- **判别轴读法（P02 vs P06，[需核对]）**：本文件按 handoff 判别轴读法收录——食物载体=底泥中离散猎物斑块→P02 侧；若 Story 正文证实连续基质处理（底泥有机质连续摄入）→ P06 翻案=换 BakeTemplate 值（结构变更需重审），不是 Profile 重绑定。
- **翻拱扰动事实族义务（世界侧登记项——coverage delta #23 原文）**：同 #5/#11——鲤自身是扰动产生者（翻拱泥云/凹痕同黑鼓鱼 feeding_traces 读法：痕迹=环境 owner 保存的可见性事实，玩家搜索信息，不改鱼程序）；它鱼扰动暴露猎物（同小口黑鲈 disturbance_events 读法）为上游事实供给义务。
- Group 面：按 coverage delta #23 吸收判定无供给拆分（单一 NormalFeeding Group）；若正文出现互斥供给证据则升级重审（结构变更非 Profile 重绑定）。
- 表达超集说明：Tier B 骨架按 P02 资源斑块单因子形（census SINGLE 族）给出，仅容纳 CSV 方向+吸收判定；Story 正文到达后若判 PATCH（带 typed context）/PLAIN（多因子）/P06（连续基质）＝换 BakeTemplate 值 + 增/删行＝结构变更需重审，不是静默改写；正文判无程序语义即撤回本文件。

Profile 引用清单：@CcpBenthicPatchProfile @CcpPreyFields @CcpDietClasses @CcpSizeWindow @CcpNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；coverage delta #23 吸收判定无 Group 面缺口）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Ccp_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族骨架投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——Tier B 骨架，归族裁决移交 README §3 登记 2） |
| FactorType(typed) | resource_patch：底质翻拱底栖猎物 patch 轴 [需正文]（benthic prey class 绑定 + 基质/结构 Factor——coverage delta #23 吸收读法；猎物构成与基质偏好参数 [需正文]） |
| FactorBinding | 常年绑定 [需正文]（无 premise 切换证据；potamodromous 若正文证实洄游期切换，照 MGC/CHB 先例按 lifecycle premise 配置级处理） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@CcpPreyFields；diet_classes=@CcpDietClasses；size_window=@CcpSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot + 基质/结构 Factor + 翻拱扰动事实族（coverage delta #23 吸收读法——同 #5/#11 世界侧登记项；两层 reconciliation OPEN——README §3 登记 1） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的底栖猎物 patch 轴事实
    （底泥中离散底栖无脊椎分布——benthic prey class；
      基质/结构轴作为 Factor 侧读取 [需正文]）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@CcpPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@CcpDietClasses 食性过滤
      与 size_window=@CcpSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用底栖猎物 patch 轴事实查询 @CcpBenthicPatchProfile
    得到 BenthicPatchFit（单 typed 因子评估；
      本步为 Tier B 骨架投影——census 判同未做，EVAL_RESOURCE_PATCH
      实例化名按同批 Tier A 三成员同构预留）

NORMALIZE_WEIGHT：
    对 BenthicPatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；typed context 中间步属 PATCH 族域，多因子组合属 PLAIN 族域）

翻拱痕迹边界：本鱼翻拱产生的泥云/凹痕由环境 owner 保存并呈现给玩家——
不进入本分布程序的读取集（同黑鼓鱼读法：痕迹≠必有鱼，鱼对局部实际猎物响应）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层（BA-T1+DynamicSpatialSlot+基质/结构 Factor）reconciliation OPEN（README §3 登记 1）；Tier B 骨架的归族裁决权移交（README §3 登记 2）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 骨架投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @CcpNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 底质/猎物背景 premise（底栖背景上游 fact [需正文]）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @CcpNormalFeedingProfile
    （底栖取向接受窗参数 [需正文]——Tier B 骨架，参数级无新拓扑）
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
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；coverage delta #23 无 Quality 面缺口 |

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

- 使用的自由度：SINGLE 族骨架投影与 typed 因子实例语义（benthic prey class 绑定——coverage delta #23 吸收读法）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 归族裁决权移交（无 census 快照——Story 正文到达后 census 判同可能改判 PATCH/PLAIN/P06 翻案，结构变更需重审；正文判无程序语义即撤回本文件）；(2) 翻拱痕迹的鱼侧程序化（世界侧可见性事实——同黑鼓鱼读法）；(3) 数值与 Profile 值域不冻结；(4) 行级 Pattern relation 的确认权（live 不可达——[需核对]，README §4 登记）。
- 品系边界：field 批鲤复合体品系文件（L1 等效层）以本文件为本体单向从属——品系不新增空间程序、不新增 typed 因子；本文件结构变更时品系重绑定清单连带更新（该批先例）。

BATCH_ID: REP-FULL-P02-001
