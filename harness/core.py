"""FCF role-separated harness contracts."""
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class HarnessLane(str, Enum):
    FISH_AUDIT = "Fish Audit"
    REPRESENTATION = "Representation"
    RESEARCH = "Ongoing research"


class HarnessState(str, Enum):
    A0 = "AUDIT_RUNNING"
    A1 = "AUDIT_PACKAGE_READY"
    A2 = "AUDIT_REVIEW_RUNNING"
    A3 = "AUDIT_EVIDENCE_PASS"
    A4 = "FISH_ARCHITECTURE_DECISION_GATE"
    B0 = "REPRESENTATION_RUNNING"
    B1 = "REPRESENTATION_PACKAGE_READY"
    B2 = "REPRESENTATION_REVIEW_RUNNING"
    B3 = "REPRESENTATION_EVIDENCE_PASS"
    B4 = "REPRESENTATION_DECISION_GATE"
    FR0 = "RESEARCH_RUNNING"
    FR1 = "RESEARCH_PACKAGE_READY"
    FR2 = "EVIDENCE_REVIEW_RUNNING"
    FR3 = "SEMANTIC_TRIAGE"


@dataclass(frozen=True)
class RoleSpec:
    name: str
    owns: Tuple[str, ...]
    excludes: Tuple[str, ...]


ROLE_REGISTRY = {
    "FCF-FISH-RESEARCHER": RoleSpec("FCF-FISH-RESEARCHER", ("reality", "strategy research", "story sweep", "research package"), ("representation PT1-PT4",)),
    "FCF-EVIDENCE-REVIEWER": RoleSpec("FCF-EVIDENCE-REVIEWER", ("fact", "evidence", "scope", "owner", "missed story"), ("worker scratchpad", "editing worker artifacts")),
    "FCF-SEMANTIC-TRIAGE": RoleSpec("FCF-SEMANTIC-TRIAGE", ("existing pattern", "compression", "coverage delta", "semantic escalation"), ("design authority",)),
    "FCF-REPRESENTATION-WORKER": RoleSpec("FCF-REPRESENTATION-WORKER", ("config", "table", "step table", "narrow DSL expression"), ("rebuilding reality baseline", "hiding authoring freedom")),
    "DESIGN-INTEGRATION-OWNER": RoleSpec("DESIGN-INTEGRATION-OWNER", ("mechanism", "tradeoffs", "formula", "owner", "gate", "narrow fixes"), ("unbounded V1 expansion",)),
    "INDEPENDENT-NARROW-REVIEWER": RoleSpec("INDEPENDENT-NARROW-REVIEWER", ("false fit", "replay", "conservation", "owner", "hidden complexity"), ("replacing upstream design", "expanding verdict scope")),
    "CROSS-BATCH-COLD-REVIEWER": RoleSpec("CROSS-BATCH-COLD-REVIEWER", ("rubber-stamp", "ontology anchoring", "over-compression"), ("routine batch workflow",)),
    "CODING-AGENT-HARNESS": RoleSpec("CODING-AGENT-HARNESS", ("executable prototype", "property tests", "concurrency", "replay", "regression fixtures"), ("mechanism promotion",)),
}

_TRANSITIONS = {
    HarnessLane.FISH_AUDIT: ((HarnessState.A0, HarnessState.A1), (HarnessState.A1, HarnessState.A2), (HarnessState.A2, HarnessState.A3), (HarnessState.A3, HarnessState.A4)),
    HarnessLane.REPRESENTATION: ((HarnessState.B0, HarnessState.B1), (HarnessState.B1, HarnessState.B2), (HarnessState.B2, HarnessState.B3), (HarnessState.B3, HarnessState.B4)),
    HarnessLane.RESEARCH: ((HarnessState.FR0, HarnessState.FR1), (HarnessState.FR1, HarnessState.FR2), (HarnessState.FR2, HarnessState.FR3)),
}


def can_transition(lane: HarnessLane, current: HarnessState, target: HarnessState) -> bool:
    return (current, target) in _TRANSITIONS[lane]


def get_role(name: str) -> RoleSpec:
    try:
        return ROLE_REGISTRY[name]
    except KeyError as exc:
        raise ValueError(f"unknown harness role: {name}") from exc
