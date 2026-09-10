#### C05｜玻璃梭鲈：低光空间

Light 是 S_FIXED 预定义 Slot；本例开启。没有新建昼夜 Runtime Mode，生产空间顺序未冻结。

样本涉及 4 张作者表、21 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 15,
  "target.anchor_distances_m": {
    "stable_cover": 0
  },
  "target.depth_m": 8,
  "target.illuminance_lux": 100
}
```

**C05_B**
```text
表达 C05_B 用于 Walleye.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C05_B_Temperature
  Anchor = @C05_B_Anchor
  Structure = @C05_B_Structure
  Depth = @C05_B_Depth
  Light = @C05_B_Light
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C05_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C05_B_Anchor]
S = 查曲线(@C05_B_Structure, AnchorDistance)
D = 查曲线(@C05_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(@C05_B_Light, target.illuminance_lux) 否则 1
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
  "case": "C05",
  "binding": "C05_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 0,
    "Structure": 1,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Light": 0.8,
    "Base": 0.8
  },
  "result": 0.8
}
```
