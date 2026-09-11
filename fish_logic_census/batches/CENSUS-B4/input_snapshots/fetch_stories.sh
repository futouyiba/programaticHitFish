#!/bin/sh
# CENSUS-B4 story fetch loop: 26 stories, order = packet_R07 table rows 1-26.
# Each line: CODE|URL
set -e
cd "$(dirname "$0")"
while IFS='|' read -r code url; do
  case "$code" in \#*|"") continue;; esac
  out="story_${code}.md"
  if [ -s "$out" ]; then echo "SKIP $code (exists)"; continue; fi
  echo "== fetching $code -> $url"
  ./fetch_notion.sh "$url" "$out" || echo "FAILED $code"
done < story_urls.txt
echo ALL_DONE
