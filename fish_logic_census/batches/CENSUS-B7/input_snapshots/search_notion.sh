#!/bin/sh
# CENSUS-B7 headless Notion search helper (read-only).
# Usage: search_notion.sh "<query>" <out_file.md> [extra_filters]
set -e
TOKEN=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_AUTH_TOKEN'])")
BASE=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_BASE_URL'])")
Q="$1"; OUT="$2"; EXTRA="${3:-}"
TMP=$(mktemp)
ANTHROPIC_AUTH_TOKEN="$TOKEN" ANTHROPIC_BASE_URL="$BASE" claude -p "用 notion MCP 的 search 工具执行搜索：query=\"$Q\", page_size=100$EXTRA
要求：把每个结果按格式逐行输出到标准输出，用唯一标记包裹：第一行输出 <<SEARCH_BEGIN>>，然后每行一个结果：标题<TAB>URL，最后一行输出 <<SEARCH_END>>。把所有结果都列出来，不要省略、不要总结、不要添加任何自己的话。如果搜索失败，只输出一行 SEARCH_FAIL 加原因。" --allowedTools "mcp__notion__*" --model "glm-5.3" > "$TMP" 2>"$OUT.err"
if grep -q "SEARCH_FAIL" "$TMP"; then echo "SEARCH_FAILED: $Q"; cat "$TMP"; exit 1; fi
python - "$TMP" "$OUT" <<'PYEOF'
import sys, html, io
raw = io.open(sys.argv[1], encoding='utf-8', errors='replace').read()
lines = raw.splitlines()
out, flag = [], False
for ln in lines:
    plain = html.unescape(ln)
    if '<<SEARCH_BEGIN>>' in plain:
        flag = True
        continue
    if '<<SEARCH_END>>' in plain:
        flag = False
        continue
    if flag:
        out.append(plain)
text = '\n'.join(out) + ('\n' if out else '')
io.open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(text)
sys.exit(0 if text.strip() else 1)
PYEOF
if [ ! -s "$OUT" ]; then echo "EMPTY_PARSE for search: $Q"; head -5 "$TMP"; exit 1; fi
echo "saved $(wc -l < "$OUT") result lines -> $OUT"
