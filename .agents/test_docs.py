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
        self.assertEqual(
            ids["RECEIPT"]["commands"],
            ["python3 tools/check_psr1_readiness.py --enrollment evidence/psr1-study/psr1_tier3_enrollment.json"],
        )

    def test_since_applies_default_and_index_fallback(self) -> None:
        import subprocess
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            def git(*args: str) -> None:
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
            git("init")
            git("config", "user.email", "test@example.com")
            git("config", "user.name", "Test")
            (root / "docs" / "adr").mkdir(parents=True)
            (root / "rfcs").mkdir(parents=True)
            (root / "docs" / "adr" / "0001-bare.md").write_text("# ADR 1\n\nDecision.\n")
            (root / "rfcs" / "RFC-0001-base.md").write_text("# RFC 1\n\nBody.\n")
            (root / "rfcs" / "README.md").write_text("| RFC | Status |\n| --- | --- |\n| [RFC-0001](RFC-0001-base.md) | Accepted |\n")
            git("add", ".")
            git("commit", "-m", "initial")
            (root / "docs" / "adr" / "0001-bare.md").write_text("# ADR 1\n\nStatus: proposed\n\nDecision.\n")
            (root / "rfcs" / "README.md").write_text("| RFC | Status |\n| --- | --- |\n| [RFC-0001](RFC-0001-base.md) | Draft |\n")
            orig_root = D.ROOT
            D.ROOT = root
            try:
                lc = {
                    "kinds": {
                        "adr": {
                            "title": "ADR",
                            "declared": "docs/adr",
                            "files": "docs/adr/[0-9]*.md",
                            "status": ["^status:\\s*(.+)$"],
                            "default": "accepted",
                            "states": ["proposed", "accepted"],
                            "aliases": {"proposed": ["proposed"], "accepted": ["accepted"]},
                            "next": {"proposed": ["accepted"], "accepted": []},
                        },
                        "rfc": {
                            "title": "RFC",
                            "declared": "rfcs/README.md",
                            "files": "rfcs/RFC-[0-9]*.md",
                            "status": ["^status:\\s*(.+)$"],
                            "states": ["Draft", "Accepted"],
                            "aliases": {"Draft": ["draft"], "Accepted": ["accepted"]},
                            "next": {"Draft": ["Accepted"], "Accepted": []},
                            "index": {
                                "file": "rfcs/README.md",
                                "row": "^\\|\\s*\\[RFC-\\d+\\]\\((?P<file>[^)]+)\\)\\s*\\|\\s*(?P<status>[^|]+?)\\s*\\|",
                            },
                        },
                    }
                }
                keys = [v["key"] for v in D.lifecycle_violations(lc, since="HEAD")]
            finally:
                D.ROOT = orig_root
            self.assertIn("adr:0001-bare.md:backward:accepted->proposed", keys)
            self.assertIn("rfc:RFC-0001-base.md:backward:Accepted->Draft", keys)

    def test_unknown_index_status_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "rfcs").mkdir(parents=True)
            (root / "rfcs" / "RFC-0001-a.md").write_text("# RFC 1\n\nStatus: Accepted\n")
            (root / "rfcs" / "README.md").write_text("| RFC | Status |\n| --- | --- |\n| [RFC-0001](RFC-0001-a.md) | INVALID |\n")
            orig_root = D.ROOT
            D.ROOT = root
            try:
                kind = {"title": "RFC", "files": "rfcs/RFC-[0-9]*.md", "status": ["^status:\\s*(.+)$"],
                        "states": ["Draft", "Accepted"], "aliases": {"Draft": ["draft"], "Accepted": ["accepted"]},
                        "next": {"Draft": ["Accepted"], "Accepted": []},
                        "index": {"file": "rfcs/README.md", "row": "^\\|\\s*\\[RFC-\\d+\\]\\((?P<file>[^)]+)\\)\\s*\\|\\s*(?P<status>[^|]+?)\\s*\\|"}}
                keys = [v["key"] for v in D.lifecycle_violations({"kinds": {"rfc": kind}})]
            finally:
                D.ROOT = orig_root
            self.assertEqual(keys, ["rfc:RFC-0001-a.md:unknown_index_status"])

    def test_checklist_items(self) -> None:
        items = D.checklist_items("- [x] Done thing.\n - [ ] Open thing.\n- not an item\n")
        self.assertEqual(items, {"Done thing.": True, "Open thing.": False})


class CrossLinks(unittest.TestCase):
    def test_accepted_spec_needs_an_accepted_intent(self) -> None:
        lc = json.loads(D.LIFECYCLES.read_text())
        spec = lc["kinds"]["spec"]
        self.assertEqual(D.normalize("Draft for review. Not implementation authority.", spec), "draft")
        self.assertEqual(D.normalize("proposed design for review.", spec), "draft")
        self.assertEqual(D.normalize("Specified. Does not implement FE.", spec), "specified")
        field = spec["requires"][0]["field"]
        import re
        self.assertEqual(re.search(field, "**Intent:** [One stage](../intent/2026-11-10-x.md).", re.M).group(1), "2026-11-10-x.md")
        self.assertEqual(re.search(field, "Intent: [x](../intent/2026-11-26-y.md). Spec: …", re.M).group(1), "2026-11-26-y.md")
        self.assertIsNone(re.search(field, "supported by its [intent record](../intent/2026-10-14-z.md).", re.M))
