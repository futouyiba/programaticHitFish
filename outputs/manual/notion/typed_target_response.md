> **类型**：类型化目标摄食响应（TYPED_TARGET_RESPONSE）｜面：Response｜状态：CANDIDATE｜名义成员：248

## 特点

全库最大响应族——对离散饵目标做类型化食物评价，三档决定吃不吃。

## 中文伪脚本（渐进累积语义）

```plain text
读取 饵/Presentation 事实（尺寸/速度/轨迹/相对位置）
EVAL_TARGET_AS_FOOD[typed] → FoodEvaluation
DECIDE 三档：接受=全额响应 / 边际=低响应 / 无响应=出局
返回 FeedingResponse
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| evaluator | typed Profile |
| tiers | 三档 DECIDE |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
