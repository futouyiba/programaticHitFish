"""Scoped review and role-separated handoff contracts."""
from dataclasses import dataclass, asdict
from typing import Any, Dict, List

from .core import ROLE_REGISTRY, HarnessState

# docs/scoped_review_protocol.md §1–§2: level is the bare grade; the
# APPROVE/REVISE outcome belongs to the verdict field as "<LEVEL>_<OUTCOME>".
_LEVELS = ("PATCH", "ARTIFACT", "MILESTONE")
_OUTCOMES = ("APPROVE", "REVISE")


@dataclass(frozen=True)
class HandoffEnvelope:
    FROM_ROLE: str
    TO_ROLE: str
    BATCH_ID: str
    CURRENT_STATE: str
    ARTIFACT_URL: str
    ROLE_PROMPT_URL: str
    REQUESTED_ACTION: str
    EXPECTED_OUTPUT: str
    BLOCKING_FINDINGS: str = "NONE"
    NOTES: str = ""

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


class ReviewContractError(ValueError):
    pass


class EnvelopeContractError(ValueError):
    pass


def validate_verdict(verdict: Dict[str, Any]) -> Dict[str, Any]:
    missing = [field for field in ("level", "scope", "baseline", "proves", "does_not_prove", "open_findings", "verdict") if field not in verdict]
    if missing:
        raise ReviewContractError(f"missing review fields: {', '.join(missing)}")
    level = verdict["level"]
    if level not in _LEVELS:
        raise ReviewContractError(f"invalid review level: {level!r} (expected one of {', '.join(_LEVELS)})")
    expected = [f"{level}_{outcome}" for outcome in _OUTCOMES]
    if verdict["verdict"] not in expected:
        raise ReviewContractError(f"verdict {verdict['verdict']!r} must match level {level!r}: expected one of {', '.join(expected)}")
    if not verdict["scope"]:
        raise ReviewContractError("review scope must be explicit")
    if not verdict["does_not_prove"]:
        raise ReviewContractError("does_not_prove must preserve review boundaries")
    return dict(verdict)


def validate_envelope(envelope: HandoffEnvelope) -> HandoffEnvelope:
    """Shape-preserving semantic checks; unknown roles/states are rejected."""
    for field in ("FROM_ROLE", "TO_ROLE"):
        role = getattr(envelope, field)
        if role not in ROLE_REGISTRY:
            raise EnvelopeContractError(f"{field} {role!r} is not in ROLE_REGISTRY")
    # Handoff convention writes CURRENT_STATE as "<code> <STATE_NAME>" (e.g.
    # "FR1 RESEARCH_PACKAGE_READY"); match the declared state token.
    state_tokens = {state.value for state in HarnessState}
    if not (set(envelope.CURRENT_STATE.split()) & state_tokens):
        raise EnvelopeContractError(f"CURRENT_STATE {envelope.CURRENT_STATE!r} is not a declared harness state")
    if not envelope.BATCH_ID:
        raise EnvelopeContractError("BATCH_ID must be explicit")
    blocking = envelope.BLOCKING_FINDINGS
    if blocking != "NONE" and "http" not in blocking:
        raise EnvelopeContractError("BLOCKING_FINDINGS must be NONE or reference URLs")
    return envelope
