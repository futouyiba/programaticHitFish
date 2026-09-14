> **状态门互斥多路径响应**（`STATE_GATED_MULTI_PATH_RESPONSE`）｜面：Response｜状态：CANDIDATE｜名义成员：2

## 特点

先过状态门（如停食洄游态），门内互斥选径（IF 门拓扑——与 ∥ 分立）。

## 骨架（一行链序）

```plain text
IF[状态门]：命中径 A / 未命中径 B（互斥） → 径内 EVAL+DECIDE → 返回 Response
```

## 完全展开实例伪脚本（停食洄游双例（大马哈鱼/美洲西鲱——§9.2 判例））

```plain text
读取 生命周期状态事实（洄游期 premise）

IF[状态门]（互斥选径——与 ∥ 并行分立）：
    命中洄游态 → 走径 A：
        径 A：迁移行为主导（抵目标河段权重高）
        摄食路径＝关闭（停食 premise——「停食≠不咬钩」中的停食侧）
    未命中 → 走径 B：
        径 B：常规 EVAL_TARGET_AS_FOOD + DECIDE 三档

返回 Response
```

## 配置表（真实结构·字段-值）

| 字段 | 值 |
|---|---|
| StateGate | lifecycle=migrating（premise 状态门——IF 拓扑） |
| PathA | 洄游径（停食 premise 携带） |
| PathB | 常规摄食径（typed 评价） |
| 判例 | §9.2：∥ 并行竞争与 IF 门互斥不得互并 |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| state_gate | premise 状态 |
| paths | 互斥多径 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*