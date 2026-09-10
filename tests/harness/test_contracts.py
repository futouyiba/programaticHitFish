import pytest

from harness import (
    HarnessLane,
    HarnessState,
    HandoffEnvelope,
    MCPNotConfigured,
    NotionMCPProvider,
    NotionTransportError,
    ROLE_REGISTRY,
    can_transition,
    classify_transport_error,
    validate_verdict,
)


def test_role_and_lane_transitions():
    assert "FCF-EVIDENCE-REVIEWER" in ROLE_REGISTRY
    assert can_transition(HarnessLane.FISH_AUDIT, HarnessState.A0, HarnessState.A1)
    assert not can_transition(HarnessLane.FISH_AUDIT, HarnessState.A0, HarnessState.B0)


def test_scoped_verdict_requires_boundary():
    verdict = {"level": "ARTIFACT_APPROVE", "scope": "artifact-x", "baseline": "sha", "proves": ["x"], "does_not_prove": ["freeze"], "open_findings": [], "verdict": "pass"}
    assert validate_verdict(verdict)["scope"] == "artifact-x"


def test_handoff_round_trip():
    envelope = HandoffEnvelope("A", "B", "batch-1", "A1", "artifact", "prompt", "review", "verdict")
    assert envelope.to_dict()["FROM_ROLE"] == "A"


def test_missing_notion_mcp_is_explicit():
    with pytest.raises(MCPNotConfigured) as exc:
        NotionMCPProvider().require_client()
    assert "MCP_NOT_CONFIGURED" in str(exc.value)


@pytest.mark.parametrize(
    "message,code",
    [
        ("tool not registered", "MCP_NOT_CONFIGURED"),
        ("403 Forbidden for page", "PAGE_ACCESS_DENIED"),
        ("page not found", "PAGE_NOT_FOUND"),
        ("connection reset by peer", "TRANSPORT_FAILURE"),
    ],
)
def test_transport_errors_are_classified(message, code):
    assert classify_transport_error(message).code == code


def test_live_read_requires_body_and_never_downgrades():
    provider = NotionMCPProvider(fetcher=lambda url: {"text": "", "status": "unverified"})
    with pytest.raises(NotionTransportError) as exc:
        provider.read_page("https://app.notion.com/p/abc")
    assert exc.value.code == "TRANSPORT_FAILURE"


def test_live_read_returns_live_source_ref():
    provider = NotionMCPProvider(fetcher=lambda url: {"text": "body", "status": "unverified", "fetched_at": "2026-09-10T00:00:00Z"})
    ref = provider.read_page("https://app.notion.com/p/abc")
    assert ref.mode == "MCP_LIVE" and ref.status == "unverified"
