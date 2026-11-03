# What looks like a regular ladder and is not: candidate structures behind the over-and-under pattern (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. The human's question: what looks like an exponential or regular step ladder, is not one, and produces results both below and above a measured value, and could be something overlooked in "the braid of the system" acting in a non-obvious functional way. Script `explore/dirac_series_vs_chain_weights.py`, raw output `explore/dirac_series_vs_chain_weights.out`. Nothing fitted. This note lists candidates and what has and has not been tested; it identifies no mechanism.

## The pattern to be explained
- The exponent profile nature shows (`HYDROGENLIKE_AND_STEP_RESULTS.md`): 3.000 at size ratio s = 137, rising to 4 to 5 as s → 1.65; the measured heavy-end value (4.04 for Z 67 → 82, 4.20 for 67 → 83) lies **between** the chain's (3.7 to 3.9) and the point-nucleus Dirac value (4.47 to 4.51).
- The chain is a sum of exponentials (one per transverse mode of S³), so its local exponent is not constant, though it looks like a regular ladder; the Dirac factor is a series in (Zα)².

## Candidate 1: a ladder that is a sum of ladders (modes)
Already in the computation. M(s) = Σ_k a_k s^−(k+1), over the odd modes k = 1, 3, 5, … of S³ (the ring's weight on even k is 1e-29). A sum of power-law ladders with rates 2, 4, 6 has a local exponent that moves from 2 toward the lowest rate as s grows, and from above it near the coincidence. That is the over-and-under behaviour in form. What it lacks as it stands: the right coefficients.

## Candidate 2: the Dirac series, a ladder with a pole (computed)
A(x) = 1/(γ(2γ − 1)), γ = √(1 − x), x = (Zα)² = 1/s²:
A = 1 + 3/2 x + 17/8 x² + 47/16 x³ + 513/128 x⁴ + 1389/256 x⁵ + 7485/1024 x⁶ + 20103/2048 x⁷ + …
p − 3 = d ln A / d ln Z = 3x + 4x² + 21/4 x³ + 55/8 x⁴ + 577/64 x⁵ + …
The ratios c_(j+1)/c_j are 1.5, 1.4167, 1.3824, 1.3644, 1.3538, 1.3472, 1.3429, tending to 4/3: the series is dominated by a geometric ladder of ratio 4/3, the pole of A at 2γ − 1 = 0, x = 3/4, s = 2/√3 = 1.1547, Z = 118.68. But there is a second singularity at γ = 0 (x = 1), a branch point, so it is not a pure exponential ladder. The heavy-end rise (s ≈ 1.65 to 2) is governed by the nearer pole at s = 1.1547. Nuclear size regularises it in nature.

## Candidate 3: do the lattice ring's odd-mode weights follow the Dirac series? (computed; partial)
If M(s) ∝ s⁻² A(1/s²), the odd modes need weights a_(2j+1)/a₁ = c_j (the series coefficients), 1, 3/2, 17/8, …. The lattice ring's weights (W_k/√λ_k, the continuum-limit rate; levels assigned to k by the multiplicities 2k(k+2); only k = 1, 3, 5 are reliable, higher levels are lattice-truncated):

| k | λ_k | ring weight W_k | a_k / a₁ | Dirac c_j needed | ratio |
|---|---|---|---|---|---|
| 1 | 0.52786 | 0.8333 | 1 | 1 | 1 |
| 3 | 1.93319 | 1.8530 | 1.1619 | 1.5 | 0.7746 |
| 5 | 3.63684 | 3.5780 | 1.6357 | 2.125 | 0.7698 |

For k = 3 and 5 the lattice weights are 0.775 and 0.770 times the Dirac coefficients: the two ratios agree to 0.6%, and 0.7746 equals √(3/5) = 0.7745967 to 6e-6. The pattern is the Dirac one up to a factor that the k = 1 normalisation absorbs (equivalently the lowest mode is 1.29 times stronger than the pattern needs). **Noticed, not claimed:** two points, the factor 0.775 is unexplained, the k ≥ 7 levels are lattice-truncated and cannot extend the test, and the numerical coincidence with √(3/5) may be one.

## Candidate 4: a golden ladder with its Galois conjugate (computed, as arithmetic)
Binet: F_n √5 = φⁿ − ψⁿ, L_n = φⁿ + ψⁿ, ψ = −1/φ. The conjugate term alternates in sign, so the ladder lands alternately above and below φⁿ/√5: F_n / (φⁿ/√5) = 1.382, 0.854, 1.056, 0.979, 1.008, 0.997, 1.001 for n = 1 to 7 (deviations +38%, −15%, +5.6%, −2.1%, +0.8%, −0.3%, +0.1%); L_n / φⁿ = 0.618, 1.146, 0.944, 1.021, 0.992, 1.003. This is a ladder that looks exponential and over- and undershoots it, with a decaying alternation of ratio ψ²ⁿ. The exact couplings found earlier (cosh(2 ln φ) = 3/2, cosh(3 ln φ) = √5, λ₁ = 5 − 2√5) are numbers of exactly this kind (Lucas and Fibonacci values). **Noticed, not claimed:** the deviation at n = 4 is +2.1%, in the range of `maps/two_percent_ledger.md`; the index was picked after seeing the table, and no quantity here has been tied to n = 4.

## Candidate 5: the repo's own braid (not tested)
`floor/field_equations_v3.txt` F18 (the braided floor: the two fold-partner Dirac shells counter-wind ±6° per transit, 60 transits = one turn) and F19 (belt trichotomy; the quark hexad {φ/2 ×4, 1/(2φ) ×8, 1 ×3} is "golden-mixed", a crossing inventory of 4 major to 8 minor); its open item (ii): "DESIGNATED HUNT: the braid-length mechanism for the quark hierarchy — the hierarchy COMPOUNDS rather than composes". That is a ladder built from two interleaved golden rates (φ/2 = 0.809 and 1/(2φ) = 0.309), which is the kind of object the question describes. No attempt was made here to build a braided two-rate ladder and compare its local exponent with the profile. That is the natural next test, and it needs the braid-length rule from the floor rather than a guess.

## What would discriminate
- **Where the exponent is measured at several Z between 3 and 66** (none found): a sum of exponentials or a Dirac-type series is smooth; a braided or conjugate-alternating ladder would have a decaying oscillation about the smooth curve, with ln s spacing set by ln φ (or the braid's rates). The data cannot show it yet.
- **Finite nuclear size and Bohr–Weisskopf corrections** for Ho, Re, Pb, Bi: they would show whether the residual r/A (0.933, 0.906, 0.855, 0.874) is smooth in Z or alternates. The two Re isotopes agree (0.9056, 0.9059).
- **Mode weights on the finer lattice:** the ring's weights beyond k = 5 on a refined 600-cell, to see whether a_k/a₁ keeps following c_j (needs a lattice larger than the dense solver can take).

## Not done
A braided two-rate ladder from F19's inventory; the exact S³ weights of a great-circle ring on the coexact harmonics (closed form, by SU(2) representation theory); a refined-lattice weight test; any link from the Binet table's 2.1% to a measured quantity.

sha256: *dirac_series_vs_chain_weights.py 03597af4e57f1afb766670bac1986f4214fa3f3e882865374426d196e4ae766f; *dirac_series_vs_chain_weights.out d2e99b2459a685cc06c45858bbf1809d4fbb13a89f2315564378f4fb678ac68c.
Command: `py -3 -I -X utf8 -u explore/dirac_series_vs_chain_weights.py > explore/dirac_series_vs_chain_weights.out` (about 10 s).
