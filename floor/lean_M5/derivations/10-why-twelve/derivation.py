#!/usr/bin/env python3
"""Container 10 -- WHY-12, the consolidation. Rests on 01, 02, 03, 09.

THIS IS A CONSOLIDATION + POSTULATE-NAMING CONTAINER, NOT A FROM-BELOW DERIVATION OF 12.
The headline grade is POSTULATE (W.4). Dressing it as a derivation is the confirmation-bias
trap the whole restart exists to avoid -- read the RIGID-AND-FREE note in HANDOFF.md. What is
actually DERIVED here is narrow and honest: the phase-ledger COUNTING arithmetic (12 radits fill
the cycle, 13 overflow), its dimension-independence, and the conditional consequence that 12 and
d=3 follow FROM the postulate. The number 12 is NOT forced from below by anything in this repo.

The framework's central number, 12, shows up on FOUR separate roads:

  - adjacency -> 12          container 01, OWED 1.6 (the live web's coordination number)
  - phase-cycle -> 12        container 02, OWED 2.6 (the registration event's write ledger)
  - icosahedral selection    container 03, step 3.4 (the triad picks the 12-vertex shell)
  - kissing-12               container 09 (twelve spheres kiss, exact in Z[phi])

W.1 asserts (POSTULATE) these are ONE 12. W.2-W.3 establish the only road that can BOUND
adjacencies at 12 -- the phase ledger -- as exact counting arithmetic (Mathlib-free) whose trig
provenance (arcsin(1/2) = pi/6) is CITED from maths-4 REFRAME-PHASE-LEDGER-ARITHMETIC (THEOREM),
because Maths 5 has no Real. W.4 names the one substrate POSTULATE the whole picture reduces to
(maths-4 GATE-PHASE-LEDGER half-a, OPEN) -- provably not derivable from its own road, equivalent
to dim=3. W.5 shows 12 and d=3 follow FROM that postulate (conditional). W.6 marks the honest
boundary: geometry ALONE cannot force 12 (the separation lever is a checked negative; the no-13th
is external).

Grades: DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---- the four 12-threads, each naming a count (from the lower containers) ----
# These COUNTS are what each lower container establishes/owes; recorded here as data, not
# recomputed (they are other containers' work). The consistency witness is that all four = 12.
THREADS = [
    {"road": "adjacency -> 12", "from": "01 / 1.6", "grade_there": "OWED", "count": 12},
    {"road": "phase-cycle -> 12", "from": "02 / 2.6", "grade_there": "OWED", "count": 12},
    {"road": "icosahedral selection", "from": "03 / 3.4", "grade_there": "DERIVED", "count": 12},
    {"road": "kissing-12", "from": "09 / 6.1,6.4", "grade_there": "DERIVED", "count": 12},
]
all_twelve = all(t["count"] == 12 for t in THREADS)

# ---- W.1 the four threads are ONE 12 -- POSTULATE (structural) ---------------
step("W.1", "the four 12-threads are one and the same 12",
     "adjacency-12 (01) = phase-12 (02) = icosahedral (03) = kissing-12 (09)",
     ["01.6", "02.6", "03.4", "09.4"],
     "the number 12 appears on four separate roads: the adjacency coordination number (01's OWED "
     "1.6), the phase-cycle write capacity (02's OWED 2.6), the icosahedral selection (03.4), and "
     "the kissing witness (09). Each road independently lands on 12. THAT THEY ARE THE SAME 12 -- "
     "one substrate fact wearing four faces -- is a structural READING, held, not proven. The "
     "consistency witness (all four counts equal 12) is necessary but not sufficient: two roads "
     "agreeing on a number does not make them the same object. Held as the reading that unifies "
     "the container.",
     "CHOSEN (one reading unifying four occurrences; the counts agree, the identity is held)",
     "POSTULATE",
     {"threads": THREADS, "all_count_twelve": all_twelve,
      "note": "counts agree (consistency); identity is the postulate, not the agreement"},
     check=None)
assert all_twelve

# ---- W.2 the phase-ledger counting arithmetic -- DERIVED --------------------
# The Mathlib-free COUNTING core. One adjacency write costs one RADIT = 1/12 of the cycle.
# Provenance (CITED from maths-4 REFRAME-PHASE-LEDGER-ARITHMETIC, needs Real, not re-proved here):
#   contact half-angle = arcsin(1/2) = pi/6 ;  split write cost = (pi/3)/2 = pi/6 ;
#   cycle capacity = 2pi / (pi/6) = 12.
# Given that capacity is 12 radits, the counting is pure integer arithmetic:
CYCLE_RADITS = 12                                   # 2pi / (pi/6) = 12  (CITED)
WRITE_COST_RADITS = 1                               # one adjacency = one pi/6 arc  (CITED)
twelve_fills = (12 * WRITE_COST_RADITS == CYCLE_RADITS)      # 12 writes saturate exactly
thirteen_overflows = (13 * WRITE_COST_RADITS > CYCLE_RADITS)  # a 13th strictly overflows
step("W.2", "the phase-ledger arithmetic: twelve pi/6-writes fill the 2pi cycle, thirteen overflow",
     "12 * (pi/6) = 2pi (fills); 13 * (pi/6) > 2pi (overflows); in radits: 12 = 12, 13 > 12",
     ["W.1"],
     "the phase cycle has capacity 2pi; one adjacency write costs pi/6 (the contact half-angle "
     "arcsin(1/2), split between the two co-owners). So the cycle holds exactly 2pi/(pi/6) = 12 "
     "writes: twelve saturate it to the last arc, a thirteenth strictly overflows. The trig "
     "provenance (arcsin(1/2) = pi/6, 12*(pi/6) = 2pi, capacity = 12) was maths-4's "
     "REFRAME-PHASE-LEDGER-ARITHMETIC (THEOREM, needs Real) -- and as of the Mathlib-setup session "
     "(2026-08-21) it is now PROVED IN-REPO at Container10.PhaseLedgerReal (import Mathlib; axioms "
     "= Mathlib's three), no longer merely cited. What is DERIVED and Mathlib-FREE HERE is the "
     "COUNTING core: with the cycle measured in radits (units of pi/6), 12 = 12 fills and 13 > 12 "
     "overflows -- pure integer arithmetic by `decide`, zero-axiom, the same shape as rung 6's "
     "5 < 9. This proves the arithmetic IF the ledger picture (W.4) is right; it does not prove "
     "the picture.",
     "UNIQUE (given the pi/6 write cost, the capacity is exactly 12)", "DERIVED",
     {"cycle_radits": CYCLE_RADITS, "write_cost_radits": WRITE_COST_RADITS,
      "twelve_fills": twelve_fills, "thirteen_overflows": thirteen_overflows,
      "provenance": {"half_angle": "arcsin(1/2) = pi/6",
                     "saturation": "12*(pi/6) = 2pi",
                     "capacity": "2pi/(pi/6) = 12",
                     "source": "maths-4 REFRAME-PHASE-LEDGER-ARITHMETIC (THEOREM)",
                     "status": "proved in-repo at Container10.PhaseLedgerReal (Mathlib) as of 2026-08-21"}},
     check="12 writes fill the cycle (12=12); a 13th overflows (13>12)")
assert twelve_fills and thirteen_overflows

# ---- W.3 the phase cap is DIMENSION-INDEPENDENT -- DERIVED -------------------
# Spatial kissing numbers vary with dimension (CITED external, standard values); the phase cap
# does NOT -- the cycle is 1-D and arcsin(1/2) = pi/6 is a two-body planar angle, the same in any
# ambient dimension. So the phase road caps adjacencies at 12 regardless of d.
KISSING = {1: 2, 2: 6, 3: 12, 4: 24}                # CITED external (known kissing numbers)
PHASE_CAP = {d: CYCLE_RADITS for d in KISSING}      # 12 in every dimension
kissing_varies = len(set(KISSING.values())) > 1
phase_cap_constant = len(set(PHASE_CAP.values())) == 1 and next(iter(PHASE_CAP.values())) == 12
step("W.3", "the phase cap is 12 in ANY dimension (unlike spatial kissing, which varies)",
     "phase_cap(d) = 2pi/(pi/6) = 12 for all d; kissing(d) = 2,6,12,24 for d = 1,2,3,4",
     ["W.2"],
     "the contact half-angle arcsin(1/2) = pi/6 is a TWO-BODY planar computation (two equal "
     "spheres in contact span a 2-plane; the subtended angle is fixed there) -- it does not depend "
     "on the ambient dimension. And the phase cycle is 1-D (2pi). So the phase capacity is 12 in "
     "EVERY dimension. Spatial kissing, by contrast, VARIES: 2 (d=1), 6 (d=2), 12 (d=3), 24 (d=4) "
     "-- cited external values. This is WHY the phase road is the only route that can bound "
     "adjacencies at 12 as such: geometry gives 12 only at d=3, but the phase ledger gives 12 "
     "everywhere. The dimension-independence of arcsin(1/2) is the cited fact; the integer "
     "'cap = 12 in any d' is the content.",
     "UNIQUE (the phase cap is 12 independent of dimension)", "DERIVED",
     {"kissing_by_dim": KISSING, "phase_cap_by_dim": PHASE_CAP,
      "kissing_varies": kissing_varies, "phase_cap_constant": phase_cap_constant,
      "cited": "kissing numbers are external; arcsin(1/2)=pi/6 is dimension-independent (maths-4)"},
     check="phase cap = 12 for all d; kissing varies (2,6,12,24)")
assert kissing_varies and phase_cap_constant

# ---- W.4 THE POSTULATE (the headline) -- POSTULATE --------------------------
step("W.4", "THE POSTULATE: the phase cycle is the ledger on which adjacencies are written",
     "each mutual adjacency costs one pi/6 arc of the 2pi phase cycle (maths-4 GATE-PHASE-LEDGER "
     "half-a, OPEN)",
     ["W.2", "W.3"],
     "THE HEADLINE, and the grade of this whole container. The load-bearing identification is: "
     "'the phase cycle is the ledger on which a registration's adjacencies are written', each "
     "mutual adjacency spending one pi/6 arc. This is maths-4's GATE-PHASE-LEDGER half-a, and it "
     "is OPEN there for a precise reason: it is provably NOT derivable from its own road (the "
     "attempt is circular via CLOSURE-ZERO-SELF-INFORMATION; see GATE-PHASE-LEDGER-HALF-ANSWERED). "
     "It is EQUIVALENT to dim=3. So why-12 does not bottom out in a theorem -- it bottoms out in "
     "ONE named substrate postulate, the same species of bedrock as the reg-1 triad (00) and the "
     "geometric-balance bridge (05). Held, not proven. NOT dressed as a derivation.",
     "POSTULATE (the substrate identification; provably not derivable from its own road)",
     "POSTULATE",
     {"postulate": "the phase cycle is the adjacency ledger; one adjacency = one pi/6 arc",
      "source": "maths-4 GATE-PHASE-LEDGER half-a (OPEN)",
      "not_derivable": "circular via CLOSURE-ZERO-SELF-INFORMATION (GATE-PHASE-LEDGER-HALF-ANSWERED)",
      "equivalent_to": "dim = 3", "is_headline": True},
     check=None)

# ---- W.5 12 and d=3 follow FROM the postulate -- DERIVED (conditional) -------
# The integer content: among the kissing numbers, 12 is the maximum reached ONLY at d=3. So, GIVEN
# W.4 (adjacency-count = phase-writes = 12) plus registration completeness (spatial saturation
# realizes the max kissing), the count is 12 and the dimension is 3 -- uniquely.
dims_with_kissing_12 = [d for d, k in KISSING.items() if k == 12]
selects_dim_three = dims_with_kissing_12 == [3]
step("W.5", "GIVEN the postulate, 12 and d=3 follow (12 is max-kissing only at d=3)",
     "IF adjacency-count = phase-writes = 12 (W.4) AND completeness, THEN count = 12 and dim = 3",
     ["W.4", "W.3"],
     "CONDITIONAL, and the conditionality is the honesty. GIVEN W.4 (the adjacency count equals "
     "the phase writes = 12) and registration completeness (a saturated substrate realizes the "
     "maximum kissing in its dimension), the adjacency count is 12 and the dimension is 3. The "
     "integer selection: 12 is the maximum kissing number ONLY at d=3 (d=2 caps at 6, d=4 reaches "
     "24), so 'saturates at 12 mutual adjacencies' picks out d=3 uniquely. This DISCHARGES 01's "
     "OWED 1.6 (adjacency -> 12) and the dim=3 upper bound AS CONSEQUENCES of the one postulate "
     "W.4 -- NOT as a from-below derivation of 12. The implication is derived; its antecedent is "
     "the postulate.",
     "UNIQUE given W.4 + completeness (12 selects d=3 uniquely)", "DERIVED",
     {"kissing_by_dim": KISSING, "dims_where_kissing_is_12": dims_with_kissing_12,
      "selects_dim_three": selects_dim_three,
      "discharges": ["01 / 1.6 (adjacency -> 12)", "the dim=3 upper bound"],
      "conditional_on": "W.4 (the postulate) -- NOT a derivation of 12 from below"},
     check="12 is max-kissing uniquely at d=3; so W.4 + completeness => 12 and d=3")
assert selects_dim_three

# ---- W.6 the honest boundary -- OWED ----------------------------------------
step("W.6", "the honest boundary: geometry ALONE cannot force 12",
     "the separation lever is a checked negative; W.4 is irreducible; the no-13th is external",
     ["W.4", "W.5"],
     "what is NOT closed, stated as loud as what is. (a) GEOMETRY ALONE does not force 12: the "
     "three-observer SEPARATION lever was checked and FAILED "
     "(03/dim4-separation-check.py, control 6/3/0 reproduced) -- the 24-cell is a fully valid 4-D "
     "neighbor shell (24 neighbors, unseparated = 0), so equal-separation admits 24 at d=4. (b) "
     "The postulate W.4 is IRREDUCIBLE -- provably not derivable from its own road. (c) The no-13th "
     "upper bound (kissing(3)=12 exactly) is EXTERNAL (Schuette-van der Waerden 1953), cited, not "
     "machine-checked here. So why-12 has no clean geometric closer in hand; a real advance would "
     "need a NEW substrate principle that specifically excludes 24 neighbors / picks 12 over 24. "
     "This is the same species of bedrock as the reg-1 triad and the bridge -- named, not smuggled.",
     "OWED (no geometric closer; the postulate is irreducible; the upper bound is external)",
     "OWED",
     {"separation_lever": "checked NEGATIVE (03/dim4-separation-check.py; 24-cell valid at d=4)",
      "postulate_irreducible": "W.4 not derivable from its own road",
      "upper_bound_external": "no 13th = Schuette-van der Waerden 1953 (cited)",
      "what_would_close_it": "a new substrate principle excluding 24 neighbors / selecting 12 over 24"},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="10-why-twelve", steps=STEPS, grades=GRADES,
           values=dict(threads=THREADS, all_count_twelve=all_twelve,
                       cycle_radits=CYCLE_RADITS, write_cost_radits=WRITE_COST_RADITS,
                       twelve_fills=twelve_fills, thirteen_overflows=thirteen_overflows,
                       kissing_by_dim=KISSING, phase_cap_by_dim=PHASE_CAP,
                       dims_where_kissing_is_12=dims_with_kissing_12,
                       selects_dim_three=selects_dim_three,
                       headline_grade="POSTULATE"))

if __name__ == "__main__":
    p = HERE / "derivation.json"
    new = json.dumps(OUT, indent=1, sort_keys=True)
    if "--check" in sys.argv:
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != new:
            print("DERIVATION IS STALE -- rerun `python3 derivation.py`")
            sys.exit(1)
        print(f"derivation: {len(STEPS)} steps, all recompute "
              f"({GRADES['DERIVED']} derived, {GRADES['POSTULATE']} postulate, {GRADES['OWED']} owed)")
    else:
        p.write_text(new, encoding="utf-8")
        print(f"wrote derivation.json: {len(STEPS)} steps "
              f"({GRADES['DERIVED']} derived, {GRADES['POSTULATE']} postulate, {GRADES['OWED']} owed)")
        for s in STEPS:
            print(f"  {s['id']:<5} [{s['grade']:<9}] {s['what']}")
