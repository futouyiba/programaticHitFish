#### BASS-S｜大口黑鲈 SummerStress

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、54 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_S_B**
```text
表达 BASS_S_B 用于 LargemouthBass.SummerStress / BAKE
模板 S_SUMMER（固定结构，仅展开便于阅读）
配置：
  OxygenMin = @BASS_S_B_OxygenMin
  Cooling = @BASS_S_B_Cooling
  Oxygen = @BASS_S_B_Oxygen
  Tradeoff = @BASS_S_B_Tradeoff
执行：
若 target.oxygen_mg_l < @BASS_S_B_OxygenMin：返回 空间权重(0)
C = 查曲线(@BASS_S_B_Cooling, target.relative_cooling)
O = 查曲线(@BASS_S_B_Oxygen, target.oxygen_margin)
T = 查曲线(@BASS_S_B_Tradeoff, target.cover_prey_tradeoff)
返回 空间权重(C × O × T)
```

本例结果：
```json
{
  "case": "BASS-S",
  "binding": "BASS_S_B",
  "template": "S_SUMMER",
  "intermediate": {
    "Cooling": 0.8,
    "Oxygen": 0.75,
    "Tradeoff": 0.6
  },
  "result": 0.36000000000000004
}
```

**BASS_S_R**
```text
表达 BASS_S_R 用于 LargemouthBass.SummerStress / RESPONSE
模板 R_FEED_REACTION（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_S_R_Match
  Presentation = @BASS_S_R_Presentation
  Salience = @BASS_S_R_Salience
  Pursuit = @BASS_S_R_Pursuit
执行：
F = 查曲线(@BASS_S_R_Match, response.feeding_match) × 查曲线(@BASS_S_R_Presentation, response.presentation_fit)
R = 查曲线(@BASS_S_R_Salience, response.trigger_salience) × 查曲线(@BASS_S_R_Pursuit, response.sustained_pursuit_demand)
返回 响应强度(MAX(F, R))
// 两通道均评价；强短刺激与持续高速追逐是两个独立输入。
```

本例结果：
```json
{
  "case": "BASS-S",
  "binding": "BASS_S_R",
  "template": "R_FEED_REACTION",
  "intermediate": {
    "Match": 0.28,
    "Presentation": 0.75,
    "Salience": 0.63,
    "Pursuit": 0.91,
    "Feeding": 0.20999999999999996,
    "Reaction": 0.5733
  },
  "result": 0.5733
}
```

**BASS_S_Q**
```text
表达 BASS_S_Q 用于 LargemouthBass.SummerStress / QUALITY
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
  "case": "BASS-S",
  "binding": "BASS_S_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 35,
      "Large": 18.0,
      "Rare": 3.5999999999999996
    }
  },
  "result": {
    "Small": 0.46904315196998125,
    "Medium": 0.3283302063789869,
    "Large": 0.16885553470919326,
    "Rare": 0.03377110694183865
  }
}
```
