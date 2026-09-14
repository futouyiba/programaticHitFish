> **类型**：结构先行四步链（STRUCTURE_FIRST_QUAD_TIER_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

蓝鳃栖息面真形：结构→…四步，结构第一（用户裁正「蓝鳃可能结构第一」的推导证实）。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[结构] 三档（先行）
EVAL[水层] 三档
EVAL[温度] 三档
EVAL[时段] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| factor_order | 结构→水层→温度→时段（推导序） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
