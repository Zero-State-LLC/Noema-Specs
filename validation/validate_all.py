#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# SIZE_LIMIT: local file is 517623 bytes / blob faae1e940a8d491836a3982913e8855b67d8d9d5.
# GitHub MCP push_files and create_or_update_file require the UTF-8 body inline.
# CallMcpTool cannot carry ~550KB JSON-escaped content (Read cap 100000 chars).
# Do not treat this stub as the restored validator.
