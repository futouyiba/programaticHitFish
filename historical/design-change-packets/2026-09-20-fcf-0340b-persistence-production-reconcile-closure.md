---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: READY_FOR_APPLICATION
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Persistence Validity × Derived Diagnostics × Production Reconcile
date: 2026-09-20
depends_on:
  - PR#13@a16a6350dd125be261e11cd59db137568c9690d3
  - PR#14@2674bf395770d45132500261a4abdf250903f582
---

# FCF 0.3.4.0-B｜Persistence Validity × Derived Diagnostics × Production Reconcile

> Historical/application packet only. Notion Current remains Authority.

## 1. Correction｜durable semantic error vs malformed typed record

PR #13 was too broad when it implied an incomplete required Component/Profile could always autosave.

Durable editor-state may contain a publish-blocking semantic error only after a valid typed/schema object exists.

Allowed durable examples:
- Temperature cross-field order invalid;
- Effective Soft Fit < 0;
- failEnvCoeff outside production-valid range;
- Source rebase creates another representable but publish-invalid combination.

These become: autosave allowed → saved with ERROR → Publish blocked.

Normal UI must NOT commit a new durable typed state for:
- raw unparseable input such as -, 0., abc;
- NaN / invalid type;
- existing numeric record with required value null;
- half-created Recipe with missing required source/identity;
- other schema-malformed partial objects.

A whole Component/override may still be unconfigured by record absence. Do not encode 'unconfigured' as an existing record with null required fields.

## 2. Closure｜diagnostics are derived, not durable truth

Current diagnostics are recomputed from:

editor-state + current schema + current validator → diagnostics

Do not persist warning/error lists as a second validity truth. Reopening the editor should recompute <0 ERROR, >1 WARNING, broken refs, cross-field errors, etc.

Logs/telemetry may persist separately but do not determine current validity.

## 3. Closed Decision｜Production → Editor is explicit bulk reconcile

Normal direction remains:

Editor durable state → Resolve → Materialize → Production

Editor State is the normal authoring truth.

Production may nevertheless be changed out-of-band by manual edits, batch tools, or engineering repair scripts.

Therefore provide an explicit user-triggered action: Reconcile / Import from Production.

No background reverse sync.

## 4. Compare canonical final values, not physical sharing

Production subtable rows may be shared because of materialization/dedupe. Reconcile must first decode Production into canonical final values per current Affinity/FishEnvAffinityRef and policy fields, then compare those values with current Editor Resolve.

Physical production row sharing is not Authoring inheritance intent.

## 5. Bulk adopt semantics

For selected numeric differences:

Production final value → current AffinityAuthoringPatch field SET

Example: Editor Grass 0.70, Production Grass 0.55 → adopt creates Affinity Grass SET 0.55.

Do NOT infer:
- Shared Template mutation;
- Species Recipe mutation;
- ADD delta;
- SpeciesConcreteSource mutation.

Production final values cannot uniquely prove those upstream intentions.

Bulk import may create many SET records. That is acceptable and explicit: it captures many out-of-band production edits without guessing upstream authoring intent.

## 6. Policy differences

Adopt Production AggregationRole / failEnvCoeff as explicit SET at the current Affinity/Policy layer. Do not automatically rewrite Shared Policy Template.

## 7. Temperature boundary

Production Temperature edits are game configuration edits, not ecological research corrections.

Adopt them as Affinity Temperature SET values. SpeciesConcreteSource changes only through its formal research/import workflow.

## 8. Shared production row changed externally

If one production profile row is shared by Affinity A/B/C and an external tool edits it, Reconcile shows final-value diffs for A/B/C.

Bulk adoption creates explicit SETs for the selected affected Affinities. It does not infer or create a Shared Template from physical row sharing.

## 9. Bulk transaction

P0 must support a batch scope large enough for many production changes. Exact UI may offer all diffs, species, affinity, component or field scopes.

Flow:
read Production snapshot → decode canonical final values → diff vs Editor Resolve → preview counts/fields/errors → select scope → confirm once → atomic editor-state commit → rerun diagnostics.

Do not require one confirmation per changed field.

## 10. Structural diffs are not silently absorbed

Do not auto-import as ordinary numeric reconcile:
- FishQualityRef → FishEnvAffinityRef mapping changes;
- unmappable/missing/duplicate owner records;
- unknown schema migration;
- Opportunity/FishRelease fields outside current Fish Behavior Editor scope.

Report them as structural differences requiring a separate workflow/owner decision.

## 11. Postcondition

For adopted numeric/policy scope, Editor Resolve should semantically match current Production values.

Physical row IDs/dedupe layout may differ on the next Publish; semantic equality is the acceptance criterion.

## 12. Full rebootstrap is separate recovery

If editor-state is lost/corrupted, rebuilding a new authoring baseline from Production is a destructive migration/recovery tool.

Daily bulk Reconcile does not try to recover original Template / Species Recipe / ADD lineage from flattened final values.

## 13. Negative Knowledge

Do not:
- auto-sync Production back into Editor;
- guess ADD/Template/SpeciesConcrete intent from final values;
- infer Shared Template from production row sharing;
- persist diagnostics as validity truth;
- encode unconfigured as null required fields;
- silently treat structural mapping changes as numeric reconcile.

## 14. Documentation targets

Rebase latest Current, then update Editor Persistence / Editor→Persistence / Editor UI+Resolve / adjudication record to close §9.2 and rewrite §9.4 around explicit bulk Production Reconcile.

## 15. Application boundary

This packet is not Current Authority. Application + readback PASS is required before APPLIED historical-ledger merge.