# E-series, one copy: link phases and the joint action (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Step 3 of `maps/critical_path.md`, first part: the pieces the audit found owed (`maps/instrument_audit.md`), built on one copy only. The second copy and the flux between copies are not yet built. Observation only: nothing was tuned to pass, and the free parameters are inputs, not fits.

Run: `py -3 -I -X utf8 -u e_series_one_copy.py > e_series_one_copy.out` (about 45 s). Script and conventions: `explore/e_series_one_copy.py` (docstring). Reuses `route56_subdiv.carrier` and `Qmat`.

## What was built
- Spinors Ψ_h ∈ ℂ² on the 1440 T-histories (site = the end vertex), the lab's T (spine D2).
- Native SU(2) transport on each T step, two choices run side by side with no preference set in advance: `q` (full unit transport Q(t s⁻¹)) and `gamma` (Clifford part, Q of the unit imaginary part).
- U(1) link phases a_e on the 720 edges, dynamical, and a face flux F_f on the 1200 triangles.
- One action: L = Σ|Ψ̇|² + (I/2)Σȧ² − κΣ|d_h|² − μΣ(1−cos F), d_h = Ψ_T(h) − e^{ika_h}Ω_hΨ_h. Parameters used: κ = k = I = 1; μ = (48/5) sin(π/5) = 5.64274 from M6 E3, taken as an input and not re-derived (also run at μ = 0).
- Integrator: velocity Verlet on all fields, links included ("live"); a frozen-link mode holds a fixed.

## Raw results (all in `e_series_one_copy.out`)
**Replays of earlier results**
- T: 144 cycles of length 10; T⁵ is the antipode on 1440 of 1440 histories.
- Face Wilson loop of `gamma` (route56_native order): trace −0.940456403668, std 2.7e-10, equal to −(8/5) sin(π/5) = −0.940456403668. The SU(2) angle printed is 236.098°, which is the SO(3) angle 123.90° quoted in `LIVE_WEB_RESULTS.md` §8.
- Face loop of `q` in index order: trace φ = 1.6180339855, angle 72° (2π/5, the triangle development of field equations F6). In telescoping order: trace 2, the identity (to the 1e-9 rounding of the carrier).

**New observations**
- Holonomy of the transport around each of the 144 T-cycles: `q`: trace +2 (identity) on all 144; `gamma`: trace −2 (−I) on all 144.
- Matter operator at a = 0 (blocks per cycle), s² = eigenvalues of M†M for d = Ψ_T − ΩΨ: `q` has 288 null modes (2 per cycle) and nonzero s² = 0.381966, 1.381966, 2.618034, 3.618034 (576 each) and 4 (288), i.e. 2 − 2cos(2πk/10). `gamma` has no null modes and s² = 0.097887, 0.824430, 2, 3.175570, 3.902113 (576 each), i.e. 2 − 2cos(π(2k+1)/10): the −I holonomy shifts every mode by half a step and opens a gap, lowest s² 0.0978870.
- Force check against finite differences (random state): analytic and numerical derivatives agree to 8 digits for the link and spinor derivatives, both transports.
- Energy: velocity-Verlet fluctuation at dt = 0.02 against dt = 0.01 falls by a factor 4.0 (for example 0.1947 → 0.0487 for `q`, μ = 0), so second order.
- Gauss law: the quantity I(div ȧ)_v + k ρ_v, with ρ_v = Σ_{h ending at v} 2 Im(Ψ†Ψ̇), is conserved to 5e-14 over 2000 steps with random initial data (the other sign drifts by 12 to 17). It holds for both transports and both μ, at finite dt.
- Continuity: ρ̇_v = (div j)_v with j_e = (∂G/∂a_e)/k, to 1.5e-15 (the other sign, 8). div of ∂V/∂a is 7e-15, so V_spec is gauge invariant.
- Gauge covariance: evolving a gauge-transformed state and transforming the evolved original agree to about 1e-14 for Ψ, Ψ̇, a and ȧ; the energy is identical.
- Neutral pair (opposite charge at vertex 0 and its antipode), Gauss-prepared to 1.5e-14, evolved to t = 40. With live links the Gauss quantity stays at 4e-15 and the field energy falls from 0.95 to 0.017 by t = 10 and then stays between 0.017 and 0.18 (`q`). With frozen links the Gauss quantity drifts by 2.5 (`q`) and 3.7 (`gamma`): the links must be allowed to respond for Gauss to hold. The charge at the two ends differs strongly between live and frozen links (for `q`, ρ at vertex 0 at t = 20: +0.2928 live, −9.4596 frozen).

## Failed run, kept
`e_series_one_copy_run1_pinv_residual.out` (first run). The "Gauss-prepared" pair had a residual of 4.88e-3 at t = 0, not roundoff. Cause: `numpy.linalg.pinv` with its default cutoff divided a roundoff remainder (about 1e-16) by a numerical zero eigenvalue of the lattice Laplacian. The preparation was changed to remove the mean and use `lstsq` with rcond = 1e-10; every other number in the two runs is the same. Superseded by `e_series_one_copy.out`.

## What this does and does not show
- It shows that the link layer and the joint action exist and are consistent: gauge covariance, a conserved Gauss quantity, continuity, and second-order energy conservation all hold, for both transports.
- The model contains an electric field (ȧ_e) and a magnetic flux (F_f through faces, with energy V_spec). No readout of a manifest magnetic effect has been taken: no source producing a net field has been built or measured.
- The two transports differ in a way that matters: `q` has cycle-constant zero modes (the disconnected ten-cycles the M6 text describes); `gamma` has none. This is observed here and not interpreted. I did not check the 288 zero modes against M6's count of 4320 per register (its register has more content).
- One copy, one spinor register, dimensionless units. κ, k, I are 1; μ is the M6 value used as an input. No calibration to any measurement has been made, so no percentage of a measured value is reported (`maps/percentage_frame.md`).
- The Gauss sign (+k ρ) is a convention of the coupling in this action; it is not a physical statement about charge.
- Not built: the second copy and flux between copies, the expressed/manifest split of a readout, the ablation switches, the second register or conjugate charge content.

sha256: *e_series_one_copy.py a3268db0df54d4264f64f25751812041192b6d923770322c41c8d9b20c5ce9ec; *e_series_one_copy.out 73bf87b47253fd0d250b257b7a2a6224aaf9cbf6c65414dd8cb02fbdb15d4dce; *e_series_one_copy_run1_pinv_residual.out d285fd35d6b9cddfe2a67ce583920844d5d928e3b2de5630dead0cec8c0d7497.
