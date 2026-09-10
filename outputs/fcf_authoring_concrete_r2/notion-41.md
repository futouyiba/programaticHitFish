#### Q3｜品质并列修正 Q3

BigGear 与 ColdNight 同时命中。后者只读原始水温/时段，不读前者改完的分布。

样本涉及 6 张作者表、29 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "night",
  "quality_context.water_temp_c": 6
}
```

**Q3**
```text
表达 Q3 用于 IllustrativeQuality / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "Q3",
  "binding": "Q3",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare",
      "ColdNight/Large",
      "ColdNight/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 30,
      "Large": 18.0,
      "Rare": 4.800000000000001
    }
  },
  "result": {
    "Small": 0.48638132295719844,
    "Medium": 0.2918287937743191,
    "Large": 0.17509727626459146,
    "Rare": 0.04669260700389106
  }
}
```
