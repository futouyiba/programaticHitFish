#### C13｜红鲑：三个独立情景，先解决范围

J 展示浮游/小型悬浮猎物 feeding；O 的 FeedingMatch 输入可覆盖浮游与较大猎物；S 演示停食取0。三者由上游 lifecycle 情景绑定，未证明 J 是正常可钓场景，不作 breaker、不加 Runtime Selector。

样本涉及 3 张作者表、24 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75
}
```

**C13_J**
```text
表达 C13_J 用于 Sockeye.JuvenileSuspended / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_J_Match
  Presentation = @C13_J_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_J_Match, response.feeding_match)
P = 查曲线(@C13_J_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_J",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.64,
    "Presentation": 0.75,
    "Feeding": 0.4800000000000001
  },
  "result": 0.4800000000000001
}
```

**C13_O**
```text
表达 C13_O 用于 Sockeye.OceanFeedingAdult / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_O_Match
  Presentation = @C13_O_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_O_Match, response.feeding_match)
P = 查曲线(@C13_O_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_O",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.8,
    "Presentation": 0.75,
    "Feeding": 0.6000000000000001
  },
  "result": 0.6000000000000001
}
```

**C13_S**
```text
表达 C13_S 用于 Sockeye.FreshwaterSpawningAdult / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_S_Match
  Presentation = @C13_S_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_S_Match, response.feeding_match)
P = 查曲线(@C13_S_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_S",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.0,
    "Presentation": 0.75,
    "Feeding": 0.0
  },
  "result": 0.0
}
```
