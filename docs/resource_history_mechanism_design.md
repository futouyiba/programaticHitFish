# FCF V1 资源与鱼类历史状态机制（Design-only）

资源状态（饱食、能量、恢复债务、警戒记忆）是鱼的持久历史，不是每次
呈现（presentation）的即时加成（bonus）。V1 先定义状态归属方（owner）、更新
时机和当前动机（motive）/进入（Entry）边界，避免“饥饿”同时成为栖息占位
（occupancy）、当前动机、E 和转化（conversion）的重复系数。

## 0. 快速阅读

**概念**：资源是世界事实（World Fact）；饱食、警戒、恢复和适应是 END-CUT 后
持久化的种群切片（Population Slice）/队列（cohort）历史（History），不是
即时加成。

**整体机制**：解析器（resolver）只读取固定（pinned）的世界/历史快照
（snapshot）；遭遇（Encounter）/终结结算（Settlement）产生类型化
HistoryDelta，历史/未来（History/Future）归属方以交易（transaction）ID 幂等
应用，下一个因果切点（causal cut）才能影响当前动机、进入或生命周期
（Lifecycle）。

**配置方式**：配置资源事实（resource fact）结构模式（schema）、History
字段/范围/初值、增量契约（delta contract）、归属方、迁移（migration）和
修订版本（revision）；编辑器（Editor）不直接改运行中遭遇候选（Candidate）
的历史值。

**中文机制描述**：鱼完成一次遭遇后，系统统一记账“更饱、更警戒或需要恢复”；
本次遭遇不被刚写入的历史反向改变，重放也不会重复累加。

```mermaid
flowchart LR
  A[World Resource + History Snapshot] --> B[Motive/Entry/Task 解释]
  B --> C[Encounter + Settlement]
  C --> D[Typed HistoryDelta]
  D --> E[END-CUT 幂等应用]
  E --> F[下一 causal cut]
```

## 1. 状态与事实分层

```text
World resource fact      节点当前可用食物/竞争/扰动事实
Fish history state       该 Population Slice 已结算的历史状态
Prospective motive       本次 opportunity 的确定性动机解释
Entry offer E             该动机是否开始 encounter
```

只有世界资源事实与已结算历史才能进入解析器。候选形成后快照这些解释；
后续历史更新不回写既有候选。

## 2. 状态 owner

| 状态/后果 | 唯一归属方 | 更新时机 | 禁止 |
|---|---|---|---|
| 饱食/能量 | 历史/未来 | END-CUT 终结结算 | 进入直接扣同一能量 |
| 警戒/记忆 | 历史/未来 | END-CUT 观察 | 每帧读取并重掷当前动机 |
| 当前资源可用性 | 种群/栖息占位 | 因果切点事实 | 作为鱼的个体饥饿记忆 |
| 前瞻当前动机（Prospective motive） | 当前动机解析器 | 机会（Opportunity）一次 | 当作候选存在 |
| 进入机会（Entry offer） | 行为策略程序（BehaviorProgram） | 机会一次 | 转化再扣“想吃” |
| 追击成本/恢复债务 | 遭遇任务动作产出；历史/未来唯一应用/持久化 | 任务动作结果 + END-CUT | 栖息占位再扣同一体能 |

## 3. 状态数据模型

```text
HistoryCell {
  population_slice_key
  satiation_0_1
  energy_0_1
  wariness_0_1
  recovery_debt
  last_updated_causal_cut
  history_revision
}
```

V1 在普通节点内使用可交换质量（exchangeable mass）：不创建持久个体鱼 ID。
只有当产品明确要求个体记忆时，才另行设计个体身份（identity）、存储和隐私
（privacy）边界；不能在 V1 中隐式引入。

## 4. 输入与输出逻辑

### 4.1 资源事实（Resource fact）

```text
resource_state = {
  prey_density,
  competition_level,
  disturbance_level,
  resource_revision
}
```

它描述节点，不描述某条鱼“饿不饿”。节点资源影响栖息占位或行为策略程序的
当前动机优先级（priority），不能直接写成通用咬钩乘数（universal bite
multiplier）。

### 4.2 前瞻当前动机（Prospective motive）

```text
motive = resolve_motive(
  program_policy,
  resource_state,
  history_snapshot,
  presentation_truth
)
```

V1 当前动机解析器是确定性的优先级/规则决策；若多个规则同优先级且重叠，
领域专用语言（DSL）编译拒绝。`FORAGE` 表示“本次有觅食解释”，不表示鱼已
消耗资源。

### 4.3 进入机会（Entry offer）

```text
E = entry_offer(program_policy, motive, presentation_truth)
```

历史可以作为规则输入（rule input），但同一饱食/警戒后果只能在进入机会中
被消费一次。进入成功不自动减少饱食；资源消耗要等实际下游结果（downstream
outcome）并在 END-CUT 结算。

### 4.4 遭遇 / 终结结算（Encounter / settlement）

实际接触、摄食、失败或逃逸由遭遇/终结结算输出类型化结果（typed outcome）：

```text
HistoryDelta {
  delta_satiation
  delta_energy
  delta_wariness
  delta_recovery_debt
  cause_id
  owner = history_future
}
```

同一结果只能产生一个 HistoryDelta。终结结算重试不得重复应用增量（delta）；
必须以 transaction_id 幂等。

## 5. 历史更新与因果切点（causal cuts）

```text
cut start: read immutable HistoryCell revision N
→ resolve motive / Entry / Encounter from snapshot
→ collect typed outcomes
→ END-CUT atomically apply deltas if revision still N
→ revision N+1
```

遭遇任务动作只生成类型化 `HistoryDelta`；历史/未来是唯一应用、持久化和
恢复该增量的归属方。并发结果使用确定性合并（deterministic merge，例如按
transaction_id 排序后合并），并维护持久的 `applied_transaction_ids` 集合：
同一 transaction_id + 相同增量是幂等重放（replay）；同一 transaction_id +
不同增量必须拒绝为冲突。冲突时拒绝旧修订版本，而不是静默覆盖。历史
更新不会重新打开已消费的机会，也不会产生第二次进入掷骰（roll）。

## 6. 与环境机制的关系

| 环境事实/状态 | 可以影响 | 不可以直接影响 |
|---|---|---|
| 温度/DO/流速 | 任务动作剖面（task profile）、栖息占位、生命周期 | 同一恢复债务再扣 E |
| 光照/浑浊度 | A_visual、感官任务动作 | 饱食/警戒直接改变 |
| 节点资源事实 | 栖息占位或当前动机规则输入 | 伪造个体历史 |
| 饱食/警戒历史（satiation/wariness history） | 当前动机/进入规则输入 | 重新分配 PSU 或改变物种能力 |

如果“资源少”和“鱼很饱”都导致 `FORAGE` 下降，必须说明一个是节点事实、
一个是历史状态，并由同一个当前动机规则一次性解释；不能在栖息占位
和 E 各扣一次同义后果。资源事实若同时进入栖息占位与当前动机，必须
登记不同的 `consequence_id`（长期资源分布 vs 本次动机），否则编译器拒绝
该组合。

## 7. 编辑器

编辑器拆为：

1. 资源事实来源（Resource fact source）：猎物/竞争/扰动、空间、修订版本、质量；
2. 历史结构模式（History schema）：字段、范围、初值、END-CUT 增量契约；
3. 当前动机规则：优先级、输入字段、重叠检测、输出当前动机；
4. 进入机会：当前动机 → E 的离散规则；
5. 结果/HistoryDelta（Outcome/HistoryDelta）：每个结算结果的唯一 cause_id 与
   交易归属；
6. 追踪（Trace）：显示历史修订版本、当前动机、E、结果、增量和归属方。

编辑器禁止直接编辑运行时某条鱼的“当前饥饿值”作为配置；只能编辑结构模式、
初值和策略。修改历史结构模式或增量契约必须生成迁移版本。

历史快照与 `applied_transaction_ids` 必须和机会/终结结算日志（journal）使用
同一崩溃边界（crash boundary）：日志持久写入成功但进程在 END-CUT 前崩溃时，
重启只能重放未应用增量；应用记录成功但响应丢失时，重复请求必须返回相同
结果，不能再次增加饱食、能量或警戒。

## 8. 关键反例

1. 每帧读取饱食并重掷 `FORAGE`；禁止，必须机会快照。
2. 进入成功立即扣饱食，随后摄食结算再扣；禁止，消耗只归结果。
3. `wariness` 同时降低栖息占位和 E，但表达同一个“鱼不愿接近”；禁止。
4. 两个并发终结结算各自应用同一 HistoryDelta；必须 transaction_id 幂等。
5. 为方便实现给普通鱼分配持久个体 ID（persistent individual ID）；V1 默认禁止。
6. 变体（Variant）把历史结构模式扩展成物种（Species）未声明字段；必须走
   版本化结构模式/迁移。

## 9. 最小闭合结论

```text
resource fact + history snapshot
→ deterministic motive
→ one Entry offer
→ typed encounter outcome
→ one idempotent END-CUT HistoryDelta
```

资源与历史机制在结构模式、修订版本、增量归属方和迁移规则闭合前，
不应实现成一个全局 `hunger_multiplier`。
