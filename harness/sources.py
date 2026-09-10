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


def _normalize_url(url: str) -> str:
    """Canonical form for identity comparison: strip query/fragment, trim slash."""
    return url.split("?", 1)[0].split("#", 1)[0].rstrip("/")


class OfflineSnapshotProvider:
    """Resolve pages against snapshot files' own identity headers.

    A snapshot file IS a snapshot of exactly the page named in its fetch
    header; a page merely mentioned inside another snapshot's body is NOT
    covered (that mismatch is the silent-downgrade this provider must never do).
    """

    mode = "SNAPSHOT_ONLY"

    def __init__(self, snapshot_root: str):
        self.root = Path(snapshot_root)

    @staticmethod
    def _identity_header(text: str) -> str:
        return "\n".join(text.splitlines()[:5])

    @staticmethod
    def _identity_urls(header: str) -> set:
        """Exact URLs this snapshot is *of*, extracted symmetrically and normalized."""
        urls = set()
        for match in re.finditer(r"Page with URL (\S+) as of", header):
            urls.add(_normalize_url(match.group(1)))
        for match in re.finditer(r'<page url="([^"]+)"', header):
            urls.add(_normalize_url(match.group(1)))
        return urls

    def find_url(self, url: str) -> SourceRef:
        target = _normalize_url(url)
        for path in sorted(self.root.glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            header = self._identity_header(text)
            if target not in self._identity_urls(header):
                continue
            fetched = re.search(r"as of (\S+):", header)
            return SourceRef(url, str(path), self.mode, "SNAPSHOT_UNVERIFIED", fetched.group(1) if fetched else None)
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
