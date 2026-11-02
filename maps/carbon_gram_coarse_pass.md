# First coarse pass: the 36 aspects of one gram of carbon against what the instrument reads out now (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. A pass over every aspect at coarse resolution, before any is refined (`maps/critical_path.md`, `maps/percentage_frame.md`). Inventory: `maps/carbon_gram_aspects.md` (8 groups A to H, 36 rows). Instrument: the E-series one- and two-copy system and its readouts (`explore/E_SERIES_*_RESULTS.md`). Nothing was calibrated and no value was forced; where nothing is read out, the row says so.

## Status vocabulary (extends `percentage_frame.md` with one level, because the instrument models a generic carrier, not carbon)
- **no readout**: the instrument has no quantity corresponding to the aspect.
- **readout, same kind**: the instrument reads out a quantity of the same kind (charge, current moment), but no carbon system is modelled, so the row's own number cannot be compared.
- **compared**: a reading exists and measure (a) was reported for a measured number in this inventory.

## The pass
| # | aspect | status | what the instrument or nature gives |
|---|---|---|---|
| A1 | rest mass, 12 u, N atoms | no readout | the instrument has a kinetic weight m and rates; the three mass readings are not reconciled |
| A2 | where the mass sits | no readout | |
| A3 | gravitational coupling (m/m_P)² | no readout | no gravity in the instrument |
| A4 | weight and field of the gram | no readout | |
| A5 | inertial = gravitational mass | no readout | |
| B1 | nuclear binding | no readout | |
| B2 | nuclear size | no readout | sizes enter only as the tick ratio ρ (an input) |
| B3 | nucleon size | no readout | its ratio to the proton Compton length, 3.9976, is used as an input ρ in the exchange sweep |
| B4 | ground-state spin and parity 0+ | readout, same kind | nature (measured, `carbon_nuclear_moments.out`): ¹²C expressed Σ\|μ\| 28.2353 μ_N, manifest none; instrument: states with nonzero expressed current and zero manifest moment |
| B5 | excited levels of ¹²C | no readout | |
| B6 | strong coupling | no readout | |
| C1 | ¹⁴C beta decay | no readout | no weak sector |
| C2 | neutrinos through the gram | no readout | |
| C3 | neutrino interaction rate | no readout | |
| C4 | neutrino mass scale | no readout | |
| C5 | weak column | no readout | |
| D1 | charge content, net zero | readout, same kind | the instrument reads per-history charge (expressed) and net charge (manifest); on a closed carrier the net charge must vanish for Gauss to hold; no count of 6N charges is modelled |
| D2 | six electrons, ionization energies | no readout | |
| D3 | bonds and molecules | no readout | |
| D4 | the lattice | no readout | |
| D5 | band structure | no readout | |
| D6 | optical response | no readout | |
| E1 | nuclear spin zero, no nuclear moment | readout, same kind | same pairing pattern as B4 |
| E2 | ground term ³P₀, no net atomic moment | readout, same kind | same pattern; no atom is modelled |
| E3 | electron magnetic moment | **compared** | moment-per-charge ratio between orders, proton over electron: model 5.44617e-4 against measured \|μ_p/μ_e\| 1.51927e-3, r = 0.35847; residual factor 2.7928 = μ_p in nuclear magnetons; geometry scaling declared, not swept; r does not cover 1 |
| E4 | collective magnetic response (susceptibility) | no readout | no external-field response is computed |
| F1 | exclusion and shell filling | no readout | |
| F2 | nuclear pairing in ¹²C | readout, same kind | same pattern as B4 |
| G1 | entropy | no readout | no temperature; the instrument is conservative |
| G2 | heat capacity, Debye | no readout | |
| G3 | phonons | no readout | |
| G4 | thermal conduction, thermal limits | no readout | |
| G5 | information counts | no readout | |
| H1 | isotopic make-up | no readout | |
| H2 | cosmic muons | no readout | |
| H3 | origin of the carbon | no readout | not modelled (the gram is taken as observed) |

## The shares (both granularities, as `percentage_frame.md` requires)
| measure | rows (of 36) | groups (of 8) |
|---|---|---|
| a readout of the same kind exists (or better) | 6 (B4, D1, E1, E2, E3, F2) = 16.7% | 4 (B, D, E, F) = 50% |
| compared | 1 (E3) = 2.8% | 1 (E) = 12.5% |
| compared, spreads cover r = 1 | 0 | 0 |

The six rows are not six independent readouts: they depend on two instrument quantities, charge and the current's magnetic moment (with the flux). Read the shares together with the ablation record (`E_SERIES_READOUTS_ABLATION_RESULTS.md` §5), not alone.

## What the pass shows
- The instrument touches the electromagnetic rows through two readouts, and the expressed-versus-manifest split lets it show the nuclear and atomic pattern of present-but-cancelled moments that nature shows (¹²C).
- The one number it meets, the proton-to-electron moment ratio, comes out as the magneton scaling given the declared size-with-tick anchor; it is a consistency of the declared anchors, not an independent test (the mass ratio sets ρ).
- Everything else in the gram (mass, the nuclear and weak sectors, atomic and chemical structure, the lattice, thermal and optical behaviour) has no readout yet. They are not refused; they are the sectors the instrument has not been given.
- Because the aspects are mutually necessary, the near-empty rows are the measure of how far the instrument is from the whole gram, and the pass should be repeated as readouts are added, at the same coarse resolution.
