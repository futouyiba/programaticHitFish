"""Minimal RC4 authoring compiler and semantic diagnostics."""

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Set, Mapping, Optional
import json
import hashlib


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


class DSLCompileError(ValueError):
    def __init__(self, diagnostics: Iterable[Diagnostic]):
        self.diagnostics = tuple(diagnostics)
        super().__init__("; ".join(d.message for d in self.diagnostics))


class _FrozenDict(dict):
    """JSON-compatible immutable mapping used inside CompiledArtifact."""
    def _blocked(self, *args, **kwargs):
        raise TypeError("compiled artifact is immutable")
    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = __ior__ = _blocked


class CompiledArtifact(dict):
    """Read-only compiled DSL artifact with a stable semantic fingerprint."""
    def __init__(self, payload: Mapping[str, Any]):
        frozen = _freeze(payload)
        super().__init__(frozen)
        self._fingerprint = payload["semantic_fingerprint"]

    def __eq__(self, other):
        if isinstance(other, Mapping) and "semantic_fingerprint" not in other:
            return _thaw({
                key: value for key, value in self.items()
                if key not in {"artifact_version", "source_path", "input_revision",
                               "diagnostics", "runtime_view", "reference_index",
                               "compiler_contract", "semantic_fingerprint"}
            }) == dict(other)
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self == other
    @property
    def semantic_fingerprint(self) -> str:
        return self._fingerprint

    def to_dict(self) -> Dict[str, Any]:
        return _thaw(self)

    def to_json(self) -> str:
        return json.dumps(self, sort_keys=True, ensure_ascii=False)
    def _blocked(self, *args, **kwargs):
        raise TypeError("CompiledArtifact is immutable")
    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = __ior__ = _blocked


def _freeze(value):
    if isinstance(value, dict):
        return _FrozenDict({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(v) for v in value)
    return value


def _thaw(value):
    if isinstance(value, dict):
        return {k: _thaw(v) for k, v in value.items()}
    if isinstance(value, tuple):
        return [_thaw(v) for v in value]
    return value


_CONTACTS = {"ENGULF", "SUCK_INTAKE", "PICKUP", "SLASH", "BITE_REMOVE", "NIBBLE"}
_MOTIVES = {"FORAGE", "DEFEND", "INVESTIGATE", "NONE"}
_GRADES = {"NONE", "WEAK", "NORMAL", "STRONG", "VERY_STRONG", "CERTAIN"}
DSL_CONTRACT_0_3_4_0 = "0.3.4.0"
_DSL_CONTRACTS = {"legacy", DSL_CONTRACT_0_3_4_0}


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


def compile_artifact(
    raw: Dict[str, Any],
    *,
    source_path: Optional[str] = None,
    input_revision: Optional[str] = None,
    contract: str = "legacy",
) -> CompiledArtifact:
    """Validate and freeze a plain authoring dictionary.

    The returned copy is safe to hand to runtime code. Runtime does not accept
    the mutable authoring object directly.
    """
    d: List[Diagnostic] = []
    if contract not in _DSL_CONTRACTS:
        raise DSLCompileError([Diagnostic("COMPILER_CONTRACT", "contract", "unknown DSL compiler contract")])
    if not isinstance(raw, dict):
        raise DSLCompileError([Diagnostic("ROOT_SHAPE", "$", "authoring artifact must be an object")])
    if source_path is not None and not isinstance(source_path, str):
        d.append(Diagnostic("SOURCE_PATH", "source_path", "source_path must be a string"))
    if input_revision is not None and not isinstance(input_revision, str):
        d.append(Diagnostic("INPUT_REVISION", "input_revision", "input_revision must be a string"))
    if contract == DSL_CONTRACT_0_3_4_0:
        required_namespaces = {"schema_version", "world_facts", "population_definitions", "species", "population_slices", "programs", "variants", "settlement_owners", "resolver_rules", "trace_contract", "arrival"}
        for namespace in sorted(required_namespaces - set(raw)):
            d.append(Diagnostic("NAMESPACE_REQUIRED", namespace, "0.3.4.0 requires this namespace"))
        if not isinstance(source_path, str) or not source_path:
            d.append(Diagnostic("SOURCE_PATH_REQUIRED", "source_path", "0.3.4.0 requires a non-empty source path"))
        if not isinstance(input_revision, str) or not input_revision:
            d.append(Diagnostic("INPUT_REVISION_REQUIRED", "input_revision", "0.3.4.0 requires a non-empty input revision"))
    allowed_top = {"schema_version", "species", "population_definitions", "population_slices", "programs", "variants", "world_facts", "settlement_owners", "resolver_rules", "trace_contract", "arrival"}
    for field in set(raw) - allowed_top:
        d.append(Diagnostic("UNKNOWN_FIELD", field, "unsupported top-level authoring field"))
    if raw.get("schema_version") != "fcf.v1":
        d.append(Diagnostic("SCHEMA_VERSION", "schema_version", "expected fcf.v1"))
    species = raw.get("species") or {}
    if not isinstance(species, dict):
        d.append(Diagnostic("SPECIES_SHAPE", "species", "Species must be an object"))
        species = {}
    for field in set(species) - {"id", "population_id", "population_definition_id", "q", "anatomy_profile", "sensory_channels", "allowed_contacts", "history_schema", "capability_limits"}:
        d.append(Diagnostic("UNKNOWN_FIELD", "species." + field, "unsupported Species field"))
    population_definitions = raw.get("population_definitions") or []
    if not isinstance(population_definitions, list):
        d.append(Diagnostic("POPULATIONS_SHAPE", "population_definitions", "population_definitions must be a list"))
        population_definitions = []
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
        elif pid:
            population_ids.add(pid)
        if not isinstance(definition.get("q"), (int, float)) or isinstance(definition.get("q"), bool) or definition.get("q", 0) <= 0:
            d.append(Diagnostic("INVALID_Q", path + ".q", "q must be > 0"))
        if contract == DSL_CONTRACT_0_3_4_0 and (not isinstance(definition.get("population_revision"), str) or not definition.get("population_revision")):
            d.append(Diagnostic("POPULATION_REVISION_REQUIRED", path + ".population_revision", "0.3.4.0 requires population_revision"))
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
    allowed_contacts = species.get("allowed_contacts") or []
    if not isinstance(allowed_contacts, list):
        d.append(Diagnostic("CONTACTS_SHAPE", "species.allowed_contacts", "allowed_contacts must be a list"))
        allowed_contacts = []
    if not all(isinstance(contact, str) for contact in allowed_contacts):
        d.append(Diagnostic("CONTACTS_SHAPE", "species.allowed_contacts", "allowed_contacts entries must be strings"))
        allowed_contacts = [contact for contact in allowed_contacts if isinstance(contact, str)]
    contacts = set(allowed_contacts)
    unknown_contacts = contacts - _CONTACTS
    if unknown_contacts:
        d.append(Diagnostic("UNKNOWN_CONTACT", "species.allowed_contacts", str(sorted(unknown_contacts))))
    capability_limits = species.get("capability_limits") or {}
    if not isinstance(capability_limits, dict):
        d.append(Diagnostic("CAPABILITY_SHAPE", "species.capability_limits", "capability_limits must be an object"))
        capability_limits = {}
    if set(capability_limits) - {"tasks", "max_defendable_distance_m"}:
        for field in set(capability_limits) - {"tasks", "max_defendable_distance_m"}:
            d.append(Diagnostic("UNKNOWN_FIELD", "species.capability_limits." + field, "unsupported capability limit"))
    capability_task_values = capability_limits.get("tasks") or []
    if not isinstance(capability_task_values, list):
        d.append(Diagnostic("TASKS_SHAPE", "species.capability_limits.tasks", "tasks must be a list"))
        capability_task_values = []
    if not all(isinstance(task, str) for task in capability_task_values):
        d.append(Diagnostic("TASKS_SHAPE", "species.capability_limits.tasks", "tasks entries must be strings"))
        capability_task_values = [task for task in capability_task_values if isinstance(task, str)]
    capability_tasks = set(capability_task_values)
    if "max_defendable_distance_m" in capability_limits:
        value = capability_limits["max_defendable_distance_m"]
        if not isinstance(value, (int, float)) or value < 0:
            d.append(Diagnostic("CAPABILITY_RANGE", "species.capability_limits.max_defendable_distance_m", "distance must be >= 0"))

    # Population identity is explicit and independent from Species capability.
    slices = raw.get("population_slices") or []
    if not isinstance(slices, list):
        d.append(Diagnostic("SLICES_SHAPE", "population_slices", "population_slices must be a list"))
        slices = []
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
        elif sid:
            slice_ids.add(sid)
        for required in ("population_id", "cohort_key", "lifecycle_role_key", "behavior_program_id"):
            if not isinstance(item.get(required), str) or not item.get(required):
                d.append(Diagnostic("SLICE_REFERENCE", path + "." + required, "required stable reference"))
        if "minimum_hold_s" in item and (not isinstance(item["minimum_hold_s"], (int, float)) or item["minimum_hold_s"] < 0):
            d.append(Diagnostic("SLICE_RANGE", path + ".minimum_hold_s", "minimum_hold_s must be >= 0"))
        if contract == DSL_CONTRACT_0_3_4_0 and item.get("population_id") not in population_ids:
            d.append(Diagnostic("MISSING_REFERENCE", path + ".population_id", "unknown PopulationDefinition reference"))

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
            if trace_contract.get("include_revisions") and source_path is not None and not input_revision:
                d.append(Diagnostic("INPUT_REVISION_REQUIRED", "input_revision", "trace contract requires an input revision"))
            if contract == DSL_CONTRACT_0_3_4_0 and trace_contract.get("include_revisions") is not True:
                d.append(Diagnostic("TRACE_REVISION_REQUIRED", "trace_contract.include_revisions", "0.3.4.0 requires revision-aware traces"))
    programs = raw.get("programs") or []
    if not isinstance(programs, list) or not programs:
        d.append(Diagnostic("PROGRAMS_REQUIRED", "programs", "at least one BehaviorProgram is required"))
        programs = []
    ids: Set[str] = set()
    for i, program in enumerate(programs):
        path = f"programs[{i}]"
        if not isinstance(program, dict):
            d.append(Diagnostic("PROGRAM_SHAPE", path, "BehaviorProgram must be an object"))
            continue
        for field in set(program) - {"id", "slice_role", "motive_priority", "tasks", "contact_types", "occupancy", "entry_offers", "reevaluation_triggers", "trigger_policies"}:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported Program field"))
        if "slice_keys" in program:
            d.append(Diagnostic("PROGRAM_IN_SLICE_IDENTITY", path + ".slice_keys", "Program cannot author PopulationSlice identity"))
        pid = program.get("id")
        if not pid or pid in ids:
            d.append(Diagnostic("DUPLICATE_ID", path + ".id", "program id must be unique"))
        elif isinstance(pid, str):
            ids.add(pid)
        priorities = program.get("motive_priority") or []
        if not isinstance(priorities, list):
            d.append(Diagnostic("MOTIVE_PRIORITY", path + ".motive_priority", "motive_priority must be a list"))
            priorities = []
        if (not all(isinstance(motive, str) for motive in priorities)
                or len(priorities) != len(set(priorities))
                or not set(priorities) <= _MOTIVES):
            d.append(Diagnostic("MOTIVE_PRIORITY", path + ".motive_priority", "motives must be unique and known"))
        occupancy = program.get("occupancy") or []
        if not isinstance(occupancy, list):
            d.append(Diagnostic("OCCUPANCY_SHAPE", f"{path}.occupancy", "occupancy must be a list"))
            occupancy = []
        for j, row in enumerate(occupancy):
            if not isinstance(row, dict):
                d.append(Diagnostic("OCCUPANCY_SHAPE", f"{path}.occupancy[{j}]", "occupancy row must be an object"))
                continue
            for field in set(row) - {"node_tag", "grade", "reason"}:
                d.append(Diagnostic("UNKNOWN_FIELD", f"{path}.occupancy[{j}].{field}", "unsupported occupancy field"))
            if row.get("grade") not in {"FORBIDDEN", "ACCIDENTAL", "MARGINAL", "GOOD", "PRIME"}:
                d.append(Diagnostic("OCCUPANCY_GRADE", f"{path}.occupancy[{j}].grade", "unknown occupancy grade"))
        program_contact_values = program.get("contact_types") or []
        if not isinstance(program_contact_values, list):
            d.append(Diagnostic("CONTACTS_SHAPE", f"{path}.contact_types", "contact_types must be a list"))
            program_contact_values = []
        if not all(isinstance(contact, str) for contact in program_contact_values):
            d.append(Diagnostic("CONTACTS_SHAPE", f"{path}.contact_types", "contact_types entries must be strings"))
            program_contact_values = [contact for contact in program_contact_values if isinstance(contact, str)]
        program_contacts = set(program_contact_values)
        if not program_contacts <= contacts:
            d.append(Diagnostic("CAPABILITY_EXPANSION", path + ".contact_types", "Program contact type is outside Species repertoire"))
        program_task_values = program.get("tasks") or []
        if not isinstance(program_task_values, list):
            d.append(Diagnostic("TASKS_SHAPE", f"{path}.tasks", "tasks must be a list"))
            program_task_values = []
        if not all(isinstance(task, str) for task in program_task_values):
            d.append(Diagnostic("TASKS_SHAPE", f"{path}.tasks", "tasks entries must be strings"))
            program_task_values = [task for task in program_task_values if isinstance(task, str)]
        program_tasks = set(program_task_values)
        if capability_tasks and not program_tasks <= capability_tasks:
            d.append(Diagnostic("CAPABILITY_EXPANSION", path + ".tasks", "Program task is outside Species capability"))
        entry_offers = program.get("entry_offers") or {}
        if not isinstance(entry_offers, dict):
            d.append(Diagnostic("ENTRY_OFFERS_SHAPE", f"{path}.entry_offers", "entry_offers must be an object"))
            entry_offers = {}
        for motive, offer in entry_offers.items():
            if not isinstance(offer, dict):
                d.append(Diagnostic("ENTRY_SHAPE", f"{path}.entry_offers.{motive}", "entry offer must be an object"))
                continue
            for field in set(offer) - {"base", "deny", "rules"}:
                d.append(Diagnostic("UNKNOWN_FIELD", f"{path}.entry_offers.{motive}.{field}", "unsupported entry offer field"))
            if motive not in _MOTIVES:
                d.append(Diagnostic("ENTRY_MOTIVE", f"{path}.entry_offers", "unknown motive"))
            if offer.get("base") not in _GRADES and not offer.get("deny", False):
                d.append(Diagnostic("ENTRY_GRADE", f"{path}.entry_offers.{motive}", "base must be a known grade"))
            for k, entry_rule in enumerate(offer.get("rules") or []):
                if not isinstance(entry_rule, dict):
                    d.append(Diagnostic("ENTRY_RULE_SHAPE", f"{path}.entry_offers.{motive}.rules[{k}]", "entry rule must be an object"))
                    continue
                for field in set(entry_rule) - {"when", "add", "subtract", "deny"}:
                    d.append(Diagnostic("UNKNOWN_FIELD", f"{path}.entry_offers.{motive}.rules[{k}].{field}", "unsupported entry rule field"))
        triggers = program.get("reevaluation_triggers") or []
        if not isinstance(triggers, list):
            d.append(Diagnostic("TRIGGERS_SHAPE", f"{path}.reevaluation_triggers", "reevaluation_triggers must be a list"))
            triggers = []
        for trigger in triggers:
            if not isinstance(trigger, str) or not trigger:
                d.append(Diagnostic("TRIGGER_ID", path + ".reevaluation_triggers", "trigger IDs must be stable strings"))
        policies = program.get("trigger_policies") or {}
        if not isinstance(policies, dict):
            d.append(Diagnostic("TRIGGER_POLICIES_SHAPE", f"{path}.trigger_policies", "trigger_policies must be an object"))
            policies = {}
        for trigger in triggers:
            policy = policies.get(trigger) or {}
            if isinstance(policy, dict):
                for field in set(policy) - {"debounce_s", "hysteresis", "revision"}:
                    d.append(Diagnostic("UNKNOWN_FIELD", f"{path}.trigger_policies.{trigger}.{field}", "unsupported trigger policy field"))
            if policy.get("debounce_s") is None or policy.get("hysteresis") is None:
                d.append(Diagnostic("TRIGGER_POLICY", f"{path}.trigger_policies.{trigger}", "trigger requires debounce_s and hysteresis"))
    program_ids = {p.get("id") for p in programs if isinstance(p, dict)}
    for i, item in enumerate(slices):
        if isinstance(item, dict) and item.get("behavior_program_id") not in program_ids:
            d.append(Diagnostic("MISSING_REFERENCE", f"population_slices[{i}].behavior_program_id", "unknown BehaviorProgram reference"))
    # Variants are compile-time policy patches. Capability fields are
    # intentionally non-overridable so a variant cannot redefine its species.
    variant_ids: Set[str] = set()
    variants = raw.get("variants") or []
    if not isinstance(variants, list):
        d.append(Diagnostic("VARIANTS_SHAPE", "variants", "variants must be a list"))
        variants = []
    for i, variant in enumerate(variants):
        path = f"variants[{i}]"
        if not isinstance(variant, dict):
            d.append(Diagnostic("VARIANT_SHAPE", path, "Variant must be an object"))
            continue
        for field in set(variant) - {"id", "species_id", "program_id", "policy_overrides"}:
            d.append(Diagnostic("UNKNOWN_FIELD", path + "." + field, "unsupported Variant field"))
        if not variant.get("id") or not variant.get("species_id"):
            d.append(Diagnostic("VARIANT_ID", path, "variant requires id and species_id"))
        if variant.get("species_id") != species.get("id"):
            d.append(Diagnostic("MISSING_REFERENCE", path + ".species_id", "Variant species reference does not match artifact Species"))
        if "program_id" in variant and variant.get("program_id") not in program_ids:
            d.append(Diagnostic("MISSING_REFERENCE", path + ".program_id", "unknown base BehaviorProgram reference"))
        variant_id = variant.get("id")
        if isinstance(variant_id, str) and variant_id in variant_ids:
            d.append(Diagnostic("DUPLICATE_VARIANT_ID", path + ".id", "variant id must be unique"))
        if isinstance(variant_id, str) and variant_id:
            variant_ids.add(variant_id)
        allowed_variant_paths = {"motive_priority", "occupancy", "entry_offers", "task_profile_id", "trigger_policies", "speed_band"}
        policy_overrides = variant.get("policy_overrides") or {}
        if not isinstance(policy_overrides, dict):
            d.append(Diagnostic("VARIANT_POLICY_SHAPE", f"{path}.policy_overrides", "policy_overrides must be an object"))
            policy_overrides = {}
        for field in policy_overrides:
            if field not in allowed_variant_paths:
                d.append(Diagnostic("VARIANT_POLICY_PATH", f"{path}.policy_overrides.{field}", "variant path is not in the policy allowlist"))
            if field in {"q", "population_id", "population_definition_id", "sensory_channels", "allowed_contacts", "anatomy_profile", "history_schema", "thermal_capability_id", "oxygen_capability_id"}:
                d.append(Diagnostic("VARIANT_CAPABILITY_EXPANSION", f"{path}.policy_overrides.{field}", "variant cannot override Species capability"))
        if contract == DSL_CONTRACT_0_3_4_0 and "policy_overrides" not in variant:
            d.append(Diagnostic("VARIANT_POLICY_REQUIRED", f"{path}.policy_overrides", "0.3.4.0 requires an explicit policy override object"))
    seen_consequences: Set[str] = set()
    owners = raw.get("settlement_owners")
    if not isinstance(owners, list) or not owners:
        d.append(Diagnostic("MISSING_SETTLEMENT_OWNER", "settlement_owners", "RC4 requires an explicit owner matrix"))
        owners = []
    valid_owner_roles = {"PROGRAM", "LIFECYCLE", "OCCUPANCY", "PERCEPTION", "MOTIVE", "ENTRY", "FUNCTIONAL", "CONVERSION", "HISTORY", "FUTURE"}
    owner_by_consequence: Dict[str, str] = {}
    for i, owner in enumerate(owners):
        if not isinstance(owner, dict):
            d.append(Diagnostic("OWNER_SHAPE", f"settlement_owners[{i}]", "owner row must be an object"))
            continue
        if set(owner) - {"physical_consequence_id", "owner"}:
            d.append(Diagnostic("UNKNOWN_FIELD", f"settlement_owners[{i}]", "owner row has unsupported field"))
            continue
        consequence = owner.get("physical_consequence_id")
        if not isinstance(consequence, str) or not consequence or consequence in seen_consequences:
            d.append(Diagnostic("DUPLICATE_SETTLEMENT_OWNER", f"settlement_owners[{i}]", "physical consequence must have one owner"))
        elif consequence:
            seen_consequences.add(consequence)
        if owner.get("owner") not in valid_owner_roles:
            d.append(Diagnostic("INVALID_SETTLEMENT_OWNER", f"settlement_owners[{i}].owner", "unknown Cause Role owner"))
        elif consequence:
            owner_by_consequence[consequence] = owner["owner"]
    allowed_world_facts = {"water_temperature_c", "dissolved_oxygen_mg_l", "flow_vector", "depth_m", "structure_tags", "substrate", "illumination_lux", "turbidity", "resource_state", "barometric_pressure_hpa", "barometric_trend"}
    world_facts = raw.get("world_facts") or []
    if not isinstance(world_facts, list):
        d.append(Diagnostic("WORLD_FACTS_SHAPE", "world_facts", "world_facts must be a list"))
        world_facts = []
    for i, fact in enumerate(world_facts):
        if not isinstance(fact, str) or fact not in allowed_world_facts:
            d.append(Diagnostic("WORLD_FACT_IS_INTERPRETATION", f"world_facts[{i}]", "World Fact must be species-neutral"))
    world_fact_set = {fact for fact in world_facts if isinstance(fact, str)}
    allowed_rule_fields = {"rule_id", "priority", "when", "requires", "then", "consequence_id", "owner", "effective_interval"}
    rule_ids: Set[str] = set()
    resolver_rules = raw.get("resolver_rules") or []
    if not isinstance(resolver_rules, list):
        d.append(Diagnostic("RULES_SHAPE", "resolver_rules", "resolver_rules must be a list"))
        resolver_rules = []
    for i, rule in enumerate(resolver_rules):
        if not isinstance(rule, dict):
            d.append(Diagnostic("RULE_SHAPE", f"resolver_rules[{i}]", "rule must be an object"))
            continue
        for field in set(rule) - allowed_rule_fields:
            d.append(Diagnostic("UNKNOWN_FIELD", f"resolver_rules[{i}].{field}", "unsupported resolver rule field"))
        for required in ("rule_id", "priority", "consequence_id", "owner"):
            if required not in rule:
                d.append(Diagnostic("RULE_FIELD_REQUIRED", f"resolver_rules[{i}].{required}", "required resolver rule field"))
        rule_id = rule.get("rule_id")
        if isinstance(rule_id, str) and rule_id in rule_ids:
            d.append(Diagnostic("DUPLICATE_ID", f"resolver_rules[{i}].rule_id", "rule id must be unique"))
        if isinstance(rule_id, str) and rule_id:
            rule_ids.add(rule_id)
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
        elif (rule.get("consequence_id") in owner_by_consequence
              and isinstance(rule.get("owner"), str)
              and rule.get("owner") != owner_by_consequence.get(rule.get("consequence_id"))):
            d.append(Diagnostic("OWNER_MISMATCH", f"resolver_rules[{i}].owner", "rule owner must match settlement owner matrix"))
        requires = rule.get("requires", [])
        if not isinstance(requires, list) or not all(isinstance(ref, str) and ref for ref in requires):
            d.append(Diagnostic("RULE_REQUIRES", f"resolver_rules[{i}].requires", "requires must be a list of stable capability references"))
        elif any(ref not in capability_tasks and ref not in contacts for ref in requires):
            d.append(Diagnostic("MISSING_REFERENCE", f"resolver_rules[{i}].requires", "rule requires an undeclared Species capability"))
        if isinstance(rule.get("then"), dict):
            forbidden = {"script", "random", "rng", "loop", "while", "for", "side_effect", "write_state"}
            for key in forbidden & set(rule["then"]):
                d.append(Diagnostic("UNSUPPORTED_EXECUTION", f"resolver_rules[{i}].then.{key}", "DSL cannot contain scripts, randomness, loops or side effects"))
        if contract == DSL_CONTRACT_0_3_4_0:
            when = rule.get("when")
            if not isinstance(when, dict) or not when:
                d.append(Diagnostic("RULE_WHEN_REQUIRED", f"resolver_rules[{i}].when", "0.3.4.0 requires a typed predicate"))
            elif set(when) - {"fact", "eq", "gt", "gte", "lt", "lte"}:
                d.append(Diagnostic("PREDICATE_OPERATOR", f"resolver_rules[{i}].when", "unsupported typed scalar predicate operator"))
            elif when.get("fact") not in world_fact_set:
                d.append(Diagnostic("MISSING_REFERENCE", f"resolver_rules[{i}].when.fact", "rule references an undeclared World Fact"))
            else:
                operators = set(when) - {"fact"}
                if not operators:
                    d.append(Diagnostic("PREDICATE_OPERATOR", f"resolver_rules[{i}].when", "predicate requires a comparison operator"))
                for operator in operators:
                    value = when.get(operator)
                    if operator != "eq" and (not isinstance(value, (int, float)) or isinstance(value, bool)):
                        d.append(Diagnostic("PREDICATE_TYPE", f"resolver_rules[{i}].when.{operator}", "numeric comparison requires a finite number"))
            if not isinstance(rule.get("requires"), list):
                d.append(Diagnostic("RULE_REQUIRES_REQUIRED", f"resolver_rules[{i}].requires", "0.3.4.0 requires an explicit capability list"))
            then = rule.get("then")
            if not isinstance(then, dict) or len(then) != 1:
                d.append(Diagnostic("RULE_THEN_TYPED", f"resolver_rules[{i}].then", "then must contain exactly one typed output"))
            elif next(iter(then)) not in {"entry_grade", "motive", "occupancy_grade", "deny"}:
                d.append(Diagnostic("RULE_THEN_TYPED", f"resolver_rules[{i}].then", "unsupported typed output"))
            if not isinstance(rule.get("effective_interval"), dict):
                d.append(Diagnostic("INTERVAL_REQUIRED", f"resolver_rules[{i}].effective_interval", "0.3.4.0 requires an effective interval"))
            if isinstance(rule.get("consequence_id"), str) and rule.get("consequence_id") not in owner_by_consequence:
                d.append(Diagnostic("MISSING_SETTLEMENT_OWNER", f"resolver_rules[{i}].consequence_id", "consequence must have exactly one settlement owner"))
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
        for j, other in enumerate(resolver_rules[i + 1:], i + 1):
            predicates_overlap = _typed_predicates_may_overlap(rule.get("when"), other.get("when"))
            b = other.get("effective_interval") if isinstance(other, dict) else None
            intervals_overlap = True
            if a and b and isinstance(a, dict) and isinstance(b, dict):
                same_clock = a.get("unit") == b.get("unit") and a.get("clock") == b.get("clock")
                comparable = all(isinstance(interval.get(key), (int, float))
                                 for interval in (a, b) for key in ("start", "end"))
                intervals_overlap = (not comparable or not same_clock or
                                     (a.get("start", 0) < b.get("end", 0) and b.get("start", 0) < a.get("end", 0)))
            if rule.get("priority") == (other.get("priority") if isinstance(other, dict) else None) and predicates_overlap and intervals_overlap:
                d.append(Diagnostic("EQUAL_PRIORITY_OVERLAP", f"resolver_rules[{i},{j}]", "equal-priority overlapping rules are ambiguous"))
    arrival = raw.get("arrival") or {}
    if not isinstance(arrival, dict):
        d.append(Diagnostic("ARRIVAL_SHAPE", "arrival", "arrival must be an object"))
        arrival = {}
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
    try:
        normalized = json.loads(json.dumps(raw, sort_keys=True, allow_nan=False))
    except (TypeError, ValueError) as exc:
        raise DSLCompileError([Diagnostic("NON_JSON_AUTHORING_VALUE", "$", str(exc))]) from exc
    canonical_payload = {"contract": contract, "input_revision": input_revision, "authoring": normalized}
    canonical = json.dumps(canonical_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    fingerprint = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    artifact = dict(normalized)
    artifact["artifact_version"] = normalized.get("schema_version")
    artifact["compiler_contract"] = contract
    artifact["source_path"] = source_path
    artifact["input_revision"] = input_revision
    artifact["semantic_fingerprint"] = fingerprint
    artifact["diagnostics"] = []
    artifact["reference_index"] = {
        "species_id": artifact.get("species", {}).get("id"),
        "population_ids": sorted(item.get("id") for item in artifact.get("population_definitions", []) if isinstance(item, dict) and item.get("id")),
        "slice_ids": sorted(item.get("id") for item in artifact.get("population_slices", []) if isinstance(item, dict) and item.get("id")),
        "program_ids": sorted(item.get("id") for item in artifact.get("programs", []) if isinstance(item, dict) and item.get("id")),
        "variant_ids": sorted(item.get("id") for item in artifact.get("variants", []) if isinstance(item, dict) and item.get("id")),
        "world_facts": sorted(artifact.get("world_facts", [])),
        "consequence_owners": {item.get("physical_consequence_id"): item.get("owner") for item in artifact.get("settlement_owners", []) if isinstance(item, dict)},
    }
    artifact["runtime_view"] = {
        "resolver_rules": sorted(
            artifact.get("resolver_rules", []),
            key=lambda rule: (rule.get("priority", 0), rule.get("rule_id", "")),
        ),
        "trace_contract": artifact.get("trace_contract"),
        "rules_by_owner": {
            owner: sorted((rule for rule in artifact.get("resolver_rules", []) if rule.get("owner") == owner), key=lambda rule: (rule.get("priority", 0), rule.get("rule_id", "")))
            for owner in sorted({rule.get("owner") for rule in artifact.get("resolver_rules", []) if rule.get("owner")})
        },
    }
    return CompiledArtifact(artifact)
