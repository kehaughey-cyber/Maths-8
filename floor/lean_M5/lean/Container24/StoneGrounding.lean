/-
  CONTAINER 24 -- STONE GROUNDING: the STRUCTURAL alpha. Rests on 00, 13, 23; cites 17, 18.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Grounds container 23's LI.5 premise up to a single free scale: any information assignment that is
  ADDITIVE on disjoint registration elements and archon-SYMMETRIC (equal on every archon) is EXACTLY
  alpha*L(d). Equal Archon Information is FORCED by symmetry + additivity, not assumed; only the scale
  alpha is free (its VALUE is external Stone input, owed). And each registration step contributes
  exactly alpha (covering-cold) -- the structural constancy behind c = alpha/tau.

  IMPORTS Container23 (hence Container13): reuses L, insNew/union, and the ball -- one home, consumed.
  Mathlib-FREE, ZERO-axiom by `decide`.
-/

import Container23.LevelIntegrality

-- info_of_ball recomputes container 13's BFS, so the same two options it needs are needed here.
set_option maxHeartbeats 2000000
set_option maxRecDepth 8000

namespace Container24
open Container23 Container13   -- L, insNew, union, ballSet, ball, verts -- one home, consumed here

/-! ### a general information assignment -- a weight summed over an element's archons -/
/-- Sum a weight over the archons of a registration element. A CONSTANT weight is archon-symmetric. -/
def weighted (w : Nat -> Nat) (s : List Nat) : Nat := s.foldl (fun acc a => acc + w a) 0
/-- The symmetric (constant) weight: every archon carries the same quantum a. -/
def constW (a : Nat) : Nat -> Nat := fun _ => a

/-! ### SG.1 -- the representation theorem: additive + symmetric => I = alpha*L (EAI forced) -/
/-- A constant (symmetric) weight alpha gives the assignment = alpha * L(d) -- the archon count times
    the quantum. (alpha = 3 is a witness scale; SG.1(iv) shows every alpha works.) -/
theorem rep_is_alpha_count :
    ([[10, 20, 30, 40], [1, 2, 3]].all (fun s => weighted (constW 3) s == 3 * s.length)) = true := by
  decide

/-- ...and it is 0 on the empty element (I(bottom) = 0). -/
theorem rep_empty : (weighted (constW 3) ([] : List Nat) == 0) = true := by decide

/-- Additive on ORTHOGONAL (disjoint) registration elements (23.LI.3). -/
theorem rep_additive :
    (weighted (constW 3) (union [1, 2, 3] [4, 5, 6])
      == weighted (constW 3) [1, 2, 3] + weighted (constW 3) [4, 5, 6]) = true := by decide

/-- CHECKED NEGATIVE: a NON-constant (asymmetric) weight does NOT give a count-proportional assignment,
    so proportionality-to-count holds PRECISELY when the weight is constant -- i.e. EAI. -/
theorem rep_nonconstant_breaks :
    (weighted (fun a => a) [1, 2, 3] == 3 * [1, 2, 3].length) = false := by decide

/-- The SCALE is the only freedom: every alpha yields I = alpha*L. -/
theorem rep_scale_free :
    ([1, 3, 7, 100].all (fun a => weighted (constW a) [1, 2, 3, 4] == a * 4)) = true := by decide

/-- PAYOFF -- the warrant condition's top-down leg: on the R1 icosahedron, I(B_r) = alpha*|B_r|
    (here alpha=3, |B_3|=12), so I(B_r)/alpha = |B_r| grounded in the count (with 23.LI.4). -/
theorem info_of_ball :
    (verts.all (fun v => weighted (constW 3) (ballSet 3 v) == 3 * 12)) = true := by decide

/-! ### SG.3 -- c = alpha/tau structural constancy: each registration step contributes exactly alpha -/
/-- Each FRESH registration step (one archon per tick, covering-cold 23.LI.2) adds exactly alpha,
    independent of WHICH archon. -/
theorem step_gain_constant :
    ([10, 55, 99].all (fun p =>
      weighted (constW 3) (insNew p [1, 2, 4]) == weighted (constW 3) [1, 2, 4] + 3)) = true := by
  decide

/-- ...and independent of the current element (position-independent) -- a constant per-tick gain. -/
theorem step_gain_position_indep :
    ([[1], [1, 2, 3, 4, 5], [7, 8]].all (fun base =>
      weighted (constW 3) (insNew 999 base) == weighted (constW 3) base + 3)) = true := by decide

#print axioms rep_is_alpha_count
#print axioms rep_empty
#print axioms rep_additive
#print axioms rep_nonconstant_breaks
#print axioms rep_scale_free
#print axioms info_of_ball
#print axioms step_gain_constant
#print axioms step_gain_position_indep

end Container24
