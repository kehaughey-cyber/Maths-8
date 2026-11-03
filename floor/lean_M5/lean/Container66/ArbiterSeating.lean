/-
  CONTAINER 66 -- THE ARBITER SEATING: re-derive the fork's arbiter lean cold, and test whether it cuts the
  288 frame-aligned ticks (65) to a unique tick up to parity (the piece that would turn the reduction chain
  61->62->64->65 into a FORCING). Answer: it reproduces the fork's arbiter census (-33, 81, 13-13-4, -93)
  exactly and cuts 288 -> 2 lean-classes of 144, but does NOT force a unique tick. Rests on 64, 65,
  06 (the carrier). GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT. `--check` fails on drift.

  The arbiter = the servicing clock through the observer (the identity's tick-clock). Seats 13/13/4 by
  latitude (universal over 288, AS.1); registration-distance lag total 81 = 9^2 (universal, AS.2); lean
  18-51 = -33 (AS.3); the four-clock total -93 is a tick-independent substrate constant. As a selector the
  4-clock lean multiset takes 2 values over the 288 (144 each) -- cuts 288 -> 2, NOT -> 1 (AS.4). VERDICT
  (AS.5): a further REDUCTION, not the forcing. This Lean certifies the cold integer bookkeeping. Mathlib-
  FREE, ZERO-axiom by decide. (The census and the 288-sweep are the exact-Python half.)
-/

namespace Container66

/-! ### AS.1 -- shells and the arbiter seat-count -/

def shells : List Nat := [1, 12, 32, 42, 32, 1]      -- |B_d| from the pole 1, d = 0..5 (diameter 5)
def seatsAbove : Nat := 13
def seatsBelow : Nat := 13
def seatsEquator : Nat := 4

/-- The causal shells from the pole sum to 120 (diameter 5), and the arbiter clock's 30 seats split
    13 above / 13 below / 4 on the equator -- seat-symmetric (universal over the 288 aligned ticks). -/
theorem shells_and_arbiter_seats :
    (1 + 12 + 32 + 42 + 32 + 1 = 120) ∧ seatsAbove + seatsBelow + seatsEquator = 30 := by decide

/-! ### AS.2 -- the lag census: total lag 81 = 9^2 -/

def lagAbove : Nat := 18
def lagBelow : Nat := 51
def lagEquator : Nat := 12

/-- Weighting the arbiter clock's seats by registration distance, the total lag is 81 = 9^2 (the winding
    budget squared) -- canonical split 18/51/12 (universal over the 288). -/
theorem arbiter_lag_is_nine_squared :
    lagAbove + lagBelow + lagEquator = 81 ∧ 81 = 9 * 9 := by decide

/-! ### AS.3 -- the lean reproduced cold; the four-clock total -93 is tick-independent -/

/-- The arbiter lean = (lag above) - (lag below) = 18 - 51 = -33 (the fork's proton lean); and BOTH
    4-clock lean-classes sum to -93 (the fork's Keystone total) -- a tick-independent substrate constant. -/
theorem arbiter_lean_and_total :
    ((18 : Int) - 51 = -33) ∧
    ((-33 : Int) + (-26) + (-22) + (-12) = -93) ∧
    ((-26 : Int) + (-25) + (-22) + (-20) = -93) := by decide

/-! ### AS.4 -- the selector cuts 288 -> 2 classes of 144, NOT -> 1 -/

def nAligned : Nat := 288
def nLeanClasses : Nat := 2
def perClass : Nat := 144

/-- The arbiter lean is 2-valued over the 288 aligned ticks (144 each), so it cuts 288 -> 2 classes of 144
    (2*144 = 288); the max-lean (-33) class = 144. It does NOT cut to a unique tick (144 > 1). -/
theorem selector_cuts_288_to_two :
    nLeanClasses * perClass = nAligned ∧ nLeanClasses = 2 ∧ perClass = 144 ∧ 1 < perClass := by decide

#print axioms shells_and_arbiter_seats
#print axioms arbiter_lag_is_nine_squared
#print axioms arbiter_lean_and_total
#print axioms selector_cuts_288_to_two

end Container66
