"""Batch structural validator for the LogicTemplate Census.

Validates the file/record contract (Orchestrator Prompt R2 §8-9; fixtures
F08/F09/F12/F16/F17). This validator checks FORM ONLY — program equivalence
reasoning stays with the census worker + independent review (Method R0 §12).

Usage:
  python fish_logic_census/scripts/validate_batch.py fish_logic_census/batches/<BATCH_ID>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Record-level checks (each returns a list of error strings)
# ---------------------------------------------------------------------------

def check_consequence_sketches(stories, sketches):
    """F08: consequence classification requires a prior sketch (or explicit
    NO_SURFACE reason)."""
    errors = []
    sketched = {s.get("story_id") for s in sketches}
    for story in stories:
        if story.get("consequence") and story.get("story_id") not in sketched:
            reason = story.get("no_surface_reason")
            if story.get("consequence") != "NO_SURFACE_EFFECT" or not reason:
                errors.append(
                    f"{story.get('story_id')}: PROGRAM_SKETCH_REQUIRED_BEFORE_CONSEQUENCE_CLASSIFICATION")
    return errors


def check_absence_claims(coverage, claims):
    """F09: strong absence claims require no EVIDENCE_INSUFFICIENT gaps."""
    errors = []
    gaps = {c["story_id"] for c in coverage
            for status in c.get("r", {}).values()
            if status == "EVIDENCE_INSUFFICIENT"}
    strong = {"NO_NEW_PROGRAM_CURRENT_EVIDENCE"}
    for claim in claims:
        if claim.get("claim") in strong and claim.get("story_id") in gaps:
            errors.append(
                f"{claim['story_id']}: ABSENCE_CLAIM_EXCEEDS_RESEARCH_COVERAGE")
        if claim.get("claim") == "NO_NEW_PROGRAM_PROVEN":
            errors.append(f"{claim['story_id']}: FORBIDDEN_CLAIM_NO_NEW_PROGRAM_PROVEN")
    return errors


def check_depth_gate(coverage):
    """F12: R1-R10 complete is not depth; a targeted second pass is required."""
    errors = []
    for entry in coverage:
        checked = [v for v in entry.get("r", {}).values()
                   if v in ("FOUND", "CHECKED_NO_DISTINCT")]
        if len(checked) == 10 and not entry.get("second_pass"):
            errors.append(f"{entry['story_id']}: TARGETED_SECOND_PASS_REQUIRED")
        for key, value in entry.get("r", {}).items():
            if value == "CHECKED_NO_DISTINCT" and not entry.get("research_log", {}).get(key):
                errors.append(f"{entry['story_id']}: CHECKED_NO_DISTINCT without research_log ({key})")
    return errors


def check_blind_freeze(programs):
    """F17: post-registry mutations need a revision record; fit-motivated
    edits carry BIAS_RISK (mechanical keyword screen; semantic judge is the
    reviewer's)."""
    errors = []
    bias_keywords = ("fit", "template", "match")
    for program in programs:
        if not program.get("registry_seen_at_creation", False):
            for mutation in program.get("post_registry_mutations", []):
                if not mutation.get("revision_recorded"):
                    errors.append(
                        f"{program['program_id']}: BLIND_SKETCH_POST_REGISTRY_MUTATION "
                        f"(no revision: {mutation.get('reason', '?')})")
                elif any(k in (mutation.get("reason") or "").lower() for k in bias_keywords) \
                        and not mutation.get("bias_risk_flagged"):
                    errors.append(
                        f"{program['program_id']}: BIAS_RISK_UNFLAGGED "
                        f"(reason mentions registry fit)")
    return errors


def check_stage_blindness(manifest):
    """F16: research stage must not read the registry before freeze."""
    if manifest.get("stage") == "RESEARCH" and manifest.get("registry_reads_before_freeze"):
        return ["RESEARCH_BLINDNESS_VIOLATION"]
    return []


# ---------------------------------------------------------------------------
# Batch-level assembly
# ---------------------------------------------------------------------------

def validate_batch(batch_dir: Path) -> int:
    errors: list[str] = []
    required = ["manifest.yaml", "programs.jsonl", "merge_tests.jsonl"]
    for name in required:
        if not (batch_dir / name).exists():
            # F08-guard: a batch may legitimately have zero programs only if the
            # manifest declares no program pressure; record and continue.
            errors.append(f"MISSING_FILE: {name}")
    manifest = {"stage": "CENSUS"}
    if (batch_dir / "manifest.yaml").exists():
        import yaml  # optional dep; tolerate absence for pure-python envs
        manifest = yaml.safe_load((batch_dir / "manifest.yaml").read_text(encoding="utf-8")) or manifest
    errors.extend(check_stage_blindness(manifest))

    def load(name):
        path = batch_dir / name
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    programs = load("programs.jsonl")
    stories = load("stories.jsonl")
    sketches = load("blind_programs.jsonl")
    coverage = load("coverage.jsonl")
    claims = load("absence_claims.jsonl")
    errors.extend(check_consequence_sketches(stories, sketches))
    errors.extend(check_absence_claims(coverage, claims))
    errors.extend(check_depth_gate(coverage))
    errors.extend(check_blind_freeze(programs))

    # census-side (Orchestrator §9)
    for test in load("merge_tests.jsonl"):
        verdict = test.get("verdict")
        if verdict == "MERGE_CONFIDENT" and test.get("structural_diffs"):
            errors.append(f"{test.get('program_id')}: MERGE_CONFIDENT with non-empty structural_diffs")
        if verdict == "TEMPLATE_EXTENSION_CANDIDATE":
            for field in ("extension_complexity_cost", "new_template_complexity_cost", "recommended_shape"):
                if not test.get(field):
                    errors.append(f"{test.get('program_id')}: EXTENSION missing {field}")
        if verdict in ("NEW_TEMPLATE_CANDIDATE", "TEMPLATE_EXTENSION_CANDIDATE", "NEW_RESOLVER") \
                and not test.get("human_review_queued"):
            errors.append(f"{test.get('program_id')}: {verdict} must enter Human Review Queue")

    print(f"validate_batch: {batch_dir.name}")
    print(f"  programs={len(programs)} stories={len(stories)} merge_tests={len(load('merge_tests.jsonl'))}")
    if errors:
        print(f"  FAIL ({len(errors)} errors)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("  PASS")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(validate_batch(Path(sys.argv[1])))
