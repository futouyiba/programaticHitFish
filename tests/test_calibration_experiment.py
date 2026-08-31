import csv
from pathlib import Path

import pytest

from fcf_v1.calibration_experiment import (
    Category,
    GRADE_MAPS,
    aggregate_sources,
    calculate_engagement,
    cumulative_probability,
    generate_experiment,
    run_assertions,
)


def test_single_winner_probabilities_sum_with_no_engagement():
    result = calculate_engagement(
        [Category("A", 50_000, "NORMAL"), Category("B", 10_000, "HIGH"), Category("ignored", 90_000, "NONE")],
        100_000,
        GRADE_MAPS["Moderate"],
    )
    assert result.p_none + sum(result.absolute_probabilities.values()) == pytest.approx(1.0)
    assert result.absolute_probabilities["ignored"] == 0.0


def test_technical_source_aggregation_is_exactly_invariant():
    grade_map = GRADE_MAPS["Wide"]
    unsplit = calculate_engagement([Category("A", 100_000, "HIGH")], 100_000, grade_map)
    split = aggregate_sources(Category("A", 1_000, "HIGH") for _ in range(100))
    aggregated = calculate_engagement(split, 100_000, grade_map)
    assert aggregated == unsplit


def test_mode_split_and_none_addition_are_invariant():
    grade_map = GRADE_MAPS["Moderate"]
    reference = calculate_engagement([Category("A", 50_000, "NORMAL")], 100_000, grade_map)
    split = calculate_engagement(
        [Category("A_1", 25_000, "NORMAL"), Category("A_2", 25_000, "NORMAL"), Category("none", 1_000_000, "NONE")],
        100_000,
        grade_map,
    )
    assert split.p_any == pytest.approx(reference.p_any)
    assert sum(split.absolute_probabilities.values()) == pytest.approx(reference.absolute_probabilities["A"])


def test_required_analytical_assertions_pass():
    run_assertions()


def test_cumulative_probability_edges():
    assert cumulative_probability(0.0, 40) == 0.0
    assert cumulative_probability(1.0, 1) == 1.0
    assert cumulative_probability(0.2, 3) == pytest.approx(0.488)


def test_small_reproducible_run_writes_all_required_csvs(tmp_path: Path):
    first = tmp_path / "first"
    second = tmp_path / "second"
    generate_experiment(first, samples=10_000, seed=1234, plots=False)
    generate_experiment(second, samples=10_000, seed=1234, plots=False)
    required = {
        "summary.csv",
        "invariance.csv",
        "substitution.csv",
        "roster_saturation.csv",
        "cadence.csv",
        "conversion_reroll.csv",
        "gear_isolation.csv",
    }
    assert {path.name for path in (first / "results").glob("*.csv")} == required
    for name in required:
        assert (first / "results" / name).read_bytes() == (second / "results" / name).read_bytes()
        with (first / "results" / name).open(newline="", encoding="utf-8") as handle:
            assert list(csv.DictReader(handle))
