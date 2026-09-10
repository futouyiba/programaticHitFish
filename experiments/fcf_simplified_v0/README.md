# FCF Simplified V0 calibration experiment

Document status: **RETAINED / GENERATED-EVIDENCE ENTRY**  
Authority: **V0 experiment only; not an FCF V1 contract**  
Scope: fixed-seed numeric calibration outputs under this directory.  
Reproduction: the command in `Reproduce` with the recorded seed.  
V1 promotion rule: outputs remain evidence until an explicit V1 owner review.

This directory is the executable numeric experiment defined by the Calibration Prototype Experiment Spec R0. It does not add mechanics, fit real fish parameters, or change the FCF design.

## Reproduce

```text
python3 -m fcf_v1.calibration_experiment --output experiments/fcf_simplified_v0 --samples 1000000 --seed 20260831
```

The run uses a fixed seed and writes the requested CSV files under `results/` and six PNG figures under `figures/`. Every parameter point uses at least 1,000,000 analytical-equivalent Bernoulli or categorical samples. Cadence verification additionally aggregates synthetic 60-minute sessions.

## Assertions

All required deterministic assertions passed: technical/mode split invariance, NONE addition invariance, probability normalization, grade monotonicity, exposure monotonicity, Hook-only upstream isolation, and Conversion-only Engagement isolation.

## Observations

- Analytical and Monte Carlo saturation/grade-map points differed by at most 0.001417 in this run.
- The largest fixed-category substitution change in the requested sweep was 125.00% (vary_A, Compressed, K/reference=0.25, varied grade=NONE).
- In the requested roster grid, P(any) >= 0.9 first appears at N=20 (pressure=0.5).
- The weaker-per-event, higher-rate technique was stronger per minute in 8 of 12 requested ratio pairs.
- Under unlimited Conversion attempts, P(at least one conversion) >= 0.9 first appears at p=0.7, N=2.
- At Exposure=K=ReferenceExposure, all maps share NORMAL=1 and therefore the same NORMAL result; their LOW/HIGH/VERY_HIGH separation differs as recorded in `results/summary.csv` and `figures/grade_map_sensitivity.png`.

## REOPEN SIGNALS

The observations above correspond only to the five requested reopen-signal categories: substitution coupling, roster saturation, cadence sensitivity, repeated Conversion attempts, and grade-map sensitivity. They are measurements for the design thread, not gameplay conclusions.

## Output schema notes

- `summary.csv`: K saturation, grade-map sensitivity, and compact reopen-signal rows.
- `invariance.csv`: exact deterministic invariance checks and differences.
- `substitution.csv`: both substitution sweep directions, analytical and simulated probabilities.
- `roster_saturation.csv`: N x pressure surface and per-category absolute probability.
- `cadence.csv`: Opportunity cadence surface plus normalized paired-technique comparisons.
- `conversion_reroll.csv`: G1/G2/G3 results; G3 cycles four synthetic semantic event-family labels, so effective attempts cap at four.
- `gear_isolation.csv`: shared-draw sequential-funnel counters for HookCompatibility and Conversion sweeps.
