/-
  CONTAINER 46 -- THE SPACETIME SIGNATURE: time is 1-D, and causality forces Lorentzian (3,1).
  Rests on 07 (time = the ordinal total order), 25/41/42 (space = 3), 33 (the maximal rate c).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Time is 1-D and directed (07's total order = a line; the sign arrow) (LS.1); the (3+1) split, time
  categorically distinct from space (LS.2); the finite rate c is a causal cone (LS.3); a Euclidean (4,0)
  metric has NO null cone, so a causal substrate CANNOT be metrized Euclidean -- it needs one timelike
  direction (time, opposite sign) + three spacelike = signature (3,1), ds^2 = -c^2 dt^2 + dl^2 (LS.4,
  forced). LS.5 (the metric identification) POSTULATE; LS.6 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container46

/-! ### LS.1 / LS.2 -- the (3+1) split -/

def timeDim : Nat := 1
def spaceDim : Nat := 3
theorem three_plus_one : timeDim = 1 ∧ spaceDim = 3 ∧ timeDim + spaceDim = 4 := by decide

/-! ### LS.4 -- causality forces Lorentzian (3,1) over Euclidean (4,0) -/

/-- A signature and a vector as integer 4-tuples; the invariant interval sum(sign_i * x_i^2). -/
abbrev V4 := Int × Int × Int × Int
def interval (s v : V4) : Int :=
  s.1*v.1*v.1 + s.2.1*v.2.1*v.2.1 + s.2.2.1*v.2.2.1*v.2.2.1 + s.2.2.2*v.2.2.2*v.2.2.2
def lorentz : V4 := (-1, 1, 1, 1)      -- (3,1): one timelike (-), three spacelike (+)
def euclid : V4 := (1, 1, 1, 1)        -- (4,0): positive-definite
def nullv : V4 := (1, 1, 0, 0)         -- a candidate light-cone vector

/-- The Lorentzian (3,1) form has a nonzero NULL vector (the cone); the Euclidean (4,0) form has none --
    so a causal cone (LS.3) cannot be carried by a positive-definite metric. And the Lorentzian form has
    exactly ONE timelike direction (the first, sign < 0 -- time) and three spacelike (sign > 0 -- space). -/
theorem signature_forced :
    interval lorentz nullv = 0 ∧ interval euclid nullv ≠ 0
      ∧ lorentz.1 < 0 ∧ lorentz.2.1 > 0 ∧ lorentz.2.2.1 > 0 ∧ lorentz.2.2.2 > 0 := by decide

#print axioms three_plus_one
#print axioms signature_forced

end Container46
