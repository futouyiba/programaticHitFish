# Simplified FCF Spatial Bake Prototype (R0)

独立的 Python 实验原型，对应 `Spatial Bake Prototype Experiment R0｜Ogre Lake Static Relation Field × Dynamic Cohort State`。所有 Bass 数值都是调参固定样例（tuning fixture），不是生物学结论。

## 运行

```bash
python3 run_experiment.py
# package-derived fixture
python3 run_fixture_experiment.py
```

输出写入 `output/`：三种烘焙（bake）表达（expanded、distance_band、continuous）各自的 FULL/Top-8/Top-4/Top-2 JSON.gz 交付物（artifact）、`benchmark.csv`、`query_results.csv`、`summary.json` 与 `spatial_hotspots.png`。

实验固定 200m×200m、1m XY、4 个深度分带（depth bands，160,000 cells），10 个栖息来源（Habitat Source），5 个投点×3 个生命周期快照（lifecycle snapshot）。运行时（Runtime）只读取合法查询单元（query cell）、静态贡献者（contributor）、动态队列标量（cohort scalar）与查找表（LUT）。

## 结果解释

`summary.json` 包含每种表达的交付物（artifact）大小、查询成本、Top-K 误差与热点排名稳定性，以及基于阈值的 PASS/FAIL/MIXED 判定（verdict）和下一轮推荐。`query_results.csv` 保留 15 个固定样例（fixture）的 FULL 结果、Top-K 结果和贡献者详情。

`run_fixture_experiment.py` 读取 `docs/spatial_bake_fixture/` 的 package-derived 2m 栅格（raster，100×100、5 个深度分带、6,190 个湿单元、13 sources），结果写入 `output_fixture/`；它与原始 1m/4-band 基线（baseline）分开报告，不应直接混合比较。
