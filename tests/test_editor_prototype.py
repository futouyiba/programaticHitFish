import json
import runpy
from copy import deepcopy
from pathlib import Path


DOC = json.loads(Path("authoring/bass_v0.json").read_text())


def test_editor_prototype_exposes_current_human_gate_workspaces():
    html = Path("editor/index.html").read_text()
    for label in (
        "Species Shared",
        "FishQuality",
        "Engagement Mode",
        "Bake Program Editor",
        "Engagement Mode Routing",
        "Resolved Preview + Provenance",
        "Routing Diagnostics",
        "Affected Objects",
        "Reset Saved Baseline",
        "Load T5 OVERALLOCATED",
    ):
        assert label in html


def test_editor_does_not_expose_legacy_business_axes_or_runtime_controls():
    html = Path("editor/index.html").read_text()
    for forbidden in ("FishMode", "Lifecycle", "ResponseSlice", "BehaviorAnchor", "OpportunityId", "CandidateEngagementMass", "RNG"):
        assert forbidden not in html


def test_component_inspector_is_generated_from_component_definitions():
    html = Path("editor/index.html").read_text()
    assert "componentDefsForOwner" in html
    assert "draft.component_definitions" in html
    assert "allowed_owners" in html
    assert "Generated from ComponentDefinition owner, type and constraints" in html

    # Workspace renderers must not hardcode the current fixture's component keys.
    species_body = html.split("function showSpecies(){", 1)[1].split("function setSpeciesParam", 1)[0]
    quality_body = html.split("function showQuality(){", 1)[1].split("function setQualityOverride", 1)[0]
    assert "structure_affinity" not in species_body
    assert "prey_size_preference" not in species_body
    assert "prey_size_preference" not in quality_body


def test_routing_workspace_discloses_fixture_scope_boundary():
    html = Path("editor/index.html").read_text()
    assert "Human fixture slice: explicit allocation + diagnostics" in html
    assert "Full ConditionAtom / RuleSet authoring remains outside 0.3.4.0 executable scope" in html


def test_editor_backend_uses_current_compiler_resolver_and_reset_contract():
    source = Path("editor/prototype.py").read_text()
    for required in (
        "lint_authoring",
        "compile_authoring",
        "resolve_bake_subject",
        "/api/inspect",
        "/api/validate",
        "/api/reset",
        "resolved_bake_subjects",
        "engagement_mode_routing_snapshot",
        "surface_program_bundle",
    ):
        assert required in source


def test_inspection_returns_provenance_even_for_invalid_draft():
    module = runpy.run_path("editor/prototype.py")
    inspect_doc = module["inspect_doc"]
    baseline = inspect_doc(deepcopy(DOC))
    assert baseline["valid"]
    resolved = baseline["resolved_bake_subjects"]["Q5::NORMAL"]
    assert resolved["params"]["prey_size_preference"]["source"] == "FISH_QUALITY"
    assert resolved["params"]["water_temperature"]["status"] == "FACT"

    broken = deepcopy(DOC)
    normal = next(m for m in broken["species"]["engagement_modes"] if m["id"] == "NORMAL")
    normal["bake_program_ref"] = "BAKE_ALT"
    report = inspect_doc(broken)
    assert not report["valid"]
    resolved = report["resolved_bake_subjects"]["Q5::NORMAL"]
    assert resolved["params"]["ambush_threshold"]["status"] == "MISSING"
    assert resolved["orphaned"][0]["key"] == "normal_bias"


def test_routing_diagnostics_surface_overallocation():
    module = runpy.run_path("editor/prototype.py")
    broken = deepcopy(DOC)
    for allocation in broken["engagement_mode_routing"]["allocations"]:
        if allocation["quality_ref"] == "Q3" and allocation["mode_ref"] == "ACTIVE_SPAWNING":
            allocation["share"] = 0.95
    report = module["inspect_doc"](broken)
    assert any(x.startswith("OVERALLOCATED: Q3") for x in report["routing_diagnostics"])


def test_reset_path_is_deterministic_without_touching_repository(tmp_path):
    module = runpy.run_path("editor/prototype.py")
    temp_config = tmp_path / "bass.json"
    mutated = deepcopy(DOC)
    mutated["species"]["shared_params"]["structure_affinity"] = 0.1
    temp_config.write_text(json.dumps(mutated))

    reset_config = module["reset_config"]
    reset_config.__globals__["CONFIG"] = temp_config
    reset_config.__globals__["BASELINE"] = deepcopy(DOC)
    first = reset_config()
    second = reset_config()
    assert first == DOC == second
    assert json.loads(temp_config.read_text()) == DOC
