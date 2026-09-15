from dataclasses import fields, replace
from fcf_v1.pre_generation import *


def test_same_input_same_opportunity_id():
    assert fixture_occurrence().basis().opportunity_id == fixture_occurrence().basis().opportunity_id


def test_fps_fragmentation_same_opportunity_set():
    assert fixture_occurrence("A").basis().opportunity_id == fixture_occurrence("B").basis().opportunity_id


def test_packet_fragmentation_same_opportunity_set():
    assert fixture_occurrence("A").basis().opportunity_id == fixture_occurrence("C").basis().opportunity_id


def test_presentation_exposure_meaning_coalescing():
    r = PreGenerationHarness().resolve(fixture_occurrence(), fixture_contributions())
    assert r.meaning_response.presentation_event == "DEFLECTION"
    assert r.meaning_response.response_band == "HIGH"
    assert len(r.entries) == 1


def test_duplicate_claim_returns_same_result():
    h = PreGenerationHarness(); o = fixture_occurrence()
    assert h.resolve(o, fixture_contributions()) == h.resolve(o, fixture_contributions(10))


def test_snapshot_rollover_does_not_rebind_old_opportunity():
    h = PreGenerationHarness(); old = fixture_occurrence(snapshot=ResolveSnapshotBundle(world_snapshot_revision="W172")); r = h.resolve(old, fixture_contributions())
    newer = replace(old, snapshot=ResolveSnapshotBundle(world_snapshot_revision="W173"))
    assert r.snapshot_fingerprint == old.snapshot.fingerprint() and r.snapshot_fingerprint != newer.snapshot.fingerprint()


def test_source_fragmentation_same_candidate_identity():
    assert fixture_contributions(1)[0].basis_key == fixture_contributions(10)[0].basis_key


def test_selection_fragmentation_invariance():
    o = fixture_occurrence()
    assert PreGenerationHarness().resolve(o, fixture_contributions(1)).selected_basis_key == PreGenerationHarness().resolve(o, fixture_contributions(10)).selected_basis_key


def test_unrelated_support_independence():
    o = fixture_occurrence(); base = PreGenerationHarness().resolve(o, fixture_contributions()).selected_basis_key
    unrelated = CandidateContribution("Bass", "Q3", "SPAWN_GUARD", "SPAWN_BED_03", 999)
    assert PreGenerationHarness().resolve(o, fixture_contributions() + (unrelated,)).selected_basis_key == base


def test_current_candidate_identity_has_no_legacy_axes():
    names = {f.name for f in fields(CandidateContribution)}
    assert names == {"species", "fish_quality", "engagement_mode", "semantic_support_ref", "selection_weight"}
    assert not ({"lifecycle_cohort", "fish_mode", "response_slice", "behavior_anchor_ref"} & names)


def test_materialization_does_not_reroll_fish_quality():
    c = CandidateContribution("Bass", "Q4", "SPAWN_GUARD", "SPAWN_BED_03", 1.0)
    o = replace(fixture_occurrence(), support=SemanticSupportRef("SPAWN_BED_03"))
    fish = PreGenerationHarness().materialize(PreGenerationHarness().resolve(o, (c,)), "ignored-trait-seed")
    assert fish.fish_quality == "Q4" and fish.engagement_mode == "SPAWN_GUARD"


def test_rng_domain_separation():
    assert rng_u("s", "selection", "k") == rng_u("s", "selection", "k")
    assert rng_u("s", "selection", "k") != rng_u("s", "trait", "k")


def test_trait_schema_extension_does_not_change_selection():
    o = fixture_occurrence(); a = PreGenerationHarness().resolve(o, fixture_contributions()).selected_basis_key
    extended = replace(o, trait_schema_version="trait-v1+unrelated-field")
    assert PreGenerationHarness().resolve(extended, fixture_contributions()).selected_basis_key == a


def test_metamorphic_fragmentation_result():
    o = fixture_occurrence(); results = []
    for n in (1, 10, 20):
        h = PreGenerationHarness(); r = h.resolve(o, fixture_contributions(n)); results.append((r.opportunity_id, tuple(e.basis_key for e in r.entries), r.selected_basis_key, h.materialize(r)))
    assert results[0] == results[1] == results[2]
