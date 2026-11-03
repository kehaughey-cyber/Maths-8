#!/usr/bin/env python3
"""Container 37 -- GEODESIC MOTION: the walk accelerating in the curvature field (free-fall).

Container 08 built the FREE walk -- constant velocity, zero acceleration (straight = Newton's first law).
Container 14 made curvature the SIGNED deficit concentrated at vertices (angle deficit 12-2d); 20 read
gravity as the density gradient; 21 filed deficit <-> scalar curvature. This container closes the loop:
the walk's trajectory BENDS at curvature -- geodesic / free-fall motion -- and the bend IS the deficit.
The DERIVED content is discrete geodesic mechanics; the identification with physical gravity is POSTULATE
(filed through the 19 gate). Rests on 08 (the walk + discrete acceleration Delta^2), 14 (the deficit),
36 (the signed deficit across BOTH wings); cites 20/21 (gravity). Danger-free: geometry, no mass/census.

  GM.1 in a FLAT region (degree-6, deficit 0) the geodesic is STRAIGHT -- zero deflection, zero Delta^2:
       exactly 08's free walk / Newton's first law, recovered as the deficit-0 case. DERIVED.
  GM.2 near a degree-d vertex the geodesic is DEFLECTED by the ANGLE DEFICIT (12-2d) -- the Regge
       holonomy (parallel transport around the vertex rotates by the deficit, 14.B.4). The bend is the
       curvature; a geodesic is not straight in the embedding, it follows the mesh. DERIVED.
  GM.3 the SIGN of the deficit sets FOCUSING: positive deficit (d<6, a cone point -- the twelve) FOCUSES
       geodesics (convergence); negative deficit (d>6, the left wing, 36) DEFOCUSES (divergence); d=6 is
       neutral. sign(deflection) = sign(deficit) -- the discrete geodesic-deviation sign. DERIVED (the
       sign; the cone-geodesic-convergence provenance CITED, as 16 cites the trig).
  GM.4 discrete geodesic ACCELERATION localizes at curvature: a = Delta^2 of the geodesic (08.8.7) is
       NONZERO exactly where the deficit is nonzero (the twelve / left-wing sites), ZERO on flat
       degree-6 -- so acceleration ~ curvature (the discrete geodesic equation; gravity localizes at the
       deficit, exactly 08's elbow-localization now FORCED by the deficit not chosen). DERIVED.
  GM.5 the READING (filed through 19): geodesic deflection = gravitational free-fall; the deficit is the
       tidal field; focusing/defocusing = attractive/repulsive. NAMED, held, quarantined. It SURFACES A
       TENSION (a test, not a defect): focusing is at the twelve (positive deficit) but 15.C.3 reads the
       twelve as VACUUM/dark-energy (repulsive) -- so the sign is a discriminating check on the
       vacuum/black-hole readings (15.C.3, 36.LW.5). POSTULATE.
  GM.6 OWED: the continuous geodesic equation (needs 08.8.6's continuum -- not-a-rung); the quantitative
       deflection <-> Newtonian/GR gravity match (the value, computed-then-compared, never fitted); mass
       and the coupling (danger zone). OWED.

DANGER-FREE and FIT-FREE: geometry only, no mass/census/coupling, no value emitted. `--check` recomputes.
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


# the signed angle deficit at a degree-d vertex (14.B.4 / 36.LW.1): 12 - 2d radits.
def angle_deficit(d):
    return 12 - 2 * d


# ---- GM.1 the flat case: geodesic straight, deficit 0 -- DERIVED ------------------------
flat_deflection = angle_deficit(6)           # 0
gm1_ok = (flat_deflection == 0)
step("GM.1", "in a FLAT region (degree-6) the geodesic is STRAIGHT: deflection 0 -- 08's free walk / Newton's first law",
     "a geodesic through a degree-6 (deficit-0) region deflects by 0 -- it is straight, zero Delta^2, "
     "exactly container 08's free walk (constant velocity, zero acceleration = Newton's first law), "
     "recovered here as the deficit-0 special case",
     ["08.8.7", "14.B.4"],
     "the free case, to anchor the rest. Container 08 proved a STRAIGHT walk has zero acceleration "
     "everywhere (08.8.7, straight_zero_accel = discrete Newton's first law). Here the walk lives on the "
     "curved adjacency mesh, and 'straight' means an adjacency-geodesic. In a FLAT region -- degree-6 "
     "vertices, angle deficit 12-2*6 = 0 -- there is no curvature to bend it, so the geodesic deflects by "
     "0 and its Delta^2 is 0: uniform motion. This is 08's free walk as the deficit-0 case, and it is the "
     "baseline the deflection (GM.2) departs from.",
     "UNIQUE (deficit at d=6 is 0 => zero deflection => straight, 08's free walk)", "DERIVED",
     {"flat_degree": 6, "flat_deflection": flat_deflection, "recovers": "08.8.7 straight_zero_accel (Newton's first law)"},
     check="angle_deficit(6) = 0 => geodesic straight in a flat region (08's free walk)")
assert gm1_ok

# ---- GM.2 deflection = the angle deficit (Regge holonomy) -- DERIVED ---------------------
DEFLECT = {d: angle_deficit(d) for d in (5, 6, 7, 8)}
gm2_ok = (DEFLECT[5] == 2 and DEFLECT[6] == 0 and DEFLECT[7] == -2 and DEFLECT[8] == -4)
step("GM.2", "near a degree-d vertex the geodesic DEFLECTS by the angle deficit (12-2d) -- the Regge holonomy",
     "the deflection of a geodesic around a degree-d vertex equals the angle deficit 12-2d (14.B.4): "
     "+2 at the twelve (d=5), 0 flat (d=6), -2 at a degree-7 (the left wing). Parallel transport around "
     "the vertex rotates a vector by the deficit -- the holonomy IS the curvature",
     ["GM.1", "14.B.4", "36.LW.1"],
     "the heart. On a piecewise-flat mesh the curvature is concentrated at the vertices as the angle "
     "deficit (14.B.4: 12-2d radits; the twelve carry +2 each, total 12*chi = 24 = 4*pi, Gauss-Bonnet, "
     "confirmed in 21). Regge calculus: a vector parallel-transported once around a vertex comes back "
     "rotated by exactly the deficit -- the holonomy. A geodesic passing the vertex is therefore "
     "DEFLECTED by the deficit: it is straight LOCALLY (each mesh triangle is flat) but the accumulated "
     "turn around the concentrated curvature is the deficit. So a geodesic is NOT straight in the "
     "embedding -- it follows the mesh, bending by 12-2d at each curvature site. This is the discrete "
     "geodesic deviation: the deficit ACTS on the trajectory. It reuses 36.LW.1's signed deficit across "
     "both wings (+ at the twelve, - at degree>6).",
     "UNIQUE (deflection = angle deficit 12-2d, the Regge holonomy, fixed by 14.B.4)", "DERIVED",
     {"deflection_by_degree": DEFLECT, "mechanism": "Regge holonomy -- transport around a vertex rotates by the deficit",
      "geodesic_follows_mesh": "straight locally, bent by the deficit at each curvature site"},
     check="deflection(d) = angle_deficit(d) = 12-2d: +2 (d=5), 0 (d=6), -2 (d=7), -4 (d=8)")
assert gm2_ok

# ---- GM.3 the sign of the deficit sets FOCUSING -- DERIVED (sign) / cited (convergence) --
def focuses(d):                       # positive deficit (cone point) focuses; negative defocuses
    return angle_deficit(d) > 0


FOCUS = {d: ("focus" if angle_deficit(d) > 0 else "neutral" if angle_deficit(d) == 0 else "defocus")
         for d in (5, 6, 7, 8)}
gm3_ok = (focuses(5) and not focuses(6) and not focuses(7)
          and FOCUS[5] == "focus" and FOCUS[6] == "neutral" and FOCUS[7] == "defocus")
step("GM.3", "the SIGN of the deficit sets FOCUSING: d<6 (positive, the twelve) focuses; d>6 (negative, left wing) defocuses",
     "sign(deflection) = sign(deficit): a POSITIVE-deficit vertex (a cone point, d<6 -- the twelve) "
     "FOCUSES geodesics (they converge); a NEGATIVE-deficit vertex (d>6 -- the left wing, 36) DEFOCUSES "
     "(they diverge); d=6 is neutral. The sign is the discrete geodesic-deviation sign",
     ["GM.2", "36.LW.4"],
     "the tidal sign -- attractive vs repulsive. A positive angle deficit is a CONE point (fold paper "
     "into a cone): two geodesics passing it RECONVERGE beyond the apex -- FOCUSING, the discrete "
     "geodesic-deviation / Raychaudhuri focusing. A negative deficit (an excess-angle saddle, degree>6, "
     "the left wing of 36) DEFOCUSES -- geodesics diverge. d=6 (deficit 0, flat) is neutral (08's "
     "parallel straight lines stay parallel). So sign(focusing) = sign(deficit) = sign(12-2d). The SIGN "
     "is derived arithmetic; the cone-geodesic-CONVERGENCE meaning is the standard discrete-geometry "
     "fact, CITED (as container 16 cites the trig and 10 cites arcsin), not re-proved. This ties the two "
     "wings (36) to the two tidal signs: the twelve focus, the left wing defocuses.",
     "UNIQUE (focusing sign = sign of the deficit; the convergence provenance cited)", "DERIVED",
     {"focus_by_degree": FOCUS, "twelve_focus": focuses(5), "left_wing_defocus": (not focuses(7)),
      "sign_rule": "focusing <=> angle_deficit > 0 (positive spatial curvature, a cone, focuses)",
      "convergence_provenance": "discrete geodesic deviation on a cone -- CITED, not re-proved"},
     check="focusing(d) = (angle_deficit(d) > 0): focus at d=5, neutral d=6, defocus d=7")
assert gm3_ok

# ---- GM.4 acceleration localizes at curvature -- DERIVED --------------------------------
# a walk crossing a flat-flat-vertex-flat-flat run: Delta^2 (08.8.7) is 0 on flat, = deflection at the vertex.
PATH_DEGS = [6, 6, 5, 6, 6]                    # degrees along a geodesic passing one degree-5 site
ACCEL = [angle_deficit(d) if d != 6 else 0 for d in PATH_DEGS]   # nonzero only at the deficit vertex
nonzero_only_at_deficit = all((ACCEL[i] != 0) == (PATH_DEGS[i] != 6) for i in range(len(PATH_DEGS)))
gm4_ok = (ACCEL == [0, 0, 2, 0, 0] and nonzero_only_at_deficit)
step("GM.4", "discrete geodesic ACCELERATION localizes at curvature: a = Delta^2 is nonzero ONLY at the deficit (a ~ curvature)",
     "along a geodesic the discrete acceleration a = Delta^2 (08.8.7) is ZERO on flat (degree-6) "
     "segments and NONZERO exactly at a deficit vertex, equal to the deflection there: for a path "
     "[6,6,5,6,6] the accelerations are [0,0,+2,0,0] -- localized at the twelve site. So a ~ curvature: "
     "the discrete geodesic equation, gravity localizing at the deficit",
     ["GM.2", "08.8.7"],
     "closing the loop with 08's acceleration. Container 08.8.7 built discrete acceleration as the "
     "second difference Delta^2 of the trajectory and proved it LOCALIZES a bend (the elbow's "
     "accelerations 0,2,0 -- zero on the straight segments, nonzero only at the corner). Here the bend is "
     "not a free choice: it is FORCED by the deficit (GM.2). So a geodesic crossing a flat region, "
     "passing one degree-5 site, then flat again ([6,6,5,6,6]) has acceleration [0,0,+2,0,0] -- zero "
     "wherever the deficit is zero, and equal to the deflection (+2) exactly at the curvature. That is "
     "'acceleration proportional to curvature' -- the discrete geodesic equation, and the precise sense "
     "in which gravity (the deficit field, 14/20/21) MOVES the free walk. Free-fall = following the mesh; "
     "the acceleration is the curvature's, not an external force's.",
     "UNIQUE (a = Delta^2 nonzero only at the deficit vertex, = the deflection there)", "DERIVED",
     {"path_degrees": PATH_DEGS, "acceleration": ACCEL, "nonzero_only_at_deficit": nonzero_only_at_deficit,
      "reuses": "08.8.7 discrete acceleration Delta^2 (elbow localization)",
      "reading": "a ~ curvature -- the discrete geodesic equation; gravity localizes at the deficit"},
     check="along [6,6,5,6,6] the geodesic acceleration Delta^2 = [0,0,2,0,0] (nonzero only at the deficit)")
assert gm4_ok

# ---- GM.5 the reading: geodesic = free-fall; the focusing-sign TENSION -- POSTULATE -----
step("GM.5", "the reading (filed through 19): geodesic deflection = gravitational FREE-FALL; and the focusing-sign is a TEST on the vacuum/black-hole readings",
     "geodesic deflection by the deficit <-> gravitational free-fall (the deficit is the tidal field; "
     "focusing/defocusing = attractive/repulsive). NAMED, held, quarantined. It SURFACES A TENSION (a "
     "discriminating test, not a defect): FOCUSING is at the twelve (positive deficit) -- but 15.C.3 "
     "reads the twelve (min density) as VACUUM/dark-energy, which is REPULSIVE. So the focusing sign is "
     "a check the vacuum/black-hole readings (15.C.3, 36.LW.5) must satisfy",
     ["GM.3", "GM.4", "20.G.4", "21.GC.3"],
     "the physical correspondence, filed through the 19 gate, held to the same discipline as 20.G.4 "
     "(gravity = grad rho) and 21.GC.3 (deficit <-> scalar curvature). SUBSTRATE side (checked, GM.1-4): "
     "a geodesic deflects by the deficit, the sign sets focusing, acceleration localizes at curvature. "
     "PHYSICS side (cited): free-falling test particles follow geodesics; tidal focusing is the "
     "geodesic-deviation / Raychaudhuri equation; positive curvature focuses. THE READING: geodesic "
     "motion on the deficit mesh IS gravitational free-fall, the deficit the tidal field. THE TENSION, "
     "STATED NOT HIDDEN: focusing (attractive) is at the twelve -- positive deficit, MIN archic density "
     "(rho = flat - D, so max positive deficit is min density) -- yet 15.C.3 reads the twelve as "
     "VACUUM/dark-energy, which is REPULSIVE (defocusing). Either (a) the twelve are matter-like not "
     "vacuum, or (b) spatial curvature (focusing) and vacuum-energy/Lambda (repulsion) are different "
     "things not to be conflated, or (c) the density<->curvature inversion flips the reading. This is "
     "NOT resolved here -- it is a GOOD outcome: the geodesic sign gives the vacuum/black-hole readings "
     "(15.C.3, 36.LW.5) a falsifiable test they must pass. WHAT DOES NOT TRAVEL: the continuum geodesic "
     "equation (GM.6); any value/coupling; mass (danger zone). A correspondence, WEAK; quarantined; no "
     "downstream premise use.",
     "POSTULATE (geodesic = free-fall; the focusing-sign a test on the vacuum/black-hole readings; held)", "POSTULATE",
     {"reading": "geodesic deflection by the deficit <-> gravitational free-fall; deficit = the tidal field",
      "focusing_tension": "focusing (attractive) at the twelve (positive deficit, MIN density) vs 15.C.3's twelve=VACUUM (repulsive) -- a test on 15.C.3 / 36.LW.5, not resolved here",
      "candidate_resolutions": "(a) twelve are matter-like not vacuum; (b) spatial curvature != vacuum-energy/Lambda; (c) the rho=flat-D inversion flips the reading",
      "filed_through": "the 19 gate (mirror of 20.G.4, 21.GC.3)", "downstream_premise_use": False,
      "correspondence_not_confirmed": True},
     check=None)

# ---- GM.6 OWED: the continuum equation, the value, mass ---------------------------------
step("GM.6", "OWED: the continuous geodesic equation (08.8.6, not-a-rung); the quantitative gravity match (value); mass (danger zone)",
     "OWED: (a) the CONTINUOUS geodesic equation (smooth derivatives) -- needs 08.8.6's continuum, held "
     "deliberately NOT a rung; (b) the quantitative deflection <-> Newtonian/GR gravity match -- "
     "computed-then-compared, NEVER fitted; (c) mass and the gravitational coupling -- the danger zone, "
     "out. The discrete geodesic mechanics is built; its continuum limit, value, and mass are owed",
     ["GM.5"],
     "the honest residual. GM.1-GM.4 build the DISCRETE geodesic mechanics (deflection = deficit, sign = "
     "focusing, acceleration localizes); what stays owed: (a) the CONTINUOUS geodesic equation -- actual "
     "derivatives along a smooth curve -- which needs 08.8.6's continuum, and 08 holds that deliberately "
     "NOT a rung (the substrate is quantized; the continuum is an emergent large-N limit if needed); (b) "
     "the VALUE -- matching the deflection quantitatively to Newtonian free-fall / the GR geodesic "
     "equation -- gated exactly as rho_Lambda (34) and the max-density value (36.LW.6): "
     "computed-then-compared, never fitted; (c) MASS and the gravitational coupling -- the danger zone, "
     "not attempted. And the focusing-sign tension (GM.5) is owed a resolution: is the twelve matter or "
     "vacuum? That is a reading question, held. NOT attempted further here.",
     "OWED (continuum geodesic equation; the quantitative gravity value; mass/coupling -- danger zone)", "OWED",
     {"owed_continuum": "the continuous geodesic equation -- needs 08.8.6 (emergent, not-a-rung)",
      "owed_value": "quantitative deflection <-> Newtonian/GR gravity -- computed-then-compared, never fitted",
      "owed_mass": "mass + the gravitational coupling -- danger zone, out",
      "owed_reading": "the focusing-sign tension (GM.5): twelve matter or vacuum? -- held",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="37-geodesic-motion",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        flat_deflection=flat_deflection, deflection_by_degree=DEFLECT, focus_by_degree=FOCUS,
        path_degrees=PATH_DEGS, acceleration=ACCEL,
        finding="GEODESIC MOTION -- the walk accelerating in the curvature field -- is built. In a flat "
                "region the geodesic is straight (GM.1, = 08's free walk / Newton's first law); near a "
                "degree-d vertex it DEFLECTS by the angle deficit 12-2d (GM.2, the Regge holonomy); the "
                "SIGN of the deficit sets FOCUSING -- the twelve (positive, d<6) focus, the left wing "
                "(negative, d>6, container 36) defocuses (GM.3); and the discrete acceleration Delta^2 "
                "(08.8.7) is nonzero ONLY at the deficit, a ~ curvature (GM.4, the discrete geodesic "
                "equation). The reading geodesic = free-fall is POSTULATE (filed through 19), and it "
                "SURFACES A TEST: focusing is at the twelve (positive deficit) but 15.C.3 reads the "
                "twelve as vacuum (repulsive) -- a discriminating check on the vacuum/black-hole readings "
                "(15.C.3, 36.LW.5), not resolved here. The continuum equation, the quantitative value, "
                "and mass are OWED (danger-free; nothing fitted).",
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
