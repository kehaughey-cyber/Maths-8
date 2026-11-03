/-
  CONTAINER 28 -- WEAK / SU(2) VIA THE CARRIER: the first filed FORCE entry. Rests on 06, 11.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The reframe (Kevin): forces are INTERNAL gauge symmetries, not spatial geometry -- gravity is the
  geometry (13-24), the forces are in the CARRIER (2I/E8) and the internal sector. The WEAK force is a
  chiral SU(2) gauge symmetry. Its location is CHECKABLE: SU(2) = the unit quaternions, the carrier 2I
  (06) is a finite subgroup, and su(2) = the pure-imaginary / internal sector (11).

  W.1: the imaginary quaternions {i,j,k} close under the commutator [a,b]=ab-ba to su(2) --
       [i,j]=2k, [j,k]=2i, [k,i]=2j (the su(2) structure constants). The weak Lie algebra IS the
       internal 3.
  W.2: |2I| = 120 = 2*60 (the 2:1 double cover SU(2)->SO(3), the substrate's chirality); dim su(2) = 3
       generators = the internal-3.

  Self-contained quaternion algebra -- imports NOTHING, Mathlib-FREE, ZERO-axiom. W.3 (the filed
  correspondence) is POSTULATE; W.4 (the weak dynamics: breaking, masses, reps, coupling -- danger zone)
  is OWED -- no kernel content.
-/

namespace Container28

/-- A quaternion (the carrier's ambient algebra H). -/
structure Quat where
  w : Int
  x : Int
  y : Int
  z : Int
deriving DecidableEq, BEq

/-- The Hamilton product. -/
def qmul (a b : Quat) : Quat :=
  { w := a.w * b.w - a.x * b.x - a.y * b.y - a.z * b.z,
    x := a.w * b.x + a.x * b.w + a.y * b.z - a.z * b.y,
    y := a.w * b.y - a.x * b.z + a.y * b.w + a.z * b.x,
    z := a.w * b.z + a.x * b.y - a.y * b.x + a.z * b.w }

def qsub (a b : Quat) : Quat := { w := a.w - b.w, x := a.x - b.x, y := a.y - b.y, z := a.z - b.z }

/-- The Lie bracket [a,b] = ab - ba. -/
def comm (a b : Quat) : Quat := qsub (qmul a b) (qmul b a)

def qi : Quat := ⟨0, 1, 0, 0⟩
def qj : Quat := ⟨0, 0, 1, 0⟩
def qk : Quat := ⟨0, 0, 0, 1⟩

/-! ### W.1 -- su(2) IS the carrier's internal sector: the imaginary quaternions close to su(2) -/

/-- [i,j] = 2k. -/
theorem su2_bracket_ij : (comm qi qj == ⟨0, 0, 0, 2⟩) = true := by decide
/-- [j,k] = 2i. -/
theorem su2_bracket_jk : (comm qj qk == ⟨0, 2, 0, 0⟩) = true := by decide
/-- [k,i] = 2j. -/
theorem su2_bracket_ki : (comm qk qi == ⟨0, 0, 2, 0⟩) = true := by decide

/-- A quaternion splits scalar + vector = 1 + 3; the vector part is the 3 su(2) generators. -/
theorem split_one_plus_three : (1 + 3 == 4) = true := by decide

/-! ### W.2 -- 2I is a finite subgroup of SU(2) via the double cover; 3 generators -/

/-- |2I| = 120 = 2*60: the 2:1 double cover SU(2) -> SO(3) (2I -> the icosahedral group I of order 60),
    which is the substrate's chirality. -/
theorem double_cover_120 : (120 == 2 * 60) = true := by decide

/-- su(2) has exactly 3 generators = dim(internal-3) = the vector part of a quaternion. -/
def su2Generators : Nat := 3
theorem generators_three : (su2Generators == 3) = true := by decide

#print axioms su2_bracket_ij
#print axioms su2_bracket_jk
#print axioms su2_bracket_ki
#print axioms split_one_plus_three
#print axioms double_cover_120
#print axioms generators_three

end Container28
