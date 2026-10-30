# α(0): mechanism candidates and status (2026-10-30)

**Status entry:** α(0): mechanism candidate = induced coupling plus Kaluza–Klein tower. Blocked on R, the charged spectrum (K2) and θ_W (K2). Current tower solutions are fits, not derivations.

## What the formula leaves (component audit)
α = e²/(4πε₀ħc). ħ, c and e (in coulombs) are SI unit conversions; ε₀ is the SI wrapper (defined by ε₀ = e²/(4πα ħc); CODATA 2022 8.8541878188(14)×10⁻¹² F/m, α = 7.2973525643(11)×10⁻³); 4π is the Gauss-law solid angle, a convention (absent in Gaussian units; not the same factor as in Hawking or in the singlet decay rate). The only content is √α = e/√(4πε₀ħc) = 0.0854245. The repo's earlier scripts use the CODATA 2018 α (7.2973525693e-3); the difference is 7×10⁻¹⁰ and changes nothing so far.
Floor: charge quantization and U(1) (node 29, electric map a POSTULATE, coupling owed); colour ℤ/3 (node 31) and the ℤ₆ hypercharge grading with fractional Y = (1/6, −1/2, −2/3, 1/3, 1), Q = T₃ + Y (node 58, F14, M6 C1.3–C1.4), so charge = (e/3)k with k = 3Q integer; "primitivity fixes the generator, not measured e/α"; absolute levels conditional on content (K2).

## What the running does (explore/alpha_running_check.py, hash in its .out)
One loop, Standard Model content, 1/α_em(m_Z) = 127.951 and sin²θ_W = 0.23122 (both recalled), b_Y = 41/6, b₂ = −19/6. Above m_Z the net slope of 1/α_em is −0.584 per e-fold (fermions alone −1.70). At the Planck mass 1/α_em = 104.9. Reaching 1/α = 1 or 1/(4π) there needs 2.64 or 2.42 per e-fold over 51.5 e-folds against 0.62 supplied: short by 4.2× or 3.9×. The hypercharge Landau pole is at 1.74×10⁴¹ GeV where 1/α_em is still 75.2.

## Mechanism candidates
1. **Fixed point of the floor's own flow:** needs a floor renormalization flow with an attractive fixed point; none exists in the repo. (Asymptotic-safety precedent not verified here.)
2. **Induced coupling (Sakharov/Zeldovich):** 1/α_Y(Λ) = 0 with 1/α(0) = (2/3π) Σ N_c Q² ln(Λ/m). With SM content Λ is the Landau pole above (1.4×10²² M_P): not usable without extra charged modes.
3. **Induced + Kaluza–Klein tower (explore/alpha_tower_check.py):** all SM charged content in one dimension, exact threshold counting. KK level coefficients: b̃_Y = 2×20/3 + 1/6 = 27/2, b̃₂ = −7 + 8 + 1/6 = 7/6 (gauge+A₅, Dirac fermions, Higgs). The hypercharge zero sits at the Planck mass for R = 28.41 ℓ_P (27.94 for 1/α_Y(M_P) = 1). The zero falls 28–35 times the tower scale for any tower scale from M_P/12 to M_P/12¹³, so it is set by the content, not by the geometry. The solved R depends on a counting convention: 15.19 (circle without orbifold), 28.41 (orbifold), 54.56 (half the KK content); the input 1/α(m_Z) moves it by 0.3% per 0.2%. The closest named floor number is 30 (Coxeter), 5.6% from 28.41, but R is solved from the measured α and moves by a factor of 2 with convention, so this is not a signal.
4. **SU(2) under the tower (explore/alpha_tower_su2.py):** b̃₂ = +7/6 > 0, so SU(2) screens above 1/R and its coupling can be induced too. With the hypercharge zero at the Planck mass, 1/α₂ falls only to 44.7 there (1/α_em = 44.7); the SU(2) zero needs 276 levels against 28.4, 9.7 times as many. A single common induced scale needs about 16 extra Dirac SU(2) doublets per KK level on top of the SM content. If both couplings vanish at Λ, sin²θ_W(Λ) is a limit of a ratio, not a number.

## Structural conclusion
Above m_Z, α_em is not a single floor number. It is α_Y and α₂ (equivalently α and θ_W): the floor owes two couplings, or one coupling plus θ_W (K2). "The missing piece is one number" holds only at α(0), after the running has already used both.

## Blockers (all geometry or K2)
1. R from the floor: not derived, so the tower cannot predict.
2. Charged spectrum and masses (K2): open, so every run uses SM content by assumption.
3. θ_W (K2): open, so α₂ is unfixed.

## Not claimed
No floor derivation of any coupling. All runs are one loop, with no thresholds above m_Z except those of the tower, with recalled inputs (1/α(m_Z), sin²θ_W, textbook β coefficients). The KK tower is a model of the extra charged modes, not a feature the floor is known to have.

sha256 (scripts/outputs in explore/): alpha_running_check.py 16bbda845a35b6b5b99b877e879d3a7f5ebe42b6be7189b7d1ffd6f7acf9c82f, .out 4824fdd75a5429ca7c61318a8522d92deaa7ac1f78c06ec52faae3684809eba3; alpha_tower_check.py bbfc51f46d1b62c7e2481d6d5525bde54efa5cef0458963f8daf943cbd7c197d, .out e9399d0381b13d3b635f80e4452493ab726e3e970fd452d41bbde9cee8b7f731; alpha_tower_su2.py 2d048b65909c018f7bb3577a8e9dbda0d2716f7cce75eb79fa40a95c8075b86b, .out 597418553fecc7d1adcff5bedbc0a1c92a21c2ab05359e6f2ce6d407a7be0390.
