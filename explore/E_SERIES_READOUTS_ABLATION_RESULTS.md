# E-series: expressed / manifest readouts, the order dependence of the moment, adjacent-rung ratios, and the ablation record (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `E_SERIES_ONE_COPY_RESULTS.md` and `E_SERIES_TWO_COPY_RESULTS.md`. Guidance followed: where a choice was arbitrary, use what nature shows if it is known and otherwise explore it; find known things to measure against; do not force a calibration; do not start from the κ_r / μ_r ablations. Nothing is fitted. Benchmarks used: the measured nuclear magnetic moments (saved IAEA table), the sizes of the rungs of one gram of carbon (`maps/carbon_complete_stack.md` §1), and CODATA 2022 moments and mass ratio (`explore/data/moment_benchmark_sourced_values.txt`).

## 1. What nature shows: ingredients present, effect not manifest (`carbon_nuclear_moments.py`)
Expressed = the sum of the free-nucleon moments in magnitude (neutron −1.9130427 μ_N and proton 2.792847351 μ_N, the table's own rows); manifest = the measured moment of the nucleus. Selected rows (nuclear magnetons; full table in `carbon_nuclear_moments.out`):

| nuclide | Jπ | Σ\|μ_i\| | signed sum | measured μ | \|μ\| / Σ\|μ_i\| |
|---|---|---|---|---|---|
| ²H | 1+ | 4.7059 | 0.8798 | 0.8574382 | 0.182 |
| ⁴He | 0+ | 9.4118 | 1.7596 | none (spin 0) | 0 |
| ¹²C | 0+ | 28.2353 | 5.2788 | none (spin 0) | 0 |
| ¹³C | 1/2− | 30.1484 | 3.3658 | 0.7023690(40) | 0.0233 |
| ¹⁴N | 1+ | 32.9412 | 6.1586 | 0.4035730(20) | 0.0123 |

Twelve nucleons in carbon-12 carry 28.2 μ_N in magnitude and the nucleus shows none; across the table the manifest moment is 0 to a few per cent of the expressed one. Two rows are inconsistent in the saved table and are not used: ¹⁶O and ⁵⁶Fe are listed as Jπ 0+ and also with a nonzero moment (1.668(12) and 1.02(11)), which a spin-0 ground state cannot have.

## 2. The instrument's readouts, expressed and manifest (`e_series_readouts.py`)
Definitions: expressed is counted on the histories (each carries its own charge ρ_h and step current g_h); manifest is what survives when they combine at the vertex or edge. Charge: manifest = |net charge| and the dipole |Σρ_v X_v|. Current: manifest magnetic moment = |Σ_e j_e B_e| with B_e = ½ X_tail ∧ X_head (the bivector of the triangle swept from the origin; current × area). States are the exact eigenmodes of the T-cycles (eigen-equation residual 6e-9 for `q`, 8e-16 for `gamma`).

Results, transport `q`, ρ = 1, kq = 1 (the `gamma` run gives the same pattern with different magnitudes):

| state | charge expressed | net Q | current expressed | current manifest |
|---|---|---|---|---|
| one ring | 12.3607 | +12.3607 | 3.4549 | 3.4549 |
| ring + its reverse ring, opposite charges | 24.7214 | 0 | 6.9098 | 0 |
| ring + its reverse ring, same charge sign | 24.7214 | +24.7214 | 6.9098 | 0 |
| all 144 rings, each decagon pair neutral | 1779.94 | 0 | 497.508 | 0 |
| all 144 rings, random charge signs | 1779.94 | −74.16 | 497.508 | 0 |

- Ring plus any other cycle (142 partners, opposite charges): manifest / expressed current from 0.3717 to 0.9283, median 0.7071.
- The dipole is zero to the carrier's 1e-8 rounding in every state.
- In these eigenmode states the current depends on the spatial phase pattern and the amplitude, not on the sign of the charge.
- So the instrument reproduces the pattern of section 1: large expressed content, with a manifest moment that ranges from all of it to none of it depending on how the pieces combine.

## 3. Moment per charge against the order, and the one measured number it meets
For one ring in a copy whose tick is ρ times longer (m = ρ², ω = s/ρ), numerically: the magnetic moment at fixed amplitude is independent of ρ, |Q| ∝ ρ, so moment per charge ∝ 1/ρ (checked from ρ = 5.4e-4 to 1836; moment/|Q| × ρ = 0.279508 throughout). If the geometry is scaled with the tick (edge = c × tick, the lab's declared anchor; area ∝ ρ²), moment per charge ∝ ρ.

Comparison: proton order against electron order, with ρ the measured mass ratio 1836.152673426 (CODATA 2022).
- model: moment per charge ratio = 1/1836.152673426 = 5.446170e-4 (the nuclear magneton over the Bohr magneton);
- measured: |μ_p / μ_e| = 1.5192704e-3;
- model / measured = **0.35847** (= 1/(μ_p/μ_N) times μ_B/μ_e; 1/2.792847 = 0.35807).

Reading: with size and tick scaled together, the instrument gives the magneton scaling (moment per charge ∝ 1/mass ∝ size). The residual factor 2.79 is the proton's own moment in nuclear magnetons, which the instrument does not produce (nor the neutron's −1.913 μ_N with zero net charge). This is not an independent test of ρ: the mass ratio sets ρ and the geometry scaling is the declared anchor, so it checks that the declared anchors are consistent with Compton-size scaling. Spreads for measure (a): measurement ~1e-9, instrument none (exact scaling); the declared geometry scaling was not swept; r = 0.358 does not cover 1.

## 4. The tick ratio as nature shows it (`e_series_ablation.py`, part A)
Sizes of the carbon-gram rungs (master table only), sorted; rungs within 3% merged: 19 distinct sizes. Adjacent ratios below the jump to the gram: 1.8946, 3.9976, 2.222, 1.2527, 1.0556, 156.36, 22.838, 6, 2.054, 1.038, 1.03, 1.067, 1.145, 1.087, 2.31, 1.157; minimum 1.03, median 1.574, maximum 156.4 (the jump from the thermal energy rung to the gram, 1.1e7, and from the gram Compton length to the τ Compton length, 3e23, are excluded).

Two-copy exchange at those ratios (κ_r = 1; links live; neutral pair of rings in A, B empty; T = 40; fraction of the total energy reaching B):

| ρ | μ_r = 0: max fraction | μ_r = M6: max fraction |
|---|---|---|
| 1.03 to 1.25 | 0.46 to 0.49 | 0.55 to 0.72 |
| 1.89 | 0.364 | 0.262 |
| 2.31 | 0.339 | 0.165 |
| 4.0 | 0.0751 | 0.0501 |
| 6 | 0.0239 | 0.0185 |
| 22.8 | 0.0011 | 0.0039 |
| 156.4 | 0.0000 | 0.0006 |

Arrival (first time above 1e-3 of the total) is 0.06 to 0.10 for ρ ≤ 2.3 and grows to 0.18, 0.28, 1.38 at ρ = 4.0, 6, 22.8; at 156 it does not occur for μ_r = 0. For κ_r = 1, μ_r = 0 the max fraction falls roughly as ρ^−2.8 between 4.0 and 6 and ρ^−2.3 between 6 and 22.8 (two-point slopes). The Gauss quantity is conserved to 7e-14 or better in every run. κ_r is a declared strength, so this is the instrument's transfer curve, not yet a comparison with a measured inter-order coupling; the hydrogen hyperfine splitting over the Rydberg energy (about 4e-7, from memory, not sourced) is the natural measured counterpart and is not done.

**Noticed after computing, not claimed:** three of the measured adjacent ratios are within 0.005 of a half-integer power of φ: 156.36 = φ^10.4988, 22.838 = φ^6.5011, 2.054 = φ^1.4958. The chance that one value falls that close to a half-integer is about 0.017; for three of 16, about 0.003. The half-integer was chosen after seeing the values, the rungs carry 0.1 to 0.2% uncertainties (0.002 to 0.004 in the exponent), and no other offset or anchor was tested. The lattice-placement map found no common offset against the Planck anchor.

## 5. Ablation record (part B)
Scenario: a neutral pair of rings (cycle 0, and cycle 22 which gives manifest/expressed current 1/√2) in copy A, Gauss-prepared with A's links, copy B empty. Base setting declared: ρ = the median measured adjacent ratio 1.5736, κ_r = 1, μ_r = M6 value, transport `q`. Time means over T = 20. Full table with all columns in `e_series_ablation.out`; ratios to base:

| switch | charge expr A | current expr A | moment man A | flux expr A | flux man A | moment man B | energy fraction in B |
|---|---|---|---|---|---|---|---|
| links frozen | 0.932 | 1.043 | 1.043 | 0 | 0 | 1.177 | 1.002 |
| charge coupling off (k = 0) | 0.932 | 1.043 | 1.043 | 0 | 0 | 1.177 | 1.049 |
| face flux energy off, both copies (μ = 0) | 0.895 | 0.690 | 0.689 | 8.35 | 5.19 | 1.224 | 1.396 |
| plaquette flux between copies off (μ_r = 0) | 0.916 | 1.286 | 1.286 | 2.03 | 2.62 | 2.587 | 1.211 |
| matter coupling between copies off (κ_r = 0) | 1.505 | 2.549 | 2.549 | 1.37 | 1.79 | 0 | 0.0757 |
| copies decoupled | 1.505 | 2.553 | 2.553 | 2.13 | 3.10 | 0 | 0 |
| transport `gamma` instead of `q` | 1.633 | 1.72 | 1.72 | 1.51 | 1.71 | 1.123 | 0.877 |
| equal ticks (ρ = 1) | 0.791 | 0.879 | 0.879 | 1.14 | 1.11 | 2.784 | 2.038 |
| ρ = 1836.152673426 | 1.505 | 1.51 | 1.51 | 1.085 | 1.109 | 1.3e-11 | 3.1e-6 |

What the record shows (no prediction was made beforehand):
- The matter readouts do not move when the links are frozen or the charge coupling is switched off (ratios 0.93 to 1.04), but the flux readouts vanish (0): the flux and its moment exist only with live links and a nonzero coupling.
- With the face-flux energy removed, the unrestrained flux grows 8.35-fold in expressed and 5.19-fold in manifest terms, and the current falls to 0.69.
- Decoupling the copies raises copy A's current and moment 2.55-fold: copy B draws on them.
- At ρ = 1836 copy B receives 3e-6 of the energy and the A-side readouts are close to the decoupled ones.
- The manifest / expressed current ratio of the A pair stays at 0.7071 to within 0.25% in every setting; the links change it very little over T = 20.
- `gamma` is not a like-for-like ablation: its ring states have different θ and ω from the `q` states, so the ratios reflect different states as well as a different transport.
- Gauss conserved to 1.8e-14 or better in every run except the frozen-link run (1.13), as before.

## Failed runs, kept
- `e_series_readouts_run1_expressed_after_cancellation.out` (script `e_series_readouts_run1.py`): expressed was counted after combining at the edge or vertex, so a pair of opposite currents on one edge counted as zero in both columns and the split could not show anything; also, the labels "charge −" were attached to states with Q > 0. Fixed by counting expressed on the histories and relabelling.
- `e_series_ablation_run1_parsed_other_tables.out` (script `e_series_ablation_run1.py`): the parser read rows from the later tables of `carbon_complete_stack.md` (energies and couplings), so the ratios beyond the gram row and the median used as base ρ (2.31) were wrong. Fixed by reading the master size table only (base ρ became 1.5736).

## Not done
No calibration. No comparison of κ_r with a measured inter-order coupling (hyperfine is the candidate). The electron magnetic moment itself and the collective susceptibility are not produced. The second-register and conjugate charge content are not built. The geometry scaling between copies is applied in the readout only, not in the dynamics.

sha256: *carbon_nuclear_moments.py c90aeb8e7e254eb035a88cbdea84dd611ed956c95691214f966c3ca222953087; *carbon_nuclear_moments.out 512df31d8ca4fdd9a0a636db0fa4abaf65b0036d4f3b1656b404061cafba183a; *e_series_readouts.py 89b3532f925d20961dc616b1c8e3c8a84e99089f39eaedcf95879800f997f9c8; *e_series_readouts.out eb65d0551abab8cab7e57ebba4b2610b5b7fa4fe742a27f782b9a99ead741eb3; *e_series_readouts_run1.py 8d1b045d8927a32a53de26472132c4aa6fa5995eaed7684e6454ba9d64e54d96; *e_series_readouts_run1_expressed_after_cancellation.out b03cb5f30622b153a1d6f8e640b006822cf02bd230d3da07e28e880ea289d9bb; *e_series_ablation.py d99f379e17abb969318a53371c9e678b6b366a7e25e23e010bca8f8f866d83c8; *e_series_ablation.out b1b2180a9f228a38ad5c11bbb146cfb5486846401a98046cdf730c36e6be9eb7; *e_series_ablation_run1.py dba666a171b18fa6a2d05530d70c25552fa5da5e0acbe0af6a462d1f2877b8f9; *e_series_ablation_run1_parsed_other_tables.out 7684fc013537d6304eff4dae3331b5ecfff27f295aa1cc50d5c5ae802e7b34b3; *data/moment_benchmark_sourced_values.txt 9097ebbd79e8e66a018705b96ab0e3d14c80be06ad070c5cf056bbb15bbd331b.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` for carbon_nuclear_moments, e_series_readouts, e_series_ablation (the last takes about 5 minutes).
