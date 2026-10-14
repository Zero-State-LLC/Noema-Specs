# validation/test_validation_entrypoint.py

- ValidationEntrypointTests · class · L30-L90 — class ValidationEntrypointTests(unittest.TestCase)
- setUp · method · L31-L60 — def setUp(self) -> None
- run_entrypoint · method · L62-L76 — def run_entrypoint(self, failure: list[str] | None = None)
- test_runs_all_checks_from_repository_root · method · L78-L82 — def test_runs_all_checks_from_repository_root(self) -> None
- test_preserves_each_failure_and_stops_before_later_checks · method · L84-L90 — def test_preserves_each_failure_and_stops_before_later_checks(self) -> None
- CIWorkflowTests · class · L93-L108 — class CIWorkflowTests(unittest.TestCase)
- test_ci_runs_required_entrypoint_on_push_and_pull_request · method · L94-L108 — def test_ci_runs_required_entrypoint_on_push_and_pull_request(self) -> None: # BaseLoader preserves GitHub's `on` key rather than YAML 1.1's boolean.
