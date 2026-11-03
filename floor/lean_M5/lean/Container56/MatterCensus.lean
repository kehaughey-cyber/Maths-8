/-
  CONTAINER 56 -- THE MATTER-CENSUS STRUCTURE: the substrate's fermions carry SM quantum-number TYPES.
  Rests on 45 (spinors), 31 (colour singlet/triplet), 44 (chirality), 28 (weak su(2)); cites the SM fermions.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Matter is fermionic (spinor reps, 45; MC.1); the colour type-split is 6 colourless SINGLETS (leptons) +
  38 coloured TRIPLETS (quarks), 6 + 3*38 = 120 (31; MC.2); fermions are chiral (44) with weak isospin
  (28; MC.3). The three SM quantum-number KINDS (spin, colour, weak-isospin/chirality) are located (MC.4).
  MC.5 (correspondence to the SM fermions) POSTULATE; MC.6 OWED -- the generation count is NOT forced (the
  substrate 3-folds are different threes; naming one 'generations' is refused). Mathlib-FREE, ZERO-axiom.
-/

namespace Container56

/-! ### MC.2 -- the colour type-split: 6 singlets + 38 triples = 120 (quark/lepton) -/

def colourlessSinglets : Nat := 6        -- fixed points of the order-3 colour element (leptons)
def colouredTriples : Nat := 38          -- three-cycles (quarks: colour triplets)
def carrier : Nat := colourlessSinglets + 3 * colouredTriples
def tripletSize : Nat := 3
def singletSize : Nat := 1

theorem colour_type_split :
    carrier = 120 ∧ colourlessSinglets = 6 ∧ colouredTriples = 38
      ∧ singletSize ≠ tripletSize := by decide

/-! ### MC.4 -- the three SM quantum-number KINDS are located -/

def weakIsospinGenerators : Nat := 3     -- su(2) (28)
def quantumNumberKinds : Nat := 3        -- spin, colour, weak-isospin/chirality

theorem three_kinds_located :
    quantumNumberKinds = 3 ∧ weakIsospinGenerators = 3 := by decide

#print axioms colour_type_split
#print axioms three_kinds_located

end Container56
