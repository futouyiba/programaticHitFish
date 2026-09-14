> **水层→温度→结构三步链**（`LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

红腹食人鱼栖息面真形：三步，时段被证据剔除（CSV 全天活跃→不入链）。

## 骨架（一行链序）

```plain text
EVAL[水层] → EVAL[温度] → EVAL[结构] → 返回 running weight（无时段步——证据砍步）
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-RBP-HAB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：midupper_pelagic_soft_layer；narrow_warm_temperature_band；submerged_structure

weight = 1.0
第 1 步 EVAL[midupper_pelagic_soft_layer（中上软水层——CSV pelagic 主体空间带）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@RBP-HAB…Profile 值域，不冻结）
第 2 步 EVAL[narrow_warm_temperature_band（窄暖温带——23-27°C ±2 强分档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@RBP-HAB…Profile 值域，不冻结）
第 3 步 EVAL[submerged_structure（沉水结构——树根/植被掩体次级锚）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@RBP-HAB…Profile 值域，不冻结）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- C: CSV=红腹食人鱼 pelagic / 23-27°C（窄带）/ 全天活跃——主体空间带（软定位）先行；窄温带次之；沉水结构（B 文件护巢面树根/水草丛佐证其结构生态=Normal 面次级锚）第三；全天活跃=无时段分档（时段步不入链——证据驱动）
- B: guarding/red_bellied_piranha.md §0 Normal 面因子集=水层（软）/结构/水温/时段（全天）（序声明为约定序不采）
- Frenzy 群游无证据（negative knowledge 原样——不立群游轴）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-RBP-HAB-BAKE） |
|---|---|
| BakeTemplate | LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 3（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step1.Factor/Axis | midupper_pelagic_soft_layer（中上软水层——CSV pelagic 主体空间带）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | narrow_warm_temperature_band（窄暖温带——23-27°C ±2 强分档）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step3.Factor/Axis | submerged_structure（沉水结构——树根/植被掩体次级锚）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| dropped_factor | 时段（CSV 全天直证剔除） |
| order | 层→温→构 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*