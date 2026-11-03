#!/usr/bin/env python3
"""Container 02 -- the registration event and the observer triad. Rung 2, rests on 00.

Rung 2 is where CHANGE enters, and so where the floor's triad stops being latent. Rungs 0-1
seated three observers structurally (a POSTULATE); their criticality "is not manifest until we
examine change" (Kevin). The registration EVENT is that first change -- a potential distinction
becoming a stable one -- and the OBSERVER TRIAD is the arithmetic of why registering a change
takes THREE, not two.

  - The registration event: a potential (a raw candidate, not yet a distinction) is stabilised
    into a distinction. Before, there is no registered state; after, state and residual are
    present together. That transition is the first difference the floor can carry.
  - Observer & observed co-emerge: they arrive together through the event -- the two WITHIN --
    neither before the other, both existent, disjoint by label. (Corrected from maths 4's
    negation-dyad to the positive, existence-founded floor.)
  - The observer triad, as arithmetic (portable, zero-axiom): rotations of n points number n,
    permutations number n!. A rotation is indistinguishable from a permutation iff n! = n --
    true at 1 and 2, false from 3. And a cyclic order TURNS iff n >= 3. So ONE is static, TWO
    has POLARITY but no turning, and THREE is the first rank that turns AND where a rotation is a
    different thing from a permutation: the first orientation. That the third observer registers
    the change is the READING -- POSTULATE, exactly maths 4's OBSERVER-TRIAD-REGISTERS-DIFFERENCE,
    not lifted by the skeleton.

Grades: DERIVED / POSTULATE / OWED, first-class. `--check` recomputes the DERIVED steps.
"""

import json
import sys
from math import factorial

STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


def is_distinction(labels):                        # container 00's criterion, reused
    return ("defined" in labels) and ("undefined" in labels)


# ------------------------------------------------------------------ the event
# A potential distinction: a raw candidate, here a base with nothing defined yet -- not stable,
# not a distinction. The event stabilises it by defining the minimal thing.
BASE = ["a", "b", "c", "d"]
potential = {x: "undefined" for x in BASE}          # candidate: nothing distinguished yet
after = dict(potential); after[BASE[0]] = "defined"  # the event: stabilise (define one)

# ---- 2.1 the registration event -- DERIVED ----------------------------------
stable_before = is_distinction(potential.values())
stable_after = is_distinction(after.values())
step("2.1", "the registration event: potential becomes stable (the first change)",
     "event : potential (raw candidate) -> stable (a distinction)", [],
     "a registration event is the process by which a potential distinction becomes a stable one. "
     "Before, nothing is distinguished (no defined thing) -- it is not yet a distinction. The "
     "event stabilises it, and THAT transition is the first difference/change the floor carries. "
     "Rung 2 is where dynamics begin; no time is claimed, only a change.",
     "UNIQUE given the stabilising rule", "DERIVED",
     {"potential": potential, "stable_before": stable_before,
      "after_event": after, "stable_after": stable_after},
     check="potential not stable; after the event, stable")
assert (not stable_before) and stable_after

# ---- 2.2 observer & observed co-emerge -- DERIVED ---------------------------
state = [x for x in BASE if after[x] == "defined"]      # observed: the registered state
residual = [x for x in BASE if after[x] == "undefined"]  # observer's ground: the co-defining rest
step("2.2", "observer and observed co-emerge through the event",
     "before: no distinction; after: state and residual present together, disjoint by label",
     ["2.1"],
     "the observer and observed are not assumed to exist independently -- they emerge together "
     "through registration. On the corrected floor these are the two WITHIN: the state and its "
     "co-defining residual, both existent, arriving together, disjoint by label (no is-not). "
     "Neither is meaningful without the other, and neither precedes the other.",
     "UNIQUE", "DERIVED",
     {"observed_state": state, "observer_ground": residual,
      "co_emerge": bool(state) and bool(residual),
      "disjoint_by_label": set(state).isdisjoint(residual)},
     check="both present together, disjoint by label")
assert state and residual and set(state).isdisjoint(residual)

# ---- 2.3 the observer triad, as arithmetic -- DERIVED (zero-axiom skeleton) --
def rotations(n): return n
def permutations(n): return factorial(n)
def has_turning(n): return any(k != 0 and (2 * k) % n != 0 for k in range(n))
table = {n: {"rotations": rotations(n), "permutations": permutations(n),
             "rotation_is_permutation": rotations(n) == permutations(n),
             "turns": has_turning(n)} for n in range(1, 9)}
closure_rank = next(n for n in range(1, 9) if rotations(n) != permutations(n) and has_turning(n))
step("2.3", "the observer triad, as arithmetic: three is the first closure rank",
     "rotations(n)=n ; permutations(n)=n! ; turning iff exists 0<k<n with 2k != 0 mod n", ["2.2"],
     "a rotation is indistinguishable from a permutation exactly when n! = n -- true at 1 and 2, "
     "false from 3. And a cyclic order turns iff n >= 3. So ONE is static; TWO has polarity (the "
     "swap) but no turning; THREE is the first rank that turns AND where a rotation differs from a "
     "permutation. Polarity is two; orientation -- a registered difference -- is three.",
     "UNIQUE", "DERIVED",
     {"table": table, "first_closure_rank": closure_rank}, check="rot=perm at 1,2; rot<perm & turns from 3")
assert closure_rank == 3
assert table[1]["rotation_is_permutation"] and table[2]["rotation_is_permutation"]
assert not table[1]["turns"] and not table[2]["turns"] and table[3]["turns"]

# ---- 2.4 the third registers the change -- POSTULATE ------------------------
step("2.4", "the third observer is what registers a change (criticality manifests here)",
     "registering a DIFFERENCE requires the third observer (the without)", ["2.3"],
     "two poles co-defining is polarity; a registered difference -- a change, an orientation -- "
     "first exists at three, exactly where the skeleton (2.3) says rotation splits from "
     "permutation and turning appears. This is where the floor's latent triad becomes CRITICAL: "
     "under change, the third's role is manifest. The reading that this rank transition IS the "
     "three-observer condition is held, not proven (maths 4's OBSERVER-TRIAD-REGISTERS-DIFFERENCE).",
     "UNIQUE", "POSTULATE",
     {"polarity_is_two": True, "registered_difference_is_three": True,
      "criticality": "manifest under change (this rung)"}, check=None)

# ---- 2.5 the event's stable product is a distinction (tie to rung 1) -- DERIVED
tie = is_distinction(after.values())
step("2.5", "the event's stable product is a distinction -- the artifact rung 1 chains",
     "stable(event) = a container-00 distinction; rung 1 subdivides its residual", ["2.1"],
     "the event is the PROCESS (potential -> stable); the registration is its stable artifact -- a "
     "container-00 distinction. That is the join to rung 1, whose recursive registration divides "
     "the residual this event leaves. The event stabilises; the chain carries on.",
     "UNIQUE", "DERIVED", {"stable_is_distinction": tie}, check="stable product is a distinction")
assert tie

# ---- 2.6 the phase cycle and its capacity -- OWED ---------------------------
step("2.6", "the phase cycle at the event, and its capacity -> 12",
     "a cyclic order of minimal arcs; saturation fixes a capacity (to be derived)", ["2.3"],
     "the event opens a cyclic/phase structure (interchangeable minimal arcs, a write ledger that "
     "saturates). Its capacity is where the 12 will come from, with the icosahedron -- but that is "
     "downstream (05/06 and the phase tier), not built here. Foreshadowed, not claimed.",
     "OWED", "OWED", {"leads_to": "phase and the 12-capacity", "built_here": False}, check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="02-registration-event", steps=STEPS, grades=GRADES,
           values=dict(base=BASE, potential=potential, after_event=after,
                       observed_state=state, observer_ground=residual,
                       triad_table=table, first_closure_rank=closure_rank))

if __name__ == "__main__":
    import pathlib
    p = pathlib.Path(__file__).parent / "derivation.json"
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
