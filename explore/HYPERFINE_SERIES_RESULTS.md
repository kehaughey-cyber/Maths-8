# The hyperfine inference examined: hydrogen, deuterium, ³He⁺ (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `E_SERIES_RESPONSE_RESULTS.md` §4. Script `explore/hyperfine_series.py`, raw output `explore/hyperfine_series.out`. Nothing fitted. Sourced: `explore/data/moment_benchmark_sourced_values.txt` (CODATA 2022 values; the three hyperfine frequencies are secondary, from search summaries of the original papers, which I did not open; the saved IAEA table for moments, spins and atomic masses). Recalled and unsourced: m_e/u = 5.485799e-4, which enters only a 1e-3-level reduced-mass factor.

## A correction to my earlier wording
I wrote that "the instrument has no α". The point made in reply is right: among the sizes of the carbon-gram rungs, the only pair with a ratio between 128 and 137.5 is the electron Compton length and the Bohr radius, a₀/ƛ_e = 137.036 = 1/α by definition (I checked: 19 distinct sizes from 24 rungs in `maps/carbon_complete_stack.md` §1, one pair in range, 137.03 from the table's rounded sizes). So α is not absent; it is the tick ratio between the electron order and the atomic order, and it carries no information beyond that definition. What the instrument lacked was α as a coupling.

## The hyperfine ratio in rung sizes
With R_mag,X = 2|μ_X|/(e c) (the radius at which a charge circling at c has the nuclear moment) and ƛ_e = ħ/(m_e c), a₀ = ƛ_e/α:

hfs / Ry = (8/3) [(2I+1)/(2I)] Z³ (R_mag,X / a₀)(ƛ_e / a₀) (1 + m_e/M)⁻³

This is the textbook Fermi contact result rewritten (it equals (8/3)[(2I+1)/(2I)](μ_X/μ_B) Z³ α² Ry): two ring sizes over the atom's size. Hydrogen: R_mag/a₀ = 1.110e-5 and ƛ_e/a₀ = α = 7.297e-3.

## Results (`hyperfine_series.out`)
| system | Z | I | μ (μ_N) | measured hfs / Ry | form / measured | with \|μ_e\| for μ_B |
|---|---|---|---|---|---|---|
| H | 1 | 1/2 | 2.7928474 | 4.317550e-7 | 0.998898 | 1.000056 |
| D | 1 | 1 | 0.8574382 | 9.951370e-8 | 0.998727 | 0.999885 |
| ³He⁺ (1969) | 2 | 1/2 | 2.1276253 | 2.634063e-6 | 0.998947 | 1.000106 |

- The form has no free parameter. It sits 0.11% to 0.13% below the measured values; almost all of that is the electron's own moment (|μ_e| = 1.00115965 μ_B, CODATA), which the first column leaves out. With it, the three systems agree to +5.6e-5, −1.15e-4 and +1.06e-4. The remaining 1e-4 is the size of the Breit, QED and nuclear-structure corrections the form does not include.
- Ratios to hydrogen: D/H measured 0.230487 against 0.230447 (1.7e-4); ³He⁺/H measured 6.100827 against 6.101130 (5e-5).
- The 1969 and 2022 ³He⁺ values differ by 1.23 Hz (1.4e-10), so the choice does not matter here.

## Does the coupling inferred from hydrogen reproduce them?
No. The instrument route calibrated on hydrogen (a coupling μ_r of 1.2531e-4 at ρ_B = 1 or 1.2098e-6 at ρ_B = 1/1836.15, weak-coupling splitting linear in the nuclear ring's moment) predicts X/H = μ_X/μ_p only:

| system | measured X/H | instrument route | ratio | the missing factor |
|---|---|---|---|---|
| D | 0.230487 | 0.307012 | 1.332 | 0.7507: the multiplicity (2I+1)/(2I) (3/2 against 2, ratio 0.75) |
| ³He⁺ | 6.100827 | 0.761812 | 0.1249 | 8.008: Z³ = 8 |

So the inferred μ_r is not a coupling constant of the instrument. Fitting hydrogen alone absorbed the whole of (8/3)(2I+1)/(2I) (R_mag/a₀)(ƛ_e/a₀) into one number, and the number then fails when the nucleus changes.

## What this says the instrument has and lacks
- **Has:** the ring moments, as e c R / 2 with R the ring's radius: the electron's (ƛ_e) and the nucleus's (R_mag,X), both tied to the ladder, and an interaction energy that is linear in each ring's moment at weak coupling.
- **Lacks:** the spin multiplicity ((2I+1)/(2I) comes from coupling the electron spin to the nuclear spin into F = I ± ½) and the electron's density at the nucleus (Z³ comes from the electron's order being a₀/Z, so the nuclear ring sits at one-over-Z of the Bohr distance). The carbon stack already contains such a rung: C⁵⁺ 1s, a₀/6.
- **Consequence:** the hyperfine measurements are a test of how orders are placed relative to each other (the electron's order at a₀/Z, the nucleus's at R_mag), not of a tunable plaquette strength. The next step this suggests is to give the second copy a size, so that the coupling between the rings is set by the ratio of their sizes (as in the rung form) instead of by μ_r; and to give the ring a spin multiplet.

## Not done
No test of the rung form on a heavier hydrogen-like system (¹³C⁵⁺ is the natural case from the carbon stack; I did not source a measured value). No attempt to derive the 8/3 or the multiplicity inside the instrument. The earlier inference of μ_r is superseded, not deleted (`E_SERIES_RESPONSE_RESULTS.md` §4 stands as a record, with this note as its examination).

## Failed run, kept
`hyperfine_series_run1_bohr_magneton_only.out` (script `hyperfine_series_run1.py`): first run, with μ_B for the electron's moment; the offsets of 0.11% to 0.13% were mostly the electron anomaly. Not an error in the physics; the correction was added in the second run.

sha256: *hyperfine_series.py fd387caf92182f29c7aa62e1c0afd61b81cda8990879197ce49c0d7882eeb845; *hyperfine_series.out a73859159e235b372418ed5cb43c8f33e53eb1551579fc9e91f96c377e8a357f; *hyperfine_series_run1.py 5ed07a11005c2f5a3325c813737db6ab9b904cc23d98f4f43cf1f44fc94bfa3d; *hyperfine_series_run1_bohr_magneton_only.out 5d317809428b9e5017a9c170124249b44631a49b36088ef04ab488e92ec6fd4d; *data/moment_benchmark_sourced_values.txt (see its current hash).
Command: `py -3 -I -X utf8 -u explore/hyperfine_series.py > explore/hyperfine_series.out`.
