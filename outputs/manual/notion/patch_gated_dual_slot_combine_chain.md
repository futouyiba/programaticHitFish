> **patch 门+双槽档链**（`PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

资源斑块门+双槽档位（BRT 出族单成员，PROV）。

## 骨架（一行链序）

```plain text
GATE[斑块在场] → SLOT[槽1] 档位 → SLOT[槽2] 档位 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB2-BRT12-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：seasonal_pulse_prey_patch；midupper_soft_layer

weight = 1.0
第 1 步 EVAL[seasonal_pulse_prey_patch（季节脉冲猎物 patch——机会场食物丰度档，'普通摄食与季节猎物脉冲'食性主句先行）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BRT12…Profile 值域，不冻结）
第 2 步 EVAL[midupper_soft_layer（中上层软定位——CSV pelagic-neritic 锚次之；结构安全/水流次级因子无 Story 证据不立）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@BRT12…Profile 值域，不冻结）
返回 weight（2 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- C'-B2: '季节猎物脉冲：猎物资源 patch 强度随季节脉冲波动（ResourcePatch 描述——Story Competing 明言）'——机会型食物丰度先行
- C: pelagic-neritic 0-28m / anadromous / 晨昏活跃
- B §0: 单步链（机会场食物丰度档位）——B 层未含 CSV 层定位步；真形按 A+C 双证据立两步（猎物场先行、水层次之）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB2-BRT12-BAKE） |
|---|---|
| BakeTemplate | PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN（渐进累积语义） |
| Step 数 | 2 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step1.Factor/Axis | seasonal_pulse_prey_patch（季节脉冲猎物 patch——机会场食物丰度档，'普通摄食与季节猎物脉冲'食性主句先行）（@Profile 值域不冻结） |
| Step1.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step2.Op | EVAL_TYPED_LAYER_FACTOR |
| Step2.Factor/Axis | midupper_soft_layer（中上层软定位——CSV pelagic-neritic 锚次之；结构安全/水流次级因子无 Story 证据不立）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| patch_gate | 二元 |
| dual_slots | 双槽档 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*