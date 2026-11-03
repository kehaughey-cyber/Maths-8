#!/usr/bin/env python3
"""Container 09 -- rung 6, kissing-twelve achievable. Rests on 05 (the bridge / geometry).

RUNG 6 (maths 4 RUNG6-KISSING-TWELVE-ACHIEVABLE, THEOREM). Twelve equal spheres can simultaneously
touch a central sphere of the same size in 3-space, without overlapping one another -- kissing
number >= 12, the icosahedral witness. The 12 points are the regular-icosahedron vertices

    (0, +-1, +-phi),  (+-1, +-phi, 0),  (+-phi, 0, +-1),        golden-ratio coordinates,

each at distance^2 = phi + 2 = R^2 from the origin (using phi^2 = phi + 1), with all pairwise
distances^2 in {4, 4+4phi, 8+4phi} -- all strictly greater than R^2, so the twelve spheres do not
touch each other (the famous 'rattle room', which is why whether a 13th fits stayed open for
centuries). The number line's rung-6 payoff, on the road to the 600-cell and the carrier (06).

EXACT and Mathlib-FREE, in Z[phi] = { a + b*phi : a,b in Z } with phi^2 = phi + 1. All norms and
distances are exact Z[phi] elements; the only ORDERING fact needed is that each pairwise distance^2
exceeds R^2, and the tightest of those (the edge, distance^2 = 4 vs R^2 = 2+phi) reduces to

    4 > 2 + phi  <=>  2 > phi  <=>  1 + sqrt5 < 4  <=>  sqrt5 < 3  <=>  5 < 9,

an integer fact. So the whole kissing result bottoms out at exact Z[phi] arithmetic plus 5 < 9.

NOT claimed here: the UPPER bound (kissing = 12 exactly, no 13th) -- that is Schuette-van der
Waerden 1953, EXTERNAL (cited, not machine-checked). And the deep question 'why does registration
SATURATE at 12' -- which is EQUIVALENT to the dim=3 upper bound (12 is the max only in 3-D) and is
the framework's central number (container 01's OWED 1.6, adjacency->12; the phase cycle->12) -- is
OWED, to fall out of the why-12 derivation, not attacked head-on.

Grades: DERIVED / POSTULATE / OWED, per step.
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- exact Z[phi]
# an element a + b*phi is the pair (a, b); phi^2 = phi + 1.
def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zmul(x, y):
    a, b = x
    c, d = y
    # (a+b phi)(c+d phi) = ac + (ad+bc) phi + bd phi^2 = (ac+bd) + (ad+bc+bd) phi
    return (a * c + b * d, a * d + b * c + b * d)


def zsq(x):
    return zmul(x, x)


Z0, Z1, ZM1, ZPHI, ZMPHI = (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)


def norm_sq(v):
    return zadd(zadd(zsq(v[0]), zsq(v[1])), zsq(v[2]))


def dist_sq(u, v):
    d = [zsub(u[i], v[i]) for i in range(3)]
    return zadd(zadd(zsq(d[0]), zsq(d[1])), zsq(d[2]))


def zpos(x):
    """Sign of a + b*phi, phi = (1+sqrt5)/2. a+b phi = (s + t*sqrt5)/2, s=2a+b, t=b. Exact by
    reducing the sqrt5 comparison to an integer one (t^2 * 5 vs s^2 with signs)."""
    a, b = x
    s, t = 2 * a + b, b
    if t == 0:
        return s > 0
    if t > 0:
        return s >= 0 or s * s < 5 * t * t
    return s > 0 and s * s > 5 * t * t


# ---- 6.1 the twelve icosahedral vertices -- DERIVED -------------------------
VERTS = []
for s1 in (Z1, ZM1):
    VERTS += [(Z0, s1, ZPHI), (Z0, s1, ZMPHI)]            # (0, +-1, +-phi)
for s1 in (Z1, ZM1):
    VERTS += [(s1, ZPHI, Z0), (s1, ZMPHI, Z0)]            # (+-1, +-phi, 0)
for s1 in (ZPHI, ZMPHI):
    VERTS += [(s1, Z0, Z1), (s1, Z0, ZM1)]                # (+-phi, 0, +-1)
count_ok = len(VERTS) == 12 and len(set(VERTS)) == 12
step("6.1", "the twelve icosahedral vertices -- the kissing witness",
     "(0,+-1,+-phi), (+-1,+-phi,0), (+-phi,0,+-1) in Z[phi]", ["05.1"],
     "the twelve candidate sphere-centers are the regular-icosahedron vertices, in golden-ratio "
     "coordinates -- twelve distinct points, the even cyclic images of (0,1,phi) with all sign "
     "choices. This is the WITNESS that kissing number >= 12; it lives in the Euclidean 3-space the "
     "bridge (05) provides.",
     "CHOSEN (a witness configuration; UNIQUE up to icosahedral symmetry)", "DERIVED",
     {"count": len(VERTS), "distinct": count_ok, "vertices": [[list(c) for c in v] for v in VERTS]},
     check="exactly 12 distinct icosahedral vertices")
assert count_ok

# ---- 6.2 equidistant from the center: every norm^2 = 2 + phi -- DERIVED ------
R2 = (2, 1)                                                # phi + 2
norms_ok = all(norm_sq(v) == R2 for v in VERTS)
step("6.2", "equidistant from the center -- every vertex has norm^2 = 2 + phi = R^2",
     "|v|^2 = 2 + phi for all twelve (using phi^2 = phi + 1)", ["6.1"],
     "each vertex is the same distance R from the origin: |(0,1,phi)|^2 = 1 + phi^2 = 2 + phi, and "
     "likewise for all twelve by symmetry. So the twelve centers lie on one sphere of radius R -- the "
     "precondition for kissing a central sphere. Exact in Z[phi].",
     "UNIQUE (all norms equal, = R^2)", "DERIVED",
     {"R_sq": list(R2), "all_norms_equal_R2": norms_ok},
     check="every vertex norm^2 = (2,1) = 2 + phi")
assert norms_ok

# ---- 6.3 three pairwise distance classes; the minimum is the edge -- DERIVED -
dclasses = {}
for i in range(12):
    for j in range(i + 1, 12):
        d = dist_sq(VERTS[i], VERTS[j])
        dclasses.setdefault(d, 0)
        dclasses[d] += 1
classes_sorted = sorted(dclasses.keys(), key=lambda p: (p[0] + p[1] * 1.618))
expected = {(4, 0), (4, 4), (8, 4)}
classes_ok = set(dclasses.keys()) == expected
min_class = classes_sorted[0]
step("6.3", "three pairwise distance classes {4, 4+4phi, 8+4phi}; the minimum is the edge",
     "pairwise dist^2 in {4, 4+4phi, 8+4phi}; min = 4 (the icosahedron edge)", ["6.1"],
     "the 66 vertex pairs take exactly three squared distances: 4 (the 30 edges), 4+4phi (the "
     "off-edges), and 8+4phi (the 6 antipodal pairs). The MINIMUM pairwise distance^2 is 4, the edge "
     "-- this is what must clear R^2 for the spheres not to overlap. All exact in Z[phi].",
     "UNIQUE (the distance multiset is fixed by the configuration)", "DERIVED",
     {"classes": {f"{p[0]}+{p[1]}phi": dclasses[p] for p in dclasses}, "as_expected": classes_ok,
      "min_dist_sq": list(min_class)},
     check="pairwise dist^2 take exactly {4, 4+4phi, 8+4phi}; min = 4")
assert classes_ok and min_class == (4, 0)

# ---- 6.4 THE KISSING: every dist^2 > R^2, reducing to 5 < 9 -- DERIVED -------
gaps = {p: zsub(p, R2) for p in dclasses}                  # dist^2 - R^2
gaps_pos = {p: zpos(g) for p, g in gaps.items()}
all_clear = all(gaps_pos.values())
# the tightest gap (edge) is 2 - phi > 0  <=>  5 < 9
edge_gap = zsub((4, 0), R2)                                # (2, -1) = 2 - phi
edge_reduces = (5 < 9)                                     # 2 - phi > 0  <=>  sqrt5 < 3  <=>  5 < 9
step("6.4", "THE KISSING -- every pairwise distance^2 exceeds R^2 (reduces to 5 < 9)",
     "dist^2 - R^2 > 0 for all three classes; the tightest, 4 - (2+phi) = 2 - phi, is > 0 <=> 5 < 9",
     ["6.2", "6.3"],
     "for the twelve spheres (radius R/2) to kiss the central one without overlapping, every "
     "pairwise distance must be at least R -- i.e. every dist^2 - R^2 >= 0. The two large gaps "
     "(2+3phi, 6+3phi) are positive because phi > 0; the tightest, the EDGE, gives 4 - (2+phi) = "
     "2 - phi, and 2 - phi > 0 <=> phi < 2 <=> 1 + sqrt5 < 4 <=> sqrt5 < 3 <=> 5 < 9. So the whole "
     "kissing result bottoms out at exact Z[phi] arithmetic plus the integer fact 5 < 9. The "
     "inequality is STRICT -- the twelve spheres rattle, they do not touch each other.",
     "UNIQUE (the kissing configuration exists; kissing number >= 12)", "DERIVED",
     {"gaps": {f"{p[0]}+{p[1]}phi": list(gaps[p]) for p in gaps},
      "all_clear_strict": all_clear, "edge_gap": list(edge_gap),
      "edge_reduces_to": "5 < 9", "reduction_true": edge_reduces},
     check="every dist^2 > R^2; the edge gap 2 - phi > 0 reduces to 5 < 9")
assert all_clear and edge_reduces

# ---- 6.5 the reading: 12 achieved; the central number -- POSTULATE ----------
step("6.5", "the reading -- 12 is achieved; whether the substrate SATURATES at 12 is the deep OWED",
     "kissing >= 12 (built); kissing = 12 and 'why exactly 12' point beyond", ["6.4"],
     "the icosahedral twelve is the kissing witness, built. Whether REGISTRATION forces exactly "
     "twelve mutual adjacencies -- the SATURATION -- is the framework's central number: it is "
     "container 01's OWED (1.6, adjacency -> 12) and the phase cycle -> 12, and it is EQUIVALENT to "
     "the dim=3 upper bound (12 is the maximum kissing number only in 3-D: d=2 caps at 6, d=4 "
     "reaches 24). So dim=3 should FALL OUT of why-12, not be attacked head-on. Held as the reading.",
     "the reading (12 achieved; saturation is the central OWED), held", "POSTULATE",
     {"achieved": "kissing >= 12", "central_owed": "why registration saturates at 12",
      "equivalent_to": "the dim=3 upper bound", "see": "container 01 (1.6), 03, CORRECTIONS #6"},
     check=None)

# ---- 6.6 the upper bound (no 13th) -- OWED ----------------------------------
step("6.6", "the upper bound (kissing = 12, no 13th) -- external / OWED",
     "no 13 equal spheres kiss a central one in 3-D (kissing(3) = 12)", ["6.4"],
     "the >= 12 half is built here. The <= 12 half -- that no 13th sphere fits -- is "
     "Schuette-van der Waerden 1953, EXTERNAL accepted mathematics, NOT machine-checked in this "
     "repo (a formalization far beyond reasonable effort). Cited, not claimed as our THEOREM; same "
     "tier as maths 4's KISSING-UPPER-BOUND-EXTERNAL. Together with 6.4 it gives kissing(3) = 12, "
     "the >= half ours and the <= half on citation.",
     "OWED (external; not machine-checked here)", "OWED",
     {"upper_bound": "kissing(3) = 12, no 13th", "source": "Schuette-van der Waerden 1953",
      "status": "external, cited, not machine-checked", "built_here": "the >= 12 half only"},
     check=None)

# ---- 6.7 the metric surface slack 3*sqrt3 - 5 -- DERIVED (Mathlib, in-repo) --
step("6.7", "the metric surface slack is exactly 3*sqrt3 - 5, in (0,1) -- the rattle, metrically",
     "twelve caps of half-angle pi/6 leave uncovered fraction 1 - 12*(1-cos(pi/6))/2 = 3*sqrt3 - 5, "
     "strictly between 0 and 1", ["6.4"],
     "6.4 shows the twelve spheres rattle COMBINATORIALLY (every pairwise dist^2 > R^2, exact in "
     "Z[phi], bottoming out at 5 < 9). This is the METRIC companion, which needs a real square root: "
     "the twelve contact caps (half-angle pi/6 = arcsin(1/2)) cover 12*(1-cos(pi/6))/2 = 6 - 3*sqrt3 "
     "of the central sphere, leaving EXACTLY 3*sqrt3 - 5 (~19.6%) uncovered -- strictly positive "
     "(the surface is NOT saturated, the rattle room) and strictly < 1. Saturation on the 1-D phase "
     "circle (twelve pi/6 arcs fill 2pi -- container 10's W.2), frustration on the 2-D surface (this "
     "slack): one angle pi/6 doing both. This was maths-4's REFRAME-PHASE-LEDGER-ARITHMETIC surface "
     "half, CITED while Maths 5 had no Real; as of the Mathlib-setup session (2026-08-21) it is "
     "PROVED IN-REPO at Container09.SurfaceSlackReal (surface_slack_exact / _pos / _lt_one; import "
     "Mathlib, axioms = Mathlib's three, kernel-confirmed). The Z[phi] core (6.1-6.4) stays "
     "zero-axiom; the two tiers are separate modules under one lib. Checked by the kernel (lake "
     "build), not by a cold Python recompute -- the model shows it Lean-proved, not re-run.",
     "UNIQUE (the surface slack is a fixed real value, 3*sqrt3 - 5)", "DERIVED",
     {"slack": "3*sqrt3 - 5", "approx": 0.196, "in_open_unit_interval": True,
      "status": "proved in-repo at Container09.SurfaceSlackReal (Mathlib) as of 2026-08-21",
      "proved_in_lean": True, "cold_recompute": False,
      "companion_to": "6.4 (the combinatorial rattle, Z[phi])"},
     check="surface slack = 3*sqrt3 - 5 in (0,1), proved at Mathlib's three axioms")

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="09-kissing-twelve", steps=STEPS, grades=GRADES,
           values=dict(R_sq=list(R2), count=len(VERTS),
                       distance_classes=[list(p) for p in sorted(dclasses)],
                       min_dist_sq=list(min_class), all_clear=all_clear,
                       vertices=[[list(c) for c in v] for v in VERTS]))

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
