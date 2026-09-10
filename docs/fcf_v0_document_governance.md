# FCF Simplified V0 文档治理清单

文档状态：**治理基线（Governance Baseline）**  
权威级别：**文档管理政策，不替代任何 FCF 机制 contract**  
适用范围：`experiments/fcf_simplified_v0/`、`bass_dynamic_preference/`、
`docs/bass_dynamic_preference_*.md`，以及与 V0 实验直接相连的 README/索引和交付镜像。

说明：当前 Git checkout 只有 `main`，没有名为 V0 的独立分支；本清单按上述路径和
“Simplified V0 / Production V0”标记界定 V0 文档范围。若后续出现真实 V0 分支，需
先做一次 source-map 对照，再决定哪些条目迁移或拆分。

## 1. 治理结论

V0 是数值校准和原型验证分支，不是 V1 机制权威，也不应被当作生产规格。V0 文档按
以下优先级解释：

1. 代码、固定输入和可复跑输出是实验事实；
2. V0 实验 README 是复现入口；
3. `docs/bass_dynamic_preference_*.md` 是解释性报告和 gate 证据；
4. V1 contract、V1 决策日志和生产验证报告不由 V0 改写，V0 只能提出差异或待决问题。

任何 V0 数值、概率、阈值或 verdict 都不能自动升级为 V1 Authority。

## 2. 文档台账与处置

| 对象 | 角色 | 当前处置 | 后续规则 |
|---|---|---|---|
| `experiments/fcf_simplified_v0/README.md` | V0 复现入口 | **保留为 canonical** | 只写运行方式、输入、输出和实验断言；不写机制新语义 |
| `experiments/fcf_simplified_v0/results/*`、`figures/*` | V0 生成证据 | **保留为 generated evidence** | 由代码重生成；禁止手工改 CSV/图；变更需记录 seed/命令 |
| `docs/bass_dynamic_preference_pressure_test.md` | 三时段案例报告 | **保留，标记解释性** | 只引用当前 fixture；不得被引用为参数 authority |
| `docs/bass_dynamic_preference_prototype_validation.md` | Prototype Gate 报告 | **保留，标记 gate evidence** | verdict 只覆盖本报告列出的 gates；不得覆盖 V1 或跨地图推广 |
| `bass_dynamic_preference/*.py`、`output.json` | 原型实现/输出 | **保留为 V0 prototype** | 与 V1 runtime 分开；参数变更必须同步测试和报告 |
| `docs/fcf_v1_*.md`、各机制 `*_mechanism_design.md` | V1 设计/contract | **不并入 V0** | V0 只能链接和提出 delta；冲突交给 V1 owner 裁决 |
| `docs/ogre_lake_*` 与 `deliverables/...` 同名文件 | 复现实验与发布镜像 | **canonical 在 `docs/`，deliverables 只做镜像** | 只改 `docs/`；发布前复制并校验 hash，禁止双源维护 |
| `docs/rf4_*` | 外部证据/研究 | **保持独立证据层** | 不作为 V0 参数来源；历史版本结论必须保留日期和适用范围 |

## 3. 重复内容处理

- 完全相同的 Ogre Lake 两份 Markdown 是发布镜像，不是两个版本。规范源为
  `docs/`；`deliverables/` 只在打包时同步。
- README、设计索引和 V0 报告中的概念摘要允许重复，但只能保留“一句话定义 + 链接”；
  公式、阈值、样例数字只允许出现在一个 canonical 实验或 contract 中。
- 若发现近似重复但内容已分叉，先标为 `DUPLICATE_DRIFT`，比较差异后决定合并或明确
  “解释层/证据层”分工；不得静默覆盖其中一份。

## 4. 冲突处理规则

发现冲突时按以下顺序处理：

1. 先区分对象类型：事实、实验参数、解释、V1 contract、状态/verdict；
2. 同层冲突：以带版本、seed、命令和生成时间的 canonical 来源为准；
3. 跨层冲突：contract 优先于报告，报告优先于摘要，实验参数不反推 contract；
4. 无法裁决：保留双方，新增 `OPEN_CONFLICT`，写明 owner、证据和截止条件；
5. 解决后在旧文档顶部加 `Superseded by` 或 `Retained for historical context`，不要
   删除历史证据。

本轮已确认的治理冲突：`docs/scoped_review_protocol.md` 的 Trial 0 叙述中出现了
“V1 Freeze 已完成”式表述，与设计索引明确列出的 external V1 gate 未完成相冲突；
该处已改为只描述“协议自审完成”，不再暗示 V1 完成。

## 5. 过时内容处理

过时不等于删除。使用三种标签：

- `SUPERSEDED`：有明确替代文档，正文只保留历史缘由和替代链接；
- `HISTORICAL`：没有替代品但仅用于追溯，禁止作为当前输入；
- `RETAINED`：仍是当前实验/contract 的唯一规范源。

任何带数字的旧实验，必须同时写明数字性质（示意、fixture、测量或 production
evidence）和复现入口。无法复现的结果只能保留为 `HISTORICAL`。

## 6. 发布前检查

- [ ] 每份 V0 文档顶部有状态、权威级别、适用范围和复现入口。
- [ ] 数值/阈值只有一个 canonical 来源，其他地方只摘要并链接。
- [ ] 生成物可由固定命令和 seed 重建，且输出目录不手工编辑。
- [ ] 所有 verdict 都声明 `level`、`scope`、`baseline`、`proves`、`does_not_prove`、
  `open_findings`、`verdict`；未声明时按 PATCH 解释。
- [ ] V0 → V1 的每个提升都有明确 owner 和 review；没有“测试通过即升级”。
- [ ] 发布镜像与规范源 hash 一致。

## 7. 本次治理后的最小工作流

```text
修改 V0 代码/输入
  → 固定 seed 重跑
  → 更新 generated evidence
  → 更新对应报告（只解释，不升级 authority）
  → 检查 V0/V1 delta 与冲突
  → 同步 docs/ 到 deliverables/ 镜像
```

本清单只证明上述文档治理政策已建立；不证明 V0 数值正确、V1 Freeze 完成或生产接入完成。
