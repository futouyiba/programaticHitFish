# 机制规格文档写作与审查指南

版本：R1  
状态：工作规范（Working Guideline）  
适用范围：FCF、鱼种机制、环境机制、Encounter、配置与规则文档  
权威级别：本指南只规范写作和审查方式，不替代任何具体机制的产品 Authority

## 0. Agent routing｜什么时候深入读取，什么时候停止

本节是 Agent 进入本指南的入口。它的作用是避免两种错误：需要时只看一个链接标题就跳过；不需要时递归读取整套机制文档，污染上下文。

### 0.1 触发条件

任务将创建、修改或审查以下机制语义或其 Authoring 表达时，进入本指南：

- 创建、修改、重构或审查 FCF、鱼种、环境、Encounter、策略故事机制文档；
- 设计或修改机制配置、Authoring 配置、规则 Schema、DSL 或编译规则；
- 绘制表达机制语义的执行链、生命周期图、Mermaid 图、空间拓扑或 Owner 边界图；
- 讨论 State、Mode、Meaning、Response、Conversion、Contact、Hook、随机判定或状态写回；
- 请求发布前检查、Artifact review、Milestone review 或“是否完成”。

若任务只是普通代码修改、与机制无关的文档编辑，或纯排版、链接修复等不改变技术含义的机械编辑，不进入本指南。机制术语翻译可能改变语义，仍应进入，但只读取相关章节和被修改段落。

### 0.2 按任务选择读取深度

| 任务 | 必读指南章节 | 还必须完整读取什么 |
|---|---|---|
| 新建或重构机制文档 | 1–6、8–9、12；涉及规则表达、DSL、随机判定或时间身份时加读 7 | 当前目标文档；声明 artifact 完成时读取其全文 |
| 只修改配置或 DSL | 6–8、12 | 被修改的配置及必要上下游合同 |
| 只修改图或执行链 | 3–5、12 | 图、图例及其解释的正文 |
| 只做机制术语翻译/双语整理 | 2、3 和被影响主题章节 | 被修改段落及术语上下文 |
| 独立 Artifact review | 11–12 + 被审主题对应章节 + Scoped Review Protocol | 被审 artifact 全文；不自动读取本指南全文 |
| RC4 / V1 Freeze adversarial review | 11–12 + 被审主题对应章节 + Scoped Review Protocol + Independent Review Checklist | scope 指定的 artifact、Authority 与 evidence |
| Milestone closure review | 11–12 + milestone 要求覆盖的章节 + Scoped Review Protocol | 原始 Goal、Definition of Done、相关 artifact、Authority 与 evidence |

只有以下情况需要读取本指南全文：审核本指南自身；任务明确验证某个 artifact 是否符合本指南的全部要求；或 Milestone 的 Definition of Done 明确包含该全量合规要求。

### 0.3 深入和停止规则

1. 先读本节，再读任务矩阵列出的章节；不要只读链接标题后直接行动。
2. `ARTIFACT` review 的“完整”指完整读取被审 artifact，不等于自动完整读取本指南或关联文档树。只有当前任务引用某个具体机制、声称要验证其 Authority，或需要做跨文档一致性检查时，才继续读取相应关联文档。
3. 指南中的模板、示例和候选方案是方法建议，不自动成为任何具体机制的 Authority。
4. 读取到能够完成当前任务和验证其明确要求时停止；不要为了“可能有用”继续递归整个文档树。
5. 如果任务范围后来扩大，重新从本节判断是否需要提升读取深度，并在 review scope 中记录扩大原因。

### 0.4 路由可验证性

- 本指南必须由仓库根目录的 [`AGENTS.md`](../AGENTS.md) 以相对链接引用；这里保留反向链接，便于核验入口与目标没有脱节。
- 如果入口链接无法解析、本节缺失，或任务矩阵指向不存在的章节，Agent 不得静默跳过；应把它报告为 routing blocker。只有任务授权修改治理文件时才修复，否则停止受影响部分。
- Artifact 或 Milestone review 的 `baseline` 必须列出本次实际读取的指南章节和 review 依赖；日常任务不要求生成额外的“已读证明”。
- 路由检查只验证“能否发现并按范围读取”，不证明任何具体机制正确，也不把本指南提升为具体机制 Authority。

这套路由本身也需要维护：文件重命名后，`AGENTS.md` 和本指南中的相对链接必须同步更新。

## 1. 这份指南解决什么问题

一篇机制文档即使包含很多概念、公式和图，也可能仍然无法实现。常见原因是：

- 没有区分“结构没定义”和“数值没校准”；
- 把持久状态、临时派生关系和行为模式混在一起；
- 把所有过程画成同一种节点和箭头；
- 把不同阶段的失败压成一个总概率；
- 用 DSL 掩盖 Owner、优先级和冲突没有定义的问题；
- 把 AI reviewer 的建议误读成人类已经作出的决定；
- 把引用过策略故事，误写成已经覆盖所有策略故事。

本指南的目标是让一份规格同时满足三件事：

1. 非技术读者能用几句话理解它在表达什么；
2. 程序、策划和数值能知道各自下一步做什么；
3. 独立 reviewer 能在明确范围内判断它是否自洽。

## 2. 推荐的文档骨架

复杂机制文档建议按以下顺序组织。简单文档可以删减，但不能删掉与当前风险相关的章节。

1. 文档身份与范围
2. 一页决策摘要
3. 中文术语与实现名速查
4. 执行主链与失败边界
5. 概念账本
6. 配置 Schema 与具体配置
7. 规则表达：普通配置、表格还是 DSL
8. 端到端策略故事
9. 因果归属与重复结算审查
10. 开放问题、验证计划与决策记录
11. 验收标准
12. 独立 review 结果

### 2.1 文档身份

正文使用中文主标签，必要时保留英文技术别名：

```text
文档状态：工作稿（Working）
权威级别：非权威
版本：R1
适用范围：Simplified V0 / Largemouth Bass
明确不负责：Contact、Hook、完整 Population Conservation
```

`Authority / Working / Proposal` 可以保留为稳定检索标签，但不应成为高层读者必须先理解的主要语言。

### 2.2 一页决策摘要

先用 3–5 句话讲清楚机制，再用表格列出决策状态。

```text
系统先判断鱼是否存在，再判断鱼是否愿意理会当前呈现。
鱼进入互动后，再判断当前动作是否能推进到攻击。
攻击之后，接触与挂钩由下游机制负责。
```

建议使用三列：

| 类别 | 应该记录什么 | 示例 |
|---|---|---|
| 已确定 | Owner、阶段边界、失败迁移、数据类型 | Engagement 成功后创建 `EngagedFish` |
| 待调参 | 阈值、概率、半衰期、容量 | `K`、Exposure radius、Conversion probability |
| 待裁决 | 产品语义或证据问题 | Guard 是否读取钓压 |

摘要不应把所有内容都标成“开放”。“开放”必须进一步说明是待调参、待产品决定还是待证据验证。

## 3. 概念类型与图形拓扑规范

执行图的首要任务不是装饰，而是让读者看出“这是数据、规则、实例、事件还是持久存储”。不要把所有节点画成同一种方框。

### 3.1 固定图形语义

| 图形 | 概念类型 | 示例 |
|---|---|---|
| 普通矩形 | 外部事实或输入数据 | World、Presentation |
| 圆角矩形 | 本次求值产生的临时派生结果 | Context Snapshot、FeedingMatch |
| 六边形 | 规则面或解析器 | Mode Resolver、Conversion Rules |
| 双边框矩形 | 本次 Encounter 的逻辑实例 | `EngagedFish` |
| 菱形 | 判定或状态迁移 | ATTACK、CONTINUE、DROP |
| 圆柱 | 跨机会保存的状态或写回存储 | CueMemory、SatiationState |
| 小圆点/事件节点 | 发生过的事件 | ContactOccurred、Hooked |

### 3.2 固定箭头语义

| 线型 | 含义 |
|---|---|
| 实线 | 当前求值的数据依赖 |
| 虚线 | 事件写回、异步更新或下一次快照可见的变化 |
| 粗实线 | Encounter 生命周期状态迁移 |
| 点线 | 非权威、调试或仅用于解释的关系 |
| 带锁定标签的箭头 | 进入下一阶段后不再重新选择上游身份 |

图中必须有图例。中文主标签、英文实现名放在第二行即可。

### 3.3 不要让一张图承担所有问题

复杂文档至少拆成两张图：

1. **求值图**：事实 → 派生语义 → 规则 → 阶段输出。
2. **生命周期图**：Engagement → `EngagedFish` → ATTACK / CONTINUE / DROP → Contact / Hook / State write-back。

如果空间拓扑也重要，再单独画地图或 SourceGroup 图。空间邻近不等于权重自动相加，图上应明确标出这一点。

## 4. 先做 Layer Admission，再建字段

新建 State、Mode、Meaning、Runtime Layer 或中间分数前，先进行准入检查。它应该位于建模流程的前半段，而不是文档最后的自审。

推荐流程：

```text
策略故事 / 反例
→ 失败边界
→ 现有模型能否表达
→ Layer Admission Test
→ Owner 与表示方式
→ 配置 / DSL
→ 编译与覆盖检查
→ Scenario replay
→ 数值校准
```

### 4.1 新层准入模板

```text
拟新增对象：
要解决的具体策略故事：
不新增它会错误合并哪些不同失败：
现有字段为什么不够：
能否用更小的派生关系解决：
独立 Owner：
允许读取：
允许写入：
可证伪预测：
验证样例：
准入结果：采纳 / 拒绝 / 延后
```

默认原则：先写出现有最小模型的可证伪预测，再决定是否扩机制。

## 5. 概念、Owner 与“原因只结算一次”

“原因只结算一次”不是说一个事实永远只能影响一个阶段，而是说同一个行为后果不能在多个阶段被匿名重复奖励或惩罚。

### 5.1 默认阶段归属

| 问题 | 默认 Owner | 典型输出 |
|---|---|---|
| 鱼在哪里、是否存在 | Spatial / Presence | `HabitatSuitability`、`LocalPresence` |
| 当前呈现意味着什么 | Meaning | `FeedingMatch`、`NestThreat` |
| 鱼愿不愿开始互动 | Response | `ResponseGrade`、`FOLLOW`、`TRACK` |
| 已参与后要完成什么动作 | Task | `TaskSignature` |
| 动作能否推进到攻击 | Conversion | `ATTACK`、`CONTINUE`、`DROP` |
| 是否形成物理接触 | Contact | `ContactAttempt` |
| 是否成功挂钩 | Hook | `HookResult` |

### 5.2 因果归属表

复杂文档建议增加一张因果归属表：

| 原因 | 具体表现 | Owner | 可影响阶段 | 禁止的重复 |
|---|---|---|---|---|
| 高温 | 鱼更靠掩体、长追逐更难 | Habitat / Conversion | Presence、Conversion | 不再额外加匿名 `HotPenalty` |
| 钓压 | 熟悉线索的响应下降 | State / Response | Response | 不直接修改 Habitat |
| 护巢 | 目标构成巢区威胁 | Meaning / Guard Mode | Response、Contact intent | 不伪装成 FeedingMatch |

审查问题：

> 同一个原因是否在 Presence、Response、Conversion 中被重复结算？如果影响多个阶段，是否对应不同、可解释的行为后果？

## 6. 配置与 DSL：先判断有没有必要

涉及配置的文档必须写配置；但不应因为“配置”一词就自动引入 DSL。

### 6.1 三层区分

```text
配置 Schema
= 系统允许哪些字段、类型和枚举

Authoring 配置
= 策划实际填写的表格、YAML 或编辑器内容

Rule DSL
= 当规则组合复杂到需要独立表达、编译和诊断时使用的规则格式
```

### 6.2 DSL 的准入条件

只有出现以下一种或多种情况时，才值得引入 DSL：

- 规则数量和条件组合明显增长；
- 需要优先级、fallback、条件树或冲突检查；
- 策划需要独立编辑规则；
- 多个鱼种、模式或场景共享规则结构；
- 需要稳定的编译产物和回放 trace；
- 固定列配置表已经变得过宽或难以维护。

如果普通表格已经清楚表达规则，就不要为“看起来更系统”而增加 DSL。

### 6.3 DSL 的正确定位

DSL 不一定是给人手写的脚本语言。更稳妥的管线是：

```text
策划表格 / YAML
→ 条件树（AST）
→ Typed IR
→ Runtime Rule
```

DSL 只表达声明式条件和类型化结果，不拥有任意脚本副作用。

### 6.4 V0 规则解析约束

以下约束适合 Simplified V0，但不是所有系统的永恒定律：

- Mode、Meaning、Task 这类单值分类规则：在同一规则面内采用确定性选择，优先级只是选择策略；
- Response、Conversion 输出可以是固定的 typed tuple，例如 grade + behavior + failure transition；
- 若未来允许多个 Modifier 组合，必须单独声明 combine policy，不能按文件顺序暗中相加；
- 每条规则有稳定 ID；
- 字段、枚举、输出类型必须经过 Schema 校验；
- 同优先级且条件重叠，默认编译失败；
- 被高优先级规则完全遮蔽的规则，应至少产生 warning；
- 缺少 fallback 或默认值的封闭分类面，应编译失败；
- 跨 Owner 写字段，应编译失败；
- Trace 必须能够返回输入快照、命中规则和输出；
- 不允许直接跨阶段修改 Presence、State、Contact 等其它 Owner 的结果。

`highest priority match wins` 只能理解为“同一规则面中的默认求值策略”，不能替代冲突检测、遮蔽检测和 Owner 设计。

## 7. 随机判定与时间身份

`opportunity_id` 和 `conversion_attempt_id` 应分开定义，它们属于不同阶段。

| 标识 | 所属阶段 | 定义 | 防止的重复 |
|---|---|---|---|
| `opportunity_id` | Engagement 前 | 一次语义呈现机会 | frame/tick/重复触发重复抽取参与 |
| `conversion_attempt_id` | Engagement 后 | `encounter_id + semantic_segment_id` | 同一语义片段重复抽取攻击 |

建议不用泛化的 `attempt_key` 作为唯一术语，除非系统确实有多个不同阶段的 attempt。若保留它，必须在字段定义中说明它是哪一个阶段的 key。

每次随机判定都必须写明：

```text
什么事件产生一次合法判定
判定身份从哪里来
同一身份是否允许重复判定
失败后进入什么状态
何时允许重试
重试上限
如何记录 random sample 与 matched rule
```

`segment_id` 必须由呈现系统在语义边界变化时稳定地产生，例如呈现类型、运动族或相对几何档位发生变化；不能由每一帧或网络包产生。

## 8. 持久状态写回合同

持久状态应采用“机会前读取，终局事件后写回”的模式：

```text
Opportunity
→ read immutable snapshot
→ Response / Conversion
→ terminal event
→ enqueue state delta
→ next opportunity sees new snapshot
```

这样可以避免本次事件立刻改变本次事件的结果。

每个持久状态至少记录：

```text
Scope / key
初始值
读取阶段
写入事件
增量或更新函数
衰减 / 恢复
下一次何时可见
```

AI reviewer 的建议不能替代状态 Owner；只有被人类决定采纳后，才进入正文合同。

## 9. 策略故事与“架构证据”

策略故事不是装饰性示例，而是模型验收和边界压力测试。

每个故事至少应记录：

```text
Situation
玩家目标
鱼侧约束 / 状态
空间与接触条件
呈现动作
预期阶段路径
可观察线索
失败边界
证据或来源
本页是否负责
```

“跨案例架构压力证据”指另一个物种或策略故事用来检查抽象边界是否可复用。它证明的是表示方式、阶段边界、Owner 分配和规则复杂度，不直接证明本物种的生物事实或数值正确。

### 9.1 覆盖表

复杂机制文档建议维护以下表格：

| 故事 | 与本页关系 | 状态 | 本页能证明什么 | 仍缺什么 |
|---|---|---|---|---|
| 直接验收故事 | 本页必须跑通 | PASS / FAIL | 当前机制是否表达目标路径 | 参数或实现问题 |
| 跨案例架构压力证据 | 检验抽象复用 | SUPPORTED / PARTIAL | Owner 与阶段边界是否合理 | 本物种验证 |
| 跨物种迁移 | 使用近缘案例 | ASSUMPTION | 可作为候选结构 | 物种行为证据 |
| 明确越界 | 由其它系统负责 | OUT OF SCOPE | 本页不承担该问题 | 对应 Owner |

不要把“引用过故事列表”写成“已覆盖全部故事”。

## 10. 决策、Review 与验证记录

不需要保存所有 AI reviewer 的原始意见。建议分成三种记录：

### 10.1 人类决策记录

这是权威记录：

```text
问题：
决定：
决定人 / Owner：
日期：
理由：
影响范围：
```

### 10.2 验证记录

```text
案例或实验 ID：
测试目标：
输入：
预期：
实际：
结论：
```

### 10.3 AI Review Finding

只记录需要追踪的意见：

```text
来源：AI review
意见：
状态：采纳 / 拒绝 / 延后
人类裁决：
对应文档位置：
```

正文只保留已经采纳的结论。未采纳但仍有参考价值的内容放入 Review Log、评论或附录。

必须始终区分：

```text
AI 提议 ≠ 人类决定
人类决定 ≠ 已被验证
已验证 ≠ 已完成数值校准
```

## 11. 独立 Review 的范围与结论格式

Routine edit 使用 `PATCH` review；准备宣称一份完整 Markdown 文档达到目标时，使用 `ARTIFACT` review；只有准备宣称整个 milestone 完成时，才使用 `MILESTONE` review。

本指南自身作为一个完整 Markdown artifact 审核时，reviewer 必须读取全文，并使用以下格式：

```text
level: ARTIFACT
scope:
  - docs/mechanism_spec_writing_and_review_guide_cn.md
baseline:
  - AGENTS.md scoped-review rules
  - 本文档的写作、图形、配置、DSL、状态、故事覆盖与记录要求
proves:
  - 该 Markdown artifact 在声明范围内结构完整、概念自洽、可执行审查
does_not_prove:
  - 任何具体 FCF 机制已经正确
  - 整个 documentation set 已完成
  - 项目或 V1 Freeze 已完成
open_findings:
  - none 或逐条列出 BLOCKER / MAJOR / MINOR / NOTE
verdict: ARTIFACT_APPROVE | ARTIFACT_REVISE
```

Reviewer 的 verdict 只能覆盖声明的 `level` 和 `scope`，不能从 artifact approval 扩大为项目完成或 V1 Freeze-ready。

## 12. 发布前自检清单

### 读者理解

- [ ] 前三分钟内能说清楚这套机制解决什么玩家问题。
- [ ] 中文解释先于英文接口名出现。
- [ ] 每个关键术语都有中文解释和实现名。
- [ ] 摘要区分已确定、待调参和待裁决。

### 图与拓扑

- [ ] 图形能区分事实、派生结果、规则、逻辑实例、事件和持久状态。
- [ ] 图中有图例。
- [ ] 实线、虚线、粗线的含义明确。
- [ ] 没有把空间邻近误画成自动权重相加。
- [ ] 求值图和生命周期图没有被迫合成一张难以阅读的图。

### 内容与 Owner

- [ ] 每个字段有数据类型、Owner、读取时机、写入时机和下游作用。
- [ ] 每个持久状态有 key、scope、更新事件和衰减。
- [ ] 每个原因的阶段归属已经说明。
- [ ] 同一原因没有被匿名重复结算。
- [ ] 新增层经过 Layer Admission Test。

### 配置、DSL 与随机性

- [ ] 文档说明为什么需要或不需要 DSL。
- [ ] DSL 有读写白名单、类型检查、冲突检查和 fallback 策略。
- [ ] `opportunity_id` 与 `conversion_attempt_id` 没有混用。
- [ ] 每次随机判定都有稳定身份、重试边界和 trace。
- [ ] 同一 frame、tick、网络包或 segment 不会无意重掷。

### 故事、Review 与发布

- [ ] 直接验收故事、架构压力证据和越界故事分开标注。
- [ ] 人类决策、验证结果和 AI review 意见分开记录。
- [ ] Open item 说明的是调参、产品裁决还是证据验证。
- [ ] 独立 reviewer 的 scope、baseline、proves 和 does_not_prove 完整。
- [ ] 没有把局部 approval 扩大成项目完成声明。
