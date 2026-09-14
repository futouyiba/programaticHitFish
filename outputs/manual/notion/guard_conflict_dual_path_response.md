> **护巢双路径并行响应**（`GUARD_CONFLICT_DUAL_PATH_RESPONSE`）｜面：Response｜状态：CANDIDATE｜名义成员：26

## 特点

食物∥入侵者两条路径并行评估后合并——不是切换，是并行竞争（∥ 拓扑）。（名义 26=registry v10 counts_v10 口径：四形式正式 nest 11/egg_mass 7/fry_school 6/host_brood 2；另 2 条 brooded 边界注记不计名义）

## 骨架（一行链序）

```plain text
并行：EVAL[食物] 与 EVAL[入侵威胁] → 合并双路径评价（算子待机制侧） → DECIDE → Defense/Feeding/低响应 → 返回 Response
```

## 完全展开实例伪脚本（护巢期双路径并行（live 例 1C 形态·§17.5 RR-T2））

```plain text
读取 当前格子的食物机会事实
读取 侵入者威胁事实（侵入距离/持续时间/威胁 Cue）

并行（∥ 拓扑——两条路径同时评估，不是切换）：
    路径 A：EVAL_FOOD_OPPORTUNITY → FoodEvaluation
    路径 B：EVAL_INTRUDER_THREAT → ThreatEvaluation

COMBINE_DUAL_PATH：
    合算两路径评价（合并算子数学＝机制侧定义——OPERATOR 占位）

DECIDE_RESPONSE（三档）：
    威胁主导 → 返回 Response(Defense)
    食物主导且无威胁 → 返回 Response(TargetFeeding)
    双边际 → 低强度混合响应

返回 Response
```

## 配置表（真实结构·字段-值）

| 字段 | 值 |
|---|---|
| ResponseTemplate | RR-DEFENSE-01 / RR-T2（∥ 双路径并行——≠IF 门互斥） |
| PathA.Evaluator | @FoodOpportunityProfile |
| PathB.Evaluator | @IntruderThreatProfile |
| CombineOp | COMBINE_DUAL_PATH（数学待机制侧） |
| 仲裁注记 | live V0：Guarding Group 只评 Defense（例 1C）——本族真值属 census↔live 对账 |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| topology | ∥ 并行（≠IF 门互斥） |
| combine | 双路径合并 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*