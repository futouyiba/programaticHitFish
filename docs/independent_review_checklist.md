# 独立窄审清单（Independent Narrow Review Checklist，RC4）

本清单（checklist）是刻意对抗性（adversarial）的。审查者（Reviewer）应检查契约（contract）并运行固定样例（fixtures），不能把绿色测试当作语义正确性（semantic correctness）的充分证明。

本清单产生的所有结论（verdict）必须遵循 [`scoped_review_protocol.md`](scoped_review_protocol.md)。如果请求没有明确指定完整交付物（artifact）或里程碑基线（milestone baseline），本窄审默认使用 `PATCH`。

## 严重级别（Severity）

* **BLOCKER/MAJOR** — 守恒破坏（conservation break）、重放/重掷漏洞（replay/reroll exploit）、矛盾的概率放置（probability placement）、两种实质不同但都合法的实现、归属方双重结算（owner double-settlement），或旗舰追踪样例（flagship）需要隐藏加成（hidden bonus）。
* **MINOR** — 不造成玩法分歧（gameplay divergence）的命名、诊断（diagnostic）或完整性（completeness）问题。
* **NOTE/V1.1** — 额外真实性（realism）或范围扩张（scope expansion）。

## 审查矩阵（Review matrix）

| 范围（Area） | 攻击（Attack） | 参考实现中的证据（Evidence in reference implementation） |
|---|---|---|
| 有限质量（Finite mass） | 保留前出现遭遇候选；重复保留；终态重试（terminal retry） | `test_conservation_and_idempotent_settlement`, `test_concurrent_materialization_has_single_reservation_owner` |
| 进入概率（Entry probability） | 有限单位概率而非泊松（Poisson）；A/T/E 各自独立 | `test_canonical_finite_unit_probability_is_exactly_binomial_semantics`, `test_arrival_placement_is_xor_not_double_counted` |
| 时间身份（Temporal identity） | FPS/tick/抖动/抛竿（cast）重放；只触发一次 | `test_same_opportunity_never_rerolls_on_jitter_or_duplicate_trigger`，稳定 ID 测试 |
| Pending | 零保留；槽位释放不重新掷骰 | `test_pending_does_not_reserve_or_reroll_and_materializes_once`，保留前取消测试 |
| 生命周期（Lifecycle） | 阈值抖动下键稳定；切片转移守恒 PSU | `test_lifecycle_slice_transfer_preserves_stock_and_identity` |
| 解析器顺序（Resolver order） | 无原始丰度预筛；确定性动机/等级 | DSL 诊断与解析器测试 |
| 栖息占位（Occupancy） | 封顶 + 再分配；行序不变性 | `test_occupancy_is_order_invariant_and_conserves_distributable_mass` |
| 遭遇（Encounter） | 软难度在下游仍可见 | `test_encounter_is_deterministic_and_soft_difficulty_stays_downstream` |
| 接触/挂钩（Contact/Hook） | 仲裁稳定；挂钩只消费下游几何 | 接触与挂钩测试 |
| 配置编写（Authoring） | 非法 q/contact/priority 被拒绝；编译产物 JSON 安全 | DSL 编译器测试 |

## V1 冻结（Freeze）前必须有人明确决定的事项

1. 确认 RC4 归属方矩阵（owner matrix）没有重复的物理后果 ID。
2. 确认生产调度器持久化机会账本（Opportunity Ledger）和终结结算交易 ID，而不是只保存在进程本地（process-local）状态。
3. 确认三个旗舰追踪样例（Spawn Bass、Trout Drift、Carp Static Bait）已作为 RC4 固定样例（fixture）编写，并能分离玩家操作（player action）的影响。
4. 确认 Coding Agent 的重放/并发/性质测试运行在生产实现（production implementation）上，而不只是参考预言机（reference oracle）。

当前仓库提供参考预言机（reference oracle）和对抗性单元固定样例（adversarial unit fixtures）；它不因此声称外部独立审查者（external Independent Reviewer）已经批准整个设计。
