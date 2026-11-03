#!/usr/bin/env python3
"""Container 11 -- the ICOSAHEDRON interior (the rank-6 icosahedral module). Rests on 03.

NUMBER IS A BUILD-ORDER LABEL. Conceptually this is the rung-5/6 icosahedral module M -- the
Z[phi]-span of the twelve icosahedral directions (0, +-1, +-phi) and cyclic -- built now, positioned
by its INCLUSION into the carrier (container 06): doubled, 2M sits inside the icosian ring's
pure-imaginary sublattice at index 32 (the 5->6 interface, already declared in INTERFACES.md and
recomputed cold by interface_probe.py; NOT re-derived here). The `05` dir label went to the
geometric-balance bridge, which owns Container05; this interior takes the next free build-order slot,
exactly as 07 (rung 4.5) and 09 (rung 6) do.

The icosahedron was SELECTED at container 03 (the three-observer separation condition picks the
12-vertex shell). This container builds that shell's INTERIOR structure, all exact in
Z[phi] = { a + b*phi : a,b in Z }, phi^2 = phi + 1, and all Mathlib-free / zero-axiom (decide):

  I.1 the TRANSFER RULE: the field norm N(a+b phi) = a^2 + ab - b^2 is multiplicative; the trace is
      2a+b. Integer field norms are what make the overlaps' norms (9,16,5) meaningful -- the
      quantization of the transfer rule IS the integrality of N.
  I.2 the RANK OBSTRUCTION: the twelve directions are six and their negatives, so the module has rank
      AT MOST 6; the six-direction determinant is +-8 != 0, so rank EXACTLY 6. rank 6 < 8 REFUTES
      identifying the 3-D overlaps with E8 lattice vectors (E8 has rank 8) -- derived, not asserted.
  I.3 the THREE FRUSTRATION OVERLAPS: the first overlapping difference at shells 2,3,4 has squared
      length 6-3phi, 20-12phi, 18-11phi (exact Z[phi]) and INTEGER field norm 9, 16, 5 -- each BELOW
      the contact distance^2 phi+2. The overlap witnesses are found by an external search; their
      lengths and norms are computed here.
  I.4 the CUBOCTAHEDRON IS NOT A TRIANGULATION: the FCC kissing shell (12 vertices, each degree 4)
      has 24 edges and, by Euler, 14 faces -- but only 8 are triangles; 6 are squares. Since
      triangular faces are the closure trichotomy's hypothesis, this is the LOAD-BEARING exclusion
      that keeps the cuboctahedron out (both it and the icosahedron are relationally separated).
  I.5 the 12+20 MINIMAL SHELL: at codifferent trace-form norm 3, the rank-6 lattice's minimal
      vectors split 12 + 20 -- twelve at squared length phi+2 (the ICOSAHEDRON directions) and twenty
      at 6-3phi (the DODECAHEDRON directions): same trace-norm, different squared lengths, the
      internal trade. AND the shell-2 overlap (6-3phi) is itself a dodecahedral minimal vector -- the
      substrate's first failure to close is a minimal vector of its own lattice.

Grades: DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- exact Z[phi]
def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)      # phi^2 = phi + 1


def znorm(x):                                          # field norm N(a+b phi) = a^2 + ab - b^2
    a, b = x
    return a * a + a * b - b * b


def ztrace(x):                                         # field trace Tr(a+b phi) = 2a + b
    return 2 * x[0] + x[1]


def trace_form(x):                                     # Tr(delta * x), delta = phi/sqrt5 -> a + b
    return x[0] + x[1]


def sqlen(v):                                          # |v|^2 in Z[phi] for a 3-vector of Z[phi]
    acc = (0, 0)
    for c in v:
        acc = zadd(acc, zmul(c, c))
    return acc


def flat(v):                                           # 3 Z[phi] coords -> 6 ints
    return [x for c in v for x in c]


def det(M):                                            # exact integer determinant
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


PHI = (1 + 5 ** 0.5) / 2                                # numeric, for the below-contact ordering only


def num(z):
    return z[0] + z[1] * PHI


# the six icosahedral directions (0, +-1, +-phi) and cyclic, as three Z[phi] coords
DIRS6 = [[(0, 0), (1, 0), (0, 1)], [(1, 0), (0, 1), (0, 0)], [(0, 1), (0, 0), (1, 0)],
         [(0, 0), (1, 0), (0, -1)], [(1, 0), (0, -1), (0, 0)], [(0, -1), (0, 0), (1, 0)]]
DIRS12 = DIRS6 + [[(-a, -b) for (a, b) in d] for d in DIRS6]   # 12 = six and their negatives

# ---- I.1 the transfer rule (field norm is multiplicative) -- DERIVED ---------
norm_mult = (znorm(zmul((6, -3), (20, -12))) == znorm((6, -3)) * znorm((20, -12)))
phi_facts = {"N_phi": znorm((0, 1)), "Tr_phi": ztrace((0, 1)),
             "N_one": znorm((1, 0)), "Tr_one": ztrace((1, 0))}
step("I.1", "the transfer rule: the Z[phi] field norm is multiplicative",
     "N(a+b phi) = a^2 + ab - b^2 ; N(xy) = N(x)N(y) ; Tr(a+b phi) = 2a+b", [],
     "the icosahedral module lives in Z[phi], and the object that makes its geometry ARITHMETIC is "
     "the field norm N(a+b phi) = a^2 + ab - b^2 (with N(phi) = -1, N(1) = 1) -- it is "
     "MULTIPLICATIVE, so every squared length in the module has an INTEGER field norm. That integer "
     "is the transfer rule's quantization: the overlaps' norms 9,16,5 (I.3) are integers precisely "
     "because N is multiplicative on exact Z[phi] squared lengths. Foundational and exact.",
     "UNIQUE (the field norm and trace are fixed by Z[phi])", "DERIVED",
     {"norm_multiplicative": norm_mult, "phi_facts": phi_facts},
     check="N is multiplicative; N(phi)=-1, Tr(phi)=1")
assert norm_mult and phi_facts == {"N_phi": -1, "Tr_phi": 1, "N_one": 1, "Tr_one": 2}

# ---- I.2 the rank obstruction (rank exactly 6) -- DERIVED --------------------
twelve_distinct = len({tuple(flat(d)) for d in DIRS12}) == 12
neg_structure = all(DIRS12[6 + i] == [(-a, -b) for (a, b) in DIRS6[i]] for i in range(6))
six_det = det([flat(d) for d in DIRS6])                # +-8 -> rank exactly 6
rank_exactly_6 = six_det != 0
step("I.2", "the rank obstruction: the module has rank EXACTLY 6 (six-direction det = 8)",
     "twelve = six and their negatives (rank <= 6); det(six flattened) = 8 != 0 (rank = 6); 6 < 8",
     ["I.1"],
     "the twelve directions are the six DIRS and their negatives, so the module they Z-span has rank "
     "AT MOST 6. And the 6x6 determinant of the six directions (flattened to six integers each) is 8, "
     "nonzero -- so they are Z-independent and the rank is EXACTLY 6. This is the RANK OBSTRUCTION: "
     "rank 6 < 8 = rank(E8), which REFUTES identifying the 3-D icosahedral overlaps with E8 lattice "
     "vectors. Derived cold (the determinant is recomputed here), not asserted; and not copying "
     "maths 4's externally-solved value -- the determinant is computed from the directions.",
     "UNIQUE (the rank is exactly 6; the E8 identification is refuted)", "DERIVED",
     {"twelve_distinct": twelve_distinct, "six_and_negatives": neg_structure,
      "six_direction_det": int(six_det), "rank_exactly_6": rank_exactly_6,
      "refutes": "rank 6 < 8 = rank(E8)"},
     check="twelve = six + negatives; det(six) = 8 != 0 so rank exactly 6")
assert twelve_distinct and neg_structure and int(six_det) == 8

# ---- I.3 the three frustration overlaps -- DERIVED --------------------------
OVERLAPS = {"shell2": [(-1, 0), (2, -1), (0, 0)],
            "shell3": [(4, -2), (0, 0), (0, 0)],
            "shell4": [(2, -1), (0, 0), (3, -2)]}
CONTACT = (2, 1)                                        # |(0,1,phi)|^2 = phi + 2
overlap_data = {}
for k, ov in OVERLAPS.items():
    s = sqlen(ov)
    overlap_data[k] = {"sq_len": list(s), "field_norm": znorm(s),
                       "below_contact": num(s) < num(CONTACT)}
norms_expected = [overlap_data["shell2"]["field_norm"], overlap_data["shell3"]["field_norm"],
                  overlap_data["shell4"]["field_norm"]]
step("I.3", "the three frustration overlaps: sq-lengths 6-3phi, 20-12phi, 18-11phi (norms 9,16,5)",
     "sqLen(overlap_k) in {6-3phi, 20-12phi, 18-11phi}; field norms 9,16,5; all < contact phi+2",
     ["I.1"],
     "the FRUSTRATION: the first overlapping difference vector found at shells 2, 3 and 4 of the "
     "module has squared length exactly 6-3phi, 20-12phi, 18-11phi (exact Z[phi]) -- each with "
     "INTEGER field norm 9, 16, 5 by the transfer rule (I.1), and each strictly BELOW the contact "
     "distance^2 phi+2. Being below contact is exactly what makes them overlaps (failures to keep "
     "the minimum separation). The overlap witnesses are found by an EXTERNAL search over shells "
     "(scope: the recursion producing them is not built here); their squared lengths and norms are "
     "COMPUTED here from the witnesses, exact.",
     "CHOSEN (the overlap witnesses; their squared lengths and norms are UNIQUE, computed)",
     "DERIVED",
     {"overlaps": overlap_data, "contact_sq": list(CONTACT), "field_norms": norms_expected},
     check="overlaps have sq-len 6-3phi/20-12phi/18-11phi, norms 9/16/5, all below phi+2")
assert norms_expected == [9, 16, 5] and all(d["below_contact"] for d in overlap_data.values())

# ---- I.4 the cuboctahedron is not a triangulation -- DERIVED ----------------
CUBO = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0),
        (1, 0, 1), (1, 0, -1), (-1, 0, 1), (-1, 0, -1),
        (0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1)]


def d2(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3))


degs = [sum(1 for b in CUBO if b != a and d2(a, b) == 2) for a in CUBO]
E = sum(degs) // 2
F = E + 2 - 12                                          # Euler: V - E + F = 2, V = 12
triangles = sum(1 for a in CUBO for b in CUBO for c in CUBO
                if d2(a, b) == 2 and d2(a, c) == 2 and d2(b, c) == 2) // 6
squares = F - triangles
step("I.4", "the cuboctahedron is NOT a triangulation: 8 triangles + 6 squares",
     "12 vertices, each degree 4; E = 24; Euler F = 14; only 8 faces are triangles, 6 are squares",
     ["I.2"],
     "the cuboctahedron (the FCC kissing shell, (+-1,+-1,0) and permutations) has twelve vertices "
     "and twelve neighbours, JUST LIKE the icosahedron, and it even tiles space. What keeps it OUT "
     "of the closure trichotomy is not separation (both shells are relationally separated) but "
     "TRIANGULATION: each vertex has degree 4, so E = 24, and Euler forces F = 14 -- but only EIGHT "
     "of those faces are triangles; the other SIX are squares. Triangular faces are the trichotomy's "
     "hypothesis (the triangle is the geometric primitive), so the frustration traces to the "
     "primitive. This is the LOAD-BEARING exclusion. All integer, exact.",
     "UNIQUE (the face census is fixed by the configuration)", "DERIVED",
     {"vertices": 12, "all_degree_4": all(x == 4 for x in degs), "edges": E, "faces": F,
      "triangles": triangles, "squares": squares},
     check="cuboctahedron: deg 4, E=24, F=14, 8 triangles + 6 squares")
assert all(x == 4 for x in degs) and E == 24 and F == 14 and triangles == 8 and squares == 6

# ---- I.5 the 12 + 20 minimal shell -- DERIVED -------------------------------
def vadd(u, v):
    return [zadd(a, b) for a, b in zip(u, v)]


def vsmul(k, v):
    return [(k * c[0], k * c[1]) for c in v]


def combine(coef):
    acc = [(0, 0), (0, 0), (0, 0)]
    for k, d in zip(coef, DIRS6):
        acc = vadd(acc, vsmul(k, d))
    return acc


shell = {}
for coef in itertools.product((-1, 0, 1), repeat=6):    # the [-1,1]^6 coefficient box
    v = combine(coef)
    s = sqlen(v)
    if trace_form(s) == 3:                              # minimal trace-form norm
        shell[tuple(flat(v))] = s
n_icosa = sum(1 for s in shell.values() if s == (2, 1))       # phi + 2
n_dodeca = sum(1 for s in shell.values() if s == (6, -3))     # 6 - 3phi
shell_total = len(shell)
overlap2_is_dodeca_minimal = sqlen(OVERLAPS["shell2"]) == (6, -3)
step("I.5", "the 12 + 20 minimal shell: 12 icosahedron (phi+2) + 20 dodecahedron (6-3phi)",
     "at trace-form norm 3: 12 vectors at sq-len phi+2, 20 at 6-3phi; same trace-norm, different "
     "squared lengths", ["I.1", "I.3"],
     "the rank-6 lattice's minimal shell (vectors at the minimal codifferent trace-form norm 3, over "
     "the [-1,1]^6 coefficient box) SPLITS 12 + 20: twelve vectors have squared length phi+2 (the "
     "ICOSAHEDRON directions) and twenty have 6-3phi (the DODECAHEDRON directions). SAME trace-form "
     "norm, DIFFERENT squared lengths -- the internal trade of the transfer rule, appearing at rank "
     "6. AND the shell-2 overlap (I.3, squared length 6-3phi) is itself one of the twenty "
     "dodecahedral minimal vectors: the substrate's first failure to close is a minimal vector of "
     "its own lattice. Exact in Z[phi]; no real arithmetic needed to see the split.",
     "UNIQUE split (12+20); the count is >= 32, scoped to the [-1,1] box (a search, not completeness)",
     "DERIVED",
     {"trace_form_norm": 3, "shell_total_in_box": shell_total, "icosahedron_count": n_icosa,
      "dodecahedron_count": n_dodeca, "icosa_sq_len": [2, 1], "dodeca_sq_len": [6, -3],
      "overlap2_is_dodecahedral_minimal": overlap2_is_dodeca_minimal,
      "scope": "coefficients in [-1,1]^6; read 32 as 'at least 32 with exactly this split'"},
     check="minimal shell splits 12 (phi+2) + 20 (6-3phi) at trace-form norm 3")
assert shell_total == 32 and n_icosa == 12 and n_dodeca == 20 and overlap2_is_dodeca_minimal

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="11-icosahedron", steps=STEPS, grades=GRADES,
           values=dict(six_direction_det=int(six_det),
                       overlap_field_norms=norms_expected, contact_sq=list(CONTACT),
                       cuboctahedron=dict(edges=E, faces=F, triangles=triangles, squares=squares),
                       shell_total=shell_total, icosahedron_count=n_icosa,
                       dodecahedron_count=n_dodeca,
                       dirs12=[flat(d) for d in DIRS12]))

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
