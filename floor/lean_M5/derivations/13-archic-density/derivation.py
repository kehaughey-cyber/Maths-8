#!/usr/bin/env python3
"""Container 13 -- ARCHIC DENSITY: the ball-growth observable |B_r(v)|. Rests on 03.

Step 1 of the physics-bridge arc, built BOTTOM-UP and COLD -- no top-down I/alpha is consulted
here (the convergence with the top-down count is a LATER meeting; this container only defines the
substrate-side observable and proves it is a genuine one). Everything is ADJACENCY-ONLY: once the
edge set is fixed, no distance, embedding or angle is ever consulted again -- a density has to be
regional, and this one is a breadth-first count over the relation itself.

  A.1 the ADJACENCY SUBSTRATE. The icosahedron re-derived COLD from its twelve vertices
      (0, +-1, +-phi) & cyclic -- edges = the pairs at the MINIMAL squared distance, which is the
      pure integer 4 (exact in Z[phi]; the next distances are 4+4phi and 8+4phi, both strictly
      larger, so the minimum needs no irrational comparison). It is a CLOSED degree-5 triangular
      mesh (V=12, E=30, F=20, Euler chi=2) -- the same closed-mesh predicate container 03 uses to
      certify its SELECTED shell, so this re-exhibits 03's object rather than trusting it. Then the
      adjacency web is REFINED by combinatorial 1->4 subdivision (each edge's midpoint a new
      registration, each triangle re-cut into four -- pure combinatorics, no coordinates), giving a
      family R1..R4 of closed webs on the same 2-sphere bound. Euler chi=2 is preserved and the
      degree spectrum is exactly {5: the original twelve, 6: every new vertex} at every level.

  A.2 the OBSERVABLE |B_r(v)|. The number of registrations within r adjacency steps of v --
      breadth-first over the relation, no distance measured. On R1 the mesh is vertex-transitive, so
      every one of the twelve has the identical profile (1, 6, 11, 12): a single vertex, its five
      neighbours, its five second-neighbours, its antipode.

  A.3 FINER THAN THE DEGREE -- not a renaming. (i) |B_1(v)| = deg(v) + 1 EXACTLY, so at r=1 the
      observable is a relabelling of the degree -- and, more usefully, the ball profile always
      DETERMINES the degree, so its partition of the vertices always refines the degree partition.
      (ii) It refines it STRICTLY: on R3 the degree sees 2 classes ({5: twelve, 6: the 150 others})
      while the ball profile sees 4 -- the 150 degree-6 vertices split into 3 profile classes
      (60/30/60). Two degree-6 vertices thus carry DIFFERENT ball profiles ((1,7,18,34) vs
      (1,7,19,35)); the degree calls them identical. A relabelling cannot separate what the degree
      identifies, so ball growth is a strictly finer observable -- this is the test the method
      demands (a new observable must do something the old one provably cannot).

  NOT here (deferred, by scope): the FLAT reference 1+3r(r+1) and the deficit flat - |B_r| (= the
  curvature, signed, conserved at 12*chi) are Step 2 (density-deficit); the physical reading of any
  extremum is Steps 3/10. This container names and validates the observable, nothing downstream.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
from collections import Counter
from itertools import combinations
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


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zmul(x, y):                                        # phi^2 = phi + 1
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def sqdist(u, v):                                      # squared distance of two Z[phi] 3-vectors
    acc = (0, 0)
    for cu, cv in zip(u, v):
        d = zsub(cu, cv)
        acc = zadd(acc, zmul(d, d))
    return acc


# the twelve icosahedron vertices (0, +-1, +-phi) and cyclic, as three Z[phi] coords
VERTS = []
for a in (1, -1):
    for b in (1, -1):
        VERTS.append(((0, 0), (a, 0), (0, b)))          # (0, a, b*phi)
        VERTS.append(((0, b), (0, 0), (a, 0)))          # cyclic
        VERTS.append(((a, 0), (0, b), (0, 0)))          # cyclic
VERTS = list(dict.fromkeys(VERTS))
assert len(VERTS) == 12

# edges = the pairs at MINIMAL squared distance. The distinct squared distances are (4,0)=4,
# (4,4)=4+4phi, (8,4)=8+4phi; the minimum is the pure integer 4, so no irrational compare is needed.
MIN_SQ = (4, 0)
R1_EDGES = sorted((i, j) for i, j in combinations(range(12), 2)
                  if sqdist(VERTS[i], VERTS[j]) == MIN_SQ)


# ---------------------------------------------------------------- graph helpers
def adj_from_edges(edges, n):
    A = {i: set() for i in range(n)}
    for i, j in edges:
        A[i].add(j)
        A[j].add(i)
    return A


def faces_from_adj(A, n):                               # facial triangles = the 3-cliques
    return [(i, j, k) for i, j, k in combinations(range(n), 3)
            if j in A[i] and k in A[i] and k in A[j]]


def edges_of_faces(faces):
    E = set()
    for a, b, c in faces:
        for x, y in ((a, b), (b, c), (c, a)):
            E.add((min(x, y), max(x, y)))
    return E


def adj_from_faces(faces, n):
    A = {i: set() for i in range(n)}
    for a, b, c in faces:
        for x, y in ((a, b), (b, c), (c, a)):
            A[x].add(y)
            A[y].add(x)
    return A


def is_closed_deg5_triangular(n, faces):
    """Container 03's closed-mesh predicate, specialised to degree 5: triangular faces, every edge
    in exactly two faces, every vertex degree 5, Euler V - E + F = 2."""
    E = edges_of_faces(faces)
    tri = all(len({x, y, z}) == 3 for x, y, z in faces)
    edge_in_2 = all(sum(1 for f in faces if e[0] in f and e[1] in f) == 2 for e in E)
    A = adj_from_faces(faces, n)
    deg5 = all(len(A[v]) == 5 for v in range(n))
    euler = (n - len(E) + len(faces) == 2)
    return tri and edge_in_2 and deg5 and euler


def subdivide(n, faces):
    """Combinatorial 1->4 triangle subdivision (adjacency-only; no coordinates). Each edge gets one
    new midpoint vertex; each triangle is re-cut into four. Original vertices keep their labels
    0..n-1 (so the twelve degree-5 vertices persist); new vertices are numbered from n up."""
    edge_id = {}
    nxt = n

    def mid(a, b):
        nonlocal nxt
        e = (min(a, b), max(a, b))
        if e not in edge_id:
            edge_id[e] = nxt
            nxt += 1
        return edge_id[e]

    new_faces = []
    for a, b, c in faces:
        ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
        new_faces += [(a, ab, ca), (b, ab, bc), (c, bc, ca), (ab, bc, ca)]
    return nxt, new_faces


def ball_profile(A, v, rmax):
    """|B_r(v)| for r = 0..rmax: breadth-first over the adjacency relation. No distance is measured
    and no embedding is consulted -- pure adjacency."""
    seen, front, out = {v}, {v}, [1]
    for _ in range(rmax):
        nxt = set()
        for u in front:
            nxt |= A[u]
        front = nxt - seen
        seen |= front
        out.append(len(seen))
    return tuple(out)


# build R1..R4
A1 = adj_from_edges(R1_EDGES, 12)
R1_FACES = faces_from_adj(A1, 12)
meshes = {"R1": (12, R1_FACES)}
n, F = 12, R1_FACES
for k in range(2, 5):
    n, F = subdivide(n, F)
    meshes[f"R{k}"] = (n, F)


def census_of(name):
    n, F = meshes[name]
    A = adj_from_faces(F, n)
    E = sum(len(s) for s in A.values()) // 2
    degc = Counter(len(A[i]) for i in range(n))
    return {"V": n, "E": E, "F": len(F), "euler": n - E + len(F),
            "deg5": degc.get(5, 0), "deg6": degc.get(6, 0)}


census = {name: census_of(name) for name in meshes}

# ---- A.1 the adjacency substrate -- DERIVED ---------------------------------
r1_closed = is_closed_deg5_triangular(12, R1_FACES)
euler_all_2 = all(c["euler"] == 2 for c in census.values())
deg_spectrum_ok = all(c["deg5"] == 12 for c in census.values()) and \
    census["R1"]["deg6"] == 0 and all(census[f"R{k}"]["deg6"] == census[f"R{k}"]["V"] - 12
                                      for k in (2, 3, 4))
step("A.1", "the adjacency substrate: the icosahedron (closed deg-5 triangular mesh) and its "
     "combinatorial refinements R1..R4",
     "V=12,E=30,F=20,chi=2 all deg 5 (03's shell, re-derived cold); 1->4 subdivision keeps chi=2 and "
     "degree spectrum {5: the twelve, 6: the rest}", ["03.4"],
     "the observable needs a substrate to live on, and it must be the substrate's OWN adjacency, not "
     "an imported lattice. So the icosahedron is re-derived COLD: its twelve vertices (0,+-1,+-phi) & "
     "cyclic, edges = the pairs at the minimal squared distance (the pure integer 4 in Z[phi]; the "
     "other distances 4+4phi, 8+4phi are strictly larger, so the minimum is exact without any "
     "irrational comparison). The result satisfies container 03's OWN closed-mesh predicate -- "
     "triangular faces, every edge in two faces, uniform degree 5, Euler chi=2 -- so this re-exhibits "
     "the shell 03 SELECTED (via the three-observer separation), it does not merely trust it. The "
     "adjacency web is then REFINED by combinatorial 1->4 subdivision (an edge-midpoint registration, "
     "each triangle re-cut into four; pure combinatorics, no coordinates): a family R1..R4 of closed "
     "webs on the same 2-sphere bound, each with chi=2 and degree spectrum exactly {5: the original "
     "TWELVE, 6: every refinement vertex}. The twelve degree-5 sites persist at every level -- the "
     "seed Step 2's curvature concentrates on.",
     "UNIQUE UP TO graph isomorphism (the icosahedron; its refinements are determined by it)",
     "DERIVED",
     {"r1_closed_deg5_triangular": r1_closed, "min_sq_distance": list(MIN_SQ),
      "r1_edges": [list(e) for e in R1_EDGES], "census": census,
      "euler_preserved": euler_all_2, "degree_spectrum": "{5: twelve, 6: rest} at every level",
      "degree_spectrum_ok": deg_spectrum_ok},
     check="R1 is a closed deg-5 triangular mesh (chi=2); subdivision keeps chi=2 and {5:12, 6:rest}")
assert r1_closed and euler_all_2 and deg_spectrum_ok
assert census["R1"] == {"V": 12, "E": 30, "F": 20, "euler": 2, "deg5": 12, "deg6": 0}
assert census["R3"] == {"V": 162, "E": 480, "F": 320, "euler": 2, "deg5": 12, "deg6": 150}

# ---- A.2 the ball-growth observable -- DERIVED ------------------------------
r1_profiles = {v: ball_profile(A1, v, 3) for v in range(12)}
r1_profile = r1_profiles[0]
r1_uniform = len(set(r1_profiles.values())) == 1
step("A.2", "the archic-density observable |B_r(v)|: a breadth-first count over adjacency",
     "|B_r(v)| = #{ registrations within r adjacency steps of v }; on R1 every vertex has profile "
     "(1, 6, 11, 12)", ["A.1"],
     "ARCHIC DENSITY is the ball-growth observable: |B_r(v)| is the number of registrations within r "
     "adjacency STEPS of v -- a breadth-first count over the relation itself. It consults NO distance, "
     "NO embedding, NO angle; once A.1 fixes the edges, only adjacency is used. It is REGIONAL (a count "
     "over an r-neighbourhood, not a per-site number) -- which is what a density has to be. On R1 the "
     "mesh is vertex-transitive, so all twelve vertices share the identical profile (1, 6, 11, 12): the "
     "vertex, its 5 neighbours (|B_1|=6), its 5 second-neighbours (|B_2|=11), its antipode (|B_3|=12) -- "
     "the whole icosahedron by radius 3, its graph diameter.",
     "UNIQUE (given the mesh and (v, r) the count is fixed)", "DERIVED",
     {"r1_ball_profile": list(r1_profile), "r1_profile_uniform_over_all_twelve": r1_uniform,
      "reads": "|B_0|=1, |B_1|=6, |B_2|=11, |B_3|=12 (diameter 3)"},
     check="on R1 every vertex has ball profile (1,6,11,12); pure adjacency, regional")
assert r1_profile == (1, 6, 11, 12) and r1_uniform

# ---- A.3 finer than the degree, NOT a renaming -- DERIVED ------------------
# (i) the relabelling identity, on every level
ball1_eq_degplus1 = True
for name, (n, F) in meshes.items():
    A = adj_from_faces(F, n)
    if not all(ball_profile(A, v, 1)[1] == len(A[v]) + 1 for v in range(n)):
        ball1_eq_degplus1 = False
# (ii) strict refinement, witnessed on R3
n3, F3 = meshes["R3"]
A3 = adj_from_faces(F3, n3)
deg3 = {v: len(A3[v]) for v in range(n3)}
prof3 = {v: ball_profile(A3, v, 3) for v in range(n3)}
deg_classes = len(set(deg3.values()))
prof_classes = len(set(prof3.values()))
prof_multiset = Counter(prof3.values())
deg6_profiles = Counter(prof3[v] for v in range(n3) if deg3[v] == 6)
# an explicit witness pair: two degree-6 vertices with distinct ball profiles
deg6_distinct = sorted({prof3[v] for v in range(n3) if deg3[v] == 6})
witness_pair = deg6_distinct[:2]
step("A.3", "finer than the degree, NOT a renaming: |B_1|=deg+1 but the profile strictly refines "
     "degree on R3",
     "|B_1(v)| = deg(v)+1 (a relabelling at r=1, and the profile always determines the degree); on "
     "R3 degree gives 2 classes, ball growth gives 4 (150 deg-6 vertices split 60/30/60)", ["A.2"],
     "the method demands a new observable prove it is not a relabelling of an old one. At r=1, "
     "|B_1(v)| = deg(v)+1 exactly -- so at r=1 ball growth IS the degree, and, generally, the profile "
     "always DETERMINES the degree (its r=1 entry), hence its partition of the vertices always REFINES "
     "the degree partition. The content is that it refines it STRICTLY: on R3 the degree sees only 2 "
     "classes (the twelve at 5, the 150 others at 6), while the ball profile sees 4 -- the 150 "
     "degree-6 vertices split into 3 profile classes (60/30/60). So two degree-6 vertices carry "
     "DIFFERENT ball profiles ((1,7,18,34) vs (1,7,19,35)) that the degree declares identical. A "
     "relabelling cannot separate what the degree identifies; ball growth does. It is a strictly finer "
     "observable -- and (foreshadowing Step 2 only) the class that grows slowest, (1,6,16,31), is "
     "exactly the twelve degree-5 sites: the observable already 'sees' where the curvature will sit.",
     "UNIQUE (the partition refinement is fixed by the meshes)", "DERIVED",
     {"ball1_eq_deg_plus_1_all_levels": ball1_eq_degplus1,
      "witness_level": "R3", "R3_degree_classes": deg_classes, "R3_profile_classes": prof_classes,
      "R3_deg6_profile_classes": len(deg6_profiles),
      "R3_profile_multiset": [[list(p), c] for p, c in sorted(prof_multiset.items())],
      "witness_pair_deg6_profiles": [list(p) for p in witness_pair],
      "strictly_finer": prof_classes > deg_classes},
     check="|B_1|=deg+1 (relabelling); R3: 2 degree classes < 4 ball-profile classes (deg-6 splits 3)")
assert ball1_eq_degplus1 and deg_classes == 2 and prof_classes == 4 and len(deg6_profiles) == 3
assert prof_multiset[(1, 6, 16, 31)] == 12 and witness_pair[0] != witness_pair[1]

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="13-archic-density", steps=STEPS, grades=GRADES,
           values=dict(r1_edges=[list(e) for e in R1_EDGES], census=census,
                       r1_ball_profile=list(r1_profile),
                       R3_profile_multiset=[[list(p), c] for p, c in sorted(prof_multiset.items())],
                       R3_degree_classes=deg_classes, R3_profile_classes=prof_classes,
                       witness_pair_deg6_profiles=[list(p) for p in witness_pair]))

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
