# Russian Fishing 4 饵料 / 窝料机制深度调研

> 文档类型：Research / Evidence Reference  
> 状态：Research Snapshot  
> 日期：2026-10-21  
> 权威级别：Non-authoritative / Reference only  
> 用途：为台钓饵料、窝料、诱鱼与中鱼适配机制提供外部产品与机制参考  
> 明确不代表：FCF Current、台钓机制 Approved、RF4 内部源码事实

---

## 0. 一页结论

本次调研重点回答一个问题：**Russian Fishing 4（RF4）里的自定义饵料 / 窝料，到底更像“科学语义向量匹配”，还是“具体 Ingredient / Bait 配置 + 聚合”？**

目前公开证据支持以下结论：

1. **没有公开证据表明 RF4 使用 `grain / sweet / animal / fruity ...` 之类连续语义向量，再通过 cosine similarity / distance 与鱼种向量做匹配。**这类算法可以作为我们自己的候选方案，但不能以 RF4 为证据。
2. RF4 的玩家侧和开发者公开语义都明显以 **具体 Component / Bait / Flavor identity** 为中心：普通窝料由 `Base + Additives + Attractants` 组成；玩家可以保存自定义 feedmix recipe；不同 component 的 mix 会合并成一个 Feeding Place，影响又会因 component 不同而不同。[S1][S2][S3]
3. **最终自定义 Feedmix 不可能仅依赖预枚举的 `RecipeID × FishID` 表。**原因是玩家可保存自己的普通 feed mix、dry mix、PVA string recipe；因此至少需要从组件重新求值，或者在制作时编译出效果。[S3]
4. RF4 明确存在 **鱼对 bait / lure 的偏好**，且同一鱼种在不同水域可能不同；世界状态重置后，鱼的栖息地和 bait/lure preference 也可能改变。[S1][S4][S5]
5. Groundbait 不是瞬时 `BiteBonus`。开发者公开说明支持一种明显的 **Local Feeding State / Feeding Place**：固定 2.5 m 作用半径、可影响区域内其他竿、不同 feedmix 可在重叠区域共同作用、具有持续性，并存在 overfeeding。[S2]
6. Groundbait 的结果不只受“味型”影响。公开机制还包括 **投放几何、颗粒大小、Feedmix 品质、投喂量、持续时间、历史投喂 / overfeeding**。[S1][S2]
7. RF4 官方手册明确提示：**配方成分越多，可能吸引到窝点的鱼种越多**；鲤鱼投喂示例又要求按当前水域鱼的偏好选择 pellet / boilie flavor。这说明“总诱鱼能力”和“鱼种针对性”至少在产品语义上不是同一件事。[S1]
8. 当前玩家实践中，大量配方会让 hookbait、groundbait、dip 围绕同一 flavor family 对齐，例如 Chocolate / Creme Brulee、Coconut & Cream、Crab、Squid。这证明 **Flavor identity 是玩家可学习、可交流、可复用的内容单位**，但不能反过来证明 RF4 后台具体公式。[S7][S8][S9][S10]

因此，若只根据公开证据重建 RF4，最符合证据的黑盒不是“科学向量模型”，而是：

```text
Ingredient / Bait identity
        +
Fish / Waterbody preference state
        +
Feed component properties
        +
Delivery / amount / history
        ↓
Component-level evaluation / aggregation
        ↓
Local Feeding Place / Local Fish Opportunity
```

其中 `ComponentID × FishID`、`FlavorFamily × FishID`、两者混合、或更复杂的内部表示，**RF4 均未公开**。

---

## 1. 研究问题与证据纪律

### 1.1 本轮问题

本轮主要回答：

- RF4 的 Groundbait / Feedmix 是怎样组成的？
- Base、Additive、Attractant 分别扮演什么产品角色？
- 自定义 Recipe 是否保留具体 Ingredient identity？
- Flavor / Ingredient 与鱼的偏好是什么关系？
- 鱼偏好是否固定，还是水域 / 世界状态相关？
- Groundbait 是直接修改咬口，还是先形成局部 Feeding Place？
- Feedmix 的空间、时间、投喂历史、过量投喂、颗粒大小如何进入结果？
- 公开证据能否支持“连续语义向量”算法？
- 如果不能，哪种黑盒架构最符合现有证据？

### 1.2 证据等级

本文区分四类信息：

| 等级 | 定义 | 本文用法 |
|---|---|---|
| **A｜官方 / 开发者直接说明** | RF4 当前用户手册、开发者指南、官方版本更新 | 可以写成“RF4 明确存在” |
| **B｜历史官方资料的可靠转录 / 翻译** | 原官方论坛内容的历史翻译、归档 | 用于补充机制演变，需注明历史性 |
| **C｜当前玩家实战数据** | 2026 年玩家配方、点位、社区数据库 | 只证明玩家实践与 Meta，不证明源码 |
| **D｜机制推断** | 根据 A/B/C 证据重建可能架构 | 必须写成“证据一致的推断”，不能写成 RF4 事实 |

---

## 2. RF4 的玩家侧配方结构

### 2.1 Ordinary Groundbait：Base + Additives + Attractants

RF4 当前官方手册把普通 Groundbait 描述为经典的黏性混合物，**主成分是 Base，可以与 Additives 和 Attractants 混合**。Dry Mix 不含液体成分，并且可以不使用 Base。[S1]

官方给出的入门示例非常直接：

```text
Crucian mix
= Ground Crackers + Millet Porridge

Roach mix
= Ground Crackers + Bloodworm
```

也就是说，玩家侧首先看到的是**具体 Ingredient 组合**，而不是一个抽象的“甜度 / 动物性 / 谷物性”控制面板。[S1]

### 2.2 官方 Recipe 只是起点，不是唯一正确答案

当前手册明确说明：Crafting 里的现成 Recipe “并不完美”，玩家可以通过实验和引入新 Component 提高效率。[S1]

同时，RF4 在 2019 年已经加入：

- 自定义 ordinary feed mix recipe template；
- 自定义 dry feed mix recipe template；
- 自定义 PVA string recipe template。[S3]

2024 年仍有补丁专门修复 custom feedmix recipe 数量计算，说明这不是已经废弃的旧功能。[S11]

**重要推论：**Groundbait 的最终效果不能只依赖一个有限集合的预设 Recipe ID；自定义 Recipe 至少需要从 Component 层求值或编译。

### 2.3 Feedmix 还可以吸收更多“真实食物组件”

历史更新明确加入：

- boilies / pellets 可作为 Groundbait additive；
- boilies 可以磨碎后作为 additive；
- 生成 Groundbait 的数量与起始材料数量有关；
- Dry Mix、PVA 等投喂形态继续扩展。[S12]

因此 RF4 的“配方”并不是只在 Base + 香精之间做选择，而是一个相当内容化的 Ingredient 组合空间。

---

## 3. Ingredient / Flavor 与鱼偏好的关系

### 3.1 鱼偏好是 RF4 的显式世界事实

当前官方手册对整体游戏的描述是：每种鱼有自己的 preference、habit、daily activity 和 habitat；**同一种鱼在不同水体也可能表现不同**。[S1]

在鲤鱼 Groundbait 示例里，官方又明确要求：

- 选择“符合该水域鱼偏好”的 pellet flavor；
- 选择“符合该水域鱼偏好”的 boilie flavor。[S1]

这已经足以证明：

```text
Fish Preference
不是纯 Species 常量
```

至少在产品层面它还读取 **Waterbody / Current World State**。

### 3.2 世界重置会改变 bait / lure preference

2025-2026 多次官方更新明确写到：世界状态重置以后，鱼可能改变 habitat，并改变对 bait 和 lure 的 preference。2026-08-20 的全水域重置仍然保持这个机制。[S4][S5]

这意味着 RF4 的“某鱼喜欢某饵”不是百科全书式永久真理，而是一种**可被 Live Ops / World State 改写的动态关系**。

这点对理解 RF4 非常重要：玩家要持续试饵、看当前记录、寻找当前有效组合，而不是只解一次永久最优配方。

### 3.3 “成分更多 → 吸引鱼种更多”是官方直接给出的策略规律

官方手册写明：在 Feedmix 里加入更多 Ingredient，可能吸引更多不同鱼种进入 Feeding Place。[S1]

这条规则至少说明：

```text
更丰富的配方
≠ 单纯把同一目标鱼的 Attraction 数值继续提高
```

它还会扩大 Species Coverage。

因此 RF4 的产品体验天然允许这样的 trade-off：

```text
广谱 Feedmix
→ 可能来鱼更多 / 品种更多
→ 不一定更“纯”

窄目标 Feedmix
→ 覆盖较少
→ 可能更利于特定目标
```

公开资料没有给出具体“纯度”公式，但这个策略方向有官方语义支撑。

---

## 4. Groundbait 不是瞬时 Buff，而是 Local Feeding Place

### 4.1 不同 Mix 会合并成一个 Feeding Place

2024 年开发者 Levo 的 Groundbait & Feeding Q/A 给出目前最直接的机制信息：[S2]

- 不同 Component 的 Feedmix 会形成一个 **united feeding place**；
- 不同 Mix 组合可能产生正面或负面结果；
- 每次 PVA / Feedmix 投放后，局部 fish population 会增加；
- 更高质量的 Feedmix 会带来更好结果。

这里的“population increases”应该按**玩家可观察语义**理解：Feed 会提高该区域的鱼量 / 机会。公开资料不能证明后台真的实例化鱼群并做 Nav 移动，也可能只是局部 candidate / opportunity 权重发生变化。

### 4.2 Feeding Place 有明确空间范围

同一开发者指南明确：

- Feeding 作用半径固定为 **2.5 m**；
- Feeder basket / PVA 在作用区域内会影响其他竿；
- 两个 Feed 区域重叠时，两个 Mix 会共同作用；
- 影响仍会因 Component 不同而不同。[S2]

这使 Groundbait 的最稳妥语义不是：

```text
当前竿 BiteChance +X%
```

而是：

```text
Position + Time + Feed History
→ Local Feeding Context
→ 区域内多竿共享
```

### 4.3 投放方式改变空间分布

当前官方 / 开发者资料至少区分：[S1][S2]

- **SPOMB**：封闭式，落水后打开，适合较大的颗粒，投放更集中；
- **SPOD**：开放式，留下 feed trail，适合小颗粒、较大 Feeding Area；
- **PVA**：保证 Feed 精确落到正在作钓的位置；
- 手抛 / slingshot / cobra：距离、噪声、精度和用途不同。

因此，RF4 的 Feeding 已明确购买到一个 **Spatial Delivery** 层，而不只是 Ingredient Preference。

### 4.4 Feed 有持续性和历史

官方手册要求效果结束后重新补窝；鲤鱼示例给出 15-20 个游戏小时后补喂的操作建议。[S1]

历史官方指南翻译也明确说明：一次 Feed 的效果会持续一段时间，时间与 spot condition / current 有关，成品描述会显示最大有效时间。[S6]

所以：

```text
Groundbait Event
→ Persistent Local State
→ Decay / Expiry
```

比“每次 Cast 当场加权一次”更符合公开机制。

---

## 5. Overfeeding：RF4 明确不是单调“越多越强”

2024 开发者指南明确确认：Active Spot 可以 overfeed。[S2]

Overfeeding 后：

- population 会下降；
- 在一段时间内不能再次提高；
- bite frequency 会明显降低；
- 建议让 Spot 休息；
- 重启游戏不会清除这个效果。

这是非常强的机制证据，因为它证明 RF4 的 Local Feed State 具有：

```text
历史
+ 累计
+ 非单调结果
+ 跨 Session 持续语义
```

因此，RF4 至少不是一个简单的：

```text
FeedAmount ↑
→ BiteChance 永远 ↑
```

系统。

值得注意：开发者还说“不同 Mix 的组合可能有正面或负面效果”，但没有说明这个负面效果究竟来自：

- Ingredient 间冲突；
- 鱼种 Preference；
- 过量投喂；
- Feed Composition 稀释；
- 或其它隐藏机制。

**所以不能据此声称 RF4 存在任意 `Ingredient A × Ingredient B` 的 pairwise synergy / conflict table。**

---

## 6. Particle Size 是另一条独立策略轴

2024 开发者指南直接回答“如何影响鱼的大小”：改变投喂颗粒尺寸。[S2]

其公开策略是：

- 小颗粒更偏向频率；
- 大颗粒更偏向大鱼；
- 可以组合多种颗粒；
- 纯大颗粒策略会牺牲 Bite Rate，换取尺寸提升。

官方手册的鲤鱼示例也直接让玩家同时使用 3 mm、7 mm、12 mm pellet，并根据水域鱼偏好选择 Flavor。[S1]

因此，RF4 明确把至少两类信息分开：

```text
Flavor / Ingredient Preference
→ “什么鱼 / 当前鱼情响应”

Particle Size
→ “频率 / 体型分布”
```

这对我们很重要：**不要尝试把所有策略都压成“味型 Match”。**

---

## 7. Quality：与“Potency”相似，但不能直接等同

2024 开发者指南明确说：更高 Quality 的 Feedmix 会带来更好结果。[S2]

一份 2019 年官方 Groundbait Guide 的中文翻译还记录了更具体的旧机制：Ingredient 星级会影响吸引能力；以 Cheese 为例，更高星级 Cheese 被解释为味道更强、吸引力也更高；多种投喂方式可叠加，但存在上限。[S6]

这为我们的 `Potency` 概念提供了一个很好的**类比**：

```text
同样的 Recipe Share
× 不同单位效果强度
→ 不同 Attraction Contribution
```

但必须守住边界：

> `Potency` 是我们自己的设计语言；RF4 公开术语是 Quality / ingredient quality / stronger smell 等，不能直接说 RF4 内部存在名为 Potency 的字段。

---

## 8. 2026 玩家 Meta：Flavor Identity 明显是可学习内容单位

以下案例属于 C 级证据：它们证明玩家当前确实这样使用系统，但**不证明后台公式**。

### 8.1 Common Carp：White Chocolate / Creme Brulee / Chocolate

2026-08-09 Amber Lake 的玩家记录：[S7]

```text
Hookbait
- Creme Brulee 18
- White Chocolate 25

Groundbait
- Corn Flour
- White Chocolate crushed
- Creme Brulee crushed
- Cream Feed Pellets
- Biscuit
- Chocolate attractant

Dip
- Chocolate
```

玩家实际把 Hookbait、Groundbait、Dip 做成高度一致的 Sweet / Cream / Chocolate flavor family。

### 8.2 Crucian Carp：Coconut & Cream

2026-07-21 Old Burg：[S8]

```text
Hookbait
- Cocos & Cream Pellets
- Cocos & Cream

Groundbait
- Corn Flour
- Coco & Cream Feed Pellets（多粒径）
- Cookies
- Coconut Cream

Dip
- Cocos Nectar
```

### 8.3 Copper Lake F1：Crab Family

2026-08-01 / 08-09 多个记录反复出现：[S9]

```text
Hookbait
- Crab & Fish / Crab & Mussels / Crab corn

Groundbait
- Ground Peas or Corn Flour
- Crab Feed Pellets（多粒径）
- King Crab Feed Pellets
- Crab & Mussels

Dip
- King Crab / Crab & Fish
```

### 8.4 Copper Lake F1：Squid Family

2026-08-11：[S10]

```text
Hookbait
- Squid artificial corn

Groundbait
- Corn Flour
- Red Squid Feed Pellets（多粒径）
- Red Squid
- Squid attractant

Dip
- Squid & Fish Mix
```

这些案例支持一个产品判断：RF4 的深度至少有一部分来自**具体 Flavor / Ingredient Identity 的发现、传播和复用**，而不是玩家学习抽象的隐藏向量。

---

## 9. RF4 到底是不是“向量算法”？

### 9.1 公开资料无法回答源码实现

RF4 没有公开以下内容：

- Fish Preference 的 Schema；
- Ingredient / Flavor 的内部特征字段；
- Feedmix 聚合公式；
- 是否存在 `FishID × IngredientID` 表；
- 是否存在 `FishID × FlavorFamily` 表；
- 是否存在 latent vector；
- Recipe 中每个 Component 的比例如何进入 Fish-specific Attraction；
- Mix 的“正面 / 负面组合”具体怎样求值。

因此我们不能写：

```text
RF4 = direct lookup
```

也不能写：

```text
RF4 = vector similarity
```

### 9.2 四种架构假说

| 假说 | 与公开证据的相容性 | 主要问题 | 当前判断 |
|---|---|---|---|
| **A. 最终 RecipeID × FishID 直接表** | 固定成品 Bait 可以成立 | 自定义 Feedmix 数量开放，无法只靠预枚举最终 Recipe | **不足以解释全部系统** |
| **B. IngredientID × FishID 直接配置后聚合** | 能解释具体 Ingredient identity、自定义 Recipe、动态偏好 | 数据量可能很大；Family 复用未知 | **高度相容** |
| **C. Flavor / Ingredient Family Default + Exact Override** | 能解释大量同 Flavor family 商品、动态偏好和少量例外 | RF4 没公开 Family 层 | **高度相容但未证实** |
| **D. 连续语义 Vector + Similarity** | 理论上也能实现所有结果 | 没有任何公开机制语言或数据证据指向这一层 | **无公开证据支持** |

### 9.3 最符合证据的黑盒重建

如果只做“最少假设”的机制重建，建议写成：

```text
FeedMix
= [Component_1, Component_2, ...]
        │
        ├─ Component identity
        ├─ quality
        ├─ particle size
        ├─ amount / portion
        └─ flavor / bait identity（具体存储方式未知）
        │
        ▼
FishPreference(fish, waterbody/world_state, component)
        │
        ▼
Aggregate Components
（公式未知；可能有 cap / nonlinearity）
        │
        ▼
Local Feeding Place
        │
        ├─ radius = 2.5m
        ├─ duration / decay
        ├─ overlap
        ├─ quality effect
        ├─ particle-size selection
        └─ overfeed state
        │
        ▼
Local Fish Population / Bite Opportunity
```

**这是一份 evidence-consistent reconstruction，不是 RF4 源码。**

---

## 10. 一个关键未知：配方“比例”在 RF4 里到底有多重要？

这是本次调研后仍不能闭合的问题。

目前公开资料能证明：

- Component 组合重要；
- Feed 投放总量重要；
- Ingredient / Feedmix Quality 重要；
- Particle Size 重要；
- Flavor Preference 重要；
- Delivery Geometry 重要；
- Feed 历史与 Overfeeding 重要；
- 起始材料数量会影响 Groundbait 产出数量。[S1][S2][S12]

但当前可访问的官方资料**没有清晰说明**：

> 在同一个 Feedmix 内，把 Ingredient A:B 从 1:1 改成 3:1，是否会连续改变 Fish-specific Attraction；如果会，具体按质量、portion、槽位还是其它方式计算？

当前玩家分享的 Recipe 通常列出 Component，但往往不列百分比，所以也不能仅靠社区配方反推出比例公式。

因此，下面两个模型对 RF4 都仍然是开放的：

```text
模型 1：Presence / Slot-driven
某 Ingredient 只要进入 Recipe，就贡献一个离散效果
```

和：

```text
模型 2：Dose / Share-driven
Ingredient 的用量 / 比例连续改变其贡献
```

**这恰恰是我们自己的台钓设计不能直接照抄 RF4、需要单独做产品裁决的地方。**

---

## 11. RF4 给我们的设计启示：什么值得借，什么不该照搬

本节只写 Reference implication，不构成台钓机制 Adoption。

### 11.1 值得借：Ingredient-first，而不是先造“食品科学空间”

RF4 最强的产品信号不是“科学”，而是：

```text
玩家认识具体 Ingredient
→ 试验具体 Recipe
→ 记住具体 Flavor / Bait
→ 在世界重置后重新试验
→ 社区传播当前有效组合
```

这种结构有几个明显优点：

- Content identity 强；
- Recipe 收集有内容价值；
- 玩家讨论语言自然；
- 策划可以直接 Override；
- Live Ops 可以改变 Preference；
- Debug 时容易回答“哪个 Component 起作用”。

因此，我们没有必要为了“科学”优先建设一个高维 `Feeding Signature Vector`。

### 11.2 Family 可以作为生产压缩层，但不应吞掉 Ingredient Identity

如果我们的鱼种和 Ingredient 数量都很大，纯：

```text
FishID × IngredientID
```

会产生配置爆炸。

一个更像生产系统、但仍保留 Ingredient identity 的候选是：

```text
Ingredient
├─ Family Default
├─ Potency / Strength
└─ Optional Exact Override

Fish / Mode
├─ Family Affinity
└─ Exact Ingredient Override（少量）
```

这里的 Family 是**Authoring Compression**，不是科学真理，也不是必须让玩家看到的连续向量。

### 11.3 Potency 值得保留为候选

RF4 的 Quality / star / stronger-smell 历史机制说明：

```text
Dose
≠ Effective Strength
```

因此我们此前讨论的：

```text
Contribution
≈ Dose × Potency × Affinity
```

仍然是很有价值的生产候选。

但它是我们的算法，不是 RF4 已公开公式。

### 11.4 Groundbait 应保持独立的 Local Context Failure Boundary

RF4 的 2.5 m 区域、跨竿共享、持续、叠加、overfeed 都进一步支持：

```text
Groundbait
→ Local Feed Context / Local Opportunity
```

与：

```text
Hookbait
→ Per-opportunity Presentation Response
```

分开。

即使工程上暂时由同一个 Runtime Package 实现，也不应该在语义上压成同一个瞬时 Response 系数。

### 11.5 我们的“V1 Recruitment 只正向”是有意识的简化，不是 RF4 复刻

我们当前讨论过的候选是：

```text
Groundbait Recruitment Modifier >= 1
```

即不适配的鱼不加权，适配鱼正向增强；鱼种比例通过不同增幅自然变化。

RF4 不能直接作为这条规则的证据，因为 RF4 明确存在：

- overfeeding 后 population / bite frequency 下降；
- 不同 Feedmix 组合可能带来负面效果。[S2]

因此如果我们采用 positive-only Recruitment，应明确理由是：

> **为了保持第一版因果清晰，把真正负向效果延后放到 Overfeeding / Conversion / Deterrence 等独立 Failure Boundary。**

这是 complexity cut，不是“RF4 就是这么做”。

### 11.6 Physical State：RF4 对 Spatial / Temporal 的证据强，对“完整三轴”证据不对称

我们此前讨论过：

- Settling｜沉降（垂直）
- Dispersion｜扩散（空间）
- Persistence｜持续（时间）

RF4 公开资料强力支持：

- **Dispersion / Spatial Delivery**：SPOMB compact、SPOD trail、PVA exact point；
- **Persistence / Temporal**：Feed duration、refeed、overfeed history。

对 **Settling / Vertical**，RF4 的公开 Groundbait 资料相对弱一些；不能因为我们的台钓现实需要，就声称 RF4 已证明一个完整的 Settling 参数体系。

---

## 12. 与当前台钓方向的关系（项目上下文，不是 RF4 证据）

当前项目总览已经把台钓定位成与路亚并行的中国市场策略玩法，并把 **饵料系统、调漂系统、窝料系统（含中鱼适配）**列为核心差异化内容；长线还包含配方收集。

因此 RF4 的参考价值不只在“怎么算鱼权重”，还在它证明了一种可运营的内容结构：

```text
具体 Ingredient / Flavor
+ 自定义 Recipe
+ 当前鱼偏好不断变化
+ 局部 Feed State
+ 社区发现与传播
```

这类内容驱动机制，比“一个鲫鱼饵 +20%”更有机会支撑长期配方探索；同时又不要求我们真的建立食品化学级的高维科学模型。

---

## 13. 下一步如果要继续验证 RF4，最有价值的是做控制变量实验

公开资料已经接近信息上限。若要进一步逼近后台关系，下一步不应继续搜更多攻略，而应直接在游戏内做 A/B Fixture。

### Experiment A｜只换 Attractant

固定：

- 水域 / 点位；
- Base；
- Additives；
- 投喂量；
- Particle Size；
- Hookbait；
- 时间窗口。

只替换 Attractant，统计：

- bite frequency；
- species composition；
- size distribution；
- onset time。

目的：判断 Attractant 更像“通用 Strength”还是“Species-specific Preference”。

### Experiment B｜同 Flavor Family，不同具体 Item

例如同为 Crab / Cream / Garlic family，替换具体商品。

目的：判断 Family Default 是否足以解释，还是 Item identity 有稳定独立效应。

### Experiment C｜同 Ingredients，不同配比

前提是当前 Crafting UI 允许严格控制 Component 用量。

目的：直接验证本次最大未知：

```text
Recipe Composition Ratio
是否连续进入 Fish Response
```

### Experiment D｜同 Recipe，不同 Quality

目的：拆开：

```text
Ingredient identity
vs
Quality / effective strength
```

### Experiment E｜同 Recipe，不同 Feed Amount / Cadence

目的：确认：

- 单调区；
- 饱和区；
- Overfeed 边界；
- 恢复时间。

### Experiment F｜世界重置前后复测

目的：确认哪些 Preference 是：

```text
Ingredient 固有属性
```

哪些是：

```text
World-state / Waterbody Override
```

---

## 14. 当前最稳妥的 RF4 机制摘要

如果要给团队只讲一分钟，可以用这段：

> RF4 的 Groundbait 不是一个固定“鱼种加成饵”。玩家用具体 Base、Additive、Attractant、pellet、boilie 等 Component 组成自定义配方；鱼对 bait / flavor 的偏好会因水域和世界状态改变。投喂后，系统在空间上形成持续的 Feeding Place，不同 Component 的 Mix 会共同作用，Feed 品质、颗粒大小、投放方式、持续时间和累计投喂都会改变结果，过量投喂还会造成反效果。公开资料没有披露 Fish × Ingredient 的具体数据结构或公式，也没有证据支持高维语义向量；从可观察 Contract 看，更像“具体 Component 配置驱动 + 局部状态聚合”。

---

## 15. Source Map

### A 级｜官方 / 开发者直接资料

**[S1] RF4 Current User Guide — Groundbait / General fish preferences**  
Russian Fishing 4 官方用户手册（PL 当前镜像）  
https://rf4.pl/userguide/  
关键证据：Base + Additives + Attractants；Dry Mix；预设 Recipe 非最优；更多 Ingredient 吸引更多鱼种；按当前水域鱼偏好选 Flavor；投放方式与补窝时间；同鱼种不同水域可有不同习性。

**[S2] RF4 Groundbait and Feeding — Levo, 2024-04-18**  
Steam Community Guide（开发者 Levo）  
https://steamcommunity.com/sharedfiles/filedetails/?id=3225629635  
关键证据：united feeding place；不同 component 影响不同；quality；2.5m；跨竿；重叠；overfeed；particle size；SPOMB / SPOD / PVA。

**[S3] RF4 Patch — 2019-12-24**  
https://steamdb.info/patchnotes/4523359/  
关键证据：玩家可保存自定义 ordinary feed mix、dry feed mix、PVA string recipe template。

**[S4] RF4 Patch — 2026-08-20**  
https://steamdb.info/patchnotes/24827700/  
关键证据：全水域 world reset；鱼可能改变 habitat 与 bait/lure preference。

**[S5] RF4 Patch — 2026-05-22**  
https://steamdb.info/patchnotes/23352218/  
关键证据：world reset 后鱼可能改变 habitat 和 bait/lure preference；说明该动态机制并非一次性事件。

**[S11] RF4 Patch — 2024-08-21**  
https://steamdb.info/patchnotes/15438263/  
关键证据：仍在维护 custom feedmix recipe 数量计算。

**[S12] RF4 historical patch/news — Groundbait crafting expansion**  
https://store.steampowered.com/news/posts/?appgroupname=Russian+Fishing+4&appids=766570HELP&enddate=1577178402  
关键证据：boilie / pellet 可作为 Groundbait additive；boilie 可 crushed；Groundbait 数量受起始材料数量影响；Dry Mix / PVA 扩展。

**补充：Levo 2023 Groundbait reply**  
https://steamcommunity.com/app/766570/discussions/9/3812911928390023484/  
关键证据：Groundbait 会吸引区域内更多鱼；分散投放扩大作用区，重复投到同一区域增加 Attraction。

### B 级｜历史官方指南翻译 / 归档

**[S6] 2019 RF4 Groundbait 官方指南中文翻译**  
https://nightkid5566s.wordpress.com/2019/11/01/russianfishing4-groundbait/  
关键证据：历史版本中 Ingredient 星级影响 Attraction；更强味道对应更强吸引；持续时间；2.5m；多投喂手段叠加但有上限。  
注意：这是第三方翻译，且机制可能随后迭代；只作历史补充。

**RF4 Japanese Current/Localized User Guide**  
https://rf4game.jp/userguide/  
补充证据：Attractant 被描述为强力诱鱼 Component；Clay 增加黏度与持续；组合 Base/Additive 可提升效果。

### C 级｜2026 玩家实战数据

**[S7] Amber Lake — Common Carp — 2026-08-09**  
https://rf4hub.com/en/fishing-spots/the-amber-lake-common-carp-2026-08-09-927245

**[S8] Old Burg — Crucian Carp — 2026-07-21**  
https://rf4hub.com/en/fishing-spots/old-burg-lake-crucian-carp-2026-07-22

**[S9] Copper Lake — F1 — Crab family — 2026-08-01**  
https://rf4hub.com/en/fishing-spots/copper-lake-f1-2026-08-01-716677

**[S10] Copper Lake — F1 — Squid family — 2026-08-11**  
https://rf4hub.com/en/fishing-spots/copper-lake-f1-2026-08-11-868981

**Old Burg — Bream — Anise / Garlic examples — 2026-08**  
https://rf4hub.com/en/fishing-spots/old-burg-lake-bream-2026-08-01  
https://rf4hub.com/en/fishing-spots/old-burg-lake-bream-2026-08-06

### C/D 边界｜社区机制讨论

**Groundbait information — 2021**  
https://steamcommunity.com/app/766570/discussions/9/3047230768367765850/  
社区回答称具体鱼的 Groundbait preference 主要靠实验发现，现实偏好有时只能提供弱提示。用于理解玩家知识获取方式，不作为后台公式证据。

---

## 16. 明确未闭合的问题

| 问题 | 当前状态 |
|---|---|
| RF4 是否存在 `FishID × IngredientID` 直接表 | **UNKNOWN** |
| RF4 是否存在 Flavor Family 中间层 | **UNKNOWN** |
| RF4 是否使用连续语义 Vector | **NO PUBLIC EVIDENCE** |
| Feedmix 内 Component 比例是否连续影响 Species Response | **UNKNOWN / 值得实测** |
| 不同 Mix 的“负面组合”具体由什么机制产生 | **UNKNOWN** |
| Flavor 对 Hookbait 与 Groundbait 是否共享同一 Preference 值 | **UNKNOWN** |
| 2.5m Feeding Radius 是否在所有当前玩法 / 水域都无例外 | 开发者指南写为 always；实际边缘情况仍可实测 |
| “fish population increase”是物理鱼群移动还是机会权重抽象 | **UNKNOWN** |

---

## 17. 本文不做的裁决

本文**不裁决**我们最终应该采用：

- `Ingredient × Fish` 直接表；
- Family Default + Exact Override；
- Feeding Signature Vector；
- Groundbait 正向-only；
- Overfeeding 是否进入首版；
- 台钓 Hookbait 与 Groundbait 是否共用同一套 Affinity。

这些属于后续 Product / Mechanism Design。本文只提供 RF4 外部证据与证据一致的设计空间缩窄。
