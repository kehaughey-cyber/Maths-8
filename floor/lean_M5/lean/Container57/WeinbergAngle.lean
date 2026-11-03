/-
  CONTAINER 57 -- CROSSING B (Rung 0): the WEINBERG ANGLE sin^2(theta_W).
  Rests on 50 (rank-2 Cartan, the Z), 29 (u(1) abelian, [i,i]=0), 28 (su(2), [i,j]=2k), 51 (the gauge
  product + the fork), 30/31/56 (colour / the census); cites the U(2) sin^2=1/2, the SU(5) 3/8, meas 0.23122.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  theta_W reduces to the U(1)_Y-vs-su(2) normalization (WA.2; su(2) carrier-fixed by 28). The abelian
  factor is SCALELESS ([X,X]=0, 29 => Killing form 0), so the EW algebra cannot fix it -- exactly why g' is
  free in the SM (WA.3). The minimal carrier normalization (the quaternion/u(2) trace form) makes T0 and T3
  equal-norm and gives sin^2(theta_W) = Tr(T3^2)/Tr(Q^2) = 2/4 = 1/2 on the doublet -- REFUTED, since the
  measured ~0.231 and the GUT 3/8 are NOT 1/2 (WA.4). u(2) omits COLOUR; the fork (container 58) supplies
  the correct grading NATIVELY -- colour Z/3 (31) x duality Z/2 (45) = Z/6, (SU(3)xSU(2)xU(1))/Z6, forced
  fractional Y=-(t/3+w/2), NOT an SU(5)/3/8 GUT route (WA.5, POSTULATE); the cold value is OWED to the
  content K2 (58/56), the fork's 1/phi^3 a fenced candidate not banked (WA.6). This Lean certifies the COLD
  arithmetic of the refutation (3/8 is the standard GUT reference in the comparison). Mathlib-FREE, ZERO-axiom.
-/

namespace Container57

/-! ### WA.4 (equal-norm) -- under the quaternion/u(2) trace form, T0 (center) and T3 are equal-norm -/

def twoNormT0 : Nat := 1        -- 2*<T0,T0> with <X,Y> = -Tr(XY): T0 = (i/2)I2 gives 1/2, x2 = 1
def twoNormT3 : Nat := 1        -- 2*<T3,T3>: T3 = (i/2)sigma3 gives 1/2, x2 = 1

theorem cartan_equal_norm : twoNormT0 = twoNormT3 := by decide

/-! ### WA.4 (the U(2) prediction) -- on the doublet, sin^2(theta_W) = 4Tr(T3^2)/4Tr(Q^2) = 2/4 = 1/2 -/

def fourTrT3sq : Nat := 1 + 1   -- 4*[(1/2)^2 + (-1/2)^2] = 2   (doublet T3 = +-1/2)
def fourTrQsq  : Nat := 0 + 4   -- 4*[0^2 + (-1)^2] = 4         (doublet Q = 0, -1)
def sinsqU2Num : Nat := 1       -- reduced fraction 2/4 = 1/2
def sinsqU2Den : Nat := 2

/-- The quaternion/u(2)-normalized (equal-norm) mixing fraction on the electroweak doublet is 1/2:
    4Tr(T3^2)=2, 4Tr(Q^2)=4, and 2/4 = 1/2 (cross-check 2*2 = 1*4). -/
theorem u2_gives_half :
    fourTrT3sq = 2 ∧ fourTrQsq = 4 ∧ fourTrT3sq * sinsqU2Den = sinsqU2Num * fourTrQsq := by decide

/-! ### WA.4 (the refutation) -- 1/2 != 3/8 (the SU(5) tree value): the U(2) shortcut is REFUTED -/

def gutNum : Nat := 3           -- SU(5) tree value 3/8 (cited)
def gutDen : Nat := 8

/-- The DISCRIMINATING refutation: the substrate's minimal (U(2)) prediction 1/2 is NOT the GUT 3/8.
    Cross-multiplied: 1*8 = 8 != 3*2 = 6. So the electroweak-only quaternion normalization is ruled out;
    theta_W must know about colour (the fork, WA.5). Not fitted; refuter stated first (G4). -/
theorem half_ne_gut :
    sinsqU2Num * gutDen ≠ gutNum * sinsqU2Den := by decide

#print axioms cartan_equal_norm
#print axioms u2_gives_half
#print axioms half_ne_gut

end Container57
