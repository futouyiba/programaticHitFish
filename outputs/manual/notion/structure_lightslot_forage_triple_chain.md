> **结构→夜槽→猎物三步链**（`STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

夜行结构种（GT/GW）——结构定位→低光槽→猎物。

## 骨架（一行链序）

```plain text
EVAL[结构] 三档 → SLOT[低光] → EVAL[猎物] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-GW-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：counter_current_zone_structure；dusk_night_slot；fish_fallen_prey_field

weight = 1.0
第 1 步 EVAL[counter_current_zone_structure（逆流区位——'Frequently occurs in counter current zones of principal rivers and creeks'）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@GW…Profile 值域，不冻结）
第 2 步 SLOT[dusk_night_slot（黄昏夜相槽——'at dusk and at night' story 原文级；modifier）]（modifier 槽位乘入）：
    黄昏夜=槽全额合入
    过渡=槽削减合入
    白昼=槽极低削减合入（modifier 非 gate）
第 3 步 EVAL[fish_fallen_prey_field（鱼+落水陆生无脊椎猎物场）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@GW…Profile 值域，不冻结）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:'Frequently occurs in counter current zones'+'at dusk and at night'——逆流伏击位先行（story 标题 Counter-Current Dusk Ambush：空间结构+时间窗复合），黄昏夜相槽 modifier 次之，猎物场殿后
- C: benthopelagic / 20-32°C / 晨昏活跃 / 追猎
- B §2.2: 追击组受限还原——本推导按 A 复合主句推得结构→夜槽→猎物三节点（RS1 轨真形从 story 重推）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-GW-BAKE） |
|---|---|
| BakeTemplate | STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_STRUCTURE_FACTOR |
| Step1.Factor/Axis | counter_current_zone_structure（逆流区位——'Frequently occurs in counter current zones（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | APPLY_DYNAMIC_SPATIAL_SLOT |
| Step2.Factor/Axis | dusk_night_slot（黄昏夜相槽——'at dusk and at night' story 原文级；modifier）（@Profile 值域不冻结） |
| Step2.TierSet | 黄昏夜=槽全额合入 / 过渡=槽削减合入 / 白昼=槽极低削减合入（modifier 非 gate） |
| Step3.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step3.Factor/Axis | fish_fallen_prey_field（鱼+落水陆生无脊椎猎物场）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| structure | 先行 |
| light_slot | 中位 |
| forage | 末位 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*