#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator.

Readable source is 517623 bytes. GitHub MCP file-push payload limits prevent
inlining that UTF-8 body; this loader gunzips the ascii85 parts beside it and
execs the original module so `python validation/validate_all.py` is unchanged.
"""
from __future__ import annotations

import base64
import gzip
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_PAYLOAD = "".join(
    (_HERE / name).read_text(encoding="ascii")
    for name in ("_va_p1.txt", "_va_p2a.txt", "_va_p2b.txt")
)
exec(gzip.decompress(base64.b85decode(_PAYLOAD)), globals())
