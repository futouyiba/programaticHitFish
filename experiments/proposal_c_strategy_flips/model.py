"""Proposal C response model, transcribed for an independent strategy experiment.

Authority (read-only input, all Candidate / Working, not production):

  futouyiba/HitFish-Up @ dcba9ee9 (2026-11-05)
    docs/proposals/lure-response-proposal-c-evaluation-items.md
    docs/proposals/lure-response-proposal-c-semantic-contract.md
    docs/proposals/lure-response-proposal-c-response-algorithm-v1.md
    docs/proposals/lure-response-proposal-c-fish-condition-mechanism-contracts.md
    docs/proposals/lure-response-proposal-c-opportunity-l-production.md
    prototypes/lure-response/proposal_c_end_to_end_probe.py
    prototypes/lure-response/proposal_c_opportunity_support_probe.py

This module copies the formulas so the experiment is self-contained. It grants no
normative status to any value here and must not be imported by production code.

Two layers are kept apart, as the contracts require:
  response C        -- five-item decision margin, sibling max
  opportunity yield -- explicitly a toy model (r * tau * coverage), used only for
                       sensitivity. It is not a claim about real game efficiency.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# --- Working parameters (Candidate; see calibration register) ---
K_CLOSE = 0.19          # no-theta single-direction scale
TRIGGER_BUDGET = 0.10   # Working budget, guardrail 0.15
K_WARY = 1.0            # Working probe scale
M0 = 0.00
M1 = 0.40

# Common tier scale, Owner 2026-11-05.
TIER_ANCHORS = (0.0, 0.25, 0.60, 1.0)
TIER_SCALES = {"tier-v2": TIER_ANCHORS}

# Opportunity toy parameters (proposal_c_opportunity_support_probe.py).
DWELL_UNITS = 0.80
Q_CAP = 1.00

RESOLVED = "Resolved"
UNKNOWN = "Unknown"
NOT_CONFIGURED = "NotConfigured"
NOT_APPLICABLE = "NotApplicable"
RI = "ResolutionIncomplete"
REJECT = "Reject"
INVALID = "InvalidInput"


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def clamp01(x: float) -> float:
    return clamp(x, 0.0, 1.0)


def tier_coordinate(value: float, anchors=TIER_ANCHORS) -> float:
    if value <= anchors[0]:
        return 0.0
    for i in range(len(anchors) - 1):
        lo, hi = anchors[i], anchors[i + 1]
        if value <= hi:
            return i + (value - lo) / (hi - lo)
    return float(len(anchors) - 1)


def tier_value(coord: float, anchors=TIER_ANCHORS) -> float:
    c = clamp(coord, 0.0, 3.0)
    i = int(c)
    if i >= 3:
        return anchors[3]
    return anchors[i] + (anchors[i + 1] - anchors[i]) * (c - i)


def shift_affinity(base: float, shift: float, anchors=TIER_ANCHORS) -> float:
    return tier_value(tier_coordinate(base, anchors) + shift, anchors)


def activity_multiplier(activity: float) -> float:
    """clamp(1/A, 0.5, 2); A=0 treated as 2. A must be in [0,2]."""
    if activity == 0.0:
        return 2.0
    return clamp(1.0 / activity, 0.5, 2.0)


def willingness_threshold(motivation: float) -> float:
    base = 0.60 - 0.40 * motivation
    if motivation > 0.80:
        base -= 0.50 * (motivation - 0.80)
    return base


def _finite(x) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(x)


def _normalize_support(value):
    """float | status -> (status, value_or_None)."""
    if isinstance(value, str):
        if value == REJECT:
            return REJECT, 0.0
        if value in (UNKNOWN, NOT_CONFIGURED, NOT_APPLICABLE, INVALID):
            return value, None
        return INVALID, None
    if not _finite(value):
        return INVALID, None
    if not 0.0 <= value <= 1.0:
        return INVALID, None
    return RESOLVED, float(value)


def food_value(base, shift, size_adjustment, scale):
    """CurrentFoodValue per evaluation-items §2 and semantic-contract §5.1."""
    if not (_finite(base) and 0.0 <= base <= 1.0):
        return INVALID, None
    if not (_finite(shift) and -1.0 <= shift <= 1.0):
        return INVALID, None
    if not _finite(size_adjustment):
        return INVALID, None
    shifted = shift_affinity(base, shift, scale)
    return RESOLVED, clamp01(shifted + size_adjustment)


@dataclass
class FishCondition:
    activity: object
    motivation: object
    wariness: object
    diet_shift: dict = field(default_factory=dict)   # family -> s | status
    tier_scale_version: str = "tier-v2"


@dataclass
class Strategy:
    name: str
    supports: dict          # family -> 0..1 | status
    base_affinity: dict     # family -> 0..1
    q: float                # speed / InterceptSpeedLimit
    siblings: list = field(default_factory=list)  # declared sibling set; defaults to supports
    trigger_strength: dict = field(default_factory=dict)  # family -> StateMatchStrength
    size_adjustment: float = 0.0
    coverage: float = 1.0   # opportunity toy only
    suspicion_load: float = 0.0
    notes: str = ""

    def sibling_set(self):
        return list(self.siblings) if self.siblings else list(self.supports)


def evaluate_family(family, strategy, fc: FishCondition):
    """Return (status, C) for one family branch."""
    scale = TIER_SCALES.get(fc.tier_scale_version)
    if scale is None:
        return RI, None

    if family not in strategy.supports:
        return UNKNOWN, None              # declared sibling without support evidence
    status, support = _normalize_support(strategy.supports.get(family))
    if status == REJECT:
        return REJECT, 0.0
    if status != RESOLVED:
        return status, None

    act_status = fc.activity
    if not _finite(act_status) or not 0.0 <= act_status <= 2.0:
        return INVALID, None
    a_mult = activity_multiplier(act_status)

    m = fc.motivation
    if not _finite(m) or not 0.0 <= m <= 1.0:
        return INVALID, None

    w = fc.wariness
    if not _finite(w) or not 0.0 <= w <= 1.0:
        return INVALID, None

    if not _finite(strategy.q) or strategy.q < 0.0:
        return INVALID, None

    base = strategy.base_affinity.get(family)
    if base is None:
        return UNKNOWN, None
    shift = fc.diet_shift.get(family)
    if shift is None:
        return UNKNOWN, None

    f_status, food = food_value(base, shift, strategy.size_adjustment, scale)
    if f_status != RESOLVED:
        return f_status, None

    strength = strategy.trigger_strength.get(family)
    if strength is None:
        return UNKNOWN, None              # missing StateMatchStrength is not zero
    if not _finite(strength) or not 0.0 <= strength <= 1.0:
        return INVALID, None
    trigger = TRIGGER_BUDGET * strength

    closing = K_CLOSE * strategy.q ** 2 * a_mult
    risk = K_WARY * w * strategy.suspicion_load
    threshold = willingness_threshold(m)

    margin = food + trigger - closing - risk - threshold
    c = clamp01((margin - M0) / (M1 - M0))
    return RESOLVED, support * c


def response(strategy: Strategy, fc: FishCondition):
    """Sibling max with skipped provenance; returns (status, C_feed, skipped, detail)."""
    results = {}
    detail = {}
    for family in strategy.sibling_set():
        status, value = evaluate_family(family, strategy, fc)
        results[family] = (status, value)
        detail[family] = status

    resolved = [v for s, v in results.values() if s == RESOLVED]
    rejected = [v for s, v in results.values() if s == REJECT]
    skipped = {f: s for f, (s, _) in results.items()
               if s in (RI, UNKNOWN, NOT_CONFIGURED, NOT_APPLICABLE)}
    if any(s == INVALID for s, _ in results.values()):
        return INVALID, None, skipped, detail
    if not resolved and rejected:
        return REJECT, 0.0, skipped, detail
    if not resolved and not rejected:
        return RI, None, skipped, detail
    return RESOLVED, max(resolved + rejected), skipped, detail


# --- Opportunity toy model (explicitly an assumption, not a game-efficiency claim) ---

def encounter_rate(q: float) -> float:
    return q / (1.0 + q / Q_CAP)


def dwell_support(q: float) -> float:
    return DWELL_UNITS / (DWELL_UNITS + q)


def toy_yield(c_feed, q: float, coverage: float = 1.0) -> float:
    """Relative per-time yield. NOT real game efficiency; toy sensitivity only."""
    if c_feed is None:
        return 0.0
    return coverage * encounter_rate(q) * dwell_support(q) * c_feed


def describe(strategy: Strategy, fc: FishCondition) -> dict:
    status, c, skipped, detail = response(strategy, fc)
    return {
        "strategy": strategy.name,
        "status": status,
        "C": c,
        "yield": toy_yield(c, strategy.q, strategy.coverage) if status == RESOLVED else None,
        "skipped": skipped,
        "branches": detail,
        "q": strategy.q,
        "activity": fc.activity,
        "motivation": fc.motivation,
        "wariness": fc.wariness,
        "diet_shift": dict(fc.diet_shift),
    }
