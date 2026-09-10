#!/usr/bin/env python3
"""validate_config.py — structural validator + semantic boundary guard
for the UsableForageAvailability config main-path artifact (r1).

Pure standard library (argparse / json / re / sys). Exit 0 = pass, 1 = fail.

Check families:
  TOP     top-level field allowlist: the config admits no author-invented
          sections, so there is no surface for author-editable intermediate
          dependencies (steps / depends_on / next-jump style content).
  STRUCT  structural shape + referential consistency: fixed row schemas for
          prey_fields / population_eligibility rows (unknown keys inside a
          row fail); diet_classes may be empty (explicit zero overlap) but
          must reference prey classes actually bound in prey_fields; size
          windows must be sane; units must be homogeneous because
          FILTERED_SUM sums across prey classes; contract.prey_field_semantics
          must be declared as raw_biomass_uncorrected.
  SNAP    snapshot-only input sourcing + raw fact-family allowlist: every
          snapshot_key must address the single Resolved Snapshot (sourcing
          another Factor's output fails), its fact segment must match the
          allowed raw-prey fact family pattern, and correction-semantics
          stems (percep / visib / adjust / correct) inside a snapshot key
          fail. (This is the config-level proxy for the "Bake factors read
          only the one Resolved Snapshot; Factor does not read Factor
          output; prey fields are raw, uncorrected biomass" constraints.
          Runtime enforcement lives in the engine, not here.)
  COMBINE fixed combine constant: operator is pinned to FILTERED_SUM and
          author_selectable is pinned to false; combine is not a choice.
  GUARD   boundary guard: excluded semantics must not appear as ANY key or
          value anywhere in the config text. Fail-closed English stem list
          (token-level prefix matching over camelCase-split letter runs) plus
          a Chinese keyword list (substring matching over keys and values,
          and over the raw text in both literal and \\uXXXX-escaped form).
          This guard is a LEXICAL PROXY for the semantic exclusion promise,
          not the promise itself: the tables enumerate the synonym families
          named in review and cannot be exhaustive (residual risk: a
          synonym not in the tables passes; found ones extend the tables).

NOT AUTHORITY. Passing this validator is a representation-shape check only.
It is not mechanism promotion, not a Freeze, and not a runtime enforcement
of snapshot isolation.

Usage:
  python validate_config.py <path/to/usable_forage.config.json>
  python validate_config.py --selftest
"""

from __future__ import annotations

import argparse
import json
import re
import sys

EXPECTED = {
    "schema_version": "usable_forage.config.r1",
    "contract_name": "UsableForageAvailability",
    "output_fact": "usable_forage_availability",
    "input_scope": "resolved_snapshot_only",
    "combine_operator": "FILTERED_SUM",
    "prey_field_semantics": "raw_biomass_uncorrected",
}

SNAPSHOT_KEY_PREFIX = "resolved_snapshot."

ALLOWED_TOP_LEVEL = {
    "schema_version", "instance", "contract",
    "prey_fields", "population_eligibility", "fixed_combine",
}

# Fixed row schemas: no key injection inside table rows.
ALLOWED_PREY_FIELD_KEYS = {
    "prey_class", "snapshot_key", "representative_size_mm", "unit",
}
ALLOWED_ELIGIBILITY_KEYS = {"population_id", "diet_classes", "size_window_mm"}
ALLOWED_WINDOW_KEYS = {"min", "max"}

# Boundary guard keyword stems (English). Deliberately conservative
# (fail-closed): a token starting with any stem is a violation even if the
# full word is innocent-looking, because nothing in this contract
# legitimately needs these semantics. Organized by the exclusion families
# named in review:
#   cover family      refuge/shelter/hiding/ambush/structure/safety/risk/
#                     concealment/cover
#   visibility family detectability/perception/reach/conspicuity/turbidity/
#                     seeing/visibility
#   capture family    catch/grasp/encounter/capture
#   energetic family  cost/handling/energetics
#   geometry          attack geometry (owner: Encounter)
EXCLUDED_SEMANTIC_STEMS = (
    # cover family
    "cover", "refuge", "shelter", "hid", "ambush", "structur",
    "safe", "risk", "conceal",
    # visibility family
    "visib", "detectab", "perceiv", "percep", "reach", "conspicu", "turbid",
    "see",
    # capture family
    "captur", "catch", "grasp", "encounter",
    # energetic family
    "energ", "cost", "handl",
    # attack geometry
    "geometr",
)

# Boundary guard keywords (Chinese), substring-matched. Chinese has no
# word segmentation in config text, so substring matching over the full
# key/value surface is the fail-closed choice. Families mirror the English
# stems. Substring hits can be broader than the intended semantics
# (e.g. any word containing the character 藏); accepted by fail-closed
# design because this contract has no legitimate Chinese content at all.
EXCLUDED_SEMANTIC_ZH = (
    # cover family
    "躲避", "藏", "庇护", "掩体", "结构", "安全", "风险", "埋伏",
    # visibility family (incl. 感知/修正 = perception / correction modifiers)
    "可见", "察觉", "感知", "修正", "浑浊",
    # capture family
    "抓", "捕获", "遭遇",
    # energetic family
    "代价", "成本",
)

# Correction-semantics stems that must never appear inside a snapshot_key:
# the prey field contract consumes RAW biomass. perception/visibility stems
# are also in the global GUARD table (defense in depth with a more precise
# message here); adjust/correct are key-level specifics. Note perceiv and
# percep are BOTH needed: perceived = perce+iv..., perception = perce+p...
CORRECTION_SEMANTIC_STEMS = ("perceiv", "percep", "visib", "adjust", "correct")

# Allowed raw-prey fact family pattern for the snapshot fact segment.
# Self-consistent with the placeholder key naming
# (resolved_snapshot.prey_biomass_density.<prey_class>). When the real
# Resolved Snapshot key table arrives this allowlist MUST be narrowed to
# the real fact families (see README section 6).
SNAPSHOT_FACT_ALLOWLIST = re.compile(
    r"^resolved_snapshot\.(raw_)?prey(_biomass)?(_density)?\.[a-z0-9_]+$")

_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_LETTER_RUN = re.compile(r"[A-Za-z]+")
_U_ESCAPE = re.compile(r"\\u([0-9a-fA-F]{4})")

FAMILY_ORDER = ("TOP", "STRUCT", "SNAP", "COMBINE", "GUARD")

FAMILY_OK = {
    "TOP": "no author-invented top-level sections (no intermediate-dependency surface)",
    "STRUCT": "structure + referential consistency "
              "(fixed row schemas, diet refs, windows, homogeneous units, "
              "prey_field_semantics declared)",
    "SNAP": "snapshot-only sourcing + raw fact-family allowlist "
            "(no Factor output, no correction-semantics key)",
    "COMBINE": "fixed combine constant FILTERED_SUM, author_selectable=false",
    "GUARD": "no excluded semantic stem or zh keyword in any key or value "
             "(stems: %s; zh keywords: %d, table in source)"
             % (", ".join(EXCLUDED_SEMANTIC_STEMS), len(EXCLUDED_SEMANTIC_ZH)),
}


def letter_tokens(text):
    """Split raw text into lowercase word tokens.

    Splits on any non-letter character and additionally on camelCase
    boundaries inside each letter run, so "cover_complexity", "CoverComplexity"
    and "coverComplexity" all yield the token "cover".
    """
    tokens = []
    for run in _LETTER_RUN.findall(text):
        spaced = _CAMEL_BOUNDARY.sub(r"\1 \2", run)
        tokens.extend(part.lower() for part in spaced.split(" ") if part)
    return tokens


def _unescape_u(text):
    """Decode \\uXXXX sequences so escaped Chinese cannot smuggle past
    the substring guard."""
    return _U_ESCAPE.sub(lambda m: chr(int(m.group(1), 16)), text)


def _walk_strings(obj):
    """Yield every key and every string value in a nested dict/list tree."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield key
            yield from _walk_strings(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from _walk_strings(item)
    elif isinstance(obj, str):
        yield obj


def guard_violations(config, raw_text):
    """English stems: token-level prefix match over the raw text.
    Chinese keywords: substring match over walked keys/values, over the raw
    text, and over the \\uXXXX-unescaped raw text (three surfaces so JSON
    escaping cannot smuggle)."""
    hits, seen = [], set()
    for token in letter_tokens(raw_text):
        for stem in EXCLUDED_SEMANTIC_STEMS:
            if token.startswith(stem) and (token, stem) not in seen:
                seen.add((token, stem))
                hits.append(
                    "GUARD: token '%s' matches excluded semantic stem '%s'"
                    % (token, stem))
    zh_surfaces = list(_walk_strings(config)) + [raw_text, _unescape_u(raw_text)]
    for kw in EXCLUDED_SEMANTIC_ZH:
        if any(kw in surface for surface in zh_surfaces):
            hits.append(
                "GUARD: zh keyword '%s' matches excluded semantic keyword" % kw)
    return hits


def _num(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _check_row_keys(v, path, row, allowed):
    unknown = sorted(set(row) - allowed)
    for key in unknown:
        v.append("STRUCT: unknown key '%s' in %s (row schema is fixed: "
                 "%s; key injection is not admitted)"
                 % (key, path, ", ".join(sorted(allowed))))


def validate(config, raw_text):
    """Return a list of violation strings, each prefixed by its family."""
    v = []

    # ---- TOP ------------------------------------------------------------
    for key in sorted(set(config) - ALLOWED_TOP_LEVEL):
        v.append("TOP: unknown top-level field '%s' "
                 "(author-invented sections are not admitted)" % key)

    # ---- STRUCT: identity ------------------------------------------------
    if config.get("schema_version") != EXPECTED["schema_version"]:
        v.append("STRUCT: schema_version must be %r"
                 % EXPECTED["schema_version"])
    contract = config.get("contract")
    if not isinstance(contract, dict):
        v.append("STRUCT: 'contract' must be an object")
        contract = {}
    if contract.get("name") != EXPECTED["contract_name"]:
        v.append("STRUCT: contract.name must be %r"
                 % EXPECTED["contract_name"])
    if contract.get("output_fact") != EXPECTED["output_fact"]:
        v.append("STRUCT: contract.output_fact must be %r"
                 % EXPECTED["output_fact"])
    if contract.get("input_scope") != EXPECTED["input_scope"]:
        v.append("STRUCT: contract.input_scope must be %r "
                 "(single Resolved Snapshot only)" % EXPECTED["input_scope"])
    if contract.get("prey_field_semantics") != EXPECTED["prey_field_semantics"]:
        v.append("STRUCT: contract.prey_field_semantics must be %r "
                 "(prey fields are declared raw; a corrected or perceived "
                 "prey field belongs to another owner)"
                 % EXPECTED["prey_field_semantics"])

    # ---- STRUCT: prey binding table + SNAP sourcing ----------------------
    prey_fields = config.get("prey_fields")
    if not isinstance(prey_fields, list) or not prey_fields:
        v.append("STRUCT: 'prey_fields' must be a non-empty list")
        prey_fields = []
    bound_classes, units = [], set()
    for i, row in enumerate(prey_fields):
        path = "prey_fields[%d]" % i
        if not isinstance(row, dict):
            v.append("STRUCT: %s must be an object" % path)
            continue
        _check_row_keys(v, path, row, ALLOWED_PREY_FIELD_KEYS)
        prey_class = row.get("prey_class")
        if not isinstance(prey_class, str) or not prey_class:
            v.append("STRUCT: %s.prey_class must be a non-empty string" % path)
        elif prey_class in bound_classes:
            v.append("STRUCT: duplicate prey_class '%s'" % prey_class)
        else:
            bound_classes.append(prey_class)
        size = row.get("representative_size_mm")
        if not _num(size) or size <= 0:
            v.append("STRUCT: %s.representative_size_mm must be a number > 0"
                     % path)
        unit = row.get("unit")
        if not isinstance(unit, str) or not unit:
            v.append("STRUCT: %s.unit must be a non-empty string" % path)
        else:
            units.add(unit)
        key = row.get("snapshot_key")
        if not isinstance(key, str) or not key.startswith(SNAPSHOT_KEY_PREFIX):
            v.append("SNAP: %s.snapshot_key must start with '%s' "
                     "(snapshot-only sourcing; a Factor output is not a "
                     "valid input)" % (path, SNAPSHOT_KEY_PREFIX))
        else:
            for token in letter_tokens(key):
                for stem in CORRECTION_SEMANTIC_STEMS:
                    if token.startswith(stem):
                        v.append("SNAP: %s.snapshot_key token '%s' carries "
                                 "correction semantics (stem '%s'); prey "
                                 "fields must be raw_biomass_uncorrected"
                                 % (path, token, stem))
                        break
            if not SNAPSHOT_FACT_ALLOWLIST.match(key):
                v.append("SNAP: %s.snapshot_key fact segment is outside the "
                         "allowed raw-prey fact family (allowlist: %s)"
                         % (path, SNAPSHOT_FACT_ALLOWLIST.pattern))
    if len(units) > 1:
        v.append("STRUCT: prey_fields units must be homogeneous for "
                 "FILTERED_SUM, found %s" % sorted(units))

    # ---- STRUCT: eligibility table + referential consistency -------------
    populations = config.get("population_eligibility")
    if not isinstance(populations, list) or not populations:
        v.append("STRUCT: 'population_eligibility' must be a non-empty list")
        populations = []
    seen_pops = set()
    for i, row in enumerate(populations):
        path = "population_eligibility[%d]" % i
        if not isinstance(row, dict):
            v.append("STRUCT: %s must be an object" % path)
            continue
        _check_row_keys(v, path, row, ALLOWED_ELIGIBILITY_KEYS)
        pid = row.get("population_id")
        if not isinstance(pid, str) or not pid:
            v.append("STRUCT: %s.population_id must be a non-empty string"
                     % path)
        elif pid in seen_pops:
            v.append("STRUCT: duplicate population_id '%s'" % pid)
        else:
            seen_pops.add(pid)
        diet = row.get("diet_classes")
        # An EMPTY diet_classes is legal and meaningful: it explicitly
        # states zero overlap between this population's diet and the bound
        # prey classes (fact produced, value 0). It is distinct from the
        # row being absent (population outside contract coverage).
        if not isinstance(diet, list):
            v.append("STRUCT: %s.diet_classes must be a list "
                     "(empty list = explicit zero overlap)" % path)
            diet = []
        if len(diet) != len(set(diet)):
            v.append("STRUCT: %s.diet_classes contains duplicates" % path)
        for prey_class in diet:
            if prey_class not in bound_classes:
                v.append("STRUCT: %s.diet_classes references prey_class '%s' "
                         "not bound in prey_fields (referential consistency)"
                         % (path, prey_class))
        window = row.get("size_window_mm")
        if not isinstance(window, dict):
            v.append("STRUCT: %s.size_window_mm must be an object {min, max}"
                     % path)
        else:
            unknown_w = sorted(set(window) - ALLOWED_WINDOW_KEYS)
            for key in unknown_w:
                v.append("STRUCT: unknown key '%s' in %s.size_window_mm "
                         "(window schema is fixed: min, max)" % (key, path))
            lo, hi = window.get("min"), window.get("max")
            if not _num(lo) or lo < 0:
                v.append("STRUCT: %s.size_window_mm.min must be a number >= 0"
                         % path)
            if not _num(hi):
                v.append("STRUCT: %s.size_window_mm.max must be a number"
                         % path)
            if _num(lo) and _num(hi) and not lo < hi:
                v.append("STRUCT: %s.size_window_mm must satisfy min < max"
                         % path)

    # ---- COMBINE ----------------------------------------------------------
    combine = config.get("fixed_combine")
    if not isinstance(combine, dict):
        v.append("COMBINE: 'fixed_combine' must be an object")
    else:
        if combine.get("operator") != EXPECTED["combine_operator"]:
            v.append("COMBINE: fixed_combine.operator must be %r "
                     "(combine is a contract constant, not author-selectable)"
                     % EXPECTED["combine_operator"])
        if combine.get("author_selectable") is not False:
            v.append("COMBINE: fixed_combine.author_selectable must be false")

    # ---- GUARD -------------------------------------------------------------
    v.extend(guard_violations(config, raw_text))
    return v


def report(violations, source):
    print("== %s ==" % source)
    for family in FAMILY_ORDER:
        family_hits = [x for x in violations if x.startswith(family + ":")]
        if family_hits:
            for hit in family_hits:
                print("[FAIL] " + hit)
        else:
            print("[OK]   %-6s %s" % (family, FAMILY_OK[family]))
    print("== result ==")
    if violations:
        print("FAIL (%d violation(s))" % len(violations))
        return 1
    print("PASS (%d check families, 0 violations)" % len(FAMILY_ORDER))
    return 0


# --------------------------------------------------------------------------
# Selftest: prove each check family actually fires on a bad input, and that
# every single stem / zh keyword in the guard tables has at least one firing
# probe (a misspelled table entry would otherwise fail silently).
# --------------------------------------------------------------------------

def _base_config():
    return {
        "schema_version": "usable_forage.config.r1",
        "instance": {
            "instance_of": "UsableForageAvailability semantic contract, representation r1",
            "example_population_id": "largemouth_bass_adult_summer",
            "note": "selftest fixture",
        },
        "contract": {
            "name": "UsableForageAvailability",
            "output_fact": "usable_forage_availability",
            "grain": "population x cell",
            "semantics": "selftest fixture semantics",
            "input_scope": "resolved_snapshot_only",
            "prey_field_semantics": "raw_biomass_uncorrected",
        },
        "prey_fields": [
            {"prey_class": "fish",
             "snapshot_key": "resolved_snapshot.prey_biomass_density.fish",
             "representative_size_mm": 80.0, "unit": "g_per_m2"},
            {"prey_class": "crayfish",
             "snapshot_key": "resolved_snapshot.prey_biomass_density.crayfish",
             "representative_size_mm": 60.0, "unit": "g_per_m2"},
        ],
        "population_eligibility": [
            {"population_id": "largemouth_bass_adult_summer",
             "diet_classes": ["fish", "crayfish"],
             "size_window_mm": {"min": 30.0, "max": 300.0}},
        ],
        "fixed_combine": {
            "operator": "FILTERED_SUM",
            "author_selectable": False,
            "rule": "selftest fixture rule",
        },
    }


# One real word per guard stem: each probe proves its stem fires.
STEM_PROBES = {
    "cover": "cover", "visib": "visible", "captur": "capture",
    "geometr": "geometry", "energ": "energy",
    "refuge": "refuge", "shelter": "shelter", "hid": "hidden",
    "ambush": "ambush", "structur": "structure", "safe": "safety",
    "risk": "risk", "conceal": "concealment",
    "detectab": "detectable", "perceiv": "perceived", "percep": "perception",
    "reach": "reachable",
    "conspicu": "conspicuous", "turbid": "turbidity", "see": "seen",
    "catch": "catches", "grasp": "grasp", "encounter": "encounter",
    "cost": "costly", "handl": "handling",
}

# One probe per zh keyword (each probe contains its keyword as a substring).
ZH_KEYWORD_PROBES = (
    "躲避", "藏匿", "庇护所", "掩体", "结构", "安全", "风险", "埋伏",
    "可见", "察觉", "感知", "修正", "浑浊", "抓捕", "捕获", "遭遇", "代价", "成本",
)


def _selftest():
    cases = []

    def case(name, mutate, expect_family):
        cfg = _base_config()
        mutate(cfg)
        cases.append((name, cfg, expect_family))

    # -- baselines & legal variants --------------------------------------
    case("baseline fixture passes unchanged", lambda c: None, None)
    case("zero-overlap population (empty diet_classes) is a legal explicit row",
         lambda c: c["population_eligibility"].append(
             {"population_id": "bluegill_juvenile_winter",
              "diet_classes": [],
              "size_window_mm": {"min": 1.0, "max": 20.0}}),
         None)
    case("raw_ prefixed fact family passes the snapshot allowlist",
         lambda c: c["prey_fields"][0].update(
             {"snapshot_key":
              "resolved_snapshot.raw_prey_biomass_density.fish"}),
         None)

    # -- GUARD: every English stem gets a firing probe --------------------
    for stem in sorted(STEM_PROBES):
        probe = STEM_PROBES[stem]

        def mutate(c, probe=probe):
            c["instance"]["note"] = (
                c["instance"]["note"] + " plus " + probe + " discount")
        case("GUARD fires on stem '%s' (probe '%s')" % (stem, probe),
             mutate, "GUARD")

    # -- GUARD: every Chinese keyword gets a firing probe ------------------
    # json.dumps below uses ensure_ascii=True on purpose: the raw text then
    # carries the keyword only in \uXXXX-escaped form, so these cases also
    # prove the unescape surface of the zh guard.
    for kw in ZH_KEYWORD_PROBES:

        def mutate(c, kw=kw):
            c["instance"]["note"] = (
                c["instance"]["note"] + " modifier " + kw)
        case("GUARD fires on zh keyword '%s'" % kw, mutate, "GUARD")

    # -- GUARD: structural smuggling shapes (from r0; expectations updated
    #    where the r1 fixed-row-schema check co-fires) ---------------------
    case("GUARD fires on key with cover stem (snake_case; row allowlist co-fires)",
         lambda c: c["prey_fields"][0].update({"cover_bonus": 1.0}),
         {"GUARD", "STRUCT"})
    case("GUARD fires on value with visib stem",
         lambda c: c["contract"].update(
             {"semantics": "discounted by water visibility"}),
         "GUARD")
    case("GUARD fires on camelCase token (CoverComplexity)",
         lambda c: c["instance"].update(
             {"note": "plus CoverComplexity adjustment"}),
         "GUARD")
    case("GUARD fires on captur stem inside combine rule text",
         lambda c: c["fixed_combine"].update(
             {"rule": "sum, then capture weighting"}),
         "GUARD")
    case("GUARD fires on geometr stem in a value",
         lambda c: c["instance"].update(
             {"note": "includes attack geometry"}),
         "GUARD")
    case("GUARD fires on energ stem in a key (row allowlist co-fires)",
         lambda c: c["prey_fields"][0].update({"energy_density": 1.0}),
         {"GUARD", "STRUCT"})

    # -- STRUCT: fixed row schemas (r1) ------------------------------------
    case("STRUCT fires on unknown key inside a prey_fields row",
         lambda c: c["prey_fields"][0].update({"trophic_weight": 1.0}),
         "STRUCT")
    case("STRUCT fires on unknown key inside an eligibility row",
         lambda c: c["population_eligibility"][0].update(
             {"season_note": "winter"}),
         "STRUCT")
    case("STRUCT fires on unknown key inside size_window_mm",
         lambda c: c["population_eligibility"][0]["size_window_mm"].update(
             {"skew": 0.1}),
         "STRUCT")
    case("STRUCT fires on prey_field_semantics drift",
         lambda c: c["contract"].update(
             {"prey_field_semantics": "legacy_biomass_mode"}),
         "STRUCT")
    case("STRUCT fires on missing prey_field_semantics",
         lambda c: c["contract"].pop("prey_field_semantics"),
         "STRUCT")

    # -- STRUCT: referential consistency (from r0) --------------------------
    case("STRUCT fires on diet class not bound in prey_fields",
         lambda c: c["population_eligibility"][0].update(
             {"diet_classes": ["fish", "crayfish", "shiner"]}),
         "STRUCT")
    case("STRUCT fires on inverted size window (min >= max)",
         lambda c: c["population_eligibility"][0].update(
             {"size_window_mm": {"min": 400.0, "max": 300.0}}),
         "STRUCT")
    case("STRUCT fires on heterogeneous units",
         lambda c: c["prey_fields"][1].update({"unit": "kcal_per_m2"}),
         "STRUCT")

    # -- SNAP: raw fact-family allowlist (r1) -------------------------------
    case("SNAP fires on correction-semantics stem in a snapshot key "
         "(GUARD perceiv co-fires)",
         lambda c: c["prey_fields"][0].update(
             {"snapshot_key":
              "resolved_snapshot.prey_biomass_density_perceived.fish"}),
         {"GUARD", "SNAP"})
    case("SNAP fires on correction-semantics stem 'correct' in a snapshot key "
         "(key-level only, not in the global guard table)",
         lambda c: c["prey_fields"][0].update(
             {"snapshot_key":
              "resolved_snapshot.prey_biomass_density_corrected.fish"}),
         {"SNAP"})
    case("SNAP fires on fact segment outside the allowed raw-prey family",
         lambda c: c["prey_fields"][0].update(
             {"snapshot_key": "resolved_snapshot.temperature.fish"}),
         "SNAP")

    # -- SNAP: sourcing (from r0) -------------------------------------------
    case("SNAP fires on Factor-output sourcing",
         lambda c: c["prey_fields"][0].update(
             {"snapshot_key": "factor.prey_fit.output"}),
         "SNAP")

    # -- COMBINE / TOP (from r0) ---------------------------------------------
    case("COMBINE fires on author-chosen operator",
         lambda c: c["fixed_combine"].update({"operator": "WEIGHTED_PRODUCT"}),
         "COMBINE")
    case("TOP fires on author-invented steps section",
         lambda c: c.update({"steps": [{"id": "s1", "depends_on": ["s0"]}]}),
         "TOP")

    failures = 0
    print("== selftest ==")
    for name, cfg, expect_family in cases:
        raw = json.dumps(cfg)  # ensure_ascii=True on purpose (see zh cases)
        violations = validate(cfg, raw)
        families = {x.split(":", 1)[0] for x in violations}
        if expect_family is None:
            ok = not violations
            detail = "expected 0 violations, got %s" % (sorted(families) or "none")
        elif isinstance(expect_family, (set, frozenset)):
            expect = set(expect_family)
            ok = families == expect
            detail = "expected families %s, got %s" % (
                sorted(expect), sorted(families) or "none")
        else:
            ok = families == {expect_family}
            detail = "expected family %s only, got %s" % (
                expect_family, sorted(families) or "none")
        status = "OK  " if ok else "FAIL"
        if not ok:
            failures += 1
        print("[%s] %-70s %s" % (status, name, "" if ok else detail))
    print("== result ==")
    if failures:
        print("SELFTEST FAIL (%d case(s) mismatched)" % failures)
        return 1
    print("SELFTEST PASS (%d cases)" % len(cases))
    return 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        # keep redirected output utf-8 regardless of console codepage
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("config_path", nargs="?",
                        help="path to usable_forage.config.json")
    parser.add_argument("--selftest", action="store_true",
                        help="run embedded detector selftest (no file needed)")
    args = parser.parse_args(argv)
    if args.selftest:
        return _selftest()
    if not args.config_path:
        parser.error("provide a config path or --selftest")
    with open(args.config_path, "r", encoding="utf-8") as handle:
        raw_text = handle.read()
    try:
        config = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        print("[FAIL] STRUCT: config is not valid JSON: %s" % exc)
        print("== result ==")
        print("FAIL (1 violation(s))")
        return 1
    if not isinstance(config, dict):
        print("[FAIL] STRUCT: config root must be a JSON object")
        print("== result ==")
        print("FAIL (1 violation(s))")
        return 1
    return report(validate(config, raw_text), args.config_path)


if __name__ == "__main__":
    sys.exit(main())
