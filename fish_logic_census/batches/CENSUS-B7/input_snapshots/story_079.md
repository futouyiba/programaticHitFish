<page url="https://app.notion.com/p/3d6a4137d23681dc8e6de202c7146199">
<ancestor-path>
<parent-data-source url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07" name="FCF Mechanism Story｜Working R2"/>
<ancestor-2-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" title="FCF Mechanism Story｜Working R2"/>
<ancestor-3-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-4-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-5-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"BatchID":"FISH-R03","Confidence":"Medium","ContractVersion":"AUDIT-R2","CoverageDelta":"None","EvidenceState":"Evidence Open","EvidenceSummary":"FishBase 食性与守巢字段支持底层 Resource/Target story；夜间/低光与跨水系差异仍开放。","FCFVerdict":"Default","FishModePressure":"Weak","GroupPressure":"None","PatternFit":"Existing Pattern","PrimaryEvaluand":["Discrete Target","Resource Patch"],"RepresentationHandoff":"Not Ready","ResearchDepth":"L2","ResponseChannels":["TargetFeeding"],"ReviewStatus":"Independent PASS","Semantic Pattern":["https://app.notion.com/p/3d6a4137d236812ebe4debf960c18987","https://app.notion.com/p/3d6a4137d2368111a1bbf2139e8b61a1"],"SourceWorkingURL":"https://www.fishbase.se/summary/Tachysurus-fulvidraco.html","SpatialPattern":["Static Habitat","Slow Reorder"],"Species":["https://app.notion.com/p/3d6a4137d2368103b01ef86ffb914ad5"],"Story":"FISH-R03｜黄颡鱼｜Yellow Catfish｜Discrete Target + Resource Patch","StoryDomain":["Ordinary Feeding","Spatial/Habitat","Resource/Patch"],"TriggerPressure":"Posture Grain OK","url":"https://app.notion.com/p/3d6a4137d23681dc8e6de202c7146199"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Reality Baseline
黄颡鱼（Yellow catfish；*Tachysurus fulvidraco*）的物种级资料支持底层、河湖通道和离散猎物故事：FishBase 将其记录为河流与湖泊底层鱼，摄食昆虫、软体动物，并偶尔摄食鱼类；公开食性汇总还列出鱼类、浮游动物和昆虫幼体等成分。FishBase 另记录雄鱼在黏土底质巢穴中守护卵和幼体，说明繁殖关系应与普通摄食分开处理。[FishBase species page](https://fishbase.se/Summary/tachysurus-fulvidraco) · [FishBase diet summary](https://fishbase.se/TrophicEco/DietCompoSummary.php?dietcode=7431&genusname=Tachysurus&speciesname=fulvidraco)
这些事实支持“底质/遮蔽 Context + Resource Patch + 离散目标”的最低能力解释。夜间活动或低光感知在本批没有足够直接来源闭合，因此不购买 Night Mode；证据状态保持 Evidence Open。
## Story / State Scope
本 Story 只覆盖普通摄食、底层资源与河湖通道；守巢繁殖作为相邻但独立的关系/生命周期候选记录，不把它并入普通 Target story。
## Strategy Story
机制侧可以把底层、巢穴/石缝附近和昆虫/软体动物资源理解为机会来源，再由离散目标进入 TargetFeeding。玩家侧的深度、底质、饵型、速度和停顿是由现实约束推出的设计推断；当前来源不支持“夜间一定更有效”或某一固定钓法的现实断言。
## Evidence
- [FishBase species page](https://fishbase.se/Summary/tachysurus-fulvidraco)：栖地、底层摄食、守巢行为。
- [FishBase diet composition](https://fishbase.se/TrophicEco/DietCompoSummary.php?dietcode=7431&genusname=Tachysurus&speciesname=fulvidraco)：公开食性成分汇总。
- [GBIF taxon record](https://www.gbif.org/species/6168091)：仅作分类身份核验，不作为行为证据。
## FCF Interpretation
PrimaryEvaluand=Resource Patch + Discrete Target；ResponseChannels=TargetFeeding；SpatialPattern=Static Habitat + Slow Reorder。守巢是独立 Relation/Guard 候选，不在本普通摄食 Story 的响应链内。
## Lowest-Power Explanation
既有 P02 Resource Patch → Discrete Target → TargetFeeding + P01 Discrete Target → TargetFeeding + Typed Context 可表达底层资源与离散摄食机会，不新增 Night Mode。
## Competing Explanation
底层捕获率的变化也可能来自水流、底质和猎物集中，而非低光本身；现有证据不足以分解各因素。
## Semantic Pattern Fit
P02 Resource Patch → Discrete Target → TargetFeeding + P01 Discrete Target → TargetFeeding + Typed Context（Existing Pattern）。本批不新增或修改 Semantic Pattern Registry。
## Verdict / Confidence / ResearchDepth
ReviewStatus=Independent PASS（终审 FISH-R03-RECON-001 确认；本节 Verdict 为历史快照，FISH-R08-FIX-001 注）。
FCFVerdict=Default（Story-level working classification，不是 Species 全局 Verdict）；Confidence=Medium；ResearchDepth=L2；EvidenceState=Evidence Open；FishModePressure=Weak；TriggerPressure=Posture Grain OK；RepresentationHandoff=Not Ready；ReviewStatus=REVISE。
## Open Questions
- 守巢是否应由独立 Relation/Guard Story 承载，并与普通摄食共享何种空间条件？
- 低光与夜间摄食是否有物种级直接研究，而不是数据库常识性推断？
- 不同河湖水系的食性比例是否足以改变 Resource Patch 权重？
## Sweep Surface Log
1. Ordinary feeding — MATERIAL STORY FOUND：昆虫、软体动物、偶尔鱼类。
2. Special feeding — SEARCHED-NO MATERIAL STORY：未找到独立特殊摄食模式。
3. Resource/patch/food field — MATERIAL STORY FOUND：底层猎物与底质资源 Patch。
4. Seasonal/depth/habitat — MATERIAL STORY FOUND：河湖通道、底层与遮蔽条件。
5. Lifecycle/migration — SEARCHED-NO MATERIAL STORY：本批未闭合迁移故事。
6. Reproduction/guard/territory/conflict — MATERIAL STORY FOUND：雄鱼守巢，但作为相邻 Relation/Guard 候选。
7. Sensory/presentation — EVIDENCE OPEN：低光和触觉通道未由直接来源闭合。
8. Persistent field/patch/substrate — MATERIAL STORY FOUND：底质和巢穴区域是持久空间线索。
9. State-stage behavior — EVIDENCE OPEN：年龄/季节食性阶段未充分闭合。
10. Actual angler response — EVIDENCE OPEN：深度、饵型、停顿仅作策略推断。
11. Non-feeding capture/ownership boundary — OUT OF PRODUCT SCOPE：未进入本 Story。
</content>
</page>
