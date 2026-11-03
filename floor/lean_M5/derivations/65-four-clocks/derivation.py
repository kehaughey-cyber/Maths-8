#!/usr/bin/env python3
"""Container 65 -- THE FOUR CLOCKS AND THE FRAME-ALIGNMENT RULE: the tick's four 30-loops on the 120 are
canonically the four quaternion axes {1,i,j,k} of the substrate's Galois-fixed canonical frame (Kevin: after
"look at the corpus again", the owed piece of 64.CX.7).

64 showed the tick C = L_a . R_b is the E8 Coxeter element (a unification, not a forcing) and that its
canonicity is NOT a conjugation question (all Coxeter elements are W-conjugate). The corpus's canonicalizer
is the CANONICAL QUATERNION FRAME (the Galois-fixed phi-free spine) + the PARITY BIT (CX.7, CORRECTIONS #12).
This container BUILDS that frame-alignment rule cold. Consumes 64's canonical tick (a, b), 06's carrier, 12's
roots; everything RECOMPUTES.

  FC.1  THE FOUR CLOCKS (DERIVED). The tick permutation tau(v) = a.v.b cuts the 120 icosians into EXACTLY
        4 orbits of 30 -- the "four H30 clocks" (CX.1; the corpus's four clocks / four 30-orbits).
  FC.2  THE CANONICAL FRAME (DERIVED). The Galois automorphism sigma (phi -> 1-phi, per-component
        (x,y)->(x+y,-y)) fixes EXACTLY the 24 phi-free Hurwitz units (= 2T); of these the 8 AXIS units
        {+-1,+-i,+-j,+-k} are the corpus's Q8 seam -- the canonical quaternion frame (4 antipodal pairs).
        (sigma is NOT a symmetry of this embedding -- it maps the other 96 icosians to the conjugate copy,
        62.ED.2/CORRECTIONS #5 -- so the frame is its FIXED spine, used as a fixed coordinate system, not
        sigma-as-a-map.)
  FC.3  THE FRAME-ALIGNMENT RULE (DERIVED, the headline). For the canonical tick, EACH clock owns EXACTLY
        ONE antipodal axis pair {+e,-e}: the 4 clocks are canonically labeled by the 4 quaternion axes
        {1,i,j,k}. The antipode C^15 = -I FIXES each clock (each clock is antipode-closed). And frame-
        alignment is a genuine SELECTOR, not a universal property: of the 480 order-5 x order-6 ticks
        EXACTLY 288 are frame-aligned (each clock one axis), with 6 distinct clock->axis labelings (the S3
        naming of {i,j,k}, the identity clock {+-1} fixed). So the frame CUTS 480 -> 288 -- a real reduction.
  FC.4  THE FOUR CLOCK-ORIGINS (DERIVED count / POSTULATE reading). 4 clocks x 30 = 120; one distinguished
        origin per clock gives 120 - 4 = 116 = 4 x 29 (the carrier minus its four clock-origins; each clock
        with 29 seats lagging behind one origin) -- the fork's native 116 that meters the neutron-proton
        splitting, now derived cold as a COUNT. WHICH seat is the origin (the + axis unit) is the parity-bit
        reading (the sign "set at the origin", the CPT chapter) -- POSTULATE, not forced.
  FC.5  (reading, POSTULATE, filed 19) THE VERDICT. The frame-alignment rule REDUCES the tick's canonicity:
        the substrate's canonical frame canonically labels the four clocks (for the 288 aligned ticks), a
        real cut 480 -> 288 -- the owed frame-alignment rule of 64.CX.7, now BUILT. But it is a REDUCTION,
        not yet a forcing: alignment + the fixed frame leave a residual (the 6 axis-labelings = naming
        {i,j,k}; 48 ticks per labeling), so a UNIQUE tick is not forced. The parity bit is the origin-sign
        (a free ZZ/2, which SHOULD be free -- P-violation). What would upgrade the reduction to a forcing:
        the arbiter's canonical seating (the fork's total-lean sign, the -93) re-derived at our standard,
        cutting 288 -> 1 up to parity. Does NOT touch the content map (K2, 63). The twin of 61/62/64's
        reductions, at the frame level.
  FC.6  OWED. The arbiter's canonical origin/lean (the fork's -93) re-derived cold -- would cut the residual
        288 to a unique tick up to parity (a forcing); and the K2 content selection (61/63). Nothing fitted;
        the refused-list binds (the fork's mass numbers, incl. the 116-metered n-p splitting, rest on this
        chain and stay CANDIDATE while K2 and the arbiter seating are owed).

THE HEADLINE: the owed "frame-alignment rule" of 64.CX.7 is BUILT. The tick's four 30-clocks are canonically
the four quaternion axes {1,i,j,k} of the Galois-fixed canonical frame -- each clock owns one antipodal axis
pair, the antipode fixes each clock -- and this frame-alignment is a genuine SELECTOR (288/480 ticks, 6
labelings), cutting the tick arbitrariness 480 -> 288. It derives the fork's 116 = 4x29 (four clock-origins)
cold. A REDUCTION toward canonicalizing the tick, not a forcing (a unique tick still needs the arbiter's
seating, owed); the residual parity bit is P-violation, which should be free. Rests on 64 (the tick), 06
(carrier + frame), 12 (roots). Everything RECOMPUTES; nothing is a literal.
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


# ================================================================ consume 06, 12, 64
CAR = json.loads((HERE.parent / "06-carrier-2i" / "derivation.json").read_text(encoding="utf-8"))
E8D = json.loads((HERE.parent / "12-e8-roots" / "derivation.json").read_text(encoding="utf-8"))
D64 = json.loads((HERE.parent / "64-coxeter-bridge" / "derivation.json").read_text(encoding="utf-8"))["values"]
BASIS = CAR["values"]["basis"]
assert D64["tick_order"] == 30 and D64["is_phi30"] is True   # the canonical tick from 64


# ================================================================ exact Z[phi] quaternion arithmetic
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


def qneg(P):
    return tuple(negc(c) for c in P)


def qone():
    return ((F(1), F(0)), (F(0), F(0)), (F(0), F(0)), (F(0), F(0)))


def qeq(P, Q):
    return all(P[k] == Q[k] for k in range(4))


def galois(q):                                       # field automorphism phi->1-phi: (a,b)->(a+b,-b)
    return tuple((a + b, -b) for (a, b) in q)


def undouble(v):
    return tuple((F(v[2 * k], 2), F(v[2 * k + 1], 2)) for k in range(4))


def double(q):
    out = []
    for (a, b) in q:
        out += [int(2 * a), int(2 * b)]
    return out


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


A_ELT = undouble(D64["a_doubled"])                   # THE canonical tick's generators (from 64)
B_ELT = undouble(D64["b_doubled"])
assert elem_order(A_ELT) == 5 and elem_order(B_ELT) == 6


def clocks_of(a, b):                                 # orbits of tau(v)=a.v.b on the 120
    seen, cl = set(), []
    for v in ICO:
        if v in seen:
            continue
        orb, x = [v], qmul(qmul(a, v), b)
        while not qeq(x, v):
            orb.append(x)
            x = qmul(qmul(a, x), b)
        seen |= set(orb)
        cl.append(orb)
    return cl


# ================================================================ FC.1 the four clocks
CLOCKS = clocks_of(A_ELT, B_ELT)
CLOCK_SIZES = sorted(len(c) for c in CLOCKS)
fc1_ok = (len(CLOCKS) == 4 and CLOCK_SIZES == [30, 30, 30, 30])
step("FC.1", "THE FOUR CLOCKS: the tick permutation tau(v)=a.v.b cuts the 120 icosians into EXACTLY 4 orbits of 30 -- the four H30 clocks (the corpus's four 30-orbits)",
     "the tick tau(v) = a.v.b (a order-5, b order-6, the canonical tick of 64) acts on the 120 icosians; its "
     "orbits are EXACTLY 4 cycles of length 30 (4*30 = 120). These are the corpus's 'four H30 clocks' (the "
     "order-30 beat in four 30-orbits). The tick's order is 30 (64.CX.1), and 120/30 = 4",
     ["64.CX.1", "06.6.5"],
     "the four clocks as first-class objects. 64 recorded that the tick cuts the 120 into 4 loops of 30 "
     "(the H4 Coxeter structure); this container makes those four clocks the object of study and asks how "
     "the canonical frame labels them. Exact-integer over Z[phi]; deterministic orbit computation.",
     "UNIQUE (4 clocks of 30, given the tick)", "DERIVED",
     {"n_clocks": len(CLOCKS), "clock_sizes": CLOCK_SIZES},
     check="the tick tau(v)=a.v.b cuts the 120 into exactly 4 orbits of 30 (the four clocks)")
assert fc1_ok

# ================================================================ FC.2 the canonical frame
GFIX = [q for q in ICO if galois(q) == q]
AXIS = [q for q in ICO if galois(q) == q and sum(1 for c in q if c != (F(0), F(0))) == 1]
N_HURWITZ, N_AXIS = len(GFIX), len(AXIS)
N_AXIS_PAIRS = N_AXIS // 2
fc2_ok = (N_HURWITZ == 24 and N_AXIS == 8 and N_AXIS_PAIRS == 4)
step("FC.2", "THE CANONICAL FRAME: the Galois automorphism sigma (phi->1-phi) fixes EXACTLY the 24 phi-free Hurwitz units (=2T); its 8 AXIS units {+-1,+-i,+-j,+-k} are the Q8 seam -- the canonical quaternion frame (4 antipodal pairs)",
     "the Galois automorphism sigma acts on each Z[phi] component by phi -> 1-phi, i.e. (a,b) -> (a+b,-b). "
     "Its FIXED icosians are exactly the 24 phi-free ones -- the Hurwitz units (= the binary tetrahedral "
     "group 2T). Of these, the 8 AXIS units (single nonzero component = +-1,+-i,+-j,+-k) are the corpus's Q8 "
     "seam -- the canonical quaternion frame, 4 antipodal pairs {+-1},{+-i},{+-j},{+-k}. sigma is NOT a "
     "symmetry of this embedding (it sends the other 96 icosians to the conjugate copy, 62.ED.2 / "
     "CORRECTIONS #5), so the frame is its FIXED spine -- a canonical coordinate system, not sigma-as-a-map",
     ["06.6.5"],
     "the substrate-native canonical frame, computed cold -- the structure CORRECTIONS #12 identified as the "
     "true canonicalizer (a fixed frame, NOT a conjugation-invariant, which by theorem cannot distinguish "
     "W-conjugate Coxeter elements). The corpus names it the 'canonical quaternion frame' (BeltComplete) / "
     "the 'sigma-fixed spine' (the silicon project); here it is the Galois-fixed locus, 24 Hurwitz units of "
     "which 8 are the axis frame. Exact-integer.",
     "UNIQUE (the Galois-fixed spine: 24 Hurwitz, 8 axis units, 4 pairs)", "DERIVED",
     {"n_galois_fixed": N_HURWITZ, "n_axis_units": N_AXIS, "n_axis_pairs": N_AXIS_PAIRS,
      "note": "the 8 axis units {+-1,+-i,+-j,+-k} = the Q8 seam = the canonical quaternion frame"},
     check="Galois sigma fixes 24 Hurwitz units (2T); 8 axis units {+-1,+-i,+-j,+-k} = 4 antipodal pairs = the frame")
assert fc2_ok

# ================================================================ FC.3 the frame-alignment rule (headline)
def axis_key(q):                                     # unsigned axis 0..3 = (1,i,j,k)
    for k in range(4):
        if q[k] != (F(0), F(0)):
            return k
    return -1


clock_of = {}
for ci, c in enumerate(CLOCKS):
    for v in c:
        clock_of[v] = ci
# the canonical tick's clock->axis labeling (each clock one antipodal axis pair)
CANON_LABEL = {}
aligned_here = True
for ci, c in enumerate(CLOCKS):
    ax = set(axis_key(q) for q in AXIS if clock_of[q] == ci)
    if len(ax) == 1:
        CANON_LABEL[ci] = ax.pop()
    else:
        aligned_here = False
CANON_ALIGNED = (aligned_here and len(set(CANON_LABEL.values())) == 4)
# the antipode C^15 = -I fixes each clock (each clock antipode-closed)
ANTIPODE_FIXES = all(qneg(v) in set(c) for c in CLOCKS for v in c)


# frame-alignment as a SELECTOR over all 480 order-5 x order-6 ticks
def is_aligned(a, b):
    cl = clocks_of(a, b)
    if len(cl) != 4 or any(len(c) != 30 for c in cl):
        return None
    co = {}
    for i, c in enumerate(cl):
        for v in c:
            co[v] = i
    lab = {}
    for i, c in enumerate(cl):
        ax = set(axis_key(q) for q in AXIS if co[q] == i)
        if len(ax) != 1:
            return None
        lab[i] = ax.pop()
    if len(set(lab.values())) != 4:
        return None
    return tuple(lab[i] for i in range(4))


O5 = [q for q in ICO if elem_order(q) == 5]
O6 = [q for q in ICO if elem_order(q) == 6]
N_TOTAL = len(O5) * len(O6)
labelings = {}
N_ALIGNED = 0
for a in O5:
    for b in O6:
        lab = is_aligned(a, b)
        if lab is not None:
            N_ALIGNED += 1
            labelings[lab] = labelings.get(lab, 0) + 1
N_LABELINGS = len(labelings)
PER_LABELING = N_ALIGNED // N_LABELINGS if N_LABELINGS else 0
fc3_ok = (CANON_ALIGNED and ANTIPODE_FIXES and N_TOTAL == 480 and N_ALIGNED == 288
          and N_LABELINGS == 6 and N_ALIGNED == N_LABELINGS * PER_LABELING and PER_LABELING == 48)
step("FC.3", "THE FRAME-ALIGNMENT RULE: each clock owns EXACTLY ONE antipodal axis pair {+e,-e} -- the 4 clocks ARE the 4 quaternion axes {1,i,j,k}; the antipode C^15=-I fixes each clock. And alignment is a SELECTOR: EXACTLY 288 of 480 ticks are frame-aligned (6 labelings) -- a real cut 480->288",
     "the canonical frame labels the four clocks. For the canonical tick, EACH of the 4 clocks contains "
     "EXACTLY ONE antipodal axis pair {+e,-e} of the frame -- so the 4 clocks are canonically identified with "
     "the 4 quaternion axes {1,i,j,k}. The antipode C^15 = -I (64.CX.4) FIXES each clock (each clock is "
     "antipode-closed: it contains v iff it contains -v). And this frame-alignment is a genuine SELECTOR, not "
     "a universal property: sweeping all 480 order-5 x order-6 ticks, EXACTLY 288 are frame-aligned (each "
     "clock exactly one axis), falling into 6 distinct clock->axis labelings (the S3 naming of {i,j,k}, the "
     "identity clock {+-1} fixed), 48 ticks per labeling. So the canonical frame CUTS the tick arbitrariness "
     "480 -> 288 -- the owed frame-alignment rule of 64.CX.7, built cold",
     ["FC.1", "FC.2", "64.CX.4"],
     "the headline, and the discharge of 64.CX.7's owed frame-alignment rule. CORRECTIONS #12 located the "
     "canonicalizer as the Galois-fixed frame + parity; this step shows the frame is NOT inert -- it "
     "canonically labels the four clocks (each clock = one quaternion axis) and, crucially, it SELECTS "
     "(288/480, not all), so it genuinely cuts the arbiterness. G4 refuter: had all 480 ticks been "
     "frame-aligned, the frame would carry no selective content (structure, not a reduction); had none been, "
     "the frame would be irrelevant -- instead exactly 288 align, a real cut. G3: the computation names no "
     "physics -- it is axis units in clocks. Exact-integer over the 480 ticks.",
     "UNIQUE (each clock one axis pair; antipode fixes clocks; 288/480 aligned, 6 labelings, 48 each)", "DERIVED",
     {"canonical_tick_aligned": CANON_ALIGNED, "canonical_clock_to_axis": [CANON_LABEL[i] for i in range(4)],
      "antipode_fixes_each_clock": ANTIPODE_FIXES,
      "n_total_ticks": N_TOTAL, "n_aligned": N_ALIGNED, "n_labelings": N_LABELINGS,
      "ticks_per_labeling": PER_LABELING,
      "note": "the 4 clocks are the 4 quaternion axes {1,i,j,k}; frame-alignment cuts 480 -> 288 (a real selector, not universal)"},
     check="each clock owns one antipodal axis pair (4 clocks = 4 axes); antipode fixes each clock; 288/480 aligned, 6 labelings, 48 each")
assert fc3_ok

# ================================================================ FC.4 the four clock-origins (116)
N_SEATS = 4 * 30
N_ORIGINS = 4
N_LAG = N_SEATS - N_ORIGINS                           # 116
fc4_ok = (N_SEATS == 120 and N_LAG == 116 and N_LAG == 4 * 29)
step("FC.4", "(reading, POSTULATE) THE FOUR CLOCK-ORIGINS: designating ONE origin per clock reads 116 = 120 - 4 = 4 x 29 (the carrier minus its four clock-origins) -- the fork's native 116 that meters the neutron-proton splitting. The origin = the + axis unit is the PARITY BIT choice, not forced -- so the fork's n-p meter rests on a reading",
     "the four clocks have 4 * 30 = 120 seats total (the whole carrier -- FC.1 arithmetic). The corpus reads "
     "116 = 4 clocks x 29 lagging seats = 120 minus four clock-ORIGINS = 4x30 - 4, and meters the "
     "neutron-proton splitting with it (Nucleons chapter). The bare arithmetic (120 - 4 = 116 = 4x29) is "
     "trivially true; what is a READING is designating ONE distinguished origin per clock and identifying it "
     "with the + axis unit -- which each aligned clock owns exactly one of (FC.3), the + chosen by the "
     "PARITY BIT ('the sign set at the origin', the CPT chapter). That parity choice is a free ZZ/2, not "
     "forced. So 116-as-the-four-origins-meter is POSTULATE, and the fork's n-p splitting built on it rests "
     "on this reading (and on K2, 59/61) -- CANDIDATE, not banked",
     ["FC.3"],
     "the fork's 116, placed honestly. The n-p splitting (fork) rests on 116; this container locates 116 in "
     "the four clocks (120 - 4) but REFUSES to over-grade it: the 'four clock-origins' one-per-clock and the "
     "origin = + axis / parity-sign identification is the arbiter reading, a free ZZ/2, POSTULATE and "
     "quarantined. So the fork's mass numbers built on 116 stay CANDIDATE. This is exactly the value-gate "
     "discipline: map the path in, do not import the answer. No mass value is computed here.",
     "POSTULATE (116 = the four clock-origins meter; the origin=+axis/parity reading, not forced)", "POSTULATE",
     {"n_clock_seats": N_SEATS, "n_origins": N_ORIGINS, "n_lag_seats": N_LAG,
      "readings": ["116 = 4 clocks x 29 lag-seats", "116 = 120 - 4 clock-origins", "116 = 4x30 - 4"],
      "origin_is_plus_axis": "the parity-bit sign, set at the origin (the CPT chapter) -- a free ZZ/2, not forced",
      "fork_np_splitting_rests_on_this": "CANDIDATE, not banked",
      "downstream_premise_use": False},
     check=None)
assert fc4_ok

# ================================================================ FC.5 the verdict -- POSTULATE (filed 19)
step("FC.5", "(verdict, POSTULATE) The frame-alignment rule REDUCES the tick's canonicity -- the canonical frame labels the four clocks (each = one quaternion axis), a real cut 480->288 (64.CX.7's owed rule, BUILT). But a REDUCTION, not a forcing: the residual (6 axis-labelings, 48/labeling) leaves the tick not-unique; the parity bit is the free origin-sign. A unique tick needs the arbiter seating (owed)",
     "the disciplined reading. The owed frame-alignment rule of 64.CX.7 is BUILT: the substrate's canonical "
     "frame (FC.2) canonically labels the four clocks -- each clock is one quaternion axis {1,i,j,k} (FC.3), "
     "the antipode fixes each -- and frame-alignment is a genuine SELECTOR (288/480). So the frame CUTS the "
     "tick arbitrariness (480 -> 288). But it is a REDUCTION, NOT a forcing: alignment plus the fixed frame "
     "leave a residual -- the 6 clock->axis labelings (the S3 naming of {i,j,k}, a convention like colour "
     "labeling) and 48 ticks per labeling -- so a UNIQUE tick is not forced. The remaining PARITY BIT is the "
     "origin-sign, a free ZZ/2 that SHOULD be free (it is P-violation, unobservable from within, the CPT "
     "chapter). What would upgrade the reduction to a forcing (cutting 288 -> 1 up to parity): the arbiter's "
     "canonical seating -- the fork's total-lean sign / the -93 -- RE-DERIVED at our standard, owed (FC.6). "
     "This is the twin, at the frame level, of 61's count-3, 62's which-A2, and 64's unification: a genuine "
     "reduction. It does NOT touch the content map (K2, 63)",
     ["FC.3", "FC.4"],
     "the corrected, disciplined standing -- and it is careful in BOTH directions. It does not dismiss the "
     "frame-alignment (the frame really does label the clocks and select 288/480 -- the over-negation of the "
     "first step-3 probe, CORRECTIONS #12, is repaired). It does not over-affirm (frame-alignment does NOT "
     "force a unique tick -- 6 labelings, 48 each remain; claiming a forcing would be the over-affirmation "
     "twin). So it lands as a reduction with the residual and the owed arbiter-seating named. No downstream "
     "premise rests on this reading; filed through 19, quarantined.",
     "POSTULATE (the frame-alignment rule reduces the tick to 288/480 -- a real cut, 64.CX.7's owed rule built; not yet a forcing; residual = axis-labeling + parity; the arbiter seating owed)", "POSTULATE",
     {"builds_cx7_frame_alignment_rule": True, "is_reduction": True, "is_forcing": False,
      "cut": "480 -> 288 aligned ticks (a real selector)",
      "residual": "6 clock->axis labelings (S3 naming of {i,j,k}) x 48 ticks per labeling; plus the parity bit (free ZZ/2, P-violation)",
      "owed_to_force": "the arbiter's canonical seating (the fork's -93 lean) re-derived cold -> cuts 288 -> 1 up to parity",
      "does_not_touch": "the content map (K2, 63)",
      "twin_of": "61's count-3, 62's which-A2, 64's unification -- a reduction at the frame level",
      "downstream_premise_use": False},
     check=None)

# ================================================================ FC.6 OWED
step("FC.6", "OWED: the arbiter's canonical origin/lean (the fork's -93) re-derived cold -- would cut the residual 288 to a unique tick up to parity (a forcing); plus the K2 content selection (61/63). Nothing fitted; the fork's mass numbers (incl. the 116-metered n-p splitting) stay CANDIDATE",
     "OWED: (a) the arbiter's canonical seating -- the fork's total-lean sign (the -93 over the four clocks, "
     "the Keystone chapter) -- RE-DERIVED at our standard (target out of view), which would cut the residual "
     "288 aligned ticks to a UNIQUE tick up to the parity bit, upgrading the reduction (FC.5) to a forcing; "
     "(b) failing that, a proof the residual is irreducible; (c) independently, the K2 content selection "
     "(which irreps are the fermions, 61/63). The fork's mass numbers -- including the neutron-proton "
     "splitting metered by the 116 of FC.4, and the proton ratio -- rest on this chain (the arbiter seating "
     "+ K2) and stay CANDIDATE, not banked, while these are owed. Nothing is fitted; the refused-list binds",
     ["FC.5"],
     "the honest residual, located and not attempted. The frame-alignment rule is built and reduces the "
     "arbiterness (480 -> 288); what remains to force a unique tick is the arbiter's canonical seating, and "
     "re-deriving it cold at our standard (not importing the fork's -93) is the next crossing. Even a unique "
     "tick would not close K2. The discipline holds: no mass value is assembled here; the fork's numbers wait "
     "on the arbiter seating and K2.",
     "OWED (the arbiter's canonical seating re-derived cold -> a forcing; plus K2)", "OWED",
     {"owed_arbiter_seating": "the fork's total-lean sign (-93) re-derived cold -> cuts 288 to a unique tick up to parity (a forcing)",
      "owed_impossibility": "or a proof the residual (axis-labeling x 48) is irreducible",
      "owed_from_61_63": "the K2 content selection -- still the lone open input",
      "fork_masses_status": "CANDIDATE (rest on the arbiter seating + K2, both owed); not banked",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="65-four-clocks",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        n_clocks=len(CLOCKS), clock_sizes=CLOCK_SIZES,
        n_galois_fixed=N_HURWITZ, n_axis_units=N_AXIS, n_axis_pairs=N_AXIS_PAIRS,
        canonical_tick_aligned=CANON_ALIGNED, canonical_clock_to_axis=[CANON_LABEL[i] for i in range(4)],
        antipode_fixes_each_clock=ANTIPODE_FIXES,
        n_total_ticks=N_TOTAL, n_aligned=N_ALIGNED, n_labelings=N_LABELINGS, ticks_per_labeling=PER_LABELING,
        n_clock_seats=N_SEATS, n_origins=N_ORIGINS, n_lag_seats=N_LAG,
        finding="THE FOUR CLOCKS AND THE FRAME-ALIGNMENT RULE (Kevin: after 'look at the corpus again', the "
                "owed piece of 64.CX.7). The tick's four 30-clocks on the 120 (FC.1) are canonically labeled "
                "by the four quaternion axes {1,i,j,k} of the Galois-fixed canonical frame (FC.2: 24 Hurwitz, "
                "8 axis units = the Q8 seam): EACH clock owns exactly one antipodal axis pair {+e,-e}, the "
                "antipode C^15=-I fixes each clock, and frame-alignment is a genuine SELECTOR -- 288 of 480 "
                "ticks align, in 6 labelings, 48 each (FC.3). So the canonical frame CUTS the tick "
                "arbitrariness 480 -> 288 -- 64.CX.7's owed frame-alignment rule, BUILT. The four clock-"
                "origins give 120-4 = 116 = 4x29 (the fork's n-p-splitting meter) cold as a count (FC.4). "
                "VERDICT (FC.5, POSTULATE): a REDUCTION toward canonicalizing the tick, NOT a forcing -- the "
                "residual (6 axis-labelings x 48) leaves the tick not-unique; the parity bit is the free "
                "origin-sign (P-violation). A unique tick needs the arbiter's canonical seating (the fork's "
                "-93 lean), OWED at our standard (FC.6) -- which would cut 288 -> 1 up to parity. Does not "
                "touch K2. The fork's mass numbers stay CANDIDATE. Nothing fitted.",
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
