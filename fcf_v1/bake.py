"""0.3.4.0-B fixed Bake template prototype.

This module intentionally does not expose a DSL or per-subject program picker.
The execution topology is system-owned; authoring only supplies component
profiles, ConditionRole switches, and finite GatePolicy values.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any, Mapping


FIXED_BAKE_TEMPLATE_PROGRAM_ID = "FCF_BAKE_TEMPLATE_V1"
BAKE_ALGORITHM_CONTRACT_VERSION = "AFLA_R2_1"

SOFT_FACTOR_MIN = 0.05
SOFT_FACTOR_MAX = 1.0
CORE_SUBOPTIMAL_FIT = 0.60
SECONDARY_LOSS_SCALE = 1.0 / 6.0
SECONDARY_LOSS_BUDGET = 0.5 * (-math.log(CORE_SUBOPTIMAL_FIT))

CONDITION_ROLES = frozenset({"CORE", "SECONDARY", "OFF"})
GATE_FAILURE_CAPS = {
    "NONE": None,
    "HARD_EXCLUDE": 0.00,
    "TRACE_RESIDUAL": 0.01,
    "LOW_RESIDUAL": 0.05,
}


class BakeConfigError(ValueError):
    pass


@dataclass(frozen=True)
class ConditionGroupSnapshot:
    condition_group_id: str
    semantic_support_ref: str
    facts: Mapping[str, Any]


@dataclass(frozen=True)
class BakeEvaluationResult:
    env_coeff: float
    spatial_opportunity_intensity: float
    trace: Mapping[str, Any]


def _clamp_soft_fit(value: float) -> float:
    if math.isnan(value):
        raise BakeConfigError("factor fit is NaN")
    return min(SOFT_FACTOR_MAX, max(SOFT_FACTOR_MIN, value))


def _validate_role(role: str) -> None:
    if role not in CONDITION_ROLES:
        raise BakeConfigError(f"invalid ConditionRole: {role}")


def _validate_gate_policy(policy: str) -> None:
    if policy not in GATE_FAILURE_CAPS:
        raise BakeConfigError(f"invalid GatePolicy: {policy}")


def _point_temperature_fit(t: float, profile: Mapping[str, Any]) -> float:
    accept_min = float(profile["acceptMin"])
    preferred_min = float(profile["preferredMin"])
    preferred_max = float(profile["preferredMax"])
    accept_max = float(profile["acceptMax"])
    shape = str(profile.get("falloffShape", "LINEAR")).upper()

    if not (accept_min <= preferred_min <= preferred_max <= accept_max):
        raise BakeConfigError("invalid temperature boundaries")
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

    x = min(1.0, max(0.0, x))
    if shape == "LINEAR":
        return x
    if shape == "SMOOTHSTEP":
        return x * x * (3.0 - 2.0 * x)
    raise BakeConfigError(f"unsupported temperature falloffShape: {shape}")


def _temperature_interval_fit(
    t_min: float,
    t_max: float,
    profile: Mapping[str, Any],
    samples: int = 257,
) -> tuple[float, float]:
    """Return (mean_fit, max_fit) for a temperature interval.

    R0 has only interval endpoints, so the interval is treated as uniformly
    distributed. A deterministic grid keeps this prototype dependency-free;
    point intervals reduce exactly to point evaluation.
    """
    if t_min > t_max:
        raise BakeConfigError("temperature range min > max")
    if t_min == t_max:
        point = _point_temperature_fit(t_min, profile)
        return point, point
    if samples < 3:
        raise BakeConfigError("temperature integration samples must be >= 3")

    step = (t_max - t_min) / (samples - 1)
    values = [_point_temperature_fit(t_min + i * step, profile) for i in range(samples)]
    # Trapezoidal mean over a uniform interval.
    mean_fit = (0.5 * values[0] + sum(values[1:-1]) + 0.5 * values[-1]) / (samples - 1)
    return mean_fit, max(values)


class FixedBakeTemplateProgram:
    """System-owned fixed topology for the 0.3.4.0-B vertical slice."""

    condition_slots = ("TEMPERATURE", "STRUCTURE", "FEEDING_LAYER", "TIME_PERIOD")
    gate_capable = frozenset({"TEMPERATURE"})

    def evaluate(
        self,
        resolved_subject: Mapping[str, Any],
        snapshot: ConditionGroupSnapshot,
    ) -> BakeEvaluationResult:
        if resolved_subject.get("bakeTemplateProgramId") != FIXED_BAKE_TEMPLATE_PROGRAM_ID:
            raise BakeConfigError("unexpected fixed Bake template program id")
        if resolved_subject.get("bakeAlgorithmContractVersion") != BAKE_ALGORITHM_CONTRACT_VERSION:
            raise BakeConfigError("unexpected Bake algorithm contract version")

        base = float(resolved_subject["baseOpportunityIntensity"])
        if math.isnan(base) or base < 0:
            raise BakeConfigError("invalid BaseOpportunityIntensity")

        bindings = resolved_subject.get("conditionBindings", {})
        components = resolved_subject.get("components", {})
        gate_results = []
        factor_results = []
        failed_caps = []
        core_loss = 0.0
        secondary_loss_unscaled = 0.0

        for condition_key in self.condition_slots:
            if condition_key not in bindings:
                raise BakeConfigError(f"missing ConditionRole/GatePolicy: {condition_key}")
            binding = bindings[condition_key]
            role = str(binding["conditionRole"])
            gate_policy = str(binding.get("gatePolicy", "NONE"))
            _validate_role(role)
            _validate_gate_policy(gate_policy)
            if gate_policy != "NONE" and condition_key not in self.gate_capable:
                raise BakeConfigError(f"GatePolicy unsupported for {condition_key}")

            needs_factor = role != "OFF"
            needs_gate = gate_policy != "NONE"
            if not needs_factor and not needs_gate:
                continue

            raw_fit: float
            gate_passed = True
            raw_inputs: Mapping[str, Any]

            if condition_key == "TEMPERATURE":
                profile = components.get("temperature")
                if profile is None:
                    raise BakeConfigError("active TEMPERATURE missing profile")
                temp_range = snapshot.facts.get("waterTemperatureRange")
                if not isinstance(temp_range, (list, tuple)) or len(temp_range) != 2:
                    raise BakeConfigError("TEMPERATURE requires waterTemperatureRange [min,max]")
                t_min, t_max = float(temp_range[0]), float(temp_range[1])
                raw_fit, max_fit = _temperature_interval_fit(t_min, t_max, profile)
                raw_inputs = {"waterTemperatureRange": [t_min, t_max], "maxFit": max_fit}
                if needs_gate:
                    threshold = float(profile["tempThreshold"])
                    gate_passed = max_fit >= threshold

            elif condition_key == "STRUCTURE":
                profile = components.get("structure", {}).get("affinity", {})
                structure_type = snapshot.facts.get("structureType")
                if not profile or structure_type not in profile:
                    raise BakeConfigError(f"STRUCTURE missing affinity for {structure_type}")
                raw_fit = float(profile[structure_type])
                raw_inputs = {"structureType": structure_type}

            elif condition_key == "FEEDING_LAYER":
                profile = components.get("feedingLayer", {}).get("affinity", {})
                layer = snapshot.facts.get("feedingEcologyLayer")
                if not profile or layer not in profile:
                    raise BakeConfigError(f"FEEDING_LAYER missing affinity for {layer}")
                raw_fit = float(profile[layer])
                raw_inputs = {"feedingEcologyLayer": layer}

            elif condition_key == "TIME_PERIOD":
                profile = components.get("timePeriod", {}).get("affinity", {})
                period = snapshot.facts.get("timePeriod")
                if not profile or period not in profile:
                    raise BakeConfigError(f"TIME_PERIOD missing affinity for {period}")
                raw_fit = float(profile[period])
                raw_inputs = {"timePeriod": period}

            else:  # pragma: no cover - condition_slots is fixed above.
                raise BakeConfigError(f"unknown condition slot: {condition_key}")

            if needs_gate:
                cap = GATE_FAILURE_CAPS[gate_policy]
                gate_results.append(
                    {
                        "conditionKey": condition_key,
                        "policy": gate_policy,
                        "passed": gate_passed,
                        "failureCap": cap,
                    }
                )
                if not gate_passed:
                    failed_caps.append(float(cap))

            if needs_factor:
                applied_fit = _clamp_soft_fit(raw_fit)
                loss = -math.log(applied_fit)
                factor_results.append(
                    {
                        "conditionKey": condition_key,
                        "conditionRole": role,
                        "rawInputs": dict(raw_inputs),
                        "rawFit": raw_fit,
                        "appliedFit": applied_fit,
                        "loss": loss,
                    }
                )
                if role == "CORE":
                    core_loss += loss
                elif role == "SECONDARY":
                    secondary_loss_unscaled += loss

        secondary_loss_raw = SECONDARY_LOSS_SCALE * secondary_loss_unscaled
        secondary_loss_applied = min(secondary_loss_raw, SECONDARY_LOSS_BUDGET)
        raw_env_coeff = math.exp(-(core_loss + secondary_loss_applied))

        gate_failure_cap = min(failed_caps) if failed_caps else None
        background_policy = resolved_subject.get("backgroundPolicy", {"enabled": False})
        floor_applied = False

        if gate_failure_cap is not None:
            final_env_coeff = min(raw_env_coeff, gate_failure_cap)
        elif bool(background_policy.get("enabled", False)):
            floor = float(background_policy["envCoeffMin"])
            if not (0.0 < floor <= 0.30):
                raise BakeConfigError("invalid envCoeffMin")
            final_env_coeff = max(raw_env_coeff, floor)
            floor_applied = final_env_coeff > raw_env_coeff
        else:
            final_env_coeff = raw_env_coeff

        intensity = base * final_env_coeff
        trace = {
            "programId": FIXED_BAKE_TEMPLATE_PROGRAM_ID,
            "algorithmContractVersion": BAKE_ALGORITHM_CONTRACT_VERSION,
            "subjectIdentity": resolved_subject.get("identity", {}),
            "conditionGroupId": snapshot.condition_group_id,
            "baseOpportunityIntensity": base,
            "gateResults": tuple(gate_results),
            "factorResults": tuple(factor_results),
            "coreLoss": core_loss,
            "secondaryLossRaw": secondary_loss_raw,
            "secondaryLossApplied": secondary_loss_applied,
            "rawEnvCoeff": raw_env_coeff,
            "gateFailureCap": gate_failure_cap,
            "backgroundFloorApplied": floor_applied,
            "finalEnvCoeff": final_env_coeff,
            "spatialOpportunityIntensity": intensity,
        }
        return BakeEvaluationResult(final_env_coeff, intensity, trace)
