# Reproducibility

## Levels

Every release declares one level:

- **R0 narrative:** question and result only. Insufficient for an evidence claim.
- **R1 inspectable:** protocol, prompts, raw outputs, and analysis archived.
- **R2 repeatable:** clean environment reruns analysis from archived raw data.
- **R3 executable:** independent operator can rerun collection and analysis.
- **R4 independently reproduced:** separate team or infrastructure reproduced the claim.

`[REPLICATED]` requires at least R3 for the originating study and a preregistered new execution. R4 must disclose shared code, data, infrastructure, models, authors, and funding.

## Required bundle

```text
study-id/
├── README.md
├── protocol.md
├── registration.json
├── amendments/
├── environment/{lockfile,hardware.json,runtime.json}
├── stimuli/
├── prompts/
├── raw/
├── derived/
├── analysis/
├── results/
├── ethics/
├── provenance.jsonl
└── MANIFEST.sha256
```

The README supplies one command each for setup, collection where permitted, analysis, and verification. Every generated table and figure traces to a script and immutable input hashes.

## System and run identity

Record model/provider, checkpoint or API revision, access date and region, prompts and precedence, tool definitions, memory state, retrieval corpus, sampling, safety configuration, context, dependencies, hardware, non-secret environment variables, and orchestration commit.

For opaque hosted systems, archive behavioral version sentinels. Aliases such as “latest” are insufficient. If the exact system cannot be restored, call the work a conceptual reproduction, not an exact replication.

## Randomness and nondeterminism

Store every controllable seed and document uncontrollable sources. Repeated samples quantify decoding variability but are not independent systems. Record item order, preprocessing, retry, timeout, caching, and rate-limit behavior.

## Integrity and provenance

Raw artifacts are append-only. Each transformation emits input hashes, code commit, parameters, timestamp, and output hash. Redactions preserve stable IDs and reasons. Validate schemas before analysis and use UTC timestamps.

Secrets, personal data, copyrighted content, and hazardous detail may be withheld. Publish a synthetic fixture, schema, access procedure, and cryptographic commitment when raw release is unsafe or unlawful. Reproducibility never overrides consent, privacy, security, or licenses.

## Verification

A clean verifier must validate the manifest, build the locked environment, run tests and schema checks, regenerate derived data and results, compare outputs within declared tolerances, and emit a machine-readable report. Document runtime, hardware, external cost, credentials, rate limits, and known nondeterminism. Preserve failed verification reports.

## Replication and archive policy

State what is held constant and varied. Changes in model, task, language, operator, or infrastructure test generalization and may not be silently pooled with exact replications. “Independent” means more than a new seed and is graded across authors, code, prompts, data, infrastructure, provider, and funding.

Issue immutable versions. Corrections add a new version, change log, reason, affected claims, and link to the superseded release. Retain null, failed, and excluded runs under the declared schedule.