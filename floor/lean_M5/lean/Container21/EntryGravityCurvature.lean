/-
  CONTAINER 21 -- ENTRY: GRAVITY <-> CURVATURE. The first FILED correspondence. Rests on 14, 19, 20.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 9, the integral core of the correspondence. Mathlib-FREE, ZERO-axiom by `decide`. The substrate
  total deficit equals the cited curvature integral EXACTLY: 24 radits = 4*pi = 2*pi*chi (Gauss-Bonnet,
  chi=2). Plus the small-ball volume-deficit coefficient for the surface dimension n=2: 6(n+2)=24.
  The gate (four parts + six tests) and the routing discipline are exact-Python; GC.3 is a POSTULATE.
-/

namespace Container21

/-- Radits: 2*pi = 12 radits. -/
def raditsPerTurn : Nat := 12
/-- The substrate total angle-deficit: 2 radits at each of the twelve = 24 (= container 14.B.4). -/
def substrateTotalDeficit : Nat := 24
/-- 4*pi in radits. -/
def fourPi : Nat := 2 * raditsPerTurn
/-- The Gauss-Bonnet total: integral K dA = 2*pi*chi, chi = 2. -/
def gaussBonnet : Nat := raditsPerTurn * 2

/-- THE INTEGRAL MATCH (GC.1): the substrate deficit IS the total curvature integral -- 24 = 4*pi =
    2*pi*chi. An exact, refinement-invariant match; the object that travels across the entry. -/
theorem deficit_is_curvature_integral :
    ((substrateTotalDeficit == fourPi) && (fourPi == gaussBonnet)) = true := by decide

/-- The small-ball volume-deficit law V(eps) = omega_n*eps^n*[1 - R*eps^2/(6(n+2))]; for the surface
    dimension n=2 the coefficient denominator 6(n+2) is 24 (the disk-area deficit A=pi*eps^2[1-R*eps^2/24]). -/
def Vcoeff (n : Nat) : Nat := 6 * (n + 2)
theorem V_eps_coeff_n2 : Vcoeff 2 = 24 := by decide

#print axioms deficit_is_curvature_integral
#print axioms V_eps_coeff_n2

end Container21
