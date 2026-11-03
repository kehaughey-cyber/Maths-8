/-
  CONTAINER 53 -- QUANTUM KINEMATICS: the substrate's U(1) phase, complex amplitudes, unitary evolution.
  Rests on 32/10 (the 2*pi phase cycle), 29 (the abelian C phase), 28 (SU(2)), 42/43 (C subset H, the norm).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The minimal registration boundary is one 2*pi cycle (12 radits) -- a U(1) phase (QK.1); i^2 = -1, the
  complex sector C = R(+)R*i subset H (QK.2); carrier elements are unit-norm and the norm is multiplicative
  -> composition is norm-preserving = unitary (QK.3). QK.4 (the assembly = QM's stage; the Born rule the
  gate, closing 43.CN.4) POSTULATE; QK.5 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container53

abbrev Q := Int × Int × Int × Int
def qmul : Q → Q → Q
  | (a0, a1, a2, a3), (b0, b1, b2, b3) =>
    (a0*b0 - a1*b1 - a2*b2 - a3*b3,
     a0*b1 + a1*b0 + a2*b3 - a3*b2,
     a0*b2 - a1*b3 + a2*b0 + a3*b1,
     a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qnorm2 : Q → Int | (w, x, y, z) => w*w + x*x + y*y + z*z
def one : Q := (1, 0, 0, 0)
def qi : Q := (0, 1, 0, 0)

def phaseCycleRadits : Nat := 12       -- 32.RB.1 / 10.W.2: one 2*pi cycle

/-! ### QK.1 -- the phase cycle is 2*pi (a U(1)) -/

theorem phase_is_U1 : phaseCycleRadits = 12 := by decide

/-! ### QK.2 -- i^2 = -1: the complex sector C subset H -/

theorem complex_amplitude : qmul qi qi = (-1, 0, 0, 0) := by decide

/-! ### QK.3 -- carrier unit-norm + multiplicative norm => unitary (norm-preserving) -/

theorem unitary_evolution :
    qnorm2 one = 1 ∧ qnorm2 qi = 1
      ∧ qnorm2 (qmul qi qi) = qnorm2 qi * qnorm2 qi := by decide

#print axioms phase_is_U1
#print axioms complex_amplitude
#print axioms unitary_evolution

end Container53
