#!/usr/bin/env python3
"""Container 01 -- recursive registration. Rung 1, rests on container 00.

REBUILT 2026-08-19 on the corrected floor. The first version was the frozen, negation-founded
chain; this one carries the corrections:

  - Registration 2+ subdivides the RESIDUAL of registration 1 (all-that-is) -- both the totality
    as ever-present context AND the minimal cut at the residual's edge. The residual is
    'undefined-existent' selected POSITIVELY (label = undefined), never `not state`. No is-not.
  - The subdivision's EXTENTS nest (each residual inside the previous), but the IDENTITY of each
    registration is a LIVE co-definition: each is defined by its ADJACENT registrations, and if
    anything changes, all the adjacent relativities change -- stepwise. That liveness is what the
    'inject' propagation shows.
  - The triad carries up: every registration is registered by three observers (container 00).

Grades, first-class: DERIVED (recomputed/checkable here), POSTULATE (stated, capped), OWED
(deferred). The live co-definition is STRUCTURAL/POSTULATE; that adjacency forces 12 -> the
icosahedron is OWED to container 05/06 -- it is NOT built here.
"""

import json
import sys

STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ------------------------------------------------------------------ the model
# All-that-is: a field of existent things, all undefined at first (registration 1's residual).
# Each further registration DEFINES the minimal still-undefined thing -- a positive relabel,
# never a negation -- leaving a nested, smaller residual.
ALL_THAT_IS = ["a", "b", "c", "d", "e"]

# ---- 1.1 registration 2+ divides the residual of all-that-is -- DERIVED ------
labels = {x: "undefined" for x in ALL_THAT_IS}     # registration 1: all-that-is, undefined
chain = []
for i in range(2, len(ALL_THAT_IS) + 2):           # registrations 2,3,...
    undefined_now = [x for x in ALL_THAT_IS if labels[x] == "undefined"]
    if len(undefined_now) <= 1:
        break                                      # need >=1 to leave a residual after defining one
    x = undefined_now[0]                           # the minimal still-undefined thing
    labels[x] = "defined"
    defined_now = [y for y in ALL_THAT_IS if labels[y] == "defined"]
    residual_now = [y for y in ALL_THAT_IS if labels[y] == "undefined"]
    chain.append({"registration": i, "defined_this_step": x,
                  "defined": list(defined_now), "residual": list(residual_now),
                  "totality": list(ALL_THAT_IS)})
step("1.1", "registration 2+ subdivides the residual of all-that-is",
     "reg N+1 : within the totality, define one more of the residual (undefined-existent)",
     [],
     "both true at once: the division is OF the totality (all-that-is is the ever-present "
     "context) AND lands its minimal cut at the residual's edge (what is not yet defined). The "
     "residual is selected positively as 'undefined', not as 'not the state'.",
     "UNIQUE given the minimal rule", "DERIVED",
     {"totality": ALL_THAT_IS, "chain": chain}, check="each step defines one residual thing")

# ---- 1.2 each registration is a container-00 distinction -- DERIVED ----------
each_is_distinction = all(len(c["defined"]) > 0 and len(c["residual"]) > 0 for c in chain)
step("1.2", "each registration is a container-00 distinction (rests on 00)",
     "each step has a defined thing AND an undefined thing -> isDistinction", ["1.1"],
     "every registration, being a defined part with a residual left, is exactly a container-00 "
     "distinction: both poles witnessed, both existent. THE DEPENDENCY on 00, computed.",
     "UNIQUE", "DERIVED",
     {"every_step_is_a_distinction": each_is_distinction}, check="both poles at every step")
assert each_is_distinction

# ---- 1.3 the extents nest -- DERIVED ----------------------------------------
nests = all(set(chain[i]["residual"]).issubset(set(chain[i - 1]["residual"]))
            for i in range(1, len(chain)))
step("1.3", "the residual nests: each is inside the previous",
     "residual_{N+1} subset of residual_N subset of ... subset of all-that-is", ["1.1"],
     "the extents are monotone -- what is defined stays defined, so the undefined residual only "
     "ever shrinks and never re-covers a defined thing. This is the positive, live form of "
     "non-overlap: the state and residual are disjoint by their labels, at every step.",
     "UNIQUE", "DERIVED",
     {"nests": nests, "residual_sizes": [len(c["residual"]) for c in chain]},
     check="residual_{k} subset of residual_{k-1}")
assert nests

# ---- 1.4 co-definition by adjacency, live, stepwise -- STRUCTURAL/POSTULATE --
# Adjacency here: a registration co-defines with its immediate neighbours in the subdivision.
# The web is LOCAL (adjacent), not all-to-all, and change propagates stepwise -- the 'inject'.
adjacency = {c["registration"]: [n["registration"] for n in chain
                                 if abs(n["registration"] - c["registration"]) == 1] for c in chain}
step("1.4", "co-definition is by adjacency -- live, stepwise (the inject)",
     "identity(reg) := its live juxtaposition to its ADJACENT registrations", ["1.1"],
     "a registration is not defined by all others but by its adjacency; the definition is forever "
     "live -- change one and its adjacent relativities change, and that change propagates STEPWISE "
     "through the web. This is exactly why 'inject' spreads one ring at a time. The count of "
     "adjacencies is where 12 and the icosahedron will come from (owed, step 1.6).",
     "LOCAL (adjacency), live", "POSTULATE",
     {"adjacency": adjacency, "propagation": "stepwise (BFS over adjacency)"}, check=None)

# ---- 1.5 relational identity -- POSTULATE -----------------------------------
step("1.5", "relational identity: a registration IS its live adjacency, nothing stored",
     "identity read off the live web of adjacent co-definitions; equal web => equal identity",
     ["1.4"],
     "identity is not independent data: a registration is its live juxtaposition to its adjacent "
     "registrations, forever co-defining. Two identities with the same live web are the same. The "
     "triad carries up -- every registration is registered by three observers (container 00).",
     "UNIQUE up to the web", "POSTULATE",
     {"determined_by": "the live adjacency web", "triad_carries_up": True}, check=None)

# ---- 1.6 adjacency -> 12 -> the icosahedron -- OWED -------------------------
step("1.6", "the adjacency count 12 -> the icosahedron: 12 ACHIEVED + shape FORCED (03/09/11); only the metric no-thirteenth remains OWED",
     "|adjacency(reg)| = 12 -> the icosahedron: the 12 is ACHIEVED and the shape FORCED; the residual is "
     "only the metric no-thirteenth (exactly 12, no 13th)", ["1.4"],
     "RETREATED 2026-09-03: this was filed 'OWED, to be earned at 05/06', and it has since been largely "
     "DISCHARGED. That a registration can carry 12 adjacencies (the kissing number) and that the 12 form "
     "the ICOSAHEDRON is FORCED downstream: container 03 forces the closed uniform triangular trichotomy "
     "(d,V) = (3,4),(4,6),(5,12) and the three-observer separation selects the icosahedron UNIQUELY "
     "(03.3.3/3.4, DERIVED); container 09 achieves the kissing 12; container 11 builds the icosahedral "
     "shell. What REMAINS is only the UPPER bound -- a substrate-native METRIC no-thirteenth (exactly 12, "
     "no 13th neighbour by geometry, not the topological census) -- and this is the SAME single open item "
     "as 03.3.7, 09.6.6 and 25.DF.3. So four OWEDs collapse to ONE open problem, which container 03 records "
     "nothing in the corpus yet supplies. The 12 is achieved and the shape forced; only its uniqueness "
     "(no 13th, hence the ambient dim=3) is open.",
     "OWED (only the metric no-thirteenth; the 12-achieved -> icosahedron is DISCHARGED by 03/09/11)", "OWED",
     {"achieved": "12 adjacencies -> the icosahedron, FORCED by 03 (closure+separation) / 09 (kissing) / 11 (shell)",
      "remaining_owed": "a substrate-native metric no-thirteenth (exactly 12, no 13th) -- the SAME open item as 03.3.7, 09.6.6, 25.DF.3",
      "consolidation": "four OWEDs (01.1.6, 03.3.7, 09.6.6, 25.DF.3) collapse to ONE open problem: the metric no-thirteenth / ambient dim=3",
      "built_here": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="01-recursive-registration", steps=STEPS, grades=GRADES,
           values=dict(totality=ALL_THAT_IS, chain=chain, adjacency=adjacency,
                       length=len(chain), nests=nests))

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
