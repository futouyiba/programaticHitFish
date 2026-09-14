> **类型**：结构→夜槽→猎物三步链（STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

夜行结构种（石斑/寡鳞胡瓜鱼？）——结构定位→低光槽→猎物。

## 中文伪脚本（渐进累积语义）

```plain text
EVAL[结构] 三档
SLOT[低光]
EVAL[猎物] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| structure | 先行 |
| light_slot | 中位 |
| forage | 末位 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
