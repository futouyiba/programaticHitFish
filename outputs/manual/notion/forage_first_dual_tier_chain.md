> **觅食先行双因子链**（`FORAGE_FIRST_DUAL_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：34

## 特点

镜像语序——跟着食物走优先，栖息带次之；与空间先行族因子集同、顺序相反，按顺序判据分立。

## 骨架（一行链序）

```plain text
读取 猎物场事实 → EVAL[猎物场] 三档：×0.01 软出局/×衰减/全额 → EVAL[空间因子] 三档：同上 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-POR-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：pelagic_schooling_prey_field；open_thermocline_deep_continuum

weight = 1.0
第 1 步 EVAL[pelagic_schooling_prey_field（中上/底层群游鱼+鱿——食性横跨水层）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@POR…Profile 值域，不冻结）
第 2 步 EVAL[open_thermocline_deep_continuum（开放水/温跃层-深水连续；热生理 typed 容忍扩展=retia mirabilia 8-10°C——story FCI 记 context 非呈现轴）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@POR…Profile 值域，不冻结）
返回 weight（2 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:'Feeds on small and medium-sized pelagic schooling species...squid'+底层鱼(cod/haddock/hake)——食性横跨中上+底层→猎物分布为空间主体，猎物场先行
- A-FCI:'温血=热生理 typed context（与蓝鳍金枪鱼同构——能力/生态位变量非呈现轴）'——温血不立独立判断步，承载为栖息轴容忍扩展注记
- A-RB:'hunt in deep water for extended periods'——温血效应=深水久留，栖息容忍带扩展而非硬边界
- C: pelagic-oceanic 0-1360m / -1~23°C 喜 11（容忍极宽=温血佐证）/ hunting macrofauna / 性格=追猎
- B §2.2: 追击组因子集=猎物场+栖息双槽（槽间序未主张——本推导从 A 正文推得猎物先行）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-POR-BAKE） |
|---|---|
| BakeTemplate | FORAGE_FIRST_DUAL_TIER_CHAIN（渐进累积语义） |
| Step 数 | 2 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step1.Factor/Axis | pelagic_schooling_prey_field（中上/底层群游鱼+鱿——食性横跨水层）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | open_thermocline_deep_continuum（开放水/温跃层-深水连续；热生理 typed 容忍扩展=retia mirabilia 8-10（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| forage_field | typed：先行 |
| space_factor | typed：次位 |
| mirror_of | SPACE_FIRST（顺序判据不并） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*