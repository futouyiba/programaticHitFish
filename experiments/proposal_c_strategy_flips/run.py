"""Run the Proposal C strategy-flip experiment and write reproducible outputs.

Usage:
    python3 run.py

Writes results/results.json, results/scenarios.csv and figures/*.svg.
All inputs are in fixtures.json; every fixture value is illustrative.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from model import (
    FishCondition,
    Strategy,
    describe,
    response,
    toy_yield,
    willingness_threshold,
    shift_affinity,
    TIER_ANCHORS,
    UNKNOWN,
    NOT_CONFIGURED,
    REJECT,
    INVALID,
)

ROOT = Path(__file__).parent
FIXTURES = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)


def make_strategy(spec: dict, shared: dict) -> Strategy:
    return Strategy(
        name=spec["name"],
        supports=dict(spec["supports"]),
        base_affinity=dict(shared["base_affinity"]),
        q=spec.get("q", 0.50),
        trigger_strength=dict(spec.get("trigger_strength", shared.get("trigger_strength", {}))),
        size_adjustment=shared.get("size_adjustment", 0.0),
        coverage=spec.get("coverage", shared.get("coverage", 1.0)),
        suspicion_load=spec.get("suspicion_load", shared.get("suspicion_load", 0.0)),
    )


def make_fish(fish: dict) -> FishCondition:
    return FishCondition(
        activity=fish["activity"],
        motivation=fish["motivation"],
        wariness=fish["wariness"],
        diet_shift=dict(fish["diet_shift"]),
    )


def run_scenarios():
    rows = []
    for axis_id, axis in FIXTURES["axes"].items():
        shared = axis["shared"]
        for sc in axis["scenarios"]:
            fish = make_fish(sc["fish"])
            for spec in axis["strategies"]:
                strategy = make_strategy(spec, shared)
                result = describe(strategy, fish)
                result.update({"axis": axis_id, "scenario": sc["id"], "label": sc["label"]})
                rows.append(result)
    return rows


def rank(rows, axis_id, scenario_id):
    vals = [r for r in rows if r["axis"] == axis_id and r["scenario"] == scenario_id]
    vals.sort(key=lambda r: (r["C"] is not None, r["C"] or 0.0), reverse=True)
    return vals


# --- sweeps ---------------------------------------------------------------

def diet_sweep():
    axis = FIXTURES["axes"]["A_diet"]
    shared = axis["shared"]
    strategies = [make_strategy(s, shared) for s in axis["strategies"]]
    out = []
    for i in range(101):
        s = -1.0 + i * 0.02
        fish = FishCondition(
            activity=1.0, motivation=0.5, wariness=0.0,
            diet_shift={"baitfish": -s, "crayfish": s},
        )
        row = {"shift": round(s, 4)}
        for st in strategies:
            _, c, _, _ = response(st, fish)
            row[st.name] = c
        out.append(row)
    return out


def find_crossover(points, key_a, key_b, x_key="shift"):
    """Return the first x where sign(a-b) changes, refined by bisection."""
    prev = None
    for p in points:
        if p[key_a] is None or p[key_b] is None:
            continue
        d = p[key_a] - p[key_b]
        if prev is not None and prev[1] * d < 0:
            lo, hi = prev[0], p[x_key]
            for _ in range(50):
                mid = (lo + hi) / 2
                fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                                     diet_shift={"baitfish": -mid, "crayfish": mid})
                axis = FIXTURES["axes"]["A_diet"]["shared"]
                a = response(make_strategy(FIXTURES["axes"]["A_diet"]["strategies"][0], axis), fish)[1]
                b = response(make_strategy(FIXTURES["axes"]["A_diet"]["strategies"][1], axis), fish)[1]
                if (a - b) * (prev[2]) > 0:
                    lo = mid
                else:
                    hi = mid
            return round((lo + hi) / 2, 4)
        prev = (p[x_key], d, d)
    return None


def motivation_sweep():
    axis = FIXTURES["axes"]["C_motivation_reaction"]
    shared = axis["shared"]
    strategies = [make_strategy(s, shared) for s in axis["strategies"]]
    out = []
    for i in range(101):
        m = i / 100
        fish = FishCondition(activity=1.0, motivation=m, wariness=0.0,
                             diet_shift={"baitfish": 0.0})
        row = {"motivation": round(m, 4)}
        for st in strategies:
            _, c, _, _ = response(st, fish)
            row[st.name] = c
        out.append(row)
    return out


def motivation_crossovers(points):
    """Crossings between natural and each reaction strategy."""
    out = {}
    for key in ("reaction_twitch_q0.60", "reaction_burst_q0.75"):
        xs = []
        prev = None
        for p in points:
            d = p["natural_q0.60"] - p[key]
            if prev is not None and prev * d < 0:
                xs.append(round(p["motivation"], 2))
            prev = d
        out[key] = xs
    return out


def diet_cross_for(gen_sup, spec_sup):
    axis = FIXTURES["axes"]["A_diet"]
    shared = axis["shared"]
    gen = Strategy(name="gen", supports={"baitfish": gen_sup, "crayfish": gen_sup},
                   base_affinity=dict(shared["base_affinity"]), q=0.5,
                   trigger_strength={"baitfish": 0.0, "crayfish": 0.0})
    spec = Strategy(name="spec", supports={"baitfish": spec_sup, "crayfish": 0.15},
                    base_affinity=dict(shared["base_affinity"]), q=0.5,
                    trigger_strength={"baitfish": 0.0, "crayfish": 0.0})
    def diff(s):
        fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                             diet_shift={"baitfish": -s, "crayfish": s})
        return response(gen, fish)[1] - response(spec, fish)[1]
    lo, hi = 0.0, 1.0
    if diff(lo) == 0:
        return 0.0
    if diff(lo) * diff(hi) > 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if diff(lo) * diff(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return round((lo + hi) / 2, 4)


def reaction_support_scan():
    axis = FIXTURES["axes"]["C_motivation_reaction"]
    shared = axis["shared"]
    natural = make_strategy(axis["strategies"][0], shared)
    rows = []
    for i in range(71):
        sup = 0.20 + i * 0.01
        reaction = Strategy(name="reaction", supports={"baitfish": sup},
                            base_affinity=dict(shared["base_affinity"]), q=0.60,
                            trigger_strength={"baitfish": 0.80})
        row = {"support": round(sup, 2)}
        for m, tag in ((0.2, "low"), (0.7, "high")):
            fish = FishCondition(activity=1.0, motivation=m, wariness=0.0,
                                 diet_shift={"baitfish": 0.0})
            row[f"natural_{tag}"] = response(natural, fish)[1]
            row[f"reaction_{tag}"] = response(reaction, fish)[1]
        rows.append(row)
    return rows


def q_sweep():
    axis = FIXTURES["axes"]["B_activity_speed"]
    shared = axis["shared"]
    out = []
    for activity in (0.6, 1.0, 1.4):
        rows = []
        q = 0.20
        while q <= 2.0001:
            st = Strategy(name=f"q{q:.2f}", supports={"baitfish": 0.85},
                          base_affinity=dict(shared["base_affinity"]), q=q,
                          trigger_strength={"baitfish": 0.0})
            fish = FishCondition(activity=activity, motivation=0.5, wariness=0.0,
                                 diet_shift={"baitfish": 0.0})
            _, c, _, _ = response(st, fish)
            rows.append({"q": round(q, 3), "C": c,
                         "yield": toy_yield(c, q, 1.0) if c is not None else None})
            q += 0.02
        out.append({"activity": activity, "points": rows})
    return out


def coverage_sensitivity():
    """How much more area would the fast strategy need to cover, at equal C?"""
    axis = FIXTURES["axes"]["B_activity_speed"]
    shared = axis["shared"]
    slow = make_strategy(axis["strategies"][0], shared)
    fast = make_strategy(axis["strategies"][1], shared)
    fish = make_fish(axis["scenarios"][1]["fish"])
    _, cs, _, _ = response(slow, fish)
    _, cf, _, _ = response(fast, fish)
    ys = toy_yield(cs, slow.q, 1.0)
    yf = toy_yield(cf, fast.q, 1.0)
    return {"slow_yield": ys, "fast_yield": yf,
            "coverage_ratio_needed": ys / yf if yf else None}


def hypothetical_cue():
    axis = FIXTURES["axes"]["D_wariness_stealth"]
    shared = axis["shared"]
    cue = axis["hypothetical_cue"]
    direct_spec, stealth_spec = axis["strategies"]
    out = []
    for i in range(101):
        w = i / 100
        fish = FishCondition(activity=1.0, motivation=0.5, wariness=w,
                             diet_shift={"baitfish": 0.0})
        direct = make_strategy(direct_spec, shared)
        stealth = make_strategy(stealth_spec, shared)
        direct.suspicion_load = cue["direct_suspicion"]
        stealth.suspicion_load = cue["stealth_suspicion"]
        _, cd, _, _ = response(direct, fish)
        _, cs, _, _ = response(stealth, fish)
        yd = toy_yield(cd, direct.q, direct.coverage)
        ys = toy_yield(cs, stealth.q, stealth.coverage)
        out.append({"wariness": round(w, 3), "C_direct": cd, "C_stealth": cs,
                    "yield_direct": yd, "yield_stealth": ys})
    return out


def cue_crossover(points):
    prev = None
    for p in points:
        d = p["yield_direct"] - p["yield_stealth"]
        if prev is not None and prev * d < 0:
            # bisect in wariness using linear interpolation is enough for reporting
            return round(p["wariness"], 2)
        prev = d
    return None


def saturation_scan():
    """Share of (food, q) space where C is exactly 0 or 1 at M=0.5, activity=1."""
    total = 0
    low = 0
    high = 0
    for fi in range(51):
        food = fi / 50
        q = 0.20
        while q <= 2.0001:
            st = Strategy(name="s", supports={"baitfish": 1.0},
                          base_affinity={"baitfish": food}, q=q,
                          trigger_strength={"baitfish": 0.0})
            fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                                 diet_shift={"baitfish": 0.0})
            _, c, _, _ = response(st, fish)
            total += 1
            if c == 0.0:
                low += 1
            elif c == 1.0:
                high += 1
            q += 0.02
    return {"total": total, "zero": low, "one": high,
            "saturated_share": (low + high) / total,
            "interior_share": 1 - (low + high) / total}


def protocol_cases():
    base = Strategy(name="base", supports={"baitfish": 1.0},
                    base_affinity={"baitfish": 0.70}, q=0.5,
                    trigger_strength={"baitfish": 0.0})
    fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                         diet_shift={"baitfish": 0.0})
    cases = {}
    cases["resolved_zero"] = response(
        Strategy(name="z", supports={"baitfish": 0.0},
                 base_affinity={"baitfish": 0.70}, q=0.5,
                 trigger_strength={"baitfish": 0.0}), fish)
    cases["unknown"] = response(
        Strategy(name="u", supports={"baitfish": UNKNOWN},
                 base_affinity={"baitfish": 0.70}, q=0.5,
                 trigger_strength={"baitfish": 0.0}), fish)
    cases["not_configured"] = response(
        Strategy(name="n", supports={"baitfish": NOT_CONFIGURED},
                 base_affinity={"baitfish": 0.70}, q=0.5,
                 trigger_strength={"baitfish": 0.0}), fish)
    cases["reject"] = response(
        Strategy(name="r", supports={"baitfish": REJECT},
                 base_affinity={"baitfish": 0.70}, q=0.5,
                 trigger_strength={"baitfish": 0.0}), fish)
    cases["invalid"] = response(
        Strategy(name="i", supports={"baitfish": 1.0},
                 base_affinity={"baitfish": 0.70}, q=float("nan"),
                 trigger_strength={"baitfish": 0.0}), fish)
    mixed = Strategy(name="mixed", supports={"baitfish": 1.0, "crayfish": UNKNOWN},
                     base_affinity={"baitfish": 0.70, "crayfish": 0.70}, q=0.5,
                     trigger_strength={"baitfish": 0.0, "crayfish": 0.0})
    mixed_fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                               diet_shift={"baitfish": 0.0, "crayfish": 0.0})
    mixed_status, mixed_c, mixed_skipped, _ = response(mixed, mixed_fish)
    cases["mixed_unknown_branch"] = {
        "status": mixed_status, "C": mixed_c, "skipped": mixed_skipped}
    cases["missing_trigger"] = response(
        Strategy(name="mt", supports={"baitfish": 1.0},
                 base_affinity={"baitfish": 0.70}, q=0.5,
                 trigger_strength={}), fish)
    missing_support = Strategy(
        name="ms", supports={"baitfish": 1.0}, siblings=["baitfish", "crayfish"],
        base_affinity={"baitfish": 0.70, "crayfish": 0.70}, q=0.5,
        trigger_strength={"baitfish": 0.0, "crayfish": 0.0})
    ms_status, ms_c, ms_skipped, _ = response(missing_support, fish)
    cases["missing_support_sibling"] = {
        "status": ms_status, "C": ms_c, "skipped": ms_skipped}
    out = {}
    for k, v in cases.items():
        out[k] = v if isinstance(v, dict) else {"status": v[0], "C": v[1]}
    return out


def reaction_flip_grid():
    """How often does the motivation flip survive across plausible strategy settings?"""
    axis = FIXTURES["axes"]["C_motivation_reaction"]
    shared = axis["shared"]
    natural = make_strategy(axis["strategies"][0], shared)
    rows = []
    for i in range(7):
        sup = 0.50 + i * 0.05
        for j in range(5):
            trig = 0.50 + j * 0.10
            for q in (0.60, 0.75):
                reaction = Strategy(name="r", supports={"baitfish": sup},
                                    base_affinity=dict(shared["base_affinity"]), q=q,
                                    trigger_strength={"baitfish": trig})
                low = FishCondition(activity=1.0, motivation=0.2, wariness=0.0,
                                    diet_shift={"baitfish": 0.0})
                high = FishCondition(activity=1.0, motivation=0.7, wariness=0.0,
                                     diet_shift={"baitfish": 0.0})
                rl = response(reaction, low)[1]
                rh = response(reaction, high)[1]
                nl = response(natural, low)[1]
                nh = response(natural, high)[1]
                rows.append({"support": round(sup, 2), "trigger": round(trig, 2), "q": q,
                             "reaction_low": rl, "reaction_high": rh,
                             "natural_low": nl, "natural_high": nh,
                             "flip": bool(rl > nl and nh > rh)})
    share = sum(1 for r in rows if r["flip"]) / len(rows)
    return rows, share


def size_scan():
    """Negative control: size adjustment shifts FoodValue for every strategy alike."""
    axis = FIXTURES["axes"]["A_diet"]
    shared = axis["shared"]
    out = []
    for i in range(21):
        size = -0.20 + i * 0.02
        fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                             diet_shift={"baitfish": 0.0, "crayfish": 0.0})
        row = {"size_adjustment": round(size, 2)}
        for spec in axis["strategies"]:
            st = make_strategy(spec, shared)
            st.size_adjustment = size
            row[spec["name"]] = response(st, fish)[1]
        out.append(row)
    return out


def dominance(rows):
    out = {}
    for axis_id in FIXTURES["axes"]:
        sc_ids = {r["scenario"] for r in rows if r["axis"] == axis_id}
        wins = {}
        for sc in sorted(sc_ids):
            ranked = rank(rows, axis_id, sc)
            if ranked and ranked[0]["C"] is not None:
                wins.setdefault(ranked[0]["strategy"], []).append(sc)
        out[axis_id] = wins
    return out


# --- SVG charts -----------------------------------------------------------

def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_bars(groups, path, title):
    width = 760
    left = 170
    right = 70
    plot_w = width - left - right
    row_h = 24
    head_h = 30
    block_gap = 16
    height = 50 + sum(head_h + row_h * len(vals) + block_gap for _, vals in groups)
    colors = ["#0f6b63", "#a85a12", "#7a4e9b"]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'font-family="PingFang SC, Noto Sans SC, sans-serif">',
             f'<rect width="100%" height="100%" fill="#ffffff"/>',
             f'<text x="24" y="24" font-size="15" fill="#1e2328">{_esc(title)}</text>']
    y = 46
    for label, values in groups:
        parts.append(f'<text x="24" y="{y+12}" font-size="12" font-weight="600" '
                     f'fill="#1e2328">{_esc(label)}</text>')
        y += head_h
        for vi, (name, val) in enumerate(values):
            v = 0.0 if val is None else val
            w = v * plot_w
            parts.append(f'<rect x="{left}" y="{y}" width="{w:.1f}" height="{row_h-6}" '
                         f'fill="{colors[vi % len(colors)]}" opacity="0.88"/>')
            parts.append(f'<text x="{left-8}" y="{y+13}" font-size="11" text-anchor="end" '
                         f'fill="#5b6470">{_esc(name)}</text>')
            parts.append(f'<text x="{left+w+6:.1f}" y="{y+13}" font-size="11" '
                         f'fill="#1e2328">{v:.3f}</text>')
            y += row_h
        y += block_gap
    parts.append(f'<line x1="{left}" y1="46" x2="{left}" y2="{height-20}" stroke="#1e2328" stroke-width="1"/>')
    parts.append(f'<text x="{left}" y="{height-6}" font-size="10" fill="#5b6470">0</text>')
    parts.append(f'<text x="{left+plot_w}" y="{height-6}" font-size="10" text-anchor="end" '
                 f'fill="#5b6470">1.0</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def svg_lines(series, path, title, xlabel, ylabel, ymax=None):
    if ymax is None:
        vals = [y for _, pts in series for _, y in pts if y is not None]
        ymax = max(vals) * 1.15 if vals else 1.0
    width, height = 760, 320
    ml, mb, mt = 60, 60, 40
    pw, ph = width - ml - 20, height - mb - mt
    xs = [p[0] for _, pts in series for p in pts]
    xmin, xmax = min(xs), max(xs)
    def X(x): return ml + (x - xmin) / (xmax - xmin) * pw
    def Y(y): return mt + ph - (y / ymax) * ph
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'font-family="PingFang SC, Noto Sans SC, sans-serif">',
             f'<rect width="100%" height="100%" fill="#ffffff"/>',
             f'<text x="{ml}" y="24" font-size="15" fill="#1e2328">{_esc(title)}</text>']
    colors = ["#0f6b63", "#a85a12", "#7a4e9b"]
    for i, (name, pts) in enumerate(series):
        d = []
        for x, y in pts:
            if y is None:
                continue
            d.append(("M" if not d else "L") + f"{X(x):.1f},{Y(y):.1f}")
        parts.append(f'<path d="{" ".join(d)}" fill="none" stroke="{colors[i % len(colors)]}" '
                     f'stroke-width="2.2"/>')
        lx = 70 + i * 160
        parts.append(f'<rect x="{lx}" y="{height-26}" width="12" height="4" fill="{colors[i % len(colors)]}"/>')
        parts.append(f'<text x="{lx+18}" y="{height-20}" font-size="11" fill="#5b6470">{_esc(name)}</text>')
    parts.append(f'<line x1="{ml}" y1="{mt+ph}" x2="{width-20}" y2="{mt+ph}" stroke="#1e2328"/>')
    parts.append(f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt+ph}" stroke="#1e2328"/>')
    for t in (0.0, ymax / 2, ymax):
        yy = Y(t)
        parts.append(f'<line x1="{ml}" y1="{yy:.1f}" x2="{width-20}" y2="{yy:.1f}" '
                     f'stroke="#ddd6c8" stroke-width="0.8"/>')
        parts.append(f'<text x="{ml-6}" y="{yy+4:.1f}" font-size="10" text-anchor="end" '
                     f'fill="#5b6470">{t:.3f}</text>')
    for k in range(5):
        xv = xmin + (xmax - xmin) * k / 4
        xx = X(xv)
        parts.append(f'<line x1="{xx:.1f}" y1="{mt+ph}" x2="{xx:.1f}" y2="{mt+ph+4}" stroke="#1e2328"/>')
        parts.append(f'<text x="{xx:.1f}" y="{mt+ph+16}" font-size="10" text-anchor="middle" '
                     f'fill="#5b6470">{xv:.2f}</text>')
    parts.append(f'<text x="{width/2:.0f}" y="{height-4}" font-size="11" text-anchor="middle" '
                 f'fill="#5b6470">{_esc(xlabel)}</text>')
    parts.append(f'<text x="14" y="{mt+ph/2}" font-size="11" text-anchor="middle" '
                 f'transform="rotate(-90 14 {mt+ph/2})" fill="#5b6470">{_esc(ylabel)}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def svg_heat(grid, path, title):
    rows, cols = len(grid), len(grid[0])
    cell = 10
    ml, mt = 60, 40
    width, height = ml + cols * cell + 20, mt + rows * cell + 60
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'font-family="PingFang SC, Noto Sans SC, sans-serif">',
             f'<rect width="100%" height="100%" fill="#ffffff"/>',
             f'<text x="{ml}" y="24" font-size="15" fill="#1e2328">{_esc(title)}</text>']
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v is None:
                color = "#cccccc"
            elif v == 0.0:
                color = "#d9d0c1"
            elif v == 1.0:
                color = "#1e2328"
            else:
                g = int(60 + 195 * (1 - v))
                color = f"rgb({g},{g},{g})"
            x = ml + c * cell
            y = mt + r * cell
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{color}"/>')
    parts.append(f'<text x="{ml+cols*cell/2:.0f}" y="{height-28}" font-size="11" '
                 f'text-anchor="middle" fill="#5b6470">q (0.2 to 2.0) →</text>')
    parts.append(f'<text x="{ml-6}" y="{mt+10}" font-size="10" text-anchor="end" fill="#5b6470">1.0</text>')
    parts.append(f'<text x="{ml-6}" y="{mt+rows*cell}" font-size="10" text-anchor="end" fill="#5b6470">0.0</text>')
    parts.append(f'<text x="{ml-6}" y="{mt+rows*cell/2:.0f}" font-size="10" text-anchor="end" fill="#5b6470">0.5</text>')
    parts.append(f'<text x="16" y="{mt+rows*cell/2:.0f}" font-size="11" text-anchor="middle" '
                 f'transform="rotate(-90 16 {mt+rows*cell/2:.0f})" fill="#5b6470">food value →</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def saturation_grid():
    grid = []
    for fi in range(51):
        food = 1.0 - fi / 50
        row = []
        q = 0.20
        while q <= 2.0001:
            st = Strategy(name="s", supports={"baitfish": 1.0},
                          base_affinity={"baitfish": food}, q=q,
                          trigger_strength={"baitfish": 0.0})
            fish = FishCondition(activity=1.0, motivation=0.5, wariness=0.0,
                                 diet_shift={"baitfish": 0.0})
            _, c, _, _ = response(st, fish)
            row.append(c)
            q += 0.02
        grid.append(row)
    return grid


def main():
    rows = run_scenarios()
    diet = diet_sweep()
    motivation = motivation_sweep()
    qs = q_sweep()
    hypo = hypothetical_cue()
    sat = saturation_scan()
    protocol = protocol_cases()

    cross = find_crossover(diet, "generalist", "specialist")
    mcross = motivation_crossovers(motivation)
    cov = coverage_sensitivity()
    cue_cross = cue_crossover(hypo)
    dom = dominance(rows)
    reaction_scan = reaction_support_scan()
    sizes = size_scan()
    reaction_grid, reaction_flip_share = reaction_flip_grid()
    diet_sensitivity = [
        [round(g, 2), round(sp, 2), diet_cross_for(g, sp)]
        for g in (0.55, 0.65, 0.75)
        for sp in (0.85, 0.92, 0.97)
    ]

    # Assertions: negative results are the point, so they are pinned too.
    assert cross is not None, "diet axis must cross somewhere"
    assert 0.0 < cross < 1.0
    assert protocol["unknown"]["status"] == "ResolutionIncomplete"
    assert protocol["not_configured"]["status"] == "ResolutionIncomplete"
    assert protocol["reject"]["status"] == "Reject"
    assert protocol["invalid"]["status"] == "InvalidInput"
    assert protocol["resolved_zero"]["status"] == "Resolved"
    assert protocol["resolved_zero"]["C"] == 0.0
    assert protocol["mixed_unknown_branch"]["status"] == "Resolved"
    assert protocol["mixed_unknown_branch"]["skipped"] == {"crayfish": "Unknown"}
    assert protocol["missing_trigger"]["status"] == "ResolutionIncomplete"
    assert protocol["missing_support_sibling"]["status"] == "Resolved"
    assert protocol["missing_support_sibling"]["skipped"] == {"crayfish": "Unknown"}
    # Pinned findings: a silent formula or fixture change must fail here.
    assert abs(cross - 0.2524) < 0.002
    assert mcross["reaction_twitch_q0.60"] == [0.65]
    assert mcross["reaction_burst_q0.75"] == [0.40]
    assert abs(cov["coverage_ratio_needed"] - 2.7243) < 0.02
    assert abs(sat["saturated_share"] - 0.7281) < 0.002
    assert abs(cue_cross - 0.24) < 0.02
    assert all(v is not None for _, _, v in diet_sensitivity)
    assert 0.0 < reaction_flip_share < 1.0
    # Slow beats fast at Response level at both activities.
    b1 = {r["strategy"]: r for r in rank(rows, "B_activity_speed", "B1_low_activity")}
    b2 = {r["strategy"]: r for r in rank(rows, "B_activity_speed", "B2_high_activity")}
    assert b1["slow_q0.45"]["C"] > b1["fast_q0.90"]["C"]
    assert b2["slow_q0.45"]["C"] > b2["fast_q0.90"]["C"]
    # At low Motivation reaction beats natural; at high Motivation natural wins.
    c1 = {r["strategy"]: r for r in rank(rows, "C_motivation_reaction", "C1_low_motivation")}
    c2 = {r["strategy"]: r for r in rank(rows, "C_motivation_reaction", "C2_high_motivation")}
    assert c1["reaction_twitch_q0.60"]["C"] > c1["natural_q0.60"]["C"]
    assert c2["natural_q0.60"]["C"] > c2["reaction_twitch_q0.60"]["C"]
    # Wariness alone changes nothing without a cue.
    d1 = {r["strategy"]: r for r in rank(rows, "D_wariness_stealth", "D1_low_wariness")}
    d2 = {r["strategy"]: r for r in rank(rows, "D_wariness_stealth", "D2_high_wariness")}
    assert d1["direct"]["C"] == d1["stealth"]["C"] == d2["direct"]["C"] == d2["stealth"]["C"]

    # CSV of scenarios
    with (RESULTS / "scenarios.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["axis", "scenario", "strategy", "status", "C", "yield", "q"])
        for r in rows:
            writer.writerow([r["axis"], r["scenario"], r["strategy"], r["status"],
                             r["C"], r["yield"], r["q"]])

    payload = {
        "meta": FIXTURES["meta"],
        "scenarios": rows,
        "diet_sweep": diet,
        "diet_crossover_shift": cross,
        "motivation_sweep": motivation,
        "motivation_crossovers": mcross,
        "q_sweep": qs,
        "coverage_sensitivity": cov,
        "hypothetical_cue": hypo,
        "cue_crossover_wariness": cue_cross,
        "saturation": sat,
        "protocol": protocol,
        "dominance": dom,
        "reaction_support_scan": reaction_scan,
        "reaction_flip_grid": reaction_grid,
        "reaction_flip_share": reaction_flip_share,
        "diet_boundary_sensitivity": diet_sensitivity,
        "size_scan": sizes,
    }
    (RESULTS / "results.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Charts
    panel = []
    for axis_id, axis in FIXTURES["axes"].items():
        for sc in axis["scenarios"]:
            vals = []
            for spec in axis["strategies"]:
                match = next(r for r in rows
                             if r["axis"] == axis_id and r["scenario"] == sc["id"]
                             and r["strategy"] == spec["name"])
                vals.append((spec["name"], match["C"]))
            panel.append((sc["id"], vals))
    svg_bars(panel[:4], FIGURES / "response_by_axis.svg", "Response C by strategy (axis A and B)")
    svg_bars(panel[4:], FIGURES / "response_by_axis_2.svg", "Response C by strategy (axis C and D)")
    svg_lines(
        [("generalist", [(p["shift"], p["generalist"]) for p in diet]),
         ("specialist", [(p["shift"], p["specialist"]) for p in diet])],
        FIGURES / "diet_flip.svg", "Diet shift sweep: C_generalist vs C_specialist",
        "diet shift s (negative = toward baitfish, positive = toward crayfish)", "C", ymax=1.0)
    svg_lines(
        [("natural", [(p["motivation"], p["natural_q0.60"]) for p in motivation]),
         ("reaction twitch", [(p["motivation"], p["reaction_twitch_q0.60"]) for p in motivation]),
         ("reaction burst", [(p["motivation"], p["reaction_burst_q0.75"]) for p in motivation])],
        FIGURES / "motivation_flip.svg", "Motivation sweep: natural vs reaction",
        "Feeding Motivation", "C", ymax=1.0)
    svg_lines(
        [(f"Activity {a['activity']}", [(p["q"], p["yield"]) for p in a["points"]]) for a in qs],
        FIGURES / "speed_yield.svg", "Toy opportunity yield vs speed (equal coverage)",
        "q (speed / intercept limit)", "relative yield")
    svg_heat(saturation_grid(), FIGURES / "saturation_map.svg",
             "C saturation map: light = 0, dark = 1 (M=0.5, Activity=1)")

    print("axis\tscenario\tstrategy\tstatus\tC\tyield")
    for r in rows:
        c = "-" if r["C"] is None else f"{r['C']:.4f}"
        y = "-" if r["yield"] is None else f"{r['yield']:.4f}"
        print(f"{r['axis']}\t{r['scenario']}\t{r['strategy']}\t{r['status']}\t{c}\t{y}")

    print("\ndiet crossover shift:", cross)
    print("motivation crossovers:", mcross)
    print("coverage ratio needed for fast to match slow:", cov["coverage_ratio_needed"])
    print("hypothetical cue crossover wariness:", cue_cross)
    print("diet boundary sensitivity:", diet_sensitivity)
    print("reaction flip share over grid:", round(reaction_flip_share, 3))
    print("size scan monotone specialist lead:",
          all(x["specialist"] >= x["generalist"] for x in sizes))
    print("saturation share:", round(sat["saturated_share"], 3),
          "zero", sat["zero"], "one", sat["one"], "of", sat["total"])
    print("dominance:", json.dumps(dom, ensure_ascii=False))
    print("protocol:", json.dumps(protocol, ensure_ascii=False))
    print("Artifacts written to results/ and figures/")


if __name__ == "__main__":
    main()
