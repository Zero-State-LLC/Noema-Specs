"""Tests for .agents/docs.py: generated blocks, procedure runner, lifecycle checks.

Run: python3 -m unittest discover -s .agents -p 'test_*.py'
Lives in .agents/ so the committed graft index (which skips dot-directories) is unaffected.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("docs_machine", HERE / "docs.py")
assert _spec and _spec.loader
D = importlib.util.module_from_spec(_spec)
sys.modules["docs_machine"] = D
_spec.loader.exec_module(D)


class RepoState(unittest.TestCase):
    def test_check_passes(self) -> None:
        self.assertEqual(D.check(), [])

    def test_skills_block_is_the_whole_procedure_manual(self) -> None:
        procs = json.loads(D.PROCEDURES.read_text())
        text = (D.ROOT / "SKILLS.md").read_text()
        self.assertEqual(len(procs["skills"]), 19)
        for name in procs["skills"]:
            self.assertIn(f"## {name}\n**Use when** ", text)


class Procedures(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self._orig = D._run_path
        D._run_path = lambda: Path(self.tmp.name) / "procedure.json"
        self.addCleanup(setattr, D, "_run_path", self._orig)
        self.procs = json.loads(D.PROCEDURES.read_text())

    def test_steps_then_validation_then_done(self) -> None:
        steps = D.steps_of(self.procs["skills"]["SKILL.RFC"])
        self.assertIn("Step 1/4", D.run_cmd(self.procs, ["run", "SKILL.RFC"]))
        with self.assertRaises(D.DocsError):
            D.run_cmd(self.procs, ["step"])  # evidence required
        for i in range(len(steps)):
            out = D.run_cmd(self.procs, ["step", "--evidence", f"did {i}"])
        self.assertIn("VALIDATE:", out)
        self.assertIn("done", D.run_cmd(self.procs, ["step", "--evidence", "review lenses applied"]))

    def test_escalation_stops_the_procedure(self) -> None:
        D.run_cmd(self.procs, ["run", "SKILL.SCHEMA"])
        self.assertIn("ESCALATED", D.run_cmd(self.procs, ["escalate", "--evidence", "public change lacks RFC"]))
        with self.assertRaises(D.DocsError):
            D.run_cmd(self.procs, ["step", "--evidence", "x"])

    def test_unknown_reference_is_caught(self) -> None:
        procs = json.loads(json.dumps(self.procs))
        procs["skills"]["SKILL.RFC"]["validation"] = "Run `SKILL.NOPE`."
        procs["blocks"] = []
        self.assertTrue(any("unknown procedure SKILL.NOPE" in e for e in D.validate_procedures(procs)))


class Lifecycles(unittest.TestCase):
    def setUp(self) -> None:
        self.rfc = json.loads(D.LIFECYCLES.read_text())["kinds"]["rfc"]

    def test_first_keyword_wins(self) -> None:
        n = lambda s: D.normalize(s, self.rfc)  # noqa: E731
        self.assertEqual(n("Draft — proposed security contract; not accepted or implemented."), "Draft")
        self.assertEqual(n("**Accepted / Implemented**"), "Accepted")
        self.assertEqual(n("Superseded by [RFC-0143](RFC-0143-x.md)."), "Superseded")
        self.assertIsNone(n("GOVERNANCE_ESCALATION_REQUIRED"))

    def test_only_forward_moves(self) -> None:
        self.assertTrue(D.forward(self.rfc, "Draft", "Accepted"))
        self.assertTrue(D.forward(self.rfc, "Accepted", "Superseded"))
        self.assertFalse(D.forward(self.rfc, "Accepted", "Draft"))
        self.assertFalse(D.forward(self.rfc, "Rejected", "Accepted"))

    def test_status_parsers(self) -> None:
        pats = self.rfc["status"]
        self.assertEqual(D.status_text("# RFC\n\n## Status\n\n**Accepted**\n", pats), "**Accepted**")
        self.assertEqual(D.status_text("- **Status**: Accepted\n", pats), "Accepted")
        self.assertEqual(D.status_text("**Status: Draft — x.**\n", pats), "Draft — x.")


if __name__ == "__main__":
    unittest.main()


class RunbooksAndChecklists(unittest.TestCase):
    def test_enrollment_approval_needs_the_operators_words(self) -> None:
        procs = json.loads(D.PROCEDURES.read_text())
        rb = procs["runbooks"]["PSR1_TIER3_ENROLLMENT"]
        ids = {st["id"]: D.step_gate(rb, i) for i, st in enumerate(rb["steps"])}
        self.assertEqual(ids["HUMAN_APPROVAL"]["kind"], "user_yes")
        self.assertEqual(ids["RECEIPT"]["kind"], "run")

    def test_checklist_items(self) -> None:
        items = D.checklist_items("- [x] Done thing.\n - [ ] Open thing.\n- not an item\n")
        self.assertEqual(items, {"Done thing.": True, "Open thing.": False})
