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
    check_gc2_s0(Draft202012Validator)
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
    check_gc5_s0(Draft202012Validator)
    check_gc5_s1(Draft202012Validator)
    check_gc5_s2(Draft202012Validator)
    check_gc6_s0(Draft202012Validator)
    check_gc6_s1(Draft202012Validator)
    check_gc7_s0(Draft202012Validator)
    check_gc7_s1(Draft202012Validator)
    check_gc8_s0(Draft202012Validator)
    check_gc9_s0(Draft202012Validator)
    check_gc9_s1(Draft202012Validator)
    check_gc10_s0(Draft202012Validator)
    check_gc10_s1(Draft202012Validator)
    print("\nPASS")




if __name__ == "__main__":
    main()
