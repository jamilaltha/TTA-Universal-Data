#!/usr/bin/env bash
set -euo pipefail

echo "[run_all_validations] Ejecutando notebooks de validación..."
jupyter nbconvert --to html --execute notebooks/01_reproduce_sparc.ipynb
jupyter nbconvert --to html --execute notebooks/02_reproduce_hubble.ipynb
jupyter nbconvert --to html --execute notebooks/03_reproduce_filaments.ipynb

mkdir -p docs/validation
mv notebooks/*.html docs/validation/ || true

echo "[run_all_validations] OK."
