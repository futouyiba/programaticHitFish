"""Executable numeric experiment for the FCF Simplified V0 calibration proposal.

This module intentionally contains only the model and fixtures defined by the
experiment specification.  It does not alter the executable FCF V1 baseline.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


REFERENCE_EXPOSURE = 100_000.0
DEFAULT_SEED = 20_260_831
DEFAULT_SAMPLES = 1_000_000

GRADES: Tuple[str, ...] = ("NONE", "LOW", "NORMAL", "HIGH", "VERY_HIGH")
GRADE_MAPS: Mapping[str, Mapping[str, float]] = {
    "Compressed": {"NONE": 0.0, "LOW": 0.6, "NORMAL": 1.0, "HIGH": 1.5, "VERY_HIGH": 2.0},
    "Moderate": {"NONE": 0.0, "LOW": 0.25, "NORMAL": 1.0, "HIGH": 2.0, "VERY_HIGH": 4.0},
    "Wide": {"NONE": 0.0, "LOW": 0.1, "NORMAL": 1.0, "HIGH": 3.0, "VERY_HIGH": 8.0},
}
K_RATIOS: Tuple[float, ...] = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
ROSTER_COUNTS: Tuple[int, ...] = (1, 2, 3, 5, 10, 20, 28, 50, 100)
ROSTER_PRESSURES: Tuple[float, ...] = (0.01, 0.025, 0.05, 0.1, 0.25, 0.5)


@dataclass(frozen=True)
class Category:
    name: str
    exposure: float
    grade: str


@dataclass(frozen=True)
class EngagementResult:
    total_weight: float
    p_any: float
    absolute_probabilities: Mapping[str, float]

    @property
    def p_none(self) -> float:
        return 1.0 - self.p_any


def aggregate_sources(sources: Iterable[Category]) -> List[Category]:
    """Aggregate technical source splits back to category exposure."""
    exposure_by_key: Dict[Tuple[str, str], float] = {}
    for source in sources:
        if source.exposure < 0:
            raise ValueError("exposure must be non-negative")
        if source.grade not in GRADES:
            raise ValueError("unknown response grade: %s" % source.grade)
        key = (source.name, source.grade)
        exposure_by_key[key] = exposure_by_key.get(key, 0.0) + source.exposure
    return [Category(name, exposure, grade) for (name, grade), exposure in exposure_by_key.items()]


def calculate_engagement(
    categories: Sequence[Category], k: float, grade_map: Mapping[str, float]
) -> EngagementResult:
    if k <= 0:
        raise ValueError("K must be positive")
    weights: List[Tuple[str, float]] = []
    for category in categories:
        if category.exposure < 0:
            raise ValueError("exposure must be non-negative")
        if category.grade not in grade_map:
            raise ValueError("grade is absent from grade map: %s" % category.grade)
        weights.append((category.name, category.exposure * grade_map[category.grade]))

    total_weight = math.fsum(weight for _, weight in weights)
    p_any = total_weight / (k + total_weight)
    absolute: Dict[str, float] = {}
    if total_weight:
        for name, weight in weights:
            absolute[name] = absolute.get(name, 0.0) + p_any * weight / total_weight
    else:
        for name, _ in weights:
            absolute.setdefault(name, 0.0)
    return EngagementResult(total_weight, p_any, absolute)


def cumulative_probability(p: float, attempts: int) -> float:
    if not 0.0 <= p <= 1.0:
        raise ValueError("probability must be in [0, 1]")
    if attempts < 0:
        raise ValueError("attempts must be non-negative")
    return 1.0 - (1.0 - p) ** attempts


def _simulate_categorical(result: EngagementResult, samples: int, rng) -> Tuple[float, Dict[str, float]]:
    labels = list(result.absolute_probabilities)
    probabilities = [result.absolute_probabilities[label] for label in labels]
    probabilities.append(result.p_none)
    counts = rng.multinomial(samples, probabilities)
    absolute = {label: counts[index] / samples for index, label in enumerate(labels)}
    simulated_any = sum(counts[:-1]) / samples
    _assert_mc_probability(simulated_any, result.p_any, samples)
    for label in labels:
        _assert_mc_probability(absolute[label], result.absolute_probabilities[label], samples)
    return simulated_any, absolute


def _simulate_bernoulli(p: float, samples: int, rng) -> float:
    simulated = float(rng.binomial(samples, p)) / samples
    _assert_mc_probability(simulated, p, samples)
    return simulated


def _assert_mc_probability(simulated: float, analytical: float, samples: int) -> None:
    standard_error = math.sqrt(analytical * (1.0 - analytical) / samples)
    tolerance = max(7.0 * standard_error, 7.0 / samples)
    if abs(simulated - analytical) > tolerance:
        raise AssertionError(
            "Monte Carlo deviation %.8f exceeds tolerance %.8f for p=%.8f, n=%d"
            % (abs(simulated - analytical), tolerance, analytical, samples)
        )


def _assert_close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError("%r != %r within %r" % (actual, expected, tolerance))


def run_assertions() -> None:
    """Run the eight deterministic assertions required by the spec."""
    for map_name, grade_map in GRADE_MAPS.items():
        for k_ratio in K_RATIOS:
            k = REFERENCE_EXPOSURE * k_ratio
            unsplit = calculate_engagement([Category("A", 100_000.0, "NORMAL")], k, grade_map)
            split = calculate_engagement(
                [Category("A_mode_1", 50_000.0, "NORMAL"), Category("A_mode_2", 50_000.0, "NORMAL")],
                k,
                grade_map,
            )
            _assert_close(split.p_any, unsplit.p_any)
            _assert_close(sum(split.absolute_probabilities.values()), unsplit.absolute_probabilities["A"])

            with_none = calculate_engagement(
                [Category("A", 100_000.0, "NORMAL"), Category("none_1", 50_000.0, "NONE"), Category("none_2", 1.0, "NONE")],
                k,
                grade_map,
            )
            _assert_close(with_none.p_any, unsplit.p_any)
            _assert_close(with_none.absolute_probabilities["A"], unsplit.absolute_probabilities["A"])
            _assert_close(with_none.p_none + sum(with_none.absolute_probabilities.values()), 1.0)

            grade_values = [
                calculate_engagement([Category("A", 50_000.0, grade)], k, grade_map).p_any
                for grade in GRADES
            ]
            if grade_values != sorted(grade_values):
                raise AssertionError("grade monotonicity failed for %s" % map_name)
            exposure_values = [
                calculate_engagement([Category("A", exposure, "NORMAL")], k, grade_map).p_any
                for exposure in (0.0, 1.0, 10_000.0, 50_000.0, 100_000.0)
            ]
            if exposure_values != sorted(exposure_values):
                raise AssertionError("exposure monotonicity failed for %s" % map_name)


def _write_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError("refusing to write empty CSV: %s" % path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _invariance_rows() -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    technical_splits = {
        "unsplit": [100_000.0],
        "50k_plus_50k": [50_000.0, 50_000.0],
        "10x10k": [10_000.0] * 10,
        "100x1k": [1_000.0] * 100,
    }
    for map_name, grade_map in GRADE_MAPS.items():
        for k_ratio in K_RATIOS:
            k = REFERENCE_EXPOSURE * k_ratio
            reference = calculate_engagement([Category("A", 100_000.0, "NORMAL")], k, grade_map)
            for case_name, pieces in technical_splits.items():
                aggregated = aggregate_sources(Category("A", piece, "NORMAL") for piece in pieces)
                result = calculate_engagement(aggregated, k, grade_map)
                difference = result.p_any - reference.p_any
                rows.append({
                    "assertion": "technical_split_p_any_invariant",
                    "grade_map": map_name,
                    "k_ratio": k_ratio,
                    "case": case_name,
                    "p_any": result.p_any,
                    "combined_absolute_probability": sum(result.absolute_probabilities.values()),
                    "reference_value": reference.p_any,
                    "difference": difference,
                    "passed": abs(difference) <= 1e-12,
                })

            mode_split = calculate_engagement(
                [Category("A_mode_1", 25_000.0, "NORMAL"), Category("A_mode_2", 25_000.0, "NORMAL")],
                k,
                grade_map,
            )
            mode_reference = calculate_engagement([Category("A", 50_000.0, "NORMAL")], k, grade_map)
            for assertion, actual, expected in (
                ("mode_split_p_any_invariant", mode_split.p_any, mode_reference.p_any),
                ("mode_split_combined_absolute_invariant", sum(mode_split.absolute_probabilities.values()), mode_reference.p_any),
            ):
                rows.append({
                    "assertion": assertion,
                    "grade_map": map_name,
                    "k_ratio": k_ratio,
                    "case": "25k_plus_25k_vs_50k",
                    "p_any": mode_split.p_any,
                    "combined_absolute_probability": sum(mode_split.absolute_probabilities.values()),
                    "reference_value": expected,
                    "difference": actual - expected,
                    "passed": math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12),
                })

            with_none = calculate_engagement(
                [Category("A", 50_000.0, "NORMAL"), Category("none_1", 25_000.0, "NONE"), Category("none_2", 75_000.0, "NONE")],
                k,
                grade_map,
            )
            rows.append({
                "assertion": "none_addition_invariant",
                "grade_map": map_name,
                "k_ratio": k_ratio,
                "case": "two_none_categories",
                "p_any": with_none.p_any,
                "combined_absolute_probability": sum(with_none.absolute_probabilities.values()),
                "reference_value": mode_reference.p_any,
                "difference": with_none.p_any - mode_reference.p_any,
                "passed": math.isclose(with_none.p_any, mode_reference.p_any, rel_tol=1e-12, abs_tol=1e-12),
            })
    return rows


def _substitution_rows(samples: int, rng) -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    for map_name, grade_map in GRADE_MAPS.items():
        for k_ratio in K_RATIOS:
            k = REFERENCE_EXPOSURE * k_ratio
            baseline = calculate_engagement(
                [Category("A", 50_000.0, "NORMAL"), Category("B", 10_000.0, "HIGH")], k, grade_map
            )
            for direction in ("vary_A", "vary_B"):
                fixed_category = "B" if direction == "vary_A" else "A"
                baseline_fixed = baseline.absolute_probabilities[fixed_category]
                for varied_grade in GRADES:
                    categories = (
                        [Category("A", 50_000.0, varied_grade), Category("B", 10_000.0, "HIGH")]
                        if direction == "vary_A"
                        else [Category("A", 50_000.0, "NORMAL"), Category("B", 10_000.0, varied_grade)]
                    )
                    result = calculate_engagement(categories, k, grade_map)
                    sim_any, sim_absolute = _simulate_categorical(result, samples, rng)
                    fixed_probability = result.absolute_probabilities[fixed_category]
                    pct_change = 0.0 if baseline_fixed == 0 else 100.0 * (fixed_probability / baseline_fixed - 1.0)
                    rows.append({
                        "grade_map": map_name,
                        "k_ratio": k_ratio,
                        "direction": direction,
                        "varied_grade": varied_grade,
                        "fixed_category": fixed_category,
                        "p_any_analytical": result.p_any,
                        "p_any_simulated": sim_any,
                        "a_probability_analytical": result.absolute_probabilities.get("A", 0.0),
                        "a_probability_simulated": sim_absolute.get("A", 0.0),
                        "b_probability_analytical": result.absolute_probabilities.get("B", 0.0),
                        "b_probability_simulated": sim_absolute.get("B", 0.0),
                        "fixed_probability_baseline": baseline_fixed,
                        "fixed_probability_pct_change": pct_change,
                    })
    return rows


def _roster_rows(samples: int, rng) -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    for count in ROSTER_COUNTS:
        for pressure in ROSTER_PRESSURES:
            p_any = count * pressure / (1.0 + count * pressure)
            rows.append({
                "category_count": count,
                "per_category_w_over_k": pressure,
                "p_any_analytical": p_any,
                "p_any_simulated": _simulate_bernoulli(p_any, samples, rng),
                "per_category_absolute_probability": p_any / count,
            })
    return rows


def _cadence_rows(samples: int, rng) -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    probabilities = (0.01, 0.02, 0.05, 0.1, 0.2, 0.4)
    rates = (1, 2, 3, 5, 10, 20, 40, 60)
    for p in probabilities:
        for rate in rates:
            p_at_least_one = cumulative_probability(p, rate)
            session_count = max(1, math.ceil(samples / (60 * rate)))
            session_engagements = rng.binomial(60 * rate, p, size=session_count)
            minute_count = max(1, math.ceil(samples / rate))
            minutes_with_engagement = rng.binomial(rate, p, size=minute_count) > 0
            simulated_rate = float(session_engagements.mean()) / 60.0
            rate_standard_error = math.sqrt(rate * p * (1.0 - p) / (60.0 * session_count))
            if abs(simulated_rate - rate * p) > max(7.0 * rate_standard_error, 7.0 / samples):
                raise AssertionError("60-minute cadence Monte Carlo deviation exceeded tolerance")
            simulated_any = float(minutes_with_engagement.mean())
            _assert_mc_probability(simulated_any, p_at_least_one, minute_count)
            rows.append({
                "record_type": "opportunity_cadence",
                "p_per_opportunity": p,
                "opportunities_per_minute": rate,
                "expected_engagements_per_minute_analytical": rate * p,
                "expected_engagements_per_minute_simulated": simulated_rate,
                "p_at_least_one_per_minute_analytical": p_at_least_one,
                "p_at_least_one_per_minute_simulated": simulated_any,
                "mc_60_minute_sessions": session_count,
                "mc_equivalent_opportunities": session_count * 60 * rate,
                "rate_a_over_rate_b": "",
                "p_a_over_p_b": "",
                "weaker_per_event_b_stronger_per_minute": "",
            })

    rate_b = 10
    p_b = 0.05
    for rate_ratio in (0.5, 0.2, 0.1):
        for p_ratio in (1.5, 2.0, 3.0, 5.0):
            rate_a = rate_b * rate_ratio
            p_a = p_b * p_ratio
            expected_a = rate_a * p_a
            expected_b = rate_b * p_b
            trials = samples
            sim_a = _simulate_bernoulli(p_a, trials, rng) * rate_a
            sim_b = _simulate_bernoulli(p_b, trials, rng) * rate_b
            rows.append({
                "record_type": "technique_comparison",
                "p_per_opportunity": "",
                "opportunities_per_minute": "",
                "expected_engagements_per_minute_analytical": "",
                "expected_engagements_per_minute_simulated": "",
                "p_at_least_one_per_minute_analytical": "",
                "p_at_least_one_per_minute_simulated": "",
                "mc_60_minute_sessions": "",
                "mc_equivalent_opportunities": trials * 2,
                "rate_a_over_rate_b": rate_ratio,
                "p_a_over_p_b": p_ratio,
                "rate_a": rate_a,
                "rate_b": rate_b,
                "p_a": p_a,
                "p_b": p_b,
                "engagements_per_minute_a_analytical": expected_a,
                "engagements_per_minute_b_analytical": expected_b,
                "engagements_per_minute_a_simulated": sim_a,
                "engagements_per_minute_b_simulated": sim_b,
                "weaker_per_event_b_stronger_per_minute": expected_b > expected_a,
            })
    return rows


def _conversion_rows(samples: int, rng) -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    probabilities = (0.01, 0.05, 0.1, 0.2, 0.4, 0.7)
    attempt_counts = (1, 2, 3, 5, 10, 20, 40)
    family_count = 4
    for p in probabilities:
        for requested_attempts in attempt_counts:
            synthetic_labels = tuple("event_family_%d" % (index % family_count) for index in range(requested_attempts))
            for gate in ("G1_unlimited", "G2_max_3", "G3_distinct_event_family"):
                effective_attempts = {
                    "G1_unlimited": requested_attempts,
                    "G2_max_3": min(requested_attempts, 3),
                    "G3_distinct_event_family": len(set(synthetic_labels)),
                }[gate]
                probability = cumulative_probability(p, effective_attempts)
                rows.append({
                    "p_convert": p,
                    "requested_attempts": requested_attempts,
                    "gate": gate,
                    "synthetic_event_family_count": family_count if gate == "G3_distinct_event_family" else "",
                    "effective_attempts": effective_attempts,
                    "p_at_least_one_conversion_analytical": probability,
                    "p_at_least_one_conversion_simulated": _simulate_bernoulli(probability, samples, rng),
                })
    return rows


def _gear_isolation_rows(samples: int, rng) -> List[Mapping[str, object]]:
    engagement_probability = 0.2
    fixed_conversion = 0.5
    fixed_contact = 0.8
    fixed_hook = 0.5
    sweep_values = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0)

    engagement_draw = rng.random(samples)
    species_draw = rng.random(samples)
    conversion_draw = rng.random(samples)
    contact_draw = rng.random(samples)
    hook_draw = rng.random(samples)
    engaged = engagement_draw < engagement_probability
    species_a = engaged & (species_draw < 0.7)
    species_b = engaged & ~species_a

    rows: List[Mapping[str, object]] = []
    hook_reference = None
    for hook_probability in sweep_values:
        converted = engaged & (conversion_draw < fixed_conversion)
        attacked = converted & (contact_draw < fixed_contact)
        hooked = attacked & (hook_draw < hook_probability)
        counters = (int(engaged.sum()), int(species_a.sum()), int(species_b.sum()), int(attacked.sum()))
        if hook_reference is None:
            hook_reference = counters
        elif counters != hook_reference:
            raise AssertionError("Hook-only change modified an upstream counter")
        rows.append({
            "sweep_stage": "HookCompatibility",
            "varied_probability": hook_probability,
            "engagement_probability": engagement_probability,
            "conversion_probability": fixed_conversion,
            "contact_probability": fixed_contact,
            "hook_probability": hook_probability,
            "engagement_count_analytical": samples * engagement_probability,
            "engaged_species_a_count_analytical": samples * engagement_probability * 0.7,
            "engaged_species_b_count_analytical": samples * engagement_probability * 0.3,
            "attack_count_analytical": samples * engagement_probability * fixed_conversion * fixed_contact,
            "hooked_count_analytical": samples * engagement_probability * fixed_conversion * fixed_contact * hook_probability,
            "engagement_count": counters[0],
            "engaged_species_a_count": counters[1],
            "engaged_species_b_count": counters[2],
            "attack_count": counters[3],
            "hooked_count": int(hooked.sum()),
        })

    conversion_reference = None
    for conversion_probability in sweep_values:
        converted = engaged & (conversion_draw < conversion_probability)
        attacked = converted & (contact_draw < fixed_contact)
        hooked = attacked & (hook_draw < fixed_hook)
        counters = (int(engaged.sum()), int(species_a.sum()), int(species_b.sum()))
        if conversion_reference is None:
            conversion_reference = counters
        elif counters != conversion_reference:
            raise AssertionError("Conversion-only change modified Engagement counters")
        rows.append({
            "sweep_stage": "Conversion",
            "varied_probability": conversion_probability,
            "engagement_probability": engagement_probability,
            "conversion_probability": conversion_probability,
            "contact_probability": fixed_contact,
            "hook_probability": fixed_hook,
            "engagement_count_analytical": samples * engagement_probability,
            "engaged_species_a_count_analytical": samples * engagement_probability * 0.7,
            "engaged_species_b_count_analytical": samples * engagement_probability * 0.3,
            "attack_count_analytical": samples * engagement_probability * conversion_probability * fixed_contact,
            "hooked_count_analytical": samples * engagement_probability * conversion_probability * fixed_contact * fixed_hook,
            "engagement_count": counters[0],
            "engaged_species_a_count": counters[1],
            "engaged_species_b_count": counters[2],
            "attack_count": int(attacked.sum()),
            "hooked_count": int(hooked.sum()),
        })

    if int(engaged.sum()) != rows[0]["engagement_count"]:
        raise AssertionError("engagement accounting mismatch")
    return rows


def _summary_rows(samples: int, rng, substitution_rows, roster_rows, cadence_rows, conversion_rows) -> List[Mapping[str, object]]:
    rows: List[Mapping[str, object]] = []
    pressure_grid = (0.0, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
    for map_name, grade_map in GRADE_MAPS.items():
        for k_ratio in K_RATIOS:
            k = REFERENCE_EXPOSURE * k_ratio
            for pressure in pressure_grid:
                weight = pressure * REFERENCE_EXPOSURE
                p_any = weight / (k + weight)
                rows.append({
                    "record_type": "engagement_saturation",
                    "grade_map": map_name,
                    "k_ratio": k_ratio,
                    "grade": "NORMAL",
                    "input_value": pressure,
                    "input_unit": "W_over_reference_exposure",
                    "analytical_value": p_any,
                    "simulated_value": _simulate_bernoulli(p_any, samples, rng),
                    "metric": "P_any",
                    "reopen_signal": "",
                })
            for grade in GRADES:
                result = calculate_engagement([Category("A", REFERENCE_EXPOSURE, grade)], k, grade_map)
                rows.append({
                    "record_type": "grade_map_sensitivity",
                    "grade_map": map_name,
                    "k_ratio": k_ratio,
                    "grade": grade,
                    "input_value": REFERENCE_EXPOSURE,
                    "input_unit": "exposure",
                    "analytical_value": result.p_any,
                    "simulated_value": _simulate_bernoulli(result.p_any, samples, rng),
                    "metric": "P_any",
                    "reopen_signal": "",
                })

    max_substitution = max(abs(float(row["fixed_probability_pct_change"])) for row in substitution_rows)
    first_roster_90 = min(
        (int(row["category_count"]) for row in roster_rows if float(row["p_any_analytical"]) >= 0.9),
        default=None,
    )
    inversions = sum(
        bool(row["weaker_per_event_b_stronger_per_minute"])
        for row in cadence_rows
        if row["record_type"] == "technique_comparison"
    )
    first_unlimited_90 = min(
        (
            int(row["requested_attempts"])
            for row in conversion_rows
            if row["gate"] == "G1_unlimited" and float(row["p_at_least_one_conversion_analytical"]) >= 0.9
        ),
        default=None,
    )
    signal_values = (
        ("max_abs_fixed_category_substitution_change_pct", max_substitution, "percent"),
        ("first_roster_count_reaching_p_any_0_9_in_grid", first_roster_90, "categories"),
        ("technique_grid_cadence_inversion_count", inversions, "of_12_pairs"),
        ("first_unlimited_attempt_count_reaching_conversion_0_9_in_grid", first_unlimited_90, "attempts"),
    )
    for metric, value, unit in signal_values:
        rows.append({
            "record_type": "reopen_signal",
            "grade_map": "",
            "k_ratio": "",
            "grade": "",
            "input_value": "",
            "input_unit": unit,
            "analytical_value": value if value is not None else "not_reached_in_grid",
            "simulated_value": "",
            "metric": metric,
            "reopen_signal": True,
        })
    return rows


def _plot_results(base_dir: Path, summary_rows, substitution_rows, roster_rows, cadence_rows, conversion_rows) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    figures = base_dir / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")

    saturation = [row for row in summary_rows if row["record_type"] == "engagement_saturation" and row["grade_map"] == "Moderate"]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for k_ratio in K_RATIOS:
        selected = [row for row in saturation if row["k_ratio"] == k_ratio]
        ax.plot([row["input_value"] for row in selected], [row["analytical_value"] for row in selected], marker="o", label="K/ref=%g" % k_ratio)
    ax.set(xscale="symlog", xlabel="Total W / ReferenceExposure", ylabel="P(any)", title="Engagement saturation curves")
    ax.legend(ncol=2)
    fig.tight_layout()
    fig.savefig(figures / "engagement_saturation_curves.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    for axis, direction, fixed in zip(axes, ("vary_A", "vary_B"), ("B", "A")):
        for map_name in GRADE_MAPS:
            selected = [row for row in substitution_rows if row["direction"] == direction and row["grade_map"] == map_name and row["k_ratio"] == 1.0]
            axis.plot(GRADES, [row["fixed_probability_pct_change"] for row in selected], marker="o", label=map_name)
        axis.axhline(0, color="black", linewidth=0.8)
        axis.set(title="%s; fixed %s" % (direction, fixed), xlabel="Varied grade", ylabel="Fixed-category absolute P change (%)")
        axis.tick_params(axis="x", rotation=25)
    axes[1].legend()
    fig.suptitle("Mixed-species substitution (K / reference = 1)")
    fig.tight_layout()
    fig.savefig(figures / "mixed_species_substitution_curves.png", dpi=180)
    plt.close(fig)

    roster_matrix = np.array([[next(float(row["p_any_analytical"]) for row in roster_rows if row["category_count"] == count and row["per_category_w_over_k"] == pressure) for pressure in ROSTER_PRESSURES] for count in ROSTER_COUNTS])
    fig, ax = plt.subplots(figsize=(8, 6))
    image = ax.imshow(roster_matrix, aspect="auto", origin="lower", vmin=0, vmax=1, cmap="viridis")
    ax.set(xticks=range(len(ROSTER_PRESSURES)), xticklabels=ROSTER_PRESSURES, yticks=range(len(ROSTER_COUNTS)), yticklabels=ROSTER_COUNTS, xlabel="Per-category w / K", ylabel="Responding category count N", title="Roster saturation: P(any)")
    fig.colorbar(image, ax=ax, label="P(any)")
    fig.tight_layout()
    fig.savefig(figures / "roster_saturation_heatmap.png", dpi=180)
    plt.close(fig)

    opportunity_rows = [row for row in cadence_rows if row["record_type"] == "opportunity_cadence"]
    p_values = (0.01, 0.02, 0.05, 0.1, 0.2, 0.4)
    rate_values = (1, 2, 3, 5, 10, 20, 40, 60)
    cadence_matrix = np.array([[next(float(row["expected_engagements_per_minute_analytical"]) for row in opportunity_rows if row["p_per_opportunity"] == p and row["opportunities_per_minute"] == rate) for rate in rate_values] for p in p_values])
    any_matrix = np.array([[next(float(row["p_at_least_one_per_minute_analytical"]) for row in opportunity_rows if row["p_per_opportunity"] == p and row["opportunities_per_minute"] == rate) for rate in rate_values] for p in p_values])
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    image = axes[0].imshow(cadence_matrix, aspect="auto", origin="lower", cmap="magma")
    axes[0].set(xticks=range(len(rate_values)), xticklabels=rate_values, yticks=range(len(p_values)), yticklabels=["%g%%" % (100 * p) for p in p_values], xlabel="Opportunities / minute", ylabel="p per opportunity", title="Expected engagements / minute")
    fig.colorbar(image, ax=axes[0], label="Expected engagements / minute")
    image = axes[1].imshow(any_matrix, aspect="auto", origin="lower", vmin=0, vmax=1, cmap="viridis")
    axes[1].set(xticks=range(len(rate_values)), xticklabels=rate_values, yticks=range(len(p_values)), yticklabels=["%g%%" % (100 * p) for p in p_values], xlabel="Opportunities / minute", ylabel="p per opportunity", title="P(at least one engagement / minute)")
    fig.colorbar(image, ax=axes[1], label="Probability")
    fig.suptitle("Opportunity cadence surface")
    fig.tight_layout()
    fig.savefig(figures / "opportunity_cadence_heatmap.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), sharey=True)
    for axis, gate, title in zip(
        axes,
        ("G1_unlimited", "G2_max_3", "G3_distinct_event_family"),
        ("G1 unlimited", "G2 max 3", "G3 distinct family"),
    ):
        for p in (0.01, 0.05, 0.1, 0.2, 0.4, 0.7):
            selected = [row for row in conversion_rows if row["p_convert"] == p and row["gate"] == gate]
            axis.plot([row["requested_attempts"] for row in selected], [row["p_at_least_one_conversion_analytical"] for row in selected], marker="o", label="p=%g" % p)
        axis.set(xlabel="Requested eligible attempts", title=title, ylim=(0, 1.02))
    axes[0].set_ylabel("P(at least one conversion)")
    axes[-1].legend(ncol=2, fontsize=8)
    fig.suptitle("Conversion reroll curves by encounter gate")
    fig.tight_layout()
    fig.savefig(figures / "conversion_reroll_curves.png", dpi=180)
    plt.close(fig)

    sensitivity = [row for row in summary_rows if row["record_type"] == "grade_map_sensitivity" and row["k_ratio"] == 1.0]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for map_name in GRADE_MAPS:
        selected = [row for row in sensitivity if row["grade_map"] == map_name]
        ax.plot(GRADES, [row["analytical_value"] for row in selected], marker="o", label=map_name)
    ax.set(xlabel="ResponseGrade", ylabel="P(any)", title="Grade-map sensitivity (Exposure = K = ReferenceExposure)", ylim=(0, 1.02))
    ax.legend()
    fig.tight_layout()
    fig.savefig(figures / "grade_map_sensitivity.png", dpi=180)
    plt.close(fig)


def _write_observation_readme(base_dir: Path, summary_rows, substitution_rows, roster_rows, cadence_rows, conversion_rows, samples: int, seed: int) -> None:
    max_sub = max(substitution_rows, key=lambda row: abs(float(row["fixed_probability_pct_change"])))
    roster_90 = [row for row in roster_rows if float(row["p_any_analytical"]) >= 0.9]
    inversions = [row for row in cadence_rows if row["record_type"] == "technique_comparison" and row["weaker_per_event_b_stronger_per_minute"]]
    conversion_90 = [row for row in conversion_rows if row["gate"] == "G1_unlimited" and float(row["p_at_least_one_conversion_analytical"]) >= 0.9]
    max_mc_error = 0.0
    for row in summary_rows:
        if isinstance(row.get("simulated_value"), float):
            max_mc_error = max(max_mc_error, abs(float(row["analytical_value"]) - float(row["simulated_value"])))

    roster_text = "not reached in the requested grid"
    if roster_90:
        first = min(roster_90, key=lambda row: int(row["category_count"]))
        roster_text = "first appears at N=%s (pressure=%s)" % (first["category_count"], first["per_category_w_over_k"])
    conversion_text = "not reached in the requested grid"
    if conversion_90:
        first_conversion = min(conversion_90, key=lambda row: int(row["requested_attempts"]))
        conversion_text = "first appears at p=%s, N=%s" % (first_conversion["p_convert"], first_conversion["requested_attempts"])

    text = f"""# FCF Simplified V0 calibration experiment

This directory is the executable numeric experiment defined by the Calibration Prototype Experiment Spec R0. It does not add mechanics, fit real fish parameters, or change the FCF design.

## Reproduce

```text
python3 -m fcf_v1.calibration_experiment --output experiments/fcf_simplified_v0 --samples {samples} --seed {seed}
```

The run uses a fixed seed and writes the requested CSV files under `results/` and six PNG figures under `figures/`. Every parameter point uses at least {samples:,} analytical-equivalent Bernoulli or categorical samples. Cadence verification additionally aggregates synthetic 60-minute sessions.

## Assertions

All required deterministic assertions passed: technical/mode split invariance, NONE addition invariance, probability normalization, grade monotonicity, exposure monotonicity, Hook-only upstream isolation, and Conversion-only Engagement isolation.

## Observations

- Analytical and Monte Carlo saturation/grade-map points differed by at most {max_mc_error:.6f} in this run.
- The largest fixed-category substitution change in the requested sweep was {float(max_sub['fixed_probability_pct_change']):.2f}% ({max_sub['direction']}, {max_sub['grade_map']}, K/reference={max_sub['k_ratio']}, varied grade={max_sub['varied_grade']}).
- In the requested roster grid, P(any) >= 0.9 {roster_text}.
- The weaker-per-event, higher-rate technique was stronger per minute in {len(inversions)} of 12 requested ratio pairs.
- Under unlimited Conversion attempts, P(at least one conversion) >= 0.9 {conversion_text}.
- At Exposure=K=ReferenceExposure, all maps share NORMAL=1 and therefore the same NORMAL result; their LOW/HIGH/VERY_HIGH separation differs as recorded in `results/summary.csv` and `figures/grade_map_sensitivity.png`.

## REOPEN SIGNALS

The observations above correspond only to the five requested reopen-signal categories: substitution coupling, roster saturation, cadence sensitivity, repeated Conversion attempts, and grade-map sensitivity. They are measurements for the design thread, not gameplay conclusions.

## Output schema notes

- `summary.csv`: K saturation, grade-map sensitivity, and compact reopen-signal rows.
- `invariance.csv`: exact deterministic invariance checks and differences.
- `substitution.csv`: both substitution sweep directions, analytical and simulated probabilities.
- `roster_saturation.csv`: N x pressure surface and per-category absolute probability.
- `cadence.csv`: Opportunity cadence surface plus normalized paired-technique comparisons.
- `conversion_reroll.csv`: G1/G2/G3 results; G3 cycles four synthetic semantic event-family labels, so effective attempts cap at four.
- `gear_isolation.csv`: shared-draw sequential-funnel counters for HookCompatibility and Conversion sweeps.
"""
    (base_dir / "README.md").write_text(text, encoding="utf-8")


def generate_experiment(base_dir: Path, samples: int = DEFAULT_SAMPLES, seed: int = DEFAULT_SEED, plots: bool = True) -> None:
    if samples < 1:
        raise ValueError("samples must be positive")
    import numpy as np

    run_assertions()
    rng = np.random.default_rng(seed)
    invariance_rows = _invariance_rows()
    substitution_rows = _substitution_rows(samples, rng)
    roster_rows = _roster_rows(samples, rng)
    cadence_rows = _cadence_rows(samples, rng)
    conversion_rows = _conversion_rows(samples, rng)
    gear_rows = _gear_isolation_rows(samples, rng)
    summary_rows = _summary_rows(samples, rng, substitution_rows, roster_rows, cadence_rows, conversion_rows)

    results = base_dir / "results"
    _write_csv(results / "summary.csv", summary_rows)
    _write_csv(results / "invariance.csv", invariance_rows)
    _write_csv(results / "substitution.csv", substitution_rows)
    _write_csv(results / "roster_saturation.csv", roster_rows)
    _write_csv(results / "cadence.csv", cadence_rows)
    _write_csv(results / "conversion_reroll.csv", conversion_rows)
    _write_csv(results / "gear_isolation.csv", gear_rows)
    if plots:
        _plot_results(base_dir, summary_rows, substitution_rows, roster_rows, cadence_rows, conversion_rows)
    _write_observation_readme(base_dir, summary_rows, substitution_rows, roster_rows, cadence_rows, conversion_rows, samples, seed)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("experiments/fcf_simplified_v0"))
    parser.add_argument("--samples", type=int, default=DEFAULT_SAMPLES)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args(argv)
    generate_experiment(args.output, samples=args.samples, seed=args.seed, plots=not args.no_plots)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
