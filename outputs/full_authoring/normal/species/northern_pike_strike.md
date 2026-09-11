# 白斑狗鱼（Northern Pike｜Esox lucius）｜横咬捕获阶段四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：捕获边界组） |
| Story | B01-S20｜白斑狗鱼｜横咬、转向吞咽与捕获阶段（census CENSUS-B1 快照全文在案）。文件名 _strike 后缀＝Story 限定：同种 S19（繁殖位移 P05，migration 批 northern_pike_spawn.md）与 S18（植被伏击，本批 northern_pike_ambush.md）不属本文件范围 |
| 冻结 Pattern | P01（census B1 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：水温 10–28℃、最适 19℃、pelagic、晨昏活跃、肉食性、追猎、淡水/半咸水（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B1 全四面判定快照） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF）；Response 语义＝仅初次接受 |
| census 程序 | P-B1-PIK-RESP（TYPED 标准成员；取饵后处理/保留/Hook=交互实例 owner OUT_OF_SCOPE） |
| 亚结构组 | 捕获边界型（capture boundary——R07「Capture Boundary 首次成轴」已证 2 例之二）＋鱼食性/体型分级维度 |
| 显式越界声明 | out_of_scope（census 原样）：横咬/转向吞咽/捕获阶段（post-instantiation） |

## 0. 上游语义与摄食形态

- 摄食形态：横咬初次接受边界（TargetFeeding 只解释最初接受——取饵成立即本面结束）。横咬后转向吞咽、捕获阶段是 post-instantiation 交互实例，owner=Encounter/Conversion/Contact 侧。
- Bake 面：census NO_SURFACE_EFFECT（StoryDomain=Capture Boundary+Ordinary Feeding；S20 无空间新证据——植被伏击空间语义属 S18 另一条 Story，本批 northern_pike_ambush.md 承载）——本文件 Bake 面为显式无 Story 派生程序声明形态（本批 BOUNDARY 标签）。
- Group 面 / Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

- **判断顺序（REP-ORDER-FIX-004 顺序还原）**：顺序还原不适用（无程序面）——本面为 BOUNDARY-DECL 显式声明形态，无 Story 派生程序可排序；顺序还原只作用于有程序面的 Bake 伪脚本（见 §2.2 显式声明）。Response 面档位展开照常适用。

Profile 引用清单：@PikNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Pik_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签；census Bake 面判语原样：S20 无空间新证据——植被伏击属 S18 另一条 Story；**顺序还原不适用（无程序面——REP-ORDER-FIX-004）**） |
| LiveLayerProjection | Static Habitat——鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载，本 Story 不添加派生因子 |

### 2.2 中文伪脚本（完全展开）

```plain text
本 Story 无派生空间程序（显式声明）
不读取本 Story 派生的空间事实
不评价本 Story 派生的 typed 因子

鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载——
本 Story（横咬捕获阶段类）的空间语义＝Static Habitat，无新增证据行
（植被伏击空间语义属 S18——由本批 northern_pike_ambush.md 承载，两文件不重复）

顺序还原不适用（无程序面）——REP-ORDER-FIX-004：本面无 Story 派生程序可排序
（BOUNDARY-DECL 显式声明形态；顺序还原只作用于有程序面的 Bake 伪脚本）
```

### 2.3 live 层投影声明

BOUNDARY-DECL 是本批显式声明形态（无程序≠省略面）；本批标签族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影——初次接受语义）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；仅初次接受） | @PikNormalFeedingProfile | 返回 FeedingResponse（初次接受档位） | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @PikNormalFeedingProfile
    得到 FoodEvaluation（TargetFeeding 只解释最初接受）

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@PikNormalFeedingProfile 值域不冻结——（仅初次接受：横咬取饵成立即本面结束））：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

后续阶段（转向吞咽/捕获处理/保留）不在本面评价——post-instantiation 交互实例，
owner=Encounter/Conversion/Contact 侧（census out_of_scope 原样）

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

- 使用的自由度：BOUNDARY-DECL 显式声明标签；R-T1 初次接受语义参数；Profile 命名。
- 放弃的自由度：(1) 横咬后阶段程序化（post-instantiation owner=交互实例侧，census out_of_scope 原样）；(2) 植被伏击空间语义（属 S18——同种异 Story 分文件先例，与 migration 批 northern_pike_spawn.md 三文件互指不重复）；(3) 数值与 Profile 值域不冻结。
- 同种三 Story 分工（S18/S19/S20 三文件三批）在 README §3 登记 6 互指闭合。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 顺序还原不适用（无程序面），Response DECIDE 档位展开）
