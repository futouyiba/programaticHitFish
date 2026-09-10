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
    required = ("level", "scope", "baseline", "proves", "does_not_prove", "open_findings", "verdict")
    missing = [field for field in required if field not in verdict]
    if missing:
        raise ReviewContractError(f"missing review fields: {', '.join(missing)}")
    level = verdict["level"]
    if level not in _LEVELS:
        raise ReviewContractError(f"invalid review level: {level!r} (expected one of {', '.join(_LEVELS)})")
    expected = [f"{level}_{outcome}" for outcome in _OUTCOMES]
    if verdict["verdict"] not in expected:
        raise ReviewContractError(f"verdict {verdict['verdict']!r} must match level {level!r}: expected one of {', '.join(expected)}")
    for field in ("scope", "baseline", "proves", "does_not_prove"):
        if not verdict[field]:
            raise ReviewContractError(f"{field} must be explicit and non-empty")
    return dict(verdict)


def validate_envelope(envelope: HandoffEnvelope) -> HandoffEnvelope:
    """Shape-preserving semantic checks; unknown roles/states are rejected."""
    for field in ("FROM_ROLE", "TO_ROLE"):
        role = getattr(envelope, field)
        if role not in ROLE_REGISTRY:
            raise EnvelopeContractError(f"{field} {role!r} is not in ROLE_REGISTRY")
    # Handoff convention writes CURRENT_STATE as "<code> <STATE_NAME>" (e.g.
    # "FR1 RESEARCH_PACKAGE_READY"); code and value must name the same state.
    tokens = envelope.CURRENT_STATE.split()
    by_name = {state.name: state.value for state in HarnessState}
    by_value = {state.value for state in HarnessState}
    if len(tokens) == 1:
        valid = tokens[0] in by_value
    else:
        valid = len(tokens) == 2 and tokens[0] in by_name and by_name.get(tokens[0]) == tokens[1]
    if not valid:
        raise EnvelopeContractError(f"CURRENT_STATE {envelope.CURRENT_STATE!r} is not a declared harness state")
    if not envelope.BATCH_ID:
        raise EnvelopeContractError("BATCH_ID must be explicit")
    blocking = envelope.BLOCKING_FINDINGS
    if blocking != "NONE":
        tokens = blocking.split()
        if not tokens or not all(token.startswith(("http://", "https://")) for token in tokens):
            raise EnvelopeContractError("BLOCKING_FINDINGS must be NONE or whitespace-separated URLs")
    return envelope
