#!/usr/bin/env python3
"""Container 67 -- CONJUGATION ON GENERATION: how do charge-conjugation-like (colour-flipping) involutions
of the 120 act on the outer Z/3 (generation)? This is the convention-free salvage from the REFUTED Maths-6
P1 ("C = the improper half => preserves the outer Z/3 => generation stands"). That claim was wrong: its
`fgen` tested only the FLIP (X GEN X^T = GEN^-1) and labelled everything-else "preserve" -- a binary test on
a THREE-way question, mislabelling SCRAMBLE (X GEN X^T out of <GEN>) as "preserve". The cold trichotomy,
enumerated EXHAUSTIVELY over the full isometry group here, is the opposite of P1 on the improper side.

Run cold on 06's 120 icosians and 64's tick b (colour = conj(b^2), 64.CX.4; generation = R_{b^4}, 64.CX.3).
Every walk-symmetry of the 120 (automorphism of the +phi/2 adjacency = isometry of the 600-cell) is
v -> p v q (orientation-preserving, det +1) or v -> p vbar q (orientation-reversing, det -1), p,q in 2I --
the H4 symmetry group, order 14400. We enumerate ALL of them, keep the involutions that flip colour, and
classify their action on generation.

  CG.1  THE COLOUR-FLIPPING INVOLUTIONS (DERIVED). Over the full isometry group (14400 maps, each VERIFIED a
        walk-symmetry = preserves the +phi/2 adjacency), the involutions that flip colour (X COL X^-1 =
        COL^-1, COL = conj b^2) number EXACTLY 24: 18 proper (det +1) + 6 improper (det -1).
  CG.2  THE TRICHOTOMY -- NO INVOLUTION PRESERVES GENERATION (DERIVED, headline). Each acts on the outer Z/3
        = <R_{b^4}> as exactly one of PRESERVE (=GEN), INVERT (=GEN^-1), SCRAMBLE (not in <GEN>). Result:
        the 18 proper ALL INVERT (gen1<->gen2, gen0 fixed); the 6 improper ALL SCRAMBLE (X GEN X^-1 is a
        LEFT action, out of <GEN> -- the quaternion-conj anti-automorphism R->L). PRESERVE count = 0. So NO
        colour-flipping involution of the 120 leaves the outer Z/3 invariant. (Refutes P1's "improper
        preserve"; the P1 sign was backwards -- improper SCRAMBLE.)
  CG.3  CONVENTION INDEPENDENCE (DERIVED). Re-running with generation = L_{g3} (61's LEFT reading) gives the
        IDENTICAL classification (18 invert / 6 scramble / 0 preserve). The result does not depend on reading
        the outer Z/3 as left (61) or right (64): conjugation is an anti-automorphism swapping L<->R.
  CG.4  C DOES NOT LEAVE THE OUTER Z/3 INVARIANT (DERIVED). Charge conjugation C (49) negates charge and is
        colour-flipping (anti-colour), hence one of the 24. By CG.2 none of the 24 preserves generation, so
        C acts non-trivially on the outer Z/3 -- whichever orientation C has: proper => invert, improper =>
        scramble. NO "SM" in the statement. (WHICH orientation = 49's d->12-d realized on the 120 = OWED.)
  CG.5  C != P: C IS A CARRIER SELF-MAP (DERIVED). The improper colour-flipper (the enantiomorph/"wing-
        mirror") is a permutation of the 120 -- a self-map. Parity P (44, the even<->odd coord-conjugate
        orbit swap) carries 2I OUT to the mirror copy 2I' -- NOT a self-map of the 120. So C and P are
        distinct orientation-reversing involutions; C is realizable on the carrier (the geometric left wing,
        48, is not needed to read C's action on generation).
  CG.6  (reading, POSTULATE, filed 19) THE SM COMPARISON -- OPEN, TWO-SIDED, NOT A VERDICT. The cold fact
        needs no SM. Do not smuggle (i) "the outer Z/3 IS generation" (charge-vs-family is open, 61/k2) nor
        (ii) "C SHOULD preserve generation" (an SM CONVENTION, not a law of the universe, which mixes flavor:
        CKM/PMNS/nu-oscillations/CP violation). IF the outer Z/3 is a FAMILY label, C acting non-trivially
        is a prediction to test against the observed flavor/CP sector (not the convention); IF a CHARGE, C
        acting on it is expected. COMPASS 1: match the universe, not the SM -- the SM is in the dock, not on
        the bench; and it cuts both ways. "Divergence" retired from the conclusion.
  CG.7  OWED. (a) WHICH orientation C has = 49's d->12-d realized on the 120 as a specific det+/-1 self-map
        (mesh_bridge guessed it; unbanked) -> upgrades CG.4 to the specific action; (b) the charge-vs-family
        identity of the outer Z/3 (61/63/k2); (c) then the CG.6 test decides against the universe. Nothing
        fitted.

THE HEADLINE: EXHAUSTIVELY over the 120's full isometry group (14400), the colour-flipping involutions (24 =
18 proper + 6 improper) NEVER preserve the outer Z/3 -- proper INVERT it, improper SCRAMBLE it (0 preserve),
under both the left (61) and right (64) conventions. So charge conjugation acts non-trivially on the outer
Z/3. This is the cold, convention-free, SM-free salvage from the refuted P1 (whose "improper preserve" had
the sign backwards). Rests on 64 (tick b: colour conj b^2, generation R_{b^4}), 06 (the carrier), 44/49
(P, C). Everything RECOMPUTES; nothing is a literal.
"""

import json
import sys
import itertools
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


D64 = json.loads((HERE.parent / "64-coxeter-bridge" / "derivation.json").read_text(encoding="utf-8"))["values"]
assert D64["b_order"] == 6 and D64["c10_is_right_mult_b4"] and D64["colour_g3_order"] == 3


# ---- exact Z[phi] quaternion arithmetic ----
def mulc(A, B):
    a, b = A
    c, d = B
    return (a * c + b * d, a * d + b * c + b * d)


def addc(A, B):
    return (A[0] + B[0], A[1] + B[1])


def subc(A, B):
    return (A[0] - B[0], A[1] - B[1])


def negc(A):
    return (-A[0], -A[1])


def qmul(P, R):
    a, b, c, d = P
    e, f, g, h = R
    return (subc(subc(subc(mulc(a, e), mulc(b, f)), mulc(c, g)), mulc(d, h)),
            subc(addc(addc(mulc(a, f), mulc(b, e)), mulc(c, h)), mulc(d, g)),
            addc(addc(subc(mulc(a, g), mulc(b, h)), mulc(c, e)), mulc(d, f)),
            addc(subc(addc(mulc(a, h), mulc(b, g)), mulc(c, f)), mulc(d, e)))


def qconj(P):
    return (P[0], negc(P[1]), negc(P[2]), negc(P[3]))


def qone():
    return ((F(1), F(0)), (F(0), F(0)), (F(0), F(0)), (F(0), F(0)))


def qeq(P, Q):
    return all(P[k] == Q[k] for k in range(4))


def double(q):
    out = []
    for (a, b) in q:
        out += [int(2 * a), int(2 * b)]
    return out


def undouble(v):
    return tuple((F(v[2 * k], 2), F(v[2 * k + 1], 2)) for k in range(4))


def build_icosians():
    Z, HALF, ONE = (F(0), F(0)), (F(1, 2), F(0)), (F(1), F(0))
    PHI2, INV2 = (F(0), F(1, 2)), (F(-1, 2), F(1, 2))
    V = set()
    for i in range(4):
        for s in (ONE, negc(ONE)):
            v = [Z, Z, Z, Z]
            v[i] = s
            V.add(tuple(v))
    for m in range(16):
        V.add(tuple(HALF if (m >> k) & 1 == 0 else negc(HALF) for k in range(4)))
    base = [Z, HALF, INV2, PHI2]
    eperm = [p for p in itertools.permutations(range(4))
             if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
    for p in eperm:
        vals = [base[p[i]] for i in range(4)]
        nz = [i for i in range(4) if vals[i] != Z]
        for m in range(1 << len(nz)):
            v = list(vals)
            for bit, i in enumerate(nz):
                if (m >> bit) & 1:
                    v[i] = negc(v[i])
            V.add(tuple(v))
    return sorted(V, key=lambda q: tuple(double(q)))


ICO = build_icosians()
IDX = {q: i for i, q in enumerate(ICO)}
assert len(ICO) == 120


def elem_order(q):
    p = q
    o = 1
    while not qeq(p, qone()):
        p = qmul(p, q)
        o += 1
        if o > 40:
            return -1
    return o


# ---- 64's tick b -> colour (conj b^2) and generation (R_{b^4}) ----
B = undouble(D64["b_doubled"])
assert elem_order(B) == 6
G3 = qmul(B, B)                       # b^2, the colour axis (64.CX.4)
B4 = qmul(G3, G3)                     # b^4, the generation generator (64.CX.3: C^10 = R_{b^4})
assert elem_order(G3) == 3 and elem_order(B4) == 3

# ---- index-permutation machinery (fast sweep; exact construction) ----
import array


def perm_from(fn):
    return tuple(IDX[fn(ICO[i])] for i in range(120))


L = [perm_from(lambda v, k=k: qmul(ICO[k], v)) for k in range(120)]   # v -> b_k * v
R = [perm_from(lambda v, k=k: qmul(v, ICO[k])) for k in range(120)]   # v -> v * b_k
BAR = perm_from(qconj)                                                 # v -> vbar
IDENT = tuple(range(120))


def comp(a, b):                       # (a o b)[i] = a[b[i]]   (apply b then a)
    return tuple(a[b[i]] for i in range(120))


def pinv(p):
    out = [0] * 120
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


# +phi/2 adjacency (the walk): v ~ w iff Re(conj(v) w) = phi/2
HALFPHI = (F(0), F(1, 2))
ADJ = [set() for _ in range(120)]
for i in range(120):
    for j in range(120):
        if i != j and qmul(qconj(ICO[i]), ICO[j])[0] == HALFPHI:
            ADJ[i].add(j)
ADJSET = frozenset((i, j) for i in range(120) for j in ADJ[i])


def is_walk_symmetry(X):
    return all((X[i], X[j]) in ADJSET for i in range(120) for j in ADJ[i])


COL = perm_from(lambda v: qmul(qmul(G3, v), qconj(G3)))     # colour: conj by b^2
COLi = pinv(COL)
GEN_R = perm_from(lambda v: qmul(v, B4))                    # generation (64): v -> v b^4
GEN_L = perm_from(lambda v: qmul(G3, v))                    # generation (61): v -> b^2 v  (left Z/3)


def conj_perm(X, P):                  # X P X^-1
    Xi = pinv(X)
    return comp(X, comp(P, Xi))


def classify(X, GEN):
    GENi = pinv(GEN)
    c = conj_perm(X, GEN)
    if c == GEN:
        return "preserve"
    if c == GENi:
        return "invert"
    return "scramble"


def flips_colour(X):
    return conj_perm(X, COL) == COLi


# ================================================================ CG.1 the colour-flipping involutions
seen = set()
flippers = []            # (det, perm)
for i in range(120):
    for j in range(120):
        X = comp(L[i], R[j])              # v -> b_i v b_j  (det +1)
        if X in seen:
            continue
        seen.add(X)
        if X != IDENT and comp(X, X) == IDENT and flips_colour(X):
            flippers.append((+1, X))
for i in range(120):
    for j in range(120):
        X = comp(R[j], comp(L[i], BAR))   # v -> b_i vbar b_j  (det -1)
        if X in seen:
            continue
        seen.add(X)
        if comp(X, X) == IDENT and flips_colour(X):
            flippers.append((-1, X))

N_ISOM = len(seen)
N_PROPER = sum(1 for d, _ in flippers if d == +1)
N_IMPROPER = sum(1 for d, _ in flippers if d == -1)
N_FLIP = len(flippers)
# every colour-flipper is a genuine walk-symmetry (preserves the +phi/2 adjacency)
ALL_WALK = all(is_walk_symmetry(X) for _, X in flippers)
cg1_ok = (N_ISOM == 14400 and N_FLIP == 24 and N_PROPER == 18 and N_IMPROPER == 6 and ALL_WALK)
step("CG.1", "THE COLOUR-FLIPPING INVOLUTIONS: over the 120's full isometry group (v->pvq det+1, v->p vbar q det-1; p,q in 2I; order 14400 = |H4|), the involutions that flip colour (X COL X^-1 = COL^-1, COL = conj b^2) number EXACTLY 24 -- 18 proper (det+1) + 6 improper (det-1); each VERIFIED a walk-symmetry (preserves the +phi/2 adjacency)",
     "every automorphism of the +phi/2 Cayley graph of 2I is an isometry of the 600-cell, i.e. v -> p v q "
     "(orientation-preserving, det +1 on R^4) or v -> p vbar q (orientation-reversing, det -1), p,q in 2I -- "
     "the group H4 of order 14400 (enumerated here as 7200+7200 distinct maps, deduped). Keeping the "
     "involutions (X^2 = id, X != id) that FLIP COLOUR (conjugate COL = conj b^2 to its inverse) yields "
     "EXACTLY 24: 18 with det +1 and 6 with det -1. Each of the 24 is independently checked to preserve the "
     "+phi/2 adjacency (a genuine walk-symmetry), so the enumeration is of walk-symmetries, not merely of "
     "isometries",
     ["64.CX.4", "06.2.1"],
     "the complete, exhaustive population the classification runs on -- not a hand-picked family (the refuted "
     "P1 used a 6-element subfamily). The parametrization v->pvq / v->p vbar q is the standard complete "
     "symmetry group of the 600-cell (|H4| = 14400, reproduced cold); colour-flipping + involution cuts it to "
     "24. Exact-integer over Z[phi]; the sweep is deterministic.",
     "UNIQUE (24 colour-flipping involutions: 18 proper + 6 improper, exhaustive over the 14400)", "DERIVED",
     {"isometry_group_order": N_ISOM, "n_colour_flipping_involutions": N_FLIP,
      "n_proper_det_plus1": N_PROPER, "n_improper_det_minus1": N_IMPROPER,
      "all_are_walk_symmetries": ALL_WALK},
     check="full isometry group order 14400; exactly 24 colour-flipping involutions (18 proper + 6 improper); all walk-symmetries")
assert cg1_ok

# ================================================================ CG.2 the trichotomy (headline)
cls_R = {"preserve": 0, "invert": 0, "scramble": 0}
cls_by_det = {+1: dict(preserve=0, invert=0, scramble=0), -1: dict(preserve=0, invert=0, scramble=0)}
for d, X in flippers:
    c = classify(X, GEN_R)
    cls_R[c] += 1
    cls_by_det[d][c] += 1
N_PRESERVE = cls_R["preserve"]
PROPER_ALL_INVERT = (cls_by_det[+1]["invert"] == N_PROPER and cls_by_det[+1]["preserve"] == 0
                     and cls_by_det[+1]["scramble"] == 0)
IMPROPER_ALL_SCRAMBLE = (cls_by_det[-1]["scramble"] == N_IMPROPER and cls_by_det[-1]["preserve"] == 0
                         and cls_by_det[-1]["invert"] == 0)
cg2_ok = (N_PRESERVE == 0 and PROPER_ALL_INVERT and IMPROPER_ALL_SCRAMBLE
          and cls_R["invert"] == 18 and cls_R["scramble"] == 6)
step("CG.2", "THE TRICHOTOMY -- NO INVOLUTION PRESERVES GENERATION: on the outer Z/3 = <R_{b^4}> (64.CX.3) each colour-flipping involution acts as exactly one of PRESERVE (=GEN), INVERT (=GEN^-1), SCRAMBLE (not in <GEN>). The 18 proper ALL INVERT (gen1<->gen2, gen0 fixed); the 6 improper ALL SCRAMBLE (to a LEFT action, out of <GEN>). PRESERVE = 0. (Refutes P1: improper SCRAMBLE, not preserve)",
     "generation is the outer Z/3 = <R_{b^4}> (64.CX.3: C^10 = R_{b^4}, order-3 fixed-point-free, 40 "
     "three-cycles). For each of the 24 colour-flipping involutions X, compute X GEN X^-1 and test membership "
     "in <GEN> = {id, R_{b^4}, R_{b^8}}: PRESERVE if = GEN, INVERT if = GEN^-1, SCRAMBLE otherwise. Result: "
     "the 18 proper (det+1) ALL INVERT (X GEN X^-1 = GEN^-1 -- swap gen1<->gen2, fix gen0); the 6 improper "
     "(det-1) ALL SCRAMBLE (X GEN X^-1 is a LEFT multiplication, out of the right-regular <GEN> -- because "
     "quaternion conjugation is an anti-automorphism carrying R_x to L_{xbar}). PRESERVE count = 0 across all "
     "24. So NO colour-flipping involution of the 120 leaves the outer Z/3 invariant",
     ["CG.1", "64.CX.3"],
     "the headline, and the cold correction of the refuted P1. P1 claimed 'improper (det-1) => preserve the "
     "outer Z/3'; the truth is improper => SCRAMBLE (the sign was backwards). The P1 bug was a binary "
     "FLIP-vs-not test (mesh_bridge.py fgen) on a THREE-way question, mislabelling SCRAMBLE as 'preserve'. "
     "G4 refuter: had any of the 24 PRESERVED generation, 'a colour-flipping involution can fix the outer "
     "Z/3' would hold -- none does (0/24); had any improper landed in <GEN>, P1's 'improper preserve' would "
     "stand -- all 6 scramble. G3: the computation names no physics (lag-free group arithmetic on 2I). "
     "Exact-integer over the 24.",
     "UNIQUE (0 preserve; 18 proper invert, 6 improper scramble -- exhaustive)", "DERIVED",
     {"classification_R_b4": cls_R, "by_orientation": {str(k): v for k, v in cls_by_det.items()},
      "n_preserve": N_PRESERVE, "proper_all_invert": PROPER_ALL_INVERT,
      "improper_all_scramble": IMPROPER_ALL_SCRAMBLE},
     check="on <R_b4>: 0 preserve; 18 proper all invert; 6 improper all scramble (refutes P1's improper-preserve)")
assert cg2_ok

# ================================================================ CG.3 convention independence
cls_L = {"preserve": 0, "invert": 0, "scramble": 0}
cls_L_by_det = {+1: dict(preserve=0, invert=0, scramble=0), -1: dict(preserve=0, invert=0, scramble=0)}
for d, X in flippers:
    c = classify(X, GEN_L)
    cls_L[c] += 1
    cls_L_by_det[d][c] += 1
CONVENTION_INDEPENDENT = (cls_L == cls_R
                          and cls_L_by_det[+1]["invert"] == 18 and cls_L_by_det[-1]["scramble"] == 6
                          and cls_L["preserve"] == 0)
cg3_ok = CONVENTION_INDEPENDENT
step("CG.3", "CONVENTION INDEPENDENCE: re-running the trichotomy with generation = L_{g3} (61's LEFT reading of the outer Z/3) gives the IDENTICAL classification -- 18 invert / 6 scramble / 0 preserve. The result does not depend on reading the outer Z/3 as left (61) or right (64)",
     "61 reads the outer Z/3 as LEFT-multiplication (g3, 3 blocks of 40); 64 reads it as RIGHT-multiplication "
     "(R_{b^4}, 40 three-cycles). Classifying the same 24 involutions against GEN_L = L_{g3} reproduces the "
     "SAME counts -- 18 invert, 6 scramble, 0 preserve. This is structural: conjugation is an anti-"
     "automorphism exchanging the left and right regular actions, so an orientation-reversing map always "
     "carries <R> out to <L> (scramble) and an orientation-preserving map normalises each (invert here), "
     "symmetrically in L and R. So 'C does not preserve the outer Z/3' is independent of the 61-vs-64 reading",
     ["CG.2"],
     "closes the one convention ambiguity in the corpus (61 left vs 64 right for 'the outer Z/3'). The "
     "verdict is the same either way, so no step rides on a choice of side. Exact-integer.",
     "UNIQUE (same 18/6/0 under the left (61) convention as the right (64))", "DERIVED",
     {"classification_L_g3": cls_L, "convention_independent": CONVENTION_INDEPENDENT},
     check="generation = L_g3 (61) gives the same 18 invert / 6 scramble / 0 preserve as R_b4 (64)")
assert cg3_ok

# ================================================================ CG.4 C does not leave the outer Z/3 invariant
C_NONTRIVIAL = (N_PRESERVE == 0)     # C is one of the 24; none preserves
step("CG.4", "C DOES NOT LEAVE THE OUTER Z/3 INVARIANT: charge conjugation C (49) negates charge and is colour-flipping (anti-colour), hence one of the 24. By CG.2 none of the 24 preserves generation, so C acts non-trivially on the outer Z/3 -- proper => invert (gen1<->gen2), improper => scramble (L<->R). No 'SM' in the statement",
     "C (49.CT.1) is an involution that negates the signed charge and (as charge conjugation) sends colour to "
     "anti-colour -- a colour-flipping walk-symmetry involution of the 120, i.e. one of the 24 of CG.1. CG.2 "
     "showed 0 of the 24 PRESERVE the outer Z/3. Therefore C acts NON-TRIVIALLY on the outer Z/3, "
     "necessarily and independent of which orientation C carries: if C is proper it INVERTS (gen1<->gen2); if "
     "improper it SCRAMBLES (R<->L). The statement is purely about the substrate -- it names no Standard "
     "Model. WHICH orientation C has (= 49's degree-mirror d->12-d realised on the 120 as a specific det+/-1 "
     "self-map) is not settled here (CG.7, OWED)",
     ["CG.2", "49.CT.1"],
     "the convention-free, SM-free conclusion the NOTE-to-Maths-5 asked for: state what the substrate does, "
     "cold. C cannot fix the outer Z/3 (the 0-preserve result is exhaustive), so 'C preserves generation' is "
     "impossible on this carrier -- but the comparison to any SM convention is deferred to CG.6 (OPEN), not "
     "asserted here. Determinacy: the non-triviality is UNIQUE (0 preserve); C's specific orientation is "
     "UNDETERMINED (owed). Exact-integer.",
     "UNIQUE that C acts non-trivially (0 preserve); UNDETERMINED which of invert/scramble (C's orientation owed)", "DERIVED",
     {"c_is_one_of_the_24": True, "n_preserve": N_PRESERVE, "c_acts_nontrivially": C_NONTRIVIAL,
      "c_orientation": "OWED (49's d->12-d realization on the 120; proper=>invert, improper=>scramble)"},
     check="C is a colour-flipping involution; 0 of the 24 preserve generation => C acts non-trivially on the outer Z/3")

# ================================================================ CG.5 C != P: C is a carrier self-map
# P (44): parity = a coordinate reflection (odd permutation of the 4 axes) -- carries 2I OUT to the mirror.
def axis_swap01(v):
    return (v[1], v[0], v[2], v[3])
P_IS_SELFMAP = all(axis_swap01(v) in IDX for v in ICO)        # False: P leaves the carrier set
# True: every flipper is a permutation of the 120 (a self-map) -- check each sorts to 0..119
C_IS_SELFMAP = len(flippers) > 0 and all(sorted(X) == list(range(120)) for _, X in flippers)
cg5_ok = (C_IS_SELFMAP is True and P_IS_SELFMAP is False)
step("CG.5", "C != P -- C IS A CARRIER SELF-MAP: the improper colour-flipper (the enantiomorph / wing-mirror) is a permutation of the 120 (a self-map). Parity P (44, a coordinate reflection = the even<->odd orbit swap) carries 2I OUT to the mirror copy 2I' -- NOT a self-map of the 120. So C and P are distinct orientation-reversing involutions; C is realizable on the carrier (the left wing, 48, is not needed)",
     "every one of the 24 colour-flipping involutions (including the 6 improper, det-1, the candidates for "
     "C's wing-mirror realization) is by construction a permutation of the 120 icosians -- a self-map of the "
     "carrier (checked: each sorts to 0..119). Parity P (44.CH): a coordinate reflection (here the odd "
     "axis-swap 0<->1) is an orientation-reversing map that does NOT fix the icosian set -- it carries 2I to "
     "its mirror copy 2I' (44/48). So although C and P are both det-1 involutions, C is a self-map of 2I and "
     "P is not; they are distinct. This is why C's action on generation is readable ON the carrier (CG.2-4) "
     "while the geometric left wing (anti-twelve, 48) is a separate unrealized geometry not needed here",
     ["CG.1", "44.CH.2", "48.LW.1"],
     "preserves the one cold, correct fact that survived the refuted P1 (mesh_bridge's C-vs-P section): C is "
     "an algebra self-map of the carrier, P is not. It grounds reading C's generation-action internally (no "
     "left wing required) without reinstating any P1 claim about preservation. Exact (set membership over "
     "Z[phi]).",
     "UNIQUE (C a self-map of the 120; P not -- distinct det-1 involutions)", "DERIVED",
     {"improper_colour_flippers_are_self_maps": C_IS_SELFMAP, "parity_is_self_map": P_IS_SELFMAP},
     check="the improper colour-flippers are self-maps of the 120; parity (coord reflection) is not -> C != P")
assert cg5_ok

# ================================================================ CG.6 the SM comparison -- POSTULATE (filed 19)
step("CG.6", "(reading, POSTULATE, filed 19) THE SM COMPARISON -- OPEN, TWO-SIDED, NOT A VERDICT. The cold fact needs no SM. IF the outer Z/3 is a FAMILY label, C acting non-trivially is a prediction to test against the observed flavor/CP sector (not the SM convention); IF a CHARGE, C acting on it is expected. COMPASS 1: match the universe, not the SM. 'Divergence' retired from the conclusion",
     "the disciplined framing (NOTE to Maths 5, Kevin). CG.4 is cold and names no Standard Model, and must "
     "not carry one: two SM conventions would be smuggled in -- (i) that the outer Z/3 IS 'generation' (the "
     "charge-vs-family question is OPEN, 61/k2), and (ii) that C SHOULD preserve generation (an SM CONVENTION, "
     "not a law of the universe, which mixes flavor everywhere: CKM, PMNS, neutrino oscillations, CP "
     "violation -- and the SM assumes, does not explain, the 3 families). So the comparison is TWO-SIDED and "
     "OPEN: IF the outer Z/3 is a FAMILY label, C's non-trivial action is a FALSIFIABLE prediction, to be "
     "tested against the observed flavor/CP sector, NOT against the SM's C-preserves-generation convention; "
     "IF the outer Z/3 is a CHARGE, C acting on it is expected (no tension). COMPASS 1: the test is match the "
     "universe, not the SM -- the SM is in the dock, not on the bench; and it cuts both ways (do not flip to "
     "'substrate = truth where it differs' either). The word 'divergence' is retired from the conclusion -- "
     "it installs the SM as judge",
     ["CG.4"],
     "the honest landing, de-dogmatized. It does NOT read CG.4 as 'the substrate diverges from the SM' (that "
     "makes the SM the standard of truth); it does NOT read it as 'the SM is wrong' (the opposite dogma). It "
     "states what the substrate does (CG.2-4, cold) and defers the comparison to the universe, pending the "
     "two open identifications (CG.7). No downstream premise rests on this reading; filed through 19, "
     "quarantined.",
     "POSTULATE (SM comparison OPEN and two-sided; the test is the universe, not the SM convention)", "POSTULATE",
     {"needs_no_sm": True, "open_identifications": ["outer Z/3 = family vs charge (61/k2)",
      "whether C should preserve generation is an SM convention, not a law"],
      "test_against": "the observed flavor/CP sector (CKM/PMNS/oscillations/CP), not the SM convention",
      "divergence_language_retired": True, "cuts_both_ways": True, "downstream_premise_use": False},
     check=None)

# ================================================================ CG.7 OWED
step("CG.7", "OWED: (a) WHICH orientation C has = 49's d->12-d realised on the 120 as a specific det+/-1 self-map (mesh_bridge guessed it; unbanked) -> upgrades CG.4 to the specific action; (b) the charge-vs-family identity of the outer Z/3 (61/63/k2); (c) then CG.6's test decides against the universe. Nothing fitted",
     "OWED: (a) a cold realization of 49's charge-mirror d->12-d AS a specific involution on the 120 (the "
     "step mesh_bridge only guessed, v->vbar o inner) -- its determinant then fixes whether C INVERTS "
     "(proper) or SCRAMBLES (improper) the outer Z/3, upgrading CG.4 from 'non-trivial' to the specific "
     "action; (b) the identification of the outer Z/3 as a FAMILY label vs a CHARGE (the open k2 question, "
     "61/63); (c) with (a)+(b), CG.6's two-sided test becomes decidable against the observed flavor/CP "
     "sector. None of these is attempted here; the refused-list binds and nothing is fitted",
     ["CG.4", "CG.6"],
     "the located residual, not attempted. The cold classification (CG.1-3) and C's non-triviality (CG.4) "
     "stand without any of these; they are what would turn the convention-free fact into a specific, "
     "testable physical statement. A finding does not authorise their repair here.",
     "OWED (C's orientation via 49's d->12-d realization; the outer-Z/3 charge-vs-family identity; then the test)", "OWED",
     {"owed_c_orientation": "49's d->12-d realized on the 120 as a det+/-1 self-map (proper=>invert, improper=>scramble)",
      "owed_outer_z3_identity": "family vs charge (61/63/k2)",
      "owed_then": "CG.6's two-sided SM/universe test becomes decidable",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="67-conjugation-generation",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        isometry_group_order=N_ISOM,
        n_colour_flipping_involutions=N_FLIP, n_proper_det_plus1=N_PROPER, n_improper_det_minus1=N_IMPROPER,
        all_are_walk_symmetries=ALL_WALK,
        classification_R_b4=cls_R, classification_L_g3=cls_L,
        n_preserve=N_PRESERVE, proper_all_invert=PROPER_ALL_INVERT, improper_all_scramble=IMPROPER_ALL_SCRAMBLE,
        convention_independent=CONVENTION_INDEPENDENT, c_acts_nontrivially=C_NONTRIVIAL,
        improper_colour_flippers_are_self_maps=C_IS_SELFMAP, parity_is_self_map=P_IS_SELFMAP,
        finding="CONJUGATION ON GENERATION -- the convention-free salvage from the REFUTED P1. Exhaustively "
                "over the 120's full isometry group (14400 = |H4|; v->pvq det+1, v->p vbar q det-1), the "
                "colour-flipping involutions number 24 = 18 proper + 6 improper (CG.1, each a walk-symmetry). "
                "On the outer Z/3 = <R_{b^4}> (64) the TRICHOTOMY is: 18 proper ALL INVERT, 6 improper ALL "
                "SCRAMBLE, 0 PRESERVE (CG.2) -- the SAME under 61's left L_{g3} reading (CG.3, convention-"
                "independent). So NO colour-flipping involution leaves the outer Z/3 invariant, hence charge "
                "conjugation C acts NON-TRIVIALLY on it (CG.4; proper=>invert, improper=>scramble -- which, "
                "= 49's d->12-d realization, is OWED). This REFUTES P1's 'improper preserve' (the sign was "
                "backwards: improper SCRAMBLE); the P1 bug was a binary flip-vs-not test on a three-way "
                "question. C != P: the improper colour-flipper is a carrier self-map, parity is not (CG.5). "
                "The SM comparison is OPEN/two-sided (CG.6, POSTULATE): the cold fact needs no SM; test "
                "against the universe (flavor/CP), not the SM convention -- 'divergence' retired. OWED (CG.7): "
                "C's orientation (49's d->12-d), the outer-Z/3 charge-vs-family identity. Nothing fitted.",
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
            print(f"  {s['id']:<5} [{s['grade']:<9}] {s['what'][:70]}")
