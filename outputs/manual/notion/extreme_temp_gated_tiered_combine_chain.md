> **类型**：极值门+无序因子集链（EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

极值温度门+因子无序集（OSC 出族单成员，PROV）。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[极值温度]
因子无序集：各因子 EXIT 档/档位乘入
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| temp_gate | 前置 |
| factor_set | unordered（证据未裁决序） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
