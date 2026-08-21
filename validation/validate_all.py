#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# SIZE_PROBE_ONLY: full local file is 517623 bytes / 10323 lines; inlining the exact UTF-8 body exceeds this MCP tool-call payload. Do not commit this stub.
