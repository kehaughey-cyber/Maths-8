/-
  CONTAINER 19 -- THE ENTRY PROTOCOL. Infrastructure: the gate for physics correspondences.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 7, infrastructure. The kernel-checkable content is the QUARANTINE invariant on the concrete
  bridge dependency graph: "an entry is never a premise" -- no DERIVED result rests on a quarantined
  physics reading. Mathlib-FREE, ZERO-axiom by `decide`. The full scan over all 77 DERIVED steps is
  exact-Python (E.2, run by verify.py); the Lean certifies the invariant on the bridge subgraph.
-/

namespace Container19

/-- The QUARANTINED READINGS: physics readings held as possibilities (named possibilities 15.C.3,
    16.D.3) and the two Stones' non-DERIVED steps (17.S.3/4/5, 18.P.3/4). Guarded against the derivation. -/
def quarantined : List String := ["15.C.3", "16.D.3", "17.S.3", "17.S.4", "17.S.5", "18.P.3", "18.P.4"]

/-- Each bridge-arc DERIVED step with its dependencies (cross-form ids). -/
def derivedDeps : List (String × List String) :=
  [ ("13.A.1", ["03.4"]),
    ("13.A.2", ["13.A.1"]),
    ("13.A.3", ["13.A.2"]),
    ("14.B.1", ["13.A.2"]),
    ("14.B.2", ["14.B.1", "13.A.2"]),
    ("14.B.3", ["14.B.2"]),
    ("14.B.4", ["14.B.2"]),
    ("14.B.5", ["14.B.2"]),
    ("15.C.1", ["14.B.2", "13.A.2"]),
    ("15.C.2", ["15.C.1", "14.B.4"]),
    ("16.D.1", ["08", "03.4"]),
    ("16.D.2", ["16.D.1", "14.B.4"]),
    ("17.S.1", []),
    ("17.S.2", ["17.S.1"]),
    ("18.P.1", []),
    ("18.P.2", ["18.P.1", "17.S.2"]) ]

/-- THE QUARANTINE: every DERIVED step's dependencies avoid every quarantined reading. -/
def quarantineHolds : Bool :=
  derivedDeps.all (fun p => p.2.all (fun d => ! quarantined.contains d))

/-- "AN ENTRY IS NEVER A PREMISE": no DERIVED result rests on a quarantined physics reading. -/
theorem quarantine_holds : quarantineHolds = true := by decide

/-- The crux, made explicit: the downstream DERIVED step 18.P.2 rests on the Stone's DERIVED ALGEBRA
    (17.S.2, scale-invariance), and NOT on the Stone's quarantined READING (17.S.3). The ruler is used,
    never imported. -/
theorem stone_used_as_algebra_not_reading :
    (derivedDeps.any (fun p => (p.1 == "18.P.2") && p.2.contains "17.S.2") &&
     (! derivedDeps.any (fun p => (p.1 == "18.P.2") && p.2.contains "17.S.3"))) = true := by decide

#print axioms quarantine_holds
#print axioms stone_used_as_algebra_not_reading

end Container19
