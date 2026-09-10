# 虹鳟（Rainbow Trout｜Oncorhynchus mykiss）｜鼠形表面饵地域变体四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：机会组） |
| Story | B01-S24｜虹鳟｜鼠形表面饵的地域策略变体（census CENSUS-B1 快照全文在案）。同种异行「硬头鳟」（=虹鳟海型，migration 批登记项）不另建文件 |
| 冻结 Pattern | P01（census B1 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：追猎、晨昏活跃、肉食性、营养级 4.08（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B1 全四面判定快照；**absence claim 在案**——阴性样本） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-RAI-RESP（TYPED 标准成员——**阴性样本**：表面鼠形饵 context 呈现参数+地域 Profile，engine 无字面差异，无新结构；absence claim 见 census absence_claims） |
| 亚结构组 | 机会组（opportunistic）· 表面饵 context 亚型 |

## 0. 上游语义与摄食形态

- 摄食形态：鼠形表面饵的地域策略变体——地域变体＝Profile 重绑定非空间程序（census Bake 面判语原样：Static Habitat；地域变体=Profile 重绑定非空间程序）。
- 阴性样本声明（census 原样）：TYPED 标准成员，engine 无字面差异，无新结构——本文件是「地域变体不产生新模板」判例的表达层固化（absence claim 在案）。这是本批重要的负知识：地域策略差异全部落在 Profile 值域，不落在结构。
- Group 面 / Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@RaiSurfaceMouseContextProfile @RaiRegionalVariantProfile @RaiNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Rai_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；无 Story 派生空间程序显式声明）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签；census Bake 面判语原样：Static Habitat；地域变体=Profile 重绑定非空间程序） |
| LiveLayerProjection | Static Habitat——鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载；地域变体由 @RaiRegionalVariantProfile 重绑定承载，不添加派生空间因子 |

### 2.2 中文伪脚本（完全展开）

```plain text
本 Story 无派生空间程序（显式声明）
不读取本 Story 派生的空间事实
不评价本 Story 派生的 typed 因子

鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载——
地域策略变体＝Profile 重绑定（@RaiRegionalVariantProfile 值域差异），非空间程序
（census 判语原样：地域变体=Profile 重绑定非空间程序）
```

### 2.3 live 层投影声明

BOUNDARY-DECL 是本批显式声明形态（无程序≠省略面）；本批标签族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影——阴性样本）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；表面饵 context 呈现参数） | @RaiNormalFeedingProfile + @RaiSurfaceMouseContextProfile + @RaiRegionalVariantProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 目标表面呈现 context（鼠形表面饵形态/水面轨迹——呈现参数）
读取 当前地域变体 Profile（地域策略差异——Profile 重绑定，census 阴性样本判语）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实与表面呈现 context 评价 @RaiNormalFeedingProfile
    （表面鼠形饵 context＝呈现参数；地域差异＝@RaiRegionalVariantProfile 值域——
      engine 无字面差异，无新结构——census absence claim 原样）
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

- 使用的自由度：R-T1 + 呈现参数（表面鼠形饵 context）；地域变体的 Profile 重绑定（census 阴性样本判语照录）；BOUNDARY-DECL 显式声明标签。
- 放弃的自由度：(1) 地域变体的结构化（新模板/新通道——census absence claim 判语：engine 无字面差异，地域差异全部 Profile 值域）；(2) 硬头鳟异行文件（同种异行不分裂——migration 批登记项照录）；(3) 数值与 Profile 值域不冻结。
- 阴性样本定位：本文件是「地域策略变体≠新结构」判例的四面固化，供后续同型 Story（地域/亚种变体类）归族引用。

BATCH_ID: REP-FULL-NORM-001
