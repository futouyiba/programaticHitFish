"""Pure RC4 resolvers for values that must be replayable and explainable."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .model import ContactType, EntryGrade, EntryMotive, GRADE_PROBABILITY
from .engine import clamp


OCCUPANCY_POINTS = {"FORBIDDEN": 0.0, "ACCIDENTAL": 0.1, "MARGINAL": 1.0, "GOOD": 4.0, "PRIME": 12.0}


def allocate_occupancy(
    distributable_psu: float,
    spatial_presence: float,
    rows: Sequence[Tuple[str, float, str]],
    *,
    nominal_density: float,
    crowding_tolerance: float,
) -> Tuple[Dict[str, float], float]:
    """RC4 iterative cap + redistribute allocation.

    Each row is ``(node_id, capacity, grade)``. Rows are input as semantic
    records; serialization order never changes the result. Equal-priority or
    duplicate node IDs are caller/compiler errors.
    """
    if distributable_psu < 0 or not 0 <= spatial_presence <= 1:
        raise ValueError("invalid distributable_psu or spatial_presence")
    if nominal_density < 0 or crowding_tolerance < 0:
        raise ValueError("density and crowding tolerance must be non-negative")
    if len({node for node, _, _ in rows}) != len(rows):
        raise ValueError("duplicate occupancy node")
    target = distributable_psu * spatial_presence
    remaining = target
    active = {node for node, _, grade in rows if grade not in ("FORBIDDEN",) and OCCUPANCY_POINTS[grade] > 0}
    result = {node: 0.0 for node, _, _ in rows}
    while active and remaining > 1e-12:
        denom = sum(cap * OCCUPANCY_POINTS[grade] for node, cap, grade in rows if node in active)
        if denom <= 0:
            break
        capped = set()
        pass_remaining = remaining
        additions: Dict[str, float] = {}
        for node, cap, grade in rows:
            if node not in active:
                continue
            desired = pass_remaining * cap * OCCUPANCY_POINTS[grade] / denom
            maximum = cap * nominal_density * crowding_tolerance
            if desired >= maximum - 1e-12:
                additions[node] = maximum
                capped.add(node)
        if not capped:
            for node, cap, grade in rows:
                if node in active:
                    result[node] += pass_remaining * cap * OCCUPANCY_POINTS[grade] / denom
            remaining = 0.0
        else:
            for node, amount in additions.items():
                result[node] += amount
            remaining -= sum(additions.values())
            active -= capped
    reserve = distributable_psu - target + max(0.0, remaining)
    return result, reserve


def resolve_motive(priority: Sequence[EntryMotive], predicates: Mapping[EntryMotive, bool]) -> EntryMotive:
    """Select the first true motive; duplicate priority is a compile error."""
    if len(priority) != len(set(priority)):
        raise ValueError("equal/duplicate motive priority is ambiguous")
    for motive in priority:
        if predicates.get(motive, False):
            return motive
    return EntryMotive.NONE


_GRADE_ORDER = list(EntryGrade)


def resolve_entry_offer(
    base: EntryGrade,
    *,
    strongest_positive_steps: int = 0,
    strongest_negative_steps: int = 0,
    explicit_compound_steps: int = 0,
    deny: bool = False,
    cap: Optional[EntryGrade] = None,
) -> EntryGrade:
    """Discrete base + strongest +/- + explicit compound resolver.

    Modifiers are integer grade steps, never arbitrary multiplicative
    coefficients. A deny dominates all modifiers; cap is applied last.
    """
    if deny:
        return EntryGrade.NONE
    if min(strongest_positive_steps, strongest_negative_steps, explicit_compound_steps) < 0:
        raise ValueError("modifier steps must be non-negative")
    index = _GRADE_ORDER.index(base)
    index += strongest_positive_steps + explicit_compound_steps
    index -= strongest_negative_steps
    result = _GRADE_ORDER[max(0, min(len(_GRADE_ORDER) - 1, index))]
    if cap is not None and _GRADE_ORDER.index(result) > _GRADE_ORDER.index(cap):
        result = cap
    return result


class EncounterState(str, Enum):
    ATTENTIVE = "ATTENTIVE"
    FOLLOWING = "FOLLOWING"
    INSPECTING = "INSPECTING"
    CHASING = "CHASING"
    INTERCEPTING = "INTERCEPTING"
    THREAT_TRACK = "THREAT_TRACK"
    COMMIT_READY = "COMMIT_READY"
    REJECTED = "REJECTED"
    DISENGAGED = "DISENGAGED"


def encounter_step(state: EncounterState, motive: EntryMotive, event: str, *, task_difficult: bool = False) -> EncounterState:
    """Small deterministic transition table; no per-transition stochastic gate."""
    if state in (EncounterState.REJECTED, EncounterState.DISENGAGED, EncounterState.COMMIT_READY):
        return state
    if motive == EntryMotive.DEFEND:
        if event in ("NEST_INTRUSION_ONSET", "INTRUSION_REMAINS_2S"):
            return EncounterState.THREAT_TRACK
        if state == EncounterState.THREAT_TRACK and event == "INTRUSION_PERSISTS":
            return EncounterState.COMMIT_READY
    if motive == EntryMotive.FORAGE:
        if state == EncounterState.ATTENTIVE and event == "TARGET_SALIENT":
            return EncounterState.FOLLOWING
        if state == EncounterState.FOLLOWING and event == "INTERCEPT_WINDOW":
            return EncounterState.INTERCEPTING
        if state == EncounterState.INTERCEPTING and event == "INTERCEPT_SUCCESS":
            return EncounterState.COMMIT_READY
        if task_difficult and event == "PURSUIT_COST_EXCEEDED":
            return EncounterState.DISENGAGED
    return state


def hook_compatibility(
    contact_type: ContactType,
    allowed_contacts: Iterable[ContactType],
    *,
    geometry_exposure: float,
    rig_orientation: float,
    timing: float,
) -> float:
    """Downstream Hook input only; upstream fish presence is not consulted."""
    if contact_type not in set(allowed_contacts):
        return 0.0
    for value in (geometry_exposure, rig_orientation, timing):
        if not 0 <= value <= 1:
            raise ValueError("hook inputs must be in [0,1]")
    return clamp(geometry_exposure * rig_orientation * timing)


def validate_arrival_placement(*, produces_new_units: bool, temporal_factor: float) -> None:
    """Enforce RC4's ARRIVAL producer XOR T-multiplier contract."""
    if produces_new_units and temporal_factor != 1.0:
        raise ValueError("ARRIVAL cannot both produce new units and apply T<1")
    if not 0.0 <= temporal_factor <= 1.0:
        raise ValueError("temporal_factor must be in [0,1]")
