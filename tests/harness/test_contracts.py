import pytest

from harness import (
    HarnessLane,
    HarnessState,
    HandoffEnvelope,
    EnvelopeContractError,
    MCPNotConfigured,
    NotionMCPProvider,
    NotionTransportError,
    OfflineSnapshotProvider,
    ROLE_REGISTRY,
    can_transition,
    classify_transport_error,
    validate_envelope,
    validate_verdict,
)


def test_role_and_lane_transitions():
    assert "FCF-EVIDENCE-REVIEWER" in ROLE_REGISTRY
    assert can_transition(HarnessLane.FISH_AUDIT, HarnessState.A0, HarnessState.A1)
    assert not can_transition(HarnessLane.FISH_AUDIT, HarnessState.A0, HarnessState.B0)


def _valid_verdict() -> dict:
    return {
        "level": "ARTIFACT",
        "scope": "artifact-x",
        "baseline": ["sha:abc"],
        "proves": ["x"],
        "does_not_prove": ["freeze"],
        "open_findings": [],
        "verdict": "ARTIFACT_APPROVE",
    }


def test_scoped_verdict_requires_boundary():
    assert validate_verdict(_valid_verdict())["scope"] == "artifact-x"


@pytest.mark.parametrize(
    "mutate",
    [
        # level must be the bare grade (protocol §1), not the graded outcome
        lambda v: v.update(level="ARTIFACT_APPROVE", verdict="ARTIFACT_APPROVE"),
        # verdict must carry the outcome and agree with level (protocol §2)
        lambda v: v.update(verdict="PATCH_APPROVE"),
        lambda v: v.update(verdict="pass"),
        lambda v: v.update(verdict="ARTIFACT_MAYBE"),
        lambda v: v.pop("does_not_prove"),
        lambda v: v.update(scope=""),
        lambda v: v.update(does_not_prove=[]),
    ],
)
def test_scoped_verdict_rejects_invalid(mutate):
    verdict = _valid_verdict()
    mutate(verdict)
    with pytest.raises(Exception):
        validate_verdict(verdict)


def test_handoff_round_trip_and_semantic_validation():
    envelope = HandoffEnvelope(
        FROM_ROLE="FCF-FISH-RESEARCHER",
        TO_ROLE="FCF-EVIDENCE-REVIEWER",
        BATCH_ID="B-1",
        CURRENT_STATE="FR1 RESEARCH_PACKAGE_READY",
        ARTIFACT_URL="artifact",
        ROLE_PROMPT_URL=".claude/agents/fcf-evidence-reviewer.md@0ccd168",
        REQUESTED_ACTION="review",
        EXPECTED_OUTPUT="verdict",
    )
    assert validate_envelope(envelope).to_dict()["FROM_ROLE"] == "FCF-FISH-RESEARCHER"


@pytest.mark.parametrize(
    "mutate",
    [
        lambda e: {**e.to_dict(), "TO_ROLE": "NOT-A-ROLE"},
        lambda e: {**e.to_dict(), "FROM_ROLE": "who"},
        lambda e: {**e.to_dict(), "CURRENT_STATE": "SOMETHING_ELSE"},
        lambda e: {**e.to_dict(), "BATCH_ID": ""},
        lambda e: {**e.to_dict(), "BLOCKING_FINDINGS": "maybe"},
    ],
)
def test_envelope_semantic_rejections(mutate):
    envelope = HandoffEnvelope(
        FROM_ROLE="FCF-FISH-RESEARCHER",
        TO_ROLE="FCF-EVIDENCE-REVIEWER",
        BATCH_ID="B-1",
        CURRENT_STATE="FR1 RESEARCH_PACKAGE_READY",
        ARTIFACT_URL="artifact",
        ROLE_PROMPT_URL=".claude/agents/fcf-evidence-reviewer.md@0ccd168",
        REQUESTED_ACTION="review",
        EXPECTED_OUTPUT="verdict",
    )
    with pytest.raises(EnvelopeContractError):
        validate_envelope(HandoffEnvelope(**mutate(envelope)))


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


def _write_snapshot(root, name: str, page_url: str, body: str = "") -> None:
    root.joinpath(name).write_text(
        f'Here is the result of "fetch" for the Page with URL {page_url} as of 2026-09-09T10:00:00Z:\n'
        f'<page url="{page_url}">\ncontent\n{body}\n</page>\n',
        encoding="utf-8",
    )


def test_snapshot_matches_own_identity_header(tmp_path):
    url = "https://app.notion.com/p/11111111111111111111111111111111"
    _write_snapshot(tmp_path, "notion-01.md", url)
    ref = OfflineSnapshotProvider(str(tmp_path)).find_url(url)
    assert ref.local_path.endswith("notion-01.md")
    assert ref.status == "SNAPSHOT_UNVERIFIED"
    assert ref.fetched_at == "2026-09-09T10:00:00Z"


def test_snapshot_url_query_suffix_still_matches(tmp_path):
    url = "https://app.notion.com/p/22222222222222222222222222222222"
    _write_snapshot(tmp_path, "notion-02.md", url)
    ref = OfflineSnapshotProvider(str(tmp_path)).find_url(url + "?pvs=204")
    assert ref.local_path.endswith("notion-02.md")


def test_page_mentioned_in_other_snapshot_body_is_missing(tmp_path):
    """Drift-report reality: Router/Current/RC4 appear only as links inside
    other snapshots — that must surface as SNAPSHOT_MISSING, never a false hit."""
    target = "https://app.notion.com/p/33333333333333333333333333333333"
    other = "https://app.notion.com/p/44444444444444444444444444444444"
    _write_snapshot(tmp_path, "notion-03.md", other, body=f'link to <a href="{target}">router</a> and id 33333333333333333333333333333333 inline')
    with pytest.raises(FileNotFoundError) as exc:
        OfflineSnapshotProvider(str(tmp_path)).find_url(target)
    assert "SNAPSHOT_MISSING" in str(exc.value)
