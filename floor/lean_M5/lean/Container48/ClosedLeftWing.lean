/-
  CONTAINER 48 -- THE CLOSED LEFT WING: closure forces the negative-curvature mirror -- 12 degree-7 at genus 2.
  Rests on 03 (the closure forcing), 36 (the left wing), 14 (Gauss-Bonnet); cites the {3,7} regular maps.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The closure law V(6-d) = 6*chi (Euler + 3F=2E + uniform degree, 03) gives the sphere (3,4),(4,6),(5,12)
  at chi=2 (CW.1); at chi=-2 (genus 2) it forces d>6: (7,12),(8,6),(9,4) -- the exact mirror under d<->12-d
  with the SAME V (CW.2). The icosahedron's mirror is 12 degree-7 vertices at genus 2, total deficit
  -24 = 12*chi (CW.3). Realizability held (CW.4); OWED (CW.5). Mathlib-FREE, ZERO-axiom.
-/

namespace Container48

/-- The closure law V*(6-d) = 6*chi (03's REFRAME-CLOSURE-FORCING, any chi): given as the check
    V*(6-d) = 6*chi on integers (d, V, chi). -/
def closureHolds (d V chi : Int) : Bool := V * (6 - d) == 6 * chi

/-- The total angle deficit of V uniform degree-d vertices: V*(12-2d) = 12*chi (Gauss-Bonnet). -/
def totalDeficit (d V : Int) : Int := V * (12 - 2*d)

/-! ### CW.1 -- the sphere spectrum at chi = 2 -/

theorem sphere_spectrum :
    closureHolds 3 4 2 ∧ closureHolds 4 6 2 ∧ closureHolds 5 12 2 := by decide

/-! ### CW.2 -- the genus-2 mirror spectrum at chi = -2 (d <-> 12-d, same V) -/

theorem mirror_spectrum :
    closureHolds 7 12 (-2) ∧ closureHolds 8 6 (-2) ∧ closureHolds 9 4 (-2)
      -- the mirror map d <-> 12-d preserves V: (5,12)<->(7,12), (4,6)<->(8,6), (3,4)<->(9,4)
      ∧ (7 = 12 - 5) ∧ (8 = 12 - 4) ∧ (9 = 12 - 3) := by decide

/-! ### CW.3 -- the icosahedron's mirror: 12 degree-7 at genus 2, total deficit -24 = 12*chi -/

theorem anti_twelve :
    closureHolds 7 12 (-2) ∧ totalDeficit 7 12 = -24 ∧ totalDeficit 5 12 = 24
      ∧ totalDeficit 7 12 = 12 * (-2) ∧ totalDeficit 5 12 = 12 * 2 := by decide

#print axioms sphere_spectrum
#print axioms mirror_spectrum
#print axioms anti_twelve

end Container48
