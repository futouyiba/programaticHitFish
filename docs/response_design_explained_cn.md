# Response 机制说明：鱼为什么会对玩家的呈现作出响应

这篇文档试图回答一个很直观、但实现起来并不简单的问题：

> 玩家把饵抛到鱼附近以后，为什么有时鱼会理它，有时不理？

如果只是做一个很粗的系统，我们完全可以给每种饵一个“吸引力”，再给每种鱼一个“偏好”，最后做一次乘法或者加法。

但只要我们希望玩家的操作真的有意义，这种做法很快就不够用了。

同一只饵，匀速回收、快速抽停、贴底拖行、撞到石头以后突然弹开，给鱼的感觉并不一样。对大口黑鲈有效的操作，也不一定对鳟鱼、鲤鱼或底栖鱼有效。甚至同一条鱼，在主动觅食、低活性、护巢等状态下，也可能对同一个动作产生不同反应。

所以 Response 这层真正要解决的，并不是“这个饵有多好”，而是：

> **当前这条鱼，面对玩家此刻实际呈现出来的这组刺激，是否形成了一条有效的响应理由？**

下面从这个问题出发，把整套思路讲清楚。

---

# 1. 先把问题拆开：这里有鱼，不等于鱼会咬

中鱼前至少有两件事需要分开看。

第一件事是：

> **这里本来有多少这种鱼的机会？**

它主要由鱼种投放、空间分布、环境适宜度、动态空间利用等决定。我们把最后落到某个局部空间上的这部分机会量，统称为 `EnvironmentMass`。

第二件事是：

> **这些已经在这里的鱼，面对玩家当前的操作，会不会对这个呈现产生响应？**

这就是 Response。

所以最重要的一条主链其实很简单：

```text
这里本来有多少鱼机会
        ×
这次操作让它有多愿意响应
        =
这次真正进入中鱼竞争的机会量
```

也就是：

```text
Contribution
=
EnvironmentMass
× ResponseMultiplier
```

这个拆分很重要，因为它把“鱼在哪里”和“鱼理不理你”分开了。

如果鱼根本不在这里，Response 再高也没用。

反过来，如果这里鱼很多，但你的呈现非常不对，它们也可以几乎完全不响应。

---

# 2. 玩家真正改变的，不是一个“吸引力数值”

玩家做一次操作时，游戏里发生的不是“吸引力 +0.2”。

比如一次 jerk-pause，实际可能同时发生：

```text
速度突然上升
方向改变
水中振动增强
随后快速减速
停顿一段时间
饵体姿态发生变化
```

再比如一次撞障碍物的 deflection：

```text
发生接触扰动
运动方向突然改变
速度突变
产生振动
可能伴随声音
```

这些才是鱼真正“面对”的东西。

因此系统先把玩家操作、饵、线组、地形交互等，解析成一组**与鱼种无关的呈现事实**。

例如：

```text
apparent_size
visual_contrast
flash
speed
speed_change
direction_change
pause_duration
vertical_motion
vibration_amplitude
vibration_frequency
sound_amplitude
sound_pattern
contact_disturbance
```

这一步只回答：

> **这里实际发生了什么？**

它还没有开始判断某条鱼喜欢不喜欢。

---

# 3. 为了让人容易理解，可以把这些事实分成六类

底层输入虽然很多，但对策划和玩家来说，不需要每次都面对十几个字段。

可以把它们整理成六类 Response 因素。

| 因素 | 主要回答什么 | 典型输入 |
|---|---|---|
| 目标匹配 Target / Relation | 这东西像不像它愿意理的目标 | feeding target affinity |
| 视觉 Visual | 看起来多大、多显眼、是否有闪光 | apparent size / contrast / flash |
| 运动 Motion / Tempo | 怎么游、怎么变速、怎么停 | speed / speed change / turn / pause / vertical motion |
| 振动 Vibration | 在水里产生怎样的水动力振动 | vibration amplitude / frequency |
| 声音 Acoustic | 有什么声音、声音模式如何 | sound amplitude / pattern |
| 接触 Contact | 有没有撞底、碰石、打草、碰结构 | contact disturbance |

这六类只是**人类理解和配置上的分组**。

系统并不是先算：

```text
视觉吸引 = 0.4
运动吸引 = 0.7
振动吸引 = 0.2
```

然后再简单相加。

原因很简单：鱼往往不是因为“总分够高”而响应，而是因为某一种完整的刺激模式成立了。

---

# 4. Response 的核心不是“因素加分”，而是“响应路径”

我们把一条完整的、可以解释的有效刺激模式，叫做 **Response Pathway｜响应路径**。

它的意思不是“一个因素”，也不是“一种食物”。

它更像：

> **这条鱼为什么会因为玩家现在的这套操作而理它？**

例如，对一条伏击型掠食鱼来说，可能有这样的几条路径：

```text
普通猎物接受
稳定游动猎物
逃窜猎物
抽停触发
碰撞 / 变向反应
```

这些路径对应的是不同的玩家策略故事。

比如：

- 匀速慢收，让饵像一条正常游动的小鱼；
- 猛抽以后停顿，让饵像受伤或突然失速的猎物；
- 撞到石头后弹开，触发反应性攻击；
- 贴底跳动，让饵像甲壳类或底栖猎物。

这里真正有价值的是：

> 玩家可以通过不同操作，走不同的有效路径。

因此 Response 不是问：

> “所有刺激总共有多少分？”

而是问：

> “现在到底有哪些有效的响应路径成立？其中最强的是哪一条？”

---

# 5. 一条 Pathway 里，每个因素先判断“契合度”

同一个速度，对不同鱼、不同路径，意义可能完全不同。

例如 `0.8 m/s`：

- 对慢速自然漂流，可能太快；
- 对稳定小鱼游动，可能很合适；
- 对快速逃窜猎物，又可能偏慢。

因此底层事实不会直接变成一个全局“吸引力”。

它会经过当前 Pathway 的解释，得到一个 `FactorFit`：

```text
实际事实
↓
这条鱼 × 当前中鱼习性模式 × 当前 Pathway 的解释
↓
契合度 FactorFit ∈ [0,1]
```

例如：

```text
speed = 0.8 m/s
```

在 `STEADY_PREY` 路径里可能得到：

```text
SpeedFit = 0.85
```

而在 `NATURAL_DRIFT` 里可能只有：

```text
SpeedFit = 0.25
```

这一步把“物理事实”和“鱼的偏好”分开了。

---

# 6. FactorFit 怎么得到

我们不希望策划给每个字段随手画一条任意复杂曲线。

大多数因素其实可以用少量通用形状表达。

## 6.1 偏好区间

适合：

```text
速度
大小
振动频率
```

例如某条鱼在某条 Pathway 中：

```text
太慢      → 不像
稍慢      → 一般
合适      → 最好
稍快      → 还能接受
太快      → 不像
```

这就是一个 Preferred Range。

## 6.2 越强越容易触发，但会饱和

适合：

```text
speed_change
flash
contact_disturbance
vibration_amplitude
```

例如碰撞扰动：

```text
太轻 → 几乎没意义
中等 → 有一定触发
明显 → 很强
更强 → 不再继续无限增加
```

## 6.3 越弱越合适

有些自然漂流、细腻操作，反而要求动作不要太大。

这时可以用 At Most 类的曲线。

## 6.4 离散关系

例如目标亲和性：

```text
不认可
次选目标
核心目标
```

可以映射成不同 Fit。

---

# 7. 一条 Pathway 内部怎么把多个 Factor 合在一起

这里我们不采用简单加法。

假设一条 `STEADY_PREY` 路径要求：

```text
目标匹配
大小合适
速度合适
```

简单相加会有一个问题：

如果目标根本不像它的食物，但速度和闪光都特别强，总分可能依然很高。

这很容易出现“一个完全错误的关键因素，被几个无关强项补回来”的现象。

另一方面，如果直接取最差项 `MIN`，又会太硬。

例如：

```text
SizeFit = 0.3
SpeedFit = 0.6
```

和：

```text
SizeFit = 0.3
SpeedFit = 1.0
```

如果都取 MIN，结果都是 `0.3`。

这意味着速度从一般做到完美，完全没有价值。

所以这版采用一个折中的办法：**几何平均**。

公式是：

```text
CoreFit
= geometric_mean(FactorFit1, FactorFit2, ...)
```

直觉上可以理解成：

> 每一项都重要；有明显短板会拖累整体，但其它项做好仍然有价值。

例如：

```text
ShapeFit = 0.3
SpeedFit = 0.6
```

结果大约是：

```text
sqrt(0.3 × 0.6)
≈ 0.42
```

而：

```text
ShapeFit = 0.3
SpeedFit = 1.0
```

结果大约是：

```text
sqrt(0.3 × 1.0)
≈ 0.55
```

可以看到：

- 形态差仍然明显拖后腿；
- 速度变好还是有收益；
- 任何一项如果完全不成立，整体也会掉到 0。

这比简单相加更像“整体像不像一种有效的猎物呈现”。

---

# 8. Gate：有些条件不是“多少分”，而是“有没有资格”

不是所有因素都适合拿来做平均。

例如一条追击型 Pathway 可能要求：

```text
Activity >= 某个最低水平
```

如果鱼现在活性太低，持续高速追击这条路径就不成立。

这类条件叫 Gate。

Gate 只回答：

> 这条路径能不能成立？

例如：

```text
Activity 不够
→ FLEEING_PREY 关闭
```

但它不会影响别的路径。

所以同一条低活性的鱼，可能：

```text
高速追击 → 不成立
抽停近距离反应 → 还能成立
撞障碍反应 → 还能成立
```

这比把 `Activity` 直接乘到所有 Response 上更符合我们想要的策略差异。

---

# 9. Pathway 还有自己的上限

不同路径本身的“价值上限”可以不同。

例如：

```text
普通猎物接受
```

即使完全成立，也只表示：

> “这个东西基本像食物，我会有一点兴趣。”

它不应该直接达到最高响应。

所以每条 Pathway 有一个 `PathwayCeiling`。

比如：

```text
BASELINE_PREY   上限较低
STEADY_PREY     上限中等
JERK_PAUSE      上限较高
CONTACT_REACTION 上限较高
```

计算：

```text
PathwayScore
=
CoreFit × PathwayCeiling
```

这样“基本合理”与“真正强策略”就能自然拉开。

---

# 10. 多条 Pathway 同时成立时怎么办

一次玩家操作完全可能同时符合多条路径。

例如：

```text
STEADY_PREY = 0.62
JERK_PAUSE = 0.88
CONTACT_REACTION = 0.41
```

这版不把它们相加。

我们取最强的一条：

```text
PositiveScore
= MAX(PathwayScore)
```

得到：

```text
0.88
```

背后的直觉是：

> 这些 Pathway 默认是“替代性的充分理由”。

鱼已经有一条很强的理由去响应，不会因为同时又满足了一条普通理由，就自动获得额外一份鱼口。

这样做还有一个很实际的好处：

不会因为我们把系统描述得更细、写了更多 Pathway，就凭空提高 Response。

如果未来确实有一种情况：

> 两个中等理由同时出现，本身就是一种明显更强的刺激故事，

那应该把这个组合写成一条真正有语义的组合路径，而不是让系统默认把所有路径加起来。

例如：

```text
PREY_TRACKING
+
CONTACT_DEFLECTION
```

如果它在玩法上确实代表一种特殊的高效触发，可以单独形成：

```text
TRACKING_DEFLECTION
```

---

# 11. Fish Condition 怎么影响 Response

鱼的状态很重要，但不要把所有状态压成一个“鱼状态系数”。

不同状态应该影响它真正负责的部分。

## Activity

主要影响：

> 这条鱼现在有没有能力完成某类动作。

比如：

```text
高速追击需要一定 Activity
```

所以 Activity 更适合作为某些 Pathway 的 Gate。

## Feeding Motivation

它更像：

> 这条鱼当前整体有多愿意进入摄食响应。

如果 Feeding Motivation 很低，可以限制整个 Feeding Mode 的最高 Response。

例如：

```text
当前最强 Pathway = HIGH
但 Feeding Motivation 最多只允许 NORMAL
→ 最终 Response = NORMAL
```

这种全局限制我们叫 CAP。

它和 Gate 的区别是：

- Gate 只关掉特定路径；
- CAP 限制当前整个 Mode 的最高响应。

---

# 12. Response 最后如何得到一个可用结果

完整过程可以压成：

```text
1. 对每条 Pathway 检查 Gate
2. 对成立的 Pathway 计算各个 Core FactorFit
3. 用几何平均得到 CoreFit
4. 乘 PathwayCeiling 得到 PathwayScore
5. 所有 Pathway 取 MAX
6. 再受全局 CAP 限制
7. 得到 FinalScore ∈ [0,1]
```

然后把连续分数映射到四档：

```text
NONE
LOW
NORMAL
HIGH
```

再把四档映射成最终 `ResponseMultiplier`。

一个示例映射可以是：

```text
NONE   → 0
LOW    → 0.25
NORMAL → 0.50
HIGH   → 1.00
```

最终：

```text
Contribution
= EnvironmentMass × ResponseMultiplier
```

Response 的作用始终是：

> 在这里本来存在的鱼机会基础上，决定这次呈现有多少能够真正进入中鱼竞争。

所以第一版里，Response 不负责把机会放大到 `1` 以上。

---

# 13. 一个完整例子：大口黑鲈面对一次抽停

假设某个局部位置，本来有一批大口黑鲈的 Feeding opportunity。

玩家使用一只小鱼型拟饵，做了一次明显的 jerk-pause。

这次操作被解析成：

```text
目标类型：小鱼型，黑鲈高度认可
大小：合适
速度突变：很明显
停顿：合适
接触扰动：很弱
鱼当前 Activity：足够
Feeding Motivation：正常
```

对于这条鱼的 Feeding Mode，我们有几条 Pathway。

## 13.1 BASELINE_PREY

它只要求：

```text
目标基本认可
```

因为是普通基础路径，上限比较低。

即使这次目标非常合适：

```text
CoreFit = 1.0
Ceiling = 0.35
Score = 0.35
```

这表示：

> 光是“像食物”本身，只能提供弱到中等之前的基础响应。

## 13.2 STEADY_PREY

这条路径更关心：

```text
目标匹配
大小
稳定速度
```

但这次玩家刚做了明显抽停，稳定速度并不突出。

假设最后算出来：

```text
Score = 0.55
```

## 13.3 JERK_PAUSE

这条路径关心：

```text
目标匹配
速度变化
停顿
```

本次三个因素都很契合。

例如：

```text
TargetFit      = 1.00
SpeedChangeFit = 0.95
PauseFit       = 0.80
```

几何平均大约：

```text
0.91
```

如果这条路径上限是 1：

```text
JERK_PAUSE Score = 0.91
```

## 13.4 CONTACT_REACTION

这次并没有明显撞底或撞结构。

所以：

```text
Score ≈ 0.2～0.3
```

最后：

```text
MAX(
  Baseline 0.35,
  Steady 0.55,
  JerkPause 0.91,
  Contact 0.25
)
= 0.91
```

如果 Feeding Motivation 没有限制：

```text
FinalScore = 0.91
```

最终落到：

```text
HIGH
→ ResponseMultiplier = 1.0
```

这时玩家得到的不是“因为 speed +0.2、pause +0.3，所以总分够高”，而是：

> **这次操作非常完整地命中了黑鲈的 JERK_PAUSE 响应路径。**

这就是这套设计最想保留的可解释性。

---

# 14. 原子姿态和分子姿态同时存在时怎么处理

这是一个很容易重复计权的问题。

例如一次完整的 jerk-pause，识别系统可能同时识别到：

```text
JERK
PAUSE
JERK_PAUSE
```

如果我们给三者分别算吸引力：

```text
JERK + PAUSE + JERK_PAUSE bonus
```

就会把同一个玩家动作重复算很多次。

所以这里分两层处理。

## 14.1 Opportunity 层

如果 JERK 和 PAUSE 本来就是同一个完整动作的一部分：

```text
JERK ──┐
       ├→ JERK_PAUSE
PAUSE ─┘
```

它们只形成一个根 Opportunity。

不是三次抽奖。

## 14.2 Response 输入层

原子动作仍然保留它们产生的基础事实：

```text
JERK
→ speed_change
→ direction_change
→ vibration

PAUSE
→ pause_duration
→ low-speed state
```

但 `JERK_PAUSE` 本身不再额外发一份：

```text
speed_change bonus
pause bonus
vibration bonus
```

也就是说：

> 分子姿态可以负责把几个原子动作绑定成一个完整语义，但不能把子动作已经产生的物理事实重新算一遍。

这让“识别更细”不会自动变成“鱼口更高”。

---

# 15. 食物类型和 Pathway 是什么关系

Pathway 不等于食物种类。

例如：

```text
小鱼
虾蟹
虫
蠕虫
```

这些首先回答：

> 这条鱼把它当成多合适的目标？

也就是 Target / Relation。

但不同目标类型又会天然支持不同的呈现策略。

例如：

```text
小鱼型
→ 稳定游动
→ 逃窜
→ 抽停

虾蟹型
→ 贴底爬行
→ 底部跳动
→ 撞底 / 碰结构

昆虫型
→ 漂流
→ 水面漂浮
```

所以比较自然的关系是：

```text
Target Archetype
→ 决定哪些 Pathway 有意义

Species × Target
→ 决定目标亲和度

实际 Presentation
→ 决定这些 Pathway 当前有多契合
```

这样“鱼想不想吃这个目标”和“这个目标应该怎么操作”就不会混成一个概念。

---

# 16. 策划最终要配置什么

如果把所有东西都做成“每条鱼 × 每个 Cue × 每个权重”，两百多种鱼很快就会失控。

因此更适合分成几层配置。

## 第一层：全局 Response 规则

全项目统一的东西，例如：

```text
NONE / LOW / NORMAL / HIGH 的分档
各档对应的 ResponseMultiplier
几种通用 Factor Evaluator 的数学形状
```

这些不应该每条鱼各配一套。

## 第二层：Logic Template

定义某种常见中鱼模式有哪些 Pathway。

例如一个通用的掠食型 Feeding Template 可以包含：

```text
BASELINE_PREY
STEADY_PREY
FLEEING_PREY
JERK_PAUSE
CONTACT_REACTION
```

Template 定义结构，不决定每条鱼的具体阈值。

## 第三层：Species × Engagement Mode 参数

每条鱼只填写差异。

例如黑鲈：

```text
喜欢多大的猎物
什么速度区间更像正常猎物
多大的 speed change 算明显
多长 pause 最合适
多强 contact 才容易触发 reaction
```

这样一条鱼是在复用模板，而不是重新发明整套算法。

## 第四层：Target Relation

独立配置：

```text
黑鲈对小鱼型目标：高
黑鲈对虾蟹：高
黑鲈对虫：中
```

Response 只读取最终的目标关系，不直接写死具体饵 SKU。

---

# 17. 一个可能的配置长什么样

下面不是最终表结构，只是为了把策划视角说清楚。

```yaml
species: LARGEMOUTH_BASS
mode: FEEDING
template: FEEDING_PREDATOR

pathways:
  STEADY_PREY:
    ceiling: 0.70
    gate:
      target_affinity: ACCEPTABLE
    factors:
      apparent_size:
        evaluator: preferred_range
        preferred: [small, medium]
      speed:
        evaluator: preferred_range
        preferred: [low, normal]

  JERK_PAUSE:
    ceiling: 1.00
    gate:
      target_affinity: ACCEPTABLE
      activity: STOP_GO_MIN
    factors:
      speed_change:
        evaluator: at_least
      pause_duration:
        evaluator: at_least

  CONTACT_REACTION:
    ceiling: 1.00
    factors:
      contact_disturbance:
        evaluator: at_least
      direction_change:
        evaluator: at_least
```

真正做编辑器时，可以把这些翻译成策划更直观的控件，而不是要求人直接写 YAML。

---

# 18. 玩家体验上，希望形成什么

这套机制不是为了让后台公式更漂亮，而是为了买到几个玩家能实际感受到的东西。

## 同一条鱼可以有多种有效打法

例如：

```text
稳定回收
抽停
撞结构
贴底跳
```

不是只有一个“正确速度”。

## 不同鱼的最佳策略不同

同一个动作：

```text
对黑鲈很好
对另一种鱼一般
对第三种鱼可能完全不成立
```

这样鱼种习性才真正进入玩法。

## 状态变化会改变最优策略

例如低活性时：

```text
高速追击失效
近距离抽停仍可用
接触反应仍可能存在
```

玩家不是只看到“鱼口统一下降 30%”，而是会发现打法应该变化。

## Debug 和调参都有解释

如果一次 Response 很低，我们可以追到：

```text
哪条 Pathway 赢了
哪条 Pathway Gate 失败了
哪个 FactorFit 很差
有没有被 Feeding Motivation CAP
```

这比一个黑箱总分更容易调，也更容易解释给策划。

---

# 19. 这套设计刻意不做什么

为了避免系统重新滑回“所有东西都乘一遍、加一遍”，这里有几件事刻意不做。

不做：

```text
视觉分 + 运动分 + 振动分 + 声音分
```

不做：

```text
JERK 分数 + PAUSE 分数 + JERK_PAUSE bonus
```

不做：

```text
命中更多 Pathway 就自动累积更多 Response
```

不做：

```text
Activity × FeedingMotivation × Exposure × Response
```

也不因为技术上把一个 support 切成更多 fragment，就产生更多鱼机会。

原则始终是：

> **同一个原因只结算一次；真正不同的策略意义才购买新的表达。**

---

# 20. 整套机制压成一张图

```text
玩家操作 / 饵 / 地形交互
        ↓
Actual Presentation
        ↓
World / Physics
        ↓
Canonical Cue / Relation Facts
        ↓

Species × Engagement Mode Response
        ↓
┌───────────────────────────────┐
│ Pathway A                     │
│ Gate                          │
│ → FactorFit × N               │
│ → 几何平均                    │
│ → × PathwayCeiling            │
│ → Score A                     │
├───────────────────────────────┤
│ Pathway B                     │
│ ...                           │
├───────────────────────────────┤
│ Pathway C                     │
│ ...                           │
└───────────────────────────────┘
        ↓
MAX(Pathway Scores)
        ↓
Profile-wide CAP
        ↓
FinalScore 0..1
        ↓
NONE / LOW / NORMAL / HIGH
        ↓
ResponseMultiplier
        ↓

EnvironmentMass × ResponseMultiplier
        ↓
ModeSelectionWeight
        ↓
Quality projection
        ↓
一次 fixed-pan weighted roll
```

---

# 21. 接下来真正值得继续验证的地方

这套结构已经可以完整从输入算到 Selection，但其中几个选择仍然值得继续用真实策略故事和配置实验去检验。

最重要的是三个：

1. **Pathway 内用几何平均是否合适。** 需要观察它是否允许了过多补偿，或者对 Factor 数量产生奇怪偏差。
2. **Pathway 间只取 MAX 是否太硬。** 要检查两条中等但独立的响应理由同时出现时，是否真的不应该更强。
3. **Pathway 的颗粒度。** 如果一个 Mode 最后需要几十条 Pathway，这套模型就失去了生产价值；如果只有两三条，又可能表达不出玩家策略差异。

这些问题更适合通过真实鱼种和真实钓法去继续推，而不是继续抽象讨论。

一个比较有效的下一步是：

```text
选 3～5 种差异明显的鱼
×
每种 2～3 个 Engagement Mode
×
每个 Mode 3～6 条真实策略故事
```

真正配一次，看看：

```text
哪些 Pathway 能共享
哪些只能物种特化
需要多少参数
哪些地方开始出现组合爆炸
```

到这一步以后，我们才能更有把握地决定几何平均、MAX 和 Template 的最终形态。
