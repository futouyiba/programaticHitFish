> **类型**：门化结构先行四步链（GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

美鱥栖息面真形：先一道门（口器/底栖形态锚），结构先行四步。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[形态锚定门]
EVAL[结构]
EVAL[温度]
EVAL[时段]
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| gate | 形态锚（口器→水层先行判据的 GATE 化） |
| order | 结构→温→时 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
