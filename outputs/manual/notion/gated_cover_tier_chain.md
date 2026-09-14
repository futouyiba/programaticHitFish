> **类型**：结构门+质量档链（GATED_COVER_TIER_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：27

## 特点

先过一道二元结构门（门值=gate_axis 八值之一），门内再走因子档位。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[结构门]：命中→继续 / 不命中→×0.01 软出局返回
EVAL[掩护/质量因子] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| gate_axis | 8 值：植被缘/静水/底带/可埋底质/池潭/礁缘/斑块/扰动窗 |
| post_gate_factor | typed |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
