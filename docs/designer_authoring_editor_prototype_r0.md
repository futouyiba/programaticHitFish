# Designer-facing Authoring Editor Prototype R0

> 术语沿革：FishMode →（2026-09-11）FishGroup →（2026-10-22）中鱼习性模式（EngagementMode）。FishGroup 概念退役，习性的数据与量级划分由中鱼习性模式承担；模式直接持有 response 程序（pathway 仲裁、meaning 引用、response policy）的引用。IA 结构与五个 walkthrough 任务不变。

运行：`python3 editor/prototype.py`，浏览器打开 `http://127.0.0.1:8765`。

原型读取并修改真实 `authoring/bass_v0.json`，验证调用现有 `lint_authoring` / `compile_authoring`；工作草稿（Working Draft）在通过 lint（静态检查）前不会写回已保存源（Saved Source）。生效预览（Effective Preview）展示编译后的慢速事实（slow facts）、响应包（response bundle）与候选贡献（CandidateContribution）。

## UX task walkthrough

| Task | Entry / actions | Lost? | Internal IDs / JSON? | Lint / preview help |
|---|---|---|---|---|
| UX-01 readiness | Species → Feeding / Slow Facts → select LOW | No / 2 actions | No | Valid status confirms scope |
| UX-02 ActiveSpawning cap | EngagementMode → SPAWN_GUARD / Species Lifecycle → Effective Preview | No / 3 actions | No | Preview shows compiled policy |
| UX-03 CueFamily | Shared Catalogs → Cue Families → species compatibility | No / 2 actions | No | Affected Objects lists modes |
| UX-04 Guard priority | EngagementMode → Pathway Arbitration | No / 2 actions | No | Ordered GUARD_DEFENSE, FEEDING visible |
| UX-05 conflict repair | Rule Editor → lint → edit priority → re-lint | No / 4 actions | No | Points to conflicting rules / fallback |

These are prototype walkthroughs (not moderated-user evidence). The low-cost HTML keeps source and effective views simultaneously visible and intentionally does not expose runtime identity, RNG or technical spatial fragments.

## IA gate

`Species` owns lifecycle, spatial, slow facts, cue compatibility and materialization. `EngagementMode` owns interaction grammar, pathway arbitration, meaning references and response policy; the mode directly references its response programs, and no separate mode object is materialized. Shared Catalogs remain shared; the mode page links to them rather than copying definitions.

Verdict: **EDITOR_IA_VALIDATED** for this prototype scope. No Authoring Schema Delta. Production UI, permissions, collaboration, history and out-of-scope gameplay stages remain open.

level: ARTIFACT
scope: `editor/prototype.py`, `editor/index.html`, this walkthrough, and editor smoke tests
baseline: current Authoring Schema / Bass fixture / compiler-linter; user-provided Designer-facing Editor Prototype R0; mechanism guide §0; scoped review protocol
proves: the proposed IA can perform the five maintenance tasks against real authoring data and show lint/effective output
does_not_prove: production UI quality, moderated usability, or full FCF completion
open_findings: none
verdict: ARTIFACT_APPROVE
