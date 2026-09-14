> **类型**：双硬门因子集链（HARD_GATED_FACTOR_COMBINE）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

生死门前置：水面可达+温度极值双硬门，过了门才轮到因子集（肺鱼/电鳗；电感知不进 Bake）。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[水面可达]：否→×0.01 软出局
GATE[温度极值]：否→×0.01 软出局
因子集：各因子档位逐步乘入（EXIT 档出局）
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| hard_gates | surface_access + 极值门 |
| factor_set | typed bounded；v2 canonical（LUN 源+EEL） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
