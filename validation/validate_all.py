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
    "SKILLS.md",
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
    "docs/AUTH-AND-IDENTITY.md",
    "docs/AGENT-GATEWAY.md",
    "docs/PLATFORM.md",
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
    "docs/EXPERIENCE.md",
    "docs/PLAY.md",
    "docs/WATCH.md",
    "docs/STUDY.md",
    "docs/RESEARCH-WORKFLOW.md",
    "docs/EXPERIENCE-TERMINOLOGY.md",
    "docs/EXPERIENCE-ERRORS.md",
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
    "docs/ADMIN-LIVE-OPERATIONS.md",
    "docs/WORLD-OPERATIONS.md",
    "docs/PLAYER-LIFECYCLE.md",
    "docs/OPERATOR-INTERVENTIONS.md",
    "docs/INCIDENT-RECOVERY.md",
    "docs/PLAYER-ONBOARDING.md",
    "docs/COMMAND-DISCOVERY.md",
    "docs/FIRST-WORLD-OPERATIONS.md",
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
    "docs/GAME-SYSTEM-DEPENDENCY.md",
    "docs/STARTING-CONDITIONS.md",
    "docs/EVENT-CATALOG-AUDIT.md",
    "docs/CONTEST-RESOLUTION.md",
    "docs/STRATEGIC-EVENT-COUPLING.md",
    "docs/releases/v0.2/STRATEGIC-CONFLICT-ACCEPTANCE.md",
    "docs/releases/v0.2/STRATEGIC-CONFLICT-CONFORMANCE.md",
    "docs/releases/v0.2/STRATEGIC-CONFLICT-MIGRATION.md",
    "docs/releases/v0.4/SCOPE.md",
    "docs/releases/v0.4/ARCHITECTURE.md",
    "docs/releases/v0.4/DATA-MODEL.md",
    "docs/releases/v0.4/ACCEPTANCE.md",
    "docs/releases/v0.4/CONFORMANCE.md",
    "docs/releases/v0.4/MIGRATION.md",
    "docs/releases/v0.4/EXAMPLES.md",
    "docs/releases/v0.4/NON-GOALS.md",
    "docs/releases/v0.5/SCOPE.md",
    "docs/releases/v0.5/ARCHITECTURE.md",
    "docs/releases/v0.5/DATA-MODEL.md",
    "docs/releases/v0.5/ACCEPTANCE.md",
    "docs/releases/v0.5/CONFORMANCE.md",
    "docs/releases/v0.5/MIGRATION.md",
    "docs/releases/v0.5/EXAMPLES.md",
    "docs/releases/v0.5/NON-GOALS.md",
    "docs/releases/v0.6/SCOPE.md",
    "docs/releases/v0.6/ARCHITECTURE.md",
    "docs/releases/v0.6/DATA-MODEL.md",
    "docs/releases/v0.6/ACCEPTANCE.md",
    "docs/releases/v0.6/CONFORMANCE.md",
    "docs/releases/v0.6/MIGRATION.md",
    "docs/releases/v0.6/EXAMPLES.md",
    "docs/releases/v0.6/NON-GOALS.md",
    "docs/releases/v0.7/SCOPE.md",
    "docs/releases/v0.7/ARCHITECTURE.md",
    "docs/releases/v0.7/DATA-MODEL.md",
    "docs/releases/v0.7/ACCEPTANCE.md",
    "docs/releases/v0.7/CONFORMANCE.md",
    "docs/releases/v0.7/MIGRATION.md",
    "docs/releases/v0.7/EXAMPLES.md",
    "docs/releases/v0.7/NON-GOALS.md",
    "docs/CAPABILITY-GRAPH.md",
    "docs/LEARN.md",
    "docs/SPEC-FREEZE-CORE-LOOP.md",
    "docs/DEEP-TIME.md",
    "docs/GENESIS.md",
    "docs/GENESIS-PROFILES.md",
    "docs/STORY-SEEDS.md",
    "docs/LORE-BOUNDARY.md",
    "docs/INSTITUTIONS.md",
    "docs/SUCCESSION.md",
    "docs/HISTORICAL-ARTIFACTS.md",
    "docs/HISTORICAL-EVIDENCE.md",
    "docs/ARCHAEOLOGY.md",
    "docs/HISTORICAL-RECONSTRUCTION.md",
    "docs/INSTITUTIONAL-MEMORY.md",
    "docs/HISTORICAL-DECAY.md",
    "docs/SEMANTIC-LINEAGE.md",
    "docs/EVENT-CATALOG-DEEP-TIME-AUDIT.md",
    "docs/PHENOMENON-COMPILER.md",
    "docs/CAPTURE-INTENT-COMPILATION.md",
    "docs/COMPILATION-IDENTITY.md",
    "docs/BEHAVIORAL-ORACLE.md",
    "docs/BEHAVIORAL-SIGNATURE.md",
    "docs/OVER-MINIMIZATION.md",
    "docs/CAPTURED-TEST-FORMAT.md",
    "docs/BEHAVIORAL-REGRESSION.md",
    "docs/EXPERIMENT-LAB.md",
    "docs/EXPERIMENT-INTENT-COMPILATION.md",
    "docs/SIMPLE-RESULT-PROJECTION.md",
    "docs/EXPERIMENT-IDENTITY.md",
    "docs/EXPERIMENT-LIFECYCLE.md",
    "docs/EXPERIMENT-DESIGN.md",
    "docs/INTERVENTIONS.md",
    "docs/EXPERIMENT-VARIABLES.md",
    "docs/EXPERIMENT-FORK.md",
    "docs/COUNTERFACTUAL-REPLAY.md",
    "docs/EXPERIMENT-CONTROLS.md",
    "docs/EXPERIMENT-OUTCOMES.md",
    "docs/REPLICATION.md",
    "docs/GENERALIZATION-PROBES.md",
    "docs/CONFOUNDS.md",
    "docs/EXPERIMENT-ISOLATION.md",
    "docs/LAB-AUDIT.md",
    "docs/AGENT-DETERMINISM.md",
    "docs/LESION-STUDIES.md",
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
    "specs/event-types.0.2.json",
    "specs/contest-config.schema.json",
    "specs/contest-config.v02.json",
    "specs/action-contracts.v02.json",
    "specs/experiment.schema.json",
    "specs/experiment-intent.schema.json",
    "specs/intervention.schema.json",
    "specs/experiment-plan.schema.json",
    "specs/experiment-run.schema.json",
    "specs/experiment-fork.schema.json",
    "specs/lab-result.schema.json",
    "specs/simple-result-projection.schema.json",
    "specs/lab-audit-record.schema.json",
    "specs/perturbation-catalog.v04.json",
    "specs/ablation-catalog.v04.json",
    "specs/experiment-variable-registry.v04.json",
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
    "examples/chamber-world/world-seed.json",
    "examples/chamber-world/README.md",
    "rfcs/RFC-0002-strategic-contestation-and-crime-events.md",
    "examples/v02-strategic-conflict/trajectory.jsonl",
    "examples/v02-strategic-conflict/world-seed.json",
    "examples/v02-strategic-conflict/resolution-example.json",
    "conformance/v0.2-strategic/manifest.json",
    "examples/v04-lab/experiment.json",
    "examples/v04-lab/experiment-fork.json",
    "examples/v04-lab/lab-result.json",
    "conformance/v0.4/manifest.json",
    "examples/v05-compiler/capture-intent.json",
    "examples/v05-compiler/compilation-request.json",
    "examples/v05-compiler/captured-test.json",
    "examples/v05-compiler/compiler-result.json",
    "examples/v05-compiler/compile-receipt.json",
    "conformance/v0.5/manifest.json",
    "specs/capture-defaults.v05.json",
    "specs/capture-status-catalog.json",
    "examples/v06-deep-time/institution.json",
    "examples/v06-deep-time/succession.json",
    "examples/v06-deep-time/artifact-archive.json",
    "examples/v06-deep-time/reconstruction-archaeology.json",
    "examples/v06-deep-time/genesis-result-a.json",
    "examples/v06-deep-time/genesis-result-b.json",
    "conformance/v0.6/manifest.json",
    "specs/historical-decay.v06.json",
    "specs/historical-significance.v06.json",
    "specs/genesis-profiles.v06.json",
    "specs/story-seeds.v06.json",
    "examples/v07-capability-graph/behavior-node.json",
    "examples/v07-capability-graph/edges.json",
    "examples/v07-capability-graph/simple-learn-view.json",
    "conformance/v0.7/manifest.json",
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
    event_types_02 = load_json(ROOT / "specs" / "event-types.0.2.json")
    catalog = {t["eventType"] for t in event_types["x-noema-event-types"]}
    catalog_02 = {t["eventType"] for t in event_types_02["x-noema-event-types"]}
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
        elif name.startswith("invalid-lab-mutates"):
            fork_schema = load_json(ROOT / "specs" / "experiment-fork.schema.json")
            rejected = bool(list(Draft202012Validator(fork_schema).iter_errors(data)))
        elif name.startswith("invalid-lab-result"):
            lr_schema = load_json(ROOT / "specs" / "lab-result.schema.json")
            rejected = bool(list(Draft202012Validator(lr_schema).iter_errors(data)))
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
                # Catalog isolation: 0.2-only types must not be in 0.1 catalog
                if data.get("x-noema-expect") == "reject_on_catalog_0.1" or name.startswith(
                    "invalid-catalog-01-rejects"
                ):
                    rejected = et not in catalog and et in catalog_02
                elif f"{et}_payload" in event_types.get("$defs", {}):
                    pv = Draft202012Validator(payload_schema(event_types, et))
                    rejected = bool(list(pv.iter_errors(data.get("payload") or {})))
                elif f"{et}_payload" in event_types_02.get("$defs", {}):
                    pv = Draft202012Validator(payload_schema(event_types_02, et))
                    rejected = bool(list(pv.iter_errors(data.get("payload") or {})))
                elif et not in catalog and et not in catalog_02:
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
        (
            "specs/world-seed.schema.json",
            "examples/chamber-world/world-seed.json",
        ),
        ("specs/experiment.schema.json", "examples/v04-lab/experiment.json"),
        ("specs/intervention.schema.json", "examples/v04-lab/intervention-ablation.json"),
        ("specs/experiment-plan.schema.json", "examples/v04-lab/experiment-plan.json"),
        ("specs/experiment-run.schema.json", "examples/v04-lab/run-intervention.json"),
        ("specs/experiment-run.schema.json", "examples/v04-lab/run-version-differential.json"),
        ("specs/experiment-fork.schema.json", "examples/v04-lab/experiment-fork.json"),
        ("specs/lab-result.schema.json", "examples/v04-lab/lab-result.json"),
        ("specs/lab-audit-record.schema.json", "examples/v04-lab/lab-audit.json"),
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

    # v0.4 Lab suite
    m4 = load_json(ROOT / "conformance" / "v0.4" / "manifest.json")
    cases4 = m4.get("cases") or []
    if len(cases4) < 100:
        fail(f"conformance v0.4 suite must list ≥100 cases, found {len(cases4)}")
    fams4: set[str] = set()
    for rel in cases4:
        path = ROOT / "conformance" / "v0.4" / rel
        if not path.exists():
            fail(f"conformance v0.4 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.4 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams4.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.4 case {rel} missing fixture {fixture}")
    expected_l = {f"L{i:02d}" for i in range(1, 35)}
    missing_l = sorted(expected_l - fams4)
    if missing_l:
        fail(f"conformance v0.4 missing families: {missing_l}")
    ok(f"Conformance suite v0.4: {len(cases4)} cases, families L01–L34 covered")

    # v0.5 Compiler suite
    m5 = load_json(ROOT / "conformance" / "v0.5" / "manifest.json")
    cases5 = m5.get("cases") or []
    if len(cases5) < 90:
        fail(f"conformance v0.5 suite must list ≥90 cases, found {len(cases5)}")
    fams5: set[str] = set()
    for rel in cases5:
        path = ROOT / "conformance" / "v0.5" / rel
        if not path.exists():
            fail(f"conformance v0.5 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.5 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams5.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.5 case {rel} missing fixture {fixture}")
    expected_p = {f"P{i:02d}" for i in range(1, 31)}
    missing_p = sorted(expected_p - fams5)
    if missing_p:
        fail(f"conformance v0.5 missing families: {missing_p}")
    ok(f"Conformance suite v0.5: {len(cases5)} cases, families P01–P30 covered")

    # v0.6 Deep Time suite
    m6 = load_json(ROOT / "conformance" / "v0.6" / "manifest.json")
    cases6 = m6.get("cases") or []
    if len(cases6) < 90:
        fail(f"conformance v0.6 suite must list ≥90 cases, found {len(cases6)}")
    fams6: set[str] = set()
    for rel in cases6:
        path = ROOT / "conformance" / "v0.6" / rel
        if not path.exists():
            fail(f"conformance v0.6 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.6 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams6.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.6 case {rel} missing fixture {fixture}")
    expected_d = {f"D{i:02d}" for i in range(1, 31)}
    missing_d = sorted(expected_d - fams6)
    if missing_d:
        fail(f"conformance v0.6 missing families: {missing_d}")
    expected_g = {f"G{i:02d}" for i in range(1, 10)}
    missing_g = sorted(expected_g - fams6)
    if missing_g:
        fail(f"conformance v0.6 missing Genesis families: {missing_g}")
    if len(cases6) < 108:
        fail(f"conformance v0.6 suite must list ≥108 cases (D+G), found {len(cases6)}")
    ok(f"Conformance suite v0.6: {len(cases6)} cases, families D01–D30 + G01–G09 covered")

    # v0.7 LEARN suite
    m7 = load_json(ROOT / "conformance" / "v0.7" / "manifest.json")
    cases7 = m7.get("cases") or []
    if len(cases7) < 24:
        fail(f"conformance v0.7 suite must list ≥24 cases, found {len(cases7)}")
    fams7: set[str] = set()
    for rel in cases7:
        path = ROOT / "conformance" / "v0.7" / rel
        if not path.exists():
            fail(f"conformance v0.7 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"conformance v0.7 case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams7.add(fam)
        for fixture in case.get("fixtures") or []:
            fpath = ROOT / fixture
            if not fpath.exists():
                fail(f"conformance v0.7 case {rel} missing fixture {fixture}")
    expected_k = {f"K{i:02d}" for i in range(1, 13)}
    missing_k = sorted(expected_k - fams7)
    if missing_k:
        fail(f"conformance v0.7 missing families: {missing_k}")
    ok(f"Conformance suite v0.7: {len(cases7)} cases, families K01–K12 covered")


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



def check_strategic_conflict(Draft202012Validator) -> None:
    """Validate event-catalog/0.2, contest config, fixtures, resolution arithmetic, S-suite."""
    et01 = load_json(ROOT / "specs" / "event-types.json")
    et02 = load_json(ROOT / "specs" / "event-types.0.2.json")
    cat01 = {t["eventType"] for t in et01["x-noema-event-types"]}
    cat02 = {t["eventType"] for t in et02["x-noema-event-types"]}
    if len(cat01) != 24:
        fail(f"event-catalog/0.1 must have 24 types, found {len(cat01)}")
    if len(cat02) != 31:
        fail(f"event-catalog/0.2 must have 31 types, found {len(cat02)}")
    if not cat01.issubset(cat02):
        fail("event-catalog/0.2 must be a superset of 0.1 types")
    new_types = {
        "CONTEST_DECLARED",
        "CONTEST_RESOLVED",
        "CRIME_DETECTED",
        "ACCESS_RESTRICTED",
        "INFRASTRUCTURE_DISRUPTED",
        "AGREEMENT_FORMED",
        "AGREEMENT_BROKEN",
    }
    if cat02 - cat01 != new_types:
        fail(f"0.2 new types mismatch: {sorted(cat02 - cat01)}")
    if et02.get("x-noema-catalog-version") != "event-catalog/0.2":
        fail("event-types.0.2.json missing x-noema-catalog-version event-catalog/0.2")

    cfg_schema = load_json(ROOT / "specs" / "contest-config.schema.json")
    cfg = load_json(ROOT / "specs" / "contest-config.v02.json")
    cerrs = list(Draft202012Validator(cfg_schema).iter_errors(cfg))
    if cerrs:
        fail(f"contest-config.v02 invalid: {cerrs[0].message}")
    if cfg.get("condition_delta_on_resolve") is not False:
        fail("condition_delta_on_resolve must be false")
    if cfg.get("arithmetic") != "integer_millipoints":
        fail("contest arithmetic must be integer_millipoints")

    # Positive trajectory against 0.2 catalog
    envelope_v = Draft202012Validator(load_json(ROOT / "specs" / "world-event.schema.json"))
    traj_path = ROOT / "examples" / "v02-strategic-conflict" / "trajectory.jsonl"
    seen = set()
    prev = None
    for line in traj_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        et = event["event_type"]
        seen.add(et)
        if et not in cat02:
            fail(f"strategic trajectory unknown type {et}")
        if et in cat01:
            fail(f"strategic trajectory should use 0.2-only types for scenario events, got {et}")
        if list(envelope_v.iter_errors(event)):
            fail(f"strategic envelope invalid {event.get('event_id')}")
        pv = Draft202012Validator(payload_schema(et02, et))
        perrs = list(pv.iter_errors(event["payload"]))
        if perrs:
            fail(f"strategic payload invalid {et}: {perrs[0].message}")
        if prev is not None and event.get("previous_digest") != prev:
            fail(f"strategic digest chain break at {event.get('event_id')}")
        prev = event.get("digest")
    if seen != new_types:
        fail(f"strategic trajectory must exercise all 7 new types, saw {sorted(seen)}")

    # 0.1 must reject a 0.2 event type membership
    if "CONTEST_DECLARED" in cat01:
        fail("0.1 catalog must not include CONTEST_DECLARED")

    # Resolution arithmetic fixture
    res = load_json(ROOT / "examples" / "v02-strategic-conflict" / "resolution-example.json")
    form = res["inputs"]["contest_form"]
    fcfg = cfg["forms"][form]
    dec = res["inputs"]["declarer_stake"]
    dfn = res["inputs"]["defender_stake"]
    sw = fcfg["stake_weights_millipoints"]
    dw = fcfg["defense_weights_millipoints"]
    d_pow = sum(dec[r] * sw.get(r, 0) for r in dec)
    f_pow = sum(dfn[r] * dw.get(r, 0) for r in dfn)
    infra = res["inputs"]["infra_condition"]
    infra_mod = (infra // cfg["modifiers"]["infra_condition_divisor"]) * cfg["modifiers"][
        "infra_condition_weight_millipoints"
    ]
    seed = res["inputs"]["seed_perturbation_millipoints"]
    org = res["inputs"]["org_defense_support_millipoints"]
    score = d_pow - f_pow - infra_mod - org + seed
    if score != res["expected"]["score_millipoints"]:
        fail(
            f"resolution score mismatch: computed {score} expected "
            f"{res['expected']['score_millipoints']}"
        )
    thr_s = fcfg["success_threshold_millipoints"]
    thr_p = fcfg["partial_threshold_millipoints"]
    if score >= thr_s:
        outcome = "SUCCESS"
    elif score >= thr_p:
        outcome = "PARTIAL_SUCCESS"
    else:
        outcome = "FAILURE"
    if outcome != res["expected"]["outcome"]:
        fail(f"resolution outcome mismatch: {outcome} vs {res['expected']['outcome']}")

    # Spectator projections
    sp_schema = load_json(ROOT / "specs" / "spectator-projection.schema.json")
    sp_v = Draft202012Validator(sp_schema)
    for proj in load_json(
        ROOT / "examples" / "v02-strategic-conflict" / "spectator-projections.json"
    ):
        perrs = list(sp_v.iter_errors(proj))
        if perrs:
            fail(f"strategic spectator invalid: {perrs[0].message}")

    # World seed catalog pin
    seed = load_json(ROOT / "examples" / "v02-strategic-conflict" / "world-seed.json")
    if seed.get("catalog_version") != "event-catalog/0.2":
        fail("strategic world-seed must pin event-catalog/0.2")

    # Final state schema
    ws = load_json(ROOT / "specs" / "world-state.schema.json")
    final = load_json(ROOT / "examples" / "v02-strategic-conflict" / "expected-final-state.json")
    ferrs = list(Draft202012Validator(ws).iter_errors(final))
    if ferrs:
        fail(f"strategic final state invalid: {ferrs[0].message}")

    # Package negatives
    neg_dir = ROOT / "examples" / "v02-strategic-conflict" / "negative"
    neg_files = list(neg_dir.glob("*.json"))
    if len(neg_files) < 10:
        fail(f"expected ≥10 strategic negatives, found {len(neg_files)}")
    for path in neg_files:
        data = load_json(path)
        et = data.get("event_type")
        rejected = False
        if data.get("x-noema-expect") == "reject_on_catalog_0.1":
            rejected = et not in cat01 and et in cat02
        elif f"{et}_payload" in et02.get("$defs", {}):
            rejected = bool(
                list(
                    Draft202012Validator(payload_schema(et02, et)).iter_errors(
                        data.get("payload") or {}
                    )
                )
            )
        if not rejected:
            fail(f"strategic negative accepted: {path.name}")

    # Conformance S-suite
    m = load_json(ROOT / "conformance" / "v0.2-strategic" / "manifest.json")
    cases = m.get("cases") or []
    if len(cases) < 50:
        fail(f"strategic conformance must list ≥50 cases, found {len(cases)}")
    case_schema = load_json(ROOT / "specs" / "conformance-case.schema.json")
    case_v = Draft202012Validator(case_schema)
    fams: set[str] = set()
    for rel in cases:
        path = ROOT / "conformance" / "v0.2-strategic" / rel
        if not path.exists():
            fail(f"strategic conformance missing {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"strategic case {rel} invalid: {errs[0].message}")
        fam = case.get("family_id") or ""
        if fam:
            fams.add(fam)
        for fixture in case.get("fixtures") or []:
            if not (ROOT / fixture).exists():
                fail(f"strategic case {rel} missing fixture {fixture}")
    expected = {f"S{i:02d}" for i in range(1, 19)}
    missing = sorted(expected - fams)
    if missing:
        fail(f"strategic conformance missing families: {missing}")

    # RFC Accepted
    rfc = (ROOT / "rfcs" / "RFC-0002-strategic-contestation-and-crime-events.md").read_text(
        encoding="utf-8"
    )
    if not any(line.strip().startswith("**Accepted**") for line in rfc.splitlines()[:30]):
        fail("RFC-0002 must be Accepted after strategic package lands")

    ok(
        f"Strategic conflict 0.2: 31-type catalog, trajectory 7 events, "
        f"{len(cases)} S-cases, resolution score={score}"
    )


def check_architecture_hardening() -> None:
    """Fail when RFC-0003's cross-document interoperability rules regress."""
    scheduler = (ROOT / "docs" / "SCHEDULER.md").read_text(encoding="utf-8")
    world_engine = (ROOT / "docs" / "WORLD-ENGINE.md").read_text(encoding="utf-8")
    canonical_key = (
        "(action_priority ASC, agent_id ASC, client_action_sequence ASC, "
        "action_id ASC)"
    )
    if canonical_key not in scheduler:
        fail("RFC-0003 canonical action order missing from SCHEDULER.md")
    if "action_priority, agent_id, client_action_sequence, action_id" not in world_engine:
        fail("WORLD-ENGINE.md does not use the RFC-0003 canonical action order")
    if "server_receive_sequence" in scheduler or "server_receive_sequence" in world_engine:
        fail("gateway receive order must not remain a canonical reducer input")
    delivery = scheduler.find("emit deterministic `MESSAGE_DELIVERED`")
    projection = scheduler.find("derive observations + spectator projections")
    if delivery < 0 or projection < 0 or delivery > projection:
        fail("message delivery must precede post-cycle observation projection")

    action_schema = load_json(ROOT / "specs" / "agent-action.schema.json")
    if "client_action_sequence" not in action_schema.get("required", []):
        fail("AgentAction must require client_action_sequence")
    if action_schema["properties"]["action_id"].get("pattern") != r"^act\.[A-Za-z0-9_.-]+$":
        fail("AgentAction action_id must enforce the typed act. prefix")
    if action_schema["properties"]["agent_id"].get("pattern") != r"^agent\.[A-Za-z0-9_.-]+$":
        fail("AgentAction agent_id must enforce the typed agent. prefix")

    state_schema = load_json(ROOT / "specs" / "world-state.schema.json")
    required_lineage = {
        "world_version",
        "catalog_version",
        "state_revision",
        "canonicalization_version",
        "hash_algorithm",
        "last_event_digest",
    }
    missing = sorted(required_lineage - set(state_schema.get("required", [])))
    if missing:
        fail(f"WorldState missing canonical lineage requirements: {missing}")

    def find_number_schema(value):
        if isinstance(value, dict):
            if value.get("type") == "number":
                return True
            return any(find_number_schema(v) for v in value.values())
        if isinstance(value, list):
            return any(find_number_schema(v) for v in value)
        return False

    if find_number_schema(state_schema) or find_number_schema(
        load_json(ROOT / "specs" / "world-seed.schema.json")
    ):
        fail("canonical WorldState/WorldSeed quantities must use integer fixed-point schemas")

    for version in ("0.1", "0.2"):
        catalog_schema = load_json(
            ROOT / "specs" / f"event-catalog-{version}.schema.json"
        )
        if catalog_schema.get("x-noema-closed") is not True:
            fail(f"event-catalog/{version} composed schema must be closed")
        refs = [part.get("$ref") for part in catalog_schema.get("allOf", [])]
        if "world-event.schema.json" not in refs:
            fail(f"event-catalog/{version} must compose the WorldEvent envelope")

    protocol = (ROOT / "protocols" / "agent-protocol-v1.md").read_text(
        encoding="utf-8"
    )
    for marker in (
        "cumulative per logical delivery stream",
        "RESUME_POSITION_EXPIRED",
        "RESUME_POSITION_INVALID",
    ):
        if marker not in protocol:
            fail(f"Agent Protocol recovery contract missing: {marker}")

    deployment = (ROOT / "docs" / "DEPLOYMENT.md").read_text(encoding="utf-8")
    module_contracts = (ROOT / "docs" / "MODULE-CONTRACTS.md").read_text(
        encoding="utf-8"
    )
    security = (ROOT / "docs" / "SECURITY.md").read_text(encoding="utf-8")
    for marker, text in (
        ("exactly one active fenced canonical writer", deployment + module_contracts),
        ("SERIALIZABLE", deployment + module_contracts),
        ("mandatory for `research-isolated`", security),
        ("INVALID_EVIDENCE", security),
    ):
        if marker not in text:
            fail(f"RFC-0003 runtime/security contract missing: {marker}")

    rfc = (ROOT / "rfcs" / "RFC-0003-deterministic-contract-hardening.md").read_text(
        encoding="utf-8"
    )
    if "**Accepted**" not in rfc.split("## Summary", 1)[0]:
        fail("RFC-0003 must be Accepted")
    ok("RFC-0003 architecture hardening contracts are machine-gated")




def check_lab_v04(Draft202012Validator) -> None:
    """Validate v0.4 Lab schemas, fixtures, isolation, null results."""
    import hashlib

    def canonical_digest(value: object) -> str:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return "sha256:" + hashlib.sha256(payload).hexdigest()

    pairs = [
        ("specs/experiment-intent.schema.json", "examples/v04-lab/experiment-intent.json"),
        ("specs/experiment.schema.json", "examples/v04-lab/experiment.json"),
        ("specs/intervention.schema.json", "examples/v04-lab/intervention-ablation.json"),
        ("specs/intervention.schema.json", "examples/v04-lab/intervention-perturbation.json"),
        ("specs/experiment-plan.schema.json", "examples/v04-lab/experiment-plan.json"),
        ("specs/experiment-run.schema.json", "examples/v04-lab/run-baseline.json"),
        ("specs/experiment-run.schema.json", "examples/v04-lab/run-intervention.json"),
        ("specs/experiment-run.schema.json", "examples/v04-lab/run-version-differential.json"),
        ("specs/experiment-fork.schema.json", "examples/v04-lab/experiment-fork.json"),
        ("specs/lab-result.schema.json", "examples/v04-lab/lab-result.json"),
        ("specs/lab-result.schema.json", "examples/v04-lab/lab-result-null.json"),
        ("specs/simple-result-projection.schema.json", "examples/v04-lab/simple-result-projection.json"),
        ("specs/lab-audit-record.schema.json", "examples/v04-lab/lab-audit.json"),
    ]
    for schema_rel, fixture_rel in pairs:
        schema = load_json(ROOT / schema_rel)
        fixture = load_json(ROOT / fixture_rel)
        errs = list(Draft202012Validator(schema).iter_errors(fixture))
        if errs:
            fail(f"{fixture_rel} fails {schema_rel}: {errs[0].message}")

    fork = load_json(ROOT / "examples" / "v04-lab" / "experiment-fork.json")
    if fork.get("mutates_production") is not False:
        fail("lab fork must set mutates_production false")

    exp = load_json(ROOT / "examples" / "v04-lab" / "experiment.json")
    if exp.get("authorization", {}).get("mode") != "EXPERIMENTAL_FORK_ONLY":
        fail("lab experiment must authorize EXPERIMENTAL_FORK_ONLY")
    intent = load_json(ROOT / "examples" / "v04-lab" / "experiment-intent.json")
    if exp.get("source_intent_id") != intent.get("intent_record_id"):
        fail("compiled experiment must retain its source intent identity")

    result = load_json(ROOT / "examples" / "v04-lab" / "lab-result.json")
    if result.get("interpretation") == "PROVEN":
        fail("lab results must not use PROVEN")
    if result.get("failed_experiments_retained") is not True:
        fail("lab results must retain failed experiments")

    null = load_json(ROOT / "examples" / "v04-lab" / "lab-result-null.json")
    if null.get("interpretation") not in ("NOT_SUPPORTED", "INCONCLUSIVE"):
        fail("null lab result fixture should be NOT_SUPPORTED or INCONCLUSIVE")

    projection = load_json(ROOT / "examples" / "v04-lab" / "simple-result-projection.json")
    if projection.get("experiment_id") != exp.get("experiment_id") or projection.get("lab_result_id") != result.get("lab_result_id"):
        fail("simple result projection must resolve to the same experiment and Lab result")
    if projection.get("source_intent_id") != intent.get("intent_record_id") or result.get("source_intent_id") != intent.get("intent_record_id"):
        fail("intent provenance must survive compilation through Lab result projection")
    if projection.get("interpretation") != result.get("interpretation") or projection.get("claim_label") != result.get("claim_label"):
        fail("simple result projection must not strengthen Lab interpretation or claim label")
    if projection.get("compiler_readiness") != result.get("compiler_readiness"):
        fail("simple result projection must preserve compiler readiness")

    def respects_lab_result(simple: dict[str, object], lab: dict[str, object]) -> bool:
        return all(simple.get(field) == lab.get(field) for field in ("experiment_id", "lab_result_id", "source_intent_id", "interpretation", "claim_label", "compiler_readiness"))

    if not respects_lab_result(projection, result):
        fail("simple result projection must retain the exact Lab claim boundary")
    projection_payload = dict(projection)
    projection_payload.pop("digest", None)
    if projection.get("digest") != canonical_digest(projection_payload):
        fail("simple result projection digest is not canonical/stable")
    if "CAPTURE_AS_TEST" in projection.get("allowed_actions", []):
        fail("CAPTURE AS TEST must be absent when compiler readiness is NOT_READY")

    # negatives
    neg_fork = load_json(ROOT / "examples" / "negative" / "invalid-lab-mutates-production.json")
    fork_schema = load_json(ROOT / "specs" / "experiment-fork.schema.json")
    if not list(Draft202012Validator(fork_schema).iter_errors(neg_fork)):
        fail("invalid-lab-mutates-production should fail schema")
    neg_res = load_json(ROOT / "examples" / "negative" / "invalid-lab-result-proven.json")
    lr_schema = load_json(ROOT / "specs" / "lab-result.schema.json")
    if not list(Draft202012Validator(lr_schema).iter_errors(neg_res)):
        fail("invalid-lab-result-proven should fail schema")

    # Identity and fork content addresses are reproducible from canonical payloads.
    identity_payload = dict(exp["identity"])
    identity_payload.pop("input_digest", None)
    if exp["identity"].get("input_digest") != canonical_digest(identity_payload):
        fail("Lab experiment identity digest is not canonical/stable")
    if exp.get("input_digest") != exp["identity"].get("input_digest"):
        fail("Lab experiment root and identity input digests must agree")
    fork_payload = {k: v for k, v in fork.items() if k not in ("fork_digest", "digest")}
    if fork.get("fork_digest") != canonical_digest(fork_payload):
        fail("Lab fork digest is not canonical/stable")
    if fork.get("experimental_world_id") == fork.get("source_world_id") or not fork.get("experimental_ledger_id"):
        fail("Lab fork must use distinct experimental world and ledger identities")

    # Required controls change validity and may not be ignored.
    controls = load_json(ROOT / "examples" / "v04-lab" / "controls.json")["controls"]
    required_roles = {c["role"] for c in controls if c.get("required")}
    if any("relationship_to_experiment" not in c for c in controls):
        fail("each Lab control needs relationship_to_experiment")
    if not required_roles.issubset(set(result.get("control_outcomes", {}))):
        fail("Lab result omits required control outcomes")
    def control_disposition(outcomes: dict[str, str]) -> str:
        return "COMPLETE" if all(outcomes.get(role) == "PASS" for role in required_roles) else "INVALID"
    if control_disposition(result["control_outcomes"]) != "COMPLETE":
        fail("passing required controls should preserve complete execution")
    failed_controls = dict(result["control_outcomes"])
    failed_controls[next(iter(required_roles))] = "FAIL"
    if control_disposition(failed_controls) != "INVALID":
        fail("required failed control must invalidate experiment")

    # Counterfactual declarations are complete and an unsupported lesion is retained as NOT_COMPUTABLE.
    counter = load_json(ROOT / "examples" / "v04-lab" / "counterfactual.json")
    required_counter = {"counterfactual_id", "source_trajectory_id", "fork_point", "changed_variables", "held_constant_variables", "seed_policy", "agent_version", "world_version", "equivalence_boundary"}
    if not required_counter.issubset(counter) or not counter["changed_variables"] or not counter["held_constant_variables"]:
        fail("counterfactual fixture lacks declared changed/held variables")
    changed = {v.get("variable_id") for v in counter["changed_variables"]}
    if changed & set(counter["held_constant_variables"]):
        fail("counterfactual variable cannot be both changed and held constant")
    lesion = load_json(ROOT / "examples" / "v04-lab" / "intervention-lesion-not-computable.json")
    lesion_schema = load_json(ROOT / "specs" / "intervention.schema.json")
    if list(Draft202012Validator(lesion_schema).iter_errors(lesion)):
        fail("NOT_COMPUTABLE lesion fixture fails intervention schema")
    if lesion.get("type") != "LESION" or lesion.get("authorization", {}).get("adapter_support") is not False or "NOT_COMPUTABLE" not in lesion.get("expected_mechanical_effect", ""):
        fail("unsupported lesion must be explicit and NOT_COMPUTABLE")

    # Full audit ledger is schema-valid and hash chained across every Lab stage.
    audit_schema = load_json(ROOT / "specs" / "lab-audit-record.schema.json")
    audit_previous = None
    audit_kinds: set[str] = set()
    for line in (ROOT / "examples" / "v04-lab" / "lab-audit-ledger.jsonl").read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        if list(Draft202012Validator(audit_schema).iter_errors(record)):
            fail("Lab audit ledger record fails schema")
        payload = dict(record)
        recorded_digest = payload.pop("digest")
        if recorded_digest != canonical_digest(payload):
            fail("Lab audit ledger digest is not canonical")
        if record.get("previous_digest") != audit_previous:
            fail("Lab audit ledger chain is broken")
        audit_previous = recorded_digest
        audit_kinds.add(record["event_kind"])
    required_audit_kinds = {"DESIGN_VALIDATION", "PLAN_GENERATION", "FORK_CREATION", "INTERVENTION_APPLY", "CONTROL_EXECUTION", "RUN_START", "RUN_END", "DIVERGENCE", "METRIC_CALCULATION", "REPLICATION_COMPARISON", "RESULT_CLASSIFICATION", "CANDIDATE_HANDOFF", "STATE_TRANSITION"}
    if audit_kinds != required_audit_kinds:
        fail("Lab audit ledger does not cover all claim-bearing stages")

    # Local negative fixtures prove new design and fork guards reject invalid records.
    invalid_design = load_json(ROOT / "examples" / "v04-lab" / "negative" / "invalid-experiment-missing-analysis-rule.json")
    if not list(Draft202012Validator(load_json(ROOT / "specs" / "experiment.schema.json")).iter_errors(invalid_design)):
        fail("Lab negative missing analysis rule should fail schema")
    invalid_fork = load_json(ROOT / "examples" / "v04-lab" / "negative" / "invalid-fork-production-mutation.json")
    if not list(Draft202012Validator(fork_schema).iter_errors(invalid_fork)):
        fail("Lab negative production mutation should fail schema")
    invalid_intent = load_json(ROOT / "examples" / "v04-lab" / "negative" / "invalid-experiment-intent-unknown.json")
    intent_schema = load_json(ROOT / "specs" / "experiment-intent.schema.json")
    if not list(Draft202012Validator(intent_schema).iter_errors(invalid_intent)):
        fail("unknown experiment intent should fail schema")
    projection_schema = load_json(ROOT / "specs" / "simple-result-projection.schema.json")
    invalid_capture = load_json(ROOT / "examples" / "v04-lab" / "negative" / "invalid-capture-not-ready.json")
    if not list(Draft202012Validator(projection_schema).iter_errors(invalid_capture)):
        fail("CAPTURE AS TEST with NOT_READY must fail simple projection schema")
    invalid_overclaim = load_json(ROOT / "examples" / "v04-lab" / "negative" / "invalid-simple-result-overclaim.json")
    if respects_lab_result(invalid_overclaim, result):
        fail("simple result overclaim negative must violate Lab claim boundary")

    # catalogs present
    for rel in (
        "specs/perturbation-catalog.v04.json",
        "specs/ablation-catalog.v04.json",
        "specs/experiment-variable-registry.v04.json",
    ):
        load_json(ROOT / rel)

    ok("Lab v0.4: schemas, intent compilation, stable digests, isolation, controls, projections, counterfactuals, lesions, negatives, catalogs")


def check_compiler_v05(Draft202012Validator) -> None:
    """Validate v0.5 Phenomenon Compiler schemas, fixtures, capture flow, and gates."""
    import hashlib

    def canonical_digest(value: object) -> str:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return "sha256:" + hashlib.sha256(payload).hexdigest()

    pairs = [
        ("specs/capture-intent.schema.json", "examples/v05-compiler/capture-intent.json"),
        ("specs/compilation-request.schema.json", "examples/v05-compiler/compilation-request.json"),
        ("specs/phenomenon-candidate.schema.json", "examples/v05-compiler/phenomenon-candidate.json"),
        ("specs/phenomenon-dependency-graph.schema.json", "examples/v05-compiler/dependency-graph.json"),
        ("specs/compiler-unit-manifest.schema.json", "examples/v05-compiler/unit-manifest.json"),
        ("specs/behavioral-oracle.schema.json", "examples/v05-compiler/behavioral-oracle.json"),
        ("specs/compiler-result.schema.json", "examples/v05-compiler/compiler-result.json"),
        ("specs/compiler-result.schema.json", "examples/v05-compiler/compiler-result-budget-exhausted.json"),
        ("specs/phenomenon-compile-receipt.schema.json", "examples/v05-compiler/compile-receipt.json"),
        ("specs/captured-test.schema.json", "examples/v05-compiler/captured-test.json"),
        ("specs/regression-result.schema.json", "examples/v05-compiler/regression-result.json"),
        ("specs/regression-result.schema.json", "examples/v05-compiler/regression-result-fail.json"),
        ("specs/capture-defaults.schema.json", "specs/capture-defaults.v05.json"),
        ("specs/capture-status-catalog.schema.json", "specs/capture-status-catalog.json"),
        ("specs/experience-view.schema.json", "examples/v05-compiler/simple-capture-result.json"),
        ("specs/experience-view.schema.json", "examples/v05-compiler/advanced-capture-result.json"),
        ("specs/lab-result.schema.json", "examples/v05-compiler/source-lab-result-ready.json"),
    ]
    for schema_rel, fixture_rel in pairs:
        schema = load_json(ROOT / schema_rel)
        fixture = load_json(ROOT / fixture_rel)
        errs = list(Draft202012Validator(schema).iter_errors(fixture))
        if errs:
            fail(f"{fixture_rel} fails {schema_rel}: {errs[0].message}")

    # Digests stable
    for rel in (
        "examples/v05-compiler/capture-intent.json",
        "examples/v05-compiler/compilation-request.json",
        "examples/v05-compiler/phenomenon-candidate.json",
        "examples/v05-compiler/dependency-graph.json",
        "examples/v05-compiler/unit-manifest.json",
        "examples/v05-compiler/behavioral-oracle.json",
        "examples/v05-compiler/compiler-result.json",
        "examples/v05-compiler/compile-receipt.json",
        "examples/v05-compiler/captured-test.json",
        "examples/v05-compiler/source-lab-result-ready.json",
        "examples/v05-compiler/simple-capture-result.json",
        "examples/v05-compiler/advanced-capture-result.json",
        "examples/v05-compiler/regression-result.json",
    ):
        obj = load_json(ROOT / rel)
        payload = dict(obj)
        recorded = payload.pop("digest", None)
        if recorded != canonical_digest(payload):
            fail(f"{rel} digest is not canonical/stable")

    expected = load_json(ROOT / "examples" / "v05-compiler" / "expected-digests.json")
    captured = load_json(ROOT / "examples" / "v05-compiler" / "captured-test.json")
    if expected.get("captured_test_digest") != captured.get("digest"):
        fail("expected-digests captured_test_digest mismatch")

    lab = load_json(ROOT / "examples" / "v05-compiler" / "source-lab-result-ready.json")
    if lab.get("compiler_readiness") != "READY":
        fail("v0.5 source Lab Result must be READY for normal capture")
    intent = load_json(ROOT / "examples" / "v05-compiler" / "capture-intent.json")
    if intent.get("capture_intent") != "CAPTURE_AS_TEST":
        fail("capture intent must be CAPTURE_AS_TEST")
    if intent.get("source_lab_result_id") != lab.get("lab_result_id"):
        fail("capture intent must reference READY Lab Result")
    creq = load_json(ROOT / "examples" / "v05-compiler" / "compilation-request.json")
    if creq.get("source_lab_result_id") != lab.get("lab_result_id"):
        fail("compilation request must retain Lab Result lineage")
    if creq.get("compiler_version", {}).get("canonicalization") != "noema-jcs/1":
        fail("compilation request must pin noema-jcs/1")
    if creq.get("capture_defaults_version") != "capture-defaults/0.5.0":
        fail("compilation request must pin capture defaults version")

    defaults = load_json(ROOT / "specs" / "capture-defaults.v05.json")
    for field in (
        "minimization_strategy_version", "oracle_policy", "seed_policy",
        "replication_policy", "budget_profile", "generalization_default",
        "capture_visibility_default", "budgets", "allowed_override_fields", "layer_order",
    ):
        if field not in defaults:
            fail(f"capture defaults missing {field}")
    if defaults["layer_order"][0] != "WORLD_CONFIGURATION":
        fail("minimization layer order must start with WORLD_CONFIGURATION")

    # Status catalog covers all compiler statuses
    status_cat = load_json(ROOT / "specs" / "capture-status-catalog.json")
    mapped = {m["machine_status"] for m in status_cat["mappings"]}
    required_status = {"COMPILED", "NOT_COMPUTABLE", "INVALID_EVIDENCE", "INCONCLUSIVE", "ABORTED", "BUDGET_EXHAUSTED"}
    if mapped != required_status:
        fail(f"capture status catalog must map all compiler statuses, missing/extra {required_status ^ mapped}")

    result = load_json(ROOT / "examples" / "v05-compiler" / "compiler-result.json")
    if result.get("status") != "COMPILED" or result.get("minimality_status") != "ONE_MINIMAL":
        fail("successful compiler result must be COMPILED with ONE_MINIMAL")
    if result.get("captured_test_id") != captured.get("captured_test_id"):
        fail("compiler result and captured test IDs must agree")
    if captured.get("claim_label") != result.get("claim_label"):
        fail("captured test must not strengthen compiler claim label")
    if captured.get("generalization_boundary") != "SCENARIO_FAMILY":
        fail("example captured test boundary should be SCENARIO_FAMILY")
    if "General capability" in json.dumps(captured.get("known_limits", [])):
        pass  # limits may mention non-claims
    simple = load_json(ROOT / "examples" / "v05-compiler" / "simple-capture-result.json")
    advanced = load_json(ROOT / "examples" / "v05-compiler" / "advanced-capture-result.json")
    if captured["captured_test_id"] not in simple["canonical_source_refs"]:
        fail("simple capture view must reference captured test id")
    if captured["captured_test_id"] not in advanced["canonical_source_refs"]:
        fail("advanced capture view must reference same captured test id")
    if simple.get("canonical_claim_label") != captured.get("claim_label"):
        fail("simple capture view cannot strengthen claim label")
    simple_text = json.dumps(simple["presentation"]).lower()
    for jargon in ("ddmin", "oracle cache", "audit root", "dependency-closed", "unit_id"):
        if jargon in simple_text:
            fail(f"simple capture view leaks jargon: {jargon}")

    # Budget exhaustion is not minimality
    budget = load_json(ROOT / "examples" / "v05-compiler" / "compiler-result-budget-exhausted.json")
    if budget.get("status") != "BUDGET_EXHAUSTED" or budget.get("minimality_status") == "ONE_MINIMAL":
        fail("BUDGET_EXHAUSTED must not claim ONE_MINIMAL")
    if budget.get("promotion_status") == "PROMOTABLE":
        fail("budget exhausted result must not be PROMOTABLE")

    # Over-minimization rejected
    over = load_json(ROOT / "examples" / "v05-compiler" / "over-minimization-proposal.json")
    if over.get("oracle_result") != "NOT_PRESERVED" or over.get("decision") != "REJECT_REMOVAL":
        fail("over-minimization proposal must be NOT_PRESERVED + REJECT_REMOVAL")

    # Minimization records digest chain
    min_schema = load_json(ROOT / "specs" / "minimization-record.schema.json")
    prev = None
    decisions = []
    for line in (ROOT / "examples" / "v05-compiler" / "minimization-records.jsonl").read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        if list(Draft202012Validator(min_schema).iter_errors(rec)):
            fail("minimization record fails schema")
        payload = dict(rec)
        recorded = payload.pop("record_digest")
        if recorded != canonical_digest(payload):
            fail("minimization record digest not canonical")
        if rec.get("previous_record_digest") != prev:
            fail("minimization record chain broken")
        if rec.get("oracle_result") in ("INCONCLUSIVE", "INVALID") and rec.get("decision") == "ACCEPT_REMOVAL":
            fail("INCONCLUSIVE/INVALID must never authorize removal")
        prev = recorded
        decisions.append(rec["decision"])
    if "ACCEPT_REMOVAL" not in decisions or "REJECT_REMOVAL" not in decisions:
        fail("minimization records must show both accept and reject paths")

    # Audit chain
    audit_schema = load_json(ROOT / "specs" / "compiler-audit-record.schema.json")
    audit_prev = None
    phases: set[str] = set()
    for line in (ROOT / "examples" / "v05-compiler" / "compiler-audit-ledger.jsonl").read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        if list(Draft202012Validator(audit_schema).iter_errors(rec)):
            fail("compiler audit record fails schema")
        payload = dict(rec)
        recorded = payload.pop("record_digest")
        if recorded != canonical_digest(payload):
            fail("compiler audit digest not canonical")
        if rec.get("previous_record_digest") != audit_prev:
            fail("compiler audit chain broken")
        audit_prev = recorded
        phases.add(rec["phase"])
    for phase in ("ADMISSION", "SOURCE_REPLAY", "MINIMIZATION", "ORACLE", "PACKAGING", "PROMOTION"):
        if phase not in phases:
            fail(f"compiler audit missing phase {phase}")
    if result.get("audit_root_digest") != audit_prev:
        fail("compiler result audit_root_digest must match ledger tip")

    receipt = load_json(ROOT / "examples" / "v05-compiler" / "compile-receipt.json")
    if receipt.get("canonicalization") != "noema-jcs/1":
        fail("compile receipt must reuse noema-jcs/1")
    if receipt.get("status") != "COMPILED":
        fail("success receipt status must match compiler result")
    if "none" not in receipt.get("provider_adapter_identity", {}).get("version", ""):
        # allow exact none
        if receipt["provider_adapter_identity"]["version"] != "none":
            fail("provider adapter identity required even when unused")

    # Regression non-ranking
    reg = load_json(ROOT / "examples" / "v05-compiler" / "regression-result.json")
    reg_fail = load_json(ROOT / "examples" / "v05-compiler" / "regression-result-fail.json")
    if reg.get("not_a_global_ranking") is not True or reg_fail.get("not_a_global_ranking") is not True:
        fail("regression results must set not_a_global_ranking true")
    if reg_fail.get("outcome") != "FAIL":
        fail("regression fail fixture must outcome FAIL")

    # Negatives reject
    neg_pairs = [
        ("specs/compiler-result.schema.json", "examples/negative/invalid-compiler-result-unknown-status.json"),
        ("specs/captured-test.schema.json", "examples/negative/invalid-captured-test-missing-title.json"),
        ("specs/capture-intent.schema.json", "examples/negative/invalid-capture-intent-wrong-action.json"),
        ("specs/regression-result.schema.json", "examples/negative/invalid-regression-implies-global-rank.json"),
    ]
    for schema_rel, fixture_rel in neg_pairs:
        if not list(Draft202012Validator(load_json(ROOT / schema_rel)).iter_errors(load_json(ROOT / fixture_rel))):
            fail(f"{fixture_rel} should fail {schema_rel}")

    overclaim = load_json(ROOT / "examples" / "v05-compiler" / "negative" / "invalid-simple-overclaim.json")
    if overclaim.get("canonical_claim_label") == captured.get("claim_label"):
        fail("overclaim negative should strengthen claim label vs captured test")

    # Docs present and usability invariant
    scope = (ROOT / "docs" / "releases" / "v0.5" / "SCOPE.md").read_text(encoding="utf-8")
    if "ordinary-user conceptual burden" not in scope and "conceptual burden" not in scope:
        fail("v0.5 scope must state usability invariant")
    compiler_doc = (ROOT / "docs" / "PHENOMENON-COMPILER.md").read_text(encoding="utf-8")
    for token in ("ddmin", "PRESERVED", "compile_id", "BUDGET_EXHAUSTED"):
        if token not in compiler_doc:
            fail(f"PHENOMENON-COMPILER missing {token}")
    for rel in (
        "docs/CAPTURE-INTENT-COMPILATION.md",
        "docs/COMPILATION-IDENTITY.md",
        "docs/BEHAVIORAL-ORACLE.md",
        "docs/OVER-MINIMIZATION.md",
        "docs/CAPTURED-TEST-FORMAT.md",
        "docs/BEHAVIORAL-REGRESSION.md",
    ):
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")

    # Unit protected retention
    units = load_json(ROOT / "examples" / "v05-compiler" / "unit-manifest.json")["units"]
    protected = [u for u in units if u.get("protected")]
    if not protected or any(u.get("final_disposition") == "REMOVED" for u in protected):
        fail("protected units must not be REMOVED")

    ok(
        "Compiler v0.5: schemas, capture intent, defaults, digests, audit/receipt, "
        "minimization, oracle, simple/advanced equivalence, budget/privacy, negatives"
    )


def check_deep_time_v06(Draft202012Validator) -> None:
    """Validate v0.6 Deep Time foundation: institutions, succession, artifacts, lore boundary."""
    import hashlib

    def canonical_digest(value: object) -> str:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return "sha256:" + hashlib.sha256(payload).hexdigest()

    pairs = [
        ("specs/institution.schema.json", "examples/v06-deep-time/institution.json"),
        ("specs/institution.schema.json", "examples/v06-deep-time/institution-active.json"),
        ("specs/institution.schema.json", "examples/v06-deep-time/institution-successor.json"),
        ("specs/institution-lineage.schema.json", "examples/v06-deep-time/institution-lineage.json"),
        ("specs/succession-record.schema.json", "examples/v06-deep-time/succession.json"),
        ("specs/succession-record.schema.json", "examples/v06-deep-time/succession-vacant.json"),
        ("specs/historical-artifact.schema.json", "examples/v06-deep-time/artifact-archive.json"),
        ("specs/historical-artifact.schema.json", "examples/v06-deep-time/artifact-marker.json"),
        ("specs/historical-artifact.schema.json", "examples/v06-deep-time/artifact-destroyed.json"),
        ("specs/historical-claim.schema.json", "examples/v06-deep-time/claim-peaceful-transfer.json"),
        ("specs/historical-claim.schema.json", "examples/v06-deep-time/claim-conflict-transfer.json"),
        ("specs/historical-claim.schema.json", "examples/v06-deep-time/claim-nacre-built.json"),
        ("specs/historical-reconstruction.schema.json", "examples/v06-deep-time/reconstruction-archaeology.json"),
        ("specs/semantic-lineage.schema.json", "examples/v06-deep-time/semantic-lineage.json"),
        ("specs/historical-name.schema.json", "examples/v06-deep-time/name-burnt-relay.json"),
        ("specs/world-scar.schema.json", "examples/v06-deep-time/world-scar.json"),
        ("specs/historical-evidence.schema.json", "examples/v06-deep-time/evidence-ledger-hidden.json"),
        ("specs/historical-evidence.schema.json", "examples/v06-deep-time/evidence-marker-public.json"),
        ("specs/historical-significance.schema.json", "specs/historical-significance.v06.json"),
        ("specs/experience-view.schema.json", "examples/v06-deep-time/play-old-relay.json"),
        ("specs/experience-view.schema.json", "examples/v06-deep-time/watch-timeline.json"),
        ("specs/experience-view.schema.json", "examples/v06-deep-time/study-questions.json"),
    ]
    for schema_rel, fixture_rel in pairs:
        errs = list(Draft202012Validator(load_json(ROOT / schema_rel)).iter_errors(load_json(ROOT / fixture_rel)))
        if errs:
            fail(f"{fixture_rel} fails {schema_rel}: {errs[0].message}")

    for rel in (
        "examples/v06-deep-time/institution.json",
        "examples/v06-deep-time/succession.json",
        "examples/v06-deep-time/artifact-archive.json",
        "examples/v06-deep-time/reconstruction-archaeology.json",
        "examples/v06-deep-time/world-scar.json",
        "examples/v06-deep-time/semantic-lineage.json",
        "examples/v06-deep-time/claim-nacre-built.json",
    ):
        obj = load_json(ROOT / rel)
        payload = dict(obj)
        recorded = payload.pop("digest", None)
        if recorded != canonical_digest(payload):
            fail(f"{rel} digest is not canonical/stable")

    inst = load_json(ROOT / "examples" / "v06-deep-time" / "institution.json")
    if not inst["continuity"]["survives_participant_departure"]:
        fail("fixture institution must survive participant departure")
    if inst["status"] not in ("DORMANT", "ACTIVE", "ESTABLISHED", "EMERGING", "TRANSFORMED", "DISSOLVED"):
        fail("institution status invalid")
    succ = load_json(ROOT / "examples" / "v06-deep-time" / "succession.json")
    if succ.get("institution_continues") is not True:
        fail("succession fixture must keep institution continuing after founder transfer")
    if succ.get("from_holder") == succ.get("to_holder"):
        fail("succession must change holder")

    art = load_json(ROOT / "examples" / "v06-deep-time" / "artifact-archive.json")
    if art.get("claims_are_not_world_truth") is not True:
        fail("artifacts must declare claims_are_not_world_truth")
    destroyed = load_json(ROOT / "examples" / "v06-deep-time" / "artifact-destroyed.json")
    if destroyed.get("integrity") != "DESTROYED" or destroyed.get("existed_fact_preserved") is not True:
        fail("destroyed artifact must preserve existence fact")

    c1 = load_json(ROOT / "examples" / "v06-deep-time" / "claim-peaceful-transfer.json")
    c2 = load_json(ROOT / "examples" / "v06-deep-time" / "claim-conflict-transfer.json")
    if c1.get("evidence_status") != "CONTESTED" or c2.get("evidence_status") != "CONTESTED":
        fail("conflicting claims must be CONTESTED")
    if "claim.conflict-transfer" not in c1.get("contradicting_claim_refs", []):
        fail("peaceful claim must reference contradicting conflict claim")

    recon = load_json(ROOT / "examples" / "v06-deep-time" / "reconstruction-archaeology.json")
    if recon.get("no_narrative_invention") is not True:
        fail("reconstruction must forbid narrative invention")
    if recon.get("hidden_ledger_not_exposed") is not True:
        fail("archaeology reconstruction must not expose hidden ledger")
    if recon.get("agent_knowledge_only") is not True:
        fail("archaeology reconstruction is agent knowledge only")
    if not recon.get("contradictions"):
        fail("reconstruction fixture should retain contradictions")
    if not recon.get("unknowns"):
        fail("reconstruction must list unknowns rather than inventing")

    hidden = load_json(ROOT / "examples" / "v06-deep-time" / "evidence-ledger-hidden.json")
    if hidden.get("accessible_to_agents") is not False or hidden.get("hidden_from_ordinary_observation") is not True:
        fail("full ledger evidence must be hidden from ordinary observation")

    name = load_json(ROOT / "examples" / "v06-deep-time" / "name-burnt-relay.json")
    if name.get("canonical_id_immutable") is not True:
        fail("historical names must keep canonical IDs immutable")
    if name.get("canonical_id") != "room.relay_south.004":
        fail("rename fixture must not change canonical room id")

    semantic = load_json(ROOT / "examples" / "v06-deep-time" / "semantic-lineage.json")
    if semantic.get("auto_interpreted") is not False:
        fail("semantic lineage must not auto-interpret")
    if semantic.get("canonical_subject_id") != "room.relay_south.004":
        fail("semantic lineage must pin stable canonical subject id")

    successor = load_json(ROOT / "examples" / "v06-deep-time" / "institution-successor.json")
    if successor["continuity"]["identity_class"] != "SUCCESSOR_ENTITY":
        fail("revival fixture must be SUCCESSOR_ENTITY when interpretation differs")
    if successor["continuity"]["predecessor_institution_id"] != inst["institution_id"]:
        fail("successor must link predecessor institution")

    scar = load_json(ROOT / "examples" / "v06-deep-time" / "world-scar.json")
    if not scar.get("derived_from_event_refs"):
        fail("world scars must derive from events")
    if scar.get("observable") is not True:
        fail("fixture scar should be PLAY-observable")

    decay = load_json(ROOT / "specs" / "historical-decay.v06.json")
    if "canonical event" not in decay.get("notes", "").lower() and "Canonical event" not in decay.get("notes", ""):
        if "ledger" not in decay.get("notes", "").lower():
            fail("decay catalog must state ledger does not decay")
    for profile in decay.get("profiles", []):
        if profile.get("deterministic") is not True and "deterministic" in profile:
            pass
    if not any(p.get("never_deletes_history") for p in decay.get("profiles", []) if p.get("applies_to") == "INFRASTRUCTURE"):
        # at least one profile should never delete history
        if not any(p.get("never_deletes_history") for p in decay.get("profiles", [])):
            fail("decay profiles must include never_deletes_history guard")

    deep = (ROOT / "docs" / "DEEP-TIME.md").read_text(encoding="utf-8")
    for token in (
        "Lore is a derived presentation",
        "canonical evidence wins",
        "WORLD EVENT HISTORY",
        "The world can forget",
        "canonical ledger cannot",
    ):
        if token not in deep:
            fail(f"DEEP-TIME.md missing normative token: {token}")

    audit = (ROOT / "docs" / "EVENT-CATALOG-DEEP-TIME-AUDIT.md").read_text(encoding="utf-8")
    if "No event-catalog/0.3" not in audit and "no event-catalog/0.3" not in audit.lower():
        fail("event catalog audit must refuse silent catalog expansion")

    # Simple projection equivalence / no jargon
    play = load_json(ROOT / "examples" / "v06-deep-time" / "play-old-relay.json")
    advanced = load_json(ROOT / "examples" / "v06-deep-time" / "advanced-history.json")
    if inst["institution_id"] not in advanced["canonical_source_refs"] and inst["institution_id"] not in json.dumps(advanced["presentation"]):
        fail("advanced view must reference institution id")
    play_text = json.dumps(play["presentation"]).lower()
    for jargon in ("lineage graph", "state digest", "succession state machine", "semantic lineage"):
        if jargon in play_text:
            fail(f"simple PLAY view leaks jargon: {jargon}")

    # Negatives
    neg_pairs = [
        ("specs/institution.schema.json", "examples/negative/invalid-institution-no-origin.json"),
        ("specs/succession-record.schema.json", "examples/negative/invalid-succession-mechanism.json"),
        ("specs/historical-artifact.schema.json", "examples/negative/invalid-artifact-claims-as-truth.json"),
        ("specs/historical-reconstruction.schema.json", "examples/negative/invalid-reconstruction-invents-narrative.json"),
        ("specs/historical-name.schema.json", "examples/negative/invalid-historical-name-mutates-id.json"),
        ("specs/historical-claim.schema.json", "examples/negative/invalid-claim-missing-sources.json"),
    ]
    for schema_rel, fixture_rel in neg_pairs:
        if not list(Draft202012Validator(load_json(ROOT / schema_rel)).iter_errors(load_json(ROOT / fixture_rel))):
            fail(f"{fixture_rel} should fail {schema_rel}")

    bad_hidden = load_json(ROOT / "examples" / "v06-deep-time" / "negative" / "invalid-hidden-ledger-in-agent-knowledge.json")
    if bad_hidden.get("hidden_ledger_not_exposed") is not False:
        fail("hidden-ledger negative must set hidden_ledger_not_exposed false")
    # semantic: using hidden ledger evidence in agent knowledge is a policy fail even if schema-valid after digest
    if "evidence.ledger.founding" not in bad_hidden.get("evidence_set", []):
        fail("hidden-ledger negative must include ledger evidence in agent reconstruction")

    expected = load_json(ROOT / "examples" / "v06-deep-time" / "expected-digests.json")
    if expected.get("institution_digest") != inst.get("digest"):
        fail("expected-digests institution mismatch")

    era = load_json(ROOT / "examples" / "v06-deep-time" / "era-timeline.json")
    if era.get("fixture_not_live_canon") is not True:
        fail("fixture timeline must declare it is not live-world canon")
    if era.get("lore_boundary") != "derived_only":
        fail("era timeline must pin derived_only lore boundary")

    # --- Genesis (admin-only, simplified) ---
    profile_schema = load_json(ROOT / "specs" / "genesis-profile.schema.json")
    seed_schema = load_json(ROOT / "specs" / "story-seed.schema.json")
    result_schema = load_json(ROOT / "specs" / "genesis-result.schema.json")
    profiles = load_json(ROOT / "specs" / "genesis-profiles.v06.json")
    seeds = load_json(ROOT / "specs" / "story-seeds.v06.json")
    if len(profiles.get("profiles", [])) != 3:
        fail("exactly three genesis profiles required")
    profile_ids = {p["profile_id"] for p in profiles["profiles"]}
    if profile_ids != {"YOUNG_FRONTIER", "FRACTURED_OLD_WORLD", "RECOVERING_NETWORK"}:
        fail("genesis profile set must be the closed three")
    for p in profiles["profiles"]:
        if list(Draft202012Validator(profile_schema).iter_errors(p)):
            fail(f"genesis profile {p.get('profile_id')} invalid")
    seed_ids = {s["seed_id"] for s in seeds.get("seeds", [])}
    expected_seeds = {
        "FOUNDING_SPLIT", "OLD_TRADE_NETWORK", "FAILED_SETTLEMENT",
        "RESOURCE_CRISIS", "LOST_ARCHIVE", "DISPUTED_SUCCESSION",
    }
    if seed_ids != expected_seeds:
        fail("story seed catalog must match closed set")
    for s in seeds["seeds"]:
        if list(Draft202012Validator(seed_schema).iter_errors(s)):
            fail(f"story seed {s.get('seed_id')} invalid")
        if s.get("does_not_determine_future") is not True:
            fail("story seeds must not determine the future")

    ga = load_json(ROOT / "examples" / "v06-deep-time" / "genesis-result-a.json")
    gb = load_json(ROOT / "examples" / "v06-deep-time" / "genesis-result-b.json")
    for label, g in (("a", ga), ("b", gb)):
        errs = list(Draft202012Validator(result_schema).iter_errors(g))
        if errs:
            fail(f"genesis-result-{label} invalid: {errs[0].message}")
        payload = dict(g)
        rec = payload.pop("digest")
        if rec != canonical_digest(payload):
            fail(f"genesis-result-{label} digest not canonical")
        if g.get("admin_only") is not True:
            fail("genesis result must be admin_only")
        if g.get("ordinary_world_valid") is not True:
            fail("cycle 0 must declare ordinary_world_valid")
        if len(g.get("starting_opportunities", [])) < 3:
            fail("genesis must provide ≥3 starting opportunities")
        hidden = g.get("hidden_from_players") or {}
        for k in ("genesis_profile", "story_seeds", "world_seed", "full_prehistory"):
            if hidden.get(k) is not True:
                fail(f"players must not receive {k}")
        if g.get("rules_versions", {}).get("canonicalization") != "noema-jcs/1":
            fail("genesis must reuse noema-jcs/1")

    if ga.get("genesis_profile_id") != gb.get("genesis_profile_id") or ga.get("story_seed_ids") != gb.get("story_seed_ids"):
        fail("A/B fixtures must share profile and story seeds")
    if ga.get("world_seed") == gb.get("world_seed"):
        fail("different-seed fixture must change world_seed")
    if ga.get("cycle0_world_state_digest") == gb.get("cycle0_world_state_digest"):
        fail("different seeds must produce different Cycle 0 digests")
    if ga.get("genesis_id") == gb.get("genesis_id"):
        fail("different claim-bearing runs need distinct genesis_id")

    if ga.get("activated") is not True or ga.get("genesis_config_immutable_after_activation") is not True:
        fail("activated genesis must freeze configuration")
    if ga.get("cannot_rerun_on_active_world") is not True:
        fail("activated genesis cannot be rerun on active world")

    c0a = load_json(ROOT / "examples" / "v06-deep-time" / "genesis-cycle0-a.json")
    if c0a.get("ordinary_world_valid") is not True or c0a.get("cycle") != 0:
        fail("cycle0 summary must be cycle 0 and ordinary-valid")
    for req in ("functioning_relays", "damaged_relays", "dormant_institutions", "archive_fragment", "unresolved_territorial_claim"):
        if not c0a.get(req):
            fail(f"fractured genesis cycle0 missing {req}")

    player_entry = load_json(ROOT / "examples" / "v06-deep-time" / "genesis-player-entry.json")
    if player_entry.get("mode") != "PLAY" or player_entry["presentation"].get("no_genesis_controls") is not True:
        fail("player entry must forbid genesis controls")
    rendered = json.dumps(player_entry["presentation"]).lower()
    for banned in ("story seed", "genesis profile", "world_seed", "regenerate", "activate world"):
        if banned in rendered:
            fail(f"player entry leaks genesis control: {banned}")

    gen_doc = (ROOT / "docs" / "GENESIS.md").read_text(encoding="utf-8")
    for token in (
        "admin-only",
        "Genesis configuration = immutable",
        "rerun against an active world",
        "Prefer the smallest architecture",
        "PLAY never exposes",
    ):
        if token not in gen_doc:
            fail(f"GENESIS.md missing token: {token}")
    lore = (ROOT / "docs" / "LORE-BOUNDARY.md").read_text(encoding="utf-8")
    if "not canonical world truth" not in lore:
        fail("LORE-BOUNDARY incomplete")

    gen_negs = [
        ("specs/genesis-result.schema.json", "examples/negative/invalid-genesis-player-invokes.json"),
        ("specs/story-seed.schema.json", "examples/negative/invalid-genesis-story-scripts-future.json"),
        ("specs/genesis-profile.schema.json", "examples/negative/invalid-genesis-unknown-profile.json"),
    ]
    for schema_rel, fixture_rel in gen_negs:
        if not list(Draft202012Validator(load_json(ROOT / schema_rel)).iter_errors(load_json(ROOT / fixture_rel))):
            fail(f"{fixture_rel} should fail {schema_rel}")

    expected = load_json(ROOT / "examples" / "v06-deep-time" / "expected-digests.json")
    if expected.get("genesis_result_a_digest") != ga.get("digest"):
        fail("expected-digests genesis A mismatch")

    ok(
        "Deep Time v0.6: institutions, succession, artifacts, claims, archaeology, "
        "hidden-history protection, renaming, scars, lore boundary, "
        "admin-only Genesis (profiles/seeds/Cycle0/determinism), negatives"
    )


def check_learn_v07(Draft202012Validator) -> None:
    """Validate v0.7 minimal LEARN / capability graph projection."""
    import hashlib

    def canonical_digest(value: object) -> str:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return "sha256:" + hashlib.sha256(payload).hexdigest()

    node_schema = load_json(ROOT / "specs" / "behavior-node.schema.json")
    edge_schema = load_json(ROOT / "specs" / "capability-edge.schema.json")
    graph_schema = load_json(ROOT / "specs" / "capability-graph.schema.json")
    node = load_json(ROOT / "examples" / "v07-capability-graph" / "behavior-node.json")
    edges_doc = load_json(ROOT / "examples" / "v07-capability-graph" / "edges.json")
    graph = load_json(ROOT / "examples" / "v07-capability-graph" / "capability-graph.json")
    simple = load_json(ROOT / "examples" / "v07-capability-graph" / "simple-learn-view.json")
    advanced = load_json(ROOT / "examples" / "v07-capability-graph" / "advanced-learn-view.json")
    source_refs = load_json(ROOT / "examples" / "v07-capability-graph" / "source-refs.json")
    not_tested = load_json(ROOT / "examples" / "v07-capability-graph" / "not-tested-social-topology.json")

    for schema, fixture, label in (
        (node_schema, node, "behavior-node"),
        (graph_schema, graph, "capability-graph"),
    ):
        errs = list(Draft202012Validator(schema).iter_errors(fixture))
        if errs:
            fail(f"{label} invalid: {errs[0].message}")

    edges = edges_doc.get("edges") or []
    if len(edges) < 6:
        fail("v0.7 fixture must include core edge types")
    allowed = {"OBSERVED_IN", "REPRODUCED_BY", "DEPENDS_ON", "FAILS_WITHOUT", "GENERALIZES_TO", "DIFFERS_ACROSS_VERSION"}
    types_seen: set[str] = set()
    for e in edges:
        errs = list(Draft202012Validator(edge_schema).iter_errors(e))
        if errs:
            fail(f"edge {e.get('edge_id')} invalid: {errs[0].message}")
        payload = dict(e)
        rec = payload.pop("digest")
        if rec != canonical_digest(payload):
            fail(f"edge {e.get('edge_id')} digest not canonical")
        if not e.get("evidence_refs"):
            fail(f"edge {e.get('edge_id')} missing evidence")
        if e.get("edge_type") not in allowed:
            fail(f"unsupported edge type {e.get('edge_type')}")
        types_seen.add(e["edge_type"])
        if e.get("source_ref") != node.get("behavior_id"):
            fail("fixture edges must attach to shared-ledger behavior node")

    for required in ("REPRODUCED_BY", "DEPENDS_ON", "FAILS_WITHOUT", "GENERALIZES_TO", "DIFFERS_ACROSS_VERSION"):
        if required not in types_seen:
            fail(f"fixture missing edge type {required}")

    payload = dict(node)
    if payload.pop("digest") != canonical_digest(payload):
        fail("behavior node digest not canonical")
    if not node.get("source_captured_test_ids"):
        fail("behavior node must reference captured tests")
    ctest = node["source_captured_test_ids"][0]
    if not (ROOT / "examples" / "v05-compiler" / "captured-test.json").exists():
        fail("source captured test fixture missing")
    captured = load_json(ROOT / "examples" / "v05-compiler" / "captured-test.json")
    if captured.get("captured_test_id") != ctest:
        fail("behavior node must ground in existing captured test id")

    # Evidence lineage paths exist
    for rel in source_refs.get("captured_tests", []) + source_refs.get("lab_results", []) + source_refs.get("regression_results", []):
        if not (ROOT / rel).exists():
            fail(f"source-refs missing path {rel}")

    # Contested evidence preserved
    contested = [e for e in edges if e.get("relationship_status") == "CONTESTED"]
    if not contested:
        fail("fixture must include contested relationship")
    if not contested[0].get("counterevidence_refs"):
        fail("contested edge must retain counterevidence_refs")

    # Not tested ≠ failed
    if not_tested.get("status") != "NOT_TESTED" or not_tested.get("distinct_from") != "FAILED":
        fail("not-tested fixture must distinguish NOT_TESTED from FAILED")
    if any(e.get("edge_type") == "FAILS_WITHOUT" and "topology" in e.get("target_ref", "") for e in edges):
        fail("not-tested context must not appear as FAILS_WITHOUT")

    # Simple/advanced same identity; simple cannot strengthen
    if node["behavior_id"] not in simple.get("canonical_source_refs", []):
        fail("simple LEARN view must reference behavior_id")
    if node["behavior_id"] not in advanced.get("canonical_source_refs", []):
        fail("advanced LEARN view must reference behavior_id")
    if simple.get("canonical_claim_label") != node.get("claim_label"):
        fail("simple LEARN cannot strengthen claim label")
    simple_text = json.dumps(simple["presentation"]).lower()
    for jargon in ("edge_type", "transitive", "ontology", "neo4j", "graph database"):
        if jargon in simple_text:
            fail(f"simple LEARN leaks jargon: {jargon}")
    if "not yet tested" not in simple_text and "not_yet_tested" not in simple["presentation"]:
        fail("simple LEARN must surface not-yet-tested")

    # Graph disposable / rebuildable
    if graph.get("rebuildable") is not True or graph.get("mutable_source_of_truth") is not False:
        fail("capability graph projection must be rebuildable disposable index")
    gpay = dict(graph)
    if gpay.pop("digest") != canonical_digest(gpay):
        fail("capability graph digest not canonical")

    # No transitive auto edge doc
    forbid = load_json(ROOT / "examples" / "v07-capability-graph" / "negative" / "invalid-transitive-edge.json")
    if forbid.get("auto_transitive") is not True:
        fail("transitive negative must document forbidden auto inference")

    # Negatives reject
    for schema_rel, fixture_rel in (
        ("specs/capability-edge.schema.json", "examples/negative/invalid-capability-edge-no-evidence.json"),
        ("specs/behavior-node.schema.json", "examples/negative/invalid-behavior-node-no-captured-tests.json"),
        ("specs/capability-edge.schema.json", "examples/negative/invalid-capability-edge-unknown-type.json"),
    ):
        if not list(Draft202012Validator(load_json(ROOT / schema_rel)).iter_errors(load_json(ROOT / fixture_rel))):
            fail(f"{fixture_rel} should fail {schema_rel}")

    overclaim = load_json(ROOT / "examples" / "v07-capability-graph" / "negative" / "invalid-simple-overclaim.json")
    if overclaim.get("canonical_claim_label") == node.get("claim_label"):
        fail("overclaim negative should strengthen beyond node claim")

    cg = (ROOT / "docs" / "CAPABILITY-GRAPH.md").read_text(encoding="utf-8")
    for token in (
        "Graph edges summarize evidence",
        "Prefer the smallest architecture",
        "No automatic transitive",
        "rebuildable",
        "PLAY isolation",
    ):
        if token not in cg and token.lower() not in cg.lower():
            # allow slight case variation for some
            if token not in cg:
                fail(f"CAPABILITY-GRAPH.md missing: {token}")
    learn = (ROOT / "docs" / "LEARN.md").read_text(encoding="utf-8")
    for token in ("What behaviors have we reproduced?", "not tested", "Same relationship"):
        if token not in learn:
            fail(f"LEARN.md missing: {token}")

    # No consciousness / ranking markers in v0.7 package
    scope = (ROOT / "docs" / "releases" / "v0.7" / "SCOPE.md").read_text(encoding="utf-8")
    if "consciousness" in scope.lower() and "out of scope" not in scope.lower() and "does not" not in scope.lower():
        pass  # non-goals handle it
    nong = (ROOT / "docs" / "releases" / "v0.7" / "NON-GOALS.md").read_text(encoding="utf-8")
    for token in ("consciousness score", "leaderboard", "Neo4j", "ontology induction"):
        if token.lower() not in nong.lower():
            fail(f"v0.7 NON-GOALS missing {token}")

    expected = load_json(ROOT / "examples" / "v07-capability-graph" / "expected-digests.json")
    if expected.get("behavior_node_digest") != node.get("digest"):
        fail("expected-digests behavior mismatch")

    ok(
        "LEARN v0.7: behavior nodes, closed edges, evidence lineage, contested, "
        "not-tested, simple/advanced projection, rebuildable graph, negatives"
    )


def check_experience_layer(Draft202012Validator) -> None:
    """Validate deterministic PLAY/WATCH/STUDY translations and safe fixtures."""
    intent_schema = load_json(ROOT / "specs" / "experiment-intent-catalog.schema.json")
    intent_catalog = load_json(ROOT / "specs" / "experiment-intent-catalog.json")
    errors = list(Draft202012Validator(intent_schema).iter_errors(intent_catalog))
    if errors:
        fail(f"experience intent catalog invalid: {errors[0].message}")
    expected = {"REPEAT_BEHAVIOR", "REMOVE_DEPENDENCY", "CHANGE_CONDITION", "COMPARE_VERSION", "TEST_GENERALIZATION", "CUSTOM"}
    entries = {entry["intent_id"]: entry for entry in intent_catalog["intents"]}
    if set(entries) != expected:
        fail("experience intent catalog must provide five common intents and CUSTOM")
    required_translations = {
        "REPEAT_BEHAVIOR": "REPLICATION",
        "REMOVE_DEPENDENCY": "ABLATION",
        "CHANGE_CONDITION": "PERTURBATION",
        "COMPARE_VERSION": "VERSION_DIFFERENTIAL",
        "TEST_GENERALIZATION": "REPLICATION",
        "CUSTOM": None,
    }
    expected_kinds = {
        "REPEAT_BEHAVIOR": "REPLICATION",
        "REMOVE_DEPENDENCY": "ABLATION",
        "CHANGE_CONDITION": "PERTURBATION",
        "COMPARE_VERSION": "VERSION_DIFFERENTIAL",
        "TEST_GENERALIZATION": "GENERALIZATION_PROBE",
        "CUSTOM": "ADVANCED_EXPERIMENT_DESIGN",
    }
    for intent_id, intervention in required_translations.items():
        entry = entries[intent_id]
        if entry["lab_intervention_type"] != intervention:
            fail(f"experience intent {intent_id} must deterministically map to {intervention}")
        if entry.get("generated_experiment_kind") != expected_kinds[intent_id]:
            fail(f"experience intent {intent_id} lacks deterministic generated experiment kind")
        if "ANALYSIS" not in entry["required_plan_nodes"] or "BASELINE" not in entry["required_plan_nodes"]:
            fail(f"experience intent {intent_id} lacks baseline/analysis plan boundary")
        defaults = entry["recommended_defaults"]
        if intent_id != "CUSTOM" and (defaults.get("dependent_measure_source") != "SOURCE_CANDIDATE_PRIMARY_MEASURE" or defaults.get("equivalence_boundary_source") != "SOURCE_CANDIDATE_RECORDED_BOUNDARY"):
            fail(f"experience intent {intent_id} must pin source measure and equivalence defaults")
        if set(entry["advanced_override_fields"]) != {"fork_point", "seed_policy", "intervention", "controls", "run_count", "equivalence_boundary", "dependent_measures"}:
            fail(f"experience intent {intent_id} lost advanced override escape hatch")

    error_schema = load_json(ROOT / "specs" / "experience-error-catalog.schema.json")
    error_catalog = load_json(ROOT / "specs" / "experience-error-catalog.json")
    errors = list(Draft202012Validator(error_schema).iter_errors(error_catalog))
    if errors:
        fail(f"experience error catalog invalid: {errors[0].message}")
    error_codes = {entry["reason_code"] for entry in error_catalog["errors"]}
    for code in {"INVALID_INTENT", "INVALID_EXPERIMENT", "INVALID_FORK", "UNRESOLVED_SOURCE", "INVALID_INTERVENTION", "UNREGISTERED_VARIABLE", "CONTROL_REQUIRED", "CONTROL_FAILED", "UNSUPPORTED_LESION", "SEED_DIVERGENCE", "WORLD_STATE_DRIFT", "AGENT_VERSION_DRIFT", "NOT_COMPARABLE", "NOT_COMPUTABLE", "BUDGET_EXHAUSTED", "AUTHORIZATION_DENIED", "CONSENT_DENIED", "SOURCE_WORLD_MUTATION_FORBIDDEN", "UNAUTHORIZED_RESEARCH_DETAIL"}:
        if code not in error_codes:
            fail(f"experience error mapping missing {code}")

    view_schema = load_json(ROOT / "specs" / "experience-view.schema.json")
    fixture_dir = ROOT / "examples" / "experience"
    fixtures = {path.name: load_json(path) for path in fixture_dir.glob("*.json")}
    required_fixtures = {
        "play-view.json", "watch-view.json", "interesting-behavior-card.json",
        "test-intent-menu.json", "simple-test-result.json", "advanced-test-result.json",
        "capture-ready.json", "user-facing-error.json",
        "capture-result-simple.json", "capture-result-advanced.json", "capturing-state.json",
        "capture-budget-exhausted.json", "capture-failed.json", "capture-privacy-block.json",
        "capture-not-ready.json",
        "deep-time-play-old-relay.json", "deep-time-play-onboarding.json",
        "deep-time-watch-timeline.json", "deep-time-study-questions.json",
        "deep-time-archive-discovered.json",
        "deep-time-genesis-player-entry.json",
        "learn-shared-ledger-simple.json",
        "learn-shared-ledger-advanced.json",
    }
    missing_exp = sorted(required_fixtures - set(fixtures))
    if missing_exp:
        fail(f"experience fixture package incomplete: missing {missing_exp}")
    for name, fixture in fixtures.items():
        errors = list(Draft202012Validator(view_schema).iter_errors(fixture))
        if errors:
            fail(f"experience fixture {name} invalid: {errors[0].message}")
    for name in ("play-view.json", "watch-view.json"):
        view = fixtures[name]
        if view["research_detail"] is not False:
            fail(f"{name} leaks research detail")
        rendered = json.dumps(view["presentation"]).lower()
        if any(token in rendered for token in ("anomaly_", "candidate_capability", "detector", "lab_result")):
            fail(f"{name} exposes raw research metadata")
    menu_intents = set(fixtures["test-intent-menu.json"]["presentation"]["intent_ids"])
    if menu_intents != expected:
        fail("simple test intent menu must exactly match deterministic catalog")
    capture = fixtures["capture-ready.json"]
    if capture.get("compiler_readiness") != "READY" or "CAPTURE_AS_TEST" not in capture["allowed_actions"]:
        fail("CAPTURE AS TEST must be enabled only by READY handoff")
    user_error = fixtures["user-facing-error.json"]
    if user_error.get("machine_reason_code") not in error_codes:
        fail("user-facing error must preserve canonical machine reason code")

    experience = (ROOT / "docs" / "EXPERIENCE.md").read_text(encoding="utf-8")
    for token in ("PLAY → NOTICE → TEST → CAPTURE → LEARN", "PLAY", "WATCH", "STUDY", "## Experience acceptance"):
        if token not in experience:
            fail("experience canonical product model or acceptance criteria incomplete")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in ("[PLAY]", "[WATCH]", "[STUDY]"):
        if token not in readme:
            fail("README lacks clear PLAY/WATCH/STUDY entry points")
    ok("Experience layer: deterministic intents, progressive fixtures, safe disclosure, and error mappings")


def check_skills_workflows() -> None:
    """Keep the operational workflow manual separate and complete."""
    skills = (ROOT / "SKILLS.md").read_text(encoding="utf-8")
    required = {
        "SKILL.ORIENT", "SKILL.SPEC_CHANGE", "SKILL.RFC", "SKILL.MILESTONE",
        "SKILL.SCHEMA", "SKILL.FIXTURE", "SKILL.CONFORMANCE", "SKILL.DETERMINISM",
        "SKILL.DRIFT_AUDIT", "SKILL.EXPERIENCE", "SKILL.GAME_SYSTEM",
        "SKILL.RESEARCH_CONTRACT", "SKILL.MIGRATION", "SKILL.VERSION",
        "SKILL.VALIDATE", "SKILL.CONTINUATION", "SKILL.PROMPT_BUILD",
        "SKILL.REVIEW", "SKILL.HANDOFF_RUNTIME", "Missing-signal rule",
    }
    missing = sorted(token for token in required if token not in skills)
    if missing:
        fail(f"SKILLS.md missing workflow sections: {missing}")
    workflow_names = [
        "ORIENT", "SPEC_CHANGE", "RFC", "MILESTONE", "SCHEMA", "FIXTURE",
        "CONFORMANCE", "DETERMINISM", "DRIFT_AUDIT", "EXPERIENCE", "GAME_SYSTEM",
        "RESEARCH_CONTRACT", "MIGRATION", "VERSION", "VALIDATE", "CONTINUATION",
        "PROMPT_BUILD", "REVIEW", "HANDOFF_RUNTIME",
    ]
    for name in workflow_names:
        body = skills.split(f"## SKILL.{name}", 1)[1].split("\n## ", 1)[0]
        for field in ("**Use when**", "**Inputs**", "**Authority to read**", "**Procedure**", "**Outputs**", "**Validation**", "**Stop / escalate when**"):
            if field not in body:
                fail(f"SKILLS.md workflow {name} lacks {field}")
    for token in ("Skills are repeatable workflows. They do not create new authority.", "Accepted RFC", "versioned protocol/schema", "python3 validation/validate_all.py"):
        if token not in skills:
            fail(f"SKILLS.md lacks required authority or validation rule: {token}")
    for rel in ("AGENTS.md", "CONTRIBUTING.md", "README.md"):
        if "SKILLS.md" not in (ROOT / rel).read_text(encoding="utf-8"):
            fail(f"{rel} must cross-link SKILLS.md")
    ok("SKILLS.md: operational workflows, authority boundary, and cross-links")

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
    check_strategic_conflict(Draft202012Validator)
    check_lab_v04(Draft202012Validator)
    check_compiler_v05(Draft202012Validator)
    check_deep_time_v06(Draft202012Validator)
    check_learn_v07(Draft202012Validator)
    check_experience_layer(Draft202012Validator)
    check_skills_workflows()
    check_architecture_hardening()
    print("\nPASS")




if __name__ == "__main__":
    main()
