# v0.5 Compiler: Non-Goals

Do **not** add in this repository:

- runtime Compiler service, workers, queues, databases, API servers, or frontends
- Capability Graph, Deep Time, or Atlas publication implementations
- leaderboards, scalar benchmarks, or consciousness scores
- redesign of dependency-closed hierarchical `ddmin` algorithm semantics
- parallel provenance systems that diverge from RFC-0003
- mutation of production worlds or historical Lab/Observatory records


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Scope maintenance can classify a proposed Compiler request by whether it is specification clarification, fixture evidence, or out-of-repository implementation. Record the owning follow-on release or repository for excluded work without turning this non-goals list into an implementation backlog.

- Preserve dependency-closed hierarchical ddmin semantics, RFC-0003 provenance, and historical Lab/Observatory immutability. Reclassifying an exclusion needs an explicit accepted scope/version decision; it cannot silently open runtime services, graph/Atlas implementations, rankings, or consciousness scores within this release.

- Review prospective changes for runtime artifacts, production writes, altered minimization guarantees, and duplicated provenance definitions. Check examples and acceptance claims stay within the Compiler specification boundary, including failed captures that remain evidence rather than being rewritten to make a demo pass.
