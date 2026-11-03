#!/usr/bin/env python3
"""Container 35 -- FORCING alpha_hat: the last unknown MEETS the cosmological constant problem -- a
CANCELLATION problem, mechanism REOPENED (not closed as external).
Rests on 33 (the Planck hypothesis -> the naive alpha_hat), 34 (the flagship / the falsification surface),
27 (alpha_hat is the one dimensionless factor); cites the measured cosmological constant (external).
Filed through the 19 gate. alpha-value plan, the force-alpha_hat step (2026-08-29, Maths 6.5;
AH.3/AH.4 CORRECTED 2026-09-03, Maths 6.6 -- see the correction note below).

THE ATTEMPT (Kevin's instruction): FORCE alpha_hat -- the single dimensionless factor the whole arc
converges to (container 34: rho_Lambda = alpha_hat x anchor x count, alpha_hat the one unknown). Forced,
NEVER fitted (refused-list: NO 1/phi^3, NO standing-lag); the mass/census DANGER ZONE stays OUT.

THE OUTCOME (graded below): the one natural, non-fitted forcing gives alpha_hat = 1 -- and it is REFUTED
by the cosmological constant, by ~122 orders of magnitude (AH.1/AH.2, DERIVED, stand). So forcing
alpha_hat MEETS the COSMOLOGICAL CONSTANT PROBLEM.

  *** CORRECTION (2026-09-03, Maths 6.6): AH.3/AH.4 previously OVER-CONCLUDED "alpha_hat is irreducibly
  external, the arc ends" -- the DISMISSAL-BIAS (Kevin caught it, third time; see
  external-input-consideration). alpha_hat=1 being refuted kills ONE SWAG (one archon = one BARE Planck
  unit); it says NOTHING about whether alpha_hat is ATTAINABLE. The honest reading of the "worst
  prediction in physics" parallel: (1) it is a POINT OF CONTACT, not a failure -- the framework and QFT
  give the SAME naive Planck-density answer for the SAME reason (one Planck-quantum per Planck-cell: QFT
  one zero-point mode per cell, the framework one archon per cell), so the archon density IS the QFT
  vacuum-mode density -- the framework is correctly WIRED IN, not wrong in a novel way; (2) the cc problem
  is a CANCELLATION problem -- the measured 10^-122 is a near-perfect-cancellation RESIDUAL, not a new
  number to derive, and QFT's scandal is that it has NO cancellation mechanism; (3) the FRAMEWORK HAS
  candidate cancellation STRUCTURE QFT's flat vacuum LACKS -- the SIGNED deficit (14.B.2), the deg-6
  MIRROR / zero-crossing (14.B.2, 15.C.2), the separately-conserved signed ball-deficit totals (14.B.5),
  and the frustration that never closes (16.D.1, epsilon ~ 7.356deg, the "slack"). So alpha_hat ~10^-122
  reads as a RESIDUAL after near-cancellation the substrate MAY force -- the F2 / signed-cancellation /
  TRANSFER-RULE lead (10^-122 ~ (l_P/L_horizon)^2 = the cancellation running Planck->cosmological), the
  plan's own lead, REOPENED. NOT "irreducibly external." (Honest obstacles, named so the reading is
  testable not fished -- see AH.3/AH.4: this substrate realizes only D>=0, so a two-sided crossing needs
  the negative-curvature geometry 15 defers; epsilon is the DYNAMO, explicitly NOT the vacuum (16.D.3),
  so a residual reading must respect that typing; and (l_P/L_horizon)^2 still carries the external horizon,
  so a residual would be substrate-cancellation-structure x boundary, not purely forced.) ***

  AH.1 the naive forced value: GIVEN the Planck hypothesis (33, one archon = one Planck-scale
       registration), the per-archon quantum is one Planck unit -- alpha_hat = 1. Forced, not fitted. DERIVED.
  AH.2 alpha_hat = 1 is REFUTED (the checked-negative): it predicts rho_Lambda ~ the Planck density
       (rho_Lambda/rho_Planck ~ alpha_hat = 1, order 0); the measured cosmological constant is ~10^-122 of
       the Planck density, so the naive forcing overshoots by ~122 orders -- the cosmological constant
       problem. The falsification surface (34) fires. DERIVED (the prediction; the measured order cited).
  AH.3 the reading (CORRECTED): the "worst prediction" parallel is a POINT OF CONTACT (same naive answer,
       same reason); the cc problem is a CANCELLATION problem; alpha_hat=1 is the UN-CANCELLED sum and
       alpha_hat ~10^-122 is the near-cancellation RESIDUAL. The framework carries candidate cancellation
       structure QFT lacks (signed deficit 14, deg-6 mirror 14/15, conserved signed totals 14.B.5,
       frustration epsilon 16). Held, quarantined. POSTULATE.
  AH.4 the honest end (CORRECTED): alpha_hat is NOT shown irreducibly external -- one refuted SWAG does
       not close its reachability. What is OWED is the cancellation/frustration/TRANSFER-RULE MECHANISM
       (the F2 lead) as the candidate route to alpha_hat -- computing the MECHANISM's structure, NEVER
       fishing for 10^-122. Refused routes (1/phi^3, standing-lag) STAY refused; the census DANGER ZONE
       stays OUT. OWED, REOPENED.

DANGER-FREE and FIT-FREE by construction: no value is fitted; the only number cited (~10^-122) is the
MEASURED cosmological constant, used to FALSIFY the naive forcing, never to fit. Grades per step.
`--check` recomputes the DERIVED steps.
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


# ================================================================ the naive forcing + the refutation
ALPHA_HAT_NAIVE = 1                 # GIVEN the Planck hypothesis (33): per-archon quantum = one Planck unit
PREDICTED_ORDER = 0                 # alpha_hat=1 => rho_Lambda/rho_Planck ~ 1 => log10 ~ 0
MEASURED_ORDER = -122              # CITED external: rho_Lambda ~ 10^-122 rho_Planck (the cosmological constant)
ORDER_GAP = PREDICTED_ORDER - MEASURED_ORDER      # = 122 orders of magnitude

# ---- AH.1 the naive forced value alpha_hat = 1 -- DERIVED -------------------------------
naive_is_one = (ALPHA_HAT_NAIVE == 1)
step("AH.1", "the naive forced value: GIVEN the Planck hypothesis (33), alpha_hat = 1 (per-archon = one Planck unit)",
     "the one natural, non-fitted forcing: GIVEN Kevin's Planck hypothesis (container 33 -- one archon = "
     "one Planck-scale registration, edge=l_P, tick=t_P), the per-archon quantum is exactly one Planck "
     "unit, so alpha_hat = alpha / (Planck quantum) = 1. Forced by the identification, NOT fitted to a target",
     ["27.DA.3"],   # the Planck hypothesis (33.PA.3) is the CONDITION, cited in prose -- not a premise:
     "the honest attempt to force alpha_hat. Container 34 showed the whole arc converges to one "
     "dimensionless unknown: rho_Lambda = alpha_hat x (Planck anchor) x (min-density count). To FORCE "
     "alpha_hat WITHOUT fitting, take the one structural route the substrate offers: the Planck hypothesis "
     "(container 33, PA.3). It identifies one archon with one Planck-scale registration (the edge = l_P, "
     "the tick = t_P). Under that identification, the per-archon quantum alpha IS one Planck unit (one "
     "Planck energy in the energy reading; one Planck length in the length reading), so the DIMENSIONLESS "
     "factor alpha_hat = alpha / (Planck quantum) = 1. This is not fitting -- it falls out of the "
     "identification (there is no free parameter to tune; the archon just IS the Planck registration). So "
     "the substrate's naive forced value is alpha_hat = 1. (It rests on the Planck hypothesis, container "
     "33 -- itself a held correspondence, structurally consistent; so alpha_hat = 1 is the forced value "
     "GIVEN 33.) Whether alpha_hat = 1 SURVIVES is AH.2.",
     "UNIQUE (given the Planck hypothesis, one archon = one Planck unit, so alpha_hat = 1)", "DERIVED",
     {"alpha_hat_naive": ALPHA_HAT_NAIVE, "naive_is_one": naive_is_one,
      "route": "the Planck hypothesis (33): one archon = one Planck-scale registration => per-archon quantum = 1 Planck unit",
      "not_fitted": "alpha_hat = 1 falls out of the identification -- no free parameter, no target",
      "rests_on": "the Planck hypothesis (33), a held correspondence -- so this is the forced value GIVEN 33"},
     check="given the Planck hypothesis (33, one archon = one Planck registration), alpha_hat = 1 (forced, not fitted)")
assert naive_is_one

# ---- AH.2 alpha_hat = 1 is REFUTED by the cosmological constant -- DERIVED (checked-negative)
predicted_ratio_order = PREDICTED_ORDER      # alpha_hat=1 -> rho_Lambda ~ Planck density -> order 0
gap_is_122 = (ORDER_GAP == 122)
refuted = (ORDER_GAP != 0)                   # predicted (0) != measured (-122): the naive forcing fails
ah2_ok = gap_is_122 and refuted
step("AH.2", "alpha_hat = 1 is REFUTED: it predicts the Planck density; the measured Lambda is ~10^-122 of it",
     "the falsification surface (34) fires: alpha_hat = 1 predicts rho_Lambda ~ the Planck density "
     "(rho_Lambda/rho_Planck ~ alpha_hat = 1, log10 order 0); the MEASURED cosmological constant is "
     "~10^-122 of the Planck density (order -122). The naive forcing overshoots by ~122 orders of "
     "magnitude -- the cosmological constant problem. alpha_hat = 1 FAILS",
     ["AH.1", "34.VV.2"],   # rests on the DERIVED assembly (34.VV.2); the falsification surface (34.VV.3) is cited in prose
     "the checked-negative -- the naive forcing is refuted, and HOW it fails is the finding. Container 34 "
     "named the falsification surface: rho_Lambda is COMPUTED from alpha_hat x rho_vac and COMPARED to the "
     "measured cosmological constant, never fitted. RUN IT with the naive alpha_hat = 1 (AH.1) and the "
     "local min-density count (O(1), container 15/34): rho_Lambda ~ 1 x (Planck density) x (O(1)) ~ the "
     "PLANCK DENSITY, so rho_Lambda/rho_Planck ~ 1 (log10 order 0). The MEASURED cosmological constant "
     "(CITED external physics) is rho_Lambda ~ 10^-122 rho_Planck (order -122). So the naive prediction "
     "overshoots the measurement by ~122 orders of magnitude -- 0 - (-122) = 122. alpha_hat = 1 is "
     "REFUTED, decisively. NOTE this is exactly the COSMOLOGICAL CONSTANT PROBLEM (the vacuum energy = the "
     "Planck density is the standard 'worst prediction in physics', ~120 orders too big): the framework's "
     "naive prediction reproduces the SAME wall all of physics hits -- not a novel error, but the deepest "
     "open problem, arrived at honestly. (The prediction order 0 is DERIVED from alpha_hat=1; the measured "
     "order -122 is CITED, the measured cosmological constant -- used to FALSIFY, never to fit.) The "
     "refutation is disciplined: I refuse to rescue alpha_hat=1 by tuning, and refuse the old routes that "
     "faked the 10^-122 (1/phi^3, standing-lag -- the refused-list).",
     "UNIQUE (alpha_hat=1 predicts order 0; measured order -122; gap 122 != 0 -> refuted)", "DERIVED",
     {"predicted_order": predicted_ratio_order, "measured_order_cited": MEASURED_ORDER,
      "order_gap": ORDER_GAP, "gap_is_122": gap_is_122, "alpha_hat_one_refuted": refuted,
      "is_cosmological_constant_problem": "the naive vacuum energy = the Planck density = the standard 'worst prediction', ~122 orders too big",
      "measured_cited": "rho_Lambda ~ 10^-122 rho_Planck -- the measured cosmological constant (external), used to FALSIFY not fit",
      "refused": "NO tuning of alpha_hat=1; NO 1/phi^3, NO standing-lag (the old fake-derivations of 10^-122)"},
     check="alpha_hat=1 predicts rho_Lambda ~ Planck density (order 0); measured ~10^-122 (order -122); gap 122 -> REFUTED")
assert ah2_ok

# ---- AH.3 the parallel is CONTACT; the cc problem is a CANCELLATION problem -- POSTULATE (the reading)
step("AH.3", "the reading: the 'worst prediction' parallel is CONTACT; the cc problem is a CANCELLATION problem; alpha_hat ~10^-122 is the RESIDUAL",
     "the naive alpha_hat=1 (AH.1) is the UN-CANCELLED sum, and the 'worst prediction in physics' parallel "
     "(AH.2) is a POINT OF CONTACT, not a failure: the framework and QFT give the SAME naive Planck-density "
     "answer for the SAME reason (one Planck-quantum per Planck-cell). The cc problem is a CANCELLATION "
     "problem -- the measured ~10^-122 is a near-cancellation RESIDUAL, not a new number -- and the "
     "framework carries candidate cancellation STRUCTURE QFT's flat vacuum LACKS: the SIGNED deficit (14), "
     "the deg-6 MIRROR (14/15), the conserved signed totals (14.B.5), the frustration epsilon (16). So "
     "alpha_hat ~10^-122 reads as a RESIDUAL the substrate MAY force -- NOT irreducibly external. Held",
     ["AH.2", "34.VV.4", "27.DA.2"],
     "the CORRECTED reading (2026-09-03) -- replacing the over-concluded 'alpha_hat is the external "
     "cosmological scale'. AH.1/AH.2 stand: the naive forcing alpha_hat=1 predicts the Planck density and "
     "is refuted by ~122 orders. The DISMISSAL-BIAS was to read that one refuted SWAG as 'alpha_hat "
     "irreducibly external, arc ends'. What the 'worst prediction in physics' parallel ACTUALLY tells us: "
     "(1) CONTACT, not failure -- the framework and QFT give the SAME naive Planck-density answer for the "
     "SAME reason: one Planck-scale quantum per Planck-scale cell (QFT counts one zero-point energy per "
     "vacuum mode; the framework counts one archon per cell), so the archon density IS the QFT vacuum-mode "
     "density. Reproducing the standard result means the framework is correctly WIRED IN, not wrong in a "
     "novel way. (2) The cc problem is a CANCELLATION problem: the measured 10^-122 is not a different "
     "number to derive -- it is a near-PERFECT cancellation, the vacuum energy almost completely cancelling "
     "and leaving a tiny residual. QFT's scandal is not that it computes the Planck density -- it is that "
     "QFT has NO mechanism to cancel it. So the naive Planck-density answer is the UN-CANCELLED sum; the "
     "real rho_Lambda is the RESIDUAL. (3) The FRAMEWORK HAS the cancellation structure QFT LACKS -- three "
     "features, all already built, that a flat vacuum does not have: the SIGNED deficit (14.B.2, curvature "
     "is +/-, not one sign); the deg-6 MIRROR / zero-crossing D=0 (14.B.2, 15.C.2) the signed density "
     "balances around; the separately-conserved signed ball-deficit TOTALS (14.B.5); and the frustration "
     "epsilon that never closes (16.D.1, ~7.356deg -- the 'slack', maths-4's first unpinned quantity). And "
     "10^-122 ~ (l_P/L_horizon)^2 ~ (t_Planck/t_universe)^2 is the cancellation running ACROSS the scales "
     "Planck->cosmological -- the transfer rule compounding, the cosmological boundary setting how far it "
     "runs. So alpha_hat ~10^-122 reads as a RESIDUAL after near-cancellation that the substrate MAY force "
     "(via the signed-density / frustration / transfer structure) -- the F2 / transfer-rule lead, REOPENED. "
     "HONEST OBSTACLES, named so this is a testable reading and NOT fishing: (i) on THIS substrate the "
     "signed deficit is ONE-SIDED (D>=0 at every vertex, 15.C.2) -- a genuine two-sided zero-crossing "
     "cancellation needs the negative-curvature geometry container 15 defers, so 'signed density crossing "
     "the mirror' is a candidate whose precondition is NOT yet met here; (ii) epsilon is the DYNAMO, "
     "explicitly NOT the vacuum (16.D.3, load-bearing) -- a residual reading must be tested AGAINST that "
     "typing, not by re-conflating epsilon with a vacuum energy; (iii) (l_P/L_horizon)^2 still carries the "
     "EXTERNAL horizon, so a residual would be substrate-cancellation-structure x boundary, not PURELY "
     "substrate-forced -- AH.3's old 'external boundary' content is not wholly wrong; what was wrong was "
     "calling alpha_hat IRREDUCIBLY external and CLOSING the door. WHAT DOES NOT TRAVEL: any value of "
     "alpha_hat; the mechanism itself (owed, AH.4); the refused routes. FALSIFICATION: if the cancellation "
     "structure demonstrably CANNOT produce a small residual without fitting, the reading weakens back "
     "toward 'external'; but that is to be SHOWN by working the mechanism, not assumed. A CORRESPONDENCE / "
     "reading; held, quarantined.",
     "POSTULATE (the parallel = contact; the cc problem = a cancellation problem; alpha_hat ~10^-122 = the near-cancellation residual; held)",
     "POSTULATE",
     {"reading": "the 'worst prediction' parallel is CONTACT (same naive answer, same reason); the cc problem is a CANCELLATION problem; alpha_hat ~10^-122 is the near-cancellation RESIDUAL",
      "contact_not_failure": "framework and QFT give the SAME naive Planck-density answer for the SAME reason (one Planck-quantum per Planck-cell) -- the archon density IS the QFT vacuum-mode density",
      "cancellation_problem": "10^-122 is a near-perfect-cancellation residual, not a new number; QFT's scandal is it has NO cancellation mechanism; alpha_hat=1 is the UN-CANCELLED sum",
      "candidate_structure": "signed deficit (14.B.2), deg-6 mirror / zero-crossing (14.B.2, 15.C.2), conserved signed totals (14.B.5), frustration epsilon (16.D.1) -- structure QFT's flat vacuum lacks",
      "transfer_across_scales": "10^-122 ~ (l_P/L_horizon)^2 ~ (t_Planck/t_universe)^2 -- the cancellation running Planck->cosmological, the transfer rule compounding",
      "honest_obstacles": "(i) this substrate is one-sided D>=0 (15.C.2) -- a two-sided crossing needs the negative-curvature geometry 15 defers; (ii) epsilon is the DYNAMO not the vacuum (16.D.3) -- respect the typing; (iii) (l_P/L_horizon)^2 still carries the external horizon -- residual = structure x boundary, not purely forced",
      "corrects_prior_35": "REPLACES the over-concluded 'alpha_hat irreducibly external, arc ends' (the dismissal-bias) -- alpha_hat=1 refuted kills ONE SWAG, not alpha_hat's reachability",
      "not_irreducibly_external": True, "correspondence_not_resolution": True,
      "weak_consistency_not_discrimination": True, "downstream_premise_use": False},
     check=None)

# ---- AH.4 alpha_hat's reachability NOT closed; the cancellation MECHANISM is owed -- OWED, REOPENED
step("AH.4", "the honest end (CORRECTED): alpha_hat is NOT shown irreducibly external -- the cancellation/transfer MECHANISM is the owed route (OWED, REOPENED)",
     "alpha_hat is NOT shown irreducibly external: one refuted SWAG (alpha_hat=1) does not close its "
     "reachability. What is OWED is the cancellation / frustration / TRANSFER-RULE MECHANISM -- the F2 lead "
     "the plan named -- as the candidate route to alpha_hat: compute the MECHANISM's STRUCTURE, NEVER fish "
     "for 10^-122. Refused routes (1/phi^3, standing-lag) STAY refused; the census DANGER ZONE stays OUT. "
     "The residual may be substrate-forced x boundary -- REOPENED, not the end",
     ["AH.3", "22.CV.3"],
     "the CORRECTED honest end (2026-09-03) -- replacing 'alpha_hat is not substrate-forceable, the arc "
     "ends'. The over-conclusion was the DISMISSAL-BIAS: killing the naive alpha_hat=1 SWAG killed a GUESS "
     "(one archon = one BARE Planck unit), NOT alpha_hat's reachability. 'alpha may be irreducibly "
     "external' remains a POSSIBLE outcome, but it is NOT to be reached by dismissing a single refuted "
     "guess -- reaching it that way is exactly the failure Kevin has now caught three times (see "
     "external-input-consideration). The LIVE reading (AH.3) is that alpha_hat ~10^-122 is a near-"
     "cancellation RESIDUAL, and the framework has candidate cancellation structure QFT lacks. So what is "
     "OWED is the MECHANISM: (a) the signed-cancellation structure -- how the SIGNED deficit (14) and the "
     "deg-6 MIRROR (14/15) and the conserved signed totals (14.B.5) combine to a small net; (b) the "
     "frustration epsilon (16) as the persistent 'slack' -- respecting 16.D.3 (epsilon is the DYNAMO, NOT "
     "the vacuum), i.e. tested against that typing, not conflated with it; (c) the TRANSFER RULE -- how a "
     "frustration at one level enters the next, compounding across scales (10^-122 ~ (l_P/L_horizon)^2), "
     "which is maths-4's 'first quantity with slack, the principled place to look' and the plan's named F2 "
     "lead. THE DISCIPLINE, LOUD: compute the mechanism's STRUCTURE, forced-not-fitted; NEVER fish for "
     "10^-122; the refused-list holds (NO 1/phi^3, NO standing-lag -- the old fake-derivations); the "
     "mass/census DANGER ZONE stays OUT. What remains OWED beyond the mechanism: the negative-curvature "
     "geometry (for a genuine two-sided crossing, container 15 defers it); and per container 22 (CV.3), "
     "the warrant (top-down meets bottom-up) before any value is 'equivalence'. If, worked honestly, the "
     "cancellation structure demonstrably cannot yield a small residual without fitting, THEN 'alpha_hat "
     "irreducibly external' would be earned -- but by demonstration, not by dismissal. So the arc does NOT "
     "end here: it reopens onto the cancellation mechanism as the real route to alpha_hat. NOT attempted "
     "further in THIS container (it is the next container's work).",
     "OWED (alpha_hat's reachability NOT closed; the cancellation/transfer mechanism is the owed candidate route; refused routes out, danger zone out)",
     "OWED",
     {"present": False,
      "verdict": "alpha_hat is NOT shown irreducibly external -- one refuted SWAG (alpha_hat=1) does not close its reachability; REOPENED",
      "corrects_prior_35": "REPLACES 'alpha_hat not substrate-forceable, arc ends' (the dismissal-bias, caught 3rd time) -- 'irreducibly external' is a possible outcome but NOT reached by dismissing one guess",
      "owed_mechanism": "the cancellation / frustration / TRANSFER-RULE mechanism (the F2 lead): (a) signed-cancellation (14, 14/15, 14.B.5); (b) epsilon as slack, tested against 16.D.3 (dynamo != vacuum); (c) the transfer rule across scales",
      "discipline": "compute the MECHANISM's structure forced-not-fitted; NEVER fish for 10^-122; refused-list holds (NO 1/phi^3, NO standing-lag); danger zone OUT",
      "not_a_fit": "the naive alpha_hat=1 is refuted not rescued; 10^-122 is the MEASURED value (falsify, never fit)",
      "owed_beyond": "the negative-curvature geometry (two-sided crossing, 15 defers it); the warrant top-down-meets-bottom-up (22.CV.3) before any value is 'equivalence'",
      "external_earned_only_by_demonstration": "if the cancellation structure demonstrably cannot yield a small residual without fitting, THEN 'external' is earned -- by demonstration, not dismissal",
      "reopened_not_ended": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="35-force-alpha-hat",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        alpha_hat_naive=ALPHA_HAT_NAIVE, naive_is_one=naive_is_one,
        predicted_order=PREDICTED_ORDER, measured_order_cited=MEASURED_ORDER, order_gap=ORDER_GAP,
        alpha_hat_one_refuted=refuted,
        alpha_hat_meets_cc_problem=True, alpha_hat_reachability_reopened=True,
        finding="FORCING alpha_hat MEETS THE COSMOLOGICAL CONSTANT PROBLEM -- a CANCELLATION problem, "
                "mechanism REOPENED. The one natural, non-fitted forcing gives alpha_hat = 1 (given the "
                "Planck hypothesis, 33 -- one archon = one Planck unit -- AH.1); it is REFUTED by ~122 "
                "orders (predicts the Planck density; measured cosmological constant is ~10^-122 of it -- "
                "AH.2, the checked-negative, reproducing the cc problem). CORRECTED reading (AH.3, "
                "POSTULATE): the 'worst prediction' parallel is a POINT OF CONTACT (framework and QFT give "
                "the SAME naive Planck-density answer for the SAME reason -- one Planck-quantum per Planck-"
                "cell); the cc problem is a CANCELLATION problem; alpha_hat=1 is the UN-CANCELLED sum and "
                "alpha_hat ~10^-122 is the near-cancellation RESIDUAL. The framework carries candidate "
                "cancellation structure QFT's flat vacuum LACKS -- signed deficit (14), deg-6 mirror "
                "(14/15), conserved signed totals (14.B.5), frustration epsilon (16). CORRECTED end (AH.4, "
                "OWED, REOPENED): alpha_hat is NOT shown irreducibly external -- one refuted SWAG does not "
                "close its reachability; what is OWED is the cancellation / frustration / TRANSFER-RULE "
                "MECHANISM (the F2 lead) as the candidate route -- computing the MECHANISM's structure, "
                "NEVER fishing for 10^-122 (refused-list holds; danger zone OUT). Honest obstacles named: "
                "this substrate is one-sided D>=0 (a two-sided crossing needs 15's deferred negative-"
                "curvature geometry); epsilon is the DYNAMO not the vacuum (16.D.3, respect the typing); "
                "(l_P/L_horizon)^2 still carries the external horizon. NOT a fit, NOT the census, NOT the "
                "refused routes. The arc does NOT end here -- it reopens onto the cancellation mechanism.",
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
