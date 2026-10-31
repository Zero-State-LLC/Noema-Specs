#!/usr/bin/env python3
"""Campaign invariant tests for the direction validator."""

from __future__ import annotations

import importlib.util
import tempfile
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


class GateContractTests(unittest.TestCase):
    LOCKED = "# PSR-1\n\n| Cohort | 6 |\n"
    UNLOCKED = "# PSR-1\n\n| Cohort | TO LOCK |\n"

    def campaign(self, active_gate="Gate PSR-1: compatibility-at-scale (BLOCKED on criteria)", **contracts):
        return {
            "id": "next-campaign",
            "state": "ACTIVE_INTEGRATION",
            "active_gate": active_gate,
            "unproven_gates": ["Gate PSR-1: compatibility-at-scale", "Gate PSR-2: hosted STUDY"],
            "gate_contracts": contracts
            or {"PSR-1": "docs/PSR-1.md", "PSR-2": "docs/PSR-2.md"},
        }

    def run_check(self, campaign, psr1=UNLOCKED, psr2=UNLOCKED, linked=("docs/PSR-1.md", "docs/PSR-2.md")):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            (root / "docs").mkdir()
            (root / "docs/PSR-1.md").write_text(psr1, encoding="utf-8")
            (root / "docs/PSR-2.md").write_text(psr2, encoding="utf-8")
            campaign_doc = "\n".join(f"[x]({Path(rel).name})" for rel in linked)
            validator.check_gate_contracts(campaign, root, campaign_doc)

    def assert_fails_with(self, *fragments, **kwargs) -> None:
        with self.assertRaises(SystemExit) as raised:
            self.run_check(**kwargs)
        for fragment in fragments:
            self.assertIn(fragment, str(raised.exception))

    def test_blocked_gates_with_linked_contracts_pass(self) -> None:
        self.run_check(self.campaign())

    def test_unproven_gate_without_contract_fails(self) -> None:
        self.assert_fails_with("PSR-2", "contract", campaign=self.campaign(**{"PSR-1": "docs/PSR-1.md"}))

    def test_contract_not_linked_from_campaign_doc_fails(self) -> None:
        self.assert_fails_with("PSR-2", "linked", campaign=self.campaign(), linked=("docs/PSR-1.md",))

    def test_unblocked_active_gate_with_to_lock_fails(self) -> None:
        campaign = self.campaign(active_gate="Gate PSR-1: compatibility-at-scale (criteria locked)")
        self.assert_fails_with("PSR-1", "TO LOCK", campaign=campaign)

    def test_unblocked_active_gate_with_to_name_fails(self) -> None:
        campaign = self.campaign(active_gate="Gate PSR-1: compatibility-at-scale (criteria locked)")
        self.assert_fails_with("PSR-1", "TO NAME", campaign=campaign, psr1="# PSR-1\n\nSteward: TO NAME\n")

    def test_unblocked_active_gate_fully_locked_passes(self) -> None:
        campaign = self.campaign(active_gate="Gate PSR-1: compatibility-at-scale (criteria locked)")
        self.run_check(campaign, psr1=self.LOCKED)


if __name__ == "__main__":
    unittest.main()
