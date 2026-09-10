# FCF Harness 项目入口

开始任务前按以下顺序恢复上下文：

1. 读取 [HARNESS_HANDOFF.md](HARNESS_HANDOFF.md) 和本文件。
2. 读取 [AGENTS.md](AGENTS.md)，遵守角色边界、机制路由和 scoped review verdict。
3. 默认路线是 FCF V1：Router → Project State Current → active target；只有任务明确要求时进入 Simplified V0 或 First-Principles。
4. 保持 Fish Audit Harness 与 Representation Harness 隔离；不得把测试通过写成 promotion 或 Freeze。
5. Notion 默认只读；离线快照必须标注 snapshot，MCP 不可用不得冒充 live Authority。

角色、状态机、handoff envelope 和来源优先级以 `HARNESS_HANDOFF.md` 为准。任何独立审核都必须声明 `level/scope/baseline/proves/does_not_prove/open_findings/verdict`。
