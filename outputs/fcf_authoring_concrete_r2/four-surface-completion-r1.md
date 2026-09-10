# C01–C15 四面补齐包 R1

## 交付口径

每个 Case 的四个 Surface 均给出状态：`完整投影`、`复用模板`、`明确不适用` 或 `未闭合 TODO`。复用项引用固定 Template ID；配置表行的顺序可调整，但不能改变模板运行顺序或拓扑。

## 可复用模板目录

| Template ID | Surface | 固定 Runtime 语义 |
|---|---|---|
| GR-GENERIC-01 | Group | Lifecycle / 状态事实 → GroupShare → FishGroup Allocation → Group Routing Result |
| BK-SPATIAL-01 | Bake | Temperature → Structure → Depth → optional Light → Fixed Combine → SpatialWeight |
| RS-FEED-01 | Response | PresentationSession → RootOccurrence → OpportunityId/Scope → Match/Presentation → ResponseBand |
| RS-DEFENSE-01 | Response | Guarding事实 → Threat predicate → Defense Profile → Defense Response |
| Q-PARALLEL-01 | Quality | Base Distribution → Condition Modifiers → Fixed Combine → Normalize → Draw |
| Q-DEFER-01 | Quality | 继承 Group Base Distribution；保留 Quality TODO，不删除该执行面 |

## 四面矩阵与具体投影

| Case | Group Routing | Bake | Response | Quality Selection |
|---|---|---|---|---|
| C01 鳕鱼 | 复用 GR-GENERIC-01；无分流差异 | 复用 BK-SPATIAL-01；`@Cod_*` | 复用 RS-FEED-01；`@Cod_Response` | 复用 Q-DEFER-01；继承 `Cod.Normal` |
| C02 叉尾鮰 | 复用 GR-GENERIC-01；`@Catfish_GroupShare` | 复用 BK-SPATIAL-01；`@Catfish_*` | 复用 RS-FEED-01；Exposure 由上游提供 | 复用 Q-DEFER-01；继承 `Catfish.Normal` |
| C03 虹鳟 | 复用 GR-GENERIC-01 | 明确不适用；不改变空间场 | 完整投影；`R_TroutDrift` | 复用 Q-DEFER-01 |
| C04 褐鳟 | 复用 GR-GENERIC-01 | 明确不适用 | 复用 RS-FEED-01；默认摄食 | 复用 Q-DEFER-01 |
| C05 梭鲈 | 复用 GR-GENERIC-01 | 复用 BK-SPATIAL-01；`@Walleye_*` | 复用 RS-FEED-01；低光不重复加 Response | 复用 Q-DEFER-01 |
| C06 蓝鳃 | 复用 GR-GENERIC-01；`Guarding` 分配 | 明确不适用 | 复用 RS-DEFENSE-01；仅 Defense | 复用 Q-DEFER-01；继承 Guarding Base |
| C07 小口黑鲈 | 复用 GR-GENERIC-01；`Parental` 分配 | 明确不适用 | 复用 RS-DEFENSE-01；仅 Defense | 复用 Q-DEFER-01；继承 Parental Base |
| C08 罗非鱼 | 复用 GR-GENERIC-01 | 明确不适用 | 完整投影；RS-FEED-02 固定双 Channel | 复用 Q-DEFER-01 |
| C09 桨鱼 | 复用 GR-GENERIC-01 | 明确不适用 | 复用 RS-FEED-01；FieldFeeding 输入 | 复用 Q-DEFER-01 |
| C10 大口水牛鱼 | 复用 GR-GENERIC-01 | 明确不适用 | 复用 RS-FEED-01；FieldFeeding 输入 | 复用 Q-DEFER-01 |
| C11 鲻鱼 | 复用 GR-GENERIC-01 | 明确不适用 | 复用 RS-FEED-01；FieldFeeding 输入 | 复用 Q-DEFER-01 |
| C12 大西洋鲑 | 完整投影；Normal / Migration 上游分流 | 明确不适用 | 完整投影；RS-FEED-01 + RS-REACTION-01 | 复用 Q-DEFER-01；Group-specific Base |
| C13 红鲑 | 完整投影；Juvenile / Ocean / Freshwater 上游分流 | 明确不适用 | 复用 RS-FEED-01；按 Group Profile | 复用 Q-DEFER-01 |
| C14 边界 | 明确不适用；仅记录边界 | 明确不适用 | 明确不适用；不进入生产 Opportunity | 明确不适用 |
| C15 边界 | 明确不适用；仅记录边界 | 明确不适用 | 明确不适用；不进入生产 Opportunity | 明确不适用 |

## 关键新增中文伪脚本

### C01/C02/C05：共用分群与空间场

```text
读取 Lifecycle、季节、环境和物种事实
→ 由 GroupShare 解析 FishGroup
→ 返回 FishGroup Allocation Result

读取该组的空间输入
→ 按模板固定顺序应用各 Profile
→ 使用固定 Combine 得到 SpatialWeight
→ 返回空间结果
```

### C06/C07：护巢组

```text
读取上游 FishGroup Allocation Result
如果当前组为 Guarding / Parental：
    读取当前刺激与照护区域关系
    如果构成威胁：
        应用 Defense Profile
        返回 Defense Response
    否则：
        返回该组默认 Defense Result
不在本模板内评价普通 Feeding，也不建立 Defense > Feeding 优先级。
```

### C08：双 Channel Feeding

```text
读取当前 FoodField 与 Presentation Opportunity
同一个 Feeding Evaluator 同时读取：
    Grazing Channel → @GrazingProfile
    Suspended Channel → @SuspendedFeedingProfile
按固定聚合规则合并两个 Channel
返回 Feeding Response
不在运行时选择互斥 Mode。
```

### C09–C11：既有 Opportunity 合同

```text
读取 PresentationSession
→ 取得合法 semantic particle
→ 解析 Root Semantic Occurrence
→ 生成 OpportunityId 与 Evaluation Scope
→ 同一 RootOccurrenceKey 只解析一次
→ 将 FoodField 作为本次 FieldFeeding evaluator 输入
→ 返回 Response Result
```

### C12/C13：上游生命周期分流

```text
读取 Lifecycle / FishGroup Allocation Result
根据已完成的上游分流取得 Group-specific Template / Profile
执行该组固定 Response 逻辑
不在同一 Fish Runtime 内新增 Stage Selector。
```

## 结果

- 四面状态已覆盖 C01–C15，共 60 个 Case × Surface 单元。
- `复用模板` 42 项；`完整投影` 6 项；`明确不适用` 11 项；`未闭合 TODO` 1 类，覆盖 C01–C13 的 13 个 Quality 单元（不是缺失 Surface）。
- 新增真正 Runtime Topology：0。
- C08 仍无 PT3 Selector；C06/C07 仍无 PT4 precedence。
- 这些是 Representation 交付补齐，不改变 Frozen Story、Design Gate 或生产参数冻结。


## R1.1 可回放的逐 Case × Surface 记录

以下记录将“复用”具体化为：输入 → 绑定/继承 → 固定执行 → Typed Result → 边界。配置表行可重排，但固定执行顺序不可由实例改变。

| Case×Surface | 输入 | 绑定 / 继承 | 固定执行与中文脚本 | Typed Result | 边界 / 状态 |
|---|---|---|---|---|---|
| C01 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Cod.Normal` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C01 · Bake | temperature、structure、depth | `BK-SPATIAL-01`; `@Cod_*` | 按 Temperature → Structure → Depth 固定顺序查 Profile → Fixed Combine → 返回 SpatialWeight | `SpatialDistributionWeight` | 实例只能改 Profile/参数/Slot；完整投影 |
| C01 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C01_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C01 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Cod.Normal` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C02 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Catfish.Normal` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C02 · Bake | temperature、structure、depth | `BK-SPATIAL-01`; `@Catfish_*` | 按 Temperature → Structure → Depth 固定顺序查 Profile → Fixed Combine → 返回 SpatialWeight | `SpatialDistributionWeight` | 实例只能改 Profile/参数/Slot；完整投影 |
| C02 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C02_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C02 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Catfish.Normal` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C03 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`RainbowTrout.Normal` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C03 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C03 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C03_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C03 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `RainbowTrout.Normal` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C04 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`BrownTrout.Normal` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C04 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C04 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C04_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C04 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `BrownTrout.Normal` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C05 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Walleye.Normal` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C05 · Bake | temperature、structure、depth、light | `BK-SPATIAL-01`; `@Walleye_*` | 按 Temperature → Structure → Depth → Light 固定顺序查 Profile → Fixed Combine → 返回 SpatialWeight | `SpatialDistributionWeight` | 实例只能改 Profile/参数/Slot；完整投影 |
| C05 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C05_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C05 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Walleye.Normal` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C06 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Bluegill.Guarding` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C06 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C06 · Response | PresentationSession、guarding group、threat relation | `RS-DEFENSE-01`; `@C06_Defense` | 读取 Guarding → 判断 Threat → 命中则应用 Defense Profile → 返回 Defense Response；不评价普通 Feeding | `DefenseResponse` | Defense-only；无 precedence/fallback |
| C06 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Bluegill.Guarding` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C07 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Smallmouth.Parental` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C07 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C07 · Response | PresentationSession、guarding group、threat relation | `RS-DEFENSE-01`; `@C07_Defense` | 读取 Guarding → 判断 Threat → 命中则应用 Defense Profile → 返回 Defense Response；不评价普通 Feeding | `DefenseResponse` | Defense-only；无 precedence/fallback |
| C07 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Smallmouth.Parental` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C08 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Tilapia.Feeding` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C08 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C08 · Response | PresentationSession、FoodField、resource facts | `RS-FEED-02`; `@C08_Grazing`, `@C08_Suspended` | 同一 Feeding Evaluator 同时评价 Grazing Channel 与 Suspended Channel → 固定聚合 → 返回响应 | `FeedingResponse` | 无互斥 Selector；PT3 candidate only |
| C08 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Tilapia.Feeding` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C09 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Paddlefish.FieldFeeding` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C09 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C09 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C09_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C09 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Paddlefish.FieldFeeding` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C10 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`BigmouthBuffalo.FieldFeeding` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C10 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C10 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C10_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C10 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `BigmouthBuffalo.FieldFeeding` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C11 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Mullet.FieldFeeding` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C11 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C11 · Response | PresentationSession、RootOccurrence、OpportunityId/Scope、match/presentation facts | `RS-FEED-01`; `C11_Response` | 解析 Opportunity → 评价 Match/Presentation → 应用 Response Profile → 返回 ResponseBand | `ResponseBand` | 默认 Feeding 路径；复用模板 |
| C11 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Mullet.FieldFeeding` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C12 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`AtlanticSalmon.Normal/Migration` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C12 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C12 · Response | 上游 FishGroup、PresentationSession、Opportunity | `RS-FEED-01` + `RS-REACTION-01` | Normal 组执行普通 Feeding；Migration 组关闭/强抑制 Feeding 并可执行 Non-feeding Reaction | `ResponseResult` | 上游分流；不购买 Stage Selector；动机未宣称闭合 |
| C12 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `AtlanticSalmon.Normal/Migration` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C13 · Group | lifecycle、season、species facts | `GR-GENERIC-01`; group=`Sockeye.Juvenile/Ocean/Spawning` | 读取事实 → 解析 GroupShare → FishGroup Allocation → 返回分群结果 | `FishGroupAllocationResult` | 由上游分流；本面不决定 Response |
| C13 · Bake | 无该 Case 的独立派生环境场 | 无 | 不执行 Bake；不把 Response 输入反写为空间场 | 无 | 明确不适用；不新增 Bake Template |
| C13 · Response | 上游 lifecycle group、PresentationSession、Opportunity | `RS-FEED-01`; group-specific Profile | 读取生命周期组 → 使用该组 Feeding Profile → 返回响应 | `ResponseResult` | juvenile/ocean/spawning 为范围分流，不新增 Template |
| C13 · Quality | quality_context、group allocation、base distribution | `Q-DEFER-01`; 继承 `Sockeye.Juvenile/Ocean/Spawning` 的 Group-specific Base Distribution | 读取既有 Base Distribution → 若有已确认 Modifier 则按 `Q-PARALLEL-01` 固定合并 → Normalize → 交抽样 Owner | `QualityDistribution` | 本 Case 未冻结独立 Quality 参数；保留 TODO/继承边界 |
| C14 · Group | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C14 · Bake | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C14 · Response | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C14 · Quality | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C15 · Group | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C15 · Bake | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C15 · Response | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |
| C15 · Quality | Frozen boundary scope | 无生产绑定 | 仅记录边界，不进入生产执行链 | 无 | 明确不适用；Frozen scope: boundary-only |

### R1.1.1 配置表最小绑定规则

每一行记录至少对应以下字段：`case_surface`、`template_id`、`input_refs`、`profile_refs`、`fixed_order`、`typed_result`、`boundary_status`。因此“复用模板”不是只写一个名称，而是有可追溯的绑定和边界。

### R1.1.2 Quality TODO 的精确位置

`Q-DEFER-01` 的 TODO 适用于 C01–C13 各自的 Quality 单元：当前只确认继承 Group Base Distribution，未冻结独立 Modifier、权重或抽取差异。C14/C15 不适用，不计入 Quality TODO。
