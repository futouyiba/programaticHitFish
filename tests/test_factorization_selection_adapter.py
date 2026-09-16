import json
from collections import defaultdict
from pathlib import Path

import pytest

from fcf_v1.authoring import compile_authoring


DOC = json.loads(Path("authoring/bass_v0.json").read_text())


def test_factorization_preserves_exact_qxm_selection_projection():
    bundle = compile_authoring(DOC)
    weights = {
        (c.fish_quality, c.engagement_mode): c.selection_weight
        for c in bundle.contributions
    }

    expected = {
        ("Q1", "NORMAL"): 1.00,
        ("Q2", "NORMAL"): 0.80,
        ("Q2", "ACTIVE_SPAWNING"): 0.15,
        ("Q2", "SPAWN_GUARD"): 0.05,
        ("Q3", "NORMAL"): 0.70,
        ("Q3", "ACTIVE_SPAWNING"): 0.20,
        ("Q3", "SPAWN_GUARD"): 0.10,
        ("Q4", "NORMAL"): 0.70,
        ("Q4", "ACTIVE_SPAWNING"): 0.20,
        ("Q4", "SPAWN_GUARD"): 0.10,
        ("Q5", "NORMAL"): 0.70,
        ("Q5", "ACTIVE_SPAWNING"): 0.15,
        ("Q5", "SPAWN_GUARD"): 0.15,
    }
    assert weights == pytest.approx(expected)

    totals = defaultdict(float)
    for contribution in bundle.contributions:
        totals[contribution.fish_quality] += contribution.selection_weight
    assert dict(totals) == pytest.approx({q: 1.0 for q in ("Q1", "Q2", "Q3", "Q4", "Q5")})


def test_bake_subject_count_is_mode_count_not_qxm_count():
    bundle = compile_authoring(DOC)
    assert len(bundle.resolved_mode_bake_configs) == len(DOC["species"]["engagement_modes"])
    assert len(bundle.resolved_mode_bake_configs) == 3
    assert len(bundle.contributions) == 13
