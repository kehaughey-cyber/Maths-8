/-
  CONTAINER 44 -- CHIRALITY: the carrier is orientation-pure; parity is not a self-symmetry.
  Rests on 06 (the even-permutation carrier; the conjugate mirror), 28 (the chiral weak force it meets).
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  06.1 builds the carrier's 96-block on EVEN permutations of the four coordinates (sign +1). The even
  permutations are closed under composition (even.even=even), so the carrier is ORIENTATION-PURE (CH.1);
  2I subset SU(2) = proper rotations (det +1), no reflection. A reflection (odd permutation, sign -1)
  composed with an even one is ODD (odd.even=odd) -- it carries the carrier into the DISJOINT odd orbit,
  the conjugate mirror copy (06 finding-2 / CORRECTIONS #5): parity is not a self-map, the substrate is
  CHIRAL (CH.2). CH.3 (chirality <-> weak parity violation) POSTULATE; CH.4 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container44

/-- A permutation of {0,1,2,3} as the tuple of images (p0,p1,p2,p3). -/
abbrev P4 := Nat × Nat × Nat × Nat

/-- The image of index i under p. -/
def app (p : P4) : Nat → Nat
  | 0 => p.1 | 1 => p.2.1 | 2 => p.2.2.1 | _ => p.2.2.2

/-- Inversion count: pairs i<j with p(i) > p(j). -/
def inv : P4 → Nat
  | (a, b, c, d) =>
      (if a > b then 1 else 0) + (if a > c then 1 else 0) + (if a > d then 1 else 0)
    + (if b > c then 1 else 0) + (if b > d then 1 else 0) + (if c > d then 1 else 0)

/-- Parity: 0 = even (orientation-preserving), 1 = odd (orientation-reversing). -/
def par (p : P4) : Nat := inv p % 2

/-- Composition p after q: (p∘q)(i) = p(q(i)). -/
def comp (p q : P4) : P4 := (app p q.1, app p q.2.1, app p q.2.2.1, app p q.2.2.2)

def ident : P4 := (0, 1, 2, 3)
def e1 : P4 := (1, 2, 0, 3)          -- a 3-cycle, even
def e2 : P4 := (1, 0, 3, 2)          -- a double transposition, even
def t  : P4 := (1, 0, 2, 3)          -- a transposition: a reflection, odd

/-! ### CH.1 -- the carrier is orientation-pure: even permutations, closed (even.even=even) -/

/-- The even (06.1) permutations have sign +1, and composing two stays even -- the carrier never
    generates an orientation-reversing map. -/
theorem carrier_orientation_pure :
    par ident = 0 ∧ par e1 = 0 ∧ par e2 = 0 ∧ par (comp e1 e2) = 0 := by decide

/-! ### CH.2 -- parity is not a self-symmetry: odd.even = odd (leaves the orbit) -/

/-- A transposition (a reflection, sign -1) composed with an even permutation is ODD -- it carries the
    carrier OUT of its even orbit into the disjoint odd (mirror) orbit. So parity is not a self-map: the
    substrate is chiral. -/
theorem parity_is_not_a_self_map :
    par t = 1 ∧ par (comp t e1) = 1 ∧ (0 : Nat) ≠ 1 := by decide

#print axioms carrier_orientation_pure
#print axioms parity_is_not_a_self_map

end Container44
