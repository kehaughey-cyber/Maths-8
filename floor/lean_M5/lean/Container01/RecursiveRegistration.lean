/-
  CONTAINER 01 -- RECURSIVE REGISTRATION . rung 1, rests on container 00

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  On the corrected floor: registration 2+ subdivides the RESIDUAL of all-that-is,
  positively (defined | undefined, no is-not); the extents NEST while co-definition is a
  LIVE web by adjacency. Imports container 00 and reuses its Existential / isDistinction /
  three-observer Registration. DERIVED (zero axioms): each stage is a distinction, the
  residual nests. POSTULATE: the triad carries up, adjacency co-definition. OWED (not
  built): adjacency -> 12 -> the icosahedron.
-/

import Container00.Distinction

namespace Container01
open Container00

/-! ### registration 2+ subdivides the residual, positively -- steps 1.1-1.3, DERIVED -/

/-- The residual: the undefined-existent things, selected POSITIVELY (= undefined), never
    as `not the state`. -/
def residual (b : Base) : Base := b.filter (· == .undefinedExistent)

/-- A concrete subdivision of all-that-is. stage0 is registration 1's residual (all
    undefined); each further registration DEFINES one more, leaving a nested residual. -/
def stage0 : Base := [.undefinedExistent, .undefinedExistent, .undefinedExistent]
def stage1 : Base := [.definedExistent,   .undefinedExistent, .undefinedExistent]
def stage2 : Base := [.definedExistent,   .definedExistent,   .undefinedExistent]

/-- Step 1.2. Each registration -- a defined thing with a residual left -- is exactly a
    container-00 distinction. THE DEPENDENCY on 00. -/
theorem stage1_is_distinction : isDistinction stage1 = true := rfl
theorem stage2_is_distinction : isDistinction stage2 = true := rfl

/-- Step 1.3. The residual nests: its extent strictly shrinks, 3 -> 2 -> 1, so what is
    defined stays defined and the undefined never re-covers it -- the positive form of
    non-overlap. -/
theorem residual_stage0_len : (residual stage0).length = 3 := rfl
theorem residual_stage1_len : (residual stage1).length = 2 := rfl
theorem residual_stage2_len : (residual stage2).length = 1 := rfl

/-! ### the triad carries up -- step 1.5, POSTULATE -/

/-- POSTULATE. Every registration is registered by three observers (container 00): any
    distinction-stage lifts to a `Registration`, given the three. That the three ARE present
    is the working hypothesis carried up from rung 0 -- encoded, not proven. -/
def liftToRegistration {Obs : Type} (within1 within2 without : Obs)
    (b : Base) (h : isDistinction b = true) : Registration Obs :=
  { within1, within2, without, artifact := b, registers := h }

/-! ### co-definition by adjacency -- step 1.4, POSTULATE; step 1.6 OWED -/

/-- POSTULATE. A registration co-defines with its ADJACENT registrations, live: a local
    web, not all-to-all, in which change propagates STEPWISE (the 'inject'). Encoded as an
    abstract adjacency relation on registration indices; its structure is stated, its being
    live is not a kernel fact. -/
structure Adjacency where
  adj      : Nat → Nat → Prop
  symm     : ∀ i j, adj i j → adj j i

-- OWED (NOT built here): the number of adjacencies a registration can carry is 12, and
-- thus the icosahedron. That proof lands at container 05/06; it is not smuggled into the
-- floor. See derivation.py step 1.6.

#print axioms stage1_is_distinction
#print axioms stage2_is_distinction
#print axioms residual_stage0_len
#print axioms residual_stage1_len
#print axioms residual_stage2_len

end Container01
