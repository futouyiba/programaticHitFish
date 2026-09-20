from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "response_fixed_pan_calibration.py"
SPEC = importlib.util.spec_from_file_location("response_fixed_pan_calibration", MODULE_PATH)
assert SPEC and SPEC.loader
cal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cal
SPEC.loader.exec_module(cal)


def test_mapping_anchors_and_order():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    assert mapping.as_dict() == {
        "NONE": 0.0,
        "LOW": 0.25,
        "NORMAL": 0.50,
        "HIGH": 1.0,
    }
    with pytest.raises(cal.CalibrationInputError):
        cal.ResponseMapping(low=0.5, normal=0.5)
    with pytest.raises(cal.CalibrationInputError):
        cal.ResponseMapping(low=0.6, normal=0.5)
    with pytest.raises(cal.CalibrationInputError):
        cal.ResponseMapping(low=0.0, normal=0.5)
    with pytest.raises(cal.CalibrationInputError):
        cal.ResponseMapping(low=0.25, normal=1.0)


def test_fixed_pan_worked_example_high_target_vs_normal_other():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    result = cal.evaluate_fixed_pan(
        [
            cal.Candidate("TARGET", 40.0, "HIGH", True),
            cal.Candidate("OTHER", 30.0, "NORMAL", False),
        ],
        pan_scale=100.0,
        mapping=mapping,
    )
    assert result.fish_mass == pytest.approx(55.0)
    assert result.rho == pytest.approx(0.55)
    assert result.p_any_fish == pytest.approx(0.55)
    assert result.p_none == pytest.approx(0.45)
    assert result.target_purity_reference == pytest.approx(40.0 / 55.0)
    assert result.saturated is False


def test_fixed_pan_worked_example_low_target_changes_rate_and_purity():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    result = cal.evaluate_fixed_pan(
        [
            cal.Candidate("TARGET", 40.0, "LOW", True),
            cal.Candidate("OTHER", 30.0, "NORMAL", False),
        ],
        pan_scale=100.0,
        mapping=mapping,
    )
    assert result.fish_mass == pytest.approx(25.0)
    assert result.rho == pytest.approx(0.25)
    assert result.p_any_fish == pytest.approx(0.25)
    assert result.target_purity_reference == pytest.approx(0.40)


def test_saturation_clamps_any_fish_but_preserves_raw_rho_diagnostic():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    result = cal.evaluate_fixed_pan(
        [
            cal.Candidate("A", 90.0, "HIGH"),
            cal.Candidate("B", 70.0, "HIGH"),
        ],
        pan_scale=100.0,
        mapping=mapping,
    )
    assert result.fish_mass == pytest.approx(160.0)
    assert result.rho == pytest.approx(1.6)
    assert result.p_any_fish == pytest.approx(1.0)
    assert result.p_none == pytest.approx(0.0)
    assert result.saturated is True
    assert result.production_overflow_composition_verified is False


def test_uniform_normal_at_half_can_cross_out_of_saturation():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    result = cal.evaluate_fixed_pan(
        [
            cal.Candidate("A", 90.0, "NORMAL"),
            cal.Candidate("B", 70.0, "NORMAL"),
        ],
        pan_scale=100.0,
        mapping=mapping,
    )
    assert result.fish_mass == pytest.approx(80.0)
    assert result.rho == pytest.approx(0.8)
    assert result.p_any_fish == pytest.approx(0.8)
    assert result.saturated is False


def test_none_band_contributes_zero_without_creating_a_second_none_pool():
    mapping = cal.ResponseMapping(low=0.25, normal=0.50)
    result = cal.evaluate_fixed_pan(
        [
            cal.Candidate("RESPONDS", 50.0, "HIGH"),
            cal.Candidate("NO_RESPONSE", 1_000_000.0, "NONE"),
        ],
        pan_scale=100.0,
        mapping=mapping,
    )
    assert result.fish_mass == pytest.approx(50.0)
    assert result.p_any_fish == pytest.approx(0.5)
    by_id = {row.candidate_id: row for row in result.candidates}
    assert by_id["NO_RESPONSE"].selection_weight == 0.0


def test_expected_native_wait_uses_semantic_opportunity_interval_only():
    assert cal.expected_native_wait_seconds(5.0, 0.5) == pytest.approx(10.0)
    assert cal.expected_native_wait_seconds(5.0, 0.25) == pytest.approx(20.0)
    assert math.isinf(cal.expected_native_wait_seconds(5.0, 0.0))
    with pytest.raises(cal.CalibrationInputError):
        cal.expected_native_wait_seconds(0.0, 0.5)


def test_mapping_sweep_uses_fixed_pan_not_additive_pool():
    rows = cal.mapping_sweep_rows(
        normal_grid=(0.5,),
        low_grid=(0.25,),
        rho_high_grid=(0.5, 1.6),
    )
    assert len(rows) == 2
    by_rho = {row["rhoHigh"]: row for row in rows}

    half = by_rho[0.5]
    assert half["pAnyHigh"] == pytest.approx(0.5)
    assert half["pAnyNormal"] == pytest.approx(0.25)
    assert half["pAnyLow"] == pytest.approx(0.125)

    saturated = by_rho[1.6]
    assert saturated["pAnyHigh"] == pytest.approx(1.0)
    assert saturated["pAnyNormal"] == pytest.approx(0.8)
    assert saturated["pAnyLow"] == pytest.approx(0.4)


def test_loader_requires_explicit_pre_response_weight(tmp_path: Path):
    good = tmp_path / "good.json"
    good.write_text(
        json.dumps(
            {
                "panScale": 100,
                "mapping": {"LOW": 0.25, "NORMAL": 0.50},
                "candidates": [
                    {
                        "candidateId": "A",
                        "preResponseWeight": 40,
                        "responseBand": "HIGH",
                        "isTarget": True,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    n, mapping, candidates = cal.load_snapshot_input(good)
    assert n == 100
    assert mapping.normal == pytest.approx(0.5)
    assert candidates[0].pre_response_weight == pytest.approx(40.0)

    bad = tmp_path / "bad.json"
    bad.write_text(
        json.dumps(
            {
                "panScale": 100,
                "mapping": {"LOW": 0.25, "NORMAL": 0.50},
                "candidates": [
                    {
                        "candidateId": "A",
                        "spatialOpportunityIntensity": 40,
                        "responseBand": "HIGH",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(KeyError):
        cal.load_snapshot_input(bad)
