> **结构先行四步链**（`STRUCTURE_FIRST_QUAD_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

蓝鳃栖息面真形：结构→…四步，结构第一（用户裁正「蓝鳃可能结构第一」的推导证实）。

## 骨架（一行链序）

```plain text
EVAL[结构] 三档（先行） → EVAL[水层] 三档 → EVAL[温度] 三档 → EVAL[时段] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-BLU-HAB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：structure_vegetation_band；benthopelagic_soft_layer；broad_temperature_band；crepuscular_time_band

weight = 1.0
第 1 步 EVAL[structure_vegetation_band（结构-植被带——巢区/掩体/植被结构区[结构先行]）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BLU-HAB…Profile 值域，不冻结）
第 2 步 EVAL[benthopelagic_soft_layer（底中软水层——软定位档位归属轴）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BLU-HAB…Profile 值域，不冻结）
第 3 步 EVAL[broad_temperature_band（宽温带——1-36°C 宽带弱分档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BLU-HAB…Profile 值域，不冻结）
第 4 步 EVAL[crepuscular_time_band（晨昏时段带）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BLU-HAB…Profile 值域，不冻结）
返回 weight（4 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- 裁决锚：HRQ-ADJUDICATION §6.2 原文举例『蓝鳃→结构先行』（人类裁决已给推导方向——蓝鳃空间行为第一约束=结构）
- A: B01-S38 story（护巢觅食食卵）栖息语境=巢区/浅水硬底（结构依赖）
- B: guarding/bluegill.md §0 Normal 面因子集=水层（软）/结构/水温/时段（序声明为约定序不采；因子集可用）
- C: benthopelagic（软定位）/ 1-36°C（极宽=弱分档）/ 晨昏活跃——证据强度递减排序：结构（裁决锚）→水层（软定位）→水温（宽带）→时段（弱锚）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-BLU-HAB-BAKE） |
|---|---|
| BakeTemplate | STRUCTURE_FIRST_QUAD_TIER_CHAIN（渐进累积语义） |
| Step 数 | 4 步 |
| Early Return 转折点数 | 4（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step1.Factor/Axis | structure_vegetation_band（结构-植被带——巢区/掩体/植被结构区[结构先行]）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | benthopelagic_soft_layer（底中软水层——软定位档位归属轴）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step3.Factor/Axis | broad_temperature_band（宽温带——1-36°C 宽带弱分档）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step4.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step4.Factor/Axis | crepuscular_time_band（晨昏时段带）（@Profile 值域不冻结） |
| Step4.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| factor_order | 结构→水层→温度→时段（推导序） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*