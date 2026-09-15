from copy import deepcopy
from authoring.maintenance_fixtures import *
from fcf_v1.authoring import lint_authoring, compile_authoring, AuthoringError


def test_four_maintenance_operations_are_local_and_valid():
    for fn in (add_normal_species, add_engagement_mode, change_readiness, add_cue_family):
        assert lint_authoring(fn(load_base())) == []
        compile_authoring(fn(load_base()))


def test_response_rule_order_does_not_change_compiled_semantics():
    d = load_base(); a = compile_authoring(d)
    d["surface_programs"]["response"][0]["rules"] = list(reversed(d["surface_programs"]["response"][0]["rules"]))
    b = compile_authoring(d)
    assert a.surface_program_bundle == b.surface_program_bundle


def test_duplicate_response_rule_ids_fail():
    d = load_base(); rules = d["surface_programs"]["response"][0]["rules"]
    rules.append({"id":"DUP","intent":"SET_RESPONSE_BAND","band":"LOW"})
    rules.append({"id":"DUP","intent":"SET_RESPONSE_BAND","band":"LOW"})
    try:
        compile_authoring(d); assert False
    except AuthoringError as e:
        assert "duplicate response rule ID" in str(e)


def test_invalid_response_intent_fails():
    d = load_base(); d["surface_programs"]["response"][0]["rules"][0]["intent"] = "CEILING"
    assert "invalid Response intent" in " ".join(lint_authoring(d))


def test_maintenance_cost_matrix_is_explicit():
    rows = maintenance_costs(); assert len(rows) == 4 and all(r["cross_owner_edits"] == 0 for r in rows)


def test_template_is_single_shallow_and_fully_materialized():
    d = load_base(); compile_authoring(d)
    d["templates"] = {"A": {"template_ref": "B"}}
    assert "inheritance" in " ".join(lint_authoring(d))
