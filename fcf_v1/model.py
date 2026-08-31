"""RC4 domain data types.

The types deliberately keep world facts, species capability, slice/program
state, opportunities, candidates, and settlement state separate. They are
plain dataclasses so an engine or editor can serialize them without depending
on a framework.
"""

from dataclasses import dataclass, field
from enum import Enum
import math
from typing import FrozenSet, Optional, Tuple


class EntryMotive(str, Enum):
    FORAGE = "FORAGE"
    DEFEND = "DEFEND"
    INVESTIGATE = "INVESTIGATE"
    NONE = "NONE"


class EntryGrade(str, Enum):
    NONE = "NONE"
    WEAK = "WEAK"
    NORMAL = "NORMAL"
    STRONG = "STRONG"
    VERY_STRONG = "VERY_STRONG"
    CERTAIN = "CERTAIN"


GRADE_PROBABILITY = {
    EntryGrade.NONE: 0.0,
    EntryGrade.WEAK: 0.15,
    EntryGrade.NORMAL: 0.40,
    EntryGrade.STRONG: 0.70,
    EntryGrade.VERY_STRONG: 0.90,
    EntryGrade.CERTAIN: 1.0,
}


class ContactType(str, Enum):
    ENGULF = "ENGULF"
    SUCK_INTAKE = "SUCK_INTAKE"
    PICKUP = "PICKUP"
    SLASH = "SLASH"
    BITE_REMOVE = "BITE_REMOVE"
    NIBBLE = "NIBBLE"


class SettlementKind(str, Enum):
    RETURN = "RETURN"
    RETURN_WARY = "RETURN_WARY"
    RELOCATE = "RELOCATE"
    RECOVERY_HOLD = "RECOVERY_HOLD"
    REMOVE_STOCK = "REMOVE_STOCK"


@dataclass(frozen=True)
class SpeciesCapability:
    species_id: str
    q: float
    allowed_contacts: FrozenSet[ContactType]
    sensory_channels: FrozenSet[str]
    anatomy_profile: str
    history_schema: str


@dataclass(frozen=True)
class WorldFacts:
    """Species-neutral physical truth; interpretation happens in a resolver."""

    water_temperature_c: float
    dissolved_oxygen_mg_l: float
    flow_vector: Tuple[float, float, float]
    depth_m: float
    structure_tags: FrozenSet[str]
    substrate: str
    illumination_lux: float
    turbidity: float
    resource_state: str
    barometric_pressure_hpa: Optional[float] = None
    barometric_trend: Optional[str] = None


@dataclass(frozen=True)
class ActualPresentation:
    """Compiled player/object/environment relation, not raw item identity."""

    presented_size_relative: float
    silhouette: str
    flash_grade: str
    vibration_grade: str
    displacement_grade: str
    speed_band: str
    acceleration: float
    drift_quality: str
    stability: float
    bottom_relation: str
    structure_contact: bool
    nest_intrusion: bool


@dataclass(frozen=True)
class FishVariant:
    """Static, flattened policy variant; never an unbounded runtime mixin."""

    variant_id: str
    species_id: str
    policy_overrides: Tuple[Tuple[str, str], ...]


@dataclass(frozen=True)
class LifecycleSlice:
    slice_id: str
    species_id: str
    lifecycle_state: str
    behavior_program: str
    entered_at: float
    minimum_hold_s: float
    exit_eligibility: str


@dataclass
class PopulationSource:
    source_id: str
    slice_id: str
    actual_supply: float
    q: float
    encounter_hold: float = 0.0
    recovery_hold: float = 0.0
    removed_stock: float = 0.0
    _reservation_seq: int = field(default=0, init=False, repr=False)

    def __post_init__(self) -> None:
        if not math.isfinite(self.q) or self.q <= 0:
            raise ValueError("q must be finite and > 0")
        for name in ("actual_supply", "encounter_hold", "recovery_hold", "removed_stock"):
            value = getattr(self, name)
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and >= 0")

    @property
    def realizable_units(self) -> int:
        # q is a gameplay-semantic scale; a non-positive q is invalid config.
        return int(self.actual_supply // self.q)

    def reserve(self) -> str:
        if self.actual_supply + 1e-12 < self.q:
            raise ValueError("insufficient ActualSupply for atomic reservation")
        self.actual_supply -= self.q
        self.encounter_hold += self.q
        self._reservation_seq += 1
        return f"{self.source_id}:reservation:{self._reservation_seq}"


@dataclass(frozen=True)
class EntryOpportunity:
    opportunity_id: str
    scope_id: str
    slice_id: str
    source_id: str
    kind: str  # FIRST_ACCESS | ARRIVAL | SEMANTIC_REEVALUATION
    trigger_id: Optional[str] = None
    semantic_snapshot_fingerprint: str = ""
    population_revision: str = ""
    eligible_units_before: Optional[int] = None
    sim_time: float = 0.0


@dataclass(frozen=True)
class EntrantProposal:
    proposal_id: str
    opportunity_id: str
    source_id: str
    slice_id: str
    scope_id: str
    unit_index: int
    motive: EntryMotive
    entry_probability: float
    created_at: float


@dataclass
class Candidate:
    candidate_id: str
    proposal: EntrantProposal
    q: float
    state: str = "ATTENTIVE"
    settled: bool = False
    contact_type: Optional[ContactType] = None
    reservation_id: Optional[str] = None
    settlement_transaction_id: Optional[str] = None
    commit_attempted: bool = False
    commit_result: Optional[bool] = None


@dataclass(frozen=True)
class ContactIntent:
    candidate_id: str
    target_id: str
    created_at: float
    geometric_order: Tuple[float, float]
    contact_type: ContactType
    semantic_intent_id: Optional[str] = None
