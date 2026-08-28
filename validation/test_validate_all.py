#!/usr/bin/env python3
"""Small standard-library smoke tests for the Specs validator."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


VALIDATOR_PATH = Path(__file__).with_name("validate_all.py")


def load_validator():
    spec = importlib.util.spec_from_file_location("noema_specs_validate_all", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MarkdownLinkValidationTests(unittest.TestCase):
    def test_reports_source_target_and_resolved_path(self) -> None:
        validator = load_validator()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            (root / "broken.md").write_text("[missing](missing.md)\n", encoding="utf-8")
            validator.ROOT = root

            with patch.object(validator, "fail", side_effect=SystemExit(1)) as fail:
                with self.assertRaises(SystemExit):
                    validator.check_markdown_links()

            message = fail.call_args.args[0]
            self.assertIn("broken.md -> missing.md", message)
            self.assertIn("(resolved: missing.md)", message)

    def test_ignores_external_anchor_and_outside_root_targets(self) -> None:
        validator = load_validator()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            (root / "target.md").write_text("# Heading\n", encoding="utf-8")
            (root / "links.md").write_text(
                "\n".join(
                    (
                        "[local](target.md#heading)",
                        "[external](https://example.com/missing.md)",
                        "[anchor](#heading)",
                        "[mail](mailto:test@example.com)",
                        "[outside](../missing.md)",
                    )
                ),
                encoding="utf-8",
            )
            validator.ROOT = root

            with patch.object(validator, "fail") as fail:
                validator.check_markdown_links()

            fail.assert_not_called()


class DependencySmokeTests(unittest.TestCase):
    def test_dependency_preflight_returns_validator_when_installed(self) -> None:
        validator = load_validator()
        self.assertIsNotNone(validator.try_import_jsonschema())


if __name__ == "__main__":
    unittest.main()
