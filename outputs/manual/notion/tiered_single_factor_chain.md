> **类型**：单因子三档链（TIERED_SINGLE_FACTOR_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：94

## 特点

全库最大族——整条空间判断只有一个 typed 因子（轴段/资源斑块/场浓度等），一步定终值。

## 中文伪脚本（渐进累积语义）

```plain text
读取 typed 因子事实
EVAL[typed 因子] 三档：最适应=全额 / 可接受=×衰减 / 不居留=×0.01 软出局
返回 running weight（单步即终值）
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| factor_type | typed：lifecycle 轴段|resource patch|场浓度 field|position 等约 29 亚群 |
| tier_members | Profile 值域 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
