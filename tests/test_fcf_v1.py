import pytest

from fcf_v1 import (
    ContactIntent,
    ContactType,
    EntryGrade,
    EntryMotive,
    EntryOpportunity,
    FCFEngine,
    PopulationSource,
    SettlementKind,
    DSLCompileError,
    SliceAllocator,
    SliceKey,
    compile_artifact,
    EncounterState,
    allocate_occupancy,
    encounter_step,
    hook_compatibility,
    resolve_entry_offer,
    resolve_motive,
    validate_arrival_placement,
    entry_trace,
    ArtifactStore,
    DurableJournal,
    SQLiteJournal,
    JournalConflict,
    run_core_conformance,
    compile_temperature_profile,
)
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import random


def _journal_process_worker(path, prefix):
    journal = DurableJournal(path)
    for i in range(10):
        journal.append_once(f"{prefix}-{i}", "TEST", {"i": i})


def _journal_same_id_worker(path, barrier, queue):
    journal = DurableJournal(path)
    barrier.wait(10)
    try:
        queue.put(journal.append_once("same-id", "TEST", {"value": 1}))
    except Exception as exc:
        queue.put(type(exc).__name__)


def _journal_conflict_worker(path, barrier, queue, value):
    journal = DurableJournal(path)
    barrier.wait(10)
    try:
        queue.put(journal.append_once("conflict-id", "TEST", {"value": value}))
    except Exception as exc:
        queue.put(type(exc).__name__)


def _sqlite_same_id_worker(path, barrier, queue):
    journal = SQLiteJournal(path)
    barrier.wait(10)
    try:
        queue.put(journal.append_once("sqlite-same", "TEST", {"value": 1}))
    except Exception as exc:
        queue.put(type(exc).__name__)
    finally:
        journal.close()




def source(actual=10.0, q=10.0, source_id="s1"):
    return PopulationSource(source_id, "slice", actual, q)


def opportunity(oid="o1", kind="FIRST_ACCESS"):
    return EntryOpportunity(oid, "scope", "slice", "s1", kind)


def test_canonical_finite_unit_probability_is_exactly_binomial_semantics():
    # The hash draw is deterministic; across many independent opportunity IDs
    # the empirical rate should approach π=.9 rather than 1-exp(-.9).
    successes = 0
    trials = 1000
    for i in range(trials):
        engine = FCFEngine([source()])
        proposals = engine.form_proposals(
            opportunity(f"o{i}"),
            accessible_fraction=1,
            temporal_factor=1,
            entry_grade=EntryGrade.VERY_STRONG,
            motive=EntryMotive.FORAGE,
        )
        successes += len(proposals)
    assert 0.85 < successes / trials < 0.95


def test_randomized_finite_mass_conservation_property():
    rng = random.Random(20260831)
    for index in range(100):
        q = float(rng.randint(1, 7))
        initial = float(rng.randint(1, 50))
        engine = FCFEngine([source(actual=initial, q=q)], detailed_capacity=100)
        before = engine.ledger_total()
        proposals = engine.form_proposals(
            opportunity(f"property-{index}"),
            accessible_fraction=rng.random(), temporal_factor=rng.random(),
            entry_grade=rng.choice(list(EntryGrade)), motive=EntryMotive.FORAGE,
            eligible_units=rng.randint(0, 20),
        )
        for proposal in proposals:
            candidate = engine.materialize(proposal)
            if candidate is not None:
                engine.settle(candidate.candidate_id, SettlementKind.RETURN)
        assert engine.ledger_total() == pytest.approx(before)
        assert engine.accounting_total() == pytest.approx(before)


def test_core_conformance_runner_accepts_reference_engine():
    report = run_core_conformance(lambda: FCFEngine([source(actual=10)], detailed_capacity=10))
    assert report.passed
    assert {check.name for check in report.checks} >= {
        "opportunity_replay_no_reroll", "finite_entry_and_settlement"
    }


def test_core_conformance_runner_accepts_sqlite_backed_engine(tmp_path):
    path = str(tmp_path / "conformance.sqlite")

    def factory():
        return FCFEngine([source(actual=10)], detailed_capacity=10,
                         journal=SQLiteJournal(path))

    report = run_core_conformance(factory)
    assert report.passed


def test_core_conformance_runner_reports_engine_failure():
    class BrokenEngine:
        def accounting_total(self):
            return 0.0

        def form_proposals(self, *args, **kwargs):
            raise RuntimeError("storage unavailable")

    report = run_core_conformance(BrokenEngine)
    assert not report.passed
    assert "RuntimeError" in report.checks[-1].detail
    assert '"passed":false' in report.to_json()


def test_same_opportunity_never_rerolls_on_jitter_or_duplicate_trigger():
    engine = FCFEngine([source()])
    first = engine.form_proposals(
        opportunity("o1"), accessible_fraction=.5, temporal_factor=1,
        entry_grade=EntryGrade.NORMAL, motive=EntryMotive.FORAGE,
    )
    second = engine.form_proposals(
        opportunity("o1"), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    assert second == []
    reevaluate = EntryOpportunity("o2", "scope", "slice", "s1", "SEMANTIC_REEVALUATION", "pause")
    engine.form_proposals(reevaluate, accessible_fraction=1, temporal_factor=1,
                          entry_grade=EntryGrade.NORMAL, motive=EntryMotive.FORAGE)
    assert engine.form_proposals(reevaluate, accessible_fraction=1, temporal_factor=1,
                                 entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE) == []
    record = engine.opportunity_record(opportunity("o1"))
    assert record["opportunity_id"] == "o1"
    assert record["result_summary"]["entry_probability"] == .4 * .5


def test_pending_does_not_reserve_or_reroll_and_materializes_once():
    engine = FCFEngine([PopulationSource("s1", "slice", 20, 10)], detailed_capacity=0)
    proposals = engine.form_proposals(
        opportunity(), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    assert proposals
    for p in proposals:
        assert engine.materialize(p) is None
    assert engine.sources["s1"].actual_supply == 20
    engine.detailed_capacity = 1
    made = engine.open_slot()
    assert len(made) == 1
    assert engine.sources["s1"].actual_supply == 10
    assert len(engine.pending) == len(proposals) - 1


def test_conservation_and_idempotent_settlement():
    engine = FCFEngine([source()])
    before = engine.ledger_total()
    proposals = engine.form_proposals(
        opportunity(), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    candidate = engine.materialize(proposals[0])
    assert candidate is not None
    assert engine.ledger_total() == before
    engine.settle(candidate.candidate_id, SettlementKind.RETURN_WARY)
    assert engine.ledger_total() == before


def test_invalid_terminal_reason_cannot_partially_settle():
    engine = FCFEngine([source()])
    before = engine.ledger_total()
    proposal = engine.form_proposals(
        opportunity("bad-settle"), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )[0]
    candidate = engine.materialize(proposal)
    held = engine.sources["s1"].encounter_hold
    with pytest.raises(ValueError):
        engine.settle(candidate.candidate_id, "UNKNOWN")
    assert engine.sources["s1"].encounter_hold == held
    engine.settle(candidate.candidate_id, SettlementKind.RETURN_WARY)
    assert engine.ledger_total() == before


def test_remove_stock_decreases_active_stock_but_preserves_audit_accounting():
    engine = FCFEngine([source()])
    before_active = engine.ledger_total()
    before_accounting = engine.accounting_total()
    proposal = engine.form_proposals(opportunity("remove"), accessible_fraction=1, temporal_factor=1,
                                     entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    candidate = engine.materialize(proposal)
    engine.settle(candidate.candidate_id, SettlementKind.REMOVE_STOCK)
    assert engine.ledger_total() == before_active - 10
    assert engine.accounting_total() == before_accounting


def test_contact_arbitration_is_order_invariant_and_tie_is_stable():
    a = ContactIntent("a", "target", 1.0, (0, 0), ContactType.BITE_REMOVE, "intent-a")
    b = ContactIntent("b", "target", 1.0, (0, 0), ContactType.NIBBLE, "intent-b")
    engine = FCFEngine([source()])
    assert engine.arbitrate_contacts([a, b], "target") == engine.arbitrate_contacts([b, a], "target")
    earlier = ContactIntent("c", "target", .5, (0, 0), ContactType.BITE_REMOVE)
    assert engine.arbitrate_contacts([a, earlier], "target") == earlier
    with pytest.raises(ValueError):
        engine.arbitrate_contacts([
            ContactIntent("x", "target", 1.0, (0, 0), ContactType.BITE_REMOVE),
            ContactIntent("y", "target", 1.0, (0, 0), ContactType.NIBBLE),
        ], "target")


def test_invalid_configuration_is_rejected():
    with pytest.raises(ValueError):
        PopulationSource("s", "slice", 1, 0).realizable_units
    with pytest.raises(ValueError):
        FCFEngine.entry_probability(1.1, 1, 1)
    with pytest.raises(ValueError):
        PopulationSource("s", "slice", -1, 10)


def test_invalid_entry_input_does_not_consume_opportunity():
    engine = FCFEngine([source()])
    op = opportunity("invalid-input")
    with pytest.raises(ValueError):
        engine.form_proposals(op, accessible_fraction=2, temporal_factor=1,
                              entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    assert engine.opportunity_record(op) is None


def test_rc4_opportunity_id_excludes_runtime_delivery_details():
    a = FCFEngine.canonical_opportunity_id("scope", "slice", "s1", "FIRST_ACCESS", "partition-1", "rev-2")
    b = FCFEngine.canonical_opportunity_id("scope", "slice", "s1", "FIRST_ACCESS", "partition-1", "rev-2")
    assert a == b
    assert a != FCFEngine.canonical_opportunity_id("scope", "slice", "s1", "FIRST_ACCESS", "partition-2", "rev-2")


def test_cancel_before_reservation_has_no_ledger_write():
    engine = FCFEngine([PopulationSource("s1", "slice", 10, 10)], detailed_capacity=0)
    proposals = engine.form_proposals(
        opportunity(), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    engine.materialize(proposals[0])
    assert engine.sources["s1"].actual_supply == 10
    assert engine.sources["s1"].encounter_hold == 0
    assert engine.expire_pending(proposals[0].proposal_id)
    assert engine.sources["s1"].actual_supply == 10


def test_lifecycle_slice_transfer_preserves_stock_and_identity():
    normal = SliceKey("bass_stock", "mature", "NORMAL")
    guard = SliceKey("bass_stock", "mature", "SPAWN_GUARD")
    allocator = SliceAllocator({normal: 80.0, guard: 20.0})
    allocator.transfer(normal, guard, 15.0)
    assert allocator.buckets[normal] == 65.0
    assert allocator.buckets[guard] == 35.0
    assert SliceKey("bass_stock", "mature", "NORMAL") == normal
    with pytest.raises(ValueError):
        allocator.transfer(normal, normal, 1.0)


def test_dsl_compiler_rejects_capability_and_priority_errors():
    bad = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 0,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["UNKNOWN"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE", "FORAGE"],
                      "occupancy": [], "entry_offers": {}}],
    }
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(bad)
    assert {x.code for x in exc.value.diagnostics} >= {"INVALID_Q", "UNKNOWN_CONTACT", "MOTIVE_PRIORITY"}


def test_dsl_compiler_returns_json_safe_copy():
    raw = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [{"node_tag": "open", "grade": "GOOD"}],
                      "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    compiled = compile_artifact(raw)
    assert compiled == raw
    assert compiled is not raw


def test_variant_can_patch_policy_but_not_species_capability():
    raw = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "variants": [{"id": "cold_policy", "species_id": "bass", "policy_overrides": {"speed_band": "SLOW"}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    assert compile_artifact(raw)["variants"][0]["id"] == "cold_policy"
    raw["variants"][0]["policy_overrides"]["q"] = 1
    with pytest.raises(DSLCompileError):
        compile_artifact(raw)


def test_dsl_rejects_world_interpretation_and_duplicate_owner():
    raw = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
        "world_facts": ["COLD"],
        "settlement_owners": [{"physical_consequence_id": "drag", "owner": "entry"},
                              {"physical_consequence_id": "drag", "owner": "conversion"}],
    }
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(raw)
    assert {x.code for x in exc.value.diagnostics} >= {"WORLD_FACT_IS_INTERPRETATION", "DUPLICATE_SETTLEMENT_OWNER"}


def test_dsl_rejects_missing_programs_nested_unknowns_and_arrival_range():
    base = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    missing = dict(base, programs=[])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(missing)
    assert any(d.code == "PROGRAMS_REQUIRED" for d in exc.value.diagnostics)
    nested = dict(base)
    nested["species"] = dict(base["species"], bogus=True)
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(nested)
    assert any(d.code == "UNKNOWN_FIELD" for d in exc.value.diagnostics)
    arrival = dict(base, arrival={"produces_new_units": False, "temporal_factor": 2})
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(arrival)
    assert any(d.code == "ARRIVAL_T_RANGE" for d in exc.value.diagnostics)


def test_dsl_rejects_unknown_population_slice_and_trace_fields():
    base = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                    "anatomy_profile": "x", "sensory_channels": ["visual"],
                    "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
        "population_slices": [{"id": "s", "population_id": "bass", "cohort_key": "mature",
                                "lifecycle_role_key": "NORMAL", "behavior_program_id": "p"}],
        "trace_contract": {"version": "v1", "required_stages": ["ENTRY"],
                           "include_inputs": True, "include_revisions": True},
    }
    assert compile_artifact(base)["population_slices"][0]["id"] == "s"
    bad = dict(base, population_slices=[dict(base["population_slices"][0], bogus=True)])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(bad)
    assert any(d.code == "UNKNOWN_FIELD" for d in exc.value.diagnostics)
    bad_trace = dict(base, trace_contract={"version": "v1", "required_stages": ["ENTRY"], "bogus": True})
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(bad_trace)
    assert any(d.code == "UNKNOWN_FIELD" for d in exc.value.diagnostics)


def test_dsl_rejects_unknown_variant_policy_and_malformed_rule():
    base = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                    "anatomy_profile": "x", "sensory_channels": ["visual"],
                    "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "variants": [{"id": "v", "species_id": "bass", "policy_overrides": {"unknown": 1}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(base)
    assert any(d.code == "VARIANT_POLICY_PATH" for d in exc.value.diagnostics)
    malformed = dict(base, variants=[], resolver_rules=[{"rule_id": "r", "priority": 1,
                                                          "consequence_id": "x", "owner": "PERCEPTION",
                                                          "effective_interval": {"start": 2, "end": 1}}])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(malformed)
    assert any(d.code == "INTERVAL_RANGE" for d in exc.value.diagnostics)


def test_dsl_resolver_overlap_uses_when_and_resolves_references():
    base = {
        "schema_version": "fcf.v1",
        "population_definitions": [{"id": "bass_stock", "q": 10}],
        "species": {"id": "bass", "population_definition_id": "bass_stock",
                    "anatomy_profile": "x", "sensory_channels": ["visual"],
                    "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "population_slices": [{"id": "s", "population_id": "bass_stock", "cohort_key": "mature",
                                "lifecycle_role_key": "NORMAL", "behavior_program_id": "p"}],
        "variants": [{"id": "v", "species_id": "bass", "program_id": "p", "policy_overrides": {"speed_band": "SLOW"}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    nonoverlap = dict(base, resolver_rules=[
        {"rule_id": "r1", "priority": 1, "when": {"fact": "water_temperature_c", "eq": 10}, "then": {}, "consequence_id": "x", "owner": "PERCEPTION"},
        {"rule_id": "r2", "priority": 1, "when": {"fact": "water_temperature_c", "eq": 11}, "then": {}, "consequence_id": "y", "owner": "PERCEPTION"},
    ])
    assert compile_artifact(nonoverlap)["variants"][0]["program_id"] == "p"
    overlap = dict(base, resolver_rules=[
        {"rule_id": "r1", "priority": 1, "when": {"fact": "water_temperature_c", "eq": 10}, "then": {}, "consequence_id": "x", "owner": "PERCEPTION"},
        {"rule_id": "r1b", "priority": 1, "when": {"fact": "water_temperature_c", "eq": 10}, "then": {}, "consequence_id": "y", "owner": "PERCEPTION"},
    ])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(overlap)
    assert any(d.code == "EQUAL_PRIORITY_OVERLAP" for d in exc.value.diagnostics)
    range_overlap = dict(base, resolver_rules=[
        {"rule_id": "r3", "priority": 1, "when": {"fact": "water_temperature_c", "gt": 10}, "then": {}, "consequence_id": "x", "owner": "PERCEPTION"},
        {"rule_id": "r4", "priority": 1, "when": {"fact": "water_temperature_c", "gt": 20}, "then": {}, "consequence_id": "y", "owner": "PERCEPTION"},
    ])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(range_overlap)
    assert any(d.code == "EQUAL_PRIORITY_OVERLAP" for d in exc.value.diagnostics)
    disjoint = dict(base, resolver_rules=[
        {"rule_id": "r5", "priority": 1, "when": {"fact": "water_temperature_c", "lt": 10}, "then": {}, "consequence_id": "x", "owner": "PERCEPTION"},
        {"rule_id": "r6", "priority": 1, "when": {"fact": "water_temperature_c", "gte": 10}, "then": {}, "consequence_id": "y", "owner": "PERCEPTION"},
    ])
    assert compile_artifact(disjoint)["resolver_rules"][1]["rule_id"] == "r6"
    adjacent_intervals = dict(base, resolver_rules=[
        {"rule_id": "r7", "priority": 1, "when": {"fact": "water_temperature_c", "gt": 10}, "then": {}, "consequence_id": "x", "owner": "PERCEPTION", "effective_interval": {"start": 0, "end": 10, "unit": "s", "clock": "SIM"}},
        {"rule_id": "r8", "priority": 1, "when": {"fact": "water_temperature_c", "gt": 10}, "then": {}, "consequence_id": "y", "owner": "PERCEPTION", "effective_interval": {"start": 10, "end": 20, "unit": "s", "clock": "SIM"}},
    ])
    assert compile_artifact(adjacent_intervals)["resolver_rules"][1]["rule_id"] == "r8"
    bad_ref = dict(base, population_slices=[dict(base["population_slices"][0], behavior_program_id="missing")])
    with pytest.raises(DSLCompileError) as exc:
        compile_artifact(bad_ref)
    assert any(d.code == "MISSING_REFERENCE" for d in exc.value.diagnostics)


def test_opportunity_slice_mismatch_is_rejected_before_ledger_consumption():
    engine = FCFEngine([source()])
    bad = EntryOpportunity("bad-slice", "scope", "other-slice", "s1", "FIRST_ACCESS")
    with pytest.raises(ValueError):
        engine.form_proposals(bad, accessible_fraction=1, temporal_factor=1,
                              entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    assert not engine.ledgers


def test_editor_edits_are_transactional_and_versions_are_immutable():
    raw = {
        "schema_version": "fcf.v1",
        "species": {"id": "bass", "population_id": "bass", "q": 10,
                     "anatomy_profile": "x", "sensory_channels": ["visual"],
                     "allowed_contacts": ["BITE_REMOVE"], "history_schema": "h"},
        "programs": [{"id": "p", "slice_role": "NORMAL", "motive_priority": ["FORAGE"],
                      "occupancy": [], "entry_offers": {"FORAGE": {"base": "NORMAL"}}}],
        "settlement_owners": [{"physical_consequence_id": "cue", "owner": "PERCEPTION"}],
    }
    store = ArtifactStore(raw, author="reviewer")
    store.edit("species.q", 12)
    v = store.save_as_new_version("change q")
    assert v.version_id == "fcf.v1:1"
    snapshot = store.versions[0].artifact
    store.edit("species.q", 15)
    assert snapshot["species"]["q"] == 12
    v.artifact["species"]["q"] = 999
    assert store.versions[0].artifact["species"]["q"] == 12
    with pytest.raises(KeyError):
        store.edit("species.missing", 1)
    assert store.versions[0].artifact["species"]["q"] == 12


def test_occupancy_is_order_invariant_and_conserves_distributable_mass():
    rows = [("prime", 1.0, "PRIME"), ("good", 2.0, "GOOD")]
    a, reserve_a = allocate_occupancy(10, 1, rows, nominal_density=3, crowding_tolerance=1)
    b, reserve_b = allocate_occupancy(10, 1, list(reversed(rows)), nominal_density=3, crowding_tolerance=1)
    assert a == b
    assert reserve_a == reserve_b
    assert sum(a.values()) + reserve_a == 10
    capped_rows = [("prime", 1.0, "PRIME"), ("good", 20.0, "GOOD")]
    c1, r1 = allocate_occupancy(100, 1, capped_rows, nominal_density=1, crowding_tolerance=1)
    c2, r2 = allocate_occupancy(100, 1, list(reversed(capped_rows)), nominal_density=1, crowding_tolerance=1)
    assert c1 == c2 and r1 == r2


def test_motive_and_entry_offer_are_deterministic_and_discrete():
    assert resolve_motive([EntryMotive.DEFEND, EntryMotive.FORAGE], {EntryMotive.DEFEND: False, EntryMotive.FORAGE: True}) == EntryMotive.FORAGE
    assert resolve_entry_offer(EntryGrade.NORMAL, strongest_positive_steps=1) == EntryGrade.STRONG
    assert resolve_entry_offer(EntryGrade.CERTAIN, strongest_negative_steps=3) == EntryGrade.NORMAL
    assert resolve_entry_offer(EntryGrade.CERTAIN, deny=True) == EntryGrade.NONE
    with pytest.raises(ValueError):
        resolve_motive([EntryMotive.FORAGE, EntryMotive.FORAGE], {})


def test_encounter_is_deterministic_and_soft_difficulty_stays_downstream():
    state = encounter_step(EncounterState.ATTENTIVE, EntryMotive.FORAGE, "TARGET_SALIENT")
    assert state == EncounterState.FOLLOWING
    assert encounter_step(state, EntryMotive.FORAGE, "PURSUIT_COST_EXCEEDED", task_difficult=True) == EncounterState.DISENGAGED
    assert encounter_step(EncounterState.ATTENTIVE, EntryMotive.DEFEND, "NEST_INTRUSION_ONSET") == EncounterState.THREAT_TRACK


def test_hook_compatibility_has_only_downstream_inputs():
    assert hook_compatibility(ContactType.BITE_REMOVE, {ContactType.BITE_REMOVE}, geometry_exposure=1, rig_orientation=.5, timing=1) == .5
    assert hook_compatibility(ContactType.NIBBLE, {ContactType.BITE_REMOVE}, geometry_exposure=1, rig_orientation=1, timing=1) == 0


def test_concurrent_materialization_has_single_reservation_owner():
    engine = FCFEngine([PopulationSource("s1", "slice", 10, 10)], detailed_capacity=8)
    proposals = engine.form_proposals(
        opportunity(), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    assert len(proposals) == 1
    with ThreadPoolExecutor(max_workers=8) as pool:
        made = list(pool.map(engine.materialize, proposals * 8))
    assert len([candidate for candidate in made if candidate is not None]) == 1
    assert engine.sources["s1"].encounter_hold == 10


def test_concurrent_materialization_never_exceeds_detailed_capacity():
    engine = FCFEngine([PopulationSource("s1", "slice", 20, 10)], detailed_capacity=1)
    proposals = engine.form_proposals(
        opportunity("capacity"), accessible_fraction=1, temporal_factor=1,
        entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
    )
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(engine.materialize, proposals))
    assert len(engine.candidates) == 1
    assert len(engine.pending) == 1


def test_commit_random_boundary_is_proposal_stable():
    e1 = FCFEngine([source()])
    p1 = e1.form_proposals(opportunity("stable"), accessible_fraction=1, temporal_factor=1,
                           entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    c1 = e1.materialize(p1)
    c1.state = "COMMIT_READY"
    result1 = e1.commit(c1.candidate_id, EntryGrade.NORMAL)
    e2 = FCFEngine([source()])
    p2 = e2.form_proposals(opportunity("stable"), accessible_fraction=1, temporal_factor=1,
                           entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    c2 = e2.materialize(p2)
    c2.state = "COMMIT_READY"
    result2 = e2.commit(c2.candidate_id, EntryGrade.NORMAL)
    assert result1 == result2


def test_commit_is_one_decision_and_cannot_be_rerolled():
    engine = FCFEngine([source()])
    proposal = engine.form_proposals(opportunity("commit-once"), accessible_fraction=1, temporal_factor=1,
                                     entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    candidate = engine.materialize(proposal)
    candidate.state = "COMMIT_READY"
    first = engine.commit(candidate.candidate_id, EntryGrade.NONE)
    second = engine.commit(candidate.candidate_id, EntryGrade.CERTAIN)
    assert first is False and second is False
    assert candidate.commit_attempted and candidate.state == "COMMIT_FAILED"


def test_active_candidate_cannot_be_evicted_without_terminal_settlement():
    engine = FCFEngine([source()])
    proposal = engine.form_proposals(opportunity("slot"), accessible_fraction=1, temporal_factor=1,
                                     entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    candidate = engine.materialize(proposal)
    with pytest.raises(ValueError):
        engine.release_slot(candidate.candidate_id)
    assert candidate.candidate_id in engine.candidates


def test_forged_or_wrong_slice_proposal_is_rejected():
    engine = FCFEngine([source()])
    proposal = engine.form_proposals(opportunity("auth"), accessible_fraction=1, temporal_factor=1,
                                     entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    forged = proposal.__class__(proposal.proposal_id, proposal.opportunity_id, proposal.source_id, "other-slice",
                                proposal.scope_id, proposal.unit_index, proposal.motive, proposal.entry_probability, proposal.created_at)
    with pytest.raises(ValueError):
        engine.materialize(forged)


def test_arrival_placement_is_xor_not_double_counted():
    validate_arrival_placement(produces_new_units=True, temporal_factor=1)
    with pytest.raises(ValueError):
        validate_arrival_placement(produces_new_units=True, temporal_factor=.5)


def test_explain_trace_is_deterministic_and_non_mutating():
    trace = entry_trace(fixture_id="f", artifact_version="fcf.v1:1", opportunity_id="o",
                        a=.8, t=1, motive="FORAGE", e=.7, q=10, reservation_id="r")
    assert trace.to_json() == trace.to_json()
    assert '"owner":"population_ledger"' in trace.to_json()


def test_durable_journal_is_idempotent_and_recoverable(tmp_path):
    path = str(tmp_path / "fcf.events.jsonl")
    journal = DurableJournal(path)
    payload = {"scope": "s", "revision": "r1"}
    assert journal.append_once("opp-1", "OPPORTUNITY_CONSUMED", payload)
    assert not journal.append_once("opp-1", "OPPORTUNITY_CONSUMED", payload)
    with pytest.raises(JournalConflict):
        journal.append_once("opp-1", "OPPORTUNITY_CONSUMED", {"scope": "different"})
    recovered = DurableJournal(path)
    assert recovered.get("opp-1")["payload"] == payload
    assert recovered.records() == journal.records()


def test_sqlite_journal_matches_durable_adapter_contract(tmp_path):
    journal = SQLiteJournal(str(tmp_path / "events.sqlite"))
    payload = {"scope": "s", "revision": "r1"}
    assert journal.append_once("e-1", "TEST", payload)
    assert not journal.append_once("e-1", "TEST", payload)
    with pytest.raises(JournalConflict):
        journal.append_once("e-1", "TEST", {"scope": "different"})
    assert journal.get("e-1")["payload"] == payload
    assert len(journal.records()) == 1
    journal.close()
    with SQLiteJournal(str(tmp_path / "context.sqlite")) as managed:
        assert managed.append_once("ctx", "TEST", {})


def test_engine_restarts_from_sqlite_journal(tmp_path):
    path = str(tmp_path / "engine.sqlite")
    journal = SQLiteJournal(path)
    engine = FCFEngine([source(actual=20)], journal=journal)
    proposal = engine.form_proposals(opportunity("sqlite-engine"), accessible_fraction=1,
                                     temporal_factor=1, entry_grade=EntryGrade.CERTAIN,
                                     motive=EntryMotive.FORAGE)[0]
    candidate = engine.materialize(proposal)
    journal.close()
    restarted = FCFEngine([source(actual=10)], journal=SQLiteJournal(path), hydrate_journal=True)
    assert restarted.candidates[candidate.candidate_id].reservation_id == candidate.reservation_id


def test_sqlite_journal_is_exactly_once_across_processes(tmp_path):
    path = str(tmp_path / "events.sqlite")
    context = multiprocessing.get_context("spawn")
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [context.Process(target=_sqlite_same_id_worker, args=(path, barrier, queue)) for _ in range(2)]
    for process in processes:
        process.start()
    results = [queue.get(timeout=15) for _ in processes]
    for process in processes:
        process.join(15)
        assert process.exitcode == 0
    assert sorted(results, key=str) == [False, True]
    journal = SQLiteJournal(path)
    assert len(journal.records()) == 1
    journal.close()




def test_durable_journal_is_integrity_safe_across_processes(tmp_path):
    path = str(tmp_path / "multi.jsonl")
    context = multiprocessing.get_context("spawn")  # fork unavailable on Windows; workers are module-level so spawn is cross-platform
    processes = [context.Process(target=_journal_process_worker, args=(path, f"p{n}")) for n in range(4)]
    for process in processes:
        process.start()
    for process in processes:
        process.join(10)
        assert process.exitcode == 0
    recovered = DurableJournal(path)
    assert len(recovered.records()) == 40


def test_durable_journal_is_exactly_once_for_same_id_across_processes(tmp_path):
    path = str(tmp_path / "same-id.jsonl")
    context = multiprocessing.get_context("spawn")  # fork unavailable on Windows; workers are module-level so spawn is cross-platform
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [context.Process(target=_journal_same_id_worker, args=(path, barrier, queue)) for _ in range(2)]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _ in processes]
    for process in processes:
        process.join(10)
        assert process.exitcode == 0
    assert sorted(results, key=str) == [False, True]
    assert len(DurableJournal(path).records()) == 1


def test_durable_journal_rejects_conflicting_same_id_across_processes(tmp_path):
    path = str(tmp_path / "conflict-id.jsonl")
    context = multiprocessing.get_context("spawn")  # fork unavailable on Windows; workers are module-level so spawn is cross-platform
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [context.Process(target=_journal_conflict_worker, args=(path, barrier, queue, value))
                 for value in (1, 2)]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _ in processes]
    for process in processes:
        process.join(10)
        assert process.exitcode == 0
    assert sorted(results, key=str) == ["JournalConflict", True]
    assert len(DurableJournal(path).records()) == 1


def test_engine_journals_opportunity_reservation_and_settlement(tmp_path):
    journal = DurableJournal(str(tmp_path / "events.jsonl"))
    engine = FCFEngine([source()], journal=journal)
    proposal = engine.form_proposals(opportunity("journaled"), accessible_fraction=1, temporal_factor=1,
                                     entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    candidate = engine.materialize(proposal)
    engine.settle(candidate.candidate_id, SettlementKind.RETURN)
    event_types = [record["event_type"] for record in journal.records()]
    assert set(event_types) == {"OPPORTUNITY_CONSUMED", "CANDIDATE_RESERVED", "CANDIDATE_SETTLED"}


def test_semantic_trigger_rolls_back_when_journal_write_fails():
    class FailingJournal:
        def append_once(self, *args, **kwargs):
            raise OSError("disk full")
        def get(self, *args, **kwargs):
            return None
    engine = FCFEngine([source()], journal=FailingJournal())
    op = EntryOpportunity("reeval-fail", "scope", "slice", "s1", "SEMANTIC_REEVALUATION", "pause")
    with pytest.raises(OSError):
        engine.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                              entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    engine.journal = None
    assert engine.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                                 entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE) is not None


def test_restart_with_existing_reservation_refuses_duplicate_materialization(tmp_path):
    journal = DurableJournal(str(tmp_path / "events.jsonl"))
    e1 = FCFEngine([source()], journal=journal)
    op = EntryOpportunity("restart", "scope", "slice", "s1", "FIRST_ACCESS")
    p1 = e1.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                           entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    assert e1.materialize(p1) is not None
    e2 = FCFEngine([source()], journal=DurableJournal(str(tmp_path / "events.jsonl")))
    with pytest.raises(ValueError):
        e2.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                          entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    changed = EntryOpportunity("restart", "scope", "slice", "s1", "FIRST_ACCESS", semantic_snapshot_fingerprint="changed")
    with pytest.raises(ValueError):
        e2.form_proposals(changed, accessible_fraction=1, temporal_factor=1,
                          entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    e3 = FCFEngine([source()], journal=DurableJournal(str(tmp_path / "events.jsonl")), hydrate_journal=True)
    assert len(e3.candidates) == 1
    assert e3.sources["s1"].actual_supply == 0
    assert e3.sources["s1"].encounter_hold == 10


def test_hydration_replays_terminal_settlement_once(tmp_path):
    path = str(tmp_path / "events.jsonl")
    e1 = FCFEngine([source()], journal=DurableJournal(path))
    op = EntryOpportunity("hydrate-settle", "scope", "slice", "s1", "FIRST_ACCESS")
    proposal = e1.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                                  entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    candidate = e1.materialize(proposal)
    e1.settle(candidate.candidate_id, SettlementKind.RETURN)
    e2 = FCFEngine([source()], journal=DurableJournal(path), hydrate_journal=True)
    assert e2.candidates[candidate.candidate_id].settled
    assert e2.sources["s1"].actual_supply == 10
    assert e2.sources["s1"].encounter_hold == 0


def test_hydration_restores_runtime_sequences_before_new_arrival(tmp_path):
    path = str(tmp_path / "events.jsonl")
    journal = DurableJournal(path)
    e1 = FCFEngine([PopulationSource("s1", "slice", 20, 10)], journal=journal)
    first = EntryOpportunity("seq-first", "scope", "slice", "s1", "FIRST_ACCESS")
    p1 = e1.form_proposals(first, accessible_fraction=1, temporal_factor=1,
                           entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)[0]
    c1 = e1.materialize(p1)
    e2 = FCFEngine([PopulationSource("s1", "slice", 20, 10)], journal=DurableJournal(path), hydrate_journal=True)
    e2.sources["s1"].actual_supply += 10
    arrival = EntryOpportunity("seq-arrival", "scope", "slice", "s1", "ARRIVAL", "arrival-1", population_revision="r2")
    p2 = e2.form_proposals(arrival, accessible_fraction=1, temporal_factor=1,
                           entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
                           eligible_units=1)[0]
    c2 = e2.materialize(p2)
    assert c2.candidate_id != c1.candidate_id
    assert c2.reservation_id != c1.reservation_id


def test_hydration_rejects_corrupt_payload_before_partial_state(tmp_path):
    path = str(tmp_path / "corrupt.jsonl")
    journal = DurableJournal(path)
    journal.append_once("opportunity:bad", "OPPORTUNITY_CONSUMED", {"scope": "s"})
    with pytest.raises(ValueError):
        FCFEngine([source()], journal=DurableJournal(path), hydrate_journal=True)


def test_flagship_spawn_bass_trace_closes_without_prey_likeness():
    guard_source = PopulationSource("bass-guard", "SPAWN_GUARD", 10, 10)
    engine = FCFEngine([guard_source])
    op = EntryOpportunity("bass-nest", "scope", "SPAWN_GUARD", "bass-guard", "FIRST_ACCESS")
    proposals = engine.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                                      entry_grade=EntryGrade.STRONG, motive=EntryMotive.DEFEND)
    candidate = engine.materialize(proposals[0])
    candidate.state = "ATTENTIVE"
    candidate.state = encounter_step(EncounterState.ATTENTIVE, EntryMotive.DEFEND, "NEST_INTRUSION_ONSET").value
    candidate.state = encounter_step(EncounterState.THREAT_TRACK, EntryMotive.DEFEND, "INTRUSION_PERSISTS").value
    assert candidate.state == EncounterState.COMMIT_READY.value
    assert engine.commit(candidate.candidate_id, EntryGrade.CERTAIN)
    intent = ContactIntent(candidate.candidate_id, "lure", 1.0, (0.0, 0.0), ContactType.BITE_REMOVE, "bass-intent")
    assert engine.arbitrate_contacts([intent], "lure") == intent
    engine.settle(candidate.candidate_id, SettlementKind.RETURN)
    assert engine.sources["bass-guard"].encounter_hold == 0


def test_flagship_trout_drift_keeps_soft_intercept_failure_downstream():
    engine = FCFEngine([PopulationSource("trout", "NORMAL", 10, 10)])
    op = EntryOpportunity("trout-drift", "scope", "NORMAL", "trout", "FIRST_ACCESS")
    proposals = engine.form_proposals(op, accessible_fraction=1, temporal_factor=1,
                                      entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    candidate = engine.materialize(proposals[0])
    state = encounter_step(EncounterState.ATTENTIVE, EntryMotive.FORAGE, "TARGET_SALIENT")
    state = encounter_step(state, EntryMotive.FORAGE, "PURSUIT_COST_EXCEEDED", task_difficult=True)
    assert candidate is not None and state == EncounterState.DISENGAGED
    engine.settle(candidate.candidate_id, SettlementKind.RETURN)
    assert engine.sources["trout"].encounter_hold == 0


def test_flagship_carp_static_bait_uses_arrival_not_periodic_reroll():
    engine = FCFEngine([PopulationSource("carp", "NORMAL", 20, 10)])
    first = EntryOpportunity("carp-arrival-1", "scope", "NORMAL", "carp", "ARRIVAL", "arrival-1", population_revision="rev-1")
    second = EntryOpportunity("carp-arrival-2", "scope", "NORMAL", "carp", "ARRIVAL", "arrival-2", population_revision="rev-2")
    p1 = engine.form_proposals(first, accessible_fraction=1, temporal_factor=1,
                               entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    engine.sources["carp"].actual_supply += 10
    p2 = engine.form_proposals(second, accessible_fraction=1, temporal_factor=1,
                               entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
                               eligible_units=1)
    assert p1 and p2
    assert first.opportunity_id != second.opportunity_id
    c1 = engine.materialize(p1[0])
    engine.settle(c1.candidate_id, SettlementKind.RETURN_WARY)
    c2 = engine.materialize(p2[0])
    assert c2 is not None
    engine.settle(c2.candidate_id, SettlementKind.RETURN)
    assert engine.ledger_total() == 30


def test_runtime_tick_ids_cannot_forge_repeated_first_access():
    engine = FCFEngine([PopulationSource("s1", "slice", 30, 10)])
    first = EntryOpportunity("runtime-tick-1", "scope", "slice", "s1", "FIRST_ACCESS")
    engine.form_proposals(first, accessible_fraction=1, temporal_factor=1,
                          entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)
    forged = EntryOpportunity("runtime-tick-2", "scope", "slice", "s1", "FIRST_ACCESS")
    with pytest.raises(ValueError):
        engine.form_proposals(forged, accessible_fraction=1, temporal_factor=1,
                              entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)


def test_first_access_trigger_ids_cannot_bypass_scope_dedupe():
    engine = FCFEngine([PopulationSource("s1", "slice", 30, 10)])
    forged = EntryOpportunity("id-x", "scope", "slice", "s1", "FIRST_ACCESS", "x")
    with pytest.raises(ValueError):
        engine.form_proposals(forged, accessible_fraction=1, temporal_factor=1,
                              entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE)


def _temperature_profile():
    return {
        "schema_version": "fcf.temperature_profile.v1",
        "profile_id": "lake_summer", "waterbody_id": "lake",
        "spatial_frame_id": "lake_grid:r1", "profile_mode": "DEPTH_LAYERS",
        "temperature_unit": "CELSIUS",
        "temporal_clock": {"clock_id": "sim_clock", "clock_revision": "r1",
                           "unit": "MILLISECONDS", "epoch": "SIMULATION_START"},
        "source_policy": {"accepted_source_kinds": ["SENSOR"],
                          "maximum_uncertainty_c": 1,
                          "freshness_by_source_s": {"SENSOR": 900},
                          "stale_behavior": "RETURN_STALE_FACT",
                          "missing_behavior": "RETURN_UNKNOWN",
                          "outlier_policy_id": "outlier:r1",
                          "calibration_policy_id": "cal:r1"},
        "interpolation_policy": {"spatial_method": "NEAREST_CELL",
                                 "maximum_spatial_gap_m": 20,
                                 "depth_method": "LINEAR_WITHIN_LAYER",
                                 "maximum_depth_gap_m": 2,
                                 "temporal_method": "HOLD_LAST",
                                 "maximum_time_gap_s": 600,
                                 "thermocline_crossing": "BLOCK",
                                 "algorithm_revision": "interp:r1"},
        "depth_layers": [
            {"layer_id": "surface", "depth_min_m": 0, "depth_max_m": 4,
             "location_cell_group_id": "basin", "samples": [
                 {"sample_id": "sample_a", "location_cell": "cell_a", "depth_m": 2,
                  "observed_at_ms": 100, "valid_from_ms": 0, "valid_to_ms": 1000,
                  "value_c": 20, "uncertainty_c": .2, "source_kind": "SENSOR",
                  "source_revision": "sensor:r1", "quality": "DIRECT",
                  "calibration_revision": None, "source_sample_ids": ["raw_a"]}]},
            {"layer_id": "deep", "depth_min_m": 7, "depth_max_m": 12,
             "location_cell_group_id": "basin", "samples": [
                 {"sample_id": "sample_b", "location_cell": "cell_a", "depth_m": 8,
                  "observed_at_ms": 100, "valid_from_ms": 0, "valid_to_ms": 1000,
                  "value_c": 16, "uncertainty_c": .4, "source_kind": "SENSOR",
                  "source_revision": "sensor:r1", "quality": "DIRECT",
                  "calibration_revision": "cal:r1", "source_sample_ids": ["raw_b"]}]},
        ],
        "thermocline_boundaries": [
            {"boundary_id": "thermocline", "location_cell_group_id": "basin",
             "top_depth_m": 4, "bottom_depth_m": 7,
             "valid_from_ms": 0, "valid_to_ms": 1000,
             "source_revision": "sensor:r1", "crossing_policy": "BLOCK_INTERPOLATION"}],
        "profile_revision": "temperature:r1",
        "source_manifest_hash": "sha256:" + "0123456789abcdef" * 4,
        "authoring_metadata": {"author": "environment", "created_at": "2026-08-31T10:00:00+08:00",
                               "change_reason": "fixture", "evidence_refs": []},
    }


def test_temperature_profile_semantic_compiler_accepts_valid_profile():
    raw = _temperature_profile()
    compiled = compile_temperature_profile(raw)
    assert compiled == raw and compiled is not raw


@pytest.mark.parametrize("mutate,code", [
    (lambda p: p["depth_layers"][1].update(depth_min_m=3), "DEPTH_LAYER_OVERLAP"),
    (lambda p: p["depth_layers"][0]["samples"][0].update(depth_m=6), "SAMPLE_OUTSIDE_LAYER"),
    (lambda p: p["depth_layers"][0]["samples"][0].update(valid_to_ms=0), "SAMPLE_VALIDITY_RANGE"),
    (lambda p: p["thermocline_boundaries"][0].update(bottom_depth_m=3), "THERMOCLINE_RANGE"),
    (lambda p: p.update(profile_mode="SINGLE_LAYER"), "SINGLE_LAYER_COUNT"),
    (lambda p: p["depth_layers"][1]["samples"][0].update(sample_id="sample_a"), "DUPLICATE_SAMPLE_ID"),
    (lambda p: p["depth_layers"][0]["samples"][0].update(source_kind="HYDRO_MODEL"), "SAMPLE_SOURCE_NOT_ALLOWED"),
    (lambda p: p["source_policy"].update(freshness_by_source_s={}), "SOURCE_FRESHNESS_MISSING"),
])
def test_temperature_profile_semantic_compiler_rejects_cross_field_errors(mutate, code):
    raw = _temperature_profile()
    mutate(raw)
    with pytest.raises(DSLCompileError) as exc:
        compile_temperature_profile(raw)
    assert any(d.code == code for d in exc.value.diagnostics)


@pytest.mark.parametrize("mutate", [
    lambda p: p["depth_layers"][0]["samples"][0].update(value_c=float("nan")),
    lambda p: p["depth_layers"][0]["samples"][0].update(uncertainty_c=float("inf")),
    lambda p: p["depth_layers"][0].update(depth_max_m=float("inf")),
    lambda p: p["thermocline_boundaries"][0].update(bottom_depth_m=float("nan")),
    lambda p: p["interpolation_policy"].update(maximum_depth_gap_m=float("inf")),
])
def test_temperature_profile_rejects_nonfinite_physical_values(mutate):
    raw = _temperature_profile()
    mutate(raw)
    with pytest.raises(DSLCompileError) as exc:
        compile_temperature_profile(raw)
    assert any(d.code in {"NONFINITE_PHYSICAL_VALUE", "DEPTH_LAYER_RANGE", "THERMOCLINE_RANGE"}
               for d in exc.value.diagnostics)
