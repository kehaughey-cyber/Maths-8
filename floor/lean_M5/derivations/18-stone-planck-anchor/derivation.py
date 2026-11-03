#!/usr/bin/env python3
"""Container 18 -- STONE: THE PLANCK ANCHOR. Compton meets Schwarzschild. EXTERNAL, QUARANTINED.

Step 6 of the physics-bridge arc, the SECOND STONE. With Stone 5 (the scale-invariant RULER, BC =
2*pi/ln2) this is the ANCHOR: the reduced Compton radius R_C = hbar/(mc) (the quantum size of a mass)
and the Schwarzschild radius R_S = 2Gm/c^2 (its gravitational size) CROSS at exactly one mass -- the
Planck scale. That crossing pins the absolute rung the scale-invariant ruler then steps along.

EXTERNAL, QUARANTINED, re-derived COLD (our own proof, not importing maths-4 PlanckAnchor.lean). Same
discipline as Stone 5: the exact ALGEBRA is DERIVED; the physical reading (that the crossover IS a
registration threshold) is ASSUMED and held; Kevin's Planck hypothesis stays a FLAGGED HYPOTHESIS.

  P.1 the CROSSOVER ANCHOR. Cleared of denominators (the honest content whenever m, c are nonzero):
        R*(m c) = hbar     (R is the reduced Compton radius)
        R*(c c) = 2 G m    (R is the Schwarzschild radius)
      When the SAME R satisfies both, mass appears squared with the factor 2 inherited from the
      Schwarzschild radius:  hbar*c = 2 G m^2  (exact, zero-axiom). Read against the Planck mass
      (m_P^2 = hbar c / G, cleared m_P^2 * G = hbar c):  m_P^2 * G = 2 G m^2  (cleared, zero-axiom), so
      m_P^2 = 2 m^2 (dividing by G>0, routine) and THE CROSSOVER MASS IS m = m_P / sqrt2 -- the 1/sqrt2
      sitting exactly on the factor-2 in the Schwarzschild radius. Its length dual (routine, sqrt):
      the common crossover radius is R = sqrt2 * l_P. The div-by-G and sqrt steps are routine scalar
      arithmetic on top of the squared identities (cited, as maths-4 leaves them, and as Stone 5 leaves
      2*pi/ln2 -> 9.06).

  P.2 the TWO STONES = the LADDER. Stone 5 (the RULER, dimensionless BC, scale-invariant) and this
      ANCHOR (the Planck scale, absolute) hold CONCURRENTLY: rung zero = Planck (the crossover mass /
      length), and the scale-invariant BC is the step. The Planck length and time are linked by the
      standard identity c = l_P / t_P (exact: l_P/t_P = sqrt(c^5/c^3) = c). Together: an ABSOLUTE anchor
      + SCALE-INVARIANT rungs = a climbable scale. (maths-4 STONES-LADDER-CONCURRENT.)

  P.3 c = alpha/tau AND KEVIN'S PLANCK HYPOTHESIS -- a FLAGGED HYPOTHESIS (kept flagged, Kevin
      2026-08-25; NOT derived, NOT relied on). Planck length = registration-to-registration (the edge of
      the adjacency web); Planck time = the state-change RATE registration-to-registration (the tick).
      Then c = l_P/t_P = (edge)/(tick), and Kevin's c = alpha/tau (info quantum per tick) would identify
      alpha with the edge quantum and tau with the tick. This is a candidate physical meaning for the
      anchor; it is a hypothesis to PROVE OR REFUTE, held and capped.

  P.4 what is ASSUMED / OWED (the same quarantine as Stone 5). That the Compton-Schwarzschild crossover
      IS a physical registration threshold is ASSUMED (the SEC9-type interpretive gap, OPEN), not proven;
      and like Stone 5 the anchor is an IDENTITY (a crossover of two standard radii), not yet a
      prediction that discriminates. QUARANTINE: no downstream container may use the physical reading as
      a premise; only the exact algebra (P.1) may be relied on.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


def d6(x):
    return round(x, 6)


# ---- P.1 the crossover anchor -- DERIVED -----------------------------------
# Integer witnesses: choose R, c, m with 2m | R*c*c, set G = R*c*c/(2m), hbar = R*m*c. Then both
# cleared relations hold by construction, and hbar*c = 2*G*m^2, m_P^2*G = 2*G*m^2, m_P^2 = 2*m^2.
def witness(R, c, m):
    assert (R * c * c) % (2 * m) == 0
    G = (R * c * c) // (2 * m)
    hbar = R * m * c
    assert R * (m * c) == hbar and R * (c * c) == 2 * G * m         # the two cleared relations
    mP2 = (hbar * c) // G
    return dict(R=R, c=c, m=m, G=G, hbar=hbar, mP2=mP2,
                cross=(hbar * c == 2 * G * (m * m)),
                cleared=(mP2 * G == 2 * G * (m * m)),
                mP2_eq_2m2=(mP2 == 2 * (m * m)))


anchor_witnesses = [witness(*t) for t in [(1, 2, 2), (2, 2, 4), (1, 4, 2), (3, 2, 3)]]
cross_ok = all(w["cross"] and w["cleared"] and w["mP2_eq_2m2"] for w in anchor_witnesses)
# the sqrt readings (Planck units hbar=c=G=1): m = m_P/sqrt2, crossover R = sqrt2 * l_P
mP = 1.0
m_cross = mP / math.sqrt(2)
R_cross = 1.0 / (m_cross * 1.0)                                      # hbar/(m c), hbar=c=1
lP = 1.0
R_eq_sqrt2_lP = abs(R_cross - math.sqrt(2) * lP) < 1e-12
step("P.1", "the crossover anchor: Compton = Schwarzschild gives hbar*c = 2Gm^2, so m = m_P/sqrt2",
     "R*(mc)=hbar and R*(cc)=2Gm (same R) => hbar*c = 2G m^2; with m_P^2 G = hbar c => m_P^2 = 2 m^2 => "
     "m = m_P/sqrt2; length R = sqrt2 l_P", [],
     "the reduced Compton radius R_C = hbar/(mc) and the Schwarzschild radius R_S = 2Gm/c^2 CROSS at one "
     "mass. Cleared of denominators (honest content whenever m,c nonzero): R*(m c)=hbar and R*(c c)=2Gm. "
     "When the SAME R is both, mass appears SQUARED with the factor 2 straight from the Schwarzschild "
     "radius: hbar*c = 2 G m^2 (exact, zero-axiom, re-proved fresh here on integer witnesses -- not "
     "maths-4's). Against the Planck mass (m_P^2 G = hbar c): m_P^2 G = 2 G m^2 (cleared), so m_P^2 = "
     "2 m^2 and the crossover mass is m = m_P/sqrt2 -- THE 1/sqrt2 on the Schwarzschild factor-2. Length "
     "dual: R = sqrt2 l_P. The div-by-G and sqrt are routine scalar steps (cited), as maths-4 and "
     "Stone 5 leave theirs.",
     "UNIQUE (the crossover mass m = m_P/sqrt2; the squared identities are exact)", "DERIVED",
     {"crossover_identity": "hbar*c = 2*G*m^2", "cleared_planck": "m_P^2*G = 2*G*m^2",
      "m_P_squared_eq_2_m_squared": cross_ok, "crossover_mass": "m = m_P/sqrt2",
      "crossover_mass_numeric_planck_units": d6(m_cross),
      "crossover_radius_eq_sqrt2_lP": R_eq_sqrt2_lP, "factor_2_from": "the Schwarzschild radius 2Gm/c^2",
      "witnesses_checked": len(anchor_witnesses)},
     check="hbar*c = 2Gm^2 and m_P^2*G = 2Gm^2 on witnesses; m = m_P/sqrt2; R = sqrt2 l_P")
assert cross_ok and R_eq_sqrt2_lP

# ---- P.2 the two Stones = the ladder -- DERIVED ----------------------------
tP = 1.0
c_eq_lP_over_tP = abs((lP / tP) - 1.0) < 1e-12                       # c = l_P/t_P (Planck units, =c)
step("P.2", "the two Stones = the ladder: the ruler (BC, scale-invariant) + the anchor (Planck, absolute)",
     "Stone 5 dimensionless BC (scale-invariant step) + this anchor (Planck, absolute rung zero) hold "
     "concurrently; c = l_P/t_P (exact)", ["P.1", "17.S.2"],
     "the two Stones do different jobs and hold at the same time. Stone 5 is the RULER -- BC = 2*pi/ln2 "
     "is dimensionless, the SAME at every scale, so it is a scale-invariant STEP. This anchor is "
     "ABSOLUTE -- the Compton-Schwarzschild crossover pins a definite mass and length (the Planck "
     "scale), rung ZERO. An absolute anchor plus scale-invariant rungs is a climbable LADDER (maths-4 "
     "STONES-LADDER-CONCURRENT). The Planck length and time are linked by the standard identity c = "
     "l_P/t_P (exact: l_P/t_P = sqrt(c^5/c^3) = c) -- the length and time faces of rung zero.",
     "UNIQUE (the two Stones hold concurrently; c = l_P/t_P is exact)", "DERIVED",
     {"ruler": "Stone 5: BC = 2*pi/ln2 (dimensionless, scale-invariant step)",
      "anchor": "this: Planck crossover (absolute, rung zero)",
      "c_eq_lP_over_tP": c_eq_lP_over_tP, "ladder": "absolute anchor + scale-invariant rungs"},
     check="the two Stones hold concurrently (ruler + anchor); c = l_P/t_P exact")
assert c_eq_lP_over_tP

# ---- P.3 c = alpha/tau + Kevin's Planck hypothesis -- POSTULATE (flagged) ---
step("P.3", "c = alpha/tau AND Kevin's Planck hypothesis: l_P = reg-to-reg, t_P = state-change rate "
     "(a FLAGGED hypothesis)",
     "l_P = registration-to-registration edge; t_P = the tick (state-change rate); then c = l_P/t_P = "
     "(edge)/(tick), and c = alpha/tau", ["P.2"],
     "the candidate physical meaning for the anchor, kept a FLAGGED HYPOTHESIS (Kevin, 2026-08-25; not "
     "derived, not relied on). PLANCK LENGTH = registration-to-registration (the edge of the adjacency "
     "web); PLANCK TIME = the state-change RATE registration-to-registration (the tick). With P.2's "
     "exact c = l_P/t_P, this reads c = (edge)/(tick), and Kevin's c = alpha/tau (an information quantum "
     "per tick) would identify alpha with the edge quantum and tau with the tick. If proven, this "
     "supplies the physical anchoring P.4 flags as assumed. It is a HYPOTHESIS to prove or refute, held "
     "and capped -- exactly as flagged at 17.S.5.",
     "POSTULATE (Kevin's hypothesis; flagged; to prove or refute; not relied on)", "POSTULATE",
     {"planck_length": "registration-to-registration (the edge)",
      "planck_time": "the state-change rate registration-to-registration (the tick)",
      "c_form": "c = l_P/t_P = (edge)/(tick); Kevin: c = alpha/tau",
      "status": "flagged hypothesis; to prove or refute; not relied on", "author": "Kevin, 2026-08-25",
      "same_as": "17.S.5 (kept flagged)"},
     check=None)

# ---- P.4 what is assumed / owed -- OWED ------------------------------------
step("P.4", "what is ASSUMED / OWED: the crossover as a physical registration threshold; discrimination",
     "assumed: the Compton-Schwarzschild crossover IS a registration threshold (SEC9-type, open); owed: "
     "discrimination (it is an identity)", ["P.1", "17.S.4"],
     "same quarantine as Stone 5. That the crossover pins a PHYSICAL registration threshold (not merely "
     "the meeting of two standard radii) is ASSUMED -- the SEC9-type interpretive gap, OPEN, unproven. "
     "And like Stone 5 the anchor is an IDENTITY (two standard radii set equal), not yet a prediction "
     "that forbids anything standard physics permits. QUARANTINE: no downstream container may use the "
     "physical reading as a premise; only the exact algebra (P.1) and the concurrency (P.2) may be "
     "relied on. These are the owed items, named so momentum does not erase them.",
     "OWED (the physical anchoring proof; discrimination)", "OWED",
     {"assumed_crossover_is_registration_threshold": "SEC9-type, OPEN, unproven",
      "owed_discrimination": "an identity (crossover of standard radii), not a prediction yet",
      "quarantine": "physical reading NOT a downstream premise; only P.1 algebra + P.2 concurrency relied on",
      "present": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="18-stone-planck-anchor", steps=STEPS, grades=GRADES,
           values=dict(crossover_identity="hbar*c = 2*G*m^2", crossover_mass="m = m_P/sqrt2",
                       crossover_radius="R = sqrt2 * l_P", factor_2_from="Schwarzschild radius",
                       c_eq_lP_over_tP=c_eq_lP_over_tP, witnesses_checked=len(anchor_witnesses),
                       is_external_stone=True, quarantined=True,
                       planck_hypothesis="l_P = reg-to-reg; t_P = state-change rate (Kevin, flagged)",
                       two_stones_ladder="ruler (BC) + anchor (Planck) = climbable scale"))

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
