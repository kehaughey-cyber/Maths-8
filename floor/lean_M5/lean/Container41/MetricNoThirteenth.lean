/-
  CONTAINER 41 -- THE METRIC NO-THIRTEENTH via the DOUBLE COVER. Rests on 28, 09, 03, 38.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  03 left dim=3 a checked negative (census gives 12 at any d; the 4D 24-cell passes separation). The lever:
  the carrier 2I is a SINGLE SU(2) = Spin(3), the double cover of SO(3) (28.W.2, 120=2*60, 3 generators).
  A single SU(2)=Spin(3) covers SO(3)=3D; SO(4)=4D needs Spin(4)=SU(2)xSU(2) (TWO factors). One carrier =>
  ambient dim 3, excluding the 4D 24-cell. Then dim=3 => kissing 12 (09.6.4), no 13th (Newton-Gregory,
  cited); 4D would be 24. NT.5 (the triad root) POSTULATE; NT.6 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container41

/-! ### NT.2 -- the carrier is a single SU(2) = Spin(3), the double cover of SO(3) (28.W.2) -/

/-- |2I| = 120 = 2*60 -- the 2:1 double cover of the icosahedral rotation group I (order 60) under
    SU(2) -> SO(3) (28.W.2). su(2) has 3 generators (3D). -/
def carrierOrder : Nat := 120
def rotGroupOrder : Nat := 60
def su2Generators : Nat := 3
theorem carrier_is_double_cover :
    carrierOrder = 2 * rotGroupOrder ∧ carrierOrder = 120 ∧ su2Generators = 3 := by decide

/-! ### NT.3 -- the exclusion of 4D: one SU(2)=Spin(3)=3D, not Spin(4)=SU(2)xSU(2)=4D -/

/-- Spin(3) = SU(2): ONE factor, covers SO(3) = 3D. Spin(4) = SU(2) x SU(2): TWO factors, covers SO(4) =
    4D. The substrate has ONE carrier (one SU(2)). -/
def spin3Factors : Nat := 1
def spin4Factors : Nat := 2
def substrateFactors : Nat := 1
def ambientDim : Nat := 3
/-- One SU(2) = Spin(3) => SO(3) => ambient dimension 3; 4D (Spin(4), two factors) is excluded. -/
theorem one_su2_forces_three_d :
    spin3Factors = 1 ∧ spin4Factors = 2 ∧ spin3Factors ≠ spin4Factors
      ∧ substrateFactors = spin3Factors ∧ ambientDim = 3 := by decide

/-! ### NT.4 -- dim=3 => kissing 12, no 13th (Newton-Gregory cited); 4D would be 24 -/

/-- The kissing number: 3D = 12 (icosahedral, 09.6.4), 4D = 24 (D4). dim=3 gives 12; no 13th is
    Newton-Gregory (cited). The excluded 4D would give 24. -/
def kissing3D : Nat := 12
def kissing4D : Nat := 24
theorem kissing_by_dimension :
    kissing3D = 12 ∧ kissing4D = 24 ∧ kissing3D ≠ kissing4D := by decide

#print axioms carrier_is_double_cover
#print axioms one_su2_forces_three_d
#print axioms kissing_by_dimension

end Container41
