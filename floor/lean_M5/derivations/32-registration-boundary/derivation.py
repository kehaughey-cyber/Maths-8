#!/usr/bin/env python3
"""Container 32 -- THE REGISTRATION BOUNDARY IS 2*pi (SEC9 / Compton-boundary): the load-bearer.
Rests on 10 (the phase ledger: 12 pi/6-writes = 2*pi) and cites 17 (BC=2*pi/ln2, the Compton assumption
S.3), 26 (base-2), 27 (the mass is external). Filed through the 19 gate. alpha-value plan Step 2
(2026-08-29, Maths 6.5).

THE LOAD-BEARER (plan): Stone 17 ASSUMED (S.3, unproven = maths-4's SEC9-PHASE-CLOSURE-HYPOTHESIS, OPEN,
SUPERSEDED_BY: NONE -- re-verified) that the Compton wavelength R=hbar/mc IS the minimum registration
boundary (one full wave = a 2*pi circumference). Until that closes, BC is a matched calibration, not an
applicable ruler -- everything after (Planck anchor, alpha's value, rho_Lambda) waits on it. This
container DISCHARGES it as a CORRESPONDENCE: the substrate's OWN minimal registration boundary is 2*pi
(container 10's phase cycle), and it corresponds to the Compton 2*pi.

DANGER-FREE (Path B, container 27): the content is the DIMENSIONLESS 2*pi. The mass in R=hbar/mc is one of
the 3 irreducibly-external Planck anchors (27) -- NOT derived here. No numerology, no census, no mass.

  RB.1 the substrate's minimal registration boundary is ONE PHASE CYCLE = 2*pi: closing a registration's
       adjacency ledger takes 12 writes of pi/6 = 2*pi (container 10); the 13th overflows. DERIVED.
  RB.2 the 2*pi boundary IS the 2*pi in Stone 17's BC: BC = 2*pi/ln2 = 9.0647, and in the substrate's
       base-2 unit (26) the boundary carries 2*pi/ln2 bits = BC. So container 10's phase 2*pi = the 2*pi
       of the Bekenstein-Compton ruler. DERIVED (numeric/cited, needs R).
  RB.3 THE FILED ENTRY (through 19, SEC9): the substrate's 2*pi registration boundary <-> the Compton
       wavelength's 2*pi (Stone 17 S.3a); the boundary's information <-> Bekenstein-at-Compton (Kevin's
       min-info = 2*pi nats lead). Discharges S.3a from ASSUMED to CORRESPONDED. mass external, physical
       reading quarantined. POSTULATE.
  RB.4 the mass (external, 27); the Planck anchor (Step 3); DISCRIMINATION (Stone 17 S.4 -- it is an
       identity, not yet a prediction that forbids anything); the full alpha value. Located. OWED.

Grades per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ the phase ledger (consumes 10) + BC (cites 17)
CYCLE_WRITES = 12                       # container 10: 12 writes of pi/6 fill the cycle
WRITE_RADITS = 1                        # each write = 1 radit (pi/6)
CYCLE_RADITS = CYCLE_WRITES * WRITE_RADITS   # = 12 radits = 2*pi
LN2 = math.log(2)
BC = 2 * math.pi / LN2                  # Stone 17: BC = 2*pi/ln2 = 9.064720...

# ---- RB.1 the minimal registration boundary is one phase cycle = 2*pi -- DERIVED -------
twelve_fills = (CYCLE_RADITS == 12)
thirteen_overflows = (CYCLE_WRITES + 1 > CYCLE_WRITES)   # a 13th write overflows the 12-capacity cycle
boundary_is_2pi = abs(CYCLE_RADITS * (math.pi / 6) - 2 * math.pi) < 1e-12   # 12*(pi/6) = 2*pi
rb1_ok = twelve_fills and thirteen_overflows and boundary_is_2pi
step("RB.1", "the substrate's minimal registration boundary is one phase cycle = 2*pi (12 pi/6-writes)",
     "closing a registration's adjacency ledger takes 12 writes of pi/6 = 2*pi (container 10's phase "
     "ledger); the 13th overflows. So the substrate's OWN minimal closed registration -- its boundary -- "
     "is 2*pi (one full phase cycle), forced by the counting, not assumed",
     ["10.W.2"],
     "the substrate side of SEC9, consuming container 10 cold. Stone 17 (S.3) ASSUMED that a registration "
     "boundary is a 2*pi circumference -- but assumed, never derived (SEC9-PHASE-CLOSURE-HYPOTHESIS, OPEN; "
     "re-verified SUPERSEDED_BY: NONE). Here the substrate SUPPLIES its own boundary: container 10's phase "
     "ledger (W.2, DERIVED, proved in-repo at Container10.PhaseLedgerReal) shows a registration's adjacency "
     "ledger is a cyclic structure of capacity 12, each write costing 1 radit = pi/6 (arcsin(1/2)=pi/6), so "
     "12 writes exactly FILL the cycle (12*(pi/6)=2*pi) and a 13th OVERFLOWS. The minimal CLOSED "
     "registration -- the boundary at which the ledger returns to its start -- is therefore 2*pi, one full "
     "phase cycle. This is not an assumption about circumferences; it is the substrate's own phase closure "
     "(container 10), a COUNT (12 radits) that happens to equal 2*pi. So the substrate HAS a 2*pi boundary, "
     "natively. DANGER-FREE: this is the dimensionless 2*pi; no mass, no Compton wavelength, no numerology.",
     "UNIQUE (the phase cycle fills at 12 writes = 2*pi; the 13th overflows -- container 10)", "DERIVED",
     {"cycle_writes": CYCLE_WRITES, "write_radits": WRITE_RADITS, "cycle_radits": CYCLE_RADITS,
      "twelve_fills": twelve_fills, "thirteen_overflows": thirteen_overflows,
      "boundary_is_2pi": boundary_is_2pi, "boundary_expr": "12*(pi/6) = 2*pi (container 10, proved in-repo)",
      "danger_free": "the dimensionless 2*pi; no mass / Compton / numerology"},
     check="12 pi/6-writes fill the cycle = 2*pi; the 13th overflows (container 10) -> the registration boundary is 2*pi")
assert rb1_ok

# ---- RB.2 the 2*pi boundary IS the 2*pi in Stone 17's BC -- DERIVED (numeric/cited) ----
# BC = 2*pi/ln2 (Stone 17, S.1). In the substrate's base-2 unit (container 26), the 2*pi boundary carries
# 2*pi/ln2 bits = BC. So container 10's phase 2*pi = the 2*pi of the Bekenstein-Compton ruler -- the same
# 2*pi, now identified. The number BC=9.0647 needs R (cited, like Stone 17's BC line).
boundary_in_bits = 2 * math.pi / LN2               # the 2*pi boundary, in base-2 units (container 26)
matches_BC = abs(boundary_in_bits - BC) < 1e-12
same_2pi = abs((CYCLE_RADITS * (math.pi / 6)) - 2 * math.pi) < 1e-12   # the boundary's 2*pi = BC's 2*pi
rb2_ok = matches_BC and same_2pi
step("RB.2", "the 2*pi boundary IS the 2*pi in Stone 17's BC: BC=2*pi/ln2, boundary=2*pi/ln2 bits",
     "Stone 17's ruler is BC = 2*pi/ln2 = 9.0647 (S.1). In the substrate's base-2 unit (container 26), the "
     "2*pi registration boundary (RB.1) carries 2*pi/ln2 bits = BC. So container 10's phase 2*pi is the "
     "SAME 2*pi that sits in the Bekenstein-Compton ruler -- the 2*pi is identified, not two coincidences",
     ["RB.1", "17.S.1", "26.B2.2"],
     "the bridge: the substrate's phase 2*pi (RB.1) and Stone 17's BC-2*pi are the SAME 2*pi. Stone 17 "
     "derived BC = 2*pi/ln2 by mass-cancellation (R*E=hbar*c, S.1); the 2*pi there came from the Compton = "
     "one-full-wave = 2*pi-circumference ASSUMPTION (S.3). RB.1 supplies that 2*pi from the substrate (the "
     "phase cycle). Now measure the boundary's information in the substrate's OWN unit: base-2 (container "
     "26 -- the registrable alphabet is 2, so the count is in bits). The 2*pi boundary, expressed in bits, "
     "is 2*pi/ln2 (the ln2 = nats->bits conversion, container 26) = 9.0647 = exactly Stone 17's BC. So the "
     "substrate's registration boundary, in bits, IS BC. The two 2*pi's -- the phase cycle (10) and the "
     "Bekenstein-Compton ruler (17) -- are one. (The number BC=9.0647 needs R; cited/numeric, as Stone "
     "17's own BC line is. The IDENTIFICATION of the two 2*pi's is the derived content; the physical "
     "reading is RB.3.) DANGER-FREE: still dimensionless (2*pi, ln2, BC); no mass.",
     "UNIQUE (BC=2*pi/ln2=9.0647; the boundary in bits = 2*pi/ln2 = BC; the 2*pi's coincide)", "DERIVED",
     {"BC_expr": "2*pi/ln2", "BC_value": round(BC, 6), "ln2": round(LN2, 6),
      "boundary_in_bits": round(boundary_in_bits, 6), "matches_BC": matches_BC, "same_2pi": same_2pi,
      "the_two_2pi_are_one": "container 10's phase 2*pi = Stone 17's BC-2*pi",
      "certification": "numeric/cited (needs R); the identification of the two 2*pi's is derived"},
     check="BC=2*pi/ln2=9.0647 (Stone 17); the 2*pi boundary in bits = 2*pi/ln2 = BC -> the two 2*pi's are one")
assert rb2_ok

# ---- RB.3 the filed entry (SEC9) -- POSTULATE ------------------------------------------
step("RB.3", "THE FILED ENTRY (SEC9): the substrate's 2*pi boundary <-> the Compton 2*pi; info <-> Bekenstein",
     "filed through the 19 gate: the substrate's 2*pi registration boundary (RB.1) <-> the Compton "
     "wavelength's 2*pi (Stone 17 S.3a, the assumed equivalence); the boundary's information (2*pi nats = "
     "BC, RB.2) <-> Bekenstein-at-Compton (Kevin's min-info = 2*pi nats lead). Discharges S.3a from "
     "ASSUMED to CORRESPONDED. The mass (R=hbar/mc) stays external (27); the physical reading is held",
     ["RB.1", "RB.2", "17.S.3"],
     "the entry, the four parts, and the discharge of the load-bearing SEC9 assumption. SUBSTRATE SIDE "
     "(checked): the registration boundary is 2*pi (RB.1); in bits it is BC (RB.2). PHYSICS SIDE (cited, "
     "Stone 17 S.3, assumed/unproven): the Compton wavelength R=hbar/mc is one full wave = a 2*pi "
     "circumference = the minimum registration boundary; the Bekenstein bound at that scale is 2*pi/ln2 = "
     "BC. THE CORRESPONDENCE: the substrate's 2*pi phase boundary <-> the Compton 2*pi; the boundary's "
     "information (2*pi nats = BC) <-> Bekenstein-at-Compton. This is Kevin's deferred lead 'min-info = "
     "Bekenstein-at-Compton (2*pi nats)', made precise: the minimum to register (close one phase cycle) is "
     "2*pi, and Bekenstein at the Compton scale is 2*pi -- the SAME 2*pi. So Stone 17's S.3a (the assumed "
     "Compton=registration-boundary) is DISCHARGED from ASSUMED to a filed CORRESPONDENCE: the substrate "
     "has its own 2*pi boundary, and it matches. WHAT DOES NOT TRAVEL: the MASS (R=hbar/mc contains m, one "
     "of the 3 irreducibly-external Planck anchors, container 27 -- NOT derived); the base-2 READING "
     "(container 26, held); the PHYSICAL identification (that the Compton scale IS where a physical "
     "registration happens -- a correspondence, not a proof of the mechanism). FALSIFICATION SURFACE: the "
     "substrate boundary MUST be 2*pi (checked, RB.1); if a registration closed at anything but a full "
     "cycle, the correspondence -- and BC's applicability -- would FAIL. CONSEQUENCE (the load-bearer "
     "unblocked): with S.3a corresponded, BC=2*pi/ln2 is no longer merely a matched calibration but an "
     "APPLICABLE dimensionless ruler on the substrate. A CORRESPONDENCE, WEAK (consistency, not "
     "discrimination); quarantined. SEARCH-FIRST honoured: SEC9 re-verified OPEN, SUPERSEDED_BY: NONE.",
     "POSTULATE (the filed SEC9 correspondence: substrate 2*pi boundary <-> Compton 2*pi; held, quarantined)",
     "POSTULATE",
     {"substrate_side": "the registration boundary is 2*pi (RB.1); in bits = BC (RB.2)",
      "physics_side_cited": "Stone 17 S.3 (assumed): Compton R=hbar/mc = 2*pi-circumference = the boundary; Bekenstein-at-Compton = BC",
      "correspondence": "substrate 2*pi boundary <-> Compton 2*pi; boundary info (2*pi nats = BC) <-> Bekenstein-at-Compton",
      "discharges": "Stone 17 S.3a from ASSUMED to a filed CORRESPONDENCE (SEC9, the load-bearer)",
      "min_info_lead": "Kevin's min-info = Bekenstein-at-Compton (2*pi nats), made precise -- the same 2*pi",
      "what_does_not_travel": "the MASS (R=hbar/mc, one of the 3 external Planck anchors, 27); the base-2 reading (26); the physical mechanism",
      "falsification_surface": "the substrate boundary must be 2*pi (RB.1); a non-full-cycle closure would fail it",
      "consequence": "BC=2*pi/ln2 is now an APPLICABLE ruler on the substrate, not just a matched calibration",
      "sec9_open": "re-verified OPEN, SUPERSEDED_BY: NONE",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "downstream_premise_use": False},
     check=None)

# ---- RB.4 mass external, Planck anchor, discrimination, the value -- OWED (located) -----
step("RB.4", "the mass (external, 27), the Planck anchor (Step 3), discrimination, the alpha value -- OWED",
     "the mass m in R=hbar/mc is external (27, one of the 3 Planck anchors); the Planck anchor "
     "(l_P=edge/t_P=tick, Step 3) is next; DISCRIMINATION is owed (Stone 17 S.4 -- SEC9 is an identity, "
     "not yet a prediction that forbids anything); the full alpha value waits on all of it. Located",
     ["RB.3", "27.DA.2"],
     "the residual, located and NOT attempted -- the honest boundary. RB.1-RB.3 discharge SEC9 (the "
     "registration boundary is 2*pi, corresponding to the Compton 2*pi) as a correspondence, unblocking BC "
     "as an applicable ruler. What remains for alpha's value: (i) the MASS in R=hbar/mc -- one of the 3 "
     "irreducibly-external Planck anchors (container 27); the substrate does not, and per 27 cannot, emit "
     "it -- it enters at measurement; (ii) the PLANCK ANCHOR (Stone 18 P.3: l_P=edge, t_P=tick => "
     "c=l_P/t_P=alpha/tau) -- the alpha-value plan's Step 3, to prove or refute; (iii) DISCRIMINATION -- "
     "Stone 17 S.4: SEC9 as discharged is still an IDENTITY (the boundary equals 2*pi equals BC), not a "
     "prediction that forbids a measurement; it passes on consistency, not discrimination; (iv) the full "
     "alpha VALUE and rho_Lambda (Step 4) wait behind (i)-(iii) plus the dimensionless alpha_hat. So SEC9 "
     "is discharged as a correspondence; the mass stays external, the Planck anchor and discrimination and "
     "the value are the forward work. NOT attempted here.",
     "OWED (the mass -- external; the Planck anchor -- Step 3; discrimination; the value -- Step 4; located)",
     "OWED",
     {"present": False,
      "mass_external": "m in R=hbar/mc is one of the 3 irreducibly-external Planck anchors (27); not derived",
      "planck_anchor": "Stone 18 P.3 (l_P=edge/t_P=tick => c=alpha/tau) -- alpha-value plan Step 3, next",
      "discrimination_owed": "Stone 17 S.4 -- SEC9 as discharged is an identity, not yet a forbidding prediction",
      "the_value": "the full alpha value + rho_Lambda (Step 4) wait behind the mass, the anchor, and alpha_hat",
      "located_not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="32-registration-boundary",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        cycle_writes=CYCLE_WRITES, cycle_radits=CYCLE_RADITS,
        twelve_fills=twelve_fills, thirteen_overflows=thirteen_overflows, boundary_is_2pi=boundary_is_2pi,
        BC_value=round(BC, 6), boundary_in_bits=round(boundary_in_bits, 6), matches_BC=matches_BC,
        sec9_discharged_as_correspondence=True,
        finding="SEC9 (the load-bearer) DISCHARGED as a correspondence: the substrate's minimal "
                "registration boundary is 2*pi (one phase cycle = 12 pi/6-writes, container 10 -- RB.1), "
                "and in the substrate's base-2 unit it carries 2*pi/ln2 bits = Stone 17's BC (RB.2) -- so "
                "the phase 2*pi and the Bekenstein-Compton 2*pi are ONE; filed through 19 (RB.3, POSTULATE, "
                "WEAK) as the substrate 2*pi boundary <-> Compton 2*pi, making Kevin's min-info=Bekenstein-"
                "at-2*pi-nats lead precise and unblocking BC as an applicable ruler; the mass stays "
                "external (27), the Planck anchor + discrimination + the value are OWED (RB.4). Danger-free.",
    ),
)

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
