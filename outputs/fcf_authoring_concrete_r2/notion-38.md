#### G3｜合成压力样本：(春 AND 温) OR (秋 AND 凉)

用于把嵌套条件的实际存法填出来，不升级为已被鱼类证据确认的深层 Group breaker。

样本涉及 5 张作者表、20 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 270,
  "slow.recent5day_temp_c": 15
}
```

**G3**
```text
表达 G3 用于 SyntheticSeasonGroup / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Seasonal = 若 ((slow.day_of_year BETWEEN @g3_spring_date_value AND slow.recent5day_temp_c GE @g3_warm_value) OR (slow.day_of_year BETWEEN @g3_fall_date_value AND slow.recent5day_temp_c LE @g3_cool_value)) 则 @G3Share 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "G3",
  "binding": "G3",
  "template": "G_SHARES",
  "intermediate": {
    "g3_either": true
  },
  "result": {
    "Seasonal": 0.25,
    "Normal": 0.75
  }
}
```
