"""FCF Simplified V0 pre-generation deterministic execution harness.

This module is intentionally small and dependency free.  Technical
fragmentation is input noise; semantic canonicalization is the authority.
"""
from dataclasses import dataclass, field, is_dataclass, asdict
from typing import Any, Iterable, Mapping, Optional, Sequence, Tuple
import hashlib, json

OpportunityId = str
CandidateBasisKey = str


def _canon(value: Any) -> Any:
    if is_dataclass(value): return _canon(asdict(value))
    if isinstance(value, Mapping): return {str(k): _canon(value[k]) for k in sorted(value)}
    if isinstance(value, (tuple, list, set, frozenset)): return [_canon(v) for v in sorted(value, key=repr)]
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
    species_slow_facts_revision: str = "bass-v0"
    response_content_bundle_version: str = "response-v0"
    presentation_interpreter_version: str = "presentation-v0"

    def fingerprint(self) -> str: return digest(self)


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
    trait_schema_version: str = "trait-v0"  # intentionally outside identity and RNG selection inputs

    def basis(self) -> "OpportunityBasis":
        # Deliberately excludes FPS, packet ids, sample counts and fragment ids.
        return OpportunityBasis(self.session_id, self.occurrence_id, self.snapshot.fingerprint())


@dataclass(frozen=True)
class OpportunityBasis:
    session_id: str
    semantic_occurrence_id: str
    snapshot_fingerprint: str

    @property
    def opportunity_id(self) -> str: return digest("opportunity", self)


@dataclass(frozen=True)
class CandidateContribution:
    species: str
    lifecycle_cohort: str
    fish_mode: str
    response_slice: str
    behavior_anchor_ref: Optional[str]
    semantic_support_ref: str
    materialization_profile_ref: str
    engagement_mass: float
    quality_weights: Tuple[Tuple[int, float], ...] = ((1, 0.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0))

    @property
    def basis_key(self) -> str:
        return digest("candidate", self.species, self.lifecycle_cohort, self.fish_mode,
                      self.response_slice, self.behavior_anchor_ref, self.semantic_support_ref,
                      self.materialization_profile_ref)


@dataclass(frozen=True)
class CandidateEntry:
    basis_key: str
    species: str
    lifecycle_cohort: str
    fish_mode: str
    response_slice: str
    behavior_anchor_ref: Optional[str]
    semantic_support_ref: str
    materialization_profile_ref: str
    engagement_mass: float
    quality_weights: Tuple[Tuple[int, float], ...]


@dataclass(frozen=True)
class MeaningResponse:
    presentation_event: str
    exposure: str
    feeding_match: str
    response_grade: str


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
    quality_support: Tuple[int, ...]
    anchor_ref: Optional[str]
    reproductive_eligible: bool


@dataclass(frozen=True)
class ConcreteFishResult:
    species: str
    fish_mode: str
    quality: int
    anchor_ref: Optional[str]
    reproductive_eligible: bool


class PreGenerationHarness:
    def __init__(self): self._claims = {}

    def resolve(self, occurrence: RootSemanticOccurrence, contributions: Iterable[CandidateContribution]) -> ResolveResult:
        oid = occurrence.basis().opportunity_id
        if oid in self._claims: return self._claims[oid]
        grouped = {}
        # Resolution is opportunity-scoped: contributions from another semantic
        # support are not eligible merely because they arrived in the same packet.
        for c in contributions:
            if c.semantic_support_ref != occurrence.support.ref:
                continue
            grouped.setdefault(c.basis_key, []).append(c)
        entries = []
        for key, cs in grouped.items():
            first = cs[0]
            mass = sum(c.engagement_mass for c in cs)
            q = tuple((quality, sum(c.quality_weights[i][1] for c in cs) / len(cs)) for i, quality in enumerate([1,2,3,4,5]))
            entries.append(CandidateEntry(key, first.species, first.lifecycle_cohort, first.fish_mode,
                first.response_slice, first.behavior_anchor_ref, first.semantic_support_ref,
                first.materialization_profile_ref, mass, q))
        entries = tuple(sorted(entries, key=lambda e: e.basis_key))
        grade = "HIGH" if occurrence.exposure == "HIGH" and occurrence.feeding_match == "VALID" else ("LOW" if occurrence.exposure == "LOW" else "NORMAL")
        meaning = MeaningResponse(occurrence.presentation_event, occurrence.exposure, occurrence.feeding_match, grade)
        total = sum(e.engagement_mass for e in entries)
        roll = rng_u(occurrence.seed, "selection", oid)
        selected = None
        if total:
            cursor = roll * total
            for e in entries:
                cursor -= e.engagement_mass
                if cursor < 0: selected = e.basis_key; break
        result = ResolveResult(oid, occurrence.snapshot.fingerprint(), meaning, entries, selected, roll)
        self._claims[oid] = result
        return result

    def materialization_plan(self, result: ResolveResult) -> Optional[MaterializationPlan]:
        if not result.selected_basis_key: return None
        e = next(e for e in result.entries if e.basis_key == result.selected_basis_key)
        eligible = tuple(q for q, w in e.quality_weights if w > 0)
        if not eligible: raise ValueError("selected candidate has no legal generation support")
        return MaterializationPlan(e.basis_key, eligible, e.behavior_anchor_ref,
                                   e.fish_mode == "SPAWN_GUARD")

    def materialize(self, result: ResolveResult, seed: Optional[str] = None) -> Optional[ConcreteFishResult]:
        plan = self.materialization_plan(result)
        if plan is None: return None
        e = next(e for e in result.entries if e.basis_key == plan.candidate_basis_key)
        eligible = plan.quality_support
        s = seed or result.opportunity_id
        quality = eligible[min(int(rng_u(s, "trait", e.basis_key) * len(eligible)), len(eligible)-1)]
        reproductive = e.fish_mode == "SPAWN_GUARD" and quality >= 2
        return ConcreteFishResult(e.species, e.fish_mode, quality, e.behavior_anchor_ref, reproductive)


def fixture_occurrence(variant: str = "A", snapshot: Optional[ResolveSnapshotBundle] = None) -> RootSemanticOccurrence:
    return RootSemanticOccurrence("session-1", "occ-deflection-1", "DEFLECTION", "HIGH", "VALID",
                                  SemanticSupportRef("GRASS_EDGE_01"), snapshot or ResolveSnapshotBundle())


def fixture_contributions(fragments: int = 1) -> Tuple[CandidateContribution, ...]:
    mass = 1.0 / fragments
    return tuple(CandidateContribution("Bass", "adult", "NORMAL", "FEEDING", None, "GRASS_EDGE_01", "bass-normal", mass) for _ in range(fragments))


if __name__ == "__main__":
    h = PreGenerationHarness(); o = fixture_occurrence(); r = h.resolve(o, fixture_contributions())
    print(json.dumps({"opportunity_id": r.opportunity_id, "selected": r.selected_basis_key, "fish": h.materialize(r).__dict__}, sort_keys=True))
