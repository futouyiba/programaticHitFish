# Notion Live vs Offline Snapshot Drift Report

生成时间：2026-09-10（本机 live fetch；Asia/Shanghai）
性质：**会话工作材料 / transport 证据**，不是 Authority，不是 Review verdict。
Live 通道：Notion 官方远程 MCP（`https://mcp.notion.com/mcp`，用户级 OAuth）。

## 1. 权威链 live 冒烟（本机首次 live 读取）

| 页面 | Live 结果 | last_edited (UTC) | verification |
|---|---|---|---|
| FCF Router（3cca…9e47） | 读取成功，默认路线/分支隔离规则完整 | 2026-09-08T09:45:45 | unverified |
| Project State Current（3cca…5e49） | 读取成功；active V1 review target 仍指向 RC4 | 2026-09-01T11:39:12 | unverified |
| V1 Core Candidate RC4（3cca…251c） | 读取成功；self-contained review target 内容完整（§0–§20） | 2026-08-30T17:57:57 | unverified |

结论：Router → Project Current → RC4 链路 live 可达，**无 `REVIEW BLOCKED BY TRANSPORT`**。
注意：这三个页面在离线快照包中**没有**完整快照（只在 baseline 文件中被链接引用）；
本次为接手机器首次直接读取 V1 权威链。

## 2. 离线快照 drift 对比

| 快照文件 | 页面 | 快照时间 (UTC) | live last_edited (UTC) | drift |
|---|---|---|---|---|
| baseline_gate.md | Representation Design Gate R1 | 2026-09-09T10:17:14 | 2026-09-09T10:17:14 | **无** |
| baseline_mapping.md | Case Mapping C01–C15 | 2026-09-09T06:52:18 | 2026-09-09T06:52:52 | ~34s，实质无 |
| baseline_bass.md | 大口黑鲈单鱼深挖 R0 | 2026-09-09T10:25:50 | 2026-09-09T16:18:44 | **有：快照后 ~5.9h 被编辑** |
| baseline_stress.md | 4 Logic Surface Stress Test R1 | 2026-09-09T10:26:32 | 2026-09-09T16:52:55 | **有：快照后 ~6.4h 被编辑** |

即：离线包四份 baseline 中两份（Bass 深挖、Stress Test）在**打包前就已过时**；
与 HARNESS_HANDOFF.md「已知缺口」的警告一致。任何 Representation 后续工作
必须以 live 页面 rebase，不得以 baseline_*.md 为最新 Working 状态。

## 3. 交接指定的下一刀目标已定位（未读取全文）

- **Summer Oxythermal Stress Representation Knife R0｜2D Profile vs Structured Trade-off vs Narrow Expression**
  `https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50`
  挂在 4 Logic Surface Stress Test R1 之下；搜索时间戳 2026-09-10T03:49Z（交接打包 ~7 分钟前创建）。
- 相关 Working 面：Bass 投影卡 D（SummerStress FishGroup）、0.3.4 Authoring Representation Checkpoint R0（OPEN-01）。

## 4. 对 harness 的影响

- `harness/sources.py` 的注入式 fetcher 设计无需改动：本会话的 live fetcher 即
  Notion MCP `fetch` 工具，由会话层注入，仓库不含凭证。
- 快照 provider 的 `SNAPSHOT_UNVERIFIED` 标记策略被本次 drift 证实为必要：
  若无 live 通道，Bass/Stress 两页的最新状态会被误当作快照内容。

## 5. 未做

- 未写回任何 Notion 页面（治理默认只读）。
- 未把本报告升级为任何 review verdict。
- 未读取 Knife 页全文（留给下一刀任务本体，按其页面自身状态声明处理）。

## 附录：本机 pytest 基线（环境说明）

- 命令：`.venv/Scripts/python -m pytest -q`（Windows 11，Python 3.14.5，项目 venv 含 pytest + numpy）。
- 基线（harness 基建 commit 91ae7e1 后）：**129 passed / 3 failed**。
- 3 个失败为 `tests/test_fcf_v1.py` 中 `multiprocessing.get_context("fork")` 的跨进程
  DurableJournal 用例（integrity_safe / exactly_once_same_id / rejects_conflicting_same_id）：
  Windows 无 fork 上下文，属交接前既有的平台差异，非回归。同文件 SQLite 版用 `"spawn"`
  在本机通过。macOS 上全量 117 passed（交接方报告）与本机数字对账一致（当时测试总数不同）。
- 修复该差异需将 fork 改为 spawn（worker 均为模块级函数，spawn 兼容），属独立小改动，
  待负责人批准后另行提交，不与 harness 基建混批。
