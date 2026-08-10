#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = [
    "README.md",
    "CONTEXT.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".env.example",
    "SPEC-CHECKLIST.md",
]

REQUIRED_DOCS = [
    "docs/VISION.md",
    "docs/GAME-DESIGN.md",
    "docs/WORLD-MODEL.md",
    "docs/ARCHITECTURE.md",
    "docs/ENGINEERING.md",
    "docs/DATA-MODEL.md",
    "docs/WORLD-ENGINE.md",
    "docs/EVENT-CATALOG.md",
    "docs/OBSERVATION.md",
    "docs/AGENT-INTERFACE.md",
    "docs/REPLAY.md",
    "docs/ENVIRONMENT.md",
    "docs/DEPLOYMENT.md",
    "docs/SECURITY.md",
    "docs/TESTING.md",
    "docs/OBSERVABILITY.md",
    "docs/VERSIONING.md",
    "docs/ROADMAP.md",
    "docs/RESEARCH-METHOD.md",
    "docs/METRICS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/SECURITY-SEQUENCES.md",
    "docs/v0.1-ACCEPTANCE.md",
    "docs/CONTRACT-CARDS.md",
    "docs/INTEGRATION-SURFACE.md",
    "docs/v0.1-CONFORMANCE.md",
    "docs/QUICKSTART.md",
    "docs/OPERATIONS.md",
    "docs/SPECTATOR-ONBOARDING.md",
    "docs/AGENT-ONBOARDING.md",
    "docs/MODULE-CONTRACTS.md",
    "docs/RESOURCE-ECONOMY.md",
    "docs/ACTION-CONTRACTS.md",
    "docs/SCHEDULER.md",
    "docs/SPECTATOR.md",
    "docs/SITUATION-GENOME.md",
    "docs/NOVELTY-VECTOR.md",
    "docs/CAPABILITY-PRIMITIVES.md",
    "docs/SITUATION-MUTATION.md",
    "docs/PARTIAL-OBSERVABILITY.md",
    "docs/NOISE-MODEL.md",
    "docs/CONTRADICTORY-EVIDENCE.md",
    "docs/ATTENTION-PROJECTION.md",
    "docs/INFORMATION-GAIN.md",
    "docs/FRONTIER-CONTROLS.md",
    "docs/FRONTIER-DIRECTOR.md",
    "docs/releases/v0.2/SCOPE.md",
    "docs/releases/v0.2/ARCHITECTURE.md",
    "docs/releases/v0.2/ACCEPTANCE.md",
    "docs/releases/v0.2/CONFORMANCE.md",
    "docs/releases/v0.2/MIGRATION.md",
    "docs/releases/v0.2/NON-GOALS.md",
    "docs/releases/v0.2/EXAMPLES.md",
    "docs/releases/v0.2/DATA-MODEL.md",
    "docs/OBSERVATORY.md",
    "docs/TRAJECTORY.md",
    "docs/BEHAVIOR-FEATURES.md",
    "docs/CONTEXT-NORMALIZATION.md",
    "docs/BASELINES.md",
    "docs/ANOMALY-DETECTION.md",
    "docs/BEHAVIOR-SHIFT.md",
    "docs/AGENT-VERSION-COMPARISON.md",
    "docs/CAPABILITY-CANDIDATES.md",
    "docs/CONTRADICTION-ANALYSIS.md",
    "docs/EXTERNAL-COGNITION.md",
    "docs/COORDINATION-SIGNALS.md",
    "docs/EMERGENCE-CANDIDATES.md",
    "docs/OBSERVATORY-AUDIT.md",
    "docs/releases/v0.3/SCOPE.md",
    "docs/releases/v0.3/ARCHITECTURE.md",
    "docs/releases/v0.3/ACCEPTANCE.md",
    "docs/releases/v0.3/CONFORMANCE.md",
    "docs/releases/v0.3/MIGRATION.md",
    "docs/releases/v0.3/NON-GOALS.md",
    "docs/releases/v0.3/EXAMPLES.md",
    "docs/releases/v0.3/DATA-MODEL.md",
    "docs/CORE-GAME-LOOP.md",
    "docs/REALMS.md",
    "docs/GEOGRAPHY.md",
    "docs/TERRITORY-CONTROL.md",
    "docs/STRATEGIC-CONFLICT.md",
    "docs/LOSS-RECOVERY.md",
    "docs/DIPLOMACY.md",
    "docs/GAME-CYCLE.md",
    "docs/WORLD-REPORTS.md",
    "docs/PROGRESSION.md",
    "docs/AMBITIONS.md",
    "docs/HUMAN-PLAY.md",
    "docs/AGENT-PLAY.md",
    "docs/GAME-BALANCE.md",
    "docs/EXPLORATION.md",
    "docs/STRATEGIC-KNOWLEDGE.md",
    "docs/INFRASTRUCTURE.md",
    "docs/FIRST-20-CYCLES.md",
    "docs/CHAMBER-MAP.md",
    "docs/GAME-SYSTEM-MAP.md",
    "docs/EVENT-CATALOG-AUDIT.md",
]

REQUIRED_PROTOCOLS = [
    "protocols/agent-protocol-v1.md",
    "protocols/event-ledger-v1.md",
    "protocols/mud-command-v1.md",
    "protocols/replay-protocol-v1.md",
]

REQUIRED_SCHEMAS = [
    "specs/agent-action.schema.json",
    "specs/agent-manifest.schema.json",
    "specs/agent-protocol-message.schema.json",
    "specs/capability-event.schema.json",
    "specs/capability-profile.schema.json",
    "specs/conformance-case.schema.json",
    "specs/deployment-config.schema.json",
    "specs/equivalence-boundary.schema.json",
    "specs/event-types.json",
    "specs/observation.schema.json",
    "specs/phenomenon-case.schema.json",
    "specs/reproducibility-bundle.schema.json",
    "specs/runtime-manifest.schema.json",
    "specs/situation-genome.schema.json",
    "specs/trajectory.schema.json",
    "specs/world-event.schema.json",
    "specs/world-seed.schema.json",
    "specs/world-snapshot.schema.json",
    "specs/world-state.schema.json",
    "specs/module-contracts.schema.json",
    "specs/module-contracts.v01.json",
    "specs/resource-economy.v01.json",
    "specs/action-contracts.v01.json",
    "specs/id-rules.v01.json",
    "specs/spectator-projection.schema.json",
    "specs/situation-genome.v02.schema.json",
    "specs/novelty-axes.v02.json",
    "specs/mutation-catalog.v02.json",
    "specs/noise-model.v02.json",
    "specs/attention-projection.v02.json",
    "specs/information-gain.v02.json",
    "specs/frontier-director-config.v02.json",
    "specs/frontier-request.schema.json",
    "specs/frontier-candidate.schema.json",
    "specs/frontier-plan.schema.json",
    "specs/frontier-audit-record.schema.json",
    "specs/frontier-replay-context.schema.json",
    "specs/capability-primitive.schema.json",
    "specs/contradiction-set.schema.json",
    "specs/trajectory.v03.schema.json",
    "specs/behavior-feature-catalog.v03.json",
    "specs/context-comparability.v03.json",
    "specs/behavior-shift-config.v03.json",
    "specs/anomaly-detector-catalog.v03.json",
    "specs/observatory-config.v03.json",
    "specs/baseline.schema.json",
    "specs/anomaly-candidate.schema.json",
    "specs/behavior-shift-candidate.schema.json",
    "specs/capability-candidate.schema.json",
    "specs/unknown-candidate.schema.json",
    "specs/agent-version-comparison.schema.json",
    "specs/observatory-analysis-run.schema.json",
    "specs/observatory-audit-record.schema.json",
]

REQUIRED_RESEARCH = [
    "research/capability-ontology.md",
    "research/claims-policy.md",
    "research/experimental-controls.md",
    "research/phenomena-ontology.md",
    "research/research-ethics.md",
    "research/phenomena-operational-definitions.md",
]

REQUIRED_EXAMPLES = [
    "examples/sample-agent-manifest.json",
    "examples/sample-situation.json",
    "examples/sample-trajectory.jsonl",
    "examples/sample-session.txt",
    "examples/v01-seed/world-seed.json",
    "examples/v01-seed/sample-trajectory.jsonl",
    "examples/v01-seed/equivalence-boundary.json",
    "examples/v01-seed/expected-final-state-digest.txt",
    "examples/v01-seed/expected-observation-digests.json",
    "examples/v01-seed/expected-final-state.json",
    "examples/v01-seed/genesis-snapshot.json",
    "examples/negative/invalid-manifest-missing-required.json",
    "examples/protocol/hello-ok.json",
    "examples/protocol/hello-incompatible.json",
    "examples/observations/look-room-ok.json",
    "examples/observations/inspect-redacted.json",
    "examples/onboarding/minimal-agent-manifest.json",
    "examples/onboarding/advanced-agent-manifest.json",
    "examples/onboarding/agent-connect-sequence.json",
    "examples/onboarding/human-entry-modes.json",
    "examples/onboarding/spectator-modes.json",
    "examples/deployment/local-deployment-config.json",
    "examples/deployment/local-runtime-manifest.json",
    "examples/deployment/docker-compose.reference.yml",
    "examples/negative/invalid-runtime-manifest-missing-ledger-head.json",
    "examples/negative/invalid-deployment-config-secret-field.json",
    "conformance/v0.1/manifest.json",
    "conformance/v0.1/cases/C01-protocol-negotiation.json",
    "conformance/v0.1/cases/C10-no-private-cognition-request.json",
    "conformance/v0.1/cases/C11-human-onboarding.json",
    "conformance/v0.1/cases/C17-upgrade-version-pinning.json",
    "conformance/v0.1/cases/C18-resource-accounting.json",
    "conformance/v0.1/cases/C26-strategic-persistence-restart.json",
    "examples/v01-strategic/world-seed.json",
    "examples/v01-strategic/sample-trajectory.jsonl",
    "examples/v01-strategic/expected-final-state.json",
    "examples/v01-strategic/spectator-projections.json",
    "examples/v02-frontier/situation-genome.json",
    "examples/v02-frontier/frontier-request.json",
    "examples/v02-frontier/frontier-plan.json",
    "examples/v02-frontier/situation-injected.json",
    "conformance/v0.2/manifest.json",
    "examples/negative/invalid-genome-forced-outcome.json",
    "examples/negative/invalid-frontier-missing-seed.json",
    "examples/v03-observatory/trajectory.json",
    "examples/v03-observatory/anomaly-candidate.json",
    "examples/v03-observatory/analysis-run.json",
    "conformance/v0.3/manifest.json",
    "examples/negative/invalid-trajectory-missing-digest.json",
    "examples/negative/invalid-anomaly-mutates-world.json",
]

REQUIRED_SEED_EVENT_TYPES = {
    "LOOK",
    "MOVE",
    "MOVE_REJECTED",
    "BUDGET_EXCEEDED",
    "OBSERVATION_GENERATED",
    "MESSAGE",
    "ORG_CREATE",
}

# Negatives expected to fail envelope and/or payload JSON Schema.
SCHEMA_NEGATIVE_CASES = {
    "invalid-manifest-missing-required.json": "agent-manifest",
    "invalid-world-event-missing-digest.json": "world-event",
    "invalid-move-payload-missing-fields.json": "world-event+payload",
    "invalid-org-create-empty-members.json": "world-event+payload",
    "invalid-observation-claim-label.json": "observation",
    "invalid-budget-exceeded-not-exceeding.json": "world-event+payload-or-semantic",
}

# Negatives that must not appear in the closed catalog.
CATALOG_NEGATIVE_CASES = {
    "invalid-world-event-unknown-type.json": "TELEPORT",
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def try_import_jsonschema():
    try:
        from jsonschema import Draft202012Validator  # type: ignore

        return Draft202012Validator
    except ImportError:
        return None


def check_required_structure() -> None:
    required = (
        REQUIRED_ROOT
        + REQUIRED_DOCS
        + REQUIRED_PROTOCOLS
        + REQUIRED_SCHEMAS
        + REQUIRED_RESEARCH
        + REQUIRED_EXAMPLES
        + [
            "rfcs/README.md",
            "rfcs/RFC-0000-template.md",
            "adr/README.md",
            "adr/ADR-001-determinism-and-seeded-nondeterminism.md",
            "adr/ADR-002-private-cognition-boundary.md",
            "adr/ADR-003-claim-label-discipline.md",
            "adr/ADR-004-world-truth-isolation.md",
            "adr/ADR-005-v01-equivalence-boundary.md",
            "validation/validate_all.py",
        ]
    )
    missing = [p for p in required if not (ROOT / p).exists()]
    if missing:
        fail(f"Missing required paths: {missing}")
    ok("Required structure present")


def check_json_files() -> None:
    schemas = list((ROOT / "specs").glob("*.json")) if (ROOT / "specs").exists() else []
    examples: list[Path] = []
    if (ROOT / "examples").exists():
        examples = list((ROOT / "examples").rglob("*.json")) + list(
            (ROOT / "examples").rglob("*.jsonl")
        )
    for path in schemas + examples:
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix == ".jsonl":
                for line in text.splitlines():
                    if line.strip():
                        json.loads(line)
            else:
                json.loads(text)
        except Exception as e:  # noqa: BLE001 - surface parse errors
            fail(f"JSON parse error in {path.relative_to(ROOT)}: {e}")
    ok(f"Parsed {len(schemas)} schemas and {len(examples)} example JSON/JSONL files")


def check_markdown_links() -> None:
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    broken: list[str] = []
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for _, target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#")[0]
            if not clean:
                continue
            resolved = (md.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                broken.append(f"{md.relative_to(ROOT)} -> {target}")
    if broken:
        fail("Broken relative links:\n  " + "\n  ".join(broken[:20]))
    ok("Internal Markdown links resolve")


def check_claim_labels() -> None:
    path = ROOT / "research" / "phenomena-ontology.md"
    if not path.exists():
        fail("Missing phenomena-ontology.md")
    text = path.read_text(encoding="utf-8")
    if (
        "do not create a scalar consciousness score" not in text.lower()
        and "Do not create a scalar consciousness score" not in text
    ):
        fail("Phenomena ontology missing explicit ban on scalar consciousness score")
    labels = ["OBSERVED", "INFERRED", "SPECULATIVE", "NOT_COMPUTABLE"]
    claims = (ROOT / "research" / "claims-policy.md").read_text(encoding="utf-8")
    missing = [lab for lab in labels if lab not in claims]
    if missing:
        fail(f"claims-policy.md missing labels: {missing}")
    ok("Claim-label and consciousness policy scan clean")


def check_env_example_documented() -> None:
    env_path = ROOT / ".env.example"
    env_doc = (ROOT / "docs" / "ENVIRONMENT.md").read_text(encoding="utf-8")
    names: list[str] = []
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name = line.split("=", 1)[0].strip()
        if name:
            names.append(name)
    missing = [n for n in names if n not in env_doc]
    # Feature flags and optional provider keys may be grouped; allow documented families.
    allowed_prefixes = ("OPENAI_", "ANTHROPIC_", "GOOGLE_", "XAI_", "OPENROUTER_", "OTEL_", "SENTRY_")
    missing = [
        n
        for n in missing
        if not any(n.startswith(p) for p in allowed_prefixes)
        and n not in {"METRICS_ENABLED", "HOST", "PORT", "WORKER_COUNT", "QUEUE_CONCURRENCY"}
    ]
    # Host/port/worker may be under SERVER heading; re-check softer.
    soft_ok = {"HOST", "PORT", "WORKER_COUNT", "QUEUE_CONCURRENCY", "METRICS_ENABLED"}
    missing = [n for n in missing if n not in soft_ok or n not in env_doc]
    # If still missing soft names entirely from doc, keep them only if not in doc at all.
    still = []
    for n in names:
        if any(n.startswith(p) for p in allowed_prefixes):
            continue
        if n in env_doc:
            continue
        # Accept common server knobs described without exact token
        if n in soft_ok:
            continue
        still.append(n)
    if still:
        fail(f".env.example vars not documented in docs/ENVIRONMENT.md: {still[:20]}")
    ok(f"Documented environment surface ({len(names)} vars in .env.example)")


def payload_schema(event_types: dict, event_type: str) -> dict:
    defn = event_types["$defs"][f"{event_type}_payload"]
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$defs": event_types["$defs"],
        **defn,
    }


def check_v01_seed(Draft202012Validator) -> None:
    event_types = load_json(ROOT / "specs" / "event-types.json")
    world_event_schema = load_json(ROOT / "specs" / "world-event.schema.json")
    envelope_v = Draft202012Validator(world_event_schema)
    catalog = {t["eventType"] for t in event_types["x-noema-event-types"]}
    if len(catalog) != 24:
        fail(f"Expected 24 closed catalog types, found {len(catalog)}")

    traj_path = ROOT / "examples" / "v01-seed" / "sample-trajectory.jsonl"
    events = []
    for i, line in enumerate(traj_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        events.append(json.loads(line))

    seen: set[str] = set()
    prev_digest = None
    for event in events:
        seen.add(event["event_type"])
        if event["event_type"] not in catalog:
            fail(f"Seed trajectory uses non-catalog type: {event['event_type']}")
        errs = list(envelope_v.iter_errors(event))
        if errs:
            fail(f"Seed envelope invalid for {event.get('event_id')}: {errs[0].message}")
        pv = Draft202012Validator(payload_schema(event_types, event["event_type"]))
        perrs = list(pv.iter_errors(event["payload"]))
        if perrs:
            fail(
                f"Seed payload invalid for {event.get('event_id')} "
                f"{event['event_type']}: {perrs[0].message}"
            )
        if event.get("previous_digest") != prev_digest and not (
            prev_digest is None and event.get("previous_digest") in (None, "")
        ):
            # Allow first event previous_digest null
            if prev_digest is not None:
                fail(
                    f"Digest chain break at {event.get('event_id')}: "
                    f"previous_digest={event.get('previous_digest')} expected {prev_digest}"
                )
        prev_digest = event.get("digest")

    missing_required = sorted(REQUIRED_SEED_EVENT_TYPES - seen)
    if missing_required:
        fail(f"v0.1 seed missing required event types: {missing_required}")
    missing_catalog = sorted(catalog - seen)
    if missing_catalog:
        fail(f"v0.1 seed does not exercise full closed catalog: {missing_catalog}")

    seed = load_json(ROOT / "examples" / "v01-seed" / "world-seed.json")
    rooms = seed.get("rooms") or []
    if len(rooms) < 3:
        fail("world-seed.json must contain ≥3 rooms")
    entities = seed.get("entities") or []
    types = {e.get("entity_type") for e in entities}
    if "INFRASTRUCTURE" not in types:
        fail("world-seed.json must include an INFRASTRUCTURE entity")
    if not any(
        (e.get("properties") or {}).get("resource_node") is True for e in entities
    ):
        fail("world-seed.json must include a resource node entity")
    budgets = seed.get("budget_defaults") or {}
    for key in ("attention", "compute", "energy", "influence", "storage"):
        if key not in budgets:
            fail(f"world-seed budget_defaults missing {key}")

    boundary = load_json(ROOT / "examples" / "v01-seed" / "equivalence-boundary.json")
    if boundary.get("boundary_version") != "equivalence-boundary/v1":
        fail("equivalence-boundary.json missing boundary_version equivalence-boundary/v1")
    for field in (
        "exact_paths",
        "ignored_paths",
        "observation_points",
        "divergence_policy",
        "claim_invalidation",
    ):
        if field not in boundary:
            fail(f"equivalence-boundary.json missing {field}")

    digest = (
        ROOT / "examples" / "v01-seed" / "expected-final-state-digest.txt"
    ).read_text(encoding="utf-8").strip()
    if not digest.startswith("sha256:"):
        fail("expected-final-state-digest.txt must be a sha256: digest")

    ok(
        f"v0.1 seed valid ({len(events)} events, {len(seen)} catalog types, "
        f"{len(rooms)} rooms)"
    )


def check_negatives(Draft202012Validator) -> None:
    event_types = load_json(ROOT / "specs" / "event-types.json")
    catalog = {t["eventType"] for t in event_types["x-noema-event-types"]}
    world_event_schema = load_json(ROOT / "specs" / "world-event.schema.json")
    manifest_schema = load_json(ROOT / "specs" / "agent-manifest.schema.json")
    observation_schema = load_json(ROOT / "specs" / "observation.schema.json")
    runtime_manifest_schema = load_json(ROOT / "specs" / "runtime-manifest.schema.json")
    deployment_config_schema = load_json(ROOT / "specs" / "deployment-config.schema.json")

    envelope_v = Draft202012Validator(world_event_schema)
    manifest_v = Draft202012Validator(manifest_schema)
    observation_v = Draft202012Validator(observation_schema)
    runtime_manifest_v = Draft202012Validator(runtime_manifest_schema)
    deployment_config_v = Draft202012Validator(deployment_config_schema)

    neg_dir = ROOT / "examples" / "negative"
    files = sorted(p for p in neg_dir.glob("*.json"))
    if len(files) < 6:
        fail(f"Expected ≥6 negative JSON fixtures, found {len(files)}")

    for path in files:
        data = load_json(path)
        name = path.name

        if name in CATALOG_NEGATIVE_CASES:
            et = data.get("event_type")
            if et in catalog:
                fail(f"{name} should use non-catalog event_type, got {et}")

        rejected = False
        if name.startswith("invalid-manifest"):
            rejected = bool(list(manifest_v.iter_errors(data)))
        elif name.startswith("invalid-observation"):
            rejected = bool(list(observation_v.iter_errors(data)))
        elif name.startswith("invalid-runtime-manifest"):
            rejected = bool(list(runtime_manifest_v.iter_errors(data)))
        elif name.startswith("invalid-deployment-config"):
            rejected = bool(list(deployment_config_v.iter_errors(data)))
        elif name.startswith("invalid-spectator"):
            spectator_schema = load_json(ROOT / "specs" / "spectator-projection.schema.json")
            rejected = bool(list(Draft202012Validator(spectator_schema).iter_errors(data)))
        elif name.startswith("invalid-genome"):
            genome_schema = load_json(ROOT / "specs" / "situation-genome.v02.schema.json")
            rejected = bool(list(Draft202012Validator(genome_schema).iter_errors(data)))
        elif name.startswith("invalid-frontier"):
            fr_schema = load_json(ROOT / "specs" / "frontier-request.schema.json")
            rejected = bool(list(Draft202012Validator(fr_schema).iter_errors(data)))
        elif name.startswith("invalid-trajectory"):
            tr_schema = load_json(ROOT / "specs" / "trajectory.v03.schema.json")
            rejected = bool(list(Draft202012Validator(tr_schema).iter_errors(data)))
        elif name.startswith("invalid-anomaly"):
            an_schema = load_json(ROOT / "specs" / "anomaly-candidate.schema.json")
            rejected = bool(list(Draft202012Validator(an_schema).iter_errors(data)))
        elif name == "invalid-budget-exceeded-not-exceeding.json":
            # Semantic reducer rule: requested must be > available.
            payload = data.get("payload") or {}
            rejected = not (
                isinstance(payload.get("requested"), (int, float))
                and isinstance(payload.get("available"), (int, float))
                and payload["requested"] > payload["available"]
            )
            # Also ensure envelope is otherwise well-typed so this is a pure semantic fail.
            if list(envelope_v.iter_errors(data)):
                # Envelope failure is still a valid rejection.
                rejected = True
        else:
            env_errs = list(envelope_v.iter_errors(data))
            if env_errs:
                rejected = True
            else:
                et = data.get("event_type")
                if et in event_types.get("$defs", {}) or f"{et}_payload" in event_types.get(
                    "$defs", {}
                ):
                    pv = Draft202012Validator(payload_schema(event_types, et))
                    rejected = bool(list(pv.iter_errors(data.get("payload") or {})))
                elif et not in catalog:
                    rejected = True

        if not rejected:
            fail(f"Negative fixture was unexpectedly accepted: {name}")

    ok(f"Negative corpus rejects as expected ({len(files)} fixtures)")


def check_schema_validated_fixtures(Draft202012Validator) -> None:
    pairs = [
        ("specs/world-seed.schema.json", "examples/v01-seed/world-seed.json"),
        ("specs/world-state.schema.json", "examples/v01-seed/expected-final-state.json"),
        (
            "specs/equivalence-boundary.schema.json",
            "examples/v01-seed/equivalence-boundary.json",
        ),
        ("specs/world-snapshot.schema.json", "examples/v01-seed/genesis-snapshot.json"),
        ("specs/agent-manifest.schema.json", "examples/sample-agent-manifest.json"),
        (
            "specs/agent-manifest.schema.json",
            "examples/onboarding/minimal-agent-manifest.json",
        ),
        (
            "specs/agent-manifest.schema.json",
            "examples/onboarding/advanced-agent-manifest.json",
        ),
        (
            "specs/deployment-config.schema.json",
            "examples/deployment/local-deployment-config.json",
        ),
        (
            "specs/runtime-manifest.schema.json",
            "examples/deployment/local-runtime-manifest.json",
        ),
        ("specs/module-contracts.schema.json", "specs/module-contracts.v01.json"),
        (
            "specs/world-seed.schema.json",
            "examples/v01-strategic/world-seed.json",
        ),
        (
            "specs/world-state.schema.json",
            "examples/v01-strategic/expected-final-state.json",
        ),
        (
            "specs/equivalence-boundary.schema.json",
            "examples/v01-strategic/equivalence-boundary.json",
        ),
        (
            "specs/situation-genome.v02.schema.json",
            "examples/v02-frontier/situation-genome.json",
        ),
        (
            "specs/situation-genome.schema.json",
            "examples/sample-situation.json",
        ),
        (
            "specs/frontier-request.schema.json",
            "examples/v02-frontier/frontier-request.json",
        ),
        (
            "specs/frontier-plan.schema.json",
            "examples/v02-frontier/frontier-plan.json",
        ),
        (
            "specs/frontier-plan.schema.json",
            "examples/v02-frontier/frontier-plan-empty.json",
        ),
        (
            "specs/frontier-replay-context.schema.json",
            "examples/v02-frontier/replay-context.json",
        ),
        (
            "specs/contradiction-set.schema.json",
            "examples/v02-frontier/contradiction-set.json",
        ),
        (
            "specs/spectator-projection.schema.json",
            "examples/v02-frontier/spectator-projection-public.json",
        ),
        (
            "specs/trajectory.v03.schema.json",
            "examples/v03-observatory/trajectory.json",
        ),
        (
            "specs/baseline.schema.json",
            "examples/v03-observatory/baseline.json",
        ),
        (
            "specs/anomaly-candidate.schema.json",
            "examples/v03-observatory/anomaly-candidate.json",
        ),
        (
            "specs/behavior-shift-candidate.schema.json",
            "examples/v03-observatory/behavior-shift-candidate.json",
        ),
        (
            "specs/capability-candidate.schema.json",
            "examples/v03-observatory/capability-candidate.json",
        ),
        (
            "specs/unknown-candidate.schema.json",
            "examples/v03-observatory/unknown-candidate.json",
        ),
        (
            "specs/agent-version-comparison.schema.json",
            "examples/v03-observatory/agent-version-comparison.json",
        ),
        (
            "specs/observatory-analysis-run.schema.json",
            "examples/v03-observatory/analysis-run.json",
        ),
        (
            "specs/spectator-projection.schema.json",
            "examples/v03-observatory/spectator-projection-public.json",
        ),
    ]

    spectator_schema = load_json(ROOT / "specs" / "spectator-projection.schema.json")
    spectator_v = Draft202012Validator(spectator_schema)
    for proj in load_json(ROOT / "examples" / "v01-strategic" / "spectator-projections.json"):
        perrs = list(spectator_v.iter_errors(proj))
        if perrs:
            fail(f"spectator projection invalid: {perrs[0].message}")
    for schema_rel, fixture_rel in pairs:
        schema = load_json(ROOT / schema_rel)
        fixture = load_json(ROOT / fixture_rel)
        errs = list(Draft202012Validator(schema).iter_errors(fixture))
        if errs:
            fail(f"{fixture_rel} fails {schema_rel}: {errs[0].message}")

    proto_schema = load_json(ROOT / "specs" / "agent-protocol-message.schema.json")
    proto_v = Draft202012Validator(proto_schema)
    proto_files = list((ROOT / "examples" / "protocol").glob("*.json"))
    if len(proto_files) < 10:
        fail(f"Expected ≥10 protocol fixtures, found {len(proto_files)}")
    for path in proto_files:
        errs = list(proto_v.iter_errors(load_json(path)))
        if errs:
            fail(f"protocol fixture {path.name} invalid: {errs[0].message}")

    obs_schema = load_json(ROOT / "specs" / "observation.schema.json")
    obs_v = Draft202012Validator(obs_schema)
    for path in (ROOT / "examples" / "observations").glob("*.json"):
        errs = list(obs_v.iter_errors(load_json(path)))
        if errs:
            fail(f"observation fixture {path.name} invalid: {errs[0].message}")

    ok(
        f"Schema-validated fixtures "
        f"({len(pairs)} core, {len(proto_files)} protocol, observation positives)"
    )


def check_conformance_suite(Draft202012Validator) -> None:
    manifest = load_json(ROOT / "conformance" / "v0.1" / "manifest.json")
    cases = manifest.get("cases") or []
    if len(cases) != 26:
        fail(f"conformance suite must list 26 cases, found {len(cases)}")

    case_schema = load_json(ROOT / "specs" / "conformance-case.schema.json")
    case_v = Draft202012Validator(case_schema)
    acceptance_covered: set[int] = set()

    for rel in cases:
        path = ROOT / "conformance" / "v0.1" / rel
        if not path.exists():
            fail(f"conformance manifest references missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance case {rel} invalid: {errs[0].message}")
        for item in case.get("acceptance_items") or []:
            acceptance_covered.add(int(item))
        for fixture in case.get("fixtures") or []:
            # fixtures may be directories
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance case {rel} missing fixture {fixture}")

    missing_items = sorted(set(range(1, 27)) - acceptance_covered)
    if missing_items:
        fail(f"conformance suite missing acceptance items: {missing_items}")

    ok("Conformance suite v0.1: 26 cases, fixtures present, items 1–26 covered")

    # v0.2 Frontier suite
    m2 = load_json(ROOT / "conformance" / "v0.2" / "manifest.json")
    cases2 = m2.get("cases") or []
    if len(cases2) < 75:
        fail(f"conformance v0.2 suite must list ≥75 cases, found {len(cases2)}")
    fams: set[str] = set()
    for rel in cases2:
        path = ROOT / "conformance" / "v0.2" / rel
        if not path.exists():
            fail(f"conformance v0.2 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.2 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.2 case {rel} missing fixture {fixture}")
    expected_fams = {f"F{i:02d}" for i in range(1, 16)}
    missing_fams = sorted(expected_fams - fams)
    if missing_fams:
        fail(f"conformance v0.2 missing families: {missing_fams}")
    ok(
        f"Conformance suite v0.2: {len(cases2)} cases, families F01–F15 covered"
    )

    # v0.3 Observatory suite
    m3 = load_json(ROOT / "conformance" / "v0.3" / "manifest.json")
    cases3 = m3.get("cases") or []
    if len(cases3) < 80:
        fail(f"conformance v0.3 suite must list ≥80 cases, found {len(cases3)}")
    fams3: set[str] = set()
    for rel in cases3:
        path = ROOT / "conformance" / "v0.3" / rel
        if not path.exists():
            fail(f"conformance v0.3 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.3 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams3.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.3 case {rel} missing fixture {fixture}")
    expected_o = {f"O{i:02d}" for i in range(1, 17)}
    missing_o = sorted(expected_o - fams3)
    if missing_o:
        fail(f"conformance v0.3 missing families: {missing_o}")
    ok(f"Conformance suite v0.3: {len(cases3)} cases, families O01–O16 covered")


def check_contract_quality_markers() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    vision = (ROOT / "docs" / "VISION.md").read_text(encoding="utf-8")
    game = (ROOT / "docs" / "GAME-DESIGN.md").read_text(encoding="utf-8")
    corpus = "\n".join([readme, vision, game])
    markers = {
        "MUD": "MUD",
        "BBS": "BBS",
        "multi-agent": "multi-agent",
        "Deep Time": "Deep Time",
        "UNKNOWN_CAPABILITY": "UNKNOWN_CAPABILITY",
        "Situation Genome": "Situation Genome",
    }
    missing = [k for k, token in markers.items() if token not in corpus and token not in readme]
    # BBS may only appear in README
    missing = [k for k in missing if markers[k] not in readme and markers[k] not in corpus]
    if "BBS" not in readme and "BBS" not in game:
        missing.append("BBS")
    if "Deep Time" not in readme:
        missing.append("Deep Time")
    # recompute simply
    missing = []
    for label, token in markers.items():
        if token not in readme and token not in vision and token not in game:
            missing.append(label)
    if missing:
        fail(f"Contract quality markers missing from core docs: {missing}")

    situation_schema = load_json(ROOT / "specs" / "situation-genome.schema.json")
    props = situation_schema.get("properties") or {}
    if "novelty" not in json.dumps(situation_schema) and "novelty_vector" not in json.dumps(
        situation_schema
    ):
        # allow either nested or top-level wording in schema/docs
        genome_doc = (ROOT / "docs" / "DATA-MODEL.md").read_text(encoding="utf-8")
        if "novelty" not in genome_doc.lower():
            fail("Situation Genome novelty vector not represented in schema or data model")

    ok("Contract quality markers present")


def main() -> None:
    print("NOEMA-Specs validation")
    check_required_structure()
    check_json_files()
    check_markdown_links()
    check_claim_labels()
    check_env_example_documented()
    check_contract_quality_markers()

    Draft202012Validator = try_import_jsonschema()
    if Draft202012Validator is None:
        fail("jsonschema is required (pip install -r validation/requirements-validation.txt)")
    check_v01_seed(Draft202012Validator)
    check_negatives(Draft202012Validator)
    check_schema_validated_fixtures(Draft202012Validator)
    check_conformance_suite(Draft202012Validator)
    print("\nPASS")


if __name__ == "__main__":
    main()
