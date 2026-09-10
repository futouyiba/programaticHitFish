# Independent Narrow Review Checklist (RC4)

本 checklist 是刻意 adversarial 的。Reviewer 应检查 contract 并运行 fixtures，不能把绿色测试当作 semantic correctness 的充分证明。

本 checklist 产生的所有 verdict 必须遵循 [`scoped_review_protocol.md`](scoped_review_protocol.md)。如果请求没有明确指定完整 artifact 或 milestone baseline，本窄审默认使用 `PATCH`。

## 严重级别（Severity）

* **BLOCKER/MAJOR** — conservation break、replay/reroll exploit、矛盾的 probability placement、两种实质不同但都合法的实现、owner double-settlement，或 flagship 需要 hidden bonus。
* **MINOR** — 不造成 gameplay divergence 的命名、diagnostic 或 completeness 问题。
* **NOTE/V1.1** — 额外 realism 或 scope expansion。

## Review matrix（审核矩阵）

| Area | Attack | Evidence in reference implementation |
|---|---|---|
| Finite mass | Candidate before reserve; duplicate reservation; terminal retry | `test_conservation_and_idempotent_settlement`, `test_concurrent_materialization_has_single_reservation_owner` |
| Entry probability | finite-unit probability, not Poisson; A/T/E distinct | `test_canonical_finite_unit_probability_is_exactly_binomial_semantics`, `test_arrival_placement_is_xor_not_double_counted` |
| Temporal identity | FPS/tick/jitter/cast replay; trigger once | `test_same_opportunity_never_rerolls_on_jitter_or_duplicate_trigger`, stable ID test |
| Pending | zero reservation; slot release no fresh roll | `test_pending_does_not_reserve_or_reroll_and_materializes_once`, cancel-before-reserve test |
| Lifecycle | threshold jitter stable key; slice transfer conserves PSU | `test_lifecycle_slice_transfer_preserves_stock_and_identity` |
| Resolver order | no raw abundance preselection; deterministic motive/grade | DSL diagnostics and resolver tests |
| Occupancy | cap + redistribute, row-order invariance | `test_occupancy_is_order_invariant_and_conserves_distributable_mass` |
| Encounter | soft task difficulty remains visible downstream | `test_encounter_is_deterministic_and_soft_difficulty_stays_downstream` |
| Contact/Hook | arbitration stable; Hook consumes only downstream geometry | contact and hook tests |
| Authoring | invalid q/contact/priority rejected; compiled artifact JSON-safe | DSL compiler tests |

## V1 Freeze 前必须有人明确决定的事项

1. 确认 RC4 owner matrix 没有重复的 physical consequence ID。
2. 确认 production scheduler 持久化 Opportunity Ledger 和 settlement transaction ID，而不是只保存在 process-local 状态。
3. 确认三个 flagship trace（Spawn Bass、Trout Drift、Carp Static Bait）已作为 RC4 fixture 编写，并能分离 player action 的影响。
4. 确认 Coding Agent 的 replay/concurrency/property 测试运行在 production implementation 上，而不只是 reference oracle。

当前 repository 提供 reference oracle 和 adversarial unit fixtures；它不因此声称 external Independent Reviewer 已经批准整个设计。
