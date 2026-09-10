"""Prototype-gate experiments layered on the existing three-epoch harness.

All coefficients and probabilities are TEST FIXTURE / TUNING PLACEHOLDER /
NOT AUTHORITY.  This module deliberately exposes failures instead of adjusting
acceptance thresholds to force a pass.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import hashlib
import math
import random
from typing import Iterable, Literal, Optional


Granularity = Literal["G1", "G2", "G3"]
ObservationMode = Literal["O0", "O1"]
ZONES = ("NORTH", "CENTRAL", "SOUTH")
HABITAT_CLASSES = ("GRASS", "WOOD", "DEEP_EDGE")
FOOD_FAMILIES = ("BAITFISH", "CRUSTACEAN", "WORM_LIKE")
STATIC_HABITAT = {"GRASS": 0.90, "WOOD": 0.80, "DEEP_EDGE": 0.70}
STATIC_DIET = {"BAITFISH": 0.90, "CRUSTACEAN": 0.80, "WORM_LIKE": 0.70}


@dataclass(frozen=True)
class Context:
    time_of_day: float
    light: float
    water_temperature: float
    temperature_trend: float
    wind: float


@dataclass(frozen=True)
class PreyState:
    baitfish_activity: float
    crustacean_activity: float
    worm_like_availability: float


@dataclass(frozen=True)
class SourceGroup:
    source_group_id: str
    zone: str
    habitat_class: str
    weight: float
    reach: float


@dataclass(frozen=True)
class TechnicalFragment:
    object_id: str
    source_group_id: str
    zone: str
    habitat_class: str
    weight: float
    reach: float


def context_at(hour: float) -> Context:
    """Generate continuous daily inputs; no epoch labels or transition state."""
    phase = 2.0 * math.pi * hour / 24.0
    daylight = 0.5 + 0.5 * math.sin(phase - math.pi / 2.0)
    water_temperature = 20.0 + 3.0 * math.sin(phase - 2.0 * math.pi * 10.0 / 24.0)
    temperature_trend = math.cos(phase - 2.0 * math.pi * 10.0 / 24.0)
    wind = 0.50 + 0.25 * math.sin(phase - 2.0 * math.pi * 14.0 / 24.0)
    return Context(hour, daylight, water_temperature, temperature_trend, wind)


def _weighted_center(raw: dict[str, float], weights: dict[str, float]) -> dict[str, float]:
    denominator = sum(weights[k] for k in raw)
    center = sum(weights[k] * raw[k] for k in raw) / denominator
    return {k: raw[k] / center for k in raw}


def resolve_spatial_class_bias(context: Context) -> dict[str, float]:
    """Resolve continuous class-level use, centered around weighted mean 1.0."""
    hot = (context.water_temperature - 20.0) / 3.0
    raw = {
        "GRASS": 1.0 + 0.28 * (1.0 - context.light) - 0.10 * hot + 0.08 * context.wind,
        "WOOD": 1.0 + 0.25 * context.light + 0.12 * hot - 0.04 * context.wind,
        "DEEP_EDGE": 1.0 + 0.18 * context.light + 0.18 * hot - 0.05 * context.temperature_trend,
    }
    return _weighted_center(raw, STATIC_HABITAT)


def resolve_feeding_bias(prey: PreyState) -> dict[str, float]:
    """Resolve relative food preference; common multiplicative uplift cancels."""
    raw = {
        "BAITFISH": max(prey.baitfish_activity, 1e-9),
        "CRUSTACEAN": max(prey.crustacean_activity, 1e-9),
        "WORM_LIKE": max(prey.worm_like_availability, 1e-9),
    }
    return _weighted_center(raw, STATIC_DIET)


def generate_map(per_zone_class: int = 5) -> list[SourceGroup]:
    """Generate 45 semantic SourceGroups by default from one stable recipe."""
    result = []
    for zone_index, zone in enumerate(ZONES):
        for class_index, habitat in enumerate(HABITAT_CLASSES):
            for index in range(per_zone_class):
                result.append(
                    SourceGroup(
                        source_group_id=f"{zone}.{habitat}.{index:02d}",
                        zone=zone,
                        habitat_class=habitat,
                        weight=round(0.80 + 0.05 * index, 6),
                        reach=round(0.72 + 0.02 * ((zone_index + class_index + index) % 5), 6),
                    )
                )
    return result


def _stable_offset(source_id: str) -> float:
    digest = hashlib.sha256(source_id.encode("utf-8")).digest()
    return ((int.from_bytes(digest[:2], "big") / 65535.0) - 0.5) * 0.24


def bias_table(granularity: Granularity, context: Context, sources: list[SourceGroup]) -> dict[str, float]:
    class_bias = resolve_spatial_class_bias(context)
    if granularity == "G1":
        return dict(class_bias)
    if granularity == "G2":
        table = {}
        for zone_index, zone in enumerate(ZONES):
            zone_raw = {
                habitat: class_bias[habitat]
                * (1.0 + 0.10 * math.sin((zone_index + 1) * (class_index + 1)))
                for class_index, habitat in enumerate(HABITAT_CLASSES)
            }
            centered = _weighted_center(zone_raw, STATIC_HABITAT)
            table.update({f"{zone}|{habitat}": value for habitat, value in centered.items()})
        return table
    table = {}
    by_zone = {zone: [source for source in sources if source.zone == zone] for zone in ZONES}
    for zone, zone_sources in by_zone.items():
        raw = {
            source.source_group_id: class_bias[source.habitat_class]
            * (1.0 + _stable_offset(source.source_group_id))
            for source in zone_sources
        }
        weights = {source.source_group_id: STATIC_HABITAT[source.habitat_class] for source in zone_sources}
        table.update(_weighted_center(raw, weights))
    return table


def bias_key(granularity: Granularity, source: SourceGroup) -> str:
    if granularity == "G1":
        return source.habitat_class
    if granularity == "G2":
        return f"{source.zone}|{source.habitat_class}"
    return source.source_group_id


def fragment_source(source: SourceGroup, count: int) -> list[TechnicalFragment]:
    return [
        TechnicalFragment(
            object_id=f"{source.source_group_id}.fragment.{index:02d}",
            source_group_id=source.source_group_id,
            zone=source.zone,
            habitat_class=source.habitat_class,
            weight=source.weight / count,
            reach=source.reach,
        )
        for index in range(count)
    ]


def aggregate_fragments(fragments: Iterable[TechnicalFragment]) -> list[SourceGroup]:
    grouped: dict[str, SourceGroup] = {}
    for fragment in fragments:
        previous = grouped.get(fragment.source_group_id)
        if previous is None:
            grouped[fragment.source_group_id] = SourceGroup(
                fragment.source_group_id,
                fragment.zone,
                fragment.habitat_class,
                fragment.weight,
                fragment.reach,
            )
        else:
            if (previous.zone, previous.habitat_class) != (fragment.zone, fragment.habitat_class):
                raise ValueError("technical fragments disagree on ecological identity")
            grouped[fragment.source_group_id] = replace(
                previous,
                weight=previous.weight + fragment.weight,
                reach=max(previous.reach, fragment.reach),
            )
    return list(grouped.values())


def source_intensity(source: SourceGroup, granularity: Granularity, table: dict[str, float]) -> tuple[float, float]:
    local = 100.0 * source.weight * STATIC_HABITAT[source.habitat_class] * table[bias_key(granularity, source)]
    return local, local * source.reach


def granularity_comparison(
    context: Context, sources: Optional[list[SourceGroup]] = None
) -> dict[str, dict]:
    sources = generate_map() if sources is None else sources
    result = {}
    for granularity in ("G1", "G2", "G3"):
        table = bias_table(granularity, context, sources)
        local_patterns = len({round(value, 8) for value in table.values()})
        # Apply a desired NORTH/GRASS local bump and count remote identities that
        # must also change because the granularity cannot express that locality.
        if granularity == "G1":
            remote_coupling = sum(
                1 for source in sources if source.zone != "NORTH" and source.habitat_class == "GRASS"
            )
        else:
            remote_coupling = 0

        # Same-zone insertion reveals G3 centering sensitivity without conflating
        # it with the required different-zone independence test.
        extra = SourceGroup("NORTH.GRASS.NEW", "NORTH", "GRASS", 1.0, 0.8)
        after_table = bias_table(granularity, context, sources + [extra])
        deltas = []
        for source in sources:
            key = bias_key(granularity, source)
            deltas.append(abs(table[key] - after_table[key]))
        max_edit_delta = max(deltas)
        result[granularity] = {
            "authoring_parameter_count": len(table),
            "runtime_bias_entries": len(table),
            "local_pattern_count": local_patterns,
            "local_pattern_expression": {
                "G1": "class-global only",
                "G2": "zone x class",
                "G3": "individual ecological SourceGroup",
            }[granularity],
            "far_distance_coupled_identities": remote_coupling,
            "same_zone_map_edit_max_existing_bias_delta": max_edit_delta,
            "map_edit_stability": "STABLE" if max_edit_delta < 1e-12 else "COUPLED_WITHIN_CENTERING_SCOPE",
            "debug_identity_count": len(table),
        }
    return result


def fragmentation_experiment(
    context: Context, generated_sources: Optional[list[SourceGroup]] = None
) -> dict[str, dict]:
    source = SourceGroup("A", "NORTH", "GRASS", 1.0, 0.8)
    one = [TechnicalFragment("A", "A", "NORTH", "GRASS", 1.0, 0.8)]
    ten = fragment_source(source, 10)
    sources = (generate_map() if generated_sources is None else generated_sources) + [source]
    result = {}
    for granularity in ("G1", "G2", "G3"):
        table = bias_table(granularity, context, sources)
        before = source_intensity(aggregate_fragments(one)[0], granularity, table)
        after = source_intensity(aggregate_fragments(ten)[0], granularity, table)
        delta = max(abs(before[0] - after[0]), abs(before[1] - after[1]))
        result[granularity] = {
            "one_object": {"local_intensity": before[0], "exposed_intensity": before[1]},
            "ten_fragments": {"local_intensity": after[0], "exposed_intensity": after[1]},
            "max_delta": delta,
            "verdict": "PASS" if delta < 1e-9 else "FAIL",
        }
    return result


def unrelated_source_experiment(
    context: Context, sources: Optional[list[SourceGroup]] = None
) -> dict[str, dict]:
    sources = generate_map() if sources is None else sources
    existing = sources[0]
    remote = SourceGroup("REMOTE.WOOD.00", "SOUTH", "WOOD", 1.0, 0.8)
    result = {}
    for granularity in ("G1", "G2", "G3"):
        before_table = bias_table(granularity, context, sources)
        after_table = bias_table(granularity, context, sources + [remote])
        before = source_intensity(existing, granularity, before_table)
        after = source_intensity(existing, granularity, after_table)
        delta = max(abs(before[0] - after[0]), abs(before[1] - after[1]))
        result[granularity] = {
            "existing_source": existing.source_group_id,
            "remote_source": remote.source_group_id,
            "before": {"local_intensity": before[0], "exposed_intensity": before[1]},
            "after": {"local_intensity": after[0], "exposed_intensity": after[1]},
            "max_delta": delta,
            "verdict": "PASS" if delta < 1e-9 else "FAIL",
        }
    return result


OBSERVATIONS = {
    "O0": ("NO_EVENT", "BITE"),
    "O1": ("NO_PRESENCE_SIGNAL", "PRESENCE_SIGNAL", "FOLLOW_OR_REJECT", "ATTACK"),
}
PRESENCE_PROBABILITY = {"NORTH": 0.32, "CENTRAL": 0.72, "SOUTH": 0.50}
RESPONSE_PROBABILITY = {"BAITFISH": 0.28, "CRUSTACEAN": 0.78, "WORM_LIKE": 0.46}
ATTACK_GIVEN_RESPONSE = 0.58


def observe(zone: str, food: str, mode: ObservationMode, rng: random.Random) -> tuple[str, str]:
    presence = rng.random() < PRESENCE_PROBABILITY[zone]
    response = presence and rng.random() < RESPONSE_PROBABILITY[food]
    attack = response and rng.random() < ATTACK_GIVEN_RESPONSE
    truth = "NO_PRESENCE" if not presence else ("NO_RESPONSE" if not response else "RESPONSE")
    if mode == "O0":
        return ("BITE" if attack else "NO_EVENT"), truth
    if not presence:
        return "NO_PRESENCE_SIGNAL", truth
    if not response:
        return "PRESENCE_SIGNAL", truth
    return ("ATTACK" if attack else "FOLLOW_OR_REJECT"), truth


def _sequential_identify(
    mode: ObservationMode,
    candidates: tuple[str, ...],
    sampler,
    score,
    rng: random.Random,
    min_each: int = 6,
    max_probes: int = 90,
    gap: float = 0.10,
) -> tuple[str, int, list[tuple[str, str, str]]]:
    seen = {candidate: 0 for candidate in candidates}
    values = {candidate: 0.0 for candidate in candidates}
    history = []
    for probe in range(max_probes):
        candidate = candidates[probe % len(candidates)]
        observation, truth = sampler(candidate, rng)
        history.append((candidate, observation, truth))
        contribution, denominator = score(observation)
        values[candidate] += contribution
        seen[candidate] += denominator
        if min(seen.values()) >= min_each:
            rates = sorted(
                ((values[c] / seen[c], c) for c in candidates), reverse=True
            )
            if rates[0][0] - rates[1][0] >= gap:
                return rates[0][1], probe + 1, history
    rates = sorted(((values[c] / max(seen[c], 1), c) for c in candidates), reverse=True)
    return rates[0][1], max_probes, history


def run_search_trial(mode: ObservationMode, rng: random.Random) -> dict:
    zone_probe_index = {zone: 0 for zone in ZONES}

    def zone_sampler(zone: str, local_rng: random.Random):
        food = FOOD_FAMILIES[zone_probe_index[zone] % len(FOOD_FAMILIES)]
        zone_probe_index[zone] += 1
        return observe(zone, food, mode, local_rng)

    if mode == "O1":
        zone_score = lambda obs: (0.0 if obs == "NO_PRESENCE_SIGNAL" else 1.0, 1)
    else:
        zone_score = lambda obs: (1.0 if obs == "BITE" else 0.0, 1)
    zone, zone_probes, zone_history = _sequential_identify(
        mode, ZONES, zone_sampler, zone_score, rng
    )

    if mode == "O1":
        food_score = lambda obs: (
            1.0 if obs in ("FOLLOW_OR_REJECT", "ATTACK") else 0.0,
            0 if obs == "NO_PRESENCE_SIGNAL" else 1,
        )
    else:
        food_score = lambda obs: (1.0 if obs == "BITE" else 0.0, 1)

    def food_sampler(food: str, local_rng: random.Random):
        return observe(zone, food, mode, local_rng)

    food, food_probes, food_history = _sequential_identify(
        mode, FOOD_FAMILIES, food_sampler, food_score, rng
    )

    # O0's binary observation cannot distinguish a hidden no-presence event from
    # a hidden no-response event.  Its minimal classifier uses the selected zone:
    # NO_EVENT in the selected zone is called RESPONSE, elsewhere PRESENCE.
    errors = 0
    eligible = 0
    presence_as_response_errors = 0
    no_presence_cases = 0
    for probed_zone, observation, truth in zone_history:
        if observation != "NO_EVENT" or truth == "RESPONSE":
            continue
        guessed = "NO_RESPONSE" if probed_zone == zone else "NO_PRESENCE"
        errors += guessed != truth
        eligible += 1
        if truth == "NO_PRESENCE":
            no_presence_cases += 1
            presence_as_response_errors += guessed == "NO_RESPONSE"
    if mode == "O0":
        for _, observation, truth in food_history:
            if observation != "NO_EVENT" or truth == "RESPONSE":
                continue
            guessed = "NO_RESPONSE"
            errors += guessed != truth
            eligible += 1
            if truth == "NO_PRESENCE":
                no_presence_cases += 1
                presence_as_response_errors += 1
    if mode == "O1":
        for _, observation, truth in zone_history + food_history:
            if truth not in ("NO_PRESENCE", "NO_RESPONSE"):
                continue
            guessed = "NO_PRESENCE" if observation == "NO_PRESENCE_SIGNAL" else "NO_RESPONSE"
            errors += guessed != truth
            eligible += 1
            if truth == "NO_PRESENCE":
                no_presence_cases += 1
                presence_as_response_errors += guessed == "NO_RESPONSE"
    return {
        "zone": zone,
        "food": food,
        "zone_probes": zone_probes,
        "food_probes": food_probes,
        "correct": zone == "CENTRAL" and food == "CRUSTACEAN",
        "cause_errors": errors,
        "cause_classifications": eligible,
        "presence_as_response_errors": presence_as_response_errors,
        "no_presence_cases": no_presence_cases,
    }


def observation_experiment(trials: int = 2000, seed: int = 20260902) -> dict[str, dict]:
    result = {}
    for mode_index, mode in enumerate(("O0", "O1")):
        rng = random.Random(seed + mode_index)
        runs = [run_search_trial(mode, rng) for _ in range(trials)]
        total_classifications = sum(run["cause_classifications"] for run in runs)
        result[mode] = {
            "trials": trials,
            "mean_probes_best_zone": sum(run["zone_probes"] for run in runs) / trials,
            "mean_probes_best_food": sum(run["food_probes"] for run in runs) / trials,
            "correct_pattern_rate": sum(run["correct"] for run in runs) / trials,
            "presence_as_response_or_inverse_rate": (
                sum(run["cause_errors"] for run in runs) / total_classifications
            ),
            "misjudge_presence_as_response_rate": (
                sum(run["presence_as_response_errors"] for run in runs)
                / sum(run["no_presence_cases"] for run in runs)
            ),
            "allowed_observations": OBSERVATIONS[mode],
        }
        result[mode]["mean_total_probes"] = (
            result[mode]["mean_probes_best_zone"] + result[mode]["mean_probes_best_food"]
        )
        result[mode]["probes_per_correct_pattern"] = (
            result[mode]["mean_total_probes"] / result[mode]["correct_pattern_rate"]
        )
    return result
