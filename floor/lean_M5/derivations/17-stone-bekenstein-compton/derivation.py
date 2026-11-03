#!/usr/bin/env python3
"""Container 17 -- STONE: BEKENSTEIN-COMPTON. The ruler BC = 2*pi/ln2. EXTERNAL, QUARANTINED.

Step 5 of the physics-bridge arc, and the FIRST STONE. A Stone is EXTERNAL, established physics held
OUTSIDE the derivation chain as a calibration a bridge must match -- read NEVER as a premise, and
re-derived COLD here (reconstructed from its relations, importing no maths-4 literal). This is where
the physical constants (hbar, c, alpha) first enter the arc at all.

THE STONE'S PURPOSE (Kevin, 2026-08-25): a KNOWN, SCALE-INVARIANT handle. BC = 2*pi/ln2 is
dimensionless, so once the bridge is made and verified, this reference can be run UP AND DOWN THE SCALE
without changing -- a fixed ruler.

WHAT "RE-DERIVE COLD" MEANS HERE (vs cite): CITING is importing "BC = 2*pi/ln2" as a fact.
RE-DERIVING COLD is reconstructing the chain from its criteria -- Bekenstein bound -> Compton scale ->
rest energy -> the cancellation -> the ln2 to bits -> the number -- recomputing that 2*pi/ln2 actually
falls out, and making every ASSUMED step an explicit POSTULATE in the chain rather than a silent
equality. The cold re-derivation's whole value is that it SURFACES the assumptions.

THE FULL CHAIN (from maths-4 `The BC constant.docx`, re-derived, not imported):
  1. Bekenstein bound (bits form):  S <= 2*pi*R*E / (hbar*c*ln2).
  2. Length scale = Compton:        R = hbar/(m c)   (the substantive move; the unique scale that
                                                       cancels -- de Broglie/Schwarzschild/thermal do not).
  3. Energy = rest energy:          E = m c^2.
  4. Substitute & cancel:           R*E = (hbar/mc)(mc^2) = hbar*c; S = 2*pi*(hbar c)/(hbar c ln2)
                                    = 2*pi/ln2 = 9.064720...  (m AND hbar,c all drop out).

THE TWO LIVE CAUTIONS (the doc's own) + Kevin's, made first-class POSTULATE/OWED here:
  - the ln2 is a UNIT CONVENTION (nats->bits); "9.0647 bits" = "2*pi nats in bits" -- no physical
    content beyond 2*pi until "why base-2 registration is FORCED not chosen" resolves (OPEN).
  - it is an IDENTITY, not a prediction -- it does not yet forbid anything standard physics permits.
  - (Kevin) the Compton = one full sine wave = a circumference (2*pi) equivalence -- i.e. R = hbar/(mc)
    IS the registration boundary -- was ASSUMED, worked by coincidence, NEVER PROVEN
    (= maths-4 SEC9-PHASE-CLOSURE-HYPOTHESIS, OPEN).

QUARANTINE: no downstream container may use this Stone's PHYSICAL reading as a premise until its
assumptions (S.3) and owed groundings (S.4) resolve. The exact ALGEBRA (S.1) and scale-invariance
(S.2) are DERIVED and may be relied on as arithmetic; the physics they are dressed in is held.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


def d6(x):
    return round(x, 6)


# ---- S.1 the cold algebra: mass cancels, BC = 2*pi/ln2 -- DERIVED -----------
# The cancellation is a pure multiplicative identity (true in any commutative semiring). Re-derived
# COLD with exact integers (not importing maths-4's mass_cancels): given R*(m*c)=hbar and E=m*c*c,
# R*E = hbar*c exactly, m absent. Checked here on integer witnesses; the Lean proves it for all Nat.
def mass_cancels(R, m, hbar, c, E):
    assert R * (m * c) == hbar and E == m * c * c            # the two cleared relations
    return R * E == hbar * c                                 # m cancels -> hbar*c


# witnesses built so the two cleared relations hold by construction: hbar=R*m*c, E=m*c*c
cancel_witnesses = [(R, m, R * m * c, c, m * c * c) for (R, m, c) in [(2, 3, 1), (5, 2, 2), (1, 7, 1)]]
cancel_ok = all(mass_cancels(R, m, hb, c, E) for (R, m, hb, c, E) in cancel_witnesses)
# the scalar value 2*pi/ln2 (needs reals; the arithmetic on top of the cancellation)
two_pi = 2 * math.pi
ln2 = math.log(2)
BC = two_pi / ln2
step("S.1", "the cold algebra: mass cancels (R*E = hbar*c), so BC = 2*pi/ln2 = 9.064720...",
     "given R=hbar/(mc) [R*mc=hbar] and E=mc^2: R*E = hbar*c (m cancels); "
     "S = 2*pi*(hbar c)/(hbar c*ln2) = 2*pi/ln2", [],
     "the Bekenstein bound in bits is S <= 2*pi*R*E/(hbar*c*ln2). Put R at the Compton scale "
     "(R*(m c)=hbar, the cleared form of R=hbar/mc) and E at the rest energy (E=m c^2). Then R*E = "
     "(hbar/mc)(mc^2) = hbar*c EXACTLY -- a pure multiplicative identity, m absent -- re-derived cold "
     "here on integer witnesses (the Lean proves it for all Nat, zero-axiom, our own proof, not maths "
     "4's). So S = 2*pi*(hbar c)/(hbar c*ln2) = 2*pi/ln2 = 9.064720... The value is reconstructed from "
     "the relations, NOT imported. hbar*c cancels top and bottom; nothing mass/energy-dependent "
     "survives.",
     "UNIQUE (the identity R*E=hbar*c is exact; 2*pi/ln2 is then fixed)", "DERIVED",
     {"mass_cancellation_holds": cancel_ok, "cancellation_law": "R*E = hbar*c (m absent)",
      "two_pi": d6(two_pi), "ln2": d6(ln2), "BC_value": round(BC, 6),
      "BC_expr": "2*pi/ln2", "reconstructed_not_imported": True},
     check="R*E = hbar*c (mass cancels) on witnesses; BC = 2*pi/ln2 = 9.064720")
assert cancel_ok and abs(BC - 9.064720) < 1e-5

# ---- S.2 scale invariance -- DERIVED (the handle) --------------------------
# For ANY positive (m, hbar, c), S = 2*pi*(hbar/(m c))*(m c^2)/(hbar c*ln2) = 2*pi/ln2 -- exactly,
# using exact rationals for the mass-dependent factor so the cancellation is provably exact (not float).
def S_over_2pi_ln2(m, hbar, c):
    # (R*E)/(hbar*c) with R=hbar/(m c), E=m c^2, as an exact Fraction -> must be 1
    R = Fr(hbar, m * c)
    E = Fr(m * c * c, 1)
    return R * E / Fr(hbar * c, 1)                           # = 1 exactly for all m
mass_range = [(1, 6, 3), (1000000, 6, 3), (7, 11, 5), (10**9, 2, 2), (3, 10**6, 4)]
all_unit = all(S_over_2pi_ln2(m, hb, c) == 1 for (m, hb, c) in mass_range)
step("S.2", "scale invariance: BC is dimensionless, the SAME for every mass -- the scale-invariant handle",
     "(R*E)/(hbar*c) = 1 for ALL positive (m, hbar, c), exact; so S = 2*pi/ln2 at every scale", ["S.1"],
     "because m and the pair (hbar, c) drop out COMPLETELY, BC = 2*pi/ln2 is a pure number -- the same "
     "at every scale. Checked exactly (in rationals, not floats) across a wide mass range: (R*E)/(hbar*c) "
     "= 1 identically, from tiny to huge m. This is the STONE'S PURPOSE (Kevin): a KNOWN, "
     "SCALE-INVARIANT reference handle -- once the bridge is made and verified, run it up and down the "
     "scale and it does not change. The maths-4 note confirms ~30 orders of magnitude (Planck mass to "
     "light neutrino) return 9.0647 to float noise; here the invariance is exact in Q.",
     "UNIQUE (dimensionless; scale-invariant by exact cancellation)", "DERIVED",
     {"ratio_is_one_for_all_masses": all_unit, "masses_checked": len(mass_range),
      "purpose": "a known, scale-invariant handle to run up/down the scale once the bridge is verified",
      "maths4_numeric_confirmation": "~30 orders of magnitude -> 9.0647 to float noise"},
     check="(R*E)/(hbar*c) = 1 exactly for every mass tested -> BC scale-invariant")
assert all_unit

# ---- S.3 the assumed equivalences -- POSTULATE (unproven) ------------------
step("S.3", "the ASSUMED equivalences (unproven): Compton = 2*pi-circumference / registration boundary; "
     "the ln2 base-2 convention",
     "R=hbar/(mc) IS the registration boundary (Compton = one full wave = 2*pi) -- ASSUMED; ln2 is a "
     "unit convention (nats->bits)", ["S.1"],
     "the cold re-derivation's job is to surface what the identity RESTS on, and it rests on assumptions "
     "that are NOT proven. (a) THE COMPTON EQUIVALENCE (Kevin, 2026-08-25): the Compton wavelength taken "
     "as one full sine wave = a circumference (2*pi), i.e. R = hbar/(mc) IS the minimum registration "
     "boundary -- this was ASSUMED; it worked, with a lot of coincidence, but was NEVER PROVEN "
     "(= maths-4 SEC9-PHASE-CLOSURE-HYPOTHESIS, OPEN). Choosing Compton is 'the substantive move, not "
     "free' -- the unique scale that cancels -- but its geometric MEANING is assumed. (b) THE ln2 "
     "CONVENTION (the doc's own caution): ln2 converts nats->bits, a UNIT convention not a physical "
     "fact; '9.0647 bits' = '2*pi nats in bits', carrying no physical content beyond 2*pi until 'why "
     "base-2 registration is FORCED not chosen' is settled. Both are held as POSTULATEs -- used to state "
     "the Stone, flagged as unproven, open to refutation. This is the honest core Kevin named.",
     "POSTULATE (assumed, unproven; the Stone's load-bearing equivalences)", "POSTULATE",
     {"compton_is_registration_boundary": "ASSUMED, never proven (SEC9-PHASE-CLOSURE-HYPOTHESIS, OPEN)",
      "compton_as_2pi_circumference": "Kevin: assumed; worked by coincidence; unproven",
      "ln2_is_unit_convention": "nats->bits; no physical content beyond 2*pi until base-2 is forced",
      "status": "held as POSTULATE, flagged unproven"},
     check=None)

# ---- S.4 what would ground / discriminate it -- OWED -----------------------
step("S.4", "what is OWED: a proof of the equivalence, why base-2 is forced, and DISCRIMINATION "
     "(it is an identity, not a prediction)",
     "owed: prove Compton=boundary; prove base-2 forced (Shannon vs registration); make it forbid "
     "something (currently only an identity)", ["S.3"],
     "for the Stone to become more than a matched calibration, three things are genuinely OWED (none "
     "supplied). (i) A PROOF of the Compton-radius-as-registration-boundary equivalence (S.3a) -- the "
     "SEC9 hypothesis, open. (ii) WHY BASE-2 (the ln2) is forced rather than chosen -- the "
     "Shannon-entropy-vs-registration-events reconciliation, open; until it resolves 9.0647 cannot be "
     "read as a registration quantum without circularity. (iii) DISCRIMINATION: the derivation is an "
     "IDENTITY, telling you what the Bekenstein bound EQUALS at a self-referential scale; it does not "
     "yet forbid anything standard physics permits. It passes CONFIRMED because the algebra and numerics "
     "hold, NOT because it discriminates. These are the owed items, named so momentum does not erase "
     "them.",
     "OWED (the groundings that would turn a calibration identity into a discriminating result)", "OWED",
     {"owed_1_prove_equivalence": "Compton = registration boundary (SEC9, open)",
      "owed_2_why_base_2": "Shannon-vs-registration reconciliation (open)",
      "owed_3_discrimination": "currently an identity, not a prediction; forbids nothing yet",
      "present": False},
     check=None)

# ---- S.5 Kevin's Planck hypothesis -- POSTULATE (to prove or refute) -------
step("S.5", "Kevin's Planck hypothesis: Planck length = registration-to-registration; Planck time = "
     "state-change rate (a hypothesis, to prove or refute)",
     "l_P = registration-to-registration edge; t_P = the state-change rate registration-to-registration "
     "(the tick)", ["S.3"],
     "a candidate ANSWER to S.3's open 'what is the registration boundary', offered by Kevin "
     "(2026-08-25) explicitly AS A HYPOTHESIS needing proof or refutation, not a result: the PLANCK "
     "LENGTH is the registration-to-registration separation (the edge of the adjacency web), and PLANCK "
     "TIME is the state-change RATE registration-to-registration (the tick). This would connect to "
     "c = alpha/tau (info quantum per tick, Step 6 territory) and would, if proven, supply the physical "
     "meaning S.3 assumes. It is NOT derived and NOT relied on anywhere; recorded as an open hypothesis "
     "to test. Held, capped, open to refutation.",
     "POSTULATE (Kevin's hypothesis; to prove or refute; not relied on)", "POSTULATE",
     {"planck_length": "registration-to-registration (the edge)",
      "planck_time": "the state-change rate registration-to-registration (the tick)",
      "connects_to": "c = alpha/tau (Step 6)", "status": "hypothesis; to prove or refute; not relied on",
      "author": "Kevin, 2026-08-25"},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="17-stone-bekenstein-compton", steps=STEPS, grades=GRADES,
           values=dict(BC_value=round(BC, 6), BC_expr="2*pi/ln2", two_pi=d6(two_pi), ln2=d6(ln2),
                       mass_cancellation="R*E = hbar*c (m absent)",
                       scale_invariant=True, masses_checked=len(mass_range),
                       is_external_stone=True, quarantined=True,
                       assumed_equivalence="Compton = 2*pi / registration boundary (SEC9, OPEN)",
                       planck_hypothesis="l_P = reg-to-reg; t_P = state-change rate (Kevin, to prove/refute)"))

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
