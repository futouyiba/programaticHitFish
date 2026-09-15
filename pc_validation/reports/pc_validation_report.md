# FCF Presentation/Cue Contract Validation — Run Report

- lane: `fcf_pc_validation` — R0 `FCF-PC-BASELINE-R0-20260915` + R1 addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`
- baseline commit: `0e4ea3d`
- R1 addendum sha256: `5b6f9effcf2b71873d74721bbb97a52f251980c3306a596402b292489739617b`
- pre-change regression: 126 passed / 0 failed (python3 -m pytest -q, 2026-09-16). NOTE: the Notion gate record for the Current Contract rebase states 166 passed / 1 skipped; the delta is recorded as open question PC-OPEN-01 and was NOT explained away.
- post-change regression: 164 passed / 0 failed (python3 -m pytest -q, 2026-09-16; = pre-change 126 + 38 new pc_validation lane tests)

## Summary

- cases: 26 (development 10, synthetic lane self-test 16)
- violations: 18
- classification counts: {"COVERED": 2}
- descriptor token counts: {'cue_basis': 13, 'cue_candidate_extension': 1, 'cue_provisional': 1}

## Findings by code

- `AFFINITY_ABSORPTION`: 1
- `AGGREGATOR_SMUGGLED`: 1
- `AWAITING_BACKFILL`: 10
- `BAND_MAPPING_NOT_DECIDED`: 1
- `CAUSE_OWNERSHIP_CONFLICT`: 1
- `DISPLACEMENT_PROVISIONAL`: 1
- `FISH_DEPENDENT_INPUT`: 1
- `FORBIDDEN_CUE_SEMANTICS`: 1
- `FRAME_METADATA_INVALID`: 1
- `FRAME_METADATA_MISSING`: 2
- `INVALID_PRIMARY_CLASSIFICATION`: 1
- `MODE_AXIS_FORBIDDEN`: 1
- `MODE_SPECIFIC_TARGET_TABLE`: 1
- `NON_AFFIRMATIVE_TREATED_AS_AFFINITY`: 1
- `NON_DETERMINISTIC_DESCRIPTOR`: 1
- `SIGNATURE_NOT_VERSIONED`: 1
- `SKU_MEMORY_LEAK`: 2
- `UNKNOWN_CUE_TOKEN`: 1

## Per-case findings

### DEV-001 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-001 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-002 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-002 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-003 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-003 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-004 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-004 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-005 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-005 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-006 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-006 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-007 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-007 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-008 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-008 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-009 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-009 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### DEV-010 (development, bundle ``)
- [info] `AWAITING_BACKFILL` @ DEV-010 — expectations/inputs not yet backfilled from 中鱼库/推导表; no semantics may be invented locally (DEVSET-REGISTRY-R0 / AGENTS.md)

### SYN-01-clean-bundle (synthetic, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### SYN-02-frame-metadata-missing (synthetic, bundle ``)
- [violation] `FRAME_METADATA_MISSING` @ cue_facts[0] — cue.speed must record reference_frame explicitly (R1 A2)
- [violation] `FRAME_METADATA_MISSING` @ cue_facts[0] — cue.speed must record temporal_scope / summary_semantics (R1 A2)

### SYN-03-vertical-motion-frame-invalid (synthetic, bundle ``)
- [violation] `FRAME_METADATA_INVALID` @ cue_facts[0] — vertical_motion may only use the gravity/world-vertical semantic (R1 A2)

### SYN-04-displacement-provisional-blocks-covered (synthetic, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- [unresolved] `DISPLACEMENT_PROVISIONAL` @ classification — case relying on cue.displacement cannot be COVERED before its summary semantics are adjudicated (R1 A2)

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

