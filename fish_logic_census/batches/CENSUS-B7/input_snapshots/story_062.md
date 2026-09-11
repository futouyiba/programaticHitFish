Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d236816e85fbca3e1ef4d667 as of 2026-09-10T14:25:25.074Z:
<page url="https://app.notion.com/p/3d6a4137d236816e85fbca3e1ef4d667">
<ancestor-path>
<parent-data-source url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07" name="FCF Mechanism Story｜Working R2"/>
<ancestor-2-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" title="FCF Mechanism Story｜Working R2"/>
<ancestor-3-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-4-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-5-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"BatchID":"FISH-R03","Confidence":"Medium","ContractVersion":"AUDIT-R2","CoverageDelta":"Candidate","EvidenceState":"Evidence Open","EvidenceSummary":"FAO/FishBase 支持河流杂食、洪泛迁移和养殖/野生边界；野生垂钓响应与因果拆分仍开放。","FCFVerdict":"Deferred","FishModePressure":"Weak","GroupPressure":"Possible","PatternFit":"Existing Pattern","PrimaryEvaluand":["Discrete Target","Resource Patch"],"RepresentationHandoff":"Not Ready","ResearchDepth":"L3","ResponseChannels":["TargetFeeding"],"ReviewStatus":"Independent PASS","Semantic Pattern":["https://app.notion.com/p/3d6a4137d236812ebe4debf960c18987","https://app.notion.com/p/3d6a4137d2368111a1bbf2139e8b61a1"],"SourceWorkingURL":"https://www.fishbase.se/summary/Pangasianodon-hypophthalmus.html","SpatialPattern":["Static Habitat","Slow Reorder"],"Species":["https://app.notion.com/p/3d6a4137d236813dafe4d08ddfd12a80"],"Story":"FISH-R03｜蓝鲨｜Iridescent Shark｜Discrete Target + Resource Patch","StoryDomain":["Ordinary Feeding","Spatial/Habitat","Resource/Patch"],"TriggerPressure":"Posture Grain OK","url":"https://app.notion.com/p/3d6a4137d236816e85fbca3e1ef4d667"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Reality Baseline
蓝鲨（Iridescent shark；*Pangasianodon hypophthalmus*）是湄公河流域大型河流鲶形鱼。FAO 资料和 FishBase 入口支持其河流栖息、杂食性以及与洪水季节相关的迁移/繁殖空间变化；食物可包含浮游生物、昆虫、甲壳类、植物材料和小型动物。养殖场中的饲料和高密度行为不能直接代表野生机制。[FAO aquaculture profile](https://www.fao.org/fishery/docs/CDrom/aquaculture/I1129m/file/en/en_pangasius.htm) · [FishBase species entry](https://www.fishbase.se/summary/Pangasianodon-hypophthalmus.html)
本 Story 只保留“河流资源 Patch + 体型/阶段变化 + 季节迁移 Context”的最低能力解释；不购买养殖专属 Mode，也不把大型个体的饵料偏好写成统一野生事实。
## Story / State Scope
覆盖野生河流环境、普通摄食、体型相关食物变化和河流/水位 Context；迁移/洪泛生命周期仅作为相邻 Evidence surface，不属于当前 feeding chain；养殖品系、投喂史、繁殖工程和非摄食捕获不在本 Story。
## Strategy Story
现实约束提示玩家侧先按水位、河段和资源集中找机会，再根据个体大小选择可达呈现。深度、饵型、速度和停顿是机制推断，不能替代直接野外垂钓证据；养殖环境的高密度反应不得外推为野生群体规则。
## Granularity / Owner Boundary
Core owner is wild river feeding through P01/P02 under typed river and resource context. Aquaculture density/feed history, stage-linked diet changes, and flood-season migration are adjacent evidence surfaces; they remain identity, context, or lifecycle inputs and do not create additional response owners in this Story. No aquaculture or migration effect is settled twice in the feeding chain.
## Evidence
- [FAO: Pangasius biology/aquaculture](https://www.fao.org/fishery/docs/CDrom/aquaculture/I1129m/file/en/en_pangasius.htm)：河流环境、杂食性和生产环境边界。
- [FishBase: Pangasianodon hypophthalmus](https://www.fishbase.se/summary/Pangasianodon-hypophthalmus.html)：身份与生态入口。
- 证据限制：野生与养殖资料混合时，策略和密度响应必须保持 Evidence Open。
## FCF Interpretation
PrimaryEvaluand=Resource Patch + Discrete Target；ResponseChannels=TargetFeeding；SpatialPattern=Static Habitat + Slow Reorder。资源先改变机会，再进入离散摄食；迁移保持为相邻 lifecycle evidence，不在本响应链重复结算。
## Lowest-Power Explanation
P01 Discrete Target → TargetFeeding + Typed Context + P02 Resource Patch → Discrete Target → TargetFeeding 已能表达当前事实，不新增 Farm Mode 或 Size Mode。
## Competing Explanation
观察到的个体聚集或摄食变化可能由水位、饲料、养殖密度或猎物集中解释，而不是单一物种状态。
## Semantic Pattern Fit
P01 Discrete Target → TargetFeeding + Typed Context + P02 Resource Patch → Discrete Target → TargetFeeding（Existing Pattern）。本批不修改 Pattern Registry。
## Verdict / Confidence / ResearchDepth
ReviewStatus=Independent PASS（终审 FISH-R03-RECON-001 确认；本节 Verdict 为历史快照，FISH-R08-FIX-001 注）。
FCFVerdict=Deferred（Story-level working classification，不是 Species 全局 Verdict）；Confidence=Medium；ResearchDepth=L3；EvidenceState=Evidence Open；FishModePressure=Weak；TriggerPressure=Posture Grain OK；RepresentationHandoff=Not Ready；ReviewStatus=REVISE。
## Open Questions
- 野生种群的体型分段食性是否能与养殖资料严格分开？
- 洪泛迁移是否稳定跨越不同湄公河河段？
- 真实垂钓响应能否由野外来源独立闭合？
## Sweep Surface Log
1. Ordinary feeding — MATERIAL STORY FOUND：杂食资源利用，食物谱随阶段/环境变化。
2. Special feeding — SEARCHED-NO MATERIAL STORY：未找到独立特殊摄食仪式。
3. Resource/patch/food field — MATERIAL STORY FOUND：河流与洪泛资源 Patch。
4. Seasonal/depth/habitat — MATERIAL STORY FOUND：水位、河段和洪泛条件。
5. Lifecycle/migration — MATERIAL STORY FOUND：迁移/繁殖背景有资料支持。
6. Reproduction/guard/territory/conflict — EVIDENCE OPEN：繁殖细节未闭合为本 Story。
7. Sensory/presentation — EVIDENCE OPEN：野生呈现响应不足。
8. Persistent field/patch/substrate — MATERIAL STORY FOUND：河道、洪泛边缘为持久搜索线索。
9. State-stage behavior — MATERIAL STORY FOUND：体型/阶段与食物谱相关；参数仍开放。
10. Actual angler response — EVIDENCE OPEN：现实钓法与养殖反应不能混用。
11. Non-feeding capture/ownership boundary — OUT OF PRODUCT SCOPE：未进入本 Story。
</content>
</page>
