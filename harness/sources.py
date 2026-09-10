"""Offline Notion snapshot access; live MCP is intentionally an adapter boundary."""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional
import re

_ERROR_CODES = (
    "MCP_NOT_CONFIGURED",
    "PAGE_ACCESS_DENIED",
    "PAGE_NOT_FOUND",
    "TRANSPORT_FAILURE",
)


class NotionTransportError(RuntimeError):
    """Classified Notion source failure; never silently downgraded to live."""

    def __init__(self, code: str, detail: str = ""):
        if code not in _ERROR_CODES:
            raise ValueError(f"unknown notion transport code: {code}")
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {detail}" if detail else code)


class MCPNotConfigured(NotionTransportError):
    def __init__(self, detail: str = "register and authorize a Notion MCP server first"):
        super().__init__("MCP_NOT_CONFIGURED", detail)


@dataclass(frozen=True)
class SourceRef:
    url: str
    local_path: Optional[str]
    mode: str
    status: str
    fetched_at: Optional[str] = None


def classify_transport_error(message: str) -> NotionTransportError:
    """Map a raw MCP failure message onto a reviewable, non-silent code."""
    lowered = (message or "").lower()
    if "not configured" in lowered or "no such tool" in lowered or "not registered" in lowered:
        return NotionTransportError("MCP_NOT_CONFIGURED", message)
    if "forbidden" in lowered or "permission" in lowered or "access denied" in lowered or "unauthorized" in lowered:
        return NotionTransportError("PAGE_ACCESS_DENIED", message)
    if "not found" in lowered or "could not find" in lowered or "does not exist" in lowered:
        return NotionTransportError("PAGE_NOT_FOUND", message)
    return NotionTransportError("TRANSPORT_FAILURE", message)


class OfflineSnapshotProvider:
    mode = "SNAPSHOT_ONLY"

    def __init__(self, snapshot_root: str):
        self.root = Path(snapshot_root)

    def find_url(self, url: str) -> SourceRef:
        page_id = re.search(r"/p/([a-f0-9]+)", url)
        needle = page_id.group(1) if page_id else ""
        for path in sorted(self.root.glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            if url in text or (needle and needle in text):
                return SourceRef(url, str(path), self.mode, "SNAPSHOT_UNVERIFIED")
        raise FileNotFoundError(f"SNAPSHOT_MISSING: {url}")


class NotionMCPProvider:
    """Read-only live source. The transport callable is injected, never guessed."""

    mode = "MCP_LIVE"

    def __init__(self, fetcher: Optional[Callable[[str], dict]] = None):
        self.fetcher = fetcher

    def require_client(self) -> Callable[[str], dict]:
        if self.fetcher is None:
            raise MCPNotConfigured()
        return self.fetcher

    def read_page(self, url: str) -> SourceRef:
        fetcher = self.require_client()
        try:
            page = fetcher(url)
        except NotionTransportError:
            raise
        except Exception as exc:  # transport boundary: classify, never fake live
            raise classify_transport_error(str(exc)) from exc
        if not page or not page.get("text"):
            raise NotionTransportError("TRANSPORT_FAILURE", f"empty page body for {url}")
        return SourceRef(url, page.get("local_path"), self.mode, page.get("status", "LIVE_UNVERIFIED"), page.get("fetched_at"))
