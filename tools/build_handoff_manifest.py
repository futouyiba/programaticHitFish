#!/usr/bin/env python3
"""Build a portable, machine-readable snapshot for a harness handoff."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "handoff_manifest.json"

KEY_NOTION_SOURCES = [
    {
        "title": "FCF Start Here / Agent Router",
        "url": "https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47",
        "role": "bootstrap_router",
    },
    {
        "title": "FCF Design Branch Index",
        "url": "https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd",
        "role": "branch_topology_and_ownership",
    },
    {
        "title": "FCF Project State Current",
        "url": "https://app.notion.com/p/3cca4137d2368114a982f3b09e965e49",
        "role": "current_authority_and_active_targets",
    },
    {
        "title": "FCF V1 Core Candidate RC4 / Closure Revision",
        "url": "https://app.notion.com/p/3cca4137d236819aa3baddca8a2c251c",
        "role": "v1_review_target",
    },
    {
        "title": "RC3 Review Adjudication & RC4 Closure Patch",
        "url": "https://app.notion.com/p/3cca4137d23681fba563eccaec1cbf8c",
        "role": "v1_closure_patch",
    },
    {
        "title": "Simplified Production V0 / Working Main",
        "url": "https://app.notion.com/p/3cda4137d23681508740ceff789abd41",
        "role": "v0_current_working_main",
    },
    {
        "title": "Production Design Document Authoring Guide",
        "url": "https://app.notion.com/p/3cfa4137d23681d68f89cc0eed80f99b",
        "role": "production_doc_authoring_governance",
    },
    {
        "title": "GPT Work Startup Prompt v2 / V1",
        "url": "https://app.notion.com/p/3cca4137d236815689b9d0cc97d4c287",
        "role": "v1_design_integration_startup",
    },
    {
        "title": "GPT Work Migration Handoff / V1",
        "url": "https://app.notion.com/p/3cca4137d236813388aadeb304bb6515",
        "role": "v1_migration_and_role_firewall",
    },
    {
        "title": "GPT Work Method Handoff / Representation",
        "url": "https://app.notion.com/p/3d6a4137d23681829824f57f9105e74f",
        "role": "representation_execution_method",
    },
    {
        "title": "FCF Research Orchestration Hub R2",
        "url": "https://app.notion.com/p/3d6a4137d236814e9f35e6ae2a761927",
        "role": "state_and_artifact_manifest",
    },
    {
        "title": "Execution Runbook R2",
        "url": "https://app.notion.com/p/3d6a4137d23681ca8265f98253f258a5",
        "role": "canonical_process_contract",
    },
    {
        "title": "Persistent Role Registry",
        "url": "https://app.notion.com/p/3d6a4137d2368137a8f3c7898e8e7ae5",
        "role": "stable_agent_roles_and_handles",
    },
    {
        "title": "Representation Design Gate R1",
        "url": "https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a",
        "role": "representation_gate",
    },
    {
        "title": "15 Case Authoring Visualization R0",
        "url": "https://app.notion.com/p/3d6a4137d236814ea872ed6305942594",
        "role": "representation_case_baseline",
    },
    {
        "title": "4 Logic Surface Authoring Stress Test R1",
        "url": "https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3",
        "role": "representation_stress_and_working_handoff",
    },
]

ROLES = [
    {
        "canonical_name": "FCF-FISH-RESEARCHER",
        "responsibility": "Reality/Strategy Research, Story Sweep, Research Package",
        "boundary": "不做 Representation PT1–PT4；不把未经审核猜测写成事实",
        "registered_handle": "01a0843e-7214-77b0-b3c2-5e7f909ed87e",
    },
    {
        "canonical_name": "FCF-EVIDENCE-REVIEWER",
        "responsibility": "独立核验事实、Evidence、Scope、Owner、Missed Story",
        "boundary": "不读 Worker scratchpad；不直接修改 Worker 产物",
        "registered_handle": "01a085a9-51ec-7161-8d99-f5b374e9b412",
    },
    {
        "canonical_name": "FCF-SEMANTIC-TRIAGE",
        "responsibility": "Existing Pattern、Compression、Coverage Delta、Semantic Escalation",
        "boundary": "不修改 Design Authority；不按自然语言名字聚类",
        "registered_handle": "01a086f5-95af-7282-ae79-1ddecf399be5",
    },
    {
        "canonical_name": "FCF-REPRESENTATION-WORKER",
        "responsibility": "已审核 Mechanism Story 到 Config/Table/Step Table/Narrow DSL",
        "boundary": "不重建 Reality Baseline；不隐藏 Authoring freedom",
        "registered_handle": "01a0848f-de82-7d93-9f3c-d4d973eec831",
    },
]


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip()


def git_status() -> dict[str, object]:
    porcelain = run("git", "status", "--porcelain=v1")
    return {
        "branch": run("git", "branch", "--show-current"),
        "head": run("git", "rev-parse", "HEAD"),
        "head_short": run("git", "rev-parse", "--short", "HEAD"),
        "head_subject": run("git", "log", "-1", "--format=%s"),
        "remotes": run("git", "remote", "-v").splitlines(),
        "porcelain": porcelain.splitlines() if porcelain else [],
        "modified_tracked": run("git", "ls-files", "-m").splitlines(),
        "deleted_tracked": run("git", "diff", "--name-only", "--diff-filter=D").splitlines(),
        "untracked": run("git", "ls-files", "--others", "--exclude-standard").splitlines(),
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        parts = set(relative.parts)
        if ".git" in parts or "__pycache__" in parts or ".pytest_cache" in parts:
            continue
        if path.name == ".DS_Store":
            continue
        if path == OUTPUT:
            continue
        category = "canonical"
        if relative.parts[0] in {"tmp"}:
            category = "scratch"
        elif relative.parts[0] in {"outputs", "deliverables"}:
            category = "delivery_bundle"
        elif relative.parts[0] in {"bass_dynamic_preference", "experiments"}:
            category = "v0_experiment"
        elif relative.parts[0] in {"docs"} and (
            "archive" in relative.parts or "rf4_" in path.name
        ):
            category = "historical_or_external_evidence"
        records.append(
            {
                "path": relative.as_posix(),
                "category": category,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return records


def notion_discovery() -> list[dict[str, object]]:
    url_re = re.compile(r"https://app\.notion\.com/p/[A-Za-z0-9_-]+")
    title_re = re.compile(
        r'<(?:page|mention-page) url="(https://app\.notion\.com/p/[A-Za-z0-9_-]+)"'
        r'(?:/)?>([^<]*)</(?:page|mention-page)>'
    )
    markdown_link_re = re.compile(
        r"\[([^\]]+)\]\((https://app\.notion\.com/p/[A-Za-z0-9_-]+)"
    )
    title_by_url: dict[str, str] = {}
    locations_by_url: dict[str, set[str]] = {}
    urls: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".html", ".js", ".txt"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        found_urls = set(url_re.findall(text))
        urls.update(found_urls)
        relative = path.relative_to(ROOT).as_posix()
        for url in found_urls:
            locations_by_url.setdefault(url, set()).add(relative)
        for url, title in title_re.findall(text):
            title_by_url.setdefault(url, title.strip())
        for title, url in markdown_link_re.findall(text):
            title_by_url.setdefault(url, title.strip())
    return [
        {
            "url": url,
            "title": title_by_url.get(url, ""),
            "discovered_in": sorted(locations_by_url.get(url, [])),
        }
        for url in sorted(urls)
    ]


def validation() -> dict[str, object]:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    output = (result.stdout + result.stderr).strip()
    return {
        "command": "python3 -m pytest -q",
        "returncode": result.returncode,
        "passed": result.returncode == 0,
        "output_tail": output[-1000:],
    }


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    files = inventory()
    by_category = Counter(item["category"] for item in files)
    manifest = {
        "manifest_version": 1,
        "generated_at_utc": generated_at,
        "snapshot_date": "2026-09-10",
        "repository": {
            "absolute_path": str(ROOT),
            "git": git_status(),
            "remote_push_available": bool(run("git", "remote")),
        },
        "state_summary": {
            "v1": {
                "authority": "FCF V1 default authority; active review target RC4",
                "status": "Freeze blocked pending production runtime/storage evidence and Independent Narrow Close Review",
            },
            "simplified_v0": {
                "authority": "branch-local Working Main",
                "status": "WORKING / NOT PROMOTED; next gate is Human Usability Validation",
            },
            "representation": {
                "status": "A4 PROCEED_TO_REPRESENTATION; B4 DESIGN_REVISE",
                "scope": "Pilot-A; 15 cases x 4 surfaces = 60 cells",
            },
        },
        "local_inventory": {
            "file_count_excluding_transient_and_manifest": len(files),
            "counts_by_category": dict(sorted(by_category.items())),
            "files": files,
        },
        "notion_sources": KEY_NOTION_SOURCES,
        "notion_urls_discovered": notion_discovery(),
        "agent_roles": ROLES,
        "handoff_protocol": {
            "bootstrap": [
                "Read HARNESS_HANDOFF.md and AGENTS.md",
                "Read FCF Router",
                "Read Project State Current",
                "Select exactly one branch-local route",
                "Read only the required Current/Working and review dependencies",
            ],
            "review_verdict_fields": [
                "level",
                "scope",
                "baseline",
                "proves",
                "does_not_prove",
                "open_findings",
                "verdict",
            ],
            "handoff_envelope_fields": [
                "FROM_ROLE",
                "TO_ROLE",
                "BATCH_ID",
                "CURRENT_STATE",
                "ARTIFACT_URL",
                "ROLE_PROMPT_URL",
                "REQUESTED_ACTION",
                "EXPECTED_OUTPUT",
                "BLOCKING_FINDINGS",
                "NOTES",
            ],
            "do_not_infer": [
                "Working/Candidate is not Current or Promotion",
                "Notion fetch success is not semantic review approval",
                "Reference tests are not production runtime evidence",
                "Cross-branch citation does not transfer ownership",
                "A missing Notion target is transport failure, not a mechanism counterexample",
            ],
        },
        "validation": validation(),
    }
    OUTPUT.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
