#!/usr/bin/env python3
"""Container 57 -- CROSSING B (Rung 0): the WEINBERG ANGLE sin^2(theta_W).

The contact plan's crossing B (CONTACT.md), attacked head-on. The owner-gate/"danger" ceremony is dropped
(2026-09-10, Kevin: "drop the danger ... just pursuit of truth; let the math be what it is; no fake walls")
-- but the five gates and honest grading are KEPT, harder than ever: G1 dimensionless-first; G2
compute-then-compare sealed; G3 renaming; G4 cannot-fail (state the refuter first); G5 no-fit.

THE HONEST LANDING: a REDUCTION + a DISCRIMINATING REFUTATION of the naive shortcut, locating the true
value in the fork. Not a cold matched value. Nothing fitted.

  WA.1  the target (G1, dimensionless): sin^2(theta_W) = g'^2/(g^2+g'^2), a pure mixing FRACTION (the angle
        between the U(1)_Y and the physical photon direction in the rank-2 Cartan plane, 50.EW.1). Measured
        sin^2(theta_W)(M_Z) ~ 0.23122; canonical GUT (SU(5)) tree value 3/8 = 0.375 -- CITED to falsify, not
        input. DERIVED (states the dimensionless target).
  WA.2  the reduction (like 43 for dim=3): theta_W IS the relative NORMALIZATION of U(1)_Y against su(2) in
        the rank-2 Cartan (50.EW.1). The su(2) side is carrier-fixed ([i,j]=2k, 28.W.1). So the whole angle
        collapses to ONE question: how is the abelian Y normalized relative to the isospin? DERIVED.
  WA.3  the abelian is SCALELESS (the crux): an abelian u(1) has [X,X]=0 (29.EM.2), so its Killing form is
        IDENTICALLY ZERO -- it carries no intrinsic normalization. Hence theta_W CANNOT be fixed by the
        electroweak algebra alone (exactly why g' is a FREE parameter in the SM); the normalization must
        come from embedding Y into a NON-ABELIAN trace (a larger structure). DERIVED (rests on 29).
  WA.4  the substrate-native candidate + its REFUTATION (G2/G3/G4/G5): the only normalization intrinsic to
        the located structure (H) is the quaternion/u(2) trace form <X,Y> = -Tr(XY), under which the two
        Cartan generators T0 (center) and T3 are EQUAL-norm. On the electroweak doublet that gives, cold,
        sin^2(theta_W) = Tr(T3^2)/Tr(Q^2) = (1/2)/1 = 1/2. REFUTER stated first (G4): a U(2) unification
        predicts 1/2; measured is ~0.231, GUT 3/8 -- NOT 1/2. So the naive quaternion-center identification
        is REFUTED (cold: 1/2 != 3/8, name-free G3, no-fit G5). The discipline working. DERIVED.
  WA.5  the honest LOCATION (why it needs the fork): the refutation's LESSON -- u(2) gives 1/2 because it
        OMITS COLOUR; the correct Tr(Q^2) runs over the FULL matter multiplet (quarks' fractional charges),
        set by the E8->SM embedding (the fork, 51.GP.4) that folds the strong sector (30) in with
        electroweak. The canonical SU(5) in E8 gives 3/8 at unification (cited), running to ~0.231 by
        external RG. So theta_W is LOCATED precisely in the fork's hypercharge normalization. POSTULATE
        (the correspondence: the located structure <-> the physical theta_W; the cold value awaits the fork).
  WA.6  OWED: the cold sin^2(theta_W) VALUE (needs the fork's embedding + the census hypercharges, 56.MC.6);
        the RG running 3/8 -> 0.231 (external QFT, not substrate). OWED.

Rests on 50 (rank-2 Cartan, the Z), 29 (u(1) abelian, [i,i]=0), 28 (su(2), [i,j]=2k), 51 (the gauge
product + the fork), 30/31 (the strong sector / colour), 56 (the matter census kinds). Cites: the Weinberg
mixing, the U(2) sin^2=1/2 result, the SU(5) 3/8, the measured 0.23122.
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


# ---- WA.1 the target: the dimensionless mixing fraction (G1) -- DERIVED -----------------
CARTAN_RANK = 2                 # 50.EW.1: Y and T3
MEASURED = 0.23122             # sin^2(theta_W)(M_Z), MS-bar -- CITED to falsify
GUT_NUM, GUT_DEN = 3, 8        # SU(5) tree value 3/8 = 0.375 -- CITED
step("WA.1", "the target (G1, dimensionless): sin^2(theta_W) = g'^2/(g^2+g'^2), the electroweak mixing fraction",
     "the dimensionless target is sin^2(theta_W) = g'^2/(g^2+g'^2) -- the mixing FRACTION setting the angle "
     "between the U(1)_Y gauge field B and the physical (massless) photon in the rank-2 electroweak Cartan "
     "plane (50.EW.1: the photon is a combination of Y and T3, the Z the orthogonal). It is a pure "
     "dimensionless number (a ratio of couplings), an alpha-hat-type quantity (27) -- forceable in "
     "principle, never manufactured. Measured sin^2(theta_W)(M_Z) ~ 0.23122; canonical GUT tree value 3/8",
     ["50.EW.1", "50.EW.4", "27.DA.2"],
     "gate G1 first: dimensionless-only. Unlike a mass or the arcsec, theta_W carries no anchor -- it is a "
     "ratio of the two electroweak couplings, so it is exactly the kind of quantity the substrate may force "
     "(27). The measured value 0.23122 and the canonical GUT value 3/8 = 0.375 are CITED here only to mark "
     "the target; they enter as falsification references (G2), never as inputs. The container computes the "
     "substrate's own answer and then compares.",
     "UNIQUE (the dimensionless target: sin^2(theta_W) = g'^2/(g^2+g'^2))", "DERIVED",
     {"cartan_rank": CARTAN_RANK, "measured": MEASURED, "gut_num": GUT_NUM, "gut_den": GUT_DEN,
      "gut_value": GUT_NUM / GUT_DEN, "dimensionless": True},
     check="the target is the dimensionless mixing fraction sin^2(theta_W)=g'^2/(g^2+g'^2); measured ~0.231, GUT 3/8 cited")
assert CARTAN_RANK == 2

# ---- WA.2 the reduction: theta_W = the U(1)_Y-vs-su(2) normalization -- DERIVED ---------
step("WA.2", "the reduction (like 43): theta_W IS the relative normalization of U(1)_Y against su(2); the su(2) side is carrier-fixed",
     "theta_W reduces to ONE question -- the relative NORMALIZATION of the abelian U(1)_Y generator against "
     "the su(2) generators in the rank-2 Cartan (50.EW.1). The su(2) side is FIXED by the carrier: the "
     "quaternion bracket [i,j]=2k, [j,k]=2i, [k,i]=2j (28.W.1) gives su(2) a definite structure and trace "
     "normalization. So everything unknown in theta_W sits in the abelian Y normalization",
     ["WA.1", "50.EW.1", "28.W.1"],
     "the reduction, in the spirit of 43 (which collapsed dim=3 to one premise). tan(theta_W) = g'/g, and a "
     "coupling is the inverse scale of its generator; so sin^2(theta_W) = g'^2/(g^2+g'^2) is entirely "
     "determined by the RATIO of the U(1)_Y normalization to the su(2) normalization. The su(2) half is not "
     "free: 28.W.1 fixed its structure constants by cold quaternion multiplication ([i,j]=2k), so su(2) "
     "carries the carrier's own trace normalization. The entire content of theta_W therefore collapses onto "
     "the ONE remaining question: how is the abelian Y normalized relative to that? WA.3 shows this cannot "
     "be answered inside the electroweak algebra.",
     "UNIQUE (theta_W collapses to the U(1)_Y-vs-su(2) normalization ratio; su(2) carrier-fixed by 28)", "DERIVED",
     {"su2_fixed_by": "28.W.1 ([i,j]=2k) -- the carrier's trace normalization",
      "reduces_to": "the relative normalization of the abelian U(1)_Y against su(2)"},
     check="theta_W reduces to the U(1)_Y-vs-su(2) normalization ratio; su(2) is carrier-fixed (28)")

# ---- WA.3 the abelian is scaleless (the crux) -- DERIVED (rests on 29) ------------------
ABELIAN_SELF_BRACKET = 0        # 29.EM.2: [i,i] = 0 -- the u(1) is abelian
KILLING_ABELIAN = 0             # abelian => ad = 0 => Killing form identically 0 => no intrinsic scale
step("WA.3", "the abelian U(1) is SCALELESS: [X,X]=0 (29) => Killing form == 0 => no intrinsic normalization -- exactly why g' is free in the SM",
     "an abelian u(1) has [X,X]=0 (29.EM.2, the abelian direction), so ad_X = 0 for its generator, so its "
     "Killing form K(X,X) = tr(ad_X ad_X) is IDENTICALLY ZERO. An abelian factor therefore carries NO "
     "intrinsic normalization -- there is no algebra-fixed scale for Y. Hence theta_W CANNOT be fixed by "
     "the electroweak algebra alone: the U(1)_Y coupling g' is a FREE parameter (exactly the SM situation). "
     "The normalization MUST come from embedding Y into a NON-abelian trace (a larger structure)",
     ["WA.2", "29.EM.2"],
     "the crux, and the honest reason theta_W is hard. This is not a substrate defect -- it is a theorem of "
     "Lie theory that mirrors the physics exactly. su(2) is non-abelian, so its Killing form is "
     "non-degenerate and it self-normalizes (WA.2). u(1) is abelian: [X,X]=0 (already cold in 29.EM.2, "
     "[i,i]=0), so ad_X=0 and the Killing form vanishes on it -- an abelian Lie algebra has no invariant "
     "inner product of its own, hence no intrinsic scale. This is PRECISELY why, in the Standard Model, the "
     "hypercharge coupling g' is a free input and sin^2(theta_W) is not predicted by the SM: the abelian "
     "factor is scaleless. So the substrate does not (and cannot) force theta_W from the electroweak "
     "algebra; it forces the QUESTION into the open -- the normalization of Y must be supplied by embedding "
     "it into a non-abelian trace. WA.4 tries the minimal such trace intrinsic to the carrier; WA.5 shows "
     "the physical one needs the fork.",
     "UNIQUE (abelian => Killing form == 0 => Y is scaleless in the EW algebra; the normalization needs a non-abelian embedding)", "DERIVED",
     {"abelian_self_bracket": ABELIAN_SELF_BRACKET, "killing_form_abelian": KILLING_ABELIAN,
      "consequence": "Y has no algebra-intrinsic scale; g' is free in the SM; the normalization needs a non-abelian trace"},
     check="abelian [X,X]=0 (29) => Killing form 0 => Y scaleless in the EW algebra; needs a non-abelian embedding")
assert ABELIAN_SELF_BRACKET == 0 and KILLING_ABELIAN == 0

# ---- WA.4 the substrate-native candidate (u(2) trace form) and its REFUTATION -----------
# The minimal normalization intrinsic to H: the quaternion/u(2) trace form <X,Y> = -Tr(XY).
# Under it T0 (center) and T3 are equal-norm. On the doublet (nu,e): T3 = +-1/2, Q = 0,-1.
# 4*Tr(T3^2) = 1+1 = 2 ; 4*Tr(Q^2) = 0+4 = 4 ; sin^2(theta_W) = 2/4 = 1/2.
FOUR_TR_T3SQ = 1 + 1                     # 4*[(1/2)^2 + (1/2)^2] = 2
FOUR_TR_QSQ = 0 + 4                      # 4*[0^2 + (-1)^2] = 4
SINSQ_U2_NUM, SINSQ_U2_DEN = 1, 2       # 2/4 reduced = 1/2
TWO_NORM_T0, TWO_NORM_T3 = 1, 1         # 2*<T0,T0> = 2*<T3,T3> = 1 (equal-norm under the trace form)
# refutation (cold): 1/2 != 3/8  <=>  1*8 != 3*2  <=>  8 != 6
u2_equals_gut = (SINSQ_U2_NUM * GUT_DEN == GUT_NUM * SINSQ_U2_DEN)   # 8 == 6 -> False
u2_refuted = not u2_equals_gut                                        # True: 1/2 != 3/8
step("WA.4", "the substrate-native candidate (u(2) trace form) gives sin^2(theta_W)=1/2 -- REFUTED (G2/G3/G4/G5): measured ~0.231, GUT 3/8, NOT 1/2",
     "the only normalization intrinsic to the located structure H (without invoking the owed fork) is the "
     "quaternion/u(2) trace form <X,Y> = -Tr(XY), under which the two Cartan generators T0 (the u(1) center) "
     "and T3 are EQUAL-norm (2<T0,T0> = 2<T3,T3> = 1). On the electroweak doublet (nu,e): T3 = +-1/2, "
     "Q = T3+Y = 0,-1, so sin^2(theta_W) = Tr(T3^2)/Tr(Q^2) = (1/4+1/4)/(0+1) = 1/2. REFUTER FIRST (G4): a "
     "U(2) unification predicts exactly 1/2; measurement gives ~0.231 and the GUT tree value is 3/8 -- NOT "
     "1/2. So the naive quaternion-center identification of Y is REFUTED (1/2 != 3/8, cold)",
     ["WA.3", "29.EM.2", "50.EW.1"],
     "the substrate's minimal honest attempt, run through all five gates and REFUTED -- the discipline "
     "working as designed (a discriminating negative). G3 (renaming): erase 'Weinberg' -- the substrate "
     "says the rank-2 Cartan (50) has an abelian direction that, normalized by the carrier's own trace form, "
     "is equal-norm to T3, and the equal-norm mixing fraction on the doublet is 1/2; produced name-free. G2 "
     "(compute-then-compare, sealed): 1/2 is computed from the trace form FIRST; the measured 0.231 and the "
     "GUT 3/8 enter HERE, cited only to falsify. G4 (cannot-fail): the refuter is stated first -- IF the "
     "electroweak U(1)_Y were simply the quaternion/u(2) center (equal-norm), sin^2(theta_W) would be 1/2; "
     "it is not, so the candidate COULD fail and DID. G5 (no-fit): 1/2 is read off the trace form, not "
     "assembled toward any target; no refused-list fishing. THE COLD FACT (Lean-checked): 4Tr(T3^2)=2, "
     "4Tr(Q^2)=4, so the fraction is 2/4 = 1/2, and 1/2 != 3/8 (1*8=8 != 3*2=6). So the substrate's minimal "
     "electroweak-only normalization is RULED OUT. This is honest forward motion: it eliminates the U(2) "
     "shortcut and forces the question to the larger embedding (WA.5). Not a cold matched value -- a "
     "discriminating refutation.",
     "UNIQUE (u(2) trace form => equal-norm => sin^2=1/2 on the doublet; 1/2 != 3/8 => REFUTED)", "DERIVED",
     {"four_tr_t3sq": FOUR_TR_T3SQ, "four_tr_qsq": FOUR_TR_QSQ,
      "sinsq_u2_num": SINSQ_U2_NUM, "sinsq_u2_den": SINSQ_U2_DEN, "sinsq_u2_value": SINSQ_U2_NUM / SINSQ_U2_DEN,
      "two_norm_t0": TWO_NORM_T0, "two_norm_t3": TWO_NORM_T3,
      "u2_refuted": u2_refuted, "u2_equals_gut": u2_equals_gut,
      "refuter": "U(2) predicts 1/2; measured ~0.231 and GUT 3/8 -- NOT 1/2",
      "gates": "G1 dimensionless (WA.1); G2 compute-then-compare (here); G3 name-free; G4 refuter=1/2; G5 no-fit"},
     check="u(2) trace form: equal-norm T0=T3; sin^2=2/4=1/2 on the doublet; 1/2 != 3/8 => REFUTED")
assert FOUR_TR_T3SQ == 2 and FOUR_TR_QSQ == 4 and u2_refuted and not u2_equals_gut

# ---- WA.5 the honest location: the fork's NATIVE route (58), not SU(5)/3/8 -- POSTULATE ---
step("WA.5", "the location (POSTULATE, filed 19; UPDATED w/ the fork): u(2) gives 1/2 because it OMITS COLOUR; the fork's route is the NATIVE Z/6 hypercharge grading (58), NOT SU(5)/3/8 -- theta_W owed to K2",
     "the refutation's LESSON: u(2) gives 1/2 because it uses only the electroweak doublet -- it OMITS "
     "COLOUR. The correct Tr(Q^2) must fold in the strong sector (colour, 30/31). The collaborator's fork "
     "(now integrated as container 58) supplies exactly this, and NOT by an SU(5)/3/8 GUT embedding: it "
     "builds hypercharge from TWO NATIVE gradings -- colour triality Z/3 (31) x duality Z/2 (45) = Z/6 -- "
     "giving (SU(3)xSU(2)xU(1))/Z6 and the forced fractional Y = -(t/3+w/2); the mass-founded Q=T3+Y is "
     "abandoned. The ABSOLUTE hypercharge levels (fork K2) remain conditional on the multiplet content. So "
     "theta_W is LOCATED precisely at K2 (the representation assignment, 58.HC.5/HC.6), NOT delivered as a "
     "cold value -- the fork's own sin^2(theta_W)=1/phi^3 is a FENCED candidate (WA.6), not banked",
     ["WA.4", "58.HC.2", "58.HC.5", "56.MC.6"],
     "the honest placement, graded POSTULATE, UPDATED after integrating the fork (container 58; CORRECTIONS "
     "logs the earlier over-cite). What the substrate has EARNED cold: theta_W is one normalization question "
     "(WA.2), the abelian factor cannot answer it (WA.3), the minimal carrier answer (u(2)->1/2) is refuted "
     "(WA.4), AND the SM gauge group (SU(3)xSU(2)xU(1))/Z6 with the forced fractional hypercharge is now "
     "native (58, from colour Z/3 x duality Z/2). What is a READING (filed 19, quarantined): that the "
     "PHYSICAL theta_W follows once the multiplet CONTENT (the absolute hypercharge levels, fork K2 / "
     "56.MC.6) is selected. CORRECTION to the prior draft: the earlier WA.5 cited the canonical SU(5)-in-E8 "
     "value 3/8 as 'what the fork must reproduce'. The actual fork does NOT take the GUT/SU(5) route -- it "
     "uses the native Z/6 grading (58) and abandons Q=T3+Y; 3/8 is retained only as the standard GUT "
     "reference in WA.4's cold comparison, NOT as the substrate's predicted value. So the correspondence "
     "'located structure <-> physical theta_W' is a POSTULATE; the cold value awaits K2. The refutation "
     "(WA.4) is name-free and stands regardless. No downstream premise rests on this reading.",
     "POSTULATE (theta_W located at the fork's native Z/6 grading + K2 content, 58; NOT SU(5)/3/8; cold value owed)", "POSTULATE",
     {"why_u2_wrong": "u(2) omits colour; the correct grading folds the strong sector in (Z/3 x Z/2 = Z/6, 58)",
      "located_in": "the native Z/6 hypercharge grading (58.HC.2) + the content selection K2 (58.HC.5 / 56.MC.6)",
      "correction": "prior draft cited SU(5)->3/8 as the fork's route; the actual fork is native Z/6, Q=T3+Y abandoned; 3/8 kept only as WA.4's GUT reference",
      "rests_on": "the correspondence located-structure <-> physical theta_W (filed 19); K2 content owed",
      "downstream_premise_use": False},
     check=None)

# ---- WA.6 OWED: the cold value (fork + census), the RG running (external) ---------------
step("WA.6", "OWED (UPDATED w/ the fork): the cold sin^2(theta_W) value needs the content K2 (58); the fork's 1/phi^3 ~ 0.2361 is a FENCED candidate, NOT banked; RG running external",
     "OWED: (a) the cold sin^2(theta_W) VALUE -- now located at the content selection K2 (58.HC.5/HC.6): "
     "the native Z/6 hypercharge grading (58) is forced, but its ABSOLUTE levels ride on which irreps are "
     "the fermions (the representation assignment, fork K2 / 56.MC.6); only then does the substrate emit its "
     "own number. (b) the fork's candidate sin^2(theta_W) = 1/phi^3 ~ 0.2360679 is a FENCED near-miss -- "
     "graded OBSERVATION by the fork (inversion-then-match, representation UNFORCED), 2.1% off measured "
     "0.23122 (MS-bar), more off on-shell -- NOT banked (rule 17: resemblance != result; the refused-list "
     "ethos). (c) the RG running to the M_Z value is external QFT, not a substrate quantity. The reduction + "
     "the refutation stand; the cold value is owed to K2",
     ["WA.4", "WA.5", "58.HC.6"],
     "the honest residual, UPDATED after the fork (58). WA.1-WA.4 make a genuine, disciplined crossing: "
     "theta_W reduces to one normalization (WA.2), shown unanswerable by the abelian algebra (WA.3), and the "
     "minimal carrier guess is refuted cold (WA.4, 1/2 != 3/8, and != measured 0.231). Integrating the fork "
     "(58) supplies the native Z/6 hypercharge grading and the forced fractional Y -- but the ABSOLUTE "
     "levels are conditional on the content (K2), so the substrate's OWN cold theta_W is still owed, now "
     "located precisely at K2 (the representation assignment). The fork's 1/phi^3 is carried as the "
     "frontier's stated target ONLY -- a fenced OBSERVATION at 2.1%, not a result, never banked. The RG "
     "running is external QFT. So the crossing is bounded and truthful: a reduction + a discriminating "
     "negative, the joint now native (58), the cold value owed to the content K2; nothing fitted.",
     "OWED (cold value owed to the content K2, 58; 1/phi^3 fenced not banked; RG external)", "OWED",
     {"owed_value": "the substrate's own sin^2(theta_W) -- owed to the content selection K2 (58.HC.5/HC.6, 56.MC.6)",
      "fork_candidate": "sin^2(theta_W) = 1/phi^3 ~ 0.2360679 -- FENCED (OBSERVATION, inversion-match, rep unforced, 2.1% off); NOT banked",
      "owed_running": "1/phi^3 (or the K2 value) -> ~0.231 by RG flow -- external QFT, not a substrate quantity",
      "next_unblock": "select the multiplet content (K2) -- the representation assignment (58 supplied the Z/6 grading)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="57-weinberg-angle",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        cartan_rank=CARTAN_RANK, measured=MEASURED, gut_num=GUT_NUM, gut_den=GUT_DEN,
        four_tr_t3sq=FOUR_TR_T3SQ, four_tr_qsq=FOUR_TR_QSQ,
        sinsq_u2_num=SINSQ_U2_NUM, sinsq_u2_den=SINSQ_U2_DEN,
        two_norm_t0=TWO_NORM_T0, two_norm_t3=TWO_NORM_T3,
        u2_refuted=u2_refuted, u2_equals_gut=u2_equals_gut,
        finding="CROSSING B (Rung 0): the WEINBERG ANGLE, attacked head-on -- a REDUCTION + a DISCRIMINATING "
                "REFUTATION, no cold matched value. sin^2(theta_W)=g'^2/(g^2+g'^2) is dimensionless (WA.1). "
                "It REDUCES to one thing: the relative normalization of U(1)_Y vs su(2) (WA.2; su(2) "
                "carrier-fixed by 28). The abelian factor is SCALELESS -- [X,X]=0 (29) => Killing form 0 => "
                "no intrinsic scale, exactly why g' is free in the SM (WA.3). The minimal carrier "
                "normalization (the quaternion/u(2) trace form) makes T0 and T3 equal-norm and gives, cold, "
                "sin^2(theta_W)=Tr(T3^2)/Tr(Q^2)=1/2 on the doublet -- REFUTED: measured ~0.231, GUT 3/8, "
                "not 1/2 (WA.4, passes G1-G5 as a discriminating negative). WHY: u(2) omits COLOUR; the "
                "correct grading folds the strong sector in. The fork (now container 58) supplies exactly "
                "this NATIVELY -- colour Z/3 (31) x duality Z/2 (45) = Z/6, giving (SU(3)xSU(2)xU(1))/Z6 and "
                "the forced fractional Y=-(t/3+w/2), abandoning Q=T3+Y -- NOT an SU(5)/3/8 GUT route (WA.5, "
                "POSTULATE; corrects the prior SU(5) over-cite). OWED: the ABSOLUTE levels + the cold value "
                "need the content K2 (58/56); the fork's sin^2(theta_W)=1/phi^3~0.2361 is a FENCED candidate "
                "(OBSERVATION, 2.1% off), NOT banked; RG running external (WA.6). Nothing fitted; the next "
                "unblock is the content selection K2.",
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
