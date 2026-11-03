/-
  CONTAINER 09 -- KISSING-TWELVE, the metric SURFACE SLACK, proved IN-REPO.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The Mathlib-free core (KissingTwelve.lean) proves the twelve spheres RATTLE combinatorially: every
  pairwise dist^2 exceeds R^2, the edge gap 2 - phi > 0 bottoming out at 5 < 9, exact in Z[phi]. THIS
  module gives the METRIC companion, which needs a real square root: the twelve contact caps
  (half-angle pi/6 = arcsin(1/2)) leave the central sphere's surface exactly 3*sqrt 3 - 5 uncovered --
  strictly between 0 and 1. Saturation on the 1-D phase circle (twelve pi/6 arcs fill 2pi, container
  10), frustration on the 2-D surface (this slack): one angle pi/6 doing both. maths-4's
  REFRAME-PHASE-LEDGER-ARITHMETIC surface half, CITED while Maths 5 had no Real; proved here.

  AXIOM TIER: this module `import Mathlib`, so its theorems widen to Mathlib's three standard axioms
  (propext, Classical.choice, Quot.sound) -- confirmed by `#print axioms` below. This does NOT affect
  KissingTwelve.lean, which imports no Mathlib and stays zero-axiom. Proofs are ported from maths-4
  formal/Closure/PhaseLedger.lean (same Lean/Mathlib pins).

  NOT here: the upper bound (no 13th) -- Schuette-van der Waerden, external, cited (KissingTwelve 6.6).
-/

import Mathlib

open Real

namespace Container09

/-- The surface slack in closed form: twelve caps of half-angle pi/6 (cap area fraction of a unit
    sphere at half-angle t is (1 - cos t)/2) leave uncovered fraction exactly 3*sqrt 3 - 5. -/
theorem surface_slack_exact :
    1 - 12 * ((1 - Real.cos (π/6)) / 2) = 3 * Real.sqrt 3 - 5 := by
  rw [cos_pi_div_six]
  ring

/-- The surface slack is strictly POSITIVE: the caps do NOT saturate the surface -- the "rattle room"
    that KissingTwelve.lean sees combinatorially (edge gap 2 - phi > 0), now the exact metric value. -/
theorem surface_slack_pos : 0 < 3 * Real.sqrt 3 - 5 := by
  nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 3), Real.sqrt_nonneg 3]

/-- And strictly less than one (the caps do cover most of the surface). So the uncovered fraction
    3*sqrt 3 - 5 ~ 19.6% lies strictly in (0,1). -/
theorem surface_slack_lt_one : 3 * Real.sqrt 3 - 5 < 1 := by
  nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 3), Real.sqrt_nonneg 3]

#print axioms surface_slack_exact
#print axioms surface_slack_pos
#print axioms surface_slack_lt_one

end Container09
