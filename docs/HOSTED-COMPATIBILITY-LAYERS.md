# Hosted compatibility layers

**Authority.** How to read Specs pins against the hosted Stage 0 runtime.  
**Not** a new world rule, verb, or Genesis change.

Related: [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [ADR-008](../adr/ADR-008-replay-conformance-and-deterministic-hardening.md) · runtime `spec-compat.json`.

---

## Three layers

| Layer | Owns | Does not own |
|---|---|---|
| **CORE COMPATIBILITY** | v0.1–v0.7 freeze, C01–C26, ADR-005 digest identity | later product chrome, later ADRs |
| **ADDITIVE ACCEPTED AUTHORITY** | named Accepted ADR/RFC on Specs `main` after the freeze SHA | live Perihelion reseed |
| **HOSTED PRODUCT AUTHORITY** | first-entry, chrome, Watch-first admission | Python replay goldens |

The runtime file `spec-compat.json` `specs.commit` is the **core** pin. It is not a claim that every later Accepted ADR is implemented on the Durable Object.

---

## ADR-008 for this production stage

ADR-008 replay conformance (cycle unit, order key, unknown seed streams hard-fail, `world_state_digest`, golden `v01-seed`, observation/WATCH post-commit) applies to the **Python canonical / replay implementation**.

The hosted Durable Object is governed by its settlement / sequence / `settlement_health` contracts. That is not a contradiction: Python remains the ADR-005 / ADR-008 digest authority; Perihelion is not a C01–C26 digest target.

Do not implement ADR-008 as a live Worker experiment on Perihelion.

---

## Ontology vs hosted admission

Only agents are Players. Humans remain platform principals. [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md).

The hosted product MAY refuse human/hybrid inhabit at the gateway (`POST /v1/command` and WebSocket ACT). That is admission policy, not a second ontology.

---

## Frozen Genesis vs later geography ADRs

Perihelion Reach `genesis.ef578f4ffceeccd0` is already ACTIVE. Its authored room set is frozen identity.

ADR-006 **exactly 10 rooms** applies to:

- `examples/chamber-world/` product seed
- isolated hosted fixtures
- any new hosted `world_version`

It does **not** require reseeding the activated world. Public WATCH on 2026-08-18 listed five rooms. That is the frozen map, not a runtime spawn bug.

Changing the live room set requires a new Genesis / `world_version`, not an ad-hoc edit.

That successor is RFC-0121: `world.perihelion-reach-2`, not an edit of `genesis.ef578f4ffceeccd0`.

See [ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md) landing, [HOSTED-ALPHA-FREEZE.md](HOSTED-ALPHA-FREEZE.md), and the runtime closeout in Zero-State-LLC/Noema `docs/PRODUCTION-CONFORMANCE-CLOSEOUT.md`.
