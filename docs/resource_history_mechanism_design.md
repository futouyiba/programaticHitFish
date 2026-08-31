# FCF V1 资源与鱼类历史状态机制（Design-only）

资源状态（饱食、能量、恢复债务、警戒记忆）是鱼的持久历史，不是每次
presentation 的即时 bonus。V1 先定义状态 owner、更新时机和 motive/Entry
边界，避免“饥饿”同时成为 occupancy、motive、E 和 conversion 的重复系数。

## 0. 快速阅读

**概念**：资源是世界事实；饱食、警戒、恢复和适应是 END-CUT 后持久化的
Population Slice/cohort History，不是即时 bonus。

**整体机制**：resolver 只读取 pinned World/History snapshot；Encounter/Settlement
产生 typed HistoryDelta，History/Future owner 以 transaction ID 幂等应用，下一
causal cut 才能影响 Motive、Entry 或 Lifecycle。

**配置方式**：配置 resource fact schema、History 字段/范围/初值、delta contract、
owner、migration 和 revision；Editor 不直接改运行中 Candidate 的历史值。

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

只有 World resource fact 与已结算 History 才能进入 resolver。Candidate
形成后 snapshot 这些解释；后续历史更新不回写既有 Candidate。

## 2. 状态 owner

| 状态/后果 | 唯一 owner | 更新时机 | 禁止 |
|---|---|---|---|
| 饱食/能量 | History/Future | END-CUT settlement | Entry 直接扣同一能量 |
| 警戒/记忆 | History/Future | END-CUT observation | 每帧读取并重掷 motive |
| 当前资源可用性 | Population/Occupancy | causal-cut fact | 作为鱼的个体饥饿记忆 |
| Prospective motive | Motive resolver | Opportunity 一次 | 当作 Candidate 存在 |
| Entry offer | BehaviorProgram | Opportunity 一次 | Conversion 再扣“想吃” |
| 追击成本/恢复债务 | Encounter task 产出；History/Future 唯一应用/持久化 | task outcome + END-CUT | Occupancy 再扣同一体能 |

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

V1 在普通节点内使用 exchangeable mass：不创建持久 individual fish ID。
只有当产品明确要求个体记忆时，才另行设计个体 identity、存储和 privacy
边界；不能在 V1 中隐式引入。

## 4. 输入与输出逻辑

### 4.1 Resource fact

```text
resource_state = {
  prey_density,
  competition_level,
  disturbance_level,
  resource_revision
}
```

它描述节点，不描述某条鱼“饿不饿”。节点资源影响 Occupancy 或
BehaviorProgram 的 motive priority，不能直接写成 universal bite multiplier。

### 4.2 Prospective motive

```text
motive = resolve_motive(
  program_policy,
  resource_state,
  history_snapshot,
  presentation_truth
)
```

V1 motive resolver 是确定性的优先级/规则决策；若多个规则同优先级且重叠，
DSL 编译拒绝。`FORAGE` 表示“本次有觅食解释”，不表示鱼已消耗资源。

### 4.3 Entry offer

```text
E = entry_offer(program_policy, motive, presentation_truth)
```

History 可以作为 rule input，但同一 satiation/wariness consequence 只能在
Entry offer 中被消费一次。Entry 成功不自动减少 satiation；资源消耗要等
实际 downstream outcome 并在 END-CUT 结算。

### 4.4 Encounter / settlement

实际接触、摄食、失败或逃逸由 Encounter/Settlement 输出 typed outcome：

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

同一 outcome 只能产生一个 HistoryDelta。Settlement 重试不得重复应用 delta；
必须以 transaction_id 幂等。

## 5. 历史更新与 causal cuts

```text
cut start: read immutable HistoryCell revision N
→ resolve motive / Entry / Encounter from snapshot
→ collect typed outcomes
→ END-CUT atomically apply deltas if revision still N
→ revision N+1
```

Encounter task 只生成 typed `HistoryDelta`；History/Future 是唯一应用、持久
化和恢复该 delta 的 owner。并发 outcome 使用 deterministic merge（例如按
transaction_id 排序后合并），并维护持久的 `applied_transaction_ids` 集合：
同一 transaction_id + 相同 delta 是幂等 replay；同一 transaction_id + 不同
delta 必须拒绝为 conflict。冲突时拒绝旧 revision，而不是静默覆盖。历史
更新不会重新打开已消费的 Opportunity，也不会产生第二次 Entry roll。

## 6. 与环境机制的关系

| 环境事实/状态 | 可以影响 | 不可以直接影响 |
|---|---|---|
| 温度/DO/流速 | task profile、occupancy、lifecycle | 同一 recovery debt 再扣 E |
| 光照/浑浊度 | A_visual、感官 task | 饱食/警戒直接改变 |
| 节点资源 fact | occupancy 或 motive rule input | 伪造个体历史 |
| satiation/wariness history | motive/Entry rule input | 重新分配 PSU 或改变 Species capability |

如果“资源少”和“鱼很饱”都导致 `FORAGE` 下降，必须说明一个是 node fact、
一个是 history state，并由同一个 motive rule 一次性解释；不能在 Occupancy
和 E 各扣一次同义后果。Resource fact 若同时进入 Occupancy 与 motive，必须
登记不同的 `consequence_id`（长期资源分布 vs 本次动机），否则编译器拒绝
该组合。

## 7. 编辑器

编辑器拆为：

1. Resource fact source：prey/competition/disturbance、空间、revision、quality；
2. History schema：字段、范围、初值、END-CUT delta contract；
3. Motive rules：优先级、输入字段、重叠检测、输出 motive；
4. Entry offers：motive → E 的离散规则；
5. Outcome/HistoryDelta：每个结算结果的唯一 cause_id 与 transaction 归属；
6. Trace：显示 history revision、motive、E、outcome、delta 和 owner。

编辑器禁止直接编辑运行时某条鱼的“当前饥饿值”作为配置；只能编辑 schema、
初值和 policy。修改 history schema 或 delta contract 必须生成 migration 版本。

History snapshot 与 `applied_transaction_ids` 必须和 Opportunity/Settlement
journal 使用同一 crash boundary：journal durable write 成功但进程在 END-CUT
前崩溃时，重启只能重放未应用 delta；应用记录成功但响应丢失时，重复请求
必须返回相同结果，不能再次增加饱食、能量或警戒。

## 8. 关键反例

1. 每帧读取 satiation 并重掷 `FORAGE`；禁止，必须 Opportunity snapshot。
2. Entry 成功立即扣 satiation，随后摄食 settlement 再扣；禁止，消耗只归 outcome。
3. `wariness` 同时降低 Occupancy 和 E，但表达同一个“鱼不愿接近”；禁止。
4. 两个并发 settlement 各自应用同一 HistoryDelta；必须 transaction_id 幂等。
5. 为方便实现给普通鱼分配 persistent individual ID；V1 默认禁止。
6. Variant 把 History schema 扩展成 Species 未声明字段；必须走版本化 schema/migration。

## 9. 最小闭合结论

```text
resource fact + history snapshot
→ deterministic motive
→ one Entry offer
→ typed encounter outcome
→ one idempotent END-CUT HistoryDelta
```

资源与历史机制在 schema、revision、delta owner 和 migration 规则闭合前，
不应实现成一个全局 `hunger_multiplier`。
