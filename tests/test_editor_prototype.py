from pathlib import Path

def test_editor_prototype_exposes_real_authoring_workspaces():
    html=Path("editor/index.html").read_text()
    for label in ("Species", "FishMode", "Shared Catalogs", "Rule Editor", "Effective / Compiled Preview", "Affected Objects"):
        assert label in html

def test_editor_does_not_expose_runtime_controls():
    html=Path("editor/index.html").read_text()
    assert "OpportunityId" not in html and "CandidateEngagementMass" not in html and "RNG" not in html

def test_editor_backend_uses_existing_compiler():
    source=Path("editor/prototype.py").read_text()
    assert "lint_authoring" in source and "compile_authoring" in source and "/api/validate" in source
