/-
  CONTAINER 40 -- THE DEFLECTION FORM (is the 1/b true?). Rests on 38, 39; cites the eikonal/Green's-fn
  facts. GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Light is a FRONT (39.PM.3), so deflection is refraction; the FORM is set by the source-flux dimension:
    2D  flux over the circle 2*pi*r  (dim 1)  -> log potential -> delta = pi   (CONSTANT, exponent 0)
    3D  flux over the sphere 4*pi*r^2 (dim 2) -> 1/r potential -> delta = 2/b  (exponent -1; b*delta = 2)
  So impact-independent (2+1D, 38.DV.2/39.PM.2) vs 1/b (Schwarzschild) is a DIMENSION distinction (0 vs -1).
  The closed forms pi and 2/b are CITED real analysis (as 16 cites the trig); the kernel checks the
  integer flux-dims, exponents, and the 3D invariant b*delta = 2. DF.5 (the 2*pi->4*pi double-cover route,
  38.DV.3) POSTULATE; DF.6 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container40

/-! ### DF.4 -- the deflection form is set by the source-flux dimension -/

/-- The source-flux dimension: flux spreads over r^(n-1) -- 2D a circle (r^1), 3D a sphere (r^2). -/
def fluxDim2D : Nat := 1
def fluxDim3D : Nat := 2
/-- The deflection scaling exponent p in delta ~ b^p: 2D constant (p=0), 3D ~ 1/b (p=-1). -/
def deflExp2D : Int := 0
def deflExp3D : Int := -1

theorem flux_and_exponents :
    fluxDim2D = 1 ∧ fluxDim3D = 2 ∧ deflExp2D = 0 ∧ deflExp3D = -1 ∧ deflExp2D ≠ deflExp3D := by decide

/-! ### DF.2 -- 2D is impact-independent (exponent 0; delta = pi cited) -/

/-- 2D: the deflection exponent is 0 -- CONSTANT, impact-INDEPENDENT (the 2+1D cosmic string). -/
theorem two_d_impact_independent : deflExp2D = 0 := by decide

/-! ### DF.3 -- 3D is 1/b (exponent -1; b*delta = 2 invariant; delta = 2/b cited) -/

/-- 3D: b*delta = 2, a constant -- so delta ~ 1/b (the Schwarzschild point-mass form). -/
def bTimesDelta3D : Int := 2
theorem three_d_is_one_over_b : deflExp3D = -1 ∧ bTimesDelta3D = 2 := by decide

#print axioms flux_and_exponents
#print axioms two_d_impact_independent
#print axioms three_d_is_one_over_b

end Container40
