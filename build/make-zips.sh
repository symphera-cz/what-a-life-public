#!/usr/bin/env bash
# Zabalí každý skill do samostatného ZIPu pro nahrání na claude.ai
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$PWD"

mkdir -p dist
# Maž jen ZIPy — v dist/ jsou i ručně udržované soubory (xlsx šablona, balíček pro ChatGPT)
rm -f dist/*.zip

for d in plugins/what-a-life/skills/*/; do
  name=$(basename "$d")
  (cd plugins/what-a-life/skills && zip -qr "$ROOT/dist/$name.zip" "$name")
  echo "OK  $name.zip"
done

echo
echo "Hotovo. ZIPy jsou v: dist/"
