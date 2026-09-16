import json
from copy import deepcopy
from pathlib import Path

import pytest

from fcf_v1.bake import (
    BakeConfigError,
    ConditionGroupSnapshot,
    FixedBakeTemplateProgram,
)


SUBJECT = json.loads(Path("authoring/bass_fixed_template_v0.json").read_text())
GROUP_FIXTURE = json.loads(
    Path("tests/fixtures/bass_fixed_template_condition_groups_v0.json").read_text()
)
PROGRAM = FixedBakeTemplateProgram()


def _snapshot(row):
    return ConditionGroupSnapshot(
        condition_group_id=row["id"],
        semantic_support_ref=row["semanticSupportRef"],
        facts=row["facts"],
    )


def _point_snapshot(temp, structure="OPEN", layer="SURFACE", period="MORNING", cid="TEST"):
    return ConditionGroupSnapshot(
        condition_group_id=cid,
        semantic_support_ref=f"{structure}_TEST",
        facts={
            "structureType": structure,
            "waterTemperatureRange": [float(temp), float(temp)],
            "feedingEcologyLayer": layer,
            "timePeriod": period,
        },
    )


def test_bass_q3_golden_condition_groups():
    rows = GROUP_FIXTURE["condition_groups"]
    results = []
    for row in rows:
        result = PROGRAM.evaluate(SUBJECT, _snapshot(row))
        assert result.env_coeff == pytest.approx(row["expectedFinalEnvCoeff"], abs=1e-12)
        assert result.spatial_opportunity_intensity == pytest.approx(
            row["expectedFinalEnvCoeff"], abs=1e-12
        )
        results.append(result.env_coeff)

    assert results[0] > results[1] > results[2]


def test_off_time_period_does_not_require_a_fake_profile():
    assert "timePeriod" not in SUBJECT["components"]
    result = PROGRAM.evaluate(SUBJECT, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))
    assert result.env_coeff == pytest.approx(1.0)
    assert not any(x["conditionKey"] == "TIME_PERIOD" for x in result.trace["factorResults"])


def test_gate_failure_cap_never_raises_a_worse_raw_result():
    subject = deepcopy(SUBJECT)
    subject["conditionBindings"]["TEMPERATURE"]["gatePolicy"] = "LOW_RESIDUAL"

    result = PROGRAM.evaluate(subject, _point_snapshot(36, "OPEN", "SURFACE", cid="GATE"))

    assert result.trace["gateFailureCap"] == pytest.approx(0.05)
    assert result.trace["rawEnvCoeff"] == pytest.approx(0.013775788532526681)
    assert result.env_coeff == pytest.approx(result.trace["rawEnvCoeff"])
    assert result.env_coeff < 0.05


def test_background_floor_only_applies_on_gate_pass_path():
    subject = deepcopy(SUBJECT)
    subject["backgroundPolicy"] = {"enabled": True, "envCoeffMin": 0.10}

    normal = PROGRAM.evaluate(subject, _point_snapshot(5, "OPEN", "SURFACE", cid="FLOOR"))
    assert normal.trace["rawEnvCoeff"] == pytest.approx(0.037570332361436386)
    assert normal.env_coeff == pytest.approx(0.10)
    assert normal.trace["backgroundFloorApplied"] is True

    subject["conditionBindings"]["TEMPERATURE"]["gatePolicy"] = "TRACE_RESIDUAL"
    failed = PROGRAM.evaluate(subject, _point_snapshot(36, "OPEN", "SURFACE", cid="FLOOR_GATE"))
    assert failed.trace["gateFailureCap"] == pytest.approx(0.01)
    assert failed.env_coeff <= 0.01
    assert failed.trace["backgroundFloorApplied"] is False


def test_base_zero_stays_zero_even_with_background_floor():
    subject = deepcopy(SUBJECT)
    subject["baseOpportunityIntensity"] = 0.0
    subject["backgroundPolicy"] = {"enabled": True, "envCoeffMin": 0.10}
    result = PROGRAM.evaluate(subject, _point_snapshot(5, "OPEN", "SURFACE"))
    assert result.spatial_opportunity_intensity == 0.0


def test_missing_condition_role_is_not_silently_off():
    subject = deepcopy(SUBJECT)
    del subject["conditionBindings"]["TIME_PERIOD"]
    with pytest.raises(BakeConfigError, match="missing ConditionRole/GatePolicy: TIME_PERIOD"):
        PROGRAM.evaluate(subject, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))


def test_active_condition_requires_its_profile():
    subject = deepcopy(SUBJECT)
    subject["conditionBindings"]["TIME_PERIOD"]["conditionRole"] = "CORE"
    with pytest.raises(BakeConfigError, match="TIME_PERIOD missing affinity"):
        PROGRAM.evaluate(subject, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))


def test_gate_policy_is_finite_and_component_capability_is_fixed():
    subject = deepcopy(SUBJECT)
    subject["conditionBindings"]["STRUCTURE"]["gatePolicy"] = "LOW_RESIDUAL"
    with pytest.raises(BakeConfigError, match="GatePolicy unsupported for STRUCTURE"):
        PROGRAM.evaluate(subject, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))

    subject = deepcopy(SUBJECT)
    subject["conditionBindings"]["TEMPERATURE"]["gatePolicy"] = "ARBITRARY_0_2"
    with pytest.raises(BakeConfigError, match="invalid GatePolicy"):
        PROGRAM.evaluate(subject, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))


def test_mapping_order_does_not_change_result():
    subject = deepcopy(SUBJECT)
    subject["conditionBindings"] = dict(reversed(list(subject["conditionBindings"].items())))
    subject["components"] = dict(reversed(list(subject["components"].items())))

    facts = {
        "timePeriod": "MORNING",
        "feedingEcologyLayer": "BOTTOM",
        "waterTemperatureRange": [15.0, 15.0],
        "structureType": "DROPOFF",
    }
    result = PROGRAM.evaluate(
        subject,
        ConditionGroupSnapshot("ORDER", "DROPOFF_01", facts),
    )
    assert result.env_coeff == pytest.approx(0.3256095471324488, abs=1e-12)


def test_worsening_a_core_factor_never_increases_env_coeff():
    preferred = PROGRAM.evaluate(SUBJECT, _point_snapshot(26, "GRASS_EDGE", "MIDDLE"))
    dropoff = PROGRAM.evaluate(SUBJECT, _point_snapshot(26, "DROPOFF", "MIDDLE"))
    open_water = PROGRAM.evaluate(SUBJECT, _point_snapshot(26, "OPEN", "MIDDLE"))
    assert preferred.env_coeff > dropoff.env_coeff > open_water.env_coeff
