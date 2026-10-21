# Response 算法说明：因子判断与聚合

本文只讨论 Response 的算法主体：

1. 输入因子有哪些；
2. 每个因子如何从实际值转成“对当前鱼、当前响应路径的契合度”；
3. 多个因子如何聚合成一条 Response Pathway 的结果；
4. 多条 Pathway 如何聚合成最终 Response；
5. 策划大致需要配置什么。

不展开空间分布、Opportunity cadence、生成后追逐行为等其它模块。

---

# 1. 算法总览

Response 的输入不是“饵的总吸引力”，而是一组已经解析好的 Presentation / Cue / Relation Facts。

算法主链如下：

```text
Canonical Facts
    ↓
逐 Pathway 读取相关因子
    ↓
每个因子计算 FactorFit ∈ [0,1]
    ↓
Gate 判定
    ↓
Core FactorFit 聚合
    ↓
PathwayScore
    ↓
多个 Pathway 取 MAX
    ↓
Profile-wide CAP
    ↓
FinalScore ∈ [0,1]
    ↓
ResponseBand
    ↓
ResponseMultiplier
```

最终与环境侧机会量汇合：

```text
Contribution
= EnvironmentMass × ResponseMultiplier
```

因此 Response 只负责回答：

> 在这次 Presentation 下，这条鱼当前有多大比例的既有机会能够真正转化为有效响应？

---

# 2. Response 使用哪些因子

底层事实按配置和阅读习惯分成 6 组。分组本身不参与计算，只用于组织输入。

| 因素组 | 具体输入 | 典型判断 |
|---|---|---|
| Target / Relation | `feeding_target_affinity` 等目标关系 | 目标是否被该鱼认可 |
| Visual | `apparent_size`、`visual_contrast`、`flash` | 大小、显著度、闪光是否契合 |
| Motion / Tempo | `speed`、`speed_change`、`direction_change`、`pause_duration`、`vertical_motion` | 运动速度、变速、变向、停顿和垂向运动是否契合 |
| Vibration | `vibration_amplitude`、`vibration_frequency` | 振动强度、频率是否契合 |
| Acoustic | `sound_amplitude`、`sound_pattern` | 声音强度和模式是否契合 |
| Contact | `contact_disturbance` | 撞底、碰结构等接触扰动是否契合 |

`Activity`、`FeedingMotivation` 不归入上述正向吸引因子：

- `Activity` 更适合参与某些 Pathway 的可行性判断；
- `FeedingMotivation` 更适合限制整个 Feeding Mode 的最高 Response。

距离、遮挡、传播等物理问题也不在 Response 中再次计算；它们应该先被解析进局地 Cue，例如更远距离对应更弱的局地振动或更小的 apparent size。

---

# 3. FactorFit：每个因子先独立判断“契合度”

每个被 Pathway 使用的输入，先通过一个 evaluator 得到：

```text
FactorFit ∈ [0,1]
```

定义为：

```text
Fit(p, j)
= Eval(
    当前事实值 x_j,
    当前 Species × Engagement Mode × Pathway 对该因子的参数
  )
```

关键点是：**FactorFit 是 Pathway-specific 的。**

同一个输入值，在不同 Pathway 中可以得到不同 Fit。

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

# 4. 常用 Factor Evaluator

第一版不需要为每个因子提供任意函数。大部分输入可以用少量通用 evaluator 表达。

## 4.1 Preferred Range｜偏好区间

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

## 4.2 At Least｜达到一定强度后趋于饱和

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

## 4.3 At Most｜越弱越契合

适合自然漂流、轻微动作等不宜过强的 Pathway。

例如：

```text
speed_change:
  0.0 → 1.0
  0.2 → 0.8
  0.5 → 0.3
  0.8 → 0
```

---

## 4.4 Enum / Relation Map｜离散映射

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

具体映射值可以统一，也可以由 Pathway / Template 参数化。

---

# 5. 各因子通常如何判断

下面给出第一版建议的默认 evaluator 类型。它们是默认建模方式，不意味着同一因子在所有 Pathway 中只能使用一种 evaluator。

| 因子 | 默认判断方式 | 备注 |
|---|---|---|
| feeding target affinity | Enum / Relation Map | 目标关系 |
| apparent size | Preferred Range | 过大、过小都可能不合适 |
| visual contrast | At Least 或 Preferred Range | 高对比并非所有 Pathway 都越高越好 |
| flash | At Least | 达到有效程度后饱和 |
| speed | Preferred Range | 不同 Pathway 的最佳速度不同 |
| speed change | At Least / At Most | jerk 与 natural drift 方向相反 |
| direction change | At Least / Enum | reaction 型 Pathway 常看变化幅度 |
| pause duration | Preferred Range / At Least | jerk-pause 可能需要最小停顿，也可能存在过长失效 |
| vertical motion | Preferred Range / Enum | 视 Pathway 判断上行、下沉、幅度 |
| vibration amplitude | At Least / Preferred Range | 某些鱼可能存在过强惩罚 |
| vibration frequency | Preferred Range | 频率通常更适合区间型偏好 |
| sound amplitude | At Least / Preferred Range | 视 Pathway 决定是否存在过强问题 |
| sound pattern | Enum Map | 模式匹配 |
| contact disturbance | At Least | 反应性触发为主 |

配置的核心不是给“Visual”“Motion”整组打一个分，而是给当前 Pathway 真正使用的具体因子配置 evaluator。

---

# 6. 一条 Pathway 由哪些因子参与

每条 Pathway 对因子只定义三种角色：

```text
GATE
CORE
IGNORE
```

## 6.1 GATE

Gate 只决定：这条 Pathway 当前能不能成立。

例如：

```text
FLEEING_PREY
Gate:
  target_affinity >= ACCEPTABLE
  activity >= PURSUIT_MIN
```

任何 Gate 失败：

```text
PathwayScore = 0
```

Gate 不进入后面的 FactorFit 聚合。

---

## 6.2 CORE

Core 是真正参与该 Pathway 强度计算的因子。

例如：

```text
STEADY_PREY
Core:
  target_fit
  apparent_size_fit
  speed_fit
```

它们各自得到 `[0,1]` 的 FactorFit，再聚合成一个 CoreFit。

---

## 6.3 IGNORE

当前 Pathway 不读取该因子。

例如 `STEADY_PREY` 可以完全忽略 contact disturbance；`CONTACT_REACTION` 也可以完全忽略 apparent size。

`IGNORE` 不等于 Fit=0，而是不参与计算。

---

# 7. Pathway 内部聚合：Core Factor 使用几何平均

对于通过 Gate 的 Pathway，Core Factor 使用无权几何平均：

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

若任一 Core FactorFit = 0：

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

因此每一个 Core Factor 都持续影响结果，同时任一因子掉到 0 都会使整条 Pathway 失效。

---

# 8. Pathway Ceiling：控制一条路径最高能给多少 Response

每条 Pathway 配一个：

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

如果 `BASELINE_PREY` 的所有 CoreFit 都是 1：

```text
PathwayScore = 0.35
```

它也不会超过自己的上限。

PathwayCeiling 用来区分：

- 基础接受；
- 正常有效策略；
- 强触发策略。

---

# 9. 多条 Pathway 之间如何聚合：取 MAX

同一条鱼在同一个 Opportunity 中可以同时满足多条 Pathway。

例如：

```text
BASELINE_PREY     = 0.35
STEADY_PREY       = 0.58
JERK_PAUSE        = 0.91
CONTACT_REACTION  = 0.34
```

最终正向 Response：

```text
PositiveScore
= MAX(0.35, 0.58, 0.91, 0.34)
= 0.91
```

这里不做：

```text
0.35 + 0.58 + 0.91 + 0.34
```

因此多识别出几条 Pathway 不会自动提高 Response；最终使用当前最强的有效响应路径。

如果确实需要表达“两种机制同时存在才更强”，则建立一条明确的 Combined Pathway，例如：

```text
TRACKING_DEFLECTION
```

它单独计算自己的 FactorFit 和 PathwayScore，再参与 MAX。

---

# 10. Profile-wide CAP：最后再处理模式级上限

某些状态不是某一条 Pathway 的局部条件，而是对整个 Engagement Mode 都成立的上限。

例如 FeedingMotivation 可以形成：

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

Activity 若只限制追击，则放在追击类 Pathway 的 Gate 中，而不是做全局 CAP。

---

# 11. 最终 Score 如何转成 ResponseBand

算法内部先得到连续的：

```text
FinalScore ∈ [0,1]
```

再量化成当前 ResponseBand：

```text
NONE
LOW
NORMAL
HIGH
```

方案一示例阈值：

```text
0             → NONE
(0, 0.40)     → LOW
[0.40, 0.75)  → NORMAL
[0.75, 1.00]  → HIGH
```

再统一映射为 ResponseMultiplier，例如：

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

Band 阈值和 Multiplier 是校准参数；它们不改变上面的 FactorFit / Pathway 聚合结构。

---

# 12. 原子姿态与分子姿态同时存在时怎么处理

Response 不直接给姿态名称配置吸引分。

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

而是先解析成 canonical facts：

```text
JERK
→ speed_change
→ direction_change
→ vibration_amplitude

PAUSE
→ pause_duration
→ speed state
```

同一个物理原因、同一个 semantic endpoint 只保留一次结果。

随后 Pathway 使用这些去重后的 facts 计算 FactorFit。

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

姿态层本身不额外叠加 attraction coefficient。

---

# 13. 一个完整数值例

假设某鱼的 Feeding Profile 中有四条 Pathway。

当前事实经过各自 evaluator 后得到：

```text
TargetFit       = 1.00
SizeFit         = 0.80
SteadySpeedFit  = 0.70
SpeedChangeFit  = 0.95
PauseFit        = 0.80
ContactFit      = 0.20
DirectionFit    = 0.60
```

所有相关 Gate 均通过。

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

多 Pathway 聚合：

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

根据示例分档：

```text
FinalScore 0.913
→ HIGH
→ ResponseMultiplier = 1.00
```

---

# 14. 配置结构

策划不需要直接配置最终 Response 公式，而是配置四层数据。

## 14.1 Global Response Config

统一配置：

```text
Band 阈值
Band → Multiplier 映射
默认 Ceiling class
```

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
```

---

## 14.2 LogicTemplate / Pathway Family

定义某类 Engagement Mode 有哪些常用 Pathway，以及每条 Pathway 使用哪些 Gate / Core Factor。

例如：

```yaml
template: FEEDING_PREDATION

pathways:
  - id: STEADY_PREY
    ceiling: 0.70
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - apparent_size: preferred_range
      - speed: preferred_range

  - id: JERK_PAUSE
    ceiling: 1.00
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - speed_change: at_least
      - pause_duration: preferred_range

  - id: CONTACT_REACTION
    ceiling: 1.00
    core:
      - contact_disturbance: at_least
      - direction_change: at_least
```

---

## 14.3 Species × Engagement Mode 参数

鱼种主要覆盖 evaluator 参数，而不是重写整套算法。

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

## 14.4 Target Relation

目标类型与鱼的关系独立维护：

```yaml
feeding_target_affinity:
  BAITFISH: CORE
  CRAWFISH: CORE
  WORM: SECONDARY
  INSECT: SECONDARY
```

Response 只读取已经解析好的 relation，而不直接读取 SKU / 具体饵 ID。

---

# 15. 算法总式

对于 Species `s`、Engagement Mode `m`、Pathway `p`：

```text
Gate_p
= AND(all gate predicates)
```

若 Gate 失败：

```text
PathwayScore_p = 0
```

否则，对每个 Core Factor `j`：

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

多 Pathway：

```text
PositiveScore
= MAX_p(PathwayScore_p)
```

应用模式级 CAP：

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
Fact
→ FactorFit
→ PathwayScore
→ PositiveScore
→ FinalScore
→ ResponseBand
→ ResponseMultiplier
```
