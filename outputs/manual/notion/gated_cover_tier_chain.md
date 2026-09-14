> **结构门+质量档链**（`GATED_COVER_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：27

## 特点

先过一道二元结构门（门值=gate_axis 八值之一），门内再走因子档位。

## 骨架（一行链序）

```plain text
GATE[结构门]：命中→继续 / 不命中→×0.01 软出局返回 → EVAL[掩护/质量因子] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（北极茴鱼（normal2 表达文件·伏击门 GATE_RIFFLE_GRAVEL·已 ×0.01 对齐））

```plain text
（伪脚本提取失败）
```

## 配置表（真实结构·字段-值——实例文件原表）



## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| gate_axis | 8 值：植被缘/静水/底带/可埋底质/池潭/礁缘/斑块/扰动窗 |
| post_gate_factor | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*