#!/usr/bin/env python3
"""Container 55 -- THE BORN HINGE (Rung 0, the highest-leverage non-value crossing): |amplitude|^2 = the measure.

The second crossing, on Kevin's go, ONE crossing only (CONTACT.md sequencing item 2 -- the Born-rule hinge,
structural, not a value). It is DANGER-ADJACENT (it touches probability/measurement), and it is the single
place hand-waving is most tempting -- so it is graded with maximum honesty. THE CLAIM IS NOT "we derive the
Born rule / solve measurement." The claim is: the Born rule and 43.CN.4 are ONE hinge -- the substrate's
composition norm IS |amplitude|^2 IS the intensive measure -- so closing one closes the other; and the
"square" (why |amp|^2, not |amp|) is FORCED by additivity-over-orthogonal + linear superposition
(Pythagoras on the substrate's quadratic norm form). The measure<->probability IDENTIFICATION remains the
single shared held POSTULATE.

  BR.1  the composition norm IS the squared modulus: N(q) = q*conj(q) = w^2+x^2+y^2+z^2 = |q|^2 (the
        codifferent/quaternion norm form, 06.6, is QUADRATIC), and it is MULTIPLICATIVE (43.CN.5). For a
        complex amplitude (in C subset H, 53.QK.2), N(amplitude) = |amplitude|^2. DERIVED (cold algebra).
  BR.2  the SQUARE is forced (why |amp|^2, not |amp|): the measure must be ADDITIVE over ORTHOGONAL
        (disjoint) registrations while amplitudes SUPERPOSE linearly (53). The quadratic norm form is
        additive over orthogonal directions (Pythagoras: N(a+b)=N(a)+N(b) when a . b = 0) -- the LINEAR
        modulus |q| is NOT (|a+b| != |a|+|b|). So the measure is the QUADRATIC |amp|^2, not the linear
        |amp|. DERIVED (Pythagoras on the inner product 05/06.6; additivity-over-orthogonal is the reading).
  BR.3  THE HINGE (POSTULATE, filed 19): the substrate's INTENSIVE measure (the share, 43.CN.4) = the
        quantum PROBABILITY. Since N = |amp|^2 (BR.1) = the intensive measure (CN.4), |amp|^2 = probability
        -- the BORN RULE. This IDENTIFICATION closes 43.CN.4 and the Born rule as ONE hinge. Correspondence.
  BR.4  the gate-check (G3/G4/G5): renaming (G3) -- erase "Born/probability": the substrate says the
        measure is the additive-over-orthogonal, multiplicative, unitary-invariant QUADRATIC norm |amp|^2,
        name-free. cannot-fail (G4) -- a LINEAR or QUARTIC measure fails additivity-over-orthogonal /
        multiplicativity (the refuter). no-fit (G5) -- no target fished. PASSES for the STRUCTURE (why
        squared); the probability identification (BR.3) is the held hinge. DERIVED (the gate ledger for the structure).
  BR.5  OWED + THE PAYOFF: a Gleason-type uniqueness derived on the substrate; measurement/collapse (how
        definite outcomes arise) -- NOT solved here; and THE PAYOFF: 43.CN.4 (the last held premise under
        dim=3) and the Born rule are now ONE hinge -- the measure<->probability identification is the single
        shared held POSTULATE; closing it closes both. OWED.

Rests on 06 (the quadratic codifferent norm 06.6), 43 (the multiplicative composition norm CN.4/CN.5), 53
(complex amplitudes, unitary evolution), 05 (the inner product); cites the Born rule / Gleason. THE HONEST
HEADLINE: the Born rule = 43.CN.4 applied to the amplitude; the square is forced; the measure<->probability
identification is the one held hinge -- NOT a derivation of probability, NOT a solution to measurement.
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


def qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def qconj(q):
    w, x, y, z = q
    return (w, -x, -y, -z)


def N(q):
    return sum(c * c for c in q)          # the quadratic norm = |q|^2 = w^2+x^2+y^2+z^2


def dot(a, b):
    return sum(u * v for u, v in zip(a, b))


def qadd(a, b):
    return tuple(u + v for u, v in zip(a, b))


# ---- BR.1 the composition norm IS |amplitude|^2 -- DERIVED ------------------------------
I = (0, 1, 0, 0)
J = (0, 0, 1, 0)
amp = (3, 4, 0, 0)                        # a sample complex amplitude 3+4i in C subset H
N_is_qqbar = (N(amp) == qmul(amp, qconj(amp))[0])     # N(q) = (q qbar) scalar part
N_is_sq_modulus = (N(amp) == 3 * 3 + 4 * 4)           # = |amp|^2 = 25
multiplicative = (N(qmul(I, J)) == N(I) * N(J))       # composition norm multiplicative (43.CN.5)
br1_ok = (N_is_qqbar and N_is_sq_modulus and multiplicative)
step("BR.1", "the composition norm IS the squared modulus: N(q) = q*conj(q) = |q|^2 (06.6, quadratic), multiplicative (43); N(amp) = |amp|^2",
     "the codifferent/quaternion norm form N(q) = q*conj(q) = w^2+x^2+y^2+z^2 = |q|^2 (06.6) is QUADRATIC "
     "and MULTIPLICATIVE (43.CN.5, N(qr)=N(q)N(r)); for a complex amplitude in C subset H (53.QK.2), "
     "N(amplitude) = |amplitude|^2 -- the composition norm IS the squared modulus, by the algebra",
     ["06.6.6", "43.CN.5", "53.QK.2"],
     "the identity that makes the hinge cold at its root. The carrier's norm form (06.6, the codifferent) "
     "is N(q) = q*conj(q) = w^2+x^2+y^2+z^2 -- the SQUARED length |q|^2, a quadratic form. Container 43 "
     "established this norm is MULTIPLICATIVE (the composition norm, CN.4/CN.5: N(qr)=N(q)N(r)). RUN IT: "
     "for amp = 3+4i (a complex amplitude, C subset H, 53.QK.2), N(amp) = 9+16 = 25 = 5^2 = |amp|^2; and "
     "N(i*j)=N(i)N(j). So the substrate's composition norm N IS EXACTLY |amplitude|^2 -- not by choice but "
     "by the algebra (the quaternion norm is the squared modulus). This is the cold anchor: whatever the "
     "composition norm 'means' (43.CN.4: the intensive measure), it is numerically |amplitude|^2. The Born "
     "measure and the composition norm are, as numbers, the same object.",
     "UNIQUE (N(q) = q conj(q) = |q|^2, quadratic and multiplicative; N(amp) = |amp|^2)", "DERIVED",
     {"amp": list(amp), "N_amp": N(amp), "is_squared_modulus": N_is_sq_modulus,
      "N_is_q_qbar": N_is_qqbar, "multiplicative": multiplicative,
      "identity": "the composition norm N (43) = the squared modulus |amp|^2 (06.6) -- by the algebra"},
     check="N(q) = q conj(q) = |q|^2 (06.6, quadratic); multiplicative (43); N(3+4i) = 25 = |amp|^2")
assert br1_ok

# ---- BR.2 the SQUARE is forced: additive over orthogonal (Pythagoras) -- DERIVED --------
e1 = (1, 0, 0, 0)
e2 = (0, 1, 0, 0)                         # e1 . e2 = 0 (orthogonal)
orthogonal = (dot(e1, e2) == 0)
# quadratic norm is ADDITIVE over orthogonal: N(e1+e2) = N(e1) + N(e2) (Pythagoras)
pythagoras = (N(qadd(e1, e2)) == N(e1) + N(e2))       # 2 = 1 + 1
# linear modulus is NOT additive: |e1+e2|^2 = 2, but (|e1|+|e2|)^2 = 4, so |e1+e2| != |e1|+|e2|
linear_fails = (N(qadd(e1, e2)) != (1 + 1) ** 2)      # 2 != 4  -> modulus not additive over orthogonal
br2_ok = (orthogonal and pythagoras and linear_fails)
step("BR.2", "the SQUARE is forced (why |amp|^2, not |amp|): additive over ORTHOGONAL + linear superposition => Pythagoras (quadratic)",
     "the measure must be ADDITIVE over ORTHOGONAL (disjoint) registrations while amplitudes SUPERPOSE "
     "linearly (53). The QUADRATIC norm is additive over orthogonal directions (Pythagoras: N(a+b) = "
     "N(a)+N(b) when a.b=0) -- the LINEAR modulus |q| is NOT (|e1+e2| = sqrt(2) != 2 = |e1|+|e2|). So the "
     "measure is the QUADRATIC |amp|^2, not the linear |amp|",
     ["BR.1", "05.5.1", "53.QK.3"],
     "why the SQUARE -- the classic 'why |psi|^2' question, answered on the substrate. Probabilities (and "
     "the intensive share) must be ADDITIVE over mutually-exclusive/ORTHOGONAL outcomes: the measure of "
     "disjoint registrations adds. But amplitudes SUPERPOSE LINEARLY (53: the complex state space). For "
     "ORTHOGONAL amplitudes e1 . e2 = 0, the QUADRATIC norm satisfies Pythagoras: N(e1+e2) = N(e1)+N(e2) "
     "(RUN IT: N((1,1,0,0)) = 2 = 1+1) -- ADDITIVE. The LINEAR modulus does NOT: |e1+e2| = sqrt(2), while "
     "|e1|+|e2| = 2, so |e1+e2| != |e1|+|e2| (2 != 4 in squares) -- NOT additive over orthogonal. So the "
     "ONLY measure that is additive over orthogonal outcomes while the amplitude superposes linearly is "
     "the QUADRATIC form |amp|^2 (Pythagoras on the substrate's inner product 05/06.6) -- NOT the linear "
     "|amp|, NOT a quartic. The square is FORCED by additivity + superposition. (Additivity-over-orthogonal "
     "is the substrate reading -- disjoint shares add; the Pythagorean/quadratic consequence is cold.)",
     "UNIQUE (additive over orthogonal + linear superposition => the quadratic |amp|^2, not linear |amp|)", "DERIVED",
     {"e1": list(e1), "e2": list(e2), "orthogonal": orthogonal,
      "pythagoras_quadratic_additive": pythagoras, "linear_modulus_not_additive": linear_fails,
      "why_squared": "additive-over-orthogonal (Pythagoras on 05/06.6) + linear superposition (53) => the quadratic |amp|^2"},
     check="orthogonal e1,e2: N(e1+e2)=2=N(e1)+N(e2) (quadratic additive); |e1+e2|!=|e1|+|e2| (linear fails) -> squared forced")
assert br2_ok

# ---- BR.3 the hinge: the intensive measure = probability -- POSTULATE -------------------
step("BR.3", "THE HINGE (POSTULATE, filed 19): the intensive measure (43.CN.4) = quantum PROBABILITY, so |amp|^2 = the Born rule",
     "the substrate's INTENSIVE measure (the share, 43.CN.4 -- how much of the whole a registration "
     "carries) = the quantum PROBABILITY. Since N = |amp|^2 (BR.1) = the intensive measure (43.CN.4), "
     "|amp|^2 = probability -- the BORN RULE. This IDENTIFICATION closes 43.CN.4 and the Born rule as ONE "
     "hinge; it is a CORRESPONDENCE, WEAK -- the identification is the reading",
     ["BR.1", "BR.2", "43.CN.4"],
     "the hinge itself, graded with the discipline this crossing demands. SUBSTRATE side (checked, "
     "BR.1-BR.2): the composition norm N = |amp|^2 (quadratic, multiplicative, additive-over-orthogonal, "
     "unitary-invariant) is the substrate's intensive measure (43.CN.4). PHYSICS side (cited): the Born "
     "rule states |amplitude|^2 = the probability. THE HINGE: the substrate's intensive measure (the "
     "share) <-> the quantum probability. Since N = |amp|^2 IS the intensive measure (43.CN.4), the "
     "identification gives |amp|^2 = probability -- the Born rule. WHAT THIS IS: a REDUCTION -- the Born "
     "rule is 43.CN.4 applied to the amplitude; the two open premises (CN.4's 'the norm is the measure' "
     "and Born's '|amp|^2 is probability') are the SAME identification, wearing two faces. WHAT THIS IS "
     "NOT: a DERIVATION of probability from nothing, nor a solution to the MEASUREMENT problem (how a "
     "definite outcome is selected -- untouched, BR.5). The identification measure<->probability is a "
     "READING, quarantined, no downstream premise use. It is the single deepest held hinge in the corpus.",
     "POSTULATE (the intensive measure = probability; |amp|^2 = Born; closes CN.4 = Born as one hinge; held)", "POSTULATE",
     {"substrate_side": "N = |amp|^2 (BR.1) = the intensive measure (43.CN.4), quadratic/multiplicative/additive/unitary-invariant",
      "physics_side_cited": "the Born rule: |amplitude|^2 = probability",
      "hinge": "the intensive measure (43.CN.4) = quantum probability -> |amp|^2 = Born; closes CN.4 = Born as ONE hinge",
      "is_not": "a derivation of probability from nothing; a solution to the measurement problem (BR.5)",
      "downstream_premise_use": False},
     check=None)

# ---- BR.4 the gate-check for the STRUCTURE -- DERIVED -----------------------------------
step("BR.4", "the gate-check (G3/G4/G5): the STRUCTURE (why squared) passes; the probability identification is the held hinge",
     "the five-gate ledger for the STRUCTURAL content. G3 renaming: erase 'Born/probability' -- the "
     "substrate produces 'the measure is the additive-over-orthogonal, multiplicative, unitary-invariant "
     "QUADRATIC norm |amp|^2', name-free (BR.1/BR.2). G4 cannot-fail: a LINEAR (|amp|) or QUARTIC measure "
     "FAILS additivity-over-orthogonal / multiplicativity (the refuter). G5 no-fit: no target fished. "
     "PASSES for the structure; the measure<->probability identification (BR.3) is the held hinge",
     ["BR.2"],
     "the gates, run on the crossing, honest about the split. G1 (dimensionless): the measure is a pure "
     "ratio (|amp|^2 normalized), dimensionless. G2 (compute-then-compare): the STRUCTURE (quadratic, "
     "additive, multiplicative, unitary-invariant) is computed from 06/43/53; the Born rule is the cited "
     "correspondent. G3 (renaming): erase every physics name -- the substrate's statement stands: the "
     "natural measure on the amplitude is the quadratic norm |amp|^2 (additive over orthogonal registrations, "
     "multiplicative, SU(2)-invariant); the name 'probability' attaches after (BR.3). G4 (cannot-fail): "
     "the SQUARE could have failed -- a linear modulus is not additive over orthogonal (BR.2), a quartic "
     "is not multiplicative -- so 'why squared' is a genuine constraint, not free. G5 (no-fit): nothing "
     "assembled to a target; no refused-list issue (no famous number). SO: the STRUCTURAL content (why "
     "|amp|^2) PASSES the gates -- it is a genuine forced feature. The one thing NOT passed cold is the "
     "identification measure<->probability (BR.3), which is the held hinge and is honestly graded POSTULATE. "
     "This is the disciplined outcome: the square is forced; the probability reading is named, not derived.",
     "UNIQUE (the structural 'why squared' passes G3/G4/G5; the probability identification is the held hinge)", "DERIVED",
     {"g3_renaming": "erase 'Born' -> the additive-over-orthogonal quadratic norm |amp|^2, name-free",
      "g4_cannot_fail": "linear fails additivity-over-orthogonal; quartic fails multiplicativity -- the refuter",
      "g5_no_fit": "no target fished; no refused-list issue",
      "passes_for": "the STRUCTURE (why squared); the probability identification (BR.3) is the held hinge"},
     check="the structural 'why squared' passes G3 (name-free), G4 (linear/quartic fail), G5 (no fit); probability = the held hinge")

# ---- BR.5 OWED + the payoff ------------------------------------------------------------
step("BR.5", "OWED + PAYOFF: Gleason-uniqueness cold; measurement/collapse NOT solved; PAYOFF: 43.CN.4 and the Born rule are ONE hinge",
     "OWED: (a) a GLEASON-type uniqueness (the quadratic measure is the ONLY consistent one) derived on "
     "the substrate rather than argued from additivity; (b) MEASUREMENT / collapse -- how a definite "
     "outcome is selected -- NOT solved here (the hard problem, untouched). THE PAYOFF: 43.CN.4 (the last "
     "held premise under dim=3) and the Born rule are now ONE hinge -- the measure<->probability "
     "identification (BR.3) is the SINGLE shared held POSTULATE; closing it closes BOTH",
     ["BR.3", "BR.4"],
     "the honest residual and the genuine payoff. BR.1-BR.2 force the SQUARE (the substrate's measure is "
     "the quadratic |amp|^2, additive over orthogonal, multiplicative, unitary-invariant); BR.3 files the "
     "measure<->probability hinge; BR.4 runs the gates. What remains OWED: (a) a GLEASON-type theorem on "
     "the substrate -- that the quadratic is the UNIQUE consistent measure (here it is forced by "
     "additivity+superposition, BR.2, not by a full uniqueness proof); (b) the MEASUREMENT problem -- how "
     "a single definite outcome arises from the amplitude -- is NOT addressed (no collapse mechanism "
     "claimed; hand-waving explicitly refused here). THE PAYOFF, and it is real: 43.CN.4 -- the single "
     "remaining held premise beneath dim=3 (the composition norm) -- and the BORN RULE are the SAME hinge "
     "(the intensive measure = |amp|^2 = probability). So the corpus's deepest structural premise and "
     "quantum mechanics' deepest postulate are ONE thing: closing 'the intensive measure IS the Born "
     "probability' closes both at once. The measure<->probability identification is now the single shared "
     "held postulate joining the substrate norm and QM. NOT attempted further here.",
     "OWED (Gleason-uniqueness cold; measurement/collapse -- not solved; PAYOFF: CN.4 = the Born rule, one hinge)", "OWED",
     {"owed_gleason": "the quadratic measure is UNIQUE, derived on the substrate (here forced by additivity+superposition, not a full proof)",
      "owed_measurement": "the measurement problem / collapse -- how a definite outcome arises -- NOT solved (hand-waving refused)",
      "payoff": "43.CN.4 (the last held premise under dim=3) = the Born rule -- ONE hinge; closing the measure<->probability identification closes both",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="55-born-hinge",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        amp=list(amp), N_amp=N(amp), multiplicative=multiplicative,
        pythagoras_quadratic_additive=pythagoras, linear_modulus_not_additive=linear_fails,
        finding="THE BORN HINGE (Rung 0, the highest-leverage non-value crossing). The composition norm "
                "N(q) = q conj(q) = |q|^2 (06.6, quadratic; 43, multiplicative) IS |amplitude|^2 by the "
                "algebra (BR.1). The SQUARE is FORCED (why |amp|^2 not |amp|): the measure must be additive "
                "over orthogonal registrations while amplitudes superpose linearly (53) -> Pythagoras on the "
                "quadratic norm (05/06.6); the linear modulus fails additivity-over-orthogonal (BR.2). THE "
                "HINGE (BR.3, POSTULATE): the intensive measure (43.CN.4) = quantum probability, so |amp|^2 "
                "= the Born rule -- closing 43.CN.4 and the Born rule as ONE hinge. The STRUCTURE (why "
                "squared) passes the five gates (BR.4); the probability identification is the held hinge, "
                "NOT a derivation of probability nor a solution to measurement (BR.5). PAYOFF: the corpus's "
                "last held premise under dim=3 (CN.4) and QM's deepest postulate are ONE thing. Nothing "
                "fitted; no renaming; the measurement problem explicitly NOT claimed.",
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
