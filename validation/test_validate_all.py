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


class GlossaryValidationTests(unittest.TestCase):
    VALID = (
        "# NOEMA\n\nIntro.\n\n## Language\n\n### Identity\n\n"
        "**Player**:\nThe in-world identity of an Agent.\n_Avoid_: human player\n\n"
        "**Controller**:\nSoftware that connects an Agent to the world.\n\n"
        "## Avoid\n\n- Do not mention v0.1 Durable Object hosting here; rules are not checked.\n"
    )

    def run_check(self, text: str):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            (root / "GLOSSARY.md").write_text(text, encoding="utf-8")
            validator.ROOT = root
            with patch.object(validator, "fail", side_effect=SystemExit(1)) as fail:
                try:
                    validator.check_glossary()
                except SystemExit:
                    pass
            return fail

    def assert_fails_with(self, text: str, *fragments: str) -> None:
        fail = self.run_check(text)
        fail.assert_called_once()
        for fragment in fragments:
            self.assertIn(fragment, fail.call_args.args[0])

    def test_well_formed_glossary_passes(self) -> None:
        self.run_check(self.VALID).assert_not_called()

    def test_missing_definition_fails(self) -> None:
        text = self.VALID.replace("Software that connects an Agent to the world.\n", "")
        self.assert_fails_with(text, "Controller", "definition")

    def test_duplicate_term_fails(self) -> None:
        text = self.VALID.replace("**Controller**:", "**Player**:")
        self.assert_fails_with(text, "Player", "twice")

    def test_implementation_token_fails(self) -> None:
        text = self.VALID.replace("Software that connects", "Durable Object software that connects")
        self.assert_fails_with(text, "Controller", "Durable Object")

    def test_version_tag_fails(self) -> None:
        text = self.VALID.replace("The in-world identity", "The v0.1 in-world identity")
        self.assert_fails_with(text, "Player", "v0.1")

    def test_avoid_line_is_not_a_definition(self) -> None:
        text = self.VALID.replace("The in-world identity of an Agent.\n", "")
        self.assert_fails_with(text, "Player", "definition")

    def test_missing_language_section_fails(self) -> None:
        self.assert_fails_with("# NOEMA\n\nNo terms.\n", "## Language")


class GraftTrackedTests(unittest.TestCase):
    def run_check(self, gitignore: str):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            (root / ".gitignore").write_text(gitignore, encoding="utf-8")
            validator.ROOT = root
            with patch.object(validator, "fail", side_effect=SystemExit(1)) as fail:
                try:
                    validator.check_graft_tracked()
                except SystemExit:
                    pass
            return fail

    def test_cache_only_ignore_passes(self) -> None:
        self.run_check(".venv/\ngraft/.cache/\n").assert_not_called()

    def test_ignoring_whole_graft_dir_fails(self) -> None:
        for line in ("/graft/", "graft/", "graft", "/graft"):
            with self.subTest(line=line):
                fail = self.run_check(f"graft/.cache/\n# note\n{line}\n")
                fail.assert_called_once()
                self.assertIn("GRAFT_NO_GITIGNORE", fail.call_args.args[0])


class DependencySmokeTests(unittest.TestCase):
    def test_dependency_preflight_returns_validator_when_installed(self) -> None:
        validator = load_validator()
        self.assertIsNotNone(validator.try_import_jsonschema())


if __name__ == "__main__":
    unittest.main()
