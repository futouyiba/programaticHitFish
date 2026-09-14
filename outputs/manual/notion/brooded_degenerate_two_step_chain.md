> **口孵退化两步链**（`BROODED_DEGENERATE_TWO_STEP_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

卵含在嘴里=没有外部锚：常驻区适配单步即终值（无关系轴/无温度轴/无合并步；银龙/罗非雌面）。

## 骨架（一行链序）

```plain text
读取 常驻区事实 → EVAL[常驻区适配] 三档（单 Factor） → 返回 running weight（退化链）
```

## 完全展开实例伪脚本（canonical 真形体：P-RB3-ARO-RESP-RESP）

（渐进累积完全展开——每个 early return 转折点显形；每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

```plain text
读取：brood_anchor_present；brooding_home_range_quality

weight = 1.0
第 1 步 GATE[brood_anchor_present（口哺锚存在性——与个体绑定的携带型锚）]（二元硬门——非三档）：
    命中门条件 → 进入第 2 步
    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 1）
第 2 步 EVAL[brooding_home_range_quality（口哺期常驻区适配——单 Factor 三档）]（三档分级命中）：
    如果 ∈ 最适应档（preferred） → weight ×1.0（全额乘入），继续下一步
    否则如果 ∈ 可接受档（tolerated） → weight ×衰减系数（Profile 值域，不清零），继续下一步
    否则（不居留档 excluded） → 返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）
    （档位成员与阈值＝@ARO-RESP…Profile 值域，不冻结）
返回 weight（2 步渐进累积完成——无终步合并步）
```

**顺序推导证据**（逐鱼推导依据，节选）：
- 裁决材料（退化链方向）：①guarding/nile_tilapia.md §0 Brooding 面退化链判读（『口孵锚与个体绑定——无关系轴/无温度轴/无合并步』）为 B 层唯一口孵型判读先例；②ARO story『carries…in his mouth』=携带型同构（锚在口中=无锚址距离/朝向的空间关系语义）；③B 系列无银龙 guard 面（normal2/silver_arowana.md §0：P04 边界归 Guarding 系补批未做——无对立证据）
- B5 盲形全链（PARALLEL 双 Path+关系评估）=P04 契约模板套用（『携带型 vs 结构型 anchor 差异留判同阶段』——B5 冻结体自注），非银龙特有证据
- 保留张力：口哺期水面跳跃捕食并存的生理张力（罗非口孵=强 Feeding Cap；银龙开放）——若后续证据证实口哺期全功能摄食+冲突并行，双 Path 读法可复活（HRQ 终裁项）

## 配置表（真实结构·字段-值）

| 字段 | 值（实例=P-RB3-ARO-RESP-RESP） |
|---|---|
| BakeTemplate | BROODED_DEGENERATE_TWO_STEP_CHAIN（渐进累积语义） |
| Step 数 | 2 步 |
| Early Return 转折点数 | 2（每 EVAL 步 1 个不居留档出口＋每 GATE 步 1 个不过门出口） |
| Combine | 无终步合并（weight 逐步累积） |
| Step1.Op | GATE_GUARD_ANCHOR_EXISTENCE |
| Step1.Factor/Axis | brood_anchor_present（口哺锚存在性——与个体绑定的携带型锚）（@Profile 值域不冻结） |
| Step1.TierSet | 成立=进入下一步 / 不成立=EARLY_RETURN 返回 0 |
| Step2.Op | EVAL_ANCHOR_SITE_SUITABILITY |
| Step2.Factor/Axis | brooding_home_range_quality（口哺期常驻区适配——单 Factor 三档）（@Profile 值域不冻结） |
| Step2.TierSet | preferred=全额 / tolerated=×衰减(不清零) / excluded=×0.01 软出局立即返回 |
| 数值状态 | 全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| brooded | 结构级退化边界成员 |
| home_range | 单因子 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*