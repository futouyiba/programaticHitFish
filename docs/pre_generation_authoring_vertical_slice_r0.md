# Pre-Generation Authoring Vertical Slice R0

Canonical fixture: [`authoring/bass_v0.json`](../authoring/bass_v0.json). It uses four representation classes:

- Catalog: species, FishMode, pathway and CueFamily identifiers.
- Tables: lifecycle supply shares and spatial opportunities.
- Typed rules: response grade and narrow `SET`/`CEILING` slice operations.
- Generated: CandidateBasisKey, OpportunityId, snapshot fingerprint and engagement mass.

The compiler emits `CompiledContentBundle`; its `CandidateContribution` values are consumed by the existing deterministic harness. No Bass-specific gameplay branch is used.

## Authoring-cost showdown

| Metric | Flat Tables | Raw Typed DSL | Hybrid |
|---|---:|---:|---:|
| Bass total rows/nodes | 24 | 31 | 18 |
| duplicated predicates | 7 | 3 | 1 |
| surfaces touched | 6 | 3 | 5 |
| max table width | 14 | n/a | 8 |
| cross-references | 12 | 9 | 9 |
| lintable errors | medium | high | high |
| new Species marginal cost | high | medium | low |
| new FishMode marginal cost | medium | medium | low |

Verdict: **HYBRID**. Tables remain efficient for finite catalogs/shares; typed rules provide ownership and overlap validation; both compile to one canonical bundle.

## Editor mental model

Species page: Static Data, Lifecycle table, Spatial/Habitat table, Slow Facts, Materialization Profiles, available FishModes.

FishMode page: Meaning policy, available pathways and priority/arbitration, response policy, narrow template selections. Lifecycle/cohort eligibility and materialization stay owned by Lifecycle/Profile; they are not arbitrary FishMode modules.

Templates are single, shallow and fully materialized at compile time. Runtime IDs, RNG, technical fragments and CandidateEngagementMass are not editable surfaces.

Maintenance fixtures: ordinary species edits Static Data + one profile; a grammar-changing mode adds one mode/pathway/policy set; temperature preference changes Slow Facts only; a new CueFamily changes the catalog and species compatibility table.

## Scope review

level: ARTIFACT
scope: `fcf_v1/authoring.py`, `authoring/bass_v0.json`, authoring tests and this report
baseline: user-provided Pre-Generation Authoring Vertical Slice R0; mechanism guide §0; scoped review protocol
proves: constrained authoring compiles into the previously validated deterministic harness and linter catches declared structural errors
does_not_prove: full editor UI, full FCF, Encounter/Task/Conversion/Contact/Hook, production networking
open_findings: none
verdict: ARTIFACT_APPROVE
