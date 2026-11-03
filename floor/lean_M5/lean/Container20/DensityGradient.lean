/-
  CONTAINER 20 -- DENSITY GRADIENT: gravity = the change in packing. Rests on 13, 14.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 8, the gradient mechanism on a small explicit graph. Mathlib-FREE, ZERO-axiom by `decide`.
  A central low-rho vertex 0 (a "twelve" analog) with higher-rho neighbours 1..4:
    - GAUSS LAW: sum_v L(v) = 0 (each edge cancels) -- gravity sources sum to zero on the closed graph;
    - SOURCE SIGN: the local minimum 0 is a positive source, L 0 > 0.
  The full R3/R4/R5 computation (localization, Gauss at every level, grad(rho) = -grad(deficit)) is
  exact-Python in derivation.py. G.4 (gravity = grad(rho); the not-a-field-equation checked-negative)
  is a POSTULATE -- no Lean.
-/

namespace Container20

/-- Each vertex as (its own rho, the rhos of its neighbours) -- a 5-vertex star, centre 0 a local
    minimum (rho 3) joined to higher-rho leaves. Avoids list indexing (List.get? is gone). -/
def graph : List (Int × List Int) :=
  [ (3, [5, 5, 6, 5]),   -- centre 0: the "twelve" analog, a local minimum
    (5, [3]),            -- leaf 1
    (5, [3]),            -- leaf 2
    (6, [3]),            -- leaf 3
    (5, [3]) ]           -- leaf 4

/-- the graph Laplacian at a vertex: L = sum over neighbours of (rho(w) - rho(v)). -/
def Lof (p : Int × List Int) : Int := p.2.foldl (fun acc w => acc + (w - p.1)) 0
def totalL : Int := (graph.map Lof).foldl (· + ·) 0

def Lcentre : Int := Lof (3, [5, 5, 6, 5])
def Lleaf3  : Int := Lof (6, [3])

/-- THE DISCRETE GAUSS LAW: the gravity sources sum to zero on the closed graph (each edge cancels). -/
theorem gauss_sources_sum_to_zero : totalL = 0 := by decide

/-- THE SOURCE SIGN: the local minimum (the centre, the "twelve" analog) is a POSITIVE source. -/
theorem local_minimum_is_positive_source : Lcentre > 0 := by decide

/-- A leaf (higher rho) is a negative sink -- the balance the Gauss law enforces. -/
theorem leaf_is_a_sink : Lleaf3 < 0 := by decide

#print axioms gauss_sources_sum_to_zero
#print axioms local_minimum_is_positive_source
#print axioms leaf_is_a_sink

end Container20
