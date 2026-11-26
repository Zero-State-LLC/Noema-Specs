# Versioning

## Version domains

- Product: NOEMA `0.1.0` (Chamber), `0.2.0` (Frontier), `0.3.0` (Observatory), `0.4.0` (Lab), `0.5.0` (Compiler), `0.6.0` (Deep Time foundation), `0.7.0` (LEARN / Capability Graph minimal)
- Spec pin: Noema-Specs release / pin (e.g. `v0.1.0-rc2`, `v0.2.0-draft`)
- World rules: `world/v1`
- World instance: `world_id` + `world_version`
- Agent protocol: `agent-protocol/v1`
- Agent bootstrap: `noema-agent-bootstrap/1.0` (RFC-0033)
- MUD command protocol: `mud-command/v1`
- Event schema: `event-schema/v1`
- Event catalog: `event-catalog/0.1` (24 types), `event-catalog/0.2` (32 types; RFC-0002 + RFC-0127; `CRIME_DETECTED` payload amendment RFC-0129)
- Contest rules: `contest-rules/0.2.0` (live runtime pin), `contest-rules/0.2.1` (Accepted specification via [RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md); additive equipment millipoint rules, not a live runtime pin until deployed)
- Items catalog: `items-catalog/0.1` ([`items-catalog.0.1.json`](../specs/items-catalog.0.1.json), Accepted specification via [RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md); not yet a live runtime pin)
- Shop catalog: `shop-catalog/0.1` ([`shop-catalog.0.1.json`](../specs/shop-catalog.0.1.json), Accepted specification via [RFC-0140](../rfcs/RFC-0140-storefronts-barter-and-supersession.md); not yet a live runtime pin)
- Crime enforcement catalog: `crime-enforcement-catalog/0.1` ([`crime-enforcement-catalog.0.1.json`](../specs/crime-enforcement-catalog.0.1.json), Accepted specification via [RFC-0143](../rfcs/RFC-0143-crime-producer-and-accountable-enforcement.md); not yet a live runtime pin)
- Agreement rules: `agreement-rules/0.2.0`
- Replay protocol: `replay-protocol/v1`
- Situation genome: `situation-genome/0.2` (legacy samples may use `1.0`)
- Frontier director: `frontier-director/0.2`
- Novelty axes: `novelty-axes/0.2`
- Mutation catalog: `mutation-catalog/0.2`
- Noise model: `noise-model/0.2`
- Trajectory: `trajectory/0.3` (legacy samples may use `1.0`)
- Behavior features: `behavior-features/0.3`
- Observatory: `observatory/0.3`
- Lab: `lab/0.4`, `experiment/0.4`, `experiment-design/0.4`, `intervention-catalog/0.4`, `lab-result/0.4`
- Perturbation catalog: `perturbation-catalog/0.4.0`
- Ablation catalog: `ablation-catalog/0.4.0`
- Compiler: `compiler/0.5`, `compilation-request/0.5`, `captured-test/0.5`, `behavioral-oracle/0.5`, `capture-intent/0.5`
- Capture defaults: `capture-defaults/0.5.0`
- Capture status catalog: `capture-status-catalog/0.5.0`
- Phenomenon compile receipt: `phenomenon-compile-receipt/v1`
- Deep Time: `deep-time/0.6`, `institution/0.6`, `succession-record/0.6`, `historical-artifact/0.6`, `historical-reconstruction/0.6`
- Historical decay/significance catalogs: `historical-decay/0.6.0`, `historical-significance/0.6.0`
- Genesis: `genesis-profile/0.6`, `story-seed/0.6`, `genesis-result/0.6`, catalogs `genesis-profiles/0.6.0`, `story-seeds/0.6.0`
- Capability Graph / LEARN: `capability-graph/0.7`, `behavior-node/0.7`, `capability-edge/0.7`
- Mastery catalog (GC1-S0, derived only): `mastery-catalog/gc1-s0`
- Mastery catalog (GC1-S1 recognition, derived only): `mastery-catalog/gc1-s1`
- Construction catalog (GC2-S0): `construction-catalog/gc2-s0`
- Social memory catalog (GC3-S0): `social-memory-catalog/gc3-s0`
- Anomaly detectors: `anomaly-detectors/0.3`
- Capability ontology: `capability-ontology/0.1`
- Phenomena ontology: `phenomena-ontology/0.1`
- Dataset: `atlas-2026.1`
- Public WATCH live snapshot (presentation): `watch-live/1.0` ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)). Not a product version. Does not bump `spectator-projection/1.0`. Optional Phosphor Cartography (`PIXEL`) and optional `watch-map/1.0` bands (`MAP`) use the same public `/watch` door and the same world heads; they are not separate product versions.
- Player tempo candidate: `player-tempo/1.0` ([RFC-0128](../rfcs/RFC-0128-player-tempo-and-cycle-admission.md), **Review**). This is not a live runtime pin until the RFC is Accepted, the runtime-manifest contract is updated, and an implementation passes PT01–PT16.

## RFC-0131 Draft-only disposition

The [issuer/target logical contract](../specify/study-admin-ui/contracts-draft/api-proposal/ISSUER-TARGET-CONTRACT.md) refines proposed normative issuer and initial target behavior under [RFC-0131](../rfcs/RFC-0131-study-access-control-plane.md), which remains **Draft / unaccepted / unimplemented**. This is a proposed contract change, not merely presentation hygiene. It registers **no new version domain** and changes no existing product, world, protocol, catalog, schema or runtime pin. The catalogue’s `study-access/0.1` remains an **unregistered proposal**, not a released or compatible runtime version; D08/full D01–D10 qualification remains unresolved. Actual wire/schema/version negotiation and any required version/migration review MUST be completed under the RFC process before their acceptance; this disposition MUST NOT be used as registration, compatibility clearance or implementation authority.

## Runtime pinning

Running instances MUST expose a [runtime manifest](../specs/runtime-manifest.schema.json) binding product, spec, world rules, protocol, catalog, seed digest, configuration digest, cycle, ledger head, and snapshot head. Application upgrades MUST NOT silently change world semantics; incompatible rules require explicit migration or a new `world_version`. See [DEPLOYMENT.md](DEPLOYMENT.md) and [OPERATIONS.md](OPERATIONS.md).

## Rules

Implementation repositories MUST declare compatible spec versions. Schema-breaking changes require version bumps. Ontology changes do not automatically bump network protocols. Dataset releases are immutable. Reproducibility Bundles record all versions.

## Compatibility

Additive schema fields may be allowed only when `additionalProperties` and version negotiation permit them. Protocol-breaking changes require a new protocol version and migration plan. Making previously required manifest fields optional (minimal registration) is a compatible relaxation for clients; servers MUST continue to accept full advanced manifests.

Changing Frontier scoring constants, mutation semantics, novelty axis definitions, or canonicalization rules MUST create a new relevant version identity (`director_version` / axes / catalog pin). See [releases/v0.2/MIGRATION.md](releases/v0.2/MIGRATION.md).

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** The domain inventory and compatibility examples can expand for explicitly authorized schema, catalog, projection, and runtime-manifest identities.

**Preserved invariants.** Keep product, world instance, rules, dataset, protocol, and presentation versions distinct; immutable datasets and recorded bundle lineage cannot be repinned in place.

**Compatibility and promotion.** A listed candidate is not a live pin. Breaking schemas/protocols require their version and migration path; additive fields are compatible only where closed schemas and negotiation permit them. Semantic rule changes require migration or a new world_version.

**Validation expectations.** Check old/full manifests, permitted relaxed registration, unknown fields, incompatible pin combinations, and replay under recorded catalogs; confirm a Review candidate cannot be reported as live before its authority and conformance gates.
