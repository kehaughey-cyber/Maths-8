/-
  CONTAINER 03 -- DIMENSIONAL EMERGENCE . rung 3, rests on 01/02

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  THE RETRACTION AND THE CORRECTION. maths 4's first rung 3 read 'mutually related' as a
  CLIQUE and got the tetrahedron; that was retracted (adjacency is local, a path). But the
  CORRECTION exists, machine-checked: closure ALONE (Euler + triangular faces + uniform
  degree, NO clique) forces exactly (d,V) = (3,4), (4,6), (5,12), and the three-observer
  condition selects the icosahedron. DERIVED here. The counting uses `omega` (Lean-core),
  so those two carry [propext, Quot.sound, Classical.choice]; the witnesses and selection
  are decidable. OWED: the upper bound (that the dimension is 3 and not more).
-/

namespace Container03

/-! ### the retraction: clique vs the local path -- step 3.2, DERIVED (zero axioms) -/

def isTri (adj : Nat → Nat → Bool) (i j k : Nat) : Bool := adj i j && adj i k && adj j k
def triCount (n : Nat) (adj : Nat → Nat → Bool) : Nat :=
  ((List.range n).flatMap fun i => (List.range n).flatMap fun j => (List.range n).filterMap fun k =>
    if decide (i < j) && decide (j < k) && isTri adj i j k then some (i,j,k) else none).length
def adjClique (i j : Nat) : Bool := i != j
def adjPath (i j : Nat) : Bool := (i + 1 == j) || (j + 1 == i)

theorem clique_has_triangles : triCount 4 adjClique = 4 := by decide
theorem local_path_has_none  : triCount 4 adjPath = 0 := by decide

/-! ### the correction: closure forces the trichotomy -- step 3.3, DERIVED (omega) -/

/-- Twelve degree-5 vertices are forced in any closed 5/6-degree triangular mesh. -/
theorem twelve_forced (V E Fc n5 n6 : Nat)
    (euler : V + Fc = E + 2) (tri : 3 * Fc = 2 * E)
    (verts : V = n5 + n6) (deg : 5 * n5 + 6 * n6 = 2 * E) : n5 = 12 := by omega

/-- A closed uniform-degree triangular mesh is the tetrahedron, octahedron, or icosahedron
    count -- nothing else. NO clique assumed anywhere; pure closure counting. -/
theorem closure_trichotomy (V E Fc d : Nat) (hd : 3 ≤ d)
    (euler : V + Fc = E + 2) (tri : 3 * Fc = 2 * E) (deg : d * V = 2 * E) :
    (d = 3 ∧ V = 4) ∨ (d = 4 ∧ V = 6) ∨ (d = 5 ∧ V = 12) := by
  match d, hd, deg with
  | 0, hd, _ => exact absurd hd (by decide)
  | 1, hd, _ => exact absurd hd (by decide)
  | 2, hd, _ => exact absurd hd (by decide)
  | 3, _, deg => omega
  | 4, _, deg => omega
  | 5, _, deg => omega
  | (n + 6), _, deg => rw [Nat.add_mul] at deg; omega

/-! ### the three shells exist, verified -- DERIVED, and selection -- step 3.4 -/

abbrev Face := Nat × Nat × Nat
def norm (a b : Nat) : Nat × Nat := if a ≤ b then (a, b) else (b, a)
def faceEdges (f : Face) : List (Nat × Nat) := [norm f.1 f.2.1, norm f.1 f.2.2, norm f.2.1 f.2.2]
def allEdges (faces : List Face) : List (Nat × Nat) :=
  (faces.flatMap faceEdges).foldl (fun acc e => if acc.contains e then acc else e :: acc) []
def faceOk (V : Nat) (f : Face) : Bool :=
  f.1 < V && f.2.1 < V && f.2.2 < V && f.1 != f.2.1 && f.1 != f.2.2 && f.2.1 != f.2.2
def meshOk (V d : Nat) (faces : List Face) : Bool :=
  let E := allEdges faces
  faces.all (faceOk V)
  && E.all (fun e => (faces.filter (fun f => (faceEdges f).contains e)).length == 2)
  && (List.range V).all (fun v => (E.filter (fun e => e.1 == v || e.2 == v)).length == d)
  && (V + faces.length == E.length + 2)

def tetraFaces : List Face := [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
def octaFaces  : List Face := [(0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)]
def icosaFaces : List Face := [(0, 1, 2), (0, 1, 7), (0, 2, 6), (0, 6, 8), (0, 7, 8), (1, 2, 5), (1, 3, 5), (1, 3, 7), (2, 4, 5), (2, 4, 6), (3, 5, 9), (3, 7, 11), (3, 9, 11), (4, 5, 9), (4, 6, 10), (4, 9, 10), (6, 8, 10), (7, 8, 11), (8, 10, 11), (9, 10, 11)]

/- The three uniform closures exist -- each a closed triangular mesh, Euler char 2. -/
set_option maxRecDepth 8192 in
theorem closures_exist :
    (meshOk 4 3 tetraFaces && meshOk 6 4 octaFaces && meshOk 12 5 icosaFaces) = true := by decide

/-- v and w are SEPARATED when some third vertex relates differently to each -- the
    three-observer condition. -/
def adjOf (E : List (Nat × Nat)) (a b : Nat) : Bool := E.contains (norm a b)
def separated (V : Nat) (E : List (Nat × Nat)) (v w : Nat) : Bool :=
  (List.range V).any (fun u => u != v && u != w && (adjOf E u v != adjOf E u w))
def unseparatedCount (V : Nat) (faces : List Face) : Nat :=
  let E := allEdges faces
  ((List.range V).flatMap fun v => (List.range V).filterMap fun w =>
    if decide (v < w) && ! separated V E v w then some (v, w) else none).length

/- Selection: exactly the icosahedron separates every pair (0 unseparated); the tetrahedron
   fails all 6 pairs, the octahedron 3. The triad forces d = 5 and the twelve. -/
set_option maxRecDepth 8192 in
theorem icosahedron_uniquely_separated :
    unseparatedCount 4 tetraFaces = 6
    ∧ unseparatedCount 6 octaFaces = 3
    ∧ unseparatedCount 12 icosaFaces = 0 := by decide

/-! ### the upper bound is NOT established -- step 3.6, DERIVED (the D4 counterexample) -/

/-- The D4 root system: the 24 vectors (+-e_i +- e_j). Its kissing set. -/
def d4Roots : List (List Int) := [[1, 1, 0, 0], [1, -1, 0, 0], [-1, 1, 0, 0], [-1, -1, 0, 0], [1, 0, 1, 0], [1, 0, -1, 0], [-1, 0, 1, 0], [-1, 0, -1, 0], [1, 0, 0, 1], [1, 0, 0, -1], [-1, 0, 0, 1], [-1, 0, 0, -1], [0, 1, 1, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, -1, -1, 0], [0, 1, 0, 1], [0, 1, 0, -1], [0, -1, 0, 1], [0, -1, 0, -1], [0, 0, 1, 1], [0, 0, 1, -1], [0, 0, -1, 1], [0, 0, -1, -1]]
def dotI (u v : List Int) : Int := (List.zipWith (· * ·) u v).foldl (· + ·) 0

/-- All 24 D4 roots are pairwise at angle >= 60 degrees (integer inner product <= 1), so
    THIRTEEN or more fit as simultaneous neighbours at d = 4 -- d = 4 is NOT excluded, and
    the upper bound dim = 3 does not follow. The substrate's no-thirteenth is topological
    (Euler: exactly twelve at any d), never metric; the sphere is not saturated by twelve.
    (The sphere's 3*sqrt3 - 5 ~ 19.6% uncovered fraction is irrational; it lives in the
    derivation, not this integer file.) -/
theorem d4_admits_thirteen :
    (d4Roots.length == 24)
    ∧ (d4Roots.all (fun u => d4Roots.all (fun v => (dotI u v <= 1) || (u == v)))) = true := by
  refine ⟨by decide, ?_⟩
  decide

-- POSTULATE (step 3.1): geometry is derived, not assumed -- the discipline that exposed the
-- imposed clique. OWED (step 3.7): a METRIC no-thirteenth from the substrate -- nothing
-- supplies one. The lower bound dim >= 3 follows from the tetrahedron minimum (4 mutually
-- adjacent = equidistant) via the geometric-balance bridge postulate.

#print axioms clique_has_triangles
#print axioms local_path_has_none
#print axioms twelve_forced
#print axioms closure_trichotomy
#print axioms closures_exist
#print axioms icosahedron_uniquely_separated
#print axioms d4_admits_thirteen

end Container03
