# 鸭嘴鲟（Paddlefish｜Polyodon spathula）｜重复刺激习惯化四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM-001（P01 普通层＝全库最大 Pattern 群 第 4 批：机会组·习惯化亚型） |
| Story | B01-S35｜鸭嘴鲟｜重复无奖励刺激的习惯化与食物恢复（census CENSUS-B1 快照全文在案）。文件名 _habituation 后缀＝Story 限定：同种 S34（幼体电感受，本批 paddlefish_electro.md）不属本文件范围 |
| 冻结 Pattern | P01（census B1 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：温和、全天活跃、滤食性、营养级 3.1（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B1 全四面判定快照） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；cue_history 输入轴；Reaction 槽 OFF） |
| census 程序 | P-B1-PAD35-RESP（TYPED 标准成员 + **cue_history 输入**——evaluator 输入 fact；状态契约 Input Contract Open→TAR-07；感觉疲劳/奖励历史/饱食需区分——Story 明言） |
| 亚结构组 | 机会组·习惯化亚型（重复无奖励刺激→响应衰减→食物恢复） |
| 待裁项携带 | cue_history 状态契约 Input Contract Open（TAR-07——census 判语原样）；感觉疲劳/奖励历史/饱食三态需区分（Story 明言，未裁） |

## 0. 上游语义与摄食形态

- 摄食形态：重复无奖励刺激的习惯化与食物恢复——Response 层 condition（census Group 面判语原样：习惯化是 Response 层 condition，不是供给拆分）。
- cue_history 输入轴（census 原样）：evaluator 的输入 fact 之一（该目标近期被呈现过且无奖励→响应衰减；食物恢复事件→重置）。这是 TYPED 族 evaluator 输入侧扩展，不是新拓扑（census 判同 TYPED 标准成员）。
- 三态区分待裁（Story 明言原样携带）：感觉疲劳（sensory fatigue）/ 奖励历史（reward history）/ 饱食（satiation）——三者对「响应衰减」的语义不同，Story 要求区分；机制侧未裁。本文件以单一 cue_history fact 占位 + 三态区分 OPEN 登记，不冒充已闭合。
- Bake 面：census NO_SURFACE_EFFECT（Static Habitat 无空间新证据）——BOUNDARY-DECL 同款显式声明形态（无 Story 派生空间程序）。
- Group 面 / Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围）。

Profile 引用清单：@PadHabituationProfile @PadNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：习惯化是 Response 层 condition）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| PadH_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签；census Bake 面判语原样：Static Habitat 无空间新证据） |
| LiveLayerProjection | Static Habitat——鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载，本 Story 不添加派生因子 |

### 2.2 中文伪脚本（完全展开）

```plain text
本 Story 无派生空间程序（显式声明）
不读取本 Story 派生的空间事实
不评价本 Story 派生的 typed 因子

鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载——
本 Story（习惯化 Response 层 condition 类）的空间语义＝Static Habitat，无新增证据行
（census 判语原样：Static Habitat 无空间新证据）
```

### 2.3 live 层投影声明

BOUNDARY-DECL 是本批显式声明形态（无程序≠省略面）；本批标签族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；cue_history 输入轴——census TYPED 标准成员扩展输入）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；cue_history 输入） | @PadNormalFeedingProfile + @PadHabituationProfile | 返回 FeedingResponse（习惯化衰减后档位） | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 当前目标的 cue_history 事实
    （该目标近期呈现次数与奖励结果——evaluator 输入 fact；
      状态契约 Input Contract Open→TAR-07——本读取行按 census 占位语义表达，
      具体 history 窗口/存储粒度归产品契约侧，不在此冻结）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实与 cue_history 事实评价 @PadNormalFeedingProfile 与 @PadHabituationProfile
    （重复无奖励刺激→响应衰减；食物恢复事件→衰减重置——Story 语义；
      感觉疲劳 / 奖励历史 / 饱食三态区分待机制侧裁决——Story 明言，本文件不冒充已闭合）
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

- 使用的自由度：R-T1 + cue_history 输入轴（TYPED 族 evaluator 输入侧扩展——census 判同在案）；BOUNDARY-DECL 显式声明标签；Profile 命名。
- 放弃的自由度：(1) cue_history 状态契约定义（Input Contract Open→TAR-07——窗口/粒度归产品契约侧）；(2) 感觉疲劳/奖励历史/饱食三态区分裁决（Story 明言待裁——归机制侧）；(3) 习惯化的 Group 化（census 判语：Response 层 condition 非供给拆分）；(4) 数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-NORM-001
