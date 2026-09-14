> **类型**：觅食先行双因子链（FORAGE_FIRST_DUAL_TIER_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：34

## 特点

镜像语序——跟着食物走优先，栖息带次之；与空间先行族因子集同、顺序相反，按顺序判据分立。

## 中文伪脚本（渐进累积语义）

```plain text
读取 猎物场事实
EVAL[猎物场] 三档：×0.01 软出局/×衰减/全额
EVAL[空间因子] 三档：同上
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| forage_field | typed：先行 |
| space_factor | typed：次位 |
| mirror_of | SPACE_FIRST（顺序判据不并） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
