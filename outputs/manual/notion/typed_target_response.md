> **类型化目标摄食响应**（`TYPED_TARGET_RESPONSE`）｜面：Response｜状态：CANDIDATE｜名义成员：248

## 特点

全库最大响应族——对离散饵目标做类型化食物评价，三档决定吃不吃。

## 骨架（一行链序）

```plain text
读取 饵/Presentation 事实（尺寸/速度/轨迹/相对位置） → EVAL_TARGET_AS_FOOD[typed] → FoodEvaluation → DECIDE 三档：接受=全额响应 / 边际=低响应 / 无响应=出局 → 返回 FeedingResponse
```

## 完全展开实例伪脚本（蓝鳃太阳鱼（Response 面·R-T1 单通道·DECIDE 三档已展开））

```plain text
读取 当前 Presentation 与巢区 / 护幼对象的关系
读取 侵入距离、持续时间、威胁 Cue

EVAL_INTRUDER_THREAT：
    用这些侵入事实评价 @BluegillGuardThreatProfile
    得到 ThreatEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-002 展开——原「评价→得到 DefenseResponse」为平铺占位；
与 §3.1 配置表「命中=返回防御 Response / 未命中=返回低、无响应」两列语义对齐）：
    按三档判定 ThreatEvaluation（档位成员=@BluegillGuardThreatProfile 值域不冻结）：
    如果 ThreatEvaluation ∈ 高威胁档：
        返回 Response(Defense)（全额防御响应）
    否则如果 ∈ 边际威胁档：
        返回低强度防御响应（削减但不清零）
    否则（无威胁档）：
        返回无响应（出局）

返回 DefenseResponse
不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program）
```

## 配置表（真实结构·字段-值——实例文件原表）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @BluegillGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding；Reaction 槽 OFF） | @BluegillNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| evaluator | typed Profile |
| tiers | 三档 DECIDE |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*