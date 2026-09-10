#### C01｜大西洋鳕：普通觅食空间

T→S→D 是填满样本所选的演示顺序；Owner 的生产空间顺序未冻结。三个独立乘因子交换顺序不改变结果。

样本涉及 4 张作者表、18 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 10,
  "target.anchor_distances_m": {
    "stable_cover": 25
  },
  "target.depth_m": 20
}
```

**C01_B**
```text
表达 C01_B 用于 AtlanticCod.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C01_B_Temperature
  Anchor = @C01_B_Anchor
  Structure = @C01_B_Structure
  Depth = @C01_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C01_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C01_B_Anchor]
S = 查曲线(@C01_B_Structure, AnchorDistance)
D = 查曲线(@C01_B_Depth, target.depth_m)
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
  "case": "C01",
  "binding": "C01_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 25,
    "Structure": 0.8,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.8
  },
  "result": 0.8
}
```
