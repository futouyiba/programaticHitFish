# FCF Harness Handoff

这份文件是把当前 FCF 工作区交给另一套 harness 的启动入口。它记录的是可复核的
工作状态、来源关系、角色边界和恢复顺序，不把任何 Working 或 Candidate 误写成
已经 Promotion 的 Authority。

快照时间：2026-09-10（Asia/Shanghai；Notion 远端页面按各自 fetch 时间记录）

## 1. 一分钟接管

本地仓库：

`/Volumes/Mac DS - Data/SharedProjects/programaticHitFish`

接管顺序：

1. 读取本文件和 [`AGENTS.md`](AGENTS.md)。
2. 读取 [FCF Router](https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47)。
3. 按任务选择 branch：
   - 默认 FCF V1：Router → Project State Current → V1 active target。
   - Simplified / V0：Router → Branch Index → Simplified Production V0 Working Main → 最新 Working checkpoint。
   - First-Principles：只在任务明确要求时，从 Branch Index 的受控 pointer 进入。
4. 读取本次任务直接相关的本地 contract；机制语义任务先按
   [`docs/mechanism_spec_writing_and_review_guide_cn.md`](docs/mechanism_spec_writing_and_review_guide_cn.md)
   第 0 节路由。
5. 如果是生产设计文档、团队同步稿或 Deep Companion，再读取
   [Production Design Document Authoring Guide](https://app.notion.com/p/3cfa4137d23681d68f89cc0eed80f99b)。
6. 只有用户明确要求写回 Notion 时才写入 Notion；默认把本地文件作为本次交接的可离线
   输入。
7. 继续前先运行：

```text
python3 -m pytest -q
```

机器可读的完整快照在 [`handoff_manifest.json`](handoff_manifest.json)，可用
[`tools/build_handoff_manifest.py`](tools/build_handoff_manifest.py) 重建。

## 2. 权威层级与分支隔离

FCF 的三条顶层设计路线必须分开：

| 路线 | 语义 | 当前入口 |
|---|---|---|
| First-Principles / Original System Model Heritage | 更早的 Mainline 第一性原理与因果树，只作显式 reference/provenance | [Branch Index](https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd) |
| FCF V1 / Full Mechanism | `R1 → Working R2 → V1 Core / Delta / RC` 的连续 lineage；无 branch qualifier 时是 FCF default approved authority | [Project State Current](https://app.notion.com/p/3cca4137d2368114a982f3b09e965e49) |
| Simplified Production V0 | 独立的极简生产、DSL、authoring 和 prototype 路线；不是 V1 revision 或 ancestor | [Simplified V0 Working Main](https://app.notion.com/p/3cda4137d23681508740ceff789abd41) |

引用、相似术语或旧文档 parent 不会改变 ownership。跨路线只能通过明确的
reference、comparison、compatibility、migration 或 adoption decision 发生。

当前 authority 顺序：

```text
FCF Router
→ Project State Current
→ branch-local Current / active Review Target
→ reviewer-adjudicated Closure Patch / successor
→ supporting evidence / rationale / history
```

`Current`、`Working`、`Candidate`、`Historical` 的状态必须原样保留。任何
`ARTIFACT_APPROVE` 只覆盖其声明的 artifact scope；不能扩大为整个项目完成或
V1 Freeze。

## 3. 当前状态

### FCF V1 / RC4

- Current 页面把 V1 active review target 指向
  [V1 Core Candidate RC4｜Closure Revision](https://app.notion.com/p/3cca4137d236819aa3baddca8a2c251c)。
- RC4 已把有限 PSU、reservation、Candidate resolver order、A/T/E、opportunity
  replay identity、lifecycle slice identity、cause owner、settlement 和
  review transport 规则收成一个 self-contained target。
- 本地 V1 设计、reference engine、journal、editor、flagship traces 和测试已经
  形成可运行基线；[`docs/verification_report.md`](docs/verification_report.md)
  明确剩余门槛是把同一 fixture contract 跑到真实 production runtime/storage，
  再完成 Independent Narrow Close Review。
- 不能把“本地 reference 测试全绿”写成 production 已接入，也不能把 RC4
  Candidate 写成已经 Freeze。

### Simplified Production V0

- 当前入口是
  [Simplified Production V0｜Working Main](https://app.notion.com/p/3cda4137d23681508740ceff789abd41)。
- 当前主线是 pre-generation、dynamic condition、authoring/compiler、editor
  和 representation 的窄闭合；V0 仍是 `WORKING / NOT PROMOTED`。
- 当前下一 Gate 是
  [Human Usability Validation R0](https://app.notion.com/p/3cfa4137d236810e8e0cc09a96e2b4e5)：
  由 2–3 名未深度参与推导的真实策划执行固定任务。Coding Agent 不再自证
  usability。
- 不能把 V0 的数值、阈值、prototype PASS 或 authoring 示例自动升级为 V1
  Authority。

### Representation / Pilot-A

- 本地交付入口：
  [`outputs/fcf_authoring_concrete_r2/README.md`](outputs/fcf_authoring_concrete_r2/README.md)
  和 [`outputs/fcf_authoring_concrete_r2/current-state-snapshot.md`](outputs/fcf_authoring_concrete_r2/current-state-snapshot.md)。
- 当前快照：`A4 = PROCEED_TO_REPRESENTATION`；`B4 = DESIGN_REVISE`；
  60 个 Case × Surface 单元已通过 preflight；已完成的 artifact review 只覆盖
  声明的 R1/R1.1 bundle。
- 四个执行面：

```text
Group Routing
Bake
Response
Quality Selection
```

- 当前方向是 per-surface hybrid：
  - Group：Config / RuleSet 倾向强；
  - Bake：Config / Typed Fact / Profile 主路径增强，DSL escape lane 尚未关闭；
  - Response：少量固定拓扑 + Profile / Channel；
  - Quality：并列 Modifier + 单次 Normalize。
- 下一刀优先读取并攻击最新
  `Summer Oxythermal Stress Representation Knife R0`；不要从旧 BA-T4
  直接冻结 Bass 专用 `MIN/MAX/PRODUCT` 嵌套，也不要回退重铺全部 15 Case。

## 4. Notion 关键链接

这些是另一套 harness 的最小远端入口。完整去重 URL 列表和本地来源在
[`handoff_manifest.json`](handoff_manifest.json) 的 `notion_sources` 与
`notion_urls_discovered` 中。

| 页面 | 用途 |
|---|---|
| [FCF Start Here / Agent Router](https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47) | 唯一 bootstrap；分支选择、治理入口和隔离规则 |
| [FCF Design Branch Index](https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd) | 三条顶层路线、provenance 和 ownership |
| [FCF Project State Current](https://app.notion.com/p/3cca4137d2368114a982f3b09e965e49) | V1 default authority、active RC、V0 branch-local pointer、Open questions |
| [V1 RC4 Closure Revision](https://app.notion.com/p/3cca4137d236819aa3baddca8a2c251c) | V1 当前 self-contained review target |
| [RC3 Review Adjudication & RC4 Closure Patch](https://app.notion.com/p/3cca4137d23681fba563eccaec1cbf8c) | RC3 review issue 的裁决和 RC4 最小修订 |
| [Simplified V0 Working Main](https://app.notion.com/p/3cda4137d23681508740ceff789abd41) | V0 当前 Working、checkpoint、dynamic/authoring/editor 指针 |
| [Production Design Document Authoring Guide](https://app.notion.com/p/3cfa4137d23681d68f89cc0eed80f99b) | 重要生产设计文档的写作、readback 和状态保真规则 |
| [GPT Work Startup Prompt v2｜V1](https://app.notion.com/p/3cca4137d236815689b9d0cc97d4c287) | V1 Design/Integration Workspace 的启动约束 |
| [GPT Work Migration Handoff｜V1](https://app.notion.com/p/3cca4137d236813388aadeb304bb6515) | V1 角色防火墙、最小 rebase、transport failure 处理 |
| [GPT Work Method Handoff｜Representation](https://app.notion.com/p/3d6a4137d23681829824f57f9105e74f) | 四面展开、Signature、Merge Test、Resolver admission |
| [FCF Research Orchestration Hub R2](https://app.notion.com/p/3d6a4137d236814e9f35e6ae2a761927) | 运行状态、Stage registry、Artifact registry、Gate decision |
| [Execution Runbook R2](https://app.notion.com/p/3d6a4137d23681ca8265f98253f258a5) | 唯一流程 contract、A/B/FR lane、并行、handoff、review |
| [Persistent Role Registry](https://app.notion.com/p/3d6a4137d2368137a8f3c7898e8e7ae5) | 长期角色名、stable handle、职责边界、handoff envelope |
| [Representation Design Gate R1](https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a) | Pilot-A 的 representation gate 及四面后续边界 |
| [15 Case Authoring Visualization R0](https://app.notion.com/p/3d6a4137d236814ea872ed6305942594) | C01–C15 原始案例和后续具体化附录 |
| [4 Logic Surface Authoring Stress Test R1](https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3) | 四面压力测试、Bass 样板、Representation working handoff |

Notion 页面当前大多标记为 `unverified`。这里的链接是可定位的来源，不代表
Notion verification 状态已经替团队完成语义审核。

## 5. 本地工作包

### Canonical V1 contract 与 runtime

- [`docs/fcf_v1_engineering_spec.md`](docs/fcf_v1_engineering_spec.md)
- [`docs/fcf_v1_overview_cn.md`](docs/fcf_v1_overview_cn.md)
- [`docs/design_closure_index.md`](docs/design_closure_index.md)
- [`docs/design_decision_log.md`](docs/design_decision_log.md)
- [`docs/implementation_readiness_matrix.md`](docs/implementation_readiness_matrix.md)
- [`docs/verification_report.md`](docs/verification_report.md)
- [`fcf_v1/`](fcf_v1)
- [`schemas/`](schemas)
- [`tests/`](tests)

### 机制设计 contract

- [`docs/temperature_mechanism_design.md`](docs/temperature_mechanism_design.md)
- [`docs/dissolved_oxygen_mechanism_design.md`](docs/dissolved_oxygen_mechanism_design.md)
- [`docs/flow_mechanism_design.md`](docs/flow_mechanism_design.md)
- [`docs/light_turbidity_mechanism_design.md`](docs/light_turbidity_mechanism_design.md)
- [`docs/depth_structure_mechanism_design.md`](docs/depth_structure_mechanism_design.md)
- [`docs/environment_factor_composition_design.md`](docs/environment_factor_composition_design.md)
- [`docs/resource_history_mechanism_design.md`](docs/resource_history_mechanism_design.md)
- [`docs/motive_behavior_program_design.md`](docs/motive_behavior_program_design.md)
- [`docs/encounter_conversion_mechanism_design.md`](docs/encounter_conversion_mechanism_design.md)
- [`docs/contact_hook_mechanism_design.md`](docs/contact_hook_mechanism_design.md)
- [`docs/fish_entity_variant_design.md`](docs/fish_entity_variant_design.md)
- [`docs/dsl_semantic_design.md`](docs/dsl_semantic_design.md)
- [`docs/editor_contract.md`](docs/editor_contract.md)
- [`docs/editor_interaction_design.md`](docs/editor_interaction_design.md)

### 治理、审核和分支关系

- [`AGENTS.md`](AGENTS.md)
- [`docs/mechanism_spec_writing_and_review_guide_cn.md`](docs/mechanism_spec_writing_and_review_guide_cn.md)
- [`docs/scoped_review_protocol.md`](docs/scoped_review_protocol.md)
- [`docs/independent_review_checklist.md`](docs/independent_review_checklist.md)
- [`docs/fcf_v0_document_governance.md`](docs/fcf_v0_document_governance.md)
- [`docs/fcf_v0_conflict_register.md`](docs/fcf_v0_conflict_register.md)
- [`docs/glossary_cn.md`](docs/glossary_cn.md)

### V0、Bass、空间和 authoring

- [`bass_dynamic_preference/`](bass_dynamic_preference)
- [`experiments/fcf_simplified_v0/`](experiments/fcf_simplified_v0)
- [`docs/bass_dynamic_preference_pressure_test.md`](docs/bass_dynamic_preference_pressure_test.md)
- [`docs/bass_dynamic_preference_prototype_validation.md`](docs/bass_dynamic_preference_prototype_validation.md)
- [`authoring/`](authoring)
- [`editor/`](editor)
- [`ogre_lake_spatial_bake/`](ogre_lake_spatial_bake)
- [`docs/spatial_bake_fixture/`](docs/spatial_bake_fixture)
- [`docs/ogre_lake_reproducible_overlay_experiment.md`](docs/ogre_lake_reproducible_overlay_experiment.md)
- [`docs/ogre-lake-spatial-authoring-explainer.html`](docs/ogre-lake-spatial-authoring-explainer.html)

### Representation 交付包和 Notion 离线快照

- [`outputs/fcf_authoring_concrete_r2/`](outputs/fcf_authoring_concrete_r2)
- 其中 `notion-00.md` 至 `notion-43.md` 是已抓取的 Notion 内容片段；
  `baseline_*.md` 是当时的源页面快照；
  `delivery-manifest.json` 是该 bundle 的文件 hash；
  `current-state-snapshot.md` 是最近一次本地状态快照。
- [`deliverables/ogre-lake-spatial-authoring-explainer-package/`](deliverables/ogre-lake-spatial-authoring-explainer-package)
  是 `docs/` 对应的发布镜像；规范源仍在 `docs/`。

`tmp/`、`.pytest_cache/`、`__pycache__/` 和 `.DS_Store` 是本地暂存或生成物，
不要把它们当作 canonical contract。`tmp/` 中的白板、PDF 图片和 SVG 仍可作为
追溯素材，但不替代 `docs/` 或 `outputs/` 的规范入口。

## 6. Agent 角色与协作框架

### 角色

| Canonical role | 负责什么 | 不负责什么 |
|---|---|---|
| `FCF-FISH-RESEARCHER` | Reality / Strategy Research、Story Sweep、Research Package | 不做 Representation PT1–PT4；不把猜测写成事实 |
| `FCF-EVIDENCE-REVIEWER` | 独立核验事实、Evidence、Scope、Owner、Missed Story | 不读 Worker scratchpad；不直接改 Worker 产物 |
| `FCF-SEMANTIC-TRIAGE` | Existing Pattern、Compression、Coverage Delta、Semantic Escalation | 不修改 Design Authority；不把自然语言相似当作 Pattern Fit |
| `FCF-REPRESENTATION-WORKER` | 已审核 Story 到 Config / Table / Step Table / Narrow DSL 的表达验证 | 不重建 Reality Baseline；不隐藏 Authoring freedom |
| Design / Integration Owner | 机制、取舍、公式、owner、Gate、窄修 | 不用“更真实”无边界扩 V1 |
| Independent Narrow Reviewer | 按声明 scope 攻击 false fit、replay、conservation、owner 和隐藏复杂度 | 不替代上游设计；不能越权扩大 verdict |
| Cross-Batch Cold Reviewer | 每约三批攻击长期角色的 rubber-stamp、ontology anchoring、过度压缩 | 不承担常规批次流程 |
| Coding Agent / Harness | executable prototype、property/concurrency/replay/regression fixture | 不把测试通过当机制 promotion |

`Independent Review` 的独立性来自 role-separated context + evidence judgment；
长期 Reviewer 可以保留自己的 Findings 经验，但不能读取 Worker 的 scratchpad、
hidden reasoning 或未经审核的猜测。

### 两条 harness 的边界

```text
Fish Audit Harness
  回答现实机制是什么，以及 FCF 应如何理解。

Representation Harness
  回答已审核机制在生产上应该如何表达。
```

A/B lane 只能在 evidence 冻结后有限并行。Audit 后续批次不能静默改写已冻结的
Representation 输入；只有 `NEW_CLASS`、`ARCHITECTURE_CHANGE`、`REALITY_CORRECTION`
或 `REPEATED_NEW_PATTERN` 才登记 `UPSTREAM_CHANGE_EVENT`。

### 标准状态机

```text
Fish Audit:
A0 AUDIT_RUNNING
→ A1 AUDIT_PACKAGE_READY
→ A2 AUDIT_REVIEW_RUNNING
→ A3 AUDIT_EVIDENCE_PASS
→ A4 FISH_ARCHITECTURE_DECISION_GATE

Representation:
B0 REPRESENTATION_RUNNING
→ B1 REPRESENTATION_PACKAGE_READY
→ B2 REPRESENTATION_REVIEW_RUNNING
→ B3 REPRESENTATION_EVIDENCE_PASS
→ B4 REPRESENTATION_DECISION_GATE

Ongoing research:
FR0 RESEARCH_RUNNING
→ FR1 RESEARCH_PACKAGE_READY
→ FR2 EVIDENCE_REVIEW_RUNNING
→ FR3 SEMANTIC_TRIAGE
```

流程规则以 [Execution Runbook R2](https://app.notion.com/p/3d6a4137d23681ca8265f98253f258a5)
为准；Hub 只记录状态和指针，Stage Prompt 只描述单一 stage。

### Agent handoff envelope

```text
FROM_ROLE:
TO_ROLE:
BATCH_ID:
CURRENT_STATE:
ARTIFACT_URL:
ROLE_PROMPT_URL:
REQUESTED_ACTION:
EXPECTED_OUTPUT:
BLOCKING_FINDINGS: NONE / URLs
NOTES: 仅必要限定，不复制长推理
```

接收方先恢复自己的长期上下文，再重新读取 Hub / Current / 输入 artifact；不能
靠上一角色的长聊天或隐藏思路接管。

## 7. Review 与状态规则

所有 independent-review verdict 都必须来自
[`docs/scoped_review_protocol.md`](docs/scoped_review_protocol.md)，并包含：

```text
level
scope
baseline
proves
does_not_prove
open_findings
verdict
```

规则：

- `PATCH_*` 只覆盖明确 diff、行或章节；
- `ARTIFACT_*` 只覆盖一个 named artifact 或 cohesive policy bundle；
- `MILESTONE_*` 才能依据原始 Goal / DoD 判断 milestone；
- 没有声明 level 的 verdict 按 PATCH 处理；
- 只有准备声明 `all complete`、`closed` 或 `Freeze-ready` 才运行 milestone
  closure review；
- Review target 读不到时只报告 `REVIEW BLOCKED BY TRANSPORT`，不能拿旧 RC、
  Mainline、Species Funnel 或其它 ledger 代替 baseline。

## 8. Git 状态与交接策略

当前 Git：

- branch：`main`
- 交接前基线 HEAD：`c08492e`（`Add authoring editor prototype and deterministic harness`）
- 交接文件已作为独立本地 checkpoint 提交；`handoff_manifest.json` 的 Git 区段是生成时快照，
  具体提交历史以接手时的 `git log` 为准。
- remote：未配置，因此当前不能执行有效 push。
- 工作区有既有改动和未跟踪文件，包含机制文档、删除的历史文件、V0/Bass、
  spatial bake、Representation bundle 以及用户提供的 `AGENTS.md`。
- 这些既有改动没有被本次交接回滚，也不应被另一套 harness 擅自清理。

本次交接只新增：

- `HARNESS_HANDOFF.md`
- `handoff_manifest.json`
- `tools/build_handoff_manifest.py`

提交策略是只 stage 上述三个文件；不把既有工作区改动混入交接提交。由于没有
remote，提交只能作为本地 checkpoint，不能宣称已推送。完整的 status、文件 hash、
Notion URL 去重清单和生成时间见 `handoff_manifest.json`。

## 9. 新 harness 的恢复清单

开始任何新任务前确认：

- [ ] 已加载本地 `AGENTS.md`，并能解析机制指南和 scoped review protocol。
- [ ] 已读取 FCF Router、Project Current、目标 branch 的 Current / Working 页面。
- [ ] 已确定本任务的 active branch，且没有因术语相似误切路线。
- [ ] 已区分 Authority、Working、Candidate、Historical、Evidence、Deferred。
- [ ] 已确认本地文件与 Notion 页面是“规范源 / 派生镜像 / 离线快照 / 生成物”中的哪一种。
- [ ] 机制任务已做 progressive disclosure，而不是无边界扫库。
- [ ] 需要独立审核时，已声明完整 `level/scope/baseline/proves/does_not_prove/open_findings/verdict`。
- [ ] 运行测试并记录命令、结果、时间；测试通过不替代语义审核或 production gate。
- [ ] 若写回 Notion，保留来源链接、状态标签和 readback 记录。
- [ ] 若做 Git 操作，只处理本任务明确产生的文件；禁止 reset、force-push 或覆盖既有工作。

## 10. 已知缺口

- Notion 页面当前大多 `unverified`；它们是可定位来源，不是自动完成的审核证明。
- 本地没有 Git remote；若需要推送，必须先由项目负责人配置并核对目标 remote。
- 生产 runtime/storage 尚未通过 RC4 的真实 factory、journal、跨进程和独立窄审
  acceptance contract。
- Simplified V0 的 Human Usability Validation 尚未完成。
- Representation 的 Bake escape lane、Summer Oxythermal 2D Profile 准入、
  PostFront overlay 收敛、Response 模板数量和最终 canonical IR 仍是 Working/Open。
- 本交接记录的是截至 2026-09-10 的状态；接手方必须以 live Current 页面和本地
  manifest 的新快照处理后续漂移。
