/-
  CONTAINER 65 -- THE FOUR CLOCKS AND THE FRAME-ALIGNMENT RULE: the tick's four 30-loops on the 120 are
  canonically the four quaternion axes {1,i,j,k} of the substrate's Galois-fixed canonical frame -- the owed
  frame-alignment rule of 64.CX.7, built cold. Rests on 64 (the tick), 06 (carrier + frame), 12 (roots).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The tick cuts the 120 into 4 clocks of 30 (FC.1); the Galois-fixed frame is the 24 Hurwitz units, 8 axis
  units = the Q8 seam (FC.2); each clock owns exactly one antipodal axis pair (the 4 clocks = the 4 axes),
  the antipode fixes each clock, and frame-alignment is a SELECTOR -- 288 of 480 ticks align, 6 labelings,
  48 each (FC.3), a real cut 480 -> 288. The four clock-origins read 120 - 4 = 116 = 4x29 (FC.4, POSTULATE:
  the origin=+axis is the parity bit). VERDICT (FC.5): a REDUCTION toward canonicalizing the tick, not a
  forcing (the arbiter seating is owed, FC.6). This Lean certifies the cold integer bookkeeping. Mathlib-
  FREE, ZERO-axiom by decide. (The frame-alignment itself and the 120x120/480-tick computations are the
  exact-Python half; the kernel banks the integer certificates.)
-/

namespace Container65

def nClocks : Nat := 4
def clockSize : Nat := 30

/-! ### FC.1 / FC.4 -- seat bookkeeping: 4 clocks x 30 = 120; 120 - 4 = 116 = 4 x 29 -/

def nOrigins : Nat := 4
def nLag : Nat := 116

/-- The four clocks tile the whole carrier (4*30 = 120), and removing one origin per clock leaves
    120 - 4 = 116 = 4*29 lagging seats -- the fork's neutron-proton-splitting meter (the arithmetic; the
    four-origins / parity interpretation is FC.4, POSTULATE). -/
theorem seat_bookkeeping :
    nClocks * clockSize = 120 ∧ 120 - nOrigins = nLag ∧ nClocks * 29 = nLag := by decide

/-! ### FC.2 -- the canonical frame: the Galois-fixed spine (24 Hurwitz), 8 axis units = 4 pairs -/

def nHurwitz : Nat := 24        -- Galois-fixed phi-free icosians (= 2T)
def nAxis : Nat := 8            -- the axis units {+-1,+-i,+-j,+-k} = the Q8 seam
def nAxisPairs : Nat := 4       -- the 4 antipodal pairs = the 4 quaternion axes

/-- The Galois-fixed frame: 24 Hurwitz units, of which 8 are axis units forming 4 antipodal pairs
    (8 = 2*4) -- one per quaternion axis {1,i,j,k}. -/
theorem canonical_frame :
    nHurwitz = 24 ∧ nAxis = 8 ∧ nAxisPairs = 4 ∧ nAxis = 2 * nAxisPairs := by decide

/-! ### FC.3 -- the frame-alignment SELECTOR: 288 of 480 ticks aligned (6 labelings, 48 each) -/

def nTotal : Nat := 480
def nAligned : Nat := 288
def nLabelings : Nat := 6
def perLabeling : Nat := 48

/-- The 4 clocks match the 4 axis pairs (each clock one axis), and frame-alignment is a genuine selector:
    288 of the 480 ticks are aligned (not all -- a real cut 480 -> 288), in 6 labelings of 48 each
    (288 = 6*48). -/
theorem frame_alignment_selector :
    nClocks = nAxisPairs ∧
    nAligned = 288 ∧ nTotal = 480 ∧ nAligned < nTotal ∧
    nLabelings = 6 ∧ nAligned = nLabelings * perLabeling := by decide

#print axioms seat_bookkeeping
#print axioms canonical_frame
#print axioms frame_alignment_selector

end Container65
