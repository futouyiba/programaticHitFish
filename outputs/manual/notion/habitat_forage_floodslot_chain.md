> **栖息→猎物+洪泛槽链**（`HABITAT_FORAGE_FLOODSLOT_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

栖息→猎物双步，链尾挂洪泛连通槽（modifier 非 gate；巴沙/斯氏鳊）。

## 骨架（一行链序）

```plain text
EVAL[栖息带] 三档 → EVAL[猎物资源] 三档 → SLOT[洪泛林连通]：连通=全额/边缘=削减/断连=极低削减 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-BAS-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：large_river_rapid_pool_band；plant_food_resource；floodplain_forest_slot

weight = 1.0
第 1 步 EVAL[large_river_rapid_pool_band（大河急流+缓段带——S8 主句复合）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BAS…Profile 值域，不冻结）
第 2 步 EVAL[plant_food_resource（植食资源）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BAS…Profile 值域，不冻结）
第 3 步 SLOT[floodplain_forest_slot（洪泛林槽——'成鱼入洪泛林'：裁决 3 洪水→DynamicSpatialSlot；modifier 非路由）]（modifier 槽位乘入）：
    洪泛连通=槽全额合入
    边缘连通=槽削减合入
    断连=槽极低削减合入（modifier 非 gate）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:植食+S8 MSF(大河急流+缓段)——栖息主句先行（急流-缓段复合带），植食资源次之
- A-S5: MSF(入洪泛林)——洪水事件槽（裁决 3 拆解规则：洪水→DynamicSpatialSlot）承载链尾 modifier
- C: benthopelagic / 20-32°C / 杂食性 / 孤僻
- B: 无表达文件——真形从 A/C 推导（蓝鲨同科对照不继承判例）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-BAS-BAKE） |
|---|---|
| BakeTemplate | HABITAT_FORAGE_FLOODSLOT_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step1.Factor/Axis | large_river_rapid_pool_band（大河急流+缓段带——S8 主句复合）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step2.Factor/Axis | plant_food_resource（植食资源）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | APPLY_DYNAMIC_SPATIAL_SLOT |
| Step3.Factor/Axis | floodplain_forest_slot（洪泛林槽——'成鱼入洪泛林'：裁决 3 洪水→DynamicSpatialSlot；modifier 非路由）（@Profile 值域不冻结） |
| Step3.TierSet | 洪泛连通=槽全额合入 / 边缘连通=槽削减合入 / 断连=槽极低削减合入（modifier 非 gate） |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| flood_slot | DynamicSpatialSlot modifier |
| habitat/forage | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*