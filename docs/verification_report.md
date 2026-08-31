# RC4 implementation verification report

## Executed checks

```text
python3 -m pytest -q                 70 passed
python3 -m json.tool schemas/...     valid JSON Schema document
python3 -m py_compile fcf_v1/*.py   passed
```

The tests cover:

- finite-unit entry probability and no Poisson substitution;
- randomized finite-mass conservation property sweep (100 deterministic cases);
- stable opportunity replay and trigger-once anti-reroll;
- Pending zero-reservation and no fresh roll on slot release;
- atomic single-owner reservation under concurrent retries;
- conservation and idempotent/rollback-safe settlement;
- stable lifecycle slice identity and PSU transfer;
- order-invariant capped occupancy allocation;
- deterministic motive, discrete EntryOffer, Encounter, and Contact/Hook;
- ARRIVAL producer XOR `T < 1` placement;
- DSL and Variant capability-boundary diagnostics;
- strict PopulationSlice/TraceContract namespaces, resolver interval shape, and
  Variant policy-allowlist diagnostics;
- PopulationDefinition and BehaviorProgram/Variant reference resolution, typed
  resolver `when` overlap and interval checks;
- TemperatureProfile semantic compilation: layer ranges/overlap, sample depth
  and validity, thermocline ranges, source allowlist/freshness, identity and
  SINGLE_LAYER constraints, plus rejection of non-finite physical values;
- downstream-only Hook inputs and proposal-stable Commit randomness;
- one-shot Commit resolution and settled-only slot release;
- proposal provenance/source-slice validation before ledger consumption;
- stable semantic Contact tie IDs and synchronized terminal settlement;
- executable Spawn Bass, Trout Drift, and Carp ARRIVAL closure traces.
- durable append-only Opportunity/Reservation/Settlement journal with replay
  idempotency, conflict detection, failed-write rollback, safe duplicate
  materialization rejection, and explicit startup hydrate/adopt after restart.
- cross-process append locking and multi-process journal integrity fixture;
  SQLite transactional adapter contract and engine restart/hydrate.
- production handoff `run_core_conformance` smoke runner against reference and
  SQLite-backed engines, including structured failure reporting.

## Remaining gate

This is reference-oracle evidence, not proof that a production implementation
is complete. The design surfaces (DSL, mechanisms, entity/Variant, and editor)
have received Independent Reviewer approval. The remaining gate is to
run the same fixture contract against the production runtime and validate its
cross-process storage adapter (the repository now includes a local journal and
hydrate/adopt contract), then obtain an Independent Narrow Close Review. Any
concrete MAJOR/BLOCKER must be adjudicated as a narrow revision; realism or
scope expansion belongs in V1.1.

## Production handoff acceptance contract

The final gate is satisfied only when:

1. Production supplies a `JournalAdapter` and starts from a pre-journal source
   snapshot with `hydrate_journal=True`.
2. The RC4 fixture set runs against production through an engine factory; no
   fixture is silently replaced by a mock.
3. Existing Opportunity IDs never trigger a new Entry draw, and duplicate
   Reservation/Settlement events remain idempotent across restart.
4. Two workers racing one event ID produce one append plus one identical replay;
   a differing payload is rejected as a conflict.
5. The deterministic 100-case conservation sweep passes and flagship traces
   remain explainable at stage/owner level.
6. Independent Narrow Close Review records `APPROVE` or
   `APPROVE_WITH_MINOR`; any MAJOR/BLOCKER reopens only its named owner
   contract and is adjudicated with a minimal patch.

Promotion is blocked if any item is missing. Realism or scope expansion belongs
to V1.1 and does not change this acceptance contract.
