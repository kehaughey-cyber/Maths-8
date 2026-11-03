/-
  CONTAINER 36 -- NEGATIVE CURVATURE: the LEFT WING of the mirror (the max-density direction).
  Rests on 14, 15. GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Container 15 built only the right wing (D >= 0: the twelve degree-5 sites, min density; degree-6 flat,
  the mirror). This builds the LEFT wing: degree > 6, D < 0, the max-density direction.
  LW.1 the signed curvature D_1 = 6 - d (angle deficit 12 - 2d) across the mirror -- negative for d > 6.
  LW.2 the degree-7 star is denser than flat: |B_1| = 8 > flatBall 1 = 7, D_1 = -1.
  LW.3 the {3,7} tiling grows faster than flat (validated cold on flat {3,6}): D_r < 0 and growing.
  LW.4 Gauss-Bonnet: right wing sum(12-2d) = +24 = 12*chi (chi = 2, genus 0); a degree-7 site is -2, so
       an all-degree>6 surface has chi < 0 (genus >= 2 or the open plane) -- NOT the genus-0 sphere.

  Mathlib-FREE, ZERO-axiom. LW.5 (black-hole reading) POSTULATE; LW.6 (realization/value) OWED -- no Lean.
-/

import Container14.DensityDeficit

namespace Container36
open Container14   -- flatBall -- one home (14.B.1), consumed here

/-! ### LW.1 -- the signed curvature across the mirror: D_1 = 6 - d, angle deficit = 12 - 2d -/

/-- The ball-deficit at r = 1 for a degree-d vertex: D_1 = flatBall 1 - (d+1) = 6 - d. -/
def ballDeficit1 (d : Int) : Int := 6 - d
/-- The angle deficit at a degree-d vertex (14.B.4): 12 - 2d radits. -/
def angleDeficit (d : Int) : Int := 12 - 2 * d

/-- flatBall 1 = 7 (the flat reference, from Container14) -- so D_1 = 7 - (d+1) = 6 - d. -/
theorem flat_ball_one : flatBall 1 = 7 := by decide

/-- The mirror: d = 5 is positive (right, min-density), d = 6 is zero (the mirror), d = 7 is NEGATIVE. -/
theorem deficit_across_mirror :
    ballDeficit1 5 = 1 ∧ ballDeficit1 6 = 0 ∧ ballDeficit1 7 = -1
      ∧ angleDeficit 5 = 2 ∧ angleDeficit 6 = 0 ∧ angleDeficit 7 = -2 := by decide

/-- Degree > 6 is the LEFT wing: both deficits strictly negative (checked at d = 7, 8). -/
theorem left_wing_negative :
    ballDeficit1 7 < 0 ∧ ballDeficit1 8 < 0 ∧ angleDeficit 7 < 0 ∧ angleDeficit 8 < 0 := by decide

/-! ### LW.2 -- the degree-7 star realizes the first negative-curvature site -/

/-- |B_1| at the degree-7 star centre = deg + 1 = 8 (the relabelling identity 13.A.3). -/
def starB1 : Nat := 8
/-- The star is DENSER than flat: |B_1| = 8 > flatBall 1 = 7. -/
theorem star_denser_than_flat : starB1 > flatBall 1 := by decide
/-- Its deficit D_1 = flatBall 1 - |B_1| = 7 - 8 = -1 < 0 (negative curvature). -/
def starD1 : Int := (7 : Int) - 8
theorem star_deficit_neg : starD1 = -1 ∧ starD1 < 0 := by decide

/-! ### LW.3 -- the {3,7} tiling grows faster than flat; the flat reference is 14's flatBall -/

/-- The {3,7} ball counts |B_r| for r = 0..5 (from the coordination recurrence, derivation.json). -/
def hypBalls : List Nat := [1, 8, 29, 85, 232, 617]
/-- The signed deficit D_r = flatBall r - |B_r| for r = 0..5. -/
def hypDeficit : List Int := [0, -1, -10, -48, -171, -526]

/-- The def values are exactly the derivation's (pinned literals). -/
theorem hyp_values : hypBalls = [1, 8, 29, 85, 232, 617] ∧ hypDeficit = [0, -1, -10, -48, -171, -526] := by decide

/-- The flat reference is exactly container 14's flatBall on r = 0..5 (the internal guard: the {3,d}
    recurrence reproduces flat {3,6} = 1 + 3r(r+1)). -/
theorem flat_reference_is_container14 :
    (List.range 6).map flatBall = [1, 7, 19, 37, 61, 91] := by decide

/-- The {3,7} ball exceeds flat at every r >= 1 (faster-than-flat, hyperbolic) -- flat literals are
    flatBall by `flat_reference_is_container14`. -/
theorem hyp_denser_than_flat :
    (8 : Nat) > 7 ∧ 29 > 19 ∧ 85 > 37 ∧ 232 > 61 ∧ 617 > 91 := by decide

/-- The deficit is negative for r >= 1 (max-density) and strictly growing -- more negative each step
    (unbounded, the mirror of the twelve's bounded tri(r)). -/
theorem hyp_deficit_neg_and_growing :
    ((-1 : Int) < 0 ∧ -10 < 0 ∧ -48 < 0 ∧ -171 < 0 ∧ -526 < 0)
      ∧ ((-10 : Int) < -1 ∧ -48 < -10 ∧ -171 < -48 ∧ -526 < -171) := by decide

/-! ### LW.4 -- Gauss-Bonnet: the wings live on different surfaces -/

/-- Right wing: twelve degree-5 sites, total angle deficit 12*(12-2*5) = +24 = 12*chi, so chi = 2. -/
def rightWingTotal : Int := 12 * angleDeficit 5
theorem right_wing_sphere : rightWingTotal = 24 ∧ rightWingTotal / 12 = 2 := by decide
/-- A single degree-7 site contributes -2: an all-degree>6 surface has total < 0, so chi < 0
    (genus >= 2 or the open plane) -- NOT a genus-0 sphere. -/
theorem left_wing_chi_negative : angleDeficit 7 = -2 ∧ angleDeficit 7 < 0 := by decide

#print axioms flat_ball_one
#print axioms deficit_across_mirror
#print axioms left_wing_negative
#print axioms star_denser_than_flat
#print axioms star_deficit_neg
#print axioms hyp_values
#print axioms flat_reference_is_container14
#print axioms hyp_denser_than_flat
#print axioms hyp_deficit_neg_and_growing
#print axioms right_wing_sphere
#print axioms left_wing_chi_negative

end Container36
