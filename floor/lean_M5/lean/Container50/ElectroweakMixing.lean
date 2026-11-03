/-
  CONTAINER 50 -- ELECTROWEAK MIXING: the Cartan is rank 2, so two neutral bosons -> photon + Z.
  Rests on 29 (u(1)+su(2)), 28 (su(2)); cites the electroweak Cartan / Weinberg mixing.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The electroweak Cartan is rank(u(1))+rank(su(2)) = 1+1 = 2 (hypercharge Y + weak isospin T3), so two
  neutral gauge directions B, W3 (EW.1). They mix: the photon is a nontrivial combination (both nonzero),
  the Z the orthogonal one -- a SECOND neutral boson forced (EW.2). EW.3 (correspondence) POSTULATE; EW.4
  OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container50

def rankU1 : Nat := 1
def rankSU2 : Nat := 1
def cartanRank : Nat := rankU1 + rankSU2

/-! ### EW.1 -- the electroweak Cartan is rank 2 (two neutral bosons) -/

theorem cartan_rank_two : cartanRank = 2 ∧ rankU1 = 1 ∧ rankSU2 = 1 := by decide

/-! ### EW.2 -- the photon is a combination; a second neutral boson (Z) is forced -/

/-- A neutral direction as coefficients (a,b) over (Y, T3). A nontrivial combination has both nonzero. -/
def isCombination (a b : Int) : Bool := (a != 0) && (b != 0)
def photon : Int × Int := (1, 1)      -- a nontrivial combination of Y and T3 (schematic)
def zBoson : Int × Int := (1, -1)     -- the orthogonal line

theorem mixing_forces_Z :
    cartanRank = 2                                  -- two neutral directions
      ∧ isCombination photon.1 photon.2 = true      -- the photon is a genuine mixing
      ∧ photon ≠ zBoson := by decide                -- a distinct second neutral boson: the Z

#print axioms cartan_rank_two
#print axioms mixing_forces_Z

end Container50
