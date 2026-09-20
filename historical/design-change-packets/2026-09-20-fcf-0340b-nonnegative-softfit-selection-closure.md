---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: APPLIED
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Nonnegative Soft Fit × Selection Compatibility Closure
date: 2026-09-20
owner_readjudication: true
depends_on:
  - PR#5@2a972ccf505f1a3d9e6c294f81324e55a2bb5e48
  - PR#9@ca22c0ea5f945e653271d1aae99fd93813531cc3
  - PR#11@99e0d38804ba9385969b119a2fd0d2324610dfb8
  - PR#12@3a4305dd925569bf6db73ef7d66b78e3c21f85ac
  - PR#13@a16a6350dd125be261e11cd59db137568c9690d3
---

# FCF 0.3.4.0-B｜Nonnegative Soft Fit × Selection Compatibility Closure

> Owner-approved re-adjudication delta. Historical/application packet only; Notion Current remains Authority.

## 1. Re-adjudication target

2026-09-18 GAP-005 allowed finite Soft Profile values outside [0,1], including negative values, to publish unchanged.

Complete-case validation found a decisive algebraic failure:

```text
CoreProduct = Π CORE Fit

one CORE = -0.5
→ CoreProduct = -0.5

two CORE = -0.5, -0.5
→ CoreProduct = +0.25
```

Negative suitability can therefore cancel itself and recreate positive opportunity.

Secondary has the same sign problem:

```text
SecondaryFactor = 0.75 + 0.25 × SecondaryProduct

one Secondary = -4
→ SecondaryFactor = -0.25

two Secondary = -3, -3
→ SecondaryProduct = 9
→ SecondaryFactor = 3
```

Existing Selection Compatibility also assumes nonnegative weights: W(q,m) >= 0.

Therefore negative Soft Fit is not a valid production value in the current Fit algebra.

## 2. Closed Decision｜split lower and upper overflow

For Structure / Feeding Layer / Time Period effective Soft Fit:

```text
Production-valid domain: [0, +∞)
Recommended range:       [0, 1]
```

TemperatureFit remains produced by its fixed curve in [0,1].

### Effective Fit < 0

```text
Editor durable state: allowed
Diagnostic: ERROR
Publish: BLOCK
Runtime: must not receive
```

### Effective Fit in [0,1]

Normal.

### Effective Fit > 1

```text
Diagnostic: WARNING
Publish: allowed
Runtime: consume authored value unchanged
No clamp
```

This preserves the useful half of GAP-005: explicit positive amplification.

## 3. Validate Effective Value, not ADD operand

Negative ADD delta remains legal when the resolved value is nonnegative.

```text
Source 0.8 + ADD -0.2 → 0.6 → PASS
Source 0.2 + ADD -0.3 → -0.1 → ERROR / Publish Block
```

Do not impose ADD delta >= 0.

SET follows the same effective-value rule.

## 4. Nonnegative proof chain

```text
StructureFit >= 0
FeedingLayerFit >= 0
TimePeriodFit >= 0
TemperatureFit in [0,1]

CoreProduct >= 0
SecondaryProduct >= 0
SecondaryFactor = 0.75 + 0.25 × SecondaryProduct >= 0.75
RawEnvCoeff >= 0

failEnvCoeff in [0,0.10]
envCoeffMin > 0
FinalEnvCoeff >= 0

BaseOpportunityIntensity >= 0

SpatialDistributionWeight
= BaseOpportunityIntensity × FinalEnvCoeff
>= 0
```

This closes the interface to Existing Selector without any transform layer.

## 5. Runtime rule

Runtime must not repair negative Soft Fit with clamp, abs, shift, normalization, fallback, or signed-weight selection.

If negative Effective Fit reaches Runtime, treat it as a contract violation / evaluation failure.

## 6. Autosave alignment

This uses the PR #13 durability boundary:

```text
negative Effective Fit
→ autosave allowed
→ saved with ERROR
→ Publish blocked
→ author can continue fixing
```

No durable Draft hierarchy is required.

## 7. GAP-005 supersession scope

Superseded:

```text
finite Effective Soft Fit < 0
→ warning only
→ publish allowed
```

Replaced by:

```text
Effective Soft Fit < 0
→ ERROR
→ durable authoring allowed
→ Publish blocked
→ Runtime must not receive
```

Still valid:

```text
Effective Soft Fit > 1
→ WARNING
→ Publish allowed
→ Runtime original value
→ no clamp
```

## 8. Negative Knowledge

Do not:

- restore symmetric treatment of both sides of [0,1];
- forbid negative ADD deltas;
- clamp negative Fit in Runtime;
- pass signed weights to Selection;
- apply abs / shift / renormalization;
- ban >1 as a side effect of this lower-bound correction;
- reinterpret 0 as an automatic Gate; Gate ownership remains unchanged.

## 9. Documentation targets

Documentation Agent should rebase latest Current and align:

1. Main B development requirement: Soft Profile domain, aggregation nonnegative proof, publish blockers, remove the negative-weight Current Open.
2. Schema / Validator: resolved Structure / Layer / Time Fit < 0 is publish-blocking ERROR; validate Effective Value, not operation sign.
3. Editor UI / condition controls: <0 ERROR, >1 WARNING; both can autosave.
4. Main Agent Control: close the negative Soft Profile × nonnegative weight-chain Open.
5. Change/adjudication record: append this Owner re-adjudication and narrowly supersede the negative half of GAP-005.

## 10. Application boundary

This packet is not Current Authority. Apply only after latest Notion Current rebase.

Application + readback PASS is required before status becomes APPLIED and before historical-ledger merge.