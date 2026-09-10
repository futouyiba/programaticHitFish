# Harness Agent Mesh｜搭建与运行手册（拓扑 C）

状态：**Working / 本机基建文档**。描述 Claude Desktop (Claude Code) 上 FCF 多角色
协作体系的落地方式；角色语义以 `HARNESS_HANDOFF.md` §6 与 `AGENTS.md` 为准。

## 1. 拓扑

```text
长期会话（用户在 Claude Desktop 打开的 tab）
├── Coordinator（默认由主工作会话兼任）
├── CROSS-BATCH-COLD-REVIEWER（跨批冷审，保留自身 Findings 经验）
└── DESIGN-INTEGRATION-OWNER（按需）

批内角色（Coordinator spawn；**暖启动**：全新上下文 + 各自角色记忆）
├── fcf-fish-researcher
├── fcf-evidence-reviewer
├── fcf-semantic-triage
├── fcf-representation-worker
└── independent-narrow-reviewer
```

持久状态**不放在对话里**：状态机推进记 Notion Hub（A0–A4 / B0–B4 / FR0–FR3），
artifact / evidence 进本 repo，本机另有 run journal。对话只是执行现场。

## 1.1 连续性 vs 独立性（暖启动机制）

治理要隔离的是**角色之间**（reviewer 看不到 worker 草稿），不是**批次之间**
（角色可以越干越熟；HARNESS_HANDOFF §6 明确允许长期 Reviewer 保留 Findings 经验）。
因此批内角色默认**暖启动 spawn**：

- spawn 时上下文全新（独立性），但先读自己的角色记忆
  `<workspace>/role_memory/<role>.md`（连续性）：渐进式读取成果、已核验来源、
  过往 Findings 模式、表达约定。
- 任务结束时把新学到的**过程性知识**增量写回自己的记忆；未审核猜测不写入。
- 记忆文件在 repo 外（不公开、不污染版本史），比长对话更抗 compaction、可审计。
- 隔离规则：角色只读写**自己的**记忆文件；禁止读取任何其它角色的记忆或草稿
  （各章程启动协议已内置，`tests/harness/test_agent_defs.py` 校验）。

需要重交互或超长记忆的角色（如 Cross-Batch Cold Reviewer、Design Owner）
升级为专属会话；同一工作日内也可对同一 agent 用 SendMessage 续聊。两种方式共用同一份章程。

## 2. 角色定义文件

- 规范源：`programaticHitFish/.claude/agents/*.md`（随 repo 版本化；
  envelope 的 `ROLE_PROMPT_URL` 绑定到具体文件 + commit SHA）。
- 部署副本：`A:\Projs\FCF-Harness-Handoff\.claude\agents\`（工作区根，
  供 cwd 在交接根目录的会话加载）。
- **同步规则**：修改角色章程只在规范源改，然后复制到工作区根；
  `tests/harness/test_agent_defs.py` 校验定义与 `harness/core.py` 的
  `ROLE_REGISTRY` 一致、reviewer 角色无写工具、章程含 envelope/边界声明，
  且（部署目录存在时）部署副本与规范源逐字一致。
- **ROLE_PROMPT_URL 约定**：envelope 中的 ROLE_PROMPT_URL 使用
  `<repo 相对路径>@<commit short SHA>` 形式（如
  `.claude/agents/fcf-evidence-reviewer.md@91ae7e1`），把章程内容锚定到具体提交；
  未推送的本地 commit 在 SHA 后标注 `(local)`。
- 只读角色的记忆写回：当前为 **Coordinator 代写机制**——角色以「记忆增量提案」
  附于报告末尾，Coordinator 逐字转写入 `role_memory/<role>.md` 并标注来源批次
  （各章程已声明）。后续若引入受限写工具再升级。
- **代写可验证性锚点**：每个批次的 agent 报告由 Coordinator **逐字归档**到
  `outputs/batches/<BATCH_ID>.md`（append-only，不改写）；角色记忆中的转写内容
  可与对应批次文件 diff 核验「逐字」。
- 新会话启动时加载 agent 定义；改完文件需要重启会话（或新开 tab）生效。

## 3. 通讯模式

### 会话 ↔ 会话（长期角色之间）

- 用本环境会话管理工具：`send_message`（按 sessionId 投递，消息以
  「来自 {来源会话}」的用户回合进入对方队列；对方正忙时排队）。
- 消息体使用 `HandoffEnvelope` 10 字段（`harness/contracts.py`），
  `NOTES` 只放必要限定，不复制长推理。
- 接收方先恢复自己的长期上下文，再重读 Hub / Current / artifact；
  不依赖发送方对话史。
- 限制：双方须为桌面端打开的会话；不能给 unattended / remote 会话发消息。

### Coordinator ↔ 批内角色（会话内 spawn）

- spawn 时把 envelope 字段写进 prompt（BATCH_ID / CURRENT_STATE /
  ARTIFACT_URL / REQUESTED_ACTION / EXPECTED_OUTPUT / 声明的 baseline）。
- Reviewer 独立性 = spawn 的干净上下文 + 只读工具白名单 + envelope
  显式 baseline；不向 reviewer 透传 Worker scratchpad。
- 需要 reviewer 续聊时用 SendMessage 续同一个 agent，不重 spawn。

### 共享底座

- Notion Hub：状态机、Stage/Artifact registry、Gate decision（默认只读；
  写回须用户明确要求 + readback）。
- repo：artifact、evidence、测试基线（`.venv/Scripts/python -m pytest -q`；
  Windows 已知 3 个 fork 平台差异失败，见 `outputs/notion-live-drift-2026-09-10.md` 附录环境）。

## 4. 与原 Codex agent server 方案的对应

| Codex 方案 | 本方案 |
|---|---|
| 多个对话任务 agent + agent server 互通讯 | 多个 CCD 会话 + 跨会话 send_message |
| 角色 system prompt | `.claude/agents/*.md` 章程（版本化） |
| 常驻消息总线 | 回合制投递（envelope + 状态机本就是异步协作） |
| 共享工作区 | 同 repo + Notion Hub + run journal |

## 5. 已知缺口

- DESIGN-INTEGRATION-OWNER、CROSS-BATCH-COLD-REVIEWER、CODING-AGENT-HARNESS
  的 agent 章程未建（长期会话承担）；需要时按同模板补。
- 跨会话消息无加密/签名；BATCH_ID 与 artifact hash 是防篡改锚点。
- 会话间通讯依赖桌面端在线；无人值守编排（cron/workflow）另行评估。
