/-
  CONTAINER 49 -- CPT: the substrate's discrete symmetries C, P, T, and CPT (unlocked by the signature 46).
  Rests on 29 (charge = signed defect), 44 (parity/chirality), 46 (the arrow + the Lorentz signature).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  C = charge conjugation = the degree-mirror d->12-d, negating the charge 12-2d (29), the flat mirror of the
  wings (36/48) (CT.1); P = the even/odd orbit swap (44, violated) (CT.2); T = the arrow reversal (46/07)
  (CT.3). Each is an involution. CPT (CT.4) via the CPT theorem, unlocked by 46 -- POSTULATE; CT.5 OWED.
  Mathlib-FREE, ZERO-axiom.
-/

namespace Container49

/-- The signed angle-defect charge 12 - 2d (29.EM.1). -/
def charge (d : Int) : Int := 12 - 2*d
/-- Charge conjugation C = the degree-mirror at d=6. -/
def C (d : Int) : Int := 12 - d
/-- Parity/time sign as an element of {+1,-1}; P and T are the sign flip. -/
def flip (s : Int) : Int := -s

/-! ### CT.1 -- C negates the charge, is an involution, fixes the neutral d=6 -/

theorem C_charge_conjugation :
    charge (C 5) = -(charge 5) ∧ charge (C 7) = -(charge 7)      -- C flips the charge
      ∧ C (C 5) = 5 ∧ C (C 8) = 8                                -- involution
      ∧ C 6 = 6 ∧ charge 6 = 0 := by decide                      -- fixes the neutral d=6

/-! ### CT.2 / CT.3 -- P and T are involutions with the sign flip -/

theorem P_and_T_involutions :
    flip (1) = -1 ∧ flip (-1) = 1 ∧ flip (flip 1) = 1 ∧ flip (flip (-1)) = -1 := by decide

#print axioms C_charge_conjugation
#print axioms P_and_T_involutions

end Container49
