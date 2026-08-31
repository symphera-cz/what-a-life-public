#!/usr/bin/env bash
# Zabalí každý skill do samostatného ZIPu pro nahrání na claude.ai
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for d in plugins/what-a-life/skills/*/; do
  name=$(basename "$d")
  (cd plugins/what-a-life/skills && zip -qr "../../dist/$name.zip" "$name")
  echo "OK  $name.zip"
done
echo
echo "Hotovo. ZIPy jsou v: dist/"
