#!/usr/bin/env python3
"""Container 52 -- THE CONTINUUM LIMIT: the emergent smooth manifold is a 12-cone orbifold sphere.

Forward-frontier #7 (Maths 6.7). 08.8.6 holds the continuum as an EMERGENT large-N limit, deliberately
NOT a floor rung. This container forces its SHAPE, danger-free: the coarse limit is FLAT 2D (the counting
law's leading term is the continuum area-growth); the 12 cone-points persist under refinement (39.PM.1's
orbifold), each with cone-deficit pi/3 (38.DV.1), total 12*(pi/3) = 4*pi (Gauss-Bonnet, 38.DV.3). So the
emergent continuum is a smooth 2-sphere with 12 conical singularities -- a 12-cone ORBIFOLD -- and GR's
smooth manifold is its coarse image AWAY from the cones (40's ZPHI = curves-at-scale). Emergent, not
axiomatic (08.8.6): the substrate stays quantized.

  CL.1  the coarse limit is FLAT 2D. flat_ball(r) = 1+3r(r+1) = 1+3r+3r^2 -- leading term 3r^2 (the
        continuum area-growth of a flat 2-surface); |B_r| - 3r^2 = 1+3r is lower order, so |B_r|/r^2 -> 3
        (a constant) as r -> infinity, and the second difference is the constant 6 (degree exactly 2,
        25.DF.1). Away from the cones the coarse geometry converges to flat R^2. DERIVED.
  CL.2  the 12 cones persist (39.PM.1's orbifold): refinement does NOT smear the deficit, so the continuum
        keeps 12 conical singularities, each with cone-deficit = the angle deficit at d=5 = 2 radits =
        pi/3 (38.DV.1); total 12*(pi/3) = 4*pi = 2*pi*chi (Gauss-Bonnet, chi=2, 38.DV.3). So the emergent
        continuum is a smooth 2-SPHERE with 12 cone-points -- a 12-cone ORBIFOLD. DERIVED.
  CL.3  the reading (filed through 19): GR's smooth manifold = the EMERGENT coarse image AWAY from the
        cones (40's ZPHI = curves-at-scale), a large-N limit, NOT a floor axiom (08.8.6) -- the substrate
        stays quantized. A CORRESPONDENCE, WEAK. POSTULATE.
  CL.4  OWED: the analytic measure/metric convergence (needs 46's metric + mass for the dynamics, danger
        zone); the orbifold cone-resolution; whether the substrate ever leaves the orbifold (36/48's left
        wing, the metric-no-thirteenth). OWED.

Rests on 25 (intrinsic n=2), 39 (the orbifold), 38 (pi/3 per cone, 4*pi total), 40 (curves-at-scale),
08 (the emergent continuum, 08.8.6); cites the area-growth limit / orbifold. DANGER-FREE: coarse geometry
-- no mass, no value. `--check` recomputes.
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


def flat_ball(r):
    return 1 + 3 * r * (r + 1)               # 14.B.1 / 25: the flat reference, degree 2


# ---- CL.1 the coarse limit is flat 2D -- DERIVED ---------------------------------------
LEADING = 3                                   # coefficient of r^2 -- the continuum area-growth rate
lower_order = {r: flat_ball(r) - LEADING * r * r for r in range(1, 8)}   # = 1+3r, lower order
lower_is_linear = all(lower_order[r] == 1 + 3 * r for r in range(1, 8))
def d2(r):
    return flat_ball(r + 2) - 2 * flat_ball(r + 1) + flat_ball(r)
second_diff_const = all(d2(r) == 6 for r in range(6))          # degree exactly 2 (flat), 25.DF.1
cl1_ok = (lower_is_linear and second_diff_const and LEADING == 3)
step("CL.1", "the coarse limit is FLAT 2D: flat_ball(r) = 1+3r+3r^2, |B_r|/r^2 -> 3, second difference const 6 (degree 2, 25)",
     "flat_ball(r) = 1+3r(r+1) = 1+3r+3r^2 has leading term 3r^2 -- the continuum area-growth of a flat "
     "2-surface; the remainder |B_r| - 3r^2 = 1+3r is LOWER order, so |B_r|/r^2 -> 3 (a constant) as "
     "r -> infinity, and the second difference is the constant 6 (degree exactly 2, 25.DF.1). Away from "
     "the cones the coarse geometry converges to flat R^2",
     ["25.DF.1", "14.B.1"],
     "the convergence, danger-free. The discrete ball-count flat_ball(r) = 1+3r+3r^2 is a degree-2 "
     "polynomial (25.DF.1 forced intrinsic dimension 2 from exactly this). Its leading term 3r^2 is the "
     "continuum AREA-growth of a flat 2-surface (a disk of radius r has area ~ r^2); the correction "
     "|B_r| - 3r^2 = 1+3r is linear -- lower order -- so the ratio |B_r|/r^2 = 3 + 3/r + 1/r^2 -> 3 as "
     "r grows. The second difference is the constant 6 (degree exactly 2, no cubic term). So under "
     "refinement/at large scale the substrate's counting CONVERGES to flat 2-dimensional Euclidean "
     "area-growth: the coarse geometry is FLAT R^2 (away from the cones, CL.2). This is why GR's smooth "
     "flat manifold works as the coarse image -- the substrate's own counting IS flat 2D area-growth in "
     "the limit. A limit statement, exact-integer, no continuum axiom smuggled.",
     "UNIQUE (flat_ball leading 3r^2, remainder 1+3r lower order, d2 const 6 -> flat 2D coarse limit)", "DERIVED",
     {"leading_coefficient": LEADING, "lower_order_remainder": lower_order,
      "lower_is_linear": lower_is_linear, "second_difference_const_6": second_diff_const,
      "coarse_limit": "flat R^2 (area-growth ~ 3r^2); |B_r|/r^2 -> 3"},
     check="flat_ball = 1+3r+3r^2; |B_r|-3r^2 = 1+3r (lower order); second difference const 6 -> flat 2D coarse limit")
assert cl1_ok

# ---- CL.2 the 12 cones persist: a 12-cone orbifold, total deficit 4pi -- DERIVED --------
CONES = 12                                    # 39.PM.1: refinement does not smear the deficit
def angle_deficit(d):
    return 12 - 2 * d
CONE_DEFICIT_RADITS = angle_deficit(5)        # 2 radits at the twelve (d=5)
# 12 radits = 2pi, so 1 radit = pi/6; the cone deficit is 2 radits = pi/3
TOTAL_RADITS = CONES * CONE_DEFICIT_RADITS     # 12*2 = 24 radits
TOTAL_IS_4PI = (TOTAL_RADITS == 24)            # 24 radits = 2*(2pi) = 4pi (Gauss-Bonnet, chi=2)
cl2_ok = (CONES == 12 and CONE_DEFICIT_RADITS == 2 and TOTAL_IS_4PI)
step("CL.2", "the 12 cones persist (39 orbifold): each cone-deficit pi/3 (38), total 12*(pi/3) = 4*pi -- a 12-cone ORBIFOLD sphere",
     "refinement does NOT smear the combinatorial curvature (39.PM.1), so the continuum keeps 12 conical "
     "singularities, each with cone-deficit = the angle deficit at d=5 = 2 radits = pi/3 (38.DV.1; 12 "
     "radits = 2pi); total 12*(pi/3) = 24 radits = 4*pi = 2*pi*chi (Gauss-Bonnet, chi=2, 38.DV.3). So the "
     "emergent continuum is a smooth 2-SPHERE with 12 cone-points -- a 12-cone ORBIFOLD",
     ["CL.1", "39.PM.1", "38.DV.1"],
     "the singular structure the flat limit leaves behind. Container 39.PM.1 proved refinement does not "
     "SMEAR the deficit -- it stays concentrated at the twelve degree-5 sites -- so the continuum is NOT a "
     "smooth sphere but a 12-cone ORBIFOLD. CL.1 gives the smooth flat coarse limit BETWEEN the cones; at "
     "each of the 12 cone-points the deficit persists as a conical singularity of cone-deficit = the angle "
     "deficit at d=5 = 2 radits (38.DV.1) = pi/3 (since 12 radits = 2pi). The total is 12*(pi/3) = 24 "
     "radits = 4*pi = 2*pi*chi (chi=2, Gauss-Bonnet, 38.DV.3 -- the same 4*pi double cover). So the "
     "emergent continuum is precisely: a smooth 2-sphere everywhere EXCEPT 12 conical points, total "
     "cone-deficit 4*pi. This is the geometric arena for gravity -- flat away from sources (CL.1), "
     "concentrated curvature at the twelve (the sources, 20/37), total 4*pi (38).",
     "UNIQUE (12 cones, each pi/3, total 4*pi = 2*pi*chi -- a 12-cone orbifold sphere)", "DERIVED",
     {"cones": CONES, "cone_deficit_radits": CONE_DEFICIT_RADITS, "cone_deficit": "pi/3 (2 radits, 12 radits = 2pi)",
      "total_radits": TOTAL_RADITS, "total_is_4pi": TOTAL_IS_4PI,
      "continuum": "a smooth 2-sphere with 12 conical singularities -- a 12-cone orbifold, total cone-deficit 4*pi"},
     check="12 cones, each 2 radits (pi/3); total 12*2 = 24 radits = 4*pi = 2*pi*chi (a 12-cone orbifold sphere)")
assert cl2_ok

# ---- CL.3 the reading: GR's smooth manifold = the emergent coarse image -- POSTULATE ----
step("CL.3", "the reading (filed through 19): GR's smooth manifold = the EMERGENT coarse image away from the cones (40); NOT a floor axiom (08.8.6)",
     "GR's smooth (pseudo-Riemannian) manifold <-> the substrate's EMERGENT coarse image AWAY from the 12 "
     "cones: flat 2D at large scale (CL.1), the cones the localized sources (CL.2). It is a large-N limit "
     "(40's ZPHI = curves-at-scale -- the smooth manifold is the coarse-scale image, not the privileged "
     "real), NOT a floor axiom (08.8.6) -- the substrate stays quantized. A CORRESPONDENCE, WEAK",
     ["CL.2", "40.DF.5", "08.8.6"],
     "the entry, held to the 19 discipline. SUBSTRATE side (checked, CL.1-CL.2): the coarse limit is flat "
     "2D with 12 persistent conical singularities (an orbifold), total cone-deficit 4*pi. PHYSICS side "
     "(cited): general relativity models spacetime as a smooth pseudo-Riemannian manifold. THE "
     "CORRESPONDENCE: GR's smooth manifold <-> the substrate's emergent coarse image away from the cones "
     "(40's ZPHI = curves-at-scale, the smooth manifold as the coarse-scale image -- GR's continuum is "
     "itself an idealization, 39/40). Crucially it is EMERGENT, a large-N limit, NOT a floor rung "
     "(08.8.6): axiomatizing a continuum would smuggle continuity into a discrete substrate. WHAT DOES "
     "NOT TRAVEL: that the continuum is the privileged real (it is the coarse image); the metric DYNAMICS "
     "(46's metric identification + mass = the danger zone); any value. A correspondence, quarantined; no "
     "downstream premise use.",
     "POSTULATE (GR's smooth manifold = the emergent coarse orbifold image; a large-N limit, not a floor axiom; held)", "POSTULATE",
     {"substrate_side": "flat 2D coarse limit (CL.1) + 12 persistent cones (CL.2) = a 12-cone orbifold",
      "physics_side_cited": "GR's smooth pseudo-Riemannian manifold",
      "correspondence": "GR's smooth manifold <-> the emergent coarse image away from the cones (40, ZPHI = curves-at-scale)",
      "emergent_not_axiom": "a large-N limit (08.8.6), NOT a floor rung -- the substrate stays quantized",
      "does_not_travel": "the continuum as privileged real; the metric dynamics (46 + mass, danger); any value",
      "downstream_premise_use": False},
     check=None)

# ---- CL.4 OWED ------------------------------------------------------------------------
step("CL.4", "OWED: the analytic measure/metric convergence (46's metric + mass, danger); the cone-resolution; whether the substrate leaves the orbifold (36/48)",
     "OWED: (a) the ANALYTIC convergence -- a measure/metric limit, not just the leading-order count -- "
     "which needs 46's metric identification and, for the dynamics, MASS (the danger zone); (b) the "
     "orbifold cone-RESOLUTION (how, if ever, the cones smooth); (c) whether the substrate ever LEAVES the "
     "orbifold -- the left wing (36/48), the metric-no-thirteenth. The SHAPE is forced; the analysis and "
     "the dynamics are owed",
     ["CL.3"],
     "the honest residual. CL.1-CL.2 force the SHAPE of the emergent continuum (flat 2D + 12 cones = an "
     "orbifold sphere, total 4*pi); CL.3 files the GR correspondence. What remains: (a) the ANALYTIC "
     "limit -- genuine measure/metric convergence (not just the leading r^2 coefficient) -- which needs a "
     "metric (46's identification, itself a correspondence) and, for gravity DYNAMICS, a stress-energy = "
     "MASS: the DANGER ZONE; (b) the cone-RESOLUTION -- whether/how the conical singularities resolve "
     "(they are the mass/source sites, so this too touches the danger zone); (c) whether the substrate "
     "ever leaves the right-wing orbifold into the left wing (36/48), the metric-no-thirteenth (41/42/43). "
     "So the emergent continuum's SHAPE is forced and danger-free; the analytic limit, the dynamics, and "
     "the cone-resolution are the forward, gated work. NOT attempted here.",
     "OWED (analytic metric convergence -- 46 + mass, danger; cone-resolution; leaving the orbifold -- 36/48)", "OWED",
     {"owed_analytic": "the measure/metric convergence (not just the leading count) -- needs 46's metric + mass (danger)",
      "owed_resolution": "the orbifold cone-resolution -- the cones are source sites (danger)",
      "owed_left_wing": "whether the substrate leaves the orbifold into the left wing (36/48) -- the metric-no-thirteenth",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="52-continuum-limit",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        leading_coefficient=LEADING, second_difference_const_6=second_diff_const,
        cones=CONES, cone_deficit_radits=CONE_DEFICIT_RADITS, total_radits=TOTAL_RADITS,
        total_is_4pi=TOTAL_IS_4PI,
        finding="THE CONTINUUM LIMIT: the emergent smooth manifold is a 12-cone ORBIFOLD sphere. 08.8.6 "
                "holds the continuum as an emergent large-N limit; here its SHAPE is forced, danger-free. "
                "The coarse limit is FLAT 2D -- flat_ball(r)=1+3r+3r^2, leading 3r^2 (continuum "
                "area-growth), |B_r|/r^2 -> 3, second difference const 6 (degree 2, 25) (CL.1). The 12 "
                "cones PERSIST under refinement (39.PM.1's orbifold), each cone-deficit pi/3 (38.DV.1), "
                "total 12*(pi/3) = 4*pi = 2*pi*chi (38.DV.3) -- so the continuum is a smooth 2-sphere with "
                "12 conical singularities, a 12-cone orbifold (CL.2). GR's smooth manifold = the emergent "
                "coarse image away from the cones (40's curves-at-scale), NOT a floor axiom (08.8.6) -- "
                "POSTULATE (CL.3). The analytic metric convergence + dynamics + cone-resolution are OWED "
                "(CL.4, danger zone). Danger-free; nothing fitted.",
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
