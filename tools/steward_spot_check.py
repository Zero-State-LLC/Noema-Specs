#!/usr/bin/env python3
"""Steward 3-artifact spot-check sampler for #423 (ADR-0009)."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any


def sample_steward_artifacts(pack_dir: Path, seed: int = 42) -> dict[str, Any]:
    rng = random.Random(seed)
    all_files = sorted(p.relative_to(pack_dir).as_posix() for p in pack_dir.rglob("*") if p.is_file())
    if not all_files:
        return {"ok": False, "error": "pack_dir contains no files", "sampled": []}

    categories = {
        "message": [f for f in all_files if "message" in f.lower() or "chat" in f.lower()],
        "observation": [f for f in all_files if "obs" in f.lower() or "turn" in f.lower()],
        "metadata": [f for f in all_files if "manifest" in f.lower() or "meta" in f.lower() or "receipt" in f.lower()],
    }
    sampled: list[dict[str, str]] = []
    chosen: set[str] = set()
    for cat, pool in categories.items():
        candidates = [f for f in pool if f not in chosen]
        if candidates:
            pick = rng.choice(candidates)
            chosen.add(pick)
            sampled.append({"category": cat, "path": pick})

    remaining = [f for f in all_files if f not in chosen]
    while len(sampled) < min(3, len(all_files)) and remaining:
        pick = rng.choice(remaining)
        remaining.remove(pick)
        chosen.add(pick)
        sampled.append({"category": "general", "path": pick})

    return {
        "ok": len(sampled) >= min(3, len(all_files)),
        "pack_dir": str(pack_dir),
        "seed": seed,
        "sample_count": len(sampled),
        "sampled": sampled,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sample 3 artifacts for ADR-0009 Steward spot-check (#423).")
    parser.add_argument("pack_dir", type=Path, help="Exported STUDY pack directory.")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args(argv)
    result = sample_steward_artifacts(args.pack_dir, seed=args.seed)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
