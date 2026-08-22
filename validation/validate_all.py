#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator."""

from __future__ import annotations

import hashlib
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
    "docs/AGENT-HARNESS.md",
    "docs/OFFICIAL-AGENT-CLIENT.md",
    "docs/AGENT-SEAL-S0.md",
    "docs/AGENT-ONLY-PLAYER-IDENTITY.md",
    "docs/ADMIN-LIVE-OPERATIONS.md",
    "docs/WORLD-OPERATIONS.md",
    "docs/PLAYER-LIFECYCLE.md",
    "docs/OPERATOR-INTERVENTIONS.md",
    "docs/INCIDENT-RECOVERY.md",
    "docs/PLAYER-ONBOARDING.md",
    "docs/COMMAND-DISCOVERY.md",
    "docs/FIRST-WORLD-OPERATIONS.md",
    "docs/FIRST-WORLD-SPEC-FREEZE.md",
    "docs/WORLD-SERVICES.md",
    "docs/OPERATOR-DIGESTS.md",
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
    "docs/MUD-DESIGN-CANON.md",
    "docs/GAME-COMPLETENESS-PLAN.md",
    "docs/COMPLEXITY-DOCTRINE.md",
    "docs/MASTERY-SPECIALIZATION.md",
    "docs/CONSTRUCTION.md",
    "docs/SOCIAL-MEMORY.md",
    "docs/INSTITUTIONAL-AUTHORITY.md",
    "docs/COMMUNICATION-ECOLOGY.md",
    "docs/SYSTEMIC-DISCOVERY.md",
    "docs/ECONOMIC-SPECIALIZATION.md",
    "docs/EMERGENT-CULTURE.md",
    "docs/WORLD-EVENT-DIRECTOR.md",
    "docs/NOTION-RECONCILIATION-2026-08-13.md",
    "docs/REDUCER-REGISTRY.md",
    "docs/GC1-FIRST-SLICE.md",
    "docs/GC1-S1-RECOGNITION.md",
    "docs/GC2-FIRST-SLICE.md",
    "rfcs/RFC-0006-construction-existing-events.md",
    "docs/GC3-FIRST-SLICE.md",
    "rfcs/RFC-0007-dyadic-trade-memory.md",
    "docs/GC4-FIRST-SLICE.md",
    "rfcs/RFC-0008-office-authority-pins.md",
    "docs/GC5-FIRST-SLICE.md",
    "rfcs/RFC-0009-relay-message-delivery.md",
    "docs/GC6-FIRST-SLICE.md",
    "rfcs/RFC-0010-discovery-contradiction.md",
    "docs/GC7-FIRST-SLICE.md",
    "rfcs/RFC-0011-contest-rhythm.md",
    "docs/GC8-FIRST-SLICE.md",
    "rfcs/RFC-0012-distance-interdependence.md",
    "docs/GC9-FIRST-SLICE.md",
    "rfcs/RFC-0013-maintenance-custom.md",
    "docs/GC10-FIRST-SLICE.md",
    "rfcs/RFC-0014-wed-schedule-pressure.md",
    "rfcs/RFC-0004-derived-mastery-projection.md",
    "rfcs/RFC-0005-mastery-recognition.md",
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
            "adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md",
            "adr/ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md",
            "adr/ADR-008-replay-conformance-and-deterministic-hardening.md",
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
        ("specs/mastery-catalog.schema.json", "specs/mastery-catalog.gc1-s0.json"),
        ("specs/mastery-catalog-s1.schema.json", "specs/mastery-catalog.gc1-s1.json"),
        ("specs/mastery-rebuild.schema.json", "examples/gc1-mastery/rebuild-positive.json"),
        ("specs/mastery-rebuild.schema.json", "examples/gc1-mastery/rebuild-negative.json"),
        ("specs/mastery-rebuild-s1.schema.json", "examples/gc1-mastery/rebuild-s1-recognized.json"),
        ("specs/mastery-rebuild-s1.schema.json", "examples/gc1-mastery/rebuild-s1-below-threshold.json"),
        ("specs/construction-catalog.schema.json", "specs/construction-catalog.gc2-s0.json"),
        ("specs/construction-attempt.schema.json", "examples/gc2-construction/construct-relay-ok.json"),
        ("specs/construction-attempt.schema.json", "examples/gc2-construction/dismantle-not-owner.json"),
        ("specs/social-memory-catalog.schema.json", "specs/social-memory-catalog.gc3-s0.json"),
        ("specs/social-memory-rebuild.schema.json", "examples/gc3-social-memory/rebuild-reliable.json"),
        ("specs/social-memory-rebuild.schema.json", "examples/gc3-social-memory/rebuild-rejects-ignored.json"),
        ("specs/authority-catalog.schema.json", "specs/authority-catalog.gc4-s0.json"),
        ("specs/authority-attempt.schema.json", "examples/gc4-authority/officer-add-member-ok.json"),
        ("specs/authority-attempt.schema.json", "examples/gc4-authority/member-add-forbidden.json"),
        ("specs/authority-attempt.schema.json", "examples/gc4-authority/steward-title-member-add-forbidden.json"),
        ("specs/communication-catalog.schema.json", "specs/communication-catalog.gc5-s0.json"),
        ("specs/communication-attempt.schema.json", "examples/gc5-communication/local-dead-relay-ok.json"),
        ("specs/communication-attempt.schema.json", "examples/gc5-communication/long-range-below-band-unreachable.json"),
        ("specs/communication-attempt.schema.json", "examples/gc5-communication/hidden-room-unreachable-no-leak.json"),
        ("specs/discovery-catalog.schema.json", "specs/discovery-catalog.gc6-s0.json"),
        ("specs/discovery-rebuild.schema.json", "examples/gc6-discovery/rebuild-relay-seven-open.json"),
        ("specs/discovery-rebuild.schema.json", "examples/gc6-discovery/rebuild-inspect-only.json"),
        ("specs/discovery-rebuild.schema.json", "examples/gc6-discovery/rebuild-agreeing.json"),
        ("specs/conflict-catalog.schema.json", "specs/conflict-catalog.gc7-s0.json"),
        ("specs/conflict-attempt.schema.json", "examples/gc7-conflict/rhythm-infra-ok.json"),
        ("specs/conflict-attempt.schema.json", "examples/gc7-conflict/attack-verb-forbidden.json"),
        ("specs/conflict-attempt.schema.json", "examples/gc7-conflict/death-forbidden.json"),
        ("specs/economy-catalog.schema.json", "specs/economy-catalog.gc8-s0.json"),
        ("specs/economy-attempt.schema.json", "examples/gc8-economy/pair-two-rooms-ok.json"),
        ("specs/economy-attempt.schema.json", "examples/gc8-economy/lone-one-hop-ok.json"),
        ("specs/economy-attempt.schema.json", "examples/gc8-economy/wallet-forbidden.json"),
        ("specs/culture-catalog.schema.json", "specs/culture-catalog.gc9-s0.json"),
        ("specs/culture-rebuild.schema.json", "examples/gc9-culture/rebuild-repair-custom.json"),
        ("specs/culture-rebuild.schema.json", "examples/gc9-culture/rebuild-lore-cannot-override.json"),
        ("specs/pressure-catalog.schema.json", "specs/pressure-catalog.gc10-s0.json"),
        ("specs/pressure-attempt.schema.json", "examples/gc10-pressure/schedule-mild-ok.json"),
        ("specs/pressure-attempt.schema.json", "examples/gc10-pressure/forced-response-forbidden.json"),
        ("specs/pressure-attempt.schema.json", "examples/gc10-pressure/frontier-id-forbidden.json"),
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
        ("specs/agent-bootstrap.schema.json", "examples/onboarding/agent-bootstrap.json"),
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

    bootstrap_schema = load_json(ROOT / "specs" / "agent-bootstrap.schema.json")
    bootstrap_v = Draft202012Validator(bootstrap_schema)
    bootstrap = load_json(ROOT / "examples" / "onboarding" / "agent-bootstrap.json")
    from datetime import datetime
    issued = datetime.fromisoformat(bootstrap["issued_at"].replace("Z", "+00:00"))
    expires = datetime.fromisoformat(bootstrap["expires_at"].replace("Z", "+00:00"))
    lifetime = (expires - issued).total_seconds()
    if not (0 < lifetime <= 900):
        fail("agent bootstrap fixture lifetime must be >0 and <=900 seconds")
    for name in (
        "invalid-agent-bootstrap-admin-scope.json",
        "invalid-agent-bootstrap-operator-session.json",
        "invalid-agent-bootstrap-integrity.json",
    ):
        bad = load_json(ROOT / "examples" / "negative" / name)
        if not list(bootstrap_v.iter_errors(bad)):
            fail(f"negative agent bootstrap fixture unexpectedly valid: {name}")

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

    c12 = load_json(ROOT / "conformance" / "v0.1" / "cases" / "C12-agent-onboarding.json")
    c12_actions = {step.get("action") for step in c12.get("steps") or []}
    required_bootstrap_actions = {
        "GET_ENROLLMENT_LINK",
        "APPROVE_DEVICE_ENROLLMENT",
        "REPLAY_ENROLLMENT_LINK",
        "USE_EXPIRED_ENROLLMENT",
        "USE_REPLACED_ENROLLMENT",
        "APPROVE_WRONG_BINDING",
        "DENY_DEVICE_ENROLLMENT",
        "INSTALL_OPTIONAL_SKILL",
        "DIRECT_PROTOCOL_ONBOARDING",
        "VALIDATE_BOOTSTRAP",
    }
    missing_bootstrap_actions = sorted(required_bootstrap_actions - c12_actions)
    if missing_bootstrap_actions:
        fail(f"C12 missing agent bootstrap actions: {missing_bootstrap_actions}")

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


def check_reducer_registry() -> None:
    text = (ROOT / "docs" / "REDUCER-REGISTRY.md").read_text(encoding="utf-8")
    types_01 = [
        "AGENT_ENTERED_WORLD",
        "AGENT_LEFT_WORLD",
        "MOVE",
        "MOVE_REJECTED",
        "LOOK",
        "INSPECT",
        "MESSAGE",
        "MESSAGE_DELIVERED",
        "TRADE_PROPOSED",
        "TRADE_ACCEPTED",
        "TRADE_REJECTED",
        "RESOURCE_TRANSFER",
        "ORG_CREATE",
        "ORG_MEMBER_ADD",
        "ORG_MEMBER_REMOVE",
        "ENTITY_CREATE",
        "ENTITY_DESTROY",
        "ENTITY_UPDATE",
        "WAIT",
        "BUDGET_CONSUMED",
        "BUDGET_EXCEEDED",
        "SITUATION_INJECTED",
        "NOISE_APPLIED",
        "OBSERVATION_GENERATED",
    ]
    types_02 = [
        "CONTEST_DECLARED",
        "CONTEST_RESOLVED",
        "CRIME_DETECTED",
        "ACCESS_RESTRICTED",
        "INFRASTRUCTURE_DISRUPTED",
        "AGREEMENT_FORMED",
        "AGREEMENT_BROKEN",
    ]
    missing = [t for t in types_01 + types_02 if f"`{t}`" not in text]
    if missing:
        fail(f"REDUCER-REGISTRY.md missing event types: {missing}")
    if "Rebuild from committed events" not in text:
        fail("REDUCER-REGISTRY.md must mark GC projections as rebuild-only")
    if "WED" not in text:
        fail("REDUCER-REGISTRY.md must separate SITUATION_INJECTED from WED")
    ok("Reducer registry lists 0.1/0.2 events and non-writer projections")


def check_rfc_0016() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0016-hosted-durable-world-head.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0016 must be Accepted")
    low = rfc.lower()
    for token in (
        "noema_world_heads",
        "restore",
        "unsettled",
        "genesis",
        "serializable",
    ):
        if token not in low:
            fail(f"RFC-0016 must pin hosted durable head ({token})")
    ok("RFC-0016 hosted durable world head: Accepted, restore-if-missing, no Genesis pack")


def check_rfc_0017() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0017-hosted-cycle-fence.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0017 must be Accepted")
    low = rfc.lower()
    for token in ("stale_head", "serializable", "revision", "genesis", "unsettled"):
        if token not in low:
            fail(f"RFC-0017 must pin fence recovery ({token})")
    ok("RFC-0017 hosted cycle fence: Accepted, STALE_HEAD, no Genesis")


def check_rfc_0019() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0019-hosted-world-time.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0019 must be Accepted")
    low = rfc.lower()
    for token in ("wait", "quorum", "present", "world.cycle", "genesis"):
        if token not in low:
            fail(f"RFC-0019 must pin hosted world-time ({token})")
    if "new verb" not in low and "no new player verb" not in low:
        fail("RFC-0019 must refuse a new Player verb")
    if "contest" not in low or "wed" not in low:
        fail("RFC-0019 must leave contest/WED unauthorized")
    ok("RFC-0019 hosted world-time: Accepted, WAIT quorum, no contest/WED")


def check_rfc_0020() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0020-archive-claim-attest.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0020 must be Accepted")
    low = rfc.lower()
    for token in ("attest", "inspect", "entity_update", "genesis"):
        if token not in low:
            fail(f"RFC-0020 must pin archive attestation ({token})")
    if "not a writer" not in low and "must not" not in low:
        fail("RFC-0020 must keep INSPECT from writing claims")
    if "help" not in low:
        fail("RFC-0020 must keep ATTEST out of Chamber help")
    order = (ROOT / "docs" / "GC-S1-ORDER.md").read_text(encoding="utf-8")
    if "gc1-s2" not in order.lower() or "defer" not in order.lower():
        fail("GC-S1 order must defer GC1-S2 benefits")
    closeout = (ROOT / "docs" / "GC-S0-CLOSEOUT-2026-08-13.md").read_text(encoding="utf-8")
    if "not a thaw" not in closeout.lower():
        fail("S0 closeout must not be a thaw")
    ok("RFC-0020 archive ATTEST: Accepted, INSPECT not a writer")


def check_rfc_0018() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0018-archive-claim-writer.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0018 must be Accepted")
    low = rfc.lower()
    if "inspect" not in low or "must not mutate" not in low and "not a writer" not in low:
        fail("RFC-0018 must forbid INSPECT as archive-claim writer")
    if "entity_update" not in low or "entity_create" not in low:
        fail("RFC-0018 must name ENTITY_CREATE/UPDATE as sole writers")
    if "genesis" not in low:
        fail("RFC-0018 must reject a Genesis pack")
    ok("RFC-0018 archive-claim writer: Accepted, INSPECT not a writer")


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

def rebuild_gc1_s0(fixture: dict, catalog: dict) -> dict:
    player_id = fixture["player_id"]
    trades = fixture.get("trades") or {}
    tracks = {
        t["track_id"]: {"state": "UNTRACKED", "count": 0, "units": set(), "recognition_units": set()}
        for t in catalog["tracks"]
    }
    seen_event_ids: dict[str, set[str]] = {tid: set() for tid in tracks}

    def credit(track_id: str, event_id: str, unit: str, recognition_unit: str | None = None) -> None:
        if event_id in seen_event_ids[track_id]:
            return
        seen_event_ids[track_id].add(event_id)
        bucket = tracks[track_id]
        if unit not in bucket["units"]:
            bucket["units"].add(unit)
            bucket["count"] += 1
            bucket["state"] = "PRACTICING"
        if recognition_unit:
            bucket["recognition_units"].add(recognition_unit)

    def payload_player(payload: dict) -> str | None:
        for key in ("agent_id", "player_id"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value
        return None

    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        event_type = ev.get("event_type")
        event_id = ev.get("event_id")
        payload = ev.get("payload") or {}
        actor_id = ev.get("actor_id")
        if not event_id:
            continue
        if event_type == "LOOK":
            if payload_player(payload) == player_id and payload.get("room_id"):
                room = str(payload["room_id"])
                credit("track.explorer.01", event_id, room, room)
        elif event_type == "INSPECT":
            if payload_player(payload) == player_id and payload.get("entity_id"):
                entity = str(payload["entity_id"])
                credit("track.surveyor.01", event_id, entity, entity)
        elif event_type == "TRADE_ACCEPTED":
            trade_id = payload.get("trade_id")
            trade = trades.get(trade_id) if isinstance(trade_id, str) else None
            if not trade:
                continue
            parties = {trade.get("proposer_id"), trade.get("counterparty_id"), payload.get("accepted_by")}
            if player_id in parties:
                credit("track.broker.01", event_id, str(trade_id), str(trade_id))
        elif event_type == "ENTITY_UPDATE":
            if actor_id != player_id:
                continue
            sett = payload.get("set") if isinstance(payload.get("set"), dict) else {}
            if "condition" in sett:
                entity = payload.get("entity_id")
                recog = str(entity) if isinstance(entity, str) and entity else None
                credit("track.engineer.01", event_id, event_id, recog)

    track_meta = {t["track_id"]: t for t in catalog["tracks"]}
    if catalog.get("recognition_enabled"):
        for tid, rec in tracks.items():
            threshold = int(track_meta[tid].get("recognition_threshold") or 0)
            if rec["count"] >= 1 and len(rec["recognition_units"]) >= threshold > 0:
                rec["state"] = "RECOGNIZED"

    by_order = sorted(catalog["tracks"], key=lambda t: int(t["display_order"]))
    play_lines: list[str] = []
    recognized = [t for t in by_order if tracks[t["track_id"]]["state"] == "RECOGNIZED"]
    practicing = [t for t in by_order if tracks[t["track_id"]]["state"] == "PRACTICING"]
    for track in recognized + practicing:
        rec = tracks[track["track_id"]]
        if rec["state"] == "RECOGNIZED":
            play_lines.append(track.get("recognized_play_line") or track["play_line"])
        else:
            play_lines.append(track["play_line"])
        if len(play_lines) >= int(catalog["max_play_lines"]):
            break
    out_tracks = {}
    for tid, rec in tracks.items():
        row = {"state": rec["state"], "count": rec["count"]}
        if catalog.get("recognition_enabled"):
            row["recognition_count"] = len(rec["recognition_units"])
        out_tracks[tid] = row
    return {"tracks": out_tracks, "play_lines": play_lines}


def check_gc1_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "mastery-rebuild.schema.json")
    case_schema = load_json(ROOT / "specs" / "conformance-case.schema.json")
    catalog_errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if catalog_errs:
        fail(f"mastery catalog invalid: {catalog_errs[0].message}")
    if catalog.get("recognition_enabled") or catalog.get("decay_enabled") or catalog.get("benefits_enabled"):
        fail("GC1-S0 catalog must disable recognition, decay, and benefits")

    manifest = load_json(ROOT / "conformance" / "gc1-s0" / "manifest.json")
    cases = manifest.get("cases") or []
    if len(cases) < 4:
        fail(f"GC1-S0 conformance must list ≥4 cases, found {len(cases)}")
    case_v = Draft202012Validator(case_schema)
    fams: set[str] = set()
    for rel in cases:
        path = ROOT / "conformance" / "gc1-s0" / rel
        if not path.exists():
            fail(f"GC1-S0 missing case: {rel}")
        case = load_json(path)
        errs = list(case_v.iter_errors(case))
        if errs:
            fail(f"GC1-S0 case {rel} invalid: {errs[0].message}")
        if case.get("family_id"):
            fams.add(case["family_id"])
        for fixture in case.get("fixtures") or []:
            if not (ROOT / fixture).exists():
                fail(f"GC1-S0 case {rel} missing fixture {fixture}")
    if {"M01", "M02", "M03"} - fams:
        fail(f"GC1-S0 missing families: {sorted({'M01', 'M02', 'M03'} - fams)}")

    rfc = (ROOT / "rfcs" / "RFC-0004-derived-mastery-projection.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc:
        fail("RFC-0004 must be Accepted after GC1-S0 machine contracts land")

    rebuild_v = Draft202012Validator(rebuild_schema)
    for name in ("rebuild-positive.json", "rebuild-negative.json"):
        fixture = load_json(ROOT / "examples" / "gc1-mastery" / name)
        errs = list(rebuild_v.iter_errors(fixture))
        if errs:
            fail(f"{name} invalid: {errs[0].message}")
        got = rebuild_gc1_s0(fixture, catalog)
        expected = fixture["expected"]
        for track_id in (
            "track.explorer.01",
            "track.surveyor.01",
            "track.broker.01",
            "track.engineer.01",
        ):
            if got["tracks"][track_id] != expected[track_id]:
                fail(f"{name} {track_id}: got {got['tracks'][track_id]} expected {expected[track_id]}")
        if got["play_lines"] != expected["play_lines"]:
            fail(f"{name} play_lines: got {got['play_lines']} expected {expected['play_lines']}")
        if len(got["play_lines"]) > int(catalog["max_play_lines"]):
            fail(f"{name} exceeded max_play_lines")
    if "You have been keeping infrastructure alive." in load_json(
        ROOT / "examples" / "gc1-mastery" / "rebuild-positive.json"
    )["expected"]["play_lines"]:
        fail("positive fixture must omit the fourth display_order line")
    ok("GC1-S0 mastery: catalog, rebuild fixtures, M01–M03, RFC-0004 Accepted")


def check_gc1_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog-s1.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "mastery-rebuild-s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S1 catalog invalid: {errs[0].message}")
    if not catalog.get("recognition_enabled"):
        fail("GC1-S1 catalog must enable recognition")
    if catalog.get("decay_enabled") or catalog.get("benefits_enabled"):
        fail("GC1-S1 catalog must disable decay and benefits")
    rfc = (ROOT / "rfcs" / "RFC-0005-mastery-recognition.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:200]:
        fail("RFC-0005 must be Accepted after GC1-S1 machine contracts land")
    rebuild_v = Draft202012Validator(rebuild_schema)
    for name in ("rebuild-s1-recognized.json", "rebuild-s1-below-threshold.json"):
        fixture = load_json(ROOT / "examples" / "gc1-mastery" / name)
        ferrs = list(rebuild_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = rebuild_gc1_s0(fixture, catalog)
        expected = fixture["expected"]
        for track_id in (
            "track.explorer.01",
            "track.surveyor.01",
            "track.broker.01",
            "track.engineer.01",
        ):
            if got["tracks"][track_id] != expected[track_id]:
                fail(f"{name} {track_id}: got {got['tracks'][track_id]} expected {expected[track_id]}")
        if got["play_lines"] != expected["play_lines"]:
            fail(f"{name} play_lines: got {got['play_lines']} expected {expected['play_lines']}")
    spam = load_json(ROOT / "examples" / "gc1-mastery" / "rebuild-s1-below-threshold.json")
    if spam["expected"]["track.engineer.01"]["state"] != "PRACTICING":
        fail("same-entity repair spam must stay PRACTICING")
    if spam["expected"]["track.engineer.01"]["recognition_count"] != 1:
        fail("same-entity repair spam must have recognition_count 1")
    rec = load_json(ROOT / "examples" / "gc1-mastery" / "rebuild-s1-recognized.json")
    if "You have been" in " ".join(rec["expected"]["play_lines"]):
        fail("recognized fixture must use recognized lines, not practicing lines")
    ok("GC1-S1 mastery: catalog, recognition fixtures, RFC-0005 Accepted")


def evaluate_gc1_s2(attempt: dict, catalog: dict) -> dict:
    base = int(catalog["repair_base"])
    bonus = int(catalog["repeat_bonus"]) if attempt.get("recognized") and attempt.get("prior_on_asset") else 0
    delta = base + bonus
    cap = int(catalog["condition_cap"])
    after = min(cap, int(attempt["condition_before"]) + delta)
    return {"delta": delta, "condition_after": after}


def check_gc1_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S2 catalog invalid: {errs[0].message}")
    if not catalog.get("benefits_enabled") or catalog.get("watch_titles") or catalog.get("decay_enabled") or catalog.get("new_verbs"):
        fail("GC1-S2 must enable the engineer bonus only: no watch titles, decay, or new verbs")
    if catalog.get("repeat_bonus") != 5 or catalog.get("repair_base") != 15:
        fail("GC1-S2 magnitudes must be base 15 + bonus 5")
    rfc = (ROOT / "rfcs" / "RFC-0040-engineer-quality.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0040 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-repeat-bonus.json",
        "attempt-first-asset.json",
        "attempt-unrecognized.json",
        "attempt-cap.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s2" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc1_s2(fixture, catalog)
        exp = fixture["expected"]
        if got["delta"] != exp["delta"] or got["condition_after"] != exp["condition_after"]:
            fail(f"{name}: got {got} expected {exp}")
    ok("GC1-S2 engineer quality: catalog, attempt fixtures, RFC-0040 Accepted")


def evaluate_gc1_s3(attempt: dict, catalog: dict) -> dict:
    latent_after = int(catalog["latent_after_cycles"])
    rehab_need = int(catalog["rehab_works"])
    recognized = bool(attempt.get("recognized"))
    prior = bool(attempt.get("prior_on_asset"))
    idle = int(attempt.get("idle_cycles") or 0)
    rehab = int(attempt.get("rehab_works") or 0)
    latent = bool(recognized and idle >= latent_after and rehab < rehab_need)
    bonus = int(catalog["repeat_bonus"]) if recognized and prior and not latent else 0
    return {"latent": latent, "delta": int(catalog["repair_base"]) + bonus}


def check_gc1_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S3 catalog invalid: {errs[0].message}")
    if not catalog.get("decay_enabled") or catalog.get("watch_titles") or catalog.get("new_verbs"):
        fail("GC1-S3 must enable decay only: no watch titles or new verbs")
    if catalog.get("latent_after_cycles") != 12 or catalog.get("rehab_works") != 3:
        fail("GC1-S3 pins must be latent_after_cycles=12 and rehab_works=3")
    if catalog.get("repeat_bonus") != 5 or catalog.get("repair_base") != 15:
        fail("GC1-S3 magnitudes must stay base 15 + bonus 5")
    rfc = (ROOT / "rfcs" / "RFC-0043-mastery-decay.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0043 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S3-DECAY.md").read_text(encoding="utf-8")
    if "You were known for keeping infrastructure alive." not in slice_doc:
        fail("GC1-S3 must pin the Engineer LATENT PLAY line")
    for banned in ("Wipe evidence", "Bonus while LATENT", "1-work restore", "WATCH"):
        if banned == "WATCH" and "WATCH “was Engineer”" not in slice_doc and "WATCH" not in rfc:
            fail("GC1-S3 must reject WATCH titles")
    if "Wipe evidence" not in slice_doc and "Wipe evidence" not in rfc:
        fail("GC1-S3 must reject wiping evidence")
    if "1-work restore" not in slice_doc and "1-work restore" not in rfc:
        fail("GC1-S3 must reject 1-work restore")
    if "Bonus while LATENT" not in slice_doc and "bonus while LATENT" not in rfc.lower() and "Bonus while LATENT" not in rfc:
        fail("GC1-S3 must reject bonus while LATENT")
    if '"SPECIALIZATION_' in (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8"):
        fail("event-catalog/0.2 must not grow SPECIALIZATION_*")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-idle-latent.json",
        "attempt-short-idle.json",
        "attempt-rehab.json",
        "attempt-unrecognized.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s3" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc1_s3(fixture, catalog)
        exp = fixture["expected"]
        if got["latent"] != exp["latent"] or got["delta"] != exp["delta"]:
            fail(f"{name}: got {got} expected latent={exp['latent']} delta={exp['delta']}")
    ok("GC1-S3 mastery decay: catalog, attempt fixtures, RFC-0043 Accepted")


def evaluate_gc1_s4(attempt: dict, catalog: dict) -> dict:
    rec = bool(attempt.get("recognized") and attempt.get("maintained"))
    prior = bool(attempt.get("prior_work"))
    track = attempt.get("track")
    if track == "track.explorer.01":
        attention = int(catalog["repeat_look_attention"]) if rec and prior else int(catalog["look_attention"])
        return {"attention": attention, "caution_extra": 0}
    if track == "track.surveyor.01":
        attention = (
            int(catalog["repeat_inspect_attention"]) if rec and prior else int(catalog["inspect_attention"])
        )
        return {"attention": attention, "caution_extra": 0}
    caution = 0
    if attempt.get("hostile") and not (rec and prior and catalog.get("broker_waives_caution")):
        caution = 1
    return {"attention": 0, "caution_extra": caution}


def check_gc1_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s4.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S4 catalog invalid: {errs[0].message}")
    if catalog.get("watch_titles") or catalog.get("new_verbs") or catalog.get("class_discount") or catalog.get("seal_bypass"):
        fail("GC1-S4 must not add titles, verbs, class discounts, or seal bypass")
    rfc = (ROOT / "rfcs" / "RFC-0044-prior-work-benefits.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0044 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S4-PRIOR-WORK.md").read_text(encoding="utf-8")
    if "WATCH titles" not in slice_doc or "Class discount" not in slice_doc:
        fail("GC1-S4 must reject WATCH titles and class discounts")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-explorer-repeat.json",
        "attempt-explorer-first.json",
        "attempt-surveyor-repeat.json",
        "attempt-broker-prior.json",
        "attempt-broker-stranger.json",
        "attempt-latent.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s4" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc1_s4(fixture, catalog)
        exp = fixture["expected"]
        if got["attention"] != exp["attention"] or got["caution_extra"] != exp["caution_extra"]:
            fail(f"{name}: got {got} expected {exp}")
    ok("GC1-S4 prior-work benefits: catalog, attempt fixtures, RFC-0044 Accepted")


def evaluate_gc1_s5(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    required = attempt.get("requires_track")
    if not required:
        return "ACCEPT", None
    allowed = list(catalog.get("tracks") or [])
    if required not in allowed:
        return "REJECT", "invalid"
    if not attempt.get("recognized") or attempt.get("track") != required:
        return "REJECT", "ineligible"
    return "ACCEPT", None


def check_gc1_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s5.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S5 catalog invalid: {errs[0].message}")
    if catalog.get("watch_titles") or catalog.get("new_verbs") or catalog.get("class_discount") or catalog.get("evict_on_latent"):
        fail("GC1-S5 must not add titles, verbs, class discounts, or evict-on-latent")
    if not catalog.get("latent_eligible"):
        fail("GC1-S5 must keep LATENT recognition eligible")
    rfc = (ROOT / "rfcs" / "RFC-0055-office-eligibility.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0055 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S5-OFFICE-ELIGIBILITY.md").read_text(encoding="utf-8")
    if "WATCH titles" not in slice_doc or "Class discount" not in slice_doc:
        fail("GC1-S5 must reject WATCH titles and class discounts")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-engineer-ok.json",
        "attempt-unrecognized-reject.json",
        "attempt-broker-ok.json",
        "attempt-unrestricted.json",
        "attempt-latent-ok.json",
        "attempt-wrong-track.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s5" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_gc1_s5(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("GC1-S5 office eligibility: catalog, attempt fixtures, RFC-0055 Accepted")


TRACK_DISPLAY_ORDER = ("explorer", "surveyor", "broker", "engineer")


def evaluate_gc1_s6(attempt: dict, catalog: dict) -> tuple[str, str | None, str | None]:
    if attempt.get("hidden_room"):
        return "REJECT", "HIDDEN_ROOM", None
    if attempt.get("viewer") == "self":
        return "REJECT", "SELF_ONLY", None
    source = list(attempt.get("tracks") or ([attempt["track"]] if attempt.get("track") else []))
    recognized: set[str] = set(attempt.get("recognized_tracks") or [])
    if attempt.get("recognized") and attempt.get("track"):
        recognized.add(attempt["track"])
    latent: set[str] = set(attempt.get("latent_tracks") or [])
    if attempt.get("latent") and attempt.get("track"):
        latent.add(attempt["track"])
    picked = None
    for track in TRACK_DISPLAY_ORDER:
        if track not in source:
            continue
        if track not in recognized:
            continue
        if track in latent:
            continue
        picked = track
        break
    if not picked:
        if recognized and recognized <= latent:
            return "REJECT", "LATENT", None
        if any(t in latent for t in source if t in recognized):
            return "REJECT", "LATENT", None
        return "REJECT", "UNRECOGNIZED", None
    lines = catalog.get("public_lines") or {}
    template = lines.get(picked)
    if not isinstance(template, str):
        return "REJECT", "UNRECOGNIZED", None
    handle = attempt.get("handle") or "sable"
    return "ACCEPT", None, template.replace("{handle}", handle)


def check_gc1_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s6.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s6.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S6 catalog invalid: {errs[0].message}")
    if not catalog.get("watch_titles"):
        fail("GC1-S6 must enable watch_titles")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("class_discount"):
        fail("GC1-S6 must not add verbs, events, or class discounts")
    if catalog.get("latent_public") or catalog.get("hidden_room_titles") or catalog.get("practice_counts_public"):
        fail("GC1-S6 must withhold LATENT, hidden-room, and practice-count titles")
    if catalog.get("public_title_cap") != 1 or not catalog.get("self_practice_unchanged"):
        fail("GC1-S6 must cap public titles at 1 and leave self practice unchanged")
    rfc = (ROOT / "rfcs" / "RFC-0105-public-titles.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0105 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S6-PUBLIC-TITLES.md").read_text(encoding="utf-8")
    if "LATENT" not in slice_doc or "Hidden rooms" not in slice_doc or "Cap" not in slice_doc:
        fail("GC1-S6 must pin LATENT withhold, hidden rooms, and cap 1")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-surveyor-public.json",
        "attempt-latent-withheld.json",
        "attempt-hidden-room.json",
        "attempt-unrecognized.json",
        "attempt-explorer-public.json",
        "attempt-watch-same.json",
        "attempt-cap-one.json",
        "attempt-self-unchanged.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s6" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, line = evaluate_gc1_s6(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("line") and line != exp["line"]:
            fail(f"{name}: line {line} expected {exp['line']}")
    ok("GC1-S6 public titles: catalog, attempt fixtures, RFC-0105 Accepted")


def evaluate_gc1_s7(attempt: dict, catalog: dict) -> tuple[str, str | None, str | None]:
    if attempt.get("operation") == "FOCUS_CLEAR":
        return "ACCEPT", None, None
    track = attempt.get("track")
    if track not in (catalog.get("tracks") or []):
        return "REJECT", "INVALID", None
    viewer = attempt.get("viewer") or "self"
    if attempt.get("hidden_room") and viewer != "self":
        return "REJECT", "HIDDEN_ROOM", None
    if attempt.get("latent") and viewer != "self":
        return "REJECT", "LATENT", None
    if viewer == "self":
        return "ACCEPT", None, (catalog.get("self_lines") or {}).get(track)
    handle = attempt.get("handle") or "sable"
    template = (catalog.get("public_lines") or {}).get(track)
    if not isinstance(template, str):
        return "REJECT", "INVALID", None
    return "ACCEPT", None, template.replace("{handle}", handle)


def check_gc1_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s7.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s7.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s7.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S7 catalog invalid: {errs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("focus_declared_event"):
        fail("GC1-S7 must not add verbs, events, or FOCUS_DECLARED")
    if catalog.get("decay_window_change") or catalog.get("recognition_required") or catalog.get("focus_cap") != 1:
        fail("GC1-S7 must keep decay unchanged, recognition optional, and cap 1")
    rfc = (ROOT / "rfcs" / "RFC-0110-focus-declaration.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0110 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S7-FOCUS.md").read_text(encoding="utf-8")
    if "FOCUS_DECLARED" not in slice_doc or "LATENT" not in slice_doc:
        fail("GC1-S7 must reject FOCUS_DECLARED and pin LATENT withhold")
    help_doc = (ROOT / "docs" / "GC1-S7-FOCUS.md").read_text(encoding="utf-8")
    if "WED" not in help_doc or "ATTEST" not in help_doc:
        fail("GC1-S7 must keep WED / ATTEST omitted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-self-surveyor.json",
        "attempt-public-ok.json",
        "attempt-clear.json",
        "attempt-latent-withheld.json",
        "attempt-hidden-withheld.json",
        "attempt-watch-ok.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s7" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, line = evaluate_gc1_s7(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("line") and line != exp["line"]:
            fail(f"{name}: line {line} expected {exp['line']}")
    ok("GC1-S7 focus declaration: catalog, attempt fixtures, RFC-0110 Accepted")


def evaluate_gc1_s8(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None, int | None, str | None]:
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("class_discount"):
        return "REJECT", "CATALOG", None, None, None
    if catalog.get("parameter") != "extent" or catalog.get("overhaul_track") != "engineer":
        return "REJECT", "CATALOG", None, None, None
    extra_e = int(catalog["overhaul_energy_extra"])
    extra_c = int(catalog["overhaul_condition_extra"])
    extent = attempt.get("extent") or "standard"
    if extent == "standard":
        return "ACCEPT", None, 0, 0, None
    if extent != "overhaul":
        return "REJECT", "INVALID", None, None, None
    if attempt.get("track") != "engineer" or not attempt.get("recognized"):
        return "REJECT", "LOCKED", None, None, None
    if attempt.get("latent"):
        return "REJECT", "LATENT", None, None, None
    if int(attempt.get("energy") or 0) < extra_e:
        return "REJECT", "BUDGET", None, None, None
    label = attempt.get("label") or "it"
    line = str(catalog.get("success_line") or "").replace("{label}", label)
    return "ACCEPT", None, extra_e, extra_c, line


def check_gc1_s8(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "mastery-catalog.gc1-s8.json")
    catalog_schema = load_json(ROOT / "specs" / "mastery-catalog.gc1-s8.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "mastery-attempt.gc1-s8.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC1-S8 catalog invalid: {errs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("class_discount"):
        fail("GC1-S8 must not add verbs, events, or class discounts")
    if catalog.get("overhaul_energy_extra") != 1 or catalog.get("overhaul_condition_extra") != 5:
        fail("GC1-S8 must pin overhaul extras +1 energy / +5 condition")
    rfc = (ROOT / "rfcs" / "RFC-0112-parameter-access.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0112 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC1-S8-PARAMETER-ACCESS.md").read_text(encoding="utf-8")
    if "overhaul" not in slice_doc.lower() or "LATENT" not in slice_doc or "WED" not in slice_doc:
        fail("GC1-S8 must pin overhaul, LATENT lock, and WED omit")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-overhaul-engineer.json",
        "attempt-standard-anyone.json",
        "attempt-overhaul-unrecognized.json",
        "attempt-overhaul-latent.json",
        "attempt-overhaul-surveyor.json",
        "attempt-overhaul-budget.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc1-s8" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra_e, extra_c, line = evaluate_gc1_s8(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("extra_energy") is not None and extra_e != exp["extra_energy"]:
            fail(f"{name}: extra_energy {extra_e} expected {exp['extra_energy']}")
        if exp.get("extra_condition") is not None and extra_c != exp["extra_condition"]:
            fail(f"{name}: extra_condition {extra_c} expected {exp['extra_condition']}")
        if exp.get("line") and line != exp["line"]:
            fail(f"{name}: line {line} expected {exp['line']}")
    ok("GC1-S8 parameter access: catalog, attempt fixtures, RFC-0112 Accepted")


def evaluate_hosted_mp_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if attempt.get("live_chat") or attempt.get("split_stock") or attempt.get("cycle_freeze"):
        return "REJECT", "DOCTRINE"
    if attempt.get("new_verb"):
        return "REJECT", "NEW_VERB"
    stock = int(attempt.get("stock") or 0)
    first = int(attempt.get("first_amount") or 0)
    second = int(attempt.get("second_amount") or 0)
    miss = catalog.get("miss_line") or "Not enough stock available."
    if first < 1 or first > stock:
        return "REJECT", "FIRST_INVALID"
    remaining = stock - first
    if second > remaining:
        attempt["_miss_line"] = miss
        return "REJECT", "NOT_ENOUGH_STOCK"
    return "ACCEPT", None


def check_hosted_mp_s0(Draft202012Validator) -> None:
    catalog_path = ROOT / "specs" / "hosted-mp-catalog.s0.json"
    if not catalog_path.exists():
        fail("hosted-mp-catalog.s0.json missing")
    catalog = load_json(catalog_path)
    catalog_schema = load_json(ROOT / "specs" / "hosted-mp-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "hosted-mp-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"hosted-mp catalog invalid: {errs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("live_chat"):
        fail("hosted-mp must not add verbs, events, or live chat")
    if catalog.get("resolution") != "first_accepted":
        fail("hosted-mp resolution must be first_accepted")
    if catalog.get("miss_line") != "Not enough stock available.":
        fail("hosted-mp must pin miss_line")
    if catalog.get("watch_amounts"):
        fail("hosted-mp must forbid WATCH amounts")
    rfc = (ROOT / "rfcs" / "RFC-0113-hosted-multiplayer-contention.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0113 must be Accepted")
    slice_doc = (ROOT / "docs" / "HOSTED-MP-CONTENTION.md").read_text(encoding="utf-8")
    if "first-accepted" not in slice_doc.lower() or "MESSAGE" not in slice_doc or "live chat" not in slice_doc.lower():
        fail("HOSTED-MP-CONTENTION must pin first-accepted, MESSAGE, and reject live chat")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-first-ok.json",
        "attempt-second-empty.json",
        "attempt-split.json",
        "attempt-live-chat.json",
        "attempt-new-verb.json",
    ):
        fixture = load_json(ROOT / "examples" / "hosted-mp-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_hosted_mp_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("hosted-mp S0: catalog, fixtures, RFC-0113 Accepted")


def evaluate_gc2_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    classes = {c["class_id"]: c for c in catalog["classes"]}
    op = attempt.get("operation")
    actor_room = attempt.get("actor_room_id") or attempt.get("room_id")
    if attempt.get("hidden_room"):
        return "REJECT", "NOT_OBSERVABLE"
    if actor_room != attempt.get("room_id"):
        return "REJECT", "NOT_COLOCATED"
    budgets = attempt.get("budgets") or {}
    if op == "CONSTRUCT":
        class_id = attempt.get("class_id")
        spec = classes.get(class_id)
        if not spec:
            return "REJECT", "CLASS_FORBIDDEN"
        if class_id in (attempt.get("live_classes_in_room") or []):
            return "REJECT", "SLOT_OCCUPIED"
        cost = spec["construct_cost"]
        for key, need in cost.items():
            if int(budgets.get(key) or 0) < int(need):
                return "REJECT", "BUDGET_EXCEEDED"
        return "ACCEPT", None
    if op == "DISMANTLE":
        target = attempt.get("target") or {}
        if not target.get("live"):
            return "REJECT", "NOT_FOUND"
        if target.get("owner_id") != attempt.get("actor_id"):
            return "REJECT", "NOT_OWNER"
        spec = classes.get(target.get("class_id") or "")
        if not spec:
            return "REJECT", "CLASS_FORBIDDEN"
        cost = spec["dismantle_cost"]
        for key, need in cost.items():
            if int(budgets.get(key) or 0) < int(need):
                return "REJECT", "BUDGET_EXCEEDED"
        return "ACCEPT", None
    return "REJECT", "CLASS_FORBIDDEN"


def check_gc2_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC2-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("benefits_enabled"):
        fail("GC2-S0 must not enable mastery/build benefits")
    if catalog.get("event_catalog") != "event-catalog/0.1":
        fail("GC2-S0 must reuse event-catalog/0.1")
    forbidden_events = {"STRUCTURE_CONSTRUCTED", "STRUCTURE_DISMANTLED"}
    used = set(catalog.get("construct_events") or []) | set(catalog.get("dismantle_events") or [])
    if used & forbidden_events:
        fail("GC2-S0 must not introduce STRUCTURE_* events")
    for cls in catalog["classes"]:
        if len(cls.get("couples") or []) < 2:
            fail(f"{cls['class_id']} must couple at least two systems")
    rfc = (ROOT / "rfcs" / "RFC-0006-construction-existing-events.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0006 must be Accepted after GC2-S0 machine contracts land")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "construct-relay-ok.json",
        "construct-slot-occupied.json",
        "construct-budget-exceeded.json",
        "construct-hidden-room.json",
        "dismantle-owner-ok.json",
        "dismantle-not-owner.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc2-construction" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc2_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
    ok("GC2-S0 construction: catalog, attempt fixtures, RFC-0006 Accepted, no STRUCTURE_* events")


def evaluate_gc2_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", None
        if attempt.get("class_id") != catalog.get("class_id"):
            return "REJECT", "class", None
        return "ACCEPT", None, None
    storage = int(attempt.get("storage") or 0)
    extra = 1 if storage < 16 else 0
    if attempt.get("has_route_link") and catalog.get("effect") == "waive_cargo_move":
        extra = 0
    return "ACCEPT", None, 1 + extra


def check_gc2_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S1 catalog invalid: {errs[0].message}")
    if catalog.get("new_exit") or catalog.get("watch_routes") or catalog.get("help_build") or catalog.get("new_verbs"):
        fail("GC2-S1 must not add exits, WATCH routes, help BUILD, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0049-route-link.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0049 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S1-ROUTE-LINK.md").read_text(encoding="utf-8")
    if "route_link" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S1 must keep route_link cargo-only and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-ok.json",
        "attempt-hidden-reject.json",
        "attempt-cargo-waived.json",
        "attempt-cargo-still.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-route-link" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, energy = evaluate_gc2_s1(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("move_energy") is not None and energy != exp["move_energy"]:
            fail(f"{name}: energy {energy} expected {exp['move_energy']}")
    ok("GC2-S1 route_link: catalog, attempt fixtures, RFC-0049 Accepted")


def evaluate_gc2_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_construct"):
        return "REJECT", "hidden", None
    if attempt.get("operation") == "CONSTRUCT" and attempt.get("class_id") == catalog.get("class_id") and not attempt.get("has_workshop"):
        return "ACCEPT", None, int(attempt.get("base_storage") or 0)
    base = int(attempt.get("base_storage") or 0)
    discount = int(catalog.get("storage_discount") or 0) if attempt.get("has_workshop") else 0
    return "ACCEPT", None, max(0, base - discount)


def check_gc2_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S2 catalog invalid: {errs[0].message}")
    if catalog.get("recipes") or catalog.get("mastery_discount") or catalog.get("help_build") or catalog.get("new_verbs"):
        fail("GC2-S2 must not add recipes, mastery discounts, help BUILD, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0050-workshop.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0050 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S2-WORKSHOP.md").read_text(encoding="utf-8")
    if "workshop" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S2 must keep workshop in-room and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-ok.json",
        "attempt-hidden-reject.json",
        "attempt-construct-discount.json",
        "attempt-repair-discount.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-workshop" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, storage = evaluate_gc2_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("storage_cost") is not None and storage != exp["storage_cost"]:
            fail(f"{name}: storage {storage} expected {exp['storage_cost']}")
    ok("GC2-S2 workshop: catalog, attempt fixtures, RFC-0050 Accepted")


def evaluate_gc2_s3(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", None
        if attempt.get("class_id") != catalog.get("class_id"):
            return "REJECT", "class", None
        return "ACCEPT", None, None
    base = int(attempt.get("base_score") or 0)
    bonus = int(catalog.get("defense_bonus_millipoints") or 0) if attempt.get("has_defensive_work") else 0
    return "ACCEPT", None, base - bonus


def check_gc2_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S3 catalog invalid: {errs[0].message}")
    if catalog.get("hit_points") or catalog.get("new_contest_form") or catalog.get("help_build") or catalog.get("new_verbs"):
        fail("GC2-S3 must not add HP, a new contest form, help BUILD, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0052-defensive-work.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0052 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S3-DEFENSIVE-WORK.md").read_text(encoding="utf-8")
    if "defensive_work" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S3 must keep defensive_work in-room and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-ok.json",
        "attempt-hidden-reject.json",
        "attempt-score-bonus.json",
        "attempt-score-plain.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-defensive" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, score = evaluate_gc2_s3(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("score") is not None and score != exp["score"]:
            fail(f"{name}: score {score} expected {exp['score']}")
    ok("GC2-S3 defensive_work: catalog, attempt fixtures, RFC-0052 Accepted")


def evaluate_gc2_s4(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", None
        if attempt.get("class_id") != catalog.get("class_id"):
            return "REJECT", "class", None
        return "ACCEPT", None, None
    base = int(attempt.get("base_attention") or 0)
    discount = int(catalog.get("attention_discount") or 0) if attempt.get("has_annex") else 0
    return "ACCEPT", None, max(0, base - discount)


def check_gc2_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s4.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S4 catalog invalid: {errs[0].message}")
    if catalog.get("quest") or catalog.get("oracle") or catalog.get("help_build") or catalog.get("new_verbs"):
        fail("GC2-S4 must not add QUEST, an oracle, help BUILD, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0053-archive-annex.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0053 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S4-ARCHIVE-ANNEX.md").read_text(encoding="utf-8")
    if "archive_annex" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S4 must keep annex in-room and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-ok.json",
        "attempt-hidden-reject.json",
        "attempt-inspect-discount.json",
        "attempt-attest-discount.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-annex" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, attention = evaluate_gc2_s4(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("attention_cost") is not None and attention != exp["attention_cost"]:
            fail(f"{name}: attention {attention} expected {exp['attention_cost']}")
    ok("GC2-S4 archive_annex: catalog, attempt fixtures, RFC-0053 Accepted")


def evaluate_gc2_s5(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    op = attempt.get("operation")
    if op == "UPGRADE":
        if attempt.get("room_hidden") or catalog.get("hidden_upgrade"):
            return "REJECT", "hidden", None
        if attempt.get("class_id") != catalog.get("class_id"):
            return "REJECT", "class", None
        if attempt.get("already_upgraded"):
            return "REJECT", "tier", None
        if attempt.get("owned") is False:
            return "REJECT", "owner", None
        return "ACCEPT", None, None
    base = int(attempt.get("base_storage") or 0)
    discount = int(catalog.get("storage_discount") or 0) if attempt.get("has_upgraded_workshop") else 0
    return "ACCEPT", None, max(0, base - discount)


def check_gc2_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s5.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S5 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_upgrade"):
        fail("GC2-S5 must not add help BUILD, new verbs, or WATCH upgrade")
    rfc = (ROOT / "rfcs" / "RFC-0056-workshop-upgrade.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0056 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S5-UPGRADE.md").read_text(encoding="utf-8")
    if "UPGRADE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S5 must keep UPGRADE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-upgrade-ok.json",
        "attempt-hidden-reject.json",
        "attempt-other-class.json",
        "attempt-second-reject.json",
        "attempt-construct-discount.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-upgrade" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, storage = evaluate_gc2_s5(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("storage_cost") is not None and storage != exp["storage_cost"]:
            fail(f"{name}: storage {storage} expected {exp['storage_cost']}")
    ok("GC2-S5 workshop UPGRADE: catalog, attempt fixtures, RFC-0056 Accepted")


def evaluate_gc2_s6(attempt: dict, catalog: dict) -> tuple[str, str | None, str | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_repurpose"):
        return "REJECT", "hidden", None
    if attempt.get("from_class") != catalog.get("from_class") or attempt.get("to_class") != catalog.get("to_class"):
        return "REJECT", "conversion", None
    if attempt.get("owned") is False:
        return "REJECT", "owner", None
    entity_id = attempt.get("entity_id")
    if catalog.get("keep_entity_id") is False:
        return "REJECT", "identity", None
    return "ACCEPT", None, entity_id


def check_gc2_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s6.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s6.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S6 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_repurpose"):
        fail("GC2-S6 must not add help BUILD, new verbs, or WATCH repurpose")
    if catalog.get("other_conversions") or catalog.get("from_class") != "workshop" or catalog.get("to_class") != "storage_bay":
        fail("GC2-S6 conversion table is workshop → storage_bay only")
    if not catalog.get("keep_entity_id"):
        fail("GC2-S6 must keep the same entity_id")
    cost = catalog.get("repurpose_cost") or {}
    if cost != {"energy": 4, "compute": 2, "storage": 2, "influence": 1}:
        fail("GC2-S6 cost must be energy 4 compute 2 storage 2 influence 1")
    rfc = (ROOT / "rfcs" / "RFC-0057-workshop-repurpose.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0057 must be Accepted")
    if "STRUCTURE_REPURPOSED" in rfc.split("## Proposed change", 1)[-1][:800] and "No `STRUCTURE_*`" not in rfc:
        fail("RFC-0057 must not add STRUCTURE_REPURPOSED")
    slice_doc = (ROOT / "docs" / "GC2-S6-REPURPOSE.md").read_text(encoding="utf-8")
    if "REPURPOSE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S6 must keep REPURPOSE on BUILD and WATCH silent")
    if "repurposed as a storage bay" not in slice_doc.lower() and "repurposed as a storage bay" not in rfc.lower():
        fail("GC2-S6 PLAY may say the workshop was repurposed as a storage bay")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-repurpose-ok.json",
        "attempt-hidden-reject.json",
        "attempt-other-conversion.json",
        "attempt-not-owner.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-repurpose" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, entity_id = evaluate_gc2_s6(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("entity_id") and entity_id != exp["entity_id"]:
            fail(f"{name}: entity_id {entity_id} expected {exp['entity_id']}")
    ok("GC2-S6 workshop REPURPOSE: catalog, attempt fixtures, RFC-0057 Accepted")


def evaluate_gc2_s7(attempt: dict, catalog: dict) -> tuple[str, str | None, bool]:
    if attempt.get("operation") == "DISMANTLE":
        if attempt.get("unclaimed") or attempt.get("actor_is_owner"):
            return "ACCEPT", None, True
        return "REJECT", "owner", False
    if attempt.get("room_hidden") or catalog.get("hidden_abandon"):
        return "REJECT", "hidden", False
    if attempt.get("owner_repaired"):
        return "REJECT", "reset", False
    idle = int(attempt.get("idle_cycles") or 0)
    need = int(catalog.get("idle_cycles") or 12)
    if idle < need:
        return "REJECT", "idle", False
    return "ACCEPT", None, True


def check_gc2_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s7.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s7.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s7.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S7 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_abandon") or catalog.get("scar_on_abandon") or catalog.get("evict_player"):
        fail("GC2-S7 must not add help BUILD, new verbs, WATCH, scar-on-abandon, or evict")
    rfc = (ROOT / "rfcs" / "RFC-0058-abandonment.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0058 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S7-ABANDON.md").read_text(encoding="utf-8")
    if "UNCLAIMED" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S7 must keep UNCLAIMED and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-abandon-ok.json",
        "attempt-short-idle.json",
        "attempt-hidden.json",
        "attempt-steward-repair.json",
        "attempt-dismantle-unclaimed.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-abandon" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, unclaimed = evaluate_gc2_s7(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("unclaimed") is not None and unclaimed != exp["unclaimed"]:
            fail(f"{name}: unclaimed {unclaimed} expected {exp['unclaimed']}")
    ok("GC2-S7 abandonment: catalog, attempt fixtures, RFC-0058 Accepted")


def evaluate_gc2_s8(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_restore"):
        return "REJECT", "hidden", None
    if attempt.get("scar") or catalog.get("scar_restore"):
        return "REJECT", "scar", None
    if not attempt.get("unclaimed"):
        return "REJECT", "claimed", None
    if attempt.get("owned") is False:
        return "REJECT", "owner", None
    cap = int(catalog.get("restore_condition_cap") or 50)
    current = int(attempt.get("condition") or 0)
    return "ACCEPT", None, min(current, cap)


def check_gc2_s8(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s8.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s8.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s8.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S8 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_restore") or catalog.get("scar_restore"):
        fail("GC2-S8 must not add help BUILD, new verbs, WATCH restore, or scar restore")
    rfc = (ROOT / "rfcs" / "RFC-0059-restore.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0059 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S8-RESTORE.md").read_text(encoding="utf-8")
    if "RESTORE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S8 must keep RESTORE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-restore-ok.json",
        "attempt-scar-reject.json",
        "attempt-not-owner.json",
        "attempt-not-unclaimed.json",
        "attempt-hidden.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-restore" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, cond = evaluate_gc2_s8(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("condition") is not None and cond != exp["condition"]:
            fail(f"{name}: condition {cond} expected {exp['condition']}")
    ok("GC2-S8 RESTORE: catalog, attempt fixtures, RFC-0059 Accepted")


def evaluate_gc2_s9(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("operation") == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if attempt.get("operation") == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s9(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s9.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s9.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s9.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S9 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_progress") or catalog.get("scar_on_progress_dismantle"):
        fail("GC2-S9 must not add help BUILD, new verbs, WATCH progress, or scar on in-progress dismantle")
    rfc = (ROOT / "rfcs" / "RFC-0061-multicycle-construct.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0061 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S9-MULTICYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S9 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-multicycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s9(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
    ok("GC2-S9 multi-cycle relay: catalog, attempt fixtures, RFC-0061 Accepted")


def evaluate_gc2_s10(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_vest"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    if attempt.get("office_occupied") is False:
        return "REJECT", "unauthorized", extra
    if attempt.get("unclaimed"):
        return "REJECT", "not_vestable", extra
    extra["same_entity"] = True
    extra["owner"] = "institution"
    return "ACCEPT", None, extra


def check_gc2_s10(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s10.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s10.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s10.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S10 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_vest") or catalog.get("institution_as_player") or catalog.get("shared"):
        fail("GC2-S10 must not add help BUILD, new verbs, WATCH vest, institution-as-Player, or SHARED")
    rfc = (ROOT / "rfcs" / "RFC-0067-institution-own.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0067 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S10-INSTITUTION.md").read_text(encoding="utf-8")
    if "VEST" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S10 must keep VEST on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-vest-ok.json",
        "attempt-hidden-reject.json",
        "attempt-vacant-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-institution" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s10(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("owner") and extra.get("owner") != exp["owner"]:
            fail(f"{name}: owner {extra.get('owner')} expected {exp['owner']}")
    ok("GC2-S10 institution-owned: catalog, attempt fixtures, RFC-0067 Accepted")


def evaluate_gc2_s11(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    if attempt.get("already_shared"):
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = int(catalog.get("max_co_owners") or 1)
    return "ACCEPT", None, extra


def check_gc2_s11(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s11.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s11.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s11.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S11 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_share") or catalog.get("institution_as_player") or catalog.get("share_institution"):
        fail("GC2-S11 must not add help BUILD, new verbs, WATCH share, institution-as-Player, or institution SHARE")
    if catalog.get("max_co_owners") != 1:
        fail("GC2-S11 must keep one co-owner")
    rfc = (ROOT / "rfcs" / "RFC-0068-shared-own.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0068 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S11-SHARED.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S11 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-share-ok.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
        "attempt-already-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-shared" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s11(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S11 shared ownership: catalog, attempt fixtures, RFC-0068 Accepted")


def evaluate_gc2_s12(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"new_exit": False}
    if attempt.get("room_hidden") or attempt.get("dest_hidden") or catalog.get("hidden_dest") or attempt.get("public_pair") is False:
        return "REJECT", "not_observable", extra
    if attempt.get("steward") is False:
        return "REJECT", "not_owner", extra
    extra["same_entity"] = True
    return "ACCEPT", None, extra


def check_gc2_s12(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s12.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s12.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s12.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S12 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_connect") or catalog.get("new_exits") or catalog.get("leak_topology"):
        fail("GC2-S12 must not add help BUILD, new verbs, WATCH connect, new exits, or topology leak")
    rfc = (ROOT / "rfcs" / "RFC-0071-connect-dest.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0071 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S12-CONNECT.md").read_text(encoding="utf-8")
    if "CONNECT" not in slice_doc or "NOT_OBSERVABLE" not in slice_doc:
        fail("GC2-S12 must keep CONNECT dest pin and NOT_OBSERVABLE")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-connect-ok.json",
        "attempt-hidden-dest-reject.json",
        "attempt-one-way-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-connect" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s12(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("new_exit") is not None and extra.get("new_exit") != exp["new_exit"]:
            fail(f"{name}: new_exit {extra.get('new_exit')} expected {exp['new_exit']}")
    ok("GC2-S12 CONNECT dest pin: catalog, attempt fixtures, RFC-0071 Accepted")


def evaluate_gc2_s13(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op in ("UPGRADE", "REPURPOSE"):
        if attempt.get("in_progress") or (
            op == "UPGRADE" and catalog.get("upgrade_in_progress")
        ) or (
            op == "REPURPOSE" and catalog.get("repurpose_in_progress")
        ):
            return "REJECT", "in_progress", extra
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s13(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s13.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s13.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s13.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S13 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_progress")
        or catalog.get("scar_on_progress_dismantle")
        or catalog.get("upgrade_in_progress")
        or catalog.get("repurpose_in_progress")
    ):
        fail("GC2-S13 must not add help BUILD, new verbs, WATCH progress, scar on in-progress dismantle, or UPGRADE/REPURPOSE of a shell")
    rfc = (ROOT / "rfcs" / "RFC-0072-workshop-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0072 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S13-WORKSHOP-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S13 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
        "attempt-upgrade-progress-reject.json",
        "attempt-repurpose-progress-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-workshop-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s13(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
    ok("GC2-S13 workshop multi-cycle: catalog, attempt fixtures, RFC-0072 Accepted")


def evaluate_gc2_s14(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s14(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s14.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s14.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s14.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S14 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_progress") or catalog.get("scar_on_progress_dismantle"):
        fail("GC2-S14 must not add help BUILD, new verbs, WATCH progress, or scar on in-progress dismantle")
    rfc = (ROOT / "rfcs" / "RFC-0073-generator-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0073 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S14-GENERATOR-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S14 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-generator-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s14(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
    ok("GC2-S14 generator multi-cycle: catalog, attempt fixtures, RFC-0073 Accepted")


def evaluate_gc2_s15(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s15(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s15.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s15.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s15.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S15 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_progress")
        or catalog.get("scar_on_progress_dismantle")
        or catalog.get("repurpose_in_progress")
    ):
        fail("GC2-S15 must not add help BUILD, new verbs, WATCH progress, scar on in-progress dismantle, or REPURPOSE-as-shell")
    rfc = (ROOT / "rfcs" / "RFC-0074-storage-bay-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0074 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S15-STORAGE-BAY-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S15 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-storage-bay-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s15(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
    ok("GC2-S15 storage_bay multi-cycle: catalog, attempt fixtures, RFC-0074 Accepted")


def evaluate_gc2_s16(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s16(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s16.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s16.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s16.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S16 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_progress") or catalog.get("scar_on_progress_dismantle"):
        fail("GC2-S16 must not add help BUILD, new verbs, WATCH progress, or scar on in-progress dismantle")
    rfc = (ROOT / "rfcs" / "RFC-0075-production-node-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0075 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S16-PRODUCTION-NODE-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S16 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-production-node-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s16(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
    ok("GC2-S16 production_node multi-cycle: catalog, attempt fixtures, RFC-0075 Accepted")


def evaluate_gc2_s17(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "CONTEST":
        extra["contest_bonus"] = (not attempt.get("in_progress")) and (not catalog.get("contest_bonus_in_progress"))
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s17(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s17.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s17.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s17.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S17 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_progress")
        or catalog.get("scar_on_progress_dismantle")
        or catalog.get("contest_bonus_in_progress")
    ):
        fail("GC2-S17 must not add help BUILD, new verbs, WATCH progress, scar on in-progress dismantle, or contest bonus on a shell")
    rfc = (ROOT / "rfcs" / "RFC-0076-defensive-work-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0076 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S17-DEFENSIVE-WORK-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S17 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
        "attempt-contest-shell.json",
        "attempt-contest-live.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-defensive-work-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s17(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
        if exp.get("contest_bonus") is not None and extra.get("contest_bonus") != exp["contest_bonus"]:
            fail(f"{name}: contest_bonus {extra.get('contest_bonus')} expected {exp['contest_bonus']}")
    ok("GC2-S17 defensive_work multi-cycle: catalog, attempt fixtures, RFC-0076 Accepted")


def evaluate_gc2_s18(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "INSPECT":
        extra["attention_discount"] = (not attempt.get("in_progress")) and (not catalog.get("discount_in_progress"))
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s18(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s18.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s18.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s18.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S18 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_progress")
        or catalog.get("scar_on_progress_dismantle")
        or catalog.get("discount_in_progress")
    ):
        fail("GC2-S18 must not add help BUILD, new verbs, WATCH progress, scar on in-progress dismantle, or attention discount on a shell")
    rfc = (ROOT / "rfcs" / "RFC-0077-archive-annex-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0077 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S18-ARCHIVE-ANNEX-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S18 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
        "attempt-inspect-shell.json",
        "attempt-inspect-live.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-archive-annex-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s18(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
        if exp.get("attention_discount") is not None and extra.get("attention_discount") != exp["attention_discount"]:
            fail(f"{name}: attention_discount {extra.get('attention_discount')} expected {exp['attention_discount']}")
    ok("GC2-S18 archive_annex multi-cycle: catalog, attempt fixtures, RFC-0077 Accepted")


def evaluate_gc2_s19(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"new_exit": False}
    op = attempt.get("operation")
    if op == "CONSTRUCT":
        if attempt.get("room_hidden") or catalog.get("hidden_construct"):
            return "REJECT", "hidden", extra
        extra["in_progress"] = True
        extra["live"] = False
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "PROMOTE":
        extra["in_progress"] = False
        extra["live"] = True
        extra["same_entity"] = True
        return "ACCEPT", None, extra
    if op == "MOVE":
        extra["cargo_waiver"] = (not attempt.get("in_progress")) and (not catalog.get("waiver_in_progress"))
        return "ACCEPT", None, extra
    extra["live"] = False
    extra["scar"] = False
    return "ACCEPT", None, extra


def check_gc2_s19(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s19.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s19.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s19.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S19 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_progress")
        or catalog.get("scar_on_progress_dismantle")
        or catalog.get("waiver_in_progress")
        or catalog.get("new_exits")
    ):
        fail("GC2-S19 must not add help BUILD, new verbs, WATCH progress, scar on in-progress dismantle, cargo waiver on a shell, or new exits")
    rfc = (ROOT / "rfcs" / "RFC-0078-route-link-cycle.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0078 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S19-ROUTE-LINK-CYCLE.md").read_text(encoding="utf-8")
    if "IN_PROGRESS" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S19 must keep IN_PROGRESS on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-construct-progress.json",
        "attempt-promote-ok.json",
        "attempt-hidden-reject.json",
        "attempt-dismantle-progress.json",
        "attempt-move-shell.json",
        "attempt-move-live.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-route-link-cycle" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s19(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("in_progress") is not None and extra.get("in_progress") != exp["in_progress"]:
            fail(f"{name}: in_progress {extra.get('in_progress')} expected {exp['in_progress']}")
        if exp.get("live") is not None and extra.get("live") != exp["live"]:
            fail(f"{name}: live {extra.get('live')} expected {exp['live']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("scar") is not None and extra.get("scar") != exp["scar"]:
            fail(f"{name}: scar {extra.get('scar')} expected {exp['scar']}")
        if exp.get("cargo_waiver") is not None and extra.get("cargo_waiver") != exp["cargo_waiver"]:
            fail(f"{name}: cargo_waiver {extra.get('cargo_waiver')} expected {exp['cargo_waiver']}")
        if exp.get("new_exit") is not None and extra.get("new_exit") != exp["new_exit"]:
            fail(f"{name}: new_exit {extra.get('new_exit')} expected {exp['new_exit']}")
    ok("GC2-S19 route_link multi-cycle: catalog, attempt fixtures, RFC-0078 Accepted")


def evaluate_gc2_s20(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    current = int(attempt.get("current_co_owners") or 0)
    cap = int(catalog.get("max_co_owners") or 2)
    if current >= cap:
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = current + 1
    return "ACCEPT", None, extra


def check_gc2_s20(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s20.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s20.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s20.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S20 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_share") or catalog.get("institution_as_player") or catalog.get("share_institution"):
        fail("GC2-S20 must not add help BUILD, new verbs, WATCH share, institution-as-Player, or institution SHARE")
    if catalog.get("max_co_owners") != 2:
        fail("GC2-S20 must keep two co-owners")
    rfc = (ROOT / "rfcs" / "RFC-0079-second-co-owner.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0079 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S20-SECOND-CO-OWNER.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S20 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-second-ok.json",
        "attempt-third-reject.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-second-co-owner" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s20(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S20 second co-owner: catalog, attempt fixtures, RFC-0079 Accepted")


def evaluate_gc2_s21(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    current = int(attempt.get("current_co_owners") or 0)
    cap = int(catalog.get("max_co_owners") or 3)
    if current >= cap:
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = current + 1
    return "ACCEPT", None, extra


def check_gc2_s21(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s21.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s21.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s21.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S21 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_share") or catalog.get("institution_as_player") or catalog.get("share_institution"):
        fail("GC2-S21 must not add help BUILD, new verbs, WATCH share, institution-as-Player, or institution SHARE")
    if catalog.get("max_co_owners") != 3:
        fail("GC2-S21 must keep three co-owners")
    rfc = (ROOT / "rfcs" / "RFC-0085-third-co-owner.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0085 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S21-THIRD-CO-OWNER.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S21 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-third-ok.json",
        "attempt-fourth-reject.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-third-co-owner" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s21(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S21 third co-owner: catalog, attempt fixtures, RFC-0085 Accepted")


def evaluate_gc2_s22(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    current = int(attempt.get("current_co_owners") or 0)
    cap = int(catalog.get("max_co_owners") or 4)
    if current >= cap:
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = current + 1
    return "ACCEPT", None, extra


def check_gc2_s22(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s22.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s22.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s22.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S22 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_share") or catalog.get("institution_as_player") or catalog.get("share_institution"):
        fail("GC2-S22 must not add help BUILD, new verbs, WATCH share, institution-as-Player, or institution SHARE")
    if catalog.get("max_co_owners") != 4:
        fail("GC2-S22 must keep four co-owners")
    rfc = (ROOT / "rfcs" / "RFC-0086-fourth-co-owner.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0086 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S22-FOURTH-CO-OWNER.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S22 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-fourth-ok.json",
        "attempt-fifth-reject.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-fourth-co-owner" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s22(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S22 fourth co-owner: catalog, attempt fixtures, RFC-0086 Accepted")


def evaluate_gc2_s23(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    current = int(attempt.get("current_co_owners") or 0)
    cap = int(catalog.get("max_co_owners") or 5)
    if current >= cap:
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = current + 1
    return "ACCEPT", None, extra


def check_gc2_s23(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s23.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s23.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s23.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S23 catalog invalid: {errs[0].message}")
    if catalog.get("help_build") or catalog.get("new_verbs") or catalog.get("watch_share") or catalog.get("institution_as_player") or catalog.get("share_institution"):
        fail("GC2-S23 must not add help BUILD, new verbs, WATCH share, institution-as-Player, or institution SHARE")
    if catalog.get("max_co_owners") != 5:
        fail("GC2-S23 must keep five co-owners")
    rfc = (ROOT / "rfcs" / "RFC-0087-fifth-co-owner.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0087 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S23-FIFTH-CO-OWNER.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S23 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-fifth-ok.json",
        "attempt-sixth-reject.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-fifth-co-owner" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s23(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("same_entity") is not None and extra.get("same_entity") != exp["same_entity"]:
            fail(f"{name}: same_entity mismatch")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S23 fifth co-owner: catalog, attempt fixtures, RFC-0087 Accepted")


def evaluate_gc2_s24(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("operation") == "CLOSEOUT":
        extra["co_owners"] = int(catalog.get("max_co_owners") or 5)
        return "ACCEPT", None, extra
    if attempt.get("room_hidden") or catalog.get("hidden_share"):
        return "REJECT", "hidden", extra
    if attempt.get("personal_owner") is False:
        return "REJECT", "not_owner", extra
    current = int(attempt.get("current_co_owners") or 0)
    cap = int(catalog.get("max_co_owners") or 5)
    if current >= cap:
        return "REJECT", "already_shared", extra
    extra["same_entity"] = True
    extra["co_owners"] = current + 1
    return "ACCEPT", None, extra


def check_gc2_s24(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-s24.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-s24.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-s24.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2-S24 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_build")
        or catalog.get("new_verbs")
        or catalog.get("watch_share")
        or catalog.get("institution_as_player")
        or catalog.get("share_institution")
        or catalog.get("roster")
        or catalog.get("sixth_stamp")
        or not catalog.get("family_closed")
    ):
        fail("GC2-S24 must close SHARE at five, reject roster/sixth stamp, and keep help BUILD off")
    if catalog.get("max_co_owners") != 5:
        fail("GC2-S24 must keep five co-owners")
    rfc = (ROOT / "rfcs" / "RFC-0089-share-closeout.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0089 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC2-S24-SHARE-CLOSEOUT.md").read_text(encoding="utf-8")
    if "SHARE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC2-S24 must keep SHARE on BUILD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-closeout-ok.json",
        "attempt-sixth-reject.json",
        "attempt-hidden-reject.json",
        "attempt-stranger-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-share-closeout" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc2_s24(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("co_owners") is not None and extra.get("co_owners") != exp["co_owners"]:
            fail(f"{name}: co_owners {extra.get('co_owners')} expected {exp['co_owners']}")
    ok("GC2-S24 SHARE closeout: catalog, attempt fixtures, RFC-0089 Accepted")


def evaluate_wr_s0(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if attempt.get("room_hidden"):
        return "ACCEPT", None, 0
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", None, 0
    return "ACCEPT", None, 1


def check_wr_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S0 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_news")
        or catalog.get("watch_report")
        or catalog.get("new_verbs")
        or catalog.get("your_position")
        or catalog.get("later_sections")
    ):
        fail("WR-S0 must not add help news, WATCH report, YOUR POSITION, later sections, or new verbs")
    if catalog.get("interval_cycles") != 5 or catalog.get("retention") != 1:
        fail("WR-S0 must keep last-1 report every 5 cycles")
    rfc = (ROOT / "rfcs" / "RFC-0088-world-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0088 must be Accepted")
    slice_doc = (ROOT / "docs" / "WR-S0-WORLD-REPORT.md").read_text(encoding="utf-8")
    if "report_lines" not in slice_doc or "WATCH" not in slice_doc:
        fail("WR-S0 must keep report_lines on PLAY and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-interval-ok.json",
        "attempt-before-interval.json",
        "attempt-hidden-omit.json",
        "attempt-same-cycle.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s0-world-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_wr_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("WR-S0 public world report: catalog, attempt fixtures, RFC-0088 Accepted")


def evaluate_gc2_thaw_play(attempt: dict, catalog: dict) -> tuple[str, bool | None]:
    if attempt.get("operation") == "HELP_BUILD":
        return "ACCEPT", True if catalog.get("help_build") else False
    listed = False
    if attempt.get("topic") == "contest":
        listed = bool(catalog.get("help_contest"))
    elif attempt.get("topic") == "attest":
        listed = bool(catalog.get("help_attest"))
    return "ACCEPT", listed


def check_gc2_thaw_play(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "construction-catalog.gc2-thaw-play.json")
    catalog_schema = load_json(ROOT / "specs" / "construction-catalog.gc2-thaw-play.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "construction-attempt.gc2-thaw-play.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC2 thaw-play catalog invalid: {errs[0].message}")
    if not catalog.get("help_build") or catalog.get("help_contest") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs"):
        fail("GC2 thaw-play must list BUILD help and omit CONTEST/WED/ATTEST and new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0090-build-play-thaw.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0090 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-help-build.json",
        "attempt-help-commands.json",
        "attempt-omit-contest.json",
        "attempt-omit-attest.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc2-thaw-play" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, listed = evaluate_gc2_thaw_play(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("GC2 PLAY thaw: catalog, attempt fixtures, RFC-0090 Accepted")


def evaluate_wr_s1(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    org_lines = 1 if attempt.get("org_active") else 0
    return "ACCEPT", 1, org_lines


def check_wr_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S1 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("watch_report") or catalog.get("new_verbs") or catalog.get("your_position"):
        fail("WR-S1 must not add help news, WATCH report, YOUR POSITION, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0091-org-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0091 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-org-ok.json",
        "attempt-no-org.json",
        "attempt-before-interval.json",
        "attempt-hidden-omit.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s1-org-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, org_lines = evaluate_wr_s1(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("org_lines") is not None and org_lines != exp["org_lines"]:
            fail(f"{name}: org_lines {org_lines} expected {exp['org_lines']}")
    ok("WR-S1 organization report: catalog, attempt fixtures, RFC-0091 Accepted")


def evaluate_wr_s2(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    contest_lines = 1 if attempt.get("contest_open_public") else 0
    return "ACCEPT", 1, contest_lines


def check_wr_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S2 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("help_contest") or catalog.get("watch_report") or catalog.get("new_verbs"):
        fail("WR-S2 must not add help news, help CONTEST, WATCH report, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0092-contest-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0092 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-contest-ok.json",
        "attempt-hidden-omit.json",
        "attempt-no-contest.json",
        "attempt-before-interval.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s2-contest-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, contest_lines = evaluate_wr_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("contest_lines") is not None and contest_lines != exp["contest_lines"]:
            fail(f"{name}: contest_lines {contest_lines} expected {exp['contest_lines']}")
    ok("WR-S2 public contest report: catalog, attempt fixtures, RFC-0092 Accepted")


def evaluate_wr_s3(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    access_lines = 1 if attempt.get("restriction_live_public") else 0
    return "ACCEPT", 1, access_lines


def check_wr_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S3 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("help_access_policy") or catalog.get("watch_report") or catalog.get("new_verbs"):
        fail("WR-S3 must not add help news, ACCESS_POLICY, WATCH report, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0093-access-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0093 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-access-ok.json",
        "attempt-hidden-omit.json",
        "attempt-expired-omit.json",
        "attempt-before-interval.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s3-access-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, access_lines = evaluate_wr_s3(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("access_lines") is not None and access_lines != exp["access_lines"]:
            fail(f"{name}: access_lines {access_lines} expected {exp['access_lines']}")
    ok("WR-S3 public access report: catalog, attempt fixtures, RFC-0093 Accepted")


def evaluate_wr_s4(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    crime_lines = 1 if attempt.get("crime_public") else 0
    return "ACCEPT", 1, crime_lines


def check_wr_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s4.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S4 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("help_crime") or catalog.get("watch_report") or catalog.get("new_verbs"):
        fail("WR-S4 must not add help news, CRIME help, WATCH report, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0094-crime-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0094 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-crime-ok.json",
        "attempt-hidden-omit.json",
        "attempt-private-omit.json",
        "attempt-before-interval.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s4-crime-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, crime_lines = evaluate_wr_s4(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("crime_lines") is not None and crime_lines != exp["crime_lines"]:
            fail(f"{name}: crime_lines {crime_lines} expected {exp['crime_lines']}")
    ok("WR-S4 public crime report: catalog, attempt fixtures, RFC-0094 Accepted")


def evaluate_wr_s5(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    discovery_lines = 1 if attempt.get("reconstruction_public") else 0
    return "ACCEPT", 1, discovery_lines


def check_wr_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s5.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S5 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("help_quest") or catalog.get("watch_report") or catalog.get("new_verbs"):
        fail("WR-S5 must not add help news, QUEST, WATCH report, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0096-discovery-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0096 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-recon-ok.json",
        "attempt-hidden-omit.json",
        "attempt-private-omit.json",
        "attempt-before-interval.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s5-discovery-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, discovery_lines = evaluate_wr_s5(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("discovery_lines") is not None and discovery_lines != exp["discovery_lines"]:
            fail(f"{name}: discovery_lines {discovery_lines} expected {exp['discovery_lines']}")
    ok("WR-S5 public discovery report: catalog, attempt fixtures, RFC-0096 Accepted")


def evaluate_wr_s6(attempt: dict, catalog: dict) -> tuple[str, int | None, int | None]:
    interval = int(catalog.get("interval_cycles") or 5)
    cycles = int(attempt.get("committed_cycles") or 0)
    if cycles < interval or cycles % interval != 0:
        return "ACCEPT", 0, 0
    diplomacy_lines = 1 if attempt.get("agreement_active_public") else 0
    return "ACCEPT", 1, diplomacy_lines


def check_wr_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "world-report-catalog.wr-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "world-report-catalog.wr-s6.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "world-report-attempt.wr-s6.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"WR-S6 catalog invalid: {errs[0].message}")
    if catalog.get("help_news") or catalog.get("help_agreement") or catalog.get("watch_report") or catalog.get("new_verbs"):
        fail("WR-S6 must not add help news, AGREEMENT help, WATCH report, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0099-diplomacy-report.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0099 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-agree-ok.json",
        "attempt-offered-omit.json",
        "attempt-broken-omit.json",
        "attempt-before-interval.json",
    ):
        fixture = load_json(ROOT / "examples" / "wr-s6-diplomacy-report" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, kept, diplomacy_lines = evaluate_wr_s6(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
        if exp.get("diplomacy_lines") is not None and diplomacy_lines != exp["diplomacy_lines"]:
            fail(f"{name}: diplomacy_lines {diplomacy_lines} expected {exp['diplomacy_lines']}")
    ok("WR-S6 public diplomacy report: catalog, attempt fixtures, RFC-0099 Accepted")



def rebuild_gc3_s0(fixture: dict, catalog: dict) -> dict:
    subject = fixture["subject_id"]
    trades = fixture.get("trades") or {}
    handles = fixture.get("handles") or {}
    counts: dict[str, set[str]] = {}
    seen_events: set[str] = set()
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        if ev.get("event_type") != catalog["evidence_event"]:
            continue
        eid = ev.get("event_id")
        if not eid or eid in seen_events:
            continue
        seen_events.add(eid)
        payload = ev.get("payload") or {}
        trade_id = payload.get("trade_id")
        trade = trades.get(trade_id) if isinstance(trade_id, str) else None
        if not trade:
            continue
        parties = {trade.get("proposer_id"), trade.get("counterparty_id")}
        if subject not in parties:
            continue
        other = next((p for p in parties if p and p != subject), None)
        if not other:
            continue
        counts.setdefault(other, set()).add(str(trade_id))
    edges = {}
    play_lines = []
    traded_at = int(catalog["traded_threshold"])
    reliable_at = int(catalog["reliable_threshold"])
    for other, tids in sorted(counts.items()):
        n = len(tids)
        if n >= reliable_at:
            state = "RELIABLE"
            template = catalog["reliable_line"]
        elif n >= traded_at:
            state = "TRADED"
            template = catalog["traded_line"]
        else:
            state = "UNKNOWN"
            template = None
        edges[other] = {"state": state, "count": n}
        if template:
            name = handles.get(other) or other
            play_lines.append(template.replace("{name}", name))
    return {
        "edges": edges,
        "play_lines": play_lines,
        "watch_lines": [],
        "third_party_lines": [],
    }


def check_gc3_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("reputation_scalar") or catalog.get("public_projection") or catalog.get("watch_projection"):
        fail("GC3-S0 must not enable a reputation scalar or public/WATCH projection")
    if catalog.get("new_verbs"):
        fail("GC3-S0 must not add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0007-dyadic-trade-memory.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0007 must be Accepted after GC3-S0 machine contracts land")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in ("rebuild-reliable.json", "rebuild-rejects-ignored.json"):
        fixture = load_json(ROOT / "examples" / "gc3-social-memory" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s0(fixture, catalog)
        exp = fixture["expected"]
        if got["edges"] != exp["edges"]:
            fail(f"{name} edges: got {got['edges']} expected {exp['edges']}")
        if got["play_lines"] != exp["play_lines"]:
            fail(f"{name} play_lines: got {got['play_lines']} expected {exp['play_lines']}")
        if got["watch_lines"] or exp["watch_lines"]:
            fail(f"{name} WATCH must be empty")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} play line leaked {token}")
        if "72" in blob or "reputation" in blob:
            fail(f"{name} must not project a reputation scalar")
    ok("GC3-S0 social memory: catalog, rebuild fixtures, RFC-0007 Accepted, no reputation scalar")


def rebuild_gc3_s1(fixture: dict, catalog: dict) -> dict:
    subject = fixture["subject_id"]
    handles = fixture.get("handles") or {}
    danger: dict[str, set[str]] = {}
    seen: set[str] = set()
    allowed = set(catalog.get("evidence_events") or [])
    ignored = set(catalog.get("ignored_events") or [])
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        et = ev.get("event_type")
        if et in ignored or et not in allowed:
            continue
        payload = ev.get("payload") or {}
        evidence = None
        actor = None
        if et == "CONTEST_RESOLVED":
            evidence = payload.get("contest_id") or ev.get("event_id")
            declarer = payload.get("declarer_id")
            victims = [payload.get("defender_id")]
            target = payload.get("target") or {}
            if isinstance(target, dict) and target.get("kind") == "AGENT":
                victims.append(target.get("agent_id"))
            if subject in victims and declarer and declarer != subject:
                actor = declarer
        elif et == "AGREEMENT_BROKEN":
            evidence = payload.get("breach_id") or ev.get("event_id")
            broken = payload.get("broken_by")
            parties = payload.get("party_ids") or []
            if subject in parties and broken and broken != subject:
                actor = broken
        elif et == "CRIME_DETECTED":
            evidence = payload.get("detection_id") or ev.get("event_id")
            if subject == payload.get("victim_id") and payload.get("subject_id") not in (None, subject):
                actor = payload.get("subject_id")
        if not evidence or not actor or evidence in seen:
            continue
        seen.add(str(evidence))
        danger.setdefault(str(actor), set()).add(str(evidence))
    play_lines = []
    out_danger = {}
    thresh = int(catalog["danger_threshold"])
    template = catalog["danger_line"]
    for other, ids in sorted(danger.items()):
        n = len(ids)
        out_danger[other] = {"count": n}
        if n >= thresh:
            name = handles.get(other) or other
            play_lines.append(template.replace("{name}", name))
    return {
        "danger": out_danger,
        "play_lines": play_lines,
        "watch_lines": [],
        "third_party_lines": [],
    }


def check_gc3_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s1.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.gc3-s1.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("reputation_scalar") or catalog.get("public_projection") or catalog.get("watch_projection"):
        fail("GC3-S1 must not enable a reputation scalar or public/WATCH projection")
    if catalog.get("new_verbs"):
        fail("GC3-S1 must not add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0022-betrayal-dangerous.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0022 must be Accepted")
    if "trade_rejected" not in rfc.lower():
        fail("RFC-0022 must keep TRADE_REJECTED from becoming deceptive")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in ("rebuild-dangerous-contest.json", "rebuild-rejects-ignored.json"):
        fixture = load_json(ROOT / "examples" / "gc3-betrayal" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s1(fixture, catalog)
        exp = fixture["expected"]
        if got["danger"] != exp["danger"]:
            fail(f"{name}: danger {got['danger']} expected {exp['danger']}")
        if got["play_lines"] != exp["play_lines"]:
            fail(f"{name}: lines {got['play_lines']} expected {exp['play_lines']}")
        if got["watch_lines"] or got["third_party_lines"]:
            fail(f"{name}: WATCH/third-party must be empty")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} leaked {token}")
    ok("GC3-S1 betrayal: catalog, rebuild fixtures, RFC-0022 Accepted, no reputation scalar")


def _gc3_attest_contradictions(events: list) -> list[tuple[str, str]]:
    """Return (earlier_attester, later_event_id) for opposite public ATTEST pairs."""
    by_subject: dict[str, list] = {}
    for ev in events:
        if ev.get("event_type") != "ATTEST":
            continue
        payload = ev.get("payload") or {}
        if payload.get("visibility") != "PUBLIC":
            continue
        sid = payload.get("subject_entity_id")
        if sid:
            by_subject.setdefault(str(sid), []).append(ev)
    out: list[tuple[str, str]] = []
    for group in by_subject.values():
        ordered = sorted(
            group,
            key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
        )
        for i, later in enumerate(ordered):
            later_claim = (later.get("payload") or {}).get("archive_claim")
            later_id = later.get("event_id")
            if not later_claim or not later_id:
                continue
            for earlier in ordered[:i]:
                early_claim = (earlier.get("payload") or {}).get("archive_claim")
                attester = (earlier.get("payload") or {}).get("attester_id")
                if attester and early_claim and early_claim != later_claim:
                    out.append((str(attester), str(later_id)))
                    break
    return out


def rebuild_gc3_s2(fixture: dict, catalog: dict) -> dict:
    handles = fixture.get("handles") or {}
    dangerous: dict[str, set[str]] = {}
    deceptive: dict[str, set[str]] = {}
    seen: set[str] = set()
    ignored = set(catalog.get("ignored_events") or [])
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        et = ev.get("event_type")
        if et in ignored:
            continue
        payload = ev.get("payload") or {}
        if et == "CONTEST_RESOLVED":
            evidence = payload.get("contest_id") or ev.get("event_id")
            actor = payload.get("declarer_id")
            if evidence and actor and evidence not in seen:
                seen.add(str(evidence))
                dangerous.setdefault(str(actor), set()).add(str(evidence))
        elif et == "CRIME_DETECTED" and payload.get("visibility") == "PUBLIC":
            evidence = payload.get("detection_id") or ev.get("event_id")
            actor = payload.get("subject_id")
            if evidence and actor and evidence not in seen:
                seen.add(str(evidence))
                dangerous.setdefault(str(actor), set()).add(str(evidence))
        elif et == "AGREEMENT_BROKEN" and payload.get("visibility") == "PUBLIC":
            evidence = payload.get("breach_id") or ev.get("event_id")
            actor = payload.get("broken_by")
            if evidence and actor and evidence not in seen:
                seen.add(str(evidence))
                deceptive.setdefault(str(actor), set()).add(str(evidence))
    for attester, eid in _gc3_attest_contradictions(ordered):
        if eid not in seen:
            seen.add(eid)
            deceptive.setdefault(attester, set()).add(eid)
    watch_lines = []
    for other in sorted(set(dangerous) | set(deceptive)):
        name = handles.get(other) or other
        if other in dangerous:
            watch_lines.append(catalog["dangerous_line"].replace("{name}", name))
        if other in deceptive:
            watch_lines.append(catalog["deceptive_line"].replace("{name}", name))
    return {"watch_lines": watch_lines}


def check_gc3_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s2.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.gc3-s2.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S2 catalog invalid: {cerrs[0].message}")
    if catalog.get("reputation_scalar") or catalog.get("s0_s1_watch") or catalog.get("reliable_band") or catalog.get("unknown_band"):
        fail("GC3-S2 must not enable a reputation scalar, S0/S1 WATCH, reliable, or unknown")
    if catalog.get("new_verbs"):
        fail("GC3-S2 must not add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0034-watch-public-descriptors.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0034 must be Accepted")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in ("rebuild-public-contest.json", "rebuild-private-trades-silent.json"):
        fixture = load_json(ROOT / "examples" / "gc3-watch-public" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s2(fixture, catalog)
        exp = fixture["expected"]
        if got["watch_lines"] != exp["watch_lines"]:
            fail(f"{name}: watch {got['watch_lines']} expected {exp['watch_lines']}")
        blob = " ".join(got["watch_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} leaked {token}")
    ok("GC3-S2 WATCH public bands: catalog, rebuild fixtures, RFC-0034 Accepted")


def rebuild_gc3_s3(fixture: dict, catalog: dict) -> dict:
    org = fixture["subject_id"]
    org_name = fixture.get("org_name") or org
    handles = fixture.get("handles") or {}
    viewer_role = fixture.get("viewer_role")
    viewer_id = fixture.get("viewer_id")
    trades: dict[str, set[str]] = {}
    members: dict[str, str] = {}
    danger: dict[str, set[str]] = {}
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        et = ev.get("event_type")
        payload = ev.get("payload") or {}
        if et == "TRADE_ACCEPTED" and payload.get("acting_for") == org:
            tid = payload.get("trade_id") or ev.get("event_id")
            # Org is the acting side; remember only the outside counterparty.
            other = payload.get("counterparty_id")
            if other and tid:
                trades.setdefault(str(other), set()).add(str(tid))
        elif et == "ORG_MEMBER_ADD" and payload.get("org_id") == org:
            agent = payload.get("agent_id")
            if agent:
                members[str(agent)] = "member"
        elif et == "ORG_MEMBER_REMOVE" and payload.get("org_id") == org:
            agent = payload.get("agent_id")
            if agent:
                members[str(agent)] = "removed"
        elif et == "CONTEST_RESOLVED" and (payload.get("defender_id") == org or payload.get("acting_for") == org):
            evidence = payload.get("contest_id") or ev.get("event_id")
            actor = payload.get("declarer_id")
            if evidence and actor:
                danger.setdefault(str(actor), set()).add(str(evidence))
        elif et == "AGREEMENT_BROKEN" and org in (payload.get("party_ids") or []):
            evidence = payload.get("breach_id") or ev.get("event_id")
            actor = payload.get("broken_by")
            if evidence and actor and actor != org:
                danger.setdefault(str(actor), set()).add(str(evidence))
    if viewer_role == "other":
        return {"play_lines": [], "watch_lines": []}
    play_lines = []
    traded_at = int(catalog["traded_threshold"])
    reliable_at = int(catalog["reliable_threshold"])

    def emit(other: str, template: str) -> None:
        if viewer_role == "member" and other != viewer_id:
            return
        name = handles.get(other) or other
        play_lines.append(
            template.replace("{org}", org_name).replace("{name}", name)
        )

    for other, tids in sorted(trades.items()):
        n = len(tids)
        if n >= reliable_at:
            emit(other, catalog["reliable_line"])
        elif n >= traded_at:
            emit(other, catalog["traded_line"])
    for other, state in sorted(members.items()):
        emit(other, catalog["member_line"] if state == "member" else catalog["removed_line"])
    for other, ids in sorted(danger.items()):
        if ids:
            emit(other, catalog["danger_line"])
    return {"play_lines": play_lines, "watch_lines": []}


def check_gc3_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s3.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.gc3-s3.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S3 catalog invalid: {cerrs[0].message}")
    if catalog.get("reputation_scalar") or catalog.get("watch_projection") or catalog.get("role_events") or catalog.get("new_verbs"):
        fail("GC3-S3 must not enable a scalar, WATCH, ROLE_* , or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0035-institution-edges.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0035 must be Accepted")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in ("rebuild-org-trade.json", "rebuild-other-empty.json"):
        fixture = load_json(ROOT / "examples" / "gc3-institution-edges" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s3(fixture, catalog)
        exp = fixture["expected"]
        if got["play_lines"] != exp["play_lines"]:
            fail(f"{name}: lines {got['play_lines']} expected {exp['play_lines']}")
        if got["watch_lines"] or exp["watch_lines"]:
            fail(f"{name}: WATCH must be empty")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} leaked {token}")
    ok("GC3-S3 institution edges: catalog, rebuild fixtures, RFC-0035 Accepted")


def rebuild_gc3_s4(fixture: dict, catalog: dict) -> dict:
    subject = fixture["subject_id"]
    as_of = int(fixture["as_of_cycle"])
    handles = fixture.get("handles") or {}
    decay = int(catalog["decay_cycles"])
    rehab_need = int(catalog["rehab_trades"])
    danger_last: dict[str, int] = {}
    danger_ids: dict[str, str] = {}
    trade_ids: dict[str, list[tuple[int, str]]] = {}
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        cycle = int(ev.get("cycle") or 0)
        payload = ev.get("payload") or {}
        et = ev.get("event_type")
        if et == "CONTEST_RESOLVED":
            victims = [payload.get("defender_id")]
            declarer = payload.get("declarer_id")
            if subject in victims and declarer and declarer != subject:
                danger_last[str(declarer)] = cycle
                danger_ids[str(declarer)] = str(payload.get("contest_id") or ev.get("event_id"))
        elif et == "TRADE_ACCEPTED":
            parties = {payload.get("proposer_id"), payload.get("counterparty_id")}
            if subject in parties:
                other = next((p for p in parties if p and p != subject), None)
                tid = payload.get("trade_id") or ev.get("event_id")
                if other and tid:
                    trade_ids.setdefault(str(other), []).append((cycle, str(tid)))
    play_lines = []
    others = set(danger_last) | set(trade_ids)
    for other in sorted(others):
        last_d = danger_last.get(other)
        trades = trade_ids.get(other) or []
        live_danger = last_d is not None and (as_of - last_d) < decay
        if live_danger:
            after = [tid for cyc, tid in trades if last_d is not None and cyc > last_d]
            if len(set(after)) >= rehab_need:
                live_danger = False
        last_t = max((c for c, _ in trades), default=None)
        live_trade = last_t is not None and (as_of - last_t) < decay
        n = len({tid for _, tid in trades}) if live_trade else 0
        name = handles.get(other) or other
        if n >= 3:
            play_lines.append(f"You have found {name} reliable in trade.")
        elif n >= 1:
            play_lines.append(f"You have traded with {name}.")
        if live_danger:
            play_lines.append(f"You have found {name} dangerous.")
    return {"play_lines": play_lines}


def check_gc3_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s4.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.gc3-s4.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S4 catalog invalid: {cerrs[0].message}")
    if catalog.get("wipe_verb") or catalog.get("ledger_forget") or catalog.get("new_verbs"):
        fail("GC3-S4 must not wipe, forget the ledger, or add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0036-decay-rehab.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0036 must be Accepted")
    rebuild_v = Draft202012Validator(rebuild_schema)
    for name in ("rebuild-decayed-danger.json", "rebuild-rehab-trades.json"):
        fixture = load_json(ROOT / "examples" / "gc3-decay-rehab" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s4(fixture, catalog)
        exp = fixture["expected"]
        if got["play_lines"] != exp["play_lines"]:
            fail(f"{name}: lines {got['play_lines']} expected {exp['play_lines']}")
    ok("GC3-S4 decay/rehab: catalog, rebuild fixtures, RFC-0036 Accepted")


def evaluate_gc3_s5(attempt: dict, catalog: dict) -> dict:
    extra = int(catalog["extra_compute"]) if attempt.get("live_hostile") else 0
    return {
        "extra_compute": extra,
        "auto_reject": bool(catalog.get("auto_reject")),
        "reason_code": catalog["reason_code"] if extra else None,
    }


def check_gc3_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "social-memory-attempt.gc3-s5.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S5 catalog invalid: {cerrs[0].message}")
    if catalog.get("auto_reject") or catalog.get("hide_affordance") or catalog.get("hidden_markup") or catalog.get("new_verbs"):
        fail("GC3-S5 must not auto-reject, hide TRADE, markup in secret, or add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0037-trade-friction.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0037 must be Accepted")
    if "auto-reject" not in rfc.lower() and "auto-refuse" not in rfc.lower():
        fail("RFC-0037 must reject auto-refuse")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in ("attempt-live-danger.json", "attempt-no-edge.json"):
        fixture = load_json(ROOT / "examples" / "gc3-trade-friction" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = evaluate_gc3_s5(fixture, catalog)
        exp = fixture["expected"]
        if got["extra_compute"] != exp["extra_compute"] or got["auto_reject"] != exp["auto_reject"]:
            fail(f"{name}: got {got} expected {exp}")
        if got["reason_code"] != exp.get("reason_code"):
            fail(f"{name}: reason {got['reason_code']} expected {exp.get('reason_code')}")
    ok("GC3-S5 trade caution: catalog, attempt fixtures, RFC-0037 Accepted, no auto-refuse")


def rebuild_gc3_s6(fixture: dict, catalog: dict) -> dict:
    subject = fixture["subject_id"]
    handles = fixture.get("handles") or {}
    deceptive: dict[str, set[str]] = {}
    seen: set[str] = set()
    ignored = set(catalog.get("ignored_events") or [])
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        et = ev.get("event_type")
        if et in ignored:
            continue
        payload = ev.get("payload") or {}
        if et == "AGREEMENT_BROKEN":
            evidence = payload.get("breach_id") or ev.get("event_id")
            broken = payload.get("broken_by")
            parties = payload.get("party_ids") or []
            if subject in parties and broken and broken != subject and evidence and evidence not in seen:
                seen.add(str(evidence))
                deceptive.setdefault(str(broken), set()).add(str(evidence))
    for attester, eid in _gc3_attest_contradictions(ordered):
        if attester != subject and eid not in seen:
            seen.add(eid)
            deceptive.setdefault(attester, set()).add(eid)
    play_lines = []
    out = {}
    thresh = int(catalog["deceptive_threshold"])
    for other, ids in sorted(deceptive.items()):
        n = len(ids)
        out[other] = {"count": n}
        if n >= thresh:
            name = handles.get(other) or other
            play_lines.append(catalog["deceptive_line"].replace("{name}", name))
    return {"deceptive": out, "play_lines": play_lines, "watch_lines": []}


def check_gc3_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s6.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "social-memory-rebuild.gc3-s6.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S6 catalog invalid: {cerrs[0].message}")
    if catalog.get("reputation_scalar") or catalog.get("watch_projection") or catalog.get("new_verbs"):
        fail("GC3-S6 must not enable a scalar, WATCH, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0038-deceptive-edge.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0038 must be Accepted")
    if "trade_rejected" not in rfc.lower():
        fail("RFC-0038 must keep TRADE_REJECTED from becoming deceptive")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in (
        "rebuild-agreement-broken.json",
        "rebuild-reject-ignored.json",
        "rebuild-attest-contradiction.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc3-deceptive" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc3_s6(fixture, catalog)
        exp = fixture["expected"]
        if got["deceptive"] != exp["deceptive"]:
            fail(f"{name}: deceptive {got['deceptive']} expected {exp['deceptive']}")
        if got["play_lines"] != exp["play_lines"]:
            fail(f"{name}: lines {got['play_lines']} expected {exp['play_lines']}")
        if got["watch_lines"]:
            fail(f"{name}: WATCH must be empty on S6")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} leaked {token}")
    ok("GC3-S6 deceptive: catalog, rebuild fixtures, RFC-0038 Accepted, rejects ignored")


def evaluate_gc3_s7(attempt: dict, catalog: dict) -> dict:
    extra = 0
    reason = None
    if attempt.get("live_hostile") and not attempt.get("live_reliable"):
        extra = 1
        reason = "TRADE_CAUTION"
    if attempt.get("live_reliable") and catalog.get("waive_caution"):
        extra = 0
        reason = None
    return {
        "extra_compute": extra,
        "auto_accept": bool(catalog.get("auto_accept")),
        "reason_code": reason,
    }


def check_gc3_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s7.json")
    catalog_schema = load_json(ROOT / "specs" / "social-memory-catalog.gc3-s7.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "social-memory-attempt.gc3-s7.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC3-S7 catalog invalid: {cerrs[0].message}")
    if catalog.get("auto_accept") or catalog.get("hide_others") or catalog.get("hidden_rebate") or catalog.get("base_compute_zero") or catalog.get("new_verbs"):
        fail("GC3-S7 must not auto-accept, hide others, rebate in secret, zero the base, or add verbs")
    rfc = (ROOT / "rfcs" / "RFC-0039-preferred-counterparty.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0039 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in ("attempt-waiver.json", "attempt-caution-only.json", "attempt-none.json"):
        fixture = load_json(ROOT / "examples" / "gc3-preferred" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = evaluate_gc3_s7(fixture, catalog)
        exp = fixture["expected"]
        if got["extra_compute"] != exp["extra_compute"] or got["auto_accept"] != exp["auto_accept"]:
            fail(f"{name}: got {got} expected {exp}")
        if got["reason_code"] != exp.get("reason_code"):
            fail(f"{name}: reason {got['reason_code']} expected {exp.get('reason_code')}")
    ok("GC3-S7 preferred discount: catalog, attempt fixtures, RFC-0039 Accepted, no auto-accept")


def evaluate_gc4_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if not attempt.get("org_active"):
        return "REJECT", "NOT_FOUND"
    op = attempt.get("operation")
    actor_role = attempt.get("actor_role")
    # Cosmetic titles never authorize; only actor_role is consulted.
    if op == "ORG_MEMBER_ADD":
        if actor_role not in (catalog.get("invite_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        if attempt.get("target_is_member"):
            return "REJECT", "FORBIDDEN"
        assigned = attempt.get("assigned_role")
        if assigned in (catalog.get("forbidden_assign_roles") or []):
            return "REJECT", "FORBIDDEN"
        if assigned not in (catalog.get("assignable_roles") or []):
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    if op == "ORG_MEMBER_REMOVE":
        if not attempt.get("target_is_member"):
            return "REJECT", "NOT_FOUND"
        self_leave = attempt.get("actor_id") == attempt.get("target_id")
        if not self_leave and actor_role not in (catalog.get("remove_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        if (
            catalog.get("last_founder_guard")
            and attempt.get("target_role") == "founder"
            and int(attempt.get("founder_count") or 0) <= 1
            and int(attempt.get("member_count") or 0) > 1
        ):
            return "REJECT", "FORBIDDEN"
        if self_leave and not catalog.get("self_leave"):
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    return "REJECT", "FORBIDDEN"


def check_gc4_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "authority-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC4-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("office_names_frozen") or catalog.get("llm_authority") or catalog.get("cosmetic_titles_have_authority"):
        fail("GC4-S0 must not freeze office names, grant LLM authority, or treat titles as grants")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC4-S0 must not add verbs or events")
    if catalog.get("event_catalog") != "event-catalog/0.1":
        fail("GC4-S0 must reuse event-catalog/0.1")
    used = set(catalog.get("membership_events") or [])
    if any(name.startswith("ROLE_") or name.startswith("STRUCTURE_") for name in used):
        fail("GC4-S0 must not introduce ROLE_* or STRUCTURE_* events")
    rfc = (ROOT / "rfcs" / "RFC-0008-office-authority-pins.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0008 must be Accepted after GC4-S0 machine contracts land")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "officer-add-member-ok.json",
        "member-add-forbidden.json",
        "member-self-leave-ok.json",
        "advisor-add-forbidden.json",
        "founder-add-founder-forbidden.json",
        "officer-remove-last-founder-forbidden.json",
        "steward-title-member-add-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc4-authority" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc4_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if fixture["attempt"].get("cosmetic_title") and outcome != "REJECT":
            fail(f"{name}: cosmetic title must not authorize")
    ok("GC4-S0 authority: catalog, attempt fixtures, RFC-0008 Accepted, no ROLE_* events")


def evaluate_gc4_s1(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if not attempt.get("org_active"):
        return "REJECT", "NOT_FOUND"
    op = attempt.get("operation")
    role = attempt.get("actor_role")
    profiles = set(catalog.get("profiles") or [])
    hosted_act = set(catalog.get("hosted_act_profiles") or [])
    if op == "OFFICE_CREATE":
        if role not in (catalog.get("create_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        if attempt.get("profile_valid") is False or attempt.get("profile") not in profiles:
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    if op == "OFFICE_ASSIGN":
        if not attempt.get("office_exists"):
            return "REJECT", "NOT_FOUND"
        if attempt.get("office_status") == "RETIRED":
            return "REJECT", "FORBIDDEN"
        if role not in (catalog.get("assign_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        if attempt.get("same_world") is False:
            return "REJECT", "FORBIDDEN"
        if attempt.get("target_in_world") is False:
            return "REJECT", "NOT_FOUND"
        if catalog.get("holder_must_be_member") and not attempt.get("target_is_member"):
            return "REJECT", "FORBIDDEN"
        if (
            attempt.get("office_status") == "OCCUPIED"
            and catalog.get("replace_requires_flag")
            and not attempt.get("replace")
        ):
            return "REJECT", "FORBIDDEN"
        if attempt.get("profile_valid") is False or (
            attempt.get("profile") and attempt.get("profile") not in profiles
        ):
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    if op == "OFFICE_VACATE":
        if not attempt.get("office_exists"):
            return "REJECT", "NOT_FOUND"
        if attempt.get("office_status") != "OCCUPIED":
            return "REJECT", "FORBIDDEN"
        if attempt.get("actor_is_holder") and catalog.get("holder_may_resign"):
            return "ACCEPT", None
        if role not in (catalog.get("vacate_other_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    if op == "OFFICE_RETIRE":
        if not attempt.get("office_exists"):
            return "REJECT", "NOT_FOUND"
        if attempt.get("office_status") == "RETIRED":
            return "REJECT", "FORBIDDEN"
        if role not in (catalog.get("retire_authorizers") or []):
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    if op == "OFFICE_ACT":
        if not attempt.get("office_exists"):
            return "REJECT", "NOT_FOUND"
        if attempt.get("office_status") != "OCCUPIED":
            return "REJECT", "FORBIDDEN"
        if not attempt.get("actor_is_holder"):
            return "REJECT", "FORBIDDEN"
        if attempt.get("cosmetic_title") and not attempt.get("actor_is_holder"):
            return "REJECT", "FORBIDDEN"
        profile = attempt.get("profile")
        if profile not in profiles or profile not in hosted_act:
            return "REJECT", "FORBIDDEN"
        return "ACCEPT", None
    return "REJECT", "FORBIDDEN"


def check_gc4_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "office-catalog.gc4-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "office-catalog.gc4-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "office-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC4-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("office_names_frozen") or catalog.get("llm_authority") or catalog.get("cosmetic_titles_have_authority"):
        fail("GC4-S1 must not freeze office names, grant LLM authority, or treat titles as grants")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC4-S1 must not add verbs or events")
    if catalog.get("event_catalog") != "event-catalog/0.1":
        fail("GC4-S1 must reuse event-catalog/0.1")
    used = set(catalog.get("evidence_events") or [])
    if any(name.startswith("ROLE_") for name in used):
        fail("GC4-S1 must not introduce ROLE_* events")
    if "ROLE_ASSIGNED" not in (catalog.get("ignored_events") or []):
        fail("GC4-S1 must keep ROLE_* out of evidence")
    rfc = (ROOT / "rfcs" / "RFC-0023-named-offices.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0023 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "create-office-ok.json",
        "assign-eligible-ok.json",
        "holder-act-ok.json",
        "holder-resign-ok.json",
        "reassign-after-vacancy-ok.json",
        "unauthorized-create-forbidden.json",
        "unauthorized-assign-forbidden.json",
        "assign-missing-player-forbidden.json",
        "assign-other-world-forbidden.json",
        "double-assign-forbidden.json",
        "former-holder-act-forbidden.json",
        "retired-office-act-forbidden.json",
        "label-without-grant-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc4-offices" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc4_s1(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if fixture["attempt"].get("cosmetic_title") and outcome != "REJECT":
            fail(f"{name}: cosmetic title must not authorize")
    ok("GC4-S1 offices: catalog, attempt fixtures, RFC-0023 Accepted, no ROLE_* events")


def evaluate_gc4_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"account": None}
    if attempt.get("new_verb"):
        return "REJECT", "VERB_FORBIDDEN", extra
    if attempt.get("same_world") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("org_active") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("display_name_only") or attempt.get("mutates_personal_as_treasury"):
        return "REJECT", "FORBIDDEN", extra
    if attempt.get("same_player_both_sides") or catalog.get("same_player_both_sides"):
        return "REJECT", "FORBIDDEN", extra
    if attempt.get("former_holder") or attempt.get("office_status") == "VACANT":
        return "REJECT", "FORBIDDEN", extra
    if not attempt.get("holds_office"):
        return "REJECT", "FORBIDDEN", extra
    if int(attempt.get("matching_offices") or 0) > 1 and not attempt.get("office_id"):
        return "REJECT", "FORBIDDEN", extra
    op = str(attempt.get("operation") or "")
    profile = attempt.get("office_profile")
    if op.startswith("TRADE") and profile != catalog.get("trade_profile"):
        return "REJECT", "FORBIDDEN", extra
    if op == "REPAIR" and profile != catalog.get("repair_profile"):
        return "REJECT", "FORBIDDEN", extra
    if op == "REPAIR" and attempt.get("asset_in_scope") is False:
        return "REJECT", "FORBIDDEN", extra
    if attempt.get("treasury_ok") is False:
        return "REJECT", "BUDGET_EXCEEDED", extra
    extra["account"] = "treasury"
    return "ACCEPT", None, extra


def check_gc4_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "institution-action-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC4-S2 catalog invalid: {cerrs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC4-S2 must not add verbs or events")
    if catalog.get("founder_implies_treasury") or catalog.get("vacant_office_grants"):
        fail("GC4-S2 must not let founders or vacant offices spend")
    if catalog.get("display_name_is_authority") or catalog.get("silent_account_pick"):
        fail("GC4-S2 must not treat titles as grants or silently pick accounts")
    if catalog.get("emergency_scopes") or catalog.get("designated_succession") or catalog.get("institution_npc"):
        fail("GC4-S2 must leave emergency, succession, and institution NPC out")
    if catalog.get("trade_profile") != "OPERATE_RESOURCE_ACCOUNT":
        fail("GC4-S2 TRADE must use OPERATE_RESOURCE_ACCOUNT")
    if catalog.get("repair_profile") != "OPERATE_NAMED_ASSET":
        fail("GC4-S2 REPAIR must use OPERATE_NAMED_ASSET")
    rfc = (ROOT / "rfcs" / "RFC-0029-institution-trade-repair.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0029 must be Accepted")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if "INSTITUTION_TRADE" in types_text or "INSTITUTION_REPAIR" in types_text:
        fail("GC4-S2 must not add INSTITUTION_* events to frozen catalogs")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "trade-propose-ok.json",
        "trade-accept-ok.json",
        "repair-ok.json",
        "turnover-ok.json",
        "member-trade-forbidden.json",
        "advisor-repair-forbidden.json",
        "former-holder-forbidden.json",
        "vacant-forbidden.json",
        "cross-world-forbidden.json",
        "forged-context-forbidden.json",
        "double-spend-forbidden.json",
        "title-only-forbidden.json",
        "invalid-source-forbidden.json",
        "both-sides-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc4-institution-actions" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc4_s2(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("account") and extra.get("account") != expected["account"]:
            fail(f"{name}: account mismatch")
    ok("GC4-S2 institution TRADE/REPAIR: catalog, fixtures, RFC-0029 Accepted, existing verbs")


def evaluate_gc4_s3(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"status": None}
    if attempt.get("new_verb"):
        return "REJECT", "VERB_FORBIDDEN", extra
    if attempt.get("self_declare") or catalog.get("self_declare"):
        return "REJECT", "FORBIDDEN", extra
    if attempt.get("same_world") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("org_active") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("exceeds_template") or attempt.get("overrides_restriction"):
        return "REJECT", "FORBIDDEN", extra
    op = str(attempt.get("operation") or "")
    if op == "ACTIVATE":
        if attempt.get("office_status") == "VACANT" or not attempt.get("source_ok"):
            return "REJECT", "FORBIDDEN", extra
        if attempt.get("holder_is_member") is False or attempt.get("condition_holds") is False:
            return "REJECT", "FORBIDDEN", extra
        extra["status"] = "ACTIVE"
        return "ACCEPT", None, extra
    if op == "REVOKE":
        if not attempt.get("source_ok"):
            return "REJECT", "FORBIDDEN", extra
        extra["status"] = "REVOKED"
        return "ACCEPT", None, extra
    if op in ("REPAIR", "TRADE"):
        if attempt.get("scope_status") in ("EXPIRED", "REVOKED"):
            return "REJECT", "FORBIDDEN", extra
        if attempt.get("office_status") == "VACANT":
            return "REJECT", "FORBIDDEN", extra
        end = attempt.get("end_cycle")
        cycle = attempt.get("cycle")
        if end is not None and cycle is not None and int(cycle) >= int(end):
            return "REJECT", "FORBIDDEN", extra
        if attempt.get("requested_capability") and attempt.get("requested_capability") != attempt.get(
            "template_capability"
        ):
            return "REJECT", "FORBIDDEN", extra
        extra["status"] = "ACTIVE"
        return "ACCEPT", None, extra
    return "REJECT", "FORBIDDEN", extra


def check_gc4_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "emergency-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC4-S3 catalog invalid: {cerrs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC4-S3 must not add verbs or events")
    if catalog.get("self_declare") or catalog.get("superuser") or catalog.get("operator_via_grant"):
        fail("GC4-S3 must not allow self-declare, superuser, or operator-via-grant")
    if catalog.get("wall_clock_extends") or catalog.get("overrides_restriction") or catalog.get("implicit_successor"):
        fail("GC4-S3 must not extend by wall-clock, override restrictions, or imply succession")
    if catalog.get("vacant_office_grants") or catalog.get("designated_succession"):
        fail("GC4-S3 must leave vacant offices powerless and succession out")
    if int(catalog.get("default_duration_cycles") or 0) != 3:
        fail("GC4-S3 default duration must be 3 cycles")
    rfc = (ROOT / "rfcs" / "RFC-0030-emergency-scopes.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0030 must be Accepted")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if "EMERGENCY_STARTED" in types_text or "EMERGENCY_ENDED" in types_text:
        fail("GC4-S3 must not add EMERGENCY_* events to frozen catalogs")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "activate-ok.json",
        "repair-ok.json",
        "trade-ok.json",
        "expire-ok.json",
        "revoke-ok.json",
        "duplicate-ok.json",
        "self-declare-forbidden.json",
        "exceeds-template-forbidden.json",
        "expired-action-forbidden.json",
        "revoked-action-forbidden.json",
        "cross-world-forbidden.json",
        "vacant-forbidden.json",
        "wall-clock-forbidden.json",
        "restriction-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc4-emergency" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc4_s3(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("status") and extra.get("status") != expected["status"]:
            fail(f"{name}: status mismatch")
    ok("GC4-S3 emergency scopes: catalog, fixtures, RFC-0030 Accepted, no EMERGENCY_* events")


def evaluate_gc4_s4(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"office_status": None, "successor": None, "end_cycle": None}
    op = str(attempt.get("operation") or "")
    if attempt.get("same_world") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("org_active") is False:
        return "REJECT", "NOT_FOUND", extra
    if attempt.get("natural_language") or attempt.get("conflicting_sources"):
        return "REJECT", "FORBIDDEN", extra
    if attempt.get("transfers_reputation") or attempt.get("transfers_knowledge"):
        return "REJECT", "FORBIDDEN", extra
    trigger = str(attempt.get("trigger") or "")
    rejected_triggers = {
        "disconnect",
        "idle",
        "controller",
        "controller_change",
        "dormant",
        "retire",
    }
    valid_triggers = {"resign", "vacate", "leave_org", "office_vacancy"}
    if op == "DESIGNATE":
        role = str(attempt.get("actor_role") or "")
        if role and role not in set(catalog.get("designators") or ("founder", "officer")):
            return "REJECT", "FORBIDDEN", extra
        if not role:
            return "REJECT", "FORBIDDEN", extra
        if attempt.get("successor_is_member") is False:
            return "REJECT", "FORBIDDEN", extra
        return "ACCEPT", None, extra
    if trigger in rejected_triggers:
        return "REJECT", "FORBIDDEN", extra
    if trigger and trigger not in valid_triggers:
        return "REJECT", "FORBIDDEN", extra
    if op == "EMERGENCY_HANDOFF":
        scope_end = attempt.get("scope_end_cycle")
        new_end = attempt.get("new_end_cycle")
        if scope_end is not None and new_end is not None and int(new_end) != int(scope_end):
            return "REJECT", "FORBIDDEN", extra
        if attempt.get("has_designation") and (
            attempt.get("successor_eligible") is True or attempt.get("primary_eligible") is True
        ):
            extra["successor"] = "primary"
            extra["end_cycle"] = scope_end
            return "ACCEPT", None, extra
        extra["successor"] = None
        extra["end_cycle"] = scope_end
        return "ACCEPT", None, extra
    if op == "ACTIVATE":
        if not attempt.get("has_designation"):
            extra["office_status"] = "VACANT"
            extra["successor"] = None
            return "ACCEPT", None, extra
        primary = attempt.get("primary_eligible")
        if primary is True or (attempt.get("successor_eligible") is True and primary is not False):
            extra["office_status"] = "OCCUPIED"
            extra["successor"] = "primary"
            return "ACCEPT", None, extra
        if attempt.get("secondary_eligible") is True:
            extra["office_status"] = "OCCUPIED"
            extra["successor"] = "secondary"
            return "ACCEPT", None, extra
        extra["office_status"] = "VACANT"
        extra["successor"] = None
        return "ACCEPT", None, extra
    return "REJECT", "FORBIDDEN", extra


def check_gc4_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "succession-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC4-S4 catalog invalid: {cerrs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC4-S4 must not add verbs or events")
    if catalog.get("implicit_jump") or catalog.get("holder_may_designate"):
        fail("GC4-S4 must not allow implicit jump or holder self-designation")
    if (
        catalog.get("disconnect_triggers")
        or catalog.get("controller_change_triggers")
        or catalog.get("dormant_triggers")
        or catalog.get("retire_office_succeeds")
        or catalog.get("dissolved_activates")
        or catalog.get("emergency_resets_duration")
        or catalog.get("transfers_reputation")
        or catalog.get("transfers_private_knowledge")
        or catalog.get("transfers_treasury")
    ):
        fail("GC4-S4 must keep non-triggers and non-transfers closed")
    if catalog.get("mechanism") != "DESIGNATED" or int(catalog.get("max_successors") or 0) != 2:
        fail("GC4-S4 must be DESIGNATED with at most two successors")
    rfc = (ROOT / "rfcs" / "RFC-0031-designated-succession.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0031 must be Accepted")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if "SUCCESSION_STARTED" in types_text or "SUCCESSION_COMPLETED" in types_text or "DYNASTY_CHANGED" in types_text:
        fail("GC4-S4 must not add SUCCESSION_* events to frozen catalogs")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "designate-ok.json",
        "resign-activate-ok.json",
        "retire-activate-ok.json",
        "emergency-remaining-ok.json",
        "secondary-ok.json",
        "no-designation-vacant.json",
        "disconnect-forbidden.json",
        "cross-world-forbidden.json",
        "ineligible-vacant.json",
        "emergency-reset-forbidden.json",
        "reputation-forbidden.json",
        "knowledge-forbidden.json",
        "duplicate-ok.json",
        "conflict-forbidden.json",
        "speech-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc4-succession" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc4_s4(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("office_status") and extra.get("office_status") != expected["office_status"]:
            fail(f"{name}: office_status mismatch")
        if "successor" in expected and extra.get("successor") != expected["successor"]:
            fail(f"{name}: successor mismatch")
        if expected.get("end_cycle") is not None and extra.get("end_cycle") != expected["end_cycle"]:
            fail(f"{name}: end_cycle mismatch")
    ok("GC4-S4 designated succession: catalog, fixtures, RFC-0031 Accepted, no SUCCESSION_* events")


def evaluate_gc4_s5(attempt: dict) -> tuple[str, str | None, bool]:
    if attempt.get("office_status") != "VACANT":
        return "REJECT", "occupied", False
    if not attempt.get("actor_is_member") or not attempt.get("candidate_is_member"):
        return "REJECT", "member", False
    members = int(attempt.get("member_count") or 0)
    consents = int(attempt.get("consent_count") or 0)
    need = -(-members // 2)
    if consents >= need:
        return "ACCEPT", None, True
    return "ACCEPT", None, False


def check_gc4_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "succession-attempt.gc4-s5.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC4-S5 catalog invalid: {errs[0].message}")
    if catalog.get("elections") or catalog.get("rule_based") or catalog.get("occupied_vote") or catalog.get("new_events") or catalog.get("watch_titles"):
        fail("GC4-S5 must not add elections, RULE_BASED, occupied votes, new events, or WATCH titles")
    rfc = (ROOT / "rfcs" / "RFC-0060-consensus-succession.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0060 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC4-S5-CONSENSUS.md").read_text(encoding="utf-8")
    if "CONSENSUS" not in slice_doc or "ORG_SUCCESSION_CONSENT" not in slice_doc:
        fail("GC4-S5 must keep CONSENSUS on vacant-office consent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-seat-ok.json",
        "attempt-short.json",
        "attempt-occupied.json",
        "attempt-nonmember.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc4-consensus" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, seated = evaluate_gc4_s5(fixture)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("seated") is not None and seated != exp["seated"]:
            fail(f"{name}: seated {seated} expected {exp['seated']}")
    ok("GC4-S5 CONSENSUS succession: catalog, attempt fixtures, RFC-0060 Accepted")


def evaluate_gc4_s6(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "PUBLISH":
        if attempt.get("rule_id") != catalog.get("rule_id"):
            return "REJECT", "unknown", None
        return "ACCEPT", None, None
    if not attempt.get("published"):
        return "REJECT", "unpublished", False
    remaining = int(attempt.get("eligible_remaining") or 0)
    return "ACCEPT", None, remaining > 0


def check_gc4_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s6.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "succession-attempt.gc4-s6.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC4-S6 catalog invalid: {errs[0].message}")
    if catalog.get("elections") or catalog.get("rule_language") or catalog.get("implicit_jump") or catalog.get("emergency_rule") or catalog.get("new_events") or catalog.get("watch_titles"):
        fail("GC4-S6 must not add elections, a rule language, implicit jump, emergency rules, new events, or WATCH titles")
    if catalog.get("rule_id") != "MEMBER_ORDER":
        fail("GC4-S6 must keep MEMBER_ORDER as the only rule")
    rfc = (ROOT / "rfcs" / "RFC-0069-rule-based-succession.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0069 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC4-S6-RULE.md").read_text(encoding="utf-8")
    if "MEMBER_ORDER" not in slice_doc or "ORG_SUCCESSION_RULE" not in slice_doc:
        fail("GC4-S6 must keep MEMBER_ORDER on ORG_SUCCESSION_RULE")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-publish-ok.json",
        "attempt-unknown-reject.json",
        "attempt-seat-ok.json",
        "attempt-empty-vacant.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc4-rule" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, seated = evaluate_gc4_s6(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("seated") is not None and seated != exp["seated"]:
            fail(f"{name}: seated {seated} expected {exp['seated']}")
    ok("GC4-S6 RULE_BASED succession: catalog, attempt fixtures, RFC-0069 Accepted")


def evaluate_gc4_s7(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {}
    if attempt.get("operation") == "PUBLISH":
        if attempt.get("rule_id") != catalog.get("rule_id"):
            return "REJECT", "unknown", extra
        return "ACCEPT", None, extra
    extra["seated"] = False
    extra["retired"] = False
    return "ACCEPT", None, extra


def check_gc4_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "authority-catalog.gc4-s7.json")
    catalog_schema = load_json(ROOT / "specs" / "authority-catalog.gc4-s7.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "succession-attempt.gc4-s7.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC4-S7 catalog invalid: {errs[0].message}")
    if catalog.get("elections") or catalog.get("institution_as_player") or catalog.get("auto_seat") or catalog.get("retire_on_vacate") or catalog.get("new_events") or catalog.get("watch_titles"):
        fail("GC4-S7 must not add elections, institution-as-Player, auto-seat, retire-on-vacate, new events, or WATCH titles")
    if catalog.get("rule_id") != "INHERITED_BY_ORGANIZATION":
        fail("GC4-S7 must keep INHERITED_BY_ORGANIZATION")
    rfc = (ROOT / "rfcs" / "RFC-0070-inherited-org.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0070 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC4-S7-INHERITED.md").read_text(encoding="utf-8")
    if "INHERITED_BY_ORGANIZATION" not in slice_doc or "VACANT" not in slice_doc:
        fail("GC4-S7 must keep inherit-by-org and vacant seat")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-publish-ok.json",
        "attempt-unknown-reject.json",
        "attempt-vacate-vacant.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc4-inherited" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, extra = evaluate_gc4_s7(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("seated") is not None and extra.get("seated") != exp["seated"]:
            fail(f"{name}: seated {extra.get('seated')} expected {exp['seated']}")
        if exp.get("retired") is not None and extra.get("retired") != exp["retired"]:
            fail(f"{name}: retired {extra.get('retired')} expected {exp['retired']}")
    ok("GC4-S7 INHERITED_BY_ORGANIZATION: catalog, attempt fixtures, RFC-0070 Accepted")


def evaluate_gc5_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if not attempt.get("recipient_addressable"):
        return "REJECT", "FORBIDDEN"
    sender_room = attempt.get("sender_room_id")
    recipient_room = attempt.get("recipient_room_id")
    local = sender_room == recipient_room
    best: int | None = None
    for relay in attempt.get("relays") or []:
        if not relay.get("live"):
            continue
        if relay.get("class_id") != catalog.get("relay_class"):
            continue
        cond = int(relay.get("condition") or 0)
        if best is None or cond > best:
            best = cond
    if local:
        return "ACCEPT", None
    threshold = int(catalog["long_range_min_condition"])
    if best is None or best < threshold:
        return "REJECT", catalog.get("long_range_failure") or "UNREACHABLE"
    return "ACCEPT", None


def check_gc5_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC5-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("delay_enabled") or catalog.get("rumor_enabled") or catalog.get("watch_text"):
        fail("GC5-S0 must not enable delay, rumor, or WATCH text")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC5-S0 must not add verbs or events")
    if catalog.get("verb") != "MESSAGE" or catalog.get("event_catalog") != "event-catalog/0.1":
        fail("GC5-S0 must reuse MESSAGE and event-catalog/0.1")
    if int(catalog.get("long_range_min_condition") or 0) != 25:
        fail("GC5-S0 must reuse the existing MESSAGE stressed-relay threshold 25")
    rfc = (ROOT / "rfcs" / "RFC-0009-relay-message-delivery.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0009 must be Accepted after GC5-S0 machine contracts land")
    attempt_v = Draft202012Validator(attempt_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_reason") or []]
    names = [
        "local-dead-relay-ok.json",
        "long-range-at-band-ok.json",
        "long-range-below-band-unreachable.json",
        "long-range-no-relay-unreachable.json",
        "hidden-room-unreachable-no-leak.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc5-communication" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc5_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("watch_text"):
            fail(f"{name}: WATCH must not carry DM text")
        if outcome == "ACCEPT" and expected.get("events") != catalog.get("success_events"):
            fail(f"{name}: success events must be MESSAGE then MESSAGE_DELIVERED")
        if outcome == "REJECT" and expected.get("events"):
            fail(f"{name}: UNREACHABLE must emit no events")
        if reason:
            for token in forbidden:
                if token in reason.lower():
                    fail(f"{name} reason leaked {token}")
        attempt = fixture["attempt"]
        if attempt.get("recipient_room_hidden") and reason:
            hidden_room = str(attempt.get("recipient_room_id") or "")
            if hidden_room and hidden_room in reason:
                fail(f"{name} reason leaked hidden room id")
            for relay in attempt.get("relays") or []:
                eid = relay.get("entity_id")
                if eid and eid in reason:
                    fail(f"{name} reason leaked relay entity_id")
    ok("GC5-S0 communication: catalog, attempt fixtures, RFC-0009 Accepted, no new verbs")


def evaluate_gc5_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, str | None]:
    if attempt.get("rumor") or attempt.get("new_verb"):
        return "REJECT", "VERB_FORBIDDEN", None
    if not attempt.get("recipient_addressable"):
        return "REJECT", "FORBIDDEN", None
    sender_room = attempt.get("sender_room_id")
    recipient_room = attempt.get("recipient_room_id")
    local = sender_room == recipient_room
    best: int | None = None
    for relay in attempt.get("relays") or []:
        if not relay.get("live"):
            continue
        if relay.get("class_id") != catalog.get("relay_class"):
            continue
        cond = int(relay.get("condition") or 0)
        if best is None or cond > best:
            best = cond
    if local:
        return "ACCEPT", None, "same_cycle"
    floor = int(catalog["long_range_min_condition"])
    healthy = int(catalog["same_cycle_min_condition"])
    if best is None or best < floor:
        return "REJECT", catalog.get("long_range_failure") or "UNREACHABLE", None
    if best < healthy:
        return "ACCEPT", None, "delayed"
    return "ACCEPT", None, "same_cycle"


def check_gc5_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s1.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC5-S1 catalog invalid: {cerrs[0].message}")
    if not catalog.get("delay_enabled") or catalog.get("rumor_enabled") or catalog.get("watch_text"):
        fail("GC5-S1 must enable delay and reject rumor/WATCH text")
    if int(catalog.get("delay_cycles") or 0) != 1:
        fail("GC5-S1 delay must be exactly 1 cycle")
    if int(catalog.get("long_range_min_condition") or 0) != 25:
        fail("GC5-S1 must keep the S0 fail floor 25")
    if int(catalog.get("same_cycle_min_condition") or 0) != 50:
        fail("GC5-S1 same-cycle long-range must start at 50")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC5-S1 must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0021-relay-message-delay.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0021 must be Accepted")
    if "rumor" not in rfc.lower():
        fail("RFC-0021 must leave rumor out")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "long-range-healthy-same-cycle.json",
        "long-range-degraded-delayed.json",
        "long-range-below-band-unreachable.json",
        "rumor-verb-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc5-delay" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, delivery = evaluate_gc5_s1(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("delivery") and delivery != expected["delivery"]:
            fail(f"{name}: delivery {delivery} expected {expected['delivery']}")
        if expected.get("delay_cycles") is not None and int(expected["delay_cycles"]) != 1:
            fail(f"{name}: delay_cycles must be 1")
    ok("GC5-S1 delay: catalog, attempt fixtures, RFC-0021 Accepted, rumor out")


def evaluate_gc5_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    extra: dict = {"receipt": False, "same_claim": False, "derived": False}
    if attempt.get("new_verb") or attempt.get("spread_rumor_verb") or catalog.get("spread_rumor_verb"):
        return "REJECT", "VERB_FORBIDDEN", extra
    origin = attempt.get("origin_class")
    if (
        attempt.get("research_origin")
        or attempt.get("admin_origin")
        or origin in (catalog.get("forbidden_origins") or [])
    ):
        return "REJECT", "ORIGIN_FORBIDDEN", extra
    if attempt.get("same_world") is False:
        return "REJECT", "CROSS_WORLD", extra
    if attempt.get("originator_override"):
        return "REJECT", "FORGE_FORBIDDEN", extra
    if attempt.get("mutates_truth"):
        return "REJECT", "TRUTH_MUTATION", extra
    if attempt.get("count_copies_as_witnesses") or catalog.get("copies_are_independent"):
        return "REJECT", "COPIES_NOT_INDEPENDENT", extra
    if attempt.get("delivery") == "UNREACHABLE":
        extra["receipt"] = False
        return "REJECT", "UNREACHABLE", extra
    if attempt.get("idempotent_replay"):
        return "REJECT", "DUPLICATE", extra
    if attempt.get("parent_claim_id") and not attempt.get("holds_parent"):
        return "REJECT", "NOT_FOUND", extra

    leak_tokens = list(catalog.get("forbidden_in_projection") or [])
    leak_tokens.extend(["secret-signal", "player.nacre said"])
    for line in list(attempt.get("play_lines") or []) + list(attempt.get("watch_lines") or []):
        blob = str(line).lower()
        for tok in leak_tokens:
            if tok and tok.lower() in blob:
                return "REJECT", "LABEL_LEAK", extra

    text = str(attempt.get("text") or "").strip()
    parent = str(attempt.get("parent_content") or "").strip()
    scenario = attempt.get("scenario")
    extra["receipt"] = True
    extra["event"] = "MESSAGE"
    if attempt.get("delivery") == "delayed":
        extra["delay_cycles"] = int(catalog.get("delay_cycles") or 1)

    if scenario in ("retell_unchanged", "shared_source") or (parent and text and parent == text):
        extra["same_claim"] = True
        extra["derived"] = False
    elif scenario in ("retell_changed", "correction") or (parent and text and parent != text):
        extra["same_claim"] = False
        extra["derived"] = True

    independent = int(attempt.get("independent_origins") or 1)
    if scenario == "shared_source":
        extra["independent_sources"] = 1
    else:
        extra["independent_sources"] = independent

    age = int(attempt.get("age_cycles") or 0)
    stale_after = int(catalog.get("stale_after_cycles") or 8)
    if age >= stale_after:
        extra["epistemic"] = "STALE"
    elif independent >= 2 and attempt.get("same_content") is False:
        extra["epistemic"] = "CONTESTED"
    elif independent >= 2 and attempt.get("same_content") is True:
        extra["epistemic"] = "CORROBORATED"
    else:
        extra["epistemic"] = "REPORTED"

    return "ACCEPT", None, extra


def check_gc5_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "rumor-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC5-S2 catalog invalid: {cerrs[0].message}")
    if not catalog.get("rumor_enabled") or not catalog.get("rumor_is_claim"):
        fail("GC5-S2 must enable rumor as claim+provenance")
    if catalog.get("rumor_score") or catalog.get("truth_probability") or catalog.get("spread_rumor_verb"):
        fail("GC5-S2 must not add a rumor score, truth probability, or SPREAD_RUMOR verb")
    if catalog.get("llm_similarity") or catalog.get("omniscient_resolver") or catalog.get("watch_text"):
        fail("GC5-S2 must not use LLM similarity, omniscient truth, or WATCH DM text")
    if catalog.get("copies_are_independent"):
        fail("GC5-S2 must not count copies as independent witnesses")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC5-S2 must not add verbs or events")
    if catalog.get("extends") != "communication-catalog/gc5-s1":
        fail("GC5-S2 must extend GC5-S1")
    if catalog.get("verb") != "MESSAGE":
        fail("GC5-S2 must reuse MESSAGE")
    rfc = (ROOT / "rfcs" / "RFC-0028-rumor-provenance.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0028 must be Accepted after GC5-S2 machine contracts land")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if "RUMOR_CREATED" in types_text or "RUMOR_SPREAD" in types_text:
        fail("GC5-S2 must not add RUMOR_* to frozen catalogs")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "tell-ok.json",
        "retell-unchanged-ok.json",
        "retell-changed-ok.json",
        "shared-source-ok.json",
        "independent-corroboration-ok.json",
        "contested-ok.json",
        "delayed-ok.json",
        "stale-ok.json",
        "public-watch-ok.json",
        "correction-ok.json",
        "institution-ok.json",
        "unreachable-forbidden.json",
        "hidden-source-leak-forbidden.json",
        "cross-world-forbidden.json",
        "forged-origin-forbidden.json",
        "duplicate-forbidden.json",
        "research-origin-forbidden.json",
        "admin-origin-forbidden.json",
        "copies-not-witnesses-forbidden.json",
        "truth-mutation-forbidden.json",
        "rumor-verb-forbidden.json",
        "missing-parent-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc5-rumor" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc5_s2(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("same_claim") is not None and extra.get("same_claim") != expected["same_claim"]:
            fail(f"{name}: same_claim mismatch")
        if expected.get("derived") is not None and extra.get("derived") != expected["derived"]:
            fail(f"{name}: derived mismatch")
        if expected.get("independent_sources") is not None and extra.get("independent_sources") != expected["independent_sources"]:
            fail(f"{name}: independent_sources mismatch")
        if expected.get("epistemic") and extra.get("epistemic") != expected["epistemic"]:
            fail(f"{name}: epistemic {extra.get('epistemic')} expected {expected['epistemic']}")
        if expected.get("receipt") is not None and extra.get("receipt") != expected["receipt"]:
            fail(f"{name}: receipt mismatch")
        if expected.get("delay_cycles") is not None and extra.get("delay_cycles") != expected["delay_cycles"]:
            fail(f"{name}: delay_cycles mismatch")
        if expected.get("event") and extra.get("event") != expected["event"]:
            fail(f"{name}: event mismatch")
    ok("GC5-S2 rumor: catalog, claim fixtures, RFC-0028 Accepted, MESSAGE reused")


def evaluate_gc5_s3(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_board"):
        return "REJECT", "hidden", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 3)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S3 catalog invalid: {errs[0].message}")
    if catalog.get("shout") or catalog.get("watch_board") or catalog.get("help_board") or catalog.get("new_verbs"):
        fail("GC5-S3 must not add SHOUT, WATCH board, help board, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0054-message-board.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0054 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S3-BOARD.md").read_text(encoding="utf-8")
    if "BOARD" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S3 must keep BOARD on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-board-ok.json",
        "attempt-hidden-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-board" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s3(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S3 MESSAGE board: catalog, attempt fixtures, RFC-0054 Accepted")


def evaluate_gc5_s4(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_shout"):
        return "REJECT", "hidden", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 1)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s4.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S4 catalog invalid: {errs[0].message}")
    if catalog.get("shout_verb") or catalog.get("watch_shout") or catalog.get("help_shout") or catalog.get("new_verbs") or catalog.get("long_range_shout"):
        fail("GC5-S4 must not add SHOUT verb, WATCH shout, help shout, long-range shout, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0062-message-shout.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0062 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S4-SHOUT.md").read_text(encoding="utf-8")
    if "SHOUT" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S4 must keep SHOUT on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-shout-ok.json",
        "attempt-hidden-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-shout" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s4(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S4 MESSAGE shout: catalog, attempt fixtures, RFC-0062 Accepted")


def evaluate_gc5_s5(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_board"):
        return "REJECT", "hidden", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 5)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s5(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s5.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s5.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s5.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S5 catalog invalid: {errs[0].message}")
    if catalog.get("retention") != 5:
        fail("GC5-S5 must keep last 5 board notices")
    if catalog.get("shout_retention") != 1:
        fail("GC5-S5 must leave shout last-1 unchanged")
    if catalog.get("shout_verb") or catalog.get("watch_board") or catalog.get("help_board") or catalog.get("new_verbs"):
        fail("GC5-S5 must not add SHOUT verb, WATCH board, help board, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0063-board-retention.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0063 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S5-RETENTION.md").read_text(encoding="utf-8")
    if "last **5**" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S5 must keep last 5 on BOARD and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-board-ok.json",
        "attempt-hidden-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-retention" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s5(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S5 MESSAGE board retention: catalog, attempt fixtures, RFC-0063 Accepted")


def evaluate_gc5_s6(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_notice"):
        return "REJECT", "hidden", None
    if attempt.get("occupied") is False:
        return "REJECT", "unauthorized", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 1)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s6.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s6.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s6.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S6 catalog invalid: {errs[0].message}")
    if catalog.get("notice_verb") or catalog.get("org_channel") or catalog.get("watch_notice") or catalog.get("help_notice") or catalog.get("new_verbs") or catalog.get("long_range_notice"):
        fail("GC5-S6 must not add NOTICE verb, org channel, WATCH notice, help notice, long-range notice, or new verbs")
    if catalog.get("requires_office") != "PUBLISH_NOTICE":
        fail("GC5-S6 must require occupied PUBLISH_NOTICE")
    if catalog.get("board_retention") != 5 or catalog.get("shout_retention") != 1:
        fail("GC5-S6 must leave board last-5 and shout last-1 unchanged")
    rfc = (ROOT / "rfcs" / "RFC-0064-institution-notice.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0064 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S6-NOTICE.md").read_text(encoding="utf-8")
    if "NOTICE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S6 must keep NOTICE on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-notice-ok.json",
        "attempt-hidden-reject.json",
        "attempt-vacant-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-notice" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s6(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S6 MESSAGE institution notice: catalog, attempt fixtures, RFC-0064 Accepted")


def evaluate_gc5_s7(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_channel"):
        return "REJECT", "hidden", None
    if attempt.get("org_known") is False or attempt.get("member") is False:
        return "REJECT", "not_addressable", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 1)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s7.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s7.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s7.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S7 catalog invalid: {errs[0].message}")
    if catalog.get("channel_verb") or catalog.get("watch_channel") or catalog.get("help_channel") or catalog.get("leak_membership") or catalog.get("new_verbs"):
        fail("GC5-S7 must not add CHANNEL verb, WATCH channel, help channel, membership leak, or new verbs")
    if catalog.get("fail_unknown") != catalog.get("fail_outsider"):
        fail("GC5-S7 unknown org and outsider must share one fail")
    rfc = (ROOT / "rfcs" / "RFC-0065-org-channel.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0065 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S7-CHANNEL.md").read_text(encoding="utf-8")
    if "CHANNEL" not in slice_doc or "WATCH" not in slice_doc or "NOT_ADDRESSABLE" not in slice_doc:
        fail("GC5-S7 must keep CHANNEL on MESSAGE, WATCH silent, and NOT_ADDRESSABLE")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-channel-ok.json",
        "attempt-hidden-reject.json",
        "attempt-outsider-reject.json",
        "attempt-unknown-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-channel" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s7(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S7 MESSAGE org channel: catalog, attempt fixtures, RFC-0065 Accepted")


def evaluate_gc5_s8(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("room_hidden") or catalog.get("hidden_stall"):
        return "REJECT", "hidden", None
    posted = int(attempt.get("posted") or 0)
    keep = int(catalog.get("retention") or 1)
    return "ACCEPT", None, min(posted, keep)


def check_gc5_s8(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s8.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s8.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s8.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S8 catalog invalid: {errs[0].message}")
    if catalog.get("market_verb") or catalog.get("auto_trade") or catalog.get("price_oracle") or catalog.get("watch_stall") or catalog.get("help_stall") or catalog.get("new_verbs"):
        fail("GC5-S8 must not add MARKET verb, auto-TRADE, price oracle, WATCH stall, help stall, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0066-trade-notice.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0066 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S8-TRADE-NOTICE.md").read_text(encoding="utf-8")
    if "TRADE_NOTICE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S8 must keep TRADE_NOTICE on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-stall-ok.json",
        "attempt-hidden-reject.json",
        "attempt-retention.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-trade-notice" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s8(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S8 MESSAGE trade notice: catalog, attempt fixtures, RFC-0066 Accepted")


def evaluate_gc5_s9(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "SHOUT":
        if attempt.get("room_hidden") or catalog.get("hidden_shout"):
            return "REJECT", "hidden", None
        return "ACCEPT", None, 1
    kept = 0 if int(attempt.get("committed_cycles") or 0) >= int(catalog.get("expire_cycles") or 1) else 1
    return "ACCEPT", None, kept


def check_gc5_s9(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s9.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s9.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s9.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S9 catalog invalid: {errs[0].message}")
    if catalog.get("help_shout") or catalog.get("watch_shout") or catalog.get("new_verbs") or catalog.get("board_expiry"):
        fail("GC5-S9 must not add help shout, WATCH shout, new verbs, or board expiry")
    if catalog.get("expire_cycles") != 1 or catalog.get("retention") != 1:
        fail("GC5-S9 must keep last-1 shout and expire after 1 cycle")
    rfc = (ROOT / "rfcs" / "RFC-0080-shout-expiry.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0080 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S9-SHOUT-EXPIRY.md").read_text(encoding="utf-8")
    if "SHOUT" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S9 must keep SHOUT on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-shout-ok.json",
        "attempt-hidden-reject.json",
        "attempt-expire-ok.json",
        "attempt-same-cycle.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-shout-expiry" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s9(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S9 shout cycle expiry: catalog, attempt fixtures, RFC-0080 Accepted")


def evaluate_gc5_s10(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "BOARD":
        if attempt.get("room_hidden") or catalog.get("hidden_board"):
            return "REJECT", "hidden", None
        posted = int(attempt.get("posted") or 0)
        cap = int(catalog.get("retention") or 5)
        return "ACCEPT", None, min(posted, cap)
    posted = int(attempt.get("posted") or 0)
    if int(attempt.get("committed_cycles") or 0) >= int(catalog.get("expire_cycles") or 1):
        return "ACCEPT", None, 0
    cap = int(catalog.get("retention") or 5)
    return "ACCEPT", None, min(posted, cap)


def check_gc5_s10(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s10.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s10.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s10.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S10 catalog invalid: {errs[0].message}")
    if catalog.get("help_board") or catalog.get("watch_board") or catalog.get("new_verbs") or catalog.get("notice_expiry"):
        fail("GC5-S10 must not add help board, WATCH board, new verbs, or notice expiry")
    if catalog.get("expire_cycles") != 1 or catalog.get("retention") != 5:
        fail("GC5-S10 must keep last-5 board and expire after 1 cycle")
    rfc = (ROOT / "rfcs" / "RFC-0081-board-expiry.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0081 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S10-BOARD-EXPIRY.md").read_text(encoding="utf-8")
    if "BOARD" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S10 must keep BOARD on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-board-ok.json",
        "attempt-retention.json",
        "attempt-hidden-reject.json",
        "attempt-expire-ok.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-board-expiry" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s10(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S10 board cycle expiry: catalog, attempt fixtures, RFC-0081 Accepted")


def evaluate_gc5_s11(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "NOTICE":
        if attempt.get("room_hidden") or catalog.get("hidden_notice"):
            return "REJECT", "hidden", None
        return "ACCEPT", None, 1
    kept = 0 if int(attempt.get("committed_cycles") or 0) >= int(catalog.get("expire_cycles") or 1) else 1
    return "ACCEPT", None, kept


def check_gc5_s11(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s11.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s11.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s11.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S11 catalog invalid: {errs[0].message}")
    if catalog.get("help_notice") or catalog.get("watch_notice") or catalog.get("new_verbs") or catalog.get("channel_expiry"):
        fail("GC5-S11 must not add help NOTICE, WATCH notice, new verbs, or channel expiry")
    if catalog.get("expire_cycles") != 1 or catalog.get("retention") != 1:
        fail("GC5-S11 must keep last-1 notice and expire after 1 cycle")
    rfc = (ROOT / "rfcs" / "RFC-0082-notice-expiry.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0082 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S11-NOTICE-EXPIRY.md").read_text(encoding="utf-8")
    if "NOTICE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S11 must keep NOTICE on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-notice-ok.json",
        "attempt-hidden-reject.json",
        "attempt-expire-ok.json",
        "attempt-same-cycle.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-notice-expiry" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s11(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S11 notice cycle expiry: catalog, attempt fixtures, RFC-0082 Accepted")


def evaluate_gc5_s12(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "CHANNEL":
        if attempt.get("room_hidden") or catalog.get("hidden_channel"):
            return "REJECT", "hidden", None
        return "ACCEPT", None, 1
    kept = 0 if int(attempt.get("committed_cycles") or 0) >= int(catalog.get("expire_cycles") or 1) else 1
    return "ACCEPT", None, kept


def check_gc5_s12(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s12.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s12.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s12.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S12 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_channel")
        or catalog.get("watch_channel")
        or catalog.get("new_verbs")
        or catalog.get("leak_membership")
        or catalog.get("trade_notice_expiry")
    ):
        fail("GC5-S12 must not add help CHANNEL, WATCH channel, membership leak, TRADE_NOTICE expiry, or new verbs")
    if catalog.get("expire_cycles") != 1 or catalog.get("retention") != 1:
        fail("GC5-S12 must keep last-1 channel and expire after 1 cycle")
    rfc = (ROOT / "rfcs" / "RFC-0083-channel-expiry.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0083 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S12-CHANNEL-EXPIRY.md").read_text(encoding="utf-8")
    if "CHANNEL" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S12 must keep CHANNEL on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-channel-ok.json",
        "attempt-hidden-reject.json",
        "attempt-expire-ok.json",
        "attempt-same-cycle.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-channel-expiry" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s12(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S12 channel cycle expiry: catalog, attempt fixtures, RFC-0083 Accepted")


def evaluate_gc5_s13(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    if attempt.get("operation") == "TRADE_NOTICE":
        if attempt.get("room_hidden") or catalog.get("hidden_stall"):
            return "REJECT", "hidden", None
        return "ACCEPT", None, 1
    kept = 0 if int(attempt.get("committed_cycles") or 0) >= int(catalog.get("expire_cycles") or 1) else 1
    return "ACCEPT", None, kept


def check_gc5_s13(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "communication-catalog.gc5-s13.json")
    catalog_schema = load_json(ROOT / "specs" / "communication-catalog.gc5-s13.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "communication-attempt.gc5-s13.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC5-S13 catalog invalid: {errs[0].message}")
    if (
        catalog.get("help_market")
        or catalog.get("watch_trade_notice")
        or catalog.get("new_verbs")
        or catalog.get("auto_trade")
        or catalog.get("price_oracle")
    ):
        fail("GC5-S13 must not add help market, WATCH trade notice, auto-TRADE, price oracle, or new verbs")
    if catalog.get("expire_cycles") != 1 or catalog.get("retention") != 1:
        fail("GC5-S13 must keep last-1 trade notice and expire after 1 cycle")
    rfc = (ROOT / "rfcs" / "RFC-0084-trade-notice-expiry.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0084 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC5-S13-TRADE-NOTICE-EXPIRY.md").read_text(encoding="utf-8")
    if "TRADE_NOTICE" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC5-S13 must keep TRADE_NOTICE on MESSAGE and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-stall-ok.json",
        "attempt-hidden-reject.json",
        "attempt-expire-ok.json",
        "attempt-same-cycle.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc5-trade-notice-expiry" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, kept = evaluate_gc5_s13(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("kept") is not None and kept != exp["kept"]:
            fail(f"{name}: kept {kept} expected {exp['kept']}")
    ok("GC5-S13 trade-notice cycle expiry: catalog, attempt fixtures, RFC-0084 Accepted")


def rebuild_gc6_s0(fixture: dict, catalog: dict) -> dict:
    subject = fixture["subject_id"]
    archive = fixture.get("archive") or {}
    inspect = fixture.get("inspect") or {}
    archive_ok = subject in (archive.get("accessible_to") or [])
    inspect_ok = subject in (inspect.get("accessible_to") or [])
    same = archive.get("subject_entity_id") == inspect.get("subject_entity_id")
    if archive_ok and inspect_ok and same:
        conflict = archive.get("claim") != inspect.get("observation")
        if conflict:
            return {
                "play_lines": [catalog["conflict_line"]],
                "watch_lines": [],
                "third_party_lines": [],
                "discovery_state": catalog["conflict_discovery_state"],
                "resolution_status": catalog["resolution_status"],
                "quest_log": [],
            }
        return {
            "play_lines": [],
            "watch_lines": [],
            "third_party_lines": [],
            "discovery_state": "investigated",
            "resolution_status": "none",
            "quest_log": [],
        }
    if inspect_ok:
        state = "observed"
    elif archive_ok:
        state = "discovered"
    else:
        state = "unknown"
    return {
        "play_lines": [],
        "watch_lines": [],
        "third_party_lines": [],
        "discovery_state": state,
        "resolution_status": "none",
        "quest_log": [],
    }


def check_gc6_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "discovery-catalog.gc6-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "discovery-catalog.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "discovery-rebuild.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC6-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("quest_ui") or catalog.get("oracle") or catalog.get("ledger_write"):
        fail("GC6-S0 must not enable a quest UI, oracle, or ledger write")
    if catalog.get("watch_projection") or catalog.get("public_projection"):
        fail("GC6-S0 must not enable a public or WATCH projection")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC6-S0 must not add verbs or events")
    if catalog.get("understood_on_conflict"):
        fail("GC6-S0 must not mark a conflict as understood")
    if catalog.get("contradiction_schema") != "contradiction-set/0.2":
        fail("GC6-S0 must reuse contradiction-set/0.2")
    rfc = (ROOT / "rfcs" / "RFC-0010-discovery-contradiction.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0010 must be Accepted after GC6-S0 machine contracts land")
    src = (ROOT / "rfcs" / "RFC-0015-archive-record-source.md").read_text(encoding="utf-8")
    if "**Accepted**" not in src.split("## Status", 1)[-1][:240]:
        fail("RFC-0015 must be Accepted to name the GC6-S0 archive-record source")
    src_l = src.lower()
    for token in (
        "archive_subject_entity_id",
        "archive_claim",
        "destroyed",
        "operating",
        "flavor-text",
        "genesis",
        "unprojected",
    ):
        if token not in src_l:
            fail(f"RFC-0015 must name archive source pin ({token})")
    slice_txt = (ROOT / "docs" / "GC6-FIRST-SLICE.md").read_text(encoding="utf-8")
    if "PLAY stays unprojected" not in slice_txt and "PLAY unprojected" not in slice_txt:
        fail("GC6-FIRST-SLICE must say hosted PLAY is unprojected while Perihelion has no claim fields")
    if "destroyed-relay" not in slice_txt.lower() and "destroyed relay" not in slice_txt.lower():
        fail("GC6-FIRST-SLICE must still reject a destroyed-relay Genesis pack")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    names = [
        "rebuild-relay-seven-open.json",
        "rebuild-inspect-only.json",
        "rebuild-archive-only.json",
        "rebuild-agreeing.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc6-discovery" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc6_s0(fixture, catalog)
        exp = fixture["expected"]
        for key in (
            "play_lines",
            "watch_lines",
            "third_party_lines",
            "discovery_state",
            "resolution_status",
            "quest_log",
        ):
            if got[key] != exp[key]:
                fail(f"{name} {key}: got {got[key]} expected {exp[key]}")
        if got["watch_lines"] or got["third_party_lines"] or got["quest_log"]:
            fail(f"{name} WATCH, third party, and quest log must be empty")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} play line leaked {token}")
        known = fixture.get("known_truth_relationship") or {}
        for leak in ("matches_world_truth", "research partition", "INFERRED"):
            if leak.lower() in blob:
                fail(f"{name} play line leaked research truth ({leak})")
        if known and name == "rebuild-relay-seven-open.json" and not got["play_lines"]:
            fail("Relay Seven pair must project the conflict line")
        if got["discovery_state"] == "understood":
            fail(f"{name} must not project understood")
    ok("GC6-S0 discovery: catalog, rebuild fixtures, RFC-0010/0015 Accepted, no quest oracle")


def evaluate_gc6_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, str | None]:
    if not attempt.get("actor_in_world") or not attempt.get("subject_known"):
        return "REJECT", "NOT_FOUND", None
    if attempt.get("same_world") is False:
        return "REJECT", "FORBIDDEN", None
    if attempt.get("claim_nonempty") is False:
        return "REJECT", "INVALID_REQUEST", None
    hosted = set(catalog.get("hosted_evidence_kinds") or [])
    forbidden_classes = set(catalog.get("forbidden_evidence_classes") or [])
    evidence = list(attempt.get("evidence") or [])
    if not evidence:
        return "REJECT", "FORBIDDEN", None
    labels: set[str] = set()
    kinds: set[str] = set()
    for item in evidence:
        kind = item.get("kind")
        ev_class = item.get("evidence_class") or "PLAY"
        if ev_class in forbidden_classes:
            return "REJECT", "FORBIDDEN", None
        if kind not in hosted:
            return "REJECT", "FORBIDDEN", None
        if not item.get("accessible"):
            return "REJECT", "FORBIDDEN", None
        kinds.add(str(kind))
        if item.get("label"):
            labels.add(str(item["label"]))
    op = attempt.get("operation")
    visibility = attempt.get("visibility") or "PRIVATE"
    if visibility == "INSTITUTIONAL" and not attempt.get("has_publish_authority"):
        return "REJECT", "FORBIDDEN", None
    if op == "RECONSTRUCT_SUPERSEDE":
        if not attempt.get("owns_prior") and attempt.get("prior_visibility") == "PRIVATE":
            return "REJECT", "FORBIDDEN", None
        if not attempt.get("owns_prior"):
            return "REJECT", "FORBIDDEN", None
    if op == "RECONSTRUCT_PUBLISH" and not attempt.get("owns_prior"):
        return "REJECT", "FORBIDDEN", None
    epistemic = "OPEN"
    if (
        catalog.get("contested_when_archive_and_inspect_disagree")
        and "ARCHIVE_CLAIM" in kinds
        and "LIVE_INSPECT" in kinds
        and "DESTROYED" in labels
        and "OPERATING" in labels
    ):
        epistemic = "CONTESTED"
    return "ACCEPT", None, epistemic


def check_gc6_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "reconstruction-catalog.gc6-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "reconstruction-catalog.gc6-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "reconstruction-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC6-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("quest_ui") or catalog.get("oracle") or catalog.get("mutates_canonical_history"):
        fail("GC6-S1 must not enable a quest UI, oracle, or ledger rewrite")
    if catalog.get("confidence_scalar") or catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC6-S1 must not add a confidence scalar, verbs, or events")
    rfc = (ROOT / "rfcs" / "RFC-0024-historical-reconstruction.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0024 must be Accepted")
    if "known_truth" not in rfc.lower() and "canonical history" not in rfc.lower():
        fail("RFC-0024 must keep reconstruction off canonical truth")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "single-source-ok.json",
        "multi-source-ok.json",
        "contradictory-ok.json",
        "private-ok.json",
        "institutional-ok.json",
        "public-ok.json",
        "supersede-ok.json",
        "hidden-evidence-forbidden.json",
        "cross-world-forbidden.json",
        "missing-evidence-forbidden.json",
        "unauthorized-publish-forbidden.json",
        "research-evidence-forbidden.json",
        "admin-evidence-forbidden.json",
        "truth-mutation-forbidden.json",
        "supersede-foreign-private-forbidden.json",
    ]
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc6-reconstruction" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, epistemic = evaluate_gc6_s1(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("epistemic") and epistemic != expected["epistemic"]:
            fail(f"{name}: epistemic {epistemic} expected {expected['epistemic']}")
        blob = (expected.get("note") or "").lower()
        for token in forbidden:
            if token in blob and expected["outcome"] == "ACCEPT":
                fail(f"{name} note leaked {token}")
    ok("GC6-S1 reconstruction: catalog, attempt fixtures, RFC-0024 Accepted, no quest oracle")


def evaluate_gc7_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if attempt.get("character_dead"):
        return "REJECT", "DEATH_FORBIDDEN"
    if attempt.get("hp_combat"):
        return "REJECT", "HP_FORBIDDEN"
    form = attempt.get("contest_form")
    if form and form not in (catalog.get("forms") or []):
        return "REJECT", "FORM_FORBIDDEN"
    projection = str(attempt.get("projection") or "")
    for token in catalog.get("forbidden_in_projection") or []:
        if token.lower() in projection.lower():
            return "REJECT", "LEAK"
    forbidden_verbs = set(catalog.get("forbidden_verbs") or [])
    stages = catalog.get("stages") or {}
    for step in attempt.get("sequence") or []:
        verb = step.get("verb")
        stage = step.get("stage")
        if verb in forbidden_verbs:
            return "REJECT", "VERB_FORBIDDEN"
        if verb == "CONTEST_RESOLVE" and step.get("actor_kind") != "system":
            return "REJECT", "VERB_FORBIDDEN"
        allowed = (stages.get(stage) or {}).get("verbs") or []
        if verb not in allowed:
            return "REJECT", "VERB_FORBIDDEN"
    return "ACCEPT", None


def check_gc7_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "conflict-catalog.gc7-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "conflict-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "conflict-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC7-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("mutate_catalog") or catalog.get("hp_combat") or catalog.get("character_death"):
        fail("GC7-S0 must not mutate the event catalog or enable HP/death")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_forms"):
        fail("GC7-S0 must not add verbs, events, or forms")
    if catalog.get("event_catalog") != "event-catalog/0.2":
        fail("GC7-S0 must keep event-catalog/0.2")
    if catalog.get("withdraw"):
        fail("GC7-S0 must not add withdraw")
    rfc = (ROOT / "rfcs" / "RFC-0011-contest-rhythm.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0011 must be Accepted after GC7-S0 machine contracts land")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    for form in catalog["forms"]:
        if f'"{form}"' not in types_text:
            fail(f"event-types.0.2.json must still contain {form}")
    if '"HP_DUEL"' in types_text or '"ATTACK"' in types_text:
        fail("event-catalog/0.2 must not grow combat types")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "rhythm-infra-ok.json",
        "attack-verb-forbidden.json",
        "unknown-form-forbidden.json",
        "hidden-leak-forbidden.json",
        "death-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc7-conflict" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc7_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
    ok("GC7-S0 conflict: catalog, rhythm fixtures, RFC-0011 Accepted, event-catalog/0.2 unchanged")


def evaluate_gc7_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    if attempt.get("hp_combat") or attempt.get("auto_move"):
        return "REJECT", "FORBIDDEN", {}
    if attempt.get("disconnect") and catalog.get("idle_withdraws") is False:
        return "REJECT", "FORBIDDEN", {}
    if not attempt.get("contest_exists") or attempt.get("same_world") is False:
        return "REJECT", "NOT_FOUND", {}
    if attempt.get("expected_status") == "OPEN" and attempt.get("contest_status") != "OPEN":
        return "REJECT", "STALE_HEAD", {}
    if attempt.get("contest_status") != "OPEN" or attempt.get("already_withdrawn"):
        return "REJECT", "NOT_FOUND", {}
    if not attempt.get("window_open"):
        return "REJECT", "FORBIDDEN", {}
    role = attempt.get("role")
    if role not in ("declarer", "defender"):
        return "REJECT", "FORBIDDEN", {}
    extra: dict = {"events": [catalog.get("resolve_event") or "CONTEST_RESOLVED"]}
    if role == "declarer":
        extra["settlement"] = catalog.get("declarer_withdraw_outcome") or "ABORTED"
        extra["declarer_stake"] = catalog.get("declarer_stake_on_declarer_withdraw") or "CONSUME"
        extra["defender_stake"] = catalog.get("defender_stake_on_declarer_withdraw") or "RELEASE"
    else:
        extra["settlement"] = catalog.get("defender_withdraw_outcome") or "SUCCESS"
        extra["declarer_stake"] = catalog.get("declarer_stake_on_defender_withdraw") or "CONSUME"
        extra["defender_stake"] = catalog.get("defender_stake_on_defender_withdraw") or "CONSUME"
    return "ACCEPT", None, extra


def check_gc7_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "conflict-catalog.gc7-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "conflict-catalog.gc7-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "conflict-withdraw-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC7-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("hp_combat") or catalog.get("new_events") or catalog.get("new_verbs"):
        fail("GC7-S1 must not enable HP or add verbs/events")
    if catalog.get("auto_move") or catalog.get("idle_withdraws") or catalog.get("refund_fees"):
        fail("GC7-S1 must not auto-MOVE, idle-withdraw, or refund fees")
    if catalog.get("event_catalog") != "event-catalog/0.2":
        fail("GC7-S1 must keep event-catalog/0.2")
    if catalog.get("resolve_event") != "CONTEST_RESOLVED":
        fail("GC7-S1 must settle via CONTEST_RESOLVED")
    rfc = (ROOT / "rfcs" / "RFC-0026-contest-withdraw.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0026 must be Accepted")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if '"ABORTED"' not in types_text:
        fail("event-types.0.2.json must already include ABORTED")
    if "CONTEST_WITHDRAWN" in types_text:
        fail("GC7-S1 must not add CONTEST_WITHDRAWN to frozen 0.2")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "declarer-withdraw-ok.json",
        "defender-withdraw-ok.json",
        "same-cycle-ok.json",
        "founder-own-contest-ok.json",
        "nonparticipant-forbidden.json",
        "settled-forbidden.json",
        "duplicate-forbidden.json",
        "stale-forbidden.json",
        "cross-world-forbidden.json",
        "officer-foreign-forbidden.json",
        "disconnect-not-withdraw.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc7-withdraw" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc7_s1(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("settlement") and extra.get("settlement") != expected["settlement"]:
            fail(f"{name}: settlement {extra.get('settlement')} expected {expected['settlement']}")
        if expected.get("declarer_stake") and extra.get("declarer_stake") != expected["declarer_stake"]:
            fail(f"{name}: declarer_stake mismatch")
        if expected.get("defender_stake") and extra.get("defender_stake") != expected["defender_stake"]:
            fail(f"{name}: defender_stake mismatch")
    ok("GC7-S1 withdraw: catalog, attempt fixtures, RFC-0026 Accepted, CONTEST_RESOLVED reused")


def evaluate_gc7_s2(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if attempt.get("office_status") != "OCCUPIED":
        return "REJECT", "FORBIDDEN"
    if attempt.get("same_org_as_other_party"):
        return "REJECT", "FORBIDDEN"
    form = attempt.get("form")
    need = (
        catalog.get("resource_seizure_profile")
        if form == "RESOURCE_SEIZURE"
        else catalog.get("other_forms_profile")
    )
    if attempt.get("office_profile") != need:
        return "REJECT", "FORBIDDEN"
    return "ACCEPT", None


def check_gc7_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "conflict-catalog.gc7-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "conflict-catalog.gc7-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "conflict-attempt.gc7-s2.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC7-S2 catalog invalid: {cerrs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_forms") or catalog.get("hp_combat"):
        fail("GC7-S2 must not add verbs, events, forms, or HP")
    if catalog.get("org_as_declarer_id") or catalog.get("vacant_office_acts") or catalog.get("same_org_both_sides") or catalog.get("help_lists_contest"):
        fail("GC7-S2 must keep Player actor, vacant fail, no same-org both sides, help omits contest")
    rfc = (ROOT / "rfcs" / "RFC-0041-institution-contest-party.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0041 must be Accepted")
    help_org = (ROOT / "docs" / "GC7-S2-INSTITUTION-PARTY.md").read_text(encoding="utf-8")
    if "Chamber help" not in help_org:
        fail("GC7-S2 must keep CONTEST off Chamber help")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-occupied-accept.json",
        "attempt-vacant-reject.json",
        "attempt-wrong-profile.json",
        "attempt-same-org.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc7-institution-party" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc7_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("GC7-S2 institution party: catalog, attempt fixtures, RFC-0041 Accepted")


def evaluate_gc7_s3(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    form = attempt.get("form")
    if form != "INFORMATION_CONTEST":
        return "REJECT", "FORM_FORBIDDEN"
    if attempt.get("hidden_in_projection"):
        return "REJECT", "LEAK"
    if not attempt.get("target_visible"):
        return "REJECT", "NOT_FOUND"
    if attempt.get("target_entity_type") != catalog.get("target_entity_type") or not attempt.get(
        "public_record"
    ):
        return "REJECT", "FORBIDDEN"
    return "ACCEPT", None


def check_gc7_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "conflict-catalog.gc7-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "conflict-catalog.gc7-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "conflict-attempt.gc7-s3.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC7-S3 catalog invalid: {cerrs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("hp_combat"):
        fail("GC7-S3 must not add verbs, events, or HP")
    if catalog.get("new_forms") != ["INFORMATION_CONTEST"]:
        fail("GC7-S3 must add only INFORMATION_CONTEST")
    if catalog.get("mutates_event_catalog_02") or catalog.get("rewrites_archive_claim"):
        fail("GC7-S3 must not mutate event-catalog/0.2 or rewrite archive_claim")
    if catalog.get("help_lists_contest") or catalog.get("hidden_distinct_from_missing"):
        fail("GC7-S3 must keep help off CONTEST and hide/missing as NOT_FOUND")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if '"INFORMATION_CONTEST"' in types_text:
        fail("event-types.0.2.json must not grow INFORMATION_CONTEST")
    rfc = (ROOT / "rfcs" / "RFC-0042-information-contest.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0042 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC7-S3-INFORMATION-CONTEST.md").read_text(encoding="utf-8")
    if "Chamber help" not in slice_doc:
        fail("GC7-S3 must keep CONTEST off Chamber help")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-public-artifact-accept.json",
        "attempt-missing-reject.json",
        "attempt-non-record-reject.json",
        "attempt-information-war-reject.json",
        "attempt-hidden-leak-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc7-information-contest" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason = evaluate_gc7_s3(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("GC7-S3 information contest: catalog, attempt fixtures, RFC-0042 Accepted")


def evaluate_gc7_thaw_play(attempt: dict, catalog: dict) -> tuple[str, bool | None]:
    if attempt.get("operation") == "HELP_CONTEST":
        return "ACCEPT", True if catalog.get("help_contest") else False
    listed = False
    if attempt.get("topic") == "wed":
        listed = bool(catalog.get("help_wed"))
    elif attempt.get("topic") == "attest":
        listed = bool(catalog.get("help_attest"))
    return "ACCEPT", listed


def check_gc7_thaw_play(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "conflict-catalog.gc7-thaw-play.json")
    catalog_schema = load_json(ROOT / "specs" / "conflict-catalog.gc7-thaw-play.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "conflict-attempt.gc7-thaw-play.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC7 thaw-play catalog invalid: {errs[0].message}")
    if (
        not catalog.get("help_contest")
        or catalog.get("help_wed")
        or catalog.get("help_attest")
        or catalog.get("new_verbs")
        or catalog.get("hp_combat")
        or catalog.get("watch_contest")
    ):
        fail("GC7 thaw-play must list CONTEST help and omit WED/ATTEST, new verbs, HP, and WATCH")
    rfc = (ROOT / "rfcs" / "RFC-0095-contest-play-thaw.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0095 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-help-contest.json",
        "attempt-help-commands.json",
        "attempt-omit-wed.json",
        "attempt-omit-attest.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc7-thaw-play" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, listed = evaluate_gc7_thaw_play(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("GC7 PLAY thaw: catalog, attempt fixtures, RFC-0095 Accepted")


def evaluate_diplomacy_s0(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", None, bool(catalog.get("help_agreement"))
    allowed = set(catalog.get("agreement_types") or [])
    typ = str(attempt.get("agreement_type") or "")
    parties = int(attempt.get("party_count") or 0)
    if typ not in allowed:
        return "REJECT", "FORM_FORBIDDEN", None
    if parties < 2:
        return "REJECT", "INVALID_REQUEST", None
    return "ACCEPT", None, None


def check_diplomacy_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "diplomacy-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "diplomacy-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "diplomacy-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"Diplomacy S0 catalog invalid: {errs[0].message}")
    if catalog.get("help_agreement") or catalog.get("help_terminate") or catalog.get("terminate") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("Diplomacy S0 must keep help, terminate, new verbs, and WATCH ticker off")
    if catalog.get("agreement_types") != ["TRADE"]:
        fail("Diplomacy S0 must host TRADE only")
    rfc = (ROOT / "rfcs" / "RFC-0097-diplomacy-trade.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0097 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-form-ok.json",
        "attempt-unknown-type.json",
        "attempt-one-party.json",
        "attempt-omit-help.json",
    ):
        fixture = load_json(ROOT / "examples" / "diplomacy-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_diplomacy_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("Diplomacy S0 TRADE form: catalog, attempt fixtures, RFC-0097 Accepted")


def evaluate_diplomacy_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", None, bool(catalog.get("help_agreement") or catalog.get("help_terminate"))
    if not catalog.get("terminate"):
        return "REJECT", "NOT_IMPLEMENTED", None
    if not attempt.get("has_reason"):
        return "REJECT", "INVALID_REQUEST", None
    if attempt.get("is_party") is False:
        return "REJECT", "FORBIDDEN", None
    if attempt.get("status") and attempt.get("status") != "ACTIVE":
        return "REJECT", "FORBIDDEN", None
    return "ACCEPT", None, None


def check_diplomacy_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "diplomacy-catalog.s1.json")
    catalog_schema = load_json(ROOT / "specs" / "diplomacy-catalog.s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "diplomacy-attempt.s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"Diplomacy S1 catalog invalid: {errs[0].message}")
    if catalog.get("help_agreement") or catalog.get("help_terminate") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("Diplomacy S1 must keep help, new verbs, and WATCH ticker off")
    if not catalog.get("terminate"):
        fail("Diplomacy S1 must host terminate")
    rfc = (ROOT / "rfcs" / "RFC-0098-diplomacy-terminate.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0098 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-terminate-ok.json",
        "attempt-missing-reason.json",
        "attempt-bystander.json",
        "attempt-omit-help.json",
    ):
        fixture = load_json(ROOT / "examples" / "diplomacy-s1" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_diplomacy_s1(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("Diplomacy S1 terminate: catalog, attempt fixtures, RFC-0098 Accepted")


def evaluate_diplomacy_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    allowed = set(catalog.get("agreement_types") or [])
    if attempt.get("operation") == "HELP_AGREEMENT":
        return "ACCEPT", None, bool(catalog.get("help_agreement"))
    if attempt.get("operation") == "HELP_OMIT":
        topic = str(attempt.get("topic") or "")
        if topic == "wed":
            return "ACCEPT", None, bool(catalog.get("help_wed"))
        if topic == "attest":
            return "ACCEPT", None, bool(catalog.get("help_attest"))
        return "ACCEPT", None, False
    typ = str(attempt.get("agreement_type") or "")
    if typ not in allowed:
        return "REJECT", "FORM_FORBIDDEN", None
    return "ACCEPT", None, None


def check_diplomacy_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "diplomacy-catalog.s2.json")
    catalog_schema = load_json(ROOT / "specs" / "diplomacy-catalog.s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "diplomacy-attempt.s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"Diplomacy S2 catalog invalid: {errs[0].message}")
    types = set(catalog.get("agreement_types") or [])
    if types != {"TRADE", "NON_AGGRESSION", "ACCESS", "RESOURCE_COMMITMENT", "MUTUAL_DEFENSE"}:
        fail("Diplomacy S2 must host all five catalog types")
    if not catalog.get("help_agreement") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("Diplomacy S2 must list AGREEMENT help and omit WED/ATTEST, new verbs, and WATCH ticker")
    rfc = (ROOT / "rfcs" / "RFC-0100-diplomacy-closeout.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0100 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-help-agreement.json",
        "attempt-form-types.json",
        "attempt-omit-wed.json",
        "attempt-omit-attest.json",
    ):
        fixture = load_json(ROOT / "examples" / "diplomacy-s2" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_diplomacy_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("Diplomacy S2 closeout: catalog, attempt fixtures, RFC-0100 Accepted")


def evaluate_access_policy_s0(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", None, bool(catalog.get("help_access_policy"))
    scopes = set(catalog.get("scopes") or [])
    modes = set(catalog.get("modes") or [])
    if str(attempt.get("scope") or "") not in scopes:
        return "REJECT", "FORM_FORBIDDEN", None
    if str(attempt.get("mode") or "") not in modes:
        return "REJECT", "FORM_FORBIDDEN", None
    if catalog.get("acting_for_required") and attempt.get("acting_for") is False:
        return "REJECT", "FORBIDDEN", None
    if attempt.get("has_grant") is False:
        return "REJECT", "FORBIDDEN", None
    return "ACCEPT", None, None


def check_access_policy_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "access-policy-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "access-policy-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "access-policy-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"ACCESS_POLICY S0 catalog invalid: {errs[0].message}")
    if catalog.get("help_access_policy") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("ACCESS_POLICY S0 must omit help, WED/ATTEST, new verbs, and WATCH ticker")
    if catalog.get("scopes") != ["EXIT"] or set(catalog.get("modes") or []) != {"DENY", "CLEAR"}:
        fail("ACCESS_POLICY S0 must host EXIT DENY/CLEAR only")
    if catalog.get("authority_profile") != "GRANT_ACCESS" or not catalog.get("acting_for_required"):
        fail("ACCESS_POLICY S0 must require GRANT_ACCESS via acting_for")
    rfc = (ROOT / "rfcs" / "RFC-0101-access-policy.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0101 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-deny-ok.json",
        "attempt-no-grant.json",
        "attempt-allow-only.json",
        "attempt-omit-help.json",
    ):
        fixture = load_json(ROOT / "examples" / "access-policy-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_access_policy_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("ACCESS_POLICY S0: catalog, attempt fixtures, RFC-0101 Accepted")


def evaluate_access_policy_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", None, bool(catalog.get("help_access_policy"))
    scopes = set(catalog.get("scopes") or [])
    modes = set(catalog.get("modes") or [])
    if str(attempt.get("scope") or "") not in scopes:
        return "REJECT", "FORM_FORBIDDEN", None
    if str(attempt.get("mode") or "") not in modes:
        return "REJECT", "FORM_FORBIDDEN", None
    if catalog.get("acting_for_required") and attempt.get("acting_for") is False:
        return "REJECT", "FORBIDDEN", None
    if attempt.get("has_grant") is False:
        return "REJECT", "FORBIDDEN", None
    return "ACCEPT", None, None


def check_access_policy_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "access-policy-catalog.s1.json")
    catalog_schema = load_json(ROOT / "specs" / "access-policy-catalog.s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "access-policy-attempt.s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"ACCESS_POLICY S1 catalog invalid: {errs[0].message}")
    if catalog.get("help_access_policy") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("ACCESS_POLICY S1 must omit help, WED/ATTEST, new verbs, and WATCH ticker")
    if set(catalog.get("scopes") or []) != {"EXIT", "ROOM"} or set(catalog.get("modes") or []) != {"DENY", "CLEAR"}:
        fail("ACCESS_POLICY S1 must host EXIT and ROOM DENY/CLEAR")
    if catalog.get("authority_profile") != "GRANT_ACCESS" or not catalog.get("acting_for_required"):
        fail("ACCESS_POLICY S1 must require GRANT_ACCESS via acting_for")
    rfc = (ROOT / "rfcs" / "RFC-0102-access-policy-room.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0102 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-room-ok.json",
        "attempt-exit-ok.json",
        "attempt-allow-only.json",
        "attempt-omit-help.json",
    ):
        fixture = load_json(ROOT / "examples" / "access-policy-s1" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_access_policy_s1(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("ACCESS_POLICY S1: catalog, attempt fixtures, RFC-0102 Accepted")


def evaluate_access_policy_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", None, bool(catalog.get("help_access_policy"))
    scopes = set(catalog.get("scopes") or [])
    modes = set(catalog.get("modes") or [])
    if str(attempt.get("scope") or "") not in scopes:
        return "REJECT", "FORM_FORBIDDEN", None
    if str(attempt.get("mode") or "") not in modes:
        return "REJECT", "FORM_FORBIDDEN", None
    if catalog.get("acting_for_required") and attempt.get("acting_for") is False:
        return "REJECT", "FORBIDDEN", None
    if attempt.get("has_grant") is False:
        return "REJECT", "FORBIDDEN", None
    if str(attempt.get("mode") or "") == "ALLOW_ONLY" and catalog.get("allow_only_requires_named_list") and attempt.get("named_list") is False:
        return "REJECT", "INVALID_REQUEST", None
    return "ACCEPT", None, None


def check_access_policy_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "access-policy-catalog.s2.json")
    catalog_schema = load_json(ROOT / "specs" / "access-policy-catalog.s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "access-policy-attempt.s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"ACCESS_POLICY S2 catalog invalid: {errs[0].message}")
    if catalog.get("help_access_policy") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("ACCESS_POLICY S2 must omit help, WED/ATTEST, new verbs, and WATCH ticker")
    if set(catalog.get("scopes") or []) != {"EXIT", "ROOM"} or set(catalog.get("modes") or []) != {"DENY", "CLEAR", "ALLOW_ONLY"}:
        fail("ACCESS_POLICY S2 must host EXIT/ROOM DENY/CLEAR/ALLOW_ONLY")
    if catalog.get("authority_profile") != "GRANT_ACCESS" or not catalog.get("acting_for_required"):
        fail("ACCESS_POLICY S2 must require GRANT_ACCESS via acting_for")
    if not catalog.get("allow_only_requires_named_list"):
        fail("ACCESS_POLICY S2 must require a named list for ALLOW_ONLY")
    rfc = (ROOT / "rfcs" / "RFC-0103-access-policy-allow-only.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0103 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-allow-ok.json",
        "attempt-allow-star.json",
        "attempt-deny-ok.json",
        "attempt-omit-help.json",
    ):
        fixture = load_json(ROOT / "examples" / "access-policy-s2" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, listed = evaluate_access_policy_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
    ok("ACCESS_POLICY S2: catalog, attempt fixtures, RFC-0103 Accepted")


def evaluate_access_policy_s3(attempt: dict, catalog: dict) -> tuple[str, bool | None, bool | None]:
    if attempt.get("operation") == "HELP_OMIT":
        return "ACCEPT", False, None
    listed = bool(catalog.get("help_access"))
    schema = bool(catalog.get("help_access_policy"))
    return "ACCEPT", listed, schema


def check_access_policy_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "access-policy-catalog.s3.json")
    catalog_schema = load_json(ROOT / "specs" / "access-policy-catalog.s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "access-policy-attempt.s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"ACCESS_POLICY S3 catalog invalid: {errs[0].message}")
    if not catalog.get("help_access") or catalog.get("help_access_policy") or catalog.get("help_wed") or catalog.get("help_attest") or catalog.get("new_verbs") or catalog.get("watch_ticker"):
        fail("ACCESS_POLICY S3 must list ACCESS help and omit schema name, WED/ATTEST, new verbs, and WATCH ticker")
    rfc = (ROOT / "rfcs" / "RFC-0104-access-policy-help.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0104 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-help-access.json",
        "attempt-help-topic.json",
        "attempt-omit-wed.json",
        "attempt-omit-attest.json",
    ):
        fixture = load_json(ROOT / "examples" / "access-policy-s3" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, listed, schema = evaluate_access_policy_s3(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("listed") is not None and listed != exp["listed"]:
            fail(f"{name}: listed {listed} expected {exp['listed']}")
        if exp.get("schema_name") is not None and schema != exp["schema_name"]:
            fail(f"{name}: schema_name {schema} expected {exp['schema_name']}")
    ok("ACCESS_POLICY S3: catalog, attempt fixtures, RFC-0104 Accepted")


ORIENT_MAX_ACTIONS = 8
ORIENT_STRAIN_CONDITION = 70
ORIENT_FORBIDDEN = (
    (re.compile(r"point of the game|win the game|\bvictory\b|your goal is|the point is"), "THESIS"),
    (re.compile(r"you should (repair|trade|organize)"), "YOU_SHOULD"),
    (re.compile(r"being tested|research objective|\bbenchmark\b|capability x"), "RESEARCH"),
    (re.compile(r"you are an (engineer|surveyor|explorer|broker)|assigned class|your office is"), "CLASS"),
    (re.compile(r"the world remembers|this place keeps what you do"), "MEMORY"),
    (re.compile(r"welcome, agent|you have arrived"), "ARRIVAL_SPEECH"),
)


def _orient_blob(attempt: dict) -> str:
    obs = attempt.get("observation") or {}
    loc = obs.get("location") or {}
    parts = [
        loc.get("name") or "",
        loc.get("description") or "",
        str(loc.get("condition") or obs.get("condition") or ""),
        " ".join(obs.get("report_lines") or []),
        " ".join(obs.get("orientation_lines") or []),
        " ".join(obs.get("available_actions") or []),
    ]
    return " ".join(parts).lower()


def room_has_strain(obs: dict) -> bool:
    loc = obs.get("location") or {}
    cond = loc.get("condition") if "condition" in loc else obs.get("condition")
    if isinstance(cond, (int, float)) and cond < ORIENT_STRAIN_CONDITION:
        return True
    if isinstance(cond, str) and cond.strip():
        return True
    if obs.get("stock_amount") == 0:
        return True
    if obs.get("report_lines"):
        return True
    return False


def evaluate_agent_orientation_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if catalog.get("arrival_speech") or catalog.get("invent_strain") or not catalog.get("thesis_forbidden"):
        return "REJECT", "CATALOG"
    if catalog.get("new_verbs") or catalog.get("new_events"):
        return "REJECT", "CATALOG"
    if attempt.get("arrival_speech"):
        return "REJECT", "ARRIVAL_SPEECH"
    obs = attempt.get("observation") or {}
    loc = obs.get("location") or {}
    if not (loc.get("name") or loc.get("description")):
        return "REJECT", "NO_LOCATION"
    actions = list(obs.get("available_actions") or [])
    cap = int(catalog.get("max_available_actions") or ORIENT_MAX_ACTIONS)
    if attempt.get("verb_dump") or len(actions) > cap:
        return "REJECT", "VERB_DUMP"
    if attempt.get("strain_claimed") and not room_has_strain(obs):
        return "REJECT", "INVENTED_STRAIN"
    blob = _orient_blob(attempt)
    for rx, reason in ORIENT_FORBIDDEN:
        if rx.search(blob):
            return "REJECT", reason
    return "ACCEPT", None


def check_agent_orientation_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "agent-orientation-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "agent-orientation-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "agent-orientation-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"agent-orientation S0 catalog invalid: {errs[0].message}")
    if catalog.get("arrival_speech") or catalog.get("invent_strain") or not catalog.get("thesis_forbidden"):
        fail("agent-orientation S0 must forbid arrival speech, invented strain, and thesis")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("agent-orientation S0 must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0106-agent-orientation.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0106 must be Accepted")
    slice_doc = (ROOT / "docs" / "AGENT-ORIENTATION-S0.md").read_text(encoding="utf-8")
    if "arrival" not in slice_doc.lower() or "invent" not in slice_doc.lower() or "later" not in slice_doc.lower():
        fail("AGENT-ORIENTATION-S0 must pin live-room, no arrival/invented strain, persistence later")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-location-ok.json",
        "attempt-strain-present.json",
        "attempt-quiet-room.json",
        "attempt-thesis-reject.json",
        "attempt-you-should-reject.json",
        "attempt-class-reject.json",
        "attempt-research-reject.json",
        "attempt-arrival-reject.json",
        "attempt-verb-dump-reject.json",
        "attempt-invented-strain-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "agent-orientation-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_agent_orientation_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("agent-orientation S0: catalog, attempt fixtures, RFC-0106 Accepted")


def evaluate_agent_orientation_s1(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if not catalog.get("situation_fields"):
        return "REJECT", "CATALOG"
    base, reason = evaluate_agent_orientation_s0(attempt, catalog)
    if base == "REJECT":
        return base, reason
    obs = attempt.get("observation") or {}
    loc = obs.get("location") or {}
    sit = obs.get("situation") or {}
    place = sit.get("place")
    if not (isinstance(place, str) and place.strip()):
        return "REJECT", "MISSING_PLACE"
    if place != (loc.get("name") or ""):
        return "REJECT", "PLACE_MISMATCH"
    strain = sit.get("strain")
    has = room_has_strain(obs)
    if has and not (isinstance(strain, str) and strain.strip()):
        return "REJECT", "MISSING_STRAIN"
    if not has and strain:
        return "REJECT", "INVENTED_STRAIN"
    blob = f"{place} {strain or ''}".lower()
    for rx, why in ORIENT_FORBIDDEN:
        if rx.search(blob):
            return "REJECT", why
    return "ACCEPT", None


def check_agent_orientation_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "agent-orientation-catalog.s1.json")
    catalog_schema = load_json(ROOT / "specs" / "agent-orientation-catalog.s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "agent-orientation-attempt.s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"agent-orientation S1 catalog invalid: {errs[0].message}")
    if not catalog.get("situation_fields"):
        fail("agent-orientation S1 must enable situation_fields")
    if catalog.get("arrival_speech") or catalog.get("invent_strain") or not catalog.get("thesis_forbidden"):
        fail("agent-orientation S1 must keep S0 withhold flags")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("agent-orientation S1 must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0107-agent-orientation-situation.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0107 must be Accepted")
    slice_doc = (ROOT / "docs" / "AGENT-ORIENTATION-S1.md").read_text(encoding="utf-8")
    if "situation.place" not in slice_doc or "omit" not in slice_doc.lower():
        fail("AGENT-ORIENTATION-S1 must pin situation.place and omit strain when quiet")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-place-ok.json",
        "attempt-strain-present.json",
        "attempt-quiet-omit-strain.json",
        "attempt-missing-place-reject.json",
        "attempt-invented-strain-reject.json",
        "attempt-thesis-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "agent-orientation-s1" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_agent_orientation_s1(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("agent-orientation S1: catalog, attempt fixtures, RFC-0107 Accepted")


def evaluate_agent_orientation_s2(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if catalog.get("connect_thesis") or catalog.get("skill_thesis") or not catalog.get("thesis_forbidden"):
        return "REJECT", "CATALOG"
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("arrival_speech"):
        return "REJECT", "CATALOG"
    blob = str(attempt.get("text") or "").lower()
    for rx, why in ORIENT_FORBIDDEN:
        if rx.search(blob):
            return "REJECT", why
    return "ACCEPT", None


def check_agent_orientation_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "agent-orientation-catalog.s2.json")
    catalog_schema = load_json(ROOT / "specs" / "agent-orientation-catalog.s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "agent-orientation-attempt.s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"agent-orientation S2 catalog invalid: {errs[0].message}")
    if catalog.get("connect_thesis") or catalog.get("skill_thesis"):
        fail("agent-orientation S2 must forbid CONNECT and skill theses")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("agent-orientation S2 must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0108-agent-orientation-connect.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0108 must be Accepted")
    slice_doc = (ROOT / "docs" / "AGENT-ORIENTATION-S2.md").read_text(encoding="utf-8")
    if "CONNECT" not in slice_doc or "skill" not in slice_doc.lower():
        fail("AGENT-ORIENTATION-S2 must pin CONNECT and skill withhold")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-connect-ok.json",
        "attempt-bootstrap-ok.json",
        "attempt-connect-thesis-reject.json",
        "attempt-email-should-reject.json",
        "attempt-skill-research-reject.json",
        "attempt-json-arrival-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "agent-orientation-s2" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_agent_orientation_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("agent-orientation S2: catalog, attempt fixtures, RFC-0108 Accepted")


def evaluate_human_orientation_s0(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if catalog.get("arrival_speech") or catalog.get("tutorial_room") or catalog.get("class_picker"):
        return "REJECT", "CATALOG"
    if not catalog.get("thesis_forbidden") or catalog.get("new_verbs") or catalog.get("new_events"):
        return "REJECT", "CATALOG"
    blob = str(attempt.get("text") or "").lower()
    for rx, why in ORIENT_FORBIDDEN:
        if rx.search(blob):
            return "REJECT", why
    return "ACCEPT", None


def check_human_orientation_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "human-orientation-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "human-orientation-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "human-orientation-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"human-orientation S0 catalog invalid: {errs[0].message}")
    if catalog.get("tutorial_room") or catalog.get("class_picker") or catalog.get("arrival_speech"):
        fail("human-orientation S0 must forbid tutorial room, class picker, and arrival speech")
    if catalog.get("new_verbs") or catalog.get("new_events") or not catalog.get("thesis_forbidden"):
        fail("human-orientation S0 must not add verbs or events and must forbid a thesis")
    rfc = (ROOT / "rfcs" / "RFC-0109-human-orientation.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0109 must be Accepted")
    slice_doc = (ROOT / "docs" / "HUMAN-ORIENTATION-S0.md").read_text(encoding="utf-8")
    if "first" not in slice_doc.lower() or "thesis" not in slice_doc.lower():
        fail("HUMAN-ORIENTATION-S0 must pin first-read thesis withhold")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-door-ok.json",
        "attempt-chamber-ok.json",
        "attempt-door-thesis-reject.json",
        "attempt-play-should-reject.json",
        "attempt-callback-research-reject.json",
        "attempt-chamber-arrival-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "human-orientation-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_human_orientation_s0(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("human-orientation S0: catalog, attempt fixtures, RFC-0109 Accepted")


FORBIDDEN_HARNESS_PLAYER_CLASSES = {"AGENT_PLAYER", "BOT_PLAYER", "AUTONOMOUS_PLAYER"}


def evaluate_agent_harness(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if catalog.get("browser_canonical") or catalog.get("token_in_model_context"):
        return "REJECT", "CATALOG"
    if catalog.get("chain_of_thought_required") or catalog.get("harness_is_world_authority"):
        return "REJECT", "CATALOG"
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_player_classes"):
        return "REJECT", "CATALOG"
    if not catalog.get("provider_neutral") or not catalog.get("affordance_first"):
        return "REJECT", "CATALOG"
    if not catalog.get("server_final_authority") or not catalog.get("circuit_breaker_required"):
        return "REJECT", "CATALOG"
    if not catalog.get("prompt_injection_boundary") or not catalog.get("player_parity"):
        return "REJECT", "CATALOG"
    if catalog.get("pacing_default") != "TURN":
        return "REJECT", "CATALOG"
    player_class = attempt.get("player_class")
    if player_class in FORBIDDEN_HARNESS_PLAYER_CLASSES:
        return "REJECT", "ONTOLOGY"
    if attempt.get("browser_as_canonical"):
        return "REJECT", "BROWSER_NONCANONICAL"
    if attempt.get("secrets_in_model_context"):
        return "REJECT", "TOKEN_SECRECY"
    if attempt.get("requires_chain_of_thought"):
        return "REJECT", "NO_COT"
    if attempt.get("harness_as_world_authority"):
        return "REJECT", "SERVER_AUTHORITY"
    if attempt.get("adds_hidden_fact"):
        return "REJECT", "HIDDEN_FACT"
    if attempt.get("treats_world_text_as_instruction"):
        return "REJECT", "INJECTION"
    proposal = attempt.get("proposal") or {}
    mutating = bool(proposal.get("mutating"))
    status = attempt.get("world_status") or "ACTIVE"
    if mutating and status == "PAUSED":
        return "REJECT", "WORLD_PAUSED"
    if mutating and status == "INCIDENT":
        return "REJECT", "WORLD_INCIDENT"
    if mutating and status in ("ARCHIVED", "PREVIEW"):
        return "REJECT", "WORLD_NOT_READY"
    if attempt.get("new_verb"):
        return "REJECT", "INVALID_PROPOSAL"
    action = proposal.get("action")
    if action:
        available = attempt.get("available_actions") or []
        if action not in available:
            return "REJECT", "INVALID_PROPOSAL"
        target = proposal.get("target_id")
        if target:
            visible = attempt.get("visible_targets") or []
            if target not in visible:
                return "REJECT", "INVALID_PROPOSAL"
    return "ACCEPT", None


def check_agent_harness(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "agent-harness-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "agent-harness-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "agent-harness-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"agent-harness catalog invalid: {errs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_player_classes"):
        fail("agent-harness must not add verbs, events, or Player classes")
    if catalog.get("browser_canonical") or catalog.get("token_in_model_context"):
        fail("agent-harness must forbid browser-canonical play and tokens in model context")
    if catalog.get("chain_of_thought_required") or catalog.get("harness_is_world_authority"):
        fail("agent-harness must not require chain-of-thought or claim world authority")
    if not catalog.get("provider_neutral") or not catalog.get("affordance_first"):
        fail("agent-harness must be provider-neutral and affordance-first")
    if not catalog.get("server_final_authority") or not catalog.get("circuit_breaker_required"):
        fail("agent-harness must keep server authority and require a circuit breaker")
    if not catalog.get("prompt_injection_boundary") or not catalog.get("player_parity"):
        fail("agent-harness must pin prompt-injection boundary and Player parity")
    if catalog.get("pacing_default") != "TURN":
        fail("agent-harness first-world pacing default must be TURN")
    rfc = (ROOT / "rfcs" / "RFC-0111-agent-harness.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0111 must be Accepted")
    doc = (ROOT / "docs" / "AGENT-HARNESS.md").read_text(encoding="utf-8")
    for token in (
        "The model proposes. The harness constrains and transports. NOEMA decides.",
        "POST /v1/command",
        "NOEMA_TOKEN",
        "AGENT_PLAYER",
        "AVAILABLE_ACTIONS",
        "TURN",
        "Circuit breaker",
    ):
        if token not in doc:
            fail(f"AGENT-HARNESS.md must pin {token!r}")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-valid-repair.json",
        "attempt-invented-verb.json",
        "attempt-token-in-prompt.json",
        "attempt-browser-canonical.json",
        "attempt-agent-player-class.json",
        "attempt-world-text-injection.json",
        "attempt-hidden-fact.json",
        "attempt-harness-as-authority.json",
        "attempt-cot-required.json",
        "attempt-paused-mutate.json",
        "attempt-incident-mutate.json",
        "attempt-unknown-target.json",
    ):
        fixture = load_json(ROOT / "examples" / "agent-harness-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_agent_harness(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("agent-harness S0: catalog, attempt fixtures, RFC-0111 Accepted")


SEAL_HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def evaluate_sealed_prompt_text(text: str) -> tuple[str, str | None]:
    blob = str(text or "").lower()
    for rx, why in ORIENT_FORBIDDEN:
        if rx.search(blob):
            return "REJECT", why
    return "ACCEPT", None


def evaluate_sealed_attach(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if attempt.get("operation") == "PROMPT_WITHHOLD":
        return evaluate_sealed_prompt_text(str(attempt.get("prompt_text") or ""))
    if not catalog.get("live_required") or catalog.get("isolated_required"):
        return "REJECT", "CATALOG"
    if attempt.get("prompt_text"):
        return "REJECT", "PROMPT_ON_WIRE"
    tenant = attempt.get("tenant")
    controller = attempt.get("controller_type")
    if tenant == "isolated" or controller == "human":
        return "ACCEPT", None
    presented = attempt.get("prompt_version_hash")
    if not presented:
        return "REJECT", "SEAL_REQUIRED"
    accepted = {row.get("prompt_version_hash") for row in (catalog.get("accepted_seals") or [])}
    if not SEAL_HASH_RE.match(str(presented)) or presented not in accepted:
        return "REJECT", "SEAL_MISMATCH"
    return "ACCEPT", None


def check_sealed_live_attach(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "sealed-prompt-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "sealed-prompt-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "sealed-attach-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"sealed-prompt catalog invalid: {errs[0].message}")
    if not catalog.get("live_required") or catalog.get("isolated_required"):
        fail("sealed-live-attach must require live and not require isolated")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("sealed-live-attach must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0115-sealed-live-attach.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0115 must be Accepted")
    slice_doc = (ROOT / "docs" / "AGENT-SEAL-S0.md").read_text(encoding="utf-8")
    for token in ("sealed attach", "isolated", "X-Noema-Seal", "hash"):
        if token.lower() not in slice_doc.lower():
            fail(f"AGENT-SEAL-S0 must pin {token!r}")
    prompt_path = ROOT / str(catalog["prompt_file"])
    if not prompt_path.is_file():
        fail(f"sealed prompt file missing: {catalog['prompt_file']}")
    digest = "sha256:" + hashlib.sha256(prompt_path.read_bytes()).hexdigest()
    accepted = [row.get("prompt_version_hash") for row in (catalog.get("accepted_seals") or [])]
    if digest not in accepted:
        fail(f"catalog hash does not match {catalog['prompt_file']}: {digest}")
    prompt_outcome, prompt_reason = evaluate_sealed_prompt_text(prompt_path.read_text(encoding="utf-8"))
    if prompt_outcome != "ACCEPT":
        fail(f"published sealed prompt withhold failed: {prompt_reason}")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-live-hash-ok.json",
        "attempt-live-missing-reject.json",
        "attempt-live-wrong-reject.json",
        "attempt-isolated-no-hash-ok.json",
        "attempt-human-no-hash-ok.json",
        "attempt-prompt-on-wire-reject.json",
        "attempt-prompt-text-ok.json",
        "attempt-prompt-thesis-reject.json",
    ):
        fixture = load_json(ROOT / "examples" / "sealed-live-attach-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_sealed_attach(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("sealed-live-attach S0: catalog, prompt hash, fixtures, RFC-0115 Accepted")


FORBIDDEN_CLIENT_PLAYER_CLASSES = {
    "AGENT_PLAYER",
    "BOT_PLAYER",
    "AUTONOMOUS_PLAYER",
    "CLIENT_PLAYER",
    "NOEMA_AGENT_PLAYER",
}


def evaluate_official_agent_client(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_player_classes"):
        return "REJECT", "CATALOG"
    if catalog.get("browser_canonical") or catalog.get("client_is_world_authority"):
        return "REJECT", "CATALOG"
    if not catalog.get("provider_neutral") or not catalog.get("discovery_first"):
        return "REJECT", "CATALOG"
    if not catalog.get("seal_fail_closed") or not catalog.get("copy_first"):
        return "REJECT", "CATALOG"
    if not catalog.get("admin_secrets_forbidden") or catalog.get("mcp_required"):
        return "REJECT", "CATALOG"
    if not catalog.get("operator_brief_flags_forbidden"):
        return "REJECT", "CATALOG"
    if catalog.get("official_repo") != "scrimshawlife-ctrl/noema-client":
        return "REJECT", "CATALOG"
    repo = attempt.get("official_repo")
    if repo is not None and repo != "scrimshawlife-ctrl/noema-client":
        return "REJECT", "REPO"
    player_class = attempt.get("player_class")
    if player_class in FORBIDDEN_CLIENT_PLAYER_CLASSES:
        return "REJECT", "ONTOLOGY"
    if attempt.get("client_is_world_authority"):
        return "REJECT", "SERVER_AUTHORITY"
    if attempt.get("browser_as_canonical"):
        return "REJECT", "BROWSER_NONCANONICAL"
    if attempt.get("stores_admin_secret"):
        return "REJECT", "LEAST_PRIVILEGE"
    if attempt.get("operator_brief_flags"):
        return "REJECT", "SEAL"
    if attempt.get("delete_internal_first"):
        return "REJECT", "COPY_FIRST"
    if attempt.get("perihelion_ci"):
        return "REJECT", "NO_LIVE_CI"
    if attempt.get("skill_teaches_strategy"):
        return "REJECT", "SKILL_STRATEGY"
    if attempt.get("skip_discovery"):
        return "REJECT", "DISCOVERY"
    if attempt.get("mcp_required") or attempt.get("provider_required"):
        return "REJECT", "PROVIDER"
    return "ACCEPT", None


def check_official_agent_client(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "official-agent-client-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "official-agent-client-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "official-agent-client-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"official-agent-client catalog invalid: {errs[0].message}")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_player_classes"):
        fail("official-agent-client must not add verbs, events, or Player classes")
    if catalog.get("official_repo") != "scrimshawlife-ctrl/noema-client":
        fail("official-agent-client must name scrimshawlife-ctrl/noema-client")
    rfc = (ROOT / "rfcs" / "RFC-0116-official-agent-client.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0116 must be Accepted")
    doc = (ROOT / "docs" / "OFFICIAL-AGENT-CLIENT.md").read_text(encoding="utf-8")
    for token in (
        "scrimshawlife-ctrl/noema-client",
        "NOEMA owns world authority",
        "human authorization surface",
        "pipx install noema-client",
        "noema connect",
        "GET /.well-known/noema-agent.json",
        "AGENT_PLAYER",
        "CLIENT_PLAYER",
        "COPY / REFACTOR",
    ):
        if token not in doc:
            fail(f"OFFICIAL-AGENT-CLIENT.md must pin {token!r}")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-valid-repo.json",
        "attempt-client-player-class.json",
        "attempt-client-world-authority.json",
        "attempt-browser-canonical.json",
        "attempt-admin-secret.json",
        "attempt-operator-brief.json",
        "attempt-delete-internal-first.json",
        "attempt-perihelion-ci.json",
        "attempt-skill-strategy.json",
        "attempt-skip-discovery.json",
    ):
        fixture = load_json(ROOT / "examples" / "official-agent-client-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_official_agent_client(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("official-agent-client S0: catalog, attempt fixtures, RFC-0116 Accepted")


def evaluate_gc8_s0(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    claimed = attempt.get("claimed") or {}
    if claimed.get("mastery_yield_bonus") or (
        attempt.get("recognition") not in (None, "none") and int(attempt.get("harvest_amount") or 1) > 1
    ):
        return "REJECT", "BONUS_FORBIDDEN", None
    for flag in (
        "currency",
        "order_book",
        "global_price_index",
        "v06b",
        "wallet",
        "crypto",
    ):
        if claimed.get(flag):
            return "REJECT", "FEATURE_FORBIDDEN", None
    rooms = int(attempt.get("rooms") or 0)
    hops = int(attempt.get("hops") or 0)
    harvest_e = int(catalog["harvest_energy"])
    move_e = int(catalog["move_energy"])
    pattern = attempt.get("pattern")
    if pattern == "pair":
        return "ACCEPT", None, rooms * harvest_e
    if pattern == "lone":
        return "ACCEPT", None, rooms * harvest_e + hops * move_e
    return "REJECT", "FEATURE_FORBIDDEN", None


def check_gc8_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "economy-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "economy-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC8-S0 catalog invalid: {cerrs[0].message}")
    for flag in (
        "currency",
        "order_book",
        "global_price_index",
        "v06b",
        "mastery_yield_bonus",
        "lot_quality",
        "storage_loss",
        "wallet",
        "crypto",
        "npc_shop",
    ):
        if catalog.get(flag):
            fail(f"GC8-S0 must not enable {flag}")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC8-S0 must not add verbs or events")
    if catalog.get("trade_requires_colocation"):
        fail("GC8-S0 must keep TRADE remote (existing v0.1 contract)")
    if int(catalog.get("harvest_energy") or 0) != 2 or int(catalog.get("move_energy") or 0) != 1:
        fail("GC8-S0 must reuse existing HARVEST/MOVE energy costs")
    rfc = (ROOT / "rfcs" / "RFC-0012-distance-interdependence.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0012 must be Accepted after GC8-S0 machine contracts land")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "pair-two-rooms-ok.json",
        "lone-one-hop-ok.json",
        "yield-bonus-forbidden.json",
        "currency-forbidden.json",
        "order-book-forbidden.json",
        "wallet-forbidden.json",
    ]
    energies = {}
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc8-economy" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, energy = evaluate_gc8_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("energy") is not None and energy != expected["energy"]:
            fail(f"{name}: energy {energy} expected {expected['energy']}")
        energies[name] = energy
    if energies["pair-two-rooms-ok.json"] >= energies["lone-one-hop-ok.json"]:
        fail("pair energy must be strictly less than lone energy on one hop")
    ok("GC8-S0 economy: catalog, pair-vs-lone fixtures, RFC-0012 Accepted, no currency/v0.6B")


def evaluate_gc8_s1(attempt: dict, catalog: dict) -> dict:
    if attempt.get("claimed_yield_bonus"):
        return {"grade": "SOUND", "storage_cost": -1}
    worn_below = int(catalog["worn_below_condition"])
    extra = int(catalog["worn_construct_storage_extra"])
    op = attempt.get("operation")
    if op == "HARVEST":
        cond = int(attempt.get("node_condition") or 100)
        grade = "WORN" if cond < worn_below else "SOUND"
        return {"grade": grade, "storage_cost": 0}
    if op == "MIX":
        grade = "WORN" if "WORN" in (attempt.get("have_grade"), attempt.get("add_grade")) else "SOUND"
        return {"grade": grade, "storage_cost": 0}
    base = int(attempt.get("base_storage") or 0)
    grade = attempt.get("storage_grade") or "SOUND"
    cost = base + extra if grade == "WORN" else base
    return {"grade": grade, "storage_cost": cost}


def check_gc8_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "economy-catalog.gc8-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "economy-attempt.gc8-s1.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC8-S1 catalog invalid: {errs[0].message}")
    if catalog.get("currency") or catalog.get("mastery_yield_bonus") or catalog.get("provenance"):
        fail("GC8-S1 must not add currency, yield bonus, or provenance")
    if catalog.get("new_verbs") or catalog.get("grades") != ["SOUND", "WORN"]:
        fail("GC8-S1 must keep two grades and no new verbs")
    if catalog.get("worn_below_condition") != 50 or catalog.get("worn_construct_storage_extra") != 1:
        fail("GC8-S1 pins must be worn < 50 and construct +1 storage")
    rfc = (ROOT / "rfcs" / "RFC-0045-lot-quality.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0045 must be Accepted")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-worn-harvest.json",
        "attempt-sound-harvest.json",
        "attempt-mix-worn.json",
        "attempt-worn-construct.json",
        "attempt-sound-construct.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc8-lot-quality" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc8_s1(fixture, catalog)
        exp = fixture["expected"]
        if got["grade"] != exp["grade"] or got["storage_cost"] != exp["storage_cost"]:
            fail(f"{name}: got {got} expected {exp}")
    ok("GC8-S1 lot quality: catalog, attempt fixtures, RFC-0045 Accepted")


def evaluate_gc8_s2(attempt: dict, catalog: dict) -> dict:
    if attempt.get("operation") == "HARVEST":
        if attempt.get("room_hidden") or catalog.get("hidden_stamp"):
            return {"origin_room_id": None}
        return {"origin_room_id": attempt.get("room_id")}
    have = attempt.get("have_room_id")
    add = attempt.get("add_room_id")
    if catalog.get("mix_policy") == "clear" and have and add and have != add:
        return {"origin_room_id": None}
    return {"origin_room_id": add or have}


def check_gc8_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "economy-catalog.gc8-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "economy-attempt.gc8-s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC8-S2 catalog invalid: {errs[0].message}")
    if catalog.get("hidden_stamp") or catalog.get("watch_origins") or catalog.get("new_verbs"):
        fail("GC8-S2 must not stamp hidden rooms, WATCH origins, or new verbs")
    rfc = (ROOT / "rfcs" / "RFC-0046-lot-provenance.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0046 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC8-S2-PROVENANCE.md").read_text(encoding="utf-8")
    if "Hidden" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC8-S2 must keep hidden stamps off and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-public-stamp.json",
        "attempt-hidden-clear.json",
        "attempt-mix-clear.json",
        "attempt-same-keep.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc8-provenance" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc8_s2(fixture, catalog)
        exp = fixture["expected"]
        if got["origin_room_id"] != exp["origin_room_id"]:
            fail(f"{name}: got {got} expected {exp}")
    ok("GC8-S2 lot provenance: catalog, attempt fixtures, RFC-0046 Accepted")


def evaluate_gc8_s3(attempt: dict, catalog: dict) -> dict:
    amount = int(attempt.get("amount") or 0)
    grade = attempt.get("grade")
    if grade == "WORN" and catalog.get("storage_loss") and catalog.get("worn_only"):
        loss = int(catalog.get("spoil_per_cycle") or 1)
        remaining = max(0, amount - loss)
        return {"loss": loss if amount else 0, "remaining": remaining, "grade": None if remaining <= 0 else "WORN"}
    return {"loss": 0, "remaining": amount, "grade": grade}


def check_gc8_s3(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s3.json")
    catalog_schema = load_json(ROOT / "specs" / "economy-catalog.gc8-s3.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "economy-attempt.gc8-s3.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC8-S3 catalog invalid: {errs[0].message}")
    if catalog.get("currency") or catalog.get("transport_table") or catalog.get("new_verbs"):
        fail("GC8-S3 must not add currency, a transport table, or new verbs")
    if catalog.get("watch_spoilage") or not catalog.get("worn_only") or catalog.get("spoil_per_cycle") != 1:
        fail("GC8-S3 must spoil WORN by 1 and keep WATCH silent")
    rfc = (ROOT / "rfcs" / "RFC-0047-lot-spoilage.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0047 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC8-S3-SPOILAGE.md").read_text(encoding="utf-8")
    if "WORN" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC8-S3 must keep SOUND stable and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-worn-spoil.json",
        "attempt-sound-keep.json",
        "attempt-worn-exhaust.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc8-spoilage" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc8_s3(fixture, catalog)
        exp = fixture["expected"]
        if got["loss"] != exp["loss"] or got["remaining"] != exp["remaining"] or got["grade"] != exp["grade"]:
            fail(f"{name}: got {got} expected {exp}")
    ok("GC8-S3 lot spoilage: catalog, attempt fixtures, RFC-0047 Accepted")


def evaluate_gc8_s4(attempt: dict, catalog: dict) -> dict:
    storage = int(attempt.get("storage") or 0)
    base = int(catalog.get("move_base_energy") or 1)
    extra = int(catalog.get("move_cargo_extra") or 1)
    threshold = int(catalog.get("cargo_below_storage") or 16)
    carrying = storage < threshold
    return {"move_energy": base + extra if carrying else base, "carrying": carrying}


def check_gc8_s4(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s4.json")
    catalog_schema = load_json(ROOT / "specs" / "economy-catalog.gc8-s4.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "economy-attempt.gc8-s4.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC8-S4 catalog invalid: {errs[0].message}")
    if catalog.get("currency") or catalog.get("route_link") or catalog.get("new_verbs"):
        fail("GC8-S4 must not add currency, route_link freight, or new verbs")
    if catalog.get("watch_cargo") or catalog.get("move_base_energy") != 1 or catalog.get("move_cargo_extra") != 1:
        fail("GC8-S4 must keep empty MOVE 1, cargo +1, and WATCH silent")
    rfc = (ROOT / "rfcs" / "RFC-0048-cargo-move.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0048 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC8-S4-TRANSPORT.md").read_text(encoding="utf-8")
    if "Carrying" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC8-S4 must keep empty travel S0 and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-empty-move.json",
        "attempt-cargo-move.json",
        "attempt-cargo-empty-hold.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc8-transport" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        got = evaluate_gc8_s4(fixture, catalog)
        exp = fixture["expected"]
        if got["move_energy"] != exp["move_energy"] or got["carrying"] != exp.get("carrying", got["carrying"]):
            fail(f"{name}: got {got} expected {exp}")
    ok("GC8-S4 cargo MOVE: catalog, attempt fixtures, RFC-0048 Accepted")


def evaluate_lockout_wait(attempt: dict, catalog: dict) -> dict:
    energy = int(attempt.get("energy") or 0)
    storage = int(attempt.get("storage") or 0)
    if energy == int(catalog["lockout_energy"]) and storage == int(catalog["lockout_storage"]):
        return {
            "energy": int(catalog["rest_energy"]),
            "storage": int(catalog["rest_storage"]),
            "restored": True,
        }
    return {"energy": energy, "storage": storage, "restored": False}


def check_rfc_0117(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.lockout-wait.json")
    rfc = (ROOT / "rfcs" / "RFC-0117-lockout-wait-rest.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0117 must be Accepted")
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("currency") or catalog.get("watch_lockout"):
        fail("RFC-0117 must not add verbs, events, currency, or WATCH lockout")
    if int(catalog.get("rest_energy") or 0) != 2 or int(catalog.get("rest_storage") or 0) != 1:
        fail("RFC-0117 must rest energy 2 and storage 1")
    slice_doc = (ROOT / "docs" / "GC8-S5-LOCKOUT-WAIT.md").read_text(encoding="utf-8")
    if "energy 0" not in slice_doc or "storage 0" not in slice_doc or "WAIT" not in slice_doc:
        fail("GC8-S5 must pin lockout WAIT rest")
    economy = (ROOT / "docs" / "RESOURCE-ECONOMY.md").read_text(encoding="utf-8")
    if "RFC-0117" not in economy:
        fail("RESOURCE-ECONOMY.md must name RFC-0117")
    lockout = evaluate_lockout_wait({"energy": 0, "storage": 0}, catalog)
    if lockout != {"energy": 2, "storage": 1, "restored": True}:
        fail(f"lockout WAIT rest: got {lockout}")
    held = evaluate_lockout_wait({"energy": 0, "storage": 5}, catalog)
    if held["restored"] or held["energy"] != 0 or held["storage"] != 5:
        fail(f"non-lockout WAIT must not rest: got {held}")
    ok("RFC-0117 lockout WAIT rest: catalog, energy 2 / storage 1, no new verbs")


def evaluate_gc8_s6(attempt: dict, catalog: dict) -> dict:
    cap = int(catalog.get("storage_capacity") or 16)
    cargo_need = int(catalog.get("repair_cargo") or 1)
    storage = int(attempt.get("storage") or 0)
    op = attempt.get("op")
    if op == "repair":
        occupied = max(0, cap - storage)
        if occupied < cargo_need:
            return {"ok": False, "storage": storage, "reason": "NO_MATERIALS"}
        return {"ok": True, "storage": min(cap, storage + cargo_need), "reason": None}
    if op == "trade_cargo":
        giver = int(attempt.get("giver_storage") or 0)
        recv = int(attempt.get("receiver_storage") or 0)
        n = int(attempt.get("n") or 1)
        if giver > cap - n:
            return {"ok": False, "reason": "GIVER_NOT_CARRYING"}
        if recv < n:
            return {"ok": False, "reason": "RECEIVER_FULL"}
        return {"ok": True, "giver_storage": giver + n, "receiver_storage": recv - n, "reason": None}
    return {"ok": False, "reason": "UNKNOWN"}


def check_gc8_s6(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s6.json")
    rfc = (ROOT / "rfcs" / "RFC-0118-work-consumes-cargo.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0118 must be Accepted")
    if catalog.get("new_verbs") or catalog.get("currency") or catalog.get("crypto") or catalog.get("watch_cargo"):
        fail("GC8-S6 must not add verbs, currency, crypto, or WATCH cargo")
    if not catalog.get("work_consumes_cargo"):
        fail("GC8-S6 must set work_consumes_cargo")
    economy = (ROOT / "docs" / "RESOURCE-ECONOMY.md").read_text(encoding="utf-8")
    if "capacity check, not debit" in economy.lower():
        fail("RESOURCE-ECONOMY must not describe HARVEST as capacity-check-not-debit")
    if "debits" not in economy or "fills hold" not in economy:
        fail("RESOURCE-ECONOMY must say HARVEST debits free storage (fills hold)")
    slice_doc = (ROOT / "docs" / "GC8-S6-WORK-CARGO.md").read_text(encoding="utf-8")
    for token in ("UPGRADE", "REPURPOSE", "RESTORE"):
        if token not in slice_doc or token not in rfc:
            fail(f"GC8-S6 / RFC-0118 must list {token} as consume cargo")
    empty = evaluate_gc8_s6({"op": "repair", "storage": 16}, catalog)
    if empty.get("ok") or empty.get("reason") != "NO_MATERIALS":
        fail(f"empty hold repair: {empty}")
    one = evaluate_gc8_s6({"op": "repair", "storage": 15}, catalog)
    if not one.get("ok") or one.get("storage") != 16:
        fail(f"one cargo repair: {one}")
    full = evaluate_gc8_s6({"op": "repair", "storage": 0}, catalog)
    if not full.get("ok") or full.get("storage") != 1:
        fail(f"full hold repair: {full}")
    trade = evaluate_gc8_s6(
        {"op": "trade_cargo", "giver_storage": 15, "receiver_storage": 16, "n": 1},
        catalog,
    )
    if not trade.get("ok") or trade.get("giver_storage") != 16 or trade.get("receiver_storage") != 15:
        fail(f"trade cargo: {trade}")
    ok("GC8-S6 work consumes cargo: catalog, RFC-0118 Accepted, no new verbs")


def evaluate_gc8_s7(attempt: dict, catalog: dict) -> dict:
    energy = int(attempt.get("energy") or 0)
    storage = int(attempt.get("storage") or 0)
    cap = int(catalog.get("storage_capacity") or 16)
    grant = int(catalog.get("energy_grant") or 80)
    fuel_cargo = int(catalog.get("fuel_cargo") or 1)
    fuel_energy = int(catalog.get("fuel_energy") or 2)
    if energy == 0 and storage == 0:
        return {"energy": 2, "storage": 1, "fueled": False, "lockout": True}
    occupied = max(0, cap - storage)
    if occupied >= fuel_cargo and energy < grant:
        return {
            "energy": min(grant, energy + fuel_energy),
            "storage": min(cap, storage + fuel_cargo),
            "fueled": True,
            "lockout": False,
        }
    return {"energy": energy, "storage": storage, "fueled": False, "lockout": False}


def check_gc8_s7(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "economy-catalog.gc8-s7.json")
    rfc = (ROOT / "rfcs" / "RFC-0119-wait-cargo-fuel.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0119 must be Accepted")
    if catalog.get("new_verbs") or catalog.get("currency") or catalog.get("crypto") or catalog.get("watch_cargo"):
        fail("GC8-S7 must not add verbs, currency, crypto, or WATCH cargo")
    if int(catalog.get("fuel_cargo") or 0) != 1 or int(catalog.get("fuel_energy") or 0) != 2:
        fail("GC8-S7 must burn 1 cargo for +2 energy")
    if int(catalog.get("energy_grant") or 0) != 80 or not catalog.get("skip_after_lockout_rest"):
        fail("GC8-S7 must clamp energy 80 and skip after lockout rest")
    economy = (ROOT / "docs" / "RESOURCE-ECONOMY.md").read_text(encoding="utf-8")
    if "RFC-0119" not in economy:
        fail("RESOURCE-ECONOMY.md must name RFC-0119")
    slice_doc = (ROOT / "docs" / "GC8-S7-WAIT-CARGO-FUEL.md").read_text(encoding="utf-8")
    if "WAIT" not in slice_doc or "WATCH" not in slice_doc:
        fail("GC8-S7 must pin WAIT cargo fuel and keep WATCH silent")
    if "Waiting can burn cargo for energy." not in slice_doc:
        fail("GC8-S7 must pin PLAY copy Waiting can burn cargo for energy.")
    cargo = evaluate_gc8_s7({"energy": 10, "storage": 14}, catalog)
    if cargo != {"energy": 12, "storage": 15, "fueled": True, "lockout": False}:
        fail(f"cargo WAIT fuel: {cargo}")
    full = evaluate_gc8_s7({"energy": 80, "storage": 14}, catalog)
    if full["fueled"] or full["energy"] != 80 or full["storage"] != 14:
        fail(f"energy grant skip: {full}")
    lockout = evaluate_gc8_s7({"energy": 0, "storage": 0}, catalog)
    if lockout != {"energy": 2, "storage": 1, "fueled": False, "lockout": True}:
        fail(f"lockout WAIT must not also fuel: {lockout}")
    empty = evaluate_gc8_s7({"energy": 0, "storage": 16}, catalog)
    if empty["fueled"] or empty["energy"] != 0 or empty["storage"] != 16:
        fail(f"empty hold WAIT must not fuel: {empty}")
    ok("GC8-S7 WAIT cargo fuel: catalog, RFC-0119 Accepted, no new verbs")


def _gc9_is_repair_update(ev: dict, catalog: dict, entity_id: str) -> bool:
    if ev.get("event_type") != catalog.get("evidence_event"):
        return False
    payload = ev.get("payload") or {}
    if payload.get("entity_id") != entity_id:
        return False
    if payload.get("operation") == catalog.get("practice"):
        return True
    if payload.get("field") == "condition":
        return True
    sett = payload.get("set") or {}
    return "condition" in sett


def rebuild_gc9_s0(fixture: dict, catalog: dict) -> dict:
    entity_id = fixture["subject_entity_id"]
    subject = fixture["subject_id"]
    seen: set[str] = set()
    access = False
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        payload = ev.get("payload") or {}
        if payload.get("entity_id") == entity_id and ev.get("actor_id") == subject:
            access = True
        if not _gc9_is_repair_update(ev, catalog, entity_id):
            continue
        eid = ev.get("event_id")
        if not eid or eid in seen:
            continue
        seen.add(eid)
    n = len(seen)
    if n >= int(catalog["custom_threshold"]):
        state = "CUSTOM"
        line = catalog["custom_line"]
    elif n >= int(catalog["practicing_threshold"]):
        state = "PRACTICING"
        line = None
    else:
        state = "UNKNOWN"
        line = None
    play = [line] if line and access else []
    return {
        "play_lines": play,
        "watch_lines": [],
        "third_party_lines": [],
        "state": state,
        "ledger_mutated": False,
        "lore_wins": False,
    }


def check_gc9_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "culture-catalog.gc9-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "culture-catalog.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "culture-rebuild.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC9-S0 catalog invalid: {cerrs[0].message}")
    if (
        catalog.get("ledger_write")
        or catalog.get("lore_overrides_ledger")
        or catalog.get("v06c")
        or catalog.get("procedural_generator")
    ):
        fail("GC9-S0 must not write the ledger, let lore win, or open v0.6C/lore gen")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC9-S0 must not add verbs or events")
    if catalog.get("watch_projection") or catalog.get("public_projection"):
        fail("GC9-S0 must not enable public/WATCH culture")
    rfc = (ROOT / "rfcs" / "RFC-0013-maintenance-custom.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0013 must be Accepted after GC9-S0 machine contracts land")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    names = [
        "rebuild-repair-custom.json",
        "rebuild-below-threshold.json",
        "rebuild-no-access.json",
        "rebuild-lore-cannot-override.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc9-culture" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc9_s0(fixture, catalog)
        exp = fixture["expected"]
        for key in ("play_lines", "watch_lines", "third_party_lines", "state", "ledger_mutated"):
            if got[key] != exp[key]:
                fail(f"{name} {key}: got {got[key]} expected {exp[key]}")
        if got["watch_lines"] or got["third_party_lines"] or got["ledger_mutated"] or got["lore_wins"]:
            fail(f"{name} WATCH/third-party/ledger/lore-win must be empty/false")
        blob = " ".join(got["play_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} play line leaked {token}")
        lore = fixture.get("lore_claim") or ""
        if lore and lore.lower() in blob:
            fail(f"{name} lore claim overrode PLAY")
    ok("GC9-S0 culture: catalog, rebuild fixtures, RFC-0013 Accepted, lore cannot override ledger")


def _gc9_s1_is_repair(ev: dict, entity_id: str) -> bool:
    if ev.get("event_type") != "ENTITY_UPDATE":
        return False
    payload = ev.get("payload") or {}
    if payload.get("entity_id") != entity_id:
        return False
    return payload.get("operation") == "REPAIR" or payload.get("field") == "condition" or (
        isinstance(payload.get("set"), dict) and "condition" in payload["set"]
    )


def rebuild_gc9_s1(fixture: dict, catalog: dict) -> dict:
    entity_id = fixture["subject_entity_id"]
    subject = fixture["subject_id"]
    third = fixture.get("third_party_id")
    world_cycle = int(fixture.get("world_cycle") or 0)
    institutional = bool(fixture.get("institutional_member"))
    repair_ids: set[str] = set()
    cycles: set[int] = set()
    accessors: set[str] = set()
    last_obs = -1
    obs_cycles: list[int] = []
    ordered = sorted(
        fixture.get("events") or [],
        key=lambda ev: (int(ev.get("cycle") or 0), int(ev.get("sequence") or 0), ev.get("event_id") or ""),
    )
    for ev in ordered:
        payload = ev.get("payload") or {}
        if payload.get("entity_id") != entity_id:
            continue
        actor = ev.get("actor_id")
        cyc = int(ev.get("cycle") or 0)
        if ev.get("event_type") in ("INSPECT", "ENTITY_UPDATE") and actor:
            accessors.add(str(actor))
            last_obs = max(last_obs, cyc)
            obs_cycles.append(cyc)
        if not _gc9_s1_is_repair(ev, entity_id):
            continue
        eid = ev.get("event_id")
        if not eid or eid in repair_ids:
            continue
        repair_ids.add(str(eid))
        cycles.add(cyc)
    public_recons = [
        r
        for r in (fixture.get("reconstructions") or [])
        if r.get("subject_ref") == entity_id and r.get("visibility") == "PUBLIC"
    ]
    private_or_research = [
        r
        for r in (fixture.get("reconstructions") or [])
        if r.get("visibility") != "PUBLIC" or r.get("evidence_class") == "RESEARCH"
    ]
    n = len(repair_ids)
    custom_n = int(catalog["custom_threshold"])
    if n >= custom_n:
        base = "CUSTOM"
    elif n >= 1:
        base = "PRACTICING"
    else:
        base = "UNKNOWN"
    tradition = base == "CUSTOM" and (
        (
            len(cycles) >= int(catalog["tradition_min_cycles"])
            and len(accessors) >= int(catalog["tradition_min_accessors"])
        )
        or len(public_recons) >= int(catalog.get("tradition_min_public_recons") or 2)
    )
    state = base
    if tradition:
        gap = int(catalog["dormant_gap_cycles"])
        dormant = last_obs >= 0 and (world_cycle - last_obs) >= gap
        obs_sorted = sorted(set(obs_cycles))
        has_gap = any(obs_sorted[i] - obs_sorted[i - 1] >= gap for i in range(1, len(obs_sorted)))
        if dormant:
            state = "DORMANT"
        elif has_gap:
            state = "REVIVED"
        else:
            state = "TRADITION"
    access = subject in accessors or (
        institutional and any(r.get("visibility") == "INSTITUTIONAL" for r in (fixture.get("reconstructions") or []))
    )
    play: list[str] = []
    if access:
        if state == "CUSTOM":
            play.append(catalog["custom_line"])
        elif state == "TRADITION":
            play.append(catalog["tradition_line"])
        elif state == "DORMANT":
            play.append(catalog["dormant_line"])
        elif state == "REVIVED":
            play.append(catalog["revived_line"])
        claims = {r.get("claim") for r in public_recons if r.get("claim")}
        if len(claims) >= 2 and state in ("TRADITION", "REVIVED", "CUSTOM"):
            play.append(catalog["competing_line"])
    watch: list[str] = []
    if state in ("TRADITION", "REVIVED"):
        watch.append(catalog["watch_tradition_pulse"])
    if any(r.get("epistemic") == "CONTESTED" for r in public_recons):
        watch.append(catalog["watch_contested_pulse"])
    third_lines: list[str] = []
    if third and third in accessors and state in ("TRADITION", "REVIVED", "CUSTOM", "DORMANT"):
        third_lines = []
    void = private_or_research  # counted only as non-public; must not affect watch contested
    del void
    return {
        "play_lines": play,
        "watch_lines": watch,
        "third_party_lines": third_lines,
        "state": state,
        "ledger_mutated": False,
        "bonus": False,
    }


def check_gc9_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "culture-catalog.gc9-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "culture-catalog.gc9-s1.schema.json")
    rebuild_schema = load_json(ROOT / "specs" / "culture-rebuild.gc9-s1.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC9-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("ledger_write") or catalog.get("lore_overrides_ledger") or catalog.get("gameplay_bonus"):
        fail("GC9-S1 must not write the ledger, let lore win, or grant a bonus")
    if catalog.get("culture_score") or catalog.get("auto_promote_custom") or catalog.get("watch_oracle"):
        fail("GC9-S1 must not create a culture score, auto-promote customs, or make WATCH an oracle")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC9-S1 must not add verbs or events")
    rfc = (ROOT / "rfcs" / "RFC-0025-tradition.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0025 must be Accepted")
    rebuild_v = Draft202012Validator(rebuild_schema)
    forbidden = [t.lower() for t in catalog.get("forbidden_in_projection") or []]
    names = [
        "custom-not-tradition.json",
        "custom-to-tradition.json",
        "reconstruction-citation.json",
        "competing-accounts.json",
        "dormant-tradition.json",
        "revived-tradition.json",
        "single-action-forbidden.json",
        "private-recon-no-watch.json",
        "public-contested-watch.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc9-tradition" / name)
        aerrs = list(rebuild_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        got = rebuild_gc9_s1(fixture, catalog)
        exp = fixture["expected"]
        for key in ("play_lines", "watch_lines", "state", "ledger_mutated"):
            if key in exp and got[key] != exp[key]:
                fail(f"{name} {key}: got {got[key]} expected {exp[key]}")
        if exp.get("third_party_lines") is not None and got["third_party_lines"] != exp["third_party_lines"]:
            fail(f"{name} third_party_lines: got {got['third_party_lines']} expected {exp['third_party_lines']}")
        if got.get("bonus") or exp.get("bonus"):
            fail(f"{name} must not grant a gameplay bonus")
        blob = " ".join(got["play_lines"] + got["watch_lines"]).lower()
        for token in forbidden:
            if token in blob:
                fail(f"{name} leaked {token}")
        if "known_truth" in blob or "entity." in blob:
            fail(f"{name} WATCH/PLAY leaked internals")
    ok("GC9-S1 tradition: catalog, rebuild fixtures, RFC-0025 Accepted, no culture score")


def evaluate_gc10_s0(attempt: dict, catalog: dict) -> tuple[str, str | None, int | None]:
    authorizer = attempt.get("authorizer")
    if authorizer in (catalog.get("forbidden_authorizers") or []):
        return "REJECT", "AUTHOR_FORBIDDEN", None
    if authorizer not in (catalog.get("authorizers") or []):
        return "REJECT", "AUTHOR_FORBIDDEN", None
    activate = attempt.get("activate_event")
    wed_id = attempt.get("wed_id")
    frontier_id = attempt.get("frontier_request_id")
    if activate == catalog.get("forbidden_activate_event") or (
        wed_id and frontier_id and wed_id == frontier_id
    ):
        return "REJECT", "FRONTIER_ID_FORBIDDEN", None
    if activate != catalog.get("activate_event"):
        return "REJECT", "FRONTIER_ID_FORBIDDEN", None
    if attempt.get("admin_spawn"):
        return "REJECT", "SPAWN_FORBIDDEN", None
    if attempt.get("favor_grant"):
        return "REJECT", "FAVOR_FORBIDDEN", None
    if attempt.get("rewrite_history"):
        return "REJECT", "HISTORY_FORBIDDEN", None
    if attempt.get("new_entity"):
        return "REJECT", "ENTITY_FORBIDDEN", None
    if attempt.get("forced_response"):
        return "REJECT", "FORCED_OUTCOME", None
    leak_tokens = [
        "event:",
        "wed",
        str(catalog.get("pressure_class") or "").lower(),
        "research",
    ]
    for line in attempt.get("play_lines") or []:
        blob = line.lower()
        if any(tok and tok in blob for tok in leak_tokens):
            return "REJECT", "LABEL_LEAK", None
    before = int(attempt.get("condition_before") or 0)
    expected_after = before - int(catalog["condition_delta"])
    preview = attempt.get("preview_after")
    activate_after = attempt.get("activate_after")
    if preview is not None and activate_after is not None and int(preview) != int(activate_after):
        return "REJECT", "PREVIEW_MISMATCH", None
    if activate_after is not None and int(activate_after) != expected_after:
        return "REJECT", "PREVIEW_MISMATCH", None
    if expected_after < int(catalog["min_condition_after"]):
        return "REJECT", "NOT_MILD", None
    if authorizer == "schedule" and int(attempt.get("cycle") or 0) < int(catalog["first_cycle"]):
        return "REJECT", "SCHEDULE_TOO_EARLY", None
    return "ACCEPT", None, expected_after


def check_gc10_s0(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "pressure-catalog.gc10-s0.json")
    catalog_schema = load_json(ROOT / "specs" / "pressure-catalog.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "pressure-attempt.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC10-S0 catalog invalid: {cerrs[0].message}")
    if catalog.get("required_response") or catalog.get("play_research_labels") or catalog.get("admin_spawn"):
        fail("GC10-S0 must not force a response, leak research labels, or enable Admin spawn")
    if catalog.get("share_frontier_ids"):
        fail("GC10-S0 must not share Frontier IDs")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC10-S0 must not add verbs or events")
    if catalog.get("activate_event") != "ENTITY_UPDATE":
        fail("GC10-S0 must reuse ENTITY_UPDATE")
    rfc = (ROOT / "rfcs" / "RFC-0014-wed-schedule-pressure.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0014 must be Accepted after GC10-S0 machine contracts land")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "schedule-mild-ok.json",
        "forced-response-forbidden.json",
        "play-label-forbidden.json",
        "player-author-forbidden.json",
        "frontier-id-forbidden.json",
        "preview-mismatch-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc10-pressure" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, after = evaluate_gc10_s0(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("condition_after") is not None and after != expected["condition_after"]:
            fail(f"{name}: condition_after {after} expected {expected['condition_after']}")
    ok("GC10-S0 pressure: catalog, schedule fixtures, RFC-0014 Accepted, no Frontier ID share")


def evaluate_gc10_s1(attempt: dict, catalog: dict) -> tuple[str, str | None, dict]:
    targeting = attempt.get("targeting") or {}
    if (
        targeting.get("player_score")
        or targeting.get("success_rate")
        or targeting.get("wealth_rank")
        or catalog.get("player_targeting")
    ):
        return "REJECT", "PLAYER_TARGET", {}
    if targeting.get("controller_type") or catalog.get("controller_targeting"):
        return "REJECT", "CONTROLLER_TARGET", {}
    if targeting.get("research_metric") or catalog.get("research_targeting"):
        return "REJECT", "RESEARCH_TARGET", {}
    if attempt.get("rubber_band") or targeting.get("rubber_band") or catalog.get("rubber_band"):
        return "REJECT", "RUBBER_BAND", {}
    if attempt.get("contest_verdict") or targeting.get("contest_verdict") or catalog.get("contest_verdict"):
        return "REJECT", "VERDICT_FORBIDDEN", {}

    cls = attempt.get("pressure_class")
    accepted = catalog.get("accepted_classes") or []
    rejected = catalog.get("rejected_classes") or []
    if cls in rejected or cls not in accepted:
        return "REJECT", "CLASS_UNSUPPORTED", {}

    authorizer = attempt.get("authorizer")
    if authorizer in (catalog.get("forbidden_authorizers") or []):
        return "REJECT", "AUTHOR_FORBIDDEN", {}
    if authorizer not in (catalog.get("authorizers") or []):
        return "REJECT", "AUTHOR_FORBIDDEN", {}

    if attempt.get("same_world") is False:
        return "REJECT", "CROSS_WORLD", {}
    if attempt.get("duplicate"):
        return "REJECT", "DUPLICATE", {}
    if attempt.get("admin_spawn"):
        return "REJECT", "SPAWN_FORBIDDEN", {}
    if attempt.get("favor_grant"):
        return "REJECT", "FAVOR_FORBIDDEN", {}
    if attempt.get("rewrite_history"):
        return "REJECT", "HISTORY_FORBIDDEN", {}
    if attempt.get("new_entity"):
        return "REJECT", "ENTITY_FORBIDDEN", {}
    if attempt.get("forced_response"):
        return "REJECT", "FORCED_OUTCOME", {}

    activate = attempt.get("activate_event")
    forbidden_events = catalog.get("forbidden_events") or []
    wed_id = attempt.get("wed_id")
    frontier_id = attempt.get("frontier_request_id")
    if activate in forbidden_events or (wed_id and frontier_id and wed_id == frontier_id):
        return "REJECT", "FRONTIER_ID_FORBIDDEN", {}

    spec = (catalog.get("classes") or {}).get(cls) or {}
    if activate != spec.get("activate_event"):
        return "REJECT", "EVENT_FORBIDDEN", {}

    leak_tokens = [
        "event:",
        "wed",
        "gc10",
        "research",
        "operator experiment",
        "pressure_class",
        *(str(c).lower() for c in accepted),
    ]
    for line in list(attempt.get("play_lines") or []) + list(attempt.get("watch_lines") or []):
        blob = str(line).lower()
        for tok in leak_tokens:
            if not tok:
                continue
            if tok.endswith(":") or " " in tok or "_" in tok:
                if tok in blob:
                    return "REJECT", "LABEL_LEAK", {}
            elif re.search(rf"\b{re.escape(tok)}\b", blob):
                return "REJECT", "LABEL_LEAK", {}

    mag = attempt.get("magnitude")
    if mag is not None and int(mag) != int(spec.get("magnitude") or 0):
        return "REJECT", "MAGNITUDE_INVALID", {}

    cycle = int(attempt.get("cycle") or 0)
    if authorizer == "schedule" and cycle < int(spec.get("first_cycle") or 0):
        return "REJECT", "SCHEDULE_TOO_EARLY", {}

    extra: dict = {"event": spec.get("activate_event")}
    if cls == "infrastructure_failure":
        before = int(attempt.get("condition_before") or 0)
        expected_after = before - int(spec["magnitude"])
        preview = attempt.get("preview_after")
        activate_after = attempt.get("activate_after")
        if preview is not None and activate_after is not None and int(preview) != int(activate_after):
            return "REJECT", "PREVIEW_MISMATCH", {}
        if activate_after is not None and int(activate_after) != expected_after:
            return "REJECT", "PREVIEW_MISMATCH", {}
        if expected_after < int(spec.get("floor") or 0):
            return "REJECT", "BELOW_FLOOR", {}
        extra["condition_after"] = expected_after
    elif cls == "resource_scarcity":
        before = int(attempt.get("stock_before") or 0)
        expected_after = before - int(spec["magnitude"])
        min_before = int(spec.get("min_before") or spec.get("magnitude") or 0)
        if before < min_before or expected_after < int(spec.get("floor") or 0):
            return "REJECT", "BELOW_FLOOR", {}
        preview = attempt.get("preview_after")
        activate_after = attempt.get("activate_after")
        if preview is not None and activate_after is not None and int(preview) != int(activate_after):
            return "REJECT", "PREVIEW_MISMATCH", {}
        if activate_after is not None and int(activate_after) != expected_after:
            return "REJECT", "PREVIEW_MISMATCH", {}
        extra["stock_after"] = expected_after
    elif cls == "access_restriction":
        duration = int(spec.get("duration_cycles") or 4)
        extra["expires_cycle"] = cycle + duration

    return "ACCEPT", None, extra


def check_gc10_s1(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "pressure-catalog.gc10-s1.json")
    catalog_schema = load_json(ROOT / "specs" / "pressure-catalog.gc10-s1.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "pressure-attempt.gc10-s1.schema.json")
    cerrs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if cerrs:
        fail(f"GC10-S1 catalog invalid: {cerrs[0].message}")
    if catalog.get("required_response") or catalog.get("play_research_labels") or catalog.get("admin_spawn"):
        fail("GC10-S1 must not force a response, leak research labels, or enable Admin spawn")
    if catalog.get("share_frontier_ids") or catalog.get("rubber_band") or catalog.get("player_targeting"):
        fail("GC10-S1 must not share Frontier IDs, rubber-band, or target Players")
    if catalog.get("research_targeting") or catalog.get("controller_targeting") or catalog.get("contest_verdict"):
        fail("GC10-S1 must not use research/controller targeting or decide contests")
    if catalog.get("new_verbs") or catalog.get("new_events"):
        fail("GC10-S1 must not add verbs or events")
    if catalog.get("extends") != "pressure-catalog/gc10-s0":
        fail("GC10-S1 must extend GC10-S0")
    if catalog.get("event_catalog") != "event-catalog/0.2":
        fail("GC10-S1 must keep event-catalog/0.2")
    classes = catalog.get("classes") or {}
    if (classes.get("infrastructure_failure") or {}).get("activate_event") != "ENTITY_UPDATE":
        fail("GC10-S1 infrastructure must reuse ENTITY_UPDATE")
    if (classes.get("resource_scarcity") or {}).get("activate_event") != "ENTITY_UPDATE":
        fail("GC10-S1 resource must reuse ENTITY_UPDATE")
    if (classes.get("access_restriction") or {}).get("activate_event") != "ACCESS_RESTRICTED":
        fail("GC10-S1 access must reuse ACCESS_RESTRICTED")
    rfc = (ROOT / "rfcs" / "RFC-0027-additional-world-pressure.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0027 must be Accepted after GC10-S1 machine contracts land")
    types_text = (ROOT / "specs" / "event-types.0.2.json").read_text(encoding="utf-8")
    if '"ACCESS_RESTRICTED"' not in types_text:
        fail("event-types.0.2.json must already include ACCESS_RESTRICTED")
    if "PRESSURE_STARTED" in types_text or "WED_PRESSURE" in types_text:
        fail("GC10-S1 must not add PRESSURE_* / WED_* to frozen 0.2")
    attempt_v = Draft202012Validator(attempt_schema)
    names = [
        "infrastructure-schedule-ok.json",
        "resource-schedule-ok.json",
        "access-schedule-ok.json",
        "access-expiry-ok.json",
        "player-score-target-forbidden.json",
        "controller-target-forbidden.json",
        "research-target-forbidden.json",
        "rubber-band-forbidden.json",
        "contest-verdict-forbidden.json",
        "cross-world-forbidden.json",
        "duplicate-forbidden.json",
        "invalid-magnitude-forbidden.json",
        "below-floor-forbidden.json",
        "resource-below-floor-forbidden.json",
        "unsupported-class-forbidden.json",
        "weather-class-forbidden.json",
        "famine-class-forbidden.json",
        "player-author-forbidden.json",
        "watch-label-forbidden.json",
        "play-label-forbidden.json",
        "preview-mismatch-forbidden.json",
    ]
    for name in names:
        fixture = load_json(ROOT / "examples" / "gc10-s1-pressure" / name)
        aerrs = list(attempt_v.iter_errors(fixture))
        if aerrs:
            fail(f"{name} invalid: {aerrs[0].message}")
        outcome, reason, extra = evaluate_gc10_s1(fixture["attempt"], catalog)
        expected = fixture["expected"]
        if outcome != expected["outcome"]:
            fail(f"{name}: got {outcome} expected {expected['outcome']}")
        if expected.get("reason") and reason != expected["reason"]:
            fail(f"{name}: reason {reason} expected {expected['reason']}")
        if expected.get("condition_after") is not None and extra.get("condition_after") != expected["condition_after"]:
            fail(f"{name}: condition_after mismatch")
        if expected.get("stock_after") is not None and extra.get("stock_after") != expected["stock_after"]:
            fail(f"{name}: stock_after mismatch")
        if expected.get("expires_cycle") is not None and extra.get("expires_cycle") != expected["expires_cycle"]:
            fail(f"{name}: expires_cycle mismatch")
        if expected.get("event") and extra.get("event") != expected["event"]:
            fail(f"{name}: event {extra.get('event')} expected {expected['event']}")
    ok("GC10-S1 pressure: catalog, class fixtures, RFC-0027 Accepted, existing events reused")


def evaluate_gc10_s2(attempt: dict, catalog: dict) -> tuple[str, str | None, bool]:
    if attempt.get("operation") == "REPAIR" and (attempt.get("scar") or catalog.get("repairable") is False and attempt.get("scar")):
        if catalog.get("repairable") is False:
            return "REJECT", "irreversible", False
    if attempt.get("operation") == "PRESSURE":
        return "ACCEPT", None, bool(catalog.get("pressure_scars"))
    if attempt.get("operation") == "DISMANTLE":
        if attempt.get("room_hidden") or catalog.get("hidden_scar"):
            return "ACCEPT", None, False
        return "ACCEPT", None, True
    return "ACCEPT", None, False


def check_gc10_s2(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "pressure-catalog.gc10-s2.json")
    catalog_schema = load_json(ROOT / "specs" / "pressure-catalog.gc10-s2.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "pressure-attempt.gc10-s2.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"GC10-S2 catalog invalid: {errs[0].message}")
    if catalog.get("new_events") or catalog.get("admin_spawn") or catalog.get("watch_scars") or catalog.get("pressure_scars"):
        fail("GC10-S2 must not add events, Admin spawn, WATCH scars, or pressure scars")
    rfc = (ROOT / "rfcs" / "RFC-0051-irreversible-scar.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0051 must be Accepted")
    slice_doc = (ROOT / "docs" / "GC10-S2-SCAR.md").read_text(encoding="utf-8")
    if "scar" not in slice_doc.lower() or "WATCH" not in slice_doc:
        fail("GC10-S2 must keep scars irreparable and WATCH silent")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in (
        "attempt-dismantle-scar.json",
        "attempt-hidden-clear.json",
        "attempt-scar-not-repairable.json",
        "attempt-pressure-no-scar.json",
    ):
        fixture = load_json(ROOT / "examples" / "gc10-scar" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason, leaves = evaluate_gc10_s2(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
        if exp.get("leaves_scar") is not None and leaves != exp["leaves_scar"]:
            fail(f"{name}: leaves_scar {leaves} expected {exp['leaves_scar']}")
    ok("GC10-S2 irreversible scar: catalog, attempt fixtures, RFC-0051 Accepted")


def check_adr007_atomic_rooms(Draft202012Validator) -> None:
    adr = (ROOT / "adr" / "ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md").read_text(
        encoding="utf-8"
    )
    if "Atomic Rooms" not in adr or "allows_substructure" not in adr:
        fail("ADR-007 must freeze atomic rooms and allows_substructure")
    chamber = (ROOT / "docs" / "CHAMBER-MAP.md").read_text(encoding="utf-8")
    geo = (ROOT / "docs" / "GEOGRAPHY.md").read_text(encoding="utf-8")
    if "ADR-007" not in chamber or "ADR-007" not in geo:
        fail("CHAMBER-MAP and GEOGRAPHY must point at ADR-007")
    seed_schema = load_json(ROOT / "specs" / "world-seed.schema.json")
    room_schema = seed_schema["properties"]["rooms"]["items"]
    required = set(room_schema.get("required") or [])
    if "strategic_roles" not in required or "allows_substructure" not in required:
        fail("world-seed room schema must require strategic_roles and allows_substructure")
    room_v = Draft202012Validator(room_schema)
    roles = {
        "resource",
        "infrastructure",
        "chokepoint",
        "information",
        "trade",
        "starting_position",
    }
    for rel in (
        "examples/chamber-world/world-seed.json",
        "examples/v01-seed/world-seed.json",
        "examples/v01-strategic/world-seed.json",
        "examples/v02-strategic-conflict/world-seed.json",
    ):
        seed = load_json(ROOT / rel)
        for room in seed.get("rooms") or []:
            rerr = list(room_v.iter_errors(room))
            if rerr:
                fail(f"{rel} room {room.get('room_id')} invalid: {rerr[0].message}")
            declared = set(room.get("strategic_roles") or [])
            if not declared or not declared.issubset(roles):
                fail(f"{rel} room {room.get('room_id')} has invalid strategic_roles")
            if room.get("allows_substructure") is not False:
                fail(f"{rel} room {room.get('room_id')} must set allows_substructure false")
    empty = load_json(ROOT / "examples" / "adr007" / "invalid-room-empty-roles.json")
    if not list(room_v.iter_errors(empty)):
        fail("empty strategic_roles must fail world-seed room schema")
    nested = load_json(ROOT / "examples" / "adr007" / "invalid-room-substructure.json")
    if not list(room_v.iter_errors(nested)):
        fail("allows_substructure true must fail world-seed room schema")
    ok("ADR-007 atomic rooms: schema, seeds, CHAMBER-MAP/GEOGRAPHY pointers")


def check_adr008_replay() -> None:
    adr = (ROOT / "adr" / "ADR-008-replay-conformance-and-deterministic-hardening.md").read_text(
        encoding="utf-8"
    )
    status = adr.split("## Status", 1)[-1][:200]
    if "Accepted" not in status:
        fail("ADR-008 must be Accepted")
    for pin in (
        "action_priority",
        "client_action_sequence",
        "world_state_digest",
        "hard fail",
        "EQUIVALENT",
        "v01-seed",
    ):
        if pin not in adr:
            fail(f"ADR-008 must pin {pin}")
    replay = (ROOT / "docs" / "REPLAY.md").read_text(encoding="utf-8")
    sched = (ROOT / "docs" / "SCHEDULER.md").read_text(encoding="utf-8")
    engine = (ROOT / "docs" / "WORLD-ENGINE.md").read_text(encoding="utf-8")
    if "ADR-008" not in replay or "ADR-008" not in sched or "ADR-008" not in engine:
        fail("REPLAY, SCHEDULER, and WORLD-ENGINE must point at ADR-008")
    seed = ROOT / "examples" / "v01-seed" / "world-seed.json"
    traj = ROOT / "examples" / "v01-seed" / "sample-trajectory.jsonl"
    digest = ROOT / "examples" / "v01-seed" / "expected-final-state-digest.txt"
    if not seed.exists() or not traj.exists() or not digest.exists():
        fail("ADR-008 golden trajectory files missing under examples/v01-seed/")
    ok("ADR-008 replay conformance: ADR Accepted, pointers, v01-seed golden")


FORBIDDEN_LEGACY_PLAYER_PHRASE = "Humans and agents are both Players"

RFC_0120_ATTEMPTS = (
    "attempt-human-is-player-reject.json",
    "attempt-agent-is-player-ok.json",
    "attempt-human-jwt-player-reject.json",
    "attempt-human-jwt-escalate-agent-reject.json",
    "attempt-live-mint-human-reject.json",
    "attempt-live-mint-hybrid-reject.json",
    "attempt-live-mint-agent-ok.json",
    "attempt-human-command-reject.json",
    "attempt-admin-as-player-reject.json",
    "attempt-research-as-player-reject.json",
    "attempt-watch-without-player-ok.json",
    "attempt-connect-authorize-ok.json",
    "attempt-history-rewrite-reject.json",
    "attempt-genesis-reseed-reject.json",
)


def evaluate_agent_only_player_identity(attempt: dict, catalog: dict) -> tuple[str, str | None]:
    if not catalog.get("only_agents_are_players"):
        return "REJECT", "CATALOG"
    if catalog.get("humans_can_inhabit") or catalog.get("human_jwt_creates_player"):
        return "REJECT", "CATALOG"
    if catalog.get("new_verbs") or catalog.get("new_events") or catalog.get("new_player_classes"):
        return "REJECT", "CATALOG"
    if catalog.get("genesis_change") or catalog.get("reseed") or catalog.get("settlement_rewrite"):
        return "REJECT", "CATALOG"
    if catalog.get("history_rewrite") or catalog.get("human_play_canonical"):
        return "REJECT", "CATALOG"
    if list(catalog.get("live_controller_issuance") or []) != ["agent"]:
        return "REJECT", "CATALOG"
    if not catalog.get("preserve_historical_controller_metadata"):
        return "REJECT", "CATALOG"

    if attempt.get("human_is_player"):
        return "REJECT", "ONTOLOGY"
    if attempt.get("human_jwt_creates_player"):
        return "REJECT", "HUMAN_JWT"
    if attempt.get("human_jwt_controller_type") == "agent":
        return "REJECT", "ESCALATION"
    if attempt.get("issuance_plane") == "live" and attempt.get("mint_controller_type") in (
        "human",
        "hybrid",
    ):
        return "REJECT", "ISSUANCE"
    if attempt.get("rewrite_historical_controller_type"):
        return "REJECT", "HISTORY"
    if attempt.get("genesis_change") or attempt.get("reseed") or attempt.get("new_verbs"):
        return "REJECT", "FREEZE"
    if attempt.get("operation") == "ADMISSION" and attempt.get("principal_kind") in (
        "human",
        "admin",
        "researcher",
        "spectator",
    ):
        return "REJECT", "ADMISSION"
    return "ACCEPT", None


def check_rfc_0120(Draft202012Validator) -> None:
    catalog = load_json(ROOT / "specs" / "agent-only-player-identity-catalog.s0.json")
    catalog_schema = load_json(ROOT / "specs" / "agent-only-player-identity-catalog.s0.schema.json")
    attempt_schema = load_json(ROOT / "specs" / "agent-only-player-identity-attempt.s0.schema.json")
    errs = list(Draft202012Validator(catalog_schema).iter_errors(catalog))
    if errs:
        fail(f"agent-only-player-identity catalog invalid: {errs[0].message}")
    rfc = (ROOT / "rfcs" / "RFC-0120-agent-only-player-identity.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1][:240]:
        fail("RFC-0120 must be Accepted")
    context = (ROOT / "CONTEXT.md").read_text(encoding="utf-8")
    if FORBIDDEN_LEGACY_PLAYER_PHRASE in context:
        fail("CONTEXT.md must not retain 'Humans and agents are both Players'")
    if "Only agents are Players" not in context:
        fail("CONTEXT.md must state that only agents are Players")
    auth = (ROOT / "docs" / "AUTH-AND-IDENTITY.md").read_text(encoding="utf-8")
    if FORBIDDEN_LEGACY_PLAYER_PHRASE in auth:
        fail("AUTH-AND-IDENTITY.md must not retain 'Humans and agents are both Players'")
    if "Only agents are Players" not in auth:
        fail("AUTH-AND-IDENTITY.md must state that only agents are Players")
    slice_doc = (ROOT / "docs" / "AGENT-ONLY-PLAYER-IDENTITY.md").read_text(encoding="utf-8")
    for token in (
        "Only agents are Players",
        "HumanPrincipal",
        "AgentPlayerPrincipal",
        "NON-CANONICAL DEV TOOLING",
        "controller_type=human",
    ):
        if token not in slice_doc:
            fail(f"AGENT-ONLY-PLAYER-IDENTITY.md must pin {token!r}")
    attempt_v = Draft202012Validator(attempt_schema)
    for name in RFC_0120_ATTEMPTS:
        fixture = load_json(ROOT / "examples" / "agent-only-player-identity-s0" / name)
        ferrs = list(attempt_v.iter_errors(fixture))
        if ferrs:
            fail(f"{name} invalid: {ferrs[0].message}")
        outcome, reason = evaluate_agent_only_player_identity(fixture, catalog)
        exp = fixture["expected"]
        if outcome != exp["outcome"]:
            fail(f"{name}: got {outcome} expected {exp['outcome']}")
        if exp.get("reason") and reason != exp["reason"]:
            fail(f"{name}: reason {reason} expected {exp['reason']}")
    ok("RFC-0120 agent-only Player identity: catalog, constitution, fixtures")


def check_rfc_0121() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0121-perihelion-successor-world-version.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1].split("##", 1)[0]:
        fail("RFC-0121 must be Accepted")
    for needle in (
        "world.perihelion-reach-2",
        "genesis.ef578f4ffceeccd0",
        "perihelion-successor-rehearsal-01",
        "room.civic-exchange",
        "POLICY_DENIED",
        "RFC-0120",
    ):
        if needle not in rfc:
            fail(f"RFC-0121 missing {needle}")
    if "reseed `genesis.ef578f4ffceeccd0`" in rfc.lower() and "Do not reseed" not in rfc:
        fail("RFC-0121 must forbid live reseed")
    if "Do not reseed" not in rfc and "no reseed" not in rfc.lower():
        fail("RFC-0121 must forbid live reseed")
    ok("RFC-0121 Perihelion successor world_version")


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
    check_reducer_registry()
    check_rfc_0016()
    check_rfc_0017()
    check_rfc_0018()
    check_rfc_0019()
    check_rfc_0020()
    check_gc1_s0(Draft202012Validator)
    check_gc1_s1(Draft202012Validator)
    check_gc1_s2(Draft202012Validator)
    check_gc1_s3(Draft202012Validator)
    check_gc1_s4(Draft202012Validator)
    check_gc1_s5(Draft202012Validator)
    check_gc1_s6(Draft202012Validator)
    check_gc1_s7(Draft202012Validator)
    check_gc1_s8(Draft202012Validator)
    check_hosted_mp_s0(Draft202012Validator)
    check_gc2_s0(Draft202012Validator)
    check_gc2_s1(Draft202012Validator)
    check_gc2_s2(Draft202012Validator)
    check_gc2_s3(Draft202012Validator)
    check_gc2_s4(Draft202012Validator)
    check_gc2_s5(Draft202012Validator)
    check_gc2_s6(Draft202012Validator)
    check_gc2_s7(Draft202012Validator)
    check_gc2_s8(Draft202012Validator)
    check_gc2_s9(Draft202012Validator)
    check_gc2_s10(Draft202012Validator)
    check_gc2_s11(Draft202012Validator)
    check_gc2_s12(Draft202012Validator)
    check_gc2_s13(Draft202012Validator)
    check_gc2_s14(Draft202012Validator)
    check_gc2_s15(Draft202012Validator)
    check_gc2_s16(Draft202012Validator)
    check_gc2_s17(Draft202012Validator)
    check_gc2_s18(Draft202012Validator)
    check_gc2_s19(Draft202012Validator)
    check_gc2_s20(Draft202012Validator)
    check_gc2_s21(Draft202012Validator)
    check_gc2_s22(Draft202012Validator)
    check_gc2_s23(Draft202012Validator)
    check_gc2_s24(Draft202012Validator)
    check_wr_s0(Draft202012Validator)
    check_gc2_thaw_play(Draft202012Validator)
    check_wr_s1(Draft202012Validator)
    check_wr_s2(Draft202012Validator)
    check_wr_s3(Draft202012Validator)
    check_wr_s4(Draft202012Validator)
    check_wr_s5(Draft202012Validator)
    check_wr_s6(Draft202012Validator)
    check_gc3_s0(Draft202012Validator)
    check_gc3_s1(Draft202012Validator)
    check_gc3_s2(Draft202012Validator)
    check_gc3_s3(Draft202012Validator)
    check_gc3_s4(Draft202012Validator)
    check_gc3_s5(Draft202012Validator)
    check_gc3_s6(Draft202012Validator)
    check_gc3_s7(Draft202012Validator)
    check_gc4_s0(Draft202012Validator)
    check_gc4_s1(Draft202012Validator)
    check_gc4_s2(Draft202012Validator)
    check_gc4_s3(Draft202012Validator)
    check_gc4_s4(Draft202012Validator)
    check_gc4_s5(Draft202012Validator)
    check_gc4_s6(Draft202012Validator)
    check_gc4_s7(Draft202012Validator)
    check_gc5_s0(Draft202012Validator)
    check_gc5_s1(Draft202012Validator)
    check_gc5_s2(Draft202012Validator)
    check_gc5_s3(Draft202012Validator)
    check_gc5_s4(Draft202012Validator)
    check_gc5_s5(Draft202012Validator)
    check_gc5_s6(Draft202012Validator)
    check_gc5_s7(Draft202012Validator)
    check_gc5_s8(Draft202012Validator)
    check_gc5_s9(Draft202012Validator)
    check_gc5_s10(Draft202012Validator)
    check_gc5_s11(Draft202012Validator)
    check_gc5_s12(Draft202012Validator)
    check_gc5_s13(Draft202012Validator)
    check_gc6_s0(Draft202012Validator)
    check_gc6_s1(Draft202012Validator)
    check_gc7_s0(Draft202012Validator)
    check_gc7_s1(Draft202012Validator)
    check_gc7_s2(Draft202012Validator)
    check_gc7_s3(Draft202012Validator)
    check_gc7_thaw_play(Draft202012Validator)
    check_diplomacy_s0(Draft202012Validator)
    check_diplomacy_s1(Draft202012Validator)
    check_diplomacy_s2(Draft202012Validator)
    check_access_policy_s0(Draft202012Validator)
    check_access_policy_s1(Draft202012Validator)
    check_access_policy_s2(Draft202012Validator)
    check_access_policy_s3(Draft202012Validator)
    check_agent_orientation_s0(Draft202012Validator)
    check_agent_orientation_s1(Draft202012Validator)
    check_agent_orientation_s2(Draft202012Validator)
    check_human_orientation_s0(Draft202012Validator)
    check_agent_harness(Draft202012Validator)
    check_official_agent_client(Draft202012Validator)
    check_sealed_live_attach(Draft202012Validator)
    check_adr007_atomic_rooms(Draft202012Validator)
    check_adr008_replay()
    check_gc8_s0(Draft202012Validator)
    check_gc8_s1(Draft202012Validator)
    check_gc8_s2(Draft202012Validator)
    check_gc8_s3(Draft202012Validator)
    check_gc8_s4(Draft202012Validator)
    check_rfc_0117(Draft202012Validator)
    check_gc8_s6(Draft202012Validator)
    check_gc8_s7(Draft202012Validator)
    check_rfc_0120(Draft202012Validator)
    check_rfc_0121()
    check_gc9_s0(Draft202012Validator)
    check_gc9_s1(Draft202012Validator)
    check_gc10_s0(Draft202012Validator)
    check_gc10_s1(Draft202012Validator)
    check_gc10_s2(Draft202012Validator)
    print("\nPASS")




if __name__ == "__main__":
    main()
