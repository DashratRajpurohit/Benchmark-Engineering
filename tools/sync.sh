#!/usr/bin/env bash
# Pull every Olympus problem on this account into .raw/ and rebuild problems/ + README.md.
# Needs: olympus CLI (logged in), python3.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .raw
olympus problems mine --json > .raw/mine.json
for id in $(python3 -c 'import json,sys; [print(p["_id"]) for p in json.load(open(".raw/mine.json"))]'); do
  olympus problems download "$id" --out ".raw/$id" --force --json > ".raw/$id.dl.json"
  olympus problems view "$id" --json > ".raw/$id.view.json"
done
python3 tools/build.py
git status --short
