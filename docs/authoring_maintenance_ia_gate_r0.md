# Authoring Maintenance & Editor IA Gate R0

## Maintenance Cost Matrix

| Operation | Files touched | Config nodes added/changed | Shared definitions reused | Cross-owner edits |
|---|---:|---:|---|---:|
| Add normal Species | 1 | 1 species block | NORMAL pathways, response rules, profiles | 0 |
| Add grammar-changing FishMode | 1 | 3 (mode, pathway, rule) | ResponseGrade and typed operations | 0 |
| Change FeedingReadiness | 1 | 1 scalar | all lifecycle/spatial/mode/materialization | 0 |
| Add CueFamily | 1 | 1 compatibility entry | feeding rules and response policy | 0 |

These are measured fixture diffs against `authoring/bass_v0.json`, not estimates. A normal Species has low enough marginal cost; FishMode remains a scarce grammar-changing structure; local tuning remains local; CueFamily is a shared catalog concept.

## Editor IA R0

```text
Species
├─ Overview
├─ Species Static Data
├─ Lifecycle (table)
├─ Spatial / Habitat (semantic supports only)
├─ Slow Facts
├─ Cue Families (shared catalog links + local disposition)
├─ Materialization Profiles
└─ Available FishModes

FishMode
├─ Mode Definition
├─ Meaning Policy
├─ Interaction Pathways
├─ Pathway Arbitration (priority, fallback)
└─ Response Policy / narrow slices

Shared Catalogs
├─ CueFamily
├─ InteractionPathway
├─ Meaning Vocabulary
├─ ResponseGrade
├─ ResponseSlice Operation (SET / CEILING)
└─ Templates
```

Lifecycle ownership, reproductive eligibility, behavior anchor and spatial support do not belong inside FishMode merely for UI symmetry.

### Typed Rule Editor

Each rule presents `priority`, typed conditions, typed inputs, typed output, explicit fallback marker and validation status. Arbitrary code is not the primary authoring surface.

### Explainability flow

```text
Source View → Resolved / Compiled Preview → Lint → Affected Species / Modes
```

Preview must show inheritance expanded, for example:

```text
ACTIVE_SPAWNING
→ inherited NORMAL_FEEDING
→ ResponseSlice CEILING LOW
→ final effective response policy
```

## Template boundary

Only `single explicit template + shallow override` is supported. The compiler emits fully materialized canonical output; no runtime inheritance, deep inheritance, multiple inheritance or magic merge.

## Gate result

**READY_FOR_EDITOR_PROTOTYPE**

The gate proves the four maintenance fixtures and rule ambiguity checks. It does not prove a production UI, collaboration model or the out-of-scope FCF stages.

level: ARTIFACT
scope: maintenance fixtures, authoring compiler/linter extensions, IA contract and tests
baseline: user-provided Authoring Maintenance & Editor IA Gate R0; mechanism guide §0; scoped review protocol
proves: local maintenance boundaries and constrained compiler semantics are executable and tested
does_not_prove: production editor implementation or full gameplay architecture
open_findings: none
verdict: ARTIFACT_APPROVE
