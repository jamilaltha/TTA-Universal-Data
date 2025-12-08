#!/usr/bin/env bash
set -euo pipefail

jupyter nbconvert --to html --execute notebooks/*.ipynb
mv notebooks/*.html docs/validation/
