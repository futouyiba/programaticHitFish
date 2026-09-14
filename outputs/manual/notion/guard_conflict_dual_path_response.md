> **类型**：护巢双路径并行响应（GUARD_CONFLICT_DUAL_PATH_RESPONSE）｜面：Response｜状态：CANDIDATE｜名义成员：28

## 特点

食物∥入侵者两条路径并行评估后合并——不是切换，是并行竞争（∥ 拓扑）。

## 中文伪脚本（渐进累积语义）

```plain text
并行：EVAL[食物] 与 EVAL[入侵威胁]
合并双路径评价（算子待机制侧）
DECIDE → Defense/Feeding/低响应
返回 Response
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| topology | ∥ 并行（≠IF 门互斥） |
| combine | 双路径合并 |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
