/-
  CONTAINER 05 -- THE GEOMETRIC-BALANCE BRIDGE / rung 5 (equidistant dimension)

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  THE BRIDGE (POSTULATE, not here): registrations CORRESPOND to points in real Euclidean
  space, mutually-adjacent ones at separation 2. What the bridge buys -- rung 5 -- is that N
  equidistant points are AFFINELY INDEPENDENT, forcing dim >= N-1. Mathlib-FREE: the whole
  content is that the GRAM determinant of an equidistant config is NONZERO (polarization:
  Gram = (D/2)(I+J), det = N*(D/2)^(N-1)). The kernel decides that by exact integer
  arithmetic. The step nonzero-det => independent => dim >= N-1 is standard linear algebra
  (maths 4's Mathlib THEOREM, cited); the general all-N port is OWED.
-/

namespace Container05

/-! ### exact integer determinants (2x2 and 3x3) -- no Mathlib -/

def det2 (a b c d : Int) : Int := a * d - b * c

def det3 (a b c d e f g h i : Int) : Int :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

/-! ### det(I + J)_{N-1} = N -- the eigenvalue-N fact, scaled away from D -- step 5.3 -/

/-- N = 2: I+J on R^1 is [[2]], det 2. -/
theorem det_IplusJ_1 : (2 : Int) = 2 := rfl
/-- N = 3: I+J on R^2 is [[2,1],[1,2]], det 3. -/
theorem det_IplusJ_2 : det2 2 1 1 2 = 3 := by decide
/-- N = 4: I+J on R^3 is [[2,1,1],[1,2,1],[1,1,2]], det 4. -/
theorem det_IplusJ_3 : det3 2 1 1 1 2 1 1 1 2 = 4 := by decide

/-! ### the Gram determinants are NONZERO -- affine independence -- step 5.4 -/

/-- The three equidistant witnesses are affinely independent: their Gram determinants are
    nonzero. This is the whole computational content of 'dim >= N-1'. -/
theorem two_points_indep   : (2 : Int) ≠ 0 := by decide
theorem triangle_indep     : det2 2 1 1 2 ≠ 0 := by decide
theorem tetrahedron_indep  : det3 2 1 1 1 2 1 1 1 2 ≠ 0 := by decide

/-- The concrete configs, at their actual scales: the equilateral triangle (D=2, Gram det 3)
    and the regular tetrahedron (D=8, Gram det 256) -- both nonzero, exactly. -/
theorem triangle_gram_det    : det2 2 1 1 2 = 3 := by decide
theorem tetrahedron_gram_det : det3 8 4 4 4 8 4 4 4 8 = 256 := by decide
theorem tetrahedron_gram_nz  : det3 8 4 4 4 8 4 4 4 8 ≠ 0 := by decide

-- DIMENSION BOUND (step 5.4): a nonzero Gram => the N-1 difference vectors are linearly
-- independent => the N equidistant points are affinely independent => ambient dim >= N-1.
-- Concretely 2 -> d>=1 (line), 3 -> d>=2 (plane), 4 -> d>=3 (volume): the tetrahedron is
-- genuinely 3-dimensional (the retracted RUNG3-TETRAHEDRON-MINIMUM, now derived). The
-- implication itself is standard linear algebra -- maths 4's Mathlib THEOREM
-- RUNG5-EQUIDISTANT-DIMENSION; the kernel here proves its computational heart (nonzero det).
--
-- POSTULATE (5.1, 5.5): the bridge -- registrations CORRESPOND to Euclidean points at
-- separation 2 (an equivalence, not an identity; not Hilbert). Added, not derived.
--
-- OWED (5.6): the general all-N statement in Maths 5's own kernel (a Mathlib port; Maths 5
-- has no Mathlib built), and METRIC dynamics -- now UNLOCKED by this bridge (container 07's
-- 7.6): velocity as distance/time on the Euclidean image.

#print axioms det_IplusJ_2
#print axioms det_IplusJ_3
#print axioms triangle_indep
#print axioms tetrahedron_indep
#print axioms tetrahedron_gram_det

end Container05
