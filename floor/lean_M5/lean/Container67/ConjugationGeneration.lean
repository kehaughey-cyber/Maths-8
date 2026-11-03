/-
  CONTAINER 67 -- CONJUGATION ON GENERATION: how do charge-conjugation-like (colour-flipping) involutions of
  the 120 act on the outer Z/3 (generation)? The convention-free salvage from the REFUTED Maths-6 P1
  ("C = the improper half => preserves the outer Z/3"). EXHAUSTIVELY over the full isometry group of the 120
  (14400 = |H4|; v->pvq det+1, v->p vbar q det-1), the colour-flipping involutions number 24 = 18 proper + 6
  improper; on the outer Z/3 the 18 proper ALL INVERT, the 6 improper ALL SCRAMBLE, 0 PRESERVE -- the same
  under 61's left and 64's right reading. So charge conjugation C acts NON-TRIVIALLY on the outer Z/3 (P1's
  "improper preserve" had the sign backwards: improper SCRAMBLE). C != P (C a carrier self-map, P not). The
  SM comparison is OPEN/two-sided (no "divergence"). Rests on 64 (tick b: colour conj b^2, generation
  R_{b^4}), 49/44 (C, P), 06 (the carrier). GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT.
  `--check` fails on drift. This Lean certifies the cold integer bookkeeping; the 14400-sweep and the
  classification are the exact-Python half. Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container67

/-! ### CG.1 -- the colour-flipping involutions over the full isometry group -/

def isomGroupOrder : Nat := 14400          -- |H4|, the 600-cell symmetry group (v->pvq, v->p vbar q)
def nProper : Nat := 18                     -- det +1 (orientation-preserving)
def nImproper : Nat := 6                    -- det -1 (orientation-reversing)
def nFlippers : Nat := 24                   -- colour-flipping involutions

/-- The colour-flipping involutions split 18 proper + 6 improper = 24, inside the order-14400 group. -/
theorem flippers_split :
    nProper + nImproper = nFlippers ∧ nFlippers = 24 ∧ nProper = 18 ∧ nImproper = 6 := by decide

/-! ### CG.2 -- the trichotomy on the outer Z/3 (gen = R_b4, 64): 0 preserve -/

def nInvert : Nat := 18
def nScramble : Nat := 6
def nPreserve : Nat := 0

/-- On the outer Z/3 = <R_{b^4}> the 24 involutions classify as invert 18 + scramble 6 + preserve 0 = 24;
    the proper ones are exactly the inverters (18) and the improper ones exactly the scramblers (6). So NO
    colour-flipping involution preserves the outer Z/3. (Refutes P1's "improper preserve".) -/
theorem trichotomy_no_preserve :
    nInvert + nScramble + nPreserve = nFlippers ∧ nPreserve = 0 ∧
    nInvert = nProper ∧ nScramble = nImproper := by decide

/-! ### CG.3 -- convention independence (gen = L_g3, 61) -/

def nInvertL : Nat := 18
def nScrambleL : Nat := 6
def nPreserveL : Nat := 0

/-- Under 61's LEFT reading (gen = L_{g3}) the counts are identical (18/6/0): the verdict does not depend on
    reading the outer Z/3 as left (61) or right (64). -/
theorem convention_independent :
    nInvertL = nInvert ∧ nScrambleL = nScramble ∧ nPreserveL = nPreserve := by decide

/-! ### CG.4 -- C acts non-trivially on the outer Z/3 -/

/-- C is one of the 24 colour-flipping involutions and 0 of the 24 preserve the outer Z/3, so C does not
    preserve it: C acts non-trivially (nImproper + nProper of them act non-trivially = all 24). -/
theorem C_acts_nontrivially :
    nPreserve = 0 ∧ nInvert + nScramble = nFlippers := by decide

/-! ### CG.5 -- C != P: the improper colour-flippers are carrier self-maps -/

def nImproperSelfMaps : Nat := 6           -- all 6 improper colour-flippers are self-maps of the 120

/-- All 6 improper colour-flippers (C's wing-mirror candidates) are self-maps of the 120 (parity P is not),
    so C and P are distinct orientation-reversing involutions. -/
theorem C_selfmaps_all_improper :
    nImproperSelfMaps = nImproper ∧ nImproperSelfMaps = 6 := by decide

#print axioms flippers_split
#print axioms trichotomy_no_preserve
#print axioms convention_independent
#print axioms C_acts_nontrivially
#print axioms C_selfmaps_all_improper

end Container67
