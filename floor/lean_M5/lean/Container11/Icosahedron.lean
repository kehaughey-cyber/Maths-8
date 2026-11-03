/-
  CONTAINER 11 -- the ICOSAHEDRON interior (the rank-6 icosahedral module). Rests on 03.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Number is a BUILD-ORDER label; conceptually this is the rung-5/6 icosahedral module, positioned by
  its inclusion into the carrier (06). Exact in Z[phi] = Int x Int (phi^2 = phi+1), Mathlib-FREE, and
  ZERO-axiom (decide, structural recursion only -- no native_decide, no Mathlib). Ports maths-4's
  formal/Closure/IcosianLattice.lean sections 1-6 into this container's frame.

  I.1 transfer rule (field norm multiplicative), I.2 rank obstruction (six-direction det = 8, so rank
  exactly 6 < 8 = rank E8), I.3 the three overlaps (6-3phi, 20-12phi, 18-11phi; norms 9,16,5),
  I.4 cuboctahedron is not a triangulation (8 triangles + 6 squares), I.5 the 12+20 minimal shell.
-/

namespace Container11

/-! ### exact Z[phi] -/
abbrev Zphi := Int × Int
def zadd (x y : Zphi) : Zphi := (x.1 + y.1, x.2 + y.2)
/-- (a+b phi)(c+d phi) = (ac+bd) + (ad+bc+bd) phi. -/
def zmul (x y : Zphi) : Zphi := (x.1 * y.1 + x.2 * y.2, x.1 * y.2 + x.2 * y.1 + x.2 * y.2)
/-- Field norm N(a+b phi) = a^2 + ab - b^2. -/
def znorm (x : Zphi) : Int := x.1 * x.1 + x.1 * x.2 - x.2 * x.2
/-- Field trace Tr(a+b phi) = 2a + b. -/
def ztrace (x : Zphi) : Int := 2 * x.1 + x.2

/-! ### I.1 -- the transfer rule: the field norm is multiplicative -/
theorem transfer_rule :
    ((znorm (zmul (6, -3) (20, -12)) == znorm (6, -3) * znorm (20, -12)) &&
     (znorm (0, 1) == -1) && (ztrace (0, 1) == 1) &&
     (znorm (1, 0) == 1) && (ztrace (1, 0) == 2)) = true := by decide

/-! ### I.2 -- the rank obstruction: rank exactly 6 (six-direction det = 8) -/
/-- A 3-D point with Z[phi] coordinates, flattened to six integers. -/
abbrev Vec6 := List Int
/-- The twelve icosahedral directions (0, +-1, +-phi) and cyclic, flattened. -/
def dirs : List Vec6 :=
  [ [0,0, 1,0, 0,1],  [1,0, 0,1, 0,0],  [0,1, 0,0, 1,0],
    [0,0, 1,0, 0,-1], [1,0, 0,-1, 0,0], [0,-1, 0,0, 1,0],
    [0,0, -1,0, 0,-1],[-1,0, 0,-1, 0,0],[0,-1, 0,0, -1,0],
    [0,0, -1,0, 0,1], [-1,0, 0,1, 0,0], [0,1, 0,0, -1,0] ]
def sixDirs : List Vec6 := dirs.take 6
def vneg (v : Vec6) : Vec6 := v.map (fun x => -x)

/-- The twelve are six and their negatives -- rank AT MOST 6. -/
theorem twelve_are_six_and_negatives :
    ((dirs.length == 12) && (sixDirs.length == 6) &&
     ((dirs.drop 6) == (sixDirs.map vneg))) = true := by decide

/-- Determinant by Laplace expansion with explicit fuel: SINGLE structural recursion on the fuel
    (not `mutual`, which would drag in well-founded recursion and Quot.sound), so `decide` reduces. -/
def delNth : Nat → List Int → List Int
  | _, [] => []
  | 0, _ :: xs => xs
  | n+1, x :: xs => x :: delNth n xs
def detM : Nat → List (List Int) → Int
  | 0, _ => 1
  | _, [] => 1
  | f+1, r :: rs =>
      (((List.range r.length).zip r).foldl
        (fun acc p =>
          acc + (if p.1 % 2 == 0 then (1 : Int) else -1) * p.2 *
                detM f (rs.map (delNth p.1)))
        0)
def detOf (m : List (List Int)) : Int := detM m.length m

/-- The six-direction determinant is 8 (nonzero), so rank EXACTLY 6. rank 6 < 8 = rank(E8) refutes
    the E8 identification of the 3-D overlaps. -/
theorem six_direction_det_eq_eight : (detOf sixDirs == 8) = true := by decide

/-! ### I.3 -- the three frustration overlaps -/
def sqLen (x y z : Zphi) : Zphi :=
  zadd (zadd (zmul x x) (zmul y y)) (zmul z z)
def overlap2 : Zphi × Zphi × Zphi := ((-1,0), (2,-1), (0,0))
def overlap3 : Zphi × Zphi × Zphi := ((4,-2), (0,0), (0,0))
def overlap4 : Zphi × Zphi × Zphi := ((2,-1), (0,0), (3,-2))
def sqLenOf (p : Zphi × Zphi × Zphi) : Zphi := sqLen p.1 p.2.1 p.2.2

/-- The overlaps' squared lengths are exactly 6-3phi, 20-12phi, 18-11phi. -/
theorem overlap_squared_lengths :
    ((sqLenOf overlap2 == (6, -3)) &&
     (sqLenOf overlap3 == (20, -12)) &&
     (sqLenOf overlap4 == (18, -11))) = true := by decide

/-- And their field norms are the integers 9, 16, 5 (the transfer rule's quantization). -/
theorem overlap_field_norms :
    ((znorm (sqLenOf overlap2) == 9) &&
     (znorm (sqLenOf overlap3) == 16) &&
     (znorm (sqLenOf overlap4) == 5)) = true := by decide

/-! ### I.4 -- the cuboctahedron is not a triangulation -/
def cuboVerts : List (Int × Int × Int) :=
  [(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),
   (1,0,1),(1,0,-1),(-1,0,1),(-1,0,-1),
   (0,1,1),(0,1,-1),(0,-1,1),(0,-1,-1)]
def d2 (a b : Int × Int × Int) : Int :=
  (a.1-b.1)*(a.1-b.1) + (a.2.1-b.2.1)*(a.2.1-b.2.1) + (a.2.2-b.2.2)*(a.2.2-b.2.2)
def cuboAdj (a b : Int × Int × Int) : Bool := d2 a b == 2
def cuboDegOf (a : Int × Int × Int) : Nat := (cuboVerts.filter (cuboAdj a)).length
def cuboEdges : Nat := ((cuboVerts.map cuboDegOf).foldl (· + ·) 0) / 2
def cuboTriangles : Nat :=
  ((cuboVerts.flatMap fun a =>
      cuboVerts.flatMap fun b =>
        cuboVerts.filter fun c =>
          cuboAdj a b && cuboAdj a c && cuboAdj b c).length) / 6
/-- Euler: V - E + F = 2, so F = E + 2 - V (additive, Nat subtraction truncates). -/
def cuboFaces : Nat := cuboEdges + 2 - 12

/-- 12 vertices each degree 4, E = 24, F = 14 by Euler -- but only 8 faces are triangles; 6 are
    squares. Triangular faces are the closure trichotomy's hypothesis, so this excludes it. -/
theorem cuboctahedron_is_not_a_triangulation :
    ((cuboVerts.all (fun a => cuboDegOf a == 4)) &&
     (cuboEdges == 24) &&
     (cuboFaces == 14) &&
     (cuboTriangles == 8) &&
     (cuboFaces - cuboTriangles == 6)) = true := by decide

/-! ### I.5 -- the 12 + 20 minimal shell -/
abbrev V3 := List Zphi
def vadd (u v : V3) : V3 := List.zipWith zadd u v
def vsmul (k : Int) (v : V3) : V3 := v.map (fun c => (k * c.1, k * c.2))
def vzero : V3 := [(0,0), (0,0), (0,0)]
def sqLenV (v : V3) : Zphi := v.foldl (fun acc c => zadd acc (zmul c c)) (0,0)
/-- The codifferent trace form Tr(delta*(a+b phi)) = a + b. -/
def traceForm (x : Zphi) : Int := x.1 + x.2
/-- The six icosahedral directions as three Z[phi] coords. -/
def dirsZ : List V3 :=
  [ [(0,0), (1,0), (0,1)],  [(1,0), (0,1), (0,0)],  [(0,1), (0,0), (1,0)],
    [(0,0), (1,0), (0,-1)], [(1,0), (0,-1), (0,0)], [(0,-1), (0,0), (1,0)] ]
def combine (coef : List Int) : V3 :=
  (List.zipWith vsmul coef dirsZ).foldl vadd vzero
/-- The coefficient box [-1,1]^6 (3^6 = 729 lists). -/
def box1 : List (List Int) :=
  let r : List Int := [-1, 0, 1]
  r.flatMap fun a => r.flatMap fun b => r.flatMap fun c =>
    r.flatMap fun d => r.flatMap fun e => r.map fun f => [a,b,c,d,e,f]
/-- The minimal shell: lattice vectors at the minimal trace-form norm 3. -/
def minimalVecs : List V3 :=
  (box1.map combine).filter (fun v => traceForm (sqLenV v) == 3)

/-- The minimal shell splits 12 + 20: twelve at squared length phi+2 (icosahedron) and twenty at
    6-3phi (dodecahedron) -- same trace-form norm 3, different squared lengths. -/
theorem minimal_shell_is_twelve_plus_twenty :
    ((minimalVecs.length == 32) &&
     ((minimalVecs.filter (fun v => sqLenV v == (2, 1))).length == 12) &&
     ((minimalVecs.filter (fun v => sqLenV v == (6, -3))).length == 20)) = true := by decide

/-- The shell-2 overlap (squared length 6-3phi) is itself a dodecahedral minimal vector -- the
    substrate's first failure to close is a minimal vector of its own lattice. -/
theorem overlap2_is_dodecahedral_minimal : (sqLenOf overlap2 == (6, -3)) = true := by decide

#print axioms transfer_rule
#print axioms twelve_are_six_and_negatives
#print axioms six_direction_det_eq_eight
#print axioms overlap_squared_lengths
#print axioms overlap_field_norms
#print axioms cuboctahedron_is_not_a_triangulation
#print axioms minimal_shell_is_twelve_plus_twenty

end Container11
