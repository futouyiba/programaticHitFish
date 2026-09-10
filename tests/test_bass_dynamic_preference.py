from bass_dynamic_preference.run_case import EPOCHS, FOODS, ZONES, run
from bass_dynamic_preference.prototype import (
    HABITAT_CLASSES,
    PreyState,
    SourceGroup,
    TechnicalFragment,
    aggregate_fragments,
    bias_key,
    bias_table,
    context_at,
    fragment_source,
    generate_map,
    granularity_comparison,
    observation_experiment,
    resolve_feeding_bias,
    resolve_spatial_class_bias,
    source_intensity,
)


def test_three_epoch_spatial_reorders_without_global_gain():
    result = run()
    ranks = [
        sorted(ZONES, key=lambda z: result["spatial"][epoch][z]["local_intensity"], reverse=True)
        for epoch in EPOCHS
    ]
    assert ranks == [
        ["Grass Edge", "Shaded Wood", "Drop-off"],
        ["Shaded Wood", "Drop-off", "Grass Edge"],
        ["Drop-off", "Grass Edge", "Shaded Wood"],
    ]
    totals = result["centered_checks"]["spatial_local_totals"]
    assert len(set(totals.values())) == 1


def test_three_epoch_feeding_reorders_without_appetite_gain():
    result = run()
    ranks = [
        sorted(FOODS, key=lambda f: result["feeding"][epoch][f]["feeding_match"], reverse=True)
        for epoch in EPOCHS
    ]
    assert ranks == [
        ["BAITFISH", "CRUSTACEAN", "WORM_LIKE"],
        ["CRUSTACEAN", "WORM_LIKE", "BAITFISH"],
        ["WORM_LIKE", "BAITFISH", "CRUSTACEAN"],
    ]
    totals = result["centered_checks"]["feeding_weighted_totals"]
    assert all(abs(v - 2.4) < 1e-6 for v in totals.values())


def test_default_neutral_conditions_are_explicit():
    result = run()
    assert result["conditions"] == {
        "satiation": "NORMAL",
        "cue_familiarity": "LOW",
        "fish_mode": "NORMAL",
        "lifecycle_cohort": "ORDINARY_NORMAL",
        "reach": 0.8,
        "local_scale": 100.0,
    }


def _fragmentation_pair(granularity):
    source = SourceGroup("A", "NORTH", "GRASS", 1.0, 0.8)
    one = [TechnicalFragment("A", "A", "NORTH", "GRASS", 1.0, 0.8)]
    ten = fragment_source(source, 10)
    map_sources = generate_map() + [source]
    table = bias_table(granularity, context_at(12.0), map_sources)
    aggregate_one = aggregate_fragments(one)[0]
    aggregate_ten = aggregate_fragments(ten)[0]
    return (
        source_intensity(aggregate_one, granularity, table),
        source_intensity(aggregate_ten, granularity, table),
    )


def test_fragmentation_invariance_g1():
    before, after = _fragmentation_pair("G1")
    assert abs(before[0] - after[0]) < 1e-9
    assert abs(before[1] - after[1]) < 1e-9


def test_fragmentation_invariance_g2():
    before, after = _fragmentation_pair("G2")
    assert abs(before[0] - after[0]) < 1e-9
    assert abs(before[1] - after[1]) < 1e-9


def test_fragmentation_invariance_g3():
    before, after = _fragmentation_pair("G3")
    assert abs(before[0] - after[0]) < 1e-9
    assert abs(before[1] - after[1]) < 1e-9


def test_unrelated_source_does_not_change_existing_region():
    sources = generate_map()
    existing = sources[0]
    remote = SourceGroup("REMOTE.WOOD.00", "SOUTH", "WOOD", 1.0, 0.8)
    for granularity in ("G1", "G2", "G3"):
        before_table = bias_table(granularity, context_at(12.0), sources)
        after_table = bias_table(granularity, context_at(12.0), sources + [remote])
        before = source_intensity(existing, granularity, before_table)
        after = source_intensity(existing, granularity, after_table)
        assert abs(before[0] - after[0]) < 1e-9
        assert abs(before[1] - after[1]) < 1e-9


def test_context_change_is_smooth():
    samples = [resolve_spatial_class_bias(context_at(minute / 60.0)) for minute in range(0, 1441, 10)]
    max_delta = max(
        abs(samples[index][habitat] - samples[index - 1][habitat])
        for index in range(1, len(samples))
        for habitat in HABITAT_CLASSES
    )
    assert max_delta < 0.02


def test_feeding_resolver_removes_common_mode_without_touching_appetite_owner():
    base = PreyState(0.7, 1.3, 0.9)
    uplift = PreyState(1.4, 2.6, 1.8)
    assert resolve_feeding_bias(base) == resolve_feeding_bias(uplift)


def test_granularity_experiment_uses_one_45_source_map():
    result = granularity_comparison(context_at(12.0))
    assert result["G1"]["authoring_parameter_count"] == 3
    assert result["G2"]["authoring_parameter_count"] == 9
    assert result["G3"]["authoring_parameter_count"] == 45
    assert result["G1"]["far_distance_coupled_identities"] > 0
    assert result["G2"]["far_distance_coupled_identities"] == 0
    assert result["G3"]["far_distance_coupled_identities"] == 0


def test_o1_separated_observation_improves_search():
    result = observation_experiment(trials=500, seed=20260902)
    assert result["O1"]["correct_pattern_rate"] > result["O0"]["correct_pattern_rate"]
    assert result["O1"]["presence_as_response_or_inverse_rate"] < result["O0"]["presence_as_response_or_inverse_rate"]
    assert result["O1"]["misjudge_presence_as_response_rate"] < result["O0"]["misjudge_presence_as_response_rate"]
    assert result["O1"]["probes_per_correct_pattern"] < result["O0"]["probes_per_correct_pattern"]
