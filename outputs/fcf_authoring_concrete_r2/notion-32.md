#### BASS-G｜大口黑鲈 Guarding

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、51 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

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

**BASS_G_B**
```text
表达 BASS_G_B 用于 LargemouthBass.Guarding / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @BASS_G_B_Temperature
  Anchor = @BASS_G_B_Anchor
  Structure = @BASS_G_B_Structure
  Depth = @BASS_G_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@BASS_G_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@BASS_G_B_Anchor]
S = 查曲线(@BASS_G_B_Structure, AnchorDistance)
D = 查曲线(@BASS_G_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(关闭槽位（不可读取）, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(关闭槽位（不可读取）, target.cover_distance_m)
Deep = 查曲线(关闭槽位（不可读取）, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "BASS-G",
  "binding": "BASS_G_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "nest_site",
    "AnchorDistance": 2.5,
    "Structure": 0.8,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.8
  },
  "result": 0.8000000000000003
}
```

**BASS_G_R**
```text
表达 BASS_G_R 用于 LargemouthBass.Guarding / RESPONSE
模板 R_DEFENSE（固定结构，仅展开便于阅读）
配置：
  Defense = @BASS_G_R_Defense
执行：
Defense = 查曲线(@BASS_G_R_Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。
```

本例结果：
```json
{
  "case": "BASS-G",
  "binding": "BASS_G_R",
  "template": "R_DEFENSE",
  "intermediate": {
    "Defense": 0.8
  },
  "result": 0.8
}
```

**BASS_G_Q**
```text
表达 BASS_G_Q 用于 LargemouthBass.Guarding / QUALITY
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
  "case": "BASS-G",
  "binding": "BASS_G_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 20,
      "Medium": 40,
      "Large": 45.0,
      "Rare": 12.0
    }
  },
  "result": {
    "Small": 0.17094017094017094,
    "Medium": 0.3418803418803419,
    "Large": 0.38461538461538464,
    "Rare": 0.10256410256410256
  }
}
```
