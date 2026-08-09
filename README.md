# Noema Specifications

Noema is a systems-driven game about discovering a world that does not explain itself. Players observe phenomena, form models, design experiments, and turn reproducible knowledge into new capabilities. This repository is the canonical, implementation-independent specification and wire-contract source for the product.

## Product promise

Noema makes scientific reasoning playable without reducing it to trivia. The world has hidden but stable rules. Instruments expose partial evidence. Experiments can falsify beliefs. Progress comes from building better explanations and using them to reach a moving frontier.

## Start here

- [Vision](docs/VISION.md)
- [Game design](docs/GAME-DESIGN.md)
- [Architecture](docs/ARCHITECTURE.md)
- [World model](docs/WORLD-MODEL.md)
- [Terminology](docs/TERMINOLOGY.md)
- [Specification checklist](SPEC-CHECKLIST.md)
- [Contributor guide](CONTRIBUTING.md)

## Contracts

- Normative protocol: [`protocols/core.md`](protocols/core.md)
- Draft 2020-12 schemas: [`specs/`](specs/)
- Valid wire documents: [`examples/`](examples/)

Current protocol identity is `noema.core` version `1.0.0`. Schema IDs are stable HTTPS identifiers rooted at `https://specs.noema.dev/1.0/`.

## System map

| Area | Canonical document |
| --- | --- |
| Adaptive progression | [Frontier Director](docs/FRONTIER-DIRECTOR.md) |
| Observation and evidence | [Observatory](docs/OBSERVATORY.md) |
| Experimental workflow | [Experiment Lab](docs/EXPERIMENT-LAB.md) |
| Content compilation | [Phenomenon Compiler](docs/PHENOMENON-COMPILER.md) |
| Knowledge-gated progression | [Capability Graph](docs/CAPABILITY-GRAPH.md) |
| Authoring and validation | [Phenomena Lab](docs/PHENOMENA-LAB.md) |

## Core principles

1. **Reality precedes explanation.** Simulation resolves from canonical laws, never the player's current theory.
2. **Evidence has provenance.** Claims trace to observations, instruments, conditions, and transformations.
3. **Failure teaches.** Negative and ambiguous results preserve useful information.
4. **Knowledge unlocks agency.** Capabilities follow demonstrated understanding, not arbitrary experience points.
5. **Mystery is fair.** Hidden rules are stable, discoverable, and sufficiently signposted.
6. **Generation is bounded.** Authored constraints and validation gates surround procedural variety.

Normative language uses **MUST**, **SHOULD**, and **MAY** as described in [CONTRIBUTING.md](CONTRIBUTING.md). Durable behavioral changes use the [RFC process](rfcs/0000-rfc-process.md).

## License

Licensing is not yet specified. Do not assume rights beyond those granted by the repository owner.
