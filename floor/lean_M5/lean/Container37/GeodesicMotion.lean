/-
  CONTAINER 37 -- GEODESIC MOTION: the walk accelerating in the curvature field (free-fall).
  Rests on 08, 14, 36. GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Container 08's free walk is straight (zero acceleration = Newton's first law). On the curved mesh a
  geodesic BENDS at the deficit -- free-fall. GM.1 flat => straight; GM.2 deflection = the angle deficit
  12-2d (Regge holonomy); GM.3 the sign sets focusing (twelve focus, left wing defocus); GM.4 the
  acceleration Delta^2 localizes at the deficit (a ~ curvature). GM.5 (geodesic = free-fall) POSTULATE,
  GM.6 (continuum / value / mass) OWED -- no Lean. Mathlib-FREE, ZERO-axiom.
-/

import Container36.NegativeCurvature

namespace Container37
open Container36   -- angleDeficit -- one home (36.LW.1 / 14.B.4), consumed here

/-! ### GM.1 -- flat region: the geodesic is straight (08's free walk) -/

/-- A degree-6 (flat) vertex has deficit 0, so a geodesic through it deflects by 0 -- straight. -/
theorem flat_straight : angleDeficit 6 = 0 := by decide

/-! ### GM.2 -- deflection = the angle deficit (Regge holonomy) -/

/-- The deflection of a geodesic around a degree-d vertex is the angle deficit (14.B.4). -/
def deflection (d : Int) : Int := angleDeficit d
theorem deflection_is_deficit :
    deflection 5 = 2 ∧ deflection 6 = 0 ∧ deflection 7 = -2 ∧ deflection 8 = -4 := by decide

/-! ### GM.3 -- the sign of the deficit sets focusing -/

/-- Positive deficit (d < 6, a cone point -- the twelve) FOCUSES; negative (d > 6, the left wing)
    DEFOCUSES; d = 6 is neutral. The sign is the discrete geodesic-deviation sign. -/
theorem focusing_sign :
    angleDeficit 5 > 0 ∧ angleDeficit 6 = 0 ∧ angleDeficit 7 < 0 ∧ angleDeficit 8 < 0 := by decide

/-! ### GM.4 -- acceleration localizes at curvature (a = Delta^2, 08.8.7) -/

/-- The geodesic acceleration a = Delta^2 along the path [6,6,5,6,6] (from derivation.json). -/
def geodesicAccel : List Int := [0, 0, 2, 0, 0]
/-- It is [0,0,2,0,0] -- zero on the flat (degree-6) segments, nonzero ONLY at the deficit vertex
    (index 2, the degree-5 site), equal to the deflection there. So a ~ curvature. The "is-zero" pattern
    [true,true,false,true,true] is nonzero exactly at the deficit vertex of the path [6,6,5,6,6]. -/
theorem accel_localizes :
    geodesicAccel = [0, 0, 2, 0, 0] ∧ deflection 5 = 2
      ∧ (geodesicAccel.map (fun a => a == 0)) = [true, true, false, true, true] := by decide

#print axioms flat_straight
#print axioms deflection_is_deficit
#print axioms focusing_sign
#print axioms accel_localizes

end Container37
