# FCF Simplified V0｜响应（Response）方案一
## 响应路径（Pathway）× 因子契合度（FactorFit）× MAX Resolution

> **Status:** Working Proposal / 方案一 / NOT PROMOTED  
> **Purpose:** 先形成一套完整、可实现、可讨论、可推翻的响应（Response）算法基线。  
> **Non-goal:** 本文暂不证明方案最合理、最真实或最终生产最优；数值也只作为方案一默认值。  
> **Branch:** FCF Simplified Production V0  
> **Scope:** 响应主算法、响应路径（Pathway）语义、因子（Factor）组织、原子/分子姿态去重、配置结构，以及选择（Selection）接口。

---

# 0. 为什么这版值得继续推｜候选推介（Candidate Pitch）

这不是一份“已经证明正确”的响应（Response）设计，而是一份**终于可以被系统性攻击的完整候选**。

它解决了此前最难讨论的空档：

```text
Canonical Cue 已经有了
↓
但“哪些算吸引因素？”“因素怎么合成？”“原子/分子怎么去重？”
“上限下限是什么？”“200 种鱼怎么配？”
这些问题此前仍然悬空
```

方案一的价值，不是宣称几何平均或 MAX 一定正确，而是第一次给出一条从输入到 SelectionWeight **没有空白步骤**的完整计算链：

```text
Canonical Facts
→ Pathway-specific FactorFit
→ Gate
→ Core Fit 聚合
→ PathwayScore
→ 多 Pathway Resolution
→ Profile-wide CAP
→ ResponseBand / Multiplier
→ EnvironmentMass × Response
→ fixed-pan Selection
```

它值得继续推的原因：

1. **把“吸引力”从一个模糊总分拆成可解释的玩家策略路径。** 视觉、运动、振动等不是各自加分，而是共同支撑某条具体响应路径（Response Pathway）。
2. **原子 / 分子姿态不再重复计权。** 识别（Recognition）可以多层并存，但同一个因果闭包（causal closure）只有一个机会（Opportunity）；响应消费去重后的规范事实（canonical facts）。
3. **数学是完整的。** 因子契合度（FactorFit）、路径内聚合、路径间聚合、上限（CAP）、量化、选择接口都有明确公式，可以直接写测试和反例。
4. **配置有压缩路径。** Global → LogicTemplate → Species × Mode Params → Target Relation，避免直接进入 `200 species × 13 cue × arbitrary weights`。
5. **失败方式清楚。** 几何平均、MAX、Secondary→Variant、Target Archetype→Pathway eligibility 都是显式假设；任何一个被反例击穿，都可以局部替换，不需要推翻整条架构。

换句话说，这份文档最重要的交付不是“答案”，而是：

> **把一个此前只能靠直觉争论的问题，压成一组可以手算、配置、仿真、做测试夹具（fixture）、做配置探针（authoring probe）的明确假设。**

---

## 0.1 给后续 Agent 的工作说明

你接手的是 **方案一 / Working Proposal / NOT PROMOTED**，不是当前权威（Current Authority）。

开始前：

1. 先按仓库根目录 `AGENTS.md` 执行机制文档 routing；
2. 按项目治理从 FCF Router rebase 到 Simplified Production V0 最新 Working；
3. 当前响应工作基线（Response Working baseline）是 Notion [`FCF Simplified V0｜Response Algorithm Working R0`](https://app.notion.com/p/3dea4137d2368184ac30c4aed9fe937e)；本文件是从该 Working 讨论中抽出的“方案一候选”，不得反向覆盖 Current；
4. FCF 唯一入口：[`Fish-Centric Conditional Funnel｜Start Here / Agent Router`](https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47)；
5. 不要为了让文档显得完整，把 Proposal / Open 静默改成 Confirmed。

### 推荐任务顺序

优先攻击，而不是润色：

1. **Geometric Mean Attack**：寻找“一个因素很差、另一个因素很好”的策略案例，判断几何平均是否允许了过强补偿或惩罚。
2. **MAX Across Pathways Attack**：寻找“两条中等独立响应理由同时存在，应否比单条中等更强”的真实策略案例。
3. **Pathway Granularity Attack**：用 5–8 个真实钓法故事检查响应路径（Pathway）是否过粗或爆炸。
4. **Secondary→Variant Attack**：验证是否导致组合式路径爆炸（combinatorial Pathway explosion）；若是，提出更小的算子（operator）。
5. **Target Archetype Boundary Attack**：区分目标亲和（target affinity）与路径资格（pathway eligibility），防止重复表达。
6. **Authoring Probe**：至少做 3–5 个鱼种（Species）× 2–3 个中鱼习性模式（EngagementMode），统计实际参数量、覆盖量（override）、模板复用（template reuse）。
7. 最后才做 LOW / NORMAL multiplier 与 `ρ=F/N` 校准（Calibration）。

### 修改纪律

- 保留本文件的“方案一”身份；若提出结构明显不同的替代方案，优先新建 `方案二`，不要把方案一悄悄改成另一套东西。
- 每次修改尽量附：`counterexample → affected assumption → proposed delta → new failure mode`。
- 若只是改善可读性，可直接修改本文件；若改变算法语义，要明确标出变更。
- 不要直接改运行时（Runtime）代码来“证明”某个算法合理；先用小型 fixture / notebook / standalone harness 做 disposable probe。

---

# 1. 一句话版本

响应（Response）不把视觉、速度、振动、声音等因素直接相加。

第一版采用：

```text
Canonical Facts
→ 对每条 Response Pathway 分别求 FactorFit
→ Gate 判定
→ Core FactorFit 做无权几何平均
→ 得到 PathwayScore
→ 多条 Pathway 取 MAX
→ 再受 Profile-wide CAP 封顶
→ 量化为 ResponseBand
→ 映射为 ResponseMultiplier
→ EnvironmentMass × ResponseMultiplier
```

公式：

```text
Gate_p = AND(all gate predicates)

if Gate_p == false:
    PathwayScore_p = 0
else:
    CoreFit_p
    = geometric_mean(Fit_p,1 ... Fit_p,n)

    PathwayScore_p
    = PathwayCeiling_p × CoreFit_p

PositiveScore
= MAX(PathwayScore_p)

FinalScore
= MIN(
    PositiveScore,
    all applicable ProfileWideCaps
)

ResponseBand
= Quantize(FinalScore)

ResponseMultiplier
= BandMultiplier(ResponseBand)
```

---

# 2. 核心概念

## 2.1 中鱼习性模式（EngagementMode）

响应剖面（Response Profile）的业务作用域仍然是：

```text
Species × Engagement Mode
```

例如：

```text
Largemouth Bass × Feeding
Largemouth Bass × Guarding
```

中鱼习性模式回答：

> 这条鱼当前以哪一种中鱼习性模式面对呈现（Presentation）？

它不是具体操作策略。

---

## 2.2 响应路径（Response Pathway）

响应路径回答：

> 在当前中鱼习性模式下，什么样的玩家呈现组合构成一条完整、可解释的有效响应路径？

示例：

```text
FEEDING
├─ BASELINE_PREY
├─ STEADY_PREY
├─ FLEEING_PREY
├─ JERK_PAUSE
└─ CONTACT_DEFLECTION
```

响应路径**不等于食物种类**。

例如 `baitfish / crawfish / insect` 属于目标 / 关系（Target / Relation）侧信息；它们可以影响 TargetFit、路径资格（Pathway eligibility）或具体参数，但不是天然“一种食物 = 一条响应路径”。

一个食物生态类型可以支持多条响应路径；一条响应路径也可以被多个具体食物类型复用。

---

## 2.3 路径准入（Pathway Admission）｜什么时候值得成为一条独立响应路径

方案一采用以下准入规则。

一组条件只有在满足至少一条时，才新建响应路径：

1. 对应不同的玩家操作策略；
2. 对应不同的主要触发故事；
3. 成功 / 失败时给玩家不同的可行动解释；
4. 无法仅通过已有响应路径的参数变化自然表达。

不因为数学上存在组合就新建响应路径。

拒绝：

```text
speed + flash
speed + vibration
speed + flash + vibration
speed + sound
...
```

除非这些组合真的对应不同玩家策略故事。

建议每个中鱼习性模式的第一版响应路径数量控制在约 3～6 条；这只是方案一的生产约束，不是领域真理。

---

# 3. 响应因素（Response Factors）

方案一把响应输入组织成 6 个策划侧因素组。

这些是**配置编写 / UI 分组（Authoring / UI Group）**，不是 6 个独立运行时得分（Runtime Score）。

| 因素组 | 典型规范输入（canonical） | 回答的问题 |
|---|---|---|
| 目标 / 关系（Target / Relation） | `feeding_target_affinity` 等 | 这是不是当前鱼认可的目标 |
| 视觉（Visual） | apparent size / contrast / flash | 看起来像什么、多显眼 |
| 运动 / 节奏（Motion / Tempo） | speed / speed change / direction change / pause / vertical motion | 怎么动、怎么停、怎么变向 |
| 振动（Vibration） | vibration amplitude / frequency | 水动力振动表现如何 |
| 声学（Acoustic） | sound amplitude / pattern | 声学刺激如何 |
| 接触（Contact） | contact disturbance | 是否发生撞底、碰结构等接触扰动 |

以下不作为正向响应因素（Response Factor）：

```text
Activity
FeedingMotivation
EnvironmentMass
距离 / 遮挡 / 传播衰减本身
Opportunity cadence
post-gen pursuit burden
```

它们分别属于状态 / 上限（State / CAP）、环境（Environment）、World/Physics、机会（Opportunity）或下游任务动作（Task）。

---

# 4. 因素角色（Factor Role）｜响应路径内因素角色

方案一只保留三种运行时（Runtime）角色：

```text
GATE
CORE
IGNORE
```

不提供独立 `ENHANCER` 算子（operator）。

## 4.1 闸门（GATE）

闸门（Gate）只决定响应路径是否有资格成立。

```text
Gate = false
→ PathwayScore = 0
```

示例：

```text
feeding_target_affinity >= ACCEPTABLE
activity >= PURSUIT_MIN
```

闸门不参与几何平均。

---

## 4.2 核心因素（CORE）

核心因素（Core Factor）真正决定这条响应路径的契合强度。

每个核心因素先得到：

```text
FactorFit ∈ [0,1]
```

然后参与路径内聚合。

---

## 4.3 忽略（IGNORE）

当前响应路径不读取该因素。

不存在：

```text
IGNORE = 0
```

它只是“不参与”。

---

## 4.4 次要因素（SECONDARY）如何处理

方案一**不定义 SECONDARY 的运行时（Runtime）数学语义**。

如果某个因素：

> 缺了不影响基础 Pathway 成立，但具备时应该形成明显更强策略，

则建立一个有名字的路径变体（Pathway Variant）。

例如：

```text
STEADY_PREY
Core:
  Target
  Size
  Speed
Ceiling = NORMAL

FLASHING_STEADY_PREY
Core:
  Target
  Size
  Speed
  Flash
Ceiling = HIGH
```

策划编辑器可以继续显示“Secondary”作为提示，但编译器（Compiler）必须把它展开成独立变体（Variant）；运行时（Runtime）不读取 `SECONDARY=0.6` 之类数值。

---

# 5. 因素评估器（Factor Evaluator）｜单因素如何得到契合度（Fit）

每条响应路径（Pathway）对其核心因素指定一个简单评估器（Evaluator）。

输出统一为：

```text
FactorFit ∈ [0,1]
```

方案一只允许少量评估器形状（Evaluator Shape）。

## 5.1 偏好区间（Preferred Range）

适合：

```text
speed
apparent_size
vibration_frequency
```

概念：

```text
过低 → 低 Fit
进入偏好区 → Fit 上升
最佳区 → 1
超过偏好区 → Fit 下降
```

配置可以使用少量关键点或区间。

---

## 5.2 至少达到（At Least）

适合：

```text
speed_change
flash
contact_disturbance
vibration_amplitude
```

概念：

```text
低于门槛 → 0
越强越匹配
达到满意区 → 饱和到 1
```

---

## 5.3 至多不超过（At Most）

适合 finesse / drift 等“不宜过强”的因素。

---

## 5.4 枚举 / 关系映射（Enum / Relation Map）

适合离散关系（Relation）：

```text
feeding_target_affinity
```

例如方案一默认：

```text
IGNORE    → 0
SECONDARY → 0.5
CORE      → 1.0
```

这里只是示意默认映射，可由关系契约（Relation Contract）替换。

---

# 6. 模式（Pattern）内算法｜为什么方案一不用 MIN

方案一不采用：

```text
PatternFit = MIN(all factors)
```

原因是纯 MIN 会丢失非瓶颈因素信息。

例如：

```text
ShapeFit = 0.3
SpeedFit = 0.6
→ MIN = 0.3

ShapeFit = 0.3
SpeedFit = 1.0
→ MIN = 0.3
```

速度从普通提高到完美完全没有效果。

方案一改用**无权几何平均**：

```text
CoreFit_p
= (Π Fit_p,j) ^ (1 / n)
```

性质：

1. 任一核心契合度（CoreFit）= 0，会令整条响应路径 = 0；
2. 所有核心因素（Core）都会持续影响结果；
3. 不允许简单线性完全补偿；
4. 不需要给每个因素（Factor）再配置权重；
5. 因素重复添加仍然会影响结果，因此编译器（Compiler）必须做端点（endpoint）去重。

示例：

```text
ShapeFit = 0.3
SpeedFit = 0.6

CoreFit
= sqrt(0.3 × 0.6)
≈ 0.424
```

而：

```text
ShapeFit = 0.3
SpeedFit = 1.0

CoreFit
= sqrt(0.3 × 1.0)
≈ 0.548
```

两者有差异，但低 ShapeFit 仍然显著拖累整体。

---

# 7. 路径上限（Pathway Ceiling）

每条响应路径配置：

```text
PathwayCeiling ∈ [0,1]
```

最终：

```text
PathwayScore
= PathwayCeiling × CoreFit
```

用途：

> 即使这条策略执行得完美，它在当前模型里最多能提供多强的响应（Response）。

方案一默认值：

```text
BASELINE pathway  → 0.35
NORMAL pathway    → 0.70
STRONG pathway    → 1.00
```

这里只是方案一初始值。

示例：

```text
BASELINE_PREY:
  Ceiling = 0.35
  CoreFit = 1
  PathwayScore = 0.35
```

普通基础匹配不会因为单项契合度（Fit）很高直接成为满响应。

---

# 8. 响应路径间算法｜MAX

同一个物种（Species）× 中鱼习性模式（EngagementMode）可以同时成立多条响应路径（Response Pathway）。

方案一：

```text
PositiveScore
= MAX(all PathwayScore)
```

例如：

```text
STEADY_PREY      = 0.62
JERK_PAUSE       = 0.88
CONTACT_REACTION = 0.41

PositiveScore = 0.88
```

含义：

> 各响应路径默认被视为替代性的充分响应理由；本次机会（Opportunity）采用当前最强的一条。

不会自动出现：

```text
0.62 + 0.88 + 0.41
```

也不会因为同时命中更多响应路径自动增加鱼口。

---

# 9. 跨响应路径协同（Synergy）

方案一不提供自动累积：

```text
NORMAL + NORMAL → HIGH
```

如果两条响应路径（Pathway）同时存在确实应形成更强效果，则必须显式建立一条组合路径（Combined Pathway）。

例如：

```text
PREY_TRACKING
CONTACT_REACTION
```

若组合本身具有独立策略意义：

```text
TRACKING_DEFLECTION
```

则把它作为第三条响应路径：

```text
TRACKING_DEFLECTION
Core:
  tracking-related factors
  contact factor
Ceiling = 1.0
```

最终仍然由 MAX 解决。

---

# 10. 剖面级上限（Profile-wide CAP）

上限（CAP）只表达：

> 当前物种 × 中鱼习性模式（Species × EngagementMode）下，所有正向响应路径都不能超过的全局上限。

例如摄食动机（FeedingMotivation）：

```text
FeedingMotivation → CapScore
```

最终：

```text
FinalScore
= MIN(
    PositiveScore,
    all applicable CapScore
)
```

默认没有上限时：

```text
CapScore = 1
```

活跃度（Activity）通常不做全局上限。

如果活跃度只限制快速追击（fast pursuit），则作为对应响应路径的闸门（Gate）：

```text
activity >= PURSUIT_MIN
```

不会压死 Contact Reaction 等其它响应路径。

---

# 11. 最终得分（FinalScore）→ 响应档位（ResponseBand）

为了兼容当前响应档位契约（ResponseBand Contract），方案一最终仍输出：

```text
NONE < LOW < NORMAL < HIGH
```

方案一默认量化阈值：

```text
FinalScore == 0
→ NONE

0 < FinalScore < 0.40
→ LOW

0.40 <= FinalScore < 0.75
→ NORMAL

0.75 <= FinalScore <= 1
→ HIGH
```

---

# 12. 响应档位（ResponseBand）→ 响应乘数（ResponseMultiplier）

方案一暂时采用已有校准种子（Calibration Seed）：

```text
NONE   = 0.00
LOW    = 0.25
NORMAL = 0.50
HIGH   = 1.00
```

因此响应（Response）最终仍只做衰减（attenuation）：

```text
0 <= ResponseMultiplier <= 1
```

不允许：

```text
ResponseMultiplier > 1
```

---

# 13. 与环境机会量（EnvironmentMass）汇合

响应（Response）与环境（Environment）分支只在最后汇合：

```text
Contribution[m,u]
=
EnvironmentMass[m,u]
× ResponseMultiplier[m,u]
```

之后：

```text
ModeSelectionWeight[m]
= Σ_u Contribution[m,u]

SelectionWeight[q,m]
= ModeSelectionWeight[m]
× ResolvedQualityShare(q|m)
```

再进入既有 fixed-pan 单次加权抽取（weighted roll）。

不增加：

```text
FishConditionCoeff
ExposureCoeff
PerceptionCoeff
PathwayCountBonus
```

---

# 14. 原子姿态 × 分子姿态

识别层允许同时存在：

```text
JERK
PAUSE
JERK_PAUSE
```

但同一因果闭包（causal closure）只形成：

```text
ONE Opportunity
```

## 14.1 机会（Opportunity）

```text
JERK ─────┐
          ├→ JERK_PAUSE root occurrence
PAUSE ────┘
                 ↓
           ONE Opportunity
```

子原子不再各自发出（emit）新机会。

---

## 14.2 响应因素（Response Factor）

响应不配置：

```text
JERK attraction
PAUSE attraction
JERK_PAUSE attraction bonus
```

而是：

```text
JERK
→ speed_change / direction_change / vibration ...

PAUSE
→ pause_duration / speed state ...

JERK_PAUSE
→ 第一版不增加额外 generic attraction bonus
```

当前规范原语（canonical primitives）先做 cause × endpoint 去重。

方案一暂不新增 sequence / inter-event-gap 运行时事实（Runtime Fact）。

如果现有原语（primitives）不能表达某个重要分子行为，留到后续方案重开（reopen），不在方案一增加新 DSL。

---

# 15. 食物类型与响应路径（Pathway）的关系

方案一明确：

```text
Food / Target Archetype ≠ Pathway
```

目标原型（Target Archetype）负责两件事：

1. 提供物种 × 目标（Species × Target）的关系 / 亲和（relation / affinity）；
2. 决定哪些路径族（Pathway Family）具有语义资格。

例如：

```text
BAITFISH
→ allowed pathways:
  STEADY_PREY
  FLEEING_PREY
  JERK_PAUSE

CRAWFISH
→ allowed pathways:
  BOTTOM_CRAWL
  BOTTOM_HOP
  CONTACT_DEFLECTION
```

但具体：

```text
LargemouthBass × CrawfishAffinity
```

仍然由关系（Relation）层给出。

这样区分：

```text
“这种鱼想不想吃这个目标”
≠
“这种目标天然支持哪些 Presentation 策略”
```

---

# 16. 配置结构

方案一采用四层配置。

## 16.1 全局响应配置（Global Response Config）

全项目一份：

```yaml
band_thresholds:
  none: 0
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

## 16.2 逻辑模板（LogicTemplate）/ 路径族（Pathway Family）

负责共享结构：

```yaml
template: FEEDING_PREDATION

pathways:
  - id: BASELINE_PREY
    ceiling_class: baseline
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - factor: target_fit
        evaluator: relation_map

  - id: STEADY_PREY
    ceiling_class: normal
    gates:
      - target_affinity >= ACCEPTABLE
    core:
      - factor: target_fit
        evaluator: relation_map
      - factor: apparent_size
        evaluator: preferred_range
      - factor: speed
        evaluator: preferred_range

  - id: JERK_PAUSE
    ceiling_class: strong
    gates:
      - target_affinity >= ACCEPTABLE
      - activity >= STOP_GO_MIN
    core:
      - factor: target_fit
        evaluator: relation_map
      - factor: speed_change
        evaluator: at_least
      - factor: pause_duration
        evaluator: at_least

  - id: CONTACT_REACTION
    ceiling_class: strong
    gates: []
    core:
      - factor: contact_disturbance
        evaluator: at_least
      - factor: direction_change
        evaluator: at_least
```

---

## 16.3 物种（Species）× 中鱼习性模式（EngagementMode）响应剖面（ResponseProfile）

只覆盖参数，不重写算法：

```yaml
species: LARGEMOUTH_BASS
mode: FEEDING
template: FEEDING_PREDATION

params:
  STEADY_PREY:
    apparent_size:
      preferred_min: ...
      preferred_max: ...
    speed:
      preferred_min: ...
      preferred_max: ...

  JERK_PAUSE:
    speed_change:
      normal_at: ...
      high_at: ...
    pause_duration:
      normal_at: ...
      high_at: ...

  CONTACT_REACTION:
    contact_disturbance:
      normal_at: ...
      high_at: ...
```

---

## 16.4 目标关系配置（Target Relation Config）

独立维护：

```yaml
species: LARGEMOUTH_BASS

feeding_target_affinity:
  BAITFISH: CORE
  CRAWFISH: CORE
  WORM: SECONDARY
  INSECT: SECONDARY
```

响应（Response）通过规范关系（canonical relation）消费，不直接查 SKU / Lure ID。

---

# 17. 完整运行时伪代码

```python
def resolve_response(profile, snapshot):
    pathway_scores = []

    for p in profile.pathways:
        if not all(gate(snapshot) for gate in p.gates):
            pathway_scores.append(0.0)
            continue

        fits = [
            evaluator(snapshot, params)
            for evaluator, params in p.core_factor_evaluators
        ]

        if not fits:
            core_fit = 1.0
        elif any(f <= 0 for f in fits):
            core_fit = 0.0
        else:
            core_fit = product(fits) ** (1.0 / len(fits))

        pathway_score = p.ceiling * core_fit
        pathway_scores.append(pathway_score)

    positive_score = max([0.0] + pathway_scores)

    profile_cap = min([1.0] + [
        cap(snapshot)
        for cap in profile.profile_wide_caps
        if cap.applies(snapshot)
    ])

    final_score = min(positive_score, profile_cap)

    if final_score <= 0:
        band = "NONE"
    elif final_score < 0.40:
        band = "LOW"
    elif final_score < 0.75:
        band = "NORMAL"
    else:
        band = "HIGH"

    multiplier = {
        "NONE": 0.00,
        "LOW": 0.25,
        "NORMAL": 0.50,
        "HIGH": 1.00,
    }[band]

    return {
        "final_score": final_score,
        "band": band,
        "multiplier": multiplier,
        "pathway_scores": pathway_scores,
    }
```

---

# 18. 黑鲈示例

假设当前：

```text
TargetFit        = 1.00
SizeFit          = 0.80
SteadySpeedFit   = 0.70
SpeedChangeFit   = 0.95
PauseFit         = 0.80
ContactFit       = 0.20
DirectionFit     = 0.60
Activity         = PASS
Feeding CAP      = 1.00
```

## BASELINE_PREY

```text
Ceiling = 0.35
CoreFit = 1.00

Score
= 0.35 × 1
= 0.35
```

## STEADY_PREY

```text
CoreFit
= cubic_root(
    1.00
  × 0.80
  × 0.70
)
≈ 0.824

Score
= 0.70 × 0.824
≈ 0.577
```

## JERK_PAUSE

```text
CoreFit
= cubic_root(
    1.00
  × 0.95
  × 0.80
)
≈ 0.913

Score
= 1.00 × 0.913
≈ 0.913
```

## CONTACT_REACTION

```text
CoreFit
= sqrt(
    0.20 × 0.60
)
≈ 0.346

Score
= 1.00 × 0.346
≈ 0.346
```

所以：

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

Feeding CAP = 1：

```text
FinalScore
= 0.913
```

量化：

```text
0.913 >= 0.75
→ HIGH
```

最终：

```text
ResponseMultiplier = 1.0
```

---

# 19. 调试（Debug）输出

每次响应求值（Response evaluation）至少输出：

```text
Species
EngagementMode
OpportunityId
EvaluationSupportId

Pathway:
  Gate results
  Core Factor raw facts
  Core FactorFit
  PathwayCeiling
  PathwayScore

WinningPathway
PositiveScore

Applied CAPs
FinalScore
ResponseBand
ResponseMultiplier
```

这样可以直接回答：

```text
为什么这次是 LOW？
哪条 Pathway 赢了？
哪一个 Factor 拉低了结果？
是 Gate 失败，还是 Fit 差？
是不是被 FeedingMotivation CAP？
```

---

# 20. 方案一明确不做

第一版不做：

```text
Cue-by-Cue weighted sum
Factor-level arbitrary weights
Pattern 内 MIN
Automatic Pathway accumulation
Noisy-OR
SECONDARY numeric coefficient
Enhancer operator
Generic molecule bonus
Recognizer-count bonus
Default LOW
ResponseMultiplier > 1
Per-Species BandMultiplier table
Second RNG for Pathway
Second RNG for Quality
```

---

# 21. 方案一的硬假设

本文主动冻结以下假设，即使它们后来可能被推翻：

1. 响应路径（Pathway）是有效的中层策略身份；
2. 核心因素（Core Factor）可以归一化为 `[0,1]` 契合度（Fit）；
3. 核心因素默认等权；
4. 几何平均足以表达第一版响应路径内的类 AND 聚合（AND-like aggregation）；
5. 响应路径默认是替代性的，因此使用 MAX；
6. 跨响应路径协同（synergy）必须显式建组合路径（Combined Pathway）；
7. Secondary 不购买独立运行时（Runtime）算子（operator）；
8. 最终仍量化为 `NONE / LOW / NORMAL / HIGH`；
9. 响应（Response）只衰减，不放大；
10. 原子 / 分子识别不改变一个因果闭包（causal closure）只有一个机会（Opportunity）的原则。

---

# 22. 后续攻击顺序

方案一形成后，不再边写边改。

建议按以下顺序攻击：

1. **路径准入（Pathway Admission）**  
   用 5～8 个真实钓法故事检查响应路径（Pathway）是否过粗 / 过细。

2. **几何平均（Geometric Mean）**  
   检查是否产生不合理补偿或因素数量偏差。

3. **跨路径取最大值（MAX Across Pathways）**  
   检查多条中等响应（Response）同时存在时是否被低估。

4. **次要因素转变体（Secondary → Variant）**  
   检查是否造成路径爆炸（Pathway Explosion）。

5. **目标原型 × 路径资格（Target Archetype × Pathway Eligibility）**  
   检查是否与 `feeding_target_affinity` 重复表达。

6. **配置编写探针（Authoring Probe）**  
   用 3～5 个鱼种 × 2～3 个中鱼习性模式（EngagementMode）实际配置，测参数规模与覆盖（Override）复杂度。

7. **校准（Calibration）**  
   最后再处理阈值、LOW/NORMAL multiplier、`ρ=F/N` 与体验时间预算。

---

# 23. 当前方案一总图

```text
Actual Presentation
        ↓
World / Physics
        ↓
Canonical Cue / Relation Facts
        +
Fish Condition
        ↓
Species × Engagement Mode ResponseProfile
        ↓
┌─────────────────────────────────────┐
│ Pathway A                           │
│ Gates → Core FactorFit → GeomMean  │
│ × Ceiling → Score_A                │
├─────────────────────────────────────┤
│ Pathway B                           │
│ Gates → Core FactorFit → GeomMean  │
│ × Ceiling → Score_B                │
├─────────────────────────────────────┤
│ Pathway C ...                       │
└─────────────────────────────────────┘
        ↓
MAX(Pathway Scores)
        ↓
MIN(Profile-wide CAP)
        ↓
FinalScore ∈ [0,1]
        ↓
Quantize
        ↓
NONE / LOW / NORMAL / HIGH
        ↓
Global BandMultiplier
        ↓
EnvironmentMass × ResponseMultiplier
        ↓
ModeSelectionWeight
        ↓
q × m SelectionWeight
        ↓
ONE fixed-pan weighted roll
```

---

# 24. 状态声明

本文件是 **“方案一”**，不是当前权威（Current Authority），也不宣称：

- 已通过现实钓鱼策略验证；
- 已通过 200 鱼种配置规模验证；
- 已通过人类可用性（Human Usability）；
- 已完成数值校准（Calibration）；
- 已晋升（Promotion）到 Simplified V0 Current；
- 已成为 0.3.4.0-B 开发要求。

它的唯一目标是：

> **先提供一个完整、无悬空算子（operator）、能从输入一路算到 SelectionWeight 的响应（Response）基线方案，供后续系统性攻击。**
