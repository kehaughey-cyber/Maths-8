# E-series, two adjacent copies with radial links and inter-copy flux (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Step 3 of `maps/critical_path.md`, second part, on top of `explore/E_SERIES_ONE_COPY_RESULTS.md`. Observation only: every parameter below is a declared choice, swept or set to zero, and nothing is tuned.

Run: `py -3 -I -X utf8 -u e_series_two_copy.py > e_series_two_copy.out` (about 4 minutes). The setup (carrier, T-histories, edges, faces, transports) is executed unchanged from `e_series_one_copy.py`.

## What was built
- Two copies A and B, each exactly the one-copy system (spinors on the 1440 histories, the transport `q` or `gamma`, U(1) links on 720 edges, face flux), on the same vertex set.
- **Tick ratio ρ (declared, swept 1, φ, 12).** B is the next order up with a tick ρ times longer: kinetic weight m_B = ρ², link inertia I_B = Iρ², potentials unchanged, so every B frequency is 1/ρ of A's. Geometry is not scaled: ρ enters only as a rate. The nesting here is a rate ratio plus an identification, not the φ^k radius of the lab.
- **Radial links b_v** (120), oriented A → B, with gauge shift (λᴮ−λᴬ)/k, so each copy keeps its own gauge freedom.
- **Two inter-copy terms, each with its own strength:** the matter term κ_r Σ_h |Ψᴬ_h − e^{−ikb}Ψᴮ_h|² (the same history in the two copies; identity identification, a declared choice), and the plaquette flux μ_r Σ_e (1−cos P_e) with P_e = aᴬ_e + b_head − aᴮ_e − b_tail through each radial square, plus radial link kinetic energy (I_r = 1). Setting κ_r or μ_r to 0 removes that term.
- Parameters: κ = k = I = I_r = 1; μ = (48/5) sin(π/5) from M6 E3 as an input; κ_r ∈ {0, 0.1, 1}, μ_r ∈ {0, M6 value}.

## Checks (all in `e_series_two_copy.out`)
- Forces against finite differences for aᴬ, aᴮ, b, Ψᴬ, Ψᴮ, both transports: agree to 7 to 9 digits (for example `q` aᴬ −37.68472371 analytic, −37.68472379 numerical).
- Gauge covariance with independent transformations in each copy and the radial links shifted accordingly: agrees to about 1e-14 for Ψ, Ψ̇, a, ȧ, b, ḃ; energy identical.
- Per-site Gauss quantities (A: I_A div ȧ_A − I_r ḃ_v + kρ^A; B: I_B div ȧ_B + I_r ḃ_v + kρ^B) conserved to 5e-14 (ρ = 1 and φ) and 1.2e-11 (ρ = 12, where the energy is about 1e5) over 2000 steps with random data, both transports.
- Energy fluctuation falls by 4.00 when the step is halved in five of the six cases (second order); `gamma` at ρ = 12 gives 3.41, observed and not explained here.
- Decoupling (κ_r = μ_r = 0, ρ = 1): copy A with B random and with B zero agree exactly (0.0).

## What the sweep shows
Setup: a neutral pair of opposite charge at vertex 0 and its antipode in A, Gauss-prepared with A's links; B empty; links live; T = 40. Fractions are of the total energy, counted in B's matter and link terms; t_arr is the first time the fraction exceeds 1e-3 (the threshold is arbitrary).

| ρ | κ_r | μ_r | `q`: t_arr, max fraction in B | `gamma`: t_arr, max fraction in B |
|---|---|---|---|---|
| 1 | 0 | 0 | none, 0 | none, 0 |
| 1 | 0.1 | 0 | 0.58, 0.454 | 0.58, 0.520 |
| 1 | 1 | 0 | 0.06, 0.589 | 0.06, 0.543 |
| 1 | 0 | M6 | 0.26, 0.0040 | 0.26, 0.0040 |
| 1 | 1 | M6 | 0.06, 0.755 | 0.06, 0.751 |
| φ | 0.1 | 0 | 1.20, 0.028 | 1.20, 0.0196 |
| φ | 1 | 0 | 0.10, 0.289 | 0.10, 0.359 |
| φ | 0 | M6 | 0.36, 0.0023 | 0.36, 0.0021 |
| φ | 1 | M6 | 0.10, 0.128 | 0.10, 0.114 |
| 12 | 0.1 | 0 | none, 0.0002 | none, 0.0001 |
| 12 | 1 | 0 | 14.04, 0.0010 | 31.50, 0.0010 |
| 12 | 0 | M6 | none, 0.0001 | none, 0.0001 |
| 12 | 1 | M6 | none, 0.0008 | none, 0.0009 |

- With κ_r = μ_r = 0 nothing reaches B, as it must.
- Energy moves into B much more through the matter coupling than through the plaquette flux alone (largest plaquette-only fraction 0.0040).
- For the same coupling, the fraction reaching B falls steeply as ρ rises: for κ_r = 0.1 it is 0.454 at ρ = 1, 0.028 at ρ = φ, 0.0002 at ρ = 12. In these runs the exchange between orders is large when their rates are close and nearly absent when they differ by a factor 12.
- Equal copies (ρ = 1) show strong exchange that does not settle: the fraction in B oscillates (for `q`, κ_r = 1, μ_r = 0: 0.34, 0.43, 0.30, 0.35 at t = 10, 20, 30, 40).
- Frozen-link control (`q`, ρ = φ, κ_r = 1, μ_r = M6 value): the maximum fraction in B is 0.1545 against 0.1281 with live links, and the Gauss quantity drifts by 11.8 against 5.3e-15. As in the one-copy result, the links must respond for Gauss to hold.
- Gauss is conserved to 1.3e-14 or better in all 30 sweep runs (15 per transport); energy fluctuation stays below 6.5e-3.

## What this does and does not show
- It shows a gauge-covariant, Gauss-conserving two-order system with flux between orders, in which transfer between orders depends strongly on the ratio of their rates. This is a property of this model with these declared couplings and is not derived from the floor.
- It does not fix the radial-hop cost of the lab, and it does not show which ρ or which κ_r nature uses. The strengths κ_r, μ_r, I_r, the identity identification of histories, and the choice of rate-ratio values are all declared.
- Geometry is not scaled between copies; both copies sit on the same 120-vertex carrier. Representing the φ^k size relation, or any common-offset question, needs more than this.
- Nothing is calibrated to a measurement, so no percentage of a measured value is reported (`maps/percentage_frame.md`). No manifest magnetic effect has been read out. The expressed/manifest split of a readout is not built; the switches κ_r = 0 and μ_r = 0 are the first ablations available.
- Not explained: the 3.41 energy-order ratio for `gamma` at ρ = 12.

## Failed run, kept
`e_series_two_copy_run1_fdtest_bug.out` (script `e_series_two_copy_run1.py`). The finite-difference test subtracted the matter terms from the potential, so the analytic and numerical derivatives disagreed for aᴬ, aᴮ and Ψ (the b derivative, which does not depend on those terms, agreed). That was an error in the test, not in the forces. The test was corrected; lines 18 onward of the two outputs are identical.

sha256: *e_series_two_copy.py bffa8ccf343ef93705a26d8d4d9fadd27759ff62ec2f8fe73b8485bb0c543627; *e_series_two_copy.out f98fe889798b15b8889a4a7b7f2edcb25204a7ca42f224d62fb04d859527da3a; *e_series_two_copy_run1.py da11a5598d771faf971e4bd5cf6f636a5ce12aa4b3ed94db29dc893d6e2fd1c0; *e_series_two_copy_run1_fdtest_bug.out 2743fe47a85bcce063684f26b29753cdb2c062abc483ae975e64b48e549111a2.
