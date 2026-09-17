"""W6 contract tests for the 0.3.4.0-B fixed Bake template.

Test names are prefixed with the W6 task-packet test ID (T1..T10) they satisfy.
Numbers are the frozen Bass golden slice; the W6 migration must not move them.
"""
import inspect
import json
import math
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

import pytest

from fcf_v1.bake import (
    SECONDARY_LOSS_BUDGET,
    AGGREGATION_ROLES,
    BakeConfigError,
    BakeEvaluationResult,
    ConditionGroup,
    FixedBakeTemplateProgram,
    RoleTransition,
    aggregate_afla,
    apply_orchestration,
    migrate_legacy_binding,
    normalize_role_transition,
)
from fcf_v1.b_legacy_adapter import (
    LegacyStockReleaseRow,
    backfill_is_background_fish,
    build_opportunity_seeds,
    project_compat_mode_membership,
    resolve_opportunity_seed_from_legacy_row,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((ROOT / "authoring" / "bass_fixed_template_v0.json").read_text())
GROUP_FIXTURE = json.loads(
    (ROOT / "tests" / "fixtures" / "bass_fixed_template_condition_groups_v0.json").read_text()
)
PROGRAM = FixedBakeTemplateProgram()

CG_02_GOLDEN = 0.3256095471324488
CG_03_GOLDEN = 0.13775788532526678


def _subject() -> dict:
    return deepcopy(FIXTURE["resolvedSubject"])


def _seed() -> dict:
    return deepcopy(FIXTURE["resolvedOpportunitySeed"])


def _group(
    temp: float = 26.0,
    structure: str = "GRASS_EDGE",
    layers: tuple = ("MIDDLE",),
    period: str = "MORNING",
    cid: str = "TEST",
) -> ConditionGroup:
    return ConditionGroup(
        condition_group_id=cid,
        structure_type=structure,
        water_temperature_range=(float(temp), float(temp)),
        feeding_ecology_layers=tuple(layers),
        time_period=period,
    )


def _roles(result: BakeEvaluationResult) -> dict:
    return {f["conditionKey"]: f["aggregationRole"] for f in result.trace["factorResults"]}


def _assert_key_absent(node: Any, forbidden: set) -> None:
    if isinstance(node, Mapping):
        for key, value in node.items():
            assert key not in forbidden, f"unexpected key {key!r} in trace"
            _assert_key_absent(value, forbidden)
    elif isinstance(node, (list, tuple)):
        for item in node:
            _assert_key_absent(item, forbidden)


# --------------------------------------------------------------------------- #
# T10 Bass golden slice
# --------------------------------------------------------------------------- #


def test_t10_bass_q3_golden_condition_groups_do_not_drift():
    results = []
    for row in GROUP_FIXTURE["condition_groups"]:
        group = ConditionGroup(
            condition_group_id=row["id"],
            structure_type=row["structureType"],
            water_temperature_range=tuple(row["waterTemperatureRange"]),
            feeding_ecology_layers=tuple(row["feedingEcologyLayers"]),
            time_period=row["timePeriod"],
        )
        result = PROGRAM.evaluate(_subject(), _seed(), group)
        assert result.env_coeff == pytest.approx(row["expectedFinalEnvCoeff"], abs=1e-12)
        assert result.spatial_opportunity_intensity == pytest.approx(
            row["expectedFinalEnvCoeff"], abs=1e-12
        )
        results.append(result.env_coeff)

    assert results[0] == pytest.approx(1.0)
    assert results[0] > results[1] > results[2]
    assert results[1] == pytest.approx(CG_02_GOLDEN, abs=1e-12)
    assert results[2] == pytest.approx(CG_03_GOLDEN, abs=1e-12)


def test_t10_bass_roles_match_the_current_contract():
    subject = _subject()
    result = PROGRAM.evaluate(subject, _seed(), _group())
    assert _roles(result) == {
        "TEMPERATURE": "CORE",
        "STRUCTURE": "CORE",
        "FEEDING_LAYER": "SECONDARY",
    }
    assert result.trace["excludedConditions"] == ("TIME_PERIOD",)
    assert subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"] == {
        "aggregationRole": "EXCLUDED",
        "gatePolicy": "NONE",
    }


def test_t10_excluded_time_period_does_not_require_a_fake_profile():
    subject = _subject()
    assert "timePeriod" not in subject["resolvedComponentProfiles"]
    result = PROGRAM.evaluate(subject, _seed(), _group(structure="GRASS_EDGE", layers=("MIDDLE",)))
    assert result.env_coeff == pytest.approx(1.0)
    assert "TIME_PERIOD" not in _roles(result)


# --------------------------------------------------------------------------- #
# T1 CORE / SECONDARY / EXCLUDED
# --------------------------------------------------------------------------- #


def test_t1_core_enters_the_core_aggregate():
    result = PROGRAM.evaluate(_subject(), _seed(), _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    assert result.trace["coreLoss"] == pytest.approx(-math.log(13 / 22) - math.log(0.60))
    assert result.trace["coreLoss"] > 0


def test_t1_secondary_enters_the_bounded_secondary_aggregate_only():
    result = PROGRAM.evaluate(_subject(), _seed(), _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    assert result.trace["secondaryLossRaw"] == pytest.approx(-math.log(0.60) / 6.0)
    assert result.trace["secondaryLossApplied"] == pytest.approx(-math.log(0.60) / 6.0)
    assert result.trace["secondaryLossRaw"] < SECONDARY_LOSS_BUDGET
    # the SECONDARY contribution never reaches coreLoss
    assert result.trace["coreLoss"] == pytest.approx(-math.log(13 / 22) - math.log(0.60))


def test_t1_secondary_budget_is_bounded_not_additive():
    subject = _subject()
    for key in ("TEMPERATURE", "STRUCTURE", "FEEDING_LAYER", "TIME_PERIOD"):
        subject["resolvedSpatialOpportunityBindings"][key]["aggregationRole"] = "SECONDARY"
    subject["resolvedComponentProfiles"]["timePeriod"] = {"affinity": {"MORNING": 0.60}}

    result = PROGRAM.evaluate(subject, _seed(), _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    assert result.trace["secondaryLossRaw"] > SECONDARY_LOSS_BUDGET
    assert result.trace["secondaryLossApplied"] == pytest.approx(SECONDARY_LOSS_BUDGET)
    assert result.trace["coreLoss"] == 0.0
    assert result.env_coeff == pytest.approx(math.sqrt(0.60))


def test_t1_excluded_evaluator_does_not_run_and_cannot_contribute():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["aggregationRole"] = "EXCLUDED"
    result = PROGRAM.evaluate(subject, _seed(), _group(temp=40.0, structure="OPEN", layers=("SURFACE",)))

    assert "TEMPERATURE" not in _roles(result)
    assert result.trace["coreLoss"] == pytest.approx(-math.log(0.30))
    assert result.trace["gateResults"] == ()


# --------------------------------------------------------------------------- #
# T2 Gate legality
# --------------------------------------------------------------------------- #


def test_t2_core_with_none_gate_is_valid():
    result = PROGRAM.evaluate(_subject(), _seed(), _group())
    assert result.trace["gateResults"] == ()
    assert result.trace["gateFailureCap"] is None


def test_t2_core_with_an_allowed_gate_is_valid():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "LOW_RESIDUAL"
    result = PROGRAM.evaluate(subject, _seed(), _group(temp=26.0))
    gates = result.trace["gateResults"]
    assert len(gates) == 1
    assert gates[0]["conditionKey"] == "TEMPERATURE"
    assert gates[0]["passed"] is True
    assert gates[0]["failureCap"] == pytest.approx(0.05)


def test_t2_secondary_with_gate_is_invalid():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["FEEDING_LAYER"]["gatePolicy"] = "LOW_RESIDUAL"
    with pytest.raises(BakeConfigError, match="unless AggregationRole=CORE"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_t2_excluded_with_gate_is_invalid():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"]["gatePolicy"] = "HARD_EXCLUDE"
    with pytest.raises(BakeConfigError, match="unless AggregationRole=CORE"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_t2_gate_on_a_non_gate_capable_core_condition_is_invalid():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["STRUCTURE"]["gatePolicy"] = "LOW_RESIDUAL"
    with pytest.raises(BakeConfigError, match="GatePolicy unsupported for STRUCTURE"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_t2_unknown_gate_policy_is_invalid():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "ARBITRARY_0_2"
    with pytest.raises(BakeConfigError, match="invalid GatePolicy"):
        PROGRAM.evaluate(subject, _seed(), _group())


# --------------------------------------------------------------------------- #
# T3 Legacy role migration
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("legacy", [
    {"conditionRole": "OFF", "gatePolicy": "NONE"},
    {"conditionRole": "OFF"},
])
def test_t3_legacy_off_none_normalizes_to_excluded_none(legacy):
    assert migrate_legacy_binding(legacy) == {"aggregationRole": "EXCLUDED", "gatePolicy": "NONE"}


@pytest.mark.parametrize("gate", ["HARD_EXCLUDE", "TRACE_RESIDUAL", "LOW_RESIDUAL"])
def test_t3_legacy_off_with_gate_requires_an_explicit_decision(gate):
    with pytest.raises(BakeConfigError, match="explicit content migration"):
        migrate_legacy_binding({"conditionRole": "OFF", "gatePolicy": gate})


def test_t3_legacy_off_with_gate_is_never_silently_coerced():
    """The two wrong auto-migrations must both be unreachable."""
    for gate in ("HARD_EXCLUDE", "TRACE_RESIDUAL", "LOW_RESIDUAL"):
        try:
            migrated = migrate_legacy_binding({"conditionRole": "OFF", "gatePolicy": gate})
        except BakeConfigError:
            continue
        pytest.fail(f"legacy OFF + {gate} was silently coerced to {migrated}")


def test_t3_runtime_rejects_an_unmigrated_legacy_condition_role():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"] = {
        "conditionRole": "OFF",
        "gatePolicy": "NONE",
    }
    with pytest.raises(BakeConfigError, match="legacy ConditionRole must be migrated"):
        PROGRAM.evaluate(subject, _seed(), _group())


# --------------------------------------------------------------------------- #
# T4 Role transition (authoring / Draft layer, not runtime)
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("new_role", ["SECONDARY", "EXCLUDED"])
def test_t4_leaving_core_clears_the_draft_gate(new_role):
    transition = normalize_role_transition(
        {"aggregationRole": "CORE", "gatePolicy": "LOW_RESIDUAL"}, new_role
    )
    assert isinstance(transition, RoleTransition)
    assert transition.binding == {"aggregationRole": new_role, "gatePolicy": "NONE"}
    assert transition.cleared_gate_policy == "LOW_RESIDUAL"
    assert transition.notice is not None


def test_t4_returning_to_core_starts_from_none():
    transition = normalize_role_transition(
        {"aggregationRole": "SECONDARY", "gatePolicy": "NONE"}, "CORE"
    )
    assert transition.binding == {"aggregationRole": "CORE", "gatePolicy": "NONE"}
    assert transition.cleared_gate_policy is None


def test_t4_staying_in_core_keeps_the_gate():
    transition = normalize_role_transition(
        {"aggregationRole": "CORE", "gatePolicy": "LOW_RESIDUAL"}, "CORE"
    )
    assert transition.binding["gatePolicy"] == "LOW_RESIDUAL"


def test_t4_normalized_binding_is_always_current_legal():
    for new_role in sorted(AGGREGATION_ROLES):
        transition = normalize_role_transition(
            {"aggregationRole": "CORE", "gatePolicy": "HARD_EXCLUDE"}, new_role
        )
        if new_role == "CORE":
            assert transition.binding["gatePolicy"] == "HARD_EXCLUDE"
        else:
            assert transition.binding["gatePolicy"] == "NONE"


# --------------------------------------------------------------------------- #
# T5 Temperature
# --------------------------------------------------------------------------- #


def test_t5_temperature_uses_the_range_midpoint_as_a_point_fit():
    result = PROGRAM.evaluate(_subject(), _seed(), _group(temp=26.0))
    temp = next(f for f in result.trace["factorResults"] if f["conditionKey"] == "TEMPERATURE")
    assert temp["rawInputs"]["representativeTemp"] == pytest.approx(26.0)
    assert temp["rawFit"] == pytest.approx(1.0)

    # a wide range still resolves through its midpoint, not through its edges
    wide = ConditionGroup("WIDE", "GRASS_EDGE", (19.0, 33.0), ("MIDDLE",), "MORNING")
    wide_result = PROGRAM.evaluate(_subject(), _seed(), wide)
    wide_temp = next(
        f for f in wide_result.trace["factorResults"] if f["conditionKey"] == "TEMPERATURE"
    )
    assert wide_temp["rawInputs"]["representativeTemp"] == pytest.approx(26.0)
    assert wide_temp["rawFit"] == pytest.approx(1.0)


def test_t5_gate_and_fit_share_one_representative_temperature():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "TRACE_RESIDUAL"
    # only the midpoint (28C) is inside the preferred band; both edges are outside accept.
    group = ConditionGroup("WIDE_GATE", "GRASS_EDGE", (0.0, 56.0), ("MIDDLE",), "MORNING")
    result = PROGRAM.evaluate(subject, _seed(), group)

    temp = next(f for f in result.trace["factorResults"] if f["conditionKey"] == "TEMPERATURE")
    gate = next(g for g in result.trace["gateResults"] if g["conditionKey"] == "TEMPERATURE")
    assert temp["rawInputs"]["representativeTemp"] == pytest.approx(28.0)
    assert temp["rawFit"] == pytest.approx(1.0)
    assert gate["passed"] is True
    assert result.trace["gateFailureCap"] is None


def test_t5_no_mean_fit_or_max_fit_dual_track_exists():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "LOW_RESIDUAL"
    result = PROGRAM.evaluate(subject, _seed(), _group(temp=26.0))
    _assert_key_absent(result.trace, {"meanFit", "maxFit", "mean_fit", "max_fit"})


def test_t5_computed_temperature_fit_is_clamped_but_authored_affinity_is_not():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "LOW_RESIDUAL"
    result = PROGRAM.evaluate(subject, _seed(), _group(temp=36.0, structure="OPEN", layers=("SURFACE",)))
    temp = next(f for f in result.trace["factorResults"] if f["conditionKey"] == "TEMPERATURE")
    assert temp["rawFit"] == pytest.approx(0.0)
    assert temp["appliedFit"] == pytest.approx(0.05)


# --------------------------------------------------------------------------- #
# T6 Feeding Ecology Layer
# --------------------------------------------------------------------------- #


def test_t6_feeding_layer_is_an_array_resolved_by_max_affinity():
    subject = _subject()
    both = PROGRAM.evaluate(_subject(), _seed(), _group(layers=("SURFACE", "MIDDLE")))
    best = PROGRAM.evaluate(subject, _seed(), _group(layers=("MIDDLE",)))
    worst = PROGRAM.evaluate(subject, _seed(), _group(layers=("SURFACE",)))

    assert both.env_coeff == pytest.approx(best.env_coeff)
    assert both.env_coeff > worst.env_coeff


def test_t6_extra_layers_never_accumulate_a_bonus():
    subject = _subject()
    two = PROGRAM.evaluate(subject, _seed(), _group(layers=("SURFACE", "MIDDLE")))
    three = PROGRAM.evaluate(subject, _seed(), _group(layers=("SURFACE", "MIDDLE", "BOTTOM")))
    assert three.env_coeff == pytest.approx(two.env_coeff)


def test_t6_an_empty_layer_array_is_invalid():
    with pytest.raises(BakeConfigError, match="at least one FeedingEcologyLayer"):
        PROGRAM.evaluate(_subject(), _seed(), _group(layers=()))


def test_t6_an_unknown_layer_is_invalid():
    with pytest.raises(BakeConfigError, match="FEEDING_LAYER missing affinity"):
        PROGRAM.evaluate(_subject(), _seed(), _group(layers=("ABYSSAL",)))


# --------------------------------------------------------------------------- #
# T7 Background switch / Background Floor
# --------------------------------------------------------------------------- #


def test_t7_non_background_fish_cannot_carry_a_floor():
    seed = _seed()
    seed["envCoeffMin"] = 0.10
    with pytest.raises(BakeConfigError, match="unless isBackgroundFish=true"):
        PROGRAM.evaluate(_subject(), seed, _group())


def test_t7_non_background_fish_may_carry_a_disabled_zero_floor():
    seed = _seed()
    seed["envCoeffMin"] = 0.0
    result = PROGRAM.evaluate(_subject(), seed, _group())
    assert result.trace["envCoeffMin"] is None
    assert result.trace["backgroundFloorApplied"] is False


def test_t7_background_fish_requires_an_explicit_floor():
    seed = _seed()
    seed["isBackgroundFish"] = True
    with pytest.raises(BakeConfigError, match="requires an explicit envCoeffMin floor"):
        PROGRAM.evaluate(_subject(), seed, _group())


def test_t7_background_fish_rejects_an_out_of_range_floor():
    seed = _seed()
    seed["isBackgroundFish"] = True
    seed["envCoeffMin"] = 0.50
    with pytest.raises(BakeConfigError, match="invalid envCoeffMin"):
        PROGRAM.evaluate(_subject(), seed, _group())


def test_t7_floor_applies_only_when_no_gate_failed():
    seed = _seed()
    seed["isBackgroundFish"] = True
    seed["envCoeffMin"] = 0.10
    result = PROGRAM.evaluate(_subject(), seed, _group(temp=5.0, structure="OPEN", layers=("SURFACE",)))

    assert result.trace["rawEnvCoeff"] == pytest.approx(0.037570332361436386)
    assert result.env_coeff == pytest.approx(0.10)
    assert result.trace["backgroundFloorApplied"] is True


def test_t7_floor_cannot_resurrect_a_gate_failure():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "TRACE_RESIDUAL"
    seed = _seed()
    seed["isBackgroundFish"] = True
    seed["envCoeffMin"] = 0.10
    result = PROGRAM.evaluate(subject, seed, _group(temp=36.0, structure="OPEN", layers=("SURFACE",)))

    assert result.trace["gateFailureCap"] == pytest.approx(0.01)
    assert result.env_coeff <= 0.01
    assert result.trace["backgroundFloorApplied"] is False


def test_t7_the_legacy_backfill_rule_is_migration_only():
    assert backfill_is_background_fish(0.30) is True
    assert backfill_is_background_fish(0.0) is False

    # an explicit switch wins over the backfill rule: no runtime derivation
    row = LegacyStockReleaseRow(
        stock_id="STOCK",
        fish_id="BASS_Q3",
        fish_pond_ref="POND",
        species_id="LARGEMOUTH_BASS",
        fish_quality_id="Q3",
        prob_weight_ideal=1.0,
        min_env_coeff=0.30,
        min_adapt_coeff=0.30,
        is_background_fish=False,
    )
    seed = resolve_opportunity_seed_from_legacy_row(row)
    assert seed["isBackgroundFish"] is False
    assert "envCoeffMin" not in seed


# --------------------------------------------------------------------------- #
# T8 Base opportunity multiply
# --------------------------------------------------------------------------- #


def test_t8_base_multiplies_exactly_once():
    low_seed = _seed()
    high_seed = _seed()
    high_seed["baseOpportunityIntensity"] = 2.5

    low = PROGRAM.evaluate(_subject(), low_seed, _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    high = PROGRAM.evaluate(_subject(), high_seed, _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))

    assert high.trace["rawEnvCoeff"] == pytest.approx(low.trace["rawEnvCoeff"])
    assert high.env_coeff == pytest.approx(low.env_coeff)
    assert high.spatial_opportunity_intensity == pytest.approx(2.5 * low.spatial_opportunity_intensity)


def test_t8_base_never_enters_afla_or_env_coeff():
    assert list(inspect.signature(aggregate_afla).parameters) == ["evaluations"]
    assert list(inspect.signature(apply_orchestration).parameters) == [
        "aggregate",
        "evaluations",
        "base_opportunity_intensity",
        "is_background_fish",
        "env_coeff_min",
    ]


def test_t8_base_zero_stays_zero_even_with_a_background_floor():
    seed = _seed()
    seed["baseOpportunityIntensity"] = 0.0
    seed["isBackgroundFish"] = True
    seed["envCoeffMin"] = 0.10
    result = PROGRAM.evaluate(_subject(), seed, _group(temp=5.0, structure="OPEN", layers=("SURFACE",)))
    assert result.spatial_opportunity_intensity == 0.0


def test_t8_canonical_output_names():
    assert [f.name for f in BakeEvaluationResult.__dataclass_fields__.values()] == [
        "env_coeff",
        "spatial_opportunity_intensity",
        "trace",
    ]
    result = PROGRAM.evaluate(_subject(), _seed(), _group())
    assert "spatialOpportunityIntensity" in result.trace
    _assert_key_absent(result.trace, {"spatialDistributionWeight", "spatial_distribution_weight"})


# --------------------------------------------------------------------------- #
# T9 Pond x Quality / persistence seam
# --------------------------------------------------------------------------- #


def _row(**overrides) -> LegacyStockReleaseRow:
    base = dict(
        stock_id="STOCK_A",
        fish_id="BASS_Q3",
        fish_pond_ref="POND_1",
        species_id="LARGEMOUTH_BASS",
        fish_quality_id="Q3",
        prob_weight_ideal=1.0,
        min_env_coeff=0.30,
        min_adapt_coeff=0.30,
    )
    base.update(overrides)
    return LegacyStockReleaseRow(**base)


def test_t9_legacy_row_maps_prob_weight_ideal_to_base_opportunity():
    seed = resolve_opportunity_seed_from_legacy_row(_row(prob_weight_ideal=1.75))
    assert seed["baseOpportunityIntensity"] == pytest.approx(1.75)
    assert seed["fishPondRef"] == "POND_1"
    assert seed["fishQualityRef"] == {"speciesId": "LARGEMOUTH_BASS", "fishQualityId": "Q3"}


def test_t9_min_adapt_coeff_is_never_merged_into_the_environment_floor():
    a = resolve_opportunity_seed_from_legacy_row(_row(min_env_coeff=0.3, min_adapt_coeff=0.3))
    b = resolve_opportunity_seed_from_legacy_row(_row(min_env_coeff=0.3, min_adapt_coeff=0.9))
    assert a == b
    assert a["envCoeffMin"] == pytest.approx(0.3)


def test_t9_min_env_coeff_zero_disables_the_floor():
    seed = resolve_opportunity_seed_from_legacy_row(_row(min_env_coeff=0.0, min_adapt_coeff=0.0))
    assert seed["isBackgroundFish"] is False
    assert "envCoeffMin" not in seed


def test_t9_duplicate_pond_quality_seed_fails_fast():
    rows = [
        _row(stock_id="STOCK_A", fish_id="BASS_Q3"),
        _row(stock_id="STOCK_A", fish_id="BASS_Q3_ALT"),
    ]
    with pytest.raises(BakeConfigError, match="duplicate FishPond x FishQuality seed"):
        build_opportunity_seeds(rows)


def test_t9_distinct_pond_quality_pairs_build_distinct_seeds():
    rows = [
        _row(stock_id="STOCK_A", fish_id="BASS_Q3", fish_pond_ref="POND_1"),
        _row(stock_id="STOCK_B", fish_id="BASS_Q3", fish_pond_ref="POND_2"),
        _row(stock_id="STOCK_C", fish_id="BASS_Q5", fish_quality_id="Q5"),
    ]
    seeds = build_opportunity_seeds(rows)
    assert set(seeds) == {("POND_1", "Q3"), ("POND_2", "Q3"), ("POND_1", "Q5")}


def test_t9_compat_mode_membership_is_a_projection_not_a_second_truth():
    truth = {"Q3": "NORMAL", "Q5": "NORMAL", "Q7": "SUMMER"}
    projected = project_compat_mode_membership(truth)
    assert projected == {"NORMAL": ["Q3", "Q5"], "SUMMER": ["Q7"]}

    # a redundant copy of the same projection adds no new truth
    assert project_compat_mode_membership(truth, declared_membership=projected) == projected

    # a divergent second membership is rejected
    with pytest.raises(BakeConfigError, match="second independently editable"):
        project_compat_mode_membership(
            truth, declared_membership={"NORMAL": ["Q3"], "SUMMER": ["Q5", "Q7"]}
        )


def test_t9_seed_rejects_a_non_boolean_background_switch():
    seed = _seed()
    seed["isBackgroundFish"] = "false"
    with pytest.raises(BakeConfigError, match="isBackgroundFish must be a boolean"):
        PROGRAM.evaluate(_subject(), seed, _group())


# --------------------------------------------------------------------------- #
# Validation layering (W5 21.3 / F4)
# --------------------------------------------------------------------------- #


def test_validation_layering_excluded_still_validates_an_authored_profile():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["STRUCTURE"]["aggregationRole"] = "EXCLUDED"
    subject["resolvedComponentProfiles"]["structure"]["affinity"]["OPEN"] = 0.02
    with pytest.raises(BakeConfigError, match="authored affinity must be within"):
        PROGRAM.evaluate(subject, _seed(), _group(structure="GRASS_EDGE"))


def test_validation_layering_excluded_does_not_require_completeness():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"]["aggregationRole"] = "EXCLUDED"
    result = PROGRAM.evaluate(subject, _seed(), _group(period="MIDNIGHT"))
    assert "TIME_PERIOD" not in _roles(result)


# --------------------------------------------------------------------------- #
# DTO separation / template identity / determinism
# --------------------------------------------------------------------------- #


def test_subject_and_seed_truth_stay_separated():
    subject = _subject()
    subject["baseOpportunityIntensity"] = 0.5
    with pytest.raises(BakeConfigError, match="must not contain Pond-owned opportunity truth"):
        PROGRAM.evaluate(subject, _seed(), _group())

    seed = _seed()
    seed["resolvedComponentProfiles"] = {}
    with pytest.raises(BakeConfigError, match="must not contain fish-side profile"):
        PROGRAM.evaluate(_subject(), seed, _group())


def test_subject_and_seed_must_share_one_fish_quality_ref():
    seed = _seed()
    seed["fishQualityRef"] = {"speciesId": "LARGEMOUTH_BASS", "fishQualityId": "Q5"}
    with pytest.raises(BakeConfigError, match="fishQualityRef mismatch"):
        PROGRAM.evaluate(_subject(), seed, _group())


def test_missing_aggregation_role_is_not_silently_excluded():
    subject = _subject()
    del subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"]
    with pytest.raises(BakeConfigError, match="missing AggregationRole/GatePolicy: TIME_PERIOD"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_the_fixed_template_cannot_be_extended_by_authoring():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["CUSTOM_FACTOR"] = {
        "aggregationRole": "CORE",
        "gatePolicy": "NONE",
    }
    with pytest.raises(BakeConfigError, match="unknown fixed-template condition"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_an_active_condition_requires_its_profile():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TIME_PERIOD"]["aggregationRole"] = "CORE"
    with pytest.raises(BakeConfigError, match="TIME_PERIOD missing affinity"):
        PROGRAM.evaluate(subject, _seed(), _group())


def test_mapping_order_does_not_change_the_result():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"] = dict(
        reversed(list(subject["resolvedSpatialOpportunityBindings"].items()))
    )
    subject["resolvedComponentProfiles"] = dict(
        reversed(list(subject["resolvedComponentProfiles"].items()))
    )
    group = ConditionGroup("ORDER", "DROPOFF", (15.0, 15.0), ("BOTTOM",), "MORNING")
    result = PROGRAM.evaluate(subject, _seed(), group)
    assert result.env_coeff == pytest.approx(CG_02_GOLDEN, abs=1e-12)


def test_replay_is_deterministic():
    first = PROGRAM.evaluate(_subject(), _seed(), _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    second = PROGRAM.evaluate(_subject(), _seed(), _group(temp=15.0, structure="DROPOFF", layers=("BOTTOM",)))
    assert first.trace == second.trace


def test_worsening_a_core_factor_never_increases_env_coeff():
    preferred = PROGRAM.evaluate(_subject(), _seed(), _group(structure="GRASS_EDGE"))
    dropoff = PROGRAM.evaluate(_subject(), _seed(), _group(structure="DROPOFF"))
    open_water = PROGRAM.evaluate(_subject(), _seed(), _group(structure="OPEN"))
    assert preferred.env_coeff > dropoff.env_coeff > open_water.env_coeff


def test_gate_consequence_only_caps_downwards():
    subject = _subject()
    subject["resolvedSpatialOpportunityBindings"]["TEMPERATURE"]["gatePolicy"] = "LOW_RESIDUAL"
    result = PROGRAM.evaluate(subject, _seed(), _group(temp=36.0, structure="OPEN", layers=("SURFACE",)))

    assert result.trace["gateFailureCap"] == pytest.approx(0.05)
    assert result.trace["rawEnvCoeff"] == pytest.approx(0.013775788532526681)
    assert result.env_coeff == pytest.approx(result.trace["rawEnvCoeff"])
    assert result.env_coeff < 0.05
