#!/usr/bin/env python3
"""Container 14 -- DENSITY DEFICIT: flat_ball - |B_r| = curvature. Rests on 13 and 03.

Step 2 of the physics-bridge arc, still BOTTOM-UP and COLD. Container 13 gave the archic-density
observable |B_r(v)|; this container measures it against the flat (defect-zero) reference and reads
the difference as curvature. Two distinct conserved quantities appear and are kept TYPED APART (the
project's failure mode is exactly conflating quantities that look alike):

  B.1 the FLAT REFERENCE flat_ball(r) = 1 + 3r(r+1). The ball count a defect-zero (degree-6)
      neighbourhood has: the flat triangular lattice puts 6r registrations on ring r, so
      |B_r| = 1 + sum_{k=1..r} 6k = 1 + 3r(r+1). It is a COUNT, not an area -- flatness here means
      DEFECT ZERO, not a plane.

  B.2 the DENSITY DEFICIT D_r(v) = flat_ball(r) - |B_r(v)|: how many registrations are missing from
      v's r-neighbourhood versus a flat one. It is SIGNED curvature -- D > 0 is slower-than-flat
      growth (positive/spherical curvature), D = 0 is flat (the mirror, a degree-6 site in open
      country), D < 0 would be faster-than-flat (hyperbolic). This closed 2-sphere realizes D >= 0
      everywhere, largest at the twelve. (The chirality reading -- "0 is a mirror, left-handed
      natural" -- is a DOWNSTREAM physical claim, NOT derived here.)

  B.3 the PRIMORDIAL LAW: at each of the twelve degree-5 registrations the deficit is exactly the
      r-th TRIANGULAR number, D_r = r(r+1)/2, independent of refinement level -- with ONE stated
      finite-size exception (R2 at r=3 gives 11, not 6, because the mesh is too small for a free
      radius-3 ball; recorded, not smoothed). Verified clean at R3, R4. The curvature is concentrated
      on the twelve and its integrated form is triangular.

  B.4 the CURVATURE CHARGE (the 12*chi conservation): the ANGLE deficit sum_v (12 - 2*deg_v) -- an
      equilateral triangulation gives a degree-d vertex angle-defect 2pi - d*(pi/3) = (12 - 2d)
      radits (12 radits = 2pi) -- is 2 radits at each of the twelve and 0 elsewhere, total 24 =
      12*chi (chi = 2), refinement-invariant. This is Gauss-Bonnet: the concentrated Regge
      curvature. It is a DIFFERENT quantity from B.2/B.3's ball deficit (per-vertex, r-independent,
      an exact integer charge), and is named separately so the two are never merged.

  B.5 the BALL-DEFICIT TOTAL is separately conserved: sum_v D_r(v) is the SAME at every refinement
      level, per radius (r=1:12, r=2:96, r=3:372, r=4:1020) -- a conservation of the same SHAPE as
      12*chi, but a distinct r-resolved quantity. It makes the deficit an observable of the BOUND,
      not an artefact of how finely the bound is divided.

  NOT here (deferred, by scope): which signed extremum is "vacuum" or "black hole" (Step 3), the
  frustration dynamo epsilon != 0 (Step 4), and any contact with I/alpha, rho_Lambda, or gravity
  (Steps 5-10). This container reads the deficit as curvature and states its two conservations.

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


# ---------------------------------------------------------------- exact Z[phi] (substrate, from 13)
def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zmul(x, y):                                        # phi^2 = phi + 1
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def sqdist(u, v):
    acc = (0, 0)
    for cu, cv in zip(u, v):
        d = zsub(cu, cv)
        acc = zadd(acc, zmul(d, d))
    return acc


VERTS = []
for a in (1, -1):
    for b in (1, -1):
        VERTS.append(((0, 0), (a, 0), (0, b)))
        VERTS.append(((0, b), (0, 0), (a, 0)))
        VERTS.append(((a, 0), (0, b), (0, 0)))
VERTS = list(dict.fromkeys(VERTS))
assert len(VERTS) == 12
MIN_SQ = (4, 0)
R1_EDGES = sorted((i, j) for i, j in combinations(range(12), 2)
                  if sqdist(VERTS[i], VERTS[j]) == MIN_SQ)


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

    new_faces = []
    for a, b, c in faces:
        ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
        new_faces += [(a, ab, ca), (b, ab, bc), (c, bc, ca), (ab, bc, ca)]
    return nxt, new_faces


def ball_size(A, v, r):                                # |B_r(v)| -- breadth-first, pure adjacency
    seen, front = {v}, {v}
    for _ in range(r):
        nxt = set()
        for u in front:
            nxt |= A[u]
        front = nxt - seen
        seen |= front
    return len(seen)


def flat_ball(r):                                      # the defect-zero reference count
    return 1 + 3 * r * (r + 1)


# build R1..R4
A1 = adj_from_edges(R1_EDGES, 12)
R1_FACES = faces_from_adj(A1, 12)
meshes = {"R1": (12, R1_FACES)}
n, F = 12, R1_FACES
for k in range(2, 5):
    n, F = subdivide(n, F)
    meshes[f"R{k}"] = (n, F)
adjs = {name: adj_from_faces(F, n) for name, (n, F) in meshes.items()}
degs = {name: {v: len(adjs[name][v]) for v in range(meshes[name][0])} for name in meshes}

# ---- B.1 the flat reference -- DERIVED --------------------------------------
flat_vals = [flat_ball(r) for r in range(5)]
ring_form_ok = all(flat_ball(r) - flat_ball(r - 1) == 6 * r for r in range(1, 5))   # 6r on ring r
step("B.1", "the flat reference flat_ball(r) = 1 + 3r(r+1): the defect-zero ball count",
     "flat triangular lattice puts 6r registrations on ring r; |B_r| = 1 + sum_{k<=r} 6k = 1 + 3r(r+1)",
     ["13.A.2"],
     "the deficit needs a reference: what |B_r| WOULD be with zero defect. In the flat triangular "
     "lattice (every vertex degree 6) ring r carries exactly 6r registrations, so flat_ball(r) = "
     "1 + sum_{k=1..r} 6k = 1 + 3r(r+1). It is a COUNT, not an area -- 'flat' here means defect "
     "zero, not an embedded plane. This is the yardstick B.2 measures the substrate against.",
     "UNIQUE (fixed by the flat triangular growth)", "DERIVED",
     {"flat_ball_0_to_4": flat_vals, "ring_r_has_6r": ring_form_ok},
     check="flat_ball = 1+3r(r+1) = [1,7,19,37,61]; ring r carries 6r")
assert flat_vals == [1, 7, 19, 37, 61] and ring_form_ok

# ---- B.2 the signed density deficit -- DERIVED ------------------------------
# deficit profiles by degree class, on R4 (the freest ball up to r=4)
r4name = "R4"
A4, deg4 = adjs[r4name], degs[r4name]
n4 = meshes[r4name][0]
prof_by_class = {}
for v in range(n4):
    prof = tuple(flat_ball(r) - ball_size(A4, v, r) for r in range(5))
    prof_by_class.setdefault((deg4[v], prof), 0)
    prof_by_class[(deg4[v], prof)] += 1
deg5_deficit_profile = next(p for (d, p), _ in prof_by_class.items() if d == 5)
all_nonneg = all(all(x >= 0 for x in p) for (_, p) in prof_by_class)
deg6_deficit_profiles = sorted({p for (d, p) in prof_by_class if d == 6})
step("B.2", "the density deficit D_r(v) = flat_ball(r) - |B_r(v)|: SIGNED curvature",
     "D_r(v) = flat_ball(r) - |B_r(v)|; > 0 spherical, = 0 flat (mirror), < 0 hyperbolic; here D >= 0",
     ["B.1", "13.A.2"],
     "the DENSITY DEFICIT is D_r(v) = flat_ball(r) - |B_r(v)|: how many registrations are missing "
     "from v's r-neighbourhood compared with a flat one of the same relational radius. It is SIGNED "
     "curvature -- D > 0 means the ball grows SLOWER than flat (positive/spherical curvature), D = 0 "
     "is flat (the mirror; a degree-6 site in open country), and D < 0 would be faster-than-flat "
     "(hyperbolic). This CLOSED 2-sphere realizes D >= 0 at every vertex (checked on R4), largest at "
     "the twelve degree-5 sites -- the positive side of the mirror. The chirality reading ('0 is a "
     "mirror, left-handed natural') is a downstream physical claim, not derived here.",
     "SIGNED; here D >= 0 (the spherical side); 0 is the flat mirror", "DERIVED",
     {"deg5_deficit_profile_r0_to_4": list(deg5_deficit_profile),
      "deg6_deficit_profiles_r0_to_4": [list(p) for p in deg6_deficit_profiles],
      "all_deficits_nonnegative_on_R4": all_nonneg,
      "sign_convention": "D>0 spherical, D=0 flat (mirror), D<0 hyperbolic"},
     check="D = flat - |B_r|; deg-5 profile (0,1,3,6,10); all D >= 0 on R4 (spherical side)")
assert deg5_deficit_profile == (0, 1, 3, 6, 10) and all_nonneg

# ---- B.3 the primordial law: r(r+1)/2 at the twelve -- DERIVED --------------
def tri(r):
    return r * (r + 1) // 2


primordial = {}
finite_size_exceptions = {}
for name in meshes:
    A, deg, nn = adjs[name], degs[name], meshes[name][0]
    for r in (1, 2, 3, 4):
        if flat_ball(r) > nn:                          # ball bigger than the whole mesh
            continue
        vals = sorted({flat_ball(r) - ball_size(A, v, r) for v in range(nn) if deg[v] == 5})
        key = f"{name}:r{r}"
        if vals == [tri(r)]:
            primordial[key] = tri(r)
        else:
            finite_size_exceptions[key] = {"got": vals, "law": tri(r)}
law_clean_R3_R4 = all(primordial.get(f"{lv}:r{r}") == tri(r)
                      for lv in ("R3", "R4") for r in (1, 2, 3, 4))
step("B.3", "the primordial law: the deficit at each of the twelve is the triangular number r(r+1)/2",
     "for deg-5 v: D_r(v) = r(r+1)/2 (= 1,3,6,10 for r=1..4), level-independent; R2 r=3 is a "
     "finite-size exception (11, not 6)", ["B.2"],
     "at each of the twelve degree-5 registrations the deficit has an exact closed form: D_r = the "
     "r-th TRIANGULAR number r(r+1)/2 (1, 3, 6, 10, ...), INDEPENDENT of refinement level. The "
     "curvature is concentrated on the twelve and its integrated (ball-count) form is triangular -- "
     "the constant second difference of r(r+1)/2 is 1, one unit of curvature per step per carrier. "
     "ONE finite-size exception is recorded rather than smoothed: at R2, r=3 the value is 11 not 6, "
     "because a 42-vertex mesh is too small for a radius-3 ball to develop freely; the law is "
     "asserted where the ball does not compete with the far side of the bound -- clean at R3 and R4.",
     "UNIQUE (the closed form; asserted where the ball is free)", "DERIVED",
     {"law": "D_r(deg-5) = r(r+1)/2", "triangular_1_to_4": [tri(r) for r in range(1, 5)],
      "clean_at_R3_R4": law_clean_R3_R4, "confirmed": primordial,
      "finite_size_exceptions": finite_size_exceptions},
     check="deg-5 deficit = r(r+1)/2 = 1,3,6,10, clean at R3/R4; R2 r=3 = 11 (finite-size), recorded")
assert law_clean_R3_R4 and finite_size_exceptions == {"R2:r3": {"got": [11], "law": 6}}

# ---- B.4 the curvature charge: angle deficit = 12*chi -- DERIVED ------------
RADITS_PER_TURN = 12                                   # 2pi = 12 radits, so pi/3 = 2 radits
angle_debt = {}
for name in meshes:
    deg, nn = degs[name], meshes[name][0]
    angle_debt[name] = sum(RADITS_PER_TURN - 2 * deg[v] for v in range(nn))
per_deg5 = RADITS_PER_TURN - 2 * 5                      # 2 radits at a degree-5 vertex
per_deg6 = RADITS_PER_TURN - 2 * 6                      # 0 at a degree-6 vertex
chi = 2
charge_is_12chi = all(d == RADITS_PER_TURN * chi for d in angle_debt.values())
step("B.4", "the curvature charge: the angle deficit sums to 12*chi = 24 (Gauss-Bonnet), invariant",
     "angle-defect (12 - 2*deg) = 2 radits per deg-5, 0 per deg-6; sum = 24 = 12*chi at every level",
     ["B.2"],
     "the CONCENTRATED curvature -- distinct from the ball deficit and named separately so they are "
     "never merged. An equilateral triangulation gives a degree-d vertex the angle defect "
     "2pi - d*(pi/3) = (12 - 2d) radits (12 radits = 2pi). That is 2 radits at each of the twelve "
     "degree-5 vertices and 0 everywhere else, so the total is 24 = 12*chi (chi = 2) -- Gauss-Bonnet, "
     "and REFINEMENT-INVARIANT (subdivision adds only degree-6 vertices, which carry no charge). "
     "This is the Regge curvature as an exact integer charge, per-vertex and r-INDEPENDENT: a "
     "DIFFERENT object from B.2/B.3's r-resolved ball deficit, though both concentrate on the twelve.",
     "UNIQUE (Gauss-Bonnet; the charge is fixed by chi)", "DERIVED",
     {"radits_per_turn": RADITS_PER_TURN, "per_deg5": per_deg5, "per_deg6": per_deg6,
      "total_per_level": angle_debt, "equals_12chi": charge_is_12chi, "chi": chi, "value": 24},
     check="angle deficit = 2 per deg-5, 0 per deg-6; total 24 = 12*chi at every level")
assert charge_is_12chi and per_deg5 == 2 and per_deg6 == 0 and all(d == 24 for d in angle_debt.values())

# ---- B.5 the ball-deficit total is refinement-invariant per radius -- DERIVED
ball_deficit_total = {}
for r in (1, 2, 3, 4):
    per_level = {}
    for name in meshes:
        A, nn = adjs[name], meshes[name][0]
        if flat_ball(r) > nn:
            continue
        per_level[name] = sum(flat_ball(r) - ball_size(A, v, r) for v in range(nn))
    ball_deficit_total[r] = per_level
invariant = {r: (len(set(pl.values())) == 1) for r, pl in ball_deficit_total.items()}
conserved_value = {r: sorted(set(pl.values()))[0] for r, pl in ball_deficit_total.items()}
step("B.5", "the ball-deficit total sum_v D_r(v) is refinement-invariant per radius (a 2nd conservation)",
     "sum_v [flat_ball(r) - |B_r(v)|] is the SAME at every level: r=1:12, r=2:96, r=3:372, r=4:1020",
     ["B.2"],
     "summed over the whole mesh, the ball deficit at each radius is IDENTICAL at every refinement "
     "level -- exactly, including where the per-vertex distribution differs. r=1 -> 12, r=2 -> 96, "
     "r=3 -> 372, r=4 -> 1020, each invariant across the levels on which the ball fits. This is a "
     "conservation law of the same SHAPE as 12*chi, and it is what makes the deficit an observable of "
     "the BOUND rather than an artefact of how finely the bound has been divided. It is a SECOND, "
     "r-resolved conservation -- kept distinct from B.4's angle-deficit charge, which it is not equal "
     "to (12, 96, 372, 1020 are not 24).",
     "UNIQUE (invariant of the bound at each radius)", "DERIVED",
     {"per_radius": ball_deficit_total, "invariant_per_radius": invariant,
      "conserved_value": conserved_value,
      "distinct_from_12chi": conserved_value != {r: 24 for r in conserved_value}},
     check="sum_v deficit is level-invariant per radius: r=1:12, r=2:96, r=3:372, r=4:1020")
assert all(invariant.values()) and conserved_value == {1: 12, 2: 96, 3: 372, 4: 1020}

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="14-density-deficit", steps=STEPS, grades=GRADES,
           values=dict(flat_ball_0_to_4=flat_vals,
                       deg5_deficit_profile=list(deg5_deficit_profile),
                       deg6_deficit_profiles=[list(p) for p in deg6_deficit_profiles],
                       triangular_1_to_4=[tri(r) for r in range(1, 5)],
                       primordial_confirmed=primordial,
                       finite_size_exceptions=finite_size_exceptions,
                       angle_deficit_total=angle_debt, angle_deficit_per_deg5=per_deg5,
                       twelve_chi=24, ball_deficit_conserved=conserved_value))

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
