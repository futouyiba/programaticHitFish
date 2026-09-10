#### BASS-F｜大口黑鲈 ForageChase

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。 Forage 的食物场强度只在 Bake 使用，Response 不再乘同一密度。

样本涉及 8 张作者表、66 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

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

**BASS_F_B**
```text
表达 BASS_F_B 用于 LargemouthBass.ForageChase / BAKE
模板 S_FORAGE（固定结构，仅展开便于阅读）
配置：
  ForageMin = @BASS_F_B_ForageMin
  Forage = @BASS_F_B_Forage
  Vertical = @BASS_F_B_Vertical
  OpenWater = @BASS_F_B_OpenWater
  Temperature = @BASS_F_B_Temperature
  Oxygen = @BASS_F_B_Oxygen
  ColdFront = 开启
  Cover = @BASS_F_B_Cover
  Deep = @BASS_F_B_Deep
执行：
若 target.forage_school_intensity < @BASS_F_B_ForageMin：返回 空间权重(0)
F = 查曲线(@BASS_F_B_Forage, target.forage_school_intensity)
V = 查曲线(@BASS_F_B_Vertical, target.vertical_alignment)
T = 查曲线(@BASS_F_B_Temperature, target.temperature_c)
O = 查曲线(@BASS_F_B_Oxygen, target.oxygen_mg_l)
W = 查曲线(@BASS_F_B_OpenWater, target.open_water_context)
Base = F × V × T × O × W
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(@BASS_F_B_Cover, target.cover_distance_m)
Deep = 查曲线(@BASS_F_B_Deep, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "BASS-F",
  "binding": "BASS_F_B",
  "template": "S_FORAGE",
  "intermediate": {
    "Forage": 0.8,
    "Vertical": 0.75,
    "Temperature": 1.0,
    "Oxygen": 1.0,
    "OpenWater": 1,
    "Base": 0.6,
    "Cover": 0.8,
    "Deep": 0.9,
    "Refuge": 0.9
  },
  "result": 0.75
}
```

**BASS_F_R**
```text
表达 BASS_F_R 用于 LargemouthBass.ForageChase / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_F_R_Match
  Presentation = @BASS_F_R_Presentation
  Familiarity = @BASS_F_R_Familiarity
执行：
F = 查曲线(@BASS_F_R_Match, response.feeding_match)
P = 查曲线(@BASS_F_R_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(@BASS_F_R_Familiarity, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "BASS-F",
  "binding": "BASS_F_R",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.76,
    "Presentation": 0.75,
    "Familiarity": 0.8,
    "Feeding": 0.5700000000000001
  },
  "result": 0.45600000000000007
}
```

**BASS_F_Q**
```text
表达 BASS_F_Q 用于 LargemouthBass.ForageChase / QUALITY
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
  "case": "BASS-F",
  "binding": "BASS_F_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 25,
      "Medium": 50,
      "Large": 30.0,
      "Rare": 6.0
    }
  },
  "result": {
    "Small": 0.22522522522522523,
    "Medium": 0.45045045045045046,
    "Large": 0.2702702702702703,
    "Rare": 0.05405405405405406
  }
}
```
