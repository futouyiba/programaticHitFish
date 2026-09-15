"""Runner for the FCF Presentation/Cue contract validation lane.

Usage (from the repository root, on the feature branch):

    python3 pc_validation/run_lane.py [--post-regression "204 passed / 1 skipped"]

Loads the lane fixtures, validates the holdout gate (must be sealed empty),
pins the run against the baseline record in ``pc_validation/baseline.json``
and the mirrored R1 addendum hash, then writes JSON + Markdown reports to
``pc_validation/reports/``.  The report separates Current-baseline
regression, PC-specific test counts and the post-change full regression
per the Design Owner ruling of 2026-09-16 (no single blended number).
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fcf_v1.pc_validation import (  # noqa: E402
    HoldoutRegistry, development_regression_summary, run_cases,
)

FIXTURES = ROOT / "pc_validation" / "fixtures"
REPORTS = ROOT / "pc_validation" / "reports"
R1_MIRROR = ROOT / "docs" / "pc_validation" / "FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16.md"
PC_TEST_FILE = ROOT / "tests" / "test_pc_validation.py"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_pc_tests() -> int:
    return sum(1 for line in PC_TEST_FILE.read_text(encoding="utf-8").splitlines()
               if line.startswith("def test_"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--post-regression", default=None,
                        help="full-repo regression result measured after the lane change")
    args = parser.parse_args()

    baseline = json.loads((ROOT / "pc_validation" / "baseline.json").read_text(encoding="utf-8"))
    if args.post_regression:
        baseline["post_change_regression"] = args.post_regression
    baseline["r1_addendum_sha256"] = sha256_of(R1_MIRROR)
    baseline["pc_specific_test_count"] = count_pc_tests()

    HoldoutRegistry.from_mapping(
        json.loads((FIXTURES / "holdout_registry.json").read_text(encoding="utf-8"))
    ).validate()  # hard gate: lane refuses to run against a non-empty/unprovenanced holdout

    devset_name = ("devset_r1_backfilled.json"
                   if (FIXTURES / "devset_r1_backfilled.json").exists()
                   else "devset_structural_r0.json")
    cases, dev_cases = [], []
    for name, synthetic in ((devset_name, False), ("lane_selftest_cases.json", True)):
        payload = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
        for case in payload["cases"]:
            case.setdefault("synthetic", synthetic)
            cases.append(case)
            if not synthetic:
                dev_cases.append(case)

    report = run_cases(cases, baseline=baseline)
    summary = development_regression_summary(report, dev_cases)

    payload = json.loads(report.to_json())
    payload["development_regression"] = summary
    md = report.to_markdown() + "\n## Development Regression\n\n```json\n" + \
        json.dumps(summary, indent=2, ensure_ascii=True, sort_keys=True) + "\n```\n"

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "pc_validation_report.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=True) + "\n", encoding="utf-8")
    (REPORTS / "pc_validation_report.md").write_text(md, encoding="utf-8")

    print(json.dumps({"summary": payload["summary"],
                      "development_regression": summary}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
