#!/usr/bin/env python3
"""Container 47 -- THE FOCUSING RESOLUTION: the 37-vs-15 tension is a spatial/spacetime TYPE error, dissolved by 46.

Step 4 of the forward frontier (Maths 6.7): resolve the discriminating tension 37.GM.5 surfaced. It read:
FOCUSING (attractive) is at the twelve (positive angle deficit, 37.GM.3), but 15.C.3 reads the twelve
(min density) as VACUUM/dark-energy, which is REPULSIVE -- an apparent contradiction. 37.GM.5 named three
candidate resolutions and left it a held reading. With the spacetime SIGNATURE now forced (46), candidate
(b) is the resolution and it is forced: the two "focusings" are DIFFERENT operators (spatial vs spacetime),
so there is no contradiction.

  FR.1  the tension, precisely. 37.GM.3: a positive spatial angle-deficit (the twelve, d<6) FOCUSES
        geodesics (attractive). 15.C.3: the twelve (min density) <-> VACUUM / dark-energy (repulsive).
        Same twelve, opposite signs -- the apparent conflict. DERIVED (restates it).

  FR.2  the two are DIFFERENT operators (needs 46's signature). 37.GM.3's focusing is SPATIAL -- the
        Gaussian curvature K of the intrinsic 2-surface (25/14, the deficit). Gravitational
        attraction/repulsion is a SPACETIME fact: the Raychaudhuri focusing of the TIMELIKE geodesic
        congruence, dtheta/dtau ~ -(rho + 3p) -- which needs the timelike direction of the signature (46).
        Spatial K and the timelike Ricci contraction R_{tt} are different objects. DERIVED (cites
        Raychaudhuri; enabled by 46).

  FR.3  therefore NO CONTRADICTION. The spacetime sign is set by rho+3p (the strong-energy quantity), NOT
        by the spatial K: for VACUUM/Lambda (w=-1) rho+3p = -2rho < 0 => REPULSIVE (defocuses timelike
        geodesics); for MATTER/dust (w=0) rho+3p = rho > 0 => attractive. This is INDEPENDENT of the
        spatial curvature sign. So a region can have positive SPATIAL curvature (37's spatial focusing) AND
        be vacuum/Lambda-dominated (15's spacetime repulsion) at once -- the two signs live on different
        axes. The 37.GM.5 tension is a spatial/spacetime TYPE error, dissolved by 46. DERIVED.

  FR.4  what is NOT decided (held): WHICH the twelve are -- vacuum (15.C.3) or matter -- is a SEPARATE
        reading. The resolution removes the CONTRADICTION (FR.3), not the reading; 15.C.3 survives,
        uncontradicted by the focusing sign. POSTULATE (held).

  FR.5  OWED: the quantitative Raychaudhuri on the substrate (needs the continuum + a stress-energy = mass,
        danger zone); deciding vacuum-vs-matter for the twelve (15.C.3, a reading + the matter census). OWED.

Rests on 37 (GM.3/GM.5, the focusing + the tension), 15 (C.3, the vacuum reading), 46 (the signature, which
separates spatial from spacetime); cites the Raychaudhuri equation / the strong energy condition.
DANGER-FREE: it dissolves a sign confusion by a type distinction; no mass, no value. `--check` recomputes.
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


# the strong-energy quantity rho + 3p for equation of state p = w*rho (the spacetime focusing sign)
def rho_plus_3p(rho, w):
    return rho + 3 * (w * rho)


# ---- FR.1 the tension, precisely -- DERIVED --------------------------------------------
def angle_deficit(d):
    return 12 - 2 * d


twelve_deficit = angle_deficit(5)                       # +2 > 0: the twelve, positive spatial curvature
spatial_focus_attractive = (twelve_deficit > 0)         # 37.GM.3: positive deficit focuses (spatial)
twelve_is_vacuum_reading = True                          # 15.C.3: the twelve (min density) <-> vacuum (repulsive)
fr1_ok = spatial_focus_attractive and twelve_is_vacuum_reading
step("FR.1", "the tension: 37.GM.3 focuses (attractive) at the twelve (positive deficit); 15.C.3 reads the twelve as VACUUM (repulsive)",
     "37.GM.3: a positive spatial angle-deficit (the twelve, d=5, deficit +2) FOCUSES geodesics -- "
     "attractive. 15.C.3: the twelve (minimum archic density) <-> VACUUM / dark-energy -- repulsive. Same "
     "twelve, opposite signs: the apparent contradiction 37.GM.5 flagged as a discriminating test",
     ["37.GM.3", "14.B.4"],
     "state the tension exactly, so the resolution is measured against it. Container 37.GM.3 derived: the "
     "SIGN of the angle deficit sets focusing -- a positive deficit (a cone point, the twelve at d=5, "
     "deficit 12-10 = +2) FOCUSES geodesics (convergence, the attractive sign). Container 15.C.3 read the "
     "twelve (the MINIMUM archic density) as the VACUUM / dark-energy direction -- which is REPULSIVE "
     "(accelerated expansion). So at the SAME twelve, 37 says attractive (focusing) and 15 says repulsive "
     "(vacuum). 37.GM.5 flagged this as a test with three candidate resolutions -- (a) the twelve are "
     "matter not vacuum; (b) spatial curvature != vacuum-energy, different things; (c) the rho=flat-D "
     "inversion flips the reading -- and left it a held reading. This container resolves it via (b), now "
     "that the signature (46) makes 'spatial vs spacetime' a real distinction.",
     "UNIQUE (the tension is a definite pair of opposite signs at the twelve)", "DERIVED",
     {"twelve_deficit": twelve_deficit, "spatial_focus_attractive": spatial_focus_attractive,
      "twelve_is_vacuum_reading": twelve_is_vacuum_reading,
      "tension": "37.GM.3 attractive (spatial focusing) vs 15.C.3 repulsive (vacuum) at the same twelve"},
     check="the twelve have positive deficit (+2, 37 focusing) and are 15.C.3's vacuum reading -- the tension")
assert fr1_ok

# ---- FR.2 the two are different operators (needs 46) -- DERIVED -------------------------
step("FR.2", "the two focusings are DIFFERENT operators: 37 is SPATIAL (Gaussian K); GR attraction is SPACETIME (Raychaudhuri, timelike) -- needs 46",
     "37.GM.3's focusing is SPATIAL -- the Gaussian curvature K of the intrinsic 2-surface (25/14, the "
     "angle deficit). Gravitational attraction/repulsion is a SPACETIME fact: the Raychaudhuri focusing "
     "of the TIMELIKE geodesic congruence, dtheta/dtau ~ -(rho+3p), which needs the timelike direction of "
     "the signature (46). Spatial K and the timelike Ricci contraction R_{tt} are DIFFERENT objects",
     ["FR.1", "46.LS.4"],
     "the crux, and it needed the signature. Before 46 there was no principled 'spatial vs spacetime' "
     "split, so the two signs looked comparable. Now: 37.GM.3's focusing is the convergence of geodesics "
     "ON THE SPATIAL 2-SURFACE -- governed by the intrinsic Gaussian curvature K (the angle deficit, "
     "14/25). Gravitational attraction/repulsion is a different thing entirely: the RAYCHAUDHURI focusing "
     "of a congruence of TIMELIKE (worldline) geodesics in spacetime, dtheta/dtau = ... - R_{mu nu} u^mu "
     "u^nu, and for a perfect fluid R_{mu nu}u^mu u^nu = 4*pi*G*(rho + 3p). That contraction is over the "
     "TIMELIKE direction u -- which exists only because the signature is Lorentzian (46.LS.4): in a "
     "Euclidean (4,0) world there is no timelike u and no Raychaudhuri attraction at all. So the two "
     "'focusings' are DIFFERENT OPERATORS: spatial K (a property of the surface at an instant) vs the "
     "timelike Ricci contraction (a property of the spacetime, sourced by rho+3p). Cited: the Raychaudhuri "
     "equation and R_{mu nu}u^mu u^nu = 4piG(rho+3p); enabled by 46's timelike direction.",
     "UNIQUE (spatial Gaussian K != the timelike Ricci contraction; the split needs 46's signature)", "DERIVED",
     {"spatial_operator": "Gaussian curvature K of the 2-surface (the angle deficit, 14/25) -- 37.GM.3",
      "spacetime_operator": "Raychaudhuri: -R_{tt} = -4piG(rho+3p) on a TIMELIKE congruence -- needs 46's timelike direction",
      "different_objects": True, "enabled_by": "46.LS.4 (the Lorentzian signature gives a timelike direction)",
      "cited": "the Raychaudhuri equation; R_{mu nu}u^mu u^nu = 4piG(rho+3p)"},
     check="37's focusing is spatial K; GR attraction is the timelike Raychaudhuri contraction (needs 46) -- different operators")

# ---- FR.3 therefore no contradiction -- DERIVED ----------------------------------------
rho = 1
sp_vacuum = rho_plus_3p(rho, -1)         # w=-1: -2rho < 0 -> repulsive (defocuses timelike geodesics)
sp_dust = rho_plus_3p(rho, 0)            # w=0:  +rho > 0 -> attractive
vacuum_repulsive = (sp_vacuum < 0)
dust_attractive = (sp_dust > 0)
# the spacetime sign (rho+3p) is INDEPENDENT of the spatial curvature sign (K): all four combos are consistent
independent_axes = True
fr3_ok = vacuum_repulsive and dust_attractive and (sp_vacuum == -2) and (sp_dust == 1)
step("FR.3", "therefore NO CONTRADICTION: the spacetime sign is rho+3p (vacuum -2rho<0 repulsive; matter rho>0 attractive), INDEPENDENT of spatial K",
     "the SPACETIME focusing sign is set by rho+3p (the strong-energy quantity), NOT by the spatial K: "
     "for VACUUM/Lambda (w=-1) rho+3p = -2rho < 0 => REPULSIVE; for MATTER/dust (w=0) rho+3p = rho > 0 => "
     "attractive. This is INDEPENDENT of the spatial curvature sign, so positive spatial curvature (37's "
     "spatial focusing) and vacuum/Lambda repulsion (15's reading) can hold AT ONCE -- no contradiction. "
     "The 37.GM.5 tension is a spatial/spacetime TYPE error, dissolved by 46",
     ["FR.2"],
     "the dissolution. The spacetime attraction/repulsion sign is -(rho+3p) (Raychaudhuri, FR.2). RUN "
     "IT: for VACUUM (equation of state p = -rho, w=-1) rho+3p = rho - 3rho = -2rho < 0, so -(rho+3p) > "
     "0 = DEFOCUSING = REPULSIVE (this is exactly why dark energy accelerates expansion); for MATTER "
     "(dust, p=0) rho+3p = rho > 0 = focusing = attractive. So the spacetime sign is a property of the "
     "matter content (rho+3p), entirely SEPARATE from the SPATIAL Gaussian curvature K (37's deficit). "
     "The two signs are on INDEPENDENT axes: a cone point can have K > 0 (spatial geodesics converge on "
     "the surface, 37.GM.3) while the same region is vacuum-dominated with rho+3p < 0 (spacetime timelike "
     "geodesics defocus, 15.C.3) -- both true, no conflict. So the apparent contradiction 37.GM.5 flagged "
     "was a TYPE ERROR: it compared a spatial curvature sign with a spacetime attraction sign as if they "
     "were the same quantity. The signature (46) is exactly what tells them apart. Resolution (b), forced.",
     "UNIQUE (rho+3p sign: vacuum -2rho<0, matter rho>0; independent of spatial K -> no contradiction)", "DERIVED",
     {"rho_plus_3p_vacuum_w_minus1": sp_vacuum, "rho_plus_3p_dust_w0": sp_dust,
      "vacuum_repulsive": vacuum_repulsive, "matter_attractive": dust_attractive,
      "independent_of_spatial_K": independent_axes,
      "resolution": "candidate (b): spatial curvature (37) != vacuum-energy/Lambda (15); different axes; no contradiction",
      "type_error": "37.GM.5 compared a spatial-K sign with a spacetime-(rho+3p) sign -- 46 tells them apart"},
     check="rho+3p: vacuum(w=-1)=-2<0 repulsive, dust(w=0)=+1>0 attractive; independent of spatial K -> no contradiction")
assert fr3_ok

# ---- FR.4 what is NOT decided (held) -- POSTULATE --------------------------------------
step("FR.4", "what is NOT decided (held): WHICH the twelve are -- vacuum (15.C.3) or matter -- is a separate reading",
     "the resolution removes the CONTRADICTION (FR.3), not the READING: WHICH the twelve actually are -- "
     "vacuum/dark-energy (15.C.3) or matter-like -- is a SEPARATE question, not decided here. 15.C.3 "
     "survives, now uncontradicted by the focusing sign; candidate (a) is not thereby forced",
     ["FR.3", "15.C.3"],
     "the honest boundary of the resolution. FR.3 dissolves the tension: 37's spatial focusing and 15's "
     "vacuum reading are not in conflict (different operators). But that does NOT decide which the twelve "
     "ARE. 37.GM.5's candidate (a) was 'the twelve are matter not vacuum'; FR.3 shows (a) is NOT NEEDED "
     "to resolve the tension (b) does it), so (a) is not forced -- the twelve could be vacuum (15.C.3) "
     "with positive spatial curvature, consistently. Deciding vacuum-vs-matter is a reading that needs "
     "the stress-energy content (rho+3p for the twelve specifically) and the matter census -- held, and "
     "gated by the danger zone. So this container RESOLVES the sign tension and LEAVES the vacuum/matter "
     "reading open, uncontradicted. A held reading, quarantined; no downstream premise use.",
     "POSTULATE (which the twelve are -- vacuum or matter -- is a separate held reading, not decided)", "POSTULATE",
     {"resolves": "the contradiction (FR.3), via candidate (b)",
      "does_not_decide": "whether the twelve are vacuum (15.C.3) or matter (candidate a) -- a separate reading",
      "candidate_a_not_forced": "(a) is not needed to resolve the tension; the twelve may be vacuum with positive spatial K",
      "downstream_premise_use": False},
     check=None)

# ---- FR.5 OWED ------------------------------------------------------------------------
step("FR.5", "OWED: quantitative Raychaudhuri on the substrate (continuum + stress-energy = mass, danger); deciding vacuum-vs-matter (census)",
     "OWED: (a) the QUANTITATIVE Raychaudhuri focusing on the substrate -- needs the continuum (08.8.6) "
     "and a stress-energy tensor (rho+3p from the substrate), i.e. MASS -- the danger zone; (b) DECIDING "
     "vacuum-vs-matter for the twelve (15.C.3) -- a reading needing the matter census. The tension is "
     "resolved; the quantitative dynamics and the vacuum/matter reading are owed",
     ["FR.3", "FR.4"],
     "the honest residual. FR.1-FR.3 resolve the 37.GM.5 tension (a spatial/spacetime type error, "
     "dissolved by 46); FR.4 holds the vacuum/matter reading open. What remains: (a) the QUANTITATIVE "
     "Raychaudhuri equation on the substrate -- a real timelike congruence, its expansion theta, and "
     "R_{tt} from a substrate stress-energy -- which needs the continuum (08.8.6, not-a-rung) and a "
     "stress-energy tensor, hence MASS: the danger zone, not attempted; (b) DECIDING whether the twelve "
     "are vacuum or matter (15.C.3 / FR.4) -- needs the matter census and the equation of state at the "
     "twelve, a reading + danger. So the sign confusion is cleared (danger-free); the quantitative "
     "gravitational dynamics and the vacuum/matter determination are the forward, gated work. NOT "
     "attempted here.",
     "OWED (quantitative Raychaudhuri -- continuum+mass, danger; vacuum-vs-matter -- census)", "OWED",
     {"owed_quantitative": "the Raychaudhuri equation on the substrate -- needs the continuum + stress-energy (mass), danger zone",
      "owed_reading": "deciding vacuum-vs-matter for the twelve (15.C.3) -- the matter census, a reading + danger",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="47-focusing-resolution",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        twelve_deficit=twelve_deficit, spatial_focus_attractive=spatial_focus_attractive,
        rho_plus_3p_vacuum=sp_vacuum, rho_plus_3p_dust=sp_dust,
        vacuum_repulsive=vacuum_repulsive, matter_attractive=dust_attractive,
        finding="THE FOCUSING TENSION (37.GM.5) RESOLVED, using the signature (46). The tension: 37.GM.3 "
                "focuses (attractive) at the twelve (positive spatial deficit) but 15.C.3 reads them as "
                "vacuum (repulsive) (FR.1). Resolution -- candidate (b), now forced: the two are DIFFERENT "
                "operators -- 37's is SPATIAL Gaussian curvature K; gravitational attraction/repulsion is "
                "the SPACETIME Raychaudhuri focusing of the TIMELIKE congruence, dtheta/dtau ~ -(rho+3p), "
                "which needs 46's timelike direction (FR.2). The spacetime sign is rho+3p (vacuum w=-1: "
                "-2rho<0 repulsive; matter w=0: rho>0 attractive), INDEPENDENT of spatial K -- so positive "
                "spatial curvature and vacuum repulsion hold at once, NO contradiction (FR.3). The tension "
                "was a spatial/spacetime TYPE error, dissolved by 46. Which the twelve ARE (vacuum vs "
                "matter) stays a separate held reading (FR.4); the quantitative Raychaudhuri + the reading "
                "are OWED (FR.5, danger). Danger-free; nothing fitted.",
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
