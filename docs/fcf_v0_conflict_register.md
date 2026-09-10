# FCF V0 冲突登记与 V0→V1 Delta

文档状态：**RETAINED / 当前治理入口**  
权威级别：**治理记录，不替代 V0 实验或 V1 contract**  
范围：Simplified V0 calibration、Bass dynamic preference prototype、Ogre Lake authoring evidence。

## 1. 冲突登记

| ID | 涉及对象 | 类型 | 当前裁决 | Owner | 解决条件 | 状态 |
|---|---|---|---|---|---|---|
| C-001 | `scoped_review_protocol.md` Trial 0；`design_closure_index.md` V1 gate | 状态表述冲突 | Trial 0 只证明协议自审，不证明 V1 Freeze | Review governance | 无需再改；后续 verdict 复用完整字段 | RESOLVED |
| C-002 | V0 reports；V1 mechanism/design docs | 权威层级差异 | V0 数值是 fixture/prototype evidence，V1 contract 保持独立 | V1 mechanism owner | 只有显式 V1 review 才能升级 | INTENTIONAL DIVERGENCE |
| C-003 | Ogre 初版 `96`；reproducible overlay `285/224/1,033` | 证据版本冲突 | `96` 仅历史示意；复现实验为当前数字入口 | Spatial authoring owner | 任何引用须注明数字语义 | RESOLVED |
| C-004 | `docs/` 与 `deliverables/` 同名 Markdown | 重复/漂移风险 | `docs/` canonical，`deliverables/` 仅发布镜像 | Release owner | 发布时复制并校验 SHA-256 | CONTROLLED |

## 2. V0→V1 Delta

| Delta | V0 内容 | V1 内容 | 分类 | 处理 |
|---|---|---|---|---|
| D-001 | 固定 seed、fixture 参数、Monte Carlo 输出 | V1 contract 的 owner、revision、replay 语义 | `non-promotable evidence` | 仅作校准证据，不写回 V1 |
| D-002 | Bass 三时段动态偏好与 Prototype Gates | V1 通用 Species/Program/Environment contract | `intentional divergence` | 保留为具体案例，不扩展为通用机制 |
| D-003 | 初版 Ogre 手工切块估算 | 可复核 overlay 的确定性计数 | `intentional divergence` | 初版归档，复现实验为当前入口 |
| D-004 | V0 通过测试的局部性质 | V1 production runtime/storage gate | `non-promotable evidence` | 测试通过不替代 production gate |
| D-005 | V0 报告中的 PASS WITH DELTA | scoped review 的 level/scope verdict | `needs V1 decision` | 报告 verdict 只覆盖自身 artifact/patch |

## 3. 使用规则

- 新发现的问题先登记，再改正文；修复后保留原 ID 和状态迁移记录。
- `intentional divergence` 不应被改写成 blocker，也不自动触发 V1 文档修改。
- `needs V1 decision` 必须指定 V1 owner；在裁决前，V0 只能继续作为证据层。
- `non-promotable evidence` 可以支持调参或反例分析，但不能成为 Authority。
- 所有 review 结论必须声明 `level`、`scope`、`baseline`、`proves`、`does_not_prove`、
  `open_findings`、`verdict`。

## 4. 当前闭合判断

本登记已覆盖本轮已发现的重复、冲突、过时和层级问题；没有把任何 V0 结果提升为 V1
Authority。它证明的是 V0 governance bundle 的记录完整性，不证明 V0 数值正确、V1
Freeze 完成或生产接入完成。

