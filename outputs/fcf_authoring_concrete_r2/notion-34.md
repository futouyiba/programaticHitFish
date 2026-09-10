#### BASS-ROUTING｜鲈鱼：五群并列 Share

四项特殊 share 与 normal residual 共5群。为暴露 overlap 验证，此演示快照同时置入冷/夏压力；是合成测试，不声称典型水体会同时如此。

样本涉及 6 张作者表、33 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 120,
  "slow.recent5day_temp_c": 18,
  "slow.scene_structures": [
    "nest_cover"
  ],
  "slow.cold_severity": 0.5,
  "slow.oxythermal_compression": 0.25,
  "slow.pelagic_forage_state": true,
  "slow.open_water_forage_availability": 0.5
}
```

**BASS_G**
```text
表达 BASS_G 用于 LargemouthBass / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Guarding = 若 (slow.day_of_year BETWEEN @guard_dates_value AND slow.recent5day_temp_c GE @guard_temp_value AND slow.scene_structures CONTAINS_ANY @guard_nest_value) 则 @BassGuardShare 否则 0
ColdSlow = 若 slow.cold_severity GT @cold_any_value 则 查曲线(@BassColdShare, slow.cold_severity) 否则 0
SummerStress = 若 slow.oxythermal_compression GT @summer_any_value 则 查曲线(@BassSummerShare, slow.oxythermal_compression) 否则 0
ForageChase = 若 (slow.pelagic_forage_state EQ @forage_state_value AND slow.open_water_forage_availability GT @forage_available_value) 则 查曲线(@BassForageShare, slow.open_water_forage_availability) 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "BASS-ROUTING",
  "binding": "BASS_G",
  "template": "G_SHARES",
  "intermediate": {
    "guard_all": true,
    "cold_any": true,
    "summer_any": true,
    "forage_all": true
  },
  "result": {
    "Guarding": 0.2,
    "ColdSlow": 0.15,
    "SummerStress": 0.1,
    "ForageChase": 0.1,
    "Normal": 0.45000000000000007
  }
}
```
