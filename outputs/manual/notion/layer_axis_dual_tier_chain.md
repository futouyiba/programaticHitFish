> **水层+轴段双步链**（`LAYER_AXIS_DUAL_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：7

## 特点

第二步是生命周期轴段（深度带/洄游廊道）而非空间因子——轴域限定是与镜像双因子族的分界。

## 骨架（一行链序）

```plain text
EVAL[水层] 三档 → EVAL[轴段（深度带/洄游廊道）] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB2-CHN-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：near_bottom_soft_layer；stage_bound_corridor_axis

weight = 1.0
第 1 步 EVAL[near_bottom_soft_layer（近底水层软定位——CSV benthopelagic 锚，与水平洄游廊道为独立维度）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@CHN…Profile 值域，不冻结）
第 2 步 EVAL[stage_bound_corridor_axis（海洋觅食区↔河口↔深河产卵段轴段——4827km 溯河 premise 取段）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@CHN…Profile 值域，不冻结）
返回 weight（2 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-B3: 海期'primarily other fish when older'+4827km 溯河——水平廊道轴段为主体；垂直近底定位为独立第二维（CSV benthopelagic 锚）先于廊道（水柱内定位先于沿廊道分档）
- C: benthopelagic 0-375m / anadromous / 晨昏活跃
- B §0: 单步链='G2/C12 样板语义方向级还原（Tier B 无行级证据）'——样板约定序不采；真形按 A+C 两维推导
- 同构对照：CHU 同批真形（近底软定位→廊道轴段两步）——同证据层同推导

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB2-CHN-BAKE） |
|---|---|
| BakeTemplate | LAYER_AXIS_DUAL_TIER_CHAIN（渐进累积语义） |
| Step 数 | 2 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_LAYER_FACTOR |
| Step1.Factor/Axis | near_bottom_soft_layer（近底水层软定位——CSV benthopelagic 锚，与水平洄游廊道为独立维度）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | stage_bound_corridor_axis（海洋觅食区↔河口↔深河产卵段轴段——4827km 溯河 premise 取段）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| layer | typed |
| axis_segment | lifecycle 轴段（非空间因子） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*