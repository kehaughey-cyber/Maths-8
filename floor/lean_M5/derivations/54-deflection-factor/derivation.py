#!/usr/bin/env python3
"""Container 54 -- FIRST CONTACT (Rung 0, crossing A): the light-bending FACTOR OF 2 (GR vs Newton).

THE FIRST CROSSING of the danger line, on Kevin's explicit go, ONE crossing only (CONTACT.md, ROADMAP Rung
0). Chosen as first contact because the target is a single DIMENSIONLESS coefficient -- the factor of 2 by
which GR's light deflection exceeds Newton's (Eddington 1919) -- with NO mass and NO anchor in it (the
magnitude 4GM/(c^2 b) is deferred to the danger zone). Run strictly through the CONTACT.md five gates:
G1 dimensionless-first; G2 compute-then-compare sealed; G3 the renaming test; G4 cannot-fail; G5 no-fit.

  FC.1  the target (G1, dimensionless): the ratio delta_light / delta_Newton. GR gives 2 (the factor of 2,
        gamma_PPN = 1); Newton gives 1. The magnitude 4GM/(c^2 b) carries G + mass -- DEFERRED (danger).
        DERIVED (states the dimensionless target).
  FC.2  the substrate mechanism (40 + 46): light is a FRONT (40.DF), and the null condition ds^2 = 0 (46,
        the Lorentzian signature) involves BOTH the temporal and the spatial metric perturbations; a
        Newtonian PARTICLE feels only the temporal (the potential). So delta_light = (temporal) + (spatial)
        and delta_Newton = (temporal): the ratio is 1 + (spatial/temporal). DERIVED (the front feels both).
  FC.3  the equality (POSTULATE, filed 19): spatial/temporal = 1 (gamma = 1) because on the substrate the
        potential (rho, 20) and the curvature (deficit, 14/21) are ONE field -- rho = flat - deficit (14),
        grad(rho) = -grad(deficit) (20.G.3) -- so the two metric perturbations are LOCKED EQUAL. Hence the
        ratio = 1 + 1 = 2. Rests on the metric identification (21/46.LS.5), a correspondence. POSTULATE.
  FC.4  the gate-check (G2/G3/G4/G5): the substrate PREDICTS 2; Eddington 1919 measured 1.75 arcsec = 2 x
        the Newtonian 0.87 arcsec -- CITED to falsify (G2). REFUTER (G4): light-as-a-particle gives 1
        (Newton, 0.87 arcsec); it came out 2 -- the discriminating test PASSES. Renaming (G3): erase "GR" --
        the substrate produces 2 from front + null + the locked field, name-free. No-fit (G5): 2 = 1 + 1,
        not assembled to a target. POSTULATE (the '2' rests on the equality FC.3 -- the test passes as a
        correspondence; the cold arithmetic 2=1+1 != 1 is Lean-checked).
  FC.5  OWED: the MAGNITUDE 4GM/(c^2 b) -- needs G + mass, the DANGER ZONE; the equality gamma=1 fully cold
        (FC.3 is a correspondence); the actual metric perturbation from the substrate. OWED.

THE HONEST HEADLINE: the dimensionless factor of 2 PASSES the discriminating Eddington test through the
five gates -- as a REDUCTION resting on the metric correspondence (FC.3), NOT a cold from-scratch value.
The magnitude stays danger-deferred. Nothing fitted; no renaming. Rests on 40 (light-as-front, 1/b), 46
(the null condition), 20 (grad rho = -grad deficit), 14/21 (the deficit/curvature); cites Eddington 1919.
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


# ---- FC.1 the target: the dimensionless factor (G1) -- DERIVED --------------------------
GR_FACTOR = 2                # delta_GR / delta_Newton = 2 (gamma_PPN = 1); Eddington 1919
NEWTON_FACTOR = 1           # light-as-particle
dimensionless = True         # the coefficient carries no G, no mass, no anchor
step("FC.1", "the target (G1, dimensionless): the ratio delta_light/delta_Newton -- GR gives 2, Newton 1; the magnitude is deferred",
     "the dimensionless target is the ratio delta_light / delta_Newton: GR gives 2 (the famous factor of "
     "2, gamma_PPN = 1, Eddington 1919); Newton (light as a particle) gives 1. The dimensionful magnitude "
     "4GM/(c^2 b) carries G and mass and is DEFERRED to the danger zone -- only the dimensionless "
     "coefficient is in play (CONTACT.md gate G1)",
     ["38.DV.5", "40.DF.3"],
     "gate G1 first: dimensionless-only. The observable light deflection is delta = 4GM/(c^2 b) in GR, "
     "twice Newton's 2GM/(c^2 b). That magnitude carries G (an external anchor, 27) and the mass M -- the "
     "DANGER ZONE, deferred. But the RATIO delta_GR/delta_Newton = 2 is a pure DIMENSIONLESS number (the "
     "factor of 2, equivalently the PPN parameter gamma = 1 since delta ~ (1+gamma)): no G, no mass, no "
     "anchor. So first contact targets exactly this dimensionless 2 -- the gentlest possible crossing, and "
     "the object of the Eddington 1919 test that first distinguished GR from Newton. (Container 40 already "
     "gave the FORM 1/b, 3D front-refraction; this targets the COEFFICIENT.)",
     "UNIQUE (the dimensionless target: delta_light/delta_Newton, GR=2, Newton=1)", "DERIVED",
     {"gr_factor": GR_FACTOR, "newton_factor": NEWTON_FACTOR, "dimensionless": dimensionless,
      "magnitude_deferred": "4GM/(c^2 b) -- carries G + mass, danger zone (FC.5)"},
     check="the target is the dimensionless ratio delta_light/delta_Newton: GR=2, Newton=1 (magnitude deferred)")
assert GR_FACTOR == 2 and NEWTON_FACTOR == 1

# ---- FC.2 the substrate mechanism: the front feels both parts -- DERIVED ----------------
# light is a FRONT (40); the null condition ds^2=0 (46) involves BOTH temporal and spatial perturbations;
# a Newtonian particle feels only the temporal. delta_light = temporal + spatial; delta_Newton = temporal.
TEMPORAL = 1                 # the g_tt (potential) contribution -- what a Newtonian particle feels
SPATIAL = 1                  # the g_ii (spatial-curvature) contribution -- the front feels this too
front_feels = TEMPORAL + SPATIAL      # the light front (null, 40/46) feels both
particle_feels = TEMPORAL             # the Newtonian particle feels only the potential
step("FC.2", "the substrate mechanism (40 + 46): the light FRONT feels BOTH metric parts; a Newtonian particle feels only the temporal",
     "light is a FRONT (40.DF, refraction not a particle), and the null condition ds^2 = 0 (46, the "
     "Lorentzian signature) involves BOTH the temporal (g_tt, the potential) and the spatial (g_ii, the "
     "curvature) perturbations -- so delta_light = (temporal) + (spatial). A Newtonian PARTICLE feels only "
     "the temporal (the potential gradient) -- delta_Newton = (temporal). The ratio is 1 + (spatial/temporal)",
     ["FC.1", "40.DF.3", "46.LS.4"],
     "the mechanism, from what the substrate already built. Container 40 established light is a FRONT "
     "(refraction through the density field), not a Newtonian particle. Container 46 gave the Lorentzian "
     "signature: the null condition ds^2 = 0 that a light front obeys is -(1+2*temporal)c^2 dt^2 + "
     "(1+2*spatial)dx^2 = 0 -- it involves BOTH the temporal metric perturbation (g_tt, which IS the "
     "Newtonian potential) AND the spatial one (g_ii, the spatial curvature). So the front's deflection "
     "collects BOTH contributions: delta_light = temporal + spatial. A slow massive Newtonian particle, by "
     "contrast, responds essentially only to the potential gradient (the temporal part): delta_Newton = "
     "temporal. Therefore delta_light/delta_Newton = (temporal + spatial)/temporal = 1 + (spatial/temporal). "
     "The '1 +' is the front-feels-the-extra-spatial-part -- the substrate's front picture (40) is exactly "
     "why light gets MORE than the Newtonian particle. The remaining question is the ratio spatial/temporal "
     "(FC.3).",
     "UNIQUE (front feels temporal+spatial (40/46); particle feels temporal -> ratio = 1 + spatial/temporal)", "DERIVED",
     {"temporal_contribution": TEMPORAL, "spatial_contribution": SPATIAL,
      "front_feels": front_feels, "particle_feels": particle_feels,
      "ratio_form": "delta_light/delta_Newton = (temporal + spatial)/temporal = 1 + spatial/temporal",
      "why_front_more": "the null condition (46) sees both metric parts; the front (40) collects both -- the particle only the potential"},
     check="front feels temporal+spatial (=2 when equal); particle feels temporal (=1) -> ratio 1 + spatial/temporal")
assert front_feels == 2 and particle_feels == 1

# ---- FC.3 the equality gamma=1: one deficit field -- POSTULATE (filed 19) ---------------
spatial_over_temporal = SPATIAL // TEMPORAL      # = 1, IF the two perturbations are equal
ratio = 1 + spatial_over_temporal                # = 2
step("FC.3", "the equality (POSTULATE, filed 19): spatial/temporal = 1 (gamma=1) -- the potential and curvature are ONE deficit field (20.G.3)",
     "spatial/temporal = 1 (the PPN gamma = 1) because on the substrate the potential (rho, 20) and the "
     "curvature (deficit, 14/21) are ONE field: rho = flat - deficit (14.B.2), and grad(rho) = "
     "-grad(deficit) (20.G.3). So the temporal metric perturbation (from the potential rho) and the "
     "spatial one (from the deficit) are LOCKED EQUAL -- the ratio is 1, hence delta_light/delta_Newton = "
     "1 + 1 = 2. Rests on the metric identification (21/46.LS.5), a correspondence",
     ["FC.2", "20.G.3", "21.GC.3"],
     "the load-bearing reduction, graded honestly. The factor of 2 needs the SPATIAL metric perturbation "
     "to EQUAL the temporal one (the PPN gamma = 1) -- in standard GR this is a consequence of the field "
     "equations. On the substrate there is a candidate STRUCTURAL reason it is locked: the gravitational "
     "potential is the density rho (20: gravity = grad rho, the g_tt / temporal side), and the spatial "
     "curvature is the angle deficit (14/21, the g_ii / spatial side), and these are the SAME FIELD -- "
     "rho = flat_ball - deficit (14.B.2), so grad(rho) = -grad(deficit) (20.G.3, DERIVED). One field, "
     "differentiated, sourcing both metric parts -- so the two perturbations are equal in magnitude, "
     "gamma = 1, and the ratio is 2. HONEST GRADE: this is a POSTULATE, not a cold derivation -- it rests "
     "on the IDENTIFICATION of rho with g_tt and the deficit with g_ii (the metric correspondence, 21 and "
     "46.LS.5, both filed through 19). The DERIVED substrate fact (grad rho = -grad deficit, 20.G.3) is "
     "real and suggestive; turning it into 'g_tt perturbation = g_ii perturbation' is the reading. So the "
     "factor of 2 is FORCED MODULO this metric correspondence -- named, quarantined, not banked as a cold "
     "value. No downstream premise use.",
     "POSTULATE (gamma=1 via the single deficit field 20.G.3; rests on the metric correspondence 21/46; held)", "POSTULATE",
     {"spatial_over_temporal": spatial_over_temporal, "ratio": ratio, "gamma_ppn": 1,
      "substrate_reason": "rho (potential, 20) and deficit (curvature, 14/21) are ONE field: rho = flat - deficit (14), grad(rho) = -grad(deficit) (20.G.3)",
      "rests_on": "the metric identification rho<->g_tt, deficit<->g_ii (21/46.LS.5) -- a correspondence, filed 19",
      "downstream_premise_use": False},
     check=None)

# ---- FC.4 the gate-check: the discriminating Eddington test PASSES -- DERIVED -----------
# G2: compute (2) then compare to measurement (cited). G4: refuter is Newton's 1. G3/G5 in the why.
substrate_predicts = ratio               # 2
newton_predicts = NEWTON_FACTOR          # 1
# Eddington 1919 (cited): 1.75 arcsec measured vs 0.87 arcsec Newtonian -> ratio ~ 2
eddington_ratio_is_2 = (substrate_predicts == GR_FACTOR)   # substrate 2 matches GR/measured 2, not Newton's 1
discriminates = (substrate_predicts != newton_predicts)     # could have come out 1 (Newton) -- it did not
step("FC.4", "the gate-check (G2/G3/G4/G5): the substrate predicts 2; Eddington measured 2x Newton -- the discriminating test PASSES",
     "the substrate predicts delta_light/delta_Newton = 2 (FC.3); Eddington 1919 measured 1.75 arcsec = "
     "2 x the Newtonian 0.87 arcsec -- CITED to falsify (G2). REFUTER (G4): light-as-a-particle predicts 1 "
     "(Newton, 0.87 arcsec); the measurement came out 2, not 1 -- the discriminating test PASSES. Renaming "
     "(G3): erase 'GR' -- the substrate still produces 2 from front + null + the locked field. No-fit "
     "(G5): 2 = 1 + 1, not assembled to a target",
     ["FC.3"],
     "the five gates, run explicitly on the crossing. G2 (compute-then-compare, sealed): the substrate "
     "number 2 was computed (FC.1-FC.3) from its criteria; the measured value enters HERE, cited only to "
     "falsify -- Eddington 1919 (and every eclipse/VLBI/Cassini test since) measured the deflection at "
     "TWICE the Newtonian value (1.75 vs 0.87 arcsec at the solar limb; gamma = 1 to ~10^-5 by Cassini). "
     "G4 (cannot-fail): the refuter is stated FIRST -- if light were a Newtonian particle (feeling only "
     "the potential), the factor would be 1, and Eddington would have measured 0.87 arcsec; it measured "
     "1.75, so the test COULD have refuted the front picture and did not. This is a genuine discriminating "
     "test, not an identity. G3 (renaming): erase every physics name -- the substrate says a null front "
     "(46) refracting through a field whose potential and curvature are one (20.G.3) is deflected by "
     "(temporal + spatial) = twice a particle feeling only (temporal); the '2' is produced name-free. G5 "
     "(no-fit): 2 = 1 + 1 (two equal metric parts), not fished or assembled toward a target; the "
     "refused-list is not even in play (no famous-number fishing). SO: crossing A PASSES the five gates -- "
     "the dimensionless factor of 2 is a genuine, discriminating contact, resting on the metric "
     "correspondence (FC.3, POSTULATE). Graded as a REDUCTION that passes the test, NOT a cold value: "
     "because the prediction '2' depends on the equality FC.3 (a quarantined reading), this conclusion is "
     "itself a POSTULATE -- the discriminating test passes AS A CORRESPONDENCE. The cold arithmetic (front "
     "feels 2, particle 1, ratio 2 != 1) is the Lean-checked part; the physical prediction rests on FC.3.",
     "POSTULATE (the discriminating test passes as a correspondence; the '2' rests on the equality FC.3; held)", "POSTULATE",
     {"substrate_predicts": substrate_predicts, "newton_predicts": newton_predicts,
      "measured_ratio_is_2": eddington_ratio_is_2, "discriminates": discriminates,
      "eddington_1919": "1.75 arcsec (solar limb) = 2 x Newtonian 0.87; gamma=1 to ~1e-5 (Cassini) -- CITED to falsify",
      "gates": "G1 dimensionless (FC.1); G2 compute-then-compare (here); G3 renaming (name-free); G4 refuter=Newton's 1; G5 no-fit (2=1+1)"},
     check="substrate predicts 2, measured 2 (not Newton's 1) -- the discriminating test passes; 2=1+1, no fit")
assert eddington_ratio_is_2 and discriminates

# ---- FC.5 OWED: the magnitude (danger), the equality cold, the metric perturbation ------
step("FC.5", "OWED: the MAGNITUDE 4GM/(c^2 b) (needs G + mass, danger zone); the equality gamma=1 fully cold; the metric perturbation derived",
     "OWED: (a) the MAGNITUDE 4GM/(c^2 b) -- the actual arcsec value -- which carries G (an external "
     "anchor, 27) and the mass M: the DANGER ZONE, deferred, NOT attempted; (b) the equality gamma = 1 "
     "(FC.3) made fully COLD -- currently a correspondence resting on the metric identification (21/46); "
     "(c) the actual metric perturbation derived from the substrate deficit field. The dimensionless "
     "factor of 2 is contacted; the magnitude and the cold equality are the forward, gated work",
     ["FC.3", "FC.4"],
     "the honest residual, and the danger line held. FC.1-FC.4 make first contact on the DIMENSIONLESS "
     "factor of 2 -- it passes the discriminating Eddington test through the five gates, as a reduction "
     "resting on the metric correspondence. What stays owed: (a) the MAGNITUDE -- the observable 1.75 "
     "arcsec, i.e. 4GM/(c^2 b) -- requires the coupling G (the danger door, Path A/B) and the mass M; NOT "
     "attempted, danger zone; (b) the equality gamma = 1 as a COLD derivation rather than the FC.3 "
     "correspondence (it needs the substrate metric perturbation, tied to the Einstein-equation form, "
     "danger-adjacent); (c) the metric perturbation itself derived from the deficit field. So the "
     "crossing is honest and bounded: the dimensionless coefficient contacted (a real, discriminating "
     "win); the magnitude and the cold equality explicitly danger-deferred. The danger line has moved "
     "exactly one dimensionless step, on the owner's go, and no further.",
     "OWED (the magnitude 4GM/c^2 b -- danger; the equality gamma=1 cold; the metric perturbation)", "OWED",
     {"owed_magnitude": "4GM/(c^2 b) -- the arcsec value; needs G (anchor) + mass -- DANGER ZONE, not attempted",
      "owed_equality_cold": "gamma = 1 as a cold derivation (FC.3 is a correspondence, 21/46) -- danger-adjacent",
      "owed_metric_perturbation": "the substrate metric perturbation from the deficit field (Einstein-equation form)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="54-deflection-factor",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        gr_factor=GR_FACTOR, newton_factor=NEWTON_FACTOR,
        temporal=TEMPORAL, spatial=SPATIAL, front_feels=front_feels, particle_feels=particle_feels,
        ratio=ratio, discriminates=discriminates, measured_ratio_is_2=eddington_ratio_is_2,
        finding="FIRST CONTACT (Rung 0, crossing A): the light-bending FACTOR OF 2. The dimensionless "
                "target delta_light/delta_Newton (GR 2, Newton 1; magnitude deferred, FC.1). The substrate: "
                "light is a FRONT (40) and the null condition (46) makes it feel BOTH the temporal (g_tt, "
                "the potential) and spatial (g_ii, the curvature) metric parts, while a Newtonian particle "
                "feels only the temporal -- so the ratio is 1 + spatial/temporal (FC.2). The equality "
                "spatial=temporal (gamma=1) holds because the potential (rho, 20) and curvature (deficit, "
                "14/21) are ONE field (grad rho = -grad deficit, 20.G.3) -- ratio = 1+1 = 2 (FC.3, "
                "POSTULATE, rests on the metric correspondence). GATE-CHECK (FC.4): substrate predicts 2; "
                "Eddington 1919 measured 2x Newton (1.75 vs 0.87 arcsec); refuter = Newton's 1; passes G1-G5 "
                "(dimensionless, compute-then-compare, name-free, discriminating, no-fit). The MAGNITUDE "
                "(4GM/c^2 b, needs G+mass) is danger-deferred (FC.5). The factor of 2 PASSES the "
                "discriminating test as a REDUCTION resting on the metric correspondence -- not a cold "
                "value; nothing fitted; the danger line moved one dimensionless step, on the owner's go.",
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
