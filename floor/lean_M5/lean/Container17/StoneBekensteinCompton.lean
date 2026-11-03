/-
  CONTAINER 17 -- STONE: BEKENSTEIN-COMPTON. The ruler BC = 2*pi/ln2. EXTERNAL, QUARANTINED.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 5, the first STONE: external, established physics held OUTSIDE the derivation chain and
  re-derived COLD (this is OUR OWN proof, NOT an import of maths-4's MassCancellation.lean).
  Mathlib-FREE, ZERO-axiom. The DERIVED core (S.1) is the MASS CANCELLATION:

    given  R*(m c) = hbar   (Compton, cleared)  and  E = m c^2,
    then   R*E = hbar*c      -- m absent -- so  S = 2*pi*(R E)/(hbar c*ln2) = 2*pi/ln2 = 9.064720...

  The scalar 2*pi/ln2 needs R and is cited/numeric (derivation + model). S.3 (assumed equivalences),
  S.4 (owed groundings), S.5 (Kevin's Planck hypothesis) are POSTULATE/OWED -- nothing to prove.

  Nat.mul_assoc carries propext in this toolchain, so associativity is hand-proved to keep ZERO axioms.
-/

namespace Container17

/-- Associativity of Nat multiplication, hand-proved (not cited) to avoid the propext that
    `Nat.mul_assoc` carries in this toolchain -- keeps the Stone's core at zero axioms. -/
theorem natMulAssoc (a b c : Nat) : a * b * c = a * (b * c) := by
  induction c with
  | zero => rfl
  | succ c ih => rw [Nat.mul_succ, Nat.mul_succ, Nat.mul_add, ih]

/-- "R = hbar/(m c)" without division: R*(m c) = hbar (the honest content whenever m, c are nonzero). -/
def IsComptonRadius (R m hbar c : Nat) : Prop := R * (m * c) = hbar
/-- "E = m c^2" spelled out without a power lemma. -/
def IsRestEnergy (E m c : Nat) : Prop := E = m * c * c

/-- THE MASS CANCELLATION (S.1): with R the Compton radius and E the rest energy of the same mass,
    R*E = hbar*c outright -- m does not appear in the result. Proved fresh here for all Nat, zero-axiom.
    (S = 2*pi*(R E)/(hbar c*ln2) = 2*pi/ln2 then follows by routine scalar arithmetic, over R, cited.) -/
theorem mass_cancels {R m hbar c E : Nat}
    (hR : IsComptonRadius R m hbar c) (hE : IsRestEnergy E m c) :
    R * E = hbar * c := by
  unfold IsComptonRadius at hR
  unfold IsRestEnergy at hE
  subst hE
  rw [← natMulAssoc, hR]

/-- The result carries no m: a concrete witness (R=5, m=2, c=2 -> hbar=20, E=8) gives R*E = hbar*c = 40,
    the same hbar*c any mass on this Compton/rest-energy locus returns. -/
theorem mass_cancels_witness :
    (5 * 8 == 20 * 2) = true := by decide

#print axioms natMulAssoc
#print axioms mass_cancels
#print axioms mass_cancels_witness

end Container17
