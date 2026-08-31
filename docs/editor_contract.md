# FCF V1 editor / attribute authoring contract

The editor is a schema-driven tool over immutable versioned artifacts. It is
not a runtime behavior scripting surface.

## Panels and ownership

| Panel | Editable | Read-only / validation |
|---|---|---|
| Species capability | anatomy profile, sensory channels, allowed contacts, task limits | `q` change is marked **scale change** and requires recalibration review |
| Population slices | cohort and lifecycle role declarations, hysteresis/minimum hold | stable `population_slice_key`; Program is not part of identity |
| Behavior Program | occupancy rules, motive priority, EntryOffer rules, whitelisted triggers | all choices must be within Species capability |
| World-factor map | neutral fact bindings and resolver interpretation | no fish-specific World Fact; one physical consequence → one owner |
| Presentation compiler | object truth, motion/geometry and cue emission mappings | raw Item/Technique IDs cannot be fish-response authority |
| Verification trace | none | stage-by-stage inputs, outputs, owner, probability, ledger delta |

## Commands

```text
open_artifact(version_id)
edit(path, value)
validate() -> Diagnostic[]
preview(trace_fixture_id, seed, causal_cut_id) -> ExplainTrace
save_as_new_version(message, author)
compile() -> CompiledArtifact
export_review_report(version_id)
```

`edit` is transactional: a failed validation leaves the prior artifact
unchanged. `save_as_new_version` stores the complete flattened artifact, a
machine-readable diff, and diagnostics. Runtime consumes only `CompiledArtifact`
and never reads editor draft state.

## Diagnostics that block save

```text
UNKNOWN_FIELD / DUPLICATE_ID / INVALID_Q
CAPABILITY_EXPANSION
EQUAL_PRIORITY_OVERLAP
WORLD_FACT_IS_FISH_INTERPRETATION
MISSING_SETTLEMENT_OWNER / DUPLICATE_SETTLEMENT_OWNER
ARRIVAL_T_AND_UNIT_PRODUCER_CONFLICT
UNSTABLE_REEVALUATION_TRIGGER
PROGRAM_IN_SLICE_IDENTITY
```

## ExplainTrace minimum shape

```json
{
  "fixture_id": "spawn_bass_guard",
  "artifact_version": "fcf.v1:42",
  "opportunity_id": "stable-hash",
  "stages": [
    {"name": "PERCEPTION", "inputs": {}, "outputs": {"A": 0.8}, "owner": "optical_propagation"},
    {"name": "MOTIVE", "inputs": {}, "outputs": {"motive": "DEFEND"}, "owner": "guard_program"},
    {"name": "ENTRY", "inputs": {}, "outputs": {"E": 0.7, "pi": 0.56}, "owner": "defend_entry_offer"},
    {"name": "RESERVATION", "inputs": {}, "outputs": {"q": 10, "reservation_id": "..."}, "owner": "population_ledger"}
  ],
  "ledger_delta": {"actual_supply": -10, "encounter_hold": 10}
}
```

The trace is an explanatory projection of authoritative decisions. It must not
perform a second roll or mutate state.
