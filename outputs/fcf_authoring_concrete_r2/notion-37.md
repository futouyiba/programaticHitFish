#### G2｜Group 同快照回退：不满足巢区

Guard share=0；Normal=1。回退是剩余份额，不是 Defense vs Feeding fallback。

样本涉及 5 张作者表、13 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 120,
  "slow.recent5day_temp_c": 18,
  "slow.scene_structures": [
    "open_water"
  ],
  "slow.cold_severity": 0.5,
  "slow.oxythermal_compression": 0.25,
  "slow.pelagic_forage_state": true,
  "slow.open_water_forage_availability": 0.5
}
```

**G2**
```text
表达 G2 用于 G2_GuardNormal / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Guarding = 若 (slow.day_of_year BETWEEN @guard_dates_value AND slow.recent5day_temp_c GE @guard_temp_value AND slow.scene_structures CONTAINS_ANY @guard_nest_value) 则 @BassGuardShare 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "G2",
  "binding": "G2",
  "template": "G_SHARES",
  "intermediate": {
    "guard_all": false
  },
  "result": {
    "Guarding": 0,
    "Normal": 1
  }
}
```
