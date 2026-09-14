> **类型**：状态门互斥多路径响应（STATE_GATED_MULTI_PATH_RESPONSE）｜面：Response｜状态：CANDIDATE｜名义成员：2

## 特点

先过状态门（如停食洄游态），门内互斥选径（IF 门拓扑——与 ∥ 分立）。

## 中文伪脚本（渐进累积语义）

```plain text
IF[状态门]：命中径 A / 未命中径 B（互斥）
径内 EVAL+DECIDE
返回 Response
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| state_gate | premise 状态 |
| paths | 互斥多径 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
