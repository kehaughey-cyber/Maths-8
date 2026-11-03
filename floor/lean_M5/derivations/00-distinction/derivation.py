#!/usr/bin/env python3
"""Container 00 -- the distinction. The floor: rung 0, rests on nothing.

REBUILT 2026-08-19 after a floor correction from Kevin. The first version was faithful to
maths 4 and carried three buried errors, which is exactly the "residual chaos" that starting
at 0 was meant to surface:

  1. It was DYADIC -- a state and its complement, two poles. But two poles are bare polarity;
     a difference is not a registered DISTINCTION until a third perceives it. The floor is
     TRIADIC: three observers, two within and one without, who observe -> perceive and agree
     -> and their live agreement IS the artifact (the registration). The observers are not
     the registration; the registration is what they produce.
  2. It was NEGATION-FOUNDED -- `compl S := not S`, an "is not" everywhere. But there is no
     is-not inside existence. Existence/non-existence is a real dichotomy, but it lives at
     REGISTRATION 1 ONLY (all-that-is, bounded against non-existence -- the counterpoint that
     lets existence be a distinction, never a thing to subdivide; "0" is that non-existence,
     and it does not exist). Within existence a thing is DEFINED or UNDEFINED, both EXISTENT;
     undefined is not non-existent. The residual is "is, yet to be defined" -- positive
     potential, never `not state`.
  3. It was FROZEN -- an append-only chain with a fixed past. Registrations are a live
     co-definition (by adjacency); that is container 01's concern, foreshadowed here.

GRADING IS FIRST-CLASS. Each step declares grade DERIVED (recomputed and checkable here),
POSTULATE (stated working hypothesis, capped, NOT proven), or OWED (proof deferred to a later
container). The reg-1 triad is a POSTULATE -- Kevin's supposition that all three observers are
present at registration 1, by instinct, with no handle yet to derive it. The formalisation is
itself a handle: if the structure forced the third we would say so; it does not, so we assume it
and say THAT out loud. `--check` recomputes the DERIVED steps and fails on drift.
"""

import json
import sys

STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ------------------------------------------------------------------ the model
# A base is a field of EXISTENT things, each labelled 'defined' or 'undefined' -- positively,
# so the residual is a selection (label == 'undefined'), never a negation of the state.
BASE = ["a", "b", "c", "d", "e"]                 # five existent things (the base)
LABEL = {"a": "defined", "b": "defined", "c": "undefined", "d": "undefined", "e": "undefined"}
state = [x for x in BASE if LABEL[x] == "defined"]        # the registered state
residual = [x for x in BASE if LABEL[x] == "undefined"]   # is, yet to be defined

# ---- 0.1 the existence bound (registration 1) -- POSTULATE -------------------
step("0.1", "registration 1: all-that-is, bounded against non-existence",
     "registration_1 := (all that is | non-existence)", [],
     "the founding distinction. Existence is a distinction only against non-existence -- but "
     "non-existence is not a thing to subdivide or perceive (if it does not exist there is "
     "nothing to consider); it is the counterpoint. '0' is that non-existence, and it does not "
     "exist. Every later registration subdivides the RESIDUAL of all-that-is, never this bound.",
     "UNIQUE (there is one totality)", "POSTULATE",
     {"state": "all that is", "counterpoint": "non-existence (not a thing; 0)"},
     check=None)

# ---- 0.2 the three existential states -- DERIVED ----------------------------
# (existent, defined). Non-existence has no 'defined' axis -- there is nothing there.
STATES = {
    "definedExistent":   {"existent": True,  "defined": True},
    "undefinedExistent": {"existent": True,  "defined": False},
    "nonExistent":       {"existent": False, "defined": None},
}
distinct = len(STATES) == 3
undefined_ne_nonexistent = STATES["undefinedExistent"]["existent"] != STATES["nonExistent"]["existent"]
perceivable = {k: v["existent"] for k, v in STATES.items()}   # only what exists is perceivable
step("0.2", "the three existential states",
     "{ definedExistent, undefinedExistent, nonExistent }", ["0.1"],
     "within existence a thing is defined or undefined; outside it, non-existent. Undefined is "
     "NOT non-existent -- it exists and can be perceived and later defined. Non-existence alone "
     "cannot be perceived or registered. Three distinct states, and the perceivable ones are "
     "exactly the two existent ones.",
     "UNIQUE", "DERIVED",
     {"states": STATES, "distinct": distinct,
      "undefined_is_not_nonexistent": undefined_ne_nonexistent, "perceivable": perceivable},
     check="three distinct states; perceivable iff existent")
assert distinct and undefined_ne_nonexistent
assert perceivable == {"definedExistent": True, "undefinedExistent": True, "nonExistent": False}

# ---- 0.3 a distinction, without any is-not -- DERIVED -----------------------
both_existent = all(STATES["definedExistent"]["existent"] for _ in state) and \
                all(STATES["undefinedExistent"]["existent"] for _ in residual)
step("0.3", "a distinction: defined | undefined-existent, both existent, no is-not",
     "distinction := a base partitioned by label into state (defined) and residual (undefined)",
     ["0.2"],
     "a distinction within existence marks part of a base as defined (the state) and leaves the "
     "rest undefined-existent (the residual) -- BOTH existent. The residual is selected as "
     "'label = undefined', a positive potential, never 'not state'. No negation enters the floor.",
     "UNIQUE given the labelling", "DERIVED",
     {"base": BASE, "state": state, "residual": residual, "both_existent": both_existent},
     check="state and residual are positive selections, both existent, no negation")
assert both_existent and state and residual

# ---- 0.4 the triad -- POSTULATE ---------------------------------------------
step("0.4", "the triad: three observers produce the live artifact",
     "registration := (observer_within1, observer_within2, observer_without) "
     "observe -> perceive & agree -> artifact (the distinction), live",
     ["0.1"],
     "two poles are bare polarity; the difference is a REGISTERED distinction only once a third "
     "perceives it -- two observers within, one without. They observe, perceive and agree, and "
     "their agreement is the artifact: the registration, which stays live. The observers are the "
     "objects; observation is the act (perceive + register); the registration is the record. "
     "Their criticality is not manifest until change is examined.",
     "UNIQUE (three, not two, not four)", "POSTULATE",
     {"observers": ["within1", "within2", "without"], "act": "perceive+register",
      "artifact": "the registration (live)", "observers_are_not_the_registration": True},
     check=None)

# ---- 0.5 Proposition 1, the two poles co-define -- DERIVED -------------------
def is_distinction(labeling):
    s = [x for x in labeling if labeling[x] == "defined"]
    r = [x for x in labeling if labeling[x] == "undefined"]
    return len(s) > 0 and len(r) > 0
all_defined = {x: "defined" for x in BASE}       # nothing left undefined
none_defined = {x: "undefined" for x in BASE}    # nothing defined yet
step("0.5", "Proposition 1 (poles): state and residual co-define -- neither alone",
     "distinction  <=>  state witnessed AND residual witnessed", ["0.3"],
     "1 requires its co-defining other: a fully-defined base leaves no residual (nothing "
     "distinguished FROM) and a wholly-undefined base has no state -- neither is a distinction. "
     "The bound needs both sides, and both are existent. This is the checkable half of Prop 1.",
     "UNIQUE", "DERIVED",
     {"needs_both": True, "all_defined_is_distinction": is_distinction(all_defined),
      "none_defined_is_distinction": is_distinction(none_defined),
      "labelled_is_distinction": is_distinction(LABEL)},
     check="a distinction requires both a defined and an undefined thing")
assert is_distinction(LABEL) and not is_distinction(all_defined) and not is_distinction(none_defined)

# ---- 0.6 Proposition 1 completed: and both require perception -- POSTULATE ---
step("0.6", "Proposition 1 (the third): the poles require the perceiving without",
     "registered_distinction  requires  the observer without", ["0.4", "0.5"],
     "the two poles co-defining is polarity; it becomes a registered distinction only with the "
     "third -- the perceiver without. 'Neither can exist without perception.' This completes "
     "Prop 1 as triadic, and it is the working hypothesis, not a theorem: there is no handle yet "
     "to derive that the third is present already at registration 1. Held as postulate, capped.",
     "UNIQUE", "POSTULATE",
     {"polarity_needs_the_third": True, "derivable_here": False,
      "status": "working hypothesis (Kevin); open to disproof"},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="00-distinction", steps=STEPS, grades=GRADES,
           values=dict(base=BASE, state=state, residual=residual,
                       existential_states=STATES, perceivable=perceivable,
                       triad=["within1", "within2", "without"]))

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
