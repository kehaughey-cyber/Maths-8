#!/usr/bin/env python3
"""Container 34 -- THE VACUUM VALUE (rho_Lambda): the flagship, configuration landed, value OWED.
Rests on 14 (flat_ball, tri -> the min density), 15 (the vacuum = min-density direction), 24 (the
structural alpha), 27 (the dimension accounting); cites 32/33 (ruler + anchor). Filed through the 19
gate. alpha-value plan Step 4 (2026-08-29, Maths 6.5) -- the culmination of the physics-bridge arc.

THE FLAGSHIP: the cosmological constant / vacuum energy density rho_Lambda. Master-handoff reading:
'vacuum = the lattice at MINIMUM archic density; dark energy = same, cosmologically.' So rho_Lambda =
alpha x rho_vac, where rho_vac = the minimum archic density (container 15, at the twelve) and alpha = the
per-archon quantum (container 24). This container LANDS THE CONFIGURATION -- what rho_Lambda IS and how it
would be checked -- with the VALUE explicitly OWED, gated behind exactly one dimensionless factor
(alpha_hat) plus the 3 irreducibly-external Planck anchors (container 27).

THE DISCIPLINE (loud): the value is computed-then-compared, NEVER fitted. Do NOT chase 1/phi^3 /
standing-lag (the old top-down near-misses). The mass/census DANGER ZONE stays OUT. rho_Lambda's NUMBER
is deferred until alpha_hat closes AND top-down meets bottom-up -- naming the owed is the result here.

  VV.1 the vacuum CONFIGURATION = the minimum archic density: container 15's rho_min = flat_ball - tri at
       the twelve = [6,16,31,51] for r=1..4; the deficit there is the triangular number tri(r)=r(r+1)/2,
       the MAXIMUM deficit -- the substrate at its lowest packing. DERIVED (exact, consumes 14).
  VV.2 the assembly rho_Lambda = alpha x rho_vac is dimensionally an ENERGY DENSITY: [alpha]=(2,-2,1)
       energy/archon, [rho_vac]=(-3,0,0) archons/volume, product = (-1,-2,1) = energy/volume = the
       cosmological constant's dimension (container 27). The FORM is derived. DERIVED (dimension).
  VV.3 the vacuum READING (15.C.3): vacuum = min archic density; dark energy = same, cosmologically;
       rho_Lambda = alpha x rho_vac the vacuum energy density. Held, quarantined. POSTULATE.
  VV.4 the VALUE, located and OWED: rho_Lambda = alpha_hat x (Planck-anchor monomial) x (min-density
       count), computed-then-compared NEVER fitted; gated behind alpha_hat (the ONE dimensionless factor
       still owed) + the 3 external anchors (27). The falsification surface; danger zone out; do NOT chase
       1/phi^3 / standing-lag. OWED.

DANGER-FREE by construction: no number is emitted, nothing is fitted, no mass/census is touched. The
result is the CONFIGURATION and the precise location of the single remaining unknown.

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


# ================================================================ the min density (consumes 14) + dims (27)
def flatBall(r):
    return 1 + 3 * r * (r + 1)              # container 14.B.1


def tri(r):
    return r * (r + 1) // 2                 # container 14 tri (the triangular number)


# ---- VV.1 the vacuum configuration = the minimum archic density -- DERIVED -------------
R = [1, 2, 3, 4]
RHO_MIN = [flatBall(r) - tri(r) for r in R]        # container 15's rho_min at the twelve = [6,16,31,51]
DEFICIT_AT_TWELVE = [tri(r) for r in R]            # the deficit there = tri(r) = [1,3,6,10], the MAX
min_is_flat_minus_tri = (RHO_MIN == [6, 16, 31, 51])
deficit_is_triangular = (DEFICIT_AT_TWELVE == [1, 3, 6, 10])
vv1_ok = min_is_flat_minus_tri and deficit_is_triangular
step("VV.1", "the vacuum CONFIGURATION = the minimum archic density (rho_min = flat_ball - tri, at the twelve)",
     "the vacuum is the substrate at its lowest packing: container 15's minimum density rho_min = "
     "flat_ball(r) - tri(r) at the twelve = [6,16,31,51] for r=1..4; the deficit there is the triangular "
     "number tri(r) = r(r+1)/2 = [1,3,6,10], the MAXIMUM deficit. That min-density configuration is the "
     "vacuum",
     ["15.C.1", "14.B.3"],
     "the substrate side of the flagship: WHAT configuration is the vacuum. The master-handoff reading is "
     "'vacuum = the lattice at MINIMUM archic density'. Container 15 (density-extremum) located that "
     "minimum: the density rho = |B_r| is LOWEST at the twelve (the deg-5 vertices), where the ball count "
     "is flat_ball(r) minus the triangular deficit tri(r). Recomputed cold here (consuming container 14's "
     "flat_ball and tri): rho_min = flat_ball - tri = [7,19,37,61] - [1,3,6,10] = [6,16,31,51] at r=1..4, "
     "and the deficit at each of the twelve is tri(r) = [1,3,6,10] -- the primordial law (14.B.3), the "
     "MAXIMUM positive curvature. So the vacuum configuration is definite: the twelve, at minimum density, "
     "maximum deficit. This is the substrate's own object (a count), exact; the IDENTIFICATION of "
     "min-density AS the physical vacuum is the reading (VV.3, 15.C.3). Here the configuration and its "
     "exact count are derived. DANGER-FREE: a count, no value.",
     "UNIQUE (rho_min = flat_ball - tri at the twelve = [6,16,31,51]; deficit = tri(r) = [1,3,6,10])",
     "DERIVED",
     {"rho_min_r1to4": RHO_MIN, "deficit_at_twelve": DEFICIT_AT_TWELVE,
      "min_is_flat_minus_tri": min_is_flat_minus_tri, "deficit_is_triangular": deficit_is_triangular,
      "config": "the vacuum = the minimum archic density = the twelve at max deficit (min packing)",
      "source": "container 15's rho_min, recomputed from container 14's flat_ball and tri"},
     check="rho_min = flat_ball - tri at the twelve = [6,16,31,51]; deficit = tri(r) = [1,3,6,10] (container 15/14)")
assert vv1_ok

# ---- VV.2 rho_Lambda = alpha x rho_vac is dimensionally an energy density -- DERIVED ----
def dadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
ALPHA_DIM = (2, -2, 1)                 # energy per archon (container 27's energy reading of alpha)
RHO_VAC_DIM = (-3, 0, 0)               # archons per volume (a number density; the volume is external, l_P^3)
ENERGY_DENSITY_DIM = (-1, -2, 1)       # energy / volume = the cosmological constant's dimension
rho_lambda_dim = dadd(ALPHA_DIM, RHO_VAC_DIM)      # (2,-2,1)+(-3,0,0) = (-1,-2,1)
is_energy_density = (rho_lambda_dim == ENERGY_DENSITY_DIM)
vv2_ok = is_energy_density
step("VV.2", "rho_Lambda = alpha x rho_vac is dimensionally an ENERGY DENSITY (-1,-2,1)",
     "the assembly rho_Lambda = alpha x rho_vac: [alpha]=(2,-2,1) energy per archon (container 27's energy "
     "reading), [rho_vac]=(-3,0,0) archons per volume, so the product = (-1,-2,1) = energy/volume = the "
     "cosmological constant's dimension. The FORM is derived and dimensionally consistent",
     ["VV.1", "24.SG.1", "27.DA.3"],
     "the assembly form of the flagship, and its dimensional consistency. The vacuum energy density "
     "rho_Lambda = (energy per archon) x (archons per volume) = alpha x rho_vac. Container 24 (SG.1) gives "
     "the per-archon quantum alpha (I = alpha x L); container 27 (DA.3) gives its energy reading, "
     "dimension (2,-2,1) = M L^2 T^-2. The vacuum number-density rho_vac = archons per unit volume has "
     "dimension (count)/(length^3) = (0,0,0)-(3,0,0) = (-3,0,0) (the volume, a length^3, is external -- "
     "the Planck volume). Their product: (2,-2,1)+(-3,0,0) = (-1,-2,1) = energy per volume = exactly the "
     "cosmological constant / vacuum-energy-density dimension. So rho_Lambda = alpha x rho_vac is "
     "dimensionally an energy density -- the assembly is consistent, the form is derived. (The VALUE is a "
     "separate matter: the count rho_vac is the substrate's, dimensionless and exact (VV.1); alpha carries "
     "the units and its value is owed -- VV.4.) DANGER-FREE: a dimension, no number.",
     "UNIQUE (rho_Lambda = alpha x rho_vac has dimension (-1,-2,1) = energy density)", "DERIVED",
     {"alpha_dim": list(ALPHA_DIM), "rho_vac_dim": list(RHO_VAC_DIM),
      "rho_lambda_dim": list(rho_lambda_dim), "energy_density_dim": list(ENERGY_DENSITY_DIM),
      "is_energy_density": is_energy_density,
      "form": "rho_Lambda = alpha (energy/archon) x rho_vac (archons/volume) = energy/volume",
      "volume_external": "the volume (l_P^3) is external -- one of the 3 Planck anchors (27)"},
     check="rho_Lambda = alpha x rho_vac: (2,-2,1)+(-3,0,0) = (-1,-2,1) = energy density -- the assembly is consistent")
assert vv2_ok

# ---- VV.3 the vacuum reading -- POSTULATE ----------------------------------------------
step("VV.3", "THE VACUUM READING (15.C.3): vacuum = min archic density; rho_Lambda = alpha x rho_vac",
     "filed through the 19 gate: vacuum = the minimum archic density (VV.1, container 15.C.3); dark energy "
     "= the same, cosmologically; rho_Lambda = alpha x rho_vac (VV.2) the vacuum energy density. A reading "
     "-- the identification of the substrate's min-density configuration with the physical vacuum -- held",
     ["VV.1", "VV.2", "15.C.3"],
     "the reading that turns the derived configuration into a physical claim. SUBSTRATE SIDE (checked): "
     "the minimum archic density is a definite configuration (VV.1); rho_Lambda = alpha x rho_vac is "
     "dimensionally an energy density (VV.2). PHYSICS SIDE (cited): the cosmological constant / dark "
     "energy is a positive vacuum energy density, the substrate's largest-scale, lowest-density regime. "
     "THE READING (container 15.C.3, held POSTULATE): the substrate at MINIMUM archic density IS the "
     "vacuum; dark energy is the same object cosmologically; and rho_Lambda = alpha x rho_vac is its "
     "energy density. WHAT DOES NOT TRAVEL: the VALUE (VV.4); the mass/census (the DANGER ZONE, out); the "
     "sign/dynamo conflation (container 16's dynamo eps is NOT the vacuum -- kept typed apart). "
     "FALSIFICATION SURFACE (the flagship's whole point): rho_Lambda, once alpha's value is in hand, is "
     "COMPUTED from alpha x rho_vac and COMPARED to the measured cosmological constant -- never fitted. If "
     "the computed value missed the measurement, the reading fails. A CORRESPONDENCE, WEAK; quarantined. "
     "This is the arc's flagship: every prior rung feeds it, and its value is the one number the whole "
     "construction is built to predict-then-check.",
     "POSTULATE (vacuum = min archic density; rho_Lambda = alpha x rho_vac; a held reading, quarantined)",
     "POSTULATE",
     {"substrate_side": "the minimum archic density configuration (VV.1); rho_Lambda = alpha x rho_vac dimensionally (VV.2)",
      "physics_side_cited": "the cosmological constant / dark energy: a positive vacuum energy density",
      "reading": "vacuum = min archic density (15.C.3); dark energy = same cosmologically; rho_Lambda = alpha x rho_vac",
      "what_does_not_travel": "the VALUE (VV.4); the mass/census (danger zone); the dynamo eps (16, NOT the vacuum -- typed apart)",
      "falsification_surface": "rho_Lambda computed from alpha x rho_vac, compared to the measured cosmological constant -- NEVER fitted",
      "the_flagship": "the one number the whole arc is built to predict-then-check",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "downstream_premise_use": False},
     check=None)

# ---- VV.4 the value, located and OWED ---------------------------------------------------
step("VV.4", "the VALUE, located: rho_Lambda = alpha_hat x (Planck anchor) x (min-density count) -- OWED",
     "the VALUE of rho_Lambda = alpha_hat x (Planck-anchor monomial) x (min-density count, VV.1), "
     "computed-then-compared NEVER fitted; gated behind alpha_hat -- the ONE dimensionless factor still "
     "owed -- plus the 3 irreducibly-external Planck anchors (27). Do NOT chase 1/phi^3 / standing-lag; "
     "the census danger zone stays out. Located, not attempted",
     ["VV.3", "27.DA.2", "22.CV.3"],
     "the residual -- and it is the precise statement of where the WHOLE ARC now stands. The configuration "
     "is landed (VV.1-VV.3): rho_Lambda is the energy density of the minimum-archic-density vacuum, = alpha "
     "x rho_vac, dimensionally exact, with the min-density COUNT the substrate's own (exact, VV.1). What "
     "remains for the VALUE: rho_Lambda = alpha_hat x (a Planck-unit anchor monomial) x (the min-density "
     "count). Everything in that product is derived or external EXCEPT ONE thing: (i) the min-density "
     "count -- derived (VV.1, container 15); (ii) the Planck anchors (l_P, m_P, ...) -- the 3 irreducibly- "
     "external numbers (container 27), accepted as external; (iii) alpha_hat -- the single DIMENSIONLESS "
     "factor, the substrate's forward work, still OWED. So the entire arc converges to one unknown: "
     "alpha_hat. THE DISCIPLINE, loud: rho_Lambda's number is COMPUTED from the product and COMPARED to "
     "the measured cosmological constant, NEVER fitted; do NOT chase 1/phi^3 or the standing-lag (the old "
     "top-down near-misses -- refused); the mass/census danger zone stays OUT; and per container 22 (CV.3) "
     "the warrant condition (top-down meets bottom-up) must also hold before any value is 'equivalence'. "
     "So the flagship's value is deferred until alpha_hat closes AND top-down meets bottom-up -- and "
     "naming that, precisely, is the honest result. NOT attempted here.",
     "OWED (the value = alpha_hat x anchor x count; gated on alpha_hat + the 3 external anchors; located)",
     "OWED",
     {"present": False,
      "form": "rho_Lambda = alpha_hat x (Planck-anchor monomial) x (min-density count, VV.1)",
      "derived_or_external": "min-density count DERIVED (VV.1); the 3 Planck anchors EXTERNAL (27)",
      "the_one_unknown": "alpha_hat -- the single dimensionless factor still owed (the substrate's forward work)",
      "discipline": "computed-then-compared NEVER fitted; do NOT chase 1/phi^3 / standing-lag (refused); census danger zone OUT",
      "warrant": "per 22.CV.3, top-down must meet bottom-up before any value is 'equivalence'",
      "located_not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="34-vacuum-value",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        rho_min_r1to4=RHO_MIN, deficit_at_twelve=DEFICIT_AT_TWELVE,
        rho_lambda_dim=list(rho_lambda_dim), is_energy_density=is_energy_density,
        configuration_landed=True, value_owed_behind_alpha_hat=True,
        finding="the FLAGSHIP, configuration landed, value OWED: the vacuum = the minimum archic density "
                "(container 15's rho_min = flat_ball - tri at the twelve = [6,16,31,51] -- VV.1), and "
                "rho_Lambda = alpha x rho_vac is dimensionally an energy density (-1,-2,1) -- VV.2; the "
                "vacuum reading is held (VV.3, POSTULATE, WEAK, with the falsification surface named -- "
                "computed-then-compared NEVER fitted); the VALUE = alpha_hat x (Planck anchor) x "
                "(min-density count) is OWED (VV.4), gated behind the ONE dimensionless factor alpha_hat "
                "plus the 3 external anchors. The whole arc converges to one unknown: alpha_hat.",
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
