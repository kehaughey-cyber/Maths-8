#!/usr/bin/env python3
"""Container 16 -- FRUSTRATION DYNAMO: the deficit never closes. Rests on 08, 03; cf 14.

Step 4 of the physics-bridge arc. The icosahedral substrate is geometrically FRUSTRATED: five regular
tetrahedra around a shared edge do not close, leaving an angular gap that is exactly nonzero. That
irreducible gap is read (as a possibility) as the PERSISTENCE ENGINE -- the delta that prevents the
substrate from ever settling. Two disciplines govern this container:

  (i)  ANTI-CONFLATION. This gap is a THIRD, distinct quantity -- not container 14's ball-growth deficit
       (flat_ball - |B_r|), and not its angle-deficit charge (12*chi = 24 radits). It is the 3-D
       DIHEDRAL packing gap. All three live on the same icosahedral geometry; none is the others. And
       Lambda = 2pi/3 (a secondary-route clue value) is distinct again. Kept typed apart on sight.
  (ii) DON'T OVER-COMMIT (the container-15 lesson). The mathematics -- the gap is exactly > 0 -- is
       DERIVED. The physical reading -- gap = dynamo = why the substrate persists; and that a
       cosmological Lambda corresponds to this DYNAMO, NOT to the vacuum (Step 3's min-density) -- is a
       POSTULATE (named possibility, no value, no downstream premise). Do not sell the reading as the
       mathematics.

  D.1 the TETRAHEDRAL GAP. The regular-tetrahedron dihedral angle is arccos(1/3) = 2*arcsin(sqrt3/3)
      (~70.5288 deg). Five tetrahedra around a common edge span 5*arccos(1/3) ~ 352.644 deg < 360 deg,
      leaving eps = 2pi - 5*arccos(1/3) = 2pi - 10*arcsin(sqrt3/3) ~ 7.356 deg > 0. STRICT positivity
      needs no numerics: eps > 0  <=>  arccos(1/3) < 2pi/5  <=>  1/3 > cos(2pi/5) = (sqrt5 - 1)/4
      <=>  3(sqrt5 - 1) < 4  <=>  3*sqrt5 < 7  <=>  45 < 49. A clean integer core (the trig provenance
      cos(2pi/5) = (sqrt5-1)/4 and arccos(1/3) = 2*arcsin(sqrt3/3) needs R, so it is CITED, as
      container 10 cites arcsin(1/2) = pi/6; the reduced inequality 45 < 49 is proved zero-axiom).

  D.2 IRREDUCIBLE, and DISTINCT from the Step-2 deficits. eps > 0 EXACTLY -- not a finite-size or
      discretization artifact, and independent of scale -- so the substrate has NO strain-free (closed)
      configuration; the frustration never resolves. And eps (~7.356 deg) is NOT the ball-growth deficit
      and NOT the angle-deficit charge 12*chi (= 24 radits); it is the dihedral packing gap. Three
      different frustrations of one geometry, named apart.

  D.3 the DYNAMO reading (POSTULATE; possible, NOT confirmed; values deferred). eps != 0 read as the
      PERSISTENCE ENGINE: the irreducible frustration is what keeps the substrate from settling, forcing
      ongoing dynamics. CRITICAL anti-conflation: this DYNAMO (the delta that prevents resolution) is
      NOT the VACUUM (Step 3's minimum-density extremum) -- different objects. A cosmological-constant-
      like Lambda, if it corresponds to anything here, corresponds to the DYNAMO, not to a vacuum energy
      density. Lambda = 2pi/3 is a secondary-route (torsion) CLUE value -- cited, not derived here, and
      distinct from eps and from 12*chi. NO value is computed or fitted.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


def d6(x):
    return round(x, 6)


# ---- D.1 the tetrahedral gap -- DERIVED -------------------------------------
dihedral = math.acos(1 / 3)                                 # regular-tetrahedron dihedral angle
dihedral_via_arcsin = 2 * math.asin(math.sqrt(3) / 3)       # = 2*arcsin(sqrt3/3), the same
identity_ok = abs(dihedral - dihedral_via_arcsin) < 1e-12
five_span = 5 * dihedral
eps = 2 * math.pi - five_span                               # = 2pi - 10*arcsin(sqrt3/3)
eps_deg = math.degrees(eps)
# STRICT positivity, exact integer core: eps>0 <=> 1/3 > cos(2pi/5)=(sqrt5-1)/4 <=> 3 sqrt5 < 7 <=> 45<49
cos_2pi_5 = math.cos(2 * math.pi / 5)                       # = (sqrt5 - 1)/4
cos_exact = (math.sqrt(5) - 1) / 4
core_lhs, core_rhs = 3 * 3 * 5, 7 * 7                       # (3 sqrt5)^2 = 45  vs  7^2 = 49
positivity_core = core_lhs < core_rhs                        # 45 < 49  <=>  eps > 0
step("D.1", "the tetrahedral gap: five regular tetrahedra around an edge leave eps ~ 7.356 deg > 0",
     "eps = 2pi - 5*arccos(1/3) = 2pi - 10*arcsin(sqrt3/3); eps > 0 <=> cos(2pi/5)=(sqrt5-1)/4 < 1/3 "
     "<=> 45 < 49", ["08", "03.4"],
     "the regular-tetrahedron DIHEDRAL angle is arccos(1/3) = 2*arcsin(sqrt3/3) (~70.5288 deg). Five "
     "tetrahedra packed around a shared edge span 5*arccos(1/3) ~ 352.644 deg, which is LESS than a full "
     "2pi -- so they do not close; the gap is eps = 2pi - 5*arccos(1/3) = 2pi - 10*arcsin(sqrt3/3) ~ "
     "7.356 deg. This is the classic geometric FRUSTRATION of icosahedral/tetrahedral packing. That eps "
     "is STRICTLY positive needs no numerics: eps > 0 iff arccos(1/3) < 2pi/5 iff 1/3 > cos(2pi/5), and "
     "cos(2pi/5) = (sqrt5 - 1)/4, so the claim is 3(sqrt5 - 1) < 4, i.e. 3*sqrt5 < 7, i.e. 45 < 49 -- a "
     "clean integer core. The trig identities (needing R) are CITED (as container 10 cites "
     "arcsin(1/2)=pi/6); the reduced inequality is proved zero-axiom.",
     "UNIQUE (the gap is fixed; strictly positive by 45 < 49)", "DERIVED",
     {"dihedral_arccos_1_3_deg": d6(math.degrees(dihedral)),
      "dihedral_eq_2_arcsin_sqrt3_3": identity_ok,
      "five_tetrahedra_span_deg": d6(math.degrees(five_span)),
      "eps_rad": d6(eps), "eps_deg": d6(eps_deg),
      "positivity_reduction": "eps>0 <=> cos(2pi/5)=(sqrt5-1)/4 < 1/3 <=> 3 sqrt5 < 7 <=> 45 < 49",
      "cos_2pi_5_check": abs(cos_2pi_5 - cos_exact) < 1e-12,
      "integer_core_lhs_45": core_lhs, "integer_core_rhs_49": core_rhs,
      "strictly_positive": positivity_core},
     check="eps = 2pi - 5*arccos(1/3) ~ 7.356 deg > 0; strict positivity reduces to 45 < 49")
assert identity_ok and positivity_core and core_lhs == 45 and core_rhs == 49
assert 7.35 < eps_deg < 7.36 and abs(cos_2pi_5 - cos_exact) < 1e-12

# ---- D.2 irreducible and distinct -- DERIVED -------------------------------
TWELVE_CHI_RADITS = 24                                       # container 14 B.4, the angle-deficit charge
LAMBDA_DEG = math.degrees(2 * math.pi / 3)                   # 120 deg, the clue value (D.3)
distinct_from_12chi = round(eps_deg, 3) != TWELVE_CHI_RADITS
distinct_from_lambda = round(eps_deg, 3) != round(LAMBDA_DEG, 3)
# scale independence: eps does not depend on any mesh size -- it is a fixed angle of the geometry
step("D.2", "the frustration is IRREDUCIBLE and DISTINCT from the Step-2 deficits",
     "eps > 0 exactly (not finite-size, scale-independent); eps (~7.356 deg) != 12*chi (24 radits) != "
     "Lambda (120 deg)", ["D.1", "14.B.4"],
     "eps is EXACTLY positive -- a fixed angle of the geometry, not a discretization or finite-size "
     "artifact, and independent of any mesh scale. So the substrate has NO strain-free (closed) "
     "configuration; the frustration never resolves. And -- the anti-conflation discipline made "
     "explicit -- eps is a THIRD, distinct quantity: NOT container 14's ball-growth deficit "
     "(flat_ball - |B_r|), and NOT its angle-deficit charge 12*chi = 24 radits (Gauss-Bonnet). eps is "
     "the 3-D DIHEDRAL packing gap (~7.356 deg). Three different frustrations of one icosahedral "
     "geometry; numerically eps != 24 != 120, and they are defined on different structures. Named apart "
     "on sight, never merged.",
     "UNIQUE (eps is a fixed positive angle; distinct from the other two frustrations)", "DERIVED",
     {"eps_deg": d6(eps_deg), "irreducible_not_finite_size": True, "scale_independent": True,
      "no_strain_free_configuration": True,
      "distinct_from_angle_deficit_12chi_24": distinct_from_12chi,
      "distinct_from_lambda_120": distinct_from_lambda,
      "three_frustrations": "ball-growth deficit (14) | angle-deficit charge 12chi=24 (14.B.4) | "
                            "dihedral gap eps~7.356deg (here)"},
     check="eps>0 is exact and scale-independent; eps != 24 (12chi) and != 120 (Lambda)")
assert distinct_from_12chi and distinct_from_lambda

# ---- D.3 the dynamo reading -- POSTULATE (values deferred) ------------------
step("D.3", "the dynamo reading: eps != 0 = the persistence engine; a DYNAMO, NOT the vacuum "
     "(POSSIBLE, NOT confirmed; values deferred)",
     "eps != 0 read as what prevents the substrate from settling; the dynamo is NOT the vacuum "
     "(Step 3 min-density); Lambda = 2pi/3 a cited clue value for the dynamo", ["D.1", "D.2", "15.C.3"],
     "the arc's working reading, NAMED as a possibility and NOT asserted (the container-15 discipline: "
     "the math is derived, the physical reading is held). eps != 0 is read as the PERSISTENCE ENGINE -- "
     "the irreducible frustration is what keeps the substrate from ever settling into a closed state, "
     "forcing ongoing dynamics. THE CRITICAL ANTI-CONFLATION (handoff, load-bearing): this DYNAMO -- the "
     "delta that prevents resolution -- is NOT the VACUUM (Step 3's minimum-density extremum, container "
     "15). They are different objects; do not conflate. A cosmological-constant-like Lambda, if it "
     "corresponds to anything in this substrate, corresponds to the DYNAMO, not to a vacuum energy "
     "density. Lambda = 2pi/3 is a SECONDARY-route (torsion) clue value -- CITED, not derived here, and "
     "distinct from eps and from 12*chi. NO value is computed or fitted; the correspondence and any "
     "value await warrant (the derivation closing AND top-down meeting bottom-up). No downstream "
     "container may use this reading as a premise.",
     "POSSIBLE, NOT confirmed; dynamo != vacuum; no value; no downstream premise", "POSTULATE",
     {"reading": "eps != 0 = persistence engine (dynamo)",
      "dynamo_is_not_the_vacuum": True,
      "vacuum_is": "Step 3 minimum-density extremum (container 15) -- a DIFFERENT object",
      "lambda_2pi_3_deg": d6(LAMBDA_DEG),
      "lambda_status": "secondary-route (torsion) clue value; CITED, not derived here; distinct from eps and 12chi",
      "status": "possible, NOT confirmed", "values": "DEFERRED",
      "downstream_premise_use": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="16-frustration-dynamo", steps=STEPS, grades=GRADES,
           values=dict(eps_rad=d6(eps), eps_deg=d6(eps_deg),
                       dihedral_deg=d6(math.degrees(dihedral)),
                       five_tetrahedra_span_deg=d6(math.degrees(five_span)),
                       integer_core_lhs_45=core_lhs, integer_core_rhs_49=core_rhs,
                       strictly_positive=positivity_core,
                       twelve_chi_radits=TWELVE_CHI_RADITS, lambda_deg=d6(LAMBDA_DEG),
                       dynamo_is_not_the_vacuum=True))

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
