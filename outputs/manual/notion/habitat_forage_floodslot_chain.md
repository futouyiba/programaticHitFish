> **类型**：栖息→猎物+洪泛槽链（HABITAT_FORAGE_FLOODSLOT_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

栖息→猎物双步，链尾挂洪泛连通槽（modifier 非 gate；巴沙/斯氏鳊）。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[栖息带] 三档
EVAL[猎物资源] 三档
SLOT[洪泛林连通]：连通=全额/边缘=削减/断连=极低削减
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| flood_slot | DynamicSpatialSlot modifier |
| habitat/forage | typed |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
