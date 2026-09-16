import json
from copy import deepcopy
from pathlib import Path

import pytest

from fcf_v1.authoring import *
from fcf_v1.pre_generation import PreGenerationHarness, fixture_occurrence

DOC = json.loads(Path("authoring/bass_v0.json").read_text())


def _mode(doc, mode_id):
    return next(m for m in doc["species"]["engagement_modes"] if m["id"] == mode_id)


def _program(doc, program_id):
    return next(p for p in doc["surface_programs"]["bake"] if p["id"] == program_id)


def _quality(doc, quality_id):
    return next(q for q in doc["fish_qualities"] if q["id"] == quality_id)


def test_bass_authoring_lints_and_compiles():
    assert lint_authoring(DOC) == []
    bundle = compile_authoring(DOC)
    assert len(bundle.contributions) == 13
    assert bundle.engagement_mode_routing_snapshot["default_mode_ref"] == "NORMAL"
    assert set(bundle.resolved_mode_bake_configs) == {"NORMAL", "ACTIVE_SPAWNING", "SPAWN_GUARD"}
    assert bundle.resolved_mode_bake_configs["NORMAL"]["identity"] == {
        "species": "Bass",
        "engagement_mode": "NORMAL",
    }


def test_factorized_bake_keeps_qxm_selection_rows_without_qxm_bake_subjects():
    bundle = compile_authoring(DOC)
    assert len(bundle.resolved_mode_bake_configs) == 3
    assert len(bundle.contributions) == 13
    assert all("fish_quality" not in resolved["identity"] for resolved in bundle.resolved_mode_bake_configs.values())
    assert {c.fish_quality for c in bundle.contributions} == {"Q1", "Q2", "Q3", "Q4", "Q5"}


def test_compiled_bundle_enters_harness():
    b = compile_authoring(DOC)
    r = PreGenerationHarness().resolve(fixture_occurrence(), b.contributions)
    assert len(r.entries) == 5 and r.selected_basis_key


def test_default_share_is_derived_inside_each_quality_bucket():
    b = compile_authoring(DOC)
    shares = {(x["quality_ref"], x["mode_ref"]): x["share"] for x in b.engagement_mode_routing_snapshot["shares"]}
    assert shares[("Q1", "NORMAL")] == 1.0
    assert shares[("Q3", "ACTIVE_SPAWNING")] == 0.20
    assert shares[("Q3", "SPAWN_GUARD")] == 0.10
    assert shares[("Q3", "NORMAL")] == pytest.approx(0.70)


@pytest.mark.parametrize("mutator, expected", [
    (lambda d: {**d, "bad": 1}, "unknown field"),
    (lambda d: {**d, "species": {**d["species"], "default_engagement_mode_ref": "MISSING"}}, "DefaultEngagementModeRef"),
    (lambda d: {**d, "engagement_mode_routing": {**d["engagement_mode_routing"], "allocations": d["engagement_mode_routing"]["allocations"] + [{"quality_ref":"Q3","mode_ref":"ACTIVE_SPAWNING","share":0.8}]}}, "duplicate ModeAllocation"),
])
def test_linter_rejects_contract_errors(mutator, expected):
    assert expected in "; ".join(lint_authoring(mutator(deepcopy(DOC))))


def test_overallocated_quality_bucket_is_invalid():
    d = deepcopy(DOC)
    for a in d["engagement_mode_routing"]["allocations"]:
        if a["quality_ref"] == "Q3" and a["mode_ref"] == "ACTIVE_SPAWNING":
            a["share"] = 0.95
        if a["quality_ref"] == "Q3" and a["mode_ref"] == "SPAWN_GUARD":
            a["share"] = 0.10
    assert "OVERALLOCATED" in "; ".join(lint_authoring(d))


def test_disjoint_overlap_contract_fails_closed_without_eligibility_layer():
    d = deepcopy(DOC)
    d["engagement_mode_routing"]["overlap_contract"] = "REQUIRE_DISJOINT_ELIGIBILITY"
    errors = "; ".join(lint_authoring(d))
    assert "UNSUPPORTED_ALLOCATION_OVERLAP_CONTRACT" in errors
    with pytest.raises(AuthoringError):
        compile_authoring(d)


def test_surface_program_bindings_are_independent():
    mode = _mode(DOC, "SPAWN_GUARD")
    assert len({mode["bake_program_ref"], mode["response_program_ref"], mode["quality_selection_program_ref"]}) == 3


def test_mode_level_resolved_preview_preserves_owner_provenance():
    r = resolve_mode_bake_config(DOC, "NORMAL", {"water_temperature": 22.0})
    assert r["identity"] == {"species": "Bass", "engagement_mode": "NORMAL"}
    assert r["params"]["structure_affinity"]["status"] == "INHERITED"
    assert r["params"]["structure_affinity"]["source"] == "SPECIES_SHARED"
    assert r["params"]["normal_bias"]["source"] == "ENGAGEMENT_MODE"
    assert r["params"]["daylight_sensitivity"]["source"] == "SHARED_PROFILE"
    assert r["params"]["daylight_sensitivity"]["source_ref"] == "BASS_BASE_PROFILE"
    assert r["params"]["water_temperature"]["status"] == "FACT"
    assert r["params"]["water_temperature"]["source"] == "ENVIRONMENT_FACT"
    assert r["program_logic"]["source"] == "PROGRAM_OWNED_LOGIC"


def test_fish_quality_stable_facts_are_independent_from_bake_provenance():
    q5 = _quality(DOC, "Q5")
    assert q5["stable_params"]["body_length_cm"] == 58.0
    r = resolve_mode_bake_config(DOC, "NORMAL", {"water_temperature": 22.0})
    assert "body_length_cm" not in r["params"]
    assert all(entry.get("source") != "FISH_QUALITY" for entry in r["params"].values())


def test_environment_fact_is_runtime_required_not_authoring_missing():
    r = resolve_mode_bake_config(DOC, "NORMAL", environment_facts=None)
    assert r["params"]["water_temperature"]["status"] == "RUNTIME_FACT_REQUIRED"
    assert not any("water_temperature" in e and "MISSING_PARAM" in e for e in lint_authoring(DOC))


def test_program_switch_exposes_inherited_missing_and_orphaned_then_repairs():
    d = deepcopy(DOC)
    normal = _mode(d, "NORMAL")
    normal["bake_program_ref"] = "BAKE_ALT"

    r = resolve_mode_bake_config(d, "NORMAL", {"water_temperature": 22.0})
    assert r["params"]["structure_affinity"]["status"] == "INHERITED"
    assert r["params"]["ambush_threshold"]["status"] == "MISSING"
    assert [x["key"] for x in r["orphaned"]] == ["normal_bias"]
    errors = lint_authoring(d)
    assert any("MISSING_PARAM: NORMAL/ambush_threshold" in e for e in errors)
    assert any("ORPHANED_PARAM: NORMAL/normal_bias" in e for e in errors)

    del normal["bake_params"]["normal_bias"]
    normal["bake_params"]["ambush_threshold"] = 0.4
    assert lint_authoring(d) == []
    assert compile_authoring(d).resolved_mode_bake_configs["NORMAL"]["program_ref"] == "BAKE_ALT"


def test_fish_quality_cannot_bind_surface_program():
    d = deepcopy(DOC)
    d["fish_qualities"][0]["bake_program_ref"] = "BAKE_NORMAL"
    assert "FishQuality cannot bind Surface Program" in "; ".join(lint_authoring(d))


def test_fish_quality_generic_bake_override_is_rejected():
    d = deepcopy(DOC)
    _quality(d, "Q5")["narrow_param_overrides"] = {"structure_affinity": 1.2}
    assert "FishQuality generic RequiredParam override is forbidden" in "; ".join(lint_authoring(d))


def test_bake_required_param_schema_cannot_read_fish_quality():
    d = deepcopy(DOC)
    spec = _program(d, "BAKE_NORMAL")["required_params"][0]
    spec["owner_policy"] = ["FISH_QUALITY", "SPECIES_SHARED"]
    d["component_definitions"]["structure_affinity"]["allowed_owners"].append("FISH_QUALITY")
    assert "Bake RequiredParamSchema cannot use FISH_QUALITY owner" in "; ".join(lint_authoring(d))


def test_required_param_schema_cannot_smuggle_control_flow():
    d = deepcopy(DOC)
    _program(d, "BAKE_ALT")["required_params"][0]["step_order"] = 3
    assert "RequiredParamSchema control flow forbidden" in "; ".join(lint_authoring(d))


def test_bake_dsl_error_is_line_localized_and_structure_lens_is_derived():
    d = deepcopy(DOC)
    _program(d, "BAKE_NORMAL")["dsl"] = "let weight = 1.0\nreturn ???"
    assert "Bake DSL line 2: invalid expression" in "; ".join(lint_authoring(d))

    compiled = compile_bake_dsl(_program(DOC, "BAKE_NORMAL")["dsl"])
    kinds = [x["kind"] for x in compiled["structure_lens"]]
    assert "RULE" in kinds and "GATE" in kinds and "EARLY_RETURN" in kinds and kinds[-1] == "RETURN"
