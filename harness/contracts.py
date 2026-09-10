"""Scoped review and role-separated handoff contracts."""
from dataclasses import dataclass, asdict
from typing import Any, Dict

_REQUIRED = ("level", "scope", "baseline", "proves", "does_not_prove", "open_findings", "verdict")
_LEVELS = {"PATCH_APPROVE", "PATCH_REVISE", "ARTIFACT_APPROVE", "ARTIFACT_REVISE", "MILESTONE_APPROVE", "MILESTONE_REVISE"}


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


def validate_verdict(verdict: Dict[str, Any]) -> Dict[str, Any]:
    missing = [field for field in _REQUIRED if field not in verdict]
    if missing:
        raise ReviewContractError(f"missing review fields: {', '.join(missing)}")
    if verdict["level"] not in _LEVELS:
        raise ReviewContractError(f"invalid review level: {verdict['level']}")
    if not verdict["scope"]:
        raise ReviewContractError("review scope must be explicit")
    if not verdict["does_not_prove"]:
        raise ReviewContractError("does_not_prove must preserve review boundaries")
    return dict(verdict)
