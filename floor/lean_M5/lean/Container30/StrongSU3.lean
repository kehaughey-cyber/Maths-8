/-
  CONTAINER 30 -- STRONG / SU(3) VIA THE CARRIER'S E8: the third filed FORCE entry. Rests on 12.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The reframe (Kevin): forces are INTERNAL/carrier gauge symmetries; gravity is the geometry (13-24). The
  strong force is an SU(3) gauge symmetry; su(3) = the A2 root system, and A2 sits inside the carrier's E8
  (container 12) -- less native than weak's 2I subset SU(2), because E8 has many A2 subsystems (an
  embedding choice), flagged honestly.

  S.1: the 6 A2 roots {e_i-e_j} all have norm 2; 6 roots + 2 rank = 8 = dim su(3) (the 8 gluons). A2
       subset E8 is CITED (12.E.3: E8's inner products {-2,-1,0,1,2} include -1).
  S.2: the A2 Cartan determinant = 3 = |Z(SU(3))| = the color TRIALITY; the cyclic coordinate permutation
       (a,b,c)->(c,a,b) is a Z/3 that permutes the 6 roots (order 3).

  Self-contained root arithmetic -- imports NOTHING, Mathlib-FREE, ZERO-axiom. S.3 (the filed
  correspondence, less native) is POSTULATE; S.4 (the strong dynamics -- danger zone) is OWED -- no
  kernel content. The 1+3+8=12 (SM trio vs the substrate's 12) is a NOTED check, NOT asserted.
-/

namespace Container30

/-- A root as an integer (L,T,M)-style triple in the sum-zero plane of Z^3. -/
abbrev Root := Int × Int × Int

/-- The 6 A2 roots {e_i - e_j : i != j}: a hexagon in the sum-zero plane, all norm 2. -/
def a2Roots : List Root :=
  [(1, -1, 0), (-1, 1, 0), (0, 1, -1), (0, -1, 1), (1, 0, -1), (-1, 0, 1)]

def norm (r : Root) : Int := r.1 * r.1 + r.2.1 * r.2.1 + r.2.2 * r.2.2

/-! ### S.1 -- su(3) = A2 (8 = 6 roots + 2 rank); A2 subset E8 (cited, 12.E.3) -/

/-- All 6 A2 roots have norm 2 (E8-normalized). -/
theorem roots_norm_two : (a2Roots.all (fun r => norm r == 2)) = true := by decide

/-- There are 6 roots. -/
theorem six_roots : (a2Roots.length == 6) = true := by decide

/-- dim su(3) = 6 roots + 2 rank = 8 = the 8 gluons. -/
theorem dim_su3_is_eight : (a2Roots.length + 2 == 8) = true := by decide

/-! ### S.2 -- the triality Z/3 = det(A2 Cartan) = 3; the cyclic Z/3 permutes the roots -/

/-- The A2 Cartan matrix [[2,-1],[-1,2]] has determinant 3 = |Z(SU(3))| = the color triality. -/
def a2CartanDet : Int := 2 * 2 - (-1) * (-1)
theorem cartan_det_three : (a2CartanDet == 3) = true := by decide

/-- The cyclic coordinate permutation (a,b,c) -> (c,a,b): the Z/3 (triality). -/
def cyc (r : Root) : Root := (r.2.2, r.1, r.2.1)

/-- The Z/3 permutes the 6 roots (each image is again a root). -/
theorem cyc_permutes_roots : (a2Roots.all (fun r => a2Roots.contains (cyc r))) = true := by decide

/-- ...and it has order 3: cyc^3 = identity on every root. -/
theorem cyc_order_three : (a2Roots.all (fun r => cyc (cyc (cyc r)) == r)) = true := by decide

#print axioms roots_norm_two
#print axioms six_roots
#print axioms dim_su3_is_eight
#print axioms cartan_det_three
#print axioms cyc_permutes_roots
#print axioms cyc_order_three

end Container30
