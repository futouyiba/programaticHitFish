> **场摄食响应**（`FOOD_FIELD_FEEDING_RESPONSE`）｜面：Response｜状态：CANDIDATE｜名义成员：16

## 特点

吃的是「场」（浓度/丰度）不是离散目标——RETURN 硬判据（evaluand=场）与 TYPED 分立。

## 骨架（一行链序）

```plain text
读取 场浓度事实 → EVAL_FIELD → FieldEvaluation → DECIDE 三档 → 返回 FieldFeedingResponse
```

## 完全展开实例伪脚本（鲢/鳙类场摄食（FOOD_FIELD 族·16 成员））

```plain text
读取 当前格子的滤食场浓度事实（prey_fields 绑定的浮游生物量——UsableForageAvailability 契约输出）

EVAL_FIELD_CONCENTRATION（三档分级命中）：
    如果 ∈ 富集档 → weight×1.0（全额乘入），继续
    否则如果 ∈ 中等档 → weight×衰减系数（不清零），继续
    否则（贫瘠档）→ 返回 weight×0.01（软出局——场没了，格子出局）

DECIDE_RESPONSE（三档）：
    FieldEvaluation ∈ 摄食活跃档 → 返回 Response(FieldFeeding)（全额响应）
    ∈ 边际档 → 低强度滤食响应（削减不清零）
    否则 → 无响应（出局）

返回 FieldFeedingResponse
```

## 配置表（真实结构·字段-值）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-FIELD-CONCENTRATION（渐进累积） |
| evaluand | field（场浓度——RETURN 硬判据：与离散目标 TYPED 分立） |
| prey_fields | @…FilterFieldPreyFields（浮游 prey class 绑定） |
| @ConcentrationProfile | 三档档位成员=Profile 值域不冻结 |
| DECIDE 档 | 接受=全额 / 边际=削减 / 无响应=出局 |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| evaluand | field（RETURN 硬判据） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*