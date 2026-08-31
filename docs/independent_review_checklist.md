# Independent Narrow Review Checklist (RC4)

This checklist is deliberately adversarial. A reviewer should inspect the
contract and run the fixtures without treating a green test suite as proof of
semantic correctness.

## Severity

* **BLOCKER/MAJOR** — conservation break, replay/reroll exploit, contradictory
  probability placement, two materially different legal implementations,
  owner double-settlement, or a flagship that needs a hidden bonus.
* **MINOR** — naming/diagnostic/completeness issue with no gameplay divergence.
* **NOTE/V1.1** — extra realism or scope expansion.

## Review matrix

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

## Required human decisions before V1 Freeze

1. Confirm the RC4 owner matrix has no duplicate physical consequence IDs.
2. Confirm the production scheduler persists the Opportunity Ledger and
   settlement transaction IDs, rather than keeping them process-local.
3. Confirm the three flagship traces (Spawn Bass, Trout Drift, Carp Static Bait)
   are authored as RC4 fixtures with player-action separability.
4. Confirm Coding Agent replay/concurrency/property runs against the production
   implementation, not only this reference oracle.

The current repository provides a reference oracle and adversarial unit
fixtures. It does not claim that an external Independent Reviewer has already
approved the design.
