#!/usr/bin/env python3
"""Container 36 -- NEGATIVE CURVATURE: the LEFT WING of the mirror (the max-density direction).

Builds what container 15 (density-extremum, C.2/C.3) DEFERRED: the negative-curvature side. The right
wing (13-16) is the icosahedral 2-sphere -- degree-5 sites (the twelve, D>0, MIN density) and degree-6
(flat, D=0, the MIRROR); it realizes only D>=0, one-sided BY CONSTRUCTION (15.C.2). This container builds
the OTHER sign: degree>6 (hyperbolic) sites, D<0, the MAX-density direction -- forced-never-fitted, cold.

Rests on 14 (the flat reference flat_ball = 1+3r(r+1) and the signed deficit D = flat - |B_r|; 14.B.2/B.4)
and 15 (the extremum / the deferred max side). The number is a build-order label.

  LW.1 the signed curvature at a degree-d vertex EXTENDS ACROSS THE MIRROR: angle deficit (12-2d) and
       ball-deficit D_1 = (6-d). d<6 => + (right, min-density, the twelve); d=6 => 0 (mirror, flat);
       d>6 => NEGATIVE (LEFT, max-density). DERIVED.
  LW.2 an explicit degree-7 STAR realizes the first negative-curvature site: |B_1| = 8 > flat_ball(1) = 7,
       so D_1 = -1 < 0 and rho = 8 EXCEEDS the right wing's rho_max = flat = 7. The max-density direction
       is REALIZED (what 15.C.2 said needs "a different, buildable geometry" -- here it is). DERIVED.
  LW.3 the {3,7} hyperbolic tiling grows FASTER than flat, VALIDATED cold: the {3,d} coordination
       recurrence reproduces flat {3,6} = 6n EXACTLY (the internal guard), then at d=7 gives rings
       [7,21,56,147,385], |B_r| = [1,8,29,85,232,617], D_r = [0,-1,-10,-48,-171,-526] < 0 and GROWING
       (exponential) -- the max-density deficit is UNBOUNDED, the mirror of the twelve's bounded tri(r).
       DERIVED (exact-integer; the flat-reproduction is the check).
  LW.4 TOPOLOGY (why the wings live on different surfaces): Gauss-Bonnet sum(12-2d) = 12*chi. Right wing
       (twelve deg-5): +24 => chi=2, genus 0 (the sphere, 14/15). All-deg>6: sum<0 => chi<0 => genus>=2
       (closed) or the OPEN hyperbolic plane. So the left wing is NOT a genus-0 sphere -- which is exactly
       WHY the right wing is forced one-sided D>=0 (chi=2>0 forbids net-negative, 15.C.2). DERIVED.
  LW.5 the READING (mirror of 15.C.3): max archic density <-> the BLACK-HOLE direction (Schwarzschild
       attaches). NAMED as a possibility, NOT confirmed -- the same discipline 15 applied to the vacuum
       side. Connects to the metric-no-thirteenth (degree>6 = the 13th-neighbour room). POSTULATE.
  LW.6 OWED: the closed higher-genus realization; the max-density / Schwarzschild VALUE; and whether the
       SUBSTRATE ever realizes degree>6 (does registration go LEFT of the mirror?) -- the metric-no-
       thirteenth (03.3.7 / 09.6.6 / 25.DF.3 / 01.1.6) from the other side. OWED.

DANGER-FREE: pure geometry/counting (no mass, no census, no coupling). Nothing is fitted; the black-hole
reading is POSTULATE, the value OWED. `--check` recomputes the DERIVED steps.
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


# ================================================================ the flat reference (container 14, cited)
def flat_ball(r):            # 14.B.1 -- the defect-zero (degree-6) reference; ONE HOME is container 14
    return 1 + 3 * r * (r + 1)


def flat_ring(r):            # the flat triangular ring: 6r
    return 6 * r


# ---- LW.1 the signed curvature across the mirror -- DERIVED ------------------------------
def angle_deficit(d):        # 14.B.4: equilateral degree-d vertex, 2pi - d*(pi/3) in radits (12 = 2pi)
    return 12 - 2 * d


def ball_deficit_1(d):       # D_1 = flat_ball(1) - (d+1) = 7 - (d+1) = 6 - d
    return 6 - d


DEG_TABLE = {d: {"angle_deficit": angle_deficit(d), "D_1": ball_deficit_1(d),
                 "sign": ("+ right/min-density" if d < 6 else "0 mirror/flat" if d == 6 else "- LEFT/max-density")}
             for d in (5, 6, 7, 8)}
lw1_ok = (ball_deficit_1(5) == 1 and ball_deficit_1(6) == 0 and ball_deficit_1(7) == -1
          and angle_deficit(7) == -2 and angle_deficit(5) == 2)
step("LW.1", "signed curvature at a degree-d vertex EXTENDS across the mirror: D_1 = 6-d (angle deficit 12-2d)",
     "the deficit D_1 = flat_ball(1) - |B_1| = 7 - (d+1) = 6 - d, and the angle deficit = 12 - 2d "
     "(14.B.4): d<6 => +(right, min-density, the twelve); d=6 => 0 (the mirror, flat); d>6 => NEGATIVE "
     "(the LEFT wing, max-density)",
     ["14.B.2", "14.B.4"],
     "container 14 made the deficit SIGNED (D>0 spherical, D=0 flat/the mirror, D<0 hyperbolic) but the "
     "icosahedral substrate realizes only D>=0 (degree<=6 everywhere). Reading the SAME formula across "
     "the mirror: at a degree-d vertex the ball-deficit at r=1 is D_1 = flat_ball(1) - |B_1| = 7 - (d+1) "
     "= 6-d, and the angle deficit (14.B.4) is 12-2d. For d = 5 (the twelve): +1 / +2 (positive curvature, "
     "SLOWER-than-flat growth, MIN density). For d = 6 (flat): 0 / 0 (the mirror). For d > 6: NEGATIVE "
     "(faster-than-flat growth, hyperbolic, MAX density). So the mirror at D=0 has a genuine LEFT side, "
     "and it is the degree>6 sites -- exactly the 'faster-than-flat, hyperbolic' D<0 that 14.B.2 named but "
     "the sphere never realized. This is the sign-mirror image of the twelve.",
     "UNIQUE (D_1 = 6-d, angle deficit = 12-2d, fixed by the equilateral-triangulation convention)", "DERIVED",
     {"table": DEG_TABLE, "mirror_at": "d=6 (D_1=0), the flat degree-6 site",
      "left_wing_is": "degree > 6 (D_1 < 0, angle deficit < 0) -- the max-density direction"},
     check="D_1(d) = 6-d and angle_deficit(d) = 12-2d; negative for d>6")
assert lw1_ok

# ---- LW.2 the explicit degree-7 star realizes the first negative-curvature site -- DERIVED
# center c=0; a 7-cycle n0..n6 (verts 1..7); triangles c-ni-n(i+1) => each ni adjacent to c and n(i+-1).
STAR_V = list(range(8))                                   # 0 = centre (degree 7), 1..7 = the ring
STAR_E = [(0, i) for i in range(1, 8)] + [(i, 1 + (i % 7)) for i in range(1, 8)]  # spokes + the 7-cycle


def _adj(edges, a, b): return (a, b) in edges or (b, a) in edges


def _ball1(edges, verts, v):
    s = {v} | {w for w in verts if _adj(edges, v, w)}
    return len(s)


star_deg0 = sum(1 for w in STAR_V if _adj(STAR_E, 0, w))   # centre degree
star_B1 = _ball1(STAR_E, STAR_V, 0)                        # |B_1| at the centre
star_D1 = flat_ball(1) - star_B1                           # 7 - 8 = -1
lw2_ok = (star_deg0 == 7 and star_B1 == 8 and star_D1 == -1 and star_B1 > flat_ball(1))
step("LW.2", "an explicit degree-7 star realizes the FIRST negative-curvature site: |B_1| = 8 > flat 7, D_1 = -1",
     "the degree-7 star (centre + a 7-cycle, triangular faces) has |B_1| = 8, so D_1 = flat_ball(1) - 8 "
     "= 7 - 8 = -1 < 0, and rho = |B_1| = 8 EXCEEDS the right wing's rho_max = flat = 7 -- the max-density "
     "direction, REALIZED",
     ["LW.1", "13.A.2"],
     "build it cold, the mirror of container 13's degree-5 vertex. A degree-7 vertex with triangular "
     "faces is a centre c adjacent to a 7-cycle n0..n6 (the triangles c-ni-n(i+1)). Its ball |B_1| = "
     "1 + 7 = 8 (the relabelling identity |B_1| = deg+1, 13.A.3). Against the flat reference flat_ball(1) "
     "= 7 (14.B.1), the deficit is D_1 = 7 - 8 = -1 < 0 -- NEGATIVE curvature. And the archic density rho "
     "= |B_1| = 8 EXCEEDS the right wing's maximum rho_max = flat = 7 (15.C.1): this site is DENSER than "
     "anything on the sphere. So the max-density extremum -- which 15.C.2 said 'is simply not realized on "
     "this substrate ... a different geometry (one carrying degree > 6 sites), real and buildable, and "
     "neither built nor characterized' -- is here, built and characterized. The twelve are the min "
     "(D=+1); the degree-7 star is the first max (D=-1); D=0 is the mirror between them.",
     "UNIQUE (the degree-7 triangular star: 8 vertices, |B_1| = 8, D_1 = -1)", "DERIVED",
     {"centre_degree": star_deg0, "B1": star_B1, "flat_ball_1": flat_ball(1), "D_1": star_D1,
      "rho_exceeds_right_wing_max": star_B1 > flat_ball(1),
      "realizes": "the max-density direction 15.C.2 deferred as 'a different, buildable geometry'"},
     check="the degree-7 star: centre degree 7, |B_1| = 8 > flat 7, D_1 = -1 < 0")
assert lw2_ok

# ---- LW.3 the {3,7} hyperbolic growth, VALIDATED cold against flat {3,6} -- DERIVED ------
def coord_seq(d, N):
    # {3,d} coordination sequence: a(0)=1, a(1)=d, a(2)=d(d-4), a(n+1)=(d-4)a(n)-a(n-1) for n>=2.
    a = [1, d]
    if N >= 2:
        a.append(d * (d - 4))
    for n in range(2, N):
        a.append((d - 4) * a[n] - a[n - 1])
    return a[:N + 1]


def balls_from_rings(rings):
    return [sum(rings[:k + 1]) for k in range(len(rings))]


N = 5
# THE GUARD: the recurrence must reproduce the flat {3,6} = 6r rings and flat_ball exactly.
flat_rings_recur = coord_seq(6, N)
flat_balls_recur = balls_from_rings(flat_rings_recur)
flat_rings_expected = [1] + [flat_ring(r) for r in range(1, N + 1)]
flat_balls_expected = [flat_ball(r) for r in range(N + 1)]
flat_reproduced = (flat_rings_recur == flat_rings_expected and flat_balls_recur == flat_balls_expected)

# THE LEFT WING: apply the validated recurrence at d=7.
hyp_rings = coord_seq(7, N)
hyp_balls = balls_from_rings(hyp_rings)
hyp_deficit = [flat_ball(r) - hyp_balls[r] for r in range(N + 1)]
all_negative_after_center = all(hyp_deficit[r] < 0 for r in range(1, N + 1))
growing = all(hyp_deficit[r + 1] < hyp_deficit[r] for r in range(1, N))   # more negative each step
lw3_ok = flat_reproduced and all_negative_after_center and growing
step("LW.3", "the {3,7} hyperbolic tiling grows FASTER than flat (validated cold on flat {3,6}): D_r < 0 and growing",
     "the {3,d} coordination recurrence a(n+1) = (d-4)a(n) - a(n-1) reproduces flat {3,6} = 6r EXACTLY "
     "(the internal guard); at d=7 it gives rings [7,21,56,147,385], |B_r| = [1,8,29,85,232,617], and "
     "D_r = flat - |B_r| = [0,-1,-10,-48,-171,-526] -- NEGATIVE and GROWING (exponential): the max-density "
     "deficit is UNBOUNDED, the mirror of the twelve's bounded tri(r)",
     ["LW.2", "14.B.1"],
     "past r=1 the negative curvature COMPOUNDS. The regular triangular tiling {3,d} has a coordination "
     "sequence fixed by the transfer recurrence a(n+1) = (d-4)a(n) - a(n-1), a(1)=d, a(2)=d(d-4). This is "
     "computed COLD and CHECKED against the one case we already own: at d=6 (flat) it must give the "
     "degree-6 rings 6r and flat_ball = 1+3r(r+1) -- and it does, exactly (flat_reproduced = the guard). "
     "Trusting it thus validated, at d=7 the rings are [7,21,56,147,385] and |B_r| = [1,8,29,85,232,617]. "
     "The deficit D_r = flat_ball(r) - |B_r| = [0,-1,-10,-48,-171,-526] is negative from r=1 and grows "
     "(more negative every step) -- hyperbolic EXPONENTIAL growth, versus flat's quadratic. So the "
     "max-density side is not just denser at a point (LW.2) but has UNBOUNDED density growth -- the exact "
     "sign-and-magnitude mirror of the twelve, whose positive deficit is the bounded triangular tri(r) "
     "= [1,3,6,10] (14.B.3). The vacuum end is a shallow minimum; the black-hole end is a runaway maximum.",
     "UNIQUE (the {3,7} coordination sequence; validated by reproducing flat {3,6})", "DERIVED",
     {"recurrence": "a(n+1) = (d-4)a(n) - a(n-1), a(1)=d, a(2)=d(d-4)",
      "flat_reproduced_guard": flat_reproduced,
      "hyp_rings_3_7": hyp_rings, "hyp_balls_3_7": hyp_balls, "flat_balls": flat_balls_expected,
      "hyp_deficit_D_r": hyp_deficit, "all_negative": all_negative_after_center, "growing": growing,
      "contrast": "flat is quadratic |B_r|~3r^2; the twelve's positive deficit tri(r) is bounded; the "
                  "left wing is exponential and unbounded"},
     check="the recurrence reproduces flat {3,6}; at d=7, D_r = [0,-1,-10,-48,-171,-526] < 0 and growing")
assert lw3_ok

# ---- LW.4 topology: the two wings live on different surfaces (Gauss-Bonnet) -- DERIVED ---
right_wing_total = 12 * angle_deficit(5)     # twelve degree-5 sites: 12 * (+2) = +24 = 12*chi => chi = 2
right_chi = right_wing_total // 12
one_deg7 = angle_deficit(7)                  # a single degree-7 site: -2 (net-negative contribution)
lw4_ok = (right_wing_total == 24 and right_chi == 2 and one_deg7 == -2 and one_deg7 < 0)
step("LW.4", "topology: the wings live on DIFFERENT surfaces -- Gauss-Bonnet sum(12-2d) = 12*chi; left needs chi<0",
     "Gauss-Bonnet: sum over vertices of (12-2d) = 12*chi. Right wing (twelve deg-5): 12*(+2) = +24 = "
     "12*chi => chi = 2, genus 0 (the sphere, 14/15). An all-degree>6 surface has sum < 0 => chi < 0 => "
     "genus >= 2 (closed) OR the OPEN hyperbolic plane. So the left wing is NOT a genus-0 sphere",
     ["LW.1", "14.B.4", "15.C.2"],
     "this is WHY the right wing is forced one-sided, and it is honest about what the left wing costs. The "
     "total angle deficit is a topological invariant: sum_v (12 - 2*deg_v) = 12*chi (Gauss-Bonnet, "
     "14.B.4). The icosahedral sphere has the twelve degree-5 sites contributing 12*(+2) = +24 = 12*chi, "
     "so chi = 2 (genus 0). A surface that is negatively curved EVERYWHERE (all deg > 6, every (12-2d) < "
     "0) must have sum < 0, hence chi < 0 -- a closed genus >= 2 surface, or the non-compact (open) "
     "hyperbolic plane. It CANNOT be a genus-0 sphere. This is exactly why container 15.C.2 found the "
     "sphere one-sided (D >= 0): on a closed genus-0 surface Gauss-Bonnet PINS the net curvature at "
     "+12*chi = +24 > 0, so it cannot be net-negative -- the left wing simply does not fit on the same "
     "surface. The two signs are not two regions of one sphere; they are two topologies. (This is the "
     "curvature-total statement only -- NOT a claim about which surface the substrate 'is'.)",
     "UNIQUE (Gauss-Bonnet: sum(12-2d) = 12*chi; right chi=2, all-deg>6 chi<0)", "DERIVED",
     {"right_wing_deficit_total": right_wing_total, "right_wing_chi": right_chi, "right_wing_genus": 0,
      "single_deg7_contribution": one_deg7,
      "left_wing_topology": "chi < 0 => genus >= 2 (closed) or the OPEN hyperbolic plane -- NOT genus-0",
      "why_right_wing_one_sided": "chi=2>0 pins net curvature +24>0 (15.C.2); net-negative cannot fit on the sphere"},
     check="right wing sum(12-2d) = +24 = 12*chi => chi=2; a degree-7 site is -2 < 0 => all-deg>6 has chi<0")
assert lw4_ok

# ---- LW.5 the reading: max density <-> the black-hole direction -- POSTULATE (quarantined)
step("LW.5", "the reading (mirror of 15.C.3): MAX archic density <-> the BLACK-HOLE direction (Schwarzschild) -- a named possibility",
     "the max-density direction (D < 0, degree > 6) <-> the BLACK-HOLE end (where Schwarzschild "
     "attaches), the sign-mirror of 15.C.3's min-density <-> vacuum. NAMED as a possibility, NOT "
     "confirmed -- held, quarantined, the same discipline 15 applied to the vacuum side",
     ["LW.3", "LW.4", "15.C.3"],
     "the arc's working correspondence for the max side, named to be tested, not asserted -- exactly the "
     "grade 15.C.3 carries for the min side (Kevin's steer: name the direction, hold confirmation until "
     "warranted). From the maths-4 clues (reference only): the minimum archic density is the vacuum / "
     "dark-energy direction (15.C.3, realized on the sphere); the MAXIMUM archic density is the "
     "BLACK-HOLE direction, where the Schwarzschild radius attaches (the max-density end many sessions "
     "ago). This container REALIZES that max direction (LW.2/LW.3) -- a genuine denser-than-flat, "
     "runaway-growth region -- and reads it, as a POSSIBILITY, as the black-hole side. It also touches "
     "the METRIC-NO-THIRTEENTH (03.3.7 / 09.6.6 / 25.DF.3 / 01.1.6): degree > 6 is precisely the "
     "'room for a 13th neighbour', so the question of whether the SUBSTRATE ever goes left of the mirror "
     "IS the metric-no-thirteenth from the other side. WHAT DOES NOT TRAVEL: any value (the Schwarzschild "
     "radius / max density -- OWED); the closed realization; whether the substrate realizes it at all. A "
     "CORRESPONDENCE / reading; held, quarantined; no downstream premise use.",
     "POSTULATE (max density <-> black-hole direction; a named possibility, not confirmed; held)", "POSTULATE",
     {"reading": "max archic density (D<0, degree>6) <-> the black-hole direction (Schwarzschild attaches)",
      "mirror_of": "15.C.3 (min density <-> vacuum), same POSTULATE discipline",
      "touches_metric_no_thirteenth": "degree>6 = the 13th-neighbour room; 'does the substrate go left of the mirror?' = 03.3.7/09.6.6/25.DF.3/01.1.6 from the other side",
      "what_does_not_travel": "the value (OWED); the closed realization; whether the substrate realizes degree>6",
      "downstream_premise_use": False, "correspondence_not_confirmed": True},
     check=None)

# ---- LW.6 OWED: the closed realization, the value, whether the substrate goes left -----
step("LW.6", "OWED: the closed higher-genus realization; the max-density / Schwarzschild VALUE; does the substrate go LEFT of the mirror?",
     "OWED: (a) a CLOSED negative-curvature realization (genus >= 2, LW.4) rather than a patch; (b) the "
     "VALUE at the max-density end (the Schwarzschild radius / max density) -- computed-then-compared, "
     "NEVER fitted; (c) whether the SUBSTRATE ever realizes degree > 6 -- the metric-no-thirteenth from "
     "the other side. The direction is built; its closure, value, and substrate-realization are owed",
     ["LW.5"],
     "the honest residual. LW.1-LW.4 build the max-density DIRECTION as a geometry (local site LW.2, "
     "growth LW.3, topology LW.4); what stays owed: (a) a CLOSED left-wing surface -- LW.4 says it needs "
     "genus >= 2; only a patch / the open plane is exhibited here, a closed hyperbolic surface is not "
     "built; (b) the VALUE -- the Schwarzschild radius fell out of the max-density end in maths 4 (clue), "
     "but here no number is emitted; it is gated the same way as rho_Lambda (34): computed-then-compared, "
     "never fitted, danger zone (mass) out; (c) the deep one -- WHETHER THE SUBSTRATE GOES LEFT OF THE "
     "MIRROR at all. The registration substrate built so far (00-13) is the icosahedral sphere, one-sided "
     "D >= 0. Whether recursion ever produces a degree>6 site is the metric-no-thirteenth question "
     "(03.3.7 / 09.6.6 / 25.DF.3 / 01.1.6 -- the four collapsed to one) seen from the negative side: a "
     "13th neighbour IS a degree-7 (left-wing) site. So the left wing's REALIZATION and the "
     "metric-no-thirteenth are the SAME open problem. NOT attempted further here.",
     "OWED (closed realization; the value; whether the substrate realizes degree>6 = the metric-no-thirteenth)", "OWED",
     {"owed_closed": "a closed genus>=2 negative-curvature surface (LW.4); only a patch/open plane is built here",
      "owed_value": "the max-density / Schwarzschild value -- computed-then-compared NEVER fitted, danger zone out",
      "owed_substrate": "whether the substrate ever realizes degree>6 -- the metric-no-thirteenth (03.3.7/09.6.6/25.DF.3/01.1.6) from the other side; a 13th neighbour IS a degree-7 site",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="36-negative-curvature",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        deg_table=DEG_TABLE, mirror_at_degree=6,
        star_centre_degree=star_deg0, star_B1=star_B1, star_D1=star_D1, flat_ball_1=flat_ball(1),
        flat_reproduced_guard=flat_reproduced,
        hyp_rings_3_7=hyp_rings, hyp_balls_3_7=hyp_balls, hyp_deficit_D_r=hyp_deficit,
        right_wing_chi=right_chi, single_deg7_deficit=one_deg7,
        finding="the LEFT WING of the mirror -- the negative-curvature / max-density direction 15.C.2 "
                "deferred -- is BUILT. Signed curvature D_1 = 6-d extends across the mirror: d>6 is "
                "NEGATIVE (LW.1); an explicit degree-7 star realizes rho = |B_1| = 8 > flat 7, D_1 = -1 "
                "(LW.2); the {3,7} tiling grows faster than flat (validated cold on flat {3,6}), D_r = "
                "[0,-1,-10,-48,-171,-526] < 0 and exponential -- an UNBOUNDED max, the mirror of the "
                "twelve's bounded min (LW.3); Gauss-Bonnet forces the left wing onto a chi<0 surface "
                "(genus>=2 or the open plane), NOT the genus-0 sphere -- which is WHY the right wing is "
                "one-sided (LW.4). The max-density <-> BLACK-HOLE reading is POSTULATE (mirror of 15.C.3); "
                "the closed realization, the value, and whether the substrate goes left of the mirror are "
                "OWED -- and that last is the metric-no-thirteenth (01.1.6/03.3.7/09.6.6/25.DF.3) from the "
                "other side. Danger-free, nothing fitted.",
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
