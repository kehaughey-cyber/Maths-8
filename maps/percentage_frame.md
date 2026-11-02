# The percentage frame, defined before any run (2026-11-02)

Authored by Claude (Sonnet 5.5) from the human's description; definitions only, nothing run. The frame has two measures, both required (the human: it is both). They are set down here before the instrument is built so the definitions cannot be shaped by results.

## Measure (a): per-reading percentage
For a reading X that the instrument produces and a measured value M with its own uncertainty and scheme:
- report the raw ratio `r = X / M` and `100 r` percent, unrounded;
- report the uncertainty on r from three separate sources, kept apart: the measurement's own uncertainty (σ_M), the instrument's numerical uncertainty, and the spread over the declared choices (φ step, radial-hop cost, number of copies, calibration handle);
- state the measurement's scheme and definition (for example MS-bar at 2 GeV versus pole mass), because a ratio across inconsistent definitions is not a result.
Agreement is not defined as a threshold. The frame reports r with its three spreads and lets the reader see whether the spreads cover 1.

Calibration: a dimensionful reading needs one handle (c, ħ, G, or a mass). Say which handle was used, and report r for every other reading separately; a reading used to set the calibration has r = 1 by construction and is excluded from the share.

## Measure (b): whole-object share
Over the inventory in `maps/carbon_gram_aspects.md`, each aspect gets one status, assigned by what was done, not by whether it agreed:
- **no readout**: the instrument has no quantity corresponding to the aspect;
- **readout, not yet compared**: a reading exists and has been produced;
- **compared**: a reading exists and measure (a) has been reported for it.
Three shares follow: the fraction of aspects with a readout, the fraction compared, and the fraction compared whose spreads cover r = 1.

Two cautions built in:
1. **The count depends on how rows are cut.** The inventory has 8 groups (A to H) and 36 rows, and splitting or merging rows changes the fractions. Report every share at both granularities (groups and rows) and say so; neither is privileged.
2. **Mutual necessity.** The aspects are not independent (remove one law and the gram does not exist), so a share is not a score and should be read together with the ablation record (below), never alone.

## Ablation record (companion to the shares)
For each layer of the instrument that can be switched off (for example the link phases), record which aspects' readouts change, vanish, or do not move. This is reported as a table, with no prediction stated beforehand.

## Expressed and manifest
Each readout is recorded twice where the distinction applies: *expressed* (the structure is present: phases, currents, moments) and *manifest* (a net effect appears: a field, a response, a force). Magnetism in the gram is the standing example: ingredients present, effect weak.

## Measurement is not neutral
Every value on either side is the result of an act of examining (the human's double-slit point). Each reading carries the protocol that produced it, and a reading is compared only with a measurement taken under a protocol whose meaning is stated.
