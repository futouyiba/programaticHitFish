# Response Fixed-Pan Calibration Harness

**Status: EXPERIMENT / VALIDATION ONLY — NOT production runtime, NOT parameter authority.**

This harness is the numeric continuation of the current Simplified V0 Response working contract:

```text
PreResponseWeight U_i
× ResponseMultiplier r_i
→ SelectionWeight W_i

F = ΣW_i
ρ = F/N

P(any fish) = min(1, ρ)
P(None) = max(0, 1-ρ)
```

It exists to collect the operating evidence needed to calibrate `LOW / NORMAL`.
It does **not** reopen the Response resolver and does **not** freeze production
multipliers.

## Why this is a separate experiment

The repository already contains `fcf_v1/calibration_experiment.py`. That older
experiment uses:

```text
P(any) = W / (K + W)
NORMAL = 1
HIGH > 1
VERY_HIGH exists
```

Those assumptions are structurally incompatible with the current fixed-pan
working semantics and the current Response anchors:

```text
NONE = 0
0 < LOW < NORMAL < HIGH
HIGH = 1
```

The older experiment is intentionally left unchanged as historical/contrast
evidence. This harness must not silently mutate back into the additive-pool model.

## Critical ownership boundary

The harness requires callers to provide `preResponseWeight` explicitly.

It does **not** infer `U_i` from any of these fields:

- `SpatialDistributionWeight`
- `spatialOpportunityIntensity`
- BaseOpportunity
- Bake output
- Exposure output

The current 0.3.4 pipeline may still contain Routing / Bake / Exposure ownership
between those values and the Response input. Guessing that seam would create a
new cross-layer contract by accident.

## Run

Worked example:

```bash
python3 experiments/response_fixed_pan_calibration.py \
  --input experiments/fixtures/response_fixed_pan_worked_example.json
```

Default mapping × `ρ_high` sweep:

```bash
python3 experiments/response_fixed_pan_calibration.py \
  --sweep-csv /tmp/response_fixed_pan_sweep.csv
```

Tests:

```bash
pytest tests/test_response_fixed_pan_calibration.py -q
```

## Output contract

For each candidate:

```text
candidateId
preResponseWeight U_i
ResponseBand
ResponseMultiplier r_i
SelectionWeight W_i
referenceCompositionShare
```

For the whole snapshot:

```text
N
F
ρ
P(any fish)
P(None)
SaturationState
targetWeight
targetPurityReference
```

`referenceCompositionShare = W_i/F` is diagnostic only. When `ρ >= 1`, exact
production composition remains unverified until the current overflow /
Quality-Priority selector wiring is checked.

## Three-pass calibration sequence

1. **Native Weight Surface** — use this harness with PRD / fallback disabled.
2. **Native Temporal Surface** — add real semantic opportunity timestamps; do not
   use frame/tick/poll frequency.
3. **Control Overlay** — only then add PRD / empty-weight decay / fallback and
   inspect how much it changes P90/P95/P99 tails versus median/strategy contrast.

Do not infer Response multipliers from final observed wait time while control
layers are active.

## Current unresolved inputs

The harness is executable, but production calibration remains open until the
current implementation/data can provide:

1. representative real `PreResponseWeight U_i` snapshots;
2. the current fixed-pan scale `N`;
3. the current exact saturated overflow selector wiring;
4. real semantic opportunity cadence / timestamps;
5. product experience targets for HIGH/NORMAL/LOW contrast.

Until then, `.25 / .50` remains only an adversarial contrast seed.
