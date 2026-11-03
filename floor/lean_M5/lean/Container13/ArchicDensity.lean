/-
  CONTAINER 13 -- ARCHIC DENSITY: the ball-growth observable |B_r(v)|. Rests on 03.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 1 of the physics-bridge arc, the R1 (icosahedron) core. Mathlib-FREE and ZERO-axiom by
  `decide`: the icosahedron adjacency (container 03's selected shell, re-derived cold) is a closed
  degree-5 triangular mesh, and the ball-growth observable |B_r(v)| = (1, 6, 11, 12) for every
  vertex, with the relabelling identity |B_1(v)| = deg(v) + 1.

  BFS is done as MONOTONE SET-GROWTH (a fixed union-into-set per radius), so the kernel work is
  linear in the radius -- not the exponential recomputation a path predicate would force. The
  strict-refinement half of A.3 (R3: ball growth splits the degree-6 vertices) is 162 vertices and
  is checked by exact integer computation in derivation.py / the model, not in the kernel.
-/

-- A big-list `decide` needs BOTH raised: maxHeartbeats (elaboration timeout) AND maxRecDepth (the
-- list-fold/flatMap recursion depth). One alone is not enough (the container-12 lesson).
set_option maxHeartbeats 2000000
set_option maxRecDepth 8000

namespace Container13

/-! ### the R1 adjacency -- the icosahedron, 30 edges (guarded against derivation.json) -/
def edges : List (Nat × Nat) := [(0, 1), (0, 2), (0, 4), (0, 6), (0, 8), (1, 2), (1, 5), (1, 6), (1, 7), (2, 3), (2, 7), (2, 8), (3, 7), (3, 8), (3, 9), (3, 10), (4, 6), (4, 8), (4, 10), (4, 11), (5, 6), (5, 7), (5, 9), (5, 11), (6, 11), (7, 9), (8, 10), (9, 10), (9, 11), (10, 11)]
def verts : List Nat := List.range 12
/-- Undirected adjacency: an unordered pair is an edge. -/
def adj (a b : Nat) : Bool :=
  edges.any (fun e => (e.1 == a && e.2 == b) || (e.1 == b && e.2 == a))
def nbrs (v : Nat) : List Nat := verts.filter (fun w => adj v w)
def deg (v : Nat) : Nat := (nbrs v).length

/-! ### ball growth |B_r(v)| as monotone set-growth over adjacency (no distance) -/
/-- Add x to s only if absent -- a duplicate-free union, so no Mathlib `dedup` is needed. -/
def insNew (x : Nat) (s : List Nat) : List Nat := if s.contains x then s else x :: s
def union (a b : List Nat) : List Nat := b.foldl (fun acc x => insNew x acc) a
/-- One breadth-first step: union in every current member's neighbours. -/
def expand (s : List Nat) : List Nat := s.foldl (fun acc v => union acc (nbrs v)) s
/-- The set of registrations within r adjacency steps of v. -/
def ballSet : Nat → Nat → List Nat
  | 0,     v => [v]
  | k + 1, v => expand (ballSet k v)
/-- |B_r(v)| -- the archic-density observable. -/
def ball (r v : Nat) : Nat := (ballSet r v).length

/-! ### A.1 (R1) -- the closed degree-5 triangular mesh -/
theorem edge_count_thirty : (edges.length == 30) = true := by decide

theorem all_degree_five : (verts.all (fun v => deg v == 5)) = true := by decide

/-- Facial triangles = the 3-cliques; counted over all ordered triples, so each is counted 6 times. -/
def triCount : Nat :=
  ((verts.flatMap fun a =>
      verts.flatMap fun b =>
        verts.filter fun c => adj a b && adj a c && adj b c).length) / 6

theorem twenty_triangular_faces : (triCount == 20) = true := by decide

/-- Euler V - E + F = 2, written additively (V + F = E + 2) so Nat subtraction never truncates:
    12 + 20 = 30 + 2. -/
theorem euler_characteristic_two : (verts.length + triCount == edges.length + 2) = true := by decide

/-! ### A.2 (R1) -- the ball-growth observable is (1, 6, 11, 12) for every vertex -/
theorem ball_profile_uniform :
    (verts.all (fun v =>
      (ball 0 v == 1) && (ball 1 v == 6) && (ball 2 v == 11) && (ball 3 v == 12))) = true := by
  decide

/-! ### A.3 (R1) -- the relabelling identity: |B_1(v)| = deg(v) + 1 -/
theorem ball_one_eq_deg_plus_one :
    (verts.all (fun v => ball 1 v == deg v + 1)) = true := by decide

#print axioms edge_count_thirty
#print axioms all_degree_five
#print axioms twenty_triangular_faces
#print axioms euler_characteristic_two
#print axioms ball_profile_uniform
#print axioms ball_one_eq_deg_plus_one

end Container13
