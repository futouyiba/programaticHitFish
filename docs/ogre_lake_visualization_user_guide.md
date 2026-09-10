# Ogre Lake 手工空间切块成本实验：使用说明

Document status：**RETAINED / explanatory guide**  
Authority：**可视化说明；非 FCF V1 mechanism contract**  
Scope：Ogre Lake overlay visualization and reader guidance.  
Reproduction：配套 HTML 与 `ogre_lake_reproducible_overlay_experiment.md`。  
V1 promotion rule：仅解释 evidence，不产生或升级机制参数。

> 本说明对应第一版教学图。第一版 `96` 是示意参数。用于评审和对外演示时，
> 请优先使用 [可复核 Overlay 实验](ogre_lake_reproducible_overlay_experiment.md)
> 及 `ogre-lake-exact-overlay-standalone.html`。

## 1. 它是什么意思

Ogre Lake 是一个 **spatial authoring cost pressure test**。它用一座约
`200m × 200m`、最大水深 `20–30m` 的假想湖泊，演示：如果 Habitat Patch
必须由策划作为静态、内部属性一致的空间单元维护，随着 Depth、Grass、
Structure、Substrate、Shade、Temperature、DO 等条件逐层加入，原本自然、
完整的区域会怎样被互不重合的边界切碎。

它不决定 FCF 最终采用 Manual、Procedural 或 Runtime Query，不模拟鱼量或
鱼行为，也不声称图中的 `96` 是生产地图的精确答案。数量是一组内部一致的
示意估算；应关注增长方式、边界交叉和变更传播，而不是把数值当作生态结论。

## 2. 先理解三个词

- **Meaningful region**：人能给出一个明确名称的区域，如“西北浅水草区”或
  “东南深坑”。
- **Manual patch**：为了让全部作者属性在区域内部保持一致，实际必须维护的
  稳定空间单元。
- **Boundary**：某项属性改变的位置。新边界如果不沿着旧边界，就会穿过并
  split 旧 Patch。

因此，一个“草区”可以是一个 meaningful region，却因为横跨浅水/深水、
晨阴/午阴和不同温度而成为多个 Manual Patch：

```text
自然区域 + 多套不重合边界
→ 取空间交集
→ 内部属性一致的 Patch 数量增长
```

## 3. 界面怎么用

界面分为四部分：

1. 顶部 Layer 选择器：在 `0`–`10` 之间前后切换；
2. 湖泊平面图：显示截至当前层累计加入的边界；
3. 右侧说明：回答新 boundary、必须 split、可 merge、策划维护和重编范围；
4. 下方曲线与表格：显示从 `1` 到约 `96` 个 Patch 的累计过程。

推荐从 Layer 0 开始，每次只前进一步。先看地图新增了哪条线，再读右侧五项，
最后看 Patch 增量。直接跳到 Layer 10 会看到“很碎”，但看不到为什么碎。

## 4. 推荐阅读路径

### 4.1 Layer 0：建立基准

基础湖泊只有岸线。湖岸虽然曲折，只要湖内尚无不同属性，整个水体仍可作为
一个 Region、一个 Patch。后面所有增量都与此基准比较。

### 4.2 Layer 1–4：看静态物理边界

- Depth 加入浅滩、drop-off 和深坑；
- Vegetation 加入草区、草边和浮萍/间植区；
- Structure 加入石区、沉木和桥墩；
- Substrate 加入泥/沙、砾石/硬底过渡。

每一步都问：“新线是否与旧线重合？”如果草区斜穿三条等深线，它不是简单
新增一个草 Patch，而是在每个被穿过的深度 Patch 中分别产生有草/无草交集。
到 Layer 4，示意估算已从 `1` 增长到约 `27`。

### 4.3 Layer 5：重点看 Shade

进入 Shade 层后，切换 `Morning`、`Afternoon`、`Dusk`。关键不是阴影面积，
而是阴影边缘会移动。同一个草区为了在静态 Patch 中表达晨午差异，可能必须
提前拆成：

| 稳定子区 | Morning | Afternoon |
|---|---|---|
| A | Shade | Light |
| B | Light | Shade |
| C | Shade | Shade |
| D | Light | Light |

只有所有支持时段的状态向量都相同，相邻 Patch 才能安全 merge。加入更多时段、
季节或天气，会引入更多可能的稳定状态组合。

### 4.4 看 Depth × Grass × Shade

观察西侧草区：Depth 先分浅/过渡/深；Grass 斜穿这些带，形成有草/草边/无草；
Shade 又从另一方向扫过。Manual Patch 最终需要表示实际存在的三者空间交集。
这里不是单一维度复杂，而是三套边界彼此独立。

### 4.5 Layer 6–7：看连续场被离散

Temperature 和 DO 更接近连续环境场。手工 Patch 通常要先选阈值桶，例如
“冷/适中/暖”或“低氧/正常”。阈值把一条等值线变成作者边界；它与 Depth、
Grass、Shade 不完全重合时，会继续 split。阈值或采样时间稍变，边界附近的
一串 Patch 都可能需要重新编辑。

### 4.6 Layer 8–10：看局部、语义和时间压力

Flow 的窄流带增量较小，却容易制造细长难选的 Patch。Spawn / Functional Tag
通常跨越物理区；若强制烘焙进互斥 Patch，它会继续切分。Period 层不是复制
三张地图，而是预拆出在任一时段会改变状态的稳定子区。

## 5. 右侧五项怎么读

- **新 boundary**：本层新增什么轮廓；
- **必须 split**：哪些旧 Patch 因被穿过而不再内部一致；
- **可 merge**：哪些相邻子区在全部累计、下游相关属性上等价；
- **策划维护**：除画线外，还要维护哪些阈值、来源、时段、状态和例外；
- **地图微调后重编**：源轮廓移动后，要重切、重赋值或重审哪些 Patch。

“字段看起来相同”不自动等于可 merge。若 Depth、Shade、DO、Functional Tag、
时段向量或任一下游消费语义不同，就应保持分开。

## 6. 如何用它做评审

逐层检查以下问题：

1. 这个 Layer 是静态输入还是会随时间变化？
2. 它与已有边界有多大概率真正重合？
3. 连续值为何要离散，阈值由谁负责？
4. 该属性能否作为正交 Tag，而不物理切开 Patch？
5. 哪些下游消费者真正要求 Patch 内部完全一致？
6. 源轮廓改变时，能否自动找出全部受影响 Patch 和引用？
7. 策划是在维护生态区域，还是在维护多个系统的空间组合？

## 7. 常见误读

- **“96 不多。”** 成本还包括属性赋值、版本、稳定 ID、引用迁移、审查、
  回归和每次地图修改后的重编。
- **“自动切割能解决。”** 它能省画线劳动，不能决定阈值、语义等价、时间
  版本和下游消费是否正确。
- **“更多 Patch 只是地图更丰富。”** 本实验 meaningful regions 约 `45`，
  Manual patches 约 `96`；差值主要来自维度交叉，而非更多可命名地点。
- **“实验已证明 Manual 不可用。”** 没有。它只提供作者成本证据，架构选择
  还取决于地图数、更新频率、工具、运行时约束和预算。

## 8. 这里到底是加法还是乘法

更准确的说法是：**记录结果时表现为逐层加法，结构压力来自受空间约束的稀疏
笛卡尔积。**

它不是简单的区域数相加：

```text
Depth 区域数 + Grass 区域数 + Shade 区域数
```

也通常不会达到完整笛卡尔积：

```text
Depth 类别数 × Grass 类别数 × Shade 状态数
```

假设 Depth 有浅/中/深 `3` 类，Grass 有无草/草内/草边 `3` 类，Shade 有
晨阴午晒、晨晒午阴、都阴、都晒 `4` 种状态，完整理论上限是：

```text
3 × 3 × 4 = 36 种状态组合
```

但真实地图不会出现全部组合：深水可能无草；某些草边从未被阴影扫过；某些
组合面积为零；相邻且全部属性等价者可以 merge。反过来，同一种状态组合若
出现在两个不连通位置，仍然是两个几何 Patch。

所以实际关系是：

```text
Patch
= 地图上实际存在的 Layer 空间交集
− 可安全合并的相邻交集
+ 同状态但不连通的独立区域
```

逐层统计写成：

```text
P(n) = P(n−1) + 本层新边界实际切出的子块数 − 本层可合并数
```

图中的 `27 + 11 = 38`、`38 + 11 = 49` 是计数表达；其中 `+11` 不是固定成本，
而取决于新边界穿过多少个已有组合 Patch。越晚加入一个独立 Layer，它通常
穿过的旧 Patch 越多。完整概括是：

> 计数过程是逐层加法；碎片化机制是稀疏、受地理约束的笛卡尔积。

Ogre Lake 的 `96` 远低于所有 Layer 完整相乘的理论上限，但仍足以显示明显的
手工碎片化压力。

完整假设、逐层数量和证据边界见
[Ogre Lake reproducible overlay experiment](ogre_lake_reproducible_overlay_experiment.md)。
