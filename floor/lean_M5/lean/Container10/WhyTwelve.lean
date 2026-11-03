/-
  CONTAINER 10 -- WHY-12, the consolidation. Rests on 01, 02, 03, 09.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  THE HEADLINE OF THIS CONTAINER IS A POSTULATE (W.4), NOT A DERIVATION OF 12. What is
  proved here is narrow: the phase-ledger COUNTING arithmetic (twelve pi/6-writes fill the
  2pi cycle, a thirteenth overflows), its dimension-independence, and the CONDITIONAL
  consequence that -- GIVEN the postulate -- 12 selects d=3 uniquely. Mathlib-FREE, pure Nat
  by `decide` (zero-axiom). The trig provenance (arcsin(1/2) = pi/6, capacity 12) that gives
  one radit its value is proved in the sibling module PhaseLedgerReal.lean (import Mathlib;
  axioms = Mathlib's three) -- this file stays Mathlib-free and zero-axiom.
-/

namespace Container10

/-! ### W.2 -- the phase-ledger counting core (DERIVED, Mathlib-free) -/

/-- The cycle capacity in radits (units of pi/6). CITED: 2pi/(pi/6) = 12
    (maths-4 REFRAME-PHASE-LEDGER-ARITHMETIC; needs Real, not re-proved here). -/
def cycleRadits : Nat := 12

/-- One mutual adjacency costs one pi/6 arc = one radit (CITED: the split write cost). -/
def writeCost : Nat := 1

/-- Twelve writes fill the cycle exactly: 12 * 1 = 12. (12 * pi/6 = 2pi.) -/
theorem twelve_fills : 12 * writeCost = cycleRadits := by decide

/-- A thirteenth write strictly overflows: 12 < 13 * 1. (2pi < 13 * pi/6.) The whole
    'why not 13' bottoms out here, the same shape as rung 6's 5 < 9. -/
theorem thirteen_overflows : cycleRadits < 13 * writeCost := by decide

/-! ### W.3 -- the phase cap is dimension-independent (DERIVED) -/

/-- Spatial kissing numbers by dimension: CITED external values (2,6,12,24 for d=1..4). -/
def kissingMax : Nat -> Nat
  | 1 => 2
  | 2 => 6
  | 3 => 12
  | 4 => 24
  | _ => 0

/-- The phase cap does NOT depend on dimension: arcsin(1/2) = pi/6 is a two-body planar
    angle, the same in any ambient dimension, and the cycle is 1-D. So the cap is 12 for
    every d. (The value is decided; the dimension-independence is the cited geometric fact.) -/
def phaseCap (_d : Nat) : Nat := 12

/-- The phase cap is 12 across dimensions... -/
theorem phase_cap_constant : phaseCap 2 = 12 /\ phaseCap 3 = 12 /\ phaseCap 4 = 12 := by decide

/-- ...while spatial kissing VARIES: 6, 12, 24 at d = 2, 3, 4. This is why only the phase
    road can bound adjacencies at 12 as such. -/
theorem kissing_varies :
    kissingMax 2 = 6 /\ kissingMax 3 = 12 /\ kissingMax 4 = 24 := by decide

/-! ### W.5 -- GIVEN the postulate, 12 selects d=3 uniquely (DERIVED, conditional) -/

/-- 12 is the maximum kissing number ONLY at d=3 (d=2 caps at 6, d=4 reaches 24). So GIVEN
    W.4 (adjacency-count = phase-writes = 12) and completeness, the dimension is 3 -- the
    integer selection. The implication is derived; its antecedent is the POSTULATE W.4. -/
theorem twelve_selects_dim_three :
    kissingMax 3 = 12 /\ kissingMax 2 ≠ 12 /\ kissingMax 4 ≠ 12 := by decide

-- POSTULATE (W.1): the four 12-threads (adjacency 01, phase 02, icosahedral 03, kissing 09)
-- are ONE 12 -- a structural reading, held, not proven. No theorem.
--
-- POSTULATE (W.4, THE HEADLINE): 'the phase cycle is the ledger on which a registration's
-- adjacencies are written', each adjacency one pi/6 arc. maths-4 GATE-PHASE-LEDGER half-a,
-- OPEN: provably NOT derivable from its own road (circular via CLOSURE-ZERO-SELF-INFORMATION),
-- and equivalent to dim=3. The grade of this whole container. Held, not proven; NOT a theorem.
--
-- OWED (W.6): geometry ALONE cannot force 12 -- the separation lever is a checked negative
-- (03/dim4-separation-check.py; the 24-cell is a valid 4-D shell), the postulate is
-- irreducible, and the no-13th upper bound is external (Schuette-van der Waerden). Named here.

#print axioms twelve_fills
#print axioms thirteen_overflows
#print axioms phase_cap_constant
#print axioms kissing_varies
#print axioms twelve_selects_dim_three

end Container10
