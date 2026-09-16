"""FCF Presentation / Cue contract validation lane.

Executes the structural contract of FCF-PC-BASELINE-R0-20260915, the
R1 addendum (FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16) and the R2 Development
Review Delta (FCF-PC-BASELINE-R2-20260916, D1-D6) and the R3 narrow delta
(FCF-PC-BASELINE-R3-CANDIDATE-20260916: contact disturbance primitive,
multi-source composition contract, crab-like dictionary reuse) against
fixture bundles.
The lane validates contract *shape* only:

- A1  fish-independent != geometry-independent boundary (R0 2.1)
- A2  kinematic reference-frame / temporal metadata (R0 3.2); D1: cue.displacement
      is NOT_ADMITTED / PROVISIONAL — removed from the core vocabulary (R2)
- A3  StaticTargetAffinity = Species x FeedingTargetKey, no Mode axis (R0 4)
- A4  classification record shape and decision order (R0 10)
- B1  CueSignature is a versioned semantic signature, never SKU memory (R0 5)
- B2  typed zero-target status, no ResponseBand mapping this round (R0 4)
- R0 8 cause-ownership double-count detection
- R0 4 deliberately-OPEN multi-target aggregation guard

It deliberately does NOT implement production physics, motion resolvers,
target interpretation, aggregation or ResponseBand mapping; those remain
open per R0 13 and must not be silently closed here.
"""
from dataclasses import dataclass
from enum import Enum
import json
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from .pre_generation import canonical_json, digest


# ---------------------------------------------------------------- contract --

# R3 (freeze-revised, ruling A): ONE generic primitive — moving contact with
# world geometry generates a fish-independent resolved disturbance fact.
# Plain OrderedBand magnitude; no composite temporal enum (movement comes
# from existing motion facts, duration/sustained from existing DurationFact
# / temporal_scope); no surface naming (avoids relation.surface ambiguity);
# no strategy token (mechanical_scrape / bottom_drag / ... stay rejected).
CONTACT_DISTURBANCE_CUE = "cue.contact_disturbance"

CUE_BASIS: Tuple[str, ...] = (
    "cue.apparent_size", "cue.visual_contrast", "cue.flash",
    "cue.speed", "cue.speed_change", "cue.direction_change",
    "cue.pause_duration", "cue.vertical_motion",
    "cue.vibration_amplitude", "cue.vibration_frequency",
    "cue.sound_amplitude", "cue.sound_pattern",
    CONTACT_DISTURBANCE_CUE,
)
CUE_CANDIDATE_EXTENSION = ("cue.chemical_intensity",)  # "?" per R0 3.2; stays candidate per R2 D4
# R2 D1: displacement was removed from the core vocabulary (NOT_ADMITTED /
# PROVISIONAL).  The name mixed several distinct physical quantities; any
# future concept (net spatial displacement / path length / hydrodynamic
# displacement / continuous contact travel) needs its own admission.
NOT_ADMITTED_CUES = ("cue.displacement",
                      # R3 Delta 2: raw multiplicity is NOT admitted; the
                      # CF-MULTI-1 counterfactual owns the reopen question.
                      "cue.source_count", "cue.lure_count",
                      "presentation.source_count", "presentation.lure_count")

# A2: facts whose frame cannot be implied by the field name must declare it.
FRAME_AMBIGUOUS_CUES = ("cue.speed", "cue.speed_change", "cue.direction_change")
# A2: vertical_motion may use an explicit gravity/world-vertical semantic.
WORLD_VERTICAL_SEMANTIC = "WORLD_VERTICAL"

# R0 7: explicitly forbidden canonical vocabulary.
FORBIDDEN_CUE_FIELDS = ("fish_visibility", "perceived_attractiveness", "injuredness", "provocation")
FORBIDDEN_PRESENTATION_FIELDS = (
    "presentation.injured_prey", "presentation.vulnerable", "presentation.easy_opportunity",
    "presentation.catchability", "presentation.presentation_quality",
    "cue.perceived_attractiveness", "cue.fish_visibility",
    "FeedingMatch", "PresentationMatch", "Universal AttractionScore",
)

# A1 / R0 2.1: a presentation/cue resolver may never read these inputs.
FISH_DEPENDENT_INPUT_TOKENS = (
    "species_preference", "engagement_mode_valuation", "fish_sensory_capability",
    "species_detection_threshold", "attractiveness", "valuation", "preference",
    "response_band", "selection_weight", "spawned_fish_state",
)
# A1: explicitly allowed reference inputs (geometry, not valuation).
GEOMETRY_INPUT_TOKENS = (
    "support_relative_distance", "support_relative_angle", "geometry",
    "medium_propagation", "background", "turbidity", "flow", "world_state",
)

# A3: affinity axes are fixed for v1.
AFFINITY_FORBIDDEN_KEY_PARTS = ("engagement_mode", "mode")

# R0 4: relation.feeding_target_affinity must not absorb these.
AFFINITY_ABSORPTION_FORBIDDEN = ("motion_quality", "drift_quality", "pause_timing",
                                 "flash_fit", "vibration_fit", "presentation_quality")

# B1: CueSignature composition.
SIGNATURE_ALLOWED_PREFIXES = ("presentation.", "cue.")
SIGNATURE_FORBIDDEN_KEYS = ("sku", "item_id", "technique_id", "merchandise_category",
                              "ui_action", "rig_identity")  # rig_identity per R3 Delta 2

# B2: typed target-resolution status.
class TargetResolutionStatus(str, Enum):
    HYPOTHESES = "HYPOTHESES"                      # 1..N typed hypotheses present
    NO_SUPPORTED_TARGET = "NO_SUPPORTED_TARGET"    # typed zero; NOT unknown
    UNKNOWN = "UNKNOWN"                            # resolution did not complete
    RESOLUTION_INCOMPLETE = "RESOLUTION_INCOMPLETE"

NON_AFFIRMATIVE_STATUSES = (TargetResolutionStatus.UNKNOWN.value,
                            TargetResolutionStatus.RESOLUTION_INCOMPLETE.value)

# R0 4: multi-target aggregation is deliberately OPEN; smuggling one in is a violation.
FORBIDDEN_AGGREGATORS = ("sum", "weighted_average", "max", "noisy_or")

# R3 (ruling A): these cues may share one physical cause (contact with world
# geometry, or one and the same acoustic/mechanical event).  Double-count
# prevention is provenance-based (ruling B): a rule consuming two of them must
# show, via cause identity in cause_provenance, that they stem from independent
# causes.  There is NO boolean override.
#
# IMPLEMENTATION CONFORMANCE FIX (2026-09-16, Design Owner adjudication of
# Blind Holdout Round 2): cue.sound_pattern joined the family.  The frozen R3
# contract already requires provenance across "contact disturbance vs
# vibration_* vs sound_*"; the family list was missing the sound_* rhythm
# aspect, so a rule double-weighting e.g. sound_amplitude + sound_pattern of
# one acoustic event (Round 2 report HR2-05 scope note) was not linted.
# Conformance fix only — no R4 semantic delta; sound_pattern was already an
# admitted CUE_BASIS member and gains no new semantics here.
CONTACT_CAUSE_FAMILY = (CONTACT_DISTURBANCE_CUE, "cue.vibration_amplitude",
                        "cue.vibration_frequency", "cue.sound_amplitude",
                        "cue.sound_pattern")

# R3 (ruling D): VALIDATION-LANE TEST VOCABULARY ONLY — the handful of
# FeedingTarget values exercised by this lane's fixtures.  This is NOT the
# canonical FeedingTarget dictionary; canonical membership authority stays
# with the FeedingTarget dictionary contract and its admission process.
FEEDING_TARGET_TEST_VOCABULARY = ("SMALL_BAITFISH", "CRUSTACEAN")

# A4: classification vocabulary and decision order.
CLASSIFICATION_VALUES = (
    "CAUSE_OWNERSHIP_CONFLICT", "UNRESOLVED",
    "COVERED", "ANNOTATION_ONLY", "DERIVED_DESCRIPTOR_ONLY",
    "NEW_GENERIC_RULE_REQUIRED", "NEW_PRIMITIVE_REQUIRED",
    "NEW_RELATION_REQUIRED", "ITEM_SPECIFIC_EXCEPTION",
)
PRIMARY_FIRST_STEP = ("CAUSE_OWNERSHIP_CONFLICT", "UNRESOLVED")  # checked before the ladder
MINIMAL_SUFFICIENT_LADDER = CLASSIFICATION_VALUES[2:]

DERIVED_DESCRIPTOR_FORBIDDEN_INPUTS = FISH_DEPENDENT_INPUT_TOKENS + ("sku", "item_id", "response")


# ----------------------------------------------------------------- findings --

class Severity(str, Enum):
    VIOLATION = "violation"    # contract breach
    UNRESOLVED = "unresolved"  # must be recorded UNRESOLVED, not implemented around
    INFO = "info"


@dataclass(frozen=True)
class Finding:
    code: str
    severity: Severity
    path: str
    detail: str
    citation: str


def _v(code: str, path: str, detail: str, citation: str) -> Finding:
    return Finding(code, Severity.VIOLATION, path, detail, citation)


def _u(code: str, path: str, detail: str, citation: str) -> Finding:
    return Finding(code, Severity.UNRESOLVED, path, detail, citation)


def _i(code: str, path: str, detail: str, citation: str) -> Finding:
    return Finding(code, Severity.INFO, path, detail, citation)


# --------------------------------------------------------------- validators --

def check_fish_independence(resolver: Mapping[str, Any], path: str) -> List[Finding]:
    """A1 / R0 2.1: same canonical support/geometry/World state => same value,
    regardless of evaluating Species or Engagement Mode identity."""
    out: List[Finding] = []
    for token in resolver.get("inputs", []):
        if token in FISH_DEPENDENT_INPUT_TOKENS:
            out.append(_v("FISH_DEPENDENT_INPUT", f"{path}.inputs",
                          f"resolver reads {token!r}", "R0 2.1 / R1 A1"))
    return out


def check_cue_vocabulary(cue_facts: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """R0 3.2 basis membership + R0 7 forbidden semantics."""
    out: List[Finding] = []
    for i, fact in enumerate(cue_facts):
        name = fact.get("name", "")
        p = f"{path}[{i}]"
        if name in FORBIDDEN_CUE_FIELDS or f"cue.{name}" in FORBIDDEN_PRESENTATION_FIELDS:
            out.append(_v("FORBIDDEN_CUE_SEMANTICS", p, f"{name!r} is forbidden vocabulary",
                          "R0 3.2 boundary / R0 7"))
        elif name in NOT_ADMITTED_CUES:
            out.append(_v("NOT_ADMITTED_CUE", p,
                          f"{name!r} is NOT_ADMITTED per R2 D1; use admitted facts or file "
                          "a semantic admission request", "R2 D1"))
        elif name not in CUE_BASIS and name not in CUE_CANDIDATE_EXTENSION:
            out.append(_v("UNKNOWN_CUE_TOKEN", p,
                          f"{name!r} is not in the frozen basis; needs admission",
                          "R0 9"))
    return out


def check_kinematic_metadata(cue_facts: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """A2: frame-ambiguous kinematics must declare reference_frame (+ temporal
    metadata); pause_duration is an upstream DurationFact; vertical_motion may
    use WORLD_VERTICAL; displacement is PROVISIONAL."""
    out: List[Finding] = []
    for i, fact in enumerate(cue_facts):
        name = fact.get("name", "")
        p = f"{path}[{i}]"
        if name in FRAME_AMBIGUOUS_CUES and not fact.get("reference_frame"):
            out.append(_v("FRAME_METADATA_MISSING", p,
                          f"{name} must record reference_frame explicitly", "R1 A2"))
        if name in FRAME_AMBIGUOUS_CUES and not fact.get("temporal_scope"):
            out.append(_v("FRAME_METADATA_MISSING", p,
                          f"{name} must record temporal_scope / summary_semantics", "R1 A2"))
        if name == CONTACT_DISTURBANCE_CUE and not fact.get("temporal_scope"):
            # duration/sustained semantics ride the existing temporal machinery;
            # the cue itself is a plain OrderedBand magnitude (ruling A)
            out.append(_v("FRAME_METADATA_MISSING", p,
                          f"{name} must record temporal_scope (duration semantics stay "
                          "on existing DurationFact / temporal_scope)", "R1 A2 / R3 ruling A"))
        if name == "cue.vertical_motion" and fact.get("reference_frame") not in (None, WORLD_VERTICAL_SEMANTIC):
            out.append(_v("FRAME_METADATA_INVALID", p,
                          "vertical_motion may only use the gravity/world-vertical semantic",
                          "R1 A2"))
    return out


def check_presentation_descriptors(descriptors: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """R0 3.1: fish-independent, cross-item reusable, not a SKU alias."""
    out: List[Finding] = []
    for i, d in enumerate(descriptors):
        name = d.get("name", "")
        p = f"{path}[{i}]"
        if name in FORBIDDEN_PRESENTATION_FIELDS or name.startswith("presentation.attractive_to_") \
                or name.startswith("presentation.good_for_"):
            out.append(_v("FORBIDDEN_PRESENTATION_FIELD", p, f"{name!r} is forbidden", "R0 7"))
        if "sku" in name or "product" in name:
            out.append(_v("SKU_ALIAS_DESCRIPTOR", p, f"{name!r} looks like a SKU alias", "R0 3.1"))
        if name in NOT_ADMITTED_CUES:
            out.append(_v("NOT_ADMITTED_CUE", p,
                          f"{name!r} is NOT_ADMITTED per R3 Delta 2 (raw multiplicity); "
                          "counterfactual CF-MULTI-1 owns the reopen question", "R3 Delta 2"))
    return out


def check_static_target_affinity(entries: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """A3: StaticTargetAffinity keyed by Species x FeedingTargetKey only; the
    relation must not absorb presentation-quality concerns (R0 4)."""
    out: List[Finding] = []
    for i, e in enumerate(entries):
        p = f"{path}[{i}]"
        for part in AFFINITY_FORBIDDEN_KEY_PARTS:
            if part in e:
                out.append(_v("MODE_AXIS_FORBIDDEN", p,
                              f"affinity key contains {part!r}; v1 axis is fixed to "
                              "Species x FeedingTargetKey", "R1 A3"))
        key = e.get("feeding_target_key")
        if key is not None and key not in FEEDING_TARGET_TEST_VOCABULARY:
            out.append(_u("DICTIONARY_MEMBER_ADMISSION_REQUIRED", p,
                          f"feeding_target_key {key!r} is outside this lane's test vocabulary "
                          f"{FEEDING_TARGET_TEST_VOCABULARY}; canonical FeedingTarget membership "
                          "is governed by its own dictionary authority — record an admission "
                          "request (R3 ruling D: CRUSTACEAN reused, nothing added)", "R3 ruling D"))
        for absorbed in AFFINITY_ABSORPTION_FORBIDDEN:
            if absorbed in e:
                out.append(_v("AFFINITY_ABSORPTION", p,
                              f"affinity entry contains {absorbed!r}; motion/drift/flash/"
                              "vibration fit must stay outside the relation", "R0 4"))
    return out


def check_dynamic_feeding_preference(entries: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """A3: dynamic preference must not become a Mode-specific target table."""
    return [
        _v("MODE_SPECIFIC_TARGET_TABLE", f"{path}[{i}]",
           "dynamic preference entry is Mode-keyed per target; forbidden auto-copy",
           "R1 A3")
        for i, e in enumerate(entries)
        if "engagement_mode_target_ranking" in e or "mode" in e.get("key_axes", ())
    ]


def check_target_resolution(resolution: Mapping[str, Any], path: str) -> List[Finding]:
    """B2: typed status; UNKNOWN / RESOLUTION_INCOMPLETE are not zero/bad
    affinity; no ResponseBand mapping this round."""
    out: List[Finding] = []
    status = resolution.get("status")
    if status not in (s.value for s in TargetResolutionStatus):
        out.append(_v("UNTYPED_TARGET_STATUS", path, f"status {status!r} is not typed", "R1 B2"))
        return out
    if status in NON_AFFIRMATIVE_STATUSES and resolution.get("affinity") is not None:
        out.append(_v("NON_AFFIRMATIVE_TREATED_AS_AFFINITY", path,
                      f"{status} must not be mapped to an affinity value", "R1 B2"))
    if resolution.get("response_band") is not None:
        out.append(_v("BAND_MAPPING_NOT_DECIDED", path,
                      "typed status -> ResponseBand mapping is open this round", "R1 B2 / R0 13"))
    return out


def cue_signature_identity(signature: Mapping[str, Any]) -> str:
    """B1: identity is the digest of version + admitted canonical facts only."""
    payload = {
        "signature_version": signature.get("signature_version"),
        "facts": {k: signature["facts"][k] for k in sorted(signature.get("facts", {}))},
    }
    return digest("cue_signature", payload)


def check_cue_signature(signature: Mapping[str, Any], path: str) -> List[Finding]:
    out: List[Finding] = []
    if not signature.get("signature_version"):
        out.append(_v("SIGNATURE_NOT_VERSIONED", path,
                      "CueSignature must carry a signature_version", "R1 B1"))
    for key in signature.get("facts", {}):
        if key in SIGNATURE_FORBIDDEN_KEYS:
            out.append(_v("SKU_MEMORY_LEAK", f"{path}.facts.{key}",
                          f"signature contains forbidden identity key {key!r}", "R1 B1"))
        elif not key.startswith(SIGNATURE_ALLOWED_PREFIXES):
            out.append(_v("SIGNATURE_UNADMITTED_SOURCE", f"{path}.facts.{key}",
                          f"{key!r} is not an admitted presentation.*/cue.* fact", "R1 B1"))
    return out


def check_classification(record: Mapping[str, Any], path: str) -> List[Finding]:
    """A4: exactly one primary, requested_deltas/flags lists, decision order,
    displacement-PROVISIONAL guard."""
    out: List[Finding] = []
    primary = record.get("primary_classification")
    if primary not in CLASSIFICATION_VALUES:
        out.append(_v("INVALID_PRIMARY_CLASSIFICATION", path,
                      f"primary_classification {primary!r} not in vocabulary", "R1 A4"))
        return out
    if not isinstance(record.get("requested_deltas", []), list):
        out.append(_v("INVALID_CLASSIFICATION_RECORD", path, "requested_deltas must be a list", "R1 A4"))
    if not isinstance(record.get("flags", []), list):
        out.append(_v("INVALID_CLASSIFICATION_RECORD", path, "flags must be a list", "R1 A4"))
    relied = record.get("relied_upon", []) or []
    if any(r in NOT_ADMITTED_CUES for r in relied) and primary == "COVERED":
        out.append(_v("NOT_ADMITTED_CUE", path,
                      "case relying on a NOT_ADMITTED cue cannot be COVERED; use admitted "
                      "facts or record a semantic admission request", "R2 D1"))
    return out


def check_cause_ownership(response_rules: Sequence[Mapping[str, Any]],
                          provenance: Mapping[str, Sequence[str]], path: str) -> List[Finding]:
    """R0 8 + R3 ruling B: double-count prevention is provenance-based.

    There is deliberately NO boolean justification override (no
    CAUSE_JUSTIFIED in contract, DSL, schema or validator logic): consuming
    two facts that share a recorded cause identity is a conflict, period.
    Independence is demonstrated only by cause provenance / cause identity.
    """
    out: List[Finding] = []
    for i, rule in enumerate(response_rules):
        p = f"{path}[{i}]"
        consumes = set(rule.get("consumes", []))
        # direct: a consumed cue plus one of its own recorded causes
        for cue in consumes:
            for cause in provenance.get(cue, []):
                if cause in consumes:
                    out.append(_v("CAUSE_OWNERSHIP_CONFLICT", p,
                                  f"rule consumes both {cue!r} and its recorded cause "
                                  f"{cause!r} (shared cause identity; no override exists)", "R0 8 / R3 B"))
        # family: two contact-cause-family members must prove independent causes
        family_hits = sorted(consumes & set(CONTACT_CAUSE_FAMILY))
        if len(family_hits) >= 2:
            cause_sets = {c: set(provenance.get(c, ())) for c in family_hits}
            shared = set.intersection(*cause_sets.values()) if cause_sets else set()
            if shared:
                out.append(_v("CAUSE_OWNERSHIP_CONFLICT", p,
                              f"rule weights {family_hits} sharing cause identity "
                              f"{sorted(shared)}", "R3 ruling A/B"))
            elif any(not cs for cs in cause_sets.values()):
                undeclared = [c for c, cs in cause_sets.items() if not cs]
                out.append(_u("CAUSE_PROVENANCE_REQUIRED", p,
                              f"rule weights {family_hits} without cause identity for "
                              f"{undeclared}; declare cause_provenance to show the consumed "
                              "facts stem from independent causes", "R3 ruling B"))
    return out


def check_aggregation_smuggling(resolvers: Sequence[Mapping[str, Any]], path: str) -> List[Finding]:
    """R0 4 deliberately OPEN: no sum/weighted average/max/Noisy-OR for
    multiple feeding-target hypotheses."""
    out: List[Finding] = []
    for i, r in enumerate(resolvers):
        for agg in FORBIDDEN_AGGREGATORS:
            if r.get("multi_target_aggregator") == agg:
                out.append(_v("AGGREGATOR_SMUGGLED", f"{path}[{i}]",
                              f"{agg!r} aggregation of hypotheses is deliberately OPEN; "
                              "record UNRESOLVED instead", "R0 4"))
    return out


def check_derived_descriptor(defn: Mapping[str, Any], path: str) -> List[Finding]:
    """A4 determinism: admitted fish-independent inputs only; same input =>
    same descriptor; no species/mode/response/SKU reads."""
    out: List[Finding] = []
    for token in defn.get("inputs", []):
        if token in DERIVED_DESCRIPTOR_FORBIDDEN_INPUTS:
            out.append(_v("NON_DETERMINISTIC_DESCRIPTOR", f"{path}.inputs",
                          f"derived descriptor reads {token!r}", "R1 A4"))
    if defn.get("nondeterministic", False):
        out.append(_v("NON_DETERMINISTIC_DESCRIPTOR", path,
                      "descriptor declares nondeterminism", "R1 A4"))
    return out


# --------------------------------------------- composition resolver (R3 D2) --

COMPOSITION_FORBIDDEN_SOURCE_KEYS = SIGNATURE_FORBIDDEN_KEYS


def check_composition_resolver(composition: Mapping[str, Any], path: str) -> List[Finding]:
    """R3 Delta 2: 0..N source-local facts -> deterministic resolver -> canonical
    snapshot.  No raw rig/SKU/technique identity anywhere; no multiplicity fact."""
    out: List[Finding] = []
    sources = composition.get("sources", [])
    if not isinstance(sources, list):
        out.append(_v("COMPOSITION_INVALID", path, "sources must be a list", "R3 Delta 2"))
        return out
    for i, source in enumerate(sources):
        for key in source:
            if key in COMPOSITION_FORBIDDEN_SOURCE_KEYS:
                out.append(_v("COMPOSITION_IDENTITY_LEAK", f"{path}.sources[{i}].{key}",
                              f"source carries forbidden identity key {key!r}", "R3 Delta 2"))
    resolver = composition.get("resolver", {})
    if not resolver.get("deterministic", False):
        out.append(_v("COMPOSITION_NON_DETERMINISTIC", f"{path}.resolver",
                      "composition resolver must be declared deterministic", "R3 Delta 2"))
    for token in resolver.get("inputs", []):
        if token in FISH_DEPENDENT_INPUT_TOKENS:
            out.append(_v("COMPOSITION_FISH_DEPENDENT", f"{path}.resolver.inputs",
                          f"resolver reads {token!r}", "R3 Delta 2 / R0 2.1"))
    return out


def counterfactual_summary(counterfactuals: Sequence[Mapping[str, Any]]) -> List[Dict[str, str]]:
    return [{"id": c.get("id", ""), "status": c.get("status", ""),
             "question": c.get("question", "")} for c in counterfactuals]


# ------------------------------------------------------------- holdout gate --

class HoldoutError(RuntimeError):
    pass


@dataclass(frozen=True)
class HoldoutRegistry:
    """R0 12: blind holdout identities are chosen by the independent Reviewer /
    Sample Agent after the implementation lane is executable and regression
    PASS.  The registry therefore starts -- and in this repo stays -- empty."""

    real_cases: Tuple[str, ...] = ()
    provenance: Optional[Mapping[str, Any]] = None

    def validate(self) -> None:
        if self.real_cases:
            raise HoldoutError(
                "HOLDOUT_NOT_EMPTY: real unseen cases may only enter via the "
                "independent Sample Agent (R0 12 / HOLDOUT-HANDOFF-R0)")
        if self.provenance is not None:
            for key in ("sample_agent", "frame_version", "delivered_at"):
                if key not in self.provenance:
                    raise HoldoutError(f"HOLDOUT_MISSING_PROVENANCE: {key} required (R1 B-discipline)")

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "HoldoutRegistry":
        return cls(tuple(data.get("real_cases", ())), data.get("provenance"))


# ------------------------------------------------------------------- report --

@dataclass(frozen=True)
class CaseResult:
    case_id: str
    bundle_id: str
    synthetic: bool
    findings: Tuple[Finding, ...]
    classification: Optional[Mapping[str, Any]] = None

    @property
    def violations(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.VIOLATION)


@dataclass(frozen=True)
class PCValidationReport:
    baseline: Mapping[str, Any]
    case_results: Tuple[CaseResult, ...]

    @property
    def violations(self) -> int:
        return sum(c.violations for c in self.case_results)

    def classification_counts(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for c in self.case_results:
            if c.classification and c.classification.get("primary_classification") in CLASSIFICATION_VALUES:
                key = c.classification["primary_classification"]
                counts[key] = counts.get(key, 0) + 1
        return dict(sorted(counts.items()))

    def findings_by_code(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for c in self.case_results:
            for f in c.findings:
                counts[f.code] = counts.get(f.code, 0) + 1
        return dict(sorted(counts.items()))

    def descriptor_token_counts(self) -> Dict[str, int]:
        return {
            "cue_basis": len(CUE_BASIS),
            "cue_candidate_extension": len(CUE_CANDIDATE_EXTENSION),
            "cue_not_admitted": len(NOT_ADMITTED_CUES),
        }

    def as_dict(self) -> Dict[str, Any]:
        return {
            "lane": "fcf_pc_validation",
            "contract": {
                "baseline_r0": "FCF-PC-BASELINE-R0-20260915",
                "baseline_r1_addendum": "FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16",
            },
            "run": dict(self.baseline),
            "summary": {
                "cases": len(self.case_results),
                "synthetic_cases": sum(1 for c in self.case_results if c.synthetic),
                "development_cases": sum(1 for c in self.case_results if not c.synthetic),
                "violations": self.violations,
                "classification_counts": self.classification_counts(),
                "findings_by_code": self.findings_by_code(),
                "descriptor_token_counts": self.descriptor_token_counts(),
            },
            "cases": [
                {
                    "case_id": c.case_id, "bundle_id": c.bundle_id, "synthetic": c.synthetic,
                    "classification": c.classification,
                    "findings": [
                        {"code": f.code, "severity": f.severity.value, "path": f.path,
                         "detail": f.detail, "citation": f.citation}
                        for f in c.findings
                    ],
                }
                for c in self.case_results
            ],
        }

    def to_json(self) -> str:
        return canonical_json(self.as_dict())

    def to_markdown(self) -> str:
        s = self.as_dict()["summary"]
        lines = [
            "# FCF Presentation/Cue Contract Validation — Run Report", "",
            f"- lane: `fcf_pc_validation` — R0 `FCF-PC-BASELINE-R0-20260915` + R1 addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`",
            f"- baseline commit: `{self.baseline.get('baseline_commit', 'n/a')}`",
            f"- R1 addendum sha256: `{self.baseline.get('r1_addendum_sha256', 'n/a')}`",
            f"- pre-change regression: {self.baseline.get('pre_change_regression', 'n/a')}",
            f"- post-change regression: {self.baseline.get('post_change_regression', 'n/a')}", "",
            "## Summary", "",
            f"- cases: {s['cases']} (development {s['development_cases']}, synthetic lane self-test {s['synthetic_cases']})",
            f"- violations: {s['violations']}",
            f"- classification counts: {json.dumps(s['classification_counts'])}",
            f"- descriptor token counts: {s['descriptor_token_counts']}",
            "",
            "## Findings by code", "",
        ]
        for code, count in (s["findings_by_code"] or {"NONE": 0}).items():
            lines.append(f"- `{code}`: {count}")
        lines += ["", "## Per-case findings", ""]
        for c in self.case_results:
            kind = "synthetic" if c.synthetic else "development"
            lines.append(f"### {c.case_id} ({kind}, bundle `{c.bundle_id}`)")
            if c.classification:
                lines.append(f"- classification: `{c.classification.get('primary_classification')}`"
                             f" deltas={c.classification.get('requested_deltas')}"
                             f" flags={c.classification.get('flags')}")
            if not c.findings:
                lines.append("- findings: none")
            for f in c.findings:
                lines.append(f"- [{f.severity.value}] `{f.code}` @ {f.path} — {f.detail} ({f.citation})")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------- lane body --

BREAKING_CLASSIFICATIONS = frozenset({
    "UNRESOLVED", "NEW_GENERIC_RULE_REQUIRED", "NEW_PRIMITIVE_REQUIRED",
    "NEW_RELATION_REQUIRED", "ITEM_SPECIFIC_EXCEPTION",
})


def development_regression_summary(report: "PCValidationReport",
                                   cases: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """Owner-adjudicated Development Regression readout (ruling 2026-09-16 step 6).

    `cases` are the raw fixture records (the report alone does not carry
    bundles).  Fish x Descriptor resurfacing is NOT measurable from DEV
    fixtures yet because no Response rules are encoded in them — stated
    honestly instead of computed from absent data.
    """
    by_id = {c.get("case_id"): c for c in cases}
    dev_ids = [c.case_id for c in report.case_results if not c.synthetic]
    distribution: Dict[str, int] = {}
    breaking, displacement_dependent, chemical_gap, ownership_watch, known_gaps = [], [], [], [], []
    used: set = set()
    backfilled = awaiting = 0
    for case_id in dev_ids:
        case = by_id.get(case_id, {})
        bundle = case.get("bundle", {})
        status = case.get("backfill_status")
        backfilled += status == "BACKFILLED"
        awaiting += status == "AWAITING_NOTION_BACKFILL"
        for fact in bundle.get("cue_facts", []):
            used.add(fact.get("name", ""))
        record = bundle.get("classification", {})
        primary = record.get("primary_classification")
        if primary in CLASSIFICATION_VALUES:
            distribution[primary] = distribution.get(primary, 0) + 1
        if primary in BREAKING_CLASSIFICATIONS:
            breaking.append(case_id)
        relied = record.get("relied_upon", []) or []
        if "cue.displacement" in relied:
            displacement_dependent.append(case_id)
        flags = record.get("flags", []) or []
        if "CHEMICAL_INTENSITY_GAP_WATCH" in flags:
            chemical_gap.append(case_id)
        if "CAUSE_OWNERSHIP_LINT_WATCH" in flags or "LINT_WATCH_DOUBLE_COUNT" in flags:
            ownership_watch.append(case_id)
        if any(f.startswith("KNOWN_DEV_GAP") for f in flags):
            known_gaps.append(case_id)
    return {
        "backfilled_count": backfilled,
        "awaiting_count": awaiting,
        "classification_distribution": dict(sorted(distribution.items())),
        "breaking_cases": sorted(breaking),
        "unused_basis_cues": {cue: "UNEXERCISED_BY_CURRENT_DEVSET"
                              for cue in sorted(set(CUE_BASIS) - used)},
        "known_dev_gap_cases": sorted(known_gaps),
        "displacement_dependent_cases": sorted(displacement_dependent),
        "chemical_intensity_gap_cases": sorted(chemical_gap),
        "ownership_watch_cases": sorted(ownership_watch),
        "fish_descriptor_resurfacing": "NOT_MEASURABLE_FROM_DEV_FIXTURES: DEV bundles carry "
                                       "fact requirements and classifications, no authored "
                                       "Response rules yet; monitor per R0 9 once rules exist",
    }


def validate_bundle(bundle: Mapping[str, Any]) -> Tuple[Finding, ...]:
    findings: List[Finding] = []
    findings += check_cue_vocabulary(bundle.get("cue_facts", []), "cue_facts")
    findings += check_kinematic_metadata(bundle.get("cue_facts", []), "cue_facts")
    findings += check_presentation_descriptors(bundle.get("presentation_descriptors", []),
                                               "presentation_descriptors")
    for i, resolver in enumerate(bundle.get("resolvers", [])):
        findings += check_fish_independence(resolver, f"resolvers[{i}]")
    findings += check_aggregation_smuggling(bundle.get("resolvers", []), "resolvers")
    for i, defn in enumerate(bundle.get("derived_descriptors", [])):
        findings += check_derived_descriptor(defn, f"derived_descriptors[{i}]")
    findings += check_static_target_affinity(bundle.get("static_target_affinity", []),
                                             "static_target_affinity")
    findings += check_dynamic_feeding_preference(bundle.get("dynamic_feeding_preference", []),
                                                 "dynamic_feeding_preference")
    if "target_resolution" in bundle:
        findings += check_target_resolution(bundle["target_resolution"], "target_resolution")
    if "cue_signature" in bundle:
        findings += check_cue_signature(bundle["cue_signature"], "cue_signature")
    if "composition" in bundle:
        findings += check_composition_resolver(bundle["composition"], "composition")
    findings += check_cause_ownership(bundle.get("response_rules", []),
                                      bundle.get("cause_provenance", {}), "response_rules")
    if "classification" in bundle:
        findings += check_classification(bundle["classification"], "classification")
    return tuple(findings)


def run_cases(cases: Sequence[Mapping[str, Any]], baseline: Mapping[str, Any]) -> PCValidationReport:
    results = []
    for case in cases:
        bundle = case.get("bundle", {})
        findings = list(validate_bundle(bundle))
        if case.get("backfill_status") == "AWAITING_NOTION_BACKFILL":
            findings.append(_i("AWAITING_BACKFILL", case.get("case_id", ""),
                               "expectations/inputs not yet backfilled from 中鱼库/推导表; "
                               "no semantics may be invented locally",
                               "DEVSET-REGISTRY-R0 / AGENTS.md"))
        results.append(CaseResult(
            case_id=case.get("case_id", ""),
            bundle_id=case.get("bundle_id", ""),
            synthetic=bool(case.get("synthetic", False)),
            findings=tuple(findings),
            classification=bundle.get("classification"),
        ))
    return PCValidationReport(baseline=baseline, case_results=tuple(results))
