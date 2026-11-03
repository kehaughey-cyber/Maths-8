# Exploring what was noticed: the plateau, the adjacency reading, and which quantities march with mass (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `TWO_GROUPS.md`. The human's remark: the heavy group's behaviour "tracks with density and gravity", so more massive atoms should follow the same arc. Script `explore/arc_exploration.py`, raw output `explore/arc_exploration.out` (278 nuclides: stable or half-life above 1e9 years, with a charge radius and a binding energy, 81 elements Z = 3 to 92). Nothing fitted. Coincidences are flagged, not claimed.

## 1. The plateau is a stay in one window, not a law
Ratio of nuclear cycles (R_N B/ħc) to atomic cycles (tan(θ/2), sin θ = Zα), mean over the nuclides of each element; times α in the last column (1/α = 137.036):

| Z | ratio | ratio × α |
|---|---|---|
| 20 | 91.3 | 0.666 |
| 40 | 117.6 | 0.858 |
| 50 | 124.5 | 0.908 |
| 60 | 131.8 | 0.962 |
| 64 | 134.5 | 0.982 |
| 67 | 135.7 | 0.990 |
| 70 | 136.1 | 0.993 |
| 75 | 135.5 | 0.989 |
| 79 | 135.4 | 0.988 |
| 82 | 136.0 | 0.993 |
| 83 | 136.1 | 0.993 |
| 90 (Th) | 138.3 | 1.009 |
| 92 (U) | 138.7 | 1.012 |

Local log-slopes between element means, nuclear d ln N/d ln Z against atomic d ln a/d ln Z: 1.385 vs 1.017 (Z 20 to 30), 1.396 vs 1.034 (30 to 40), 1.311 vs 1.059 (40 to 50), 1.405 vs 1.092 (50 to 60), 1.342 vs 1.136 (60 to 70), **1.206 vs 1.206 (70 to 83)**, 1.486 vs 1.300 (83 to 92). The ratio is flat only in the window 70 to 83, where the two slopes happen to be equal; it was rising before (slope 0.2 to 0.4) and rises again after (0.19). It crosses 1/α near Z ≈ 86 and continues to 1.012/α at U. So the near-equality with 1/α at Z = 67 to 83 (0.988 to 0.993) is the stay of a rising curve passing through, and its height is an accident of where the slopes cross. This **corrects the earlier reading** of a plateau "at about 0.99/α" as a feature: ledger entry 9 is amended accordingly. The components of the nuclear slope (charge radius 0.24 to 0.57, binding energy 0.91 to 1.10) show that the stay in 70 to 83 comes from the radius growing more slowly (0.243) there.

## 2. The adjacency reading, made quantitative
The exponent excess of the hyperfine energy over 3 as a function of the size ratio s = 1/(Zα) to the electron Compton rung: p − 3 = 3/s² to 0.0% at s = 137 and 68.5, +0.7% at 13.7, +2.9% at 6.85, +6.8% at 4.57, +21% at 2.74, +46% at 2.05, +95% at 1.65. The local slope d ln(p − 3)/d ln s is **−2.000** at s = 68.5 and 27.4 (−2.002), −2.03 at 6.85, −2.19 at 3.43, −2.79 at 2.05, −3.8 at 1.65, −11 at 1.2 (the pole at s = 1.155).
- So the influence of the neighbouring rung on the exponent is an **inverse square in the size ratio**: p − 3 ≈ 3(ƛ_e/R)² = 3(v/c)², equivalently p ≈ 3(1 + (v/c)²) for the 1s electron; it steepens into the pole only as s approaches 1.155.
- The running depends on the electron Compton rung alone (it is a function of Zα). The nuclear order's adjacency (R_e/R_N = 115 to 152) shows up separately, as the shortfall from the point-nucleus form (r/A = 0.93 to 0.86).
- The carbon-stack rungs near the ions' atomic orders: the heavy ions' orders lie 1.65 to 2.05 times above the electron Compton rung and 11 to 14 times below the C⁵⁺ 1s rung (a₀/6); for H the atomic order is the a₀ rung itself, for ³He⁺ it is a₀/2 (a factor 2 from that rung and 3 above C⁵⁺ 1s).

## 3. Which quantities march along the arc, and which saturate
One nuclide per element, Z ≥ 20 (`arc_exploration.out` §3; the first run of this table had the nuclear mass 10⁶ too large and so (M/m_P)² 10¹² too large; kept as `arc_exploration_run1_mass_1e6.out`, the other sections are identical):
- **Marching with Z (and θ):** the nuclear order's cycles (35.4 at Z = 67, 45.9 at 83, 53.5 at U; correlation with θ 0.9995), the mass (ln A, 0.978), the gravitational registration (M/m_P)² = GM²/ħc (2.9e-37 at Li, 1.6e-34 at Ho, 2.5e-34 at Bi; 0.978 for its logarithm), and the nuclear cycles per nucleon (0.154 at Z = 20, 0.215 at 67, 0.220 at 83, 0.225 at U; 0.955). These correlations are not informative by themselves: every quantity is monotonic in Z, and θ ≈ Zα.
- **Not marching:** the equivalent-sphere nuclear density (R = √(5/3) R_ch) saturates, 0.112 to 0.139 fm⁻³ (mean 0.128, a 21% spread; it peaks near Pb and falls to 0.131 at U), and correlates with θ at only 0.82.
- So the arc is a **mass-and-size arc, not a density arc**. At constant density a nucleus of A nucleons has radius ∝ A^(1/3) and binding energy ∝ A, so its registration count grows as A^(4/3) and its gravitational registration as A². The nuclear saturation also ties A to Z (A ≈ 2 to 2.5 Z for the heavy stable nuclei), and that is why mass, nuclear information and gravity all go up together with the atom's relativistic angle: the atomic order depends only on Z, and nuclear stability links A to Z.
- Gravity is not doing anything at these scales: (M/m_P)² is below 3e-34 for every atom here, so its agreement with the arc is an agreement of monotonic trends, not a mechanism.

## What this says about the reading
- **Quantified:** the exponent's running is the influence of one neighbouring rung (the electron's Compton rung) and falls as the inverse square of the size ratio, p − 3 ≈ 3(v/c)². The far-order regime (s ≳ 14, p − 3 < 0.016) is where that influence is below 1.6%; the adjacent regime (s ≲ 5) is where it exceeds 10%.
- **Withdrawn:** the idea of a pinned plateau at about 0.99/α in the nuclear-to-atomic cycle ratio.
- **Supported, weakly:** that heavier atoms follow the same arc, because nuclear stability links mass to Z; not that density or gravity drives it (density saturates, gravity is negligible).

## Not done
The finite-size and Bohr–Weisskopf corrections that would test the nuclear order's own adjacency (the shortfall r/A against a computed correction); an actual source of the saturation density (the nuclear liquid-drop terms) beyond the observed constancy; anything for Z > 92 (no stable or long-lived nuclides; the pole is at Z = 118.7 and the critical charge at 137).

sha256: *arc_exploration.py ac9765c52320c2770019c62fd72ee82c182f0a4b432bde2df30e2ba2b3b4b330; *arc_exploration.out fdf9dff38ea6a7ed5959b2f66d1d29de4e66a8f4543614a957a816c61099ac76; *arc_exploration_run1.py e3560edaca9e4a5703117177a32f83bff68964aab0b198f4d5630a19f9a22b0e; *arc_exploration_run1_mass_1e6.out 8db2bb3b315708906475260d9c8a310f540f6340b47a7b4cb434b1897155fcbd.
Command: `py -3 -I -X utf8 -u explore/arc_exploration.py > explore/arc_exploration.out` (a few seconds).
