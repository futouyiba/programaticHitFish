> **类型**：环境梯度趋避响应（CUE_GUIDED_APPROACH_AVOID）｜面：Response｜状态：CANDIDATE｜名义成员：1

## 特点

沿环境 cue 梯度趋近或避开（单例族）。

## 中文伪脚本（渐进累积语义）

```plain text
读取 cue 梯度
EVAL[梯度方向] → 趋近/避开
返回 Approach/Avoid
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| cue | 环境梯度 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
