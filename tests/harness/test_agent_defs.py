"""Agent mesh definitions must stay in sync with harness/ ROLE_REGISTRY."""
from pathlib import Path

import pytest

from harness import ROLE_REGISTRY

AGENTS_DIR = Path(__file__).resolve().parents[2] / ".claude" / "agents"

# Roles shipped in the first active batch (topology C, hybrid mesh).
ACTIVE_ROLES = {
    "fcf-fish-researcher",
    "fcf-evidence-reviewer",
    "fcf-semantic-triage",
    "fcf-representation-worker",
    "independent-narrow-reviewer",
}

# Reviewers verify, they never mutate worker output, run commands, or edit remote pages.
READONLY_ROLES = {"fcf-evidence-reviewer", "independent-narrow-reviewer", "fcf-semantic-triage"}
WRITE_TOOLS = {"Write", "Edit", "NotebookEdit", "Bash"}
NOTION_READ_TOOLS = {"mcp__notion__notion-fetch", "mcp__notion__notion-search"}


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---"), f"{path.name} must start with frontmatter"
    header = text.split("---", 2)[1]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key.strip()] = value.strip()
    return fields


def agent_files() -> dict[str, Path]:
    files = {p.stem: p for p in AGENTS_DIR.glob("*.md")}
    assert files, f"no agent definitions found under {AGENTS_DIR}"
    return files


def test_active_roles_exist():
    files = agent_files()
    missing = ACTIVE_ROLES - set(files)
    assert not missing, f"missing agent definitions: {sorted(missing)}"


def test_agent_names_map_to_role_registry():
    for stem, path in agent_files().items():
        fields = parse_frontmatter(path)
        assert fields.get("name") == stem, f"{path.name}: frontmatter name mismatch"
        registry_key = stem.upper()
        assert registry_key in ROLE_REGISTRY, (
            f"{path.name}: role '{registry_key}' is not in harness ROLE_REGISTRY"
        )
        assert fields.get("description"), f"{path.name}: description required"


def test_reviewers_are_readonly():
    for stem, path in agent_files().items():
        fields = parse_frontmatter(path)
        tools = {t.strip() for t in fields.get("tools", "").split(",") if t.strip()}
        if stem in READONLY_ROLES:
            leaked = tools & WRITE_TOOLS
            assert not leaked, f"{stem} is a reviewer; write/exec tools leaked: {sorted(leaked)}"
            notion_write = {t for t in tools if t.startswith("mcp__notion__")} - NOTION_READ_TOOLS
            assert not notion_write, f"{stem}: non-read Notion tools leaked: {sorted(notion_write)}"


def test_deployed_copies_match_canonical_source():
    """When the workspace-root deploy dir exists it must equal the repo source."""
    deployed = AGENTS_DIR.parents[2] / ".claude" / "agents"
    if not deployed.is_dir():
        pytest.skip("workspace-root agent deploy dir not present on this machine")
    for stem in ACTIVE_ROLES:
        deployed_file = deployed / f"{stem}.md"
        assert deployed_file.exists(), f"deployed copy missing: {stem}.md"
        assert deployed_file.read_text(encoding="utf-8") == (AGENTS_DIR / f"{stem}.md").read_text(encoding="utf-8"), (
            f"{stem}.md: deployed copy drifted from canonical source"
        )


def test_charters_declare_envelope_and_exclusions():
    for stem, path in agent_files().items():
        text = path.read_text(encoding="utf-8")
        assert "BATCH_ID" in text or "envelope" in text, f"{stem}: charter must reference handoff envelope/BATCH_ID"
        assert "## 边界" in text or "不负责" in text, f"{stem}: charter must declare exclusions"


def test_charters_use_role_memory_warm_start():
    """Warm start: fresh context + own curated memory file, never other roles'."""
    for stem, path in agent_files().items():
        text = path.read_text(encoding="utf-8")
        assert "role_memory" in text, f"{stem}: charter must wire role memory (continuity)"
        assert "不读其它角色" in text, f"{stem}: charter must forbid reading other roles' memory"
