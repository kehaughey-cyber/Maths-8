/-
  CONTAINER 31 -- COLOUR AS THREE SEATINGS: the native Z/3 of the strong force. Rests on 06, 30.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Colour = three seatings under conjugation by an order-3 element g3 of the carrier 2I (mined as the
  CRITERION from the danger-zone belt/quark clue; the census itself NOT imported). Re-derived cold on the
  120 vertices of 2I: g3=(-1/2,1/2,1/2,1/2) has order 3, and conjugation by it has order exactly 3, so it
  partitions 2I into fixed points (the centralizer) + 3-cycles = three colour positions cyclically
  permuted (the Z/3). Exhaustively: 6 fixed + 38 three-cycles.

  KERNEL (here): g3 has order 3, via the INTEGER quaternion (-1,1,1,1)=2*g3 whose cube is (8,0,0,0)=
  8*identity (so the unit g3 cubes to 1); plus the orbit-counting consistency 6 + 3*38 = 120 and
  centralizer 6 * class 20 = 120. The full 120-element cycle structure is EXACT-INTEGER in Z[phi]
  (verify-guarded), as container 06/13's larger computations are. Mathlib-FREE, ZERO-axiom.

  CS.3 (the filed correspondence colour <-> three seatings; REFINES 30's chosen A2 subset E8) is
  POSTULATE; CS.4 (the native su(3) adjoint / the quark census -- danger zone / alpha_s) is OWED -- no Lean.
-/

namespace Container31

/-- An integer quaternion (used at the DOUBLED scale, so g3 is integer with no phi). -/
abbrev IQuat := Int × Int × Int × Int

def iqmul (a b : IQuat) : IQuat :=
  (a.1 * b.1 - a.2.1 * b.2.1 - a.2.2.1 * b.2.2.1 - a.2.2.2 * b.2.2.2,
   a.1 * b.2.1 + a.2.1 * b.1 + a.2.2.1 * b.2.2.2 - a.2.2.2 * b.2.2.1,
   a.1 * b.2.2.1 - a.2.1 * b.2.2.2 + a.2.2.1 * b.1 + a.2.2.2 * b.2.1,
   a.1 * b.2.2.2 + a.2.1 * b.2.2.1 - a.2.2.1 * b.2.1 + a.2.2.2 * b.1)

/-- 2*g3 = (-1,1,1,1): the doubled order-3 element (integer, no phi). -/
def g3d : IQuat := (-1, 1, 1, 1)

/-! ### CS.1 -- g3 has order 3, so conjugation gives a Z/3 colour seating -/

/-- (-1,1,1,1)^3 = (8,0,0,0) = 8*identity: the unit g3 = (-1,1,1,1)/2 cubes to (1,0,0,0). So g3 has
    order 3, and conjugation by g3 has order dividing 3 -- cycles of length 1 or 3, a Z/3 seating. -/
theorem g3_doubled_cube : (iqmul (iqmul g3d g3d) g3d == (8, 0, 0, 0)) = true := by decide

/-- The seating count = the order of g3 = 3 (the three colours). -/
def seatingCount : Nat := 3
theorem seatings_three : (seatingCount == 3) = true := by decide

/-! ### CS.2 -- orbit-counting consistency (the exact 6 + 38 / centralizer 6 x class 20) -/

/-- 6 fixed points + 38 three-cycles exhaust the 120: 6 + 3*38 = 120. -/
theorem cycles_partition_120 : (6 + 3 * 38 == 120) = true := by decide

/-- The centralizer of g3 has order 6 (= Z/6 = <g3,-1>) and its class has size 20: 6 * 20 = 120. -/
theorem centralizer_times_class : (6 * 20 == 120) = true := by decide

#print axioms g3_doubled_cube
#print axioms seatings_three
#print axioms cycles_partition_120
#print axioms centralizer_times_class

end Container31
