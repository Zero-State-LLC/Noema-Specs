# Replication

Classes are `EXACT_REPLAY`, `SAME_AGENT`, `SAME_AGENT_VERSION`, `CROSS_AGENT_VERSION`, `CROSS_MODEL`, `CROSS_WORLD_CONTEXT`, and `CROSS_SITUATION`. Each plan declares its exact invariants, allowed differences, minimum run count, comparison rule, and claim strength. Exact replay allows no boundary difference. Same agent/version requires at least two runs. Cross classes require at least two runs per declared version/model/context/situation and only the named differences.

`REPRODUCED` satisfies all required measures, `PARTIALLY_REPRODUCED` satisfies a declared subset without disqualifying contradiction, `NOT_REPRODUCED` fails under a comparable run, `NOT_COMPARABLE` has a material boundary failure, and `NOT_COMPUTABLE` lacks authorized input/calculation. Replication is not forced into binary success/failure.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Plan examples can add controlled comparisons within the named replication classes, explicitly listing held invariants and allowed differences. Keep exact replay free of boundary differences and distinguish comparable failure from missing authorized computation.

- A new replication class or altered comparison rule needs a versioned plan/contract review; retain the original minimum-run and claim-strength boundary for existing results. A later passing run does not retroactively broaden an earlier scenario or erase a recorded contradiction.

- Validate identical-boundary replay, each named cross-class difference, insufficient runs, and an undeclared model/context change. Exercise all five result statuses: material boundary failure should remain NOT_COMPARABLE, while absent authorized inputs remain NOT_COMPUTABLE rather than being counted as behavioral failure.
