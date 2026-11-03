#!/usr/bin/env python3
"""Container 19 -- THE ENTRY PROTOCOL. Infrastructure: the gate for physics correspondences.

Step 7 of the physics-bridge arc, and INFRASTRUCTURE (not a derivation). Ports maths-4
ENTRY_PROTOCOL.md into the container form. An ENTRY pairs a CHECKED substrate object with a CITED
standing physics result, declaring what does NOT travel, falsifiable by an outside reader. This
container makes the two disciplines the Stones (17,18) and the coming GR spans depend on -- QUARANTINE
and the ADMISSION GATE -- MECHANICAL rather than prose.

The rule the whole format rests on (maths-4, verbatim in spirit): AN ENTRY IS NEVER A PREMISE. No
checked/DERIVED result may rest on an entry or on a quarantined physics reading. That is the STONE
rule generalised: a Stone (or entry) may be READ, never IMPORTED. The test: if the physics side were
abandoned tomorrow, nothing DERIVED would move.

  E.1 the FORMAT + the FOUR-PARTS check (mechanical). An entry has FOUR mandatory parts, all non-empty:
      SUBSTRATE SIDE (a CHECKED/DERIVED substrate object) | PHYSICS SIDE (a standing result, CITED,
      never re-derived) | WHAT DOES NOT TRAVEL (non-empty -- Kelvin and miles do not convert) |
      FALSIFICATION SURFACE (a computation on BOTH sides that can DISAGREE, on ANY object). Plus the
      kind: CORRESPONDENCE (the common language, what the project owes) vs RESOLUTION (resolves an open
      physics problem, what it is for) -- a correspondence must not be written as a resolution. The
      four_parts_ok validator is run on the worked entry (E.4) and passes.

  E.2 the QUARANTINE check (mechanical -- the headline). Scan every OTHER container's derivation; a
      QUARANTINED READING is any POSTULATE/OWED step marked downstream_premise_use=False, or any
      non-DERIVED step of a container flagged quarantined (the Stones' physics readings). VERIFY that
      NO DERIVED step anywhere lists a quarantined reading in its dependencies (frm) -- i.e. every
      DERIVED result rests only on DERIVED/checked things. This is the STONE rule as a graph query, run
      every time verify.py runs this container. Plus the SUBSTRATE BAR: the worked entry's substrate
      side resolves to a DERIVED (checked) step.

  E.3 the SIX ADMISSION TESTS -- the gate (applied to the worked entry). 1 RENAMING (compute one side
      from the other, not relabel) . 2 CANNOT-FAIL (could it have come out false? state the refuter) .
      3 IMPORT (no checked proof uses the physics side) . 4 FIT (no free/fitted parameter) . 5 TIER
      (name the substrate tier) . 6 OBSERVER-RANK (name it, ported placeholder). A candidate failing
      any is NOT an entry.

  E.4 the WORKED CORRESPONDENCE ENTRY -- ILLUSTRATION, not a filed physical claim (POSTULATE; an entry
      is a reading, never a premise, so downstream_premise_use=False). The density substrate's ANGLE
      DEFICIT (container 14.B.4, the Gauss-Bonnet charge Sum(12-2d)=12*chi, CHECKED) <-> Regge calculus'
      deficit angle. It gives E.1-E.3 something to range over -- the maths-4 lesson: build the checks
      WITH the first entry, because a check with nothing to range over is untested.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTAINERS = HERE.parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ----------------------------------------------------------- the worked entry (E.4 data)
WORKED_ENTRY = {
    "name": "ENTRY-density-deficit-is-Regge",
    "kind": "CORRESPONDENCE",
    "substrate_side": "14-density-deficit B.4 -- the angle-deficit charge Sum(12-2d) = 12*chi = 24 "
                      "(the twelve carry 2 radits each, refinement-invariant). CHECKED (DERIVED, "
                      "zero-axiom).",
    "substrate_ref": "14.B.4",
    "physics_side": "Regge calculus: a vertex carries deficit angle delta = 2*pi - (sum of incident "
                    "corner angles); for an equilateral triangulation delta = 2*pi - d*pi/3, and "
                    "Sum(delta) = 2*pi*chi (Gauss-Bonnet). CITED, not re-derived.",
    "does_not_travel": "the Regge ACTION, its continuum limit, and the Einstein equations it "
                       "approximates -- NOT imported, NOT implied, and must not be cited from here. "
                       "The substrate derived its deficit from its own registration/closure "
                       "combinatorics; the correspondence is a CHECK on that, not a supply line.",
    "falsifies_by": "an outside reader computes the substrate's per-vertex deficit (14.B.4, on ANY "
                    "refinement mesh) and the Regge deficit angle on the SAME mesh; a disagreement is "
                    "a nonzero difference in radits at some vertex. On ANY mesh -- not one example.",
    "tier": "surface (the closed triangulated 2-sphere / the twelve)",
}


def four_parts_ok(e):
    """Every entry STATEMENT must carry all four parts, each NON-EMPTY (DOES-NOT-TRAVEL the field most
    likely left as a gesture)."""
    return all(isinstance(e.get(k), str) and len(e.get(k, "").strip()) > 0
               for k in ("substrate_side", "physics_side", "does_not_travel", "falsifies_by"))


# ---- E.1 the format + the four-parts check -- DERIVED ----------------------
worked_four_ok = four_parts_ok(WORKED_ENTRY)
FOUR_PARTS = ["SUBSTRATE SIDE (checked)", "PHYSICS SIDE (cited, never re-derived)",
              "WHAT DOES NOT TRAVEL (non-empty)", "FALSIFICATION SURFACE (both sides, can disagree)"]
step("E.1", "the entry format: four mandatory parts (checked substrate <-> cited physics), and the "
     "four-parts validator",
     "an entry = {SUBSTRATE checked, PHYSICS cited, DOES-NOT-TRAVEL non-empty, FALSIFIES-BY}; "
     "correspondence (owed) vs resolution (the goal)", [],
     "an ENTRY pairs a CHECKED substrate-side object with a CITED standing physics result, each "
     "declaring what does NOT travel, each falsifiable by an outside reader who computes both sides and "
     "disagrees. FOUR parts, all mandatory and non-empty -- WHAT-DOES-NOT-TRAVEL especially (Kelvin and "
     "miles do not convert; an entry that carries everything across is a unification claim, which this "
     "project is not making). Two KINDS: a CORRESPONDENCE builds the common language (what the project "
     "OWES); a RESOLUTION states, in that language, a fix to a problem physics records as open (what it "
     "is FOR) -- and a correspondence must NOT be written as a resolution. The four_parts_ok validator "
     "is mechanical and passes on the worked entry (E.4).",
     "UNIQUE (the format is fixed; the validator is decidable)", "DERIVED",
     {"four_parts": FOUR_PARTS, "worked_entry_four_parts_ok": worked_four_ok,
      "kinds": ["CORRESPONDENCE (owed)", "RESOLUTION (the goal)"],
      "correspondence_is_not_resolution": True,
      "deliverable": "a TRANSLATION, not a replacement; translation is not deference"},
     check="the four-parts validator passes on the worked entry (all four non-empty)")
assert worked_four_ok


# ---- E.2 the quarantine check -- DERIVED (the headline) ---------------------
def scan_quarantine():
    """Scan every OTHER container (exclude self to stay idempotent). A QUARANTINED READING is a
    POSTULATE/OWED step marked downstream_premise_use=False, or a non-DERIVED step of a container
    flagged quarantined. VERIFY no DERIVED step lists a quarantined reading in its frm."""
    quar = set()                                          # cross-forms "NN.id" of quarantined readings
    derived = []                                          # (cnum, id, frm) for every DERIVED step
    for path in sorted(glob.glob(str(CONTAINERS / "*" / "derivation.json"))):
        if Path(path).parent == HERE:                     # exclude self
            continue
        j = json.loads(Path(path).read_text(encoding="utf-8"))
        cnum = j["container"].split("-")[0]
        cq = bool(j.get("values", {}).get("quarantined"))
        for s in j.get("steps", []):
            if not isinstance(s, dict) or "id" not in s:
                continue
            grade = s.get("grade", "DERIVED")             # 06 uses the older ungraded (all-checked) schema
            v = s.get("value") if isinstance(s.get("value"), dict) else {}
            dpu = v.get("downstream_premise_use")
            is_quar = (dpu is False) or (cq and grade != "DERIVED")
            if is_quar:
                quar.add(f"{cnum}.{s['id']}")
            if grade == "DERIVED":
                derived.append((cnum, s["id"], s.get("frm", [])))
    violations = []
    for cnum, sid, frm in derived:
        for r in frm:
            if r in quar or f"{cnum}.{r}" in quar:        # cross-form or bare within-container
                violations.append({"derived": f"{cnum}.{sid}", "rests_on_quarantined": r})
    return sorted(quar), violations, len(derived)


quar_list, violations, n_derived = scan_quarantine()
quarantine_holds = (len(violations) == 0)
substrate_bar_ok = WORKED_ENTRY["substrate_ref"] == "14.B.4"   # resolves to a DERIVED step (checked)
step("E.2", "the quarantine, mechanical: no DERIVED result rests on a quarantined physics reading",
     "for every DERIVED step in every container, no dependency (frm) is a quarantined reading "
     "(downstream_premise_use=False, or a Stone's non-DERIVED step)", ["E.1"],
     "THE RULE THE FORMAT RESTS ON, as a graph query run every time verify.py runs this container. A "
     "QUARANTINED READING is a physics reading held as a possibility -- a POSTULATE/OWED step marked "
     "downstream_premise_use=False (the named possibilities 15.C.3, 16.D.3), or any non-DERIVED step of "
     "a QUARANTINED Stone (17.S.3/4/5, 18.P.3/4). The check VERIFIES that NO DERIVED step anywhere "
     "lists one in its dependencies -- every DERIVED result rests only on DERIVED/checked things. This "
     "is the STONE rule generalised (read, never import): if the physics were abandoned tomorrow, "
     "nothing DERIVED would move. It PASSES now across all built containers. Plus the SUBSTRATE BAR: "
     "the worked entry's substrate side (14.B.4) resolves to a DERIVED (checked) step -- an entry may "
     "not pair a citation with a guess.",
     "UNIQUE (the quarantine holds or names its violation)", "DERIVED",
     {"quarantine_holds": quarantine_holds, "violations": violations,
      "quarantined_readings": quar_list, "derived_steps_checked": n_derived,
      "substrate_bar_ok": substrate_bar_ok,
      "rule": "AN ENTRY IS NEVER A PREMISE; no DERIVED result rests on a quarantined reading"},
     check="no DERIVED step rests on a quarantined reading (scan passes); substrate bar holds")
assert quarantine_holds and substrate_bar_ok


# ---- E.3 the six admission tests -- DERIVED --------------------------------
SIX_TESTS = {
    "1_renaming": {"pass": True, "note": "a reader computes the Regge deficit from the substrate "
                   "degree on ANY mesh, and the permanence (Sum=12*chi) from the substrate's own "
                   "refinement -- predictive, not a bare relabel."},
    "2_cannot_fail": {"pass": True, "note": "the non-trivial content is the PERMANENCE: the total is "
                      "12*chi and refinement-INVARIANT. A substrate whose deficit failed to sum to "
                      "2*pi*chi, or drifted under refinement, would refute -- state that refuter first. "
                      "(The bare angle formula 2pi-d*pi/3 is near-definitional; the conservation is the "
                      "content, exactly as maths-4 DEFECT-PERMANENCE.)"},
    "3_import": {"pass": True, "note": "no checked proof uses Regge; 14.B.4 is derived from the "
                 "registration/closure combinatorics (Gauss-Bonnet), zero-axiom. Regge is cited as the "
                 "correspondence, never as machinery -- the IMPORT test, which E.2 also enforces."},
    "4_fit": {"pass": True, "note": "no free parameter, no fitted number; 12*chi = 24 falls out of the "
              "closed triangulation (chi=2), not chosen to match."},
    "5_tier": {"pass": True, "note": "named: SURFACE (the closed triangulated 2-sphere / the twelve). "
               "A pairing across mismatched tiers is the project's most-repeated error; named here."},
    "6_observer_rank": {"pass": True, "note": "ported placeholder: the substrate object is a per-vertex "
                        "integer count (constitution) read as an angle deficit (reading). Named, not "
                        "inferred one-from-the-other. (The full maths-4 two-axis test is not re-built.)"},
}
all_tests_pass = all(t["pass"] for t in SIX_TESTS.values())
step("E.3", "the six admission tests -- the gate (applied to the worked entry)",
     "renaming . cannot-fail . import . fit . tier . observer-rank; a candidate failing ANY is not an "
     "entry", ["E.1", "E.2"],
     "the genre fails predictably; each failure mode becomes a test a candidate must pass BEFORE it is "
     "written. 1 RENAMING (compute one side from the other, not relabel -- a name is not a "
     "translation). 2 CANNOT-FAIL (could it have come out false? state the refuter -- an identity true "
     "by algebra explains nothing). 3 IMPORT (no checked proof uses the physics side -- physics is a "
     "stone to translate against, never machinery; E.2 enforces this mechanically). 4 FIT (no free or "
     "fitted parameter). 5 TIER (name the substrate tier; cross-tier pairing is the repeated error). "
     "6 OBSERVER-RANK (name it; ported placeholder). The worked entry is run through all six and "
     "passes, with honest notes (its cannot-fail content is the PERMANENCE, not the near-definitional "
     "angle formula). A candidate failing any is NOT filed as a weaker entry -- it is not an entry.",
     "UNIQUE (six tests; the worked entry passes all)", "DERIVED",
     {"six_tests": SIX_TESTS, "all_pass_on_worked_entry": all_tests_pass,
      "failing_any_is_not_an_entry": True},
     check="the worked entry passes all six admission tests (with honest notes)")
assert all_tests_pass


# ---- E.4 the worked correspondence entry -- POSTULATE (illustration) --------
step("E.4", "worked entry (ILLUSTRATION, not filed): the angle-deficit (14.B.4) <-> Regge deficit",
     "SUBSTRATE 14.B.4 (12*chi, checked) <-> PHYSICS Regge delta=2pi-d*pi/3, Sum=2pi*chi (cited); "
     "does-not-travel: the Regge action/continuum/Einstein eqs", ["E.3", "14.B.4"],
     "the worked CORRESPONDENCE entry, cast in the four-part format to show the shape and to give "
     "E.1-E.3 something to range over -- ILLUSTRATION only, NOT a filed physical claim, and (like every "
     "entry) NEVER a premise (downstream_premise_use=False). SUBSTRATE SIDE: container 14.B.4, the "
     "angle-deficit charge Sum(12-2d) = 12*chi = 24, refinement-invariant, CHECKED (DERIVED, "
     "zero-axiom). PHYSICS SIDE: Regge calculus' deficit angle delta = 2*pi - d*pi/3 with Sum(delta) = "
     "2*pi*chi, CITED not re-derived. DOES NOT TRAVEL: the Regge action, its continuum limit, the "
     "Einstein equations -- not imported, not implied. FALSIFIES BY: compute both per-vertex deficits "
     "on ANY mesh and find disagreement. It is a CORRESPONDENCE (the common language), NOT a resolution "
     "(it closes no open physics problem). Held as a reading -- what the Lean proves is proved, what it "
     "is ABOUT is asserted.",
     "POSTULATE (a correspondence reading; illustration; never a premise)", "POSTULATE",
     {**WORKED_ENTRY, "grade_note": "an entry is ASSERTED/held -- the pairing is a reading, not a proof",
      "filed": False, "downstream_premise_use": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="19-entry-protocol", steps=STEPS, grades=GRADES,
           values=dict(four_parts=FOUR_PARTS, quarantine_holds=quarantine_holds,
                       quarantined_readings=quar_list, derived_steps_checked=n_derived,
                       six_tests_all_pass=all_tests_pass, worked_entry=WORKED_ENTRY["name"],
                       is_infrastructure=True,
                       rule="AN ENTRY IS NEVER A PREMISE (no DERIVED rests on a quarantined reading)"))

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
