from pathlib import Path


def test_editor_prototype_exposes_current_authoring_workspaces():
    html = Path("editor/index.html").read_text()
    for label in ("Species", "FishQuality", "Engagement Mode Routing", "Engagement Mode", "Surface Programs", "Effective / Compiled Preview", "Affected Objects"):
        assert label in html


def test_editor_does_not_expose_legacy_business_axes_or_runtime_controls():
    html = Path("editor/index.html").read_text()
    for forbidden in ("FishMode", "Lifecycle", "ResponseSlice", "BehaviorAnchor", "OpportunityId", "CandidateEngagementMass", "RNG"):
        assert forbidden not in html


def test_editor_backend_uses_current_compiler_outputs():
    source = Path("editor/prototype.py").read_text()
    assert "lint_authoring" in source and "compile_authoring" in source and "/api/validate" in source
    assert "engagement_mode_routing_snapshot" in source and "surface_program_bundle" in source
