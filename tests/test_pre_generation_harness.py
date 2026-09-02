from dataclasses import replace
from fcf_v1.pre_generation import *


def test_same_input_same_opportunity_id():
    assert fixture_occurrence().basis().opportunity_id == fixture_occurrence().basis().opportunity_id

def test_fps_fragmentation_same_opportunity_set():
    assert fixture_occurrence("A").basis().opportunity_id == fixture_occurrence("B").basis().opportunity_id

def test_packet_fragmentation_same_opportunity_set():
    assert fixture_occurrence("A").basis().opportunity_id == fixture_occurrence("C").basis().opportunity_id

def test_presentation_exposure_meaning_coalescing():
    o = fixture_occurrence(); r = PreGenerationHarness().resolve(o, fixture_contributions())
    assert r.meaning_response.presentation_event == "DEFLECTION"
    assert r.meaning_response.exposure == "HIGH" and r.meaning_response.feeding_match == "VALID"
    assert len(r.entries) == 1

def test_duplicate_claim_returns_same_result():
    h = PreGenerationHarness(); o = fixture_occurrence(); a = h.resolve(o, fixture_contributions()); b = h.resolve(o, fixture_contributions(10))
    assert a == b

def test_snapshot_rollover_does_not_rebind_old_opportunity():
    h = PreGenerationHarness(); old = fixture_occurrence(snapshot=ResolveSnapshotBundle(world_snapshot_revision="W172")); r = h.resolve(old, fixture_contributions())
    newer = replace(old, snapshot=ResolveSnapshotBundle(world_snapshot_revision="W173"))
    assert r.snapshot_fingerprint == old.snapshot.fingerprint() and r.snapshot_fingerprint != newer.snapshot.fingerprint()

def test_source_fragmentation_same_candidate_identity():
    a = fixture_contributions(1)[0]; b = fixture_contributions(10)[0]
    assert a.basis_key == b.basis_key

def test_selection_fragmentation_invariance():
    h1, h2 = PreGenerationHarness(), PreGenerationHarness(); o = fixture_occurrence()
    assert h1.resolve(o, fixture_contributions(1)).selected_basis_key == h2.resolve(o, fixture_contributions(10)).selected_basis_key

def test_unrelated_support_independence():
    o = fixture_occurrence(); h = PreGenerationHarness()
    base = h.resolve(o, fixture_contributions()).selected_basis_key
    unrelated = CandidateContribution("Bass", "adult", "NORMAL", "FEEDING", None, "SPAWN_BED_03", "bass-normal", 999)
    assert PreGenerationHarness().resolve(o, fixture_contributions() + (unrelated,)).selected_basis_key == base

def test_guard_anchor_provenance():
    c = CandidateContribution("Bass", "adult", "SPAWN_GUARD", "GUARD_DEFENSE", "Nest_03", "SPAWN_BED_03", "guard", 1.0)
    o = replace(fixture_occurrence(), support=SemanticSupportRef("SPAWN_BED_03")); r = PreGenerationHarness().resolve(o, (c,)); assert PreGenerationHarness().materialize(r).anchor_ref == "Nest_03"

def test_guard_materialization_eligibility():
    c = CandidateContribution("Bass", "adult", "SPAWN_GUARD", "GUARD_DEFENSE", "Nest_03", "SPAWN_BED_03", "guard", 1.0)
    o = replace(fixture_occurrence(), support=SemanticSupportRef("SPAWN_BED_03")); fish = PreGenerationHarness().materialize(PreGenerationHarness().resolve(o, (c,)))
    assert fish.reproductive_eligible and fish.quality >= 2

def test_generation_support_fragmentation_invariance():
    c = CandidateContribution("Bass", "adult", "SPAWN_GUARD", "GUARD_DEFENSE", "Nest_03", "SPAWN_BED_03", "guard", 1.0)
    o = replace(fixture_occurrence(), support=SemanticSupportRef("SPAWN_BED_03")); h = PreGenerationHarness(); a = h.materialize(h.resolve(o, (c,)), "fixed")
    h = PreGenerationHarness(); b = h.materialize(h.resolve(o, (replace(c, engagement_mass=.1),) * 10), "fixed")
    assert a == b

def test_rng_domain_separation():
    assert rng_u("s", "selection", "k") == rng_u("s", "selection", "k")
    assert rng_u("s", "selection", "k") != rng_u("s", "trait", "k")

def test_trait_schema_extension_does_not_change_selection():
    o = fixture_occurrence(); h = PreGenerationHarness(); a = h.resolve(o, fixture_contributions()).selected_basis_key
    extended = replace(o, trait_schema_version="trait-v1+unrelated-field")
    assert PreGenerationHarness().resolve(extended, fixture_contributions()).selected_basis_key == a

def test_metamorphic_fragmentation_result():
    o = fixture_occurrence(); results = []
    for n in (1, 10, 20):
        h = PreGenerationHarness(); r = h.resolve(o, fixture_contributions(n)); results.append((r.opportunity_id, tuple(e.basis_key for e in r.entries), r.selected_basis_key, h.materialize(r)))
    assert results[0] == results[1] == results[2]
