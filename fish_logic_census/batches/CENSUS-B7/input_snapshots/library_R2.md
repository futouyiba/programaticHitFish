Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b as of 2026-09-10T17:00:56.987Z:
<page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b">
<ancestor-path>
<parent-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-2-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"title":"鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
<callout icon="🧭" color="blue_bg">
	**R2 CURRENT CONTRACT.** R2 已将架构分析原子从“Species Row”改为 **Mechanism Story**。下方旧 Pilot/R1 段落保留为历史记录；凡与本节冲突，以本节 + Canonical Runbook R2 为准。
</callout>
## R2.1 三层数据模型
- <mention-database url="https://app.notion.com/p/c0b41cf615194168808a36e0476a45ad">FCF 逐鱼机制分类｜Working</mention-database>：一条鱼的 coverage/index；旧 species-level FCFVerdict 仅历史摘要。
- <mention-database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da">FCF Mechanism Story｜Working R2</mention-database>：一条记录 = 一个真实 Mechanism / Strategy Story；这是 R2 架构分析原子。
- <mention-database url="https://app.notion.com/p/56606f9a062d4864b4b0018e3b32ef64">FCF Semantic Pattern Registry｜Working R2</mention-database>：跨鱼 Semantic Pattern 聚类；**不是** Production Logic Template。
## R2.2 Mandatory Story Sweep
全部 267 鱼都必须进行广度 Sweep，主动检查 ordinary/special feeding、resource/patch/field、season/habitat、lifecycle/migration、reproduction/guard/conflict、sensory/presentation、persistent resource behavior、状态差异、现实钓手策略改变和 capture boundary。
每个 sweep surface 标：`MATERIAL STORY FOUND / SEARCHED-NO MATERIAL STORY / EVIDENCE OPEN / OUT OF PRODUCT SCOPE`。
**禁止**用浅层 L1 先判“没有架构压力”。Story 发现后再决定 L2/L3 深度。
## R2.3 Story Evidence State
Deferred 不再混成一个桶：
```plain text
Identity Deferred
Evidence Open
Product Scope Deferred
Input Contract Open
```
## R2.4 Ownership
- **Fish Reality & Strategy Research Worker**：公共鱼种 Review Overlay、Species Coverage、Mechanism Story、Research Batch Package；主任务是现实资料、Strategy Story、习性/状态差异与 Mechanism Story 发现，不负责 Representation；
- **Independent Evidence Reviewer**：Read-only，只写 Reviewer Report；审核 Reality correctness、Story completeness、False Positive/False Negative；
- **Semantic Triage Gate**：维护 Working Semantic Pattern 的 Candidate/Merge/Compression/RepresentationImpact，并出 Triage Packet；不得设置 `Design Authority Accepted` 或改 0.3.4；
- **主设计 Chat**：只处理 `SEMANTIC_ESCALATION` 与正式 Design Authority；
- **Representation Harness / B Lane**：只判断 control-flow / PT / production representation，不重新研究 Reality。
## R2.5 Fish Reality & Strategy Research Campaign
常规批次约 25–30 Species：
```plain text
Fish Research Worker
→ Self-QA / Cold Review
→ Independent Evidence Reviewer
→ Semantic Triage Gate
→ AUTO_CONTINUE / COVERAGE_DELTA / SEMANTIC_ESCALATION / REVISE
```
**BatchID 命名：** 后续研究批次只使用 `FISH-R01 / FISH-R02 / FISH-R03 ...`。R2 部署早期已经写入数据库/Package 的 `B01` 仅视为 `FISH-R01` 的 legacy alias；不要复制或重跑同一批。`B0–B4` 字样永久保留给 Representation Lane。
每 2–3 批运行 Cross-Batch Reviewer。只有 `SEMANTIC_ESCALATION` 固定回主设计 Chat；普通批次可在 GPT Work 内闭环。
## R2.6 Handoff / Continuous Campaign
- `UPSTREAM_CHANGE_EVENT`：现实纠错 / canonical semantic change / repeated new pattern 等，立即进入影响判断；
- `COVERAGE_DELTA_PACK`：语义不必改变、但可能出现新的 Representation coverage；周期性发给 Representation，由其决定是否回归。
- Semantic Triage 输出 `AUTO_CONTINUE_RESEARCH` 或 `EMIT_COVERAGE_DELTA` 时，应把 Hub 推到下一个 `FISH-Rxx / FR0 RESEARCH_READY`；原 Fish Research Work 下一次只需重新读取 Hub，即可继续下一批，不需要重新提供完整 Prompt。
- Triage=`REVISE_RESEARCH_BATCH` 时只回当前 Research Worker 修本批；Triage=`SEMANTIC_ESCALATION` 时暂停受影响语义闭合并提交主设计 Chat。
Fish Research / Triage 判断 **semantic novelty**；Representation 判断 **representation novelty**。
## R2.7 R2 Prompts / Review Context
- <mention-page url="https://app.notion.com/p/3d6a4137d23681b08dd8d7f04f951ab4">FCF Semantic Review Context R0｜Triage Judgment Pack</mention-page>：FR3 / Cross-Batch 的强制判题上下文；Fish Research Worker 在 Reality Sweep 前不以它作为研究起点。
- <mention-page url="https://app.notion.com/p/3d6a4137d2368188bca7d9a5b3d32e0d">GPT Work Prompt R2｜Fish Reality & Strategy Research Campaign｜Mechanism Story Sweep</mention-page>
- <mention-page url="https://app.notion.com/p/3d6a4137d23681c299c9f20605d5886e">Persistent Independent Reviewer Prompt R2｜Fish Research Evidence + Story Discovery</mention-page>
- <mention-page url="https://app.notion.com/p/3d6a4137d2368158b252c710e8c6937e">Persistent Semantic Triage Gate Prompt R2｜Fish Research Routine Auto-Gate</mention-page>
- <mention-page url="https://app.notion.com/p/3d6a4137d236813bb0ece56700a22a76">Cross-Batch Reviewer Prompt R2｜Fish Research Drift / Saturation</mention-page>
## 0. Status
WORKING / CROSS-BRANCH REFERENCE MAINTENANCE
本页负责两件事：
1. 对公共鱼种参考库做 267 条全量资料审计、补缺与纠错；
2. 在不覆盖公共事实层的前提下，为 FCF 机制设计建立逐鱼 Mechanism Classification。
## 1. 基本原则
- 公共资料事实、策划候选标签、项目设计值、FCF 机制推导分层保存，不互相冒充。
- 空白表示缺资料，不按 0 解释。
- `AI审核状态` 保留源表语义；本轮使用独立的 `资料复核状态 / 资料复核备注` 记录本次审计。
- 已确认错误可直接纠正；无法可靠闭合的标记 `需补资料 / 需人工确认`，不猜。
- 每次修改数据库属性时，同步更新鱼种资料页正文。
## 2. 每条鱼的资料审计模板
1. 身份：中文名 / 英文名 / 学名 / 科属是否一致；
2. 栖息：水体、栖息带、深度、温度范围是否缺失或冲突；
3. 摄食：摄食类型、主要对象、候选食性是否一致；
4. 生命周期：迁徙、繁殖期或阶段性空间变化是否有关键缺失；
5. 行为：时段、天气、性格等候选标签是否需要降级、修正或补来源；
6. 体型：最大记录、常见体长、体长口径是否可比；
7. 数据 provenance：哪些是 Source Fact / Verified Fact / Derived Candidate / Design Value；
8. 资料复核结论：无问题 / 已修正 / 需补资料 / 需人工确认。
## 3. FCF Mechanism Classification 模板
资料审计完成或达到足够置信度后，再做机制分类：
- `PrimaryEvaluand`：Discrete Target / Food Field / Resource Patch / Relation Object / Other；
- `ResponseChannels`：TargetFeeding / FieldFeeding / RelationalConflict / Other；
- `SpatialPattern`：Static Habitat / Slow Reorder / Lifecycle Migration / Runtime Overlay；
- `LifecycleOrGroupPressure`：是否需要 FishGroup / Regime；
- `PreExistingBundlePressure`：是否存在值得独立 FishMode 的行为程序包；
- `RuntimeContextPressure`：Flow / Substrate / FoodPatch / Territory / Anchor / Other；
- `TriggerPressure`：Posture Grain 足够 / 需要 Field Opportunity / Open；
- `FCFVerdict`：Default / Group-only / Mode Candidate / Grammar Breaker / Deferred。
## 4. 审计顺序
先按风险与机制信息量分批，而不是按鱼名随机顺序：
1. 滤食 / plankton / variable feeding / 摄食类型缺失；
2. grazing / herbivory / benthic foraging；
3. predator / ambush / pursuit；
4. 迁徙 / 洄游 / spawning habitat change；
5. 海水与特殊底栖 / 软体 / 鳐鲨等边界案例；
6. 其余普通鱼种补齐。
## 5. 第一批目标｜Feeding Mechanism High-Risk
优先处理：
- `摄食类型` 与 `食性（源表候选）` 明显冲突；
- `摄食类型 = variable`；
- 滤食型 / plankton feeding；
- 摄食类型为空，但机制上可能重要；
- 当前案例库已经依赖的 Silver Carp / Bighead Carp / Herring / Grass Carp / Common Carp 等。
## 6. Promotion 边界
本页的 FCF 分类只是 Evidence / Working Classification。只有跨鱼种聚类、Case Regression 和 Config Schema Review 通过后，才 Promote 到 0.3.4 主规格。
### 6.1 Single Writer｜写权限边界
- **公共鱼种资料库 + Review Overlay：** Fish Audit Work 是唯一写入者；其它 Chat / Reviewer 只读并提交 Review Finding。
- **FCF 逐鱼机制分类｜Working：** Fish Audit Work 是唯一写入者；完整 Evidence Chain 写在对应鱼种 Working 页面正文，数据库字段只存筛选结论与摘要。
- **Case Library：** 当前机制讨论对话维护；Fish Audit Work 不直接改。
- **Config Schema Proposal：** 配置表对话维护；Fish Audit Work 不直接改。
- **0.3.4 Main Spec：** 只在独立 Promotion Review 后由机制 Owner / Promotion Session 写入；Fish Audit Work、Reviewer、Schema 对话均不得直接 Promote。
- 任一非 Owner 发现错误，只提交 `REVIEW FINDING / SEMANTIC ISSUE / SCHEMA ISSUE`，不得跨 Owner 直接修正文。
### 6.2 Rebase-before-write
每次写入公共鱼种页或 FCF Working 条目前，必须先读取该页/条目最新版本。若发现上次读取后内容已经被其它写入者改变：
1. 先比较差异；
2. 保留对方已存在内容；
3. 只写本次最小必要修改；
4. 无法无冲突合并时标记 `WRITE CONFLICT` 并暂停该条。
### 6.3 Low-Bias Read Protocol｜先现实核验，再看候选标签
FCF Audit 默认读取公共库视图：`view://3d6a4137-d236-81be-b014-000cc111ddeb`（`FCF Audit｜Low-Bias Read`）。第一阶段只使用身份、基础生态、原始摄食类型、Review Overlay 与 provenance。
第一阶段**默认不参与判断**：价值等级/价格、俄4映射、重量段/重量参数、资源状态，以及 `性格 / 天气偏好 / 时段偏好 / 候选水温带 / 食性（源表候选）` 等策划推导标签。
先独立形成 `Reality Baseline`，再进入第二阶段读取候选标签做对拍：
```plain text
Reality Baseline
vs
Existing Candidate Labels
```
候选标签只能用于发现冲突/补资料，不能反向证明自身正确。
### 6.4 Library Read Path
- **全库 Manifest：** 仍使用 `view://330f683d-940b-41a6-8131-761a96853e68`，`mode: view` 分页直到 `has_more=false`；CSV 仅作为 2026-09-08 baseline snapshot。
- **Pilot / Batch 选鱼：** 优先使用 `FCF Audit｜Low-Bias Read` 窄视图，避免无关字段造成 anchoring。
- **单条正式审计和写入前：** 必须重新 fetch 该鱼 live page。Work 开始改库后，不得把旧 CSV 当 Current。
### 6.5 Review Gate
每条鱼写完后先做 Mechanical QA；每个 Batch 完成后做 Worker Cold Review。字段使用：
- `ResearchDepth = L1 / L2 / L3`
- `Confidence = High / Medium / Low`
- `ReviewStatus = Unreviewed / Self-QA Passed / Independent PASS / REVISE`
- `BatchID`
- `ContractVersion`
Pilot 固定为约 25 条，并在继续扩库前运行一次真正独立 Reviewer。Pilot 通过后：每 2–3 个 Batch 再做一次独立 Reviewer；遇到 `ARCHITECTURE OPEN / MODE OPEN / TRIGGER OPEN / DATA MODEL OPEN / IDENTITY CONFLICT / REPEATED NEW PATTERN` 立即升级，不等待批次结束。
`Independent PASS` 只代表该逐鱼 Working 结论通过独立复核，**不等于**已 Promote 到 0.3.4。
<database url="https://app.notion.com/p/c0b41cf615194168808a36e0476a45ad" inline="false" data-source-url="collection://aa896faf-d194-4e66-9fe6-9628822deaa8">FCF 逐鱼机制分类｜Working</database>
## 7. Batch A｜Feeding Mechanism High-Risk｜第一轮结果
首轮已完成 7 条高信息量记录的专项处理，并建立 Public Facts 与 FCF Working Classification 的隔离层：
- 鲢鱼 / Silver Carp：保留源快照，复核为 `Filter`；FCF = FieldFeeding / Grammar Breaker。
- 大西洋鲱鱼 / Atlantic Herring：修正英文名；复核为 `Target/Particulate + Filter + Mixed/Switching`；FCF 不分两个 FishMode。
- 大西洋鲭 / Atlantic Mackerel：复核为肉食性，且支持 particulate / filter 双机制；作为 Herring 的独立重复证据。
- 日本竹荚鱼 / Japanese Jack Mackerel：复核为肉食性 + `Target/Particulate`；作为 `planktivory ≠ filter feeding` 的负例。
- 欧白鲑 / Vendace：确认食谱具有显著季节变化且包含 benthic prey；Filter-only 解释被否定，但其它生态字段仍需补资料。
- 毛鳞鱼 / Capelin：确认 zooplankton diet；具体摄食机制未闭合，不从猎物类型推导 Filter。
- 湖白鲑 / Lake Whitefish：发现身份冲突，Lake Whitefish 与 `Coregonus artedi` 不一致；整条记录隔离为 `需人工确认`，FCF 暂停分类。
### 7.1 第一轮结构性发现
1. `食性类别` 与 `摄食机制` 必须分轴；“肉/植/杂食”回答吃什么，“Filter/Particulate/Grazing”回答怎么吃。
2. `planktivory` 不能自动映射为 `FilterFeeding`。
3. 同一 Species 能在 Target/Particulate 与 Filter 之间按当前 prey context 切换，因此 Grammar/Channel 与 FishMode 必须分层。
4. 身份冲突优先于参数纠错：名称、英文名、学名不闭合时，整条生态数据进入 quarantine，不逐字段猜修。
5. 公共库保留源快照；专项核验写入 Review Overlay；FCF 推导进入独立 Working 数据库。
### 7.2 下一批
继续处理 Feeding High-Risk 中剩余 `variable / plankton / 滤食候选 / 摄食类型缺失` 记录；完成这一组后再进入 grazing / herbivory / benthic foraging。
## 8. Batch B｜Carp Feeding Triad｜鳙鱼 / 草鱼 / 鲤鱼
- 鳙鱼 / Bighead Carp：源字段方向基本可用；专项复核确认 `Filter`，食性类别为杂食性。FCF = Food Field / FieldFeeding，不购买 FishMode。
- 草鱼 / Grass Carp：专项复核支持植食 + `Grazing`。FCF 上自然摄食以 Resource Patch 为背景，但垂钓中的钩饵仍可由 TargetFeeding + Patch Context 表达，暂不购买 Grazing Mode。
- 鲤鱼 / Common Carp：发现第二个明确摄食错误。源快照 `hunting macrofauna (predator) / 肉食性` 与专项资料冲突；复核为杂食性、`Benthic Foraging + Target/Particulate`。FCF 支持 Resource Patch + Discrete Target 双层结构，不要求 PatchForagingMode。
### 8.1 对当前架构的新增证据
这三条形成一个连续谱：
```plain text
Bighead Carp
Food Field → Filter

Grass Carp
Resource Patch → Grazing → 垂钓时仍可落到 Hook Target

Common Carp
Benthic / Food Patch → 搜寻多个 item → Hook Target
```
因此 `Food Field / Resource Patch / Discrete Target` 应被视为不同 Evaluand / Context 尺度；但尺度不同本身仍不等于 FishMode。
<page url="https://app.notion.com/p/3d6a4137d2368144bf31d42f6ab86467">GPT Work 执行 Prompt R1｜全库鱼种审计 + FCF 机制分类</page>
<page url="https://app.notion.com/p/3d6a4137d23681f9948bfda1c637e74a">Independent Reviewer Prompt R1｜FCF Fish Audit Pilot</page>
<page url="https://app.notion.com/p/3d6a4137d23681bfb5bee50856ef6c78">PILOT REVIEW PACKAGE｜Pilot-A｜AUDIT-R1</page>
<page url="https://app.notion.com/p/3d6a4137d23681748e38f94df8649d42">Pilot-A Independent Review Round 1 / REVISE</page>
<page url="https://app.notion.com/p/3d6a4137d23681e0b393c6c9d33b414e">Pilot-A Independent Review Round 2 / PASS</page>
<page url="https://app.notion.com/p/3d6a4137d23681d3862bea5320526a35">GPT Work 执行 Prompt R0｜Targeted Audit｜8 Uncertain Representation Breakers</page>
<page url="https://app.notion.com/p/3d6a4137d23681ac83f6fed813c33dd2">定向审计附录｜表达验证关键未决案例 R0（Targeted Audit Addendum｜Representation Breakers R0）</page>
<page url="https://app.notion.com/p/3d6a4137d23681d98ba2ee8f3599dc0f">定向鱼种事实独立审核报告 R1｜C06–C13｜ARTIFACT_APPROVE</page>
<database url="https://app.notion.com/p/282f4afd6fcd4a089b857eca02dc18da" inline="false" data-source-url="collection://1c5f9fd8-ea3b-4290-a11d-98e173b03a07">FCF Mechanism Story｜Working R2</database>
<database url="https://app.notion.com/p/56606f9a062d4864b4b0018e3b32ef64" inline="false" data-source-url="collection://a6862092-fdbb-4dc9-9b82-b1f32d0e980f">FCF Semantic Pattern Registry｜Working R2</database>
<page url="https://app.notion.com/p/3d6a4137d2368188bca7d9a5b3d32e0d">GPT Work Prompt R2｜Fish Reality & Strategy Research Campaign｜Mechanism Story Sweep</page>
<page url="https://app.notion.com/p/3d6a4137d23681c299c9f20605d5886e">Persistent Independent Reviewer Prompt R2｜Fish Research Evidence + Story Discovery</page>
<page url="https://app.notion.com/p/3d6a4137d2368158b252c710e8c6937e">Persistent Semantic Triage Gate Prompt R2｜Fish Research Routine Auto-Gate</page>
<page url="https://app.notion.com/p/3d6a4137d236813bb0ece56700a22a76">Cross-Batch Reviewer Prompt R2｜Fish Research Drift / Saturation</page>
<page url="https://app.notion.com/p/3d6a4137d23681b08dd8d7f04f951ab4">FCF Semantic Review Context R0｜Triage Judgment Pack</page>
<page url="https://app.notion.com/p/3d6a4137d23681df94d9daa0fa8c682c">FISH-R01｜Mechanism Story Sweep｜FR1 Research Package（legacy B01）</page>
<page url="https://app.notion.com/p/3d6a4137d236810bbd94fd718a24499b">Fish Research Campaign Orchestrator R1｜Persistent-Agent Routing</page>
<page url="https://app.notion.com/p/3d6a4137d2368180bc4bc16c889970b9">FR2 Sharded Evidence Review Protocol R0｜Exceptional Fallback Only</page>
<page url="https://app.notion.com/p/3d6a4137d236815eb5ececb18e4d1d2f">FR2 Evidence Review Integrator Prompt R0｜Fresh Batch Verdict</page>
<page url="https://app.notion.com/p/3d6a4137d2368154b185ed6f9facb2ed">FISH-R01｜Independent Evidence Review R2｜PASS</page>
<page url="https://app.notion.com/p/3d6a4137d2368137a8f3c7898e8e7ae5">FCF Campaign Agent Registry R0｜Persistent Role Handles</page>
<page url="https://app.notion.com/p/3d6a4137d23681c69bd8ee2b0059ffd7">Evidence Reviewer Context Ledger R0｜Persistent Review Memory</page>
<page url="https://app.notion.com/p/3d6a4137d23681859c6dee221f68e0bd">FISH-R01｜FR2-C Shard Evidence Review</page>
<page url="https://app.notion.com/p/3d6a4137d2368145bcd4d4b39ce2349c">FISH-R01｜FR2-A Shard Evidence Review</page>
<page url="https://app.notion.com/p/3d6a4137d2368159a92fca4158ac1ba8">FISH-R01｜FR2-B Shard Evidence Review</page>
<page url="https://app.notion.com/p/3d6a4137d23681ff9585efcdd757e9c9">FISH-R01｜FR2 Evidence Review Integrator｜Round 1</page>
<page url="https://app.notion.com/p/3d6a4137d23681be8bbce84feaeee5c8">FISH-R02｜Mechanism Story Sweep｜FR1 Research Package</page>
<page url="https://app.notion.com/p/3d6a4137d236813b81c4e0e50bb0775f">FISH-R03｜Research Package Draft｜Completion Claims Withdrawn</page>
<page url="https://app.notion.com/p/3d7a4137d236816fb7c0d2df9218c1b9">FISH-R04｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681189c1ac57ed611f477">FISH-R05｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681448eb2c480d28ea0fe">FISH-R05｜Independent Evidence Reviewer Report｜FR2-R2 Fresh 复核（窄域）｜PATCH_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d23681c2a72ee4c1978935ce">FISH-R06｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681a88fadd2f4764b5720">FISH-R06｜Independent Evidence Reviewer Report｜FR2-001｜ARTIFACT_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d23681f18518ff6400289324">FISH-R06｜Independent Evidence Reviewer Report｜FR2-R2 修后复核｜PATCH_REVISE（F-8 口径句）</page>
<page url="https://app.notion.com/p/3d7a4137d23681e8b9f2c532513b81a4">FISH-R07｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681229d4be1a516adeb03">FISH-R07｜Independent Evidence Reviewer Report｜FR2-001｜ARTIFACT_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d23681638e1eeb3c260ce56d">FISH-R07｜Independent Evidence Reviewer Report｜FR2-R2 修后复核｜PATCH_REVISE（1 字残留）</page>
<page url="https://app.notion.com/p/3d7a4137d2368172bfedc8017819589a">FISH-R08｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681bebdbefd10748185f0">FISH-R08｜Independent Evidence Reviewer Report｜FR2-001｜ARTIFACT_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d2368106a37bd4f80bb677c5">FISH-R08｜Independent Evidence Reviewer Report｜FR2-R2 修后复核｜PATCH_REVISE（F-3 连带统计）</page>
<page url="https://app.notion.com/p/3d7a4137d236817fbe3aef0803fdfc97">FISH-R09｜Research Package｜FR3 CLOSED</page>
<page url="https://app.notion.com/p/3d7a4137d23681208c40fedb586ba3c8">FISH-R09｜Independent Evidence Reviewer Report｜FR2-001｜ARTIFACT_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d23681d1b054eebab5adab05">FISH-R09｜Independent Evidence Reviewer Report｜FR2-R2 修后复核｜PATCH_REVISE（2 处数字残留）</page>
<page url="https://app.notion.com/p/3d7a4137d23681549d58f9e16284f092">FISH-R10｜Research Package｜FR3 CLOSED｜全库收官</page>
<page url="https://app.notion.com/p/3d7a4137d23681458ceaccaa187829c1">FISH-R10｜Independent Evidence Reviewer Report｜FR2-001｜全库收官+事故验证｜ARTIFACT_REVISE</page>
<page url="https://app.notion.com/p/3d7a4137d23681baac0cf2998e120d85">FISH-R10｜Independent Evidence Reviewer Report｜FR2-R2 收官章｜PATCH_REVISE（机械项残留）</page>
</content>
</page>
