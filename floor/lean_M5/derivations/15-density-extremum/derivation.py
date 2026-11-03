#!/usr/bin/env python3
"""Container 15 -- DENSITY EXTREMUM: the two signed directions. Rests on 14, 13, 03.

Step 3 of the physics-bridge arc. The deficit (14) is SIGNED; this container reads its extrema as two
directions and NAMES the physical ends they COULD correspond to -- as a possibility, NOT a confirmed
identification. Kevin's steer (2026-08-25): "note what it is and the possibility; hold off confirmation
until warranted. At this point it is possible but not confirmed. Name the directions, keep values
deferred." So: C.1 and C.2 are DERIVED mathematics; C.3 is a POSTULATE-graded NAMED POSSIBILITY with
NO value computed and NO downstream premise use.

  C.1 the DENSITY EXTREMUM. Archic density rho(v) = |B_r(v)| (the observable of 13). Across the
      substrate rho attains its MINIMUM exactly at the twelve degree-5 sites -- rho_min(r) =
      flat_ball(r) - r(r+1)/2 (the maximum deficit, the maximum positive curvature) -- and its MAXIMUM
      at the flattest degree-6 sites, rho_max(r) = flat_ball(r), the flat value (attained cleanly at
      R4, where a degree-6 vertex sits far enough from every one of the twelve to have deficit 0). So
      there is a real density gradient rho_min < rho_max, from the twelve up to the flat mirror.

  C.2 the SIGNED MIRROR and what THIS substrate realizes. D = 0 (a degree-6 site, deficit zero) is the
      mirror between the two signs. Two facts, kept distinct (the first is a law, the second is this
      construction's): (a) Gauss-Bonnet fixes the TOTAL angle deficit at 12*chi = 24 > 0, so a closed
      genus-0 surface must be NET positively curved -- a law of the topology. (b) THIS substrate (the
      geodesic subdivision of the icosahedron) happens to have every vertex degree <= 6 -- no
      negative-curvature (degree>6) site ANYWHERE -- so here rho never exceeds flat. (b) is NOT forced by
      (a): a closed sphere may carry local saddle vertices as long as they are outweighed; ours has none
      by construction, not by law. So the maximum-density end is simply NOT REALIZED on this substrate --
      it is not a "complement" or reflection of the minimum-density side (the two signs are independent
      regions, not mirror images), and it is not forbidden in general. A region of rho > flat requires a
      DIFFERENT geometry (one carrying degree>6 sites); that geometry is real and buildable, and this
      container neither builds it nor commits to how the high-density regime is reached.

  C.3 the NAMED POSSIBILITY (POSTULATE; values deferred; possible, NOT confirmed). The arc's working
      correspondence (handoff, from maths-4 clues -- reference only, not derived here):
        - MINIMUM archic density  <->  the VACUUM / dark-energy direction  (realized here, at the twelve);
        - MAXIMUM archic density  <->  the BLACK-HOLE direction (where the Schwarzschild radius attaches,
          per the clue) -- NOT realized on this substrate (a different, buildable geometry, not built here).
      This is NAMED as a possibility to be tested, NOT asserted. NO value is computed or fitted; even
      the ASSIGNMENT (which extremum <-> which physics) is part of what awaits warrant -- as is the
      GEOMETRY of the max-density end (whether it is negative curvature or another high-density mechanism
      is not decided here). Warrant = the derivation closing AND the top-down count meeting the bottom-up
      (the arc's standing condition). No downstream container may use this correspondence as a premise
      until it is confirmed.

  NOT here: the frustration dynamo epsilon != 0 (Step 4); the Stones / the ruler alpha (Steps 5-6); any
  rho_Lambda VALUE (Step 10, OWED). This container states the two directions and the mirror, and holds
  the physical naming as an explicit possibility.

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


# ---------------------------------------------------------------- substrate (cold, as 13/14)
def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def sqdist(u, v):
    acc = (0, 0)
    for cu, cv in zip(u, v):
        dd = zsub(cu, cv)
        acc = zadd(acc, zmul(dd, dd))
    return acc


VERTS = []
for a in (1, -1):
    for b in (1, -1):
        VERTS.append(((0, 0), (a, 0), (0, b)))
        VERTS.append(((0, b), (0, 0), (a, 0)))
        VERTS.append(((a, 0), (0, b), (0, 0)))
VERTS = list(dict.fromkeys(VERTS))
assert len(VERTS) == 12
R1_EDGES = sorted((i, j) for i, j in combinations(range(12), 2)
                  if sqdist(VERTS[i], VERTS[j]) == (4, 0))


def adj_from_edges(edges, n):
    A = {i: set() for i in range(n)}
    for i, j in edges:
        A[i].add(j)
        A[j].add(i)
    return A


def faces_from_adj(A, n):
    return [(i, j, k) for i, j, k in combinations(range(n), 3)
            if j in A[i] and k in A[i] and k in A[j]]


def adj_from_faces(faces, n):
    A = {i: set() for i in range(n)}
    for a, b, c in faces:
        for x, y in ((a, b), (b, c), (c, a)):
            A[x].add(y)
            A[y].add(x)
    return A


def subdivide(n, faces):
    edge_id = {}
    nxt = n

    def mid(a, b):
        nonlocal nxt
        e = (min(a, b), max(a, b))
        if e not in edge_id:
            edge_id[e] = nxt
            nxt += 1
        return edge_id[e]

    nf = []
    for a, b, c in faces:
        ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
        nf += [(a, ab, ca), (b, ab, bc), (c, bc, ca), (ab, bc, ca)]
    return nxt, nf


def ball_size(A, v, r):
    seen, front = {v}, {v}
    for _ in range(r):
        nxt = set()
        for u in front:
            nxt |= A[u]
        front = nxt - seen
        seen |= front
    return len(seen)


def flat_ball(r):
    return 1 + 3 * r * (r + 1)


def tri(r):
    return r * (r + 1) // 2


A1 = adj_from_edges(R1_EDGES, 12)
R1_FACES = faces_from_adj(A1, 12)
meshes = {"R1": (12, R1_FACES)}
n, F = 12, R1_FACES
for k in range(2, 5):
    n, F = subdivide(n, F)
    meshes[f"R{k}"] = (n, F)
adjs = {name: adj_from_faces(F, n) for name, (n, F) in meshes.items()}
degs = {name: {v: len(adjs[name][v]) for v in range(meshes[name][0])} for name in meshes}

# ---- C.1 the density extremum -- DERIVED ------------------------------------
# On R4 (the freest level up to r=4): rho(v) = |B_r(v)|; find the extrema and their degree classes.
r4 = "R4"
A4, deg4, n4 = adjs[r4], degs[r4], meshes[r4][0]
rho_min, rho_max, argmin_deg, argmax_deg = {}, {}, {}, {}
for r in (1, 2, 3, 4):
    rr = {v: ball_size(A4, v, r) for v in range(n4)}
    lo, hi = min(rr.values()), max(rr.values())
    rho_min[r], rho_max[r] = lo, hi
    argmin_deg[r] = sorted({deg4[v] for v in rr if rr[v] == lo})
    argmax_deg[r] = sorted({deg4[v] for v in rr if rr[v] == hi})
rho_min_list = [rho_min[r] for r in (1, 2, 3, 4)]
rho_max_list = [rho_max[r] for r in (1, 2, 3, 4)]
min_at_twelve = all(argmin_deg[r] == [5] for r in (1, 2, 3, 4))
max_is_flat = all(rho_max[r] == flat_ball(r) and argmax_deg[r] == [6] for r in (1, 2, 3, 4))
min_formula = all(rho_min[r] == flat_ball(r) - tri(r) for r in (1, 2, 3, 4))
gradient_real = all(rho_min[r] < rho_max[r] for r in (1, 2, 3, 4))
step("C.1", "the density extremum: rho_min at the twelve (flat - r(r+1)/2), rho_max at the flat mirror",
     "rho(v)=|B_r(v)|; min over substrate = flat_ball(r) - r(r+1)/2 (the twelve); max = flat_ball(r) "
     "(flattest deg-6); rho_min < rho_max", ["14.B.2", "13.A.2"],
     "archic density rho(v) = |B_r(v)| is the observable of container 13. Across the substrate its "
     "MINIMUM is attained exactly at the twelve degree-5 sites -- rho_min(r) = flat_ball(r) - r(r+1)/2, "
     "the MAXIMUM deficit / maximum positive curvature (14's primordial law seen as an extremum) -- and "
     "its MAXIMUM at the flattest degree-6 sites, rho_max(r) = flat_ball(r), the flat value (attained "
     "cleanly at R4, where a degree-6 vertex sits far enough from all twelve to have deficit 0). There "
     "is a real density GRADIENT rho_min < rho_max, from the twelve up to the flat mirror. Exact "
     "integer, computed on R4.",
     "UNIQUE (the extremal sites and values are fixed by the mesh)", "DERIVED",
     {"level": r4, "rho_min_r1_to_4": rho_min_list, "rho_max_r1_to_4": rho_max_list,
      "min_at_the_twelve_deg5": min_at_twelve, "max_is_flat_deg6": max_is_flat,
      "rho_min_formula_flat_minus_triangular": min_formula, "gradient_real": gradient_real},
     check="rho_min = flat - r(r+1)/2 at the twelve = [6,16,31,51]; rho_max = flat = [7,19,37,61]")
assert min_at_twelve and max_is_flat and min_formula and gradient_real
assert rho_min_list == [6, 16, 31, 51] and rho_max_list == [7, 19, 37, 61]

# ---- C.2 the signed mirror and one-sidedness -- DERIVED --------------------
max_degree = {name: max(degs[name].values()) for name in meshes}
no_hyperbolic = all(m <= 6 for m in max_degree.values())
net_deficit = {name: sum(12 - 2 * degs[name][v] for v in range(meshes[name][0])) for name in meshes}
net_positive = all(d == 24 for d in net_deficit.values())
step("C.2", "the signed mirror (D=0, deg 6) and what THIS substrate realizes (rho <= flat)",
     "TOTAL angle deficit Sum(12-2d)=12*chi=24>0 (topology, a law); this construction's max degree = 6 "
     "everywhere (no negative-curvature site here, by construction not by law)", ["C.1", "14.B.4"],
     "D = 0 -- a degree-6 site, deficit zero -- is the MIRROR between the two signs of the curvature. "
     "TWO facts, kept distinct: (a) a LAW -- Gauss-Bonnet fixes the TOTAL angle deficit at 12*chi = 24 > "
     "0, so a closed genus-0 surface must be NET positively curved; (b) THIS construction's -- the "
     "geodesic subdivision of the icosahedron happens to give every vertex degree <= 6 (no "
     "negative-curvature degree>6 site anywhere), so here rho never exceeds flat. (b) is NOT forced by "
     "(a): a closed sphere MAY carry local saddle vertices if they are outweighed; ours has none by "
     "construction. So the maximum-density end is simply NOT REALIZED on this substrate -- it is NOT a "
     "'complement' or reflection of the minimum-density side (the two signs are independent regions, not "
     "mirror images), and it is NOT forbidden in general. A region of rho > flat requires a DIFFERENT "
     "geometry (one carrying degree>6 sites) -- real and buildable, neither built nor characterized here.",
     "UNIQUE (the total 12*chi is topological; the all-degree<=6 is this construction's, stated as such)",
     "DERIVED",
     {"max_degree_per_level": max_degree, "no_hyperbolic_vertex_here": no_hyperbolic,
      "net_angle_deficit_per_level": net_deficit, "net_positive_total_is_topological": net_positive,
      "twelve_chi": 24, "mirror_at": "D=0 (degree 6, deficit zero)",
      "all_degree_le_6_is_constructional_not_forced": True,
      "max_density_end": "NOT realized here; a different, buildable geometry, not a reflection of this one"},
     check="net total deficit = 24 = 12*chi > 0 (topology); max degree <= 6 here (this construction)")
assert no_hyperbolic and net_positive and all(d == 24 for d in net_deficit.values())

# ---- C.3 the named possibility -- POSTULATE (values deferred) ---------------
step("C.3", "the named possibility: min density <-> vacuum, max density <-> black hole (POSSIBLE, "
     "NOT confirmed; values deferred)",
     "minimum archic density <-> vacuum/dark-energy direction (realized, the twelve); maximum archic "
     "density <-> black-hole direction (Schwarzschild attaches; NOT realized on this substrate)", ["C.1", "C.2"],
     "the arc's working correspondence, NAMED as a possibility to test and NOT asserted (Kevin, "
     "2026-08-25: possible, not confirmed; name the directions, defer values). From the maths-4 clues "
     "(reference only, not derived here): MINIMUM archic density corresponds to the VACUUM / "
     "dark-energy direction -- realized on this substrate at the twelve; MAXIMUM archic density "
     "corresponds to the BLACK-HOLE direction, where the Schwarzschild radius attaches (per the clue) "
     "-- NOT realized on THIS substrate (a different, buildable geometry; see C.2). NO value is computed "
     "or fitted; what awaits WARRANT is BOTH the ASSIGNMENT (which extremum <-> which physical end) AND "
     "the GEOMETRY of the max-density end (whether negative curvature or another high-density mechanism "
     "-- not decided here; comparing a discrete-graph curvature sign to a physical one now would be "
     "reading a contradiction off a road not yet built). Warrant = the derivation closing AND the "
     "top-down count meeting the bottom-up. No downstream container may use this as a premise until "
     "confirmed. This is the honest state: a possibility, held and capped.",
     "POSSIBLE, NOT confirmed; no value; no downstream premise until warranted", "POSTULATE",
     {"min_density_direction": "vacuum / dark-energy (realized: the twelve)",
      "max_density_direction": "black hole / Schwarzschild (NOT realized here; a different buildable geometry)",
      "mirror": "flat (D=0, degree 6)", "status": "possible, NOT confirmed",
      "values": "DEFERRED (Step 10 owes the value, only after close AND top-down meets bottom-up)",
      "assignment_also_unconfirmed": True, "max_density_geometry_undecided": True,
      "downstream_premise_use": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="15-density-extremum", steps=STEPS, grades=GRADES,
           values=dict(rho_min_r1_to_4=rho_min_list, rho_max_r1_to_4=rho_max_list,
                       max_degree_per_level=max_degree, net_angle_deficit_per_level=net_deficit,
                       twelve_chi=24, min_density_direction="vacuum / dark-energy (realized)",
                       max_density_direction="black hole (NOT realized here; a different buildable geometry)",
                       naming_status="possible, NOT confirmed; values deferred"))

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
