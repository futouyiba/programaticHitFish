"""Tackle visibility model built from the tackle.xlsx sample subset.

The sample rows come from the configured Lines and Leaders sheets. `opacity` and
`color` exist in the workbook; `clarity` is an added test parameter (the config
has no material-clarity field). Weights and the exposure factor are declared
assumptions, not Contract values.

visibility(component) =
    0.45 * (1 - clarity)          # material visibility
  + 0.30 * thickness_score^0.5    # perceived thickness, sublinear
  + 0.15 * (1 - opacity/100)      # config opacity, 0 = opaque
  + 0.10 * color_contrast         # RGB distance from declared water color

rig_visibility = max(component visibilities)   # the most visible part dominates
SuspicionLoad  = exposure_factor * rig_visibility
"""

from __future__ import annotations

import json
import math
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "stealth_samples.json").read_text(encoding="utf-8"))
WEIGHTS = DATA["meta"]["weights"]
WATER = tuple(DATA["meta"]["water_rgb"])
EXPOSURE = DATA["meta"]["exposure_factor"]


def color_contrast(color: str) -> float:
    if str(color).strip().lower() == "clear":
        return 0.0
    c = str(color).strip().lstrip("#")
    if len(c) != 6:
        return 0.5
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    dist = math.sqrt((r - WATER[0]) ** 2 + (g - WATER[1]) ** 2 + (b - WATER[2]) ** 2)
    return dist / math.sqrt(3 * 255 ** 2)


def _range(samples):
    ds = [s["diameter"] for s in samples]
    return min(ds), max(ds)


LINE_RANGE = _range(DATA["lines"])
LEADER_RANGE = _range(DATA["leaders"])


def thickness_score(diameter: float, bounds) -> float:
    lo, hi = bounds
    if hi == lo:
        return 0.0
    return max(0.0, min(1.0, (diameter - lo) / (hi - lo)))


def component_visibility(sample: dict, bounds) -> float:
    t = thickness_score(sample["diameter"], bounds) ** 0.5
    return (
        WEIGHTS["clarity"] * (1.0 - sample["clarity"])
        + WEIGHTS["thickness"] * t
        + WEIGHTS["opacity"] * (1.0 - sample["opacity"] / 100.0)
        + WEIGHTS["color"] * color_contrast(sample["color"])
    )


def line_visibility(sample: dict) -> float:
    return component_visibility(sample, LINE_RANGE)


def leader_visibility(sample: dict) -> float:
    return component_visibility(sample, LEADER_RANGE)


def find(kind: str, sample_id: int) -> dict:
    for s in DATA[kind]:
        if s["id"] == sample_id:
            return s
    raise KeyError(sample_id)


def rig_details(rig: dict) -> dict:
    line = find("lines", rig["line_id"])
    leader = find("leaders", rig["leader_id"])
    lv = line_visibility(line)
    dv = leader_visibility(leader)
    vis = max(lv, dv)
    return {
        "rig": rig["name"],
        "line": line["mark"],
        "leader": leader["mark"],
        "line_visibility": round(lv, 4),
        "leader_visibility": round(dv, 4),
        "rig_visibility": round(vis, 4),
        "suspicion_load": round(EXPOSURE * vis, 4),
        "coverage": rig["coverage"],
    }


def rig_suspicion(rig: dict) -> float:
    return rig_details(rig)["suspicion_load"]
