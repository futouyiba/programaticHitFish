# BATCH｜INFRA-REVIEW-001

- 保存说明：agent 报告逐字归档（reviewer 无写工具；由 Coordinator 保存，内容未改写）。
- 归档时间：2026-09-10
- 角色：independent-narrow-reviewer（命名角色，首次正式运行）
- 被审对象：commit 91ae7e1（基线 0ccd168）；处置见 fdbc7ef 与 INFRA-REVIEW-001-PATCH-002

---

## Scoped Review Verdict

```text
level: ARTIFACT
scope:
  - commit 91ae7e16bcc96d0b3ec60575d7775da0fb0c8108 "feat: add role-separated agent harness
    (contracts, charters, notion providers)"（16 文件，719 insertions）
  - harness/core.py（ROLE_REGISTRY 8 角色、3 lane / 13 状态、can_transition）
  - harness/contracts.py（HandoffEnvelope 10 字段、validate_verdict）
  - harness/sources.py（SourceRef、OfflineSnapshotProvider、NotionMCPProvider、
    classify_transport_error、4 类错误码）
  - .claude/agents/*.md 5 份章程 + 工作区根部署副本 A:\Projs\FCF-Harness-Handoff\.claude\agents\
  - tests/harness/test_agent_defs.py、tests/harness/test_contracts.py
  - docs/harness_agent_mesh.md、CLAUDE.md、outputs/notion-live-drift-2026-09-10.md、
    pyproject.toml、.gitignore 增量
baseline:
  - HARNESS_HANDOFF.md §6（角色表、两条 harness 边界、标准状态机、envelope 10 字段）、§7（review 规则）
  - AGENTS.md（scoped review verdict 字段与 level 语义、review 依赖路由）
  - docs/scoped_review_protocol.md 全文（§1–§7，含 Trial 0 自审记录）
  - 审核材料：tmp/harness-infra-review-001/{commit-info,diff-stat,diff-full}.txt（完整 SHA 91ae7e16bcc96d0b3ec60575d7775da0fb0c8108，基线 origin/main @ 0ccd168）
  - 磁盘源文件逐字比对 diff（防「审的材料非 commit 内容」）：一致
  - 部署副本 5/5（3 份全文 + 2 份 tools 行）与规范源比对：一致
proves:
  - ROLE_REGISTRY 8 角色与 HARNESS_HANDOFF §6 角色表一一对应，owns/excludes 语义映射一致
  - 状态机 13 状态、3 条 lane 的值字符串与 §6 逐字一致；can_transition 单向链与 §6 状态图一致，
    跨 lane 转移被正确拒绝
  - HandoffEnvelope 10 字段名与 §6 envelope 逐字一致；frozen dataclass + asdict 往返无字段丢失
  - transport 边界符合"禁止静默降级"：未配置→显式 MCPNotConfigured；空页体→TRANSPORT_FAILURE；
    非 transport 异常→classify 后 raise from，不吞、不降级、不伪造 live
  - 3 个 reviewer 角色 tools 白名单实际无写工具（逐份核对），与治理"reviewer 只读"一致；
    fish-researcher 的 Web/notion-search 属检索需要，合理
  - replay：validate_verdict / classify_transport_error / can_transition 均为纯函数，无隐藏状态；
    find_url 的 sorted(glob) 保证确定性
  - hidden complexity 检查通过：harness 包零第三方依赖（dataclasses/pathlib/typing/re），
    pyproject 仅加 packages.find，无未声明依赖引入
  - .gitignore 增 .claude/settings.local.json 合理（本地权限缓存不入库）
does_not_prove:
  - 不证明 FCF 任何机制语义、V1/V0 文档集或 RC4 状态；本审是基建审核，
    CURRENT_STATE 借用 A2 位不构成状态机推进
  - 不证明 Execution Runbook R2 对回退/REVISE 转移的定义与 can_transition 相容
    （Runbook 是 Notion 页，未列入本批 baseline，无法裁决）
  - 不证明部署副本未来持续同步（当前无自动校验，见 F5）
  - 不证明 Windows 3 个 fork 失败的定性（未运行测试，依据 coordinator 声明 + 本批文档证据）
open_findings:
  - BLOCKER F1：validate_verdict 的 level 合法值与治理文档直接矛盾，verdict 字段零校验
  - BLOCKER F2：OfflineSnapshotProvider.find_url 会把"被其它快照链接引用的页面"静默错配为"有快照"，
    且该 provider 零测试覆盖
  - MINOR F3：docs 引用 drift 报告不存在的"附录环境"章节，Windows 3-fail 基线无书面落点
  - MINOR F4：暖启动机制承诺断链——4 个只读角色章程要求写回角色记忆，但工具白名单无任何写工具
  - MINOR F5：ROLE_PROMPT_URL 无 SHA 绑定 + 部署副本无同步校验，与 docs §2 自身承诺不符
  - MINOR F6：WRITE_TOOLS 黑名单不含 Bash 与 Notion 写类 MCP 工具，reviewer 只读护栏不全
  - MINOR F7：HandoffEnvelope 无语义校验（CURRENT_STATE/TO_ROLE 不对照状态机与 registry）
verdict: ARTIFACT_REVISE
```

## Findings 详情（节选要点，全文以 verdict 块为准）

### F1（BLOCKER｜false fit + conservation）
- baseline（scoped_review_protocol.md:19-20 与 AGENTS.md 字段表）定义 `level: PATCH | ARTIFACT | MILESTONE`（纯等级），`verdict: <LEVEL>_APPROVE | <LEVEL>_REVISE`（结论）；代码 `_LEVELS` 六值合并强加给 level。
- 后果：治理合法输入 `level: "ARTIFACT"` 被拒；`verdict` 字段零校验（"level":"ARTIFACT_APPROVE" 配 "verdict":"pass" 通过）；错误契约被测试固化为绿灯。

### F2（BLOCKER｜false fit）
- `find_url` needle 子串对快照全文匹配：「被引用」被当「存在」。drift 报告明载 Router/Current/RC4 三页只在 baseline 文件中被链接引用——按此规则会错配返回 local_path 指向错误文件。OfflineSnapshotProvider 零测试覆盖。

### F3（MINOR）docs 引用不存在的「附录环境」（报告仅 §1–§5）。
### F4（MINOR）4 个只读角色章程要求写回角色记忆但无写工具；本批 reviewer 自身实测复现。
### F5（MINOR）ROLE_PROMPT_URL 无 SHA 绑定；部署副本无自动校验。
### F6（MINOR）WRITE_TOOLS 不含 Bash 与 Notion 写类 MCP 工具。
### F7（MINOR）HandoffEnvelope 无语义校验。

另记：can_transition 仅单向前进，与 baseline 状态图一致；REVISE 回退是否由 Execution Runbook R2 定义留作 open question。

## 角色记忆增量（无法自写，请 coordinator 或用户代写入）

（见 role_memory/independent-narrow-reviewer.md「INFRA-REVIEW-001」段——由 Coordinator 逐字转写）

## 给 coordinator 的处置建议

F1、F2 修复前不应将该 commit 推送或在其上叠加依赖 `validate_verdict` / `find_url` 的流程；F4 需要一次显式的机制决策（写回路径归谁）。修复后按 PATCH 级重审对应 diff 即可，无需重跑本 ARTIFACT 全审（6 项 scope 中 core.py 状态机、envelope 形状、transport 错误分类、章程-治理一致性四块已核过且无 blocker）。
