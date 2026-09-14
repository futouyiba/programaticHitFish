> **类型**：门化温度次置四步链（GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

巨骨舌鱼栖息面真形：门+四步，温度第二位（25-29℃ 窄带证据压过结构[需正文]）。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[硬门]
EVAL[温度]（次置——窄带强证据）
EVAL[结构]
EVAL[时段]
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| order | 温→构→时（vs 美鱥构→温→时=ORDER 差异不并） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
