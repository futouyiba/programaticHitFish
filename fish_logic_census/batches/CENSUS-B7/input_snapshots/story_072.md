Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d236817698b9df62d395e226 as of 2026-09-10T14:25:39.795Z:
<page url="https://app.notion.com/p/3d6a4137d236817698b9df62d395e226">
<ancestor-path>
<parent-data-source url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07" name="FCF Mechanism Story｜Working R2"/>
<ancestor-2-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" title="FCF Mechanism Story｜Working R2"/>
<ancestor-3-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-4-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-5-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"BatchID":"FISH-R03","Confidence":"Medium","ContractVersion":"AUDIT-R2","CoverageDelta":"Candidate","EvidenceState":"Evidence Open","EvidenceSummary":"PMC/PubMed 支持活蚌鳃腔产卵、胚胎发育和雄性竞争；物种/亚种边界与全年策略仍开放。","FCFVerdict":"Deferred","FishModePressure":"Weak","GroupPressure":"Possible","PatternFit":"Existing Pattern","PrimaryEvaluand":["Relation Object"],"RepresentationHandoff":"Not Ready","ResearchDepth":"L3","ResponseChannels":["RelationalConflict"],"ReviewStatus":"Independent PASS","Semantic Pattern":["https://app.notion.com/p/3d6a4137d23681dd8804d14893ed7701"],"SourceWorkingURL":"https://www.fishbase.se/summary/Rhodeus-ocellatus.html","SpatialPattern":["Static Habitat","Lifecycle Migration"],"Species":["https://app.notion.com/p/3d6a4137d236811a8026c51a549dcacb"],"Story":"FISH-R03｜高体鳑鲏｜Rosy Bitterling｜Relation Object","StoryDomain":["Spatial/Habitat","Reproduction/Guard","Conflict/Relation","Lifecycle/Migration"],"TriggerPressure":"Posture Grain OK","url":"https://app.notion.com/p/3d6a4137d236817698b9df62d395e226"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Reality Baseline
高体鳑鲏（Rosy bitterling；*Rhodeus ocellatus*）的关键现实事实是繁殖关系而非普通摄食：雌鱼把卵产入活淡水蚌的鳃腔，胚胎在蚌体内发育，雄鱼在繁殖期围绕产卵机会和配偶竞争表现出关系性行为。[PMC study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3399850/) · [PubMed study](https://pubmed.ncbi.nlm.nih.gov/24925267/)
这条证据支持 Relation Object / Condition 候选：淡水蚌是繁殖所需的外部关系对象，不能并入普通 Target Feeding。当前资料对具体野外种群、亚种边界、摄食与垂钓响应仍不完整，EvidenceState 保持 Evidence Open。
## Story / State Scope
本 Story 只覆盖繁殖关系、对象依赖与繁殖期空间机会；普通摄食、全年迁移、种群差异和非摄食捕获不在同一结论内。
## Strategy Story
对机制设计的含义是：只有在活淡水蚌这一关系对象存在且处于可用状态时，繁殖相关机会才成立；这不是一个“更容易攻击”的普通饵料故事。任何面向玩家的寻找位置或时段建议都只能作为关系对象的场景推断，不能声称现实垂钓者普遍利用该繁殖关系。
## Evidence
- [Bitterling–mussel reproductive interaction](https://pmc.ncbi.nlm.nih.gov/articles/PMC3399850/)：产卵进入活蚌鳃腔及胚胎发育。
- [Male reproductive competition](https://pubmed.ncbi.nlm.nih.gov/24925267/)：繁殖关系对象与雄性竞争线索。
- [Spawning period observation](https://www.jstage.jst.go.jp/article/jji1950/32/1/32_1_79/_article/-char/en)：繁殖期和迁移观察；不把单一地点观察外推为全物种常态。
- [Subspecies-specific source](https://esj-journals.onlinelibrary.wiley.com/doi/10.1007/s10144-004-0201-0)：明确存在亚种范围，避免把亚种资料无条件升级为全物种结论。
## FCF Interpretation
PrimaryEvaluand=Relation Object；ResponseChannels=RelationalConflict。Relation Object 的成立条件是活淡水蚌及繁殖期语境；普通摄食不属于本 Story。
## Lowest-Power Explanation
既有 P04 Persistent Guard Condition + Relation → RelationalConflict 已能表达“对象依赖的繁殖关系”和雄性竞争，不购买新 FishMode。
## Competing Explanation
部分观察也可能由繁殖期空间集中或一般配偶竞争解释；当前材料不足以判定是否需要独立的强状态或全局关系锁。
## Semantic Pattern Fit
P04 Persistent Guard Condition + Relation → RelationalConflict（Existing Pattern）。本批不新增或修改 Semantic Pattern Registry。
## Verdict / Confidence / ResearchDepth
ReviewStatus=Independent PASS（终审 FISH-R03-RECON-001 确认；本节 Verdict 为历史快照，FISH-R08-FIX-001 注）。
FCFVerdict=Deferred（Story-level working classification，不是 Species 全局 Verdict）；Confidence=Medium；ResearchDepth=L3；EvidenceState=Evidence Open；FishModePressure=Weak；GroupPressure=Possible；TriggerPressure=Posture Grain OK；RepresentationHandoff=Not Ready；ReviewStatus=REVISE。
## Open Questions
- 当前四篇文献的物种/亚种边界能否为本条目形成统一身份基线？
- 繁殖对象关系是否需要显式生命周期 owner，还是由 Relation Object 条件承载？
- 普通摄食与繁殖关系是否共享空间机会但不共享响应通道？
## Sweep Surface Log
1. Ordinary feeding — SEARCHED-NO MATERIAL STORY：本批没有以普通摄食为核心的可核验新故事。
2. Special feeding — SEARCHED-NO MATERIAL STORY：未发现特殊摄食行为可独立建模。
3. Resource/patch/food field — EVIDENCE OPEN：蚌分布与繁殖机会的空间关系未充分闭合。
4. Seasonal/depth/habitat — MATERIAL STORY FOUND：繁殖期和水域条件影响关系对象机会。
5. Lifecycle/migration — MATERIAL STORY FOUND：繁殖期迁移/产卵关系有文献支持。
6. Reproduction/guard/territory/conflict — MATERIAL STORY FOUND：蚌内产卵、雄性竞争与关系对象依赖。
7. Sensory/presentation — EVIDENCE OPEN：求偶信号与对象识别的可用机制细节不足。
8. Persistent field/patch/substrate — EVIDENCE OPEN：蚌床/底质是否构成持久 Patch 需直接资料。
9. State-stage behavior — MATERIAL STORY FOUND：繁殖期状态与非繁殖期应分开；阶段参数未闭合。
10. Actual angler response — OUT OF PRODUCT SCOPE：没有把繁殖关系写成现实钓法。
11. Non-feeding capture/ownership boundary — OUT OF PRODUCT SCOPE：未进入本 Story。
</content>
</page>
