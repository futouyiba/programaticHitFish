> **空间先行双因子链**（`SPACE_FIRST_DUAL_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：61

## 特点

先找合适的地方，再找吃的——空间因子（水层/结构/栖境带）先行出局，猎物场第二。

## 骨架（一行链序）

```plain text
读取 空间因子事实（水层/结构/栖境带） → EVAL[空间因子] 三档：最适应=全额乘入 / 可接受=×衰减 / 不居留=×0.01 软出局返回 → EVAL[猎物场] 三档：同上 → 返回 running weight（逐步累积，无合并步）
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-RKB-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：rocky_reef_structure；hard_shell_prey_field

weight = 1.0
第 1 步 EVAL[rocky_reef_structure（沿岸岩礁结构 1-10m）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@RKB…Profile 值域，不冻结）
第 2 步 EVAL[hard_shell_prey_field（底栖硬壳猎物：贝类/海胆——喙齿磿碎方向锚，食性 FishBase 无述 EO 弱证据）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@RKB…Profile 值域，不冻结）
返回 weight（2 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB 主句:'Inhabits coastal rocky reefs'（岩礁 1-10m）——栖息主句=第一判据（蓝鳃判例同型：结构证据强+食性证据弱→结构先行）
- A-S1/S2: EO(磯食无述)/EO(喙齿磿碎)——食性证据弱，硬壳猎物场步记 open_semantics
- C: reef-associated 1-10m / 17-27°C / hunting macrofauna / 性格=追猎
- B §2.2: 追击组双槽（硬壳猎物场+岩礁结构）受限还原——本推导按 A 主句证据倒序（结构先行），与 B 样板展示序相反=顺序判据分歧记录

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-RKB-BAKE） |
|---|---|
| BakeTemplate | SPACE_FIRST_DUAL_TIER_CHAIN（渐进累积语义） |
| Step 数 | 2 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_STRUCTURE_FACTOR |
| Step1.Factor/Axis | rocky_reef_structure（沿岸岩礁结构 1-10m）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step2.Factor/Axis | hard_shell_prey_field（底栖硬壳猎物：贝类/海胆——喙齿磿碎方向锚，食性 FishBase 无述 EO 弱证据）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| space_factor | typed：水层带/结构/栖境带 |
| forage_field | typed：猎物场/资源场 |
| tier_members | Profile 值域（档位成员不冻结） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*