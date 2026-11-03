/-
  CONTAINER 38 -- THE DEFLECTION VALUE. Rests on 37, 36, 14, 21. GENERATED FROM derivation.json BY
  check/gen_lean.py. DO NOT EDIT BY HAND. `python3 gen_lean.py --check` fails on disagreement.

  DV.1 the per-site deflection = the deficit in radits (2 at the twelve = pi/3 = 60deg, pi cited).
  DV.2 the deflection is the FULL deficit (deflection = angleDeficit) -- impact-parameter-independent,
       a conical defect / cosmic string (cone-unrolling cited).
  DV.3 the TOTAL over the twelve = 12*2 = 24 radits = 2*12 -- TWO full 2pi turns, the DOUBLE COVER
       (Gauss-Bonnet 4pi = 2*pi*chi, 21; the 2I spinor structure, 06).
  DV.4 (cosmic-string reading) POSTULATE; DV.5 (observable GR magnitude, danger zone) OWED -- no Lean.
  Mathlib-FREE, ZERO-axiom.
-/

import Container37.GeodesicMotion

namespace Container38
open Container37 Container36   -- deflection (37), angleDeficit (36) -- one home each, consumed here

/-! ### DV.1 -- the per-site deflection value (radits; pi/3 = 60deg at the twelve cited) -/

/-- The deflection around a degree-d vertex, in radits (37.GM.2 / 14.B.4): 2 at the twelve, 0 flat,
    -2 at a degree-7. (1 radit = pi/6, so 2 radits = pi/3 = 60 deg -- the radian value cites pi.) -/
theorem deflection_value :
    deflection 5 = 2 ∧ deflection 6 = 0 ∧ deflection 7 = -2 := by decide

/-! ### DV.2 -- the deflection is the FULL deficit (impact-parameter-independent, conical) -/

/-- The deflection equals the full angle deficit at the vertex -- no dependence on any impact parameter
    (the conical-defect / cosmic-string form). The cone-unrolling geometry is cited. -/
theorem deflection_is_full_deficit :
    deflection 5 = angleDeficit 5 ∧ deflection 6 = angleDeficit 6 ∧ deflection 7 = angleDeficit 7 := by decide

/-! ### DV.3 -- the total = 4*pi = the double cover -/

/-- The total deflection over the twelve degree-5 sites, in radits: 12 * 2 = 24. -/
def totalTwelve : Int := 12 * deflection 5
/-- 24 radits = 2 * 12 = TWO full 2*pi turns (12 radits = 2*pi) -- the double cover (= 4*pi,
    Gauss-Bonnet 2*pi*chi, container 21; the 2I spinor structure, container 06). -/
theorem total_is_double_cover : totalTwelve = 24 ∧ totalTwelve = 2 * 12 := by decide

#print axioms deflection_value
#print axioms deflection_is_full_deficit
#print axioms total_is_double_cover

end Container38
