#!/bin/sh
# CENSUS-B7 story fetch loop: 112 stories, from fetch_pairs.tsv (id -> url -> title).
# Tolerant loop: failures don't stop; retry pass at end; SKIP if file exists.
cd "$(dirname "$0")"
while IFS="	" read -r id url title; do
  out="${id}.md"
  if [ -s "$out" ]; then echo "SKIP $id (exists)"; continue; fi
  sh fetch_notion.sh "$url" "$out" || echo "FAILED: $id $title"
done < fetch_pairs.tsv
echo "== retry pass =="
while IFS="	" read -r id url title; do
  out="${id}.md"
  if [ -s "$out" ]; then continue; fi
  echo "RETRY $id"
  sh fetch_notion.sh "$url" "$out" || echo "STILL-FAILED: $id $title"
done < fetch_pairs.tsv
echo "== done =="
ls story_*.md 2>/dev/null | wc -l
