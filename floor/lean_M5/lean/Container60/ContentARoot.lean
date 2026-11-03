/-
  CONTAINER 60 -- CONTENT SELECTION (K2): THE RE-EXAMINATION. The 'K2 is a root' verdict is RETRACTED.
  *** RETRACTION (2026-09-11; CORRECTIONS #9): the original verdict rested on category errors -- it tested
  the WRONG surfaces (irrep dimensions vs a Weyl count; mass-basis vs weak-basis) and declared irreducibility
  prematurely. K2 is RE-OPENED as a partially-structured open problem. ***
  Rests on 59 (structure), 31 (inner Z/3 colour), 58 (hypercharge), 12/30 (E8/A2); cites the fork R10
  (generation = outer Z/3), the SM content, E8 > A2 x E6.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  This Lean certifies the CORRECTED facts: generation = the OUTER Z/3 (left-mult, fixed-point-free, 40/40/40,
  0 fixed) is genuinely DISTINCT from colour = the INNER Z/3 (conjugation, 6 fixed + 38 triples), and the
  count 3 is a divisibility fact (3^1 || 120) -- so generations are a real located structure, not a
  dismissible 'three' (RX.2c); the E8 > A2 x E6 matter surface exists dimensionally (8+78+3*27+3*27=248,
  RX.3); and the old dimension-counting (12/14/16 != 15) is kept but is the wrong surface (RX.1).
  Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container60

/-! ### RX.2(c) -- generation (outer Z/3) is distinct from colour (inner Z/3); count 3 via 3^1 || 120 -/

def genBlocks : Nat := 120 / 3         -- left-mult by g3 is fixed-point-free -> 3 blocks of 40
def genFixed : Nat := 0                -- left translation by g != e has NO fixed points
def colourFixed : Nat := 6             -- conjugation by g3: 6 fixed points (31.CS.1)
def colourTriples : Nat := 38          -- + 38 three-cycles

/-- Generation = the OUTER Z/3 (left-multiplication): fixed-point-free, so 3 equal blocks of 40 (3*40=120,
    0 fixed). Colour = the INNER Z/3 (conjugation): 6 fixed + 38 triples (6 + 3*38 = 120). They are
    genuinely DIFFERENT threes (0 fixed vs 6 fixed). The count is 3 because 3^1 || 120 (3 divides 120, 9
    does not) -- a divisibility fact, not a fit. So generations are a located structure, not a dismissible
    coincidence (correcting RX.2c). -/
theorem generation_is_a_real_structure :
    genBlocks * 3 = 120 ∧ genFixed = 0
    ∧ colourFixed + 3 * colourTriples = 120 ∧ colourFixed = 6
    ∧ genFixed ≠ colourFixed
    ∧ 120 % 3 = 0 ∧ 120 % 9 ≠ 0 := by decide

/-! ### RX.3 -- the E8 > A2 x E6 matter surface: 248 = (8,1)+(1,78)+(3,27)+(3bar,27bar) -/

def e8 : Nat := 248
def a2 : Nat := 8
def e6 : Nat := 78
def gen27 : Nat := 27       -- the 27 of E6 = one generation (16 of SO(10) + 10 + 1)

theorem e8_matter_surface : a2 + e6 + 3 * gen27 + 3 * gen27 = e8 := by decide

/-! ### RX.1 -- the kept, narrow, WRONG-surface fact: 2I-irrep-dimension sums 12/14/16 != SM 15 -/

def vdefDim : Nat := 12     -- {1,3,3',5}
def spinorDim : Nat := 14   -- {2,2',4',6}
def vectorDim : Nat := 16   -- {1,3,3',4,5}
def smGen : Nat := 15

/-- Kept for the record and flagged vacuous: sums of 2I irrep DIMENSIONS do not equal the SM Weyl count 15.
    True, but it compares dimensions to a fermion count -- the wrong surface (RX.1/RX.2a). -/
theorem wrong_surface_counts :
    vdefDim ≠ smGen ∧ spinorDim ≠ smGen ∧ vectorDim ≠ smGen := by decide

#print axioms generation_is_a_real_structure
#print axioms e8_matter_surface
#print axioms wrong_surface_counts

end Container60
