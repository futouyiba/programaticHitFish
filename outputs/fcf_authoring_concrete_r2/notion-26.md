#### C12｜大西洋鲑：上游分群后使用两个绑定

两个 Binding 分别被已分配的 Group 调用，同一鱼不连续执行两个 Binding。Migration 演示选择普通 Feeding 关闭；Reaction 不声称已证明领地攻击或任一单一生物动机。

样本涉及 3 张作者表、15 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.trigger_salience": 0.8,
  "response.sustained_pursuit_demand": 0.2
}
```

**C12_N**
```text
表达 C12_N 用于 AtlanticSalmon.NormalFeeding / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C12_N_Match
  Presentation = @C12_N_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C12_N_Match, response.feeding_match)
P = 查曲线(@C12_N_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C12",
  "binding": "C12_N",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.8,
    "Presentation": 0.75,
    "Feeding": 0.6000000000000001
  },
  "result": 0.6000000000000001
}
```

**C12_M**
```text
表达 C12_M 用于 AtlanticSalmon.FreshwaterSpawningMigration / RESPONSE
模板 R_REACTION（固定结构，仅展开便于阅读）
配置：
  Salience = @C12_M_Salience
  Pursuit = @C12_M_Pursuit
执行：
R = 查曲线(@C12_M_Salience, response.trigger_salience)
D = 查曲线(@C12_M_Pursuit, response.sustained_pursuit_demand)
返回 响应强度(R × D)
// 上游 Migration 分群；普通 Feeding 关闭。不读取 Runtime Stage Predicate。
```

本例结果：
```json
{
  "case": "C12",
  "binding": "C12_M",
  "template": "R_REACTION",
  "intermediate": {
    "Salience": 0.4,
    "Pursuit": 0.82,
    "Reaction": 0.328
  },
  "result": 0.328
}
```
