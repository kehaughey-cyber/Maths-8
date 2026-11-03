# The hydrogen-like series, and what the shape says about the step (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `SIZE_EXPONENT_ORIGIN.md`. Scripts: `hydrogenlike_series.py`, `size_exponent_listening.py` (raw `.out` beside each). Nothing fitted except where a search is stated. All measured hyperfine values are secondary (search summaries of the papers, which I did not open); they are in `explore/data/moment_benchmark_sourced_values.txt`.

## On φ
The step φ was an assertion: the lab README says the φ step per copy is the original visualizer's choice, and the lattice map found no common offset on the φ tower. I built the chain notes on it. Below the step is not assumed; the shape of the exponent against the size ratio is compared first, and the step is read from it.

## 1. What was measured (`hydrogenlike_series.out`)
| ion | Z | size ratio s = 1/(Zα) | E | r = E / E_nr | Dirac point-nucleus A | r / A |
|---|---|---|---|---|---|---|
| H | 1 | 137.04 | 5.874326 μeV | 0.99994 | 1.00008 | 0.99986 |
| D | 1 | 137.04 | 1.353953 μeV | 1.00011 | 1.00008 | 1.00003 |
| ³He⁺ | 2 | 68.52 | 35.838 μeV | 0.99989 | 1.00032 | 0.99957 |
| ¹⁶⁵Ho⁶⁶⁺ | 67 | 2.045 | 2.1646 eV (572.79 nm) | 1.4370 | 1.5395 | 0.933 |
| ¹⁸⁷Re⁷⁴⁺ | 75 | 1.827 | 2.7479 eV (451.2 nm) | 1.6057 | 1.7731 | 0.906 |
| ¹⁸⁵Re⁷⁴⁺ | 75 | 1.827 | 2.7207 eV (455.7 nm) | 1.6063 | 1.7731 | 0.906 |
| ²⁰⁷Pb⁸¹⁺ | 82 | 1.671 | 1.2159 eV (1019.7 nm) | 1.7722 | 2.0718 | 0.855 |
| ²⁰⁹Bi⁸²⁺ | 83 | 1.651 | 5.0840 eV | 1.8564 | 2.1250 | 0.874 |

E_nr is the non-relativistic contact form that reproduced H, D and ³He⁺ (with the electron's actual moment). s is the ratio of the electron-order size a₀/Z to the electron's Compton length. At Z = 1, 2, r = 1 to 1.1e-4. At Z ≥ 67 the measured splitting is 1.44 to 1.86 times E_nr; the point-nucleus Dirac factor A = 1/(γ(2γ−1)), γ = √(1−(Zα)²), accounts for most of it, and the 7% to 15% shortfall (r/A) has the sign and order expected from finite nuclear size and Bohr–Weisskopf effects, which are not computed here. The Re isotope assignment is inferred (energy ∝ moment, so ¹⁸⁷Re is the shorter wavelength) and is flagged. No measured value was found for Li²⁺ or other light hydrogen-like ions (only theory), so the range Z = 3 to 66 has no measurement.

Measured exponent between pairs (moments and multiplicity divided out): Z 1 → 2: 3.0015 (Dirac 3.0019); 2 → 67: 3.1034 (Dirac point-nucleus 3.1229); 67 → 82: 4.0379 (Dirac 4.4701); 67 → 83: 4.1958 (Dirac 4.5052). The 82 → 83 pair (6.83) is not a Z-dependence: neighbouring ions with different nuclear spin and structure.

So the exponent of the absolute energy in the electron-order size is 3 at large size ratio (s = 137, 68.5) and rises toward 4 to 5 as the atom's order approaches the electron's Compton order (s → 2 → 1.65); the Dirac factor gives the profile p_D(s) = 3 + (1/s²)/γ (1/γ + 2/(2γ−1)): 3.000 at s = 137, 3.016 at 14, 3.15 at 4.6, 4.05 at 2.0, 5.1 at 1.65.

## 2. What the chain gives (`size_exponent_listening.out`)
The chain's exponent against s, exact for a semi-infinite chain mode by mode (the six levels of the lattice face-energy operator on which the ring source has weight: 0.5279, 1.9332, 3.5563, … with weights 0.833, 1.853, 3.578, …; the ring couples only to odd k), with the +1 for a fixed-moment source. Two free parameters: the step q and μ_r/μ.
- **With the far field held at 3** (one condition, μ_r fixed by q), the rms difference from the Dirac profile over s = 2.5 to 140 is 0.018 (q = 1.05), 0.022 (1.1), 0.028 (1.2), 0.030 (√φ), 0.033 (φ), 0.035 (e^(1/φ)), 0.036 (2), 0.044 (2.5), 0.052 (3), 0.065 (4). The shape is nearly independent of the step; it prefers finer steps slightly. At q = φ (μ_r/μ = λ₁) the difference is within 0.015 for s from 4.6 to 137 (for example s = 10: Dirac 3.0304, chain 3.0425; s = 3.3: 3.3138 against 3.2778), and −0.49 at s = 2, where the chain is finite at coincidence and the Dirac factor diverges.
- **Free two-parameter search** (80 × 100 grid): best rms 0.0233 at q = 1.0571, μ_r/μ = 43.3, far-field p_E = 2.988. The curve of best rms against q is not sharp (0.033 to 0.056 over q = 1.2 to 4) and has no preference for φ.
- **Pairs.** Chain exponents for the measured pairs (q = φ, μ_r/μ = λ₁; q = 1.0571, 43.29; q = 1.3009, 1.831):

| Z pair | measured | Dirac point | chain φ | chain q = 1.057 | chain q = 1.301 |
|---|---|---|---|---|---|
| 1 → 2 | 3.0015 | 3.0003 | 3.0012 | 2.9882 | 3.0181 |
| 2 → 67 | 3.1034 | 3.1228 | 3.1045 | 3.0978 | 3.1171 |
| 67 → 82 | 4.0379 | 4.4701 | 3.7200 | 3.9157 | 3.8174 |
| 67 → 83 | 4.1958 | 4.5052 | 3.7271 | 3.9271 | 3.8266 |

For Z ≥ 67 the measured exponent lies between the chain's (3.7 to 3.9) and the point-nucleus Dirac value (4.5); the measured values contain finite-size and Bohr–Weisskopf effects that neither contains, so that bracketing is not a test of either.

## What this says
- **The step:** the shape does not select φ. The profile agreement holds for any step from 1.05 to 2 within about 0.02 to 0.035 rms, and the free search prefers a fine step (q ≈ 1.06), consistent with a continuous scale axis (as the far-field exponent 2.99993 and the absence of a common offset on the tower already suggested). φ costs 2.3% in the far-field exponent and little in the shape.
- **The profile is a property of nature that the instrument has to match.** The exponent at fixed moments is 3 for s ≫ 1 and rises as the electron-order size approaches the electron Compton length; the chain, built from the lattice's own mode spectrum with its far field set to 3, follows that rise from s ≈ 4 to 140 to within about 0.015 and falls short of it below s ≈ 3.
- **What stays argued:** the +1 from a fixed-moment source (needs tick ∝ size); that the coincidence of layers (c = 0) corresponds to s = 1; the chain being a field-propagation model while the nuclear contact term itself is not built. The agreement at s = 4.6 to 14 (0.007 to 0.014) is within the range where the chain's tail decays more slowly than the Dirac excess (3/s²): at s = 137 the chain's excess over 3 (0.0007) is about three times the Dirac one (0.0002).

## Not done
Finite nuclear size and Bohr–Weisskopf corrections for Ho, Re, Pb, Bi (so no test of the chain below s ≈ 3); any measured hydrogen-like value for 3 ≤ Z ≤ 66 (none found); the primary hyperfine papers; a derivation of the +1 and of the identification c = 0 ↔ s = 1 inside the instrument.

sha256: *hydrogenlike_series.py c3915dded268c9a1157fa31e017095dc9d2a2de0b32e66d500e79075cde94c7f; *hydrogenlike_series.out 82f38d2e80373f7978edde5049a1ef781382cbd3330b191f1eea2251dccf5827; *size_exponent_listening.py cc6cfd7089049642c0b3ebc3102412d1127de67fd3b01ab98ae719804f7ccf95; *size_exponent_listening.out 1df1aed189f63621772a1764c2a8f70f35593980a48b3173c88e068457f7e374; *data/moment_benchmark_sourced_values.txt 5eb91044e3941fbae169ecdf0f7e412aabb0774802300f9d73211ff6a588922f.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` (a few seconds each).
