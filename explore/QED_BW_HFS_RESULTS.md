# Single-particle magnetization and vacuum polarization for the heavy-ion hyperfine splittings (2026-11-03)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `NUCLEAR_SIZE_HFS_RESULTS.md` (finite charge and two magnetization bounds). Scripts and raw outputs: `bw_single_particle.py/.out`, `vp_hfs.py/.out`, `combine_hfs.py/.out`. Nothing fitted. **The bound-state self-energy is not computed** (a one-loop all-order calculation is beyond NumPy and mpmath here); no recalled number is used for it.

## 1. Single-particle Bohr–Weisskopf (`bw_single_particle.out`)
The valence nucleon's orbital current and spin magnetization replace the two bounds. Derivation is in the script header: the 1s electron's transition current is a toroidal L = 1 current with vector potential a(r) sin θ φ̂, a = (4π/3) ã, ã(r) = r⁻² ∫₀ʳ c r'³ dr' + r ∫ᵣ^∞ c dr', c = GF/r²; the energy is −∫ j·A (orbital) and −∫ M·B (spin). Nucleon: Woods–Saxon (r₀ = 1.25 fm, a = 0.65 fm, spin–orbit 0.44 V₀ (ħ/m_π c)², Coulomb for protons), depth set so the orbital is bound by the measured separation energy (AME2020, `explore/data/ame2020_mass_1.mas20.txt`: S_p(¹⁸⁷Re) = 5.9969, S_n(²⁰⁸Pb) = 7.3679 for the p½ neutron hole, S_p(²⁰⁹Bi) = 3.7990 MeV).

**Checks that passed** (printed in the output): the Clebsch–Gordan relative sign agrees with a numerical diagonalization of J² for (l, j) = (2, 5/2), (1, 1/2), (5, 9/2), (4, 7/2); the point limit gives W_orb = W_spin = 1.00000000; an s-wave spin-only uniform sphere through the new code gives δ = −0.020688 / −0.019894 / −0.015206 (Bi / Pb / Re) against the old uniform-sphere integral −0.020683 / −0.019889 / −0.015203 (differences ≤ 5e-6, quadrature).

**Result** (δ_BW, relative to the point dipole in the same electron wave function; WS parameter set 1; the spread over r₀ = 1.20/1.30 fm and ±2 MeV in binding energy is inside the quoted range):
| ion | state | Schmidt, free g_s | g_s × 0.6 | spin part scaled so total μ = measured | old bounds (uniform … shell) |
|---|---|---|---|---|---|
| ¹⁸⁷Re⁷⁴⁺ | π d5/2, μ_orb 2.000 + μ_spin 2.793 | −0.01401 (−0.0131 … −0.0150) | −0.01306 | −0.01246 | −0.0152 … −0.0241 |
| ²⁰⁷Pb⁸¹⁺ | ν p1/2 hole, spin only | −0.03163 (−0.0298 … −0.0337) | same | same | −0.0199 … −0.0315 |
| ²⁰⁹Bi⁸²⁺ | π h9/2, μ_orb +4.909, μ_spin −2.285 | −0.00244 (−0.0022 … −0.0027) | −0.00889 | −0.01140 | −0.0207 … −0.0326 |

For Bi the orbital and spin parts have opposite sign (Schmidt μ = 2.62 against the measured 4.09), so the correction is small and depends strongly on how the spin g-factor is treated (−0.2% to −1.1%); for Pb (spin only) it equals the thin-shell bound. ¹⁶⁵Ho is **not modelled**: its 7/2⁻ ground state is a deformed Nilsson state with no spherical |l, j = 7/2⟩ partner of the right parity in the proton shell below Z = 82; ¹⁸⁷Re is also deformed, so its entry is a spherical estimate. A first complete run, without the scaled-to-measured-μ variant, is kept as `bw_single_particle_run1.py` and `bw_single_particle_run1_no_muexp.out`.

## 2. Vacuum polarization (`vp_hfs.out`)
Two pieces. (wf) The Uehling potential of the (uniform-sphere) nuclear charge added to the Dirac equation, δ_wf = I(V + V_U)/I(V) − 1, computed non-perturbatively with the same solver. (ml) The magnetic loop: the nuclear vector potential carries the same photon-propagator correction, 1/r² → (1/r²)[1 + (2α/3π) ∫ w(t) e^(−2tr)(1 + 2tr) dt], first order, point dipole (nuclear size inside this small term neglected).

**Check at low Z (point nucleus):** total/(α(Zα)) = 0.7558, 0.7602, 0.7682, 0.7839, 0.8198 for Z = 1, 2, 4, 8, 16 (wf 0.3826 → 0.4581, ml 0.3733 → 0.3618; the analytic leading magnetic-loop coefficient from the formula is 3/8 = 0.375). The expected leading coefficient 3/4 for the vacuum-polarization part is recalled, not sourced here; the numbers tend to it as Z → 0 with an O(Zα) rise.
**Heavy ions** (finite sphere): δ_wf, δ_ml, total = Ho 3.015e-03, 1.340e-03, **+4.354e-03**; Re 3.880e-03, 1.554e-03, **+5.434e-03**; Pb 4.838e-03, 1.759e-03, **+6.597e-03**; Bi 4.991e-03, 1.789e-03, **+6.781e-03**. The energy of the 1s level shifts by −3.7e-05 … −1.06e-04 m_e c² (more bound). Vacuum polarization *raises* the splitting by 0.44% to 0.68%, so with the finite charge and magnetization already counted it makes the leftover larger, not smaller. A first run crashed at Z = 4 (a variable `vals` of the solver's bracket scan overwrote the table); kept as `vp_hfs_run1.py` and `vp_hfs_run1_vals_clash.out/.err`, the Z = 1 and 2 lines of which are identical to the final run.

## 3. What is left (`combine_hfs.out`)
left = measured r/A ÷ [(1 + BR)(1 + BW)(1 + VP)] − 1. Measured r/A with relative uncertainty: Ho 0.93344 (2.6e-4), Re 0.90557 (4.4e-4), Pb 0.85539 (2.0e-4), Bi 0.87360 (1.6e-4); the measured splittings are secondary values (from search summaries).
| ion | left, uniform … shell bounds | left, single-particle (three variants) |
|---|---|---|
| Ho | −0.0148 … −0.0082 | not modelled |
| Re | −0.0153 … −0.0063 | −0.0165, −0.0174, −0.0180 |
| Pb | −0.0310 … −0.0194 | −0.0193 (all three) |
| Bi | −0.0028 … +0.0095 | −0.0210, −0.0147, −0.0122 |
For comparison, before vacuum polarization (BR + uniform BW only): Ho −0.0105, Re −0.0099, Pb −0.0246, Bi +0.0040.

**What this says.** With the single-particle magnetization and vacuum polarization, the computed corrections no longer close the gap: what remains is **−0.8% to −2.1%** for all four ions, negative in every variant of the single-particle model (−1.2% to −2.1% for Bi; −1.9% for Pb; −1.6% to −1.8% for Re; −0.8% to −1.5% for Ho by the old bounds). The earlier agreement within 1–2% was between the finite-charge-plus-bounds numbers and the measurement with vacuum polarization absent; adding the (positive) vacuum polarization moves every ion down by 0.4% to 0.7%. A remainder of this sign and size is what a negative bound-state self-energy correction would supply, which is the one piece not computed here; the free-electron anomalous moment is already in E_nr (the measured |μ_e|). That reading cannot be tested here; noticed, not claimed: the leading-order self-energy coefficient I recall, α(Zα)(ln 2 − 13/4), evaluates to −0.91% (Ho), −1.02% (Re), −1.12% (Pb), −1.13% (Bi), the same sign and size as the leftovers but from a recalled coefficient and a series that is not converged at Zα = 0.5 to 0.6, so it is a comparison of magnitudes, not a result. The residual is a standard-physics remainder with a candidate cause, not an entry in the 2% sense of the ledger.

## Not done
Self-energy (the remaining piece); the Wichmann–Kroll and higher-order vacuum polarization; the nuclear size inside the magnetic loop; deformed nucleon wave functions (Ho, Re); the true core-polarization split of the measured moments (only the three bracketing choices of the spin g-factor were used); primary papers behind the measured splittings. No connection to the instrument or to the exponents 2cos θ − 1 was attempted.

sha256: *bw_single_particle.py 5d5915bdeca607ccc6a5448071d7c4859b968a77039156742c47aa372f8e3715; *bw_single_particle.out 9e0af192ccfa0060bd4090f0424fc07f4bfd01f0de76aeb607f792562c7f022d; *bw_single_particle_run1.py df242cb3cce39a26bdb0c42386e923d5e1d9f8f8a97922e563ec1fe7c6521c45; *bw_single_particle_run1_no_muexp.out 0bfdf37f301b28096f184b4f145245ae89217ec1c299e2e8ba2cc5750d1b2820; *vp_hfs.py 53839a6d921845a7e5fc5ba90fb507d1bb266b86cf275010e8605b63ab9e3869; *vp_hfs.out dcbf012c8a29f50adc6ea528d16e41ceba042d0b0214918c689e6200e0ec8f56; *vp_hfs_run1.py 2dac0775de7594ae3d5c25d07ab0448aa5c0dc586c6633804bc7c981bb186fab; *vp_hfs_run1_vals_clash.out f0d9881377c03cea7d4a2bfb6195935f389eb926cf294080b544a37e94bc9d3e; *combine_hfs.py 0caea5723464cec49e6135c40f7e4639826a539b22d779cea85be7145002ba2f; *combine_hfs.out 17470e032769357fc07eade6130d90201e2cd5e983d34603b98ccbb6acb76ace.
Commands: `py -3 -I -X utf8 -u explore/bw_single_particle.py > explore/bw_single_particle.out` (about 25 s); `py -3 -I -X utf8 -u explore/vp_hfs.py > explore/vp_hfs.out` (tens of minutes; not timed); `py -3 -I -X utf8 -u explore/combine_hfs.py > explore/combine_hfs.out`.
