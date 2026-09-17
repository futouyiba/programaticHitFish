"""0.3.4.0-B fixed Bake template prototype.

B-current runtime contract only. The module intentionally exposes no author-editable
DSL or per-subject program picker. Static authoring resolves to a fish-side subject
and a pond-side opportunity seed; environment evaluation consumes those two objects
plus one canonical ConditionGroup.

Runtime responsibility split (W6 task packet 3.4):

    Component Evaluator -> FactorFit + optional CORE Gate evidence
    AFLA                -> CORE / SECONDARY aggregate -> RawEnvCoeff
    Orchestration       -> Gate consequence / Background Floor / Base multiply

`aggregate_afla()` deliberately receives only component evaluations: no condition
fact, no Gate consequence, no Base opportunity.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any, Mapping, Sequence


FIXED_BAKE_TEMPLATE_PROGRAM_ID = "FCF_BAKE_TEMPLATE_V1"
BAKE_ALGORITHM_CONTRACT_VERSION = "AFLA_R2_1"

SOFT_FACTOR_MIN = 0.05
SOFT_FACTOR_MAX = 1.0
CORE_SUBOPTIMAL_FIT = 0.60
SECONDARY_LOSS_SCALE = 1.0 / 6.0
SECONDARY_LOSS_BUDGET = 0.5 * (-math.log(CORE_SUBOPTIMAL_FIT))
ENV_COEFF_MIN_MAX = 0.30

AGGREGATION_ROLES = frozenset({"CORE", "SECONDARY", "EXCLUDED"})
LEGACY_AGGREGATION_ROLE_ALIASES = {"OFF": "EXCLUDED"}
GATE_FAILURE_CAPS = {
    "NONE": None,
    "HARD_EXCLUDE": 0.00,
    "TRACE_RESIDUAL": 0.01,
    "LOW_RESIDUAL": 0.05,
}


class BakeConfigError(ValueError):
    pass


@dataclass(frozen=True)
class ConditionGroup:
    condition_group_id: str
    structure_type: str
    water_temperature_range: tuple[float, float]
    feeding_ecology_layers: tuple[str, ...]
    time_period: str


@dataclass(frozen=True)
class BakeEvaluationResult:
    env_coeff: float
    spatial_opportunity_intensity: float
    trace: Mapping[str, Any]


# --------------------------------------------------------------------------- #
# AggregationRole / Gate legality
# --------------------------------------------------------------------------- #


def _validate_role_gate(role: str, gate_policy: str) -> None:
    if role not in AGGREGATION_ROLES:
        raise BakeConfigError(f"invalid AggregationRole: {role}")
    if gate_policy not in GATE_FAILURE_CAPS:
        raise BakeConfigError(f"invalid GatePolicy: {gate_policy}")
    if role != "CORE" and gate_policy != "NONE":
        raise BakeConfigError("GatePolicy must be NONE/absent unless AggregationRole=CORE")


def migrate_legacy_binding(binding: Mapping[str, Any]) -> Mapping[str, str]:
    """Normalize legacy ConditionRole into current AggregationRole.

    OFF + NONE is losslessly equivalent to EXCLUDED + NONE. Legacy OFF with an
    active Gate is *not* losslessly representable under the current contract:
    EXCLUDED + Gate is illegal, and silently promoting it to CORE + Gate would
    buy unspecified Core aggregate participation. It therefore requires an
    explicit content decision instead of adapter guesswork.
    """
    if "aggregationRole" in binding:
        role = str(binding["aggregationRole"])
    elif "conditionRole" in binding:
        role = str(binding["conditionRole"])
    else:
        raise BakeConfigError("missing AggregationRole")

    gate_policy = str(binding.get("gatePolicy", "NONE"))
    if role in LEGACY_AGGREGATION_ROLE_ALIASES:
        if gate_policy != "NONE":
            raise BakeConfigError(
                "legacy OFF + non-NONE GatePolicy requires explicit content migration: "
                "do not auto-map to EXCLUDED or CORE"
            )
        role = LEGACY_AGGREGATION_ROLE_ALIASES[role]

    _validate_role_gate(role, gate_policy)
    return {"aggregationRole": role, "gatePolicy": gate_policy}


def migrate_legacy_bindings(
    bindings: Mapping[str, Mapping[str, Any]]
) -> Mapping[str, Mapping[str, str]]:
    return {key: migrate_legacy_binding(value) for key, value in bindings.items()}


@dataclass(frozen=True)
class RoleTransition:
    """Authoring-layer outcome of a Draft AggregationRole change."""

    binding: Mapping[str, str]
    cleared_gate_policy: str | None
    notice: str | None


def normalize_role_transition(
    previous_binding: Mapping[str, Any], new_role: str
) -> RoleTransition:
    """Authoring-layer Draft normalization for an AggregationRole change.

    Leaving CORE clears GatePolicy in the Draft instead of keeping an invisible
    shadow Gate; returning to CORE starts from GatePolicy=NONE so the author has
    to re-enable the Gate explicitly. This is a Draft/authoring concern, not a
    runtime definition: the runtime only ever sees legal resolved bindings.
    """
    if new_role not in AGGREGATION_ROLES:
        raise BakeConfigError(f"invalid AggregationRole: {new_role}")
    previous_role = str(
        previous_binding.get("aggregationRole", previous_binding.get("conditionRole", ""))
    )
    previous_gate = str(previous_binding.get("gatePolicy", "NONE"))

    if new_role != "CORE":
        gate_policy = "NONE"
    elif previous_role == "CORE":
        gate_policy = previous_gate
    else:
        gate_policy = "NONE"

    _validate_role_gate(new_role, gate_policy)
    cleared = previous_gate if (new_role != "CORE" and previous_gate != "NONE") else None
    notice = (
        f"AggregationRole={new_role} is not CORE; GatePolicy {previous_gate} cleared to NONE"
        if cleared
        else None
    )
    return RoleTransition({"aggregationRole": new_role, "gatePolicy": gate_policy}, cleared, notice)


# --------------------------------------------------------------------------- #
# Profile-owner validation (independent of this Surface's AggregationRole)
# --------------------------------------------------------------------------- #


def _clamp_computed_soft_fit(value: float) -> float:
    if not math.isfinite(value):
        raise BakeConfigError("computed factor fit is not finite")
    return min(SOFT_FACTOR_MAX, max(SOFT_FACTOR_MIN, value))


def _authored_affinity(value: Any, label: str) -> float:
    result = float(value)
    if not math.isfinite(result) or not (SOFT_FACTOR_MIN <= result <= SOFT_FACTOR_MAX):
        raise BakeConfigError(
            f"{label} authored affinity must be within [{SOFT_FACTOR_MIN}, {SOFT_FACTOR_MAX}]"
        )
    return result


def _temperature_params(profile: Mapping[str, Any]) -> tuple[float, float, float, float, str]:
    accept_min = float(profile["acceptMin"])
    preferred_min = float(profile["preferredMin"])
    preferred_max = float(profile["preferredMax"])
    accept_max = float(profile["acceptMax"])
    shape = str(profile.get("falloffShape", "LINEAR")).upper()
    if not all(math.isfinite(x) for x in (accept_min, preferred_min, preferred_max, accept_max)):
        raise BakeConfigError("temperature boundaries must be finite")
    if not (accept_min <= preferred_min <= preferred_max <= accept_max):
        raise BakeConfigError("invalid temperature boundaries")
    if shape not in {"LINEAR", "SMOOTHSTEP"}:
        raise BakeConfigError(f"unsupported temperature falloffShape: {shape}")
    return accept_min, preferred_min, preferred_max, accept_max, shape


def validate_component_profiles(components: Mapping[str, Any]) -> None:
    """Profile-owner schema / range validation.

    Runs for every authored profile regardless of this Surface's AggregationRole.
    EXCLUDED only means "Spatial Opportunity does not consume this condition"; it
    must not let an already-authored illegal profile go unchecked until the role
    is switched back to CORE.
    """
    temperature = components.get("temperature")
    if temperature is not None:
        _temperature_params(temperature)
    for section_key, label in (
        ("structure", "STRUCTURE"),
        ("feedingLayer", "FEEDING_LAYER"),
        ("timePeriod", "TIME_PERIOD"),
    ):
        section = components.get(section_key)
        if section is None:
            continue
        for name, value in section.get("affinity", {}).items():
            _authored_affinity(value, f"{label}/{name}")


# --------------------------------------------------------------------------- #
# Temperature point fit
# --------------------------------------------------------------------------- #


def _falloff_value(x: float, shape: str) -> float:
    x = min(1.0, max(0.0, x))
    if shape == "LINEAR":
        return x
    return x * x * (3.0 - 2.0 * x)


def _point_temperature_fit(t: float, profile: Mapping[str, Any]) -> float:
    accept_min, preferred_min, preferred_max, accept_max, shape = _temperature_params(profile)
    if t <= accept_min or t >= accept_max:
        return 0.0
    if preferred_min <= t <= preferred_max:
        return 1.0
    if t < preferred_min:
        width = preferred_min - accept_min
        x = 1.0 if width == 0 else (t - accept_min) / width
    else:
        width = accept_max - preferred_max
        x = 1.0 if width == 0 else (accept_max - t) / width
    return _falloff_value(x, shape)


def _representative_temperature(temp_range: Sequence[Any]) -> tuple[float, float, float]:
    if not isinstance(temp_range, (list, tuple)) or len(temp_range) != 2:
        raise BakeConfigError("TEMPERATURE requires waterTemperatureRange [min,max]")
    t_min, t_max = float(temp_range[0]), float(temp_range[1])
    if not math.isfinite(t_min) or not math.isfinite(t_max):
        raise BakeConfigError("temperature range must be finite")
    if t_min > t_max:
        raise BakeConfigError("temperature range min > max")
    return t_min, t_max, (t_min + t_max) / 2.0


# --------------------------------------------------------------------------- #
# Component Evaluator -> FactorFit + optional CORE Gate evidence
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ComponentEvaluation:
    condition_key: str
    aggregation_role: str
    raw_inputs: Mapping[str, Any]
    raw_fit: float
    applied_fit: float
    loss: float
    gate_result: Mapping[str, Any] | None


def evaluate_component(
    condition_key: str,
    *,
    aggregation_role: str,
    gate_policy: str,
    components: Mapping[str, Any],
    condition_group: ConditionGroup,
    gate_capable: Sequence[str],
) -> ComponentEvaluation | None:
    """Evaluate one condition slot, or return None when EXCLUDED.

    The evaluator owns the FactorFit and any Gate evidence for this condition.
    It does not aggregate, cap, floor or multiply the Base opportunity.
    """
    if aggregation_role == "EXCLUDED":
        return None
    if gate_policy != "NONE" and condition_key not in gate_capable:
        raise BakeConfigError(f"GatePolicy unsupported for {condition_key}")

    is_computed_continuous_fit = False
    gate_passed = True

    if condition_key == "TEMPERATURE":
        profile = components.get("temperature")
        if profile is None:
            raise BakeConfigError("active TEMPERATURE missing profile")
        t_min, t_max, representative = _representative_temperature(
            condition_group.water_temperature_range
        )
        raw_fit = _point_temperature_fit(representative, profile)
        raw_inputs = {
            "waterTemperatureRange": [t_min, t_max],
            "representativeTemp": representative,
        }
        is_computed_continuous_fit = True
        if gate_policy != "NONE":
            threshold = float(profile["tempThreshold"])
            if not math.isfinite(threshold) or not (0.0 <= threshold <= 1.0):
                raise BakeConfigError("tempThreshold must be within [0,1]")
            gate_passed = raw_fit >= threshold

    elif condition_key == "STRUCTURE":
        profile = components.get("structure", {}).get("affinity", {})
        structure_type = condition_group.structure_type
        if not profile or structure_type not in profile:
            raise BakeConfigError(f"STRUCTURE missing affinity for {structure_type}")
        raw_fit = _authored_affinity(profile[structure_type], f"STRUCTURE/{structure_type}")
        raw_inputs = {"structureType": structure_type}

    elif condition_key == "FEEDING_LAYER":
        profile = components.get("feedingLayer", {}).get("affinity", {})
        layers = tuple(condition_group.feeding_ecology_layers)
        if not layers:
            raise BakeConfigError("FEEDING_LAYER requires at least one FeedingEcologyLayer")
        missing = [layer for layer in layers if layer not in profile]
        if not profile or missing:
            raise BakeConfigError(f"FEEDING_LAYER missing affinity for {missing or layers}")
        layer_fits = {
            layer: _authored_affinity(profile[layer], f"FEEDING_LAYER/{layer}") for layer in layers
        }
        raw_fit = max(layer_fits.values())
        raw_inputs = {"feedingEcologyLayers": list(layers), "layerFits": layer_fits}

    elif condition_key == "TIME_PERIOD":
        profile = components.get("timePeriod", {}).get("affinity", {})
        period = condition_group.time_period
        if not profile or period not in profile:
            raise BakeConfigError(f"TIME_PERIOD missing affinity for {period}")
        raw_fit = _authored_affinity(profile[period], f"TIME_PERIOD/{period}")
        raw_inputs = {"timePeriod": period}

    else:  # pragma: no cover
        raise BakeConfigError(f"unknown condition slot: {condition_key}")

    applied_fit = _clamp_computed_soft_fit(raw_fit) if is_computed_continuous_fit else raw_fit

    gate_result = None
    if gate_policy != "NONE":
        gate_result = {
            "conditionKey": condition_key,
            "policy": gate_policy,
            "passed": gate_passed,
            "failureCap": GATE_FAILURE_CAPS[gate_policy],
        }

    return ComponentEvaluation(
        condition_key=condition_key,
        aggregation_role=aggregation_role,
        raw_inputs=raw_inputs,
        raw_fit=raw_fit,
        applied_fit=applied_fit,
        loss=-math.log(applied_fit),
        gate_result=gate_result,
    )


# --------------------------------------------------------------------------- #
# AFLA -> CORE / SECONDARY aggregate -> RawEnvCoeff
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class AflaAggregate:
    core_loss: float
    secondary_loss_raw: float
    secondary_loss_applied: float
    raw_env_coeff: float


def aggregate_afla(evaluations: Sequence[ComponentEvaluation]) -> AflaAggregate:
    """AFLA owns CORE / SECONDARY aggregation only.

    It takes no Base opportunity, no Gate consequence and no Background Floor:
    those are orchestration responsibilities and must not leak in here.
    """
    core_loss = 0.0
    secondary_loss_unscaled = 0.0
    for evaluation in evaluations:
        if evaluation.aggregation_role == "CORE":
            core_loss += evaluation.loss
        elif evaluation.aggregation_role == "SECONDARY":
            secondary_loss_unscaled += evaluation.loss

    secondary_loss_raw = SECONDARY_LOSS_SCALE * secondary_loss_unscaled
    secondary_loss_applied = min(secondary_loss_raw, SECONDARY_LOSS_BUDGET)
    raw_env_coeff = math.exp(-(core_loss + secondary_loss_applied))
    return AflaAggregate(core_loss, secondary_loss_raw, secondary_loss_applied, raw_env_coeff)


# --------------------------------------------------------------------------- #
# Orchestration -> Gate consequence / Background Floor / Base multiply
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class OrchestrationOutcome:
    gate_failure_cap: float | None
    background_floor_applied: bool
    final_env_coeff: float
    spatial_opportunity_intensity: float


def apply_orchestration(
    aggregate: AflaAggregate,
    evaluations: Sequence[ComponentEvaluation],
    *,
    base_opportunity_intensity: float,
    is_background_fish: bool,
    env_coeff_min: float | None,
) -> OrchestrationOutcome:
    """Gate failure cap-down only; the Background Floor can never resurrect it."""
    failed_caps = [
        float(evaluation.gate_result["failureCap"])
        for evaluation in evaluations
        if evaluation.gate_result is not None and not evaluation.gate_result["passed"]
    ]
    gate_failure_cap = min(failed_caps) if failed_caps else None

    floor_applied = False
    if gate_failure_cap is not None:
        final_env_coeff = min(aggregate.raw_env_coeff, gate_failure_cap)
    elif is_background_fish:
        if env_coeff_min is None:
            raise BakeConfigError("isBackgroundFish=true requires an explicit envCoeffMin floor")
        final_env_coeff = max(aggregate.raw_env_coeff, float(env_coeff_min))
        floor_applied = final_env_coeff > aggregate.raw_env_coeff
    else:
        final_env_coeff = aggregate.raw_env_coeff

    return OrchestrationOutcome(
        gate_failure_cap=gate_failure_cap,
        background_floor_applied=floor_applied,
        final_env_coeff=final_env_coeff,
        spatial_opportunity_intensity=base_opportunity_intensity * final_env_coeff,
    )


# --------------------------------------------------------------------------- #
# Resolved DTO validation
# --------------------------------------------------------------------------- #


def _require_quality_ref(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise BakeConfigError(f"{label} fishQualityRef must be a mapping")
    if not value.get("fishQualityId"):
        raise BakeConfigError(f"{label} fishQualityRef missing fishQualityId")
    return value


def validate_opportunity_seed(seed: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the Pond×Quality opportunity seed, including the explicit switch."""
    if any(key in seed for key in ("resolvedComponentProfiles", "resolvedSpatialOpportunityBindings")):
        raise BakeConfigError("ResolvedOpportunitySeed must not contain fish-side profile/binding truth")
    if not seed.get("fishPondRef"):
        raise BakeConfigError("ResolvedOpportunitySeed missing fishPondRef")
    _require_quality_ref(seed.get("fishQualityRef"), "seed")

    base = float(seed["baseOpportunityIntensity"])
    if not math.isfinite(base) or base < 0:
        raise BakeConfigError("invalid BaseOpportunityIntensity")

    if "isBackgroundFish" not in seed:
        raise BakeConfigError("ResolvedOpportunitySeed missing isBackgroundFish")
    is_background_fish = seed["isBackgroundFish"]
    if not isinstance(is_background_fish, bool):
        raise BakeConfigError("isBackgroundFish must be a boolean")

    env_coeff_min = seed.get("envCoeffMin")
    if env_coeff_min is not None:
        env_coeff_min = float(env_coeff_min)
        if not math.isfinite(env_coeff_min):
            raise BakeConfigError("invalid envCoeffMin")

    if not is_background_fish:
        if env_coeff_min not in (None, 0.0):
            raise BakeConfigError(
                "envCoeffMin must be 0/absent/disabled unless isBackgroundFish=true"
            )
        env_coeff_min = None
    else:
        if env_coeff_min is None:
            raise BakeConfigError("isBackgroundFish=true requires an explicit envCoeffMin floor")
        if not (0.0 < env_coeff_min <= ENV_COEFF_MIN_MAX):
            raise BakeConfigError("invalid envCoeffMin")

    resolved: dict[str, Any] = {
        "fishPondRef": seed["fishPondRef"],
        "fishQualityRef": dict(seed["fishQualityRef"]),
        "baseOpportunityIntensity": base,
        "isBackgroundFish": is_background_fish,
    }
    if env_coeff_min is not None:
        resolved["envCoeffMin"] = env_coeff_min
    return resolved


def validate_spatial_opportunity_subject(subject: Mapping[str, Any]) -> Mapping[str, Any]:
    if any(
        key in subject
        for key in ("fishPondRef", "baseOpportunityIntensity", "backgroundPolicy", "isBackgroundFish")
    ):
        raise BakeConfigError(
            "ResolvedSpatialOpportunitySubject must not contain Pond-owned opportunity truth"
        )
    _require_quality_ref(subject.get("fishQualityRef"), "subject")
    return subject


# --------------------------------------------------------------------------- #
# Fixed template program
# --------------------------------------------------------------------------- #


class FixedBakeTemplateProgram:
    """System-owned fixed topology for the 0.3.4.0-B vertical slice."""

    condition_slots = ("TEMPERATURE", "STRUCTURE", "FEEDING_LAYER", "TIME_PERIOD")
    gate_capable = frozenset({"TEMPERATURE"})

    def evaluate(
        self,
        resolved_subject: Mapping[str, Any],
        resolved_seed: Mapping[str, Any],
        condition_group: ConditionGroup,
    ) -> BakeEvaluationResult:
        validate_spatial_opportunity_subject(resolved_subject)
        seed = validate_opportunity_seed(resolved_seed)

        subject_quality = dict(resolved_subject["fishQualityRef"])
        if subject_quality != seed["fishQualityRef"]:
            raise BakeConfigError("subject/seed fishQualityRef mismatch")

        components = resolved_subject.get("resolvedComponentProfiles", {})
        validate_component_profiles(components)

        bindings = resolved_subject.get("resolvedSpatialOpportunityBindings", {})
        unknown_conditions = set(bindings) - set(self.condition_slots)
        if unknown_conditions:
            raise BakeConfigError(f"unknown fixed-template condition(s): {sorted(unknown_conditions)}")

        evaluations: list[ComponentEvaluation] = []
        excluded_conditions: list[str] = []
        for condition_key in self.condition_slots:
            if condition_key not in bindings:
                raise BakeConfigError(f"missing AggregationRole/GatePolicy: {condition_key}")
            binding = bindings[condition_key]
            if "conditionRole" in binding:
                raise BakeConfigError(
                    "legacy ConditionRole must be migrated before B-current evaluation"
                )
            role = str(binding.get("aggregationRole", ""))
            gate_policy = str(binding.get("gatePolicy", "NONE"))
            _validate_role_gate(role, gate_policy)
            evaluation = evaluate_component(
                condition_key,
                aggregation_role=role,
                gate_policy=gate_policy,
                components=components,
                condition_group=condition_group,
                gate_capable=self.gate_capable,
            )
            if evaluation is not None:
                evaluations.append(evaluation)
            else:
                excluded_conditions.append(condition_key)

        aggregate = aggregate_afla(evaluations)
        outcome = apply_orchestration(
            aggregate,
            evaluations,
            base_opportunity_intensity=seed["baseOpportunityIntensity"],
            is_background_fish=seed["isBackgroundFish"],
            env_coeff_min=seed.get("envCoeffMin"),
        )

        trace = {
            "programId": FIXED_BAKE_TEMPLATE_PROGRAM_ID,
            "algorithmContractVersion": BAKE_ALGORITHM_CONTRACT_VERSION,
            "fishQualityRef": subject_quality,
            "fishPondRef": seed["fishPondRef"],
            "conditionGroupId": condition_group.condition_group_id,
            "baseOpportunityIntensity": seed["baseOpportunityIntensity"],
            "isBackgroundFish": seed["isBackgroundFish"],
            "envCoeffMin": seed.get("envCoeffMin"),
            "excludedConditions": tuple(excluded_conditions),
            "gateResults": tuple(
                evaluation.gate_result
                for evaluation in evaluations
                if evaluation.gate_result is not None
            ),
            "factorResults": tuple(
                {
                    "conditionKey": evaluation.condition_key,
                    "aggregationRole": evaluation.aggregation_role,
                    "rawInputs": dict(evaluation.raw_inputs),
                    "rawFit": evaluation.raw_fit,
                    "appliedFit": evaluation.applied_fit,
                    "loss": evaluation.loss,
                }
                for evaluation in evaluations
            ),
            "coreLoss": aggregate.core_loss,
            "secondaryLossRaw": aggregate.secondary_loss_raw,
            "secondaryLossApplied": aggregate.secondary_loss_applied,
            "rawEnvCoeff": aggregate.raw_env_coeff,
            "gateFailureCap": outcome.gate_failure_cap,
            "backgroundFloorApplied": outcome.background_floor_applied,
            "finalEnvCoeff": outcome.final_env_coeff,
            "spatialOpportunityIntensity": outcome.spatial_opportunity_intensity,
        }
        return BakeEvaluationResult(
            outcome.final_env_coeff, outcome.spatial_opportunity_intensity, trace
        )
