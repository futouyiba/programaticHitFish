> **门化结构先行四步链**（`GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

美鱥栖息面真形：先一道门（口器/底栖形态锚），结构先行四步。

## 骨架（一行链序）

```plain text
GATE[形态锚定门] → EVAL[结构] → EVAL[温度] → EVAL[时段] → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-HNC-HAB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：demersal_gravel_zone；gravel_run_structure；cool_temperature_band；morning_time_band

weight = 1.0
第 1 步 GATE[demersal_gravel_zone（底层砾石硬定位——美鱥口器形态绑定底层取食/筑巢，非底层=出局）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[gravel_run_structure（砾石潭渊结构——筑巢基质/掩体）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@HNC-HAB…Profile 值域，不冻结）
第 3 步 EVAL[cool_temperature_band（冷水温带——溪流冷水向）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@HNC-HAB…Profile 值域，不冻结）
第 4 步 EVAL[morning_time_band（早晨时段带）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@HNC-HAB…Profile 值域，不冻结）
返回 weight（4 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- 裁决锚：HRQ-ADJUDICATION §6.2 原文举例『美鱥口器形态→水层先行』（人类裁决已给推导方向——口器特化绑定底层取食→底层水层定位先行）
- B: guarding/hornyhead_chub.md §0 Normal 面因子集=水层硬定位（demersal）/结构/水温/时段（早晨）（序声明为约定序不采；硬定位出局语义=第一步门化[RB-1 GRH/RRH bottom_layer_zone GATE 化判例]）
- C: demersal / 溪流冷水 / 早晨活跃——口器特化（底层砾石取食+筑巢）→结构（砾石）→水温（冷水）→时段（早晨）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-HNC-HAB-BAKE） |
|---|---|
| BakeTemplate | GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN（渐进累积语义） |
| Step 数 | 4 步 |
| Early Return 转折点数 | 4（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_ZONE |
| Step1.Factor/Axis | demersal_gravel_zone（底层砾石硬定位——美鱥口器形态绑定底层取食/筑巢，非底层=出局）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | gravel_run_structure（砾石潭渊结构——筑巢基质/掩体）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step3.Factor/Axis | cool_temperature_band（冷水温带——溪流冷水向）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step4.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step4.Factor/Axis | morning_time_band（早晨时段带）（@Profile 值域不冻结） |
| Step4.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| gate | 形态锚（口器→水层先行判据的 GATE 化） |
| order | 结构→温→时 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*