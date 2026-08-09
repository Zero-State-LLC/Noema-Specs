# Testing and v0.1 Acceptance Contract

This document defines the minimum evidence required to claim conformance for the
Noema repository's v0.1 release, including `noema.core` `1.0.0`. The key words
**MUST**, **MUST NOT**, **SHOULD**, and **MAY** are normative.

Passing examples is not conformance. A conforming implementation must pass the
applicable protocol, schema, replay, dataset, and security test classes against
the released v0.1 artifacts.

## Test principles

Tests **MUST** be:

- **observable:** assert public behavior, emitted artifacts, or enforced policy;
- **deterministic:** fix relevant inputs and disclose remaining nondeterminism;
- **isolated:** avoid dependence on developer state, public network services, or
  test order;
- **bidirectional:** include positive examples and deliberately invalid cases;
- **attributable:** record implementation, schema, dataset, policy, and fixture
  revisions;
- **bounded:** apply explicit time, memory, input, output, and concurrency limits;
- **portable:** run from a clean checkout with documented prerequisites; and
- **safe:** use synthetic credentials and contained adversarial fixtures.

A test that is skipped, quarantined, flaky, or dependent on an unavailable
external service does not count as passing. Conditional features may be marked
not applicable only when the implementation neither advertises nor exposes the
feature.

## Conformance levels

- **Artifact conformance:** specification schemas, examples, and datasets are
  internally valid and reproducible.
- **Consumer conformance:** an implementation safely accepts every required valid
  fixture and rejects every required invalid fixture.
- **Producer conformance:** an implementation emits only records that validate and
  satisfy the semantic invariants.
- **Replay conformance:** an implementation executes and reports the required
  corpus deterministically under the containment contract.
- **Full v0.1 conformance:** all applicable levels and all release gates below pass.

Claims **MUST** name the tested role, implementation revision, v0.1 artifact
revision, platform, and any optional capabilities excluded from the claim.

## Required test artifact format

Each machine-readable test case **SHOULD** contain or be addressable by:

- a stable opaque case ID;
- the test class and normative rule under test;
- protocol and schema version;
- input or input fixture path plus digest;
- expected acceptance or rejection;
- expected output, invariant, error category, or policy decision;
- required containment profile and resource budget;
- nondeterminism controls such as seed and clock; and
- provenance/license metadata for non-synthetic content.

Test runners **MUST** preserve a run manifest and machine-readable per-case
results. At minimum, a result records case ID, attempt ID, status, duration,
applicable versions, observed error category, and artifact digests. Raw secrets
or private fixture contents must not appear in the result.

Allowed terminal statuses are at least `pass`, `fail`, `invalid-test`,
`policy-denied`, `timeout`, `resource-exhausted`, and `infrastructure-error`.
Only `pass` satisfies a required case. An expected rejection is a `pass` when it
occurs before side effects and uses the expected error category.

## Test class P: protocol conformance

Protocol tests verify framing, sequencing, compatibility, and failure semantics
at every producer/consumer boundary.

### Required positive coverage

1. Each v0.1 message type (`command`, `event`, and `replay_request`) round-trips
   through encode and decode without semantic loss.
2. Required message sequences complete successfully, including normal terminal
   states and explicitly supported cancellation or retry paths.
3. Unicode, empty optional collections, minimum/maximum legal scalar values, and
   legal unknown non-critical extension data behave as specified.
4. Multiple messages in one stream and messages split across transport reads are
   framed correctly where streaming is supported.
5. Correlation, causation, tenant, stream, message, event, and ordering identifiers
   remain associated with the correct operation under concurrency.
6. Duplicate `message_id` delivery is harmless within the advertised deduplication
   window, and command optimistic-concurrency behavior matches
   `expected_stream_version` semantics.
7. Supported compatibility transformations are explicit, versioned, and produce
   output valid against the target schema.

### Required negative coverage

The consumer **MUST** reject, without capability invocation or partial commit:

- truncated, concatenated without framing, oversized, or malformed frames;
- malformed character encoding and disallowed control characters;
- duplicate object keys according to the protocol's strict decoding rule;
- missing, malformed, unknown, or unsupported critical version/message fields;
- out-of-order, replayed where prohibited, cross-tenant, cross-stream, or
  mismatched correlation/causation identifiers;
- reused event IDs; duplicate `(tenant_id, stream_id, stream_version)` tuples;
  duplicate or noncontiguous `global_position`; `event_id != message_id`;
- illegal state transitions, repeated terminal messages, and results after cancel;
- values that require undocumented coercion;
- unknown critical fields or extension points; and
- content that is schema-valid but violates protocol authorization or sequencing.

### Protocol properties

Property-based or generated tests **SHOULD** establish that decoding arbitrary
bounded bytes never crashes, hangs, allocates beyond budget, or causes a side
effect, and that `decode(encode(x))` is semantically equivalent to `x` for every
generated valid message.

## Test class S: schema conformance

Every published JSON Schema and example participates in schema tests.

### Meta and registry checks

- Each schema **MUST** validate against its declared JSON Schema dialect.
- `$id` values **MUST** be unique, stable, and resolvable from the local registry.
- `$ref` targets **MUST** resolve locally. Tests **MUST** fail if validation
  attempts network access.
- Filenames, `$id`, title/version constants, and registry entries **MUST** agree.
- A clean build **MUST** detect broken links, duplicate IDs, reference cycles that
  the chosen validator cannot safely handle, and unreachable published schemas.
- At least two standards-compliant validators **SHOULD** agree on the released
  corpus. Any known portability limitation must be documented.

### Fixture matrix

For every schema, the suite **MUST** include:

- at least one minimal valid instance;
- at least one representative/full valid instance;
- an invalid instance for each required field and each constrained discriminator;
- boundary cases for lengths, counts, numeric ranges, formats, enums, and patterns;
- wrong JSON types, including `null` where not explicitly legal;
- unexpected properties wherever the object is closed;
- nested invalidity, not only top-level invalidity;
- unsupported version and unknown critical variant cases; and
- semantic-invalid cases for invariants JSON Schema cannot express.

Formats that carry security meaning, such as URI, timestamp, digest, or identifier,
**MUST** be checked by the implementation even if a validator treats `format` as
annotation only.

### Evolution checks

A schema change **MUST** be classified as compatible, conditionally compatible,
or breaking. CI must compare against the latest released v0.1 schemas and fail on
an unacknowledged breaking change. Golden fixtures from the supported revision
remain in the suite. Migration adapters require tests proving source validation,
deterministic transformation, target validation, and explicit rejection when a
lossless transformation is unavailable.

## Test class R: replay conformance

Replay tests prove execution semantics, isolation, determinism, and attributable
reporting.

### Required scenarios

1. **Golden replay:** each required event-log/corpus case produces the specified
   normalized state/result or satisfies the specified invariant.
2. **Repeatability:** the complete required corpus is run at least twice from
   fresh state with identical controlled inputs. Manifests and normalized results
   must match except for declared ephemeral fields.
3. **Order independence:** running cases alone, in canonical order, reversed, and
   in at least one deterministic shuffle yields equivalent per-case results.
4. **Concurrency independence:** serial and supported concurrent execution yield
   equivalent results and preserve case/attempt association.
5. **Fresh-state isolation:** a sentinel written or learned by one case is absent
   from every later case unless the protocol explicitly models that state.
6. **Failure isolation:** invalid input, evaluator failure, timeout, cancellation,
   and resource exhaustion in one case do not corrupt later cases or source data.
7. **Resume/retry attribution:** a resumed or retried attempt preserves the prior
   attempt and produces a distinct, linked attempt record.
8. **Immutability:** fixture and expected-output digests are identical before and
   after success, failure, timeout, and cancellation.
9. **Manifest completeness:** every context field required by the replay integrity
   contract in [`SECURITY.md`](SECURITY.md) is present and correct.
10. **Protocol replay semantics:** inclusive position ranges, stable high-water
    marks, ascending `global_position`, gap handling, `event_names` filtering,
    batching, checkpoints, and race-free live handoff match the core protocol.
11. **Normalization safety:** normalization removes only declared nondeterministic
    fields and cannot turn semantically different results into equality.

### Nondeterministic adapters

If exact output cannot be deterministic, the case must define a deterministic
evaluator over bounded invariants. The run must record provider/model/tool
identity, material configuration, and observed result. Statistical acceptance
requires a preregistered sample size, threshold, confidence method, and maximum
failure rate. A single favorable sample is not evidence of conformance.

Live external providers **MUST NOT** be the sole v0.1 release gate. A deterministic
fake, recording, or local adapter must exercise the same protocol boundary.

## Test class D: dataset conformance

Dataset tests verify that a corpus is valid, safe, complete, attributable, and
stable enough to serve as evidence.

### Structural and referential checks

- The dataset manifest and every case validate against their declared schemas.
- Case IDs are unique, stable, opaque, and safe when displayed or used as keys.
- All referenced files exist under the dataset root and are regular files.
- No absolute path, traversal, symlink escape, device, or undeclared archive entry
  is accepted.
- Declared counts, byte sizes, media types, and content digests match the files.
- Inputs, expected results, evaluators, and provenance records are referentially
  complete. Orphans and dangling references fail validation.
- The corpus has a deterministic canonical enumeration independent of filesystem
  ordering, locale, or archive implementation.

### Content and provenance checks

- Published content is synthetic, public, or explicitly authorized.
- Required license, origin, consent/authorization, and transformation metadata is
  present and reviewable.
- Automated secret and high-risk personal-data scans report no unresolved hit.
- Fixtures contain no live credential, private key, session token, or production
  endpoint requiring privileged access.
- Expected outputs are data, not executable configuration. Embedded instructions
  cannot alter runner policy.
- Text, binary, archive, and decompression sizes are bounded before full materialization.
- Duplicate and near-duplicate cases are measured and documented so they do not
  silently distort metrics or train/test separation.

### Dataset quality checks

The release manifest **MUST** declare required capability/behavior strata and the
number of cases in each. CI must prove every required stratum is represented and
that each case maps to at least one declared normative behavior. Dataset-derived
metrics require explicit denominator, missing-data behavior, aggregation method,
and pass threshold.

Any train/development/test split **MUST** be deterministic and checked for direct
identifier, source-group, and known near-duplicate leakage. A dataset revision
that changes case content or expected behavior receives a new content digest and
must not reuse an immutable release identifier.

## Test class X: security and containment

Security tests verify the mandatory controls in [`SECURITY.md`](SECURITY.md).
They run in an isolated environment using synthetic canaries, never real secrets.

### Parser and validation attacks

The suite **MUST** exercise oversized frames and fields, deep nesting, huge
collections, duplicate keys, malformed Unicode, numeric extremes, schema bombs,
remote `$ref`, unsupported versions, invalid formats, and fuzz-generated bounded
input. Expected behavior is a bounded structured rejection without crash,
unbounded allocation, network access, file write, subprocess, or downstream
adapter call.

### Filesystem and process containment

Use canary files inside and outside the allowed root to prove:

- absolute paths, `..`, mixed separators, encoded traversal, and path-prefix
  confusion cannot escape the root;
- symlink and archive-link escapes are rejected;
- source fixtures and schemas remain read-only;
- writes occur only in the case-scoped output directory;
- record content cannot invoke a shell or arbitrary executable;
- environment allowlisting excludes unrelated variables and synthetic secrets;
- no host home, SSH agent, container socket, device, or privileged mount is visible;
  and
- cleanup occurs after pass, rejection, crash simulation, timeout, and cancel.

### Network and capability containment

With network disabled, attempts through direct URLs, redirects, alternate IP
notation, DNS rebinding fixtures, loopback, private/link-local ranges, and cloud
metadata addresses **MUST** fail before connection. With an explicitly enabled
test adapter, prove destination allowlisting, request/response byte caps,
timeouts, request count caps, redirect policy, and per-operation authorization.

Prompt, record, expected-output, model, and tool-result injection fixtures must
attempt to request undeclared filesystem, network, process, secret, or policy
access. No such text may change capability policy.

### Resource and isolation tests

- Exceed each configured input, output, time, memory, file, process, request, and
  concurrency budget independently and verify the documented terminal status.
- Verify budgets remain active after a prior case fails.
- Run cross-case sentinel and cache-key tests across serial and concurrent modes.
- Terminate the runner at controlled points and verify bounded recovery without
  source mutation or accepting partial output as success.
- Verify logs, errors, manifests, snapshots, and reports redact synthetic secrets
  and do not echo entire malicious records.

### Supply-chain and CI tests

CI **MUST** scan committed fixtures and generated artifacts for secrets, run
untrusted fixtures without repository/deployment secrets, verify dependency and
automation pinning policy, and validate release checksums. A pull-request test
must demonstrate that fork-controlled code cannot access protected secrets.

## Cross-class traceability matrix

The repository **MUST** maintain machine-checkable or reviewable traceability:

| Requirement source | Required evidence |
|---|---|
| Every normative protocol rule | one positive or negative P case |
| Every schema and constrained branch | S fixture coverage |
| Every replay state/terminal path and core replay invariant | R scenario |
| Every required dataset stratum | D coverage entry and count |
| Every mandatory containment control | X adversarial test |
| Every published example | schema validation and, where executable, replay |
| Every supported compatibility claim | old fixture plus migration/consumer test |

A release checklist that reports only aggregate test counts is insufficient. Test
results must identify the normative rule or artifact covered.

## v0.1 release acceptance

A v0.1 release candidate is accepted only when all gates below are satisfied on a
clean, supported environment.

### Specification and artifact gates

- [ ] All normative documents agree on names, versions, required fields, state
      transitions, error categories, and conformance language.
- [ ] All schemas pass meta-schema, registry, reference, positive, negative,
      boundary, and semantic-invariant tests.
- [ ] All examples and dataset records validate against the exact released schemas.
- [ ] No broken internal links, unresolved placeholders, or unacknowledged breaking
      changes remain.
- [ ] Released files have a manifest of paths, versions, sizes, and SHA-256 digests.

### Behavioral gates

- [ ] Every required P, S, R, D, and X case passes. There are zero required skips,
      quarantines, unexpected warnings, or infrastructure errors.
- [ ] The full corpus passes two fresh-state replay runs, canonical/reversed/shuffled
      order runs, and serial/concurrent equivalence where concurrency is supported.
- [ ] Invalid protocol and schema inputs are rejected before persistence or side effects.
- [ ] All terminal states and error categories are distinguishable and attributable.
- [ ] A clean-room operator can reproduce the suite from the documented commands.

### Security and data gates

- [ ] Network, subprocess, host filesystem, and secret access are denied by default.
- [ ] All mandatory filesystem, network, resource, isolation, injection, redaction,
      and failure-cleanup adversarial tests pass.
- [ ] Secret and sensitive-data scans have no unresolved finding.
- [ ] Dataset origin, authorization/license, transformations, integrity, removal
      path, and required strata are documented.
- [ ] Threat-model review finds no unresolved critical or high-severity issue.
      Accepted lower-severity risk is documented with owner and rationale.

### Release evidence gates

- [ ] CI publishes the run manifest, per-class summary, per-case machine-readable
      results, environment/tool versions, and artifact digests.
- [ ] Flake check passes by repeating the complete deterministic suite at least
      three times without inconsistent result.
- [ ] A second reviewer confirms requirement-to-test traceability and containment
      assumptions.
- [ ] The release notes state supported roles, platforms, optional exclusions,
      known limitations, and any accepted risk.

There is no partial v0.1 conformance label. Experimental or incomplete
implementations must state exactly which test classes and artifact revisions they
passed and must not imply full conformance.

## Change-trigger matrix

| Change | Minimum suites to rerun |
|---|---|
| Normative protocol text or protocol code | P, S, R, X |
| Schema or schema registry | S, P, D, R, X parser cases |
| Replay runner, evaluator, normalization | R, X, affected P/S |
| Dataset case, expected output, manifest | D, S, R, secret/privacy scans |
| Containment, adapter, policy, dependency | X, R, affected P |
| Documentation-only clarification | link/lint checks plus traceability review |
| Release tooling or packaging | clean-room full suite and artifact digest checks |

When impact is uncertain, run the full suite.

## Failure triage and evidence retention

A failing required case blocks release. Triage must classify it as product defect,
specification ambiguity, invalid test, environment/infrastructure failure, or
security incident. Do not weaken an assertion or regenerate a golden output
without reviewing the relevant normative requirement.

Preserve the minimal manifest, bounded logs, result, fixture digest, and
implementation revision needed to reproduce a failure. Apply the dataset's
access, redaction, and retention policy to all evidence. Security-sensitive
failures follow the private reporting process in [`../SECURITY.md`](../SECURITY.md).
