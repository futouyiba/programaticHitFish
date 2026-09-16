# FCF Presentation/Cue Contract Validation — Run Report

- lane: `fcf_pc_validation` — R0 `FCF-PC-BASELINE-R0-20260915` + R1 addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`
- baseline commit: `c412a6e254a86502538746d2f82a5327f7b4a1ff`
- R1 addendum sha256: `5b6f9effcf2b71873d74721bbb97a52f251980c3306a596402b292489739617b`
- pre-change regression: 210 passed / 1 skipped (R2 lane state, re-verified at branch point)
- post-change regression: 217 passed / 1 skipped (python3 -m pytest -q, 2026-09-16, after Round 2 conformance fix; 169 Current + 48 PC-specific)

## Summary

- cases: 82 (development 51, synthetic lane self-test 31)
- violations: 31
- classification counts: {"ANNOTATION_ONLY": 4, "COVERED": 49, "NEW_PRIMITIVE_REQUIRED": 1, "UNRESOLVED": 1}
- descriptor token counts: {'cue_basis': 13, 'cue_candidate_extension': 1, 'cue_not_admitted': 5}

## Findings by code

- `AFFINITY_ABSORPTION`: 1
- `AGGREGATOR_SMUGGLED`: 1
- `BAND_MAPPING_NOT_DECIDED`: 1
- `CAUSE_OWNERSHIP_CONFLICT`: 5
- `CAUSE_PROVENANCE_REQUIRED`: 2
- `COMPOSITION_IDENTITY_LEAK`: 1
- `COMPOSITION_NON_DETERMINISTIC`: 1
- `DICTIONARY_MEMBER_ADMISSION_REQUIRED`: 3
- `FISH_DEPENDENT_INPUT`: 1
- `FORBIDDEN_CUE_SEMANTICS`: 1
- `FRAME_METADATA_INVALID`: 1
- `FRAME_METADATA_MISSING`: 3
- `INVALID_PRIMARY_CLASSIFICATION`: 1
- `MODE_AXIS_FORBIDDEN`: 1
- `MODE_SPECIFIC_TARGET_TABLE`: 1
- `NON_AFFIRMATIVE_TREATED_AS_AFFINITY`: 1
- `NON_DETERMINISTIC_DESCRIPTOR`: 1
- `NOT_ADMITTED_CUE`: 5
- `SIGNATURE_NOT_VERSIONED`: 1
- `SKU_MEMORY_LEAK`: 2
- `UNKNOWN_CUE_TOKEN`: 2

## Per-case findings

### DEV-001 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-002 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- findings: none

### DEV-003 (development, bundle ``)
- classification: `ANNOTATION_ONLY` deltas=['admit presentation.chemical_signature candidate values (sparse item annotation)', 'admit PREPARED_FOOD as FeedingTargetKey dictionary member'] flags=['CHEMICAL_INTENSITY_GAP_WATCH']
- [unresolved] `DICTIONARY_MEMBER_ADMISSION_REQUIRED` @ static_target_affinity[0] — feeding_target_key 'PREPARED_FOOD' is outside this lane's test vocabulary ('SMALL_BAITFISH', 'CRUSTACEAN'); canonical FeedingTarget membership is governed by its own dictionary authority — record an admission request (R3 ruling D: CRUSTACEAN reused, nothing added) (R3 ruling D)

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
- classification: `COVERED` deltas=[] flags=['RESOLVED_BY_R3_DELTA_1']
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

### H01 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['MECHANICAL_DOMINANT_CHANNEL_REUSE']
- findings: none

### H02 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['SHORT_EVENT_TEMPORAL']
- findings: none

### H03 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['SURFACE_RELATION_REUSE']
- findings: none

### H04 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['FALL_PHASE_NO_BOTTOM_CONTACT']
- findings: none

### H05 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['REFERENCE_FRAME_RESOLVED_BY_SUPPORT_RELATIVE_RULE']
- findings: none

### H06 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['DISCRETE_CONTACT_EVENT_EXPRESSIBLE']
- findings: none

### H07 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['HISTORICAL_R2_NEW_GENERIC_RULE_REQUIRED', 'COUNTERFACTUAL_PENDING_MULTIPLICITY']
- findings: none

### H08 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['NO_LIVE_SEMANTIC_NEEDED']
- findings: none

### H09 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['MULTI_COMPONENT_HETEROGENEOUS_FACT_UNION']
- findings: none

### H10 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['LIGHT_DOUBLE_COUNT_RESOLVED_BY_EFFECTIVE_RECEIVER_RELATIVE_CUE']
- findings: none

### H11 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['ZERO_DISPLACEMENT_EXPRESSIBLE_WITHOUT_cue.displacement']
- findings: none

### H12 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['HISTORICAL_R2_NEW_PRIMITIVE_REQUIRED', 'RESOLVED_BY_R3_DELTA_1']
- findings: none

### H13 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['HISTORICAL_R2_NEW_PRIMITIVE_REQUIRED', 'RESOLVED_BY_R3_DELTA_1']
- findings: none

### H14 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['HISTORICAL_R2_ANNOTATION_ONLY', 'RESOLVED_BY_R3_DELTA_3_REUSE']
- findings: none

### H15 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['NON_FEEDING_MODE_VIA_REACTION_CHANNEL', 'POST_GEN_SCOPE_NOTE']
- findings: none

### H16 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['CHEMICAL_TYPE_BOUNDARY_WORKS']
- findings: none

### H17 (development, bundle ``)
- classification: `NEW_PRIMITIVE_REQUIRED` deltas=['cue.odor_concentration / chemical magnitude — DEFERRED / NOT_ADMITTED per R3; H17 is confirmatory only'] flags=['KNOWN_DEFERRED_CANDIDATE', 'CONFIRMATORY_ONLY_POSSIBLE_CONTAMINATION']
- findings: none

### H18 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['STRATEGY_DIFF_LIVES_OUTSIDE_PRESENTATION_SEMANTICS']
- findings: none

### HR2-01 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['DELTA1_GENERALIZES_TO_VEGETATION', 'RULING_A_NEGATIVE_SPACE_RESPECTED']
- findings: none

### HR2-02 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['DELTA1_AXIS_PRE_VISITED', 'DISCRETE_IMPULSE_NO_TEMPORAL_ENUM_NEEDED']
- findings: none

### HR2-03 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['SUBSTRATE_DESCRIPTOR_TEMPTATION_DECLINED', 'DELTA1_GENERALIZES_TO_SOFT_SUBSTRATE', 'HETEROGENEOUS_COMPONENT_UNION']
- findings: none

### HR2-04 (development, bundle ``)
- classification: `ANNOTATION_ONLY` deltas=['FeedingTarget dictionary value AMPHIBIAN (fish-neutral; canonical FeedingTarget dictionary admission process per R3 ruling D scope; CRUSTACEAN reuse is not defensible for frog)'] flags=['FEEDING_TARGET_DICTIONARY_PRESSURE', 'CRUSTACEAN_REUSE_NOT_DEFENSIBLE', 'TARGET_AMBIGUITY_ABSORBED_BY_AFFINITY']
- [unresolved] `DICTIONARY_MEMBER_ADMISSION_REQUIRED` @ static_target_affinity[0] — feeding_target_key 'AMPHIBIAN' is outside this lane's test vocabulary ('SMALL_BAITFISH', 'CRUSTACEAN'); canonical FeedingTarget membership is governed by its own dictionary authority — record an admission request (R3 ruling D: CRUSTACEAN reused, nothing added) (R3 ruling D)

### HR2-05 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['SOUND_PATTERN_BLIND_EXERCISE', 'SOUND_PATTERN_STATUS_BLIND_SUPPORTED_UTILITY']
- findings: none

### HR2-06 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['MULTI_SOURCE_HETEROGENEOUS_UNION', 'NO_RIG_IDENTITY_NEEDED', 'SEMANTIC_QUESTION_PRE_VISITED_R1']
- findings: none

### HR2-07 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['HETEROGENEOUS_COUPLED_COMPONENTS_UNION', 'ROTATION_PERIODICITY_ABSORBED_BY_VIBRATION_FREQUENCY', 'CAUSAL_COUPLING_NOT_NEEDED_FISH_SIDE']
- findings: none

### HR2-08 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['COMPONENT_INTERNAL_CONTACT_OUT_OF_CONTACT_DISTURBANCE_SCOPE', 'PROVENANCE_MECHANISM_EXERCISED']
- findings: none

### HR2-09 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['GLOW_ABSORBED_BY_EFFECTIVE_RECEIVER_RELATIVE_CONTRAST', 'NO_LIGHT_INTENSITY_PRIMITIVE_NEEDED', 'MIXED_CHANNEL_UNION']
- findings: none

### HR2-10 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['PARTIAL_UNKNOWN_EXPRESSIBLE_VIA_TYPED_BANDS', 'LIVE_PROVENANCE_AGAIN_NOT_NEEDED', 'LIVE_QUESTION_PRE_VISITED_R1', 'NIGHT_CONTEXT_PRE_EXERCISED_H10']
- findings: none

### HR2-11 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['CONTEXT_OUT_OF_LANE_GEOMETRY', 'IN_FAMILY_UNSEEN_CONFIG']
- findings: none

### HR2-12 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['SINGLE_CAUSE_DUAL_ASPECT_FORCES_SINGLE_CHANNEL_CONSUMPTION', 'PROVENANCE_MECHANISM_EXERCISED', 'KILL_SIGNAL_C_OBSERVATION_POINT']
- findings: none

### HR2-13 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['PRESSURE_FAMILIARITY_OUT_OF_LANE_SCOPE', 'R3_S3_AXIS_ATTACKED']
- findings: none

### HR2-14 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['NO_RIG_IDENTITY_NEEDED', 'HETEROGENEOUS_UNION']
- findings: none

### HR2-15 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['RECEIVER_RELATIVE_EXTENDS_TO_ACOUSTIC_MASKING', 'NO_SN_RATIO_DESCRIPTOR_NEEDED', 'UPSTREAM_DATA_READINESS_NOTE']
- findings: none

### HR2-16 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['PLUME_GEOMETRY_OUT_OF_CUE_SIDE', 'ZERO_MOTION_NEGATIVE_SPACE', 'CHEMICAL_MAGNITUDE_ECHO_CONFIRMATORY_ONLY']
- findings: none

### HR2-C1 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['CONFIRMATORY_CONTAMINATED', 'NOT_BLIND_EVIDENCE', 'MULTIPLICITY_ADMISSION_PRESSURE_REPEAT', 'CF_MULTI_1_EVIDENCE_STRENGTHENED']
- findings: none

### HR2-C2 (development, bundle ``)
- classification: `COVERED` deltas=[] flags=['POSSIBLE_CONTAMINATION', 'NOT_BLIND_EVIDENCE', 'OWNERSHIP_ROUTING_TO_WORLD_EXPOSURE', 'CHEMICAL_INTENSITY_CANDIDATE_SECOND_SCENARIO']
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
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule consumes both 'cue.visual_contrast' and its recorded cause 'turbidity' (shared cause identity; no override exists) (R0 8 / R3 B)

### SYN-13-boolean-override-removed (synthetic, bundle ``)
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule consumes both 'cue.visual_contrast' and its recorded cause 'turbidity' (shared cause identity; no override exists) (R0 8 / R3 B)

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

### SYN-18-contact-disturbance-valid (synthetic, bundle ``)
- findings: none

### SYN-19-contact-disturbance-metadata-missing (synthetic, bundle ``)
- [violation] `FRAME_METADATA_MISSING` @ cue_facts[0] — cue.contact_disturbance must record temporal_scope (duration semantics stay on existing DurationFact / temporal_scope) (R1 A2 / R3 ruling A)

### SYN-20-strategy-token-rejected (synthetic, bundle ``)
- [violation] `UNKNOWN_CUE_TOKEN` @ cue_facts[0] — 'cue.mechanical_scrape' is not in the frozen basis; needs admission (R0 9)

### SYN-21-contact-family-provenance-required (synthetic, bundle ``)
- [unresolved] `CAUSE_PROVENANCE_REQUIRED` @ response_rules[0] — rule weights ['cue.contact_disturbance', 'cue.sound_amplitude'] without cause identity for ['cue.contact_disturbance', 'cue.sound_amplitude']; declare cause_provenance to show the consumed facts stem from independent causes (R3 ruling B)

### SYN-22-multiplicity-not-admitted (synthetic, bundle ``)
- classification: `COVERED` deltas=[] flags=[]
- [violation] `NOT_ADMITTED_CUE` @ cue_facts[0] — 'cue.source_count' is NOT_ADMITTED per R2 D1; use admitted facts or file a semantic admission request (R2 D1)
- [violation] `NOT_ADMITTED_CUE` @ classification — case relying on a NOT_ADMITTED cue cannot be COVERED; use admitted facts or record a semantic admission request (R2 D1)

### SYN-23-composition-clean (synthetic, bundle ``)
- findings: none

### SYN-24-composition-violations (synthetic, bundle ``)
- [violation] `COMPOSITION_IDENTITY_LEAK` @ composition.sources[0].rig_identity — source carries forbidden identity key 'rig_identity' (R3 Delta 2)
- [violation] `COMPOSITION_NON_DETERMINISTIC` @ composition.resolver — composition resolver must be declared deterministic (R3 Delta 2)

### SYN-25-crab-dictionary-admission (synthetic, bundle ``)
- [unresolved] `DICTIONARY_MEMBER_ADMISSION_REQUIRED` @ static_target_affinity[0] — feeding_target_key 'CRAB' is outside this lane's test vocabulary ('SMALL_BAITFISH', 'CRUSTACEAN'); canonical FeedingTarget membership is governed by its own dictionary authority — record an admission request (R3 ruling D: CRUSTACEAN reused, nothing added) (R3 ruling D)

### SYN-26-contact-family-shared-cause (synthetic, bundle ``)
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule weights ['cue.contact_disturbance', 'cue.sound_amplitude'] sharing cause identity ['substrate_grind'] (R3 ruling A/B)

### SYN-27-contact-family-independent-causes (synthetic, bundle ``)
- findings: none

### SYN-28-sound-pattern-shared-cause-conflict (synthetic, bundle ``)
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule weights ['cue.contact_disturbance', 'cue.sound_pattern'] sharing cause identity ['bottom_contact_scrape'] (R3 ruling A/B)

### SYN-29-sound-pattern-independent-causes-clean (synthetic, bundle ``)
- findings: none

### SYN-30-sound-pattern-provenance-required (synthetic, bundle ``)
- [unresolved] `CAUSE_PROVENANCE_REQUIRED` @ response_rules[0] — rule weights ['cue.contact_disturbance', 'cue.sound_pattern'] without cause identity for ['cue.contact_disturbance', 'cue.sound_pattern']; declare cause_provenance to show the consumed facts stem from independent causes (R3 ruling B)

### SYN-31-acoustic-pair-shared-cause-conflict (synthetic, bundle ``)
- [violation] `CAUSE_OWNERSHIP_CONFLICT` @ response_rules[0] — rule weights ['cue.sound_amplitude', 'cue.sound_pattern'] sharing cause identity ['chug_sequence'] (R3 ruling A/B)

## Development Regression

```json
{
  "awaiting_count": 0,
  "backfilled_count": 51,
  "breaking_cases": [
    "H17"
  ],
  "chemical_intensity_gap_cases": [
    "DEV-003",
    "DEV-S5"
  ],
  "classification_distribution": {
    "ANNOTATION_ONLY": 4,
    "COVERED": 46,
    "NEW_PRIMITIVE_REQUIRED": 1
  },
  "displacement_dependent_cases": [],
  "fish_descriptor_resurfacing": "NOT_MEASURABLE_FROM_DEV_FIXTURES: DEV bundles carry fact requirements and classifications, no authored Response rules yet; monitor per R0 9 once rules exist",
  "known_dev_gap_cases": [],
  "ownership_watch_cases": [
    "DEV-S4"
  ],
  "unused_basis_cues": {}
}
```

## Open Counterfactuals (R3 Delta 2)

```json
[
  {
    "id": "CF-MULTI-1",
    "question": "When aggregate cue / target semantics are equal, is there a residual, player-relevant strategy difference between single-source and multi-source presentations that must be preserved in Response?",
    "status": "OPEN_PENDING_EVIDENCE"
  }
]
```
