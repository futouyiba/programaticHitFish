#!/usr/bin/env python3
"""Small local editor prototype; run: python3 editor/prototype.py"""
import json
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from fcf_v1.authoring import compile_authoring, lint_authoring, AuthoringError

ROOT=Path(__file__).resolve().parents[1]; CONFIG=ROOT/'authoring'/'bass_v0.json'
HTML=(Path(__file__).parent/'index.html').read_text()

class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj, content_type='application/json'):
        data=obj.encode() if isinstance(obj,str) else json.dumps(obj, indent=2).encode()
        self.send_response(code); self.send_header('Content-Type',content_type); self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        if self.path=='/': return self._send(200,HTML,'text/html; charset=utf-8')
        if self.path=='/api/config': return self._send(200,json.loads(CONFIG.read_text()))
        self._send(404,{"error":"not found"})
    def do_POST(self):
        n=int(self.headers.get('Content-Length','0')); doc=json.loads(self.rfile.read(n))
        if self.path=='/api/validate':
            errors=lint_authoring(doc)
            if errors: return self._send(200,{"valid":False,"errors":errors})
            b=compile_authoring(doc); return self._send(200,{"valid":True,"errors":[],"effective":{"slow_facts":b.species_slow_facts,"response":b.response_content_bundle,"contributions":[c.__dict__ for c in b.contributions]}})
        if self.path=='/api/save':
            if lint_authoring(doc): return self._send(422,{"valid":False,"errors":lint_authoring(doc)})
            CONFIG.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n'); return self._send(200,{"saved":True})
        self._send(404,{"error":"not found"})

if __name__=='__main__':
    print('Editor prototype: http://127.0.0.1:8765'); HTTPServer(('127.0.0.1',8765),Handler).serve_forever()
