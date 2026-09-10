#!/usr/bin/env python3
"""Run the three-epoch Bass pressure-test fixture.

Every number in this module is deliberately a TEST FIXTURE / TUNING PLACEHOLDER /
NOT AUTHORITY.  The script tests semantic separation; it does not implement the
open Engagement probability contract.
"""

from __future__ import annotations

import json
from pathlib import Path


EPOCHS = ("Morning", "Midday", "Evening")
ZONES = ("Grass Edge", "Shaded Wood", "Drop-off")
FOODS = ("BAITFISH", "CRUSTACEAN", "WORM_LIKE")
STATIC_SPATIAL = {"Grass Edge": 0.90, "Shaded Wood": 0.80, "Drop-off": 0.70}
STATIC_DIET = {"BAITFISH": 0.90, "CRUSTACEAN": 0.80, "WORM_LIKE": 0.70}
SPATIAL_BIAS = {
    "Morning": {"Grass Edge": 1.30, "Shaded Wood": 0.90, "Drop-off": 0.7285714286},
    "Midday": {"Grass Edge": 0.70, "Shaded Wood": 1.20, "Drop-off": 1.1571428571},
    "Evening": {"Grass Edge": 0.90, "Shaded Wood": 0.80, "Drop-off": 1.3571428571},
}
FEEDING_BIAS = {
    "Morning": {"BAITFISH": 1.30, "CRUSTACEAN": 0.90, "WORM_LIKE": 0.7285714286},
    "Midday": {"BAITFISH": 0.70, "CRUSTACEAN": 1.30, "WORM_LIKE": 1.0428571429},
    "Evening": {"BAITFISH": 0.90, "CRUSTACEAN": 0.80, "WORM_LIKE": 1.3571428571},
}
PRESENTATION_MATCH = {"BAITFISH": 0.95, "CRUSTACEAN": 0.90, "WORM_LIKE": 0.85}
REACH = 0.80
LOCAL_SCALE = 100.0
RESPONSE_WEIGHT = {"NONE": 0.0, "LOW": 0.25, "NORMAL": 1.0, "HIGH": 2.0}


def response_for(match: float) -> tuple[str, str]:
    if match >= 0.80:
        return "STRONG", "HIGH"
    if match >= 0.65:
        return "VALID", "NORMAL"
    if match >= 0.40:
        return "MARGINAL", "LOW"
    return "INVALID", "NONE"


def run() -> dict:
    spatial: dict = {}
    feeding: dict = {}
    for epoch in EPOCHS:
        spatial[epoch] = {}
        for zone in ZONES:
            local = LOCAL_SCALE * STATIC_SPATIAL[zone] * SPATIAL_BIAS[epoch][zone]
            spatial[epoch][zone] = {
                "static_preference": STATIC_SPATIAL[zone],
                "dynamic_bias": SPATIAL_BIAS[epoch][zone],
                "local_intensity": round(local, 6),
                "exposed_intensity": round(local * REACH, 6),
            }
        feeding[epoch] = {}
        for food in FOODS:
            raw = STATIC_DIET[food] * FEEDING_BIAS[epoch][food] * PRESENTATION_MATCH[food]
            match = min(1.0, raw)
            meaning, grade = response_for(match)
            feeding[epoch][food] = {
                "static_diet_fit": STATIC_DIET[food],
                "dynamic_bias": FEEDING_BIAS[epoch][food],
                "presentation_match": PRESENTATION_MATCH[food],
                "raw_feeding_match": round(raw, 6),
                "feeding_match": round(match, 6),
                "meaning": meaning,
                "response_grade": grade,
            }

    # Centering check: relative reweighting preserves the weighted fixture sum.
    spatial_totals = {
        e: round(sum(v["local_intensity"] for v in spatial[e].values()), 6) for e in EPOCHS
    }
    feeding_totals = {
        e: round(sum(STATIC_DIET[f] * FEEDING_BIAS[e][f] for f in FOODS), 6) for e in EPOCHS
    }
    return {
        "status": "TEST FIXTURE / TUNING PLACEHOLDER / NOT AUTHORITY",
        "conditions": {
            "satiation": "NORMAL",
            "cue_familiarity": "LOW",
            "fish_mode": "NORMAL",
            "lifecycle_cohort": "ORDINARY_NORMAL",
            "reach": REACH,
            "local_scale": LOCAL_SCALE,
        },
        "spatial": spatial,
        "feeding": feeding,
        "centered_checks": {
            "spatial_local_totals": spatial_totals,
            "feeding_weighted_totals": feeding_totals,
            "expected_spatial_total": round(LOCAL_SCALE * sum(STATIC_SPATIAL.values()), 6),
            "expected_feeding_total": round(sum(STATIC_DIET.values()), 6),
        },
    }


def main() -> None:
    output = run()
    path = Path(__file__).with_name("output.json")
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
