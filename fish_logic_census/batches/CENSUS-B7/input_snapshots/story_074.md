Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d23681338a9cc4c040b22091 as of 2026-09-10T14:25:20.198Z:
<page url="https://app.notion.com/p/3d6a4137d23681338a9cc4c040b22091">
<ancestor-path>
<parent-data-source url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07" name="FCF Mechanism Story｜Working R2"/>
<ancestor-2-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" title="FCF Mechanism Story｜Working R2"/>
<ancestor-3-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-4-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-5-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"BatchID":"FISH-R03","Confidence":"Medium","ContractVersion":"AUDIT-R2","CoverageDelta":"Candidate","EvidenceState":"Evidence Open","EvidenceSummary":"FishBase/FAO 支持藻类、附着生物和碎屑连续资源；野生/养殖边界与现实 FieldFeeding 呈现仍开放。","FCFVerdict":"Deferred","FishModePressure":"None","GroupPressure":"None","PatternFit":"Existing Pattern","PrimaryEvaluand":["Resource Patch"],"RepresentationHandoff":"Not Ready","ResearchDepth":"L3","ResponseChannels":["FieldFeeding"],"ReviewStatus":"Independent PASS","Semantic Pattern":["https://app.notion.com/p/3d6a4137d236810696fbdb25e854c094"],"SourceWorkingURL":"https://www.fishbase.se/summary/Cirrhinus-molitorella.html","SpatialPattern":["Static Habitat","Slow Reorder"],"Species":["https://app.notion.com/p/3d6a4137d23681b6af04ca22f4c55a87"],"Story":"FISH-R03｜鲮｜Mud Carp｜Resource Patch","StoryDomain":["Spatial/Habitat","Resource/Patch","Capture Boundary"],"TriggerPressure":"Field Opportunity Candidate","url":"https://app.notion.com/p/3d6a4137d23681338a9cc4c040b22091"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Reality Baseline
鲮（Mud carp；*Cirrhinus molitorella*）是华南淡水鲤科鱼类。FishBase 物种入口及 FAO 养殖资料支持其以藻类、附着生物和底质有机碎屑为主要资源，并在河流、池塘和缓流环境中利用连续食物场；养殖饲料条件不能直接代表野生行为。[FishBase species entry](https://www.fishbase.se/summary/Cirrhinus-molitorella.html) · [FAO aquaculture profile](https://www.fao.org/4/ab915e/ab915e00.htm)
这支持 Resource Patch + FieldFeeding 候选，但连续资源摄食不等于一个新 FishMode，也不自动证明某种固定钓法。
## Story / State Scope
覆盖底质/附着资源、连续摄食场和流速/水体条件；不宣称完整繁殖迁移、养殖到野生迁移或非摄食捕获。
## Strategy Story
机制侧先定位藻类、附着生物和有机碎屑集中的底质 Patch，再由 FieldFeeding 处理持续摄食机会。玩家侧的底质、深度、饵料和停顿是设计推断；不能把“连续资源场”压缩成单一离散目标或固定底钓参数。
## Evidence
- [FishBase: Cirrhinus molitorella](https://www.fishbase.se/summary/Cirrhinus-molitorella.html)：身份与生态入口。
- [FAO aquaculture profile](https://www.fao.org/4/ab915e/ab915e00.htm)：藻类/附着资源与养殖边界；不把养殖数据直接当野外概率。
## FCF Interpretation
PrimaryEvaluand=Resource Patch；ResponseChannels=FieldFeeding；SpatialPattern=Static Habitat + Slow Reorder。
## Lowest-Power Explanation
P03 Food Field → FieldFeeding / Field Opportunity 已能表达连续底质资源，无需新增 Grass/Filter Mode。
## Competing Explanation
资源场位置也可能由流速、底质和水质共同决定；摄食密度变化不能单独归因于藻类质量。
## Semantic Pattern Fit
P03 Food Field → FieldFeeding / Field Opportunity（Existing Pattern）。不修改 Pattern Registry。
## Verdict / Confidence / ResearchDepth
ReviewStatus=Independent PASS（终审 FISH-R03-RECON-001 确认；本节 Verdict 为历史快照，FISH-R08-FIX-001 注）。
FCFVerdict=Deferred（Story-level working classification，不是 Species 全局 Verdict）；Confidence=Medium；ResearchDepth=L3；EvidenceState=Evidence Open；FishModePressure=None；TriggerPressure=Field Opportunity Candidate；RepresentationHandoff=Not Ready；ReviewStatus=REVISE。
## Open Questions
- 野生与养殖食物谱的边界能否逐项核验？
- 附着资源 Patch 是否存在稳定季节重排？
- 现实垂钓的 FieldFeeding 呈现是否有独立证据？
## Sweep Surface Log
1. Ordinary feeding — MATERIAL STORY FOUND：藻类、附着生物和碎屑资源。
2. Special feeding — SEARCHED-NO MATERIAL STORY：未发现独立特殊摄食仪式。
3. Resource/patch/food field — MATERIAL STORY FOUND：连续底质资源场。
4. Seasonal/depth/habitat — MATERIAL STORY FOUND：流速、底质和水体条件。
5. Lifecycle/migration — EVIDENCE OPEN：迁移边界未闭合。
6. Reproduction/guard/territory/conflict — SEARCHED-NO MATERIAL STORY：未发现可核验关系故事。
7. Sensory/presentation — EVIDENCE OPEN：FieldFeeding 感知响应待资料。
8. Persistent field/patch/substrate — MATERIAL STORY FOUND：底质/附着层是持久线索。
9. State-stage behavior — EVIDENCE OPEN：阶段差异未闭合。
10. Actual angler response — EVIDENCE OPEN：呈现为设计推断。
11. Non-feeding capture/ownership boundary — MATERIAL STORY FOUND：连续摄食与离散钓获边界需下游 owner 处理。
</content>
</page>
