/-
  CONTAINER 55 -- THE BORN HINGE: |amplitude|^2 = the composition norm = the intensive measure.
  Rests on 06 (the quadratic codifferent norm), 43 (the multiplicative composition norm), 53 (complex
  amplitudes, unitary evolution), 05 (the inner product); cites the Born rule / Gleason.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  N(q) = q*conj(q) = |q|^2 (06.6, quadratic), multiplicative (43); N(amp) = |amp|^2 (BR.1). The square is
  forced: the quadratic norm is ADDITIVE over orthogonal (Pythagoras), the linear modulus is NOT (BR.2).
  BR.3 the measure<->probability hinge (closes 43.CN.4 = the Born rule) POSTULATE; BR.5 OWED (measurement
  NOT solved). Mathlib-FREE, ZERO-axiom.
-/

namespace Container55

abbrev Q := Int × Int × Int × Int
def qmul : Q → Q → Q
  | (a0, a1, a2, a3), (b0, b1, b2, b3) =>
    (a0*b0 - a1*b1 - a2*b2 - a3*b3,
     a0*b1 + a1*b0 + a2*b3 - a3*b2,
     a0*b2 - a1*b3 + a2*b0 + a3*b1,
     a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj : Q → Q | (w, x, y, z) => (w, -x, -y, -z)
def N : Q → Int | (w, x, y, z) => w*w + x*x + y*y + z*z    -- the quadratic norm = |q|^2
def qadd : Q → Q → Q | (a0,a1,a2,a3),(b0,b1,b2,b3) => (a0+b0,a1+b1,a2+b2,a3+b3)

def amp : Q := (3, 4, 0, 0)      -- 3 + 4i, a complex amplitude (C subset H)
def qi : Q := (0, 1, 0, 0)
def qj : Q := (0, 0, 1, 0)
def e1 : Q := (1, 0, 0, 0)
def e2 : Q := (0, 1, 0, 0)       -- e1 . e2 = 0 (orthogonal)

/-! ### BR.1 -- the composition norm is the squared modulus, multiplicative -/

theorem norm_is_squared_modulus :
    N amp = (qmul amp (qconj amp)).1 ∧ N amp = 25 ∧ N (qmul qi qj) = N qi * N qj := by decide

/-! ### BR.2 -- the square is forced: quadratic additive over orthogonal, linear not -/

/-- The quadratic norm is ADDITIVE over orthogonal directions (Pythagoras: N(e1+e2)=N(e1)+N(e2)); the
    linear modulus is NOT ( |e1+e2|^2 = 2, but (|e1|+|e2|)^2 = 4 ). So the additive-over-orthogonal
    measure (with linear superposition) is the QUADRATIC |amp|^2, not the linear |amp| -- the square. -/
theorem square_forced :
    N (qadd e1 e2) = N e1 + N e2            -- Pythagoras: quadratic is additive over orthogonal
      ∧ N (qadd e1 e2) = 2
      ∧ N (qadd e1 e2) ≠ (1 + 1) * (1 + 1)  -- 2 != 4: the linear modulus is NOT additive over orthogonal
      := by decide

#print axioms norm_is_squared_modulus
#print axioms square_forced

end Container55
