import json
from copy import deepcopy
from pathlib import Path
import pytest
from fcf_v1.authoring import *
from fcf_v1.pre_generation import PreGenerationHarness, fixture_occurrence

DOC = json.loads(Path("authoring/bass_v0.json").read_text())


def test_bass_authoring_lints_and_compiles():
    assert lint_authoring(DOC) == []
    bundle = compile_authoring(DOC)
    assert len(bundle.contributions) == 13
    assert bundle.engagement_mode_routing_snapshot["default_mode_ref"] == "NORMAL"


def test_compiled_bundle_enters_harness():
    b = compile_authoring(DOC); r = PreGenerationHarness().resolve(fixture_occurrence(), b.contributions)
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
        if a["quality_ref"] == "Q3" and a["mode_ref"] == "ACTIVE_SPAWNING": a["share"] = 0.95
        if a["quality_ref"] == "Q3" and a["mode_ref"] == "SPAWN_GUARD": a["share"] = 0.10
    assert "OVERALLOCATED" in "; ".join(lint_authoring(d))


def test_surface_program_bindings_are_independent():
    mode = next(m for m in DOC["species"]["engagement_modes"] if m["id"] == "SPAWN_GUARD")
    assert len({mode["bake_program_ref"], mode["response_program_ref"], mode["quality_selection_program_ref"]}) == 3
