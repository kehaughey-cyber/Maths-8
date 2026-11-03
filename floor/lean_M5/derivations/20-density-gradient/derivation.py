#!/usr/bin/env python3
"""Container 20 -- DENSITY GRADIENT: gravity = the change in packing. Rests on 13, 14.

Step 8 of the physics-bridge arc (the next-10 roadmap, Kevin-approved 2026-08-25). Still BOTTOM-UP and
COLD. Container 13 gave the density observable rho(v) = |B_r(v)|; this container takes its GRADIENT
across the lattice -- the arc's claim that "gravity is the change in the packing." The DERIVED content
is the gradient observable and its structure; the physical reading "gradient = gravity" is a NAMED
possibility (POSTULATE), with the actual GR correspondence deferred to the Step 9 entry.

  G.1 the GRADIENT observable. For an edge (u,v): the density difference rho(u)-rho(v). Per vertex:
      the gradient magnitude gm(v) = sum_{w~v} |rho(w)-rho(v)|, and the graph Laplacian
      L(v) = sum_{w~v} (rho(w)-rho(v)). Adjacency-only, like |B_r| itself -- no distance, no embedding.

  G.2 GRAVITY LOCALIZES -- flat regions have NO gravity. Most of the substrate has ZERO gradient
      (rho locally constant); the gradient is nonzero only NEAR the twelve, and the nonzero region
      GROWS with r. The twelve are LOCAL MINIMA of rho (every neighbour has higher rho), so there
      gm = L (all differences positive) -- the gradient SOURCES. "No change in packing -> no gravity"
      is realized: gravity is not everywhere, it is where the density varies.

  G.3 the SOURCES SUM TO ZERO (a discrete Gauss law), and gradient = -gradient(deficit). sum_v L(v) = 0
      EXACTLY -- each edge (u,v) contributes rho(v)-rho(u) once and rho(u)-rho(v) once, cancelling. So
      the gravity sources sum to zero on the CLOSED substrate (like total charge zero on a closed
      universe): the twelve's positive sources are balanced by negative-L neighbours. And since
      rho = flat_ball(r) - deficit (14) with flat_ball constant per r, grad(rho) = -grad(deficit): the
      density gradient IS the negative of the curvature-deficit gradient.

  G.4 the NAMED reading (POSTULATE; possible, NOT confirmed): gravity = the density gradient. And a
      CHECKED-NEGATIVE kept explicit so it is never over-claimed: the naive discrete Poisson
      field-equation Laplacian(rho) = k*deficit does NOT hold (L(deg-5) = 5r, not proportional to the
      deficit tri(r)). "Gravity = grad(rho)" is a GRADIENT claim, not a field-equation claim here; the
      physical force, its direction, and any value are deferred to the Step 9 GR entry and Step 10.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
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
for k in range(2, 6):
    n, F = subdivide(n, F)
    meshes[f"R{k}"] = (n, F)


def field(level, r):
    n, F = meshes[level]
    A = adj_from_faces(F, n)
    deg = {v: len(A[v]) for v in range(n)}
    rho = {v: ball_size(A, v, r) for v in range(n)}
    gm = {v: sum(abs(rho[w] - rho[v]) for w in A[v]) for v in range(n)}
    lap = {v: sum(rho[w] - rho[v] for w in A[v]) for v in range(n)}
    return n, A, deg, rho, gm, lap


# ---- G.1 the gradient observable -- DERIVED --------------------------------
LVL, R = "R4", 3
FIELDS = {lvl: field(lvl, R) for lvl in ("R3", "R4", "R5")}      # compute each level ONCE (cache)
n4, A4, deg4, rho4, gm4, lap4 = FIELDS[LVL]
deg5_gm = sorted({gm4[v] for v in range(n4) if deg4[v] == 5})
deg5_lap = sorted({lap4[v] for v in range(n4) if deg4[v] == 5})
gm_well_defined = (deg5_gm == deg5_lap == [5 * R])          # twelve are minima: gm = lap = 5r
step("G.1", "the density gradient: edge differences of rho, the per-vertex magnitude and the Laplacian",
     "for edge (u,v): rho(u)-rho(v); gm(v)=sum|rho(w)-rho(v)|; L(v)=sum(rho(w)-rho(v)); adjacency-only",
     ["13.A.2", "14.B.2"],
     "gravity is the CHANGE in the packing, so the object is the GRADIENT of the density observable "
     "rho(v)=|B_r(v)| (container 13). Per edge (u,v): the difference rho(u)-rho(v). Per vertex: the "
     "gradient magnitude gm(v) = sum over neighbours |rho(w)-rho(v)|, and the graph Laplacian L(v) = "
     "sum (rho(w)-rho(v)). Both are pure adjacency -- no distance, no embedding -- exactly like |B_r| "
     "itself. At each of the twelve (a local minimum of rho) every neighbour is higher, so gm = L = 5r "
     "(five neighbours, each higher by r). Computed cold on " + LVL + " at r=" + str(R) + ".",
     "UNIQUE (the gradient fields are fixed by rho on the mesh)", "DERIVED",
     {"level": LVL, "radius": R, "deg5_gradient_magnitude": deg5_gm, "deg5_laplacian": deg5_lap,
      "twelve_are_minima_gm_eq_lap_eq_5r": gm_well_defined},
     check="gm and L are well-defined adjacency fields; at the twelve gm = L = 5r")
assert gm_well_defined

# ---- G.2 gravity localizes -- DERIVED --------------------------------------
zero_grad = {lvl: sum(1 for v in range(FIELDS[lvl][0]) if FIELDS[lvl][4][v] == 0)
             for lvl in ("R3", "R4", "R5")}
totals = {lvl: FIELDS[lvl][0] for lvl in ("R3", "R4", "R5")}
frac_flat = {lvl: f"{zero_grad[lvl]}/{totals[lvl]}" for lvl in zero_grad}
# flat fraction GROWS as the mesh refines at fixed r (twelve become sparser); at the finest level most
# of space is flat -- gravity localized near the sources. (At fixed mesh it shrinks as r grows.)
flat_grows_with_refinement = zero_grad["R3"] / totals["R3"] < zero_grad["R5"] / totals["R5"]
most_flat_at_finest = zero_grad["R5"] > totals["R5"] // 2
twelve_are_sources = all(gm4[v] > 0 for v in range(n4) if deg4[v] == 5)
step("G.2", "gravity localizes: flat regions have NO gradient; it is nonzero only near the twelve",
     "most vertices have gm=0 (rho locally constant = flat = no gravity); gm>0 only near the twelve "
     "(the sources)", ["G.1"],
     "the substrate realization of 'no change in packing -> no gravity'. Large regions have ZERO "
     "gradient -- rho is locally constant there, flat, no gravity: " + str(frac_flat) + " (the flat "
     "fraction). As the mesh REFINES at fixed r the flat fraction GROWS (the twelve become sparser; at "
     "the finest level R5, " + frac_flat["R5"] + " is flat) -- toward the physical picture: most of "
     "space is flat, gravity localized near the sources. (At a fixed mesh the flat region shrinks as r "
     "grows, the influence reaching further.) The gradient is nonzero only NEAR the twelve, which are "
     "local MINIMA of rho (gm>0 at all twelve, the gradient SOURCES). Gravity is exactly where the "
     "density varies.",
     "UNIQUE (the zero-gradient set is fixed by the mesh)", "DERIVED",
     {"zero_gradient_counts": zero_grad, "totals": totals, "flat_fraction": frac_flat,
      "flat_grows_with_refinement": flat_grows_with_refinement, "most_flat_at_finest": most_flat_at_finest,
      "twelve_are_sources": twelve_are_sources},
     check="large flat regions (no gravity), growing with refinement; the twelve are the sources")
assert flat_grows_with_refinement and most_flat_at_finest and twelve_are_sources

# ---- G.3 sources sum to zero (Gauss) + grad(rho) = -grad(deficit) -- DERIVED
total_lap = {lvl: sum(FIELDS[lvl][5][v] for v in range(FIELDS[lvl][0]))
             for lvl in ("R3", "R4", "R5")}
gauss_holds = all(t == 0 for t in total_lap.values())
# grad(rho) = -grad(deficit): rho = flat - deficit, flat const per r, so rho(w)-rho(v) = deficit(v)-deficit(w)
balldef = {v: flat_ball(R) - rho4[v] for v in range(n4)}
grad_is_neg_deficit = all(
    (rho4[w] - rho4[v]) == (balldef[v] - balldef[w]) for v in range(n4) for w in A4[v])
step("G.3", "the sources sum to zero (a discrete Gauss law), and grad(rho) = -grad(deficit)",
     "sum_v L(v) = 0 exactly (each edge cancels); rho = flat - deficit so rho(w)-rho(v) = "
     "deficit(v)-deficit(w)", ["G.1", "14.B.2"],
     "TWO exact facts. (a) THE GAUSS LAW: sum over all vertices of L(v) is 0 -- each edge (u,v) "
     "contributes rho(v)-rho(u) at u and rho(u)-rho(v) at v, which cancel. So the gravity SOURCES sum "
     "to zero on the CLOSED substrate (as total charge is zero on a closed universe): the twelve's "
     "positive sources are exactly balanced by the negative-L neighbours. Checked at every level: "
     + str(total_lap) + ". (b) GRADIENT DUALITY: since rho = flat_ball(r) - deficit (14) and flat_ball "
     "is constant per r, grad(rho) = -grad(deficit) edge-by-edge -- the density gradient IS the "
     "negative of the curvature-deficit gradient. Gravity (grad rho) and curvature (deficit) are the "
     "same field, differentiated.",
     "UNIQUE (both are exact identities)", "DERIVED",
     {"total_laplacian_per_level": total_lap, "gauss_sources_sum_to_zero": gauss_holds,
      "grad_rho_eq_neg_grad_deficit": grad_is_neg_deficit},
     check="sum_v L(v) = 0 at every level (Gauss); rho(w)-rho(v) = deficit(v)-deficit(w) everywhere")
assert gauss_holds and grad_is_neg_deficit

# ---- G.4 the named reading + the checked-negative -- POSTULATE --------------
# checked-negative: L(deg-5) = 5r is NOT proportional to the deficit tri(r)
lap5, def5 = 5 * R, tri(R)
not_poisson = (lap5 * tri(2) != tri(R) * (5 * 2))          # 5r/tri(r) not constant across r -> not proportional
step("G.4", "the named reading: gravity = the density gradient (POSSIBLE, NOT confirmed); and the "
     "checked-negative (not a field equation)",
     "gravity = grad(rho) -- named, held; the Poisson field equation Laplacian(rho)=k*deficit does NOT "
     "hold (checked)", ["G.2", "G.3"],
     "the arc's claim, NAMED as a possibility and held (the container-15 discipline: the math is "
     "derived, the physical reading is a POSTULATE). Gravity = the density gradient grad(rho). AND a "
     "CHECKED-NEGATIVE kept explicit so it is never over-claimed: the naive discrete POISSON field "
     "equation Laplacian(rho) = k*deficit does NOT hold -- L(deg-5) = 5r (r=2 -> 10, r=3 -> 15) is not "
     "proportional to the ball deficit tri(r) (3, 6). So 'gravity = grad(rho)' is a GRADIENT claim, NOT "
     "a field-equation claim here. The physical FORCE, its direction (toward the vacuum or the "
     "black-hole extremum), and any VALUE are deferred to the Step 9 GR correspondence entry (through "
     "the container-19 gate) and Step 10. No downstream container may use this reading as a premise.",
     "POSSIBLE, NOT confirmed; a gradient claim not a field equation; no value; no downstream premise",
     "POSTULATE",
     {"reading": "gravity = grad(rho) (the change in packing)",
      "checked_negative_poisson": "Laplacian(rho) = k*deficit does NOT hold (L(deg5)=5r != k*tri(r))",
      "not_a_field_equation": not_poisson,
      "deferred_to": "Step 9 GR entry (gravity <-> curvature) and Step 10 (value)",
      "downstream_premise_use": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="20-density-gradient", steps=STEPS, grades=GRADES,
           values=dict(level=LVL, radius=R, deg5_gradient=5 * R,
                       zero_gradient_counts=zero_grad, totals=totals,
                       gauss_sources_sum_to_zero=gauss_holds,
                       grad_rho_eq_neg_grad_deficit=grad_is_neg_deficit,
                       gravity_is_gradient="named possibility (POSTULATE); not a field equation",
                       checked_negative="Laplacian(rho) != k*deficit"))

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
