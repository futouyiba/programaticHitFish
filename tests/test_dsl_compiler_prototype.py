import json
from copy import deepcopy

import pytest

from fcf_v1 import ArtifactStore, CompiledArtifact, DSLCompileError, DSL_CONTRACT_0_3_4_0, compile_artifact


def minimal_artifact():
    return {
        "schema_version": "fcf.v1",
        "species": {
            "id": "bass",
            "population_id": "bass",
            "q": 10,
            "anatomy_profile": "x",
            "sensory_channels": ["visual"],
            "allowed_contacts": ["BITE_REMOVE"],
            "history_schema": "h",
            "capability_limits": {"tasks": ["FORAGE"]},
        },
        "programs": [{
            "id": "p",
            "slice_role": "NORMAL",
            "motive_priority": ["FORAGE"],
            "tasks": ["FORAGE"],
            "contact_types": ["BITE_REMOVE"],
            "occupancy": [],
            "entry_offers": {"FORAGE": {"base": "NORMAL"}},
        }],
        "settlement_owners": [
            {"physical_consequence_id": "cue", "owner": "PERCEPTION"}
        ],
        "trace_contract": {
            "version": "trace:v1",
            "required_stages": ["ENTRY"],
            "include_revisions": True,
        },
    }


def test_compiled_artifact_is_immutable_json_safe_and_deterministic():
    raw = minimal_artifact()
    compiled = compile_artifact(raw, source_path="example.json", input_revision="r1")
    repeated = compile_artifact(deepcopy(raw), source_path="example.json", input_revision="r1")

    assert isinstance(compiled, CompiledArtifact)
    assert compiled.semantic_fingerprint == repeated.semantic_fingerprint
    assert compiled["source_path"] == "example.json"
    assert compiled["input_revision"] == "r1"
    json.dumps(compiled, sort_keys=True)
    with pytest.raises(TypeError):
        compiled["species"]["q"] = 2
    with pytest.raises(TypeError):
        compiled["programs"] += ()
    raw["species"]["q"] = 1
    assert compiled["species"]["q"] == 10


def test_rule_capability_owner_and_forbidden_execution_checks_fail_closed():
    raw = minimal_artifact()
    raw["resolver_rules"] = [{
        "rule_id": "r",
        "priority": 1,
        "requires": ["UNKNOWN_TASK"],
        "then": {"script": "return 1"},
        "consequence_id": "cue",
        "owner": "ENTRY",
    }]
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(raw)
    codes = {diagnostic.code for diagnostic in exc.value.diagnostics}
    assert {"MISSING_REFERENCE", "UNSUPPORTED_EXECUTION", "OWNER_MISMATCH"} <= codes


def test_nested_unknown_fields_and_equal_priority_overlap_are_rejected():
    raw = minimal_artifact()
    raw["programs"][0]["occupancy"] = [{"node_tag": "open", "grade": "GOOD", "bogus": True}]
    raw["resolver_rules"] = [
        {
            "rule_id": "a",
            "priority": 1,
            "when": {"fact": "water_temperature_c", "gte": 10},
            "then": {},
            "consequence_id": "cue",
            "owner": "PERCEPTION",
            "effective_interval": {"start": 0, "end": 10, "unit": "s", "clock": "SIM"},
        },
        {
            "rule_id": "b",
            "priority": 1,
            "when": {"fact": "water_temperature_c", "gte": 10},
            "then": {},
            "consequence_id": "cue",
            "owner": "PERCEPTION",
            "effective_interval": {"start": 10, "end": 20, "unit": "s", "clock": "SIM"},
        },
    ]
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(raw)
    codes = {diagnostic.code for diagnostic in exc.value.diagnostics}
    assert "UNKNOWN_FIELD" in codes
    assert "EQUAL_PRIORITY_OVERLAP" not in codes


def strict_artifact():
    with open("examples/dsl_0_3_4_0_minimal.json", encoding="utf-8") as handle:
        return json.load(handle)


def test_strict_contract_requires_provenance_and_emits_indexes():
    raw = strict_artifact()
    compiled = compile_artifact(raw, contract=DSL_CONTRACT_0_3_4_0, source_path="canonical.json", input_revision="r1")
    assert compiled["compiler_contract"] == DSL_CONTRACT_0_3_4_0
    assert tuple(compiled["reference_index"]["program_ids"]) == ("forage_program",)
    assert compiled["runtime_view"]["rules_by_owner"]["ENTRY"][0]["rule_id"] == "warm_entry"
    assert compiled.semantic_fingerprint == compile_artifact(raw, contract=DSL_CONTRACT_0_3_4_0, source_path="other.json", input_revision="r1").semantic_fingerprint
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(raw, contract=DSL_CONTRACT_0_3_4_0, source_path="canonical.json")
    assert "INPUT_REVISION_REQUIRED" in {item.code for item in exc.value.diagnostics}


@pytest.mark.parametrize("mutator, code", [
    (lambda raw: raw["resolver_rules"][0].pop("when"), "RULE_WHEN_REQUIRED"),
    (lambda raw: raw["resolver_rules"][0].update({"consequence_id": "missing"}), "MISSING_SETTLEMENT_OWNER"),
    (lambda raw: raw["resolver_rules"][0]["when"].update({"bogus": 1}), "PREDICATE_OPERATOR"),
    (lambda raw: raw["resolver_rules"][0].update({"then": {"entry_grade": "NORMAL", "motive": "FORAGE"}}), "RULE_THEN_TYPED"),
])
def test_strict_contract_rejects_ambiguous_or_unresolved_semantics(mutator, code):
    raw = strict_artifact()
    mutator(raw)
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(raw, contract=DSL_CONTRACT_0_3_4_0, source_path="canonical.json", input_revision="r1")
    assert code in {item.code for item in exc.value.diagnostics}


def test_editor_strict_store_saves_compiled_fingerprint():
    store = ArtifactStore(strict_artifact(), contract=DSL_CONTRACT_0_3_4_0, source_path="canonical.json", input_revision="r1")
    version = store.save_as_new_version("strict prototype")
    assert version.version_id == version.artifact["semantic_fingerprint"]
    assert version.artifact["compiler_contract"] == DSL_CONTRACT_0_3_4_0
