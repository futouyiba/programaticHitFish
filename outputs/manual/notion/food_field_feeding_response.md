> **类型**：场摄食响应（FOOD_FIELD_FEEDING_RESPONSE）｜面：Response｜状态：CANDIDATE｜名义成员：16

## 特点

吃的是「场」（浓度/丰度）不是离散目标——RETURN 硬判据（evaluand=场）与 TYPED 分立。

## 中文伪脚本（渐进累积语义）

```plain text
读取 场浓度事实
EVAL_FIELD → FieldEvaluation
DECIDE 三档
返回 FieldFeedingResponse
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| evaluand | field（RETURN 硬判据） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
