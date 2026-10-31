#!/usr/bin/env python3
"""Campaign invariant tests for the direction validator."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


VALIDATOR_PATH = Path(__file__).with_name("validate_direction.py")


def load_validator():
    spec = importlib.util.spec_from_file_location("noema_specs_validate_direction", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CampaignInvariantTests(unittest.TestCase):
    def campaign(self, **fields):
        base = {
            "id": "next-campaign",
            "state": "ACTIVE_INTEGRATION",
            "active_gate": "Gate 1: Compatibility at scale (BLOCKED on criteria)",
            "unproven_gates": ["Gate 1: Compatibility at scale"],
        }
        base.update(fields)
        return base

    def assert_fails_with(self, campaign, *fragments: str) -> None:
        validator = load_validator()
        with self.assertRaises(SystemExit) as raised:
            validator.check_campaign_invariant(campaign)
        for fragment in ("next-campaign", *fragments):
            self.assertIn(fragment, str(raised.exception))

    def test_active_campaign_with_open_gate_passes(self) -> None:
        load_validator().check_campaign_invariant(self.campaign())

    def test_active_campaign_without_unproven_gates_fails(self) -> None:
        # The #361 state: ACTIVE_INTEGRATION with nothing left to prove.
        self.assert_fails_with(self.campaign(unproven_gates=[]), "unproven_gates")

    def test_active_campaign_whose_active_gate_is_complete_fails(self) -> None:
        self.assert_fails_with(
            self.campaign(active_gate="Gate F: Successor decision packet (COMPLETE)"),
            "active_gate",
        )

    def test_paused_campaign_without_unproven_gates_passes(self) -> None:
        load_validator().check_campaign_invariant(
            self.campaign(state="DEFERRED", active_gate="none", unproven_gates=[])
        )

    def test_paused_campaign_listing_unproven_gates_fails(self) -> None:
        self.assert_fails_with(self.campaign(state="DEFERRED"), "unproven_gates")


if __name__ == "__main__":
    unittest.main()
