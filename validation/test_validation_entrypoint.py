#!/usr/bin/env python3
"""Exercise the shell boundary with a recording interpreter, never recursive discovery.

These orchestration tests do not replace real repository validation.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ["-m", "unittest", "discover", "-s", "validation", "-p", "test_*.py"],
    ["validation/validate_all.py"],
    ["validation/validate_direction.py"],
    ["validation/validate_freshness.py", "--offline"],
    ["validation/validate_gateb_traceability.py"],
]


class ValidationEntrypointTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(
            prefix="noema-entrypoint-", dir=os.environ.get("JCODE_SCRATCH_DIR")
        )
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "specs with spaces"
        (self.root / "validation").mkdir(parents=True)
        shutil.copy2(ROOT / "validation/run.sh", self.root / "validation/run.sh")
        shutil.copy2(
            ROOT / "validation/requirements-validation.txt",
            self.root / "validation/requirements-validation.txt",
        )
        self.venv = self.root / "test venv"
        (self.venv / "bin").mkdir(parents=True)
        interpreter = self.venv / "bin/python"
        interpreter.write_text(
            f"#!{sys.executable}\n"
            "import json, os, sys\n"
            "with open(os.environ['CALL_LOG'], 'a') as log:\n"
            "    log.write(json.dumps({'args': sys.argv[1:], 'cwd': os.getcwd()}) + '\\n')\n"
            "if sys.argv[1:] == json.loads(os.environ.get('FAIL_COMMAND', '[]')):\n"
            "    sys.exit(37)\n",
            encoding="utf-8",
        )
        interpreter.chmod(0o755)
        self.log = self.root / "calls.jsonl"
        self.install = [
            "-m", "pip", "install", "--disable-pip-version-check", "-q",
            "-r", str(self.root / "validation/requirements-validation.txt"),
        ]

    def run_entrypoint(self, failure: list[str] | None = None):
        self.log.unlink(missing_ok=True)
        result = subprocess.run(
            ["bash", str(self.root / "validation/run.sh")],
            cwd=self.root.parent,
            env={
                **os.environ,
                "NOEMA_VALIDATION_VENV": str(self.venv),
                "CALL_LOG": str(self.log),
                "FAIL_COMMAND": json.dumps(failure or []),
            },
            capture_output=True, text=True, timeout=30,
        )
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        return result, calls

    def test_runs_all_checks_from_repository_root(self) -> None:
        result, calls = self.run_entrypoint()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([call["args"] for call in calls], [self.install, *CHECKS])
        self.assertTrue(all(call["cwd"] == str(self.root) for call in calls[1:]))

    def test_preserves_each_failure_and_stops_before_later_checks(self) -> None:
        commands = [self.install, *CHECKS]
        for index, command in enumerate(commands):
            with self.subTest(command=command):
                result, calls = self.run_entrypoint(failure=command)
                self.assertEqual(result.returncode, 37, result.stderr)
                self.assertEqual([call["args"] for call in calls], commands[:index + 1])


class CIWorkflowTests(unittest.TestCase):
    def test_ci_runs_required_entrypoint_on_push_and_pull_request(self) -> None:
        # BaseLoader preserves GitHub's `on` key rather than YAML 1.1's boolean.
        workflow = yaml.load(
            (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
            Loader=yaml.BaseLoader,
        )
        for event in ("push", "pull_request"):
            self.assertEqual(workflow["on"][event]["branches"], ["main"])
        job = workflow["jobs"]["build"]
        self.assertNotIn("if", job)
        self.assertNotIn("continue-on-error", job)
        checks = [step for step in job["steps"] if step.get("run", "").strip() == "bash validation/run.sh"]
        self.assertEqual(len(checks), 1, "CI must run the shared validation entrypoint")
        self.assertNotIn("if", checks[0])
        self.assertNotIn("continue-on-error", checks[0])


if __name__ == "__main__":
    unittest.main()
