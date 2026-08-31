# Fish-Centric Conditional Funnel (FCF) V1

This repository is the executable design baseline for the RC4 mechanism. The
authoritative contracts are documented in [`docs/fcf_v1_engineering_spec.md`](docs/fcf_v1_engineering_spec.md)
and exercised by the tests in [`tests/test_fcf_v1.py`](tests/test_fcf_v1.py).

中文入口总览见 [`docs/fcf_v1_overview_cn.md`](docs/fcf_v1_overview_cn.md)，其中包含
概念、整体机制、配置示例、中文术语和主链路图示。

Additional review surfaces:

- [`docs/editor_contract.md`](docs/editor_contract.md) — transactional editor and attribute workflow;
- [`docs/flagship_traces.md`](docs/flagship_traces.md) — Spawn Bass, Trout Drift, and Carp Static Bait;
- [`docs/independent_review_checklist.md`](docs/independent_review_checklist.md) — narrow close review matrix;
- [`docs/verification_report.md`](docs/verification_report.md) — executed evidence and remaining gate.

The prototype intentionally models the V1 semantic boundaries rather than a
full game runtime: finite source-local population units, opportunity-ledger
entry, just-in-time candidates, deterministic encounter conversion, commit,
contact arbitration, hook compatibility, and idempotent settlement.

Run the verification suite with:

```text
python3 -m pytest -q
```

## Simplified V0 calibration experiment

The isolated, numeric-only calibration experiment can be reproduced with:

```text
python3 -m fcf_v1.calibration_experiment --output experiments/fcf_simplified_v0
```

It generates analytical and fixed-seed Monte Carlo CSV results plus the six
requested figures without changing the FCF V1 runtime model.

## Production handoff smoke check

The production runtime should expose a factory that satisfies the
`JournalAdapter`-backed engine contract. Run the deterministic handoff check
before the full fixture suite:

```python
from fcf_v1 import FCFEngine, SQLiteJournal, run_core_conformance

def production_factory():
    return FCFEngine(
        production_sources(),
        journal=SQLiteJournal("/var/lib/fcf/events.sqlite"),
        detailed_capacity=production_capacity(),
    )

report = run_core_conformance(production_factory)
if not report.passed:
    raise SystemExit(report.to_json())
```

The smoke check is intentionally narrow (finite entry, no-reroll replay,
idempotent settlement, and conservation). CI must additionally run the full
RC4 fixture/concurrency/property suite and persist the JSON report as review
evidence.
