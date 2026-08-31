"""Explain/verification trace structures with no state mutation."""

from dataclasses import asdict, dataclass
import json
from typing import Any, Dict, Iterable, Tuple


@dataclass(frozen=True)
class StageTrace:
    name: str
    inputs: Dict[str, Any]
    outputs: Dict[str, Any]
    owner: str


@dataclass(frozen=True)
class ExplainTrace:
    fixture_id: str
    artifact_version: str
    opportunity_id: str
    stages: Tuple[StageTrace, ...]
    ledger_delta: Dict[str, float]

    def to_json(self) -> str:
        # sort_keys ensures stable review diffs and replay snapshots.
        return json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))


def entry_trace(
    *,
    fixture_id: str,
    artifact_version: str,
    opportunity_id: str,
    a: float,
    t: float,
    motive: str,
    e: float,
    q: float,
    reservation_id: str,
) -> ExplainTrace:
    """Build the canonical four-stage trace without sampling or mutation."""
    if not 0.0 <= a <= 1.0 or not 0.0 <= t <= 1.0 or not 0.0 <= e <= 1.0:
        raise ValueError("A, T and E must be in [0,1]")
    pi = a * t * e
    return ExplainTrace(
        fixture_id=fixture_id,
        artifact_version=artifact_version,
        opportunity_id=opportunity_id,
        stages=(
            StageTrace("PERCEPTION", {"access_fraction": a}, {"A": a}, "perception_access"),
            StageTrace("MOTIVE", {}, {"motive": motive}, "slice_behavior_program"),
            StageTrace("ENTRY", {"A": a, "T": t, "E": e}, {"E": e, "pi": pi}, "motive_entry_offer"),
            StageTrace("RESERVATION", {"q": q}, {"q": q, "reservation_id": reservation_id}, "population_ledger"),
        ),
        ledger_delta={"actual_supply": -q, "encounter_hold": q},
    )
