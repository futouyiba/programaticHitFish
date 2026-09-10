#### C03｜虹鳟：自然漂流匹配

明确 FIRST_MATCH + 默认0；结果只到 ResponseStrength，不创建 Follow/Track/Attack 状态或后生成追击。

样本涉及 6 张作者表、14 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.natural_drift_fit": 0.7
}
```

**C03_R**
```text
表达 C03_R 用于 RainbowTrout.Normal / RESPONSE
模板 R_BANDS（固定结构，仅展开便于阅读）
配置：
  Default = @C03_R_Default
执行：
读取 本次 Scope 的只读 facts
按以下 priority 顺序，第一条满足就返回 指定响应强度
优先级 10：若 (response.feeding_match GE @C03_good_match_value AND response.natural_drift_fit GE @C03_drift_value)：返回 响应强度(0.8)
优先级 20：若 response.feeding_match GE @C03_some_match_value：返回 响应强度(0.25)
否则 返回 响应强度(@C03_R_Default)
```

本例结果：
```json
{
  "case": "C03",
  "binding": "C03_R",
  "template": "R_BANDS",
  "intermediate": {
    "C03_high": true
  },
  "result": 0.8
}
```
