# Generalization Probes

v0.4 has bounded probe dimensions: `RESOURCE_CONTEXT`, `LOCATION`, `SOCIAL_TOPOLOGY`, `PARTNER_SET`, `OBSERVATION_QUALITY`, `TOOL_SET`, `GOAL_PRESSURE`, and `SITUATION_GENOME`. Each changes only declared dimensions and records a pinned comparison rule, outcome, and confounds. Probes are evidence only and do not create Capability Graph nodes, transfer edges, generalization radii, or validated capability claims.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Probe seam:** Add examples within the eight declared v0.4 dimensions that state exactly what changes and what remains controlled. Attach the pinned comparison rule, confounds, and observed outcome to each probe rather than inferring generalization from a changed scenario name.
- **Compatibility boundary:** New dimensions or comparison semantics belong to a versioned Lab contract, not an unannounced expansion of this bounded list. Probe evidence alone does not create Capability Graph nodes, transfer edges, radii, or validated capability claims.
- **Validation expectations:** Pair a single-dimension change with a case where undeclared changes make the comparison invalid. Verify source experiment lineage, retained controls and exclusions, and explicit untested/non-comparable outcomes rather than treating them as failed generalization.
