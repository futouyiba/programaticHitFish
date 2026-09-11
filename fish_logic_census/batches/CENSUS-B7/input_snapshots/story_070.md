以下是“fetch”对 URL 为 https://app.notion.com/p/3d6a4137d23681deb421c7a1c9d53f83 的页面在 2026-09-10T14:26:41.323Z 的结果：

<page url="https://app.notion.com/p/3d6a4137d23681deb421c7a1c9d53f83">
<ancestor-path>
<parent-data-source url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07" name="FCF Mechanism Story｜Working R2"/>
<ancestor-2-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" title="FCF Mechanism Story｜Working R2"/>
<ancestor-3-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-4-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-5-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"BatchID":"FISH-R03","Confidence":"Medium","ContractVersion":"AUDIT-R2","CoverageDelta":"Candidate","EvidenceState":"Evidence Open","EvidenceSummary":"FAO/FishBase 支持空气呼吸、低氧/洪泛环境、体型相关食性和迁移；现实策略与因果拆分仍开放。","FCFVerdict":"Default","FishModePressure":"Weak","GroupPressure":"None","PatternFit":"Existing Pattern","PrimaryEvaluand":["Discrete Target","Resource Patch"],"RepresentationHandoff":"Not Ready","ResearchDepth":"L3","ResponseChannels":["TargetFeeding"],"ReviewStatus":"Independent PASS","Semantic Pattern":["https://app.notion.com/p/3d6a4137d236812ebe4debf960c18987","https://app.notion.com/p/3d6a4137d2368111a1bbf2139e8b61a1"],"SourceWorkingURL":"https://www.fishbase.se/summary/Clarias-gariepinus.html","SpatialPattern":["Static Habitat","Slow Reorder"],"Species":["https://app.notion.com/p/3d6a4137d2368128a794d77b5088c486"],"Story":"FISH-R03｜革胡子鲶｜African Sharptooth Catfish｜Discrete Target + Resource Patch","StoryDomain":["Ordinary Feeding","Spatial/Habitat","Resource/Patch"],"TriggerPressure":"Posture Grain OK","url":"https://app.notion.com/p/3d6a4137d23681deb421c7a1c9d53f83"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Reality Baseline
革胡子鲶（African sharptooth catfish；*Clarias gariepinus*）的现实基线可由 FAO 与 FishBase 的物种资料闭合到以下范围：栖息于河流、湖泊、沼泽和可能季节性干涸的洪泛区；具辅助空气呼吸能力，能够在低氧和水体收缩条件下维持生存。FAO 资料记录其食性随体型变化，从浮游动物和昆虫幼体到较大鱼类，属于机会性、广食性的捕食者；FishBase 还记录其在洪泛季节进行迁移和繁殖相关移动。[FAO biology](https://www.fao.org/4/w3595e/w3595e04.htm) · [FishBase](https://www.fishbase.se/summary/Clarias-gariepinus.html)
这些事实支持“资源 Patch + 离散目标 + 低氧/洪泛 Context”的最低能力解释。空气呼吸是现实边界，不自动创建独立 Night 或 Low-Oxygen Mode；低氧环境的可捕获机会与水体收缩仍需要更细物种级证据。
## Story / State Scope
本 Story 覆盖普通摄食、体型相关食物变化与低氧/季节水体条件；洪泛迁移/繁殖移动仅作为相邻 Evidence surface，不属于当前 feeding chain；不宣称所有地域种群、养殖系统、繁殖细节或非摄食捕获。
## Strategy Story
现实策略约束是：鱼可能在低氧、浅滩、洪泛边缘或泥底资源区保持可用状态，且食物谱随体型改变。对玩家的设计含义是先按水体状态和资源 Patch 找位置，再在离散目标和底层机会之间切换呈现。饵种、深度、速度与停顿属于基于上述现实约束的策略推断；本批没有把“夜钓”或“低氧专用呈现”写成已被直接垂钓研究证明的事实。
## Granularity / Owner Boundary
Core owner is ordinary feeding through P01/P02 under typed habitat and resource context. Low-oxygen tolerance, body-size diet shifts, and flood-season movement are adjacent evidence surfaces that modify context or lifecycle state; they do not create additional response owners in this Story and must not be double-settled. Migration/reproduction remains an open adjacent Story candidate, outside the current feeding chain.
## Evidence
- [FAO: Clarias gariepinus biology](https://www.fao.org/4/w3595e/w3595e04.htm)：栖地、空气呼吸、体型相关食性和洪泛环境。
- [FishBase species page](https://www.fishbase.se/summary/Clarias-gariepinus.html)：身份、迁移和生态入口。
- 证据限制：当前材料能支持现实边界与机会类型，不能闭合一个统一的现实“低氧攻击概率”或通用钓法参数。
## FCF Interpretation
PrimaryEvaluand=Resource Patch + Discrete Target；ResponseChannels=TargetFeeding；SpatialPattern=Static Habitat + Slow Reorder。资源场先提供机会，离散猎物再进入 TargetFeeding；洪泛迁移保持为相邻 lifecycle evidence，不在本响应链重复结算。
## Lowest-Power Explanation
既有 P02 Resource Patch → Discrete Target → TargetFeeding + P01 Discrete Target → TargetFeeding + Typed Context 足以表达低氧/洪泛背景下的资源重排和机会性捕食，无需新增 FishMode。
## Competing Explanation
观察到的“低氧仍可捕获”也可能来自猎物集中、浅水边缘或水位变化，而不是空气呼吸直接提高攻击倾向；目前不能把这些因果拆开。
## Semantic Pattern Fit
P02 Resource Patch → Discrete Target → TargetFeeding + P01 Discrete Target → TargetFeeding + Typed Context（Existing Pattern）。本批不新增或修改 Semantic Pattern Registry。
## Verdict / Confidence / ResearchDepth
ReviewStatus=Independent PASS（终审 FISH-R03-RECON-001 确认；本节 Verdict 为历史快照，FISH-R08-FIX-001 注）。
FCFVerdict=Default（Story-level working classification，不是 Species 全局 Verdict）；Confidence=Medium；ResearchDepth=L3；EvidenceState=Evidence Open；FishModePressure=Weak；TriggerPressure=Posture Grain OK；RepresentationHandoff=Not Ready；ReviewStatus=REVISE。
## Open Questions
- 体型分段的食物谱是否能转成可审计的资源权重，而不变成硬编码新模式？
- 洪泛迁移在不同地域种群中是否稳定？
- 现实垂钓中低氧、泥底和浅滩的响应是否有交叉来源？
## Sweep Surface Log
1. Ordinary feeding — MATERIAL STORY FOUND：广食性、机会性捕食，体型改变食物谱。
2. Special feeding — SEARCHED-NO MATERIAL STORY：未找到足以独立建模的特殊摄食仪式。
3. Resource/patch/food field — MATERIAL STORY FOUND：洪泛区、浅滩和季节性水体形成资源机会。
4. Seasonal/depth/habitat — MATERIAL STORY FOUND：低氧、泥底、洪泛和水体收缩。
5. Lifecycle/migration — MATERIAL STORY FOUND：洪泛季节迁移/繁殖移动。
6. Reproduction/guard/territory/conflict — EVIDENCE OPEN：繁殖行为细节未闭合为本 Story。
7. Sensory/presentation — EVIDENCE OPEN：空气呼吸与感知通道对呈现响应的直接证据不足。
8. Persistent field/patch/substrate — MATERIAL STORY FOUND：泥底、沼泽、洪泛边缘为持久空间线索。
9. State-stage behavior — MATERIAL STORY FOUND：食性随体型变化；阶段边界仍需精化。
10. Actual angler response — EVIDENCE OPEN：饵、深度、速度为机制推断，缺直接交叉验证。
11. Non-feeding capture/ownership boundary — OUT OF PRODUCT SCOPE：未进入本 Story。
</content>
</page>
