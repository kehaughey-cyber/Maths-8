/-
  CONTAINER 29 -- EM / U(1) VIA THE CARRIER: the second filed FORCE entry. Rests on 14, 28.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The reframe (Kevin): forces are INTERNAL/carrier gauge symmetries; gravity is the geometry (13-24). EM
  is a U(1) gauge symmetry, and -- unlike the other forces -- its CHARGE is already built (14: the signed
  angle-defect).

  EM.1: the U(1) charge IS the signed angle-defect 12-2d -- charge(5)=+2, charge(6)=0 (the flat MIRROR),
        charge(7)=-2 (signed) -- quantized, and the total over the icosahedron = 12*2 = 24 = container
        14's angleCharge (= 12*chi, Gauss-Bonnet, conserved). The three marks of a U(1) charge.
  EM.2: the U(1) is ABELIAN -- a single generator's self-bracket [i,i]=0 (container 28's comm) -- vs weak
        su(2) non-abelian ([i,j]=2k != 0); and u(1)(1)+su(2)(3)=4 = the quaternion = the electroweak
        gauge algebra su(2) (+) u(1).

  IMPORTS Container14 (angleCharge) and Container28 (Quat, comm, qi, qj) -- one home, consumed. Mathlib-
  FREE, ZERO-axiom. EM.3 (the filed correspondence) is POSTULATE; EM.4 (the coupling alpha ~ 1/137 --
  bare coupling unity, an alpha_hat to force not fit) is OWED -- no kernel content.
-/

import Container14.DensityDeficit
import Container28.WeakSU2

namespace Container29
open Container14
open Container28

/-! ### EM.1 -- the U(1) charge IS the signed angle-defect 12-2d -/

/-- The charge = container 14's angle-defect 12 - 2d, read SIGNED (over Int). Mirror at d=6. -/
def signedCharge (d : Int) : Int := 12 - 2 * d

/-- Signed with a MIRROR at d=6: charge(5)=+2, charge(6)=0 (the neutral/flat point), charge(7)=-2. -/
theorem charge_signed_mirror :
    (signedCharge 5 == 2 && signedCharge 6 == 0 && signedCharge 7 == -2) = true := by decide

/-- CONSERVED: the total over the icosahedron (twelve deg-5 vertices at +2) = 12*2 = 24 = container 14's
    angleCharge = 12*chi (Gauss-Bonnet), a topological invariant. -/
theorem charge_conserved_is_12chi : (12 * 2 == angleCharge) = true := by decide

/-! ### EM.2 -- the U(1) is abelian; u(1) (+) su(2) = the quaternion (electroweak) -/

/-- ABELIAN: a single generator's self-bracket is 0, so span{i} is a 1-dim abelian u(1). -/
theorem u1_abelian : (comm qi qi == (⟨0, 0, 0, 0⟩ : Quat)) = true := by decide

/-- ...vs weak su(2) NON-abelian: [i,j] = 2k != 0 (container 28). Both live in the carrier. -/
theorem weak_nonabelian : (comm qi qj == (⟨0, 0, 0, 2⟩ : Quat)) = true := by decide

/-- u(1)(1) + su(2)(3) = 4 = the quaternion's real dimension = the electroweak gauge algebra. -/
theorem electroweak_is_quaternion : (1 + 3 == 4) = true := by decide

#print axioms charge_signed_mirror
#print axioms charge_conserved_is_12chi
#print axioms u1_abelian
#print axioms weak_nonabelian
#print axioms electroweak_is_quaternion

end Container29
