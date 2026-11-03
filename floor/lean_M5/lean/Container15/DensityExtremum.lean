/-
  CONTAINER 15 -- DENSITY EXTREMUM: the two signed directions. Rests on 14, 13, 03.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 3 of the physics-bridge arc, the R1-checkable core. IMPORTS Container14 (15 rests on 14) and
  reuses its `flatBall`, `tri`, `angleCharge` (and transitively Container13's `verts`, `deg`).
  Mathlib-FREE and ZERO-axiom by `decide`:

    C.1  rho_min(r) = flat_ball(r) - tri(r) = [6,16,31,51] (the twelve), rho_max(r) = flat_ball(r) =
         [7,19,37,61] (the flat mirror), and rho_min < rho_max (a real gradient) for r = 1..4;
    C.2  one-sidedness: every R1 vertex has degree <= 6 (no hyperbolic vertex); the net angle deficit
         is 24 = 12*chi > 0 (Gauss-Bonnet, net positive) -- reusing Container14.

  The spatial extremum (rho_min at the twelve, rho_max at the flat sites) is exhibited on R4 and is
  exact-integer in the derivation/model. C.3 is a POSTULATE (a named possibility), no Lean.
-/

import Container14.DensityDeficit

set_option maxHeartbeats 1000000
set_option maxRecDepth 8000

namespace Container15
open Container13 Container14

/-! ### C.1 -- the density extrema: rho_min at the twelve, rho_max at the flat mirror -/
/-- Minimum archic density at radius r: the twelve, flat_ball(r) - tri(r). -/
def rhoMin (r : Nat) : Nat := flatBall r - tri r
/-- Maximum archic density on this substrate: the flat mirror value flat_ball(r). -/
def rhoMax (r : Nat) : Nat := flatBall r

theorem density_extrema_values :
    ((rhoMin 1 == 6) && (rhoMin 2 == 16) && (rhoMin 3 == 31) && (rhoMin 4 == 51) &&
     (rhoMax 1 == 7) && (rhoMax 2 == 19) && (rhoMax 3 == 37) && (rhoMax 4 == 61)) = true := by decide

/-- The density gradient is real: the minimum (the twelve) is strictly below the flat maximum. -/
theorem minimum_below_flat_gradient :
    rhoMin 1 < rhoMax 1 ∧ rhoMin 2 < rhoMax 2 ∧ rhoMin 3 < rhoMax 3 ∧ rhoMin 4 < rhoMax 4 := by decide

/-! ### C.2 -- one-sidedness: net positive curvature, no hyperbolic vertex (R1) -/
/-- Gauss-Bonnet: the total angle deficit is 24 = 12*chi, strictly positive -- net positive curvature. -/
theorem net_curvature_positive : angleCharge = 24 ∧ 0 < 12 * 2 := by decide

/-- No hyperbolic vertex on R1: every vertex has degree <= 6 (the substrate is the positive side). -/
theorem no_hyperbolic_vertex_R1 : ∀ v ∈ verts, deg v ≤ 6 := by decide

#print axioms density_extrema_values
#print axioms minimum_below_flat_gradient
#print axioms net_curvature_positive
#print axioms no_hyperbolic_vertex_R1

end Container15
