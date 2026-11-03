/-
  CONTAINER 25 -- DIMENSION FORCING: intrinsic n=2 forced, ambient 3 owed. Rests on 13, 14, 03.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The counting law forces the INTRINSIC dimension n=2 (the ball-growth polynomial degree): container
  14's flat reference flat_ball(r)=1+3r(r+1) is DEGREE 2 -- second difference the nonzero constant 6,
  third difference 0 -- and the ring (shell) count is linear (6 per step), the signature of a 2-D
  space. A 1-D line 2r+1 is degree 1 (second difference 0), so the substrate is NOT 1-D; the vanishing
  third difference rules out degree 3. The curvature coefficient 6(n+2)=24 at n=2 (DF.2) equals the
  Gauss-Bonnet total 12*chi=24 (container 14's angleCharge) ONLY for the sphere (chi=2): with n fixed
  at 2 it fails for chi != 2, so that equality is a COINCIDENCE, not a forced identity.

  IMPORTS Container14: reuses flatBall and angleCharge -- one home, consumed. Mathlib-FREE, ZERO-axiom.
  The AMBIENT dimension 3 (container 03's metric no-thirteenth, 3.7) is OWED -- no kernel content.
-/

import Container14.DensityDeficit

namespace Container25
open Container14   -- flatBall, angleCharge -- one home, consumed here

/-! ### DF.1 -- the counting law forces the intrinsic dimension n=2 (flat_ball is degree 2) -/

/-- Second difference constant 6: flat_ball(r+2) - 2 flat_ball(r+1) + flat_ball(r) = 6, written
    additively (no Nat subtraction) -- the hallmark of a DEGREE-2 polynomial. -/
theorem flat_ball_second_diff_const :
    ([0, 1, 2, 3, 4, 5].all (fun r =>
      flatBall (r + 2) + flatBall r == 2 * flatBall (r + 1) + 6)) = true := by decide

/-- Third difference 0: flat_ball(r+3) - 3 flat_ball(r+2) + 3 flat_ball(r+1) - flat_ball(r) = 0
    (additively) -- so the degree is EXACTLY 2 (not 3). -/
theorem flat_ball_third_diff_zero :
    ([0, 1, 2, 3, 4, 5].all (fun r =>
      flatBall (r + 3) + 3 * flatBall (r + 1) == 3 * flatBall (r + 2) + flatBall r)) = true := by decide

/-- The ring (shell) count is LINEAR: flat_ball(r+1) = flat_ball(r) + 6(r+1), i.e. the shell grows by
    6 per step (6r). A shell grows as r^(d-1), so linear => d-1 = 1 => intrinsic dimension d = 2. -/
theorem ring_is_linear :
    ([0, 1, 2, 3, 4, 5, 6].all (fun r =>
      flatBall (r + 1) == flatBall r + 6 * (r + 1))) = true := by decide

/-- CONTRAST: a 1-D lattice ball 2r+1 has second difference 0 (degree 1), so the substrate is NOT 1-D. -/
def line1d (r : Nat) : Nat := 2 * r + 1
theorem line_is_degree1 :
    ([0, 1, 2, 3, 4, 5].all (fun r => line1d (r + 2) + line1d r == 2 * line1d (r + 1))) = true := by
  decide

/-! ### DF.2 -- the coefficient 6(n+2)=24 forced at n=2; =12*chi a sphere coincidence -/

/-- The curvature coefficient 6(n+2) in V(eps)=w_n eps^n [1 - R eps^2 / (6(n+2))] (container 21). -/
def coeff (n : Nat) : Nat := 6 * (n + 2)

/-- At the forced intrinsic dimension n=2, the coefficient is 24. -/
theorem coeff_at_n2 : (coeff 2 == 24) = true := by decide

/-- It equals the substrate's MEASURED Gauss-Bonnet total angle charge (container 14, angleCharge=24). -/
theorem coeff_eq_measured_gauss_bonnet : (coeff 2 == angleCharge) = true := by decide

/-- ...but 6(n+2)=12*chi holds ONLY for the sphere (chi=2): with n fixed at 2 it fails for chi=1 and
    chi=0 (the torus). So the equality is a SPHERE COINCIDENCE, not a forced identity. -/
theorem coeff_eq_gb_only_sphere :
    ((coeff 2 == 12 * 2) && !(coeff 2 == 12 * 1) && !(coeff 2 == 12 * 0)) = true := by decide

#print axioms flat_ball_second_diff_const
#print axioms flat_ball_third_diff_zero
#print axioms ring_is_linear
#print axioms line_is_degree1
#print axioms coeff_at_n2
#print axioms coeff_eq_measured_gauss_bonnet
#print axioms coeff_eq_gb_only_sphere

end Container25
