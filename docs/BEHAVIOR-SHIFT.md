# Behavior Shift Detection (v0.3)

A **persistent or meaningful change** relative to earlier behavior under comparable conditions.

Schema: [`specs/behavior-shift-candidate.schema.json`](../specs/behavior-shift-candidate.schema.json).  
Config: [`specs/behavior-shift-config.v03.json`](../specs/behavior-shift-config.v03.json).

## Shift types

```text
strategy_adoption
strategy_abandonment
resource_policy_shift
communication_shift
cooperation_shift
risk_posture_shift
information_seeking_shift
tool_use_shift
organization_role_shift
```

## Rules (defaults, versioned)

| Parameter | Default |
|-----------|---------|
| pre_window_cycles | 20 |
| post_window_cycles | 20 |
| min_magnitude_millipoints | 250 |
| min_persistence_cycles | 10 |
| context | COMPARABLE or CONDITIONALLY_COMPARABLE with declared confounds |

## Forms

* temporary response — fails persistence  
* regime shift — passes magnitude + persistence  
* progressive drift — multi-window monotonic change  
* oscillation — variance high, no sustained mean shift  

Distinguish temporary crisis response from regime shift.

## Extension Points

These are non-normative extension directions for the detector and its projections. A new shift family should declare its feature inputs, pre/post windows, magnitude and persistence rule, and confound handling in a versioned definition. Preserve the difference between temporary crisis response and persistent shift; no detector result becomes world truth or a gameplay reward. Validate short-lived spikes, threshold boundaries, missing windows, and identical-data replay before promoting a definition. Public views remain permissioned projections; the UI notes below do not grant access to private traces.

- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize shift types (strategy_adoption, strategy_abandonment, resource_policy_shift, communication_shift, cooperation_shift, risk_posture_shift, information_seeking_shift, tool_use_shift, organization_role_shift), parameters (pre_window_cycles, post_window_cycles, min_magnitude_millipoints, min_persistence_cycles, context), forms (temporary response, regime shift, progressive drift, oscillation), "persistent or meaningful change", "Distinguish temporary crisis response from regime shift." in /study /watch surfaces. Ties to prior behavior i18n (interesting, learned, etc.).
- **Research and public projections**: Run detector comparisons in the authorized research plane. Controllers receive only their Agent Player observations; they do not gain the detector registry or other Players’ traces. Human WATCH is a supported platform surface with public redaction, not an alternative Player mode.
- **Permissioned research comparison**: Compare detector versions only within authorized evidence scope. Access-policy slices do not grant Controllers detector configuration or private research traces. Public shift summaries must be derived from permitted observations, not hidden detector state.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic cards for shifts (role="region"), ARIA for types/parameters, live regions for new shifts, keyboard filters, contrast. CDP on /study.
- **noema skill / plugin atoms**: Atoms for behavior shift registry, candidate viewer, persistence analyzer for plugins + gateway /study /LEARN + Chamber matrix/contest.
- **LCA2 / MUD handoff / cross-refs**: To BEHAVIOR-FEATURES, ANOMALY-DETECTION, CONTEST-RESOLUTION, STRATEGIC-CONFLICT, DATA-MODEL, R3 evidence bundle, MUD craft for shift mechanics, Observatory. R3 Chamber fixtures provide representative local preparation only; Gate B acceptance additionally requires independent external Controller runs and redacted receipts.
- **Elevation (UX/DX/AX)**: UX discoverable shifts in Chamber; DX modular + i18n + graft + atoms; AX semantic/ARIA + CDP. Per AGENTS.md.

(Expanded per "merge and continue".)
### Presentation integration notes
- i18n centralization (STRINGS + t()) for shift types (strategy_adoption, resource_policy_shift, etc.), parameters, forms in study/watch UI — ties to R3 Chamber behavior shifts, LCA2 handoff R3, oracle/regression.
- AX for shift UI (roles for shift cards, live regions for detections, keyboard, contrast).
- CDP/browser_exec for shift evidence in /study.
- Cross-refs: ui.py study_html, handoff map R3, AX audit, noema skill, 8765.
- Elevation upheld.
- Future: Live shift alerts in Chamber, plugin for dynamic detection.
