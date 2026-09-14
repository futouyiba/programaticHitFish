> **类型**：底带硬门+底质+资源链（ZONE_SUBSTRATE_RESOURCE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：7

## 特点

非底层直接出局（硬门），然后底质档、资源档。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[底带]：demersal？否→×0.01 软出局
EVAL[底质] 三档
EVAL[资源] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| zone_gate | 底带二元 |
| substrate | typed |
| resource | typed |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
