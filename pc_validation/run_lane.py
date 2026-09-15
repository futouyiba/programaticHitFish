"""Runner for the FCF Presentation/Cue contract validation lane.

Usage (from the repository root, on the feature branch):

    python3 pc_validation/run_lane.py [--post-regression "141 passed / 0 failed"]

Loads the lane fixtures, validates the holdout gate (must be sealed empty),
pins the run against the baseline record in ``pc_validation/baseline.json``
and the mirrored R1 addendum hash, then writes JSON + Markdown reports to
``pc_validation/reports/``.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fcf_v1.pc_validation import HoldoutRegistry, run_cases  # noqa: E402

FIXTURES = ROOT / "pc_validation" / "fixtures"
REPORTS = ROOT / "pc_validation" / "reports"
R1_MIRROR = ROOT / "docs" / "pc_validation" / "FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16.md"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--post-regression", default=None,
                        help="full-repo regression result measured after the lane change")
    args = parser.parse_args()

    baseline = json.loads((ROOT / "pc_validation" / "baseline.json").read_text(encoding="utf-8"))
    if args.post_regression:
        baseline["post_change_regression"] = args.post_regression
    baseline["r1_addendum_sha256"] = sha256_of(R1_MIRROR)

    HoldoutRegistry.from_mapping(
        json.loads((FIXTURES / "holdout_registry.json").read_text(encoding="utf-8"))
    ).validate()  # hard gate: lane refuses to run against a non-empty/unprovenanced holdout

    cases = []
    for name, synthetic in (("devset_structural_r0.json", False), ("lane_selftest_cases.json", True)):
        payload = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            case.setdefault("synthetic", synthetic)
            cases.append(case)

    report = run_cases(cases, baseline=baseline)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "pc_validation_report.json").write_text(report.to_json() + "\n", encoding="utf-8")
    (REPORTS / "pc_validation_report.md").write_text(report.to_markdown() + "\n", encoding="utf-8")

    summary = json.loads(report.to_json())["summary"]
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
