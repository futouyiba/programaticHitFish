#!/bin/sh
# CENSUS-B6 story fetch loop: 47 stories, order = packet_R10 Representative Coverage/Story Links rows 1-47.
set -e
cd "$(dirname "$0")"
while IFS='|' read -r code url; do
  case "$code" in \#*|"") continue;; esac
  out="story_${code}.md"
  if [ -s "$out" ]; then echo "SKIP $code (exists)"; continue; fi
  echo "== fetching $code -> $url"
  ./fetch_notion.sh "$url" "$out" || echo "FAILED $code"
done < story_urls_R10.txt
echo ALL_DONE
