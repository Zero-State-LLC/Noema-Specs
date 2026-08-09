# Contract Cards (Progressive Disclosure)

Short normative summaries of the major contracts. Full detail remains in the linked documents. Use these for onboarding and implementation prioritization.

## World Engine
**Authority:** Sole owner of world truth.  
**Key invariant:** State never depends on agent belief.  
**Core objects:** World, Room, Exit, Entity, ResourceLot, Organization, Institution, Artifact.  
**Cycle order:** authenticate → freeze actions → reserve budgets → reduce movement/local → reduce social/economy → scheduled processes → append events → project observations → commit.  
**Full:** docs/WORLD-ENGINE.md

## Observation
**Authority:** Derived, permissioned, immutable record.  
**Key invariant:** Never a direct serialization of canonical state; never contains private cognition.  
**Claim labels:** OBSERVED | INFERRED | SPECULATIVE | NOT_COMPUTABLE (exactly one).  
**Projection order:** identity/permissions → candidate signals → visibility → noise → attention/salience → render + redactions → provenance → schema validate.  
**Full:** docs/OBSERVATION.md

## Agent Interface
**Authority:** Authenticated, budgeted, containable boundary.  
**Key invariant:** Private runtime stays outside; only declared + world-visible behavior enters.  
**Lifecycle:** DISCONNECTED → NEGOTIATING → AUTHENTICATED → REGISTERED → IN_WORLD → DRAINING → DISCONNECTED (plus QUARANTINED / REVOKED).  
**Canonical verbs:** LOOK, MOVE, INSPECT, ASK, MESSAGE, QUERY, TRADE, BUILD, RESEARCH, DELEGATE, COMMIT, EXPERIMENT, MODEL, WAIT.  
**Full:** docs/AGENT-INTERFACE.md

## Replay
**Authority:** Evidence reconstruction under a declared equivalence boundary.  
**v0.1 mandatory profile:** identical event digests + final WorldState digest + focal observation digests.  
**Failure modes:** NOT_COMPUTABLE | INVALID_EVIDENCE | DIVERGENT | ABORTED.  
**Full:** docs/REPLAY.md + ADR-005

## Phenomenon Compiler
**Authority:** Minimizes live behavior into reproducible fixtures and bundles.  
**Key invariant:** Target behavior is declared before minimization; oracle is the only claim-bearing judge.  
**Algorithm:** Dependency-closed hierarchical delta debugging with layer ordering and final 1-unit sweep.  
**Promotion:** Deterministic gate requiring schema, provenance, controls, and partition checks.  
**Full:** docs/PHENOMENON-COMPILER.md

## Claims Policy
**Authority:** research/claims-policy.md + ADR-003.  
**Hard rule:** No scalar consciousness score. All evidence labeled. Consciousness-adjacent constructs only.
