/-
  CONTAINER 09 -- KISSING-TWELVE / rung 6. Rests on 05 (the bridge / Euclidean 3-space).

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Twelve equal spheres kiss a central one in 3-space without overlapping: the icosahedron
  vertices (0,+-1,+-phi) & cyclic, each at norm^2 = 2+phi = R^2, pairwise dist^2 in
  {4, 4+4phi, 8+4phi} -- all > R^2, so they rattle (don't touch). EXACT and Mathlib-FREE in
  Z[phi] (Int x Int, phi^2 = phi+1); the tightest gap (edge) 2-phi > 0 bottoms out at 5 < 9.
  NOT here: the upper bound (no 13th; Schuette-van der Waerden, external).
-/

namespace Container09

/-! ### exact Z[phi] = { a + b*phi : a b : Int }, phi^2 = phi + 1 -- no Mathlib -/

abbrev ZPhi := Int × Int

def zadd (x y : ZPhi) : ZPhi := (x.1 + y.1, x.2 + y.2)
def zsub (x y : ZPhi) : ZPhi := (x.1 - y.1, x.2 - y.2)
/-- (a+b phi)(c+d phi) = (ac+bd) + (ad+bc+bd) phi, using phi^2 = phi+1. -/
def zmul (x y : ZPhi) : ZPhi := (x.1 * y.1 + x.2 * y.2, x.1 * y.2 + x.2 * y.1 + x.2 * y.2)
def zsq (x : ZPhi) : ZPhi := zmul x x

def normSq3 (x y z : ZPhi) : ZPhi := zadd (zadd (zsq x) (zsq y)) (zsq z)
def distSq3 (ax ay az bx by_ bz : ZPhi) : ZPhi :=
  normSq3 (zsub ax bx) (zsub ay by_) (zsub az bz)

/-! ### the geometry -- equidistant, and the edge -- steps 6.2, 6.3, DERIVED -/

/-- A vertex (0, 1, phi) is at norm^2 = 2 + phi = R^2. All twelve are, by symmetry
    (derivation.py checks every one). -/
theorem vertex_norm_R2 : normSq3 (0, 0) (1, 0) (0, 1) = (2, 1) := by decide

/-- An edge pair (0,1,phi) & (0,-1,phi) has dist^2 = 4 -- the minimum pairwise distance. -/
theorem edge_distSq_four :
    distSq3 (0, 0) (1, 0) (0, 1)  (0, 0) (-1, 0) (0, 1) = (4, 0) := by decide

/-! ### THE KISSING -- every gap dist^2 - R^2 is positive -- step 6.4, DERIVED -/

/-- The sign of a + b*phi (phi = (1+sqrt5)/2): write it (s + t*sqrt5)/2 with s = 2a+b, t = b,
    and decide s + t*sqrt5 > 0 by an INTEGER comparison of s^2 and 5*t^2 (with signs). Its
    correctness is the standard sqrt5 fact (Maths 5 has no Real); its evaluation is decided. -/
def zpos (x : ZPhi) : Bool :=
  let s := 2 * x.1 + x.2
  let t := x.2
  if t == 0 then decide (0 < s)
  else if 0 < t then decide (0 ≤ s) || decide (s * s < 5 * t * t)
  else decide (0 < s) && decide (5 * t * t < s * s)

/-- THE KISSING, tightest case: the EDGE gap is 4 - (2+phi) = 2 - phi > 0. Via zpos this
    reduces to 9 > 5 (i.e. sqrt5 < 3, phi < 2) -- the whole result's arithmetic heart. -/
theorem edge_gap_pos : zpos (2, -1) = true := by decide
/-- The two larger gaps: 2 + 3phi and 6 + 3phi, positive because phi > 0. -/
theorem gap_offedge_pos : zpos (2, 3) = true := by decide
theorem gap_antipodal_pos : zpos (6, 3) = true := by decide

/-- The arithmetic heart, standalone: 2 - phi > 0 <=> sqrt5 < 3 <=> 5 < 9. -/
theorem kissing_reduces_to : (5 : Int) < 9 := by decide

-- So twelve spheres (radius R/2) kiss the central sphere without overlapping: strict, they
-- rattle. Kissing number >= 12.
--
-- POSTULATE (6.5): 12 is ACHIEVED here. Whether registration SATURATES at exactly 12 mutual
-- adjacencies is the framework's central number -- container 01's OWED 1.6 (adjacency->12),
-- the phase cycle->12 -- and is EQUIVALENT to the dim=3 upper bound (12 is the max kissing
-- number only in 3-D). It should fall out of why-12, not be attacked head-on.
--
-- OWED (6.6): the upper bound (no 13th; kissing(3) = 12) is Schuette-van der Waerden 1953,
-- EXTERNAL, cited, not machine-checked here. The >= 12 half is ours; the <= 12 half is cited.

#print axioms vertex_norm_R2
#print axioms edge_distSq_four
#print axioms edge_gap_pos
#print axioms gap_offedge_pos
#print axioms kissing_reduces_to

end Container09
