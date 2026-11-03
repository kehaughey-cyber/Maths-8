/-
  CONTAINER 02 -- THE REGISTRATION EVENT & THE OBSERVER TRIAD . rung 2, rests on 00

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Rung 2 is where CHANGE enters, so where the floor's latent triad becomes critical.
  DERIVED (zero axioms where marked): the event (potential -> stable) on the corrected
  floor, observer/observed co-emergence, and the observer-triad arithmetic (three is the
  first rank that turns and where a rotation differs from a permutation). POSTULATE: that
  this IS the three-observer condition. OWED: the phase cycle -> 12.
-/

import Container00.Distinction

namespace Container02
open Container00

/-! ### the registration event -- steps 2.1, 2.2, 2.5, DERIVED -/

/-- A potential distinction: a raw candidate, nothing defined yet -- not a distinction. -/
def potential : Base := [.undefinedExistent, .undefinedExistent, .undefinedExistent, .undefinedExistent]

/-- The event stabilises it by defining the minimal thing: now a distinction. -/
def afterEvent : Base := [.definedExistent, .undefinedExistent, .undefinedExistent, .undefinedExistent]

/-- Step 2.1. The potential is not yet stable (nothing distinguished). -/
theorem potential_not_stable : isDistinction potential = false := rfl

/-- Step 2.1. After the event it is stable -- a distinction. The transition IS the first
    change the floor carries. -/
theorem event_stabilises : isDistinction afterEvent = true := rfl

/-- Step 2.2 / 2.5. Observer and observed co-emerge: a defined thing AND an undefined thing
    are present together after the event -- exactly a distinction, disjoint by label. This is
    also the join to rung 1: the stable product is the artifact rung 1 chains. -/
theorem observer_observed_co_emerge : isDistinction afterEvent = true := rfl

/-! ### the observer triad, as arithmetic -- step 2.3, DERIVED, zero axioms -/

/-- rotations of n points: the cyclic group has order n. -/
def rotations (n : Nat) : Nat := n

/-- permutations of n points: n!. -/
def permutations : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * permutations n

/-- a cyclic order TURNS iff some non-identity rotation differs from its inverse:
    0 < k < n with 2k not 0 mod n. -/
def hasTurning (n : Nat) : Bool :=
  (List.range n).any (fun k => decide (k ≠ 0) && decide ((2 * k) % n ≠ 0))

/-- ONE is static: the only permutation is the identity, and there is no turning. -/
theorem one_static : rotations 1 = permutations 1 ∧ hasTurning 1 = false := by decide

/-- TWO has POLARITY but NO TURNING: rotations = permutations = 2, the swap is its own
    inverse. -/
theorem two_polarity_no_turning :
    rotations 2 = permutations 2 ∧ hasTurning 2 = false := by decide

/-- THREE turns AND a rotation differs from a permutation: 3 < 6, directed turning exists. -/
theorem three_turns_and_differs :
    rotations 3 < permutations 3 ∧ hasTurning 3 = true := by decide

/-- THREE is the first closure rank -- the whole one/two/three transition in one statement. -/
theorem three_is_first_closure_rank :
    rotations 1 = permutations 1
    ∧ rotations 2 = permutations 2
    ∧ rotations 3 < permutations 3
    ∧ hasTurning 1 = false ∧ hasTurning 2 = false ∧ hasTurning 3 = true := by decide

/-- and it does not coincide again on the reachable range 3..8. -/
theorem differs_three_through_eight :
    ([3, 4, 5, 6, 7, 8].all (fun n => decide (rotations n < permutations n))) = true := by decide

/-! ### the third registers the change -- step 2.4, POSTULATE -/

/-- POSTULATE. That the rank-three transition above IS the three-observer condition -- that
    registering a CHANGE (a difference, an orientation) takes the third observer, the
    without -- is the reading. The arithmetic skeleton is proven; the reading is held, not
    lifted. This is where the floor's latent triad becomes critical: under change. -/
def registersDifference : Prop := ∀ n : Nat, hasTurning n = true → 3 ≤ n

-- OWED (NOT built here): the event opens a cyclic/phase structure whose saturating capacity
-- is where 12 (and the icosahedron) come from. That lands at the phase tier / 05-06.

#print axioms potential_not_stable
#print axioms event_stabilises
#print axioms observer_observed_co_emerge
#print axioms one_static
#print axioms two_polarity_no_turning
#print axioms three_turns_and_differs
#print axioms three_is_first_closure_rank
#print axioms differs_three_through_eight

end Container02
