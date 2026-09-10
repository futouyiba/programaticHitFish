# Ogre Lake minimal spatial-bake fixture

Document status：**RETAINED / generated fixture documentation**  
Authority：**空间事实 fixture；非 FCF V1 mechanism contract**  
Scope：Ogre Lake grid、layer labels、SourceGroup 与 provenance 输入。  
Reproduction：`docs/experiments/export_spatial_bake_fixture.js` 及对应 fixture 命令。  
V1 promotion rule：fixture 输出只能作为 prototype evidence，不能自行升级为 V1 数据或规则。

这是供独立 Python prototype 使用的静态空间 fixture。它只表达空间事实、生态
SourceGroup、逐 cell layer label、统计和 provenance；不包含 Bass 数量、cohort
share、动态鱼情、Entry、Occupancy 或其他运行时状态。

## 坐标系统

- 世界范围：`200m × 200m`；
- 原点：`(0, 0)` 位于西南角；
- `+X` 向东/向右，`+Y` 向北/向上；
- 网格索引从 `cell_x=0, cell_y=0` 开始，`cell_x` 向东增加，`cell_y` 向北增加；
- 单元大小：`2m × 2m`；
- 单元中心：

  ```text
  world_x = (cell_x + 0.5) * 2
  world_y = (cell_y + 0.5) * 2
  ```

`lake_grid.json` 中的 `water_cells` 对每个 wet cell 都写出中心坐标；`outside_cells`
明确列出不在水域内的 cell。不存在第三种“未知是否 wet”的状态。

## Depth bands

```text
0_2     [0, 2) m
2_5     [2, 5) m
5_10    [5, 10) m
10_16   [10, 16) m
16_30   [16, 30] m
```

边界按左闭右开处理，最后一档包含 30m 上限。`depth_m` 已逐 wet cell 材料化；
`lake_grid.json.depth_function` 和 `experiments/ogre_lake_overlay_model.js` 同时
保留可复现的确定性深度函数。

## 文件说明

- `lake_grid.json`：网格尺寸、坐标约定、wet/outside、逐 cell depth；
- `habitat_sources.json`：唯一 gameplay identity 的 SourceGroup。因为本 fixture
  的 source 几何由确定性函数生成，使用 `mask_cells` 而不是伪造 polygon；
- `cell_layer_labels.json`：每个 wet cell 的原始 layer label，用于 overlap 和
  counterexample 分析；
- `source_metadata.json`：统计、来源、重叠信息和 fixture 标记；
- `experiments/ogre_lake_overlay_model.js`：生成上述输入的确定性模型；
- `experiments/export_spatial_bake_fixture.js`：导出脚本。

## Polygon / mask provenance

所有 mask 都来自 Ogre Lake 的人工确定性 fixture 函数，不来自真实湖泊测量、
RF4 内部数据或生产地图。它们是为了稳定复现空间切分关系而构造的 raster mask。
因此不能把 mask 的轮廓、阈值或面积当作生态校准结果。

## Source identity 与 connected patch 的关系

`source_id` 是 gameplay identity，例如 `GRASS_WEST_01` 或 `BRIDGE_DOCK_WEST_01`。
同一个 source 被 raster 切成多个 cell 或多个 connected patch 时，仍只保留一个
`source_id`。反过来，同一个累计 layer state 在多个不连通位置出现时，会形成多个
connected patch，但不会自动生成多个 source。

```text
SourceGroup identity  ≠  raster cell  ≠  connected Patch
```

SourceGroup 是作者/玩法对象；Patch 是累计状态向量的空间连通分量。

## Overlap 定义

不同 source 的 mask 可以重叠，且 fixture 明确允许这种重叠。对一个 wet cell，
如果它同时出现在两个或更多 source 的 `mask_cells` 中，就算一个 source overlap。
例如草边可以与 DROP_OFF 或 SPAWN_BED 重叠；这不是重复 source，而是多个生态
关系共同作用于同一空间。

`source_metadata.json` 给出 overlap cell 数和按参与 source 数量分组的统计。
Prototype 不应因为 overlap 自动复制 source；应保留 source identity，再由查询
逻辑决定返回单个 source、source 集合或冲突。

## 2D 与 3D 对齐

`lake_grid.json`、`habitat_sources.json` 和 `cell_layer_labels.json` 完全按同一
`100 × 100`、`2m` 水平网格对齐。`habitat_volume_count_3d=1033` 是同一水平输入
加上 2m 垂直体素的统计结果；为保持“最小 fixture”，本包不逐 voxel 导出 3D
volume 文件。Python prototype 可以先用二维输入验证 overlap，再按模型脚本中的
depth 和垂向规则派生 3D cells。

## Fixture 数值

`connected_patch_count_2d=285`、`habitat_volume_count_3d=1033`、wet cell 数、
source 统计和所有 labels 都是 fixture 值。它们的用途是验证 parser、overlay、
connected-component、source identity 和 counterexample；不是 RF4 事实或生产预算。

动态状态仍由 prototype 单独注入，不应写回这些 static JSON。
