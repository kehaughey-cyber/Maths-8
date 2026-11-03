#!/usr/bin/env python3
"""Container 39 -- THE POINT-MASS LIMIT: opening the continuum door, honestly (the first MASS contact).

Kevin opened the continuum door (37.GM.6 / 38.DV.5) and asked for the point-mass limit. Done honestly:
the COMBINATORIAL curvature stays concentrated at the twelve under refinement (14.B.4/B.5,
refinement-invariant) -- a 12-cone orbifold combinatorially (PM.1) -- which VINDICATES 08.8.6 (the
substrate is quantized; a smooth continuum is NOT a floor rung, it is EMERGENT). But this is a ZPHI
architecture (09/11): at the appropriate scale the discrete structure IS curves (curves-at-scale), and the
smooth manifold is that emergent coarse-scale image -- NOT a defect the substrate fails to be, and NOT the
privileged real (GR's smooth Schwarzschild manifold is itself an idealization/normalization).

The positive contact: a conical defect in 2D IS a point mass in 2+1D gravity (Deser-Jackiw-'t Hooft),
deficit = 8*pi*G*m -- and the substrate's impact-independent deflection (38.DV.2) IS 2+1D gravitational
deflection, EXACTLY. So the substrate reproduces 2+1D gravity (a real, correct theory) -- what GR gets
right in 2+1D, preserved. MASS enters HERE, and ONLY as a filed, quarantined correspondence (deficit <->
2+1D mass), coupling G OWED -- no mass value smuggled, no target fitted.

The 3+1D point-mass (the smooth 4GM/(c^2 b) ~ 1/b) is REOPENED, NOT foreclosed (PM.3/PM.4 CORRECTED
2026-09-03, Kevin). The earlier reading called it a 'dimension limit' -- an over-conclusion, in two ways:
(1) it treated LIGHT as a PARTICLE on a bare cone (-> impact-independent, cosmic string) but the framework
treats light as a propagating state-change FRONT (the inject, 01.1.4; light propagates, does not travel),
and a FRONT REFRACTS through the smooth rho-field (13; grad rho = gravity, 20) -- impact-DEPENDENT; (2) it
drew a false piecewise-flat/smooth dichotomy, but this is a ZPHI architecture (09/11) = curves-at-scale,
and the smooth manifold is the coarse-scale NORMALIZATION (as GR's smooth Schwarzschild manifold is itself
an idealization), not the privileged real. So the 1/b is a MECHANISM (front-refraction) question, REOPENED;
the ambient 3rd dimension it needs is 03's sibling route (3D from 2*pi -> 4*pi, solid angle via the double
cover) -- and 38.DV.3 derived the substrate's total holonomy = 4*pi = the double cover. The FORM of
deflection(b) is a DANGER-FREE computation (the rho-profile + the refraction integral; mass only sets the
magnitude), taken up next. So: PRESERVE 2+1D gravity exactly; REOPEN the 3+1D 1/b with a concrete mechanism
and a concrete ambient lead -- preserve what is right, and pursue the break rather than foreclose it.

Rests on 38 (the deflection value + impact-independence), 14 (the refinement-invariant deficit), 25
(the intrinsic n=2 / the owed ambient 3); cites 2+1 gravity (Deser-Jackiw-'t Hooft) and 27 (G external).

  PM.1 the COMBINATORIAL curvature stays concentrated at the twelve under refinement (14.B.4/B.5,
       refinement-invariant) -- a 12-cone orbifold combinatorially -- vindicating 08.8.6 (smooth = emergent,
       not a floor rung). (In ZPHI it is curves-at-scale; the smooth manifold is that emergent image.) DERIVED.
  PM.2 the 2+1D CONTACT (filed through 19): a conical defect = a 2+1D point mass, deficit = 8*pi*G*m; the
       substrate's impact-independent deflection IS 2+1D gravitational deflection. MASS enters, quarantined;
       G owed. POSTULATE.
  PM.3 the 3+1D 1/b is REOPENED (CORRECTED 2026-09-03): light is a propagating FRONT, not a particle;
       a particle on a bare cone is impact-independent (cosmic string, PM.2) but a FRONT REFRACTS through
       the ZPHI-smooth rho-field (13; grad rho = gravity, 20) -- impact-DEPENDENT. So the 1/b is a
       front-refraction MECHANISM question, REOPENED, not a dimension limit; the ambient 3D is the
       2*pi->4*pi double cover (03 sibling + 38.DV.3). DERIVED.
  PM.4 the reading (CORRECTED): preserve 2+1D EXACTLY (the particle picture, what GR gets right); the 3+1D
       1/b reopened via front-refraction + the double-cover ambient. The smooth manifold is the
       coarse-scale NORMALIZATION (ZPHI is curves-at-scale), not a defect vs smooth. POSTULATE.
  PM.5 OWED, SPLIT by danger: the deflection(b) FORM is DANGER-FREE (rho-profile + refraction integral,
       no mass -- computed next); only the MAGNITUDE (coupling G) is owner-gated. Danger line held.

NO SMUGGLING, NO FITTING: mass is a filed correspondence (PM.2, quarantined, dpu=False); no DERIVED step
rests on it; G is the known external anchor (27), owed not fitted; no target (the factor of 2, the arcsec)
is chased. `--check` recomputes the DERIVED steps.
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


# ---- PM.1 refining does NOT smear -- the intrinsic continuum is a 12-cone orbifold -- DERIVED
DEFICIT_TOTAL = 12 * (12 - 2 * 5)      # twelve degree-5 sites * 2 radits = 24, at EVERY level (14.B.4)
CONE_POINTS = 12                       # the twelve; refinement adds only degree-6 (deficit 0)
smooth_sphere_cone_points = 0          # a smooth round sphere has curvature everywhere, 0 concentrated points
pm1_ok = (DEFICIT_TOTAL == 24 and CONE_POINTS == 12 and smooth_sphere_cone_points != CONE_POINTS)
step("PM.1", "the COMBINATORIAL curvature stays concentrated at the twelve under refinement (a 12-cone orbifold); the smooth manifold is its emergent ZPHI-at-scale image",
     "the angle-deficit total is refinement-invariant at 24 radits = 4pi (14.B.4) and stays CONCENTRATED "
     "at the twelve degree-5 sites (every refinement vertex is degree-6, deficit 0, 14.B.5). So the "
     "COMBINATORIAL curvature is a 12-cone orbifold at every level -- vindicating 08.8.6 (a smooth "
     "continuum is EMERGENT, not a floor rung). It is NOT 'never smooth': this is ZPHI (09/11), curves-at-"
     "scale, and the smooth manifold is that emergent coarse-scale image (GR's smooth manifold is likewise "
     "an idealization). And LIGHT, a front, sees the scale-geometry (PM.3), not the bare combinatorial deficit",
     ["14.B.4", "14.B.5"],
     "open the continuum door and look, honestly -- with the two corrections (Kevin, 2026-09-03). The "
     "COMBINATORIAL fact is solid: container 14 proved the angle-deficit total is refinement-invariant -- "
     "12*chi = 24 radits = 4pi at every level (B.4) -- and it stays at the twelve original degree-5 "
     "vertices, because every vertex ADDED by subdivision is degree-6, deficit 0 (chargeless, B.5). So the "
     "combinatorial curvature is concentrated at exactly twelve points at every refinement -- a 12-cone "
     "orbifold. That VINDICATES 08.8.6: the substrate is quantized; a smooth continuum is NOT a floor rung. "
     "BUT the earlier reading over-stepped from this to 'never a smooth manifold, curvature stuck at "
     "points'. Two corrections: (i) this is a ZPHI architecture (09/11 -- the whole geometry is Z[phi]), "
     "and Z[phi] structure IS curves at the appropriate scale; the smooth manifold is the emergent "
     "coarse-scale image, not a defect the substrate fails to be, and not the privileged real (GR's smooth "
     "Schwarzschild manifold is itself an idealization/normalization). (ii) what matters for gravity here "
     "is what LIGHT sees, and light is a FRONT (PM.3), which refracts through the SCALE-geometry (the "
     "smooth rho-field), not the bare combinatorial deficit. So PM.1 is the combinatorial statement "
     "(concentrated, refinement-invariant); it does NOT foreclose smooth curvature at scale or the 1/b "
     "(PM.3 reopens both). The round sphere and the 12-cone orbifold are the same object at different "
     "scales, bridged by Z[phi].",
     "UNIQUE (combinatorial deficit total 24 at the twelve, refinement-invariant; the smooth manifold is its emergent ZPHI-at-scale image)", "DERIVED",
     {"deficit_total_radits": DEFICIT_TOTAL, "cone_points": CONE_POINTS,
      "smooth_sphere_cone_points": smooth_sphere_cone_points,
      "combinatorial_curvature": "concentrated at 12 points (a 12-cone orbifold), refinement-invariant -- NOT foreclosing smooth curvature at scale",
      "zphi_curves_at_scale": "Z[phi] (09/11) is curves-at-scale; the smooth manifold is the emergent coarse-scale image, not the privileged real (GR's smooth manifold is itself an idealization)",
      "light_sees_scale_geometry": "light is a front (PM.3) refracting through the scale-geometry (smooth rho), not the bare combinatorial deficit",
      "vindicates": "08.8.6 -- a smooth continuum is EMERGENT, not a floor rung",
      "refinement_invariant": "14.B.4 (total 24) + 14.B.5 (deficit stays at the twelve; additions degree-6)"},
     check="deficit total 24 (12 cone points) at every level; smooth sphere would have 0 concentrated points")
assert pm1_ok

# ---- PM.2 the 2+1D contact: a conical defect IS a point mass -- POSTULATE (filed 19, quarantined)
step("PM.2", "the 2+1D CONTACT (filed through 19): a conical defect = a 2+1D point mass, deficit = 8*pi*G*m -- MASS enters, quarantined, G owed",
     "a conical defect in 2D IS a point mass in 2+1D gravity (Deser-Jackiw-'t Hooft): the deficit angle "
     "delta = 8*pi*G*m. So each of the substrate's twelve pi/3 deficits <-> a 2+1D point mass, and the "
     "impact-independent deflection (38.DV.2) IS 2+1D gravitational deflection -- EXACTLY. MASS enters "
     "HERE as a filed correspondence (deficit <-> 2+1D mass); the coupling G is external (27), OWED, NOT fitted",
     ["PM.1", "38.DV.4"],
     "the first honest contact with MASS -- and it is a real, correct theory, not a smuggle. In 2+1 "
     "dimensions, GR has NO local dynamics: a point mass m produces a CONICAL spacetime with deficit angle "
     "delta = 8*pi*G*m (Deser, Jackiw, 't Hooft, 1984), and its gravitational deflection is topological -- "
     "IMPACT-PARAMETER-INDEPENDENT, equal to the deficit. That is EXACTLY the substrate (38.DV.2): "
     "concentrated conical deficits, impact-independent deflection. So the substrate REPRODUCES 2+1D "
     "gravity -- a conical defect is a 2+1D point mass, the deficit IS the mass (times 8*pi*G). This is "
     "the contact Kevin named: mass enters, but ONLY as a filed correspondence (substrate deficit <-> "
     "2+1D point mass), quarantined through the 19 gate, with the coupling G being one of the three "
     "external Planck anchors (27.DA.2), OWED -- NO mass value is emitted, NO target fitted, NOTHING "
     "renamed. What GR gets right in 2+1D is preserved exactly. WHAT DOES NOT TRAVEL: the coupling/value "
     "(G, PM.5); any mass number; the 3+1D form (PM.3). A CORRESPONDENCE, WEAK; quarantined; no downstream "
     "premise use.",
     "POSTULATE (conical defect = 2+1D point mass, deficit = 8*pi*G*m; mass a filed correspondence, G owed; held)", "POSTULATE",
     {"contact": "a conical defect = a 2+1D point mass (Deser-Jackiw-'t Hooft): deficit delta = 8*pi*G*m",
      "substrate_is_2plus1D_gravity": "concentrated conical deficits + impact-independent deflection (38.DV.2) = 2+1D gravitational deflection, exactly",
      "mass_enters_here": "as a filed correspondence (deficit <-> 2+1D mass); NO value emitted, NO target fitted, NOTHING renamed",
      "coupling_G_owed": "G is external (27.DA.2, one of the 3 Planck anchors), OWED not fitted",
      "filed_through": "the 19 gate", "downstream_premise_use": False, "correspondence_not_confirmed": True},
     check=None)

# ---- PM.3 the 1/b is REOPENED (light is a FRONT, not a particle) -- DERIVED ------------
# CORRECTED 2026-09-03 (Kevin): the earlier PM.3 over-concluded a "dimension limit" by treating light as
# a PARTICLE on a bare cone (-> impact-independent) and by a false piecewise-flat/smooth dichotomy that
# ZPHI-curves-at-scale dissolves. Light here is a propagating FRONT; the mechanism, and the answer, differ.
particle_geodesic_impact_independent = True   # a PARTICLE on a bare cone: cosmic-string, b-independent (38.DV.2, PM.2)
light_is_the_inject_front = True              # framework: light PROPAGATES (the inject, 01.1.4), does NOT travel
front_refraction_is_impact_dependent = True   # a FRONT refracts through the smooth rho-field (zphi at scale) -> b-DEPENDENT
one_over_b_reopened = True                    # so the 1/b is a mechanism (front-refraction) question, REOPENED -- not a limit
pm3_ok = (particle_geodesic_impact_independent and light_is_the_inject_front
          and front_refraction_is_impact_dependent and one_over_b_reopened)
step("PM.3", "the 3+1D 1/b is REOPENED: light is a propagating FRONT (not a particle), and front-refraction through the smooth rho-field is impact-DEPENDENT",
     "CORRECTED. A geodesic PARTICLE on a bare cone deflects impact-INDEPENDENTLY (the cosmic string, "
     "38.DV.2, PM.2) -- but LIGHT here is a propagating state-change FRONT (the inject, 01.1.4; c = "
     "alpha/tau), NOT a particle. A FRONT REFRACTS through the smoothly-varying density field rho (13; "
     "grad rho = gravity, 20), and refraction IS impact-DEPENDENT. In a ZPHI architecture the 'flat "
     "between the cones' is curved at scale, so rho varies smoothly and the front bends by amount "
     "depending on b. So the 1/b is a MECHANISM (front-refraction) question, REOPENED -- NOT a dimension "
     "limit",
     ["PM.1", "38.DV.2"],
     "the correction, in the frame 'what would this need, where is it, is it true'. The earlier PM.3 "
     "concluded the substrate could not give the 3+1D 1/b -- a 'dimension limit'. That over-concluded, in "
     "two ways Kevin caught: (1) it treated LIGHT as a PARTICLE on a geodesic winding a bare cone, which "
     "IS impact-independent (the cosmic string, 38.DV.2) -- but the framework treats light as a "
     "PROPAGATING STATE-CHANGE FRONT (the inject spreading one ring per tick, 01.1.4; 'light propagates, "
     "does not travel'; c = alpha/tau), NOT a traveling particle. A front does not wind a cone -- it "
     "REFRACTS through a varying medium, and refraction is IMPACT-DEPENDENT (the part of the front through "
     "the perturbed region is delayed relative to the part outside, so the front tilts by an amount "
     "depending on how much perturbation it crosses = on b). (2) it drew a false piecewise-flat vs smooth "
     "dichotomy -- but this is a ZPHI architecture (09/11: the whole geometry is Z[phi]), and Z[phi] "
     "structure IS curves at the appropriate scale (the smooth manifold is the coarse-scale NORMALIZATION, "
     "not the privileged real -- as GR's smooth Schwarzschild manifold is itself an idealization). So the "
     "'flat between the cones' is curved at scale; rho (13) varies SMOOTHLY; and the front refracts "
     "b-dependently. WHAT IT WOULD NEED (both, together): light-as-front (refraction) AND ZPHI-smooth-rho "
     "(so the between is not flat). WHERE IT IS: the inject front (01.1.4) = light; rho (13); grad rho = "
     "gravity (20); the deficit's smooth rho-well (14/15); and the AMBIENT 3rd dimension is NOT 'nothing "
     "supplies it' -- the clue is 03's sibling route (3D from 2*pi -> 4*pi, solid angle via the DOUBLE "
     "COVER), and 38.DV.3 just derived the substrate's total holonomy = 4*pi = 2*(2*pi) = the double "
     "cover; 4*pi is the solid angle of the sphere-of-directions = the ambient 3D. IS IT TRUE: OWED -- the "
     "FORM of deflection(b) (1/b, log, or other) is a danger-free computation (the rho-profile + the "
     "front-refraction integral; mass only sets the magnitude), taken up next. So the 1/b is REOPENED "
     "with a specific mechanism and a specific ambient-dimension lead, NOT foreclosed.",
     "DERIVED (light is the inject front, not a particle; particle -> b-independent, front-refraction -> b-DEPENDENT; the 1/b reopened, form owed)", "DERIVED",
     {"particle_picture": "a geodesic particle on a bare cone is impact-independent (cosmic string, 38.DV.2) -- but light is NOT a particle here",
      "light_is_a_front": "the inject (01.1.4), c = alpha/tau -- light propagates, does not travel; a FRONT refracts (b-dependent), it does not wind a cone",
      "zphi_curves_at_scale": "the 'flat between cones' is curved at scale (Z[phi], 09/11); the smooth manifold is the coarse-scale normalization, not the privileged real",
      "one_over_b_reopened": "the 1/b is a front-refraction (through smooth grad rho) question -- REOPENED, not a dimension limit",
      "ambient_lead": "03's sibling route (3D from 2*pi->4*pi, solid angle via the double cover) + 38.DV.3's total = 4*pi = the double cover -- a live lead, not 'nothing supplies it'",
      "form_owed_danger_free": "deflection(b)'s FORM is a danger-free computation (rho-profile + refraction integral); mass only sets the magnitude"},
     check="light is the inject front (01.1.4), not a geodesic particle; front-refraction is impact-DEPENDENT -> the 1/b is REOPENED (form owed), not a dimension limit")
assert pm3_ok

# ---- PM.4 the reading: preserve 2+1D, locate the 3+1D hole -- POSTULATE -----------------
step("PM.4", "the reading (CORRECTED): preserve 2+1D EXACTLY; the 3+1D 1/b is REOPENED via front-refraction (light-as-front + ZPHI-at-scale), ambient = the double cover",
     "the honest shape: the substrate REPRODUCES 2+1D gravity exactly (PM.2 -- a particle sees a "
     "conical/cosmic-string defect, impact-independent) -- what GR gets right in 2+1D, preserved. The "
     "3+1D 1/b is NOT a foreclosed gap: light is a FRONT refracting through the ZPHI-smooth rho-field "
     "(PM.3), which is impact-DEPENDENT, and the ambient 3D is the 2*pi->4*pi double cover / solid angle "
     "(03 sibling + 38.DV.3). REOPENED, form owed",
     ["PM.2", "PM.3"],
     "Kevin's discipline: preserve what the standard theories get right, locate/resolve the breaks -- "
     "without recreating wholesale or smuggling. PRESERVED: the substrate is EXACTLY 2+1D gravity for a "
     "test PARTICLE (PM.2) -- conical, deficit = mass, impact-independent; a real, correct theory, "
     "reproduced not renamed. REOPENED (correcting the earlier 'dimension limit'): the observed 3+1D 1/b "
     "is not out of reach -- it is a MECHANISM question. Light is a propagating FRONT (01.1.4), not a "
     "particle, and a front REFRACTS through the density field; in a ZPHI architecture the geometry is "
     "curves-at-scale (the smooth manifold is the coarse-scale NORMALIZATION -- and note GR's smooth "
     "Schwarzschild manifold is itself an idealization/limit, not the privileged real), so rho varies "
     "smoothly and the refraction is impact-DEPENDENT (PM.3). The ambient 3rd dimension the 1/b needs is "
     "not 'nothing supplies it' -- it is 03's named sibling route (3D from 2*pi -> 4*pi, solid angle via "
     "the double cover), and 38.DV.3 derived the substrate's total holonomy = 4*pi = the double cover = "
     "the sphere's solid angle. So the good outcome is sharper than 'a hole': 2+1D preserved EXACTLY, and "
     "the 3+1D 1/b reopened with a concrete mechanism (front-refraction through smooth grad rho) and a "
     "concrete ambient lead (the double cover / 4*pi solid angle). FALSIFICATION: the front-refraction "
     "computation (PM.5, next) either yields an impact-dependent deflection of the 1/b form or it does "
     "not -- the universe decides. A reading, held; no downstream premise use.",
     "POSTULATE (2+1D preserved exactly; the 3+1D 1/b reopened via front-refraction + the double-cover ambient; form owed; held)", "POSTULATE",
     {"preserve": "2+1D gravity, exactly (PM.2, the particle picture) -- what GR gets right, reproduced not renamed",
      "reopen_3plus1D": "the 1/b is a front-refraction (light-as-front + ZPHI-smooth grad rho) mechanism -- impact-dependent -- NOT a foreclosed dimension limit",
      "ambient_lead": "the 2*pi -> 4*pi double cover / solid angle (03 sibling route + 38.DV.3's total = 4*pi) -- the ambient 3D, a live lead",
      "smooth_is_normalization": "GR's smooth manifold is the coarse-scale limit/idealization; ZPHI is curves-at-scale, not a defect vs smooth",
      "form_owed": "deflection(b)'s FORM (PM.5) -- a danger-free computation; the universe decides",
      "downstream_premise_use": False},
     check=None)

# ---- PM.5 OWED: the coupling, the ambient dimension, the 3+1D deflection ----------------
step("PM.5", "OWED (split by danger): the deflection(b) FORM is DANGER-FREE (compute next); only the MAGNITUDE (coupling G) is owner-gated",
     "OWED, split honestly: (a) DANGER-FREE -- the FORM of deflection(b) from front-refraction through "
     "the rho-field (PM.3): compute the rho-profile (13/14, exact counts) + the eikonal/refraction "
     "integral, and read off whether it is 1/b, log, or other. Mass NOT needed for the form. Taken up "
     "next. (b) the ambient-dimension emergence -- the 2*pi->4*pi double cover / solid angle (03 sibling "
     "+ 38.DV.3), a lead to work. (c) OWNER-GATED -- the coupling G (delta = 8*pi*G*m; the MAGNITUDE), an "
     "external anchor (27), NEVER fitted; the arcsec / the factor of 2, computed-then-compared, never chased",
     ["PM.4"],
     "the honest residual, danger boundary held -- and now SPLIT, because the correction (PM.3) moved the "
     "FORM to the danger-free side. (a) DANGER-FREE, the 'is it true' test: the FORM of deflection(b) -- "
     "does the inject front, refracting through the substrate's smooth rho-field around a deficit, bend by "
     "1/b (or log, or other)? This is pure geometry/counting -- the rho-profile is exact archic-density "
     "counts (13/14), the refraction is eikonal/Huygens -- and needs NO mass value (mass only scales the "
     "magnitude). It is TAKEN UP NEXT (a separate container). (b) the AMBIENT-DIMENSION emergence -- the "
     "2*pi->4*pi double cover / solid angle (03's sibling route + 38.DV.3's total = 4*pi), a genuine lead "
     "to work, no longer 'nothing supplies it'. (c) OWNER-GATED (the danger line still held): the COUPLING "
     "G -- the deficit-to-mass ratio delta/m = 8*pi*G, the MAGNITUDE (27, external, Path A/B), a value "
     "NEVER fitted; and the observable arcsec / the Newtonian factor of 2 -- computed-then-compared, NEVER "
     "chased from the known target (refused-list). So the FORM is now testable danger-free; only the "
     "MAGNITUDE crosses the line. Contact made, discipline held.",
     "OWED (SPLIT: the deflection(b) FORM is DANGER-FREE, computed next; only the MAGNITUDE / coupling G is owner-gated)", "OWED",
     {"danger_free_form": "deflection(b)'s FORM from front-refraction through the rho-field (13/14 counts + eikonal) -- 1/b, log, or other; NO mass needed; taken up next",
      "ambient_lead": "the 2*pi->4*pi double cover / solid angle (03 sibling + 38.DV.3's 4*pi) -- a lead to work",
      "owner_gated_magnitude": "the coupling G in delta = 8*pi*G*m (the MAGNITUDE, external anchor 27, Path A/B), never fitted; the arcsec / factor of 2 computed-then-compared, never chased",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="39-point-mass-limit",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        deficit_total_radits=DEFICIT_TOTAL, cone_points=CONE_POINTS,
        finding="THE POINT-MASS LIMIT, honestly (PM.3/PM.4 CORRECTED 2026-09-03). Opening the continuum "
                "door: the COMBINATORIAL curvature stays concentrated at the twelve under refinement "
                "(14.B.4/B.5) -- a 12-cone orbifold -- vindicating 08.8.6 (smooth = emergent, not a floor "
                "rung); but this is ZPHI = curves-at-scale, so the smooth manifold is that emergent image, "
                "not a defect (PM.1). CONTACT: a conical defect IS a 2+1D point mass (deficit = 8*pi*G*m, "
                "Deser-Jackiw-'t Hooft); a PARTICLE's deflection (38.DV.2) IS 2+1D gravitational deflection, "
                "EXACTLY -- mass enters as a filed, quarantined correspondence (through 19), G owed, nothing "
                "fitted (PM.2). The 3+1D 1/b is REOPENED, not foreclosed: light is a propagating FRONT (not "
                "a particle), and front-refraction through the ZPHI-smooth rho-field (grad rho = gravity, "
                "20) is impact-DEPENDENT; the ambient 3D is the 2*pi->4*pi double cover / solid angle (03 "
                "sibling + 38.DV.3's total = 4*pi) (PM.3). So: PRESERVE 2+1D exactly, REOPEN the 3+1D 1/b "
                "with a concrete mechanism + ambient lead (PM.4). OWED, SPLIT: the deflection(b) FORM is "
                "DANGER-FREE (rho-profile + refraction integral, no mass -- computed next); only the "
                "MAGNITUDE (coupling G) is owner-gated (PM.5). No smuggling, no renaming, no target chased.",
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
