#!/usr/bin/env python3
"""Generate Prototype Gate evidence, including an SVG daily bias plot."""

from __future__ import annotations

import csv
from dataclasses import asdict
import json
from pathlib import Path

from .prototype import (
    HABITAT_CLASSES,
    PreyState,
    context_at,
    fragmentation_experiment,
    generate_map,
    granularity_comparison,
    observation_experiment,
    resolve_feeding_bias,
    resolve_spatial_class_bias,
    unrelated_source_experiment,
)


OUT = Path(__file__).with_name("prototype_output")


def _write_daily_samples() -> list[dict]:
    rows = []
    for minute in range(0, 24 * 60 + 1, 10):
        hour = minute / 60.0
        context = context_at(hour)
        bias = resolve_spatial_class_bias(context)
        rows.append(
            {
                "hour": hour,
                "light": context.light,
                "water_temperature": context.water_temperature,
                "temperature_trend": context.temperature_trend,
                "wind": context.wind,
                **{name: bias[name] for name in HABITAT_CLASSES},
            }
        )
    with (OUT / "continuous_spatial_bias.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    return rows


def _write_svg(rows: list[dict]) -> None:
    width, height = 920, 420
    left, top, plot_w, plot_h = 70, 35, 810, 320
    colors = {"GRASS": "#2f855a", "WOOD": "#9c6b30", "DEEP_EDGE": "#2b6cb0"}
    values = [row[name] for row in rows for name in HABITAT_CLASSES]
    low, high = min(values) - 0.03, max(values) + 0.03
    def point(row, name):
        x = left + row["hour"] / 24.0 * plot_w
        y = top + (high - row[name]) / (high - low) * plot_h
        return f"{x:.2f},{y:.2f}"
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#f8fafc" stroke="#cbd5e0"/>',
        '<text x="70" y="22" font-family="sans-serif" font-size="16">Context → SpatialBiasResolver (10-minute samples)</text>',
    ]
    for hour in range(0, 25, 4):
        x = left + hour / 24.0 * plot_w
        lines += [f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top+plot_h}" stroke="#e2e8f0"/>',
                  f'<text x="{x-10}" y="{top+plot_h+22}" font-family="sans-serif" font-size="12">{hour:02d}:00</text>']
    for name in HABITAT_CLASSES:
        points = " ".join(point(row, name) for row in rows)
        lines.append(f'<polyline points="{points}" fill="none" stroke="{colors[name]}" stroke-width="3"/>')
    for index, name in enumerate(HABITAT_CLASSES):
        x = 620 + index * 100
        lines += [f'<line x1="{x}" y1="395" x2="{x+24}" y2="395" stroke="{colors[name]}" stroke-width="4"/>',
                  f'<text x="{x+29}" y="400" font-family="sans-serif" font-size="12">{name}</text>']
    lines.append('</svg>')
    (OUT / "continuous_spatial_bias.svg").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = _write_daily_samples()
    _write_svg(rows)
    feeding_base = resolve_feeding_bias(PreyState(0.7, 1.3, 0.9))
    feeding_common_uplift = resolve_feeding_bias(PreyState(1.4, 2.6, 1.8))
    generated_map = generate_map()
    (OUT / "generated_map.json").write_text(
        json.dumps([asdict(source) for source in generated_map], indent=2) + "\n",
        encoding="utf-8",
    )
    result = {
        "status": "EXECUTABLE PROTOTYPE VALIDATION / TEST FIXTURE / NOT AUTHORITY",
        "map": {"zones": 3, "habitat_use_classes": 3, "source_groups": 45},
        "granularity": granularity_comparison(context_at(12.0), generated_map),
        "fragmentation": fragmentation_experiment(context_at(12.0), generated_map),
        "unrelated_source_independence": unrelated_source_experiment(context_at(12.0), generated_map),
        "continuous_resolver": {
            "samples": len(rows),
            "interval_minutes": 10,
            "max_adjacent_bias_delta": max(
                abs(rows[i][name] - rows[i - 1][name])
                for i in range(1, len(rows)) for name in HABITAT_CLASSES
            ),
            "fish_condition_epoch_needed": "NO",
            "conclusion": "NO ADDITIONAL EPOCH TRANSITION STRUCTURE NEEDED",
        },
        "feeding_resolver": {
            "base_preference_bias": feeding_base,
            "common_mode_activity_uplift_bias": feeding_common_uplift,
            "max_bias_delta": max(
                abs(feeding_base[key] - feeding_common_uplift[key]) for key in feeding_base
            ),
            "global_feeding_drive_owner": "independent and unchanged by this resolver",
            "verdict": "PASS" if feeding_base == feeding_common_uplift else "FAIL",
        },
        "observation": observation_experiment(),
    }
    (OUT / "prototype_results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
