"""Legacy persistence adapter for the 0.3.4.0-B opportunity seed.

Migration-only seam. Nothing in this module is a Current Runtime definition:

* `backfill_is_background_fish()` is the one-time legacy backfill rule
  (`isBackgroundFish := min_env_coeff > 0`). After backfill the explicit switch
  carries the business meaning; the Current Runtime never derives it.
* `resolve_opportunity_seed_from_legacy_row()` maps the existing production chain
  `FishPond -> StockRelease -> FishRelease` onto `ResolvedOpportunitySeed` without
  inventing a new core persistence table.

Field mapping (Main Control Checkpoint 22.2 / 23.2):

    prob_weight_ideal -> baseOpportunityIntensity
    min_env_coeff     -> envCoeffMin
    min_adapt_coeff   -> Response-side, OUT OF B P0 (accepted, never consumed)

`min_env_coeff` and `min_adapt_coeff` are numerically identical in the whole
legacy dataset; they must not be merged by name or by value.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from fcf_v1.bake import BakeConfigError, validate_opportunity_seed


@dataclass(frozen=True)
class LegacyStockReleaseRow:
    """One `StockRelease` / `FishRelease` row, reduced to the B-relevant fields."""

    stock_id: str
    fish_id: str
    fish_pond_ref: str
    species_id: str
    fish_quality_id: str
    prob_weight_ideal: float
    min_env_coeff: float
    min_adapt_coeff: float
    is_background_fish: bool | None = None


def backfill_is_background_fish(min_env_coeff: float) -> bool:
    """One-time legacy backfill. Not a Current Runtime derivation."""
    return float(min_env_coeff) > 0.0


def resolve_opportunity_seed_from_legacy_row(row: LegacyStockReleaseRow) -> Mapping[str, Any]:
    is_background_fish = (
        row.is_background_fish
        if row.is_background_fish is not None
        else backfill_is_background_fish(row.min_env_coeff)
    )
    seed: dict[str, Any] = {
        "fishPondRef": row.fish_pond_ref,
        "fishQualityRef": {
            "speciesId": row.species_id,
            "fishQualityId": row.fish_quality_id,
        },
        "baseOpportunityIntensity": float(row.prob_weight_ideal),
        "isBackgroundFish": is_background_fish,
    }
    if is_background_fish:
        seed["envCoeffMin"] = float(row.min_env_coeff)
    return validate_opportunity_seed(seed)


def build_opportunity_seeds(
    rows: Sequence[LegacyStockReleaseRow],
) -> Mapping[tuple[str, str], Mapping[str, Any]]:
    """Resolve one seed per `FishPond x FishQualityRef`, failing fast on duplicates.

    Production `(stock_id, fish_id)` is unique, but `release_id` is shared across
    the exploration variants of one pond. Row-by-row expansion must therefore not
    silently turn one logical seed into several candidate seeds.
    """
    seeds: dict[tuple[str, str], Mapping[str, Any]] = {}
    for row in rows:
        seed = resolve_opportunity_seed_from_legacy_row(row)
        key = (seed["fishPondRef"], seed["fishQualityRef"]["fishQualityId"])
        if key in seeds:
            raise BakeConfigError(
                f"duplicate FishPond x FishQuality seed for {key}: "
                "resolve the existing composition rule instead of double-counting"
            )
        seeds[key] = seed
    return seeds


def project_compat_mode_membership(
    quality_to_affinity: Mapping[str, str],
    *,
    declared_membership: Mapping[str, Sequence[str]] | None = None,
) -> Mapping[str, Sequence[str]]:
    """Project Compat Mode membership from the existing authoring truth.

    `FishQualityRef -> FishEnvAffinityRef` stays the only editable membership
    source; the Compat Mode view is derived from it. A separately editable
    membership that disagrees with the projection is rejected rather than
    persisted as a second Quality->Mode truth.
    """
    projected: dict[str, list[str]] = {}
    for fish_quality_id, affinity_ref in quality_to_affinity.items():
        projected.setdefault(affinity_ref, []).append(fish_quality_id)

    if declared_membership is not None:
        normalized = {key: sorted(value) for key, value in declared_membership.items()}
        expected = {key: sorted(value) for key, value in projected.items()}
        if normalized != expected:
            raise BakeConfigError(
                "Compat Mode membership must not form a second independently editable "
                "FishQuality -> Mode truth"
            )
    return projected
