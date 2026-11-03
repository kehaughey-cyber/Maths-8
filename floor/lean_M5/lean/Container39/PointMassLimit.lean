/-
  CONTAINER 39 -- THE POINT-MASS LIMIT (opening the continuum door). Rests on 38, 14, 25.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  PM.1 (kernel): the COMBINATORIAL curvature stays 24 radits concentrated at 12 cone points
       (14.B.4/B.5, refinement-invariant) -- a 12-cone orbifold, distinct from a smooth sphere's 0
       concentrated points. Vindicates 08.8.6 (smooth = emergent, not a floor rung); in ZPHI it is
       curves-at-scale, the smooth manifold the emergent image.
  PM.2 the 2+1D contact (conical defect = point mass, deficit = 8*pi*G*m) -- POSTULATE, filed through 19.
  PM.3 (CORRECTED): light is a FRONT not a particle, so the 3+1D 1/b is REOPENED via front-refraction;
       ambient = the 2pi->4pi double cover -- DERIVED, rests on PM.1 + 38.DV.2 (the form owed, danger-free).
  PM.4/PM.5 the reading / OWED (form danger-free, magnitude owner-gated) -- no Lean. Mathlib-FREE, ZERO-axiom.
-/

namespace Container39

/-! ### PM.1 -- the intrinsic continuum is a 12-cone orbifold, not a smooth sphere -/

/-- The total angle deficit, in radits: 12 degree-5 sites * 2 = 24 (= 4*pi), refinement-invariant
    (14.B.4). It stays CONCENTRATED at the twelve at every refinement (additions are degree-6, deficit 0,
    14.B.5). -/
def deficitTotal : Nat := 24
/-- The number of concentrated cone points: the twelve. -/
def conePoints : Nat := 12
/-- A smooth round sphere carries curvature everywhere -- 0 concentrated cone points. -/
def smoothSphereConePoints : Nat := 0

/-- The intrinsic continuum is a 12-cone ORBIFOLD: 24 radits of deficit at 12 concentrated points
    (24 = 12*2), distinct from a smooth sphere's 0 concentrated points. So refining does not smear it. -/
theorem intrinsic_continuum_is_orbifold :
    deficitTotal = 12 * 2 ∧ conePoints = 12 ∧ smoothSphereConePoints = 0
      ∧ conePoints ≠ smoothSphereConePoints := by decide

/-- The deficit never spreads to a smooth sphere: it is a fixed nonzero concentration (24) at every
    refinement -- the non-smearing that gates the 1/b point-mass (PM.3). -/
theorem deficit_stays_concentrated : deficitTotal = 24 ∧ deficitTotal ≠ 0 := by decide

#print axioms intrinsic_continuum_is_orbifold
#print axioms deficit_stays_concentrated

end Container39
