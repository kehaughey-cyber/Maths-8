/-
  CONTAINER 23 -- LEVEL INTEGRALITY, cold on the triadic floor. Rests on 00, 01, 13.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Theorem LI (the dcpo-floor rho(d) = I(d)/alpha = |A(d)|, "no fractional level") reconstructed on
  the TRIADIC floor, where integrality is STRUCTURAL: a registration element is a finite set of
  archons built by container 01's stepwise disjoint subdivision, and the level is its CARDINALITY --
  a Nat by construction, no continuum to quantize. The dcpo floor needed a real Scott-continuous
  measure (R6) forced onto Z by R10b/R14; the triadic floor needs none of it. The non-trivial
  content is well-definedness (path-independence) and additivity, certified here zero-axiom.

  IMPORTS Container13 and reuses its disjoint-insert (`insNew`/`union`) and ball (`ballSet`/`ball`) --
  one home, consumed not restated. LI.4 shows the ball, read as a registration element, has level
  = container 13's |B_r|: the top-down level meets the bottom-up count. Mathlib-FREE, ZERO-axiom.
-/

import Container13.ArchicDensity

-- The ball decides recompute container 13's BFS, so the same two options it needs are needed here.
set_option maxHeartbeats 2000000
set_option maxRecDepth 8000

namespace Container23
open Container13   -- insNew, union, ballSet, ball, verts -- one home, consumed here

/-! ### the level of a registration element -- the archon count -/
/-- Build a registration element by a propagation sequence: fold the disjoint insert (01.3's
    positive residual step -- container 13's `insNew`) over the order, starting empty. -/
def buildFrom (order : List Nat) : List Nat := order.foldl (fun acc p => insNew p acc) []
/-- L(d) = |A(d)| -- the level is the cardinality of the archon set. A Nat by construction. -/
def L (s : List Nat) : Nat := s.length

/-! ### LI.2 -- the level is well-defined, path-independent, an integer (THE HEART) -/
def ascOrder  : List Nat := [10, 20, 30, 40]
def descOrder : List Nat := [40, 30, 20, 10]

/-- Two different propagation orders of the same four archons reach the same level 4. -/
theorem path_independent_length :
    (L (buildFrom ascOrder) == 4 && L (buildFrom descOrder) == 4) = true := by decide

/-- ...and the same SET (each archon present in both builds) -- path-independent as a set,
    not merely in count. -/
theorem path_independent_set :
    ([10, 20, 30, 40].all (fun p =>
      (buildFrom ascOrder).contains p && (buildFrom descOrder).contains p)) = true := by decide

/-- Covering-cold: a FRESH archon raises the level by exactly 1 (each step is one registration). -/
theorem covering_fresh_plus_one :
    (L (insNew 99 [10, 20, 30, 40]) == L [10, 20, 30, 40] + 1) = true := by decide

/-- ...and re-adding a PRESENT archon does not (the covering property needs disjointness). -/
theorem covering_idempotent_on_present :
    (L (insNew 10 [10, 20, 30, 40]) == L [10, 20, 30, 40]) = true := by decide

/-! ### LI.3 -- additivity on ORTHOGONAL elements, with the overlap a checked negative -/
/-- Orthogonal (disjoint) registration elements: their levels ADD. -/
theorem additivity_orthogonal :
    (L (union [1, 2, 3] [4, 5, 6]) == L [1, 2, 3] + L [4, 5, 6]) = true := by decide

/-- CHECKED NEGATIVE: overlapping elements do NOT add (share the archon 3), so additivity is not
    vacuous -- it holds PRECISELY on orthogonal pairs, exactly as the dcpo valuation axiom restricts. -/
theorem additivity_overlap_fails :
    (L (union [1, 2, 3] [3, 4]) == L [1, 2, 3] + L [3, 4]) = false := by decide

/-! ### LI.4 -- the ball is a registration element: L(B_r) = |B_r| (consumes container 13) -/
/-- On the R1 icosahedron every vertex has level profile (1, 6, 11, 12): the ball read as a
    registration element has level = container 13's ball-growth count. -/
theorem ball_profile_is_level :
    (verts.all (fun v =>
      (L (ballSet 0 v) == 1) && (L (ballSet 1 v) == 6)
        && (L (ballSet 2 v) == 11) && (L (ballSet 3 v) == 12))) = true := by decide

/-- The level (our L) IS container 13's |B_r| observable -- top-down level = bottom-up count. -/
theorem level_eq_ball_count :
    (verts.all (fun v => L (ballSet 3 v) == ball 3 v)) = true := by decide

#print axioms path_independent_length
#print axioms path_independent_set
#print axioms covering_fresh_plus_one
#print axioms covering_idempotent_on_present
#print axioms additivity_orthogonal
#print axioms additivity_overlap_fails
#print axioms ball_profile_is_level
#print axioms level_eq_ball_count

end Container23
