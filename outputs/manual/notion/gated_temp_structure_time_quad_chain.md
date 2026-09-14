> **门化温度次置四步链**（`GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

巨骨舌鱼栖息面真形：门+四步，温度第二位（25-29℃ 窄带证据压过结构[需正文]）。

## 骨架（一行链序）

```plain text
GATE[硬门] → EVAL[温度]（次置——窄带强证据） → EVAL[结构] → EVAL[时段] → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-ARA-HAB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：demersal_bottom_zone；narrow_warm_temperature_band；floodplain_wood_structure；crepuscular_time_band

weight = 1.0
第 1 步 GATE[demersal_bottom_zone（底层硬定位——CSV demersal，非底层=出局）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[narrow_warm_temperature_band（窄暖温带——25-29°C ±2 强分档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@ARA-HAB…Profile 值域，不冻结）
第 3 步 EVAL[floodplain_wood_structure（洪泛林木质结构——掩体方向级）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@ARA-HAB…Profile 值域，不冻结）
第 4 步 EVAL[crepuscular_time_band（晨昏时段带）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@ARA-HAB…Profile 值域，不冻结）
返回 weight（4 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- C: CSV=巨骨舌鱼 demersal / 25-29°C（窄带）/ 晨昏活跃——硬定位（出局语义）先行=第一过滤；窄暖温带（CSV 直证强分档）次之；洪泛林结构（B 文件方向级 [需正文]）第三；晨昏最后
- B: guarding/arapaima.md §0 Normal 面因子集=水层硬定位（demersal）/结构/水温/时段（序声明为约定序不采；因子集可用）
- 与 B 文件声明序差异：水温与结构互换（依据=CSV 窄温带证据强度>结构 [需正文] 方向级）——逐鱼推导产物

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-ARA-HAB-BAKE） |
|---|---|
| BakeTemplate | GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN（渐进累积语义） |
| Step 数 | 4 步 |
| Early Return 转折点数 | 4（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_ZONE |
| Step1.Factor/Axis | demersal_bottom_zone（底层硬定位——CSV demersal，非底层=出局）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | narrow_warm_temperature_band（窄暖温带——25-29°C ±2 强分档）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step3.Factor/Axis | floodplain_wood_structure（洪泛林木质结构——掩体方向级）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step4.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step4.Factor/Axis | crepuscular_time_band（晨昏时段带）（@Profile 值域不冻结） |
| Step4.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| order | 温→构→时（vs 美鱥构→温→时=ORDER 差异不并） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*