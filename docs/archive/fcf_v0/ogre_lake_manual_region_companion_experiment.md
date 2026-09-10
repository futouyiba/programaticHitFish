# Simplified FCF Spatial Authoring Cost Visualization Experiment

Document status: **SUPERSEDED / HISTORICAL**  
Authority: **V0 authoring-cost evidence only; not mechanism authority**  
Replacement: [`../ogre_lake_reproducible_overlay_experiment.md`](../../ogre_lake_reproducible_overlay_experiment.md)

> **历史版本说明**：本文件的 `96` 是第一版人工设定的二维示意参数，不是几何
> 计算结果。可复核的共同细分实验、修正后的时间处理和 2.5D/3D 扩展见
> [Ogre Lake reproducible overlay experiment](../../ogre_lake_reproducible_overlay_experiment.md)。
> 本文件保留用于说明初始假设，不应再引用 `96` 作为工作量测算。

## 0. 文档定位

这是 Manual Region Proposal 的 **companion experiment**。它提供作者成本证据，
不修改 FCF 主机制，不裁决 Manual / Procedural / Runtime Query，也不替代环境
机制的 semantic owner、snapshot、revision 或计算契约。

- [可视化使用说明](../../ogre_lake_visualization_user_guide.md)
- [深度与结构机制](../../depth_structure_mechanism_design.md)
- [光照与浑浊度机制](../../light_turbidity_mechanism_design.md)
- [温度机制](../../temperature_mechanism_design.md)
- [溶解氧机制](../../dissolved_oxygen_mechanism_design.md)
- [Flow 机制](../../flow_mechanism_design.md)

## 1. 实验问题与控制条件

实验问题是：当 Habitat Patch 必须由策划作为内部属性一致的静态空间单元
维护时，独立环境边界叠加会怎样增加 Patch 数量、赋值工作和变更传播？

Ogre Lake 约 `200m × 200m`，最大水深 `20–30m`，包含浅滩、深坑、drop-off、
草区、草边、石区、沉木、桥墩、浮萍/间植、开放水面和局部阴影。

控制条件：不追求 GIS/CFD/生态精度；每次只增加一个 Layer；只有不重合边界
才制造 split；只有空间相邻且全部累计属性等价才允许 merge；数量是可读的
一致性估算，不是精确几何输出或人日预算。

## 2. 推导方法

```text
上一层 Patch 集合
+ 新 Layer 边界
→ 找出边界穿过的旧 Patch
→ 拆成内部属性一致的子区
→ 检查全部累计属性的等价性
→ 合并安全相邻子区
→ 得到新 Patch 集合
```

若每层是分类函数 `L_i(x)`，静态 Patch 至少要区分累计状态向量：

```text
S_n(x) = [L_1(x), L_2(x), ... L_n(x)]
```

增长由边界交叉决定，不是各层区域数简单相加。最坏情况接近组合增长；实际
地图因边界局部化、重合和 merge 而低于最坏情况。

### 2.1 加法计数与笛卡尔积压力

实验表格使用逐层递推：

```text
P(n) = P(n−1) + split(n) − merge(n)
```

因此表面上是加法。但 `split(n)` 由新边界与全部旧边界形成的实际空间交集
决定，结构上接近稀疏笛卡尔积。若 Depth 有 `3` 类、Grass 有 `3` 类、Shade
有 `4` 种时段向量，完整理论上限是 `3 × 3 × 4 = 36` 个状态组合；地图只保留
非空组合，再按邻接和全部下游语义等价性 merge。同状态若空间不连通，仍需
作为不同几何 Patch 维护。

所以实际 Patch 数可概括为：

```text
实际存在的 Layer 空间交集
− 可安全合并的相邻交集
+ 同状态但不连通的独立区域
```

`27 → 38` 写成 `+11` 只是计数结果，不代表新增 Shade 的成本天然等于 11；
它取决于 Shade 边界穿过多少个已经由 Depth、Grass、Structure 和 Substrate
组合形成的 Patch。计数是加法，碎片化压力来自受地理约束的组合。

## 3. 逐层推导

| Layer | Regions | Patches | 新 boundary 与 split | 可 merge | 策划维护与地图微调影响 |
|---|---:|---:|---|---|---|
| 0 Geometry | 1 | 1 | 只有湖岸；不拆 | 不适用 | 岸线、水域 ID；岸线变化只改水域边界 |
| 1 Depth | 4 | 6 | 浅滩、两级 drop-off、内嵌深坑切开水体 | 相邻同深度级且无其他差异 | 阈值、等深线、地形命名；刷地形影响约 2–4 个 |
| 2 Vegetation | 8 | 14 | 草区、草边、浮萍斜穿深度带 | 全部累计属性相同的相邻草段 | 类型、密度、草边、季节；改轮廓影响约 4–7 个 |
| 3 Structure | 12 | 20 | 石区、沉木、桥墩切开浅滩和开放水 | 对象可共享参数，不相邻几何不能 merge | 范围、类型、影响半径、状态；移动对象影响约 2–5 个 |
| 4 Substrate | 16 | 27 | 底质斜线穿过深度、草和结构 | 不相邻同值区只能共享参数 | 类别、混合、过渡带；重刷影响约 5–8 个 |
| 5 Shade | 21 | 38 | 移动阴影切开同一草区和深度带 | 全时段 Shade 向量相同者 | 遮挡源、时段状态、例外；移动后影响约 8–13 个 |
| 6 Temperature | 26 | 49 | 阈值等值线穿过开放水、深坑、草边和阴影 | 温度桶及其他属性全相同 | 阈值、窗口、插值、季节；偏移影响约 9–15 个 |
| 7 DO | 31 | 61 | 低氧舌与 Temp、Depth 错位 | DO 相同仍须检查全部属性 | 阈值、昼夜/季节、缺测；变化影响约 10–17 个 |
| 8 Flow | 33 | 65 | 入/出水口窄流带切开局部开放水和桥墩区 | 流速与方向语义都等价 | 流向、流速档、宽度、事件；影响约 3–6 个 |
| 9 Functional tags | 39 | 78 | 产卵场/nursery 跨越物理 Patch | 正交 Tag 模型可能避免部分物理切分 | 物种、季节、优先级；扩缩影响约 8–14 个 |
| 10 Period | 45 | 96 | 预拆任一时段会改变的稳定状态区 | 全时段状态向量相同者 | 状态表、切换、季节版本；变化影响约 12–22 个 |

### 3.1 从 Geometry 到 Substrate：为什么 1 变 27

Depth 首先建立六个空间单元。Grass 不是沿等深线生长，因此每个被穿过的深度
单元都产生有草/无草或草边交集。小型 Structure 又在局部切开这些交集；一条
斜向 Substrate 过渡线会连续穿过多块已有 Patch。前四层都是静态的，仍已出现
“生态区域少、内部一致性 Patch 多”的差异。

### 3.2 Shade：为什么移动边界要求提前拆

Morning 与 Afternoon 阴影从不同方向扫过同一草区。若运行时只读取静态 Patch，
至少要预拆“晨阴午晒、晨晒午阴、都阴、都晒”等实际存在的稳定子区。加入
Dusk 后，理论二值组合从 `2²` 变为 `2³`；地图未必出现所有组合，但每条新增
阴影边缘都可能继续穿过旧 Patch。

### 3.3 Depth × Grass × Shade：典型交叉切割

```text
Depth：浅 / 过渡 / 深
× Grass：无草 / 草内 / 草边
× Shade vector：晨阴午晒 / 晨晒午阴 / 都阴 / 都晒
```

Manual Patch 不是为理论笛卡尔积的所有组合建区，而是为地图上实际存在的每个
相邻交集建区。任何一套轮廓移动，都会改变多个交集的面积、邻接和属性归属。

### 3.4 Temperature / DO：连续场为什么继续制造边界

两者本来是连续场。手工 Patch 需要先阈值化为响应桶，等值线因此变成作者边界。
Temperature 与 Depth 相关、DO 与 Temp 相关，不等于轮廓完全重合。只要不是同
一个空间函数，就会出现 `Depth × Temp × DO` 的实际交集；阈值、采样窗口或输入
revision 改变时，边界附近的一串 Patch 需要重编。

### 3.5 Functional tags 与 Period：物理边界之外的压力

玩法语义区按物种、季节或功能定义，常跨越物理区域。若 Tag 被烘焙进互斥
Patch 类型就会切分；允许正交叠加可减少部分几何碎片，但查询、冲突和审计仍
需处理。Period 层也不是复制三张地图，而是为全部时段预先形成稳定状态分区。

## 4. 数量说明

累计序列为：

```text
1 → 6 → 14 → 20 → 27 → 38 → 49 → 61 → 65 → 78 → 96
```

对应本层增量：

```text
+1, +5, +8, +6, +7, +11, +11, +12, +4, +13, +18
```

证据意义：Patch 增长快于 meaningful regions；最大增量来自移动边界、错位
边界和语义跨区；越到后期，同样大小的新轮廓会穿过更多已有组合 Patch。

## 5. 最易造成碎片化的维度

1. **Period × Shade**：移动边界迫使静态 Patch 表达多时段状态向量；
2. **Depth × Grass × Shade**：地形、植被和投影边界天然不保证重合；
3. **Temperature / DO**：连续场阈值化，且两套等值线不完全对齐；
4. **Functional tags**：玩法语义区跨越物理区；
5. **Small structures**：面积小但局部边缘密，对选择、邻接和对象移动敏感。

## 6. 手工方案真正维护什么

成本不只是画多边形，而是：边界生产、交叉切割、累计属性赋值、merge 等价性
判断、时段/季节版本、源变化后的影响传播、稳定 ID 与外部引用迁移、缝隙/重叠/
孤岛检查、回归审查，以及理解每个小 Patch 为何存在。首次生成后，后半部分会
随每次地图修改重复发生。

## 7. 工具可缓解的部分

- 自动轮廓叠加与布尔切割；
- 从源 Layer 生成候选 Patch；
- 模板、继承和批量赋值；
- 相邻同值检测和 merge 建议；
- 显示来源 Layer、状态向量和下游消费者；
- 变更前影响预览；
- 缝隙、重叠、孤岛、过小区和失效引用检查；
- 稳定 ID、差异、迁移记录和回归快照；
- 按 Layer/时段过滤，降低视觉噪音。

这些能力可显著减少机械劳动，使首次生成更可控。

## 8. 工具难以解决的结构性部分

- **组合边界仍存在**：自动计算交集不能让独立边界不再相交；
- **动态连续场与静态 Patch 错配**：重新烘焙不能消除阈值、更新频率和版本迁移；
- **等价性是语义问题**：字段相同不证明所有下游消费者等价；
- **变更传播不可避免**：工具能列出影响范围，不能免除验证、审查和发布；
- **阈值与例外仍需负责**：自动生成不能证明温度阈值、采样时段或 Tag 正确。

## 9. 对 Manual Region Proposal 的中立证据

- 少量静态、基本重合的 Layer 下，手工 Patch 仍然直观；
- 成本更受独立边界数量、错位程度和时间变化影响，而不只由地图面积决定；
- Shade、Temperature、DO 若预烘焙进静态 Patch，会产生明显预拆和版本压力；
- 自动切割、继承、影响分析和验证工具能降低机械成本；
- 工具不能消除组合边界、动态场错配、语义等价判断和引用迁移；
- 是否接受该成本，需要结合生产地图数、更新频率、作者预算、运行时能力和下游
  一致性要求另行评估。

本实验不作 promotion/reject。它是一套可重复的证据流程：Proposal 的字段、
Layer 或工具能力改变时，可重新走 Layer 0–10，比较 Patch 增长和重编范围。

真实游戏截图参照下的第二轮估算见
[RF4 Old Burg Lake authoring estimate](rf4_old_burg_spatial_authoring_estimate.md)。
