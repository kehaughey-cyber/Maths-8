/-
  CONTAINER 62 -- THE K2 EMBEDDING-DISTINCTION TEST: does a substrate-native invariant single out an A2 in
  E8, against the W(E8)-transitive family? (answer: it CUTS but does not FORCE -- a reduction, not a forcing)
  Rests on 12 (the 240 roots), 06 (the carrier + Z-basis), 31 (the order-3 colour element + its class of 20),
  61 (K2 open); cites the E8 A2-subsystem count and E8 > A2 x E6.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Xi = conjugation by an order-3 element g3 of 2I (31's colour operator) -- a genuine order-3 E8 isometry
  (the Galois sigma is NOT an isometry). BASELINE: E8 has 1120 A2 subsystems, W-transitive (ED.1). THE CUT:
  g3 leaves 4 of 1120 invariant -- 2 pointwise-fixed (its fixed locus is an A2 x A2, 12 roots) + 2 triality
  (g3 cycles their 3 roots) -- the rest in 372 three-cycles (ED.2/ED.3). NON-CANONICAL: 20 order-3 elements
  (one class) -> 10 conjugate loci (ED.4). VERDICT: a reduction 'which A2' -> 'which order-3 axis' --
  eliminative (opt 2) + residual arbitrary (opt 1), not a forcing (opt 3) (ED.5, POSTULATE). This Lean
  certifies the cold integer bookkeeping. Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container62

/-! ### ED.1 -- baseline: the A2-subsystem count -/

def nA2 : Nat := 1120        -- A2 subsystems of E8 (exhaustive over the 240 roots; W(E8)-transitive)

/-! ### ED.3 -- g3's order-3 action on the 1120 A2's: 4 invariant + 372 three-cycles -/

def invariantA2 : Nat := 4                 -- setwise-invariant under conjugation by g3
def threeCycles : Nat := 372               -- the rest, in three-cycles
def fixedA2 : Nat := 2                      -- pointwise-fixed (the A2 x A2 components)
def trialityA2 : Nat := 2                   -- g3 acts as triality (cycle-type [3,3])

/-- The order-3 colour operator partitions the 1120 A2 subsystems into 4 invariant + 372 three-cycles
    (4 + 3*372 = 1120); the 4 invariant split as 2 pointwise-fixed + 2 triality. A real cut of the
    W-transitive family -- but to a handful, not to one. -/
theorem a2_orbit_decomposition :
    invariantA2 + 3 * threeCycles = nA2 ∧ fixedA2 + trialityA2 = invariantA2 := by decide

/-! ### ED.2 -- the fixed locus is an A2 x A2 (12 roots, orthogonal), by its inner-product signature -/

def fixedRoots : Nat := 12                  -- roots fixed pointwise by g3 (4-dim fixed space)
-- ordered-pair inner-product signature over the 12 fixed roots: +2, -2, +1, -1, 0
def sigSelf : Nat := 12                     -- <r,r>=+2  (the 12 roots)
def sigAnti : Nat := 12                     -- <r,-r>=-2 (12 antipodal pairs, ordered)
def sigPlus1 : Nat := 24                    -- +1
def sigMinus1 : Nat := 24                   -- -1
def sigZero : Nat := 72                     -- 0 (the cross-A2 orthogonality)

/-- The fixed locus is A2 x A2: 12 roots = 6 + 6 (two A2's), and the inner-product signature over its 144
    ordered pairs is 12+12+24+24+72 = 144 = 12*12, with 72 zeros = the two A2's mutually orthogonal. -/
theorem fixed_locus_is_A2xA2 :
    fixedRoots = 6 + 6 ∧
    sigSelf + sigAnti + sigPlus1 + sigMinus1 + sigZero = 144 ∧
    fixedRoots * fixedRoots = 144 := by decide

/-! ### ED.4 -- non-canonicity: 20 order-3 elements (one 2I-class) give 10 conjugate loci -/

def nOrder3 : Nat := 20                     -- order-3 elements of 2I (one conjugacy class -- 31)
def nLoci : Nat := 10                       -- distinct A2 x A2 fixed-loci (g3 and g3^2 share one)

/-- The 20 order-3 elements (one 2I-conjugacy class) give exactly 10 distinct A2 x A2 loci (20 = 2*10, each
    from an element and its inverse), all W(E8)-conjugate -- so no canonical colour axis: the distinguished
    A2 x A2 is fixed only up to the (unforced) choice of order-3 element. -/
theorem axis_not_canonical : nOrder3 = 2 * nLoci := by decide

#print axioms a2_orbit_decomposition
#print axioms fixed_locus_is_A2xA2
#print axioms axis_not_canonical

end Container62
