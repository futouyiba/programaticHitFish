> **底带门五步链（含深度档）**（`ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

底带门+深度档+底质+资源，五步形。

## 骨架（一行链序）

```plain text
GATE[底带] → EVAL[深度] 三档 → EVAL[底质] 三档 → EVAL[资源] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-SMB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：bottom_layer_zone；deep_pool_depth_band；pool_backwater_substrate；shellfish_algae_benthic_resource

weight = 1.0
第 1 步 GATE[bottom_layer_zone（底层水层带——demersal 硬定位）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[deep_pool_depth_band（深潭深度带 ≥4m——本鱼 CSV 独有深度注记）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@SMB…Profile 值域，不冻结）
第 3 步 EVAL[pool_backwater_substrate（河湾潭果底泥栖境：pools/backwaters/main channels+湖库）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@SMB…Profile 值域，不冻结）
第 4 步 EVAL[shellfish_algae_benthic_resource（贝/藻底泥资源——磿食口径）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@SMB…Profile 值域，不冻结）
返回 weight（4 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:'feed on shellfish and algae, by grinding with the bony plates in its throat'+'Adults inhabit pools, backwaters and main channels...also in lakes'——亚口科第三例，demersal 硬定位→深度→底泥栖境→资源
- C: demersal / 深度下限 4m（四亚口鱼中唯本鱼有深度注记——B §0 声明独有深度档步）/ 21-33°C
- B §2.2: P06 链=GATE_ZONE→深度带档→底泥栖境档→底泥资源档（CSV 方向级推导）——与 A/C 一致

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-SMB-BAKE） |
|---|---|
| BakeTemplate | ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN（渐进累积语义） |
| Step 数 | 4 步 |
| Early Return 转折点数 | 4（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_ZONE |
| Step1.Factor/Axis | bottom_layer_zone（底层水层带——demersal 硬定位）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_TYPED_DEPTH_FACTOR |
| Step2.Factor/Axis | deep_pool_depth_band（深潭深度带 ≥4m——本鱼 CSV 独有深度注记）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_SUBSTRATE_FACTOR |
| Step3.Factor/Axis | pool_backwater_substrate（河湾潭果底泥栖境：pools/backwaters/main channels+湖库）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step4.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step4.Factor/Axis | shellfish_algae_benthic_resource（贝/藻底泥资源——磿食口径）（@Profile 值域不冻结） |
| Step4.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| depth | 显式档位步 |
| substrate/resource | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*