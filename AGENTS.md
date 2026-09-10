# FCF Agent Instructions（中文治理版）

## Scoped review verdict（带范围的审核结论）

每个 independent-review verdict 都必须声明 authority level 和 scope：

- `PATCH_APPROVE` / `PATCH_REVISE`：只覆盖明确列出的 diff、行或章节；
- `ARTIFACT_APPROVE` / `ARTIFACT_REVISE`：覆盖一份完整 named artifact，或一个明确命名的 cohesive policy bundle；
- `MILESTONE_APPROVE` / `MILESTONE_REVISE`：依据原始 Goal 和 Definition of Done 审核指定 milestone。

如果 reviewer 没有声明 level，一律按 `PATCH_*` 处理。

每个 verdict 必须包含以下字段；字段名保持英文以便机器解析：

```text
level
scope
baseline
proves
does_not_prove
open_findings
verdict
```

Agent 不得扩大 review verdict 的证明范围。patch 或 artifact approval 不能证明项目、整套文档或 V1 Freeze 已完成。

只有准备声明 `all complete`、`closed`、`Freeze-ready` 或同等结论时，才运行 milestone closure review。日常修改不需要完整 coverage audit。

Milestone reviewer 必须先检查 requirement coverage，再检查 semantic correctness。任何明确要求处于 missing 或 partial 状态，都必须阻止 `MILESTONE_APPROVE`。

## Mechanism documentation routing（机制文档按需深入读取）

当任务将创建、修改或审查以下机制语义或其 Authoring 表达时，Agent 必须先读取并遵循
[机制规格文档写作与审查指南](docs/mechanism_spec_writing_and_review_guide_cn.md) 的第 0 节
“Agent routing”，再按该节的任务矩阵深入读取所需章节：

- FCF、鱼种机制、环境机制、Encounter 或策略故事文档；
- 机制配置、Authoring 配置、Rule DSL 或规则编译；
- 表达机制语义的执行链、生命周期图、Mermaid 图或概念拓扑；
- Owner、状态写回、随机判定、失败边界或重复结算；
- 机制文档的发布前审查、Artifact review 或 Milestone review。

读取深度必须遵守指南中的 progressive disclosure 规则，并区分“完整读取审核对象”与“完整读取本指南”：

- 先读入口路由，再读与当前任务直接相关的章节；
- `ARTIFACT` review 必须完整读取被审 artifact，但本指南仍按风险路由；审核本指南自身、明确验证“符合本指南全部要求”，或做涵盖该要求的 Milestone review 时，才读取本指南全文；
- 不要因为存在链接就递归读取整套文档；无关的代码、普通业务文档和不涉及机制的任务不读取该指南；
- 纯排版、链接修复或不改变技术含义的机械编辑，不因文件位于机制文档中而自动升级读取深度；
- 不要把指南中的示例、候选方案或模板自动当成具体机制的 Authority。

Review 依赖必须按用途分流：

- 任何 independent-review verdict：必须读取 [Scoped Review Protocol](docs/scoped_review_protocol.md)；
- RC4 工程语义、V1 Freeze adversarial review，或任务明确引用该清单时：再读取 [Independent Review Checklist](docs/independent_review_checklist.md)；
- 其它机制文档 review 不默认加载 RC4 专项 checklist。

本节只提供路由和强制读取条件；指南正文负责解释原则、模板和例子。若文件移动或重命名，必须同步修复上述相对链接。

若指南链接无法解析、第 0 节缺失，或任务矩阵指向不存在的章节，不得静默略过：先报告 routing blocker；只有当前任务授权修改治理文件时才修复，否则停止受影响部分。Artifact 或 Milestone review 的 `baseline` 必须列出本次实际读取的指南章节及 review 依赖。

## Production Design Document Authoring Guide（FCF Notion Governance）

当任务创建、重构或审查机制框架闭合稿、团队同步稿、Production Design Doc、Deep Companion 或实现前设计说明时，除本地机制规格指南外，必须读取并遵循 FCF Governance 的
[Production Design Document Authoring Guide](https://app.notion.com/p/3cfa4137d23681d68f89cc0eed80f99b)。

该页面是 **Authoring Guide / AI Skill**，不是机制 Current Authority。它要求：

- 先完成 Router → Project Current → Branch → latest Working baseline 的最小 rebase；
- 先做 Source Map、Existing Base Check、Gap Classification、Closure Skeleton，再组装正文；
- 区分 `MECHANISM BLOCKER`、`DOCUMENTATION GAP`、`IMPLEMENTATION DETAIL`、`DEFERRED / NON-BLOCKING`；
- 文档至少提供一屏 mental model、完整因果主链、模块 Input/Logic/Output/Boundary、Worked Example、Production Bridge、Player Feedback、Validation/Open/Deferred；
- 写后执行 Reader/Production Attack、Mechanism Integrity Attack 与 readback；
- 不得因润色、示例或完整性压力把 `Working / Open / Proposal / Deferred` 静默写成 Current。

它与本地 [机制规格文档写作与审查指南](docs/mechanism_spec_writing_and_review_guide_cn.md) 的关系是：本地指南负责机制语义的风险路由与审查深度；Notion Authoring Guide 负责生产设计文档的阅读结构、具体化、工程桥接与交付验收。两者均不替代具体分支的机制 Authority。
