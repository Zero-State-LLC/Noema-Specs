#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${NOEMA_VALIDATION_VENV:-$ROOT/.venv}"

if [[ ! -x "$VENV_DIR/bin/python" ]]; then
  python3 -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" -m pip install --disable-pip-version-check -q \
  -r "$ROOT/validation/requirements-validation.txt"

cd "$ROOT"
"$VENV_DIR/bin/python" -m unittest discover -s validation -p 'test_*.py'
"$VENV_DIR/bin/python" validation/validate_all.py
"$VENV_DIR/bin/python" validation/validate_direction.py
"$VENV_DIR/bin/python" validation/validate_freshness.py --offline
