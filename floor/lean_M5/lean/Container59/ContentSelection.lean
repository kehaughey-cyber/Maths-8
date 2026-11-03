/-
  CONTAINER 59 -- CONTENT SELECTION (K2): is the fermion multiplet content FORCED?
  Rests on 45 (central -1), 58 (w/t gradings), 31 (colour), 09/11 (the twelve), 56 (census); cites the fork
  R25/R26, the SL(2,5)/A5 irreps, the SM generation.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The substrate FORCES the matter STRUCTURE: 2I's 9 irreps (sum dim^2 = 120), the central-character split
  A5 {1,3,3',4,5} / spinor {2,2',4',6} (each 60, KS.1); the matter lattice = the 12-vertex conjugation rep
  1+3+3'+5 (dim 12, KS.2); the mass spectrum 12/d over {1,3,3',5} = {12,4,4,0} (KS.4). It does NOT force the
  CONTENT MAP (KS.3, scoped negative): the SM generation is 15 (16 with nu_R), but the natural content sizes
  are 12 / 14 / 16 -- NONE is 15, so which irreps are the fermions is under-determined (the fork's own
  COMPARISON). The 16=16-with-nu_R coincidence is a noticing, NOT banked. Consequence (KS.4, POSTULATE): the
  absolute hypercharges (58) and the fork's mass numbers rest on this un-forced map. This Lean certifies the
  cold counting. Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container59

/-! ### KS.1 -- 2I's 9 irreps: sum dim^2 = 120; the central-character split is 60 / 60 -/

def sumDim2All : Nat := 1*1 + 2*2 + 2*2 + 3*3 + 3*3 + 4*4 + 4*4 + 5*5 + 6*6   -- all 9 irreps
def sumDim2A5  : Nat := 1*1 + 3*3 + 3*3 + 4*4 + 5*5                            -- {1,3,3',4,5}
def sumDim2Spin: Nat := 2*2 + 2*2 + 4*4 + 6*6                                  -- {2,2',4',6}

theorem irrep_split : sumDim2All = 120 ∧ sumDim2A5 = 60 ∧ sumDim2Spin = 60 := by decide

/-! ### KS.2/KS.3 -- the natural content sizes 12 / 14 / 16, and the SM generation 15 -/

def matterDim : Nat := 1 + 3 + 3 + 5          -- matter lattice {1,3,3',5}  (12-vertex rep)
def spinorDim : Nat := 2 + 2 + 4 + 6          -- spinor set {2,2',4',6}
def vectorDim : Nat := 1 + 3 + 3 + 4 + 5      -- vector set {1,3,3',4,5}
def smGen     : Nat := 6 + 3 + 3 + 2 + 1      -- SM chiral generation Q,u_c,d_c,L,e_c
def smWithNuR : Nat := smGen + 1              -- with a right-handed neutrino

/-- The substrate's natural matter-content sizes are 12, 14, 16; the SM chiral generation is 15 (16 with
    nu_R). NONE of the natural sizes equals 15 -- the content selection is not fixed by counting. The only
    coincidence, vectorDim = smWithNuR = 16, needs nu_R and does not respect SU(3)xSU(2) structure (a
    noticing, not banked). -/
theorem count_mismatch :
    matterDim = 12 ∧ spinorDim = 14 ∧ vectorDim = 16 ∧ smGen = 15
    ∧ matterDim ≠ smGen ∧ spinorDim ≠ smGen ∧ vectorDim ≠ smGen
    ∧ vectorDim = smWithNuR := by decide

/-! ### KS.4 -- the mass-law spectrum 12/d over {1,3,3',5} = {12,4,4,0} (5 does not divide 12) -/

def massOf (d : Nat) : Nat := if 12 % d = 0 then 12 / d else 0   -- % avoids Dvd (keeps it propext-free)

theorem mass_spectrum :
    massOf 1 = 12 ∧ massOf 3 = 4 ∧ massOf 5 = 0 ∧ 12 % 5 ≠ 0 := by decide

#print axioms irrep_split
#print axioms count_mismatch
#print axioms mass_spectrum

end Container59
