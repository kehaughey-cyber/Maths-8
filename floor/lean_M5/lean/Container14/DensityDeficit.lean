/-
  CONTAINER 14 -- DENSITY DEFICIT: flat_ball - |B_r| = curvature. Rests on 13 and 03.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 2 of the physics-bridge arc, the R1 core. IMPORTS Container13 and reuses its ball-growth
  observable `ball`, `deg`, `verts` (14 rests on 13 -- the floor-up dependency in the kernel).
  Mathlib-FREE and ZERO-axiom by `decide`:

    B.1  the flat reference flat_ball(r) = 1 + 3r(r+1) = [1,7,19,37,61];
    B.3  the primordial law at r=1: flat_ball(1) - |B_1(v)| = 1 = tri(1) for every R1 vertex;
    B.4  the curvature charge: angle deficit (12 - 2*deg) = 2 per deg-5 vertex, sum 24 = 12*chi.

  The r>=2 primordial law and the ball-deficit-total conservation (B.5) span 162+ vertices and are
  checked by exact-integer computation in the derivation/model, not in the kernel.
-/

import Container13.ArchicDensity

set_option maxHeartbeats 1000000
set_option maxRecDepth 8000

namespace Container14
open Container13

/-! ### B.1 -- the flat reference flat_ball(r) = 1 + 3r(r+1) -/
def flatBall (r : Nat) : Nat := 1 + 3 * r * (r + 1)
/-- The r-th triangular number, the primordial-law closed form. -/
def tri (r : Nat) : Nat := r * (r + 1) / 2

theorem flat_ball_values :
    ((flatBall 0 == 1) && (flatBall 1 == 7) && (flatBall 2 == 19) &&
     (flatBall 3 == 37) && (flatBall 4 == 61)) = true := by decide

/-! ### B.4 -- the curvature charge: the angle deficit, summing to 12*chi -/
/-- Equilateral angle defect at a degree-d vertex: 2pi - d*(pi/3) = (12 - 2d) radits (12 = 2pi). -/
def angleDefect (v : Nat) : Nat := 12 - 2 * deg v
def angleCharge : Nat := (verts.map angleDefect).foldl (· + ·) 0

/-- On R1 every vertex is degree 5, so the angle defect is 2 radits at each of the twelve. -/
theorem angle_defect_two_per_vertex : (verts.all (fun v => angleDefect v == 2)) = true := by decide

/-- The total angle deficit is 24 = 12*chi (chi = 2) -- Gauss-Bonnet, the concentrated curvature. -/
theorem curvature_charge_is_twelve_chi :
    ((angleCharge == 24) && (24 == 12 * 2)) = true := by decide

/-! ### B.3 -- the primordial law at r=1: flat_ball(1) - |B_1(v)| = tri(1) -/
theorem primordial_law_r1 :
    (verts.all (fun v => flatBall 1 - ball 1 v == tri 1)) = true := by decide

#print axioms flat_ball_values
#print axioms angle_defect_two_per_vertex
#print axioms curvature_charge_is_twelve_chi
#print axioms primordial_law_r1

end Container14
