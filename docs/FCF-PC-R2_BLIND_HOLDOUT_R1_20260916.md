# FCF-PC-R2 Blind Holdout Round 1 — Final Adjudicated Archive

**Report ID:** `FCF-PC-R2_BLIND_HOLDOUT_R1_20260916`  
**Date:** 2026-09-16  
**Repository:** `futouyiba/programaticHitFish`  
**Branch:** `fcf-v0-current-contract-rebase`  
**Parent baseline commit:** `9c2beebd2e2b1f5757223149e9c65f16bb200841`  
**Status:** `FINAL / IMMUTABLE AFTER COMMIT`  
**Round:** Blind Holdout Round 1  
**Post-reveal evidence status:** `DEVELOPMENT EVIDENCE`

---

## 1. Final Design Owner adjudication

```text
HOLDOUT_PASS_WITH_NARROW_DELTA
```

This is the accepted Round 1 adjudication.

The final archive corrects one statistical-scope issue from the pre-adjudication accounting: **H17 chemical concentration / chemical magnitude is family-level contaminated and is therefore confirmatory evidence only. It is excluded from the Blind Holdout primary denominator and from the blind pass/fail metric.**

No change to Presentation Contract R2 is made by this archive commit.

---

## 2. Scoped review record

```text
level
ARTIFACT

scope
FCF Presentation Contract R2 — Blind Holdout Round 1 final adjudicated report only.
This archive records the accepted Round 1 result, corrected blind-valid denominator,
contaminated/confirmatory split, narrow-delta family identity, and post-reveal evidence lifecycle.

baseline
FCF-PC-BASELINE-R2-20260916
repository parent: 9c2beebd2e2b1f5757223149e9c65f16bb200841

proves
Round 1 produced sufficient blind-valid coverage to accept HOLDOUT_PASS_WITH_NARROW_DELTA
under the final Design Owner accounting.
The primary blind metric contains 17 blind-valid cases.
H17 is not part of that primary metric.
The two NEW_PRIMITIVE_REQUIRED cases belong to one semantic capability family.

does_not_prove
This report does not modify or promote R2.
It does not design R3.
It does not select Round 2 cases.
It does not establish that every possible Presentation semantic is covered.
It does not convert contaminated evidence back into blind evidence.

open_findings
One NEW_GENERIC_RULE_REQUIRED finding remains as a narrow delta.
Two NEW_PRIMITIVE_REQUIRED findings remain, but they collapse to one semantic capability family:
continuous moving contact-generated disturbance.

verdict
HOLDOUT_PASS_WITH_NARROW_DELTA
```

---

## 3. Primary Blind Holdout metric

The final primary metric is:

```text
Blind-valid N = 17

COVERED                    13
ANNOTATION_ONLY             1
NEW_GENERIC_RULE_REQUIRED   1
NEW_PRIMITIVE_REQUIRED      2
```

The four categories sum to the full blind-valid denominator of 17.

The two `NEW_PRIMITIVE_REQUIRED` cases are **not two unrelated primitive families**. They are two observations of the same semantic capability family:

```text
continuous moving contact-generated disturbance
```

This family-level collapse is part of the final adjudication and must be preserved when the Round 1 result is cited later.

---

## 4. Confirmatory / contaminated evidence

Separately from the Blind-valid denominator:

```text
Confirmatory / contaminated evidence N = 1
H17 chemical magnitude
```

### H17 treatment

H17 tested chemical concentration / magnitude semantics. Because the relevant semantic family had already contaminated the blind boundary at family level, H17 is downgraded to **confirmatory evidence**.

H17 therefore:

- remains useful as discussion and confirmation evidence;
- remains part of the historical Round 1 record;
- **does not participate in `Blind-valid N`;**
- **does not participate in blind pass/fail accounting;**
- must not be used later to inflate the apparent blind coverage of R2.

Any earlier Round 1 summary that used 18 as the blind primary denominator is superseded by this final archive.

---

## 5. Case-level final accounting boundary

Round 1 consisted of case IDs H01–H18. The final adjudication changes the statistical role of H17 but does not rewrite the original pre-unblind observations.

The following case-level identities are explicitly fixed by the final adjudication:

| Case | Final role in Round 1 archive | Final classification / note |
|---|---|---|
| H12 | Blind-valid | `NEW_PRIMITIVE_REQUIRED`; same semantic capability family as H13 |
| H13 | Blind-valid | `NEW_PRIMITIVE_REQUIRED`; same semantic capability family as H12 |
| H17 | Confirmatory / contaminated | chemical concentration / magnitude; excluded from blind metric |

For H01–H11, H14–H16, and H18, this archive does **not** post-hoc reconstruct hidden labels, URLs, minimum evidence spans, or individual classifications from aggregate totals. Those fields must be read from the sealed pre-unblind case record if a later audit needs the exact row-level provenance. This non-reconstruction rule is intentional: after reveal, inferred row metadata would itself be contaminated and would no longer be an exact blind record.

The authoritative aggregate accounting for those remaining blind-valid cases is exactly the distribution in §3 and must not be reverse-engineered into case identities without the original sealed record.

---

## 6. Narrow-delta interpretation

Round 1 does not justify a broad rewrite of the Presentation Contract.

The accepted result contains only these delta classes at the metric level:

```text
1 × ANNOTATION_ONLY
1 × NEW_GENERIC_RULE_REQUIRED
2 × NEW_PRIMITIVE_REQUIRED
```

The two primitive-required observations reduce to one capability family:

```text
continuous moving contact-generated disturbance
```

This report records that fact only. It deliberately does **not** design the generic rule, does **not** define a new R3 primitive API, and does **not** alter R2.

---

## 7. Evidence lifecycle after reveal

Effective from the Round 1 reveal / Design Owner adjudication:

```text
All Round 1 cases = Development evidence
```

Consequences:

- H01–H18 may be used for subsequent development, regression, annotation refinement, and design discussion;
- none of H01–H18 may be reused as unseen blind evidence for a later holdout claim;
- H17 remains specially marked as confirmatory / contaminated even inside the Development evidence pool;
- future blind evaluation must use evidence not exposed by this Round 1 reveal.

This is an evidence-lifecycle statement only. It does not select or propose any Round 2 cases.

---

## 8. Archive exclusions

This commit is intentionally restricted to the report artifact.

```text
R2 modification          NO
R3 design                NO
Round 2 case selection   NO
Contract promotion       NO
Additional adjudication  NO
```

No implementation or contract files are changed by this archive action.

---

## 9. Immutable receipt semantics

The Git commit containing this file is the immutable report receipt.

The commit SHA is intentionally **not self-embedded inside the file**, because doing so would require a second content-changing commit and would make the self-reference non-identical. The immutable SHA is to be recorded externally alongside this report after the single archive commit succeeds.

The immutable receipt binds:

- this exact report content;
- the final `Blind-valid N = 17` accounting;
- the separate H17 confirmatory / contaminated evidence treatment;
- the `HOLDOUT_PASS_WITH_NARROW_DELTA` verdict;
- the single semantic capability family identity for H12/H13;
- the post-reveal transition of all Round 1 cases to Development evidence;
- the explicit non-actions: no R2 modification, no R3 design, no Round 2 case selection.

---

## 10. Final archive summary

```text
Round 1 verdict
HOLDOUT_PASS_WITH_NARROW_DELTA

Blind-valid N = 17
COVERED                    13
ANNOTATION_ONLY             1
NEW_GENERIC_RULE_REQUIRED   1
NEW_PRIMITIVE_REQUIRED      2

NEW_PRIMITIVE semantic capability families = 1
continuous moving contact-generated disturbance

Confirmatory / contaminated evidence N = 1
H17 chemical magnitude

After reveal
All Round 1 cases are Development evidence

R2 changed?              NO
R3 designed?             NO
Round 2 cases selected?  NO
```
