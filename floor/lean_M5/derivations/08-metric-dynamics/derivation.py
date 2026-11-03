#!/usr/bin/env python3
"""Container 08 -- metric dynamics. Rests on 05 (the bridge) and 07 (the ordinal walk).

THE LADDER CLOSES. Kevin's ladder was: ORDINAL-dynamics (07) -> the geometric-balance BRIDGE (05)
-> METRIC dynamics (here). Container 07 built the directed walk with ORDINAL structure only --
succession, direction, rate as a pure ratio (the rationals), cyclic return -- positions were bare
integer counts, no distance. The bridge (05) gives those positions a EUCLIDEAN METRIC. Metric
dynamics is 07's walk seen across the bridge: now the walk has DISTANCE, and dim >= 2 (05's rung 5)
lets it TURN, so the metric can finally distinguish

    SPEED (rate of motion -- path length per tick)  from  VELOCITY (rate of net displacement).

A walk can move at full speed yet get nowhere (reverse), or turn so displacement < path. That gap
is exactly what the metric adds over the ordinal count, and it is the triangle inequality.

THE REALS enter here (8.2): a turned walk's net displacement has length sqrt(2) -- irrational. The
number ladder is now complete: integers (04, directions) -> rationals (07, rates) -> REALS (here,
distances via the metric). This is why the reals waited for the bridge.

DISCRETE ACCELERATION (8.7) is the buildable increment on top of the ladder: the SECOND DIFFERENCE
of position, Delta^2 x_t = s_{t+1} - s_t (the change of step). Uniform motion <=> zero acceleration
(the discrete Newton's-first-law); a turn/reversal localizes nonzero acceleration; the reversal is a
maximal flip (|a|^2 = 4); the accelerations telescope to the net velocity change. All exact on the
integer lattice -- NO continuum: the continuous/curvature layer stays EMERGENT (8.6), not a rung.

Mathlib-FREE: distances are handled as exact integer squared-lengths (dot products); where a length
is irrational (sqrt of a non-square) that is named, not mechanised. Positions live on the integer
lattice the bridge's unit separation gives. Grades: DERIVED / POSTULATE / OWED, per step.
"""

import json
import sys
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- exact 2D metric
def vadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def normsq(u):
    return dot(u, u)


def net(walk):
    n = (0, 0)
    for s in walk:
        n = vadd(n, s)
    return n


def is_square(m):
    return m >= 0 and isqrt(m) ** 2 == m


E1, E2 = (1, 0), (0, 1)
NE1, NE2 = (-1, 0), (0, -1)

# sample walks -- now 2-D, because the bridge gives dim >= 2 (05) and the walk can TURN.
WALKS = {
    "straight": [E1, E1, E1],          # net (3,0): |net|^2 = 9, path 3 -> straight (equality)
    "turned":   [E1, E2],              # net (1,1): |net|^2 = 2, path 2 -> turn (sqrt2!)
    "reversed": [E1, NE1],             # net (0,0): moves, nets nothing (speed>0, velocity 0)
    "elbow":    [E1, E1, E2, E2],      # net (2,2): |net|^2 = 8, path 4 -> 2*sqrt2
}

# ---- 8.1 across the bridge: positions are Euclidean points -- DERIVED --------
unit_steps = all(normsq(s) == 1 for w in WALKS.values() for s in w)
can_turn = normsq(net(WALKS["turned"])) != (sum(1 for _ in WALKS["turned"])) ** 2  # a genuine turn exists
step("8.1", "across the bridge, the walk is a trajectory in Euclidean space",
     "positions in the integer lattice (bridge's unit separation); steps are unit vectors; dim >= 2",
     ["05.4", "07.1"],
     "the geometric-balance bridge (05) maps the walk's positions to points in Euclidean space, at "
     "the unit separation. The ordinal walk (07) was 1-D on the integer line; here dim >= 2 (05's "
     "rung 5: 3 equidistant points force a plane) lets the trajectory TURN -- a perpendicular step "
     "exists. Steps are unit vectors; a walk is a lattice trajectory. The substrate is still "
     "relational; this is its Euclidean image.",
     "UNIQUE given the bridge (the image is fixed by the correspondence)", "DERIVED",
     {"steps_are_unit": unit_steps, "turning_possible": can_turn,
      "space": "integer lattice, dim >= 2 (from 05)"},
     check="steps are unit vectors; a genuine 2-D turn exists (dim >= 2 from the bridge)")
assert unit_steps and can_turn

# ---- 8.2 the metric: Euclidean distance, and THE REALS -- DERIVED ------------
dist_data = {}
reals_enter = False
for name, w in WALKS.items():
    ns = normsq(net(w))
    sq = is_square(ns)
    dist_data[name] = {"net": list(net(w)), "disp_sq": ns,
                       "disp": (str(isqrt(ns)) if sq else f"sqrt({ns})"), "rational": sq}
    if not sq:
        reals_enter = True
step("8.2", "the metric -- Euclidean distance, and the REALS enter",
     "|net|^2 = <net,net> (exact) ; |net| = sqrt(|net|^2) -- irrational when |net|^2 is non-square",
     ["8.1"],
     "the bridge's inner product gives distance: the net displacement's length is sqrt(<net,net>). "
     "For an axis walk that is rational, but a TURNED walk nets (1,1), length sqrt(2) -- IRRATIONAL. "
     "So distance is a REAL, not a rational. This completes the number ladder: integers (04, "
     "directions) -> rationals (07, rates) -> REALS (distances, here). The reals waited for the "
     "metric, which waited for the bridge. Squared lengths stay exact integers; the irrational "
     "length is named, not mechanised.",
     "UNIQUE (the distance is fixed by the metric)", "DERIVED",
     {"distances": dist_data, "reals_enter_via": "sqrt of a non-square displacement (e.g. sqrt2)"},
     check="|net|^2 exact; a turned walk gives a non-square (sqrt2) -> the reals")
assert reals_enter

# ---- 8.3 speed vs velocity -- DERIVED ---------------------------------------
def speed_num(w):        # path length (unit steps: one length-1 step per tick) = #ticks
    return len(w)


def velocity_magsq(w):   # |net|^2 / T^2  (a rational, squared)
    T = len(w)
    return (normsq(net(w)), T * T)


sv = {}
for name, w in WALKS.items():
    T = len(w)
    vmsq = velocity_magsq(w)
    g = gcd(vmsq[0], vmsq[1])
    sv[name] = {"time": T, "path": speed_num(w), "speed": "1 (unit motion)",
                "velocity_magsq": f"{vmsq[0]}/{vmsq[1]}",
                "velocity_magsq_reduced": f"{vmsq[0] // g}/{vmsq[1] // g}"}
step("8.3", "speed vs velocity -- the metric splits the ordinal rate in two",
     "speed = path/time (= 1, unit motion) ; velocity = net/time (a VECTOR), |velocity| = |net|/T",
     ["8.2", "07.3"],
     "with a metric, 07's single 'rate' splits: SPEED is path length per tick (the rate of MOTION), "
     "VELOCITY is net displacement per tick (the rate of getting SOMEWHERE) -- and it is a VECTOR, "
     "with a direction the bridge's space supplies. 07's rational rate is revealed as the velocity "
     "MAGNITUDE; the metric adds speed and the vector nature. For unit motion speed = 1; velocity "
     "magnitude = |net|/T <= 1.",
     "UNIQUE (speed and velocity are fixed by the trajectory)", "DERIVED",
     {"speed_velocity": sv, "note": "07's rate = velocity magnitude; metric adds speed & direction"},
     check="speed = path/time; velocity = net/time (vector); computed per walk")

# ---- 8.4 velocity <= speed -- the triangle inequality -- DERIVED ------------
tri = {}
for name, w in WALKS.items():
    ns = normsq(net(w))
    T = len(w)
    straight = (ns == T * T)                      # |net| = path  <=> straight
    tri[name] = {"disp_sq": ns, "path_sq": T * T, "velocity_le_speed": ns <= T * T,
                 "straight_equality": straight}
triangle_holds = all(t["velocity_le_speed"] for t in tri.values())
step("8.4", "velocity <= speed -- the triangle inequality (displacement <= distance travelled)",
     "|net| <= path ; equality iff the walk is straight (no turn, no reversal)", ["8.3"],
     "the net displacement never exceeds the distance travelled: |net| <= path, i.e. |net|^2 <= T^2. "
     "Equality holds exactly when the walk is STRAIGHT -- every step the same direction, no turn and "
     "no reversal. The DEFICIT (speed above velocity) measures wandering: the reversed walk moves at "
     "full speed yet nets zero (velocity 0) -- motion without progress, which the ordinal count "
     "could not see and the metric makes precise. This is the metric structure's core.",
     "UNIQUE (the inequality is a fixed metric fact)", "DERIVED",
     {"triangle": tri, "equality_iff": "straight (no turn, no reversal)"},
     check="|net|^2 <= T^2 for every walk; equality iff straight")
assert triangle_holds

# ---- 8.5 metric motion is the bridge-image of ordinal dynamics -- POSTULATE --
step("8.5", "metric motion is the bridge-image of ordinal dynamics -- the ladder closes",
     "metric dynamics = ordinal dynamics (07) under the bridge (05); substrate stays relational",
     ["8.4", "05.5"],
     "speed and velocity are the Euclidean IMAGE of 07's succession and rate, carried across the "
     "bridge (05). The substrate remains the relational floor; the trajectory is its image, not the "
     "thing -- do not reify it ('all of math is a language ... to describe a thing', Kevin). With "
     "this the ladder Kevin drew is complete: ordinal (07) -> bridge (05) -> metric (here). Held as "
     "the reading, capped.",
     "the reading (metric = bridge-image of ordinal), held", "POSTULATE",
     {"ladder": "ordinal (07) -> bridge (05) -> metric (08)", "substrate": "the relational floor"},
     check=None)

# ---- 8.6 the continuum as an EMERGENT limit, NOT a floor rung -- OWED --------
step("8.6", "the continuum as an EMERGENT limit, NOT a floor rung -- OWED (discrete accel is 8.7)",
     "the CONTINUOUS layer (smooth trajectory, actual derivatives, curvature) EMERGES as a large-N "
     "limit of the quantized walk -- it is not a floor primitive to axiomatize in", ["8.4"],
     "the DISCRETE half of acceleration is now BUILT at 8.7 (the second difference Delta^2, "
     "Mathlib-free). What remains here is a substrate COMMITMENT, not a missing computation. The "
     "CONTINUOUS layer -- a smooth trajectory, actual derivatives, curvature -- would need the reals "
     "as a COMPLETE ordered field with calculus. But the substrate is QUANTIZED ('quantized & "
     "orchestrated information', Kevin): everything built is discrete (registrations, ticks, the "
     "integer lattice; the reals entered at 8.2 only as algebraic distances like sqrt2, NOT as a "
     "continuum). So continuity here is EMERGENT -- a large-N limit of the discrete metric dynamics, "
     "to fall out later IF something needs it -- and is NOT a rung to build. Axiomatizing a continuum "
     "at the floor would smuggle continuity into a discrete substrate, the same category error as "
     "coordinates-before-motion. This is a substrate commitment (owner's): the evidence points to "
     "emergent, not fundamental.",
     "OWED -- deliberately: the continuum is EMERGENT (a large-N limit), not a floor rung", "OWED",
     {"discrete_acceleration": "BUILT at 8.7 (the second difference Delta^2, Mathlib-free)",
      "continuous_layer": "EMERGENT: a large-N limit of the quantized dynamics, not a floor primitive",
      "why_not_a_rung": "the substrate is quantized/discrete; an axiomatized continuum would smuggle "
                        "continuity in (a coordinates-before-motion category error)",
      "built_here": False},
     check=None)

# ---- 8.7 discrete acceleration: the second difference Delta^2 -- DERIVED ------
# acceleration_t = Delta^2 x_t = Delta v_t = v_{t+1} - v_t = s_{t+1} - s_t  (t = 0 .. T-2)
def accel_of(w):
    return [(w[t + 1][0] - w[t][0], w[t + 1][1] - w[t][1]) for t in range(len(w) - 1)]


accel_data = {}
for name, w in WALKS.items():
    a = accel_of(w)
    tot = (sum(s[0] for s in a), sum(s[1] for s in a))
    accel_data[name] = {"accel": [list(s) for s in a],
                        "accel_magsq": [normsq(s) for s in a],
                        "all_zero": all(s == (0, 0) for s in a),
                        "telescopes_to_net_velocity_change": tot == (w[-1][0] - w[0][0], w[-1][1] - w[0][1]),
                        "sum_accel": list(tot)}
straight_zero_accel = accel_data["straight"]["all_zero"]
turn_nonzero_accel = not accel_data["turned"]["all_zero"]
reversal_is_maximal = accel_data["reversed"]["accel_magsq"] == [4]      # a full flip, |a|^2 = 4
elbow_localizes = accel_data["elbow"]["accel_magsq"] == [0, 2, 0]        # nonzero only at the corner
telescopes = all(d["telescopes_to_net_velocity_change"] for d in accel_data.values())
step("8.7", "discrete acceleration -- the second difference Delta^2 (uniform motion <=> zero accel)",
     "a_t = Delta^2 x_t = v_{t+1} - v_t = s_{t+1} - s_t ; straight <=> a = 0 everywhere ; "
     "sum a_t = v_last - v_first (telescopes)",
     ["8.3", "8.4"],
     "the BUILDABLE half of acceleration, in the same discrete Mathlib-free style -- NO continuum. "
     "Discrete acceleration is the SECOND DIFFERENCE of position, equivalently the first difference "
     "of velocity: a_t = v_{t+1} - v_t = s_{t+1} - s_t, the change of step vector, a vector on the "
     "integer lattice. Its facts: (1) a STRAIGHT walk (constant step) has ZERO acceleration "
     "everywhere -- uniform motion, the discrete Newton's-first-law, and exactly 8.4's "
     "'equality iff straight' seen locally; (2) acceleration is nonzero exactly at a TURN or "
     "REVERSAL and LOCALIZES the bend -- the elbow's accel is (0,0),(-1,1),(0,0): zero on the "
     "straight segments, nonzero only at the corner; (3) a REVERSAL is the maximal single "
     "acceleration, |a|^2 = 4 (a full 180-degree flip of the unit step); (4) the accelerations "
     "TELESCOPE: their sum is v_last - v_first, the net change of velocity over the walk. All exact "
     "integer-lattice differences -- the discrete increment, with the continuum left emergent (8.6).",
     "UNIQUE (the second difference is fixed by the trajectory)", "DERIVED",
     {"acceleration": accel_data, "straight_zero_accel": straight_zero_accel,
      "turn_nonzero_accel": turn_nonzero_accel, "reversal_magsq_is_4": reversal_is_maximal,
      "elbow_localizes_at_corner": elbow_localizes, "telescopes": telescopes,
      "definition": "a_t = Delta^2 x_t = s_{t+1} - s_t (second difference of position)"},
     check="Delta^2: straight=0 accel; turn/reversal nonzero; reversal |a|^2=4; sum telescopes")
assert straight_zero_accel and turn_nonzero_accel and reversal_is_maximal and elbow_localizes and telescopes

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="08-metric-dynamics", steps=STEPS, grades=GRADES,
           values=dict(walks={k: [list(s) for s in v] for k, v in WALKS.items()},
                       distances=dist_data, triangle=tri, reals_enter=reals_enter,
                       triangle_holds=triangle_holds, acceleration=accel_data,
                       accel_telescopes=telescopes))

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
