#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "specs/current-state.v1.yaml"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def get_json(url: str) -> tuple[int | None, dict]:
    request = urllib.request.Request(url, headers={"User-Agent": "noema-spec-freshness/1"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as exc:
        return exc.code, {}
    except urllib.error.URLError:
        return None, {}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    state = yaml.safe_load(STATE.read_text(encoding="utf-8"))
    production = state.get("runtimes", {}).get("production_alpha", {})
    expected_world = production.get("world")
    expected_genesis = production.get("genesis_id")
    endpoints = production.get("required_endpoints")
    if not expected_world or not expected_genesis:
        fail("production world and genesis expectations are required")
    if endpoints != ["/ready", "/version"]:
        fail("production freshness endpoints must be /ready and /version")
    if args.offline:
        print("OK: freshness expectations are structurally complete")
        return

    ready_status, ready = get_json("https://noema.guru/ready")
    version_status, version = get_json("https://noema.guru/version")
    if ready_status is None or version_status is None:
        print("WARN: production freshness could not be determined because noema.guru was unreachable")
        return
    if ready_status != 200 or ready.get("ready") is not True:
        fail(f"/ready unhealthy: HTTP {ready_status}")
    world = ready.get("world", {})
    if world.get("world_id") != expected_world:
        fail(f"live world drift: {world.get('world_id')} != {expected_world}")
    if world.get("genesis_id") != expected_genesis:
        fail(f"live genesis drift: {world.get('genesis_id')} != {expected_genesis}")
    if version_status != 200:
        fail(f"/version missing: HTTP {version_status}")
    if version.get("world_id") != expected_world:
        fail(f"version world drift: {version.get('world_id')} != {expected_world}")
    if not version.get("worker_version_id"):
        fail("/version lacks worker_version_id")
    print(f"OK: live freshness matches {expected_world} / {expected_genesis} / {version['worker_version_id']}")


if __name__ == "__main__":
    main()
