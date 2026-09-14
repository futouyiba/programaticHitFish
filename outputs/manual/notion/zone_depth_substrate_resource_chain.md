> **类型**：底带门五步链（含深度档）（ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

底带门+深度档+底质+资源，五步形。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[底带]
EVAL[深度] 三档
EVAL[底质] 三档
EVAL[资源] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| depth | 显式档位步 |
| substrate/resource | typed |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
