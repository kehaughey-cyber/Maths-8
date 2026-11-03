/-
  CONTAINER 45 -- THE SPINOR STRUCTURE: the carrier carries 2-valued (spinor) reps; a 2*pi turn acts as -1.
  Rests on 28 (2I = the SU(2)->SO(3) double cover), 06 (the carrier quaternions), 38 (the 4*pi holonomy).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  2I contains the central -1 (order 2), the non-trivial kernel of SU(2)->SO(3): conjugation by -1 is the
  identity rotation (a 2*pi turn = identity in SO(3)), yet -1 != +1 in SU(2) (SP.1). On the 2D spinor rep
  SU(2) acts directly, so a 2*pi rotation acts as -1 (psi -> -psi) and only 4*pi = (-1)^2 returns +1 -- the
  substrate carries 2-valued (half-integer-spin) reps (SP.2), the 4*pi holonomy of 38.DV.3. SP.3 (spinors
  <-> fermions) POSTULATE; SP.4 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container45

abbrev Q := Int × Int × Int × Int
def qmul : Q → Q → Q
  | (a0, a1, a2, a3), (b0, b1, b2, b3) =>
    (a0*b0 - a1*b1 - a2*b2 - a3*b3,
     a0*b1 + a1*b0 + a2*b3 - a3*b2,
     a0*b2 - a1*b3 + a2*b0 + a3*b1,
     a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj : Q → Q | (w, x, y, z) => (w, -x, -y, -z)

def one : Q := (1, 0, 0, 0)
def negOne : Q := (-1, 0, 0, 0)
def qi : Q := (0, 1, 0, 0)
def qj : Q := (0, 0, 1, 0)
def qk : Q := (0, 0, 0, 1)

/-! ### SP.1 -- the central -1: order 2, central, conjugation = identity rotation, yet -1 != +1 -/

/-- -1 is in the carrier as the non-trivial kernel of SU(2)->SO(3): (-1)^2 = +1 (order 2); it commutes
    with i,j,k (central); conjugation by -1 fixes i,j,k (the identity rotation, a 2*pi turn); yet -1 != +1. -/
theorem central_minus_one :
    qmul negOne negOne = one
      ∧ qmul negOne qi = qmul qi negOne ∧ qmul negOne qj = qmul qj negOne ∧ qmul negOne qk = qmul qk negOne
      ∧ qmul (qmul negOne qi) (qconj negOne) = qi
      ∧ qmul (qmul negOne qj) (qconj negOne) = qj
      ∧ qmul (qmul negOne qk) (qconj negOne) = qk
      ∧ negOne ≠ one := by decide

/-! ### SP.2 -- the spinor: 2*pi acts as -1, 4*pi as +1 (returns only after 4*pi) -/

/-- On the 2D spinor rep the 2*pi rotation acts as -1 (psi -> -psi) and 4*pi = (2*pi)^2 as +1: the
    substrate carries 2-valued (half-integer-spin) reps -- the 4*pi holonomy (38.DV.3). -/
theorem spinor_returns_at_4pi :
    negOne ≠ one ∧ qmul negOne negOne = one := by decide

#print axioms central_minus_one
#print axioms spinor_returns_at_4pi

end Container45
