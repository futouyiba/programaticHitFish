# RC4 旗舰追踪样例（Flagship Traces）

这些是紧凑的验收追踪样例。它们规定语义输入与玩家可见证据；不引入鱼种×饵或季节系数。

## 产卵护巢鲈鱼（Spawn Bass）

```text
temperature/season progression
  -> LifecycleCommitment(mature, SPAWN_GUARD)
  -> stable SliceKey(bass_stock, mature, SPAWN_GUARD)
depth + substrate + structure + light
  -> OccupancyAllocationGrade(PRIME on SPAWN_SITE)
NEST_INTRUSION_ONSET
  -> Perception A -> DEFEND motive -> EntryOffer E
  -> finite entry -> Candidate -> THREAT_TRACK
INTRUSION_REMAINS_2S + INTRUSION_PERSISTS
  -> COMMIT_READY -> ContactIntent(BITE_REMOVE or allowed defensive type)
```

玩家策略：离开巢床、改变入侵距离，或改变停顿/持续性。不要求与猎物形态相似。

## 鳟鱼漂流（Trout Drift）

```text
temperature + DO + flow
  -> occupancy and task context
player control + current
  -> ActualPresentation(drift quality, speed, stability)
light/turbidity/occlusion
  -> Perception A
prey-shaped drift cue
  -> FORAGE motive -> EntryOffer E -> Candidate
intercept demand
  -> deterministic Conversion (difficulty remains observable)
```

玩家策略：改变位置、漂流路线、速度、稳定性或深度。同一种拖拽后果必须只有一个归属方：
物理上不可能时归进入（Entry），只是困难时归转化（Conversion）。

## 鲤鱼静态饵（Carp Static Bait）

```text
groundbait deployment
  -> Resource Patch / cue
  -> future aggregation
  -> ARRIVAL of newly eligible finite mass
  -> FORAGE Entry
actual consumption
  -> future SatiationMixture
```

玩家策略：等待新增到达质量、改变呈现或换位。替代性的资源竞争与饱食相互独立，因此
鱼的出现量可以上升而转化下降，无需隐藏的倒 U 形系数。
