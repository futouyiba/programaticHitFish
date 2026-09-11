#!/bin/sh
# CENSUS-B7 read-only Notion fetch helper (headless claude -> MCP notion fetch).
# Based on B3-B6 fetch_notion.sh; B7 hardening: tolerate HTML-escaped markers
# (model sometimes emits &lt;&lt;SNAPSHOT_BEGIN&gt;&gt;) and unescape output.
# Usage: fetch_notion.sh <notion_url> <out_file.md>
set -e
TOKEN=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_AUTH_TOKEN'])")
BASE=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_BASE_URL'])")
URL="$1"; OUT="$2"
TMP=$(mktemp)
ANTHROPIC_AUTH_TOKEN="$TOKEN" ANTHROPIC_BASE_URL="$BASE" claude -p "用 notion MCP 的 fetch 工具获取这个页面：$URL
要求：把 fetch 返回的页面 markdown 全文【逐字】输出到标准输出，用唯一标记包裹：第一行输出 <<SNAPSHOT_BEGIN>>，正文逐字输出，最后一行输出 <<SNAPSHOT_END>>（这个结束标记必须一字不差）。不要总结、不要省略、不要添加任何自己的话。如果 fetch 失败或页面不存在，只输出一行 FETCH_FAIL 加原因。" --allowedTools "mcp__notion__*" --model "glm-5.3" > "$TMP" 2>"$OUT.err"
if grep -q "FETCH_FAIL" "$TMP"; then echo "FETCH_FAILED: $URL"; cat "$TMP"; exit 1; fi
# strip the model-catalog warning lines claude prints to stdout, keep between markers;
# accept both raw and HTML-escaped marker forms, then unescape entities via python
python - "$TMP" "$OUT" <<'PYEOF'
import sys, html, io
raw = io.open(sys.argv[1], encoding='utf-8', errors='replace').read()
lines = raw.splitlines()
out, flag = [], False
for ln in lines:
    plain = html.unescape(ln)
    if '<<SNAPSHOT_BEGIN>>' in plain:
        flag = True
        continue
    if '<<SNAPSHOT_END>>' in plain:
        flag = False
        continue
    if flag:
        out.append(plain)
text = '\n'.join(out) + ('\n' if out else '')
io.open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(text)
sys.exit(0 if text.strip() else 1)
PYEOF
if [ ! -s "$OUT" ]; then echo "EMPTY_PARSE for $URL; raw:"; head -5 "$TMP"; exit 1; fi
echo "saved $(wc -c < "$OUT") bytes -> $OUT"
