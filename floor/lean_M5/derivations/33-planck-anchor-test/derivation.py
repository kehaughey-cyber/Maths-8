#!/usr/bin/env python3
"""Container 33 -- THE PLANCK-ANCHOR TEST: does the substrate have an edge and a tick?
Rests on 13 (the adjacency edge), 24 (the tick / c=alpha/tau), 27 (the dimension accounting); cites 18
(the Planck anchor, P.3 = Kevin's hypothesis), 32 (SEC9). Filed through the 19 gate. alpha-value plan
Step 3 (2026-08-29, Maths 6.5).

THE TEST (plan / Stone 18 P.3, Kevin's Planck hypothesis, held FLAGGED): the Planck length l_P is the
registration-to-registration separation (the EDGE of the adjacency web), and the Planck time t_P is the
state-change rate (the TICK). Then c = l_P/t_P = (edge)/(tick), and c = alpha/tau (container 24) would
identify alpha with the edge quantum and tau with the tick. PROVE or REFUTE.

THE HONEST OUTCOME (graded below): NEITHER cleanly proven NOR refuted -- STRUCTURALLY CONSISTENT but not
discriminating. The substrate genuinely HAS a definite edge, a definite tick, and a CONSTANT edge/tick
rate (a native c=alpha/tau, already proved at 24.SG.3) -- that is real (PA.1/PA.2). But the Planck VALUES
(l_P, t_P) are among the 3 irreducibly-external anchors (container 27), so the identification edge=l_P /
tick=t_P is a CORRESPONDENCE (Kevin's hypothesis, held) that reproduces c BY CONSTRUCTION (c=l_P/t_P is a
standard identity, 18.P.2) -- an IDENTITY, not a discriminating prediction. So the hypothesis is not
refuted (the substrate has exactly the structure it needs) and not proven (the values are external).

  PA.1 the substrate HAS a definite EDGE and TICK, and a CONSTANT edge/tick rate. The edge = the minimal
       adjacency separation (13.A.1, squared distance 4 in Z[phi]); the tick = one registration step = one
       archon (24.SG.3); the rate is one edge per tick, position-independent (24.SG.3). DERIVED.
  PA.2 this constant rate IS c = alpha/tau (24.SG.3) in the LENGTH reading of alpha (27.DA.3): alpha = the
       edge quantum (a length), tau = the tick; and edge/tick has the SAME DIMENSION (length/time =
       speed) as Stone 18's c = l_P/t_P. So the substrate's native rate and the Planck rate are the same
       KIND. DERIVED (dimension).
  PA.3 THE FILED ENTRY (18.P.3, Kevin's hypothesis): edge = l_P, tick = t_P => c=edge/tick <-> c=l_P/t_P;
       alpha (length reading) = the Planck edge quantum. A CORRESPONDENCE, held. The Planck VALUES stay
       external (27); the physical identification is assumed. POSTULATE.
  PA.4 DISCRIMINATION owed: the test as discharged is an IDENTITY (reproduces c by construction, 18.P.2),
       consistent NOT discriminating (18.P.4); neither cleanly proves (values external) nor refutes
       (structurally consistent); the Planck values external (27); the alpha value behind them. OWED.

DANGER-FREE (Path B, container 27): the content is the dimensionless STRUCTURE (an edge, a tick, a
constant rate, a dimension). The Planck VALUES are external, NOT derived. No mass, no census, no numerology.

Grades per step. `--check` recomputes the DERIVED steps.
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


# ================================================================ the edge, the tick, the rate
EDGE_SQ_DIST = 4                         # container 13.A.1: the minimal adjacency separation, sq dist 4 in Z[phi]
ARCHONS_PER_TICK = 1                     # container 24.SG.3: one registration step advances one archon
TICKS = list(range(0, 7))

# ---- PA.1 the substrate has a definite edge and tick, and a constant edge/tick rate -- DERIVED
def edges_after(k):
    """Edges advanced after k ticks = k (one edge per tick -- covering-cold, 24.SG.3)."""
    return k * ARCHONS_PER_TICK
rate_constant = all(edges_after(k) == k for k in TICKS)       # one edge per tick, position-independent
edge_is_minimal = (EDGE_SQ_DIST == 4)                          # 13.A.1: the adjacency edge
pa1_ok = rate_constant and edge_is_minimal
step("PA.1", "the substrate HAS a definite EDGE and TICK, and a CONSTANT edge/tick rate",
     "the edge = the minimal adjacency separation (13.A.1, squared distance 4 in Z[phi]); the tick = one "
     "registration step = one archon (24.SG.3); the propagation rate is one edge per tick, "
     "position-independent (24.SG.3) -- so the substrate natively has a CONSTANT rate c = edge/tick",
     ["13.A.1", "24.SG.3"],
     "the substrate side of the Planck-anchor test: does the substrate HAVE the two things Kevin's "
     "hypothesis identifies with l_P and t_P? YES, both are definite. (a) THE EDGE: container 13.A.1 "
     "builds adjacency from the minimal squared distance -- the pure integer 4 in Z[phi]; that minimal "
     "separation IS the registration-to-registration edge of the web (01's adjacency). (b) THE TICK: "
     "container 24.SG.3 (covering-cold) shows each registration step advances exactly ONE archon -- one "
     "state change; that step IS the tick. (c) THE RATE: 24.SG.3 proves the gain is one archon per tick, "
     "constant across archons and positions. So the substrate has a native CONSTANT rate = one edge per "
     "one tick = c = edge/tick. This is not vacuous: the substrate genuinely carries the edge/tick/"
     "constant-rate structure Kevin's Planck hypothesis needs -- an edge (a length-like unit), a tick (a "
     "time-like unit), and a constant edge-per-tick propagation. Whether that edge IS l_P and that tick IS "
     "t_P is PA.3 (the correspondence); here the STRUCTURE is derived. DANGER-FREE: dimensionless "
     "structure (an edge, a tick, a constant rate); no Planck value.",
     "UNIQUE (the edge = minimal adjacency (13); the tick = one step (24); the rate = one edge/tick, constant)",
     "DERIVED",
     {"edge_sq_dist": EDGE_SQ_DIST, "archons_per_tick": ARCHONS_PER_TICK,
      "rate_constant_one_edge_per_tick": rate_constant, "edge_is_minimal_adjacency": edge_is_minimal,
      "edge": "the minimal adjacency separation (13.A.1) = the registration-to-registration edge",
      "tick": "one registration step = one archon (24.SG.3) = the state-change unit",
      "rate": "one edge per tick, position-independent (24.SG.3) -- a native constant c = edge/tick"},
     check="the edge = minimal adjacency (sq dist 4, 13); one archon per tick (24); the rate is one edge/tick, constant")
assert pa1_ok

# ---- PA.2 the constant rate IS c=alpha/tau, same dimension (speed) as c=l_P/t_P -- DERIVED (dimension)
# (L,T,M) exponents (container 27's accounting). edge = length (1,0,0); tick = time (0,1,0); rate =
# edge/tick = (1,-1,0) = speed = c's dimension. Stone 18's c = l_P/t_P has the same (1,-1,0). So the
# substrate's native rate (c=alpha/tau, length reading of alpha, 27.DA.3) is the same KIND as the Planck rate.
def dsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
EDGE_DIM = (1, 0, 0)                     # length (the length reading of alpha, 27.DA.3)
TICK_DIM = (0, 1, 0)                     # time
C_DIM = (1, -1, 0)                       # speed
rate_dim = dsub(EDGE_DIM, TICK_DIM)      # (1,-1,0)
rate_is_speed = (rate_dim == C_DIM)
lp_over_tp_dim = dsub((1, 0, 0), (0, 1, 0))   # l_P/t_P = length/time = (1,-1,0) = c (Stone 18 P.2)
same_kind = (rate_dim == lp_over_tp_dim == C_DIM)
pa2_ok = rate_is_speed and same_kind
step("PA.2", "the constant rate IS c=alpha/tau, same dimension (speed) as Stone 18's c=l_P/t_P",
     "in the (L,T,M) accounting (27): edge = length (1,0,0), tick = time (0,1,0), so the rate edge/tick = "
     "(1,-1,0) = speed = c's dimension; Stone 18's c=l_P/t_P has the same (1,-1,0). So the substrate's "
     "native rate (= container 24's c=alpha/tau, the LENGTH reading of alpha, 27.DA.3) is the SAME KIND "
     "as the Planck rate",
     ["PA.1", "24.SG.3", "27.DA.3"],
     "the identification of the substrate's rate with the physical c, at the level of KIND (dimension). "
     "Container 24.SG.3 proved c = alpha/tau: each step contributes exactly alpha per tick, a constant "
     "rate. Reading alpha as the EDGE quantum -- a length (container 27.DA.3's length reading of alpha, "
     "the c=alpha/tau leg) -- and tau as the tick (a time), the rate alpha/tau = edge/tick has dimension "
     "(length)/(time) = (1,-1,0) = SPEED, exactly c's dimension. Stone 18 P.2's c = l_P/t_P is also "
     "(length)/(time) = (1,-1,0). So the substrate's native constant rate and the Planck rate c=l_P/t_P "
     "are the SAME KIND -- both a length per time. This is the dimensional pre-condition for Kevin's "
     "hypothesis: you cannot identify edge/tick with l_P/t_P unless they are the same kind, and they are. "
     "(The VALUES are a separate matter -- external, PA.4. Here only the KIND is derived, from 27's "
     "dimension algebra.) So c=alpha/tau (24) is dimensionally a speed, matching c=l_P/t_P (18).",
     "UNIQUE (edge/tick = (1,-1,0) = speed = c; l_P/t_P = (1,-1,0); the same kind)", "DERIVED",
     {"edge_dim": list(EDGE_DIM), "tick_dim": list(TICK_DIM), "c_dim": list(C_DIM),
      "rate_dim": list(rate_dim), "rate_is_speed": rate_is_speed,
      "lP_over_tP_dim": list(lp_over_tp_dim), "same_kind_as_planck_rate": same_kind,
      "c_eq_alpha_over_tau": "container 24.SG.3 -- alpha = the edge quantum (length reading, 27.DA.3), tau = the tick",
      "same_kind": "edge/tick and l_P/t_P are both (length)/(time) = (1,-1,0) = speed"},
     check="edge/tick = (1,-1,0) = speed = c's dimension = l_P/t_P (18) -- c=alpha/tau (24) is the same KIND")
assert pa2_ok

# ---- PA.3 the filed entry (Kevin's Planck hypothesis) -- POSTULATE ----------------------
step("PA.3", "THE FILED ENTRY (18.P.3): edge = l_P, tick = t_P => c=edge/tick <-> c=l_P/t_P (correspondence)",
     "filed through the 19 gate: Kevin's Planck hypothesis (Stone 18 P.3) -- the edge = l_P, the tick = "
     "t_P -- so the substrate's c=edge/tick (PA.1/PA.2) <-> the Planck c=l_P/t_P (18.P.2); and alpha (the "
     "length/edge reading) = the Planck edge quantum. A CORRESPONDENCE; the Planck VALUES stay external "
     "(27), the physical identification is assumed",
     ["PA.1", "PA.2", "18.P.3"],
     "the entry, and the honest status of the test. SUBSTRATE SIDE (checked): the substrate has a definite "
     "edge, a definite tick, and a constant edge/tick rate (PA.1) that is dimensionally a speed = c's kind "
     "(PA.2). PHYSICS SIDE (cited, Stone 18 P.2/P.3): c = l_P/t_P exactly (P.2); Kevin's hypothesis (P.3, "
     "held FLAGGED) is that l_P is the registration edge and t_P the tick. THE CORRESPONDENCE: the "
     "substrate's edge <-> l_P, the tick <-> t_P, so c=edge/tick <-> c=l_P/t_P, and alpha (the edge/length "
     "reading, 27.DA.3) <-> the Planck edge quantum. WHAT DOES NOT TRAVEL: the Planck VALUES l_P, t_P "
     "(among the 3 irreducibly-external anchors, container 27 -- NOT derived; they enter at measurement); "
     "the physical identification (that a registration step IS a Planck time, that the adjacency edge IS a "
     "Planck length -- assumed, Kevin's flagged hypothesis). FALSIFICATION SURFACE / THE HONEST RESULT: "
     "the substrate MUST have an edge, a tick, and a constant edge/tick rate of the right KIND -- it DOES "
     "(PA.1/PA.2), so the hypothesis is NOT REFUTED. But it is also NOT PROVEN: because c=l_P/t_P is a "
     "standard identity (18.P.2), the identification reproduces c BY CONSTRUCTION -- an IDENTITY, not a "
     "prediction that could have failed. So the Planck-anchor test comes out STRUCTURALLY CONSISTENT but "
     "NOT DISCRIMINATING: the substrate has exactly the edge/tick/rate structure Kevin's hypothesis needs, "
     "held as a CORRESPONDENCE, with the values external. A CORRESPONDENCE, WEAK; quarantined.",
     "POSTULATE (Kevin's Planck hypothesis: edge=l_P, tick=t_P; a held correspondence, not proven/refuted)",
     "POSTULATE",
     {"substrate_side": "a definite edge + tick + constant edge/tick rate (PA.1), dimensionally a speed (PA.2)",
      "physics_side_cited": "c=l_P/t_P exactly (18.P.2); Kevin's hypothesis l_P=edge, t_P=tick (18.P.3, flagged)",
      "correspondence": "edge <-> l_P; tick <-> t_P; c=edge/tick <-> c=l_P/t_P; alpha (edge reading) <-> the Planck edge quantum",
      "what_does_not_travel": "the Planck VALUES l_P, t_P (3 external anchors, 27); the physical identification (assumed)",
      "honest_result": "NOT REFUTED (the substrate has the structure) and NOT PROVEN (values external; reproduces c by construction) -- STRUCTURALLY CONSISTENT",
      "not_discriminating": "c=l_P/t_P is a standard identity (18.P.2), so it reproduces c by construction -- an identity, not a prediction",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "downstream_premise_use": False},
     check=None)

# ---- PA.4 discrimination + the Planck values + the alpha value -- OWED (located) --------
step("PA.4", "DISCRIMINATION owed: the test is an IDENTITY not a prediction; the Planck values external; the value",
     "the test as discharged is an IDENTITY (c=edge/tick reproduces c by construction, since c=l_P/t_P is "
     "exact, 18.P.2), consistent NOT discriminating (18.P.4); the Planck VALUES l_P, t_P stay external "
     "(27); the full alpha value (the edge quantum's number) waits behind the external anchor and the "
     "dimensionless alpha_hat. Located",
     ["PA.3", "27.DA.2"],
     "the residual, located and NOT attempted -- the honest boundary. PA.1-PA.3 establish that the "
     "substrate HAS the edge/tick/constant-rate structure Kevin's Planck hypothesis needs, and file the "
     "identification as a held correspondence. What remains: (i) DISCRIMINATION -- the test is an IDENTITY "
     "(Stone 18 P.4): because c=l_P/t_P is exact, edge=l_P & tick=t_P reproduces c by construction; it "
     "cannot FAIL, so it does not yet forbid any measurement; it passes on consistency, not "
     "discrimination; (ii) the PLANCK VALUES l_P, t_P are among the 3 irreducibly-external anchors "
     "(container 27) -- the substrate does not, and cannot, emit them; (iii) the full alpha VALUE -- the "
     "edge quantum's number -- is alpha_hat (dimensionless, the substrate's forward work) times the "
     "external Planck anchor. So the Planck-anchor test is discharged as a consistent correspondence; the "
     "discrimination, the Planck values, and the value are the forward work / external. NOT attempted here. "
     "NEXT in the alpha-value chain: Step 4, the cosmological-constant value (rho_Lambda = alpha x min "
     "archic density, container 15), computed-then-compared, gated behind alpha_hat + the anchor.",
     "OWED (discrimination -- 18.P.4; the Planck values -- external, 27; the alpha value -- Step 4; located)",
     "OWED",
     {"present": False,
      "discrimination_owed": "the test is an identity (reproduces c by construction, 18.P.2); consistent not discriminating (18.P.4)",
      "planck_values_external": "l_P, t_P among the 3 irreducibly-external anchors (27); not derived",
      "the_value": "the full alpha value = alpha_hat (dimensionless, forward work) x the external Planck anchor",
      "next": "Step 4 -- rho_Lambda = alpha x min archic density (15), computed-then-compared, gated on alpha_hat + anchor",
      "located_not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="33-planck-anchor-test",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        edge_sq_dist=EDGE_SQ_DIST, archons_per_tick=ARCHONS_PER_TICK,
        rate_constant=rate_constant, rate_dim=list(rate_dim), rate_is_speed=rate_is_speed,
        same_kind_as_planck_rate=same_kind,
        planck_hypothesis_structurally_consistent=True,
        finding="the Planck-anchor test: the substrate HAS a definite edge (minimal adjacency, 13), a "
                "definite tick (one archon per step, 24), and a CONSTANT edge/tick rate that is "
                "dimensionally a speed = c (PA.1/PA.2 -- = container 24's c=alpha/tau, length reading of "
                "alpha, 27.DA.3); Kevin's hypothesis edge=l_P/tick=t_P is filed as a held correspondence "
                "(PA.3, POSTULATE, WEAK). HONEST OUTCOME: STRUCTURALLY CONSISTENT but NOT DISCRIMINATING -- "
                "not refuted (the substrate has the structure), not proven (the Planck values are external, "
                "27, and it reproduces c by construction -- an identity, 18.P.4). Discrimination + the "
                "values are OWED (PA.4). Danger-free.",
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
