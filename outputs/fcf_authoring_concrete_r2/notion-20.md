#### C06｜护巢蓝鳃太阳鱼

Previous: Defense/Feeding precedence 未决 → Updated: 上游 Guarding 分群，只评价 Defense 并返回。普通 Feeding Slot 不存在；不声称现实绝不摄食。

样本涉及 3 张作者表、5 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.intrusion_strength": 0.5
}
```

**C06_R**
```text
表达 C06_R 用于 Bluegill.Guarding / RESPONSE
模板 R_DEFENSE（固定结构，仅展开便于阅读）
配置：
  Defense = @C06_R_Defense
执行：
Defense = 查曲线(@C06_R_Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。
```

本例结果：
```json
{
  "case": "C06",
  "binding": "C06_R",
  "template": "R_DEFENSE",
  "intermediate": {
    "Defense": 0.6
  },
  "result": 0.6
}
```
