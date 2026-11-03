#!/usr/bin/env python3
"""Container 05 -- the geometric-balance bridge, and rung 5 (equidistant dimension).

THE BRIDGE. This is where the pre-spatial RELATIONAL floor ends and standing GEOMETRY begins.
The geometric-balance postulate (maths 4 BRIDGE-GEOMETRIC-BALANCE-POSTULATE, GRADE AXIOM) says:
registrations CORRESPOND to points in a real Euclidean space, with mutually-adjacent registrations
at a fixed minimum separation -- unit spheres in mutual contact (radius 1, centers distance 2
apart). It is an EQUIVALENCE (the registration structure corresponds to a Euclidean configuration),
NOT an identity (a registration is not a point); and Euclidean means real coordinates + the ordinary
inner product -- explicitly NOT Hilbert space. It is ADDED, not derived: a POSTULATE. It rests on
container 01's non-overlap adjacency (what "mutually adjacent" refers to). It is the crossing
Kevin's ladder reaches after ordinal dynamics: ordinal-dynamics (07) -> THIS bridge -> metric.

RUNG 5 -- what the bridge immediately buys (maths 4 RUNG5-EQUIDISTANT-DIMENSION, THEOREM). N
pairwise-equidistant points in a real inner product space are AFFINELY INDEPENDENT, forcing ambient
dimension >= N-1. The proof mechanism, exact and Mathlib-free (polarization): fix a base point; the
N-1 difference vectors each have norm^2 = D and pairwise inner product D/2, so their GRAM matrix is
(D/2)(I + J), whose determinant is N * (D/2)^(N-1) != 0 -- hence linearly independent, hence the N
points are affinely independent, hence dim >= N-1. Concretely: 2 -> d>=1 (a line), 3 -> d>=2 (a
plane), 4 -> d>=3 (a volume) -- "the tetrahedron is genuinely 3-dimensional", the retracted
RUNG3-TETRAHEDRON-MINIMUM's stipulation now DERIVED.

The CONCRETE cases (N = 2,3,4 -- all the framework needs for the bridge) are DERIVED here by exact
integer determinant, Mathlib-free and zero-axiom. The GENERAL all-N statement is maths 4's
RUNG5-EQUIDISTANT-DIMENSION (Mathlib THEOREM); as of the Mathlib-setup session (2026-08-21) it is
PROVED IN-REPO at Container05.EquidistantDimensionReal (import Mathlib, axioms = Mathlib's three),
no longer cited (step 5.6). NOT claimed: the UPPER bound (dim = 3 exactly), which is container 03's
open thread; and Hilbert-space machinery.

Grades: DERIVED / POSTULATE / OWED, per step.
"""

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


# ---------------------------------------------------------------- exact geometry
def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def dist2(u, v):
    return dot([a - b for a, b in zip(u, v)], [a - b for a, b in zip(u, v)])


def det(M):
    """Exact determinant by fraction-based Gaussian elimination (M a list of lists)."""
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if A[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            d = -d
        d *= A[i][i]
        inv = A[i][i]
        for r in range(i + 1, n):
            f = A[r][i] / inv
            A[r] = [A[r][c] - f * A[i][c] for c in range(n)]
    return d


def gram_of_config(points):
    """The Gram matrix of the difference vectors p_i - p_0 (i = 1..N-1)."""
    p0 = points[0]
    diffs = [[a - b for a, b in zip(p, p0)] for p in points[1:]]
    return [[dot(u, v) for v in diffs] for u in diffs]


# Concrete equidistant configurations, exact integer coordinates. (An equilateral triangle needs
# no coords in 2D -- sqrt3 -- but sits exactly in 3D, so the triangle here lives in R^3.)
CONFIGS = {
    2: [(0,), (2,)],                                             # two points on a line, d^2 = 4
    3: [(0, 0, 0), (1, 1, 0), (1, 0, 1)],                       # equilateral triangle in R^3, d^2 = 2
    4: [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],      # regular tetrahedron, d^2 = 8
}

# ---- 5.1 the geometric-balance bridge -- POSTULATE (the AXIOM) ---------------
step("5.1", "the geometric-balance bridge -- registrations correspond to Euclidean points",
     "registration structure <-> points in real Euclidean space; mutually adjacent at separation 2 "
     "(unit spheres in contact)", [],
     "THE BRIDGE, added not derived. Where the pre-spatial relational floor ends and standing "
     "GEOMETRY begins: registrations CORRESPOND to points in a real Euclidean space (real "
     "coordinates + ordinary inner product, NOT Hilbert), mutually-adjacent ones at a fixed minimum "
     "separation -- unit spheres in mutual contact, centers distance 2 apart. An EQUIVALENCE, not an "
     "identity (a registration is not a point). It rests on container 01's non-overlap adjacency for "
     "what 'mutually adjacent' means. Held as the postulate; this is exactly the AXIOM maths 4 files.",
     "the correspondence (bridge), held -- an added axiom", "POSTULATE",
     {"correspondence": "registration structure <-> Euclidean configuration",
      "separation": 2, "spheres": "radius 1, centers 2 apart", "is": "equivalence, not identity",
      "not": "Hilbert space", "rests_on": "container 01 (non-overlap adjacency)"},
     check=None)

# ---- 5.2 equidistant => Gram = (D/2)(I + J) -- DERIVED (polarization) --------
poly_checks = {}
for N, pts in CONFIGS.items():
    # verify equidistance and the polarization Gram (diag D, off-diag D/2)
    D = dist2(pts[0], pts[1])
    equi = all(dist2(a, b) == D for i, a in enumerate(pts) for b in pts[i + 1:])
    G = gram_of_config(pts)
    diag_ok = all(G[i][i] == D for i in range(len(G)))
    off_ok = all(G[i][j] == Fr(D, 2) for i in range(len(G)) for j in range(len(G)) if i != j)
    poly_checks[N] = {"D": D, "equidistant": equi, "gram_diag_is_D": diag_ok,
                      "gram_offdiag_is_D_over_2": off_ok, "gram": [[str(x) for x in r] for r in G]}
polarization_holds = all(c["equidistant"] and c["gram_diag_is_D"] and c["gram_offdiag_is_D_over_2"]
                         for c in poly_checks.values())
step("5.2", "equidistant points -> the Gram of differences is (D/2)(I + J) -- polarization",
     "v_i = p_i - p_0 ; <v_i,v_i> = D ; <v_i,v_j> = D/2 (i != j)", ["5.1"],
     "fix a base point; the N-1 difference vectors each have norm^2 = the common distance^2 D (each "
     "p_i is at distance^2 D from p_0), and pairwise inner product D/2 by polarization "
     "(<v_i,v_j> = (|v_i|^2 + |v_j|^2 - |v_i - v_j|^2)/2 = (D + D - D)/2, since |p_i - p_j|^2 = D "
     "too). So the Gram matrix is D on the diagonal, D/2 off it = (D/2)(I + J). Verified exactly on "
     "concrete configs (line, tetrahedron).",
     "UNIQUE (the Gram is fixed by equidistance alone)", "DERIVED",
     {"configs": poly_checks, "gram_form": "(D/2)*(I + J)"},
     check="each equidistant config has Gram diag D, off-diag D/2")
assert polarization_holds

# ---- 5.3 the Gram determinant is N*(D/2)^(N-1) != 0 -- DERIVED ---------------
# det((D/2)(I+J)_{N-1}) = (D/2)^{N-1} * det(I+J)_{N-1} = (D/2)^{N-1} * N.
def IplusJ(k):
    return [[2 if i == j else 1 for j in range(k)] for i in range(k)]


det_checks = {}
closed_form_ok = True
for N in range(2, 8):
    k = N - 1
    d_IJ = det(IplusJ(k))                        # should be N (integer)
    det_checks[N] = {"det_I_plus_J": str(d_IJ), "closed_form_N": N, "matches": (d_IJ == N)}
    closed_form_ok = closed_form_ok and (d_IJ == N)
# and on the concrete configs, det(Gram) = N*(D/2)^{N-1}, nonzero
config_det_ok = {}
for N, pts in CONFIGS.items():
    G = gram_of_config(pts)
    dG = det(G)
    D = dist2(pts[0], pts[1])
    expect = Fr(N) * Fr(D, 2) ** (N - 1)
    config_det_ok[N] = {"det_gram": str(dG), "expected_N_times_half_D_pow": str(expect),
                        "nonzero": dG != 0, "matches": dG == expect}
all_nonzero = all(c["nonzero"] and c["matches"] for c in config_det_ok.values())
step("5.3", "the Gram determinant is N*(D/2)^(N-1) != 0",
     "det((D/2)(I+J)_{N-1}) = (D/2)^{N-1} * det(I+J)_{N-1} = (D/2)^{N-1} * N", ["5.2"],
     "the eigenvalues of I + J on R^{N-1} are N (once, eigenvector all-ones) and 1 (multiplicity "
     "N-2), so det(I + J)_{N-1} = N; scaling by D/2 gives det(Gram) = N*(D/2)^{N-1}. For D > 0 this "
     "is strictly positive, hence NONZERO. Verified exactly: det(I+J) = N for N = 2..7, and "
     "det(Gram) matches on the concrete configs. This nonzero Gram is the whole content of affine "
     "independence.",
     "UNIQUE (the determinant is a fixed nonzero value)", "DERIVED",
     {"det_I_plus_J": det_checks, "config_dets": config_det_ok,
      "closed_form": "N*(D/2)^(N-1)"},
     check="det(I+J)_{N-1} = N for N=2..7; det(Gram) nonzero on the configs")
assert closed_form_ok and all_nonzero

# ---- 5.4 affinely independent => dim >= N-1 -- DERIVED (concrete) ------------
bounds = {2: 1, 3: 2, 4: 3}
dim_bounds = {N: {"points": N, "dim_at_least": N - 1,
                  "gram_nonzero": config_det_ok.get(N, det_checks[N])["matches"] if N in config_det_ok else True}
              for N in (2, 3, 4)}
step("5.4", "nonzero Gram => affinely independent => dim >= N-1 (the tetrahedron is 3-D)",
     "det(Gram) != 0 => the N-1 differences are independent => the N points are affinely "
     "independent => ambient dim >= N-1", ["5.3"],
     "a nonzero Gram determinant means the N-1 difference vectors are linearly independent, so the "
     "N equidistant points are affinely independent, so the ambient space has dimension at least "
     "N-1. Concretely: 2 points force d>=1 (a line), 3 force d>=2 (a plane), 4 force d>=3 (a volume). "
     "This is the DERIVATION of 'the tetrahedron is genuinely 3-dimensional' -- replacing the "
     "retracted RUNG3-TETRAHEDRON-MINIMUM stipulation. The kernel checks the Gram determinants "
     "(N=2,3,4); the general det != 0 => independent => dim bound is the standard linear-algebra "
     "fact, now PROVED IN-REPO at Container05.EquidistantDimensionReal (Mathlib; see 5.6).",
     "the LOWER bound dim >= N-1 (the upper bound is NOT claimed -- see 03)", "DERIVED",
     {"dimension_bounds": dim_bounds, "reading": "2->line, 3->plane, 4->volume",
      "replaces": "retracted RUNG3-TETRAHEDRON-MINIMUM (now derived)"},
     check="dim >= N-1 for N=2,3,4 via the nonzero Gram determinant")

# ---- 5.5 correspondence, not identity -- POSTULATE (the reading) -------------
step("5.5", "the bridge is an EQUIVALENCE, not an identity -- the reading",
     "registration structure <-> Euclidean configuration (corresponds to); registration != point",
     ["5.1"],
     "the geometry is a CORRESPONDENCE the registration structure admits, not a claim that a "
     "registration IS a point in R^n. The relational floor (rungs 0-4.5) remains the substrate; the "
     "Euclidean picture is its faithful image across the bridge. This guards against reifying the "
     "coordinates -- 'all of math is a language ... to describe a thing' (Kevin). Held as the "
     "reading, capped.",
     "the reading (equivalence not identity), held", "POSTULATE",
     {"equivalence_not_identity": True, "substrate": "the relational floor (rungs 0-4.5)",
      "image": "the Euclidean configuration"},
     check=None)

# ---- 5.6 the general all-N theorem -- now PROVED IN-REPO (Mathlib) -----------
step("5.6", "the general all-N theorem -- now PROVED IN-REPO (Mathlib)",
     "for-all N: equidistant => affinely independent => finrank >= N-1", ["5.4"],
     "the GENERAL all-N statement -- and the formal 'det != 0 => independent => finrank >= N-1' "
     "chain -- is maths 4's RUNG5-EQUIDISTANT-DIMENSION (THEOREM). It was CITED while Maths 5 had "
     "no Mathlib; as of the Mathlib-setup session (2026-08-21) it is PROVED IN-REPO at "
     "Container05.EquidistantDimensionReal (equidistant_affineIndependent, "
     "equidistant_card_le_finrank_succ, and the concrete two/three/four_equidistant_force_*), which "
     "`import Mathlib` and so carry exactly Mathlib's three axioms (propext, Classical.choice, "
     "Quot.sound) -- kernel-confirmed by #print axioms. The Mathlib-free core (GeometricBridge.lean, "
     "N=2,3,4 by exact integer Gram determinant) stays ZERO-axiom; the two tiers are separate "
     "modules under one lib. Checked by the kernel (lake build), not by a cold Python recompute -- "
     "the model shows it as Lean-proved, not re-run. (The other thing this step once foreshadowed, "
     "METRIC dynamics, is built downstream as container 08 -- Kevin's ladder ordinal->bridge->metric.)",
     "the general lower bound dim >= N-1, proved in-repo (the UPPER bound is NOT claimed -- see 03)",
     "DERIVED",
     {"general_theorem": "maths 4 RUNG5-EQUIDISTANT-DIMENSION",
      "status": "proved in-repo at Container05.EquidistantDimensionReal (Mathlib) as of 2026-08-21",
      "proved_in_lean": True, "cold_recompute": False,
      "metric_dynamics": "built downstream as container 08", "built_here": True},
     check="the all-N equidistant => finrank >= N-1 theorem builds at Mathlib's three axioms")

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="05-geometric-bridge", steps=STEPS, grades=GRADES,
           values=dict(separation=2, det_I_plus_J={str(N): det_checks[N]["det_I_plus_J"]
                                                   for N in det_checks},
                       dimension_bounds={str(k): v for k, v in bounds.items()},
                       polarization_holds=polarization_holds, all_nonzero=all_nonzero))

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
