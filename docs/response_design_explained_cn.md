# 响应（Response）算法说明：因子判断与聚合

文档状态：**解释层（Explainer）**  
权威级别：**非规范源（non-canonical）。响应公式、阈值与样例数值的唯一权威来源是 [response_scheme_1.md](response_scheme_1.md)（方案一；其自身为 Working proposal，尚未 Promotion 为 Current Authority）**  
适用范围：方案一中因子判断与聚合部分的中文讲解；本文数值与方案一冲突时，以方案一为准。

本文只讨论响应的算法主体：

1. 输入因子有哪些；
2. 每个因子如何从实际值转成“对当前鱼、当前响应路径的契合度”；
3. 多个因子如何聚合成一条响应路径（Response Pathway）的结果；
4. 多条路径如何聚合成最终响应；
5. 策划大致需要配置什么。

不展开空间分布、机会节律（Opportunity cadence）、生成后追逐行为等其它模块。

---

# 1. 算法总览

响应的输入不是“饵的总吸引力”，而是一组已经解析好的呈现 / 线索 / 关系事实（Presentation / Cue / Relation Facts）。

算法主链如下：

```text
Canonical Facts（规范事实）
    ↓
逐条 Pathway（响应路径）读取相关因子
    ↓
每个因子计算 FactorFit（因子契合度）∈ [0,1]
    ↓
Gate（闸门）判定
    ↓
Core FactorFit（核心因子契合度）聚合
    ↓
PathwayScore（路径得分）
    ↓
多条 Pathway 取 MAX（最大值）
    ↓
Profile-wide CAP（档案级上限）
    ↓
FinalScore（最终得分）∈ [0,1]
    ↓
ResponseBand（响应档位）
    ↓
ResponseMultiplier（响应乘数）
```

最终与环境侧机会量汇合：

```text
Contribution
= EnvironmentMass × ResponseMultiplier
```

因此响应只负责回答：

> 在这次 Presentation 下，这条鱼当前有多大比例的既有机会能够真正转化为有效响应？

---

# 2. 响应使用哪些因子

底层事实按配置和阅读习惯分成 6 组。分组本身不参与计算，只用于组织输入。

| 因素组 | 具体输入 | 典型判断 |
|---|---|---|
| 目标 / 关系（Target / Relation） | `feeding_target_affinity` 等目标关系 | 目标是否被该鱼认可 |
| 视觉（Visual） | `apparent_size`、`visual_contrast`、`flash` | 大小、显著度、闪光是否契合 |
| 运动 / 节奏（Motion / Tempo） | `speed`、`speed_change`、`direction_change`、`pause_duration`、`vertical_motion` | 运动速度、变速、变向、停顿和垂向运动是否契合 |
| 振动（Vibration） | `vibration_amplitude`、`vibration_frequency` | 振动强度、频率是否契合 |
| 声学（Acoustic） | `sound_amplitude`、`sound_pattern` | 声音强度和模式是否契合 |
| 接触（Contact） | `contact_disturbance` | 撞底、碰结构等接触扰动是否契合 |

`Activity`（活跃度）、`FeedingMotivation`（摄食动机）不归入上述正向吸引因子：

- 活跃度更适合参与某些路径的可行性判断；
- 摄食动机更适合限制整个摄食模式（Feeding Mode）的最高响应。

距离、遮挡、传播等物理问题也不在响应中再次计算；它们应该先被解析进局地线索（Cue），例如更远距离对应更弱的局地振动或更小的表观大小（apparent size）。

---

# 3. 因子契合度（FactorFit）：每个因子先独立判断“契合度”

每条路径使用的输入，先通过一个评估器（evaluator）得到：

```text
FactorFit ∈ [0,1]
```

定义为：

```text
Fit(p, j)
= Eval(
    当前事实值 x_j,
    当前 Species × EngagementMode × Pathway 对该因子的参数
  )
```

关键点是：**因子契合度是按路径区分的（Pathway-specific）。**

同一个输入值，在不同路径中可以得到不同契合度（Fit）。

例如：

```text
speed = 0.8 m/s
```

可能得到：

```text
STEADY_PREY.speed_fit = 0.85
NATURAL_DRIFT.speed_fit = 0.20
FLEEING_PREY.speed_fit = 0.55
```

因此不存在一张全局的：

```text
0.8 m/s → attraction = 0.7
```

真正存在的是：

```text
0.8 m/s
在某条鱼的某条 Pathway 中
→ 当前 SpeedFit
```

---

# 4. 常用因子评估器（Factor Evaluator）

第一版不需要为每个因子提供任意函数。大部分输入可以用少量通用评估器表达。

## 4.1 偏好区间（Preferred Range）

适合有“最佳范围”的因子：

```text
apparent_size
speed
vibration_frequency
pause_duration
```

典型形状：

```text
过低       最佳区        过高
 0 ──↗────── 1 ──────↘── 0
```

可以用 4～6 个关键点或“最佳区 + 两侧衰减区”配置。

例如：

```text
speed:
  0.1 m/s → 0.1
  0.4 m/s → 0.7
  0.7 m/s → 1.0
  1.0 m/s → 0.8
  1.5 m/s → 0.2
```

---

## 4.2 至少达到（At Least）：达到一定强度后趋于饱和

适合强度型触发：

```text
speed_change
flash
contact_disturbance
vibration_amplitude
sound_amplitude
```

典型形状：

```text
太弱        有效       饱和
 0 ─────↗───────↗────── 1
```

例如：

```text
contact_disturbance:
  < 0.2 → 0
  0.4   → 0.5
  0.7   → 1.0
  > 0.7 → 1.0
```

达到足够强度后不继续无限增加。

---

## 4.3 至多不超过（At Most）：越弱越契合

适合自然漂流、轻微动作等不宜过强的路径。

例如：

```text
speed_change:
  0.0 → 1.0
  0.2 → 0.8
  0.5 → 0.3
  0.8 → 0
```

---

## 4.4 枚举 / 关系映射（Enum / Relation Map）

适合：

```text
feeding_target_affinity
sound_pattern
某些方向 / 类型枚举
```

例如：

```text
feeding_target_affinity:
  IGNORE    → 0.0
  SECONDARY → 0.5
  CORE      → 1.0
```

具体映射值可以统一，也可以由路径 / 模板（Template）参数化。

---

# 5. 各因子通常如何判断

下面给出第一版建议的默认评估器类型。它们是默认建模方式，不意味着同一因子在所有路径中只能使用一种评估器。

| 因子 | 默认判断方式 | 备注 |
|---|---|---|
| feeding target affinity | 枚举 / 关系映射 | 目标关系 |
| apparent size | 偏好区间 | 过大、过小都可能不合适 |
| visual contrast | 至少达到 或 偏好区间 | 高对比并非所有路径都越高越好 |
| flash | 至少达到 | 达到有效程度后饱和 |
| speed | 偏好区间 | 不同路径的最佳速度不同 |
| speed change | 至少达到 / 至多不超过 | jerk 与 natural drift 方向相反 |
| direction change | 至少达到 / 枚举 | reaction 型路径常看变化幅度 |
| pause duration | 偏好区间 / 至少达到 | jerk-pause 可能需要最小停顿，也可能存在过长失效 |
| vertical motion | 偏好区间 / 枚举 | 视路径判断上行、下沉、幅度 |
| vibration amplitude | 至少达到 / 偏好区间 | 某些鱼可能存在过强惩罚 |
| vibration frequency | 偏好区间 | 频率通常更适合区间型偏好 |
| sound amplitude | 至少达到 / 偏好区间 | 视路径决定是否存在过强问题 |
| sound pattern | 枚举映射 | 模式匹配 |
| contact disturbance | 至少达到 | 反应性触发为主 |

配置的核心不是给“视觉”“运动”整组打一个分，而是给当前路径真正使用的具体因子配置评估器。

---

# 6. 一条响应路径由哪些因子参与

每条路径对因子只定义三种角色：

```text
GATE
CORE
IGNORE
```

## 6.1 闸门（GATE）

闸门只决定：这条路径当前能不能成立。

例如：

```text
FLEEING_PREY
Gate:
  target_affinity >= ACCEPTABLE
  activity >= PURSUIT_MIN
```

任何闸门失败：

```text
PathwayScore = 0
```

闸门不进入后面的因子契合度聚合。

---

## 6.2 核心（CORE）

核心因子是真正参与该路径强度计算的因子。

例如：

```text
STEADY_PREY
Core:
  target_fit
  apparent_size_fit
  speed_fit
```

它们各自得到 `[0,1]` 的因子契合度，再聚合成一个核心契合度（CoreFit）。

---

## 6.3 忽略（IGNORE）

当前路径不读取该因子。

例如 `STEADY_PREY` 可以完全忽略接触扰动（contact disturbance）；`CONTACT_REACTION` 也可以完全忽略表观大小（apparent size）。

`IGNORE` 不等于契合度为 0，而是不参与计算。

---

# 7. 路径内部聚合：核心因子使用几何平均

对于通过闸门的路径，核心因子（Core Factor）使用无权几何平均：

```text
CoreFit_p
= (Fit_1 × Fit_2 × ... × Fit_n) ^ (1/n)
```

也可以写成：

```text
CoreFit_p
= exp(
    average(ln(Fit_j))
  )
```

若任一核心因子契合度为 0：

```text
CoreFit_p = 0
```

### 示例

```text
TargetFit = 1.00
SizeFit   = 0.80
SpeedFit  = 0.60
```

则：

```text
CoreFit
= (1.00 × 0.80 × 0.60) ^ (1/3)
≈ 0.783
```

如果 SpeedFit 从 0.60 提升到 1.00：

```text
CoreFit
= (1.00 × 0.80 × 1.00) ^ (1/3)
≈ 0.928
```

因此每一个核心因子都持续影响结果，同时任一因子掉到 0 都会使整条路径失效。

---

# 8. 路径上限（PathwayCeiling）：控制一条路径最高能给多少响应

每条路径配一个：

```text
PathwayCeiling ∈ [0,1]
```

然后：

```text
PathwayScore_p
= PathwayCeiling_p × CoreFit_p
```

例如：

```text
BASELINE_PREY ceiling = 0.35
STEADY_PREY   ceiling = 0.70
JERK_PAUSE    ceiling = 1.00
```

如果 `BASELINE_PREY` 的所有核心契合度都是 1：

```text
PathwayScore = 0.35
```

它也不会超过自己的上限。

路径上限用来区分：

- 基础接受；
- 正常有效策略；
- 强触发策略。

---

# 9. 多条路径之间如何聚合：取最大值（MAX）

同一条鱼在同一个机会（Opportunity）中可以同时满足多条路径。

例如：

```text
BASELINE_PREY     = 0.35
STEADY_PREY       = 0.58
JERK_PAUSE        = 0.91
CONTACT_REACTION  = 0.34
```

最终正向得分（PositiveScore）：

```text
PositiveScore
= MAX(0.35, 0.58, 0.91, 0.34)
= 0.91
```

这里不做：

```text
0.35 + 0.58 + 0.91 + 0.34
```

因此多识别出几条路径不会自动提高响应；最终使用当前最强的有效响应路径。

如果确实需要表达“两种机制同时存在才更强”，则建立一条明确的组合路径（Combined Pathway），例如：

```text
TRACKING_DEFLECTION
```

它单独计算自己的因子契合度和路径得分，再参与最大值聚合。

---

# 10. 档案级上限（Profile-wide CAP）：最后再处理模式级上限

某些状态不是某一条路径的局部条件，而是对整个中鱼习性模式（EngagementMode）都成立的上限。

例如摄食动机可以形成：

```text
FeedingMotivation → CapScore ∈ [0,1]
```

最终：

```text
FinalScore
= MIN(
    PositiveScore,
    all applicable ProfileWideCaps
  )
```

例如：

```text
PositiveScore = 0.91
FeedingCap    = 0.60
```

则：

```text
FinalScore = 0.60
```

活跃度若只限制追击，则放在追击类路径的闸门中，而不是做全局上限。

---

# 11. 最终得分如何转成响应档位（ResponseBand）

算法内部先得到连续的：

```text
FinalScore ∈ [0,1]
```

再量化成当前响应档位：

```text
NONE
LOW
NORMAL
HIGH
```

方案一默认量化阈值（方案一 §11）：

```text
0             → NONE
(0, 0.40)     → LOW
[0.40, 0.75)  → NORMAL
[0.75, 1.00]  → HIGH
```

再统一映射为响应乘数（ResponseMultiplier），方案一暂时沿用已有校准种子（Calibration Seed，方案一 §12）：

```text
NONE   → 0.00
LOW    → 0.25
NORMAL → 0.50
HIGH   → 1.00
```

最终：

```text
Contribution
= EnvironmentMass × ResponseMultiplier
```

档位阈值和乘数是校准参数；它们不改变上面的因子契合度 / 路径聚合结构。

---

# 12. 原子姿态与分子姿态同时存在时怎么处理

响应不直接给姿态名称配置吸引分。

例如识别层同时得到：

```text
JERK
PAUSE
JERK_PAUSE
```

不会计算：

```text
JERK score
+ PAUSE score
+ JERK_PAUSE bonus
```

而是先解析成规范事实（canonical facts）：

```text
JERK
→ speed_change
→ direction_change
→ vibration_amplitude

PAUSE
→ pause_duration
→ speed state
```

同一个物理原因、同一个语义端点（semantic endpoint）只保留一次结果。

随后路径使用这些去重后的事实计算因子契合度。

例如：

```text
JERK_PAUSE Pathway
Core:
  target_fit
  speed_change_fit
  pause_duration_fit
```

也就是说：

```text
姿态识别
→ canonical facts
→ FactorFit
→ PathwayScore
```

姿态层本身不额外叠加吸引系数（attraction coefficient）。

---

# 13. 一个完整数值例

假设某鱼的摄食剖面（Feeding Profile）中有四条路径。

当前事实经过各自评估器后得到：

```text
TargetFit       = 1.00
SizeFit         = 0.80
SteadySpeedFit  = 0.70
SpeedChangeFit  = 0.95
PauseFit        = 0.80
ContactFit      = 0.20
DirectionFit    = 0.60
```

所有相关闸门均通过。

## BASELINE_PREY

```text
Core:
  TargetFit = 1.00

Ceiling = 0.35

CoreFit = 1.00
PathwayScore = 0.35
```

## STEADY_PREY

```text
Core:
  TargetFit      = 1.00
  SizeFit        = 0.80
  SteadySpeedFit = 0.70

CoreFit
= (1.00 × 0.80 × 0.70)^(1/3)
≈ 0.824

Ceiling = 0.70

PathwayScore
= 0.824 × 0.70
≈ 0.577
```

## JERK_PAUSE

```text
Core:
  TargetFit      = 1.00
  SpeedChangeFit = 0.95
  PauseFit       = 0.80

CoreFit
= (1.00 × 0.95 × 0.80)^(1/3)
≈ 0.913

Ceiling = 1.00

PathwayScore = 0.913
```

## CONTACT_REACTION

```text
Core:
  ContactFit   = 0.20
  DirectionFit = 0.60

CoreFit
= sqrt(0.20 × 0.60)
≈ 0.346

Ceiling = 1.00

PathwayScore = 0.346
```

多路径聚合：

```text
PositiveScore
= MAX(
    0.35,
    0.577,
    0.913,
    0.346
  )
= 0.913
```

假设当前 Feeding CAP = 1：

```text
FinalScore = 0.913
```

根据默认分档（方案一 §11/§12）：

```text
FinalScore 0.913
→ HIGH
→ ResponseMultiplier = 1.00
```

---

# 14. 配置结构

策划不需要直接配置最终响应公式，而是配置四层数据。

## 14.1 全局响应配置（Global Response Config）

统一配置：档位阈值、档位到乘数的映射、默认上限类别（Ceiling class）。

例如：

```yaml
band_thresholds:
  low_upper: 0.40
  normal_upper: 0.75

band_multiplier:
  NONE: 0.00
  LOW: 0.25
  NORMAL: 0.50
  HIGH: 1.00

default_pathway_ceiling:
  baseline: 0.35
  normal: 0.70
  strong: 1.00
```

---

## 14.2 逻辑模板（LogicTemplate）/ 路径族（Pathway Family）

定义某类中鱼习性模式有哪些常用路径，以及每条路径使用哪些闸门 / 核心因子。

例如：

```yaml
template: FEEDING_PREDATION

pathways:
  - id: STEADY_PREY
    ceiling_class: normal
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - apparent_size: preferred_range
      - speed: preferred_range

  - id: JERK_PAUSE
    ceiling_class: strong
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - speed_change: at_least
      - pause_duration: preferred_range

  - id: CONTACT_REACTION
    ceiling_class: strong
    core:
      - contact_disturbance: at_least
      - direction_change: at_least
```

`ceiling_class` 的取值（baseline / normal / strong）由 14.1 全局响应配置的
`default_pathway_ceiling` 解析为具体数值（0.35 / 0.70 / 1.00），与第 8 节的示例数值
对应；配置写法以方案一 §16.2 为准。

---

## 14.3 物种 × 中鱼习性模式参数

物种主要覆盖评估器参数，而不是重写整套算法。

例如：

```yaml
species: LARGEMOUTH_BASS
mode: FEEDING

overrides:
  STEADY_PREY:
    speed:
      preferred_min: ...
      preferred_max: ...

  JERK_PAUSE:
    speed_change:
      effective_at: ...
      saturated_at: ...
    pause_duration:
      preferred_min: ...
      preferred_max: ...
```

---

## 14.4 目标关系（Target Relation）

目标类型与鱼的关系独立维护：

```yaml
feeding_target_affinity:
  BAITFISH: CORE
  CRAWFISH: CORE
  WORM: SECONDARY
  INSECT: SECONDARY
```

响应只读取已经解析好的关系（relation），而不直接读取 SKU / 具体饵 ID。

---

# 15. 算法总式

对于物种 `s`、中鱼习性模式 `m`、路径 `p`：

```text
Gate_p
= AND(all gate predicates)
```

若闸门失败：

```text
PathwayScore_p = 0
```

否则，对每个核心因子 `j`：

```text
Fit_p,j
= Eval_p,j(
    Fact_j,
    Params_s,m,p,j
  )
```

然后：

```text
CoreFit_p
= geometric_mean(Fit_p,1 ... Fit_p,n)
```

```text
PathwayScore_p
= PathwayCeiling_p × CoreFit_p
```

多路径：

```text
PositiveScore
= MAX_p(PathwayScore_p)
```

应用模式级上限：

```text
FinalScore
= MIN(
    PositiveScore,
    Cap_1,
    Cap_2,
    ...
  )
```

最后：

```text
ResponseBand
= Quantize(FinalScore)

ResponseMultiplier
= BandMultiplier(ResponseBand)
```

并进入：

```text
Contribution
= EnvironmentMass × ResponseMultiplier
```

整个算法的计算层级因此是：

```text
Fact（事实）
→ FactorFit（因子契合度）
→ PathwayScore（路径得分）
→ PositiveScore（正向得分）
→ FinalScore（最终得分）
→ ResponseBand（响应档位）
→ ResponseMultiplier（响应乘数）
```
