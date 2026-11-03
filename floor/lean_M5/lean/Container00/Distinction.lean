/-
  CONTAINER 00 -- THE DISTINCTION . the floor, rung 0, rests on nothing

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The floor is TRIADIC, EXISTENCE-FOUNDED, and carries NO is-not:
   - existence/non-existence is a real bound, but only at registration 1 (the totality,
     all-that-is against non-existence). Non-existence is the counterpoint, not a thing.
   - within existence a thing is DEFINED or UNDEFINED, both existent; undefined is not
     non-existent. The residual is a positive selection, never `not state`.
   - a distinction is registered by THREE observers (two within, one without); the
     registration is their live artifact, not the observers.
  DERIVED here (zero axioms, constructive -- no decide, no Mathlib): the three states and
  the no-is-not distinction. POSTULATE (stated, not proven): the existence bound and the
  triad. See statement.md for the grading.
-/

namespace Container00

/-! ### the three existential states -- step 0.2, DERIVED -/

/-- Non-existence is the counterpoint of registration 1, not a thing to subdivide. Within
    existence a thing is defined or undefined -- both existent. -/
inductive Existential where
  | definedExistent
  | undefinedExistent
  | nonExistent
deriving DecidableEq, BEq

/-- Only what exists can be perceived or registered. All three cases written out (no
    wildcard), because a wildcard matcher would drag `propext` in for a Bool computation. -/
def perceivable : Existential → Bool
  | .definedExistent   => true
  | .undefinedExistent => true
  | .nonExistent       => false

/-- Undefined is NOT non-existent -- it exists, and can be perceived and later defined. -/
theorem undefined_ne_nonexistent :
    Existential.undefinedExistent ≠ Existential.nonExistent :=
  fun h => Existential.noConfusion h

/-- Exactly the two existent states are perceivable; non-existence is not. Stated as
    three facts rather than one conjunction, to keep every one of them zero-axiom. -/
theorem defined_perceivable   : perceivable .definedExistent = true := rfl
theorem undefined_perceivable : perceivable .undefinedExistent = true := rfl
theorem nonexistent_not_perceivable : perceivable .nonExistent = false := rfl

/-! ### a distinction, without any is-not -- steps 0.3 & 0.5, DERIVED -/

/-- A base is a field of existent things, each defined or undefined. -/
abbrev Base := List Existential

/-- The state and the residual are POSITIVE selections -- `= defined`, `= undefined` --
    never `not state`. A distinction needs BOTH witnessed (Proposition 1, the two poles). -/
def isDistinction (b : Base) : Bool :=
  (b.filter (· == .definedExistent) |>.isEmpty |> not) &&
  (b.filter (· == .undefinedExistent) |>.isEmpty |> not)

/-- The base emitted from the derivation: 2 defined, 3 undefined. -/
def base : Base := [.definedExistent, .definedExistent, .undefinedExistent, .undefinedExistent, .undefinedExistent]

/-- Step 0.3/0.5. The labelled base is a distinction: a defined thing and an undefined
    thing are both present, both existent. -/
theorem base_is_distinction : isDistinction base = true := rfl

/-- Proposition 1, the two poles co-define: a wholly-defined base leaves no residual to be
    distinguished from, and a wholly-undefined base has no state -- neither is a distinction. -/
theorem all_defined_is_not_a_distinction :
    isDistinction [.definedExistent, .definedExistent] = false := rfl

theorem none_defined_is_not_a_distinction :
    isDistinction [.undefinedExistent, .undefinedExistent] = false := rfl

/-! ### the triad -- steps 0.1, 0.4, 0.6, POSTULATE -/

/-- Step 0.1 (POSTULATE). Registration 1 is the existence bound: all-that-is against
    non-existence. Encoded as the marker that a base IS all-that-is at registration 1; that
    existence is the founding distinction is stated, not proven. -/
def registrationOne (b : Base) : Prop := ∀ x ∈ b, perceivable x = true

/-- Step 0.4/0.6 (POSTULATE -- the working hypothesis). A registration is produced by three
    observers, two within and one without, whose live agreement IS the artifact (a
    distinction). The structure REQUIRES three observers to build one -- but its existing
    does not prove all three are present already at registration 1. That is instinct, held
    as postulate, with no handle yet to derive it. `Observer` is left abstract: the source
    names the observer as an object but does not say what it is. -/
structure Registration (Observer : Type) where
  within1  : Observer
  within2  : Observer
  without  : Observer
  artifact : Base
  registers : isDistinction artifact = true

/-- The observers are NOT the registration: the artifact is a separate field, their
    product. Reading it back is a projection, never an identification. -/
def Registration.record {Observer : Type} (R : Registration Observer) : Base := R.artifact

-- Axiom report on the DERIVED theorems only (the postulates are structures, not claims):
#print axioms undefined_ne_nonexistent
#print axioms defined_perceivable
#print axioms undefined_perceivable
#print axioms nonexistent_not_perceivable
#print axioms base_is_distinction
#print axioms all_defined_is_not_a_distinction
#print axioms none_defined_is_not_a_distinction

end Container00
