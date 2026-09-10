#!/bin/sh
# CENSUS-B3 read-only Notion fetch helper (headless claude -> MCP notion fetch).
# Usage: fetch_notion.sh <notion_url> <out_file.md>
set -e
TOKEN=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_AUTH_TOKEN'])")
BASE=$(python -c "import json;print(json.load(open(r'C:\Users\futou\.claude\settings.json'))['env']['ANTHROPIC_BASE_URL'])")
URL="$1"; OUT="$2"
TMP=$(mktemp)
ANTHROPIC_AUTH_TOKEN="$TOKEN" ANTHROPIC_BASE_URL="$BASE" claude -p "用 notion MCP 的 fetch 工具获取这个页面：$URL
要求：把 fetch 返回的页面 markdown 全文【逐字】输出到标准输出，用唯一标记包裹：第一行输出 <<SNAPSHOT_BEGIN>>，正文逐字输出，最后一行输出 <<SNAPSHOT_END>>（这个结束标记必须一字不差）。不要总结、不要省略、不要添加任何自己的话。如果 fetch 失败或页面不存在，只输出一行 FETCH_FAIL 加原因。" --allowedTools "mcp__notion__*" --model "glm-5.3" > "$TMP" 2>"$OUT.err"
if grep -q "FETCH_FAIL" "$TMP"; then echo "FETCH_FAILED: $URL"; cat "$TMP"; exit 1; fi
# strip the model-catalog warning lines claude prints to stdout, keep between markers
awk '/<<SNAPSHOT_BEGIN>>/{flag=1;next}/<<SNAPSHOT_END>>/{flag=0}flag' "$TMP" > "$OUT"
if [ ! -s "$OUT" ]; then echo "EMPTY_PARSE for $URL; raw:"; head -5 "$TMP"; exit 1; fi
echo "saved $(wc -c < "$OUT") bytes -> $OUT"
