# RF4 自定义饵 / 窝料聚合机制复盘与台钓配方算法建议

> **文档状态**：Design Research / Working Proposal，非 FCF Current / Approved / Promotion  
> **日期**：2026-10-27  
> **来源**：2026-10-27 已完成的 Deep Research《RF4 自定义饵 / 窝料聚合机制复盘与台钓配方算法建议》。本 GitHub 版本保留其主要研究结论、数值 Fixture、公式、方案、风险及验收项，按 Markdown 整理。  
> **证据边界**：RF4 内部配方聚合公式未公开；下文算法、数值 Fixture、参数及推荐均属于 FCF 设计推演，不是 RF4 源码事实。  
> **兼容性提醒**：本文提出的 `EffectTargetKey`（尤其“果香 / 蒜香”等）是研究提案，**不得自动视为已批准的 `FeedingTargetKey` 或化学 Cue Contract**；后续须按 FCF Authority 单独审查。本文不修改 Notion Current。

## 结论摘要

第一版**不建议直接采用全 Ingredient 线性加权**，也不建议逐 Ingredient 独立饱和。研究建议测试一个 Hybrid：

**同作用 Target 先聚合 → Target 级边际递减 → 小药独立剂量上限 → 有限 Recipe Grammar**。

其设计动机是同时处理三个风险：

1. **单品统治**：线性加权在固定预算下，单目标鱼通常把份额分配给系数最高的 Ingredient。
2. **拆分套利**：逐 Ingredient 凹函数饱和使一个等效成分拆成多个 ID 后凭空变强。
3. **多 Target 堆叠**：Target 级饱和虽然允许内部混配最优，但可能把策略变成“每个不同 Target 都加一点”。

推荐优先用**稀疏鱼种偏好、主攻最多两槽、同 Target 合并、小药限额**控制第三类风险，而非立即叠加 DiversityPenalty、Pair Synergy 或高维 Flavor Vector。

**重要限定**：这是待验证的 Working Proposal。Target 分组的语义是否足够稳定、混配策略是否真有深度、添加小药是否始终支配不添加，均需 Fixture 验收；不应直接提升为生产方案。

## 一、RF4 证据回顾

公开资料支持 RF4 是 **Component-centric（成分中心）**的配方系统：普通 Groundbait 包含 Base、Additives、Attractants；玩家可以保存自定义 Feedmix；不同 Component 的 Mix 可共同形成 Feeding Place；鱼对 bait / flavor 的偏好可随水域和世界状态变化。

RF4 的策略深度并不全来自“味型公式”。开发者资料将 Feeding Place 的空间、持续时间、投放重叠、Quality、particle size、overfeeding 分开讨论。由此可以区分：

- 配方是否适合鱼种；
- 投放之后窝点如何随时间、空间和历史演化；
- 钩饵 Presentation 与鱼的即时 Response。

| RF4 公开证据 | 来源等级 | 支持的判断 | 不支持的推断 |
|---|---|---|---|
| 普通 Groundbait 由 Base + Additives + Attractants 构成；自定义配方可选不同 Ingredient | 官方指南 | 配方围绕具体 Component；覆盖鱼种是策略维度 | 无法证明内部是线性、向量或协同表 |
| 2019 增加自定义 ordinary feed mix / dry mix / PVA 模板；后续仍维护 custom feedmix | 官方补丁 | 不能仅靠预枚举固定 RecipeID 表覆盖所有自定义配方 | 不能确定求值发生在制作时还是 Runtime |
| 不同 Component Mix 可进入 united feeding place；有 2.5m、重叠、Quality、particle size、overfeeding 等规则 | 开发者资料 | Groundbait 是持续的局部 Feeding State | 不足以推出任意 Ingredient Pair Synergy |
| World Reset 可能改变鱼的 habitat 和 bait / lure preference | 官方补丁 | Fish Preference 可以随世界 / 水域状态变化 | 动态偏好不代表必须使用复杂聚合公式 |
| 玩家围绕 Chocolate/Cream、Crab、Squid 等味型搭配钩饵、窝料、Dip | 玩家经验 | 具体 Ingredient / Flavor identity 是可学习和传播的知识单位 | “同味搭配”不能证明后台存在额外组合 Bonus |

**仍然未知**：RF4 的 Ingredient × Fish 数值表、Flavor Family 具体结构、是否采用连续向量、具体聚合公式，以及同一 Feedmix 中 A:B 从 1:1 改为 3:1 是否连续改变鱼种吸引力。Presence/Slot-driven 与 Dose/Share-driven 解释仍然开放。

主要资料：

- [RF4 Current User Guide](https://rf4.pl/userguide/)
- [RF4 Groundbait and Feeding — Levo, 2024](https://steamcommunity.com/sharedfiles/filedetails/?id=3225629635)
- [2019 Custom Feedmix Patch](https://steamdb.info/patchnotes/4523359/)
- [2026 World Reset / bait preference](https://steamdb.info/patchnotes/24827700/)
- [此前 RF4 深度调研](https://github.com/futouyiba/programaticHitFish/blob/main/docs/research/2026-10-21-rf4-bait-groundbait-mechanism-deep-research.md)
- [此前配方聚合风险记录](https://github.com/futouyiba/programaticHitFish/blob/main/docs/research/2026-10-26-groundbait-recipe-aggregation-risk-research-snapshot.md)

## 二、候选算法与数值攻击

### 2.1 人工 6 Ingredient × 5 Fish Fixture

**仅用于攻击算法行为，不是 RF4 数据或 FCF 平衡定值。**

| Ingredient | 角色 / Target | 鲫鱼 | 鲤鱼 | 鳊鱼 | 白条 | 鲢鳙 |
|---|---|---:|---:|---:|---:|---:|
| 玉米粉 | 基础 / 谷物 | 0.70 | 0.85 | 0.55 | 0.35 | 0.20 |
| 面包屑 | 基础 / 谷物 | 0.65 | 0.55 | 0.75 | 0.75 | 0.45 |
| 红虫 | 主攻 / 虫饵 | 0.90 | 0.35 | 0.85 | 0.90 | 0.15 |
| 虾粉 | 主攻 / 甲壳 | 0.55 | 0.90 | 0.45 | 0.25 | 0.10 |
| 黑加仑小药 | 小药 / 果香 | 0.75 | 0.95 | 0.45 | 0.30 | 0.15 |
| 大蒜小药 | 小药 / 蒜香 | 0.60 | 0.45 | 0.85 | 0.75 | 0.20 |

### 2.2 三种候选

| 候选 | 数学定义 | 主要收益 | 退化策略 | 主要成本 |
|---|---|---|---|---|
| **A：线性加权** | `Q_f = Σ_i s_i E_{if}`，`Σs=1` | 极简、可 Trace、同效 ID 拆分不套利 | 单鱼目标集中于系数最高的成分 | Ingredient × Fish 矩阵 |
| **B：Target 级饱和** | `X_{ft}=Σ_{i∈t}s_iE_{if}`；`Q_f=Σ_t(1−exp(−k_tX_{ft}))` | 同 Target 合并；可产生内部混配最优 | 有效 Target 越多越有利的拼盘 | Target 分类与 `k_t` |
| **C：角色分道 + 小药限额** | `Food=Σsolid sE`；`Attr=min(Cap,dE)`；`Q=Food+Attr` | 边界清楚、便宜、小药受控 | 主体仍逐角色选择最强成分 | A + Recipe Grammar + Cap |

统一单调函数 `Sat(Σ_i s_i E_{if})` 不能改变单鱼最优排序；它只改变分值尺度，不改变最大值的位置。

### 2.3 A 的单品统治

固定玉米粉 60%，主攻预算 40% 在红虫和虾粉之间分配，只看鲤鱼：

| 红虫 | 虾粉 | A 线性鲤鱼分 |
|---:|---:|---:|
| 0% | 40% | **0.870** |
| 10% | 30% | 0.815 |
| 20% | 20% | 0.760 |
| 30% | 10% | 0.705 |
| 40% | 0% | 0.650 |

因为 `E_{虾粉,鲤}=0.90 > E_{红虫,鲤}=0.35`，最优解是 **40% 全虾粉**。中间混合只是加权平均。若其他约束不变，玩家容易把配方当成查表题。

### 2.4 逐 Ingredient 饱和的拆分套利

设：

~~~text
Q = Σ_i [1 − exp(−10 s_i)]
~~~

固定有效份额 10%，只改变等效成分的 ID 数量：

| 配置 | 输出 |
|---|---:|
| 1 个等效成分 × 10% | 0.632 |
| 2 个等效成分 × 5% | 0.787 |
| 5 个等效成分 × 2% | 0.906 |

实际信号没有增加，结果却变强。因此**不能按 Ingredient ID 各自重置饱和曲线**。任何饱和都必须在等效信号完成合并后发生。

### 2.5 B 的内部混配最优

对同一 Target 先合并：

~~~text
X[f,t] = Σ_{i∈t} share[i] × E[i,f]
Q[f]   = Σ_t (1 − exp(−4 × X[f,t]))
~~~

仍固定 60% 玉米粉，40% 在虫饵 / 甲壳 Target 间分配：

| 虫饵 | 甲壳 | A：线性鲤鱼 | B：Target 饱和鲤鱼 |
|---:|---:|---:|---:|
| 0% | 40% | **0.870** | 1.355 |
| 10% | 30% | 0.815 | **1.381** |
| 20% | 20% | 0.760 | 1.325 |
| 30% | 10% | 0.705 | 1.178 |
| 40% | 0% | 0.650 | 0.916 |

在这个人工 Fixture 中，**10% 虫饵 + 30% 甲壳**优于 40% 甲壳。原因不是显式“虫 + 虾 Synergy +20%”，而是甲壳 Target 已进入边际递减区，转移少量预算到另一个有响应的 Target 可能更有效。

这说明 B *可以*产生内部最优，不代表它对所有鱼或所有内容集都能产生健康策略。

### 2.6 B 的反噬：多 Target 拼盘

在研究报告的一组人工 Fixture 中，固定 60% 谷物，将其余 40% 分给越来越多、对鲫鱼都有正响应的 Target，得到：

| 有效 Target 数 | 报告中的相对分 |
|---:|---:|
| 1 | 1.332 |
| 2 | 1.412 |
| 3 | 1.523 |
| 4 | 1.537 |

这组数值来自研究推演示例，**不是 RF4 实测**，具体扩展 Target 的系数未在原报告中完整列出，不能将其视为可独立复算的 6×5 标准 Fixture。

结构性风险明确：解决“单品统治”后，最优策略可能退化成**尽可能搜集更多不同 Target**。Target 级饱和必须与 Recipe Grammar、鱼偏好稀疏性共同验收。

### 2.7 C 的边界价值与不足

对 `60% 玉米 + 40% 虾粉` 加标准剂量小药，设单鱼 Attractant 最大贡献暂取 0.12：

| 配方 | 鲫鱼 | 鲤鱼 | 鳊鱼 | 白条 | 鲢鳙 |
|---|---:|---:|---:|---:|---:|
| 主体，无小药 | 0.640 | 0.870 | 0.510 | 0.310 | 0.160 |
| + 黑加仑 | 0.753 | **0.990** | 0.578 | 0.355 | 0.183 |
| + 大蒜 | 0.730 | 0.938 | **0.630** | **0.423** | 0.190 |

小药有明显修正作用，但不应完全替代主攻饵。然而 C 没有解决主体的单品统治，所以适合作为 **Recipe Grammar / Attractant Boundary**，而非独立完整的聚合机制。

另外，若小药始终正向、无真实成本且允许不占主体份额，则“加一点小药”仍可能严格支配“不加”。**Dose Cap 限制幅度，并不自动解决支配关系**；需在后续测试中加入实际成本、鱼种干扰或其他有依据的取舍。

### 2.8 可复现的算法骨架

~~~python
from collections import defaultdict
from math import exp

def linear(recipe, E, fish):
    return sum(share * E[ingredient][fish]
               for ingredient, share in recipe.items())

def target_saturation(recipe, E, target_of, fish, k=4.0):
    exposure = defaultdict(float)
    for ingredient, share in recipe.items():
        exposure[target_of[ingredient]] += share * E[ingredient][fish]
    return sum(1.0 - exp(-k * value) for value in exposure.values())

def role_split(food_recipe, attractant, E, fish, attr_cap=0.12):
    food = linear(food_recipe, E, fish)
    if attractant is None:
        return food
    attractant_bonus = min(attr_cap, 0.15 * E[attractant][fish])
    return food + attractant_bonus
~~~

## 三、研究推荐机制：B + C Hybrid

### 3.1 固体份额预算

~~~text
基础饵 + 主攻饵 + 状态饵
Σ_{i∈Solid} share[i] = 1
~~~

状态饵占固体预算；如果未来改善雾化、持钩或持续时间，它不能成为免费 Buff。比如 15% 状态饵意味着相应的 15% 不再用于其他固体诱食信号。

**但状态饵的具体物理效果目前是 TODO，不得仅凭配方名自动获得额外加成。**

### 3.2 同 Target 先合并

研究提案为 Ingredient 标注一个离散 `EffectTargetKey`，例如谷物、虫饵、甲壳，以及尚待语义审查的果香、蒜香、奶香。

对鱼 `f`、Target `t`：

\[
X_{f,t}=\sum_{\substack{i\in Solid\\target(i)=t}}s_iE_{i,f}
\]

这里 `E[i,f]` 仍是具体 Ingredient × Fish 的 Bake 结果。因此红虫 A 与红虫 B 可以拥有不同的 `E[i,f]`，但若属于同一等效 Target，应先合并为同一 Exposure，再饱和。

**Authority 风险**：现有 FCF `FeedingTargetKey` 主要描述可摄食目标；“果香 / 蒜香”等化学线索不应未经审查直接塞入同一个已批准 Target 字典。研究建议在落实前拆清“食物目标”和“化学线索”的语义归属。

### 3.3 Target 级边际递减

\[
H_{f,t}=1-e^{-k_tX_{f,t}}
\]

\[
FoodFit_f=\sum_tH_{f,t}
\]

`FoodFit` / `RecipeFit` 是相对强度，不是概率，因此没有必要强制位于 0～1。真正的投放量、时间、历史、空间、过量投喂效果应留给下游 Feeding Place 处理，而非全压进 RecipeFit。

### 3.4 小药剂量边界

小药不参与固体 100g 质量预算，使用独立 `DoseUnit`；研究提出将剂量换成有上限的 Exposure：

\[
A_{f,t}=\min\left(A_{cap},\sum_j d_jE_{j,f}\right)
\]

候选统一式：

\[
RecipeFit_f=\sum_t\left[1-e^{-k_t(X_{f,t}+\gamma A_{f,t})}\right]
\]

研究意图：小药进入对应的边际递减通道，而非无限累加固定 Bonus。不过其物理含义、是否能与食物 Target 共用饱和曲线、以及零成本正向小药的支配性，都**尚未验证**。

### 3.5 Recipe Grammar 首轮参数（仅 Fixture，不是定案）

| 项目 | 建议测试范围 | 理由 |
|---|---|---|
| 基础饵 | 1 槽，固体质量 50–70% | 保留主体，避免 100% 主攻化 |
| 主攻饵 | 1–2 槽，合计 20–40% | 两槽允许有限互补，抑制无限拼盘 |
| 状态饵 | 0–1 槽，0–20%，占固体预算 | 状态收益应承担份额机会成本 |
| 小药 | 0–1 槽 | 暂不引入多小药组合复杂度 |
| 小药计量 | 标准 `DoseUnit` | UI 后续再决定 ml/g |
| `k_t` | 未指定；建议首测 2.5–5.0 | 在归一化 Exposure 上制造有限边际递减 |
| `A_cap` | 未指定；建议等效 Exposure 0.03–0.08 / 标准批次 | 小药有存在感，但不替代主体 |
| 玩家配比步长 | UI 5% 或“份” | 避免精确到 17.3% 的数学极值玩法 |

### 3.6 防止多 Target 越多越好

优先测试三个约束：

1. **鱼种偏好稀疏**：某鱼在当前 World State 下只有 1 个 Primary、1–2 个 Secondary，其余 Weak/None；不能让十几个 Target 都有中高正响应。
2. **主攻最多两槽**：即使某鱼偏好三个 Target，也不能无成本全部塞入。
3. **同 Target 合并**：红虫、蚯蚓粉、虫粉若被判定为同作用 Target，不能因商品 ID 不同而重复获得饱和曲线重置。

只有这些仍无法阻止“全家桶”，才考虑新增条件关系。**不建议首版增加 DiversityPenalty、IngredientCountPenalty、PurityPenalty、任意 Pair Synergy 或 Flavor Vector。**

### 3.7 与 FCF 其他层的因果边界

~~~mermaid
flowchart TD
    R[Base + Target + State] --> X[Recipe Target Exposure]
    A[0–1 Attractant + Dose Cap] --> X
    X --> H[Target-level Diminishing Return]
    H --> Q[RecipeFit / Source-local Facts]
    Q --> G[Groundbait Local Feeding Place]
    Q --> B[Hookbait Presentation / Response]
    G --> L[Amount / Time / History / Overfeed]
~~~

该图是研究层级草图，**不代表已经批准的 Runtime Contract**。Groundbait 应影响局部 Feeding Context / Fish Opportunity，Hookbait 应通过 fish-independent Presentation/Cue → Species × EngagementMode Response；不应在配方层直接输出 BiteChance，也不能因“同味”重复加成。

## 四、Authoring 与可维护性

### 4.1 避免逐格手填 Ingredient × Fish

假设 84 Fish × 100 Ingredient = 8400 cells。Runtime 表并不大，真正成本在策划生产、解释和调试。

研究建议：

~~~text
Fish Archetype
    ↓
FamilyAffinity Default
    + Waterbody / World Preference
    ↓
Ingredient
  ├─ EffectTargetKey
  ├─ Authoring Strength
  └─ Exact Override
    ↓
Bake
    ↓
E[Ingredient][Fish]
~~~

Family Default 是 Authoring 压缩层，不是必须暴露给 Runtime 的科学模型。具体 Ingredient identity 保留，通过少量 Exact Override 表达例外。

建议的 Authoring 流程：

1. Fish × Family 使用 `NONE / LOW / GOOD / BEST` 离散档，工具映射数值。
2. Ingredient 选择一个主 Target。
3. 通过 `FamilyAffinity × Ingredient Strength` 生成默认 `E[i,f]`。
4. 仅特殊关系填写 Exact Ingredient × Fish Override。
5. World / Waterbody Preference 优先修改 Fish × Family，而非复制全矩阵。
6. Bake 后 Runtime 读取 IngredientID、TargetKey、E[Fish]、Recipe Share。
7. Debug Trace 展示每个 Target 内各 Ingredient 贡献、合计 Exposure 和饱和后结果。

至少配备 Matrix Heatmap、Family 批量生成、Override Diff、Recipe Simulator、Fish Ranking Compare、Pareto 检查、Split-invariance 自动测试、异常值扫描。

研究提出首轮观察指标：**Exact Override 占完整矩阵的比例约 ≤10–15%**。这是经验性目标，不是已经验证的硬标准；若长期远超，说明 Family / Target 抽象未必降低维护成本。

### 4.2 Debug Trace 示例

~~~text
鲤鱼
谷物 Target:
  玉米粉 60% × E 0.85 = 0.510
  Exposure = 0.510
  Saturated = ...
甲壳 Target:
  虾粉 30% × E 0.90 = 0.270
  Exposure = 0.270
  Saturated = ...
果香 / 化学线索（语义待审）:
  黑加仑 Dose ...
~~~

## 五、必须通过的验收 Fixture

| 测试 | 输入 | 预期 | 首轮判定 |
|---|---|---|---|
| 同 Target 拆分不套利 | 30% 红虫 vs 15% 等效红虫 A + 15% B | 等效输出一致 | 差异 ≤1% |
| 单 Target 可专精 | 某鱼仅强响应甲壳，主攻两槽 | 全甲壳胜过无意义混合 | 不强迫所有鱼都混配 |
| 双 Target 内部最优 | 同时响应虫饵与甲壳，固定预算 | 非端点配比胜过两端 | 至少一组提升约 3–10% |
| 第三弱 Target 不统治 | 优秀双 Target 中加入第三弱 Target | 不应稳定上涨 | 收益 ≤2%，或预算稀释后下降 |
| 小药不可统治 | 差主体 + 最大合法小药 vs 好主体无小药 | 小药不能跨越完整品质档 | 总 RecipeFit 影响建议 ≤10–20%；另查“始终添加”支配性 |
| World Preference 排序反转 | 同 Recipe 集合切换水域 / 世界偏好 | 部分 Top Recipe 改变 | 目标鱼 Top-3 合理变化，不是全鱼随机翻 |
| 状态饵承担成本 | 0% vs 15% 零诱食 State Ingredient | Food Exposure 下降 | 物理效果未落实前不能免费 Buff |
| 内容扩展可维护 | 新增 20 Ingredient + 5 Fish | 多数值由 Default 自动生成 | Override 约 ≤10–15%，无 N² Pair 配置 |

另外应新增两项 **Authority / 语义测试**：

- **Target 标签拆分不套利**：同一有效信号不能仅因被命名成“果香 A / 果香 B”就获得双倍边际收益。
- **食物目标与化学线索不串线**：`FeedingTargetKey`、`chemical_signature`、Groundbait Feeding Context、Hookbait Response 之间不得出现未经批准的隐式映射或重复计分。

验收的目标不是“不同配方分数不同”，而是出现真正的**非支配策略、合理内部取舍、鱼种间差异、动态鱼情下可解释的变化、玩家可从反馈学习、策划可定位原因**。

## 六、风险分级

| 优先级 | 风险 | 退化表现 | 研究建议 |
|---|---|---|---|
| P0 | 多 Target 拼盘统治 | 每种味道都加一点 | 主攻最多两槽、稀疏偏好、同 Target 合并、第三弱 Target Fixture |
| P0 | 明牌 / 攻略化 | 查表即可找到唯一配方 | 不公开精确 E/RecipeFit；慢周期水域偏好；提供趋势反馈 |
| P0 | 拆分套利 | 五个近似商品强于一个等量商品 | Saturation 在等效 Target 聚合后；新 Ingredient 跑 split test |
| P1 | Family 吞掉 Item identity | 同类商品只是换皮 | Item-level E、少量 Override、成本 / 状态 / Quality 区分 |
| P1 | 数据维护爆炸 | 84 Fish × Ingredient 全手填 | Family Default、Override Diff、覆盖率报警 |
| P1 | 小药替代主攻 | 少量小药决定绝大部分效果 | 单槽、Dose/Exposure Cap；验证机会成本和支配性 |
| P2 | 过度数学化 | 玩家研究 17.3% / 12.7% 精确极值 | 5% 或“份”步长；不暴露精确函数 |
| P2 | 黑箱总分 | 雾化、粒径、过量投喂全混进一个 Q | RecipeFit、Physical State、Local Feeding Place 分层 |

## 七、研究结论与下一步

**RF4 的公开资料不能证明它采用 Target Saturation。** 更稳妥的借鉴对象是 RF4 已体现的产品结构：具体 Ingredient / Flavor identity、自定义 Recipe、动态 Fish Preference、局部 Feeding Place，以及玩家实验、知识发现和社区传播。

在当前三个候选中，研究认为值得首先验证的最小非线性是：

~~~text
Same Target Aggregation
→ Target-level Diminishing Return
~~~

它能在人工 Fixture 中产生内部混配最优，并避免按 Ingredient ID 拆分套利；但也会引入多 Target 拼盘风险，需要先用现有 Recipe Grammar 和稀疏 Preference 测试。

**下一步**：选择 20–30 个真实台钓 Ingredient、5–8 条代表鱼，建立固定 Family Default / Item Override 数据，使用完全相同的 Fixture 对照 A、B、Hybrid。只有当 Hybrid 仍稳定产生第三、第四弱 Target 堆叠，或无法提供足够的内部混配最优时，才考虑更复杂的角色条件关系。首版不引入任意 Ingredient × Ingredient Pair Table。

### 仍待对抗性 Review 的问题

1. `EffectTargetKey` 是否只是额外的标签复杂度？食物目标和化学味型是否应分离？
2. 在单鱼目标、固定槽位下，B 的最优配比是否仍然容易被攻略固定？
3. 如果小药没有机会成本，“加满一个小药”是否仍是支配策略？
4. 多 Target 的饱和曲线是否造成 Target 标签命名套利？
5. Recipe 层新增的参数、规则和工具成本是否真的低于直接的 Ingredient × Fish 表？
6. World / Waterbody Preference 的动态变化是否可观察、可学习，而非用隐藏随机数掩盖明牌？

这些问题均保持 **Open**。研究结论不等于设计批准。
