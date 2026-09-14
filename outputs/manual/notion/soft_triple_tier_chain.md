> **软三步无门链**（`SOFT_TRIPLE_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：3

## 特点

无硬门，三步软档直连（跨科重复，PROV 系）。

## 骨架（一行链序）

```plain text
EVAL[因子1] 三档 → EVAL[因子2] 三档 → EVAL[因子3] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-CAR1-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：near_bottom_soft_layer；substrate_upturnability；benthic_prey_patch

weight = 1.0
第 1 步 EVAL[near_bottom_soft_layer（近底软水层——benthopelagic 软定位三档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@CAR1…Profile 值域，不冻结）
第 2 步 EVAL[substrate_upturnability（底质可拱性三档——口部翻拱的物理依赖）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@CAR1…Profile 值域，不冻结）
第 3 步 EVAL[benthic_prey_patch（底栖猎物斑块丰度三档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@CAR1…Profile 值域，不冻结）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A: RB 主句『用口部翻拱底泥，摄食底栖无脊椎、植物碎屑和种子』——翻拱取食对底质可拱性有物理依赖：可拱性先于斑块丰度（软定位首步无门）
- B: patch/common_carp.md §0 判断顺序=近底带水层定位→底质可拱性→底栖猎物斑块（同序独立确认；三步无门形）
- C: benthopelagic 0-29m / 3-35°C

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-CAR1-BAKE） |
|---|---|
| BakeTemplate | SOFT_TRIPLE_TIER_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 3（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step1.Factor/Axis | near_bottom_soft_layer（近底软水层——benthopelagic 软定位三档）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | substrate_upturnability（底质可拱性三档——口部翻拱的物理依赖）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_PREY_FACTOR |
| Step3.Factor/Axis | benthic_prey_patch（底栖猎物斑块丰度三档）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| factors | typed ×3 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*