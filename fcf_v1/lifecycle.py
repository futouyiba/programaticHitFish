"""Stable PopulationSlice identity and conservation-preserving lifecycle transfer."""

from dataclasses import dataclass
import threading
from typing import Dict, Tuple


@dataclass(frozen=True)
class SliceKey:
    species_population_id: str
    cohort_key: str
    lifecycle_role_key: str


@dataclass
class LifecycleCommitment:
    key: SliceKey
    lifecycle_state: str
    entered_at: float
    minimum_hold_s: float
    hysteresis: float
    exit_eligibility: str


class SliceAllocator:
    """Moves PSU between stable slice buckets as one logical transaction."""

    def __init__(self, buckets: Dict[SliceKey, float]):
        self.buckets = dict(buckets)
        self._lock = threading.RLock()

    def transfer(self, from_key: SliceKey, to_key: SliceKey, amount: float) -> None:
        with self._lock:
            if amount < 0:
                raise ValueError("amount must be >= 0")
            if self.buckets.get(from_key, 0.0) + 1e-12 < amount:
                raise ValueError("insufficient PSU for slice transfer")
            if from_key == to_key:
                raise ValueError("same-key lifecycle transfer is not a state transition")
            before = sum(self.buckets.values())
            # Apply as a two-write transaction; restore if the second write fails.
            old_from = self.buckets.get(from_key, 0.0)
            old_to = self.buckets.get(to_key, 0.0)
            try:
                self.buckets[from_key] = old_from - amount
                self.buckets[to_key] = old_to + amount
            except Exception:
                self.buckets[from_key] = old_from
                self.buckets[to_key] = old_to
                raise
            assert abs(sum(self.buckets.values()) - before) < 1e-9
