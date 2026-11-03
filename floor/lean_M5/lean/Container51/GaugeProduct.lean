/-
  CONTAINER 51 -- THE SM GAUGE PRODUCT: U(1) x SU(2) x SU(3) as electroweak(2I) x strong(E8).
  Rests on 28 (su(2)), 29 (u(1)), 30 (su(3)=A2 subset E8), 31 (colour Z/3 native); cites the SM gauge group.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The located gauge dimensions u(1)=1, su(2)=3, su(3)=8 sum to 1+3+8=12 (GP.1). They form the product
  U(1)xSU(2)xSU(3) -- electroweak(2I) x strong(E8/A2) (GP.2). CAVEAT (31): 1+3+8=12 NUMERICALLY, but 8 does
  NOT divide the vertex-stabilizer order 10, so NOT a forced decomposition of the geometric twelve (GP.3).
  GP.4 (joint, deferred to fork) POSTULATE; GP.5 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container51

def u1Dim : Nat := 1
def su2Dim : Nat := 3
def su3Dim : Nat := 8
def total : Nat := u1Dim + su2Dim + su3Dim
def vertexStab : Nat := 10          -- the 2I-stabilizer of a vertex (order 10)

/-! ### GP.1 -- the located gauge dimensions sum to 12 -/

theorem gauge_dimensions : u1Dim = 1 ∧ su2Dim = 3 ∧ su3Dim = 8 ∧ total = 12 := by decide

/-! ### GP.3 -- the caveat: 1+3+8=12 numerically, but 8 does not divide 10 (not a forced decomposition) -/

/-- 1+3+8 = 12 equals the geometric twelve numerically, BUT an 8-orbit would need 8 | (vertex-stabilizer
    order 10), and 8 does NOT divide 10 -- so the twelve do NOT split 1+3+8 as a symmetry decomposition
    (31). The coincidence is flagged, not banked. -/
theorem not_a_forced_decomposition :
    total = 12 ∧ ¬ (vertexStab % su3Dim = 0) := by decide

#print axioms gauge_dimensions
#print axioms not_a_forced_decomposition

end Container51
