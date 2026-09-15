"""FCF Simplified V0 pre-generation deterministic execution harness.

Current-contract version:
- candidate identity = Species x FishQuality x EngagementMode x SemanticSupport
- LifecycleCohort / ResponseSlice / pre-generation BehaviorAnchor are not candidate identity
- FishQuality is resolved before selection, so materialization does not re-roll quality
"""
from dataclasses import dataclass, is_dataclass, asdict
from typing import Any, Iterable, Mapping, Optional, Tuple
import hashlib
import json

OpportunityId = str
CandidateBasisKey = str


def _canon(value: Any) -> Any:
    if is_dataclass(value):
        return _canon(asdict(value))
    if isinstance(value, Mapping):
        return {str(k): _canon(value[k]) for k in sorted(value)}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_canon(v) for v in sorted(value, key=repr)]
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(_canon(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(*parts: Any) -> str:
    return hashlib.sha256(canonical_json(parts).encode()).hexdigest()


def rng_u(seed: str, domain: str, key: str = "") -> float:
    """Stateless, domain-separated draw. Adding fields in another domain is safe."""
    return int.from_bytes(hashlib.sha256(f"{seed}|{domain}|{key}".encode()).digest()[:8], "big") / 2**64


@dataclass(frozen=True)
class ResolveSnapshotBundle:
    spatial_artifact_version: str = "spatial-v0"
    world_snapshot_revision: str = "W172"
    species_slow_facts_revision: str = "bass-v1"
    engagement_mode_routing_revision: str = "routing-v1"
    surface_program_bundle_version: str = "surface-v1"
    presentation_interpreter_version: str = "presentation-v0"

    def fingerprint(self) -> str:
        return digest(self)


@dataclass(frozen=True)
class SemanticSupportRef:
    ref: str


@dataclass(frozen=True)
class RootSemanticOccurrence:
    session_id: str
    occurrence_id: str
    presentation_event: str
    exposure: str
    feeding_match: str
    support: SemanticSupportRef
    snapshot: ResolveSnapshotBundle
    seed: str = "fixture-seed"
    trait_schema_version: str = "trait-v0"

    def basis(self) -> "OpportunityBasis":
        return OpportunityBasis(self.session_id, self.occurrence_id, self.snapshot.fingerprint())


@dataclass(frozen=True)
class OpportunityBasis:
    session_id: str
    semantic_occurrence_id: str
    snapshot_fingerprint: str

    @property
    def opportunity_id(self) -> str:
        return digest("opportunity", self)


@dataclass(frozen=True)
class CandidateContribution:
    species: str
    fish_quality: str
    engagement_mode: str
    semantic_support_ref: str
    selection_weight: float

    @property
    def basis_key(self) -> str:
        return digest("candidate", self.species, self.fish_quality, self.engagement_mode, self.semantic_support_ref)


@dataclass(frozen=True)
class CandidateEntry:
    basis_key: str
    species: str
    fish_quality: str
    engagement_mode: str
    semantic_support_ref: str
    selection_weight: float


@dataclass(frozen=True)
class MeaningResponse:
    presentation_event: str
    exposure: str
    feeding_match: str
    response_band: str


@dataclass(frozen=True)
class ResolveResult:
    opportunity_id: str
    snapshot_fingerprint: str
    meaning_response: MeaningResponse
    entries: Tuple[CandidateEntry, ...]
    selected_basis_key: Optional[str]
    selection_roll: float


@dataclass(frozen=True)
class MaterializationPlan:
    candidate_basis_key: str


@dataclass(frozen=True)
class ConcreteFishResult:
    species: str
    fish_quality: str
    engagement_mode: str


class PreGenerationHarness:
    def __init__(self):
        self._claims = {}

    def resolve(self, occurrence: RootSemanticOccurrence, contributions: Iterable[CandidateContribution]) -> ResolveResult:
        oid = occurrence.basis().opportunity_id
        if oid in self._claims:
            return self._claims[oid]

        grouped = {}
        for c in contributions:
            if c.semantic_support_ref != occurrence.support.ref:
                continue
            grouped.setdefault(c.basis_key, []).append(c)

        entries = []
        for key, cs in grouped.items():
            first = cs[0]
            entries.append(CandidateEntry(key, first.species, first.fish_quality, first.engagement_mode, first.semantic_support_ref, sum(c.selection_weight for c in cs)))
        entries = tuple(sorted(entries, key=lambda e: e.basis_key))

        band = "HIGH" if occurrence.exposure == "HIGH" and occurrence.feeding_match == "VALID" else ("LOW" if occurrence.exposure == "LOW" else "NORMAL")
        meaning = MeaningResponse(occurrence.presentation_event, occurrence.exposure, occurrence.feeding_match, band)
        total = sum(e.selection_weight for e in entries)
        roll = rng_u(occurrence.seed, "selection", oid)
        selected = None
        if total:
            cursor = roll * total
            for e in entries:
                cursor -= e.selection_weight
                if cursor < 0:
                    selected = e.basis_key
                    break
        result = ResolveResult(oid, occurrence.snapshot.fingerprint(), meaning, entries, selected, roll)
        self._claims[oid] = result
        return result

    def materialization_plan(self, result: ResolveResult) -> Optional[MaterializationPlan]:
        if not result.selected_basis_key:
            return None
        return MaterializationPlan(result.selected_basis_key)

    def materialize(self, result: ResolveResult, seed: Optional[str] = None) -> Optional[ConcreteFishResult]:
        plan = self.materialization_plan(result)
        if plan is None:
            return None
        e = next(e for e in result.entries if e.basis_key == plan.candidate_basis_key)
        return ConcreteFishResult(e.species, e.fish_quality, e.engagement_mode)


def fixture_occurrence(variant: str = "A", snapshot: Optional[ResolveSnapshotBundle] = None) -> RootSemanticOccurrence:
    return RootSemanticOccurrence("session-1", "occ-deflection-1", "DEFLECTION", "HIGH", "VALID", SemanticSupportRef("GRASS_EDGE_01"), snapshot or ResolveSnapshotBundle())


def fixture_contributions(fragments: int = 1) -> Tuple[CandidateContribution, ...]:
    weight = 1.0 / fragments
    return tuple(CandidateContribution("Bass", "Q3", "NORMAL", "GRASS_EDGE_01", weight) for _ in range(fragments))


if __name__ == "__main__":
    h = PreGenerationHarness()
    r = h.resolve(fixture_occurrence(), fixture_contributions())
    fish = h.materialize(r)
    print(json.dumps({"opportunity_id": r.opportunity_id, "selected": r.selected_basis_key, "fish": fish.__dict__ if fish else None}, sort_keys=True))
