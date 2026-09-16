"""Presentation/Cue contract validation lane tests (FCF-PC-BASELINE-R0 + R1 addendum).

Every assertion cites the contract clause it enforces.  Synthetic fixtures
exercise validator behavior only; development-set fixtures stay structural
until backfilled from 中鱼库 / 推导表.
"""
import json
from pathlib import Path

from fcf_v1.pc_validation import (
    CUE_BASIS, CONTACT_CAUSE_FAMILY, HoldoutError, HoldoutRegistry,
    check_composition_resolver, counterfactual_summary,
    check_aggregation_smuggling, check_cause_ownership, check_classification,
    check_cue_signature, check_cue_vocabulary, check_derived_descriptor,
    check_dynamic_feeding_preference, check_fish_independence,
    check_kinematic_metadata, check_presentation_descriptors,
    check_static_target_affinity, check_target_resolution,
    cue_signature_identity, development_regression_summary, run_cases,
    validate_bundle,
)

FIXTURES = Path(__file__).resolve().parent.parent / "pc_validation" / "fixtures"


def _codes(findings):
    return [f.code for f in findings]


def _load(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


# --- A1 / R0 2.1 fish-independence != geometry-independence -----------------

def test_species_preference_input_is_violation():
    assert _codes(check_fish_independence({"inputs": ["species_preference"]}, "r")) == ["FISH_DEPENDENT_INPUT"]


def test_geometry_reference_inputs_are_legal():
    assert check_fish_independence(
        {"inputs": ["support_relative_distance", "support_relative_angle", "turbidity", "flow"]}, "r"
    ) == []


# --- A2 kinematic metadata ----------------------------------------------------

def test_speed_family_requires_frame_metadata():
    assert _codes(check_kinematic_metadata([{"name": "cue.speed"}], "c")) == [
        "FRAME_METADATA_MISSING", "FRAME_METADATA_MISSING"]


def test_declared_local_water_frame_passes():
    assert check_kinematic_metadata(
        [{"name": "cue.speed", "reference_frame": "LOCAL_WATER", "temporal_scope": "1.0s"}], "c") == []


def test_ground_frame_is_equally_legal_frame_choice_is_not_implied_by_lane():
    # A2: the lane must not pick a universal frame; both explicit choices validate.
    assert check_kinematic_metadata(
        [{"name": "cue.speed", "reference_frame": "GROUND", "temporal_scope": "1.0s"}], "c") == []


def test_pause_duration_exempt_from_frame_requirement():
    assert check_kinematic_metadata([{"name": "cue.pause_duration"}], "c") == []


def test_vertical_motion_only_world_vertical():
    assert _codes(check_kinematic_metadata(
        [{"name": "cue.vertical_motion", "reference_frame": "LOCAL_WATER"}], "c")) == ["FRAME_METADATA_INVALID"]
    assert check_kinematic_metadata(
        [{"name": "cue.vertical_motion", "reference_frame": "WORLD_VERTICAL"}], "c") == []


def test_not_admitted_cue_reliance_blocks_covered_classification():
    # R2 D1: cue.displacement is NOT_ADMITTED; a COVERED claim relying on it is a violation
    record = {"primary_classification": "COVERED", "requested_deltas": [], "flags": [],
              "relied_upon": ["cue.displacement"]}
    assert _codes(check_classification(record, "c")) == ["NOT_ADMITTED_CUE"]


def test_not_admitted_reliance_ok_as_unresolved_with_admission_request():
    record = {"primary_classification": "UNRESOLVED",
              "requested_deltas": ["admission request for a displacement-family concept per R2 D1"],
              "flags": [], "relied_upon": ["cue.displacement"]}
    assert check_classification(record, "c") == []


def test_not_admitted_cue_rejected_at_vocabulary_level():
    assert _codes(check_cue_vocabulary([{"name": "cue.displacement"}], "c")) == ["NOT_ADMITTED_CUE"]


# --- vocabulary admission -----------------------------------------------------

def test_unknown_cue_token_requires_admission():
    assert "UNKNOWN_CUE_TOKEN" in _codes(check_cue_vocabulary([{"name": "cue.reaction_grade"}], "c"))


def test_all_basis_tokens_accepted():
    assert check_cue_vocabulary([{"name": n} for n in CUE_BASIS], "c") == []


def test_forbidden_cue_semantics_rejected():
    assert _codes(check_cue_vocabulary([{"name": "injuredness"}], "c")) == ["FORBIDDEN_CUE_SEMANTICS"]


def test_forbidden_presentation_fields_rejected():
    assert _codes(check_presentation_descriptors([{"name": "presentation.injured_prey"}], "d")) == \
        ["FORBIDDEN_PRESENTATION_FIELD"]
    assert _codes(check_presentation_descriptors([{"name": "presentation.attractive_to_bass"}], "d")) == \
        ["FORBIDDEN_PRESENTATION_FIELD"]


def test_sku_alias_descriptor_rejected():
    assert "SKU_ALIAS_DESCRIPTOR" in _codes(
        check_presentation_descriptors([{"name": "presentation.rapala_product_123"}], "d"))


# --- A3 feeding target axes ---------------------------------------------------

def test_affinity_rejects_mode_axis():
    assert _codes(check_static_target_affinity(
        [{"species": "Bass", "engagement_mode": "NORMAL_FEEDING", "feeding_target_key": "CRUSTACEAN"}],
        "a")) == ["MODE_AXIS_FORBIDDEN"]


def test_affinity_species_target_axis_passes():
    assert check_static_target_affinity(
        [{"species": "Bass", "feeding_target_key": "SMALL_BAITFISH", "affinity": "BEST"}], "a") == []


def test_affinity_absorbing_motion_quality_rejected():
    assert "AFFINITY_ABSORPTION" in _codes(
        check_static_target_affinity([{"species": "Bass", "feeding_target_key": "WORM_LIKE_FOOD",
                                       "drift_quality": "GOOD"}], "a"))


def test_dynamic_preference_must_not_become_mode_target_table():
    assert _codes(check_dynamic_feeding_preference(
        [{"species": "Bass", "engagement_mode_target_ranking": {"NORMAL_FEEDING": ["SMALL_BAITFISH"]}}],
        "dp")) == ["MODE_SPECIFIC_TARGET_TABLE"]


# --- B2 typed zero-target -----------------------------------------------------

def test_no_supported_target_is_typed_and_clean():
    assert check_target_resolution({"status": "NO_SUPPORTED_TARGET"}, "t") == []


def test_unknown_mapped_to_affinity_rejected():
    assert "NON_AFFIRMATIVE_TREATED_AS_AFFINITY" in _codes(
        check_target_resolution({"status": "UNKNOWN", "affinity": "NONE"}, "t"))


def test_band_mapping_not_decided_this_round():
    assert "BAND_MAPPING_NOT_DECIDED" in _codes(
        check_target_resolution({"status": "HYPOTHESES", "response_band": "HIGH"}, "t"))


def test_untyped_status_rejected():
    assert _codes(check_target_resolution({"status": "ZERO"}, "t")) == ["UNTYPED_TARGET_STATUS"]


# --- B1 CueSignature ----------------------------------------------------------

def test_signature_rejects_sku_memory():
    assert "SKU_MEMORY_LEAK" in _codes(check_cue_signature(
        {"signature_version": "v0", "facts": {"sku": "XRAP-10"}}, "s"))


def test_signature_rejects_unadmitted_source():
    assert "SIGNATURE_UNADMITTED_SOURCE" in _codes(check_cue_signature(
        {"signature_version": "v0", "facts": {"world_state": "W172"}}, "s"))


def test_signature_requires_version():
    assert _codes(check_cue_signature({"facts": {"cue.speed": "MID"}}, "s")) == ["SIGNATURE_NOT_VERSIONED"]


def test_two_skus_same_facts_share_familiarity_identity():
    a = {"signature_version": "pc-sig-v0", "facts": {"cue.speed": "MID", "cue.visual_contrast": "HIGH"}}
    b = {"signature_version": "pc-sig-v0", "facts": {"cue.visual_contrast": "HIGH", "cue.speed": "MID"}}
    assert cue_signature_identity(a) == cue_signature_identity(b)
    c = {"signature_version": "pc-sig-v0", "facts": {"cue.speed": "FAST", "cue.visual_contrast": "HIGH"}}
    assert cue_signature_identity(a) != cue_signature_identity(c)


# --- A4 classification protocol ----------------------------------------------

def test_classification_record_shape_enforced():
    assert _codes(check_classification({"primary_classification": "MOSTLY_COVERED"}, "c")) == \
        ["INVALID_PRIMARY_CLASSIFICATION"]
    assert check_classification({"primary_classification": "COVERED", "requested_deltas": [],
                                 "flags": []}, "c") == []


# --- R0 8 cause ownership -----------------------------------------------------

def test_double_count_conflict_detected():
    provenance = {"cue.visual_contrast": ["turbidity", "background"]}
    rule = {"rule_id": "r1", "consumes": ["cue.visual_contrast", "turbidity"]}
    assert _codes(check_cause_ownership([rule], provenance, "rules")) == ["CAUSE_OWNERSHIP_CONFLICT"]


def test_cause_justified_declaration_clears_conflict():
    provenance = {"cue.visual_contrast": ["turbidity"]}
    rule = {"rule_id": "r2", "consumes": ["cue.visual_contrast", "turbidity"],
            "cause_justified": "independent range-gating reason recorded"}
    assert check_cause_ownership([rule], provenance, "rules") == []


# --- R0 4 open aggregation ----------------------------------------------------

def test_aggregator_smuggling_rejected():
    assert _codes(check_aggregation_smuggling([{"multi_target_aggregator": "noisy_or"}], "r")) == \
        ["AGGREGATOR_SMUGGLED"]
    assert check_aggregation_smuggling([{"multi_target_aggregator": None}], "r") == []


# --- A4 determinism -----------------------------------------------------------

def test_nondeterministic_descriptor_rejected():
    assert _codes(check_derived_descriptor({"inputs": ["response"]}, "d")) == \
        ["NON_DETERMINISTIC_DESCRIPTOR"]
    assert check_derived_descriptor({"inputs": ["cue.speed", "cue.apparent_size"]}, "d") == []


# --- holdout gate (R0 12) -----------------------------------------------------

def test_holdout_registry_must_stay_empty():
    HoldoutRegistry().validate()  # empty + no provenance is the only legal in-repo state


def test_holdout_with_real_cases_raises():
    try:
        HoldoutRegistry(real_cases=("HOLDOUT-001",)).validate()
        raise AssertionError("expected HOLDOUT_NOT_EMPTY")
    except HoldoutError as exc:
        assert "HOLDOUT_NOT_EMPTY" in str(exc)


def test_holdout_payload_requires_full_provenance():
    try:
        HoldoutRegistry(provenance={"sample_agent": "x"}).validate()
        raise AssertionError("expected HOLDOUT_MISSING_PROVENANCE")
    except HoldoutError as exc:
        assert "HOLDOUT_MISSING_PROVENANCE" in str(exc)


def test_repo_holdout_fixture_is_sealed_empty():
    registry = HoldoutRegistry.from_mapping(_load("holdout_registry.json"))
    assert registry.real_cases == () and registry.provenance is None
    registry.validate()


# --- lane over fixtures -------------------------------------------------------

def test_selftest_cases_produce_exactly_expected_finding_codes():
    for case in _load("lane_selftest_cases.json")["cases"]:
        got = sorted(_codes(validate_bundle(case["bundle"])))
        assert got == sorted(case["expected_codes"]), case["case_id"]


def test_dev_regression_fixture_backfilled_and_classified():
    cases = _load("devset_r3_dev.json")["cases"]
    assert len(cases) == 15  # DEV-001..010 + five strategy stories (incl. Owner-added Walleye)
    report = run_cases(cases, baseline={})
    assert report.violations == 0  # backfilled DEV content must be contract-clean
    for case, result in zip(cases, report.case_results):
        assert case["backfill_status"] == "BACKFILLED", case["case_id"]
        assert case["provenance"]["notion"], case["case_id"]  # every case cites its sources
        assert result.classification is not None, case["case_id"]
    distribution = development_regression_summary(report, cases)["classification_distribution"]
    assert distribution == {"ANNOTATION_ONLY": 3, "COVERED": 12}
    by_id = {c["case_id"]: c for c in cases}
    assert by_id["DEV-010"]["bundle"]["classification"]["primary_classification"] == "COVERED"  # R3 Delta 1
    assert "RESOLVED_BY_R3_DELTA_1" in by_id["DEV-010"]["bundle"]["classification"]["flags"]
    for case in cases:  # D1: not used as a fact and not relied upon anywhere
        bundle = case.get("bundle", {})
        assert all(f["name"] != "cue.displacement" for f in bundle.get("cue_facts", [])), case["case_id"]
        assert "cue.displacement" not in (bundle.get("classification", {}).get("relied_upon") or []), case["case_id"]


def test_dev_r3_outcome_per_owner_ruling():
    cases = _load("devset_r3_dev.json")["cases"]
    summary = development_regression_summary(run_cases(cases, baseline={}), cases)
    assert summary["breaking_cases"] == []
    assert summary["known_dev_gap_cases"] == []  # gap closed by R3 Delta 1
    assert summary["displacement_dependent_cases"] == []
    assert summary["chemical_intensity_gap_cases"] == ["DEV-003", "DEV-S5"]  # D4 unchanged
    assert summary["ownership_watch_cases"] == ["DEV-S4"]  # D5 unchanged
    # within the original 15-case file alone sound_pattern is still unexercised;
    # across the combined Development set (this file + 18 round-1 cases) H10 exercises it
    assert summary["unused_basis_cues"] == {"cue.sound_pattern": "UNEXERCISED_BY_CURRENT_DEVSET"}
    combined = cases + _load("holdout_round1_devset.json")["cases"]
    assert development_regression_summary(run_cases(combined, baseline={}), combined)["unused_basis_cues"] == {}

def test_round1_cases_now_development():
    cases = _load("holdout_round1_devset.json")["cases"]
    assert len(cases) == 18
    report = run_cases(cases, baseline={})
    assert report.violations == 0
    summary = development_regression_summary(report, cases)
    assert summary["classification_distribution"] == {"COVERED": 17, "NEW_PRIMITIVE_REQUIRED": 1}
    by_id = {c["case_id"]: c for c in cases}
    for cid in ("H12", "H13"):
        assert by_id[cid]["bundle"]["classification"]["primary_classification"] == "COVERED"  # Delta 1
        assert by_id[cid]["historical_classification_under_r2"] == "NEW_PRIMITIVE_REQUIRED"
    assert by_id["H07"]["bundle"]["classification"]["flags"] == [
        "HISTORICAL_R2_NEW_GENERIC_RULE_REQUIRED", "COUNTERFACTUAL_PENDING_MULTIPLICITY"]
    assert by_id["H14"]["bundle"]["classification"]["primary_classification"] == "COVERED"  # Delta 3 reuse
    assert by_id["H17"]["bundle"]["classification"]["primary_classification"] == "NEW_PRIMITIVE_REQUIRED"
    for case in cases:  # no ResponseBand numbers anywhere in round-1 material
        assert "response_band" not in case.get("bundle", {}).get("target_resolution", {})

def test_counterfactual_cf_multi_1_open():
    cfs = _load("counterfactuals.json")["counterfactuals"]
    assert counterfactual_summary(cfs) == [{"id": "CF-MULTI-1", "status": "OPEN_PENDING_EVIDENCE",
        "question": cfs[0]["question"]}]
    assert cfs[0]["snapshots"]["single"] == cfs[0]["snapshots"]["multi_composed_equal"]  # aggregates controlled equal
    assert "YES" in cfs[0]["decision_rule"] and "NO" in cfs[0]["decision_rule"]

def test_contact_cause_family_and_new_validators():
    # Delta 1: family guard
    rule = {"rule_id": "r", "consumes": ["cue.surface_contact_disturbance", "cue.vibration_amplitude"]}
    assert _codes(check_cause_ownership([rule], {}, "rules")) == ["CAUSE_OWNERSHIP_CONFLICT"]
    ok = {"rule_id": "r2", "consumes": ["cue.surface_contact_disturbance", "cue.vibration_amplitude"],
          "cause_justified": "vibration carries the blade's own rotary cause; disturbance carries the substrate plume"}
    assert check_cause_ownership([ok], {}, "rules") == []
    assert set(CONTACT_CAUSE_FAMILY) == {"cue.surface_contact_disturbance", "cue.vibration_amplitude",
                                         "cue.vibration_frequency", "cue.sound_amplitude"}
    # Delta 2: composition validator
    good = {"sources": [{"cue.flash": "HIGH"}], "resolver": {"deterministic": True, "inputs": ["cue.flash"]}}
    assert check_composition_resolver(good, "c") == []
    bad = {"sources": [{"sku": "X"}], "resolver": {"deterministic": False, "inputs": ["species_preference"]}}
    assert _codes(check_composition_resolver(bad, "c")) == ["COMPOSITION_IDENTITY_LEAK",
                                                            "COMPOSITION_NON_DETERMINISTIC",
                                                            "COMPOSITION_FISH_DEPENDENT"]


def test_dev_fixture_never_asserts_responseband_numbers():
    for case in _load("devset_r3_dev.json")["cases"]:
        assert "response_band" not in case.get("bundle", {}).get("target_resolution", {})


def test_report_json_and_markdown_shapes():
    cases = (_load("devset_r3_dev.json")["cases"]
             + _load("holdout_round1_devset.json")["cases"]
             + _load("lane_selftest_cases.json")["cases"])
    report = run_cases(cases, baseline={"baseline_commit": "c412a6e",
                                        "r1_addendum_sha256": "test-hash"})
    data = json.loads(report.to_json())
    assert data["summary"]["cases"] == len(cases)
    assert data["summary"]["synthetic_cases"] == 25
    assert data["summary"]["development_cases"] == 33  # 15 original + 18 round-1
    assert data["summary"]["findings_by_code"].get("AWAITING_BACKFILL", 0) == 0
    assert data["summary"]["findings_by_code"]["FRAME_METADATA_MISSING"] == 4  # SYN-02 x2 + SYN-19 x2
    assert data["summary"]["findings_by_code"]["NOT_ADMITTED_CUE"] == 5  # SYN-04 x2 + SYN-17 + SYN-22 x2
    assert data["summary"]["findings_by_code"]["DICTIONARY_MEMBER_ADMISSION_REQUIRED"] == 2  # DEV-003 + SYN-25
    # 12 + 17 dev COVERED + 3 synthetic COVERED (SYN-01/04/22), 3 dev ANNOTATION_ONLY,
    # 1 synthetic UNRESOLVED (SYN-17), 1 NEW_PRIMITIVE (H17)
    assert data["summary"]["classification_counts"] == \
        {"ANNOTATION_ONLY": 3, "COVERED": 32, "NEW_PRIMITIVE_REQUIRED": 1, "UNRESOLVED": 1}
    assert data["summary"]["descriptor_token_counts"] == \
        {"cue_basis": 13, "cue_candidate_extension": 1, "cue_not_admitted": 5}
    md = report.to_markdown()
    assert "FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16" in md
    assert "c412a6e" in md and "test-hash" in md
