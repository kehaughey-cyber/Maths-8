/-
  CONTAINER 54 -- FIRST CONTACT (Rung 0, crossing A): the light-bending factor of 2 (GR vs Newton).
  Rests on 40 (light-as-front, 1/b), 46 (the null condition), 20 (grad rho = -grad deficit), 14/21; cites Eddington 1919.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  The dimensionless target is delta_light/delta_Newton (GR 2, Newton 1; magnitude deferred). Light is a
  FRONT (40) and the null condition (46) makes it feel BOTH the temporal (g_tt, potential) and spatial
  (g_ii, curvature) metric parts; a Newtonian particle feels only the temporal (FC.2). The two parts are
  locked equal (gamma=1) because the potential (rho, 20) and curvature (deficit, 14/21) are one field
  (grad rho = -grad deficit, 20.G.3) -- so the ratio = 1+1 = 2, differing from Newton's 1 (FC.3/FC.4, the
  discriminating Eddington test). FC.3 the equality is a POSTULATE (rests on the metric correspondence);
  FC.5 OWED (the magnitude, danger). Mathlib-FREE, ZERO-axiom.
-/

namespace Container54

def temporal : Nat := 1        -- the g_tt (potential) contribution -- a Newtonian particle feels this
def spatial : Nat := 1         -- the g_ii (spatial-curvature) contribution -- the front feels this too
def frontFeels : Nat := temporal + spatial     -- the light front (null, 40/46) feels both
def particleFeels : Nat := temporal            -- the Newtonian particle feels only the potential

/-! ### FC.2 -- the front feels both metric parts; the particle feels one -/

theorem front_feels_both :
    frontFeels = temporal + spatial ∧ frontFeels = 2 ∧ particleFeels = 1 := by decide

/-! ### FC.3 / FC.4 -- ratio = 1+1 = 2, discriminated from Newton's 1 -/

def ratio : Nat := frontFeels / particleFeels   -- = 2 (front / particle, with the parts locked equal)
def grFactor : Nat := 2
def newtonFactor : Nat := 1

/-- With the two metric perturbations locked equal (gamma=1, FC.3), the light front deflects twice the
    Newtonian particle: ratio = 2 = the GR/Eddington factor, and it DIFFERS from Newton's 1 -- the
    discriminating test (Eddington 1919 measured 2x Newton). Not fitted: 2 = 1 + 1. -/
theorem factor_of_two :
    ratio = 2 ∧ ratio = grFactor ∧ ratio ≠ newtonFactor := by decide

#print axioms front_feels_both
#print axioms factor_of_two

end Container54
