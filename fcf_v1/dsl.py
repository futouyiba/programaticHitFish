"""Minimal RC4 authoring compiler and semantic diagnostics."""

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Set


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


class DSLCompileError(ValueError):
    def __init__(self, diagnostics: Iterable[Diagnostic]):
        self.diagnostics = tuple(diagnostics)
        super().__init__("; ".join(d.message for d in self.diagnostics))


_CONTACTS = {"ENGULF", "SUCK_INTAKE", "PICKUP", "SLASH", "BITE_REMOVE", "NIBBLE"}
_MOTIVES = {"FORAGE", "DEFEND", "INVESTIGATE", "NONE"}
_GRADES = {"NONE", "WEAK", "NORMAL", "STRONG", "VERY_STRONG", "CERTAIN"}


def _typed_predicates_may_overlap(left: Any, right: Any) -> bool:
    """Conservative overlap check for V1's scalar typed predicate subset.

    Supported predicates have ``fact`` plus one or more of ``eq``, ``gt``,
    ``gte``, ``lt`` and ``lte``. Unknown shapes fail closed: the compiler
    treats them as possibly overlapping instead of relying on input order.
    """
    if not isinstance(left, dict) or not isinstance(right, dict):
        return True
    if left.get("fact") != right.get("fact"):
        return False
    allowed = {"fact", "eq", "gt", "gte", "lt", "lte"}
    if set(left) - allowed or set(right) - allowed or not left.get("fact"):
        return True
    if "eq" in left or "eq" in right:
        left_eq = left.get("eq") if "eq" in left else None
        right_eq = right.get("eq") if "eq" in right else None
        if "eq" in left and "eq" in right:
            return left_eq == right_eq
        eq_value = left_eq if "eq" in left else right_eq
        if not isinstance(eq_value, (int, float)) or isinstance(eq_value, bool):
            return True

    def bounds(predicate: Dict[str, Any]):
        if "eq" in predicate:
            value = predicate["eq"]
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                return None
            return value, True, value, True
        lower, lower_closed = None, False
        upper, upper_closed = None, False
        if "gt" in predicate:
            lower, lower_closed = predicate["gt"], False
        if "gte" in predicate:
            lower, lower_closed = predicate["gte"], True
        if "lt" in predicate:
            upper, upper_closed = predicate["lt"], False
        if "lte" in predicate:
            upper, upper_closed = predicate["lte"], True
        values = [value for value in (lower, upper) if value is not None]
        if not values or not all(isinstance(value, (int, float)) for value in values):
            return None
        return lower, lower_closed, upper, upper_closed

    a = bounds(left)
    b = bounds(right)
    if a is None or b is None:
        return True
    a_low, a_low_closed, a_high, a_high_closed = a
    b_low, b_low_closed, b_high, b_high_closed = b
    lower = a_low if b_low is None or (a_low is not None and a_low > b_low) else b_low
    upper = a_high if b_high is None or (a_high is not None and a_high < b_high) else b_high
    if lower is None or upper is None:
        return True
    if lower < upper:
        return True
    if lower > upper:
        return False
    left_contains = ((a_low is None or lower > a_low or a_low_closed) and
                     (a_high is None or lower < a_high or a_high_closed))
    right_contains = ((b_low is None or lower > b_low or b_low_closed) and
                      (b_high is None or lower < b_high or b_high_closed))
    return left_contains and right_contains


def compile_artifact(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and freeze a plain authoring dictionary.

    The returned copy is safe to hand to runtime code. Runtime does not accept
    the mutable authoring object directly.
    """
    d: List[Diagnostic] = []
    allowed_top = {"schema_version", "species", "population_definitions", "population_slices", "programs", "variants", "world_facts", "settlement_owners", "resolver_rules", "trace_contract", "arrival"}
    for field in set(raw) - allowed_top:
        d.append(Diagnostic("UNKNOWN_FIELD", field, "unsupported top-level authoring field"))
    if raw.get("schema_version") != "fcf.v1":
        d.append(Diagnostic("SCHEMA_VERSION", "schema_version", "expected fcf.v1"))
    species = raw.get("species") or {}
    for field in set(species) - {"id", "population_id", "population_definition_id", "q", "anatomy_profile", "sensory_channels", "allowed_contacts", "history_schema", "capability_limits"}:
        d.append(Diagnostic("UNKNOWN_FIELD", "species." + field, "unsupported Species field"))
    population_definitions = raw.get("population_definitions") or []
    population_ids: Set[str] = set()
    for i, definition in enumerate(population_definitions):
        path = f"population_definitions[{i}]"
        allowed = {"id", "q", "cohort_axes", "history_scope", "population_revision"}
        if not isinstance(definition, dict):
            d.append(Diagnostic("POPULATION_SHAPE", path, "PopulationDefinition must be an object"))
            continue
        for field in set(definition) - allowed:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported PopulationDefinition field"))
        pid = definition.get("id")
        if not isinstance(pid, str) or not pid or pid in population_ids:
            d.append(Diagnostic("DUPLICATE_ID", path + ".id", "population id must be unique"))
        population_ids.add(pid)
        if not isinstance(definition.get("q"), (int, float)) or definition.get("q", 0) <= 0:
            d.append(Diagnostic("INVALID_Q", path + ".q", "q must be > 0"))
    population_ref = species.get("population_definition_id")
    q = species.get("q")
    if population_definitions:
        if population_ref not in population_ids:
            d.append(Diagnostic("MISSING_REFERENCE", "species.population_definition_id", "unknown PopulationDefinition reference"))
        referenced_q = next((x.get("q") for x in population_definitions if x.get("id") == population_ref), None)
        if "q" in species and species.get("q") != referenced_q:
            d.append(Diagnostic("POPULATION_Q_MISMATCH", "species.q", "legacy q must match referenced PopulationDefinition"))
        if "population_id" in species and species.get("population_id") != population_ref:
            d.append(Diagnostic("POPULATION_ID_MISMATCH", "species.population_id", "legacy population_id must match referenced definition"))
        q = referenced_q
    if not isinstance(q, (int, float)) or q <= 0:
        d.append(Diagnostic("INVALID_Q", "species.q", "q must be > 0"))
    contacts = set(species.get("allowed_contacts") or [])
    unknown_contacts = contacts - _CONTACTS
    if unknown_contacts:
        d.append(Diagnostic("UNKNOWN_CONTACT", "species.allowed_contacts", str(sorted(unknown_contacts))))
    capability_limits = species.get("capability_limits") or {}
    if set(capability_limits) - {"tasks", "max_defendable_distance_m"}:
        for field in set(capability_limits) - {"tasks", "max_defendable_distance_m"}:
            d.append(Diagnostic("UNKNOWN_FIELD", "species.capability_limits." + field, "unsupported capability limit"))
    capability_tasks = set(capability_limits.get("tasks") or [])
    if "max_defendable_distance_m" in capability_limits:
        value = capability_limits["max_defendable_distance_m"]
        if not isinstance(value, (int, float)) or value < 0:
            d.append(Diagnostic("CAPABILITY_RANGE", "species.capability_limits.max_defendable_distance_m", "distance must be >= 0"))

    # Population identity is explicit and independent from Species capability.
    slices = raw.get("population_slices") or []
    slice_ids: Set[str] = set()
    for i, item in enumerate(slices):
        path = f"population_slices[{i}]"
        allowed = {"id", "population_id", "cohort_key", "lifecycle_role_key", "behavior_program_id", "minimum_hold_s", "hysteresis_policy_id"}
        if not isinstance(item, dict):
            d.append(Diagnostic("SLICE_SHAPE", path, "PopulationSlice must be an object"))
            continue
        for field in set(item) - allowed:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported PopulationSlice field"))
        sid = item.get("id")
        if not isinstance(sid, str) or not sid or sid in slice_ids:
            d.append(Diagnostic("DUPLICATE_ID", path + ".id", "slice id must be unique"))
        slice_ids.add(sid)
        for required in ("population_id", "cohort_key", "lifecycle_role_key", "behavior_program_id"):
            if not isinstance(item.get(required), str) or not item.get(required):
                d.append(Diagnostic("SLICE_REFERENCE", path + "." + required, "required stable reference"))
        if "minimum_hold_s" in item and (not isinstance(item["minimum_hold_s"], (int, float)) or item["minimum_hold_s"] < 0):
            d.append(Diagnostic("SLICE_RANGE", path + ".minimum_hold_s", "minimum_hold_s must be >= 0"))

    trace_contract = raw.get("trace_contract")
    if trace_contract is not None:
        if not isinstance(trace_contract, dict):
            d.append(Diagnostic("TRACE_CONTRACT_SHAPE", "trace_contract", "trace_contract must be an object"))
        else:
            allowed_trace = {"version", "required_stages", "include_inputs", "include_revisions"}
            for field in set(trace_contract) - allowed_trace:
                d.append(Diagnostic("UNKNOWN_FIELD", "trace_contract." + field, "unsupported trace contract field"))
            if not isinstance(trace_contract.get("version"), str) or not trace_contract.get("version"):
                d.append(Diagnostic("TRACE_CONTRACT_VERSION", "trace_contract.version", "version is required"))
            if not isinstance(trace_contract.get("required_stages"), list) or not trace_contract.get("required_stages"):
                d.append(Diagnostic("TRACE_CONTRACT_STAGES", "trace_contract.required_stages", "at least one stage is required"))
            for flag in ("include_inputs", "include_revisions"):
                if flag in trace_contract and not isinstance(trace_contract[flag], bool):
                    d.append(Diagnostic("TRACE_CONTRACT_FLAG", "trace_contract." + flag, "flag must be boolean"))
    programs = raw.get("programs") or []
    if not isinstance(programs, list) or not programs:
        d.append(Diagnostic("PROGRAMS_REQUIRED", "programs", "at least one BehaviorProgram is required"))
        programs = []
    ids: Set[str] = set()
    for i, program in enumerate(programs):
        path = f"programs[{i}]"
        for field in set(program) - {"id", "slice_role", "motive_priority", "tasks", "contact_types", "occupancy", "entry_offers", "reevaluation_triggers", "trigger_policies"}:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported Program field"))
        if "slice_keys" in program:
            d.append(Diagnostic("PROGRAM_IN_SLICE_IDENTITY", path + ".slice_keys", "Program cannot author PopulationSlice identity"))
        pid = program.get("id")
        if not pid or pid in ids:
            d.append(Diagnostic("DUPLICATE_ID", path + ".id", "program id must be unique"))
        ids.add(pid)
        priorities = program.get("motive_priority") or []
        if len(priorities) != len(set(priorities)) or not set(priorities) <= _MOTIVES:
            d.append(Diagnostic("MOTIVE_PRIORITY", path + ".motive_priority", "motives must be unique and known"))
        for j, row in enumerate(program.get("occupancy") or []):
            if row.get("grade") not in {"FORBIDDEN", "ACCIDENTAL", "MARGINAL", "GOOD", "PRIME"}:
                d.append(Diagnostic("OCCUPANCY_GRADE", f"{path}.occupancy[{j}].grade", "unknown occupancy grade"))
        program_contacts = set(program.get("contact_types") or [])
        if not program_contacts <= contacts:
            d.append(Diagnostic("CAPABILITY_EXPANSION", path + ".contact_types", "Program contact type is outside Species repertoire"))
        program_tasks = set(program.get("tasks") or [])
        if capability_tasks and not program_tasks <= capability_tasks:
            d.append(Diagnostic("CAPABILITY_EXPANSION", path + ".tasks", "Program task is outside Species capability"))
        for motive, offer in (program.get("entry_offers") or {}).items():
            if motive not in _MOTIVES:
                d.append(Diagnostic("ENTRY_MOTIVE", f"{path}.entry_offers", "unknown motive"))
            if offer.get("base") not in _GRADES and not offer.get("deny", False):
                d.append(Diagnostic("ENTRY_GRADE", f"{path}.entry_offers.{motive}", "base must be a known grade"))
        for trigger in program.get("reevaluation_triggers") or []:
            if not isinstance(trigger, str) or not trigger:
                d.append(Diagnostic("TRIGGER_ID", path + ".reevaluation_triggers", "trigger IDs must be stable strings"))
        policies = program.get("trigger_policies") or {}
        for trigger in program.get("reevaluation_triggers") or []:
            policy = policies.get(trigger) or {}
            if policy.get("debounce_s") is None or policy.get("hysteresis") is None:
                d.append(Diagnostic("TRIGGER_POLICY", f"{path}.trigger_policies.{trigger}", "trigger requires debounce_s and hysteresis"))
    program_ids = {p.get("id") for p in programs}
    for i, item in enumerate(slices):
        if isinstance(item, dict) and item.get("behavior_program_id") not in program_ids:
            d.append(Diagnostic("MISSING_REFERENCE", f"population_slices[{i}].behavior_program_id", "unknown BehaviorProgram reference"))
    # Variants are compile-time policy patches. Capability fields are
    # intentionally non-overridable so a variant cannot redefine its species.
    variant_ids: Set[str] = set()
    for i, variant in enumerate(raw.get("variants") or []):
        path = f"variants[{i}]"
        for field in set(variant) - {"id", "species_id", "program_id", "policy_overrides"}:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported Variant field"))
        if not variant.get("id") or not variant.get("species_id"):
            d.append(Diagnostic("VARIANT_ID", path, "variant requires id and species_id"))
        if variant.get("species_id") != species.get("id"):
            d.append(Diagnostic("MISSING_REFERENCE", path + ".species_id", "Variant species reference does not match artifact Species"))
        if "program_id" in variant and variant.get("program_id") not in {p.get("id") for p in programs}:
            d.append(Diagnostic("MISSING_REFERENCE", path + ".program_id", "unknown base BehaviorProgram reference"))
        if variant.get("id") in variant_ids:
            d.append(Diagnostic("DUPLICATE_VARIANT_ID", path + ".id", "variant id must be unique"))
        variant_ids.add(variant.get("id"))
        allowed_variant_paths = {"motive_priority", "occupancy", "entry_offers", "task_profile_id", "trigger_policies", "speed_band"}
        for field in (variant.get("policy_overrides") or {}):
            if field not in allowed_variant_paths:
                d.append(Diagnostic("VARIANT_POLICY_PATH", f"{path}.policy_overrides.{field}", "variant path is not in the policy allowlist"))
            if field in {"q", "population_id", "population_definition_id", "sensory_channels", "allowed_contacts", "anatomy_profile", "history_schema", "thermal_capability_id", "oxygen_capability_id"}:
                d.append(Diagnostic("VARIANT_CAPABILITY_EXPANSION", f"{path}.policy_overrides.{field}", "variant cannot override Species capability"))
    seen_consequences: Set[str] = set()
    owners = raw.get("settlement_owners")
    if not isinstance(owners, list) or not owners:
        d.append(Diagnostic("MISSING_SETTLEMENT_OWNER", "settlement_owners", "RC4 requires an explicit owner matrix"))
        owners = []
    valid_owner_roles = {"PROGRAM", "LIFECYCLE", "OCCUPANCY", "PERCEPTION", "MOTIVE", "ENTRY", "FUNCTIONAL", "CONVERSION", "HISTORY", "FUTURE"}
    for i, owner in enumerate(owners):
        if not isinstance(owner, dict) or set(owner) - {"physical_consequence_id", "owner"}:
            d.append(Diagnostic("UNKNOWN_FIELD", f"settlement_owners[{i}]", "owner row has unsupported field"))
            continue
        consequence = owner.get("physical_consequence_id")
        if not consequence or consequence in seen_consequences:
            d.append(Diagnostic("DUPLICATE_SETTLEMENT_OWNER", f"settlement_owners[{i}]", "physical consequence must have one owner"))
        seen_consequences.add(consequence)
        if owner.get("owner") not in valid_owner_roles:
            d.append(Diagnostic("INVALID_SETTLEMENT_OWNER", f"settlement_owners[{i}].owner", "unknown Cause Role owner"))
    allowed_world_facts = {"water_temperature_c", "dissolved_oxygen_mg_l", "flow_vector", "depth_m", "structure_tags", "substrate", "illumination_lux", "turbidity", "resource_state", "barometric_pressure_hpa", "barometric_trend"}
    for i, fact in enumerate(raw.get("world_facts") or []):
        if fact not in allowed_world_facts:
            d.append(Diagnostic("WORLD_FACT_IS_INTERPRETATION", f"world_facts[{i}]", "World Fact must be species-neutral"))
    allowed_rule_fields = {"rule_id", "priority", "when", "requires", "then", "consequence_id", "owner", "effective_interval"}
    rule_ids: Set[str] = set()
    for i, rule in enumerate(raw.get("resolver_rules") or []):
        if not isinstance(rule, dict):
            d.append(Diagnostic("RULE_SHAPE", f"resolver_rules[{i}]", "rule must be an object"))
            continue
        for field in set(rule) - allowed_rule_fields:
            d.append(Diagnostic("UNKNOWN_FIELD", f"resolver_rules[{i}].{field}", "unsupported resolver rule field"))
        for required in ("rule_id", "priority", "consequence_id", "owner"):
            if required not in rule:
                d.append(Diagnostic("RULE_FIELD_REQUIRED", f"resolver_rules[{i}].{required}", "required resolver rule field"))
        if rule.get("rule_id") in rule_ids:
            d.append(Diagnostic("DUPLICATE_ID", f"resolver_rules[{i}].rule_id", "rule id must be unique"))
        rule_ids.add(rule.get("rule_id"))
        if not isinstance(rule.get("priority"), int):
            d.append(Diagnostic("RULE_PRIORITY", f"resolver_rules[{i}].priority", "priority must be an integer"))
        if "when" in rule and not isinstance(rule.get("when"), dict):
            d.append(Diagnostic("RULE_WHEN", f"resolver_rules[{i}].when", "when must be typed predicate object"))
        if "then" in rule and not isinstance(rule.get("then"), dict):
            d.append(Diagnostic("RULE_THEN", f"resolver_rules[{i}].then", "then must be typed output object"))
        if not isinstance(rule.get("owner"), str) or not rule.get("owner"):
            d.append(Diagnostic("INVALID_SETTLEMENT_OWNER", f"resolver_rules[{i}].owner", "owner must be non-empty"))
        if not isinstance(rule.get("consequence_id"), str) or not rule.get("consequence_id"):
            d.append(Diagnostic("RULE_CONSEQUENCE", f"resolver_rules[{i}].consequence_id", "consequence_id must be non-empty"))
        interval = rule.get("effective_interval")
        if interval is not None:
            if not isinstance(interval, dict) or set(interval) - {"start", "end", "unit", "clock"}:
                d.append(Diagnostic("INTERVAL_SHAPE", f"resolver_rules[{i}].effective_interval", "interval requires start/end/unit/clock"))
            elif (not all(key in interval for key in ("start", "end", "unit", "clock"))
                  or not isinstance(interval["unit"], str) or not interval["unit"]
                  or not isinstance(interval["clock"], str) or not interval["clock"]
                  or interval["start"] >= interval["end"]):
                d.append(Diagnostic("INTERVAL_RANGE", f"resolver_rules[{i}].effective_interval", "interval must be half-open with start < end"))
        a = rule.get("effective_interval")
        for j, other in enumerate((raw.get("resolver_rules") or [])[i + 1:], i + 1):
            predicates_overlap = _typed_predicates_may_overlap(rule.get("when"), other.get("when"))
            b = other.get("effective_interval") if isinstance(other, dict) else None
            intervals_overlap = True
            if a and b and isinstance(a, dict) and isinstance(b, dict):
                same_clock = a.get("unit") == b.get("unit") and a.get("clock") == b.get("clock")
                intervals_overlap = (not same_clock or
                                     (a.get("start", 0) < b.get("end", 0) and b.get("start", 0) < a.get("end", 0)))
            if rule.get("priority") == (other.get("priority") if isinstance(other, dict) else None) and predicates_overlap and intervals_overlap:
                d.append(Diagnostic("EQUAL_PRIORITY_OVERLAP", f"resolver_rules[{i},{j}]", "equal-priority overlapping rules are ambiguous"))
    arrival = raw.get("arrival") or {}
    if set(arrival) - {"produces_new_units", "temporal_factor"}:
        d.append(Diagnostic("UNKNOWN_FIELD", "arrival", "unsupported ARRIVAL field"))
    if not 0.0 <= arrival.get("temporal_factor", 1.0) <= 1.0:
        d.append(Diagnostic("ARRIVAL_T_RANGE", "arrival.temporal_factor", "temporal_factor must be in [0,1]"))
    if arrival.get("produces_new_units") and arrival.get("temporal_factor", 1.0) != 1.0:
        d.append(Diagnostic("ARRIVAL_T_CONFLICT", "arrival", "ARRIVAL cannot both produce units and apply T<1"))
    if d:
        raise DSLCompileError(d)
    # Deep copy through JSON-compatible values without accepting arbitrary
    # executable objects.
    import json
    return json.loads(json.dumps(raw, sort_keys=True))
