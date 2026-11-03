# The heavy group's shortfall: finite nuclear charge and magnetization computed (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `ARC_EXPLORATION.md` ("remaining shortfall in the heavy group"). Scripts: `nuclear_size_hfs.py`, `nuclear_size_hfs_scan.py` (raw `.out` beside each). Nothing fitted. The measured splittings and moments are those of `HYDROGENLIKE_AND_STEP_RESULTS.md` (secondary); QED corrections (self-energy, vacuum polarization) are **not computed** here.

## Method
Dirac radial equations for the 1s electron (κ = −1, G = rg, F = rf; units ħ = c = m_e = 1), solved by shooting in ln r (RK4). Point nucleus V = −Zα/r; uniform charged sphere of radius R = √(5/3) R_ch (matching the rms charge radius). The point-dipole hyperfine radial integral is I = ∫ G F / r² dr (normalised ∫(G² + F²) dr = 1); with a magnetization distribution the integrand carries M(r), the fraction of the magnetization inside r (uniform sphere (r/R)³ inside; thin shell 0 inside; both at the same R, as bounds). δ_BR = I(finite charge, point dipole)/I(point nucleus) − 1; δ_BW = I_M/I(point dipole, same wavefunction) − 1.

**Validation (the numbers that make the rest usable).** On the point nucleus the solver gives E = √(1 − (Zα)²) to 5e-14 and I/(−(Zα)³) = the Breit factor 1/(γ(2γ−1)) to 3e-6 for Z = 1, 20, 50, 67, 83 (for example Z = 83: 2.12496434 against 2.12497074). The factor A used throughout the earlier notes is the converged value of this integral, not an assumption.

## Results (`nuclear_size_hfs.out`)
| ion | R (fm) | δ_BR | δ_BW uniform | δ_BW shell | BR + BW (uniform … shell) | measured r/A − 1 | left over (uniform … shell) |
|---|---|---|---|---|---|---|---|
| ³He⁺ | 2.54 | −0.00014 | −0.00005 | −0.00009 | −0.00020 … −0.00023 | −0.00043 | −0.00023 … −0.00020 |
| ¹⁶⁵Ho⁶⁶⁺ | 6.72 | −0.04610 | −0.01109 | −0.01761 | −0.0572 … −0.0637 | −0.0666 | −0.0094 … −0.0028 |
| ¹⁸⁷Re⁷⁴⁺ | 6.93 | −0.07123 | −0.01520 | −0.02411 | −0.0864 … −0.0953 | −0.0944 | −0.0080 … +0.0009 |
| ²⁰⁷Pb⁸¹⁺ | 7.09 | −0.10522 | −0.01989 | −0.03147 | −0.1251 … −0.1367 | −0.1446 | −0.0195 … −0.0079 |
| ²⁰⁹Bi⁸²⁺ | 7.13 | −0.11148 | −0.02068 | −0.03264 | −0.1322 … −0.1441 | −0.1264 | +0.0058 … +0.0177 |

(H: δ_BR = −0.00003, δ_BW −0.00001 to −0.00002.) In absolute energies (E_point-Dirac × (1 + BR + BW)) against the measurement, uniform/shell: Ho 2.186/2.171 eV against 2.1646 (+1.0%/+0.3%); Re 2.772/2.745 against 2.7479 (+0.9%/−0.1%); Pb 1.2436/1.2272 against 1.2159 (+2.3%/+0.9%); Bi 5.0505/4.9809 against 5.0840 (−0.7%/−2.0%).

- The finite charge carries most of the shortfall (−4.6% for Ho to −11.1% for Bi); the magnetization distribution adds −1.1% to −3.3% between the two bounds. Together they account for the measured shortfall to within 1% for Ho and Re (0.1% to 0.9%), within 0.8% to 2.0% for Pb, and overshoot Bi by 0.6% to 1.8%.
- The residuals (+1.8% to −2.0%, depending on the magnetization model) are of the size of what is not computed: QED (of order a few tenths of a percent, by recollection, not computed), the true single-particle magnetization distribution (spin and orbital parts of the valence nucleon) between the two bounds, and the moments (Bi table value 4.092 against the uncorrected NMR 4.1106, +0.45%; Pb 0.5906 against 0.59258, +0.34%). The Bi theory values in the search results (5.10 eV, with a single-particle model and QED) are 0.3% above its measurement; this computation without QED is 0.7% below.
- Pb and Bi are neighbours with different valence nucleons (a neutron hole in p½ and a proton in h9/2): their residuals have opposite sign (−2.0%…−0.8% against +0.6%…+1.8%), as a spread of magnetization models would give.

## Scaling and model dependence (`nuclear_size_hfs_scan.out`)
- **Fermi against uniform.** A Fermi charge distribution (a = 0.5234 fm) of the same rms radius changes δ_BR by only +0.0003 (Ho), +0.0004 (Re), +0.0005 (Pb), +0.0006 (Bi): for Bi −0.11093 against −0.11148. The shape of the charge distribution is not what is left.
- **Dependence on the nuclear size.** At Z = 83, with the charge radius scaled by 0.25, 0.5, 1, 2, 4, δ_BR = −0.0486, −0.0736, −0.1115, −0.1689, −0.2547; the local exponent d ln|δ_BR|/d ln R_N is 0.598, 0.600, 0.600, 0.592, against 2γ − 1 = 0.5914 for the point-nucleus Dirac wavefunction (the density near the origin goes as r^(2γ−2), so the integral over the nucleus goes as R^(2γ−1)). In the non-relativistic limit γ → 1 the exponent is 1.
- **Dependence on Z at fixed radius (5.5211 fm):** δ_BR = −0.0047 (Z = 20), −0.0132 (40), −0.0342 (60), −0.0726 (75), −0.1115 (83); local exponent in Z 1.51, 2.34, 3.38, 4.23.

## What this says
- The heavy group's shortfall is the nuclear order reaching into the atomic one: a finite charge (4.6% to 11.1%) and a spread-out magnetization (1% to 3%). With them computed, the measured splittings agree with the model to 1% or 2%, the remainder being of the size of QED and of the magnetization-model uncertainty. So the earlier "7% to 15%" is accounted for.
- **The nuclear rung's influence is a power law in its size with an exponent set by the Lorentz angle:** δ_BR ∝ (R_N/ƛ_e)^(2cos θ − 1) (0.59 at θ = 37°, tending to 1 as θ → 0), while the electron rung's influence on the exponent is 3 sin²θ at leading order. Both are governed by the same θ = arcsin(Zα), but the nuclear one has an exponent that itself runs with θ: a ladder whose rate depends on where you stand on it.
- That makes the two orders' effects of different kinds: the electron rung's reach is an inverse square (fixed exponent 2 in the size ratio, a series in sin²θ), the nuclear rung's is a power with a running exponent 2cos θ − 1 and a prefactor that grows steeply with Z (exponent 1.5 to 4.2).

## Not done
QED (self-energy and vacuum polarization) for these ions; the single-particle magnetization distribution (the valence nucleon's spin and orbital densities) in place of the two bounds; the diamagnetically corrected moments; a Fermi or deformed distribution for Ho and Re (strongly deformed, Q = 3.6 and 2.0 barn); a connection between the running exponent 2cos θ − 1 and the instrument's chain.

sha256: *nuclear_size_hfs.py 1460d21f83186548f5c56a8b49e673809d7716299b83d4bc151ce9794b060702; *nuclear_size_hfs.out ff177de7d178d82cba54905ef5eef36fd1c14a7fbcf9b8d678abcf70ed781016; *nuclear_size_hfs_scan.py 4f8169f527d3dba97f226a76b75b3a73bee6744326ee5529e78b9182da1bdfe6; *nuclear_size_hfs_scan.out 6715335b28d874bc0745e2bd101cf3470d18f1ab1292607b234e14a6f479c903.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` (a few minutes each; pure-Python shooting).
