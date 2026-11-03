/-
  CONTAINER 10 -- WHY-12, the phase-ledger TRIG PROVENANCE, proved IN-REPO.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  This module retires container 10's cited debt (W.2). The counting core (WhyTwelve.lean) is
  Mathlib-free and zero-axiom (12 = 12 fills, 13 > 12 overflows, in radits). The TRIG
  provenance that gives one radit its value pi/6 was CITED from maths-4
  REFRAME-PHASE-LEDGER-ARITHMETIC because Maths 5 had no Real. With Mathlib set up it is
  PROVED here: arcsin(1/2) = pi/6, twelve of them saturate 2pi, a thirteenth overflows, and
  the split-write capacity is exactly 12.

  AXIOM TIER: this module `import Mathlib`, so its theorems widen to Mathlib's three standard
  axioms (propext, Classical.choice, Quot.sound) -- confirmed by `#print axioms` below. This
  does NOT affect WhyTwelve.lean, which imports no Mathlib and stays zero-axiom. Proofs are
  ported from maths-4 formal/Closure/PhaseLedger.lean (same Lean/Mathlib pins).
-/

import Mathlib

open Real

namespace Container10

/-- The kissing contact half-angle is exactly pi/6: a neighbor of radius r at center distance
    2r subtends arcsin(r/2r) = arcsin(1/2). (This is what makes one adjacency cost pi/6.) -/
theorem kissing_half_angle : arcsin (1/2) = π/6 := by
  rw [show (1/2 : ℝ) = sin (π/6) by rw [sin_pi_div_six]]
  exact arcsin_sin (by linarith [pi_pos]) (by linarith [pi_pos])

/-- 12 adjacencies at pi/6 each spend the 2pi cycle EXACTLY (the saturation W.2 counts). -/
theorem phase_ledger_saturates_at_twelve : (12 : ℝ) * (π/6) = 2 * π := by ring

/-- A 13th adjacency strictly OVERFLOWS the cycle (the overflow W.2 counts). -/
theorem thirteenth_overflows : 2 * π < (13 : ℝ) * (π/6) := by
  have h := pi_pos
  linarith

/-- The full shared interface between two same-sized registrations in contact has angular
    width 2*arcsin(1/2) = pi/3; split equally between the two co-owners, pi/6 each. -/
theorem shared_interface_width : 2 * arcsin (1/2) = π/3 := by
  rw [kissing_half_angle]; ring

/-- Ledger capacity under SPLIT writes (pi/6 each): exactly twelve -- the value the
    Mathlib-free counting core (cycleRadits = 12) takes as given. -/
theorem capacity_split : (2 * π) / (π/6) = 12 := by
  have hpi : π ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

#print axioms kissing_half_angle
#print axioms phase_ledger_saturates_at_twelve
#print axioms thirteenth_overflows
#print axioms shared_interface_width
#print axioms capacity_split

end Container10
