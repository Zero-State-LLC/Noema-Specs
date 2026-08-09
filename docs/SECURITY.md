# Security Contract

This document defines the security boundary for the Noema repository's v0.1
release. Its core wire contract is `noema.core` `1.0.0`. The key words **MUST**,
**MUST NOT**, **SHOULD**, and **MAY** are normative.

Noema exchanges untrusted structured records and supports deterministic replay
over datasets. A valid record is not necessarily a trusted record. Schema
validation establishes shape only. It does not grant authority, establish truth,
or make embedded content safe to execute.

## Security objectives

A conforming implementation protects these properties:

1. **Confidentiality:** records, datasets, prompts, credentials, and derived
   artifacts are disclosed only to authorized principals and sinks.
2. **Integrity:** accepted records retain their meaning, provenance, ordering,
   and content across transport, persistence, and replay.
3. **Availability:** hostile or malformed input cannot consume unbounded time,
   memory, storage, network, or subprocess capacity.
4. **Determinism:** replay is isolated from undeclared ambient state and produces
   reproducible outcomes or an explicit, bounded nondeterminism report.
5. **Non-amplification:** data or instructions in a record cannot acquire more
   privilege merely by being parsed, transformed, retrieved, or replayed.
6. **Auditability:** security-relevant decisions are attributable without placing
   secrets or sensitive record contents in logs.

## Trust boundaries and assets

The threat model treats each of the following as an independent trust boundary:

- producer to transport;
- transport to parser/validator;
- validator to storage or dataset builder;
- dataset to replay runner;
- replay runner to model, tool, network, filesystem, or subprocess adapter;
- runner to evaluator and report publisher;
- operator or CI identity to secrets and policy configuration.

Protected assets include source records, dataset rows, expected outputs,
provenance, record identifiers, replay results, evaluation labels, credentials,
policy files, audit events, and unpublished vulnerabilities.

Unless authenticated by a deployment-specific mechanism, all producers,
records, datasets, schemas discovered at runtime, expected outputs, model text,
tool results, filenames, URLs, and metadata **MUST** be treated as untrusted.

## Threat actors and assumptions

Relevant actors include a malicious producer, a compromised transport or
storage layer, an attacker who contributes a dataset or pull request, a curious
operator with excess access, a compromised dependency or model/provider, and an
unintentional author whose malformed fixture triggers unsafe behavior.

Noema v0.1 does not assume that:

- JSON Schema validation proves semantic truth or authorization;
- provenance fields are authentic without an external integrity mechanism;
- model-generated text is safe or instruction-free;
- replaying a previously safe case remains safe under changed adapters or policy;
- record identifiers are secret, globally trustworthy, or safe as pathnames;
- hiding a field name provides confidentiality; or
- containment supplied only by a prompt is a security boundary.

## Principal threats

| Threat | Example | Required control |
|---|---|---|
| Parser abuse | deep nesting, huge strings, duplicate keys, numeric edge cases | byte/depth/item limits, strict decoding, fail closed |
| Schema confusion | wrong version, remote `$ref`, permissive unknown fields | pinned local schemas, explicit version dispatch, closed objects where specified |
| Injection | record text tells a model or tool to ignore policy | data/instruction separation, allowlisted capabilities, independent authorization |
| Capability escape | replay reads host files or invokes a shell | deny-by-default sandbox and explicit adapters |
| Network exfiltration | embedded URL or tool call sends dataset content | network off by default, destination allowlist, output filtering |
| Path traversal | identifier becomes `../../secret` | generated paths, canonicalization, root confinement |
| Resource exhaustion | replay bomb or unbounded output | per-case and run-wide quotas, cancellation, output caps |
| Cross-case leakage | state from one case influences another | fresh case context or proven reset, scoped temporary storage |
| Dataset poisoning | expected output encodes attacker-controlled policy | review, provenance, integrity checks, separation of data and executable config |
| Replay tampering | inputs or policy change without attribution | immutable run manifest and content digests |
| Secret leakage | credentials appear in fixtures, errors, or traces | secret scanning, redaction, least-privilege injection, no secret serialization |
| Dependency compromise | parser/evaluator package executes malicious code | lockfiles, review, provenance/SBOM where available, isolated CI |
| Authorization confusion | valid message crosses `tenant_id` or stream boundary | authenticate principal and authorize every read/write/replay separately |
| Event-store corruption | gaps, duplicate positions, or in-place event mutation | enforced uniqueness/contiguity, append-only storage, integrity audit |
| Identifier collision | two cases overwrite or impersonate one another | uniqueness checks and collision-safe storage keys |

## Mandatory containment profile

Containment is required whenever untrusted data is parsed, transformed, or
replayed. A v0.1 conforming runner **MUST** implement the following baseline.

### Process and filesystem

- Run cases with the minimum OS privileges available. Do not run as root.
- Use a dedicated, case-scoped working directory.
- Make the project, fixtures, and schemas read-only to the replay process.
- Permit writes only to a bounded case output directory.
- Reject absolute paths, traversal components, device paths, and symlink escapes
  at every record-to-path boundary.
- Do not expose the host home directory, SSH agent, Docker socket, cloud metadata
  credentials, package-manager credentials, or unrelated environment variables.
- Disable subprocess execution by default. An enabled command **MUST** be an
  argument-vector invocation of an allowlisted executable, never implicit shell
  evaluation of record content.

### Network and external capabilities

- Network access **MUST** be disabled by default.
- If a test explicitly requires network access, it **MUST** use a declared
  adapter with an allowlist, timeout, byte limit, request count limit, and
  synthetic or non-sensitive payloads.
- Redirects, alternate IP representations, DNS rebinding, and access to loopback,
  link-local, private, and metadata-service addresses **MUST** be blocked unless
  the specific test contract authorizes the destination.
- Models, tools, event stores, and projectors are capabilities. Selecting an adapter does not authorize a
  side effect. Each read, write, request, replay range, or invocation **MUST** pass policy.

### Resource budgets

Implementations **MUST** enforce finite, configurable budgets before allocating
or executing work, including:

- input and decompressed byte limits;
- JSON nesting, string, array, and object-member limits;
- dataset case and aggregate-byte limits;
- per-case wall-clock and, where available, CPU limits;
- process, file, file-descriptor, memory, request, and output-byte limits; and
- run-wide concurrency and failure thresholds.

Limit violations **MUST** terminate the affected operation with a structured,
non-sensitive error. A failed case must not disable limits for later cases.

### Isolation and state

- Each case **MUST** receive a fresh state context, or a reset mechanism whose
  equivalence to a fresh context is tested.
- Randomness, clocks, locale, timezone, model/provider version, policy version,
  adapter configuration, and relevant environment inputs **MUST** be fixed or
  recorded in the replay manifest.
- Caches **MUST** be keyed by every input that can affect the result and must not
  cross authorization domains.
- Cleanup **MUST** run after success, failure, timeout, and cancellation.

Containers can strengthen these controls but are not sufficient by themselves.
A container with a host socket, writable source mount, broad network access, or
host credentials is not contained.

## Protocol and schema handling

A conforming implementation **MUST**:

1. frame messages unambiguously and enforce a maximum frame size;
2. decode using a documented character encoding and reject malformed encoding;
3. define and test duplicate-object-key behavior, with rejection preferred;
4. dispatch on an explicit supported protocol/schema version;
5. reject unknown critical message types, fields, and versions;
6. resolve schemas only from an implementation-controlled, pinned registry;
7. disable remote reference fetching during validation;
8. validate before semantic processing, persistence, or capability invocation;
9. perform semantic checks that schemas cannot express, including uniqueness,
   ordering, referential integrity, digest matching, authorization, contiguous
   stream/global positions, and `event_id == message_id`; and
10. return bounded errors that identify the violated rule without echoing full
    records or secrets.

Consumers **MUST NOT** silently coerce values to make an invalid record pass.
Compatibility adapters must be explicit, versioned transformations whose input
and output both validate.

If authenticity is required, transport or artifact signatures **MUST** cover the
canonical bytes plus the protocol version and security-relevant context. The
specification does not define a universal v0.1 signing scheme.

### Tenant and event-store isolation

- An authenticated principal **MUST** be authorized independently for the
  `tenant_id`, target stream, command, subscription, and replay interval.
- A producer-controlled `tenant_id`, `stream_id`, or metadata field is never an
  authorization decision.
- Stores **MUST** enforce the uniqueness and contiguity rules in
  [`../protocols/core.md`](../protocols/core.md) atomically with append.
- A rejected command, failed optimistic-concurrency check, or unauthorized replay
  **MUST NOT** advance a stream, consume a global position, or disclose existence
  of another tenant's events beyond the deployment's documented error policy.
- Event correction occurs only through new events. Audit and replay tooling must
  detect in-place mutation or deletion that violates the advertised retention
  contract.

## Dataset safety

Only synthetic, public, or explicitly authorized content may enter a published
v0.1 conformance dataset. Dataset maintainers **MUST**:

- document origin, license, consent or authorization, and transformations;
- minimize personal and confidential information;
- scan for secrets and high-risk personal data before commit and release;
- assign stable opaque case identifiers rather than embedding personal data;
- store integrity digests in the release manifest;
- review expected outputs independently from the producer when practical;
- treat archive entries, filenames, MIME types, and embedded links as untrusted;
- reject archive traversal, links, unexpected special files, and decompression
  beyond configured limits; and
- provide a removal/correction path for data that should not have been included.

Raw production transcripts, credentials, access tokens, private keys, session
cookies, precise private locations, and regulated identifiers **MUST NOT** be
committed as fixtures.

## Replay integrity

A replay result is auditable only when its execution context is attributable.
Every run **MUST** emit a manifest that records, directly or by digest:

- dataset and case version;
- input and expected-output digests;
- protocol and schema versions;
- implementation revision;
- policy and containment profile;
- evaluator revision;
- adapter/model/tool versions and configuration relevant to results;
- seed, clock mode, and other controlled nondeterminism inputs;
- start/end time, terminal status, and bounded error category; and
- result artifact digests.

Replays **MUST NOT** mutate source fixtures or expected outputs. A partial,
timed-out, policy-denied, or infrastructure-failed run must be distinguishable
from a semantic test failure. Retry and resume operations must preserve the
original attempt and create a new attributable attempt.

## Secrets, privacy, and logging

Secrets **MUST** enter only through a deployment secret mechanism, be scoped to
the minimum adapter and lifetime, and never be serialized into records,
datasets, manifests, snapshots, errors, or test artifacts.

Logs **SHOULD** contain case IDs, digests, rule IDs, counts, durations, and status
rather than raw content. If content logging is explicitly enabled, access and
retention controls **MUST** match the underlying dataset. Redaction must occur
before data crosses a process, provider, log, telemetry, or error-reporting
boundary. Hashing low-entropy sensitive data does not anonymize it.

Deployments **MUST** define retention and deletion behavior for inputs, outputs,
temporary files, caches, telemetry, backups, and provider-side storage.

## Supply-chain and CI controls

- Dependencies and automation actions **SHOULD** be pinned to immutable versions.
- Pull requests from untrusted forks **MUST NOT** receive repository or deployment
  secrets, and their fixtures **MUST** run without privileged host mounts.
- Generated schemas, datasets, and release artifacts **MUST** be reproducible or
  accompanied by reviewed provenance and integrity digests.
- A schema or policy change **MUST** trigger all relevant conformance and security
  tests. Changes that weaken a boundary require explicit security review.
- Release artifacts **SHOULD** include checksums and, where supported, signed
  provenance and an SBOM for executable reference tooling.

## Failure and incident behavior

Security controls fail closed. If schema identity, authorization, integrity,
containment setup, or a required budget cannot be established, processing stops
before side effects.

After suspected compromise, operators should isolate the runner, preserve
bounded audit evidence, rotate exposed credentials, invalidate affected
artifacts, identify impacted dataset versions and replay runs, and publish a
coordinated advisory. Never publish sensitive evidence to prove impact.

## Explicit v0.1 non-goals

The v0.1 specification does not claim to provide multi-tenant isolation,
cryptographic provenance, malware detection, content moderation, privacy-law
compliance, anonymous telemetry, or safe execution of arbitrary code. A
deployment that requires these properties must add and test them independently.

## Verification

The normative verification matrix, including adversarial fixtures and v0.1 exit
criteria, is defined in [`TESTING.md`](TESTING.md). An implementation is not
v0.1 conforming if it passes functional examples but does not satisfy the
security test class.
