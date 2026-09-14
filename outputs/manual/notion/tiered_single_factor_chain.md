> **单因子三档链**（`TIERED_SINGLE_FACTOR_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：94

## 特点

全库最大族——整条空间判断只有一个 typed 因子（轴段/资源斑块/场浓度等），一步定终值。

## 骨架（一行链序）

```plain text
读取 typed 因子事实 → EVAL[typed 因子] 三档：最适应=全额 / 可接受=×衰减 / 不居留=×0.01 软出局 → 返回 running weight（单步即终值）
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-TIL2-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：periphyton_suspended_field

weight = 1.0
第 1 步 EVAL[periphyton_suspended_field（附着-悬浮颗粒场——刮食基质与水柱悬浮连续场）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@TIL2…Profile 值域，不冻结）
返回 weight（1 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A: story FCFI=P03（typed field/substrate evaluator + 已有 Response；环境颗粒变化与鱼响应分开 owner）
- B: guarding/nile_tilapia.md §0 NormalFeeding 双通道（刮食+悬浮颗粒——live 例 3 表达；本面按 story P03 走场形）
- C: benthopelagic 0-20m / 植食性 / browsing on substrate / 全天活跃

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-TIL2-BAKE） |
|---|---|
| BakeTemplate | TIERED_SINGLE_FACTOR_CHAIN（渐进累积语义） |
| Step 数 | 1 步 |
| Early Return 转折点数 | 1（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_FOOD_FIELD_CONCENTRATION |
| Step1.Factor/Axis | periphyton_suspended_field（附着-悬浮颗粒场——刮食基质与水柱悬浮连续场）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| factor_type | typed：lifecycle 轴段|resource patch|场浓度 field|position 等约 29 亚群 |
| tier_members | Profile 值域 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*