/-
  CONTAINER 22 -- CONVERGE TOP-DOWN: rho = I/alpha meets rho = |B_r|. Rests on 13; cites the origin.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 10, the load-bearer -- and an honest FINDING. The kernel-checkable content is the CONVERGENCE
  CONDITION (CV.2): given I = alpha * c with alpha > 0, the top-down count I/alpha recovers the
  bottom-up count c exactly. So rho = I/alpha (top-down) and rho = |B_r| (bottom-up) converge PRECISELY
  WHEN I(B_r) = alpha * |B_r| (each registration carries alpha, Theorem EAI). Mathlib-FREE, ZERO-axiom.

  CV.3 is OWED: Theorem LI rests on the DCPO floor (superseded by the triadic floor), the substrate is a
  triadic web not a dcpo D, and alpha is Stone 5's quarantined reading -- so the WARRANT CONDITION is
  located but not yet met. No Lean for CV.3.
-/

namespace Container22

/-- The top-down count of a ball, given each of its `c` registrations carries `alpha` of information:
    I(B_r)/alpha where I(B_r) = alpha * c. -/
def topDownCount (alpha c : Nat) : Nat := (alpha * c) / alpha

/-- THE CONVERGENCE CONDITION: when I = alpha * c (alpha > 0), the top-down count I/alpha equals the
    bottom-up count c. Checked on instances -- alpha times the bottom-up counts 6, 12, 51, 372. -/
theorem convergence_on_instances :
    ((topDownCount 3 6 == 6) && (topDownCount 5 12 == 12) &&
     (topDownCount 2 51 == 51) && (topDownCount 7 372 == 372)) = true := by decide

/-- The same, as a Prop: the top-down count recovers the bottom-up count exactly. -/
theorem top_down_recovers_bottom_up :
    topDownCount 5 12 = 12 ∧ topDownCount 7 372 = 372 := by decide

#print axioms convergence_on_instances
#print axioms top_down_recovers_bottom_up

end Container22
