#!/usr/bin/env python3
"""Container 66 -- THE ARBITER SEATING: re-derive the fork's arbiter lean cold, and test whether it cuts the
288 frame-aligned ticks (65) to a unique tick up to parity -- the piece that would turn the reduction chain
(61 count -> 62 axis -> 64 mechanism -> 65 frame) into a FORCING (Kevin: "run the arbiter seating").

Run target out of view (the fork's -33 / -93 / 81 kept out of the forcing), cold on 06's 120 icosians, 64's
tick, 65's frame. latitude(v) = Re(v) (the ziggurat height, relative to the pole 1); lag-depth(v) = the
registration distance = the adjacency graph distance from the pole 1 (shells {1,12,32,42,32,1}).

  AS.1  THE ARBITER CLOCK (DERIVED). The arbiter is the SERVICING clock -- the tick's 30-clock through the
        observer (the identity 1), i.e. the axis-1 clock of 65. Its seat-count by latitude is EXACTLY
        13 above / 13 below / 4 on the equator (mean latitude zero) -- and this seat-symmetry is UNIVERSAL:
        13/13/4 for ALL 288 frame-aligned ticks.
  AS.2  THE LAG CENSUS (DERIVED). Weighting each seat by its registration distance (graph distance from 1),
        the arbiter clock's total lag is EXACTLY 81 = 9^2 (the lag budget squared, eta(W)=9) -- UNIVERSAL
        across all 288 aligned ticks. For the canonical tick the split is 18 above / 51 below / 12 equator.
  AS.3  THE LEAN, REPRODUCED COLD (DERIVED). The arbiter LEAN = (lag above) - (lag below) = 18 - 51 = -33
        for the canonical tick -- the fork's proton lean, cold. And the FOUR-CLOCK TOTAL lean is EXACTLY
        -93 (the fork's Keystone total), which is a TICK-INDEPENDENT CONSTANT: the four clocks partition all
        120 seats, so the total = sum over all 120 of sign(Re v) * dist(1,v) = -93 regardless of the tick.
        (So -93 is a substrate constant, not a selector; the parity bit is its global-reflection mirror +93.)
  AS.4  THE SELECTOR TEST (DERIVED, the headline). Does the arbiter lean CUT the 288? Seat 13/13/4 and lag
        81 are universal (no cut). But the 4-clock lean MULTISET takes EXACTLY 2 values over the 288 aligned
        ticks: (-33,-26,-22,-12) [144 ticks -- the canonical / max-arbiter-lean class] and
        (-26,-25,-22,-20) [144 ticks]. So the arbiter lean CUTS 288 -> 2 classes of 144 (the arbiter clock's
        own lean is -33 or -25, 144 each). It does NOT cut to a unique tick.
  AS.5  (reading, POSTULATE, filed 19) THE VERDICT. The arbiter seating is a genuine, cold-reproduced
        SELECTOR (it reproduces the fork's -33 / 81=9^2 / 13-13-4 / -93 exactly, unfitted, and it cuts
        288 -> 2 lean-classes; the max-lean -33 class = 144 contains the canonical tick and the proton's
        -33). But it does NOT force a UNIQUE tick up to parity: 144 remain in the -33 class (12 with the S3
        axis-labeling, 16 or 32 each). So the reduction chain DEEPENS (61 -> 62 -> 64 -> 65 -> 66) but the
        FORCING is NOT achieved -- a unique tick up to parity remains owed. The parity bit is the global
        reflection (-93 <-> +93), unobservable from within. Does NOT touch the content map (K2). The fork's
        -33 / 81 / 116 are now grounded cold; its mass numbers stay CANDIDATE (K2 + the 144 residual).
  AS.6  OWED. A principle selecting a unique tick within the max-lean class (144 -> 1 up to parity/labeling),
        or a proof the residual is irreducible; the K2 content selection (61/63). Nothing fitted.

THE HEADLINE: the fork's arbiter seating is REAL -- its census reproduces cold and unfitted (the arbiter
clock is seat-symmetric 13/13/4, total lag 81=9^2, lean -33; the four-clock total -93 is a tick-independent
substrate constant). As a canonical selector it CUTS the 288 frame-aligned ticks to 2 lean-classes of 144
(the max-lean -33 class holds the canonical tick and the proton's -33) -- a further REDUCTION, NOT the
forcing to a unique tick that Kevin's chain asked whether it achieves. It does not: 144 remain. So the
reduction chain deepens by one honest step; the forcing stays owed. Rests on 64 (the tick), 65 (the frame /
aligned ticks), 06 (the carrier). Everything RECOMPUTES; nothing is a literal.
"""

import json
import sys
import itertools
from fractions import Fraction as F
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


CAR = json.loads((HERE.parent / "06-carrier-2i" / "derivation.json").read_text(encoding="utf-8"))
D64 = json.loads((HERE.parent / "64-coxeter-bridge" / "derivation.json").read_text(encoding="utf-8"))["values"]
D65 = json.loads((HERE.parent / "65-four-clocks" / "derivation.json").read_text(encoding="utf-8"))["values"]
assert D64["tick_order"] == 30 and D65["n_aligned"] == 288


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


def galois(q):
    return tuple((a + b, -b) for (a, b) in q)


def sign_phi(comp):                                  # exact sign of a + b*phi (phi = (1+sqrt5)/2)
    a, b = comp
    p, q = 2 * a + b, b                              # 2*(a+b phi) = (2a+b) + b*sqrt5 = p + q*sqrt5
    if q == 0:
        return (a > 0) - (a < 0)
    if p == 0:
        return (q > 0) - (q < 0)
    if (p > 0) == (q > 0):
        return 1 if p > 0 else -1
    lhs, rhs = p * p, 5 * q * q                      # opposite signs: compare p^2 vs 5 q^2
    if p > 0:                                        # q<0: >0 iff p^2 > 5 q^2
        return 1 if lhs > rhs else (-1 if lhs < rhs else 0)
    return 1 if rhs > lhs else (-1 if rhs < lhs else 0)


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


# ---- adjacency (v~w iff Re(conj(v) w) = phi/2), BFS distances from the pole 1 ----
HALFPHI = (F(0), F(1, 2))
ADJ = {i: set() for i in range(120)}
for i in range(120):
    for j in range(i + 1, 120):
        if qmul(qconj(ICO[i]), ICO[j])[0] == HALFPHI:
            ADJ[i].add(j)
            ADJ[j].add(i)


def dists_from(src):
    d = [None] * 120
    d[src] = 0
    fr = [src]
    while fr:
        nf = []
        for x in fr:
            for y in ADJ[x]:
                if d[y] is None:
                    d[y] = d[x] + 1
                    nf.append(y)
        fr = nf
    return d


DPOLE = dists_from(IDX[qone()])
SHELLS = sorted(Counter(DPOLE).items())               # [(0,1),(1,12),(2,32),(3,42),(4,32),(5,1)]
SIGN = [sign_phi(ICO[i][0]) for i in range(120)]       # sign of Re(v) (exact)

AXIS = [q for q in ICO if galois(q) == q and sum(1 for c in q if c != (F(0), F(0))) == 1]
AXSET = set(AXIS)


def axis_key(q):
    for k in range(4):
        if q[k] != (F(0), F(0)):
            return k
    return -1


A_ELT = undouble(D64["a_doubled"])
B_ELT = undouble(D64["b_doubled"])
O5 = [q for q in ICO if elem_order(q) == 5]
O6 = [q for q in ICO if elem_order(q) == 6]


def clocks_idx(a, b):
    seen, cl = set(), []
    for v in ICO:
        if v in seen:
            continue
        orb, x = [v], qmul(qmul(a, v), b)
        while not qeq(x, v):
            orb.append(x)
            x = qmul(qmul(a, x), b)
        seen |= set(orb)
        cl.append([IDX[q] for q in orb])
    return cl


def arbiter_census(cl):
    """the arbiter clock = the clock containing the identity 1; its seat-count and lag by latitude."""
    arb = next(c for c in cl if IDX[qone()] in c)
    above = [i for i in arb if SIGN[i] > 0]
    below = [i for i in arb if SIGN[i] < 0]
    eq = [i for i in arb if SIGN[i] == 0]
    wa = sum(DPOLE[i] for i in above)
    wb = sum(DPOLE[i] for i in below)
    we = sum(DPOLE[i] for i in eq)
    return (len(above), len(below), len(eq), wa, wb, we, wa - wb, wa + wb + we)


def aligned_leans(a, b):
    """if frame-aligned, return (arbiter_census, 4-clock-lean-tuple-by-axis); else None."""
    cl = clocks_idx(a, b)
    if len(cl) != 4 or any(len(c) != 30 for c in cl):
        return None
    labs = []
    for c in cl:
        axs = set(axis_key(ICO[i]) for i in c if ICO[i] in AXSET)
        if len(axs) != 1:
            return None
        labs.append(next(iter(axs)))
    if len(set(labs)) != 4:
        return None
    leans = {}
    for c, k in zip(cl, labs):
        wa = sum(DPOLE[i] for i in c if SIGN[i] > 0)
        wb = sum(DPOLE[i] for i in c if SIGN[i] < 0)
        leans[k] = wa - wb
    return arbiter_census(cl), tuple(leans[k] for k in range(4))


# ================================================================ AS.1 the arbiter clock (canonical + sweep)
CANON = arbiter_census(clocks_idx(A_ELT, B_ELT))
CANON_SEATS = (CANON[0], CANON[1], CANON[2])
# sweep the 288 aligned ticks
seat_ct = Counter()
lag_ct = Counter()
arb_lean_ct = Counter()
multiset_ct = Counter()
N_ALIGNED = 0
for a in O5:
    for b in O6:
        r = aligned_leans(a, b)
        if r is None:
            continue
        N_ALIGNED += 1
        cen, leans = r
        seat_ct[(cen[0], cen[1], cen[2])] += 1
        lag_ct[cen[7]] += 1
        arb_lean_ct[cen[6]] += 1
        multiset_ct[tuple(sorted(leans))] += 1
SEAT_UNIVERSAL = (dict(seat_ct) == {(13, 13, 4): 288})
as1_ok = (CANON_SEATS == (13, 13, 4) and SEAT_UNIVERSAL and N_ALIGNED == 288)
step("AS.1", "THE ARBITER CLOCK: the servicing clock through the observer (the identity's clock, axis-1 of 65) has seat-count 13 above / 13 below / 4 equator (mean latitude zero) -- and this seat-symmetry is UNIVERSAL: 13/13/4 for ALL 288 frame-aligned ticks",
     "the arbiter is the tick's 30-clock through the observer -- the clock containing the identity 1 (the "
     "axis-1 clock of 65, the composite order-5 x order-6 servicing circuit). Classifying its 30 seats by "
     "latitude sign (Re(v) > 0 above, < 0 below, = 0 on the equator -- exact sign over Z[phi]) gives EXACTLY "
     "13 above / 13 below / 4 equator -- seat-symmetric about the equator (mean latitude zero). Sweeping all "
     "288 frame-aligned ticks (65), this 13/13/4 holds for EVERY one -- a universal property of the arbiter "
     "clock, reproducing the fork's arbiter seat census cold",
     ["65.FC.3", "64.CX.1"],
     "the arbiter clock, grounded. The fork's Proton-Capture chapter states the arbiter's 30-step walk is "
     "'symmetric about the equator -- 13 above, 13 below, 4 on the equator, mean latitude zero'. Here that is "
     "reproduced cold as the identity's tick-clock, and shown UNIVERSAL across the 288 aligned ticks. "
     "Exact-integer over Z[phi] (exact latitude sign); deterministic clock computation.",
     "UNIQUE (arbiter seat-count 13/13/4, universal over the 288)", "DERIVED",
     {"canonical_arbiter_seats": list(CANON_SEATS), "seat_distribution": {str(k): v for k, v in seat_ct.items()},
      "seat_universal_13_13_4": SEAT_UNIVERSAL, "n_aligned": N_ALIGNED, "shells": SHELLS},
     check="the arbiter (identity) clock has seats 13/13/4 by latitude, universal over all 288 aligned ticks")
assert as1_ok

# ================================================================ AS.2 the lag census
CANON_LAG = (CANON[3], CANON[4], CANON[5])            # (18, 51, 12) for the canonical tick
CANON_TOTLAG = CANON[7]                               # 81
LAG_UNIVERSAL = (dict(lag_ct) == {81: 288})
as2_ok = (CANON_TOTLAG == 81 and CANON_LAG == (18, 51, 12) and LAG_UNIVERSAL)
step("AS.2", "THE LAG CENSUS: weighting each seat by its registration distance (graph distance from the pole 1; shells {1,12,32,42,32,1}), the arbiter clock's TOTAL LAG is EXACTLY 81 = 9^2 -- UNIVERSAL over the 288. The canonical split is 18 above / 51 below / 12 equator",
     "lag-depth(v) = the registration distance = the adjacency-graph distance from the pole 1 (the causal "
     "shells {1,12,32,42,32,1}, diameter 5). Summing lag-depth over the arbiter clock's 30 seats gives "
     "EXACTLY 81 = 9^2 (the lag budget eta(W)=9, squared) -- and this total 81 is UNIVERSAL across all 288 "
     "aligned ticks. For the canonical tick the split by latitude is 18 above / 51 below / 12 equator "
     "(18+51+12 = 81) -- the fork's arbiter dwell census, cold",
     ["AS.1"],
     "the fork's '81 = 9^2' lag budget and the 18/51/12 dwell, reproduced cold. The registration distance is "
     "the substrate's own causal depth (the diameter-5 shells); its sum over the arbiter clock is exactly the "
     "winding budget squared. That the total 81 is universal (like the 13/13/4 seat-count) means these are "
     "structural features of every aligned tick's arbiter clock, not fitted. Exact-integer (BFS distances).",
     "UNIQUE (arbiter total lag 81 = 9^2, universal; canonical split 18/51/12)", "DERIVED",
     {"canonical_lag_split": list(CANON_LAG), "canonical_total_lag": CANON_TOTLAG,
      "lag_distribution": {str(k): v for k, v in lag_ct.items()}, "total_lag_universal_81": LAG_UNIVERSAL},
     check="arbiter clock total lag = 81 = 9^2 (universal over 288); canonical split 18/51/12")
assert as2_ok

# ================================================================ AS.3 the lean, reproduced cold; -93 constant
CANON_LEAN = CANON[6]                                 # -33
# the four-clock total lean is tick-independent: sum over all 120 of sign(Re v)*dist(1,v)
TOTAL_LEAN_ALL120 = sum(SIGN[i] * DPOLE[i] for i in range(120))
# check both multiset classes sum to the same constant
MULTISET_SUMS = sorted(set(sum(m) for m in multiset_ct))
as3_ok = (CANON_LEAN == -33 and TOTAL_LEAN_ALL120 == -93 and MULTISET_SUMS == [-93])
step("AS.3", "THE LEAN, REPRODUCED COLD: the arbiter lean = (lag above) - (lag below) = 18 - 51 = -33 (the fork's proton lean). The FOUR-CLOCK TOTAL lean is -93 (the fork's Keystone total) -- but it is a TICK-INDEPENDENT CONSTANT (the clocks partition all 120), so -93 is a substrate constant, NOT a selector",
     "the arbiter LEAN = (lag-weighted above) - (lag-weighted below) = 18 - 51 = -33 for the canonical tick "
     "-- the fork's proton lean (Proton-Capture chapter), reproduced cold. The FOUR-CLOCK TOTAL lean is "
     "EXACTLY -93 (the fork's Keystone total, 'the arbiter chose BELOW'). CRUCIAL: because the four clocks "
     "PARTITION all 120 seats, the four-clock total = sum over ALL 120 of sign(Re v) * dist(1, v) = -93 -- a "
     "TICK-INDEPENDENT substrate constant (every aligned tick's four leans sum to -93; both lean-multiset "
     "classes of AS.4 sum to -93). So -93 is a substrate CONSTANT, not a selector; the parity bit is its "
     "global-reflection mirror +93 (reflect the carrier -> flip every Re-sign), unobservable from within",
     ["AS.1", "AS.2"],
     "the fork's -33 and -93, reproduced cold AND correctly typed. The -93 is real, but it is a global "
     "constant (a sum over all 120 seats), so it cannot select a tick -- an honest correction to any reading "
     "that treats -93 as a tick-property. The parity bit (the fork's 'sign set at the origin, +93 vs -93') "
     "is the global reflection of the carrier, the free ZZ/2 -- consistent with 65.FC.4 (the origin-sign). "
     "Exact-integer.",
     "UNIQUE (arbiter lean -33; four-clock total -93 = a tick-independent substrate constant)", "DERIVED",
     {"canonical_arbiter_lean": CANON_LEAN, "four_clock_total_lean": TOTAL_LEAN_ALL120,
      "total_is_tick_independent": (MULTISET_SUMS == [-93]),
      "parity_bit": "the global reflection of the carrier (-93 <-> +93), unobservable from within"},
     check="arbiter lean = -33; four-clock total = -93 = sum_all sign(Re v)*dist(1,v), tick-independent")
assert as3_ok

# ================================================================ AS.4 the selector test (headline)
MULTISETS = {str(list(k)): v for k, v in multiset_ct.items()}
N_MULTISETS = len(multiset_ct)
ARB_LEAN_VALUES = dict(sorted(arb_lean_ct.items()))
MAXLEAN = max(abs(k) for k in arb_lean_ct)            # 33
N_MAXLEAN = arb_lean_ct[-MAXLEAN] + arb_lean_ct.get(MAXLEAN, 0)   # 144 (the -33 class)
as4_ok = (N_MULTISETS == 2 and set(multiset_ct.values()) == {144}
          and dict(arb_lean_ct) == {-33: 144, -25: 144} and N_MAXLEAN == 144)
step("AS.4", "THE SELECTOR TEST: seat 13/13/4 and lag 81 are UNIVERSAL (no cut), but the 4-clock lean MULTISET takes EXACTLY 2 values over the 288 -- (-33,-26,-22,-12) [144] and (-26,-25,-22,-20) [144]. So the arbiter lean CUTS 288 -> 2 classes of 144; the arbiter's own lean is -33 or -25 (144 each). NOT a unique tick",
     "does the arbiter lean CUT the 288 frame-aligned ticks? Seat-count (13/13/4, AS.1) and total lag "
     "(81, AS.2) are UNIVERSAL -- they carry no selective content. But the arbiter clock's LEAN is -33 for "
     "144 of the 288 and -25 for the other 144; equivalently the sorted 4-clock lean multiset takes EXACTLY "
     "2 values -- (-33,-26,-22,-12) [144 ticks, the max-arbiter-lean / canonical class] and "
     "(-26,-25,-22,-20) [144 ticks] (both summing to -93, AS.3). So the arbiter lean CUTS 288 -> 2 classes "
     "of 144. It does NOT cut to a unique tick: 144 remain in the -33 class (12 with the S3 axis-labeling, "
     "16 or 32 each)",
     ["AS.3", "65.FC.3"],
     "the decisive result -- and it is neither dismissal nor forcing. The arbiter lean is NOT inert (it "
     "genuinely splits the 288 into two lean-classes, 144 each) -- so re-deriving the arbiter seating IS a "
     "real further selector. But it does NOT achieve the forcing Kevin's chain asked whether it reaches: it "
     "cuts 288 -> 2, not 288 -> 1. G4 refuter: had the arbiter lean been universal (one value for all 288), "
     "the arbiter seating would carry no selective content; had it been 288-valued, it would pick a unique "
     "tick -- instead it is 2-valued (144/144). G3: the computation names no physics -- it is lag-weighted "
     "latitude sums on tick-clocks. Exact-integer over the 288.",
     "UNIQUE (arbiter lean 2-valued: -33 [144] / -25 [144]; cuts 288 -> 2, not -> 1)", "DERIVED",
     {"n_lean_multisets": N_MULTISETS, "lean_multiset_counts": MULTISETS,
      "arbiter_lean_values": ARB_LEAN_VALUES, "max_arbiter_lean": MAXLEAN, "n_in_maxlean_class": N_MAXLEAN,
      "cut": "288 -> 2 classes of 144 (NOT -> 1)"},
     check="arbiter lean is 2-valued (-33:144, -25:144); 4-clock lean multiset has 2 classes of 144; cuts 288->2")
assert as4_ok

# ================================================================ AS.5 verdict -- POSTULATE (filed 19)
step("AS.5", "(verdict, POSTULATE) The arbiter seating is a genuine cold-reproduced SELECTOR (reproduces -33/81/13-13-4/-93 exactly; cuts 288 -> 2 lean-classes, the max-lean -33 class = 144 holding the canonical tick + the proton's -33) but does NOT force a unique tick. The reduction chain DEEPENS (61->62->64->65->66); the FORCING is NOT achieved -- 144 remain",
     "the disciplined verdict. Re-deriving the arbiter seating cold REPRODUCES the fork's arbiter apparatus "
     "exactly and unfitted: the arbiter (servicing) clock is seat-symmetric 13/13/4 (AS.1), total lag "
     "81 = 9^2 (AS.2), lean -33 (AS.3); the four-clock total -93 is a tick-independent substrate constant "
     "(AS.3). As a canonical selector it CUTS the 288 frame-aligned ticks to 2 lean-classes of 144 (AS.4); "
     "the max-arbiter-lean class (-33) holds the canonical tick and the proton's -33. But it does NOT force "
     "a UNIQUE tick up to parity: 144 remain (12 with the S3 axis-labeling, 16/32 each). So the reduction "
     "chain DEEPENS by one honest step (61 count-3 -> 62 which-A2 -> 64 the tick=Coxeter -> 65 the frame "
     "480->288 -> 66 the arbiter lean 288->2) but the FORCING that Kevin's chain asked whether the arbiter "
     "seating achieves is NOT reached: a unique tick up to parity remains owed (AS.6). The parity bit is the "
     "global carrier-reflection (-93 <-> +93). Does NOT touch the content map (K2, 63). The fork's arbiter "
     "numbers (-33, 81, the 116 of 65) are now grounded cold; its mass numbers stay CANDIDATE (they rest on "
     "K2 and on the 144-fold residual, both owed)",
     ["AS.4"],
     "the honest landing, careful in both directions. It does NOT dismiss the arbiter seating (it is a real "
     "selector -- 288 -> 2 -- and it reproduces the fork's numbers cold, a genuine advance in grounding the "
     "fork). It does NOT over-affirm (it is NOT the forcing -- 144 remain; claiming 'canonical tick forced' "
     "would be the over-affirmation twin of CORRECTIONS #12's dismissal). So the chain 61->62->64->65->66 is "
     "five honest reductions, and the forcing stays owed -- the truthful state. No downstream premise rests "
     "on this reading; filed through 19, quarantined.",
     "POSTULATE (the arbiter seating cuts 288 -> 2, reproduces the fork's -33/81/-93 cold; a further reduction, NOT a forcing; a unique tick remains owed)", "POSTULATE",
     {"reproduces_fork_cold": ["arbiter 13/13/4", "lag 81=9^2", "lean -33", "four-clock total -93"],
      "is_selector": True, "cut": "288 -> 2 lean-classes of 144 (max-lean -33 class = 144)",
      "is_forcing": False, "residual": "144 in the -33 class (12 with S3 axis-labeling, 16/32 each)",
      "chain": "61 count-3 -> 62 which-A2 -> 64 tick=Coxeter -> 65 frame 480->288 -> 66 arbiter-lean 288->2 (all reductions)",
      "parity_bit": "the global carrier-reflection (-93 <-> +93)",
      "does_not_touch": "the content map (K2, 63); fork mass numbers stay CANDIDATE",
      "downstream_premise_use": False},
     check=None)

# ================================================================ AS.6 OWED
step("AS.6", "OWED: a principle selecting a UNIQUE tick within the max-lean (-33) class (144 -> 1 up to parity/labeling), or a proof the residual is irreducible; plus the K2 content selection (61/63). Nothing fitted",
     "OWED: (a) a substrate principle that cuts the 144-tick max-arbiter-lean class to a UNIQUE tick (up to "
     "the parity bit and the S3 axis-naming) -- would complete the forcing the chain 61->62->64->65->66 has "
     "been approaching; (b) failing that, a proof the residual (144, or 12 up to labeling) is irreducible -- "
     "the arbiterness is genuinely a family; (c) independently, the K2 content selection (which irreps are "
     "the fermions, 61/63). The fork's mass numbers (the 116-metered n-p splitting, the proton ratio) rest "
     "on the arbiter seating (now partly grounded) AND on K2 AND on the 144-fold residual -- CANDIDATE, not "
     "banked. Nothing fitted; the refused-list binds",
     ["AS.5"],
     "the honest residual, located and not attempted. The arbiter seating reduces the arbiterness (288 -> 2, "
     "or -> the 144 max-lean class) but does not force a unique tick; what remains is the finest cut, and "
     "re-deriving it (or proving it irreducible) is the next crossing. Even a unique tick would not close "
     "K2. The discipline holds: no mass value is assembled here.",
     "OWED (a unique-tick selector within the 144 class, or the irreducibility proof; plus K2)", "OWED",
     {"owed_unique_tick": "a principle cutting the 144 max-lean class to 1 up to parity/labeling (-> the forcing)",
      "owed_impossibility": "or a proof the 144-fold residual is irreducible",
      "owed_from_61_63": "the K2 content selection -- still the lone open input",
      "fork_masses_status": "CANDIDATE (rest on the arbiter seating + K2 + the 144 residual)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="66-arbiter-seating",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        shells=SHELLS,
        canonical_arbiter_seats=list(CANON_SEATS), seat_universal_13_13_4=SEAT_UNIVERSAL,
        canonical_lag_split=list(CANON_LAG), canonical_total_lag=CANON_TOTLAG, total_lag_universal_81=LAG_UNIVERSAL,
        canonical_arbiter_lean=CANON_LEAN, four_clock_total_lean=TOTAL_LEAN_ALL120,
        n_aligned=N_ALIGNED, n_lean_multisets=N_MULTISETS, lean_multiset_counts=MULTISETS,
        arbiter_lean_values=ARB_LEAN_VALUES, max_arbiter_lean=MAXLEAN, n_in_maxlean_class=N_MAXLEAN,
        finding="THE ARBITER SEATING (Kevin: run the piece that would turn the chain into a forcing). Cold, "
                "target out of view. The arbiter = the servicing clock through the observer (the identity's "
                "tick-clock). Its census reproduces the fork EXACTLY and unfitted: seats 13/13/4 (AS.1, "
                "universal over the 288), total lag 81 = 9^2 (AS.2, universal; canonical split 18/51/12), "
                "lean -33 (AS.3); the four-clock total -93 is a TICK-INDEPENDENT substrate constant (the "
                "clocks partition all 120). As a SELECTOR (AS.4): seat and lag are universal (no cut), but "
                "the 4-clock lean multiset takes EXACTLY 2 values over the 288 -- (-33,-26,-22,-12) [144] and "
                "(-26,-25,-22,-20) [144] -- so the arbiter lean CUTS 288 -> 2 classes of 144 (the max-lean "
                "-33 class holds the canonical tick + the proton's -33). VERDICT (AS.5, POSTULATE): a genuine "
                "further REDUCTION (288 -> 2), NOT the forcing -- it does NOT cut 288 -> 1; 144 remain. The "
                "chain deepens (61->62->64->65->66, all reductions); a unique tick up to parity remains OWED "
                "(AS.6). The parity bit is the global carrier-reflection (-93 <-> +93). Does not touch K2. "
                "The fork's -33/81/-93/116 are grounded cold; its mass numbers stay CANDIDATE. Nothing fitted.",
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
