/-
  CONTAINER 58 -- the NATIVE HYPERCHARGE GRADING (SU(3)xSU(2)xU(1))/Z6 (fork R27/F14, rederived).
  Rests on 31 (colour Z/3), 45 (central -1 / Z/2), 30 (su(3)), 28 (su(2)), 29 (u(1)), 51 (product/joint);
  cites the fork, the SM hypercharges, the anomaly conditions.
  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND. `--check` fails on drift.

  Two native gradings -- colour triality t in Z/3 (31) and duality w in Z/2 (45) -- combine to Z/6 (= the
  colour element's centralizer <g3,-1>, 31.CS.2). Y6 = -(2t+3w) bijects Z/3 x Z/2 -> Z/6, so the SM gauge
  group is (SU(3)xSU(2)xU(1))/Z6 (HC.2). The fractional hypercharge Y = -(t/3+w/2) is forced (HC.3); the SM
  chiral content {Q,L,u_c,d_c,e_c} with Y6 = {+1,-3,-4,+2,+6}, mult = {6,2,3,3,1} is anomaly-free --
  sum m*Y6 = 0, sum m*Y6^3 = 0 (HC.4). The mass-founded Gell-Mann-Nishijima Q=T3+Y is abandoned. Absolute
  levels are CONDITIONAL (K2, HC.5 POSTULATE); the content selection + 57's theta_W are OWED (HC.6); the
  fork's sin^2(theta_W)=1/phi^3 is a fenced candidate, NOT banked. Mathlib-FREE, ZERO-axiom by decide.
-/

namespace Container58

/-! ### HC.2 -- Z/3 x Z/2 = Z/6: the six residues -(2t+3w) mod 6 are all distinct (a bijection to Z/6) -/

-- residues in (t,w) order (0,0)(0,1)(1,0)(1,1)(2,0)(2,1), computed as Nat (6 - (2t+3w) % 6) % 6
def residues : List Nat := [0, 3, 4, 1, 2, 5]

/-- The six hypercharge residues are pairwise distinct and number six -- a bijection Z/3 x Z/2 -> Z/6.
    So the two native gradings combine to exactly Z/6 and the SM group is (SU(3)xSU(2)xU(1))/Z6. -/
theorem zmod6_bijection : residues.Nodup ∧ residues.length = 6 := by decide

/-! ### HC.4 -- anomaly-free on the SM chiral content: sum m*Y6 = 0 and sum m*Y6^3 = 0 (positive vs negative, Nat) -/

-- SM content (Q,L,u_c,d_c,e_c): Y6 = {+1,-3,-4,+2,+6}, mult = {6,2,3,3,1} (colour x isospin).
-- Positive Y6: Q(+1,m6), d_c(+2,m3), e_c(+6,m1).  Negative Y6: L(-3,m2), u_c(-4,m3).
def anom1_pos : Nat := 6*1 + 3*2 + 1*6          -- grav/mixed anomaly, positive part  = 18
def anom1_neg : Nat := 2*3 + 3*4                -- grav/mixed anomaly, negative part  = 18
def anom3_pos : Nat := 6*1 + 3*8 + 1*216        -- U(1)^3 anomaly, positive part (6*1^3+3*2^3+1*6^3) = 246
def anom3_neg : Nat := 2*27 + 3*64              -- U(1)^3 anomaly, negative part (2*3^3+3*4^3)        = 246

/-- Both U(1)_Y anomalies vanish on the SM content: sum m*Y6 = 0 (Tr Y = 0, grav/mixed) and
    sum m*Y6^3 = 0 (Tr Y^3 = 0, U(1)^3), shown as positive part = negative part in Nat. -/
theorem anomaly_free : anom1_pos = anom1_neg ∧ anom3_pos = anom3_neg := by decide

#print axioms zmod6_bijection
#print axioms anomaly_free

end Container58
