> **类型**：patch 门+双槽档链（PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

资源斑块门+双槽档位（BRT 出族单成员，PROV）。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[斑块在场]
SLOT[槽1] 档位
SLOT[槽2] 档位
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| patch_gate | 二元 |
| dual_slots | 双槽档 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
