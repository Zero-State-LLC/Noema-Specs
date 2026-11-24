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
"$VENV_DIR/bin/python" validation/validate_gateb_traceability.py
PYTHONPATH="$ROOT" "$VENV_DIR/bin/python" -c "import tests.test_locked_contracts as t; t.test_psr1_enrollment_receipt_valid_and_invalid(); t.test_psr1_cohort_summary_valid_and_invalid(); t.test_study_promotion_receipt_valid_and_invalid(); t.test_rfc0131_invite_request_valid_and_invalid()"
