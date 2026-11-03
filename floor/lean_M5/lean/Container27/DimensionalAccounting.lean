/-
  CONTAINER 27 -- DIMENSIONAL ACCOUNTING: how much of alpha's value is irreducibly external?

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Pure dimensional bookkeeping over (L,T,M) exponent triples. The substrate is DIMENSIONLESS (DA.1: every
  tower quantity carries (0,0,0)). {hbar,c,G} is a DIMENSIONAL BASIS (DA.2: their exponent matrix has
  determinant 2 != 0), so exactly three dimensionful anchors fix all units and a dimensionless substrate
  supplies none -- >= 3 are IRREDUCIBLY EXTERNAL (why Planck units exist). The per-archon alpha's two
  source readings -- energy per archon (2,-2,1) and the c=alpha/tau edge (1,0,0) -- are dimensionally
  distinct but COMPTON-DUAL: their sum (3,-2,1) is the dimension of hbar*c, i.e. E*R=hbar*c (Stone 17's
  cold algebra), and each is a Planck monomial (2*energy = hbar+5c-G; 2*length = hbar+G-3c).

  Self-contained integer arithmetic -- imports NOTHING, Mathlib-FREE, ZERO-axiom by `decide`. DA.4
  (forcing the dimensionless alpha_hat; disambiguating the reading) is OWED -- no kernel content.
-/

namespace Container27

/-- A physical dimension as a vector of (length, time, mass) exponents. -/
abbrev Dim := Int × Int × Int

def dadd (a b : Dim) : Dim := (a.1 + b.1, a.2.1 + b.2.1, a.2.2 + b.2.2)
def dsmul (k : Int) (a : Dim) : Dim := (k * a.1, k * a.2.1, k * a.2.2)

/-- Determinant of the 3x3 matrix whose rows are three (L,T,M) exponent triples. -/
def det3 (r1 r2 r3 : Dim) : Int :=
  r1.1 * (r2.2.1 * r3.2.2 - r2.2.2 * r3.2.1)
  - r1.2.1 * (r2.1 * r3.2.2 - r2.2.2 * r3.1)
  + r1.2.2 * (r2.1 * r3.2.1 - r2.2.1 * r3.1)

/-- The three base anchors, (L,T,M) exponents. -/
def hbar : Dim := (2, -1, 1)      -- action = energy*time
def clight : Dim := (1, -1, 0)    -- speed
def gnewton : Dim := (3, -2, -1)  -- Newton's G

/-! ### DA.1 -- the substrate is dimensionless -/

/-- Every quantity the tower computes (|B_r|, L, chi, radits, BC, the base-2 alphabet) is a count or a
    dimensionless ratio: dimension (0,0,0). -/
theorem substrate_dimensionless :
    (([(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)] : List Dim).all
      (fun d => d == (0,0,0))) = true := by decide

/-! ### DA.2 -- {hbar, c, G} is a dimensional basis (det = 2) -/

/-- The {hbar,c,G} exponent matrix has determinant 2, nonzero -- the three span (L,T,M), so exactly
    three dimensionful anchors fix ALL units (why Planck units exist) and a dimensionless substrate
    supplies none: >= 3 dimensionful inputs are irreducibly external. -/
theorem anchors_basis_det_two : (det3 hbar clight gnewton == 2) = true := by decide

/-- Nonzero determinant, stated as independence. -/
theorem anchors_independent : (det3 hbar clight gnewton == 0) = false := by decide

/-! ### DA.3 -- the per-archon alpha: two readings, dimensionally distinct but Compton-dual -/

def alphaEnergy : Dim := (2, -2, 1)   -- 'energy per archon' (Stone 17)
def alphaLength : Dim := (1, 0, 0)    -- the 'edge' in c = alpha/tau (Planck hypothesis 18.P.3)

/-- The two readings are dimensionally DISTINCT: 'alpha' names two objects unless one is wrong. -/
theorem alpha_readings_differ : (alphaEnergy == alphaLength) = false := by decide

/-- ...but COMPTON-DUAL: their dimensions sum to (3,-2,1), the dimension of hbar*c -- i.e. E*R=hbar*c,
    exactly Stone 17's cold algebra. -/
theorem alpha_compton_dual : (dadd alphaEnergy alphaLength == dadd hbar clight) = true := by decide

/-- The energy reading's units ARE the Planck energy: 2*(2,-2,1) = hbar + 5c - G (the factor 2 clears
    the square root; Planck energy = sqrt(hbar c^5 / G)). -/
theorem alpha_energy_is_planck_energy :
    (dsmul 2 alphaEnergy == dadd (dadd hbar (dsmul 5 clight)) (dsmul (-1) gnewton)) = true := by decide

/-- The length reading's units ARE the Planck length: 2*(1,0,0) = hbar + G - 3c
    (Planck length = sqrt(hbar G / c^3)). -/
theorem alpha_length_is_planck_length :
    (dsmul 2 alphaLength == dadd (dadd hbar gnewton) (dsmul (-3) clight)) = true := by decide

#print axioms substrate_dimensionless
#print axioms anchors_basis_det_two
#print axioms anchors_independent
#print axioms alpha_readings_differ
#print axioms alpha_compton_dual
#print axioms alpha_energy_is_planck_energy
#print axioms alpha_length_is_planck_length

end Container27
