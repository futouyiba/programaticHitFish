> **类型**：软三步无门链（SOFT_TRIPLE_TIER_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：3

## 特点

无硬门，三步软档直连（跨科重复，PROV 系）。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[因子1] 三档
EVAL[因子2] 三档
EVAL[因子3] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| factors | typed ×3 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
