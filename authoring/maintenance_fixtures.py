"""Executable maintenance operations for the current-contract authoring gate."""
from copy import deepcopy
import json
from pathlib import Path


def load_base():
    return json.loads((Path(__file__).parent / "bass_v0.json").read_text())


def add_normal_species(doc):
    out = deepcopy(doc)
    out["species"]["species_id"] = "Trout"
    out["species"]["slow_facts"] = {"FeedingReadiness": "NORMAL", "FeedingCueDisposition": {"SHAD": "NEUTRAL"}}
    return out


def add_engagement_mode(doc):
    out = deepcopy(doc)
    out["species"]["engagement_modes"].append({
        "id": "AMBUSH",
        "bake_program_ref": "BAKE_AMBUSH",
        "response_program_ref": "RESPONSE_AMBUSH",
        "quality_selection_program_ref": "QUALITY_DEFAULT",
    })
    out["surface_programs"]["bake"].append({"id": "BAKE_AMBUSH", "dsl": "return ambush_fit * weight"})
    out["surface_programs"]["response"].append({"id": "RESPONSE_AMBUSH", "rules": [
        {"id": "AMBUSH_STRIKE", "intent": "SET_RESPONSE_BAND", "band": "HIGH"},
        {"id": "AMBUSH_FALLBACK", "intent": "SET_RESPONSE_BAND", "band": "LOW", "fallback": True},
    ]})
    return out


def change_readiness(doc):
    out = deepcopy(doc)
    out["species"]["slow_facts"]["FeedingReadiness"] = "HIGH"
    return out


def add_cue_family(doc):
    out = deepcopy(doc)
    out["species"]["slow_facts"]["FeedingCueDisposition"]["FROG"] = "PREFERRED"
    return out


def maintenance_costs():
    return [
        {"operation": "Add normal Species", "files_touched": 1, "nodes_added": 1, "shared_reused": "default routing + surface programs", "cross_owner_edits": 0},
        {"operation": "Add EngagementMode", "files_touched": 1, "nodes_added": 3, "shared_reused": "QualitySelection + typed Response intents", "cross_owner_edits": 0},
        {"operation": "Change FeedingReadiness", "files_touched": 1, "nodes_added": 1, "shared_reused": "routing + all surface programs", "cross_owner_edits": 0},
        {"operation": "Add CueFamily", "files_touched": 1, "nodes_added": 1, "shared_reused": "Response Programs", "cross_owner_edits": 0},
    ]
