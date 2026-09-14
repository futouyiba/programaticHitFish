> **底带硬门+底质+资源链**（`ZONE_SUBSTRATE_RESOURCE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：7

## 特点

非底层直接出局（硬门），然后底质档、资源档。

## 骨架（一行链序）

```plain text
GATE[底带]：demersal？否→×0.01 软出局 → EVAL[底质] 三档 → EVAL[资源] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-GRH-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：bottom_layer_zone；mud_to_rock_pool_substrate；insect_larvae_resource

weight = 1.0
第 1 步 GATE[bottom_layer_zone（底层水层带——demersal 硬定位，与 RRH 同属同构）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[mud_to_rock_pool_substrate（泥底-岩底池潭/急滩底质——昆虫幼生栖境）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@GRH…Profile 值域，不冻结）
第 3 步 EVAL[insect_larvae_resource（蜉蝣/石蝇/摇蚊幼生——story 明确 S1 MSF）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@GRH…Profile 值域，不冻结）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:'They feed on immature mayflies, caddisflies and midges'+'mud-bottomed to rock-bottomed pools, runs and riffles'——与 RRH 同属 Moxostoma 链形同构，资源构成走 Profile 值域非结构差异（B §0 明言同属判语）
- C: demersal / 11-19°C——硬定位锚
- B §2.2: P06 链=GATE_ZONE→底质栖境档→无脊椎资源档——与 A 一致

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-GRH-BAKE） |
|---|---|
| BakeTemplate | ZONE_SUBSTRATE_RESOURCE_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 3（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_ZONE |
| Step1.Factor/Axis | bottom_layer_zone（底层水层带——demersal 硬定位，与 RRH 同属同构）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_TYPED_SUBSTRATE_FACTOR |
| Step2.Factor/Axis | mud_to_rock_pool_substrate（泥底-岩底池潭/急滩底质——昆虫幼生栖境）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step3.Factor/Axis | insect_larvae_resource（蜉蝣/石蝇/摇蚊幼生——story 明确 S1 MSF）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| zone_gate | 底带二元 |
| substrate | typed |
| resource | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*