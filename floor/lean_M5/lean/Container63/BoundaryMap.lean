/-
  CONTAINER 63 -- THE NATIVE / HAND-OFF / OPEN BOUNDARY MAP for the SM sector.
  Rests on 58 (native ℤ/6 grading), 62 (embedding-distinction), 57 (θ_W / abelian-scaleless), 12 (E8 roots);
  cites the E8 GUT chains, SU(5) hypercharge, the McKay correspondence, and fork F13/F14/F15.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  NATIVE VALUE: the SM group from two native gradings (BM.1, cf 58); the count 3 (61); the native
  hypercharge normalization -> θ_W ≠ GUT 3/8 (BM.3, a testable divergence, U(1)_Y abelian/scaleless, 57);
  the mass law {12,4,4,0} (F15); levels-from-structure-by-anomaly (BM.4). HAND-OFF: the E8-GUT embedding
  reproduces SM Y via the SAME GUT SU(5) with sin²θ_W=3/8, selecting nothing (BM.2, generic; 62). OPEN
  INPUT: the content map, STRUCTURAL -- the spinor matter is an su(2)_L spin-tower {1/2,1/2,3/2,5/2}=14, not
  SM doublet content (14≠8≠15) (BM.4). This Lean certifies the cold bookkeeping. Mathlib-FREE, ZERO-axiom.
-/

namespace Container63

/-! ### BM.2 -- hand-off: the GUT normalization sin²θ_W = 3/8 -/

def trT3sq_x3 : Nat := 3 * 2      -- 3 * Tr(T3^2),  Tr(T3^2) = 2 over a generation
def trQsq_x3  : Nat := 16          -- 3 * Tr(Q^2),   Tr(Q^2) = 16/3 over a generation

/-- Over one generation, sin²θ_W = Tr(T3²)/Tr(Q²) = 2/(16/3) = 6/16 = 3/8 -- the classic SU(5)/GUT value,
    shared by every E8 chain (all factor through the same GUT SU(5)). Certified as 6·8 = 16·3 (=48). -/
theorem sin2_thetaW_is_three_eighths : trT3sq_x3 * 8 = trQsq_x3 * 3 := by decide

/-! ### BM.4 -- open input: the central-character split, the spin-tower, and the structural gap -/

def vecSumSq : Nat := 1*1 + 3*3 + 3*3 + 4*4 + 5*5      -- vector {1,3,3',4,5}  = 60
def spinSumSq : Nat := 2*2 + 2*2 + 4*4 + 6*6            -- spinor {2,2',4',6}   = 60
def spinDim : Nat := 2 + 2 + 4 + 6                       -- spinor total states  = 14
def smDoubletStates : Nat := 3*2 + 1*2                   -- SM doublets Q(3,2)+L(1,2) = 8
def smGeneration : Nat := 15                             -- one chiral generation (Weyl)

/-- The substrate's matter splits by central character into two Σd²=60 halves (vector + spinor = 120), and
    the spinor set has 14 states -- neither the SM doublet content (8) nor a generation (15). The content
    map is unforced and the gap is structural. -/
theorem split_and_structural_gap :
    vecSumSq = 60 ∧ spinSumSq = 60 ∧ vecSumSq + spinSumSq = 120 ∧
    spinDim = 14 ∧ spinDim ≠ smDoubletStates ∧ spinDim ≠ smGeneration := by decide

/-! ### BM.4 -- the su(2)_L spin-tower: McKay principal dims = 2j+1; the spinor members at odd 2j -/

def dimAtSpin (twoJ : Nat) : Nat := twoJ + 1            -- dim V_j = 2j+1 (McKay principal series)

/-- The principal McKay series has dims 2j+1 for 2j=0..5 (= irreps 1,2,3,4',5,6); the spinor members sit at
    ODD 2j -- 2 (2j=1), 4' (2j=3), 6 (2j=5) -- so 4' is the irreducible spin-3/2 (dim 4), which does NOT
    split as 2+2 (Q12). The spinor set is a spin-tower, not weak doublets. -/
theorem spin_tower :
    dimAtSpin 0 = 1 ∧ dimAtSpin 1 = 2 ∧ dimAtSpin 2 = 3 ∧
    dimAtSpin 3 = 4 ∧ dimAtSpin 4 = 5 ∧ dimAtSpin 5 = 6 ∧
    dimAtSpin 1 = 2 ∧ dimAtSpin 3 = 4 ∧ dimAtSpin 5 = 6 := by decide

#print axioms sin2_thetaW_is_three_eighths
#print axioms split_and_structural_gap
#print axioms spin_tower

end Container63
