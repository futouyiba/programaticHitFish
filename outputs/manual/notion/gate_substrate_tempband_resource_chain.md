> **底质门→深冷带→资源链**（`GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：4

## 特点

深冷水种（白鲑/黄鲈）：底质门先行，接着深冷复合带，再资源。

## 骨架（一行链序）

```plain text
GATE[底质] → EVAL[深冷复合带] 三档（如 −1.3~14℃ 带归属） → EVAL[资源] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（canonical 真形体：P-RB1-WIT-BAKE）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：可埋软泥底质；cold_deep_mud_band；benthic_invert_prey_field

weight = 1.0
第 1 步 GATE[可埋软泥底质（鲽形目贴底埋伏体构——'soft mud bottoms'）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[cold_deep_mud_band（深冷泥底复合带：2-6°C / usually 45-366m——story 原文复合描述不拆解）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@WIT…Profile 值域，不冻结）
第 3 步 EVAL[benthic_invert_prey_field（甲壳/多毛/蛇尾+鱼类）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@WIT…Profile 值域，不冻结）
返回 weight（3 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- A-RB:'soft mud bottoms in fairly deep water'+'2°C - 6°C'+'usually 45 - 366 m'——软泥可埋先行（鲽形目体构），深冷泥底复合带次之（原文一句群不虚构拆解）
- A-S1: MSF(甲壳/多毛/蛇尾)——底栖无脊椎资源步有据
- C: demersal 18-1570m / 2-6°C 喜 4（极窄深冷带）——深冷强锚
- B §2.2: 伏击组 GATE_BURYABLE→掩体档两步——本推导多出深冷复合带步（A 原文级证据）→与 RS1 归族 GATED_COVER_TIER_CHAIN 分歧挂 HRQ（族移动提案）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB1-WIT-BAKE） |
|---|---|
| BakeTemplate | GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN（渐进累积语义） |
| Step 数 | 3 步 |
| Early Return 转折点数 | 3（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_BURYABLE_SUBSTRATE |
| Step1.Factor/Axis | 可埋软泥底质（鲽形目贴底埋伏体构——'soft mud bottoms'）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_TYPED_HABITAT_FACTOR |
| Step2.Factor/Axis | cold_deep_mud_band（深冷泥底复合带：2-6°C / usually 45-366m——story 原文复合描述不拆解）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| Step3.Op | EVAL_TYPED_FORAGE_FACTOR |
| Step3.Factor/Axis | benthic_invert_prey_field（甲壳/多毛/蛇尾+鱼类）（@Profile 值域不冻结） |
| Step3.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| tempband | 深冷带档 |
| substrate_gate/resource | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*