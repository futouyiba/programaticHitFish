# FCF Presentation/Cue Contract Validation — Run Report

- lane: `fcf_pc_validation` — R0 `FCF-PC-BASELINE-R0-20260915` + R1 addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`
- baseline commit: `9c2beebd2e2b1f5757223149e9c65f16bb200841`
- R1 addendum sha256: `5b6f9effcf2b71873d74721bbb97a52f251980c3306a596402b292489739617b`
- pre-change regression: 169 passed / 1 skipped on 9c2beebd (measured 2026-09-16; NOT assumed from prior 166/1 — full inventory in baseline_regression below)
- post-change regression: 210 passed / 1 skipped (python3 -m pytest -q, 2026-09-16; 9c2 baseline 169/1 + 41 PC-specific tests in tests/test_pc_validation.py)

## Summary

- cases: 32 (development 15, synthetic lane self-test 17)
- violations: 21
- classification counts: {"ANNOTATION_ONLY": 3, "COVERED": 13, "UNRESOLVED": 2}
- descriptor token counts: {'cue_basis': 12, 'cue_candidate_extension': 1, 'cue_not_admitted': 1}

## Findings by code

- `AFFINITY_ABSORPTION`: 1
- `AGGREGATOR_SMUGGLED`: 1
- `BAND_MAPPING_NOT_DECIDED`: 1
- `CAUSE_OWNERSHIP_CONFLICT`: 1
- `FISH_DEPENDENT_INPUT`: 1
- `FORBIDDEN_CUE_SEMANTICS`: 1
- `FRAME_METADATA_INVALID`: 1
- `FRAME_METADATA_MISSING`: 2
- `INVALID_PRIMARY_CLASSIFICATION`: 1
- `MODE_AXIS_FORBIDDEN`: 1
- `MODE_SPECIFIC_TARGET_TABLE`: 1
- `NON_AFFIRMATIVE_TREATED_AS_AFFINITY`: 1
- `NON_DETERMINISTIC_DESCRIPTOR`: 1
- `NOT_ADMITTED_CUE`: 3
- `SIGNATURE_NOT_VERSIONED`: 1
- `SKU_MEMORY_LEAK`: 2
- `UNKNOWN_CUE_TOKEN`: 1

## Per-case findings

### DEV-001 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-002 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-003 (development, bundle ``)
- classification: `ANNOTATION_ONLY` deltas=['admit presentation.chemical_signature candidate values (sparse item annotation)', 'admit PREPARED_FOOD as FeedingTargetKey dictionary member'] flags=['CHEMICAL_INTENSITY_GAP_WATCH']
- findings: none

### DEV-004 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-005 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-006 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-007 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-008 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-009 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-010 (development, bundle ``)
- classification: `UNRESOLVED` deltas=['D3 question: is relation.bottom + ordinary admitted motion facts sufficient for the bottom-drag strategy the product needs; if not, is the missing piece a continuous-contact physical cue, a temporal summary, or another reusable primitive (do NOT add mechanical_scrape / continuous_drag / bottom_scrape from this case alone)'] flags=['KNOWN_DEV_GAP_CONTINUOUS_BOTTOM_CONTACT_MECHANICAL_CAUSE']
- findings: none

### DEV-S1 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-S2 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-S3 (development, bundle ``)
- classification: `ANNOTATION_ONLY` deltas=['admit presentation.prey_stage candidate values (Enum member admission)'] flags=[]
- findings: none

### DEV-S4 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['LINT_WATCH_DOUBLE_COUNT']
- findings: none

### DEV-S5 (development, bundle ``)
- classification: `ANNOTATION_ONLY` deltas=['admit presentation.chemical_signature candidate values'] flags=['CHEMICAL_INTENSITY_GAP_WATCH']
- findings: none

### SYN-01-clean-bundle (synthetic, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### SYN-02-frame-metadata-missing (synthetic, bundle ``)
- [violation] `FRAME_METADATA_MISSING` @ cue_facts[0] — cue.speed must record reference_frame explicitly (R1 A2)
- [violation] `FRAME_METADATA_MISSING` @ cue_facts[0] — cue.speed must record temporal_scope / summary_semantics (R1 A2)

### SYN-03-vertical-motion-frame-invalid (synthetic, bundle ``)
- [violation] `FRAME_METADATA_INVALID` @ cue_facts[0] — vertical_motion may only use the gravity/world-vertical semantic (R1 A2)

### SYN-04-displacement-not-admitted-blocks-covered (synthetic, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- [violation] `NOT_ADMITTED_CUE` @ cue_facts[0] — 'cue.displacement' is NOT_ADMITTED per R2 D1; use admitted facts or file a semantic admission request (R2 D1)
- [violation] `NOT_ADMITTED_CUE` @ classification — case relying on a NOT_ADMITTED cue cannot be COVERED; use admitted facts or record a semantic admission request (R2 D1)

### SYN-05-fish-dependent-resolver (synthetic, bundle ``)
- [violation] `FISH_DEPENDENT_INPUT` @ resolvers[0].inputs — resolver reads 'species_preference' (R0 2.1 / R1 A1)

### SYN-06-forbidden-vocabulary (synthetic, bundle ``)
- [violation] `FORBIDDEN_CUE_SEMANTICS` @ cue_facts[0] — 'injuredness' is forbidden vocabulary (R0 3.2 boundary / R0 7)
- [violation] `UNKNOWN_CUE_TOKEN` @ cue_facts[1] — 'cue.reaction_bait_grade' is not in the frozen basis; needs admission (R0 9)

### SYN-07-affinity-mode-axis (synthetic, bundle ``)
- [violation] `MODE_AXIS_FORBIDDEN` @ static_target_affinity[0] — affinity key contains 'engagement_mode'; v1 axis is fixed to Species x FeedingTargetKey (R1 A3)
- [violation] `AFFINITY_ABSORPTION` @ static_target_affinity[0] — affinity entry contains 'motion_quality'; motion/drift/flash/vibration fit must stay outside the relation (R0 4)

### SYN-08-mode-specific-dynamic-target-table (synthetic, bundle ``)
- [violation] `MODE_SPECIFIC_TARGET_TABLE` @ dynamic_feeding_preference[0] — dynamic preference entry is Mode-keyed per target; forbidden auto-copy (R1 A3)

### SYN-09-typed-zero-target (synthetic, bundle ``)
- [violation] `NON_AFFIRMATIVE_TREATED_AS_AFFINITY` @ target_resolution — UNKNOWN must not be mapped to an affinity value (R1 B2)
- [violation] `BAND_MAPPING_NOT_DECIDED` @ target_resolution — typed status -> ResponseBand mapping is open this round (R1 B2 / R0 13)

### SYN-10-sku-memory-signature (synthetic, bundle ``)
- [violation] `SKU_MEMORY_LEAK` @ cue_signature.facts.sku — signature contains forbidden identity key 'sku' (R1 B1)
- [violation] `SKU_MEMORY_LEAK` @ cue_signature.facts.ui_action — signature contains forbidden identity key 'ui_action' (R1 B1)

### SYN-11-unversioned-signature (synthetic, bundle ``)
- [violation] `SIGNATURE_NOT_VERSIONED` @ cue_signature — CueSignature must carry a signature_version (R1 B1)

### SYN-12-cause-ownership-conflict (synthetic, bundle ``)
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule consumes both 'cue.visual_contrast' and its recorded cause 'turbidity' without CAUSE_JUSTIFIED (R0 8)

### SYN-13-cause-justified-clears (synthetic, bundle ``)
- findings: none

### SYN-14-aggregator-smuggled (synthetic, bundle ``)
- [violation] `AGGREGATOR_SMUGGLED` @ resolvers[0] — 'max' aggregation of hypotheses is deliberately OPEN; record UNRESOLVED instead (R0 4)

### SYN-15-nondeterministic-descriptor (synthetic, bundle ``)
- [violation] `NON_DETERMINISTIC_DESCRIPTOR` @ derived_descriptors[0].inputs — derived descriptor reads 'species_preference' (R1 A4)

### SYN-16-invalid-classification-record (synthetic, bundle ``)
- classification: `MOSTLY_COVERED` deltas=[] flags=[]
- [violation] `INVALID_PRIMARY_CLASSIFICATION` @ classification — primary_classification 'MOSTLY_COVERED' not in vocabulary (R1 A4)

### SYN-17-displacement-admission-request-path (synthetic, bundle ``)
- classification: `UNRESOLVED` deltas=['admission request for a displacement-family concept (net spatial displacement / path length / ...) per R2 D1'] flags=[]
- [violation] `NOT_ADMITTED_CUE` @ cue_facts[0] — 'cue.displacement' is NOT_ADMITTED per R2 D1; use admitted facts or file a semantic admission request (R2 D1)

## Development Regression

```json
{
  "awaiting_count": 0,
  "backfilled_count": 15,
  "breaking_cases": [
    "DEV-010"
  ],
  "chemical_intensity_gap_cases": [
    "DEV-003",
    "DEV-S5"
  ],
  "classification_distribution": {
    "ANNOTATION_ONLY": 3,
    "COVERED": 11,
    "UNRESOLVED": 1
  },
  "displacement_dependent_cases": [],
  "fish_descriptor_resurfacing": "NOT_MEASURABLE_FROM_DEV_FIXTURES: DEV bundles carry fact requirements and classifications, no authored Response rules yet; monitor per R0 9 once rules exist",
  "known_dev_gap_cases": [
    "DEV-010"
  ],
  "ownership_watch_cases": [
    "DEV-S4"
  ],
  "unused_basis_cues": {
    "cue.sound_pattern": "UNEXERCISED_BY_CURRENT_DEVSET"
  }
}
```
