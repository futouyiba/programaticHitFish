#### Q2｜品质并列修正 Q2

低活性：Small/Medium×1.2，Large/Rare×0.7。桶与成体关系只是演示映射，不声称小=幼体、大=成体的生物同一性。

样本涉及 6 张作者表、29 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "gear.hook_size_index": 1,
  "gear.bait_size_cm": 3,
  "quality_context.time_band": "inactive",
  "quality_context.water_temp_c": 20
}
```

**Q2**
```text
表达 Q2 用于 IllustrativeQuality / QUALITY
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
  "case": "Q2",
  "binding": "Q2",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "LowActivity/Small",
      "LowActivity/Medium",
      "LowActivity/Large",
      "LowActivity/Rare"
    ],
    "raw": {
      "Small": 60.0,
      "Medium": 36.0,
      "Large": 10.5,
      "Rare": 3.5
    }
  },
  "result": {
    "Small": 0.5454545454545454,
    "Medium": 0.32727272727272727,
    "Large": 0.09545454545454546,
    "Rare": 0.031818181818181815
  }
}
```
