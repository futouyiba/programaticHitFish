"""Fixed-pan Response calibration harness for FCF Simplified V0.

STATUS: EXPERIMENT / VALIDATION ONLY — NOT production runtime.

This module implements the numeric surface currently needed to calibrate
ResponseBand -> ResponseMultiplier without reopening Response structure.

It deliberately does NOT:
- resolve Response rules;
- derive PreResponseWeight from Bake output;
- own opportunity cadence;
- implement PRD / empty-weight decay / fallback;
- freeze production LOW / NORMAL multipliers;
- define saturated production composition policy.

The caller must supply PreResponseWeight (U_i) explicitly. That boundary is
intentional: Bake / Routing / Exposure ownership must not be guessed here.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Optional, Sequence


BANDS = ("NONE", "LOW", "NORMAL", "HIGH")

DEFAULT_NORMAL_GRID = (0.50, 0.60, 0.67, 0.75, 0.80)
DEFAULT_LOW_GRID = (0.20, 0.25, 0.33, 0.40, 0.50)
DEFAULT_RHO_HIGH_GRID = (0.25, 0.40, 0.50, 0.60, 0.80, 1.00, 1.25, 1.50, 2.00)


class CalibrationInputError(ValueError):
    pass


@dataclass(frozen=True)
class ResponseMapping:
    low: float
    normal: float

    def __post_init__(self) -> None:
        if not (0.0 < self.low < self.normal < 1.0):
            raise CalibrationInputError(
                "require 0 < LOW < NORMAL < HIGH(=1); got LOW=%r NORMAL=%r"
                % (self.low, self.normal)
            )

    def multiplier(self, band: str) -> float:
        token = str(band).upper()
        if token == "NONE":
            return 0.0
        if token == "LOW":
            return self.low
        if token == "NORMAL":
            return self.normal
        if token == "HIGH":
            return 1.0
        raise CalibrationInputError("unknown ResponseBand: %r" % band)

    def as_dict(self) -> dict[str, float]:
        return {
            "NONE": 0.0,
            "LOW": self.low,
            "NORMAL": self.normal,
            "HIGH": 1.0,
        }


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    pre_response_weight: float
    response_band: str
    is_target: bool = False

    def __post_init__(self) -> None:
        if not self.candidate_id:
            raise CalibrationInputError("candidate_id is required")
        if not math.isfinite(self.pre_response_weight) or self.pre_response_weight < 0.0:
            raise CalibrationInputError("pre_response_weight must be finite and >= 0")
        if str(self.response_band).upper() not in BANDS:
            raise CalibrationInputError("invalid ResponseBand: %r" % self.response_band)


@dataclass(frozen=True)
class CandidateProjection:
    candidate_id: str
    pre_response_weight: float
    response_band: str
    response_multiplier: float
    selection_weight: float
    is_target: bool
    reference_composition_share: float


@dataclass(frozen=True)
class FixedPanSnapshot:
    pan_scale: float
    fish_mass: float
    rho: float
    p_any_fish: float
    p_none: float
    saturated: bool
    target_weight: float
    target_purity_reference: float
    candidates: tuple[CandidateProjection, ...]
    production_overflow_composition_verified: bool = False

    def as_dict(self) -> dict[str, object]:
        return {
            "panScale": self.pan_scale,
            "fishMass": self.fish_mass,
            "rho": self.rho,
            "pAnyFish": self.p_any_fish,
            "pNone": self.p_none,
            "saturated": self.saturated,
            "targetWeight": self.target_weight,
            "targetPurityReference": self.target_purity_reference,
            "productionOverflowCompositionVerified": self.production_overflow_composition_verified,
            "candidates": [
                {
                    "candidateId": c.candidate_id,
                    "preResponseWeight": c.pre_response_weight,
                    "responseBand": c.response_band,
                    "responseMultiplier": c.response_multiplier,
                    "selectionWeight": c.selection_weight,
                    "isTarget": c.is_target,
                    "referenceCompositionShare": c.reference_composition_share,
                }
                for c in self.candidates
            ],
        }


def _validate_pan_scale(pan_scale: float) -> float:
    value = float(pan_scale)
    if not math.isfinite(value) or value <= 0.0:
        raise CalibrationInputError("pan_scale must be finite and > 0")
    return value


def evaluate_fixed_pan(
    candidates: Sequence[Candidate],
    *,
    pan_scale: float,
    mapping: ResponseMapping,
) -> FixedPanSnapshot:
    """Project explicit PreResponseWeight through Response into a fixed pan.

    Current working transfer:
        W_i = U_i * r_i
        F   = sum(W_i)
        rho = F / N
        P(any fish) = min(1, rho)
        P(None)     = max(0, 1-rho)

    reference_composition_share = W_i/F is always emitted as a diagnostic.
    In the saturated region it MUST NOT be treated as verified production
    composition until the exact overflow / quality-priority selector is checked.
    """

    n = _validate_pan_scale(pan_scale)
    weighted: list[tuple[Candidate, float, float]] = []
    for candidate in candidates:
        r = mapping.multiplier(candidate.response_band)
        w = candidate.pre_response_weight * r
        weighted.append((candidate, r, w))

    fish_mass = math.fsum(row[2] for row in weighted)
    rho = fish_mass / n
    p_any = min(1.0, rho)
    p_none = max(0.0, 1.0 - rho)
    target_weight = math.fsum(w for candidate, _, w in weighted if candidate.is_target)
    target_purity = target_weight / fish_mass if fish_mass > 0.0 else 0.0

    projections = tuple(
        CandidateProjection(
            candidate_id=candidate.candidate_id,
            pre_response_weight=candidate.pre_response_weight,
            response_band=str(candidate.response_band).upper(),
            response_multiplier=r,
            selection_weight=w,
            is_target=candidate.is_target,
            reference_composition_share=(w / fish_mass if fish_mass > 0.0 else 0.0),
        )
        for candidate, r, w in weighted
    )

    return FixedPanSnapshot(
        pan_scale=n,
        fish_mass=fish_mass,
        rho=rho,
        p_any_fish=p_any,
        p_none=p_none,
        saturated=rho >= 1.0,
        target_weight=target_weight,
        target_purity_reference=target_purity,
        candidates=projections,
    )


def expected_native_wait_seconds(opportunity_interval_seconds: float, p_any: float) -> float:
    """Geometric mean wait under iid native opportunities.

    This is a sanity-check projection only. It intentionally excludes PRD /
    fallback and assumes the supplied interval is a real semantic opportunity
    interval, not frame/tick/poll frequency.
    """

    interval = float(opportunity_interval_seconds)
    probability = float(p_any)
    if not math.isfinite(interval) or interval <= 0.0:
        raise CalibrationInputError("opportunity interval must be finite and > 0")
    if not (0.0 <= probability <= 1.0):
        raise CalibrationInputError("p_any must be within [0,1]")
    if probability == 0.0:
        return math.inf
    return interval / probability


def uniform_band_projection(rho_high: float, multiplier: float) -> float:
    """P(any) if a HIGH-state fish mass is uniformly attenuated by multiplier."""

    rho = float(rho_high)
    r = float(multiplier)
    if not math.isfinite(rho) or rho < 0.0:
        raise CalibrationInputError("rho_high must be finite and >= 0")
    if not math.isfinite(r) or not (0.0 <= r <= 1.0):
        raise CalibrationInputError("multiplier must be within [0,1]")
    return min(1.0, rho * r)


def mapping_sweep_rows(
    normal_grid: Iterable[float] = DEFAULT_NORMAL_GRID,
    low_grid: Iterable[float] = DEFAULT_LOW_GRID,
    rho_high_grid: Iterable[float] = DEFAULT_RHO_HIGH_GRID,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for normal in normal_grid:
        for low in low_grid:
            try:
                mapping = ResponseMapping(low=float(low), normal=float(normal))
            except CalibrationInputError:
                continue
            for rho_high in rho_high_grid:
                p_high = uniform_band_projection(rho_high, 1.0)
                p_normal = uniform_band_projection(rho_high, mapping.normal)
                p_low = uniform_band_projection(rho_high, mapping.low)
                rows.append(
                    {
                        "rLow": mapping.low,
                        "rNormal": mapping.normal,
                        "rhoHigh": float(rho_high),
                        "pAnyHigh": p_high,
                        "pAnyNormal": p_normal,
                        "pAnyLow": p_low,
                        "highToNormalDelta": p_high - p_normal,
                        "normalToLowDelta": p_normal - p_low,
                        "highSaturated": float(rho_high) >= 1.0,
                        "normalSaturated": float(rho_high) * mapping.normal >= 1.0,
                        "lowSaturated": float(rho_high) * mapping.low >= 1.0,
                    }
                )
    return rows


def load_snapshot_input(path: Path) -> tuple[float, ResponseMapping, list[Candidate]]:
    """Load an explicit projection fixture.

    Schema:
      {
        "panScale": 2000000,
        "mapping": {"LOW": 0.4, "NORMAL": 0.67},
        "candidates": [
          {
            "candidateId": "...",
            "preResponseWeight": 123,
            "responseBand": "HIGH",
            "isTarget": true
          }
        ]
      }

    The fixture must already contain PreResponseWeight. This harness does not
    infer it from Bake or SpatialOpportunity fields.
    """

    raw = json.loads(path.read_text(encoding="utf-8"))
    mapping_raw = raw["mapping"]
    mapping = ResponseMapping(
        low=float(mapping_raw["LOW"]),
        normal=float(mapping_raw["NORMAL"]),
    )
    candidates = [
        Candidate(
            candidate_id=str(row["candidateId"]),
            pre_response_weight=float(row["preResponseWeight"]),
            response_band=str(row["responseBand"]),
            is_target=bool(row.get("isTarget", False)),
        )
        for row in raw["candidates"]
    ]
    return float(raw["panScale"]), mapping, candidates


def write_sweep_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise CalibrationInputError("refusing to write an empty sweep")
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="explicit PreResponseWeight projection fixture")
    parser.add_argument("--sweep-csv", type=Path, help="write the default mapping x rho sweep")
    args = parser.parse_args(argv)

    if args.input:
        pan_scale, mapping, candidates = load_snapshot_input(args.input)
        result = evaluate_fixed_pan(candidates, pan_scale=pan_scale, mapping=mapping)
        print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))

    if args.sweep_csv:
        write_sweep_csv(args.sweep_csv, mapping_sweep_rows())

    if not args.input and not args.sweep_csv:
        parser.error("provide --input and/or --sweep-csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
