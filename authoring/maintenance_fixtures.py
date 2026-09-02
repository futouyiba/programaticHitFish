"""Four executable maintenance operations used by the IA gate."""
from copy import deepcopy
import json
from pathlib import Path

def load_base(): return json.loads((Path(__file__).parent / "bass_v0.json").read_text())

def add_normal_species(doc):
    out=deepcopy(doc); out["species"]={"species_id":"Trout","slow_facts":{"FeedingReadiness":"NORMAL","FeedingCueDisposition":{"SHAD":"NEUTRAL"}},"fish_modes":[{"id":"NORMAL","pathways":["FEEDING"]}]}; return out

def add_grammar_mode(doc):
    out=deepcopy(doc); out["species"]["fish_modes"].append({"id":"AMBUSH","pathways":["AMBUSH_STRIKE"]}); out["pathways"].append({"id":"AMBUSH_STRIKE"}); out["rules"].append({"id":"AMBUSH_STRIKE_RULE","priority":30,"grade":"HIGH","operation":"SET","conditions":{"mode":"AMBUSH"}}); return out

def change_readiness(doc):
    out=deepcopy(doc); out["species"]["slow_facts"]["FeedingReadiness"]="HIGH"; return out

def add_cue_family(doc):
    out=deepcopy(doc); out["species"]["slow_facts"]["FeedingCueDisposition"]["FROG"]="PREFERRED"; return out

def maintenance_costs():
    return [
      {"operation":"Add normal Species","files_touched":1,"nodes_added":1,"shared_reused":"NORMAL_FEEDING, pathways, profiles","cross_owner_edits":0},
      {"operation":"Add FishMode","files_touched":1,"nodes_added":3,"shared_reused":"ResponseGrade, SET rule","cross_owner_edits":0},
      {"operation":"Change FeedingReadiness","files_touched":1,"nodes_added":1,"shared_reused":"all policies/lifecycle/spatial","cross_owner_edits":0},
      {"operation":"Add CueFamily","files_touched":1,"nodes_added":1,"shared_reused":"Feeding rules and response policy","cross_owner_edits":0},
    ]
