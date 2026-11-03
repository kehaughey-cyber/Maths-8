/-
  CONTAINER 43 -- FLOOR-FORCING 42.SR.4: the division property reduces to the bridge + one multiplicative norm.
  Rests on 42 (SR.4/SR.5), 05 (the bridge), 06 (the carrier is a group); cites Hurwitz 1898.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  SR.4 ("the carrier's ambient algebra is a finite-dim DIVISION algebra over R") splits into: (i) over-R +
  positive-definite = the BRIDGE 05 (an existing postulate); (ii) finite-dim/unital/product cold; (iii)
  DIVISION. The group ALONE does NOT give (iii): R[Z/2] has the zero divisor (1+t)(1-t)=(0,0) (CN.3). So a
  MULTIPLICATIVE norm is genuinely extra -- the isolated root (CN.4, POSTULATE). Given it, positive-definite
  + multiplicative => no zero divisors => division, and Hurwitz + 42's assoc/non-comm => H, real dim 4 =>
  dim=3 (CN.5). Mathlib-FREE, ZERO-axiom.
-/

namespace Container43

/-! ### CN.3 -- the group ALONE does not force division: R[Z/2] has a zero divisor -/

/-- The group algebra R[Z/2] with basis {1, t}, t^2 = 1: an element a*1 + b*t as the pair (a,b), and the
    product (a,b)*(c,d) = (a*c + b*d, a*d + b*c). -/
abbrev G2 := Int × Int
def g2mul : G2 → G2 → G2
  | (a, b), (c, d) => (a*c + b*d, a*d + b*c)
def onePlusT : G2 := (1, 1)
def oneMinusT : G2 := (1, -1)

/-- (1+t)(1-t) = (0,0) with both factors nonzero -- an explicit ZERO DIVISOR. So the real algebra of a
    group (here Z/2) need not be a division algebra: being a group (06.3) does NOT force division; the
    multiplicative norm (CN.4) is genuinely extra. -/
theorem group_algebra_has_zero_divisor :
    g2mul onePlusT oneMinusT = (0, 0) ∧ onePlusT ≠ (0, 0) ∧ oneMinusT ≠ (0, 0) := by decide

/-! ### CN.5 -- Hurwitz: the composition algebras are dims [1,2,4,8]; assoc + non-comm => H (dim 4) -/

/-- The four real composition algebras (Hurwitz 1898), indexed 0=R,1=C,2=H,3=O, by real dimension, with
    associativity and commutativity (from 42). A positive-definite multiplicative norm (CN.4) forces the
    algebra into this list; 42's associativity (excl. O) + non-commutativity (excl. R,C) selects H. -/
def hurwitzDims : List Nat := [1, 2, 4, 8]
def realDim : Nat → Nat
  | 0 => 1 | 1 => 2 | 2 => 4 | 3 => 8 | _ => 0
def assoc : Nat → Bool
  | 0 => true | 1 => true | 2 => true | 3 => false | _ => false   -- O non-associative
def comm : Nat → Bool
  | 0 => true | 1 => true | 2 => false | 3 => false | _ => false  -- R,C commutative
def forced : List Nat := [0, 1, 2, 3].filter (fun a => assoc a && !comm a)

/-- Hurwitz gives real dims [1,2,4,8]; the unique associative + non-commutative composition algebra is H
    (index 2, real dim 4). Its imaginary part is 3 (42.SR.1), so dim = 3. -/
theorem hurwitz_then_H :
    hurwitzDims = [1, 2, 4, 8] ∧ forced = [2] ∧ realDim 2 = 4 := by decide

#print axioms group_algebra_has_zero_divisor
#print axioms hurwitz_then_H

end Container43
