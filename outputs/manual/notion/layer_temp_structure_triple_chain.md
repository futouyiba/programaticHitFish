> **类型**：水层→温度→结构三步链（LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

红腹食人鱼栖息面真形：三步，时段被证据剔除（CSV 全天活跃→不入链）。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[水层]
EVAL[温度]
EVAL[结构]
返回 running weight（无时段步——证据砍步）
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| dropped_factor | 时段（CSV 全天直证剔除） |
| order | 层→温→构 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
