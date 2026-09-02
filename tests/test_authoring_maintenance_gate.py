from copy import deepcopy
from authoring.maintenance_fixtures import *
from fcf_v1.authoring import lint_authoring, compile_authoring, AuthoringError

def test_four_maintenance_operations_are_local_and_valid():
    for fn in (add_normal_species, add_grammar_mode, change_readiness, add_cue_family):
        assert lint_authoring(fn(load_base())) == []
        compile_authoring(fn(load_base()))

def test_rule_order_does_not_change_compiled_semantics():
    d=load_base(); a=compile_authoring(d)
    d["rules"]=list(reversed(d["rules"])); b=compile_authoring(d)
    assert a.response_content_bundle == b.response_content_bundle

def test_ambiguous_and_duplicate_rules_fail():
    d=load_base(); d["rules"].append({"id":"DUP","priority":10,"grade":"LOW","operation":"SET","conditions":{}})
    d["rules"].append({"id":"DUP","priority":10,"grade":"LOW","operation":"SET","conditions":{}})
    try: compile_authoring(d); assert False
    except AuthoringError as e: assert "duplicate semantic rule ID" in str(e) and "overlapping" in str(e)

def test_missing_fallback_fails():
    d=load_base(); d["rules"]=[r for r in d["rules"] if not r.get("fallback")]
    try: compile_authoring(d); assert False
    except AuthoringError as e: assert "missing required fallback" in str(e)

def test_maintenance_cost_matrix_is_explicit():
    rows=maintenance_costs(); assert len(rows)==4 and all(r["cross_owner_edits"]==0 for r in rows)

def test_template_is_single_shallow_and_fully_materialized():
    d=load_base(); out=compile_authoring(d)
    assert out.response_content_bundle["template_ref"] == "NORMAL_FEEDING_BASE"
    d["templates"]={"A":{"template_ref":"B"}}
    assert "inheritance" in " ".join(lint_authoring(d))
