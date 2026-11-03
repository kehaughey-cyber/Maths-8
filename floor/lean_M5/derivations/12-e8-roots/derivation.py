#!/usr/bin/env python3
"""Container 12 -- the E8 ROOT SYSTEM (the 240 minimal vectors). Rests on 06 (the carrier).

NUMBER IS A BUILD-ORDER LABEL. Conceptually this is rung 7 -- E8 as a ROOT SYSTEM -- positioned by
IMPORT above container 06 (the carrier), which built the icosian ring and showed its codifferent
Gram is even, unimodular (det 1), even-diagonal == E8. The 6 -> 7 boundary was DECLARED in
INTERFACES.md ("E8 sits downstream of the CARRIER, not the icosahedron"); this container builds the
E8 side of it: the ROOTS.

THE 240, DERIVED FROM A NORM-2 CRITERION -- not a solved-externally literal. maths 4 carried the 240
roots as a literal list "solved externally" (Closure/IcosianE8.lean's 240-vector table). Here the 240
are the MINIMAL VECTORS of container 06's E8 Gram H (= half_gram): the exhaustive set

    { c in Z^8 : c^T H c = 2 }        (H positive-definite, so this is finite and searchable)

found by an EXACT short-vector enumeration (Fincke-Pohst over the Cholesky-without-sqrt form). The
search is EXHAUSTIVE (it is the standard complete short-vector algorithm) and reproducible; the count
it returns is exactly 240, and the 240 vectors it returns are the witness, checkable against the
criterion. The minimal norm of E8 is 2, so these are E8's roots / minimal vectors -- the kissing
configuration in 8 dimensions.

WHAT IS DERIVED HERE: the count (240) from the norm-2 criterion; that the roots are all norm 2,
closed under negation (120 antipodal pairs), and pairwise inner products lie in {-2,-1,0,1,2} (the
simply-laced / crystallographic ADE condition). WHAT IS CITED: that 240 is OPTIMAL (the maximum
kissing number in 8-D, E8 -- Viazovska 2016), external accepted mathematics -- the same tier as
container 09's no-13th (Schuette-van der Waerden) in 3-D. NOT claimed: the Weyl group, the Dynkin
diagram, or E8 as a Lie algebra -- only the root system as a point configuration.

Grades: DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps (incl. the
exhaustive enumeration).
"""

import json
import sys
from fractions import Fraction as Fr
from math import floor, ceil, sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- consume the carrier (06)
CARRIER = json.loads((HERE.parent / "06-carrier-2i" / "derivation.json").read_text(encoding="utf-8"))
H = CARRIER["values"]["half_gram"]          # the E8 Gram (even, unimodular det 1) -- container 06's
ICOSIANS = CARRIER["values"]["icosians_count"]   # 120
N = 8


def det(M):
    A = [[Fr(x) for x in r] for r in M]
    n = len(A)
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if A[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            d = -d
        d *= A[i][i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
    return d


def qform(c):                                # c^T H c, exact
    return sum(H[i][j] * c[i] * c[j] for i in range(N) for j in range(N))


def inner(a, b):                             # a^T H b, exact
    return sum(H[i][j] * a[i] * b[j] for i in range(N) for j in range(N))


# ---- E.1 the E8 lattice from the carrier -- DERIVED -------------------------
detH = det(H)
symmetric = all(H[i][j] == H[j][i] for i in range(N) for j in range(N))
even_diag = all(H[i][i] % 2 == 0 for i in range(N))
step("E.1", "the E8 lattice from the carrier: even, unimodular (det 1), rank 8",
     "H = container 06's half_gram; det H = 1; H symmetric; diagonal even -> E8, minimal norm 2",
     ["06"],
     "container 06 built the icosian ring and its codifferent Gram, and showed the HALF-Gram H is "
     "EVEN (integer values, even diagonal), UNIMODULAR (det 1) and rank 8 -- which is E8, the unique "
     "even unimodular lattice in dimension 8. This container consumes H across the declared 6 -> 7 "
     "boundary (INTERFACES.md) and re-verifies its defining invariants cold: det H = 1, symmetric, "
     "even diagonal. E8's minimal norm is 2; its minimal vectors are the ROOTS, built next.",
     "UNIQUE (E8 is the unique even unimodular lattice in dim 8)", "DERIVED",
     {"det_half_gram": int(detH), "symmetric": symmetric, "even_diagonal": even_diag,
      "rank": N, "source": "container 06 half_gram (the 6->7 interface)"},
     check="H is symmetric, even-diagonal, det 1 (the E8 Gram)")
assert detH == 1 and symmetric and even_diag

# ---- E.2 THE 240 ROOTS -- exhaustive norm-2 enumeration -- DERIVED ----------
# Fincke-Pohst: Cholesky-without-sqrt of H gives q[i][i] = d_i, q[i][j] = u_ij (j>i), so
# Q(x) = sum_i d_i (x_i + sum_{j>i} u_ij x_j)^2 -- bound each coordinate in turn, exact.
def cholesky_form(G):
    q = [[Fr(0)] * N for _ in range(N)]
    for i in range(N):
        q[i][i] = Fr(G[i][i]) - sum(q[k][i] ** 2 * q[k][k] for k in range(i))
        for j in range(i + 1, N):
            q[i][j] = (Fr(G[i][j]) - sum(q[k][i] * q[k][j] * q[k][k] for k in range(i))) / q[i][i]
    return q


def enumerate_norm2(G, C=Fr(2)):
    q = cholesky_form(G)
    found = []
    x = [0] * N

    def rec(i, bound):
        s = sum(q[i][j] * x[j] for j in range(i + 1, N))
        rad = bound / q[i][i]
        if rad < 0:
            return
        sr = sqrt(float(rad))
        lo, hi = ceil(float(-s) - sr - 1e-9), floor(float(-s) + sr + 1e-9)
        for xi in range(lo, hi + 1):
            x[i] = xi
            nb = bound - q[i][i] * (Fr(xi) + s) ** 2
            if nb < -Fr(1, 10 ** 6):
                continue
            if i == 0:
                if qform(x) == C:
                    found.append(x[:])
            else:
                rec(i - 1, nb)
        x[i] = 0

    rec(N - 1, C)
    return found


ROOTS = sorted(tuple(r) for r in enumerate_norm2(H))       # canonical order for a stable emit
ROOTS = [list(r) for r in ROOTS]
count = len(ROOTS)
all_norm2 = all(qform(r) == 2 for r in ROOTS)
distinct = len({tuple(r) for r in ROOTS}) == count
step("E.2", "the 240 roots: the minimal (norm-2) vectors of E8, from the norm-2 criterion",
     "{ c in Z^8 : c^T H c = 2 } enumerated exhaustively (Fincke-Pohst) = exactly 240 distinct vectors",
     ["E.1"],
     "THE HEADLINE, and the derivation of 240 from a CRITERION rather than a literal. The E8 roots "
     "are the lattice's minimal vectors -- the c in Z^8 with c^T H c = 2 (H positive-definite, so "
     "the set is finite). An EXACT short-vector enumeration (Fincke-Pohst over the sqrt-free Cholesky "
     "form) searches them exhaustively and returns EXACTLY 240 distinct vectors. This is the count "
     "maths 4 carried as a solved-externally literal; here it is the output of a reproducible "
     "exhaustive search over container 06's own Gram. The 240 vectors are the witness (checkable "
     "against c^T H c = 2); their completeness is the exhaustiveness of the enumeration.",
     "UNIQUE (the norm-2 set is fixed; the enumeration is exhaustive)", "DERIVED",
     {"root_count": count, "all_norm_2": all_norm2, "distinct": distinct, "roots": ROOTS,
      "criterion": "c^T H c = 2 over the E8 Gram H (container 06)"},
     check="exhaustive norm-2 enumeration returns exactly 240 distinct roots, all c^T H c = 2")
assert count == 240 and all_norm2 and distinct

# ---- E.3 the root system is crystallographic (simply-laced) -- DERIVED ------
rootset = {tuple(r) for r in ROOTS}
neg_closed = all(tuple(-x for x in r) in rootset for r in ROOTS)
antipodal_pairs = count // 2
ip_values = sorted({inner(a, b) for a in ROOTS for b in ROOTS})
simply_laced = set(ip_values) <= {-2, -1, 0, 1, 2}
step("E.3", "the root system is crystallographic: norm 2, negation-closed, inner products in {-2..2}",
     "all roots norm 2; -root is a root (120 antipodal pairs); <root, root'> in {-2,-1,0,1,2}",
     ["E.2"],
     "the 240 form a ROOT SYSTEM, checked cold: every root has norm 2 (one length -- E8 is "
     "SIMPLY-LACED); the set is closed under negation, so it splits into 120 antipodal pairs "
     "(+-alpha); and every pairwise inner product <alpha, beta> lies in {-2,-1,0,1,2}, with +-2 only "
     "for beta = +-alpha. That integer-bounded inner product is the CRYSTALLOGRAPHIC (ADE) condition "
     "-- the arithmetic signature of a root system. All exact over H.",
     "UNIQUE (fixed by the root set)", "DERIVED",
     {"negation_closed": neg_closed, "antipodal_pairs": antipodal_pairs,
      "inner_product_values": ip_values, "simply_laced": simply_laced},
     check="negation-closed (120 pairs); inner products exactly {-2,-1,0,1,2}")
assert neg_closed and simply_laced and ip_values == [-2, -1, 0, 1, 2]

# ---- E.4 the kissing number of E8 is 240; optimality is external -- OWED ----
twice_icosians = (count == 2 * ICOSIANS)
step("E.4", "the kissing number of E8 is 240 -- built here as >= 240; optimality is external",
     "240 minimal vectors at norm 2 -> 240 unit spheres kiss in 8-D; = 240 optimal is Viazovska 2016",
     ["E.2"],
     "the 240 roots are the minimal vectors, all at the same minimal norm 2, so 240 equal spheres "
     "kiss a central one in 8 dimensions -- kissing number >= 240, BUILT here (the >= half, exactly "
     "as container 09 builds kissing >= 12 in 3-D). That 240 is OPTIMAL -- the MAXIMUM kissing number "
     "in dimension 8, with E8 the unique optimal packing -- is Viazovska 2016, EXTERNAL accepted "
     "mathematics, cited not machine-checked here (a formalization far beyond reasonable effort; same "
     "tier as the no-13th in 3-D). Noted, held lightly: 240 = 2 * 120 = twice the icosian units of "
     "the carrier (06) -- a relation on the record, not a claim.",
     "OWED (>= 240 built; = 240 optimal is external / cited)", "OWED",
     {"kissing_lower_bound": count, "optimal_is_external": "Viazovska 2016 (dim 8)",
      "built_here": ">= 240 (the minimal-vector count)", "240_is_twice_120": twice_icosians},
     check=None)
assert twice_icosians

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="12-e8-roots", steps=STEPS, grades=GRADES,
           values=dict(half_gram=H, det_half_gram=int(detH), root_count=count,
                       roots=ROOTS, inner_product_values=ip_values,
                       antipodal_pairs=antipodal_pairs, negation_closed=neg_closed,
                       simply_laced=simply_laced, twice_icosians=twice_icosians))

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
              f"({GRADES['DERIVED']} derived, {GRADES['POSTULATE']} postulate, {GRADES['OWED']} owed); "
              f"{count} roots")
        for s in STEPS:
            print(f"  {s['id']:<5} [{s['grade']:<9}] {s['what']}")
