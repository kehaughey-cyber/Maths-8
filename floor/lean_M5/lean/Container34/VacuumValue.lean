/-
  CONTAINER 34 -- THE VACUUM VALUE (rho_Lambda): the flagship, configuration landed, value OWED.
  Rests on 14, 15, 24, 27. GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  rho_Lambda = alpha x rho_vac, where rho_vac = the minimum archic density (container 15, at the twelve)
  and alpha = the per-archon quantum (24). VV.1: rho_min = flat_ball - tri at the twelve = [6,16,31,51]
  for r=1..4 (flat_ball r = tri r + rho_min); the deficit there = tri(r) = [1,3,6,10], the maximum.
  VV.2: rho_Lambda = alpha x rho_vac is dimensionally an ENERGY DENSITY -- (2,-2,1)+(-3,0,0) = (-1,-2,1).

  IMPORTS Container14 (flat_ball, tri). Mathlib-FREE, ZERO-axiom. VV.3 (the vacuum reading) is POSTULATE;
  VV.4 (the VALUE, gated on alpha_hat + the 3 external anchors -- computed-then-compared, NEVER fitted) is
  OWED -- no Lean. The whole arc converges to one unknown: alpha_hat.
-/

import Container14.DensityDeficit

namespace Container34
open Container14   -- flatBall, tri -- one home, consumed here

/-! ### VV.1 -- the vacuum configuration = the minimum archic density (rho_min = flat_ball - tri) -/

/-- At each of the twelve, flat_ball(r) = tri(r) + rho_min(r), with rho_min = [6,16,31,51] for r=1..4 --
    i.e. the minimum density rho_min = flat_ball - tri (the deficit tri(r) is the maximum). -/
theorem rho_min_values :
    ([(1, 6), (2, 16), (3, 31), (4, 51)].all (fun p => flatBall p.1 == tri p.1 + p.2)) = true := by decide

/-- The deficit at the twelve is the triangular number tri(r) = [1,3,6,10] for r=1..4. -/
theorem deficit_is_triangular :
    ([(1, 1), (2, 3), (3, 6), (4, 10)].all (fun p => tri p.1 == p.2)) = true := by decide

/-! ### VV.2 -- rho_Lambda = alpha x rho_vac is dimensionally an energy density -/

/-- A physical dimension as (L,T,M) exponents (container 27). -/
abbrev Dim := Int × Int × Int
def dadd (a b : Dim) : Dim := (a.1 + b.1, a.2.1 + b.2.1, a.2.2 + b.2.2)

def alphaDim : Dim := (2, -2, 1)     -- energy per archon (27's energy reading of alpha)
def rhoVacDim : Dim := (-3, 0, 0)    -- archons per volume (the volume, l_P^3, external)
def energyDensityDim : Dim := (-1, -2, 1)   -- energy / volume = the cosmological constant's dimension

/-- rho_Lambda = alpha x rho_vac has dimension (2,-2,1)+(-3,0,0) = (-1,-2,1) = energy density. -/
theorem rho_lambda_is_energy_density : (dadd alphaDim rhoVacDim == energyDensityDim) = true := by decide

#print axioms rho_min_values
#print axioms deficit_is_triangular
#print axioms rho_lambda_is_energy_density

end Container34
