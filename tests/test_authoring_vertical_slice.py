import json
from pathlib import Path
import pytest
from fcf_v1.authoring import *
from fcf_v1.pre_generation import PreGenerationHarness, fixture_occurrence

DOC=json.loads(Path("authoring/bass_v0.json").read_text())

def test_bass_authoring_lints_and_compiles():
    assert lint_authoring(DOC)==[]
    bundle=compile_authoring(DOC)
    assert len(bundle.contributions)==3

def test_compiled_bundle_enters_harness():
    b=compile_authoring(DOC); h=PreGenerationHarness(); r=h.resolve(fixture_occurrence(), b.contributions)
    assert r.entries and r.selected_basis_key

@pytest.mark.parametrize("mutator", [
    lambda d: {**d, "bad": 1},
    lambda d: {**d, "lifecycles":[{**d["lifecycles"][0],"supply_share":2}] + d["lifecycles"][1:]},
    lambda d: {**d, "species":{**d["species"],"fish_modes":[{"id":"X","pathways":["MISSING"]}]}},
    lambda d: {**d, "rules":[{**d["rules"][0],"grade":"BROKEN"}]},
])
def test_linter_rejects_contract_errors(mutator):
    assert lint_authoring(mutator(DOC))
