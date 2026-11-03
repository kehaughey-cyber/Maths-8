/-
  CONTAINER 61 -- THE K2 SURFACE TEST: do the right surfaces FORCE the SM content? (answer: no)
  Rests on 60 (the re-examination), 12/30 (E8/A2), 31 (Weyl-transitivity), 58 (hypercharge); cites the
  E8 = A2 x E6 branching, E6 = SO(10) x U(1), the SM generation, the fork R10.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Surface A (E8 = A2 x E6): 248 = 8+78+3*27+3*27, 240 = 6+72+162, 27 = 16+10+1, (3,27) = 3 generations
  (ST.1) -- BUT generic to every E8 theory, the A2 Weyl-arbitrary (31), exotics unprojected -> a filed
  LEAD, not a forcing (ST.2). Surface B (regular rep C[2I], dim = sum d_i^2 = 120): the outer-Z/3
  generation gives 3 blocks of 40 (3^1||120, substrate-specific count 3, ST.3) -- BUT a block (40) != one
  SM generation (15/16) and no principle selects the fermions (ST.4). VERDICT: K2 OPEN -- content unforced
  by either surface; count 3 near-forced via generation = the outer Z/3 (ST.5, POSTULATE). This Lean
  certifies the cold bookkeeping. Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container61

/-! ### ST.1 -- Surface A: the E8 = A2 x E6 branching bookkeeping -/

def e8 : Nat := 248
def branchDims : Nat := 8 + 78 + 3*27 + 3*27         -- (8,1)+(1,78)+(3,27)+(3bar,27bar)
def e8Roots : Nat := 240
def branchRoots : Nat := 6 + 72 + 162                -- A2 + E6 + ((3,27)+(3bar,27bar))
def e6_27 : Nat := 16 + 10 + 1                        -- 27 of E6 = 16+10+1 of SO(10); 16 = one generation

theorem e8_branching :
    branchDims = e8 ∧ branchRoots = e8Roots ∧ e6_27 = 27 := by decide

/-! ### ST.3 -- Surface B: the regular rep, and the substrate-specific generation count 3 -/

def regDim : Nat := 1*1 + 2*2 + 2*2 + 3*3 + 3*3 + 4*4 + 4*4 + 5*5 + 6*6   -- sum d_i^2 = 120
def genBlock : Nat := regDim / 3                       -- 40 (outer Z/3 fixed-point-free -> 3 blocks)

/-- The regular rep has dim 120; the outer-Z/3 generation grading gives 3 equal blocks of 40 (3*40=120);
    and 3^1 || 120 (3 divides 120, 9 does not) forbids enlargement to Z/9 -- so the count is exactly 3, a
    property of |2I| = 120, not generic-E8. -/
theorem generation_count_three :
    regDim = 120 ∧ genBlock = 40 ∧ genBlock * 3 = 120 ∧ 120 % 3 = 0 ∧ 120 % 9 ≠ 0 := by decide

/-! ### ST.4 -- Surface B does not force the content: a block is not one SM generation -/

def smGen : Nat := 15        -- one SM generation (Weyl fermions)
def smNuR : Nat := 16        -- with a right-handed neutrino

/-- A generation block (40 states) is neither the SM generation 15 nor 16 (with nu_R): the block is larger
    than one generation's fermion content, and no substrate rule selects the fermions within it. -/
theorem block_not_a_generation : genBlock ≠ smGen ∧ genBlock ≠ smNuR := by decide

#print axioms e8_branching
#print axioms generation_count_three
#print axioms block_not_a_generation

end Container61
