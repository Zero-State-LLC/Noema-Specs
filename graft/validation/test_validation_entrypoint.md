# validation/test_validation_entrypoint.py

- ValidationEntrypointTests · class · L31-L109 — class ValidationEntrypointTests(unittest.TestCase)
- setUp · method · L32-L51 — def setUp(self) -> None
- write_recording_interpreter · method · L53-L70 — def write_recording_interpreter(self, host_interpreter: Path) -> None
- run_entrypoint · method · L72-L86 — def run_entrypoint(self, failure: list[str] | None = None)
- test_runs_checks_when_host_interpreter_path_contains_spaces · method · L88-L95 — def test_runs_checks_when_host_interpreter_path_contains_spaces(self) -> None
- test_runs_all_checks_from_repository_root · method · L97-L101 — def test_runs_all_checks_from_repository_root(self) -> None
- test_preserves_each_failure_and_stops_before_later_checks · method · L103-L109 — def test_preserves_each_failure_and_stops_before_later_checks(self) -> None
- CIWorkflowTests · class · L112-L127 — class CIWorkflowTests(unittest.TestCase)
- test_ci_runs_required_entrypoint_on_push_and_pull_request · method · L113-L127 — def test_ci_runs_required_entrypoint_on_push_and_pull_request(self) -> None: # BaseLoader preserves GitHub's `on` key rather than YAML 1.1's boolean.
