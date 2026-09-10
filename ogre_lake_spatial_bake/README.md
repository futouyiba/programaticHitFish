# Simplified FCF Spatial Bake Prototype (R0)

独立的 Python 实验原型，对应 `Spatial Bake Prototype Experiment R0｜Ogre Lake Static Relation Field × Dynamic Cohort State`。所有 Bass 数值都是 tuning fixture，不是生物学结论。

## 运行

```bash
python3 run_experiment.py
# package-derived fixture
python3 run_fixture_experiment.py
```

输出写入 `output/`：三种 bake 表达（expanded、distance_band、continuous）各自的 FULL/Top-8/Top-4/Top-2 JSON.gz artifact、`benchmark.csv`、`query_results.csv`、`summary.json` 与 `spatial_hotspots.png`。

实验固定 200m×200m、1m XY、4 depth bands（160,000 cells），10 个 Habitat Source，5 个投点×3 lifecycle snapshot。Runtime 只读取合法 query cell、静态 contributor、动态 cohort scalar 与 LUT。

## 结果解释

`summary.json` 包含每种表达的 artifact 大小、查询成本、Top-K 误差与热点排名稳定性，以及基于阈值的 PASS/FAIL/MIXED verdict 和下一轮推荐。`query_results.csv` 保留 15 个 fixture 的 FULL 结果、Top-K 结果和 contributor 详情。

`run_fixture_experiment.py` 读取 `docs/spatial_bake_fixture/` 的 package-derived 2m raster（100×100、5 depth bands、6,190 wet cells、13 sources），结果写入 `output_fixture/`；它与原始 1m/4-band baseline 分开报告，不应直接混合比较。
