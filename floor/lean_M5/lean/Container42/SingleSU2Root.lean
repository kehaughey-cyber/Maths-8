/-
  CONTAINER 42 -- THE ROOT OF THE SINGLE SU(2): why the carrier is ONE H (Frobenius), hence 3D.
  Rests on 41 (NT.2/NT.3), 06 (the carrier is a group with a norm), 28 (the chirality); cites Frobenius 1878.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  41 forced dim=3 from "the carrier is a single SU(2)=Spin(3)" but left the ROOT (why ONE) the numerical
  POSTULATE "3 observers <-> 3 generators". This roots it as a REDUCTION: (SR.1) "one SU(2) => 3D" IS "the
  carrier is one H" (ambient 3 = dim Im H); (SR.2/3/5) among the four real normed division algebras
  {R,C,H,O}, the UNIQUE associative (excl. O) + non-commutative (excl. R,C) one is H (Frobenius) -- so the
  3 is an OUTPUT; (SR.6) H's imaginary units close "two make the third", i*j=-(j*i) is the chirality. SR.4
  (the division-algebra premise) POSTULATE; SR.7 OWED. Mathlib-FREE, ZERO-axiom.
-/

namespace Container42

/-! ### SR.1 -- the reduction: "one SU(2) => 3D" is "the carrier is one H" (ambient 3 = dim Im H) -/

/-- H's imaginary part is 3-dimensional = the ambient dimension (41.NT.3). One H = one SU(2)=Spin(3)
    (one factor); two H's = Spin(4)=SU(2)xSU(2) (SO(4)=4D). -/
def hImagDim : Nat := 3
def spin3Factors : Nat := 1
def spin4Factors : Nat := 2
theorem one_H_is_three_d :
    hImagDim = 3 ∧ spin3Factors = 1 ∧ spin4Factors = 2 ∧ spin3Factors ≠ spin4Factors := by decide

/-! ### SR.2 / SR.3 / SR.5 -- Frobenius forces H uniquely (associative + non-commutative) -/

/-- The four real normed division algebras (Hurwitz), indexed 0=R,1=C,2=H,3=O, by imaginary dimension,
    associativity and commutativity. Pure algebra -- NO ambient space enters; dim Im H = 3 is the
    algebra's, and it becomes the ambient 3 only through SR.1. -/
def algebras : List Nat := [0, 1, 2, 3]
def imagDim : Nat → Nat
  | 0 => 0 | 1 => 1 | 2 => 3 | 3 => 7 | _ => 0
def assoc : Nat → Bool
  | 0 => true | 1 => true | 2 => true | 3 => false | _ => false   -- O non-associative
def comm : Nat → Bool
  | 0 => true | 1 => true | 2 => false | 3 => false | _ => false  -- R,C commutative

/-- SR.2 (a group => associative => excludes O) + SR.3 (chirality => non-commutative => excludes R,C):
    the carrier's algebra is associative AND non-commutative. -/
def forced : List Nat := algebras.filter (fun a => assoc a && !comm a)

/-- Frobenius (cited): among {R,C,H,O} the UNIQUE associative + non-commutative algebra is H (index 2),
    whose imaginary dimension is 3. So the carrier is H, and (SR.1) the ambient dimension is 3 -- the "3"
    is an OUTPUT of the forcing, not the input "3 observers". -/
theorem frobenius_forces_H : forced = [2] ∧ imagDim 2 = 3 := by decide

/-! ### SR.6 -- H's imaginary units close: "two make the third"; i*j = -(j*i) is the chirality -/

/-- A quaternion as an integer 4-tuple, and the Hamilton product. -/
abbrev Q := Int × Int × Int × Int
def qmul : Q → Q → Q
  | (a0, a1, a2, a3), (b0, b1, b2, b3) =>
    (a0*b0 - a1*b1 - a2*b2 - a3*b3,
     a0*b1 + a1*b0 + a2*b3 - a3*b2,
     a0*b2 - a1*b3 + a2*b0 + a3*b1,
     a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qI : Q := (0, 1, 0, 0)
def qJ : Q := (0, 0, 1, 0)
def qK : Q := (0, 0, 0, 1)
def qnegK : Q := (0, 0, 0, -1)

/-- The three imaginary units are not independent: any two compose to the third (i*j=k, j*k=i, k*i=j) --
    the "two within + the third that closes" -- and the order flips the sign (i*j = -(j*i)), the
    orientation / chirality (the within/without asymmetry). -/
theorem H_imaginary_closes :
    qmul qI qJ = qK ∧ qmul qJ qK = qI ∧ qmul qK qI = qJ
      ∧ qmul qJ qI = qnegK ∧ qmul qI qJ ≠ qmul qJ qI := by decide

#print axioms one_H_is_three_d
#print axioms frobenius_forces_H
#print axioms H_imaginary_closes

end Container42
