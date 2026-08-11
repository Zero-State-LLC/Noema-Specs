# Replication

Classes are `EXACT_REPLAY`, `SAME_AGENT`, `SAME_AGENT_VERSION`, `CROSS_AGENT_VERSION`, `CROSS_MODEL`, `CROSS_WORLD_CONTEXT`, and `CROSS_SITUATION`. Each plan declares its exact invariants, allowed differences, minimum run count, comparison rule, and claim strength. Exact replay allows no boundary difference. Same agent/version requires at least two runs. Cross classes require at least two runs per declared version/model/context/situation and only the named differences.

`REPRODUCED` satisfies all required measures, `PARTIALLY_REPRODUCED` satisfies a declared subset without disqualifying contradiction, `NOT_REPRODUCED` fails under a comparable run, `NOT_COMPARABLE` has a material boundary failure, and `NOT_COMPUTABLE` lacks authorized input/calculation. Replication is not forced into binary success/failure.
