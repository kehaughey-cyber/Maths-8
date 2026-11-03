/-
  CONTAINER 16 -- FRUSTRATION DYNAMO: the deficit never closes. Rests on 08, 03; cf 14.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 4 of the physics-bridge arc, the integer core. Mathlib-FREE and ZERO-axiom by `decide`.
  The tetrahedral gap eps = 2pi - 5*arccos(1/3) = 2pi - 10*arcsin(sqrt3/3) ~ 7.356 deg is STRICTLY
  positive, and that reduces EXACTLY to an integer inequality:

    eps > 0  <=>  arccos(1/3) < 2pi/5  <=>  1/3 > cos(2pi/5) = (sqrt5 - 1)/4
             <=>  3*sqrt5 < 7  <=>  (3 sqrt5)^2 < 7^2  <=>  45 < 49.

  The trig identities need R and are CITED (as container 10 cites arcsin(1/2) = pi/6). The kernel
  proves the reduced core 45 < 49 (45 = (3 sqrt5)^2 = 9*5, 49 = 7^2), which certifies 3*sqrt5 < 7,
  hence eps > 0. D.3 (the dynamo reading) is a POSTULATE -- no Lean.
-/

namespace Container16

/-! ### D.1 -- the tetrahedral gap is strictly positive, via the integer core 45 < 49 -/

/-- The squared forms: 45 = (3*sqrt5)^2 = 9*5, and 49 = 7^2. -/
theorem squared_core : ((3 * 3 * 5 == 45) && (7 * 7 == 49)) = true := by decide

/-- The reduced integer core: 45 < 49. Since 45 = (3 sqrt5)^2 and 49 = 7^2 (both sides positive),
    this certifies 3*sqrt5 < 7, i.e. cos(2pi/5) = (sqrt5-1)/4 < 1/3, i.e. arccos(1/3) < 2pi/5, i.e.
    five tetrahedra around an edge span < 2pi -- the gap eps = 2pi - 5*arccos(1/3) is STRICTLY > 0. -/
theorem frustration_strictly_positive : 45 < 49 := by decide

/-- Equivalent Bool form of the core, for the model's guard. -/
theorem frustration_core_bool : (Nat.blt 45 49) = true := by decide

#print axioms squared_core
#print axioms frustration_strictly_positive
#print axioms frustration_core_bool

end Container16
