"""Small production-handoff conformance runner.

Production runtimes can expose an adapter factory and run this smoke contract
before the full fixture suite.  It intentionally checks only RC4 invariants;
game-specific behavior remains in the flagship fixtures.
"""

from dataclasses import dataclass
import json
from typing import Callable, List, Protocol

from .model import EntryGrade, EntryMotive, EntryOpportunity, SettlementKind


class EngineContract(Protocol):
    def accounting_total(self) -> float: ...
    def form_proposals(self, opportunity: EntryOpportunity, **kwargs): ...
    def materialize(self, proposal): ...
    def settle(self, candidate_id: str, kind: SettlementKind): ...


@dataclass(frozen=True)
class ConformanceCheck:
    name: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class ConformanceReport:
    checks: List[ConformanceCheck]

    @property
    def passed(self) -> bool:
        return all(check.passed for check in self.checks)

    def as_dict(self):
        """Return a stable, JSON-safe CI/audit representation."""
        return {
            "passed": self.passed,
            "checks": [
                {"name": check.name, "passed": check.passed, "detail": check.detail}
                for check in self.checks
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":"))


def run_core_conformance(make_engine: Callable[[], EngineContract]) -> ConformanceReport:
    """Run a deterministic entry/reservation/settlement smoke contract.

    `make_engine` must return an engine configured with a finite source whose
    stable ID is ``s1`` and slice ID ``slice``.  This convention keeps the
    handoff runner independent of the production dependency-injection layer.
    """
    checks: List[ConformanceCheck] = []
    try:
        engine = make_engine()
        before = engine.accounting_total()
        opportunity = EntryOpportunity(
            "conformance-opportunity", "conformance", "slice", "s1", "FIRST_ACCESS"
        )
        proposals = engine.form_proposals(
            opportunity, accessible_fraction=1.0, temporal_factor=1.0,
            entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
        )
        replay = engine.form_proposals(
            opportunity, accessible_fraction=1.0, temporal_factor=1.0,
            entry_grade=EntryGrade.CERTAIN, motive=EntryMotive.FORAGE,
        )
        checks.append(ConformanceCheck("opportunity_replay_no_reroll", replay == [],
                                       f"replay_proposals={len(replay)}"))
        candidate = engine.materialize(proposals[0]) if proposals else None
        if candidate is None:
            raise AssertionError("CERTAIN entry did not produce a materialized candidate")
        engine.settle(candidate.candidate_id, SettlementKind.RETURN)
        engine.settle(candidate.candidate_id, SettlementKind.RETURN)
        after = engine.accounting_total()
        checks.append(ConformanceCheck("finite_entry_and_settlement", before == after,
                                       f"before={before}, after={after}"))
    except Exception as exc:  # report failures without hiding the cause
        checks.append(ConformanceCheck("finite_entry_and_settlement", False,
                                       f"{type(exc).__name__}: {exc}"))
    return ConformanceReport(checks)
