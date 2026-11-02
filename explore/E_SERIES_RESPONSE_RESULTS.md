# Is the 0.358 a scale; susceptibility, spin, resonance, and the coupling between orders (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `E_SERIES_ZEEMAN_RESULTS.md`. Scripts: `proton_magnetic_scale.py`, `e_series_response.py`, `e_series_resonance.py` (raw `.out` beside each). Nothing fitted; units κ = k = 1, μ = the M6 value 5.642738 where used. Sourced added: Rydberg energy 13.605693122990 eV, α = 7.2973525643e-3 (CODATA 2022), hydrogen hyperfine 1420.405751768(2) MHz = 5.8743261841 μeV (secondary), in `explore/data/moment_benchmark_sourced_values.txt`.

## 0. Does the 0.358 point to a scale?
Yes, as the same number read as a length and a mass (`proton_magnetic_scale.out`). A charge e circling at c on radius R has μ = e c R / 2, so the measured proton moment defines
- R_mag = 2μ_p/(e c) = 5.8736e-16 m = 2.79285 ƛ_p = 0.6986 r_p (ƛ_p = 2.1031e-16 m; r_p = 0.84075 fm = 3.9977 ƛ_p), and 0.358 = ƛ_p / R_mag;
- m_eff = ħ/(c R_mag) = m_p/(μ_p in μ_N) = 335.96 MeV (m_p/3 is 312.76 MeV).

The textbook quark relation (from memory) μ_n = −(2/3)(m_p/m_q) μ_N gives m_q = 326.97 MeV from the neutron, 2.7% below the proton's. Both are the usual constituent-quark mass scale, about 330 MeV, length about 0.59 fm. On the φ tower R_mag is at k = 93.5959, between ƛ_p (91.4616) and r_p (94.3413); no measured rung sits there. R_mag / r_p = 0.6986 is within 1.2% of 1/√2, noticed and not claimed. Caveat: this restates 1/2.79 as a length. That it is a physical scale of the proton's magnetic structure rests on the constituent reading, which is not derived here.

## 1. Susceptibility: the flux the matter induces on live links (`e_series_response.out`)
State: ring in cycle 0 (charge +1) and ring in cycle 22 (charge −1), each normalised to unit charge.
- **Static link response (lattice Ampère law).** With the matter fixed, the link field minimising G + V_spec solves H a* = −g (H the Hessian of G + V at a = 0, g = ∂G/∂a; rank 619 of 720, residual 6e-16). It puts a circulation Φ = Σ a*_e = 0.066228 through ring 0 against a ring current g = −0.095106 per step (|Φ/g| = 0.696), lowers the link energy by 0.006299, and shifts the ring's own frequency from 0.618034 to 0.611732: −1.02%. The sign of Φ against the current depends on the sign conventions of the action, which I have not tied to a Lenz statement; the frequency shift does not depend on them.
- **Live run.** Over T = 40 the dynamic ring-0 circulation has mean 0.066563 (min 0.0048, max 0.1258), against the static 0.066228: the live links oscillate about the static solution to 0.5% (first and second halves 0.0669 and 0.0662). Gauss drift 1.2e-15.
- **The matter's own flux response, links held.** One quantum in each circulation sense: M(α) = −(Area/10) Σ ω′(α) is zero at α = 0 and grows with flux (0.000908 at α = 0.01, 0.00908 at 0.1). χ = dM/dB = 0.0266907 per quantum pair, equal to the analytic (Area/10)² sin(θ/2) = 0.0266907, positive (the levels' curvature in flux is concave, so M follows B).
- **Not combined:** the links' response and the matter's response have been read separately; the self-consistent susceptibility that includes both is not computed.

## 2. Spin separately from the orbital ring
- **In the existing action, none.** The two spinor components of a ring mode are degenerate under flux: splitting 0 (`q`) and 2e-16 (`gamma`) at α = 0.1. The U(1) link phase acts on both alike, so spin splitting needs a coupling the action does not have (the transport is not made to rotate with the link field).
- **The Dirac operator route.** D_ij = exp(i k a_ij) γ_ij on the 600-cell (240 × 240) replays the repo's results: Hermitian, kernel 28, spectrum −7.6085 to 4.1291, 13 levels with multiplicities 6, 2, 12, 20, 30, 24, 28, 18, 8, 30, 30, 12, 20 (`LIVE_WEB_RESULTS.md` §8). Under the flux on ring 0 the 28 kernel modes respond to first order with 10 of them shifting symmetrically: ±0.6667, ±0.4045 (two each), ±0.1030 (two each) per unit α, and 18 not shifting (the finite-difference check at α = 1e-4 agrees). Other levels respond similarly (level 2.1796, multiplicity 8: ±0.2697, ±0.1030, four unshifted). These are Zeeman-type linear responses of the Dirac states. I did not decompose them into spin and orbital parts.

## 3. A driven transition between the two levels (`e_series_resonance.out`)
Static flux α₀ splits kq = +1 and −1 by Δ. A second-harmonic modulation of the ring's link phase, α₁ = 0.06 cos(Ωt) cos(4πn/10) (couples kq by 2), starting in kq = +1; T = 600; fraction of the mode energy found in kq = −1.
- α₀ = 0.05: Δ = 0.0950957; peak at Ω/Δ = 1.0000, fraction 0.486, half-height width Ω/Δ from 0.955 to 1.045.
- α₀ = 0.1: Δ = 0.1901321; peak at Ω/Δ = 1.0000, fraction 0.990 (a full flip), width 0.970 to 1.022.
- Doubling the field doubles the resonance frequency (0.095096 → 0.190132). Off resonance at 0.5Δ the transfer is 7e-4 (pilot run, α₁ = 0.02, T = 400).

So the instrument has the magnetic-resonance condition: Ω = Δ = 2μB.

## 4. The coupling between orders as a splitting
Two rings, one in each copy (A: ρ = 1; B: ρ_B), unit charge each, coupled only through the plaquette flux μ_r (κ_r = 0); equilibrium link field for fixed matter; splitting = E*(co) − E*(counter), in units of ω_A = 0.618034.

| ρ_B | μ_r | \|splitting\| / ω_A |
|---|---|---|
| 1 | 1e-6 | 3.446e-9 |
| 1 | 1e-4 | 3.445e-7 |
| 1 | 1e-2 | 3.427e-5 |
| 1 | 1 | 2.272e-3 |
| 1 | 5.64 | 5.571e-3 |
| 1 | 100 | 9.547e-3 |
| 1/1836.15 | 1e-6 | 3.569e-7 |
| 1/1836.15 | 1e-4 | 3.569e-5 |
| 1/1836.15 | 1 | 0.263 |
| 1/1836.15 | 100 | 1.772 |

The co-circulating configuration is the lower one in every row. At weak coupling the splitting is linear in μ_r and saturates at large μ_r. At equal μ_r it is 103.6 times larger for ρ_B = 1/1836 than for ρ_B = 1 (not 1836: the faster ring's larger amplitude also stiffens its own links).

Measured counterpart: hydrogen hyperfine / Rydberg = 5.874326e-6 / 13.605693 = 4.31755e-7. The textbook formula (from memory) (16/3)(μ_p/μ_B) α² gives 4.31984e-7, 1.0005 of the measured: the measured ratio is the nuclear moment ratio times α² times an order-1 geometric factor. The instrument carries no α. The plaquette coupling that makes the instrument's splitting equal the measured ratio is μ_r = 1.2531e-4 for ρ_B = 1 and 1.2098e-6 for ρ_B = 1/1836.15, that is 2.2e-5 and 2.1e-7 of the intra-order μ. This is a calibration of one declared parameter from one measurement, with the geometry unscaled in the dynamics; it has not been tested against a second measurement (deuterium or ³He⁺ hyperfine are the candidates; not sourced), so it is an inference to test, not a result.

## Failed runs, kept
- `e_series_response_run1_H_shadowed.out` (`e_series_response_run1.py`): sections 1 and 2 ran; section 4 crashed because I reused the name `H` (the number of histories) for the Hessian. The kernel finite-difference check in that run also printed only the unshifted zeros.
- `e_series_response_run2_signed_inversion.out` (`e_series_response_run2.py`): section 4 ran; the inversion for μ_r compared the signed splitting (negative) with a positive target and reported that no μ_r worked. Fixed by using magnitudes.
- Resonance: a first pilot selected only one vector of the degenerate spinor pair as "mode 9" (weight 0.959) and a helper was missing; both were fixed before the scan (the scan output is the only saved run).

## Not done
Combined links-plus-matter susceptibility; spin/orbital decomposition of the Dirac responses; the resonance with a perpendicular (different-plane) drive; any second hyperfine measurement; geometry scaling inside the dynamics.

sha256: *proton_magnetic_scale.py a89efa924a0d917673bb7cd3daf9650fa40d61bcf06195c12c92debd47d98dcd; *proton_magnetic_scale.out 0fdd8c8120988763eeab7221f18bf8f0738bab574bdd5e848d5a225e07883a00; *e_series_response.py 4441668fd16e6da7478c4f3d9cbfb25a8cd9db9da124f2581f6e42ca530f70c4; *e_series_response.out 15a5b4874431fc396571f3d6f00e04a00f7498e1d4eb1ac72177451372c5a6b3; *e_series_response_run1.py b8d0afa00fcb110cc313be1b1ca718eda581a276dd188f8005902f06de9f1286; *e_series_response_run1_H_shadowed.out 6371244abff86c46ff7a70eb93aaf6bba88b28cc2e662e079e7c90df107d25de; *e_series_response_run2.py 68fb8bd018975e503c1bd7fcbb789d38d37b509d7a333509991c86d31260a9ac; *e_series_response_run2_signed_inversion.out 17289a37a4f49188239b3a43dcf5c99a27a62db4f8333290f295c307ecf7caa5; *e_series_resonance.py eb1845e4acb35696afcb099dfe68f0bfbe4b78e88a5d8857e5e5107aed4dd773; *e_series_resonance.out 73239394261aba9bbad96cd0e109472858112d63f30d605b9c7f72aeb539fe0b; *data/moment_benchmark_sourced_values.txt 69dabd3a2b600b535a0630b683f7d0dd361de0114dfc1b948d43e7ee768c71b2.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` for proton_magnetic_scale, e_series_response (about 3 minutes), e_series_resonance (about 3 minutes).
