/-
  CONTAINER 04 -- THE INTEGERS / THE ADDITIVE INVERSE . rung 4, rests on container 01

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  An integer is a SIGNED DISPLACEMENT: a pair (a,b) : Nat x Nat read 'a against b',
  compared by CROSS-ADD (a+d = c+b) so Nat's truncated subtraction is never invoked --
  the positive form, no is-not. 0 is the COUNTERPOINT (the diagonal class (n,n)); +1 and
  -1 are the two unit DIRECTIONS off it. THE HEADLINE: every pair has an additive
  inverse -- its reversed direction -- which Nat lacks. Imports Container01: rung 1's
  count is the Nat this completes. DERIVED, ZERO axioms (no Quotient => no Quot.sound;
  cancellation hand-proved to dodge propext).
-/

import Container01.RecursiveRegistration

namespace Container04

/-! ### Nat's cancellation, hand-proved to stay axiom-free -/

/-- `Nat.add_right_cancel` pulls `propext` in this Lean version; proved fresh by
    induction so every theorem below stays zero-axiom. -/
theorem natAddRightCancel (a b c : Nat) (h : a + c = b + c) : a = b := by
  induction c with
  | zero => simpa using h
  | succ c ih =>
    apply ih
    have h2 : (a + c).succ = (b + c).succ := by
      rw [← Nat.add_succ, ← Nat.add_succ]; exact h
    exact Nat.succ.inj h2

/-- `(a+b)+(c+d) = (a+c)+(b+d)` from `add_assoc`/`add_comm` alone -- the one
    rearrangement the congruence proofs need. -/
theorem swap22 (a b c d : Nat) : (a + b) + (c + d) = (a + c) + (b + d) := by
  calc (a + b) + (c + d)
      = a + (b + (c + d)) := Nat.add_assoc a b (c + d)
    _ = a + ((b + c) + d) := by rw [← Nat.add_assoc b c d]
    _ = a + ((c + b) + d) := by rw [Nat.add_comm b c]
    _ = a + (c + (b + d)) := by rw [Nat.add_assoc c b d]
    _ = (a + c) + (b + d) := (Nat.add_assoc a c (b + d)).symm

/-! ### an integer is a signed displacement -- step 4.2, DERIVED -/

/-- A candidate integer: `(a, b)` read 'a against b', a direction with magnitude. -/
abbrev IntPair := Nat × Nat

/-- Same integer = same net displacement, by CROSS-ADD (never subtraction). -/
def IntEquiv (p q : IntPair) : Prop := p.1 + q.2 = q.1 + p.2

theorem IntEquiv.refl (p : IntPair) : IntEquiv p p := rfl

/-- `Eq.symm h`, not `h.symm`: dot notation on `IntEquiv` (a `def`) would self-refer. -/
theorem IntEquiv.symm {p q : IntPair} (h : IntEquiv p q) : IntEquiv q p := Eq.symm h

theorem IntEquiv.trans {p q r : IntPair} (h1 : IntEquiv p q) (h2 : IntEquiv q r) :
    IntEquiv p r := by
  apply natAddRightCancel _ _ q.2
  calc p.1 + r.2 + q.2
      = p.1 + (r.2 + q.2) := Nat.add_assoc p.1 r.2 q.2
    _ = p.1 + (q.2 + r.2) := by rw [Nat.add_comm r.2 q.2]
    _ = p.1 + q.2 + r.2 := (Nat.add_assoc p.1 q.2 r.2).symm
    _ = q.1 + p.2 + r.2 := by rw [h1]
    _ = q.1 + (p.2 + r.2) := Nat.add_assoc q.1 p.2 r.2
    _ = q.1 + (r.2 + p.2) := by rw [Nat.add_comm p.2 r.2]
    _ = q.1 + r.2 + p.2 := (Nat.add_assoc q.1 r.2 p.2).symm
    _ = r.1 + q.2 + p.2 := by rw [h2]
    _ = r.1 + (q.2 + p.2) := Nat.add_assoc r.1 q.2 p.2
    _ = r.1 + (p.2 + q.2) := by rw [Nat.add_comm q.2 p.2]
    _ = r.1 + p.2 + q.2 := (Nat.add_assoc r.1 p.2 q.2).symm

/-! ### the operations -- pointwise, no sign split (subtraction is never invoked) -/

def addPair (p q : IntPair) : IntPair := (p.1 + q.1, p.2 + q.2)

/-- Negation reverses the direction: 'a against b' becomes 'b against a'. -/
def negPair (p : IntPair) : IntPair := (p.2, p.1)

def zeroPair : IntPair := (0, 0)
def onePair : IntPair := (1, 0)      -- +1, one net step the defined way
def negOnePair : IntPair := (0, 1)   -- -1, one net step the other way

/-! ### '0' is the counterpoint -- the diagonal class -- step 4.3, DERIVED -/

/-- Every balanced pair `(n,n)` is at 0: the diagonal a=b IS the zero class. 0 names
    BALANCE, the counterpoint, not an object among the counts. -/
theorem diagonal_is_zero (n : Nat) : IntEquiv (n, n) zeroPair := by
  show n + 0 = 0 + n
  rw [Nat.add_zero, Nat.zero_add]

/-! ### +1 and -1 are the two unit directions -- step 4.4, DERIVED -/

/-- The two directions are DISTINCT: +1 is not -1. `IntEquiv onePair negOnePair` unfolds
    to `1 + 1 = 0 + 0` = `Nat.succ 1 = 0`, a constructor clash `Nat.noConfusion` refutes
    directly -- no `decide`, and (unlike `Nat.succ_ne_zero`, which pulls `propext` in this
    Lean) no axiom. -/
theorem plus_one_ne_minus_one : ¬ IntEquiv onePair negOnePair := fun h =>
  Nat.noConfusion h

/-! ### THE HEADLINE -- every integer has an additive inverse -- step 4.5, DERIVED -/

/-- The one thing Nat lacks (no n with n+1=0), supplied for EVERY pair: reverse the
    direction and the sum balances to the counterpoint. -/
theorem add_neg_equiv_zero (p : IntPair) : IntEquiv (addPair p (negPair p)) zeroPair := by
  show p.1 + p.2 + 0 = 0 + (p.2 + p.1)
  rw [Nat.add_zero, Nat.zero_add, Nat.add_comm p.1 p.2]

/-- +1 and -1 are mutually inverse -- the two directions meet at the counterpoint. A
    corollary of the headline, since `negOnePair` is defeq `negPair onePair`. -/
theorem plus_add_minus_zero : IntEquiv (addPair onePair negOnePair) zeroPair :=
  add_neg_equiv_zero onePair

/-! ### the operations are well-defined on the class -- step 4.6, DERIVED -/

/-- Addition does not depend on the chosen representatives -- it is an operation on
    integers, not on pairs. -/
theorem addPair_congr {p p' q q' : IntPair} (hp : IntEquiv p p') (hq : IntEquiv q q') :
    IntEquiv (addPair p q) (addPair p' q') := by
  show (p.1 + q.1) + (p'.2 + q'.2) = (p'.1 + q'.1) + (p.2 + q.2)
  calc (p.1 + q.1) + (p'.2 + q'.2)
      = (p.1 + p'.2) + (q.1 + q'.2) := swap22 p.1 q.1 p'.2 q'.2
    _ = (p'.1 + p.2) + (q'.1 + q.2) := by rw [hp, hq]
    _ = (p'.1 + q'.1) + (p.2 + q.2) := swap22 p'.1 p.2 q'.1 q.2

/-- Negation, likewise representative-independent. -/
theorem negPair_congr {p p' : IntPair} (h : IntEquiv p p') :
    IntEquiv (negPair p) (negPair p') := by
  show p.2 + p'.1 = p'.2 + p.1
  rw [Nat.add_comm p.2 p'.1, Nat.add_comm p'.2 p.1]
  exact Eq.symm h

/-! ### the count embeds, preserving addition -- step 4.6, DERIVED -/

/-- The count n embeds as pure defined-direction displacement. -/
def ofNatPair (n : Nat) : IntPair := (n, 0)

/-- Embedding preserves addition OUTRIGHT (definitionally, not merely up to ~): counting
    is a genuine sub-structure of the integers, not a relabelling. -/
theorem ofNatPair_add (a b : Nat) :
    ofNatPair (a + b) = addPair (ofNatPair a) (ofNatPair b) := rfl

/-- The thin, honest tie to rung 1 (imported): rung 1's `RecursiveRegistration` produces
    a genuine Nat -- the length of its concrete residual witness -- and that count embeds
    as `(n, 0)`. No rich structural correspondence is claimed; the point is only that the
    Nat this rung completes is honestly available from the floor below. Stated for rung
    1's own count via `.length`, so no literal is typed here. -/
example : ofNatPair (Container01.residual Container01.stage0).length
            = ((Container01.residual Container01.stage0).length, 0) := rfl

/-! ### multiplication -- the ring core -- step 4.8, DERIVED

    From here the axiom report widens: `omega` discharges the linear rearrangements over
    the (opaque) product terms, at the cost of Lean's three standard axioms
    [propext, Classical.choice, Quot.sound]. The ADDITIVE theorems above stay zero-axiom;
    `#print axioms` shows exactly where the product's arithmetic enters. -/

/-- (a-b)(c-d) = (ac+bd) - (ad+bc), kept in Nat -- no subtraction is invoked. -/
def mulPair (p q : IntPair) : IntPair :=
  (p.1 * q.1 + p.2 * q.2, p.1 * q.2 + p.2 * q.1)

/-- THE HEADLINE of the product: it is well-defined on the CLASSES -- multiplication is
    genuinely an operation on the integers, not on pairs. (First argument; the second
    follows by commutativity.) -/
theorem mulPair_congr {p p' q : IntPair} (hp : IntEquiv p p') :
    IntEquiv (mulPair p q) (mulPair p' q) := by
  have A : p.1 * q.1 + p'.2 * q.1 = p'.1 * q.1 + p.2 * q.1 := by
    rw [← Nat.add_mul, hp, Nat.add_mul]
  have B : p'.1 * q.2 + p.2 * q.2 = p.1 * q.2 + p'.2 * q.2 := by
    rw [← Nat.add_mul, ← hp, Nat.add_mul]
  show p.1 * q.1 + p.2 * q.2 + (p'.1 * q.2 + p'.2 * q.1)
       = p'.1 * q.1 + p'.2 * q.2 + (p.1 * q.2 + p.2 * q.1)
  omega

/-- +1 = (1,0) is the multiplicative unit. -/
theorem mul_one_equiv (p : IntPair) : IntEquiv (mulPair p onePair) p := by
  show p.1 * 1 + p.2 * 0 + p.2 = p.1 + (p.1 * 0 + p.2 * 1)
  omega

/-- The product is commutative (on the classes). -/
theorem mulPair_comm (p q : IntPair) : IntEquiv (mulPair p q) (mulPair q p) := by
  show p.1 * q.1 + p.2 * q.2 + (q.1 * p.2 + q.2 * p.1)
       = q.1 * p.1 + q.2 * p.2 + (p.1 * q.2 + p.2 * q.1)
  rw [Nat.mul_comm q.1 p.2, Nat.mul_comm q.2 p.1, Nat.mul_comm q.1 p.1,
      Nat.mul_comm q.2 p.2]
  omega

/-- The product distributes over the sum (on the left). With congruence, unit and
    commutativity, the integers are a commutative RING -- multiplication is real. -/
theorem left_distrib_equiv (p q r : IntPair) :
    IntEquiv (mulPair p (addPair q r)) (addPair (mulPair p q) (mulPair p r)) := by
  show p.1 * (q.1 + r.1) + p.2 * (q.2 + r.2)
       + (p.1 * q.2 + p.2 * q.1 + (p.1 * r.2 + p.2 * r.1))
     = p.1 * q.1 + p.2 * q.2 + (p.1 * r.1 + p.2 * r.2)
       + (p.1 * (q.2 + r.2) + p.2 * (q.1 + r.1))
  rw [Nat.mul_add, Nat.mul_add, Nat.mul_add, Nat.mul_add]
  omega

/-! ### the order and the ORIENTATION -- step 4.9, DERIVED -/

/-- (a,b) <= (c,d) iff a+d <= c+b -- cross-add, no subtraction. -/
def lePair (p q : IntPair) : Prop := p.1 + q.2 ≤ q.1 + p.2

/-- Orientation: (a,b) is positive iff its net leans defined-ward (b < a) -- WHICH of the
    two directions is the positive one. -/
def isPos (p : IntPair) : Prop := p.2 < p.1

theorem lePair_refl (p : IntPair) : lePair p p := Nat.le_refl _

theorem lePair_total (p q : IntPair) : lePair p q ∨ lePair q p := Nat.le_total _ _

/-- THE ORIENTATION: every integer is positive, the counterpoint 0, or negative (its
    reverse positive) -- exactly how the two directions and the counterpoint partition the
    number line. This is the orientation owed by step 4.4's 'directions'. -/
theorem orientation_trichotomy (p : IntPair) :
    isPos p ∨ IntEquiv p zeroPair ∨ isPos (negPair p) := by
  rcases Nat.lt_trichotomy p.1 p.2 with h | h | h
  · exact Or.inr (Or.inr h)
  · exact Or.inr (Or.inl (by show p.1 + 0 = 0 + p.2; omega))
  · exact Or.inl h

/-- +1 is the positive direction; -1 is not. The orientation is fixed. (`isPos onePair`
    is defeq `0 < 1`; `isPos negOnePair` is defeq `1 < 0`.) -/
theorem plus_is_positive : isPos onePair := Nat.zero_lt_one
theorem minus_not_positive : ¬ isPos negOnePair := Nat.not_lt_zero 1

/-- EXCLUSIVITY of the orientation: at most one of positive / counterpoint / negative holds.
    With `orientation_trichotomy` (at least one) this makes the split EXACTLY one, in the
    kernel -- the two directions and the counterpoint genuinely partition the line. -/
theorem orientation_exclusive (p : IntPair) :
    ¬(isPos p ∧ IntEquiv p zeroPair) ∧
    ¬(isPos p ∧ isPos (negPair p)) ∧
    ¬(IntEquiv p zeroPair ∧ isPos (negPair p)) := by
  refine ⟨?_, ?_, ?_⟩ <;> rintro ⟨h1, h2⟩ <;>
    simp only [isPos, IntEquiv, negPair, zeroPair] at h1 h2 <;> omega

/-! ### associativity of the product -- step 4.10, DERIVED -/

/-- The product is associative -- the last ring axiom, now mechanised. Distributing
    (`mul_add`/`add_mul`) and reassociating the triple products (`mul_assoc`) puts both
    sides over the same eight degree-3 monomials; `omega` closes the linear identity. -/
theorem mulPair_assoc (p q r : IntPair) :
    IntEquiv (mulPair (mulPair p q) r) (mulPair p (mulPair q r)) := by
  simp only [IntEquiv, mulPair, Nat.add_mul, Nat.mul_add, Nat.mul_assoc]
  omega

-- POSTULATE (step 4.7, NOT proven): the identification of this signed-displacement
-- structure WITH the floor's number line -- +1/-1 the two registration directions, 0 the
-- counterpoint. Kevin's floor note, earned by the algebra above but held, not derived.
--
-- OWED (step 4.8, NOT built here): multiplication (a,b)*(c,d) = (ac+bd, ad+bc) and the
-- total order (which direction is positive). Both derive from this same pair construction
-- and complete Z beyond its additive group; they belong to the ring/order rungs downstream.

#print axioms IntEquiv.trans
#print axioms diagonal_is_zero
#print axioms plus_one_ne_minus_one
#print axioms add_neg_equiv_zero
#print axioms plus_add_minus_zero
#print axioms addPair_congr
#print axioms negPair_congr
#print axioms ofNatPair_add
-- the ring/order theorems -- omega widens these to the three standard axioms:
#print axioms mulPair_congr
#print axioms mul_one_equiv
#print axioms mulPair_comm
#print axioms left_distrib_equiv
#print axioms orientation_trichotomy
#print axioms orientation_exclusive
#print axioms mulPair_assoc

end Container04
