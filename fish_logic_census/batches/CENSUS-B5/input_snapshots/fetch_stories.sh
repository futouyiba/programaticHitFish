#!/bin/sh
# CENSUS-B5 story fetch loop: 52 stories (R08 26 + R09 26), order = packet table rows.
set -e
cd "$(dirname "$0")"
for list in story_urls_R08.txt story_urls_R09.txt; do
  while IFS='|' read -r code url; do
    case "$code" in \#*|"") continue;; esac
    out="story_${code}.md"
    if [ -s "$out" ]; then echo "SKIP $code (exists)"; continue; fi
    echo "== fetching $code -> $url"
    ./fetch_notion.sh "$url" "$out" || echo "FAILED $code"
  done < "$list"
done
echo ALL_DONE
