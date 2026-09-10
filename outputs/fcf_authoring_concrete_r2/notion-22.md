#### C08｜罗非鱼：固定双通道

Previous: SELECT Profile candidate/结构未决 → Updated: 单 evaluator + 两固定 Slot 已闭合。MAX 只是本样本固定聚合函数，具体数值/聚合生产标定未完成；不是结构 blocker。

样本涉及 3 张作者表、7 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.grazing_availability": 0.75,
  "food.suspended_availability": 0.5
}
```

**C08_R**
```text
表达 C08_R 用于 Tilapia.Feeding / RESPONSE
模板 R_DUAL_FIXED（固定结构，仅展开便于阅读）
配置：
  Grazing = @C08_R_Grazing
  Suspended = @C08_R_Suspended
执行：
G = 查曲线(@C08_R_Grazing, food.grazing_availability)
S = 查曲线(@C08_R_Suspended, food.suspended_availability)
返回 响应强度(MAX(G, S))
// G、S 总是都算。没有按资源条件 SELECT Profile。
```

本例结果：
```json
{
  "case": "C08",
  "binding": "C08_R",
  "template": "R_DUAL_FIXED",
  "intermediate": {
    "Grazing": 0.6,
    "Suspended": 0.45
  },
  "result": 0.6000000000000001
}
```
