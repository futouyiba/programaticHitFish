> **类型**：水层+轴段双步链（LAYER_AXIS_DUAL_TIER_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：7

## 特点

第二步是生命周期轴段（深度带/洄游廊道）而非空间因子——轴域限定是与镜像双因子族的分界。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[水层] 三档
EVAL[轴段（深度带/洄游廊道）] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| layer | typed |
| axis_segment | lifecycle 轴段（非空间因子） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
