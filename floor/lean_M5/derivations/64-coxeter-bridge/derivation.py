#!/usr/bin/env python3
"""Container 64 -- THE COXETER-30 BRIDGE: the substrate's tick IS the E8 Coxeter element, and colour +
generation + the fold + the mass scale are all powers/aspects of that ONE dynamical element (Maths 6.9).

After 62/63 ran K2 as STATIC algebra (A2 subsystems, reps, embeddings), Kevin caught that the framework's
live structure is DYNAMICAL (the walk / the tick): "this is the statics/dynamics fiasco all over again."
This container formalizes the in-session finding. The tick is the composite screw C = L_a . R_b -- left-
multiplication by an order-5 icosian a and right-multiplication by an order-6 icosian b -- realized as an
8x8 isometry on container 06's Z-basis of the icosian ring (= container 12's E8 lattice). Everything below
RECOMPUTES cold from 06 (the carrier + basis) and 12 (the 240 roots); nothing is a literal. The witness pair
(a, b) is found BY CRITERION (order-5 x order-6 whose tick has characteristic polynomial Phi_30), the
protocol's "criterion + witness" -- not imported.

  CX.1  THE TICK IS AN ORDER-30 E8 ISOMETRY (DERIVED). C = L_a . R_b (a order 5, b order 6) preserves the
        codifferent form (C H C^T = H) and has order EXACTLY 30. As a permutation it cuts the 240 roots into
        8 cycles of length 30 (8 helices; 8*30=240) and the 120 icosians into 4 cycles of length 30
        (4*30=120) -- the H4 Coxeter element on the 120, the E8 Coxeter element on the 240 (one 30).
  CX.2  THE SPECTRUM IS E8'S (DERIVED, the headline). The characteristic polynomial of C is EXACTLY the 30th
        cyclotomic polynomial Phi_30(x) = x^8 + x^7 - x^5 - x^4 - x^3 + x + 1. Its roots are the primitive
        30th roots of unity exp(2*pi*i*m/30) for m in {1,7,11,13,17,19,23,29} -- EXACTLY the E8 exponents
        (the 8 = rank(E8) integers in [1,30) coprime to 30; sum 120 = h*rank/2). So the tick's eigenvalue
        angles ARE the E8 exponents: C is the E8 Coxeter element (order 30 = the Coxeter number h). Integer
        certificate (the Phi_30 coefficients), no floats.
  CX.3  GENERATION IS A POWER OF THE TICK (DERIVED). C^10 = R_{b^4} is PURE right-multiplication (a^10=1 kills
        the left factor; b^10=b^4), an order-3 element that is FIXED-POINT-FREE: 40 three-cycles on the 120
        (40/40/40 blocks) and 80 three-cycles on the 240, zero fixed points. This IS the outer/generation
        Z/3 (left/right-regular, fixed-point-free -- distinct from colour's inner conjugation Z/3). So 61's
        "generation = the outer Z/3" is upgraded to "generation = C^10, a power of the substrate's own
        time-evolution" -- a real advance toward a derivation of the count 3.
  CX.4  COLOUR AND THE FOLD ARE ALSO POWERS/ASPECTS OF THE TICK (DERIVED). Conjugation by g3 = b^2 (the
        tick's own order-3 generator) has fixed locus an A2 x A2 (12 roots, signature 12/12/24/24/72) --
        EXACTLY container 62's colour cut, now tied to the tick. And C^15 = -I: the central fold (a 2*pi
        turn = the duality w = the antipode, container 45's central -1) is the tick's half-turn. So colour
        (inner, g3=b^2), generation (outer, C^10=R_{b^4}), and the fold (central, C^15=-I) are all powers or
        aspects of the ONE tick C -- answering 62/63's owed "mechanism" (option 3 form): the mechanism is
        the dynamics / the arrow of time.
  CX.5  THE MASS-LAW WALK SHARES THE TICK (DERIVED). The +phi/2 adjacency (the degree-12 icosian graph whose
        walk carries the native mass law m_d = 12/d, notation-ref R25/R26) is preserved by the tick
        permutation tau(v) = a.v.b: tau is a graph automorphism of the shell (A[i][j] = A[tau i][tau j]).
        So the mass-scale walk COMMUTES with the tick and all its powers (the pentagon C^6, generation C^10,
        the fold C^15). Mass + colour + generation + the fold are one dynamical element -- the tick.
  CX.6  (reading, POSTULATE, filed 19) THE VERDICT. The substrate's own time-evolution (the tick) IS the E8
        Coxeter element; colour, generation, the fold, and the mass scale are aspects of this ONE element.
        So the "non-generic reason for the E8 structure" that 62/63 said was OWED is DYNAMICAL (the arrow of
        time), not a static subalgebra. HONEST CAVEAT: this is a UNIFICATION, not a forcing -- all E8
        Coxeter elements are W(E8)-conjugate, and the tick is one of that conjugacy class, so it does NOT
        force a UNIQUE colour A2 (the same residual as 62: canonical only up to the tick's conjugacy). What
        is NEW: the arbitrariness is UNIFIED (one tick -> colour + generation + fold + mass, coherently) and
        PHYSICALIZED (tied to the dynamics). It does NOT touch the content map (63's structural gap stands).
  CX.7  OWED. A substrate reason to CANONICALIZE the tick among its W-conjugates (would upgrade the
        unification to a forcing -- the dynamical form of 62's ED.6 canonical colour axis, possibly a
        separate program), OR a proof none exists. The K2 content selection proper (which irreps are the
        fermions, 61/63) remains owed. Nothing fitted.

THE HEADLINE: run as walks (not static algebra), the substrate's tick C = L_a . R_b IS the E8 Coxeter
element (char poly Phi_30; eigenvalue angles = the E8 exponents). Colour (conj by b^2), generation
(C^10 = pure right-mult, fixed-point-free), the fold (C^15 = -1), and the mass-law walk are all powers or
aspects of that ONE element -- the non-generic, DYNAMICAL origin of the E8 structure that 62/63 left owed.
A unification, not a forcing (the tick is W-conjugate to every E8 Coxeter element). Rests on 06 (carrier +
Z-basis), 12 (the 240 roots); grounds 61 (generation = the outer Z/3), ties 62 (the colour A2xA2 cut) and
45 (the central -1) to the tick. Everything RECOMPUTES from those objects; nothing is a literal.
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


# ================================================================ consume 06 (basis) + 12 (roots, Gram)
CAR = json.loads((HERE.parent / "06-carrier-2i" / "derivation.json").read_text(encoding="utf-8"))
E8D = json.loads((HERE.parent / "12-e8-roots" / "derivation.json").read_text(encoding="utf-8"))
BASIS = CAR["values"]["basis"]                       # 8x8 int: Z-basis of the icosian ring, DOUBLED coords
H = E8D["values"]["half_gram"]                        # E8 Gram in basis coords
ROOTS = [tuple(r) for r in E8D["values"]["roots"]]    # 240 roots, c in Z^8 (basis coords), c^T H c = 2
N = 8
RSET = set(ROOTS)
assert len(ROOTS) == 240 and CAR["values"]["half_gram"] == H


def inner(a, b):
    return sum(H[i][j] * a[i] * b[j] for i in range(N) for j in range(N))


# ================================================================ exact Z[phi] quaternion arithmetic
def mulc(A, B):                                       # (a+b phi)(c+d phi) = (ac+bd)+(ad+bc+bd) phi
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


def undouble(v):                                     # doubled int coords -> quaternion, comp=(v[2k]/2,v[2k+1]/2)
    return tuple((F(v[2 * k], 2), F(v[2 * k + 1], 2)) for k in range(4))


def double(q):                                       # quaternion -> doubled int coords
    out = []
    for (a, b) in q:
        ta, tb = 2 * a, 2 * b
        assert ta.denominator == 1 and tb.denominator == 1
        out += [int(ta), int(tb)]
    return out


# ---- the 120 icosians (mirror of 06.icosians_120), sorted canonically for a reproducible witness
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
    return sorted(V, key=lambda q: tuple(double(q)))       # canonical order -> reproducible search


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


# ---- matrix inverse over F; the doubled-coord <-> basis-coord bridge
def matinv(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] + [F(1 if i == k else 0) for k in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                fr = A[r][c]
                A[r] = [A[r][k] - fr * A[c][k] for k in range(2 * n)]
    return [[A[i][n + j] for j in range(n)] for i in range(n)]


BINV = matinv(BASIS)


def coords_of_doubled(w):                            # solve c . BASIS = w  ->  c = w . BINV (must be integral)
    c = [sum(w[k] * BINV[k][j] for k in range(N)) for j in range(N)]
    ci = tuple(int(x) for x in c)
    assert all(F(ci[j]) == c[j] for j in range(N))
    return ci


def left_matrix(g):                                  # x -> g.x, as 8x8 int matrix (row i = image of basis_i)
    return [list(coords_of_doubled(double(qmul(g, undouble(BASIS[i]))))) for i in range(N)]


def right_matrix(g):                                 # x -> x.g
    return [list(coords_of_doubled(double(qmul(undouble(BASIS[i]), g)))) for i in range(N)]


def conj_matrix(g):                                  # x -> g.x.g^-1
    gi = qconj(g)
    return [list(coords_of_doubled(double(qmul(qmul(g, undouble(BASIS[i])), gi)))) for i in range(N)]


def apply_M(Mat, x):
    return tuple(sum(x[i] * Mat[i][j] for i in range(N)) for j in range(N))


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def matpow(A, n):
    R = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    for _ in range(n):
        R = matmul(R, A)
    return R


I8 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
NEG_I8 = [[-1 if i == j else 0 for j in range(N)] for i in range(N)]


def faddeev_charpoly(A):                             # coeffs [c0..c8] of det(xI-A); integer for integer A
    c = [F(1)]
    Ak = None
    for k in range(1, N + 1):
        if k == 1:
            Ak = [[F(A[i][j]) for j in range(N)] for i in range(N)]
        else:
            Mk = [[Ak[i][j] + (c[-1] if i == j else 0) for j in range(N)] for i in range(N)]
            Ak = [[sum(F(A[i][t]) * Mk[t][j] for t in range(N)) for j in range(N)] for i in range(N)]
        tr = sum(Ak[i][i] for i in range(N))
        c.append(-tr / k)
    return [int(x) for x in c]


def cycle_lengths(perm):                             # perm: dict elem -> image
    seen, lens = set(), []
    for x in perm:
        if x in seen:
            continue
        cyc, y = [x], perm[x]
        while y != x:
            cyc.append(y)
            y = perm[y]
        seen |= set(cyc)
        lens.append(len(cyc))
    return sorted(lens)


# ================================================================ CX.1/CX.2 find the tick by criterion
PHI30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]               # x^8+x^7-x^5-x^4-x^3+x+1, the 30th cyclotomic
EXPONENTS = [1, 7, 11, 13, 17, 19, 23, 29]           # E8 exponents = residues in [1,30) coprime to 30
O5 = [q for q in ICO if elem_order(q) == 5]
O6 = [q for q in ICO if elem_order(q) == 6]

TICK = None
for a in O5:
    La = left_matrix(a)
    for b in O6:
        C = matmul(La, right_matrix(b))
        if faddeev_charpoly(C) == PHI30:
            TICK = (a, b, C)
            break
    if TICK:
        break
assert TICK is not None, "no Coxeter tick found"
A_ELT, B_ELT, C = TICK
A_DBL, B_DBL = double(A_ELT), double(B_ELT)

# order exactly 30
CORDER, P = 1, C
while P != I8:
    P = matmul(P, C)
    CORDER += 1
    if CORDER > 60:
        break
CT = [[C[j][i] for j in range(N)] for i in range(N)]
ISOMETRY = (matmul(matmul(C, H), CT) == H)

# helices: the tick as a permutation of the 240 roots and the 120 icosians
perm_roots = {r: apply_M(C, r) for r in ROOTS}
assert all(v in RSET for v in perm_roots.values())
ROOT_CYCLES = cycle_lengths(perm_roots)


def tau(v):
    return qmul(qmul(A_ELT, v), B_ELT)


IDX = {v: i for i, v in enumerate(ICO)}
assert all(tau(v) in IDX for v in ICO)
perm_ico = {IDX[v]: IDX[tau(v)] for v in ICO}
ICO_CYCLES = cycle_lengths(perm_ico)

HELIX_240 = (set(ROOT_CYCLES) == {30} and len(ROOT_CYCLES) == 8)
HELIX_120 = (set(ICO_CYCLES) == {30} and len(ICO_CYCLES) == 4)
CHARPOLY = faddeev_charpoly(C)
cx1_ok = (elem_order(A_ELT) == 5 and elem_order(B_ELT) == 6 and CORDER == 30
          and ISOMETRY and HELIX_240 and HELIX_120)
step("CX.1", "THE TICK IS AN ORDER-30 E8 ISOMETRY. C = L_a . R_b (a order 5, b order 6 icosians) preserves the E8 form and has order EXACTLY 30; it cuts the 240 roots into 8 helices of 30 (8*30=240) and the 120 icosians into 4 loops of 30 (4*30=120)",
     "the substrate tick is the composite screw C = L_a . R_b: left-multiply by an order-5 icosian a, "
     "right-multiply by an order-6 icosian b, as an 8x8 integer isometry on 06's Z-basis (= 12's E8 "
     "lattice). C H C^T = H (isometry), and C has order EXACTLY 30 (a^10=1 and b needs 6 | n, so 30 | n; "
     "order 30). The witness (a, b) is found BY CRITERION -- the first order-5 x order-6 pair (canonical "
     "icosian order) whose tick has characteristic polynomial Phi_30 (CX.2) -- not imported. As a "
     "permutation, C cuts the 240 roots into 8 cycles of length 30 (8 helices; 8*30=240) and the 120 "
     "icosians into 4 cycles of length 30 (4*30=120) -- the H4 Coxeter element on the 120, one 30",
     ["06.6.5", "12.E.2"],
     "the object the whole container is about, built cold. The tick is the substrate's OWN time-evolution "
     "(the propagative screw of the notation-ref R5/R7-R9); 62/63 treated K2 as static subalgebra, but "
     "Kevin's catch is that the live structure is DYNAMICAL. Here the tick is realized as an exact 8x8 "
     "isometry on the E8 lattice and shown to have order 30 = the E8 Coxeter number h, cutting both the 240 "
     "roots (8 helices) and the 120 icosians (4 loops) into length-30 orbits. Exact-integer over H; the "
     "witness pair is a reproducible criterion-search, not a literal.",
     "UNIQUE UP TO conjugacy (the tick is one E8 Coxeter element; all such are W(E8)-conjugate)", "DERIVED",
     {"a_order": elem_order(A_ELT), "b_order": elem_order(B_ELT), "tick_order": CORDER,
      "isometry": ISOMETRY, "root_cycle_lengths": sorted(set(ROOT_CYCLES)), "n_root_cycles": len(ROOT_CYCLES),
      "ico_cycle_lengths": sorted(set(ICO_CYCLES)), "n_ico_cycles": len(ICO_CYCLES),
      "a_doubled": A_DBL, "b_doubled": B_DBL,
      "helix_240_is_8x30": HELIX_240, "helix_120_is_4x30": HELIX_120},
     check="C = L_a.R_b: order 30, C H C^T=H, 8 cycles of 30 on 240 roots, 4 cycles of 30 on 120 icosians")
assert cx1_ok

# ================================================================ CX.2 the spectrum is E8's (Phi_30)
EXP_OK = (EXPONENTS == [m for m in range(1, 30) if __import__("math").gcd(m, 30) == 1])
EXP_SUM = sum(EXPONENTS)
cx2_ok = (CHARPOLY == PHI30 and EXP_OK and len(EXPONENTS) == 8 and EXP_SUM == 120)
step("CX.2", "THE SPECTRUM IS E8's. The tick's characteristic polynomial is EXACTLY Phi_30(x)=x^8+x^7-x^5-x^4-x^3+x+1; its eigenvalue angles are the E8 exponents {1,7,11,13,17,19,23,29} -- so the tick IS the E8 Coxeter element",
     "the characteristic polynomial of C (Faddeev-LeVerrier over the integers) is EXACTLY the 30th "
     "cyclotomic polynomial Phi_30(x) = x^8 + x^7 - x^5 - x^4 - x^3 + x + 1. Its roots are the primitive "
     "30th roots of unity exp(2*pi*i*m/30) for m in {1,7,11,13,17,19,23,29} -- the 8 = rank(E8) integers in "
     "[1,30) coprime to 30, which are EXACTLY the E8 exponents (sum 120 = h*rank/2 = 30*8/2). So the tick's "
     "eigenvalue angles ARE the E8 exponents and its order 30 IS the Coxeter number h: C is an E8 Coxeter "
     "element. The certificate is the integer coefficient vector of Phi_30 -- no floating-point eigenvalues",
     ["CX.1"],
     "the headline, and the 'non-generic reason for the E8 structure' that 62/63 said was OWED, now supplied "
     "-- dynamically. 62's ED.6 and 63 asked for a substrate reason the E8 structure is picked out; the "
     "answer is that the substrate's own tick IS the Coxeter element -- the single conjugacy class that "
     "generates E8's whole eigenvalue skeleton (its exponents / its Coxeter plane). G4 refuter: had the "
     "charpoly been any other degree-8 integer polynomial (not Phi_30), C would not be a Coxeter element and "
     "the claim would fail cold; it is exactly Phi_30. G3: the computation never names 'physics' -- it is "
     "the spectrum of a quaternion screw on a lattice. Exact-integer (the charpoly coefficients).",
     "UNIQUE (char poly = Phi_30; the 8 E8 exponents, sum 120)", "DERIVED",
     {"charpoly": CHARPOLY, "is_phi30": (CHARPOLY == PHI30), "exponents": EXPONENTS,
      "exponents_are_coprime_residues": EXP_OK, "n_exponents": len(EXPONENTS), "exponent_sum": EXP_SUM,
      "coxeter_number": 30, "rank": 8},
     check="char poly of C = Phi_30 = x^8+x^7-x^5-x^4-x^3+x+1; exponents {1,7,11,13,17,19,23,29}, sum 120")
assert cx2_ok

# ================================================================ CX.3 generation = a power of the tick
B4 = B_ELT
for _ in range(3):
    B4 = qmul(B4, B_ELT)                             # b^4
C10 = matpow(C, 10)
GEN_IS_RIGHT_B4 = (C10 == right_matrix(B4))
GEN_ORDER = 30 // __import__("math").gcd(30, 10)     # = 3
gen_perm_ico = {IDX[v]: IDX[qmul(v, B4)] for v in ICO}
GEN_FIXED_120 = sum(1 for i in gen_perm_ico if gen_perm_ico[i] == i)
GEN_CYC_120 = cycle_lengths(gen_perm_ico)
gen_perm_roots = {r: apply_M(C10, r) for r in ROOTS}
GEN_FIXED_240 = sum(1 for r in ROOTS if apply_M(C10, r) == r)
GEN_CYC_240 = cycle_lengths(gen_perm_roots)
cx3_ok = (GEN_IS_RIGHT_B4 and elem_order(B4) == 3 and GEN_FIXED_120 == 0
          and set(GEN_CYC_120) == {3} and len(GEN_CYC_120) == 40
          and GEN_FIXED_240 == 0 and set(GEN_CYC_240) == {3} and len(GEN_CYC_240) == 80)
step("CX.3", "GENERATION IS A POWER OF THE TICK. C^10 = R_{b^4} is PURE right-multiplication, an order-3 FIXED-POINT-FREE element -- 40 three-cycles on the 120 (40/40/40) and 80 on the 240 = the outer/generation Z/3. Grounds 61",
     "C^10 = R_{b^4}: because a^10 = 1 (a order 5) the left factor dies, and b^10 = b^4 (b order 6), so C^10 "
     "is PURE right-multiplication by b^4. b^4 has order 3, and right-multiplication by a non-identity group "
     "element is FIXED-POINT-FREE, so C^10 is an order-3 fixed-point-free map: 40 three-cycles on the 120 "
     "icosians (the 40/40/40 generation blocks) and 80 three-cycles on the 240 roots, zero fixed points. "
     "This is precisely the OUTER (left/right-regular) Z/3 -- fixed-point-free, distinct from colour's INNER "
     "conjugation Z/3 (6 fixed + 38 triples, 31/62). So 61's 'generation = the outer Z/3' is realized as "
     "generation = C^10, a power of the substrate's own time-evolution",
     ["CX.1", "61.ST.3"],
     "the upgrade 61 was reaching for. 61 identified generation with the outer Z/3 but could only MOTIVATE "
     "the count 3 (via 3^1||120 and the triadic floor), not derive it from the dynamics. Here generation is "
     "a specific POWER of the tick (C^10), so the count-3 is the order of C^10 -- an order forced by the "
     "tick's own period 30 (30/gcd(30,10)=3). G4 refuter: had C^10 had any fixed point, or order != 3, it "
     "could not be the fixed-point-free generation Z/3; it is exactly order-3 fixed-point-free. G3: no "
     "'generation' label enters the computation -- it is the 10th power of a lattice isometry. Exact-integer.",
     "UNIQUE (C^10 = R_{b^4}, order 3, fixed-point-free: 40 three-cycles on 120, 80 on 240)", "DERIVED",
     {"c10_is_right_mult_b4": GEN_IS_RIGHT_B4, "gen_order": GEN_ORDER, "b4_order": elem_order(B4),
      "gen_fixed_120": GEN_FIXED_120, "gen_cycle_len_120": sorted(set(GEN_CYC_120)),
      "gen_n_cycles_120": len(GEN_CYC_120),
      "gen_fixed_240": GEN_FIXED_240, "gen_cycle_len_240": sorted(set(GEN_CYC_240)),
      "gen_n_cycles_240": len(GEN_CYC_240)},
     check="C^10 = R_{b^4} (a^10=1, b^10=b^4), order 3, fixed-point-free: 40 three-cycles on 120, 80 on 240")
assert cx3_ok

# ================================================================ CX.4 colour + fold are aspects of the tick
G3 = qmul(B_ELT, B_ELT)                              # b^2, the tick's own order-3 generator
COL_ORDER = elem_order(G3)
Mc = conj_matrix(G3)
FIXED_ROOTS = [r for r in ROOTS if apply_M(Mc, r) == r]
ipc = {}
for x in FIXED_ROOTS:
    for y in FIXED_ROOTS:
        ipc[inner(x, y)] = ipc.get(inner(x, y), 0) + 1
IP_SIG = {str(k): ipc[k] for k in sorted(ipc)}
A2xA2 = (len(FIXED_ROOTS) == 12 and IP_SIG == {"-2": 12, "-1": 24, "0": 72, "1": 24, "2": 12})
C15 = matpow(C, 15)
FOLD_IS_NEG_I = (C15 == NEG_I8)
cx4_ok = (COL_ORDER == 3 and A2xA2 and FOLD_IS_NEG_I)
step("CX.4", "COLOUR AND THE FOLD ARE ALSO POWERS/ASPECTS OF THE TICK. Conjugation by g3=b^2 (the tick's own order-3 generator) fixes an A2 x A2 (12 roots, 62's colour cut); and C^15 = -I is the central fold (45's -1). Colour, generation, fold: ONE tick",
     "the tick's own order-3 generator is g3 = b^2. Conjugation by g3 fixes EXACTLY 12 roots with the "
     "inner-product signature 12/12/24/24/72 of an A2 x A2 -- EXACTLY container 62's colour cut, now tied to "
     "the tick. And C^15 = -I: since C has order 30, its half-power C^15 is the central involution -1 -- the "
     "2*pi turn = the duality w = the antipode/central character (container 45's central -1). So colour "
     "(INNER, conjugation by g3 = b^2), generation (OUTER, C^10 = right-mult by b^4), and the fold (CENTRAL, "
     "C^15 = -1) are all powers or aspects of the ONE tick C -- and the mass-law walk too (CX.5). This "
     "answers 62/63's owed 'mechanism' (option-3 form): the mechanism is the dynamics / the arrow of time",
     ["CX.1", "62.ED.2", "45.SP.1"],
     "the unification, and the tie back to 62/45. 62 found colour as conjugation by an order-3 element with "
     "fixed locus A2 x A2; here that order-3 element is the tick's OWN generator b^2 -- so 62's static "
     "colour cut is an aspect of the dynamical tick. 45's central -1 (the spinor 2*pi -> -1) is C^15, the "
     "tick's half-turn. So the substrate's three Z-structures -- inner colour, outer generation, central "
     "duality -- are all read off the ONE tick, not three coincidental threes/twos. G3: the computation is "
     "conjugation and matrix powers of a lattice isometry; no physics name enters. Exact-integer.",
     "UNIQUE (conj by b^2 fixes an A2xA2, 12 roots; C^15 = -I central)", "DERIVED",
     {"colour_g3_order": COL_ORDER, "colour_fixed_root_count": len(FIXED_ROOTS),
      "colour_ip_signature": IP_SIG, "colour_fixed_locus_is_A2xA2": A2xA2,
      "c15_is_neg_identity": FOLD_IS_NEG_I,
      "note": "colour = conj b^2 (inner Z/3); generation = C^10 = R_{b^4} (outer Z/3); fold = C^15 = -1 (central) -- all aspects of the ONE tick"},
     check="conj by b^2 fixes an A2xA2 (12 roots, sig 12/12/24/24/72); C^15 = -I (the central fold)")
assert cx4_ok

# ================================================================ CX.5 the mass-law walk shares the tick
HALF_PHI = (F(0), F(1, 2))                            # phi/2 as (a + b*phi) = 0 + (1/2)phi


def re_inner(v, w):                                   # scalar part Re(conj(v).w), a Z[phi] pair
    return qmul(qconj(v), w)[0]


ADJ = [[1 if re_inner(ICO[i], ICO[j]) == HALF_PHI else 0 for j in range(120)] for i in range(120)]
DEGREES = set(sum(row) for row in ADJ)
MASS_COMMUTES = all(ADJ[i][j] == ADJ[perm_ico[i]][perm_ico[j]] for i in range(120) for j in range(120))
cx5_ok = (DEGREES == {12} and MASS_COMMUTES)
step("CX.5", "THE MASS-LAW WALK SHARES THE TICK. The +phi/2 adjacency (the degree-12 icosian graph carrying the native mass law m_d=12/d) is preserved by the tick permutation tau(v)=a.v.b -- so the mass scale commutes with the tick and ALL its powers. Mass + colour + generation + fold = one tick",
     "the native mass law (notation-ref R25/R26: m_d = 12/d, the twelve-witness census's Galois-symmetrized "
     "walk eigenvalue) lives on the +phi/2 ADJACENCY -- the degree-12 icosian graph where v ~ w iff "
     "Re(conj(v).w) = phi/2. The tick permutation tau(v) = a.v.b PRESERVES this adjacency: "
     "Re(conj(a v b).(a w b)) = Re(conj(b).conj(v).w.b) = Re(conj(v).w) (Re is conjugation-invariant and "
     "conj(a)a = 1), so ADJ[i][j] = ADJ[tau i][tau j] -- tau is a graph automorphism of every shell. Hence "
     "the mass-law walk COMMUTES with the tick and all its powers: the pentagon C^6 (order 5), generation "
     "C^10 (order 3), the fold C^15 (order 2). Mass, colour, generation, and the fold are one dynamical "
     "element -- the tick. (The 120x120 commutation is exact-integer, verify-guarded.)",
     ["CX.1", "CX.3", "CX.4"],
     "the last thread that ties the mass scale into the same tick -- the open item from the session boot "
     "('does a power of the tick tie the mass-law walk in?'). The nine association-scheme walks on the 120 "
     "(the inner-product shells) all commute with the two-sided 2I-action, and the tick is one two-sided "
     "element, so every shell -- including the +phi/2 mass walk -- is simultaneously graded by the tick's "
     "eigenspaces. So the mass spectrum, colour, generation, and the fold are not four coincidences but four "
     "faces of the ONE tick. G3: no mass VALUE is computed or fitted here -- only that the mass-carrying "
     "graph is tick-invariant. Exact-integer over Z[phi].",
     "UNIQUE (the +phi/2 degree-12 walk is tau-invariant; mass shares the tick)", "DERIVED",
     {"adjacency_degree": sorted(DEGREES), "mass_walk_commutes_with_tick": MASS_COMMUTES,
      "note": "tau(v)=a.v.b is a graph automorphism of the +phi/2 shell -> the mass-law walk shares the tick with colour/generation/fold"},
     check="the +phi/2 degree-12 walk on the 120 is preserved by the tick permutation tau(v)=a.v.b (mass shares the tick)")
assert cx5_ok

# ================================================================ CX.6 the verdict -- POSTULATE (filed 19)
step("CX.6", "(verdict, POSTULATE) The substrate's TICK IS the E8 Coxeter element; colour, generation, the fold, and the mass scale are aspects of that ONE element -- the DYNAMICAL origin of the E8 structure that 62/63 left owed. A UNIFICATION, not a forcing",
     "the disciplined reading. The substrate's own time-evolution -- the tick C = L_a . R_b -- IS the E8 "
     "Coxeter element (CX.2), and colour (conj b^2, CX.4), generation (C^10, CX.3), the fold (C^15, CX.4) "
     "and the mass-law walk (CX.5) are all powers or aspects of it. So the 'non-generic reason for the E8 "
     "structure' that 62 (ED.6) and 63 named OWED is DYNAMICAL -- the arrow of time -- not a static "
     "subalgebra. HONEST CAVEAT (do not overclaim): this is a UNIFICATION, NOT a forcing. All E8 Coxeter "
     "elements are W(E8)-conjugate, and the tick is one member of that conjugacy class, so it does NOT force "
     "a UNIQUE colour A2 -- the same residual arbitrariness as 62 (canonical only up to the tick's "
     "conjugacy). What is NEW and real: the arbitrariness is UNIFIED (one tick simultaneously fixes colour, "
     "generation, the fold, and the mass grading, coherently) and PHYSICALIZED (tied to the substrate's "
     "dynamics). It does NOT touch the content map -- 63's structural gap (which irreps are the fermions) "
     "stands untouched. So: a genuine reduction/unification (the twin, at the dynamical level, of 61's "
     "count-3 and 62's which-A2 reductions), NOT a forcing, NOT a solution to K2",
     ["CX.2", "CX.3", "CX.4", "CX.5"],
     "the corrected, disciplined standing -- neither dismissal nor over-affirmation. It would be easy to "
     "over-read 'the tick is the E8 Coxeter element' as forcing the E8 structure uniquely; it does not (all "
     "Coxeter elements are conjugate). It would be easy to dismiss it as 'just a Coxeter element'; it is not "
     "-- it UNIFIES colour, generation, the fold, and the mass scale under one dynamical object, exactly the "
     "kind of reduction the program is after (FRONTIER: a structure reduced to a named root/mechanism is the "
     "success). The open question that would move it to a forcing (CX.7): a substrate reason to canonicalize "
     "the tick among its W-conjugates. No downstream premise rests on this reading; filed through 19, "
     "quarantined.",
     "POSTULATE (the tick = the E8 Coxeter element; colour/generation/fold/mass its aspects -- a unification, not a forcing; the E8 mechanism is dynamical)", "POSTULATE",
     {"tick_is_e8_coxeter": True, "unifies": ["colour (conj b^2)", "generation (C^10)", "fold (C^15)", "mass-law walk"],
      "is_forcing": False, "is_unification": True,
      "e8_mechanism": "dynamical (the arrow of time), not a static subalgebra -- answers 62.ED.6 / 63's owed mechanism at the unification level",
      "residual": "the tick is W(E8)-conjugate to every E8 Coxeter element -> colour A2 canonical only up to the tick's conjugacy (same residual as 62)",
      "does_not_touch": "the content map (63's structural gap: which irreps are the fermions) is untouched",
      "twin_of": "61's count-3 and 62's which-A2 reductions, now at the dynamical level",
      "downstream_premise_use": False},
     check=None)

# ================================================================ CX.7 OWED
step("CX.7", "OWED (refined 2026-09-17, Kevin's 'look at the corpus again'): the canonicalizer is NOT a W(E8)/conjugation invariant (all Coxeter elements are W-conjugate -- a theorem; 'no edge is privileged'). It is the substrate's Galois-fixed canonical FRAME (the 24 Hurwitz / 8-axis Q8 seam) + the PARITY BIT; owed is the fork's FRAME-ALIGNMENT rule (the four clocks / arbiter) re-derived cold. Plus the content selection K2 (61/63). Nothing fitted",
     "OWED, correctly scoped. The tick's canonicity is NOT a conjugation question -- all E8 Coxeter elements "
     "are W(E8)-conjugate (a theorem; the substrate itself has 'no privileged edge' under 2I-conjugation, so "
     "asking a conjugation-invariant to single one out is category-wrong, the CORRECTIONS #7/#12 trap). The "
     "substrate's ACTUAL canonicalizers are structures OUTSIDE W(E8), and the corpus names them: (i) the "
     "CANONICAL QUATERNION FRAME = the Galois-fixed (phi-free) spine -- computed cold as the 24 Hurwitz units "
     "(= 2T), of which the 8 axis units {+-1,+-i,+-j,+-k} are the corpus's Q8 seam; and (ii) the PARITY BIT -- "
     "the mirror L_a.R_{b^-1} is a fixed-point-free involution pairing the 8 conjugation-orbits of Coxeter "
     "ticks into 4 chiral pairs (the free ZZ/2 'set at the origin, unobservable from within', the "
     "charge-conjugate families A<->B of the CPT chapter). So relative to the fixed frame the residual is the "
     "parity bit. What is OWED to turn the unification (CX.6) into a forcing: the FRAME-ALIGNMENT RULE -- the "
     "fork's four-clocks / arbiter seating that ties the tick to the canonical frame -- RE-DERIVED at our "
     "standard (their docs grade it THEOREM; we have not rebuilt it cold). Independently, the K2 content "
     "selection (which irreps are the fermions, 61/63) remains owed; no content is fitted here",
     ["CX.6"],
     "the honest residual, RE-EXAMINED after Kevin caught an over-negation ('no canonical tick emerges' was "
     "the scoped-negative-as-forbidden-region error, CORRECTIONS #7). The first pass tested only "
     "conjugation-invariants -- which by theorem cannot distinguish W-conjugate Coxeter elements -- and "
     "wrongly read that as 'no canonical tick'. Looked at with the corpus's own canonicalizers (the "
     "Galois-fixed frame + the parity bit, both computed cold: 24 Hurwitz / 8 axis; mirror pairs 8->4), the "
     "tick IS canonical relative to the frame, up to a parity ZZ/2 that SHOULD be free (it is P-violation). "
     "So this is a REDUCTION ('which tick' -> 'the frame-alignment rule + the parity bit'), not a "
     "checked-negative -- the frame-alignment rule (the four clocks / arbiter) is the owed piece, the "
     "concrete route from unification to forcing. The discipline holds: nothing about the SM multiplets is "
     "assembled here; the four-clocks re-derivation must pass the value-gate cold.",
     "OWED (the fork's frame-alignment rule / the four clocks re-derived cold -> a forcing; plus the content selection from 61/63)", "OWED",
     {"canonicalizer_is_not_conjugation_invariant": "all E8 Coxeter elements are W-conjugate (theorem); 'no edge is privileged' -- a conjugation-invariant CANNOT distinguish them (CORRECTIONS #7/#12)",
      "located_canonical_frame": "the Galois-fixed phi-free spine: 24 Hurwitz units (2T), of which 8 axis units {+-1,+-i,+-j,+-k} = the Q8 seam (computed cold)",
      "located_parity_bit": "the mirror L_a.R_{b^-1} is a fixed-point-free involution pairing the 8 conjugation-orbits into 4 chiral pairs -- the free ZZ/2 set at the origin (CPT chapter)",
      "owed_frame_alignment_rule": "the fork's four-clocks / arbiter seating tying the tick to the canonical frame, re-derived at our standard (-> a forcing up to parity)",
      "owed_from_61_63": "the content selection K2 (which irreps are the fermions) -- still the lone open input",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="64-coxeter-bridge",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        a_order=elem_order(A_ELT), b_order=elem_order(B_ELT), a_doubled=A_DBL, b_doubled=B_DBL,
        tick_order=CORDER, isometry=ISOMETRY,
        charpoly=CHARPOLY, is_phi30=(CHARPOLY == PHI30), exponents=EXPONENTS,
        exponent_sum=EXP_SUM, coxeter_number=30, rank=8,
        root_cycle_lengths=sorted(set(ROOT_CYCLES)), n_root_cycles=len(ROOT_CYCLES),
        ico_cycle_lengths=sorted(set(ICO_CYCLES)), n_ico_cycles=len(ICO_CYCLES),
        helix_240_is_8x30=HELIX_240, helix_120_is_4x30=HELIX_120,
        c10_is_right_mult_b4=GEN_IS_RIGHT_B4, gen_order=GEN_ORDER,
        gen_fixed_120=GEN_FIXED_120, gen_n_cycles_120=len(GEN_CYC_120),
        gen_fixed_240=GEN_FIXED_240, gen_n_cycles_240=len(GEN_CYC_240),
        colour_g3_order=COL_ORDER, colour_fixed_root_count=len(FIXED_ROOTS),
        colour_ip_signature=IP_SIG, colour_fixed_locus_is_A2xA2=A2xA2,
        c15_is_neg_identity=FOLD_IS_NEG_I,
        adjacency_degree=sorted(DEGREES), mass_walk_commutes_with_tick=MASS_COMMUTES,
        finding="THE COXETER-30 BRIDGE (Maths 6.9; Kevin's statics/dynamics catch), formalized. Run as "
                "WALKS, the substrate's tick C = L_a . R_b (a order-5, b order-6 icosians) is an order-30 E8 "
                "isometry (CX.1) whose characteristic polynomial is EXACTLY Phi_30 -- its eigenvalue angles "
                "are the E8 exponents {1,7,11,13,17,19,23,29}, so C IS the E8 Coxeter element (CX.2, the "
                "'non-generic reason for the E8 structure' 62/63 owed, supplied dynamically). It cuts the 240 "
                "roots into 8 helices of 30 and the 120 icosians into 4 loops of 30 (the H4 Coxeter, one 30). "
                "GENERATION = C^10 = R_{b^4}, pure right-mult, order-3 fixed-point-free (40/40/40 on 120, 80 "
                "three-cycles on 240) = the outer Z/3 (CX.3, grounds 61). COLOUR = conj by g3=b^2, fixed "
                "locus an A2 x A2 (12 roots, 62's cut); the FOLD = C^15 = -I, the central -1 (45) -- so "
                "colour (inner), generation (outer), the fold (central) are all powers/aspects of the ONE "
                "tick (CX.4). The +phi/2 MASS-LAW walk commutes with the tick (CX.5), so mass shares it too. "
                "VERDICT (CX.6, POSTULATE): the substrate's time-evolution IS the E8 Coxeter element; colour, "
                "generation, the fold, and the mass scale are its aspects -- the E8 mechanism is DYNAMICAL "
                "(the arrow of time). A UNIFICATION, not a forcing (all E8 Coxeter elements are W-conjugate; "
                "the tick is one -> no unique colour A2, the same residual as 62); it does NOT touch the "
                "content map (63). OWED (CX.7): a canonical tick (-> a forcing), or the impossibility proof; "
                "plus the content selection K2. Nothing fitted.",
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
