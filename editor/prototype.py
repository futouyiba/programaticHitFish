#!/usr/bin/env python3
"""Small local current-contract editor prototype; run: python3 editor/prototype.py"""
import json
import sys
from copy import deepcopy
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fcf_v1.authoring import compile_authoring, lint_authoring, resolve_mode_bake_config

CONFIG = ROOT / "authoring" / "bass_v0.json"
HTML = (Path(__file__).parent / "index.html").read_text()
BASELINE = json.loads(CONFIG.read_text())
DEMO_ENVIRONMENT_FACTS = {"water_temperature": 22.0}


def _quality_stable_snapshot(doc):
    return {
        q.get("id"): {
            "base_weight": q.get("base_weight"),
            "stable_params": deepcopy(q.get("stable_params", {})),
        }
        for q in doc.get("fish_qualities", [])
        if q.get("id")
    }


def inspect_doc(doc):
    """Return current-contract diagnostics and provenance even for an invalid draft."""
    errors = lint_authoring(doc)
    resolved = {}
    species = doc.get("species", {})
    for mode in species.get("engagement_modes", []):
        key = mode.get("id")
        try:
            resolved[key] = resolve_mode_bake_config(
                doc,
                key,
                environment_facts=DEMO_ENVIRONMENT_FACTS,
            )
        except Exception as exc:
            resolved[key] = {"error": str(exc)}
    return {
        "valid": not errors,
        "errors": errors,
        "resolved_mode_bake_configs": resolved,
        "fish_quality_stable": _quality_stable_snapshot(doc),
        "routing_diagnostics": [
            error for error in errors
            if error.startswith("OVERALLOCATED") or error.startswith("COMPATIBILITY_CONFLICT")
        ],
    }


def reset_config():
    CONFIG.write_text(json.dumps(BASELINE, indent=2, ensure_ascii=False) + "\n")
    return deepcopy(BASELINE)


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj, content_type="application/json"):
        data = obj.encode() if isinstance(obj, str) else json.dumps(obj, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_doc(self):
        n = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(n)) if n else {}

    def do_GET(self):
        if self.path == "/":
            return self._send(200, HTML, "text/html; charset=utf-8")
        if self.path == "/api/config":
            return self._send(200, json.loads(CONFIG.read_text()))
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/api/reset":
            return self._send(200, {"reset": True, "config": reset_config()})

        doc = self._read_doc()
        if self.path == "/api/inspect":
            return self._send(200, inspect_doc(doc))

        if self.path == "/api/validate":
            errors = lint_authoring(doc)
            if errors:
                result = inspect_doc(doc)
                result["valid"] = False
                return self._send(200, result)
            b = compile_authoring(doc)
            current = inspect_doc(doc)
            return self._send(200, {
                "valid": True,
                "errors": [],
                "resolved_mode_bake_configs": current["resolved_mode_bake_configs"],
                "fish_quality_stable": current["fish_quality_stable"],
                "routing_diagnostics": [],
                "effective": {
                    "slow_facts": b.species_slow_facts,
                    "routing": b.engagement_mode_routing_snapshot,
                    "surface_programs": b.surface_program_bundle,
                    "resolved_mode_bake_configs": b.resolved_mode_bake_configs,
                    "contributions": [c.__dict__ for c in b.contributions],
                },
            })

        if self.path == "/api/save":
            errors = lint_authoring(doc)
            if errors:
                return self._send(422, {"valid": False, "errors": errors})
            CONFIG.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
            return self._send(200, {"saved": True})

        self._send(404, {"error": "not found"})


if __name__ == "__main__":
    print("Editor prototype: http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
