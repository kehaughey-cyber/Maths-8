/-
  CONTAINER 47 -- THE FOCUSING RESOLUTION: the 37-vs-15 tension is a spatial/spacetime TYPE error, dissolved by 46.
  Rests on 37 (the focusing + the tension), 15 (the vacuum reading), 46 (the signature).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  37.GM.3 focuses (attractive) at the twelve (positive spatial deficit); 15.C.3 reads them as vacuum
  (repulsive) -- the tension (FR.1). Resolution (b), forced by 46: 37's focusing is SPATIAL (Gaussian K);
  gravitational attraction/repulsion is the SPACETIME Raychaudhuri focusing of the TIMELIKE congruence,
  set by rho+3p, needing 46's timelike direction (FR.2). rho+3p: vacuum (w=-1) = -2rho < 0 (repulsive);
  matter (w=0) = +rho > 0 (attractive) -- INDEPENDENT of the spatial K, so no contradiction (FR.3). FR.4
  (which the twelve are) POSTULATE; FR.5 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container47

/-- The angle deficit 12 - 2d (the spatial Gaussian curvature charge, 14/37). -/
def deficit (d : Int) : Int := 12 - 2*d

/-- rho + 3p for equation of state p = w*rho -- the spacetime (Raychaudhuri) focusing quantity. -/
def rhoPlus3p (rho w : Int) : Int := rho + 3*(w*rho)

/-! ### FR.1 -- the twelve have positive spatial deficit (37 focusing) -/

theorem twelve_spatial_focus : deficit 5 = 2 ∧ deficit 5 > 0 := by decide

/-! ### FR.3 -- the spacetime sign is rho+3p, independent of spatial K -> no contradiction -/

/-- With rho = 1: vacuum (w = -1) gives rho+3p = -2 < 0 (REPULSIVE, defocuses timelike geodesics); matter
    (w = 0) gives rho+3p = +1 > 0 (attractive). The spacetime sign is set by rho+3p, NOT by the spatial
    deficit -- so positive spatial curvature (deficit 5 = 2 > 0) and vacuum repulsion (rhoPlus3p 1 (-1) < 0)
    hold at once: no contradiction. -/
theorem no_contradiction :
    rhoPlus3p 1 (-1) = -2 ∧ rhoPlus3p 1 (-1) < 0
      ∧ rhoPlus3p 1 0 = 1 ∧ rhoPlus3p 1 0 > 0
      ∧ deficit 5 > 0 := by decide

#print axioms twelve_spatial_focus
#print axioms no_contradiction

end Container47
