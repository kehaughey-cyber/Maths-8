#!/usr/bin/env python3
"""Container 03 -- dimensional emergence. Rung 3, rests on 01 (adjacency) and 02 (the triad).

RETRACTION AND CORRECTION. maths 4's first rung 3 (RUNG3-TETRAHEDRON-MINIMUM) was RETRACTED for
reading "n mutually related distinctions" as a CLIQUE. That retraction was right -- but a
retraction kills the claim it names, not the question, and the CORRECTION already existed,
machine-checked, and went unconnected for weeks (the ledger's own lesson: "an absent derivation
is not a derived absence"). This container carries BOTH.

The correction is REFRAME-CLOSURE-FORCING (maths 4 formal/Closure/TwelveForced.lean) plus
SELECTION-BY-RELATIONAL-SEPARATION (Separation.lean):

  - Closure ITSELF -- Euler (V+F=E+2), triangular faces (3F=2E), uniform degree d (dV=2E) --
    with NO CLIQUE forces exactly three closed shells: (d,V) = (3,4) tetrahedron, (4,6)
    octahedron, (5,12) icosahedron; d>=6 never closes. The shape IS forced.
  - The three-observer condition SELECTS the icosahedron: a pair of vertices is 'separated' only
    when some THIRD relates differently to each. Exactly the icosahedron has every pair separated
    (tetra fails all 6 pairs, octa 3 antipodal, icosa 0). d=5, and the twelve, are forced -- and
    this is rung 2's triad doing the selecting.
  - Dimension >= 3: the minimum closure, the tetrahedron, is 4 MUTUALLY adjacent registrations
    (the only clique among the three), i.e. 4 equidistant points, which force ambient dimension
    at least three (via the geometric-balance bridge). The one thing still OPEN is the UPPER
    bound (that it is 3 and not more).

Grades DERIVED / POSTULATE / OWED, first-class. `--check` recomputes the DERIVED steps.
Sibling route Kevin also names (2pi -> 4pi = 2pi+2pi, sphere/solid-angle emergence via the
double cover) lives on the phase/double-cover tier; noted, not this container's derivation.
"""

import json
import sys
from itertools import combinations

STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------- the three closures, as explicit combinatorial meshes (maths 4) -------
TETRA = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
OCTA = [(0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)]
ICOSA = [(0, 1, 2), (0, 1, 7), (0, 2, 6), (0, 6, 8), (0, 7, 8), (1, 2, 5), (1, 3, 5), (1, 3, 7),
         (2, 4, 5), (2, 4, 6), (3, 5, 9), (3, 7, 11), (3, 9, 11), (4, 5, 9), (4, 6, 10),
         (4, 9, 10), (6, 8, 10), (7, 8, 11), (8, 10, 11), (9, 10, 11)]


def edges(faces):
    E = set()
    for a, b, c in faces:
        for x, y in [(a, b), (a, c), (b, c)]:
            E.add((min(x, y), max(x, y)))
    return E


def is_closed_mesh(V, d, faces):
    E = edges(faces)
    tri = all(x < V and y < V and z < V and len({x, y, z}) == 3 for x, y, z in faces)
    edge2 = all(sum(1 for f in faces if e[0] in f and e[1] in f) == 2 for e in E)
    deg = all(sum(1 for e in E if v in e) == d for v in range(V))
    euler = (V + len(faces) == len(E) + 2)
    return tri and edge2 and deg and euler


def unseparated(V, faces):                       # pairs NOT separated by a third vertex
    E = edges(faces)
    A = lambda u, v: (min(u, v), max(u, v)) in E
    return sum(1 for v, w in combinations(range(V), 2)
               if not any(A(u, v) != A(u, w) for u in range(V) if u not in (v, w)))


# ---- 3.1 geometry is derived, not assumed -- POSTULATE ----------------------
step("3.1", "geometry is derived -- dimension must emerge from relational structure",
     "no space or metric assumed; 'surface' and 'closure' read combinatorially", [],
     "Axiom 3: space and time are not posited; geometric structure emerges from stable "
     "relational configurations. So dimension must be DERIVED from adjacency -- and that "
     "discipline is exactly what exposes an imposed clique as an assumption, not a derivation.",
     "framing", "POSTULATE", {"geometry_is_combinatorial": True}, check=None)

# ---- 3.2 the retraction: the clique was wrong -- DERIVED ---------------------
def tri_count(n, adj):
    return sum(1 for i, j, k in combinations(range(n), 3) if adj(i, j) and adj(i, k) and adj(j, k))
clique = lambda i, j: i != j
path = lambda i, j: abs(i - j) == 1
step("3.2", "the retraction: a clique closes at 4, but registration adjacency is a path",
     "K_n closes uniquely at 4; the local path (rung 1) has no triangles", [],
     "maths 4's first rung 3 read 'mutually related' as a CLIQUE and got the tetrahedron. But "
     "registration N+1 is adjacent only to N (rung 1), a PATH, which has no triangles and closes "
     "nowhere. The tetrahedron-from-a-clique was geometry imposed. RUNG3-TETRAHEDRON-MINIMUM was "
     "retracted for exactly this -- correctly.",
     "the clique premise fails", "DERIVED",
     {"clique_triangles_at_4": tri_count(4, clique), "path_triangles_at_4": tri_count(4, path),
      "retracted": True}, check="clique has triangles, the local path has none")
assert tri_count(4, clique) == 4 and tri_count(4, path) == 0

# ---- 3.3 the correction: closure forces the trichotomy, NO clique -- DERIVED --
# For uniform degree d, closed triangular: E=dV/2, F=dV/3, Euler V+F=E+2 => V=12/(6-d).
trich = {}
for d in range(3, 8):
    if d < 6 and (12 % (6 - d) == 0):
        trich[d] = 12 // (6 - d)
witnesses = {"tetra": is_closed_mesh(4, 3, TETRA), "octa": is_closed_mesh(6, 4, OCTA),
             "icosa": is_closed_mesh(12, 5, ICOSA)}
step("3.3", "the correction: closure alone forces exactly three shells (no clique)",
     "Euler (V+F=E+2) + triangular (3F=2E) + uniform degree d (dV=2E) => V = 12/(6-d)", ["3.1"],
     "REFRAME-CLOSURE-FORCING: with NO clique assumed, the three counting identities of a closed "
     "uniform triangular mesh force (d,V) = (3,4) tetrahedron, (4,6) octahedron, (5,12) "
     "icosahedron, and d>=6 never closes. The shape IS forced -- machine-checked at maths 4. The "
     "three shells are exhibited as explicit meshes, each verified closed with Euler characteristic 2.",
     "UNIQUE (exactly three)", "DERIVED",
     {"trichotomy": trich, "witnesses_verified": witnesses,
      "d_ge_6_impossible": all(d not in trich for d in range(6, 8))},
     check="d=3->V=4, d=4->V=6, d=5->V=12; d>=6 impossible; all three meshes verify")
assert trich == {3: 4, 4: 6, 5: 12} and all(witnesses.values())

# ---- 3.4 selection: the three-observer condition picks the icosahedron -- DERIVED
sep = {"tetra": (4, unseparated(4, TETRA)), "octa": (6, unseparated(6, OCTA)),
       "icosa": (12, unseparated(12, ICOSA))}
step("3.4", "the triad selects the icosahedron: only it has every pair separated by a third",
     "separated(v,w) := some third vertex relates differently to each; unseparated count = 0 only for icosa",
     ["3.3", "3.2"],
     "SELECTION-BY-RELATIONAL-SEPARATION: a pair of vertices is distinguished only when a THIRD "
     "relates differently to each -- rung 2's three-observer condition. Of the three closures, "
     "exactly the icosahedron separates every pair (tetra fails all 6 pairs, octa 3 antipodal, "
     "icosa 0). d=5 and the TWELVE are forced, not chosen -- and it is the triad doing it.",
     "UNIQUE (the icosahedron)", "DERIVED",
     {"unseparated_pairs": sep, "selected": "icosahedron", "twelve_forced": True},
     check="unseparated: tetra 6, octa 3, icosa 0")
assert sep["icosa"][1] == 0 and sep["tetra"][1] == 6 and sep["octa"][1] == 3

# ---- 3.5 dimension >= 3 -- DERIVED lower bound (rests on a bridge POSTULATE) --
tetra_mutually_adjacent = all((min(i, j), max(i, j)) in edges(TETRA) for i, j in combinations(range(4), 2))
step("3.5", "dimension is at least three (the lower bound)",
     "the minimum closure = tetrahedron = 4 mutually adjacent = 4 equidistant => dim >= 3", ["3.3"],
     "the tetrahedron is the only one of the three closures that is a complete graph -- its 4 "
     "registrations are MUTUALLY adjacent, hence 4 equidistant points, which force ambient "
     "dimension at least three. The adjacency-to-equidistance step is the geometric-balance "
     "bridge (a POSTULATE), so the lower bound is derived on top of that stated bridge, not "
     "from nothing. THREE-DIMENSIONS-LOWER-BOUND.",
     "dim >= 3", "DERIVED",
     {"tetra_mutually_adjacent": tetra_mutually_adjacent, "equidistant_points": 4,
      "ambient_dimension_at_least": 3, "rests_on_bridge_postulate": True},
     check="the tetrahedron is a clique of 4 -> 4 equidistant -> dim >= 3")
assert tetra_mutually_adjacent

# ---- 3.6 the upper bound is NOT established -- a CHECKED negative -- DERIVED --
# Searched the maths 4 ledger (2026-08-19): the upper bound was ATTEMPTED
# (THREE-IS-THE-SATURATED-KISSING-DIMENSION) and RETRACTED one day later; the settled state is
# DIMENSION-UPPER-BOUND-NOT-ESTABLISHED, with a machine-checked negative and an exact counterexample.
import math
sphere_covered_by_12 = 6 * (1 - math.sqrt(3) / 2)          # 6 - 3*sqrt3 ~ 0.804
sphere_uncovered = 1 - sphere_covered_by_12                # 3*sqrt3 - 5 ~ 0.196
d4_roots = [tuple(v) for i in range(4) for j in range(i + 1, 4)
            for si in (1, -1) for sj in (1, -1)
            for v in [[si if k == i else sj if k == j else 0 for k in range(4)]]]
d4_all_admissible = all(sum(a * b for a, b in zip(u, w)) <= 1
                        for x, u in enumerate(d4_roots) for w in d4_roots[x + 1:])
step("3.6", "the upper bound is NOT established -- and that is a checked negative, not an absent one",
     "sphere not saturated by twelve (3*sqrt3 - 5 uncovered); D4 admits >=13 neighbours at d=4",
     ["3.5"],
     "the upper bound (dim = 3, not more) was ATTEMPTED via 'twelve fits and no thirteenth fits' "
     "and RETRACTED: the substrate's no-thirteenth is TOPOLOGICAL (Euler gives exactly twelve at "
     "any d -- a census), never METRIC (a thirteenth could not FIT). Only a metric one bounds the "
     "dimension. Two checked facts settle it: (a) SPHERE-IS-NOT-SATURATED-BY-TWELVE -- twelve caps "
     "of half-angle pi/6 leave the sphere 3*sqrt3 - 5 ~ 19.6% uncovered (the circle saturates, the "
     "sphere frustrates); (b) the D4 root system's 24 roots are pairwise >= 60 degrees, so >=13 fit "
     "at d=4. So d=4 is NOT excluded and dim = 3 does NOT follow. dim >= 3 stands; the upper bound "
     "does not. Unlike the clique, there is no disconnected repair -- this negative is the answer.",
     "dim >= 3; upper bound not established", "DERIVED",
     {"sphere_uncovered_by_12": "3*sqrt3 - 5 (about 0.196)",
      "sphere_uncovered_value": round(sphere_uncovered, 4),
      "d4_roots": len(d4_roots), "d4_all_pairwise_ge_60deg": d4_all_admissible,
      "d4_excluded": False, "lower_bound": 3, "upper_bound": "NOT established (checked)"},
     check="sphere left ~19.6% uncovered by twelve; D4 admits >=13 neighbours at d=4")
assert abs(sphere_uncovered - (3 * math.sqrt(3) - 5)) < 1e-9 and d4_all_admissible and len(d4_roots) == 24

# ---- 3.7 the one thing genuinely owed -- OWED -------------------------------
step("3.7", "what is genuinely owed: a METRIC no-thirteenth from the substrate",
     "a substrate statement that the bound admits no thirteenth neighbour BY GEOMETRY", ["3.6"],
     "the only route to dim = 3 that is not circular would be a substrate-native METRIC saturation "
     "-- the bound admitting no thirteenth by geometry, not by the topological census. Nothing in "
     "the corpus supplies one, and the checked negative above says the naive route (the phase "
     "circle's thirteenth) does not transfer to the sphere. This, and only this, is OPEN.",
     "OWED", "OWED", {"needed": "a metric no-thirteenth from the substrate", "present": False}, check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="03-dimensional-emergence", steps=STEPS, grades=GRADES,
           values=dict(trichotomy=trich, witnesses=witnesses, unseparated=sep,
                       selected="icosahedron", dim_lower_bound=3,
                       upper_bound_established=False, d4_excluded=False, d4_roots=len(d4_roots),
                       sphere_uncovered_by_12="3*sqrt3 - 5 (~0.196)",
                       clique_triangles_at_4=tri_count(4, clique), path_triangles_at_4=tri_count(4, path),
                       faces=dict(tetra=[list(f) for f in TETRA], octa=[list(f) for f in OCTA],
                                  icosa=[list(f) for f in ICOSA]),
                       d4=[list(r) for r in d4_roots]))

if __name__ == "__main__":
    import pathlib
    p = pathlib.Path(__file__).parent / "derivation.json"
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
