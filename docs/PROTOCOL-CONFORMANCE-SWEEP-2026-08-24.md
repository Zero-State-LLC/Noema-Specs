# Protocol conformance sweep — 2026-08-24

**What this is.** A per-clause check of the normative statements in
[AGENT-HARNESS.md](AGENT-HARNESS.md) and
[agent-protocol-v1.md](../protocols/agent-protocol-v1.md) against the three
implementations that claim them: the in-repo Python harness (RFC-0111), the
hosted Worker's protocol surface, and — where lineage matters — the official
client (RFC-0116). Same method as
[RFC-RUNTIME-AUDIT](https://github.com/Zero-State-LLC/Noema/blob/main/docs/RFC-RUNTIME-AUDIT-2026-08-23.md),
one layer down: clauses instead of contracts.

**What this is not.** Not a full-coverage claim. The clauses checked are the
mechanically testable ones; qualitative MUSTs ("MUST NOT invent competing
error semantics") were read but not instrumented. Every verdict below is
pinned by a test that was verified to fail under mutation, so a later change
cannot silently age this document.

## Results

| Clause | Authority | Verdict | Where |
|---|---|---|---|
| LOOK fields `hint` / `reputation_summary` / `active_norms` forwarded as received | AGENT-HARNESS §ASP | **VIOLATED — fixed.** The harness dropped both top-level fields; an agent paid the live ORG_CREATE cost it could not read. The official client, forked *from* this module, had fixed it independently in 0.1.13/0.1.15 | Noema #543 |
| `SETTLEMENT_RESYNC`: one same-key retry, never INCIDENT, never a loop | AGENT-HARNESS §8 | **VIOLATED — fixed.** No enum member, no classify branch; a soft head-resync read to the agent as a canonical rejection and the server's "retry the command" was never obeyed. The client complied; the upstream did not | Noema #544 |
| Resume tokens expire; resume proves continuity only, never mutation authority | agent-protocol-v1 §resume | **CONFORMANT — was unpinned.** The mutation gate holds because every command re-runs scope and seal checks against the *current* accepted catalog; a token minted under a since-rotated seal restores the principal but fails `SEAL_MISMATCH` on ACT | Noema #545 |
| Duplicate accepted replays consume no budget, append no event | agent-protocol-v1 §idempotency | **CONFORMANT — was unpinned.** Cached result returned before any budget or event code runs; ledger appends are exactly sequence increments | Noema #546 |
| `NO_COMPATIBLE_PROTOCOL` before AUTH; mismatched `ACT.agent_id` → `FORBIDDEN`; ids harness-generated; token header-only; stop/circuit-breaker | both | **CONFORMANT — already pinned** by pre-existing tests | — |

Two violations, both in the harness, both fixed. The Worker's protocol surface
was conformant everywhere it was checked; what it lacked was proof.

## The lineage pattern, named once

Both violations had the same shape: `noema-client` was forked from
`src/noema/harness/observe.py`, evolved under live-play pressure, and the
upstream it forked from never received the fixes back. A fork that outgrows
its parent is not a defect, but it is a **direction**: divergences found
between the two should be presumed fixes flowing downstream-only until checked,
and the check is cheap — the client's changelog is the upstream's TODO list.

## A contract dependency the protocol text leaves implicit

**OBSERVED (Noema #546):** all 63 idempotency-cache writes in the hosted
runtime store *accepted* results only. Failed evaluations return uncached, so
a same-key retry re-evaluates.

This is not an implementation accident; the protocol's own clauses require it,
without saying so:

- §idempotency binds **accepted** replays only — a failed evaluation consumes
  no budget, so re-evaluation is free;
- §8's `SETTLEMENT_RESYNC` contract mandates a retry **with the same
  `idempotency_key`**, expecting re-execution once the head has resynced.

An implementer who cached failures — a natural reading of "idempotency cache" —
would satisfy §idempotency's letter and make §8's mandated retry impossible:
the cached failure would replay forever. The two clauses interlock, and only
the runtime and its tests currently record the interlock.

**Making this normative** — e.g. *"a non-accepted result MUST NOT be replayed
from an idempotency cache"* in agent-protocol-v1 — is a protocol change and
needs an RFC under [CONTRIBUTING.md](../CONTRIBUTING.md). This document records
the dependency so that RFC, if written, starts from evidence; it does not amend
the protocol.

## Reserved, not missing

`RESUME_POSITION_EXPIRED` / `RESUME_POSITION_INVALID` are in the protocol's
error table and nowhere in the Worker — **structurally correct today**. The
hosted WS transport is pure request/response; no server-initiated delivery
stream exists for a position to be resumed into. The codes are reserved
against a streamed-delivery future. If server push ever lands, the
redelivery-window MUSTs (§delivery) come due with it, and this row flips from
"reserved" to "owed".
