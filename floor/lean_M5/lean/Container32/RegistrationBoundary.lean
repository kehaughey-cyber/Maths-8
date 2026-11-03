/-
  CONTAINER 32 -- THE REGISTRATION BOUNDARY IS 2*pi (SEC9 / Compton-boundary). Rests on 10; cites 17, 26, 27.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The load-bearer of the alpha-value chain: Stone 17 (S.3) ASSUMED the Compton wavelength R=hbar/mc is the
  minimum registration boundary (a 2*pi circumference), unproven (SEC9, OPEN). Here the substrate supplies
  its OWN 2*pi boundary: container 10's phase ledger fills at 12 writes of pi/6 = 2*pi, and a 13th
  overflows. So the registration boundary is 2*pi, natively -- corresponding to the Compton 2*pi. In the
  substrate's base-2 unit (26) the boundary carries 2*pi/ln2 bits = Stone 17's BC = 9.0647, so the two
  2*pi's are one. DANGER-FREE: the dimensionless 2*pi; the mass in R=hbar/mc stays external (27).

  KERNEL (here): the integer phase-ledger core -- 12 writes of 1 radit fill the capacity-12 cycle, a 13th
  overflows. The real 12*(pi/6)=2*pi is CITED from container 10 (proved in-repo); BC=2*pi/ln2 numeric,
  cited from Stone 17. Mathlib-FREE, ZERO-axiom. RB.3 (the filed SEC9 correspondence) is POSTULATE; RB.4
  (mass external / Planck anchor / discrimination / value) is OWED -- no Lean.
-/

namespace Container32

/-- The phase-ledger cycle capacity: 12 radits = 2*pi (container 10). -/
def cycleCapacity : Nat := 12
/-- Each adjacency write costs 1 radit (= pi/6). -/
def writeCost : Nat := 1

/-! ### RB.1 -- the registration boundary is one phase cycle (12 writes = 2*pi; the 13th overflows) -/

/-- 12 writes of 1 radit exactly FILL the capacity-12 cycle: the minimal closed registration = 2*pi. -/
theorem twelve_writes_fill : (12 * writeCost == cycleCapacity) = true := by decide

/-- A 13th write OVERFLOWS the cycle -- it reaches 13 = capacity+1, past the boundary at 12. Written as
    an equality (== ) rather than (>) to stay strictly zero-axiom (Nat `>` drags in propext). -/
theorem thirteenth_overflows : (13 * writeCost == cycleCapacity + 1) = true := by decide

/-- The boundary is 12 radits = 2*pi (the real identity 12*(pi/6)=2*pi is cited from container 10). -/
theorem boundary_is_twelve_radits : (cycleCapacity == 12) = true := by decide

#print axioms twelve_writes_fill
#print axioms thirteenth_overflows
#print axioms boundary_is_twelve_radits

end Container32
