#!/usr/bin/env python3
"""Container 24 -- STONE GROUNDING: ground the STRUCTURAL alpha. Rests on 00, 13, 23; cites 17, 18.

Step 12 of the physics-bridge arc (revised roadmap). Discharges container 22's owed_c AS FAR AS THE
WARRANT CONDITION NEEDS IT -- which is the STRUCTURAL alpha-link (I = alpha*L), NOT alpha's numeric
value. Container 23 reconstructed Theorem LI cold (the level L(d)=|A(d)| is a well-defined additive
integer count) but left LI.5 -- "IF every archon carries a common quantum alpha THEN I(d)=alpha*L(d)"
-- a POSTULATE. This container GROUNDS that premise: it shows the common-alpha (EAI) is FORCED, not
assumed, up to a single free scale.

SCOPE (Kevin's decision, Maths 6.5): ground the STRUCTURAL alpha only. alpha's VALUE and physical
reading (energy/bit units, base-2/ln2, Compton=registration-boundary) enter at the Stones as EXTERNAL
input and stay quarantined/owed -- per SEC9's own resurrect condition (an OWNER DECISION to accept
mass/hbar/c as external, or derive them -- the mass/census DANGER ZONE, out of scope) and Kevin's
2026-07-16 note deferring the "registration min-info = Bekenstein-at-Compton (2*pi nats)" conjecture as
a marked lead for a later session. SEC9-PHASE-CLOSURE-HYPOTHESIS is OPEN (searched: SUPERSEDED_BY NONE).

  SG.1  the REPRESENTATION THEOREM (DERIVED). Any information assignment that is ADDITIVE on disjoint
        registration elements (23.LI.3) and archon-SYMMETRIC (equal on every archon) is EXACTLY
        alpha*L(d) for a single constant alpha -- the per-archon quantum. Equal-weight (EAI) is FORCED
        by symmetry + additivity, not assumed; a NON-constant weight breaks proportionality-to-count (a
        checked negative). Only the SCALE alpha is free. Payoff: I(B_r) = alpha*|B_r| -- the warrant
        condition's top-down leg, now grounded in the count.
  SG.2  archon INTRINSICNESS (POSTULATE, the triadic R15b). An archon is container 00's featureless
        level-0 primitive; if information is INTRINSIC to an archon (not its web-position), it is equal
        on every archon -- licensing SG.1's symmetry. Lighter than the dcpo's R15b-as-new-axiom because
        the triadic archon manifestly has no intrinsic distinguishing feature; EAI grounded MODULO this.
  SG.3  c = alpha/tau STRUCTURAL CONSTANCY (DERIVED). Each registration step contributes EXACTLY alpha
        (covering-cold, 23.LI.2: one fresh archon per step), independent of which archon or where -- so
        the per-tick information gain is constant. This is the structural core of the master handoff's
        "c=alpha/tau constant, proved from equal archon information + the covering property" (value owed).
  SG.4  the VALUE, LOCATED (OWED, quarantined). alpha's numeric value + physical reading are EXTERNAL
        Stone input (17/18), never a premise: base-2/ln2 (S.4), Compton=boundary (SEC9 OPEN), the Planck
        hypothesis (P.3), the deferred min-info=Bekenstein conjecture. downstream_premise_use=False.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ the model (consumes 13 + 23)
# The disjoint-insert step and the level are container 13/23's -- one home, consumed here.
def insNew(p, s):
    return s if p in s else s + [p]


def union(a, b):
    acc = list(a)
    for x in b:
        acc = insNew(x, acc)
    return acc


def L(s):
    return len(s)


def weighted(w, s):
    """A general information assignment: sum a weight over the archons of s. w constant = symmetric."""
    return sum(w(a) for a in s)


def constW(a):
    return lambda _archon: a


# ---- SG.1 the representation theorem -- DERIVED ----------------------------------------
ALPHA = 3                                   # a concrete scale for the witnesses; alpha is the FREE scale
# (i) constant (symmetric) weight alpha => the assignment IS alpha * L(d)
rep_is_alpha_count = all(weighted(constW(ALPHA), s) == ALPHA * L(s)
                         for s in ([10, 20, 30, 40], [1, 2, 3], []))
# (ii) additive on disjoint registration elements (consumes 23.LI.3)
rep_additive = (weighted(constW(ALPHA), union([1, 2, 3], [4, 5, 6]))
                == weighted(constW(ALPHA), [1, 2, 3]) + weighted(constW(ALPHA), [4, 5, 6]))
# (iii) CHECKED NEGATIVE: a non-constant (asymmetric) weight breaks proportionality-to-count --
#       so equal-weight/EAI is exactly what forces I proportional to L.
rep_nonconstant_breaks = (weighted(lambda a: a, [1, 2, 3]) != ALPHA * 3)   # 6 != 9
# (iv) the SCALE is the only freedom: any alpha gives I = alpha*L (the structure is scale-independent)
rep_scale_free = all(weighted(constW(a), [1, 2, 3, 4]) == a * 4 for a in (1, 3, 7, 100))
sg1_ok = rep_is_alpha_count and rep_additive and rep_nonconstant_breaks and rep_scale_free
step("SG.1", "the representation theorem: additive + archon-symmetric => I(d) = alpha*L(d) (EAI forced)",
     "an information assignment additive on disjoint elements (23.LI.3) and equal on every archon "
     "(symmetric) equals alpha*L(d) for one constant alpha; non-constant weight breaks it (checked "
     "negative); only the scale alpha is free",
     ["23.LI.2", "23.LI.3", "13.A.2"],
     "the grounding of container 23's LI.5 premise. LI.5 assumed 'every archon carries a common quantum "
     "alpha'; here that is FORCED, not assumed. Model a general information assignment as a weight summed "
     "over an element's archons. Additivity on disjoint elements is 23.LI.3. SYMMETRY -- equal weight on "
     "every archon -- makes the weight CONSTANT, call it alpha; then the assignment is exactly alpha*L(d) "
     "(the archon count times the quantum). The CHECKED NEGATIVE is essential: a NON-constant "
     "(asymmetric) weight does NOT give a count-proportional assignment (sum of archon-ids on {1,2,3} is "
     "6, not alpha*3) -- so proportionality-to-count holds PRECISELY WHEN the weight is constant, i.e. "
     "EAI. And the SCALE is the ONLY freedom: every alpha yields I=alpha*L, so the structure is fixed and "
     "alpha is a single free constant (its value is SG.4's owed external input). Equal Archon Information "
     "is now a REPRESENTATION theorem up to scale, not a postulate. Its payoff meets the warrant "
     "condition: for a ball, I(B_r) = alpha*L(B_r) = alpha*|B_r| (23.LI.4) -- the top-down I/alpha "
     "recovers the bottom-up count, grounded in the count rather than assumed.",
     "UNIQUE up to the scale alpha (symmetric additive assignment = alpha*L; alpha the one free constant)",
     "DERIVED",
     {"rep_is_alpha_count": rep_is_alpha_count, "rep_additive_on_disjoint": rep_additive,
      "nonconstant_weight_breaks_count_proportionality": rep_nonconstant_breaks,
      "scale_is_the_only_freedom": rep_scale_free,
      "EAI_is_forced_not_assumed": True,
      "payoff": "I(B_r) = alpha*L(B_r) = alpha*|B_r| (with 23.LI.4) -- the warrant condition's top-down leg",
      "alpha_value": "the single free scale -- SG.4's owed external Stone input"},
     check="constant (symmetric) weight => I=alpha*L; non-constant breaks it; every alpha gives I=alpha*L")
assert sg1_ok

# ---- SG.2 archon intrinsicness -- POSTULATE (the triadic R15b) --------------------------
step("SG.2", "archon intrinsicness (the triadic R15b): information is intrinsic => symmetric (POSTULATE)",
     "an archon is container 00's featureless level-0 primitive; IF information is intrinsic to an archon "
     "(not its web-position) THEN it is equal on every archon -- the symmetry SG.1 consumes",
     ["00.2", "00.3", "SG.1"],
     "the one genuine assumption behind EAI, named and held. SG.1 needs SYMMETRY (equal weight per "
     "archon). What licenses it: an archon on the triadic floor is container 00's LEVEL-0 PRIMITIVE -- one "
     "registration, FEATURELESS in itself (all its structure is relational / web-position, 01). So the "
     "only way two archons could carry different information is if information depended on web-POSITION. "
     "The postulate (the triadic analog of the dcpo floor's R15b, 'I is an intrinsic order-theoretic "
     "quantity, not dependent on extrinsic coordinates') is that information is INTRINSIC to the archon. "
     "Given featurelessness, intrinsic => equal => symmetric. This is LIGHTER than the dcpo's R15b (there "
     "an added axiom, with a topological transitivity obstruction) because the triadic archon MANIFESTLY "
     "has no intrinsic distinguishing feature -- but it is still an assumption, so it is graded POSTULATE. "
     "EAI is grounded MODULO this: SG.1 forces I=alpha*L once symmetry holds, and SG.2 is why symmetry "
     "holds. (Note: archons in different web-positions -- deg-5 vs deg-6, 13.A.3 -- differ RELATIONALLY, "
     "not intrinsically; each still carries one alpha. The COUNT varies by site, the per-archon quantum "
     "does not -- consistent with 23.)",
     "POSTULATE (intrinsicness of information; featurelessness is from 00, intrinsicness is assumed)",
     "POSTULATE",
     {"archon_is_featureless": "container 00 level-0 primitive; all structure relational (01)",
      "intrinsicness_postulate": "information is intrinsic to an archon, not its web-position (triadic R15b)",
      "therefore": "intrinsic + featureless => equal on every archon => symmetric (SG.1's hypothesis)",
      "lighter_than_dcpo_R15b": "the triadic archon manifestly has no intrinsic distinguishing feature",
      "eai_grounded_modulo_this": True},
     check=None)

# ---- SG.3 c = alpha/tau structural constancy -- DERIVED --------------------------------
# Each fresh registration step adds EXACTLY alpha (covering-cold: one fresh archon per step, 23.LI.2),
# independent of which archon or where -- so the per-tick information gain is constant.
step_gain_constant = all(
    weighted(constW(ALPHA), insNew(p, [1, 2, 4])) == weighted(constW(ALPHA), [1, 2, 4]) + ALPHA
    for p in (10, 55, 99))
# constant across DIFFERENT current elements too (position-independent)
step_gain_position_indep = all(
    weighted(constW(ALPHA), insNew(999, base)) == weighted(constW(ALPHA), base) + ALPHA
    for base in ([1], [1, 2, 3, 4, 5], [7, 8]))
sg3_ok = step_gain_constant and step_gain_position_indep
step("SG.3", "c = alpha/tau structural constancy: every registration step contributes exactly alpha",
     "each covering step adds one fresh archon (23.LI.2), so the information gain per step is exactly "
     "alpha, independent of which archon or which current element -- a constant per-tick gain",
     ["SG.1", "23.LI.2"],
     "the structural core of the master handoff's 'c = alpha/tau is constant, proved from equal archon "
     "information content and the covering property' -- both of which are now cold (SG.1's EAI-up-to-scale "
     "and 23.LI.2's covering). A registration advances one archon per tick (covering-cold: each step adds "
     "exactly one fresh archon). By SG.1 each archon carries alpha, so each step's information gain is "
     "EXACTLY alpha -- checked constant across different added archons AND different current elements "
     "(position-independent). Reading tau as the tick (one registration step), the per-tick information "
     "rate is alpha/tau, CONSTANT across archons and states. This is the STRUCTURAL constancy only -- the "
     "VALUE of c (and of alpha, tau) is external (SG.4). It grounds WHY c is constant (equal quanta + "
     "one-per-tick), not what c IS. Ties structurally to Stone 6 (18) and the Planck hypothesis "
     "c=(edge)/(tick), which remain quarantined for their physical reading.",
     "UNIQUE (the per-step gain is exactly alpha; constant by covering + EAI)", "DERIVED",
     {"step_gain_is_alpha": step_gain_constant, "constant_across_position": step_gain_position_indep,
      "reading": "per-tick information gain = alpha; rate alpha/tau constant across archons/states",
      "structural_only": "the CONSTANCY is grounded; the VALUE of c/alpha/tau is external (SG.4)",
      "master_handoff_line": "c=alpha/tau proved from equal archon info + covering (both now cold)"},
     check="each fresh registration step adds exactly alpha, constant across archon and current element")
assert sg3_ok

# ---- SG.4 the value, located -- OWED (quarantined) -------------------------------------
step("SG.4", "the VALUE of alpha, located: external Stone input, never a premise (OWED, quarantined)",
     "alpha's numeric value + physical reading (energy/bit units, base-2/ln2, Compton=boundary) are "
     "EXTERNAL Stone input (17/18), quarantined; base-2 (S.4), SEC9 (OPEN), the Planck hypothesis (P.3), "
     "and the min-info=Bekenstein conjecture stay owed -- the danger zone (mass/census) is out of scope",
     ["SG.1", "17.S.3", "17.S.4", "18.P.3"],
     "the honest boundary, first-class and quarantined. This container grounds the STRUCTURAL alpha "
     "(SG.1-SG.3): the substrate has a native information content -- the archon count L in alpha-units -- "
     "and I=alpha*L is forced up to the scale alpha. What it does NOT do, by Kevin's explicit scope "
     "decision (Maths 6.5) and SEC9's own resurrect condition, is fix alpha's VALUE or its physical "
     "reading. That is EXTERNAL Stone input: (i) base-2 / the ln2 (Stone 5 S.4, why registration is "
     "base-2, unsettled); (ii) the Compton = registration-boundary equivalence (SEC9-PHASE-CLOSURE-"
     "HYPOTHESIS, OPEN -- searched, SUPERSEDED_BY NONE, no repair exists; grounding it needs mass/hbar/c "
     "derived, which is the mass/census DANGER ZONE with no attempt anywhere, or an owner decision to "
     "accept them as external); (iii) Kevin's Planck hypothesis l_P/t_P = edge/tick (Stone 6 P.3, "
     "flagged); (iv) the conjecture that a registration's minimum information content = the Bekenstein "
     "bound at Compton (2*pi nats), which Kevin's 2026-07-16 note explicitly DEFERS as 'unprovable yet, a "
     "marked lead for a later session'. NONE is a premise here (downstream_premise_use=False): the "
     "warrant condition (container 22) needs only the STRUCTURAL alpha-link, which SG.1 supplies; alpha's "
     "value is a Step-14 (rho_Lambda) concern that waits on this external input. The count is grounded; "
     "the ruler's value is external.",
     "OWED (alpha's value/reading is external Stone input; located, not closed here)", "OWED",
     {"structural_alpha_grounded": "SG.1-SG.3: I=alpha*L forced up to scale; EAI a representation theorem",
      "value_is_external": "alpha's numeric value + physical reading enter at the Stones (17/18)",
      "owed_base2": "why base-2 registration (Stone 5 S.4, ln2) -- unsettled",
      "owed_sec9": "Compton=registration-boundary (SEC9, OPEN, SUPERSEDED_BY NONE; needs mass/hbar/c or owner decision)",
      "owed_planck": "Kevin's Planck hypothesis l_P/t_P=edge/tick (Stone 6 P.3, flagged)",
      "deferred_conjecture": "registration min-info = Bekenstein-at-Compton (2*pi nats) -- Kevin 2026-07-16, marked lead",
      "danger_zone_out": "mass/census (deriving mass/hbar/c) is out of scope",
      "warrant_condition": "needs only the structural alpha-link (SG.1); value waits (Step 14)",
      "downstream_premise_use": False, "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="24-stone-grounding",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        alpha_witness=ALPHA,
        rep_is_alpha_count=rep_is_alpha_count,
        rep_additive_on_disjoint=rep_additive,
        nonconstant_weight_breaks=rep_nonconstant_breaks,
        scale_is_the_only_freedom=rep_scale_free,
        step_gain_is_alpha=step_gain_constant,
        step_gain_position_indep=step_gain_position_indep,
        eai_is_representation_theorem=True,
        structural_alpha_grounded=True,
        alpha_value_is_external_owed=True,
        closes="container 22 owed_c (the structural alpha-link; warrant condition's convergence grounded)",
        still_owed="alpha's VALUE + physical reading (base-2/SEC9/Planck) -- external Stone input, Step 14",
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
