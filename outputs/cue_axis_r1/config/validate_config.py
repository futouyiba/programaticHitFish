#!/usr/bin/env python3
"""validate_config.py — structural validator + semantic boundary guard
for the Presentation Cue axis modal expansion config artifact (r1).

Pure standard library (argparse / json / re / sys). Exit 0 = pass, 1 = fail.

Check families:
  TOP     top-level field allowlist: the config admits no author-invented
          sections, so there is no surface for author-editable intermediate
          dependencies (steps / depends_on / axis-pairing sections).
  STRUCT  structural shape + referential consistency: identity fields pinned;
          fixed row schemas for profile_slots / fact_atoms / instances /
          lookup-table / contract / combine rows (unknown keys inside a row
          fail); slot fact_atoms must be declared in the fact_atoms table;
          instance bound_slot must reference a declared slot; every declared
          slot must be bound by at least one instance row.
  AXIS    axis admission: the two cue axes are Unary Profile lookups at the
          P0 stage of the Primitive Admission Ladder (Knife §11) and nothing
          else. Fires on: arity drift, a fact_atom that is a list (two input
          axes) or a Profile reference (nesting), ladder-stage drift, an
          unknown or missing slot in the closed slot set, the same fact
          feeding two slots, key names suggesting a second / pairing axis,
          and a lookup-table input referencing another Profile (nested
          lookup). This is the "unary only, no nesting, no 2D" verify.
  FACT    closed fact enum: fact_atom values must be exactly the two
          batch-admitted presentation-side computed facts
          (BaitScentIntensity / LureElectricField); grammar_form must be the
          Grammar 5.1 V2/V3 reuse declaration; columns_added must be 0
          (zero new columns); computed_by must be presentation-side.
  COMBINE fixed combine: operator pinned to FIXED_COMBINE, operator_math
          pinned to UNDEFINED (the combine math is a mechanism-side open
          item per live §17.2 operator annotation; this artifact freezes
          only the boundary: parallel Fit input into the existing RR-T1
          channel, no new channel, no new topology), author_selectable
          false.
  GUARD   boundary guard: excluded semantics must not appear as ANY key or
          value anywhere in the config text. Fail-closed English stem list
          (token-level prefix matching over camelCase-split letter runs)
          plus a Chinese keyword list (substring matching over keys and
          values, and over the raw text in both literal and \\uXXXX-escaped
          form). Exclusion families for THIS batch (per REP-CUE-AXIS-001):
          capture / attack / strike and the incapacitation family
          (麻痹 = paralysis, 冻结 = freeze, plus the electric-discharge
          variants 电击/击晕 etc.) — those semantics belong to the
          Encounter / Conversion owner (story #47 boundary: the electro
          axis carries sensing only). This guard is a LEXICAL PROXY for
          the semantic exclusion promise, not the promise itself: the
          tables cannot be exhaustive (residual risk: a synonym not in
          the tables passes; found ones extend the tables).

NOT AUTHORITY. Passing this validator is a representation-shape check only.
It is not mechanism promotion, not a Freeze, and not a runtime enforcement.

Usage:
  python validate_config.py <path/to/cue_axis.config.json>
  python validate_config.py --selftest
"""

from __future__ import annotations

import argparse
import json
import re
import sys

EXPECTED = {
    "schema_version": "cue_axis.config.r1",
    "contract_name": "PresentationCueAxisModalExpansion",
    "contract_surface": "Response",
    "output_facts": ["ScentCueFit", "ElectroFieldCueFit"],
    "input_scope": "presentation_side_computed_facts_only",
    "axis_semantics": "unary_profile_lookup_only",
    "modality_boundary": "sensing and trigger adaptation only",
    "grammar_form": "Grammar 5.1 V2/V3 reuse",
    "columns_added": 0,
    "computed_by": "presentation_side_computed_fact",
    "ladder_stage": "P0_unary_profile_lookup",
    "arity": "unary",
    "combine_into": "existing RR-T1 channel FIXED_COMBINE",
    "combine_operator": "FIXED_COMBINE",
    "combine_math": "UNDEFINED",
    "combine_joins": ("each axis Fit enters the existing RR-T1 "
                      "Feeding / Reaction channel fixed combine as one "
                      "parallel input; no new channel and no new combine "
                      "topology"),
}

# Closed admission sets for THIS batch (two axes, two facts). Extending the
# sets is a new spec/batch action, not an author action.
SLOT_ENUM = ("@ScentCueProfile", "@ElectroFieldProfile")
FACT_ENUM = ("BaitScentIntensity", "LureElectricField")
SLOT_MODALITY = {
    "@ScentCueProfile": "chemical_scent",
    "@ElectroFieldProfile": "electric_field_sensing",
}

ALLOWED_TOP_LEVEL = {
    "schema_version", "instance", "contract",
    "profile_slots", "fact_atoms", "instances", "combine",
}

# Fixed row schemas: no key injection inside table rows.
ALLOWED_INSTANCE_META_KEYS = {"instance_of", "example_instances", "note"}
ALLOWED_CONTRACT_KEYS = {
    "name", "surface", "output_facts", "grain", "semantics",
    "input_scope", "axis_semantics", "modality_boundary",
}
ALLOWED_SLOT_KEYS = {
    "slot", "meaning", "axis_modality", "arity", "fact_atom",
    "ladder_stage", "combine_into",
}
ALLOWED_FACT_KEYS = {
    "fact_atom", "grammar_form", "columns_added", "fact_semantics",
    "computed_by",
}
ALLOWED_INSTANCE_KEYS = {
    "population_id", "bound_slot", "profile_instance",
    "example_lookup_table",
}
ALLOWED_LOOKUP_KEYS = {"input", "fit"}
ALLOWED_COMBINE_KEYS = {
    "operator", "operator_math", "joins", "author_selectable", "rule",
}

# Boundary guard keyword stems (English). Deliberately conservative
# (fail-closed): a token starting with any stem is a violation even if the
# full word is innocent-looking, because nothing in this contract
# legitimately needs these semantics. Organized by the exclusion families
# named for THIS batch:
#   capture family        capture/catch/grasp/encounter/seize/hook/swallow/
#                         bite (owner: Encounter / Conversion)
#   attack family         attack/strike/kill
#   incapacitation family paralysis/stun/frozen/electrocution/shock/
#                         immobilize + the freeze variants (麻痹/冻结 in zh;
#                         story #47 remote-incapacitation boundary)
EXCLUDED_SEMANTIC_STEMS = (
    # capture family
    "captur", "catch", "grasp", "encounter", "seiz", "hook", "swallow",
    "bit",
    # attack family
    "attack", "strike", "kill",
    # incapacitation family. Note freez AND froz are BOTH needed:
    # freeze/freezing = freez+..., frozen/froze = froz+... (single-stem
    # morphology misses one of the two forms).
    "paraly", "stun", "freez", "froz", "electrocut", "shock", "immobil",
)

# Boundary guard keywords (Chinese), substring-matched. Chinese has no
# word segmentation in config text, so substring matching over the full
# key/value surface is the fail-closed choice. Families mirror the English
# stems. Single-character entries (抓/咬/吞/钩/扑/杀) over-match any
# compound containing the character; accepted by fail-closed design
# because this config's legitimate Chinese content is only the two
# Profile meaning strings and the two fact semantics strings, none of
# which uses these characters.
EXCLUDED_SEMANTIC_ZH = (
    # capture family
    "捕获", "抓", "遭遇", "咬", "吞", "钩",
    # attack family
    "攻击", "袭击", "扑", "杀",
    # incapacitation family
    "麻痹", "冻结", "电击", "击晕", "眩晕", "麻木", "制服",
)

# Key shapes that suggest a second / pairing input axis inside a slot row.
# The structural row allowlist already fails unknown keys (STRUCT); these
# shapes additionally fire AXIS because they are the 2D / pairing surface
# this batch explicitly does not admit.
_SECOND_AXIS_KEY = re.compile(
    r"(?i)(pair|2d|second|cross|input_?2|interaction)")

_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_LETTER_RUN = re.compile(r"[A-Za-z]+")
_U_ESCAPE = re.compile(r"\\u([0-9a-fA-F]{4})")

FAMILY_ORDER = ("TOP", "STRUCT", "AXIS", "FACT", "COMBINE", "GUARD")

FAMILY_OK = {
    "TOP": "no author-invented top-level sections (no intermediate-dependency "
           "or axis-pairing surface)",
    "STRUCT": "structure + referential consistency (identity pinned, fixed "
              "row schemas, declared facts/slots, every slot bound)",
    "AXIS": "unary-only axis admission (closed slot set, single fact atom, "
            "P0 stage, no nesting, no second axis, no 2D)",
    "FACT": "closed fact enum (2 presentation-side computed facts, Grammar "
            "5.1 V2/V3 reuse, zero new columns)",
    "COMBINE": "FIXED_COMBINE into existing RR-T1 channel, operator_math "
               "UNDEFINED, author_selectable=false",
    "GUARD": "no excluded semantic stem or zh keyword in any key or value "
             "(capture/attack/incapacitation families; stems: %s; "
             "zh keywords: %d, table in source)"
             % (", ".join(EXCLUDED_SEMANTIC_STEMS), len(EXCLUDED_SEMANTIC_ZH)),
}


def letter_tokens(text):
    """Split raw text into lowercase word tokens.

    Splits on any non-letter character and additionally on camelCase
    boundaries inside each letter run, so "capture_window", "CaptureWindow"
    and "captureWindow" all yield the token "capture".
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
    return unknown


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
    _check_row_keys(v, "contract", contract, ALLOWED_CONTRACT_KEYS)
    if contract.get("name") != EXPECTED["contract_name"]:
        v.append("STRUCT: contract.name must be %r"
                 % EXPECTED["contract_name"])
    if contract.get("surface") != EXPECTED["contract_surface"]:
        v.append("STRUCT: contract.surface must be %r"
                 % EXPECTED["contract_surface"])
    if contract.get("output_facts") != EXPECTED["output_facts"]:
        v.append("STRUCT: contract.output_facts must be %r"
                 % (EXPECTED["output_facts"],))
    if contract.get("input_scope") != EXPECTED["input_scope"]:
        v.append("STRUCT: contract.input_scope must be %r "
                 "(presentation-side computed facts only)"
                 % EXPECTED["input_scope"])
    if contract.get("axis_semantics") != EXPECTED["axis_semantics"]:
        v.append("STRUCT: contract.axis_semantics must be %r "
                 "(the axes are unary profile lookups, nothing else)"
                 % EXPECTED["axis_semantics"])
    if contract.get("modality_boundary") != EXPECTED["modality_boundary"]:
        v.append("STRUCT: contract.modality_boundary must be %r "
                 "(outcome semantics belong to another owner)"
                 % EXPECTED["modality_boundary"])
    meta = config.get("instance")
    if isinstance(meta, dict):
        _check_row_keys(v, "instance", meta, ALLOWED_INSTANCE_META_KEYS)

    # ---- STRUCT + AXIS: profile slot table --------------------------------
    slots = config.get("profile_slots")
    if not isinstance(slots, list) or not slots:
        v.append("STRUCT: 'profile_slots' must be a non-empty list")
        slots = []
    slot_names, slot_facts = [], {}
    for i, row in enumerate(slots):
        path = "profile_slots[%d]" % i
        if not isinstance(row, dict):
            v.append("STRUCT: %s must be an object" % path)
            continue
        unknown = _check_row_keys(v, path, row, ALLOWED_SLOT_KEYS)
        for key in unknown:
            if _SECOND_AXIS_KEY.search(key):
                v.append("AXIS: key '%s' in %s suggests a second / pairing "
                         "input axis; cue axes are admitted as unary P0 "
                         "lookups only (no 2D)" % (key, path))
        slot = row.get("slot")
        if not isinstance(slot, str) or not slot:
            v.append("STRUCT: %s.slot must be a non-empty string" % path)
        elif slot in slot_names:
            v.append("STRUCT: duplicate slot '%s'" % slot)
        else:
            slot_names.append(slot)
            if slot not in SLOT_ENUM:
                v.append("AXIS: slot '%s' is outside the closed slot set %s "
                         "(admitting a new axis is a spec action, not an "
                         "author action)" % (slot, list(SLOT_ENUM)))
        if slot in SLOT_ENUM:
            expected_modality = SLOT_MODALITY.get(slot)
            if row.get("axis_modality") != expected_modality:
                v.append("AXIS: slot '%s' axis_modality must be %r"
                         % (slot, expected_modality))
        if row.get("arity") != EXPECTED["arity"]:
            v.append("AXIS: slot '%s' arity must be %r (unary lookup only; "
                     "a second input axis is not admitted)"
                     % (slot, EXPECTED["arity"]))
        if row.get("ladder_stage") != EXPECTED["ladder_stage"]:
            v.append("AXIS: slot '%s' ladder_stage must be %r "
                     "(Primitive Admission Ladder P0; typed 2D is P1 and is "
                     "not admitted for these axes)"
                     % (slot, EXPECTED["ladder_stage"]))
        if row.get("combine_into") != EXPECTED["combine_into"]:
            v.append("AXIS: slot '%s' combine_into must be %r "
                     "(the Fit joins the existing channel; it does not open "
                     "a new one)" % (slot, EXPECTED["combine_into"]))
        fact = row.get("fact_atom")
        if isinstance(fact, list):
            v.append("AXIS: %s.fact_atom must be a single fact atom string, "
                     "not a list (multiple input axes = not unary)" % path)
        else:
            if isinstance(fact, str) and fact.startswith("@"):
                v.append("AXIS: %s.fact_atom '%s' references a Profile; the "
                         "lookup input must be a fact atom, not another "
                         "Profile's output (no nested lookup)"
                         % (path, fact))
            if not isinstance(fact, str) or not fact:
                v.append("STRUCT: %s.fact_atom must be a non-empty string"
                         % path)
            slot_facts[slot] = fact

    for slot in SLOT_ENUM:
        if slot not in slot_names:
            v.append("AXIS: declared slot '%s' is missing from "
                     "profile_slots (the batch ships both axes)" % slot)
    fact_loads = {}
    for slot, fact in slot_facts.items():
        fact_loads.setdefault(fact, []).append(slot)
    for fact, fed_slots in sorted(fact_loads.items()):
        if isinstance(fact, str) and len(fed_slots) > 1:
            v.append("AXIS: fact atom '%s' feeds more than one slot (%s); "
                     "one fact, one unary axis (this batch's admitted shape)"
                     % (fact, ", ".join(sorted(fed_slots))))

    # ---- STRUCT + FACT: fact atom table ------------------------------------
    facts = config.get("fact_atoms")
    if not isinstance(facts, list) or not facts:
        v.append("STRUCT: 'fact_atoms' must be a non-empty list")
        facts = []
    declared_facts = []
    for i, row in enumerate(facts):
        path = "fact_atoms[%d]" % i
        if not isinstance(row, dict):
            v.append("STRUCT: %s must be an object" % path)
            continue
        _check_row_keys(v, path, row, ALLOWED_FACT_KEYS)
        fact = row.get("fact_atom")
        if not isinstance(fact, str) or not fact:
            v.append("STRUCT: %s.fact_atom must be a non-empty string" % path)
        else:
            if fact in declared_facts:
                v.append("STRUCT: duplicate fact_atom '%s'" % fact)
            else:
                declared_facts.append(fact)
            if fact not in FACT_ENUM:
                v.append("FACT: fact atom '%s' is outside the closed enum %s "
                         "(new cue facts are a spec action, not an author "
                         "action)" % (fact, list(FACT_ENUM)))
        if row.get("grammar_form") != EXPECTED["grammar_form"]:
            v.append("FACT: %s.grammar_form must be %r (Grammar 5.1 column "
                     "structure reuse, no new column structure)"
                     % (path, EXPECTED["grammar_form"]))
        if row.get("columns_added") != EXPECTED["columns_added"]:
            v.append("FACT: %s.columns_added must be %d (zero new columns: "
                     "the facts ride the existing V2/V3 condition-atom "
                     "column variants)" % (path, EXPECTED["columns_added"]))
        if row.get("computed_by") != EXPECTED["computed_by"]:
            v.append("FACT: %s.computed_by must be %r (the intensity / "
                     "field feature is computed upstream on the "
                     "presentation side, not here)"
                     % (path, EXPECTED["computed_by"]))
    for fact in FACT_ENUM:
        if fact not in declared_facts:
            v.append("FACT: declared fact '%s' is missing from fact_atoms "
                     "(the batch ships both facts)" % fact)
    for slot, fact in slot_facts.items():
        if isinstance(fact, str) and fact not in declared_facts:
            v.append("STRUCT: slot '%s' binds fact_atom '%s' which is not "
                     "declared in fact_atoms (referential consistency)"
                     % (slot, fact))

    # ---- STRUCT + AXIS: instance bindings + example lookup tables ----------
    instances = config.get("instances")
    if not isinstance(instances, list) or not instances:
        v.append("STRUCT: 'instances' must be a non-empty list")
        instances = []
    bound_pairs, bound_slots = set(), set()
    for i, row in enumerate(instances):
        path = "instances[%d]" % i
        if not isinstance(row, dict):
            v.append("STRUCT: %s must be an object" % path)
            continue
        _check_row_keys(v, path, row, ALLOWED_INSTANCE_KEYS)
        pid = row.get("population_id")
        if not isinstance(pid, str) or not pid:
            v.append("STRUCT: %s.population_id must be a non-empty string"
                     % path)
        slot = row.get("bound_slot")
        if not isinstance(slot, str) or slot not in slot_names:
            v.append("STRUCT: %s.bound_slot must be one of the slots "
                     "declared in profile_slots (%s)"
                     % (path, list(SLOT_ENUM)))
        else:
            bound_slots.add(slot)
            if (pid, slot) in bound_pairs:
                v.append("STRUCT: duplicate binding (population '%s', slot "
                         "'%s')" % (pid, slot))
            bound_pairs.add((pid, slot))
        profile = row.get("profile_instance")
        if not isinstance(profile, str) or not profile.startswith("@"):
            v.append("STRUCT: %s.profile_instance must be a Profile name "
                     "starting with '@'" % path)
        table = row.get("example_lookup_table")
        if not isinstance(table, list) or not table:
            v.append("STRUCT: %s.example_lookup_table must be a non-empty "
                     "list" % path)
            table = []
        for j, entry in enumerate(table):
            epath = "%s.example_lookup_table[%d]" % (path, j)
            if not isinstance(entry, dict):
                v.append("STRUCT: %s must be an object" % epath)
                continue
            _check_row_keys(v, epath, entry, ALLOWED_LOOKUP_KEYS)
            entry_input = entry.get("input")
            if not isinstance(entry_input, str) or not entry_input:
                v.append("STRUCT: %s.input must be a non-empty string "
                         "(a fact band label)" % epath)
            elif entry_input.startswith("@"):
                v.append("AXIS: %s.input '%s' references a Profile; the "
                         "lookup table maps fact bands to Fit values, it "
                         "cannot consume another Profile's output (no "
                         "nested lookup)" % (epath, entry_input))
            if not _num(entry.get("fit")):
                v.append("STRUCT: %s.fit must be a number (placeholder, "
                         "not frozen)" % epath)
    for slot in slot_names:
        if slot not in bound_slots:
            v.append("STRUCT: declared slot '%s' has no instance binding "
                     "(every shipped slot row is bound by at least one "
                     "example instance)" % slot)

    # ---- COMBINE ------------------------------------------------------------
    combine = config.get("combine")
    if not isinstance(combine, dict):
        v.append("COMBINE: 'combine' must be an object")
    else:
        _check_row_keys(v, "combine", combine, ALLOWED_COMBINE_KEYS)
        if combine.get("operator") != EXPECTED["combine_operator"]:
            v.append("COMBINE: combine.operator must be %r (the axes join "
                     "the existing channel's fixed combine; this is not an "
                     "author choice)" % EXPECTED["combine_operator"])
        if combine.get("operator_math") != EXPECTED["combine_math"]:
            v.append("COMBINE: combine.operator_math must be %r (the "
                     "combine math is a mechanism-side open item and must "
                     "stay visibly undefined, not silently defined here)"
                     % EXPECTED["combine_math"])
        if combine.get("author_selectable") is not False:
            v.append("COMBINE: combine.author_selectable must be false")
        if combine.get("joins") != EXPECTED["combine_joins"]:
            v.append("COMBINE: combine.joins must state the pinned "
                     "joins declaration (existing RR-T1 channel fixed "
                     "combine, one parallel input, no new channel)")

    # ---- GUARD ---------------------------------------------------------------
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
            print("[OK]   %-7s %s" % (family, FAMILY_OK[family]))
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
        "schema_version": "cue_axis.config.r1",
        "instance": {
            "instance_of": "Presentation Cue axis modal expansion "
                           "semantic contract, representation r1",
            "example_instances": ["selftest fixture"],
            "note": "selftest fixture",
        },
        "contract": {
            "name": "PresentationCueAxisModalExpansion",
            "surface": "Response",
            "output_facts": ["ScentCueFit", "ElectroFieldCueFit"],
            "grain": "population x current presentation",
            "semantics": "selftest fixture semantics",
            "input_scope": "presentation_side_computed_facts_only",
            "axis_semantics": "unary_profile_lookup_only",
            "modality_boundary": "sensing and trigger adaptation only",
        },
        "profile_slots": [
            {"slot": "@ScentCueProfile",
             "meaning": "味型/信息素强度→触发适配",
             "axis_modality": "chemical_scent",
             "arity": "unary",
             "fact_atom": "BaitScentIntensity",
             "ladder_stage": "P0_unary_profile_lookup",
             "combine_into": "existing RR-T1 channel FIXED_COMBINE"},
            {"slot": "@ElectroFieldProfile",
             "meaning": "拟饵/环境电场特征→触发适配",
             "axis_modality": "electric_field_sensing",
             "arity": "unary",
             "fact_atom": "LureElectricField",
             "ladder_stage": "P0_unary_profile_lookup",
             "combine_into": "existing RR-T1 channel FIXED_COMBINE"},
        ],
        "fact_atoms": [
            {"fact_atom": "BaitScentIntensity",
             "grammar_form": "Grammar 5.1 V2/V3 reuse",
             "columns_added": 0,
             "fact_semantics": "当前呈现的味型/信息素强度（上游呈现侧计算事实）",
             "computed_by": "presentation_side_computed_fact"},
            {"fact_atom": "LureElectricField",
             "grammar_form": "Grammar 5.1 V2/V3 reuse",
             "columns_added": 0,
             "fact_semantics": "拟饵电场特征（上游呈现侧计算事实）",
             "computed_by": "presentation_side_computed_fact"},
        ],
        "instances": [
            {"population_id": "sea_lamprey_migratory_spring",
             "bound_slot": "@ScentCueProfile",
             "profile_instance": "@SeaLampreyMigratoryScentCue",
             "example_lookup_table": [
                 {"input": "none", "fit": 0.0},
                 {"input": "moderate_bait_scent", "fit": 0.5},
                 {"input": "strong_spawning_pheromone", "fit": 1.0},
             ]},
            {"population_id": "electric_eel_sensing",
             "bound_slot": "@ElectroFieldProfile",
             "profile_instance": "@ElectricEelElectroSense",
             "example_lookup_table": [
                 {"input": "no_field", "fit": 0.0},
                 {"input": "strong_field", "fit": 1.0},
             ]},
        ],
        "combine": {
            "operator": "FIXED_COMBINE",
            "operator_math": "UNDEFINED",
            "joins": ("each axis Fit enters the existing RR-T1 "
                      "Feeding / Reaction channel fixed combine as one "
                      "parallel input; no new channel and no new combine "
                      "topology"),
            "author_selectable": False,
            "rule": "selftest fixture rule",
        },
    }


# One real word per guard stem: each probe proves its stem fires.
STEM_PROBES = {
    "captur": "capture", "catch": "catches", "grasp": "grasps",
    "encounter": "encounters", "seiz": "seizes", "hook": "hooked",
    "swallow": "swallowing", "bit": "bites", "attack": "attack",
    "strike": "strikes", "kill": "kills", "paraly": "paralysis",
    "stun": "stunned", "freez": "freezing", "froz": "frozen",
    "electrocut": "electrocution", "shock": "shock", "immobil": "immobilized",
}

# One probe per zh keyword (each probe contains its keyword as a substring).
ZH_KEYWORD_PROBES = (
    "捕获", "抓取", "遭遇", "咬住", "吞下", "上钩", "攻击", "袭击",
    "扑咬", "击杀", "麻痹", "冻结", "电击", "击晕", "眩晕", "麻木", "制服",
)


def _selftest():
    cases = []

    def case(name, mutate, expect_family):
        cfg = _base_config()
        mutate(cfg)
        cases.append((name, cfg, expect_family))

    # -- baselines & legal variants ----------------------------------------
    case("baseline fixture passes unchanged", lambda c: None, None)
    case("a second population may bind the same slot (slot is reusable)",
         lambda c: c["instances"].append(
             {"population_id": "crucian_carp_pond_scent",
              "bound_slot": "@ScentCueProfile",
              "profile_instance": "@CrucianPondScentCue",
              "example_lookup_table": [
                  {"input": "none", "fit": 0.0},
                  {"input": "moderate_bait_scent", "fit": 0.4}]}),
         None)

    # -- GUARD: every English stem gets a firing probe -----------------------
    for stem in sorted(STEM_PROBES):
        probe = STEM_PROBES[stem]

        def mutate(c, probe=probe):
            c["instance"]["note"] = (
                c["instance"]["note"] + " plus " + probe + " modifier")
        case("GUARD fires on stem '%s' (probe '%s')" % (stem, probe),
             mutate, "GUARD")

    # -- GUARD: every Chinese keyword gets a firing probe --------------------
    # json.dumps below uses ensure_ascii=True on purpose: the raw text then
    # carries the keyword only in \uXXXX-escaped form, so these cases also
    # prove the unescape surface of the zh guard.
    for kw in ZH_KEYWORD_PROBES:

        def mutate(c, kw=kw):
            c["instance"]["note"] = (
                c["instance"]["note"] + " modifier " + kw)
        case("GUARD fires on zh keyword '%s'" % kw, mutate, "GUARD")

    # -- GUARD: structural smuggling shapes ----------------------------------
    case("GUARD fires on key with capture stem (slot row allowlist co-fires)",
         lambda c: c["profile_slots"][0].update({"capture_window": 1.0}),
         {"STRUCT", "GUARD"})
    case("GUARD fires on value with attack stem",
         lambda c: c["contract"].update(
             {"semantics": "shaping plus attack shaping"}),
         "GUARD")
    case("GUARD fires on camelCase token (AttackWindowProfile)",
         lambda c: c["instance"].update(
             {"note": "plus AttackWindowProfile modifier"}),
         "GUARD")
    case("GUARD fires on zh keyword in a fact_semantics value",
         lambda c: c["fact_atoms"][1].update(
             {"fact_semantics": "含麻痹语义的走私值"}),
         "GUARD")

    # -- STRUCT: fixed row schemas -------------------------------------------
    case("STRUCT fires on unknown key inside a profile_slots row",
         lambda c: c["profile_slots"][0].update({"trophic_note": "x"}),
         "STRUCT")
    case("STRUCT fires on unknown key inside a fact_atoms row",
         lambda c: c["fact_atoms"][0].update({"units": "au"}),
         "STRUCT")
    case("STRUCT fires on unknown key inside an instances row",
         lambda c: c["instances"][0].update({"season_note": "spring"}),
         "STRUCT")
    case("STRUCT fires on unknown key inside a lookup table row",
         lambda c: c["instances"][0]["example_lookup_table"][0].update(
             {"band": "high"}),
         "STRUCT")
    case("STRUCT fires on axis_semantics drift",
         lambda c: c["contract"].update(
             {"axis_semantics": "unary_or_2d_profile"}),
         "STRUCT")
    case("STRUCT fires on missing contract.input_scope",
         lambda c: c["contract"].pop("input_scope"),
         "STRUCT")
    case("STRUCT fires on slot fact_atom not declared in fact_atoms",
         lambda c: c["profile_slots"][0].update(
             {"fact_atom": "BaitScentConcentration"}),
         "STRUCT")
    case("STRUCT fires on instance bound_slot outside the declared slots",
         lambda c: c["instances"][0].update({"bound_slot": "@TasteProfile"}),
         "STRUCT")
    case("STRUCT fires on duplicate (population, slot) binding",
         lambda c: c["instances"].append(
             {"population_id": "sea_lamprey_migratory_spring",
              "bound_slot": "@ScentCueProfile",
              "profile_instance": "@SeaLampreyNightScentCue",
              "example_lookup_table": [{"input": "none", "fit": 0.0}]}),
         "STRUCT")

    # -- AXIS: unary-only admission -------------------------------------------
    case("AXIS fires on fact_atom as a list (two input axes = not unary)",
         lambda c: c["profile_slots"][0].update(
             {"fact_atom": ["BaitScentIntensity", "WaterCurrentSpeed"]}),
         "AXIS")
    case("AXIS fires on fact_atom referencing a Profile (no nested lookup; "
         "STRUCT co-fires on undeclared fact)",
         lambda c: c["profile_slots"][0].update(
             {"fact_atom": "@FeedingProfile"}),
         {"AXIS", "STRUCT"})
    case("AXIS fires on arity drift (binary)",
         lambda c: c["profile_slots"][0].update({"arity": "binary"}),
         "AXIS")
    case("AXIS fires on ladder_stage drift (typed 2D is P1, not admitted)",
         lambda c: c["profile_slots"][0].update(
             {"ladder_stage": "P1_typed_2d_interaction_profile"}),
         "AXIS")
    case("AXIS fires on axis_pair key in a slot row (second-axis surface; "
         "row allowlist co-fires)",
         lambda c: c["profile_slots"][0].update(
             {"axis_pair": ["BaitScentIntensity", "WaterCurrentSpeed"]}),
         {"STRUCT", "AXIS"})
    case("AXIS fires on the same fact feeding two slots (completeness "
         "STRUCT co-fires)",
         lambda c: c["profile_slots"].append(
             {"slot": "@ScentCueNightProfile",
              "meaning": "夜间味型适配",
              "axis_modality": "chemical_scent",
              "arity": "unary",
              "fact_atom": "BaitScentIntensity",
              "ladder_stage": "P0_unary_profile_lookup",
              "combine_into": "existing RR-T1 channel FIXED_COMBINE"}),
         {"AXIS", "STRUCT"})
    case("AXIS fires on lookup input referencing another Profile "
         "(no nested lookup)",
         lambda c: c["instances"][0]["example_lookup_table"][0].update(
             {"input": "@FlashProfile"}),
         "AXIS")
    case("AXIS fires on a declared slot missing from profile_slots "
         "(STRUCT co-fires on the unbound instance)",
         lambda c: c["profile_slots"].pop(1),
         {"AXIS", "STRUCT"})
    case("STRUCT fires on a declared slot left without any instance binding",
         lambda c: c["instances"].pop(1),
         "STRUCT")

    # -- FACT: closed enum + zero new columns ----------------------------------
    case("FACT fires on fact atom outside the closed enum "
         "(slot + table mutated consistently)",
         lambda c: (
             c["fact_atoms"][1].update({"fact_atom": "LureVoltageTrace"}),
             c["profile_slots"][1].update({"fact_atom": "LureVoltageTrace"})),
         "FACT")
    case("FACT fires on columns_added drift (a new column would be a new "
         "column structure)",
         lambda c: c["fact_atoms"][0].update({"columns_added": 1}),
         "FACT")
    case("FACT fires on grammar_form drift (no new column variants)",
         lambda c: c["fact_atoms"][0].update(
             {"grammar_form": "Grammar 5.1 V5 new columns"}),
         "FACT")
    case("FACT fires on computed_by drift (world-side computation is not "
         "this batch's fact)",
         lambda c: c["fact_atoms"][0].update(
             {"computed_by": "world_side_computed_fact"}),
         "FACT")

    # -- COMBINE ---------------------------------------------------------------
    case("COMBINE fires on author-chosen operator",
         lambda c: c["combine"].update({"operator": "WEIGHTED_PRODUCT"}),
         "COMBINE")
    case("COMBINE fires on silently-defined combine math (must stay "
         "visibly UNDEFINED)",
         lambda c: c["combine"].update({"operator_math": "MAX"}),
         "COMBINE")
    case("COMBINE fires on author_selectable=true",
         lambda c: c["combine"].update({"author_selectable": True}),
         "COMBINE")
    case("COMBINE fires on joins drift (a new channel is not admitted)",
         lambda c: c["combine"].update(
             {"joins": "a scent-dedicated second channel"}),
         "COMBINE")

    # -- TOP --------------------------------------------------------------------
    case("TOP fires on author-invented steps section",
         lambda c: c.update({"steps": [{"id": "s1", "depends_on": ["s0"]}]}),
         "TOP")
    case("TOP fires on author-invented axis_pairs section (the 2D pairing "
         "surface is not a section)",
         lambda c: c.update({"axis_pairs": [
             ["BaitScentIntensity", "WaterCurrentSpeed"]]}),
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
                        help="path to cue_axis.config.json")
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
