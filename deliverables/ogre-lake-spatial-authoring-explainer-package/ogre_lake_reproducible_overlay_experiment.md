# Ogre Lake 可复核空间 Overlay 实验

Document status：**RETAINED / canonical evidence**  
Authority：**可复核 authoring-cost evidence；非 FCF V1 mechanism contract**  
Scope：Ogre Lake spatial overlay counts and 2D/2.5D/3D extensions.  
Reproduction：`docs/experiments/ogre_lake_overlay_model.js` and the reproduction entry in §9.  
V1 promotion rule：结果只能作为 authoring evidence，不能自行升级为 V1 policy 或参数。

## 0. 结论先行

第一版 Ogre Lake 的 `96` 是人工设定的二维示意参数，不是几何计算结果。本轮
用明确、确定性的空间分类函数重新计算后，得到：

```text
最终 2D connected patches：285
最终 unique state vectors：224
2m 垂直体素扩展后的 connected habitat volumes：1,033
```

这三个数回答不同问题：

- `224`：实际出现了多少种不同的累计属性组合；
- `285`：这些组合在平面上形成多少个互不连通的 Patch；
- `1,033`：加入水柱垂直分层、光衰减、垂向 Temperature/DO 后形成多少个连通
  Habitat Volume。

本实验仍然不裁决 Manual / Procedural / Runtime Query。它只把作者成本证据从
“手写增量”升级为“可重复执行的共同细分计数”。

## 1. 修正了什么

### 1.1 不再手工指定 Patch 增量

每个 Layer 都有明确分类函数。最终 Patch 是累计状态向量相同的四邻域连通
分量，不再先写 `+11`、`+18` 再补解释。

### 1.2 Depth 与 Shade 真正交叉

Depth 首先形成五个分级，但因岸形、中央岛、浅滩和深坑而产生 `24` 个平面
连通 Patch。每个 Shade 快照再分别切割这些已经包含 Depth、Vegetation、
Structure 和 Substrate 的 Patch。

### 1.3 时间快照不重复计算

旧版先加入 Shade，又在最后加入 Period，存在重复计算风险。新版改成：

```text
Shade · Morning
Shade · Afternoon
Shade · Dusk
```

三个边界依次加入，之后不再添加抽象 Period Layer。

### 1.4 二维与三维分开报告

二维结果叫 `Patch`。加入 `2m` 垂直分层后的结果叫 `Habitat Volume`，不再把
平面等深带和垂直水层混在同一增长表中。

## 2. 可重复输入

### 2.1 空间离散

- 湖泊范围：`200m × 200m`；
- 水平网格：`100 × 100`；
- 单元大小：`2m × 2m`；
- 水域单元数：`6,190`；
- 连通性：二维使用四邻域，三维使用六邻域。

网格不是生态精度声明，而是为了让每个数字能够复算。更细分辨率可能改变边缘
附近的小 Patch 数，因此分辨率必须和结果一起报告。

### 2.2 Layer 分类

| Layer | 明确分类 |
|---|---|
| Geometry | wet / outside，含中央岛洞 |
| Depth | `0–2m / 2–5m / 5–10m / 10–16m / 16m+` |
| Vegetation | open / grass core / grass edge / pads |
| Structure | none / rock / wood / bridge-dock |
| Substrate | mud / sand / gravel-hard |
| Shade Morning | light / shade |
| Shade Afternoon | light / shade，方向不同 |
| Shade Dusk | light / shade，方向再次不同 |
| Temperature | afternoon snapshot：cold / temperate / warm |
| DO | dawn snapshot：low / medium / normal |
| Flow | still / local flow |
| Functional | spawn / nursery / ambush 的位集合 |

这些是压力测试输入，不是生态校准值。关键是所有边界明确、可复算且彼此不被
强制对齐。

## 3. 精确计数方法

对每个水域网格单元 `x`，累计状态向量定义为：

```text
S_n(x) = [L_0(x), L_1(x), ..., L_n(x)]
```

两个相邻单元只有在 `S_n` 完全相同时才连通。Patch 数为：

```text
P_n = number_of_connected_components(S_n)
```

本层净新增：

```text
ΔP_n = P_n − P_(n−1)
```

“被本层切开的旧 Patch”则通过检查每个旧连通分量内部是否出现两个或更多本层
类别得到。它与净新增不同：一个旧 Patch 可能被切成三块，净新增为二；多个
切分也可能因新状态的连通关系产生不同结果。

## 4. 逐层结果

| Layer | Unique state vectors | Connected patches | 净新增 | 被切开的旧 Patch |
|---|---:|---:|---:|---:|
| 0 Geometry | 1 | 1 | +1 | 0 |
| 1 Depth | 5 | 24 | +23 | 1 |
| 2 Vegetation | 17 | 58 | +34 | 4 |
| 3 Structure | 32 | 82 | +24 | 12 |
| 4 Substrate | 58 | 106 | +24 | 19 |
| 5 Shade · Morning | 77 | 122 | +16 | 12 |
| 6 Shade · Afternoon | 91 | 138 | +16 | 14 |
| 7 Shade · Dusk | 106 | 150 | +12 | 12 |
| 8 Temperature · afternoon | 128 | 175 | +25 | 21 |
| 9 DO · dawn | 162 | 223 | +48 | 36 |
| 10 Flow | 174 | 235 | +12 | 12 |
| 11 Functional tags | 224 | 285 | +50 | 47 |

累计序列：

```text
1 → 24 → 58 → 82 → 106 → 122 → 138 → 150
  → 175 → 223 → 235 → 285
```

## 5. 如何解释这些数字

### 5.1 五个 Depth 状态为什么成为 24 个 Patch

类别数不是 Patch 数。相同深度状态会被中央岛、岸形、浅滩和深坑分成多个
不连通分量。因此五种状态在平面上形成 24 个可独立定位的 Patch。

### 5.2 Vegetation 为什么净增 34

Vegetation 只有四种状态，但草区、草边和 pads 跨越多个 Depth Patch。同一种
`grass edge × depth band` 还可能在空间上不连通，因此 17 种累计状态形成 58
个连通 Patch。

### 5.3 Shade 与 Depth 如何交叉

Morning 不是新增一个阴影 Patch，而是切开 12 个已有 Patch，净增 16。
Afternoon 从另一方向穿过 Morning 后的共同细分，切开 14 个旧 Patch，再增 16。
Dusk 继续切开 12 个旧 Patch，再增 12。

因此 Shade 的贡献是：

```text
106 → 122 → 138 → 150
```

而不是“已有 106，再加三个阴影区等于 109”。

### 5.4 DO 为什么比单个 Shade 快照增加更多

到 DO 加入时，地图已经包含 Depth、Vegetation、Structure、Substrate、三个
Shade 快照和 Temperature。DO 阈值边界穿过 36 个旧 Patch，形成 48 个净新增。
这是“越晚加入的错位边界可能切开更多已有共同细分”的直接结果。

### 5.5 224 种状态为什么有 285 个 Patch

同一状态向量可以在湖的多个位置出现。由于它们不相邻，不能成为同一个几何
Patch。因此 `connected patches > unique state vectors`。

## 6. 2.5D/3D 扩展

二维共同细分完成后，同一湖面输入按 `2m` 垂直体素扩展，并加入：

- surface / mid-water / near-bottom；
- Morning / Afternoon / Dusk Shade 与深度衰减共同形成的光照等级；
- 随深度变化的 Temperature；
- 随深度和深坑位置变化的 DO；
- 原有 Vegetation、Structure、Substrate、Flow 和 Functional 状态。

结果：

```text
水体体素：25,407
连通 Habitat Volumes：1,033
```

`25,407` 是离散采样单元，不代表策划必须逐体素编辑；`1,033` 才是相同累计
三维状态的连通体数量。但即使编辑器能自动生成，策划仍需维护分类规则、来源、
阈值、例外、稳定 identity 和变更验证。

## 7. 结果的有效范围

### 可以证明

- 深度分区本身就可能产生多个不连通 Patch；
- Shade 与每个被穿过的 Depth/Grass/Structure/Substrate Patch 分别交叉；
- 多时段必须按各快照共同细分，不能用一个抽象 Period 增量代替；
- state vector 数量与 connected patch 数量不同；
- 加入垂直水层后，问题会从二维 Patch 转成更多的 Habitat Volume；
- 后加入的非重合边界可以切开大量已有 Patch。

### 不能证明

- 真实生产湖泊一定有 `285` 或 `1,033`；
- `2m` 是正确生产分辨率；
- 本实验的 Temperature、DO 或 Shade 轮廓生态上准确；
- RF4 或任何其他游戏内部采用相同数据结构。

## 8. 对 Manual Region Proposal 的中立证据

本轮加强的证据是：当 Manual Region 被定义为所有已烘焙属性的原子共同细分，
作者对象数取决于边界图的实际交叉和连通分量，而不是 Layer 数的简单相加。
二维确定性示例已达到 285，三维扩展达到 1,033。

这不自动否定 Manual。若某些维度保持为正交 Layer、运行时查询或派生字段，
就不必全部物理烘焙成同一组原子 Patch；相应成本会从 Patch 数转移到查询、
冲突、缓存、调试和运行时一致性。方案取舍仍需另行评估。

## 9. 复现入口

- 交互页面：`ogre-lake-exact-overlay-standalone.html`
- 确定性模型：`experiments/ogre_lake_overlay_model.js`
- 执行：`node docs/experiments/ogre_lake_overlay_model.js`
