
#### Proof entries for IV.1 (route 56)

**C-R1 The degree-7 threshold (§28 of `LIVE_WEB_RESULTS.md`): PROVED / CHECKED.**
*Statement.* Let 2I be the binary icosahedral group (the 120 unit icosians), 2 its defining spinor representation and 2′ the Galois conjugate (√5 → −√5). The internal harmonics of polynomial degree n transform as Sym^n(2′). Then Sym^n(2′) contains no copy of 2 for 0 ≤ n ≤ 6, and n = 7 is the first n for which it does (multiplicity 1; it appears again at n = 13).
*Proof.* The character of Sym^n(V) at a group element with eigenvalues e^{±it} on V is sin((n+1)t)/sin t (n+1 or (−1)^n (n+1) at t = 0, π). For 2 the angle t is given by cos t = Re(u) for the unit icosian u; for 2′ it is given by the Galois conjugate of Re(u), which lies in [−1, 1] for every element of 2I. The multiplicity of 2 in Sym^n(2′) is the group average of χ_Sym^n(2′) · χ_2 over the 120 elements. Orthonormality of the characters is verified first (⟨2,2⟩ = ⟨2′,2′⟩ = 1, ⟨2,2′⟩ = 0). The averages for n = 0 … 13 are 0 except n = 7 and n = 13, which give 1. ∎ (a finite computation over 120 elements, exact up to floating-point rounding.)
*Check.* `explore/spine_route56_check.py` → `explore/spine_route56_check.out` (last line `RESULT PASS`). The same script finds the first icosahedral invariant of the binary form at degree 12, matching Klein.
*Status.* PROVED / CHECKED. It explains why the recorded zero-mode count (§23, §26: polynomials of degree ≤ 6 are zero modes of the Weyl block, the exact ℤ[φ] threshold at 7) has the threshold it has; it does not by itself prove the zero-mode statement for the lattice operator.

**The rest of IV.1: COMPUTED, recorded, not re-proved here.** Each result is in `explore/LIVE_WEB_RESULTS.md` with its script and raw output; the script is the proof. Reproduce status is from `explore/REPRODUCE_REPORT_2026-11-02.md`.

| result | section | script(s) | reproduce |
|---|---|---|---|
| the 28 massless Dirac modes = {1, 2′, 3′} ⊗ spinor; the selection is Galois, not chirality | §9, §10, §12 | `route56_kernel.py`, `route56_chirality.py`, `route56_selection.py` | MATCH |
| subdivision scale flow (smooth levels converge as θ²; the non-smooth sector and the 28-core do not) | §14 | `route56_subdiv.py` | MATCH |
| exact icosian shells are Hecke shells; the Hecke T_p is K(120, 720) | §21 | `route56_hecke.py`, `route56_hecke_check.py` | `route56_hecke_check` DIFFERS (undiagnosed) |
| 4D icosian lattice Dirac operator: exact E(k, k′), internal sector flat to order 7, 4-dimensional zero manifold | §22, §23 | `route56_lattice4d.py`, `route56_window.py`, `route56_internal_poly.py` | MATCH |
| internal momentum renormalises the velocity (2J1(r)/r for r ≤ 2), not a mass term | §24, §25 | `route56_mass_probe*.py`, `route56_velmap.py` | MATCH |
| degree ≤ 6 zero modes, threshold 7 in ℤ[φ] | §26, §28 | `route56_exact_moments.py`, `route56_irrep_content.py` | MATCH (the group-theory half is C-R1) |
| E8 invariant subalgebra under 2I_L × 2I_R is zero (§30); "no route to SU(3)" WITHDRAWN (§31) | §29 to §31 | `route56_core_joint.py`, `route56_e8_a` to `route56_e8_f` | `route56_e8_c` to `_f` ERROR in a fresh export (a probably untracked data file) |
| mass fork; inertia E/v² with no rest mass; k′ dynamics (Landau-Zener band flips) | §32 to §34 | `route56_massfork*.py`, `route56_inertia*.py`, `route56_dynamics.py` | MATCH |
| scale, link, approximants, core (inherited) | §16 to §20 | `route56_core.py`, `route56_link.py`, `route56_approx.py` | DIFFER (undiagnosed) |
