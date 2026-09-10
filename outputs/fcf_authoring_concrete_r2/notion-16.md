#### C02｜斑点叉尾鮰：近底空间

普通近底觅食样本；气味留在 Exposure Owner，本表不再扣一次 Feeding。生产空间顺序未冻结。

样本涉及 4 张作者表、18 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 25,
  "target.anchor_distances_m": {
    "stable_cover": 50
  },
  "target.depth_m": 3
}
```

**C02_B**
```text
表达 C02_B 用于 ChannelCatfish.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C02_B_Temperature
  Anchor = @C02_B_Anchor
  Structure = @C02_B_Structure
  Depth = @C02_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C02_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C02_B_Anchor]
S = 查曲线(@C02_B_Structure, AnchorDistance)
D = 查曲线(@C02_B_Depth, target.depth_m)
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
  "case": "C02",
  "binding": "C02_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 50,
    "Structure": 0.7,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.7
  },
  "result": 0.7000000000000001
}
```
