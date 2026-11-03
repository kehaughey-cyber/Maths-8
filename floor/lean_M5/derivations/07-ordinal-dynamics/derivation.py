#!/usr/bin/env python3
"""Container 07 -- ordinal (relational) dynamics. Rests on 02 (change) and 04 (order/direction).

DEPENDENCY POSITION is rung 4.5: the maturation of CHANGE (container 02, the registration event --
"the elemental dynamics seat", Kevin) along DIRECTION and ORDER (container 04). The directory
number (07) is a build-order label only; the floor-up truth is the imports (rests on 02 and 04),
not the number. Placed after the geometry/carrier stubs (05, 06) purely because this joint was
identified later.

Kevin's ladder: ORDINAL-dynamics (here) -> the geometric-balance bridge -> METRIC dynamics. The
split is load-bearing:
  - ORDINAL / relational dynamics -- succession, the directed step, rate as a step-RATIO, cyclic
    return, observer-relativity. Uses ONLY floor objects (registration, adjacency, change,
    direction); NO coordinates, NO distance. Built here.
  - METRIC dynamics -- velocity as distance/time, acceleration, trajectories in space. Needs the
    bridge (positions in Euclidean space with a metric). OWED, not built.

The elemental object is a DIRECTED WALK on the relational line: change (02) taking a signed step
(04's +1/-1) per tick, the ticks ordered by the integer order (04). Positions are INTEGERS
(relational counts -- WHICH registration), never spatial coordinates. "All of math is a language
... to describe a thing" (Kevin): the walk is language for ordered, directed change; the thing is
quantized & orchestrated information, its relativity, and the observers -- do not reify it.

THE HEADLINE (7.3): rate = net displacement per tick = a RATIO of an integer and a positive count
= the RATIONALS, the pre-geometric number-object between integers (04) and the reals (which arrive
only at the bridge). Its equality is cross-MULTIPLY, exactly mirroring integers' cross-ADD (04.2).

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


# ---------------------------------------------------------------- the objects
# A walk is a sequence of signed steps, each +1 or -1 (container 04's two directions). Positions
# are integer partial sums -- relational, not spatial. Everything below uses only integer counts.
PLUS, MINUS = +1, -1
DIRECTIONS = [PLUS, MINUS]


def net(walk):
    return sum(walk)                       # net displacement; in Lean, foldl addPair (04)


def positions(walk):
    p, out = 0, [0]
    for s in walk:
        p += s
        out.append(p)
    return out


WALK = [PLUS, PLUS, MINUS, PLUS, MINUS, PLUS]   # sample: net +2 over 6 ticks
HALF = [PLUS, PLUS, MINUS]                       # net +1 over 3 ticks -- same RATE 1/3
CYCLE = [PLUS, PLUS, MINUS, MINUS]               # net 0 -- returns; period 4

# ---- 7.1 succession -- change ordered into a history -- DERIVED --------------
HLEN = len(WALK)
ticks = list(range(HLEN + 1))
before = lambda i, j: i <= j                      # the tick order = 04's total order on indices
order_total = all(before(i, j) or before(j, i) for i in ticks for j in ticks)
order_transitive = all((not (before(i, j) and before(j, k))) or before(i, k)
                       for i in ticks for j in ticks for k in ticks)
step("7.1", "succession -- change (02) ordered into a history by the integer order (04)",
     "a history: change-events indexed by ticks, ordered by t <= u (04's total order)", [],
     "container 02 says change ENTERS (the registration event, potential -> stable). Dynamics "
     "begins when changes SUCCEED one another -- ordered by the integer line (04). The tick order "
     "IS 04's total order restricted to indices: total and transitive, so every pair of moments is "
     "comparable (before/after). This is the first before/after, and it needs no space -- only the "
     "order already built.",
     "the order is UNIQUE (04's total order); each event's content is CHOSEN", "DERIVED",
     {"history_length": HLEN, "order_total": order_total, "order_transitive": order_transitive,
      "seat": "container 02's change event", "index_by": "container 04's integer order"},
     check="the tick order is total & transitive (04's order on indices)")
assert order_total and order_transitive

# ---- 7.2 the directed step -- each change carries a direction -- DERIVED -----
step_set_ok = set(WALK) <= set(DIRECTIONS) and set(HALF) <= set(DIRECTIONS)
dirs_distinct = DIRECTIONS[0] != DIRECTIONS[1]
step("7.2", "the directed step -- each change carries a direction (04's +1 / -1)",
     "each tick's change is a signed step in {+1, -1}; a walk is a sequence of them", ["7.1"],
     "a change is not merely THAT something changed (02) but WHICH WAY (04): each step is one of "
     "the two directions off the counterpoint, +1 or -1 -- distinct (04.4). Change (02) composed "
     "with direction (04) is the DIRECTED step. Still ordinal: the step is +1/-1 on the relational "
     "line, not a displacement in space.",
     "UNIQUE (the two directions are 04's units)", "DERIVED",
     {"directions": DIRECTIONS, "distinct": dirs_distinct, "walk": WALK, "steps_valid": step_set_ok},
     check="steps drawn from 04's two distinct directions {+1,-1}")
assert step_set_ok and dirs_distinct

# ---- 7.3 net and RATE -- the rationals enter -- DERIVED (headline) -----------
def rate(walk):
    return (net(walk), len(walk))                 # (net displacement, tick count)


def rate_equiv(r1, r2):
    return r1[0] * r2[1] == r2[0] * r1[1]          # cross-MULTIPLY (cf 04.2's cross-ADD)


N, T = net(WALK), len(WALK)
rate_walk, rate_half = rate(WALK), rate(HALF)
same_rate = rate_equiv(rate_walk, rate_half)
# a walk and its k-fold repeat have the same rate -- rate is a genuine ratio, not a raw pair.
scale_ok = all(rate_equiv(rate(WALK * k), rate_walk) for k in [1, 2, 3])
step("7.3", "net and RATE -- the rationals enter (net displacement per tick)",
     "net = sum of steps (04's addPair) ; rate = (net, ticks) ; equal iff net1*T2 = net2*T1",
     ["7.2"],
     "the net displacement of a walk is the sum of its signed steps -- an integer (04). The RATE "
     "is that net PER tick: a ratio of an integer and a positive count. That ratio is the "
     "RATIONALS -- the number-object between the integers (04) and the reals (which arrive only at "
     "the bridge, with the metric). Its equality is cross-MULTIPLY, exactly mirroring how integers "
     "are pairs under cross-ADD (04.2): a walk and its double-speed repeat share one rate. "
     "Dynamics-as-rate FORCES a new number, and it is still pre-geometric (a ratio of counts).",
     "the rate is UNIQUE (as a rational); its (net,ticks) representative is CHOSEN", "DERIVED",
     {"net": N, "ticks": T, "rate_walk": list(rate_walk), "rate_half": list(rate_half),
      "same_rate_by_cross_multiply": same_rate, "scale_invariant": scale_ok},
     check="rate is a ratio: walk & double-speed repeat equal by cross-multiply")
assert same_rate and scale_ok

# ---- 7.4 cyclic return -- the first periodic dynamics -- DERIVED -------------
def returns(walk):
    return net(walk) == 0


return_iff_balanced = all(returns(w) == (w.count(PLUS) == w.count(MINUS))
                          for w in [WALK, HALF, CYCLE, [PLUS, MINUS], [PLUS, PLUS]])
cycle_returns = returns(CYCLE)
period = next((t for t in range(1, len(CYCLE) + 1) if net(CYCLE[:t]) == 0 and t > 0
               and positions(CYCLE)[t] == positions(CYCLE)[0]), None)
step("7.4", "cyclic return -- the first periodic dynamics (change that comes back)",
     "a walk returns iff net = 0 iff #(+1) = #(-1); it closes to the counterpoint", ["7.3"],
     "the simplest non-trivial dynamics that CLOSES: a balanced walk (equal +1 and -1 steps) "
     "returns to where it began -- net ~ 0, the counterpoint (04.3). This is the first PERIODIC "
     "dynamics, the seat of cycles and clocks. The SPECIFIC period (container 02's OWED, phase "
     "cycle -> 12, and the clue-doc four clocks) is NOT forced here -- only that return exists and "
     "means balance; the 12 is cited downstream, not smuggled.",
     "UNIQUE (return <-> balance); the period is a property of the walk", "DERIVED",
     {"cycle": CYCLE, "returns": cycle_returns, "period": period,
      "return_iff_balanced": return_iff_balanced,
      "specific_period_12": "OWED to 02 / the clocks (not forced here)"},
     check="return <-> net 0 <-> balanced (+1 count = -1 count)")
assert cycle_returns and return_iff_balanced

# ---- 7.5 observer-relativity of the walk -- POSTULATE ------------------------
# the walk records STEPS (differences), not absolute positions; the origin is not part of it.
pos = positions(WALK)
c = 3
shifted = [p + c for p in pos]
net_invariant = (shifted[-1] - shifted[0]) == (pos[-1] - pos[0])
steps_invariant = all((shifted[i + 1] - shifted[i]) == (pos[i + 1] - pos[i])
                      for i in range(len(pos) - 1))
origin_relative = shifted[0] != pos[0]
step("7.5", "observer-relativity -- origin is observer-relative; step & net are invariant",
     "shift all positions by c: the steps and the net displacement are unchanged; the origin is not",
     ["7.1", "7.3"],
     "the walk is defined by its STEPS (differences), so the absolute origin is not part of it -- a "
     "different observer (02's observer/observed co-emergence) sees the same walk from a shifted "
     "origin. What all observers agree on is the DIRECTION of each step and the NET displacement "
     "between two ticks; the absolute position they need not. This is the seed of RELATIVITY -- "
     "Galilean, but ordinal and pre-metric. Held as the reading, not proven.",
     "the reading (relativity of the origin), held", "POSTULATE",
     {"net_invariant": net_invariant, "steps_invariant": steps_invariant,
      "origin_is_observer_relative": origin_relative,
      "invariants": "direction of each step; net displacement between ticks"},
     check=None)

# ---- 7.6 metric dynamics -- DISCHARGED by container 08 (retreated 2026-09-03) --------------
step("7.6", "metric dynamics -- velocity, acceleration, trajectories -- DISCHARGED by container 08 (only the CONTINUOUS trajectory is 08.8.6, deliberately not-a-rung)",
     "velocity, acceleration, and the (discrete) trajectory are BUILT across the bridge in container 08; "
     "the CONTINUOUS trajectory is 08.8.6 -- an emergent large-N limit, deliberately not a rung", ["7.3"],
     "RETREATED 2026-09-03: this deferred metric dynamics to 'after the bridge', and the bridge (05) + "
     "metric dynamics (08) have since been BUILT. Container 08 discharges it: velocity as net "
     "displacement per tick (08.8.3), speed as path per tick (08.8.3), the trajectory in Euclidean space "
     "(08.8.1), the triangle inequality velocity<=speed (08.8.4), and DISCRETE ACCELERATION -- the second "
     "difference Delta^2 (08.8.7, DERIVED zero-axiom: straight => zero acceleration = Newton's first law, "
     "a turn localizes the bend, a reversal is the maximal accel). So 07's ordinal rate IS 08's velocity "
     "magnitude, across the bridge. What remains is ONLY the CONTINUOUS trajectory (actual derivatives, a "
     "smooth curve) -- container 08.8.6 -- and 08 holds it deliberately NOT a rung: the substrate is "
     "quantized, so continuity is an emergent large-N limit to fall out later IF needed, never a floor "
     "axiom (axiomatizing a continuum would smuggle continuity into a discrete substrate). The genuine "
     "unbuilt FORWARD edge is not this at all: it is DYNAMICS UNDER INFLUENCE -- the walk ACCELERATING in "
     "the density gradient (20, gravity = grad rho), i.e. geodesic / free-fall motion -- which couples "
     "08 (kinematics) to 20/21 (gravity) and is danger-free geometry (no mass). Deferred there, not here.",
     "OWED (only the CONTINUOUS trajectory, 08.8.6 -- deliberately not-a-rung; discrete metric dynamics DISCHARGED by 08)", "OWED",
     {"discharged_by": "container 08 -- velocity/speed (8.3), trajectory (8.1), triangle inequality (8.4), discrete acceleration Delta^2 (8.7)",
      "remaining": "only the CONTINUOUS trajectory (08.8.6) -- emergent large-N limit, deliberately not a rung (quantized substrate)",
      "forward_edge": "dynamics under influence -- the walk accelerating in the density gradient (20) = geodesic/free-fall motion, coupling 08<->20/21, danger-free; NOT built",
      "built_here": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="07-ordinal-dynamics", steps=STEPS, grades=GRADES,
           values=dict(walk=WALK, half=HALF, cycle=CYCLE, net=N, ticks=T,
                       rate_walk=list(rate_walk), directions=DIRECTIONS,
                       cycle_returns=cycle_returns, cycle_period=period))

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
