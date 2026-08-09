# Observatory

## Purpose

The Observatory converts world signals into provenance-bearing observations through explicit instrument models. It is the only standard bridge from canonical truth to player-visible measurement.

## Observation record

An observation MUST include stable ID, world and session references, subject, phenomenon, instrument and calibration versions, operator, location, simulation interval, acquisition settings, values and units, uncertainty, detection status, environmental conditions, artifact digest, raw-record reference, transformations, quality flags, and integrity digest.

## Acquisition pipeline

`signal → sampling → instrument response → calibration → noise → detection/censoring → transformation → quality assessment → immutable record`

Each stage is versioned. Raw samples SHOULD be retained when practical. Derived records cite all parent observations and the exact transformation.

## Instruments

An instrument defines observable channels, operating range, resolution, response curve, sampling behavior, interference, calibration procedure, resource cost, hazards, and accessibility presentation. Instruments may be biased or imperfect, but those properties are stable and discoverable.

## Calibration and quality

Calibration has reference, procedure, time, environmental scope, result, and expiry. Records outside valid calibration remain available with flags. Quality states include valid, suspect, invalid, saturated, below-detection, censored, contaminated, and incomplete. Invalid data cannot satisfy evidence requirements unless the requirement explicitly studies invalidity.

## Presentation

The interface distinguishes raw and derived values, value and uncertainty, no signal and no sample, and measurement and annotation. Unit conversion never changes stored canonical values. Alternate visual, auditory, textual, and haptic presentations preserve semantics.

## Integrity and access

Observations are append-only. Corrections and recalibrations create derived or superseding records. Exports preserve provenance and redact hidden or private fields by policy. Collaborative imports remain untrusted until integrity, version, and permission checks pass.

## Failure behavior

Interrupted acquisition produces an incomplete record when any usable sample exists. Storage failure does not fabricate a value. Unsupported instruments or channels fail before world intervention. Retry semantics prevent duplicate observations.

## Acceptance criteria

- A player can trace a displayed value to instrument, calibration, conditions, and transformation.
- Saturation and below-detection are not represented as ordinary numeric values.
- Recalibration never rewrites the original record.
- Equivalent unit displays round-trip without semantic loss.
- Observatory output contains no unrestricted world-truth payload.
