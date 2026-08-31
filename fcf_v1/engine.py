"""Small deterministic RC4 engine used as an executable contract oracle."""

from copy import deepcopy
from dataclasses import dataclass, field
import hashlib
import threading
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

from .model import (
    Candidate,
    ContactIntent,
    EntryGrade,
    EntryMotive,
    EntryOpportunity,
    EntrantProposal,
    GRADE_PROBABILITY,
    PopulationSource,
    SettlementKind,
)
from .journal import JournalAdapter


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_uniform(seed: str) -> float:
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") / float(1 << 64)


@dataclass
class OpportunityLedger:
    """One stable record per PresentationScope × Slice × Source."""

    consumed_opportunities: Set[str] = field(default_factory=set)
    consumed_semantic_keys: Dict[Tuple[str, str, str], str] = field(default_factory=dict)
    consumed_triggers: Set[str] = field(default_factory=set)
    materialized_proposals: Set[str] = field(default_factory=set)
    records: Dict[str, Dict[str, object]] = field(default_factory=dict)

    def admit(self, opportunity: EntryOpportunity) -> bool:
        if opportunity.kind not in {"FIRST_ACCESS", "ARRIVAL", "SEMANTIC_REEVALUATION"}:
            raise ValueError("unsupported entry opportunity kind")
        if opportunity.kind == "SEMANTIC_REEVALUATION" and not opportunity.trigger_id:
            raise ValueError("semantic reevaluation requires stable trigger_id")
        if opportunity.opportunity_id in self.consumed_opportunities:
            current = self.records[opportunity.opportunity_id]
            replay_identity = {
                "presentation_scope_id": opportunity.scope_id,
                "population_slice_key": opportunity.slice_id,
                "source_id": opportunity.source_id,
                "opportunity_kind": opportunity.kind,
                "semantic_trigger_id": opportunity.trigger_id,
                "semantic_snapshot_fingerprint": opportunity.semantic_snapshot_fingerprint,
                "source_population_revision_basis": opportunity.population_revision,
                "eligible_units_before": opportunity.eligible_units_before,
            }
            if any(current.get(key) != value for key, value in replay_identity.items()):
                raise ValueError("opportunity_id replay identity mismatch")
            return False
        if opportunity.kind == "FIRST_ACCESS":
            if opportunity.trigger_id is not None:
                raise ValueError("FIRST_ACCESS cannot use trigger_id to create extra partitions")
            semantic_key = (opportunity.kind, "scope-source-first-access", "")
        elif opportunity.kind == "ARRIVAL":
            if not opportunity.trigger_id and not opportunity.population_revision:
                raise ValueError("ARRIVAL requires stable arrival identity or population revision")
            semantic_key = (opportunity.kind, opportunity.trigger_id or "", opportunity.population_revision)
        else:
            semantic_key = (opportunity.kind, opportunity.trigger_id or "", "")
        previous_id = self.consumed_semantic_keys.get(semantic_key)
        if previous_id is not None:
            raise ValueError(f"semantic opportunity already consumed as {previous_id}")
        if opportunity.kind == "SEMANTIC_REEVALUATION" and opportunity.trigger_id:
            if opportunity.trigger_id in self.consumed_triggers:
                return False
            self.consumed_triggers.add(opportunity.trigger_id)
        self.consumed_opportunities.add(opportunity.opportunity_id)
        self.consumed_semantic_keys[semantic_key] = opportunity.opportunity_id
        self.records[opportunity.opportunity_id] = {
            "opportunity_id": opportunity.opportunity_id,
            "presentation_scope_id": opportunity.scope_id,
            "population_slice_key": opportunity.slice_id,
            "source_id": opportunity.source_id,
            "opportunity_kind": opportunity.kind,
            "semantic_trigger_id": opportunity.trigger_id,
            "semantic_snapshot_fingerprint": opportunity.semantic_snapshot_fingerprint,
            "source_population_revision_basis": opportunity.population_revision,
            "eligible_units_before": opportunity.eligible_units_before,
            "consumed_units": [],
            "consumed_at_sim_time": opportunity.sim_time,
            "result_summary": None,
        }
        return True


class FCFEngine:
    def __init__(
        self,
        sources: Iterable[PopulationSource],
        detailed_capacity: int = 4,
        journal: Optional[JournalAdapter] = None,
        hydrate_journal: bool = False,
    ):
        if detailed_capacity < 0:
            raise ValueError("detailed_capacity must be non-negative")
        source_list = list(sources)
        if len({s.source_id for s in source_list}) != len(source_list):
            raise ValueError("source_id must be unique")
        self.sources: Dict[str, PopulationSource] = {s.source_id: s for s in source_list}
        self.ledgers: Dict[Tuple[str, str, str], OpportunityLedger] = {}
        self.pending: Dict[str, EntrantProposal] = {}
        self.proposals: Dict[str, EntrantProposal] = {}
        self.candidates: Dict[str, Candidate] = {}
        self._settlement_transactions: Set[str] = set()
        self._settlement_owner: Dict[str, str] = {}
        self._lock = threading.RLock()
        self.detailed_capacity = detailed_capacity
        self._candidate_seq = 0
        self.journal = journal
        if hydrate_journal:
            if self.journal is None or not hasattr(self.journal, "records"):
                raise ValueError("hydrate_journal requires a readable journal")
            self._hydrate_journal()

    def _hydrate_journal(self) -> None:
        """Replay a journal against a pre-journal source snapshot.

        The scheduler must supply the source snapshot from immediately before
        the journal's first event. A mismatch is a hard error; silently
        continuing would risk duplicate reservation or settlement.
        """
        records = self.journal.records()
        self._validate_journal_records(records)
        pending_settlements = []
        max_candidate_seq = 0
        max_reservation_seq: Dict[str, int] = {}
        for event in records:
            typ = event["event_type"]
            payload = event["payload"]
            if typ == "OPPORTUNITY_CONSUMED":
                op = EntryOpportunity(
                    event["event_id"].split("opportunity:", 1)[-1], payload["scope"], payload["slice"],
                    payload["source"], payload["kind"], payload.get("trigger"),
                    payload.get("semantic_snapshot_fingerprint", ""), payload.get("revision", ""),
                    payload.get("eligible_units_before"), payload.get("sim_time", 0.0),
                )
                self._ledger(op).admit(op)
            elif typ == "CANDIDATE_RESERVED":
                source = self.sources[payload["source"]]
                q = float(payload["q"])
                if source.actual_supply + 1e-12 < q:
                    raise ValueError("journal reservation exceeds supplied source snapshot")
                source.actual_supply -= q
                source.encounter_hold += q
                proposal = EntrantProposal(
                    payload["proposal_id"], payload["opportunity_id"], payload["source"],
                    payload["slice"], payload["scope"], int(payload["unit_index"]),
                    EntryMotive(payload["motive"]), float(payload["entry_probability"]),
                    float(payload["created_at"]),
                )
                self.proposals[proposal.proposal_id] = proposal
                ledger = self.ledgers[(proposal.scope_id, proposal.slice_id, proposal.source_id)]
                ledger.materialized_proposals.add(proposal.proposal_id)
                candidate = Candidate(payload["candidate_id"], proposal, q, reservation_id=payload["reservation_id"])
                self.candidates[candidate.candidate_id] = candidate
                try:
                    max_candidate_seq = max(max_candidate_seq, int(str(candidate.candidate_id).rsplit("-", 1)[1]))
                except (ValueError, IndexError):
                    pass
                try:
                    max_reservation_seq[proposal.source_id] = max(
                        max_reservation_seq.get(proposal.source_id, 0),
                        int(str(candidate.reservation_id).rsplit(":", 1)[1]),
                    )
                except (ValueError, IndexError):
                    pass
            elif typ == "CANDIDATE_SETTLED":
                pending_settlements.append((event["event_id"].split("settlement:", 1)[-1], payload))
        for transaction_id, payload in pending_settlements:
            self._settle(payload["candidate_id"], SettlementKind(payload["kind"]),
                         relocate_source_id=payload.get("relocate_source_id"),
                         settlement_transaction_id=transaction_id)
        self._candidate_seq = max_candidate_seq
        for source_id, sequence in max_reservation_seq.items():
            self.sources[source_id]._reservation_seq = sequence

    @staticmethod
    def _validate_journal_records(records: Sequence[Mapping[str, Any]]) -> None:
        """Validate all payload shapes before mutating any recovered state."""
        required = {
            "OPPORTUNITY_CONSUMED": {"scope", "slice", "source", "kind", "trigger", "revision",
                                     "semantic_snapshot_fingerprint", "eligible_units_before"},
            "CANDIDATE_RESERVED": {"candidate_id", "proposal_id", "opportunity_id", "scope", "slice", "source",
                                    "unit_index", "motive", "entry_probability", "created_at", "reservation_id", "q"},
            "CANDIDATE_SETTLED": {"candidate_id", "reservation_id", "kind", "relocate_source_id", "q"},
        }
        for index, event in enumerate(records):
            event_type = event.get("event_type")
            if event_type not in required:
                raise ValueError(f"unsupported journal event type at index {index}")
            payload = event.get("payload")
            if not isinstance(payload, Mapping) or not required[event_type] <= set(payload):
                raise ValueError(f"invalid {event_type} payload at index {index}")

    def _journal_append(self, event_id: str, event_type: str, payload: Dict[str, Any]) -> None:
        if self.journal is not None:
            self.journal.append_once(event_id, event_type, payload)

    @staticmethod
    def canonical_opportunity_id(
        scope_id: str,
        slice_id: str,
        source_id: str,
        kind: str,
        trigger_or_partition: str,
        population_revision: str,
    ) -> str:
        """Stable semantic ID; runtime callback/tick IDs are excluded."""
        payload = "|".join(
            (scope_id, slice_id, source_id, kind, trigger_or_partition, population_revision)
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]

    def _ledger(self, opportunity: EntryOpportunity) -> OpportunityLedger:
        key = (opportunity.scope_id, opportunity.slice_id, opportunity.source_id)
        return self.ledgers.setdefault(key, OpportunityLedger())

    @staticmethod
    def entry_probability(a: float, t: float, e: float) -> float:
        """RC4 π = clamp(A × T × E, 0, 1)."""
        for value in (a, t, e):
            if not 0.0 <= value <= 1.0:
                raise ValueError("A, T and E must be in [0, 1]")
        return clamp(a * t * e)

    def form_proposals(
        self,
        opportunity: EntryOpportunity,
        *,
        accessible_fraction: float,
        temporal_factor: float,
        entry_grade: EntryGrade,
        motive: EntryMotive,
        now: float = 0.0,
        eligible_units: Optional[int] = None,
    ) -> List[EntrantProposal]:
        # Ledger consumption and deterministic draws are one serializable
        # operation under concurrent presentation evaluators.
        with self._lock:
            return self._form_proposals(
                opportunity,
                accessible_fraction=accessible_fraction,
                temporal_factor=temporal_factor,
                entry_grade=entry_grade,
                motive=motive,
                now=now,
                eligible_units=eligible_units,
            )

    def _form_proposals(
        self,
        opportunity: EntryOpportunity,
        *,
        accessible_fraction: float,
        temporal_factor: float,
        entry_grade: EntryGrade,
        motive: EntryMotive,
        now: float = 0.0,
        eligible_units: Optional[int] = None,
    ) -> List[EntrantProposal]:
        """Consume one legal opportunity and form finite source-local proposals.

        A proposal is a statistical eligibility result. It does not reserve
        population mass; reservation occurs only at materialization.
        """
        source = self.sources[opportunity.source_id]
        if source.slice_id != opportunity.slice_id:
            raise ValueError("opportunity source/slice provenance mismatch")
        if not isinstance(entry_grade, EntryGrade) or not isinstance(motive, EntryMotive):
            raise ValueError("entry_grade and motive must be typed enums")
        if eligible_units is not None and eligible_units < 0:
            raise ValueError("eligible_units must be non-negative")
        p = self.entry_probability(
            accessible_fraction, temporal_factor, GRADE_PROBABILITY[entry_grade]
        )
        local_ledger = self.ledgers.get((opportunity.scope_id, opportunity.slice_id, opportunity.source_id))
        if self.journal is not None and self.journal.get("opportunity:" + opportunity.opportunity_id) is not None:
            if local_ledger is None or opportunity.opportunity_id not in local_ledger.records:
                raise ValueError("opportunity exists in journal; hydrate runtime state before replay")
        ledger = self._ledger(opportunity)
        if not ledger.admit(opportunity):
            return []
        try:
            self._journal_append(
                "opportunity:" + opportunity.opportunity_id,
                "OPPORTUNITY_CONSUMED",
                {"scope": opportunity.scope_id, "slice": opportunity.slice_id, "source": opportunity.source_id,
                 "kind": opportunity.kind, "trigger": opportunity.trigger_id,
                 "revision": opportunity.population_revision,
                 "semantic_snapshot_fingerprint": opportunity.semantic_snapshot_fingerprint,
                 "eligible_units_before": opportunity.eligible_units_before},
            )
        except Exception:
            ledger.consumed_opportunities.discard(opportunity.opportunity_id)
            ledger.records.pop(opportunity.opportunity_id, None)
            if opportunity.kind == "SEMANTIC_REEVALUATION" and opportunity.trigger_id:
                ledger.consumed_triggers.discard(opportunity.trigger_id)
            for key, value in list(ledger.consumed_semantic_keys.items()):
                if value == opportunity.opportunity_id:
                    ledger.consumed_semantic_keys.pop(key, None)
            raise
        if motive == EntryMotive.NONE or entry_grade == EntryGrade.NONE:
            ledger.records[opportunity.opportunity_id]["result_summary"] = {
                "proposal_count": 0,
                "entry_probability": p,
            }
            return []
        units = source.realizable_units if eligible_units is None else min(
            eligible_units, source.realizable_units
        )
        proposals: List[EntrantProposal] = []
        for unit in range(max(0, units)):
            record = ledger.records[opportunity.opportunity_id]
            record["consumed_units"].append(unit)
            if stable_uniform(f"entry:{opportunity.opportunity_id}:{unit}") < p:
                proposal_id = f"{opportunity.opportunity_id}:u{unit}"
                proposals.append(
                    EntrantProposal(
                        proposal_id=proposal_id,
                        opportunity_id=opportunity.opportunity_id,
                        source_id=opportunity.source_id,
                        slice_id=opportunity.slice_id,
                        scope_id=opportunity.scope_id,
                        unit_index=unit,
                        motive=motive,
                        entry_probability=p,
                        created_at=now,
                    )
                )
                self.proposals[proposal_id] = proposals[-1]
        ledger.records[opportunity.opportunity_id]["result_summary"] = {
            "proposal_count": len(proposals),
            "entry_probability": p,
        }
        return proposals

    def opportunity_record(self, opportunity: EntryOpportunity) -> Optional[Mapping[str, object]]:
        """Read-only durable-style record for Explain/Replay tooling."""
        ledger = self.ledgers.get((opportunity.scope_id, opportunity.slice_id, opportunity.source_id))
        record = ledger.records.get(opportunity.opportunity_id) if ledger else None
        return deepcopy(record) if record is not None else None

    def materialize(self, proposal: EntrantProposal) -> Optional[Candidate]:
        """Materialize immediately or place as Pending without reservation."""
        with self._lock:
            return self._materialize(proposal)

    def _materialize(self, proposal: EntrantProposal) -> Optional[Candidate]:
        canonical = self.proposals.get(proposal.proposal_id)
        if canonical != proposal:
            raise ValueError("proposal is not a valid Entry result for this engine")
        source = self.sources.get(proposal.source_id)
        if source is None or source.slice_id != proposal.slice_id:
            raise ValueError("proposal source/slice provenance mismatch")
        if proposal.proposal_id in self.pending:
            return None
        if len(self.candidates) >= self.detailed_capacity:
            self.pending[proposal.proposal_id] = proposal
            return None
        return self._reserve_and_materialize(proposal)

    def _reserve_and_materialize(self, proposal: EntrantProposal) -> Optional[Candidate]:
        with self._lock:
            source = self.sources[proposal.source_id]
            ledger = self.ledgers.setdefault(
                (proposal.scope_id, proposal.slice_id, proposal.source_id), OpportunityLedger()
            )
            # Unit identity is source/opportunity-local; a proposal can be
            # materialized at most once even if a scheduler retries it.
            if proposal.proposal_id in ledger.materialized_proposals:
                return None
            if self.journal is not None and self.journal.get("reservation:" + proposal.proposal_id) is not None:
                raise ValueError("reservation already exists in journal; hydrate runtime state before replay")
            try:
                reservation_id = source.reserve()
            except ValueError:
                return None
            ledger.materialized_proposals.add(proposal.proposal_id)
            self._candidate_seq += 1
            candidate = Candidate(
                candidate_id=f"candidate-{self._candidate_seq}",
                proposal=proposal,
                q=source.q,
                reservation_id=reservation_id,
            )
            try:
                self._journal_append(
                    "reservation:" + proposal.proposal_id,
                    "CANDIDATE_RESERVED",
                    {"candidate_id": candidate.candidate_id, "proposal_id": proposal.proposal_id,
                     "opportunity_id": proposal.opportunity_id, "scope": proposal.scope_id,
                     "slice": proposal.slice_id, "source": proposal.source_id, "unit_index": proposal.unit_index,
                     "motive": proposal.motive.value, "entry_probability": proposal.entry_probability,
                     "created_at": proposal.created_at, "reservation_id": reservation_id, "q": source.q},
                )
            except Exception:
                source.actual_supply += source.q
                source.encounter_hold -= source.q
                ledger.materialized_proposals.discard(proposal.proposal_id)
                raise
            self.candidates[candidate.candidate_id] = candidate
            return candidate

    def open_slot(self) -> List[Candidate]:
        """Materialize pending proposals into an already-open slot."""
        with self._lock:
            return self._open_slot()

    def _open_slot(self) -> List[Candidate]:
        created: List[Candidate] = []
        for proposal_id in list(self.pending):
            if len(self.candidates) >= self.detailed_capacity:
                break
            proposal = self.pending.pop(proposal_id)
            candidate = self._reserve_and_materialize(proposal)
            if candidate is not None:
                created.append(candidate)
            else:
                # Reservation may race with another source consumer. Keep the
                # same proposal available while its original opportunity can
                # still be revalidated; never replace it with a new roll.
                self.pending[proposal_id] = proposal
        return created

    def release_slot(self, candidate_id: str, *, now: float = 0.0) -> List[Candidate]:
        """Close a settled Candidate's slot, then materialize Pending.

        An active Candidate cannot be evicted: its reservation must first be
        settled by an explicit terminal reason.
        """
        with self._lock:
            candidate = self.candidates.get(candidate_id)
            if candidate is None:
                raise KeyError(candidate_id)
            if not candidate.settled:
                raise ValueError("cannot release an unsettled Candidate slot")
            self.candidates.pop(candidate_id)
            return self._open_slot()

    def commit(self, candidate_id: str, grade: EntryGrade) -> bool:
        with self._lock:
            return self._commit(candidate_id, grade)

    def _commit(self, candidate_id: str, grade: EntryGrade) -> bool:
        candidate = self.candidates[candidate_id]
        if candidate.commit_attempted:
            return bool(candidate.commit_result)
        if candidate.state != "COMMIT_READY":
            return False
        # Runtime candidate IDs are not semantic. Replay uses the stable
        # opportunity/proposal identity as the random boundary.
        candidate.commit_attempted = True
        success = stable_uniform(f"commit:{candidate.proposal.proposal_id}") < GRADE_PROBABILITY[grade]
        candidate.commit_result = success
        if success:
            candidate.state = "COMMITTED"
        else:
            candidate.state = "COMMIT_FAILED"
        return success

    @staticmethod
    def arbitrate_contacts(intents: Sequence[ContactIntent], target_id: str) -> Optional[ContactIntent]:
        valid = [i for i in intents if i.target_id == target_id]
        if not valid:
            return None
        # Earliest valid geometric event wins. Exact abstract ties use a
        # stable random tie-break independent of list/serialization order.
        valid.sort(key=lambda i: (i.created_at, i.geometric_order))
        best = valid[0]
        tied = [i for i in valid if (i.created_at, i.geometric_order) == (best.created_at, best.geometric_order)]
        if len(tied) == 1:
            return best
        if any(i.semantic_intent_id is None for i in tied):
            raise ValueError("abstract contact ties require stable semantic_intent_id")
        index = int(stable_uniform("contact:" + target_id) * len(tied))
        return sorted(tied, key=lambda i: i.semantic_intent_id or i.candidate_id)[index]

    def settle(
        self,
        candidate_id: str,
        kind: SettlementKind,
        *,
        relocate_source_id: Optional[str] = None,
        settlement_transaction_id: Optional[str] = None,
    ) -> None:
        with self._lock:
            self._settle(candidate_id, kind, relocate_source_id=relocate_source_id,
                         settlement_transaction_id=settlement_transaction_id)

    def _settle(
        self,
        candidate_id: str,
        kind: SettlementKind,
        *,
        relocate_source_id: Optional[str] = None,
        settlement_transaction_id: Optional[str] = None,
    ) -> None:
        candidate = self.candidates[candidate_id]
        transaction_id = settlement_transaction_id or f"settle:{candidate.reservation_id}"
        if candidate.settled:
            return
        if transaction_id in self._settlement_transactions:
            if self._settlement_owner.get(transaction_id) != candidate_id:
                raise ValueError("settlement transaction already belongs to another candidate")
            return
        source = self.sources[candidate.proposal.source_id]
        if source.encounter_hold + 1e-12 < candidate.q:
            raise AssertionError("candidate settlement without EncounterHold")
        if kind == SettlementKind.RELOCATE and (not relocate_source_id or relocate_source_id not in self.sources):
            raise ValueError("relocate_source_id required")
        if kind == SettlementKind.RELOCATE and self.sources[relocate_source_id].q != candidate.q:
            raise ValueError("relocation target q must match Candidate q")
        if kind not in {
            SettlementKind.RETURN,
            SettlementKind.RETURN_WARY,
            SettlementKind.RELOCATE,
            SettlementKind.RECOVERY_HOLD,
            SettlementKind.REMOVE_STOCK,
        }:
            raise ValueError(kind)
        self._journal_append(
            "settlement:" + transaction_id,
            "CANDIDATE_SETTLED",
            {"candidate_id": candidate_id, "reservation_id": candidate.reservation_id,
             "kind": kind.value, "relocate_source_id": relocate_source_id, "q": candidate.q},
        )
        source.encounter_hold -= candidate.q
        if kind in (SettlementKind.RETURN, SettlementKind.RETURN_WARY):
            source.actual_supply += candidate.q
        elif kind == SettlementKind.RELOCATE:
            self.sources[relocate_source_id].actual_supply += candidate.q
        elif kind == SettlementKind.RECOVERY_HOLD:
            source.recovery_hold += candidate.q
        elif kind == SettlementKind.REMOVE_STOCK:
            source.removed_stock += candidate.q
        candidate.settled = True
        candidate.settlement_transaction_id = transaction_id
        self._settlement_transactions.add(transaction_id)
        self._settlement_owner[transaction_id] = candidate_id

    def expire_pending(self, proposal_id: str) -> bool:
        """Expire a proposal without a ledger write; no replacement roll."""
        return self.pending.pop(proposal_id, None) is not None

    def ledger_total(self) -> float:
        return sum(
            s.actual_supply + s.encounter_hold + s.recovery_hold
            for s in self.sources.values()
        )

    def accounting_total(self) -> float:
        """Active Stock plus removed-stock tombstones for audit conservation."""
        return self.ledger_total() + sum(s.removed_stock for s in self.sources.values())
