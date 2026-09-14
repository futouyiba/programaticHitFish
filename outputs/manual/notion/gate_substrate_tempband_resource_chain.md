> **类型**：底质门→深冷带→资源链（GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：4

## 特点

深冷水种（白鲑/黄鲈）：底质门先行，接着深冷复合带，再资源。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[底质]
EVAL[深冷复合带] 三档（如 −1.3~14℃ 带归属）
EVAL[资源] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| tempband | 深冷带档 |
| substrate_gate/resource | typed |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
