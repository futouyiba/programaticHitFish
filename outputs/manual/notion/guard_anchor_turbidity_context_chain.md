> **类型**：护巢四步+浊度语境链（GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

护巢锚门四步后加一个浊度修饰步（浑水种淡水石斑/朱氏鲈）。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[锚存在性]
EVAL[锚适配]
EVAL[关系]
EVAL[温度]
EVAL[浊度] 三档（语境修饰）
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| turbidity | 语境档（unary 修饰步） |
| anchor | 四形式 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
