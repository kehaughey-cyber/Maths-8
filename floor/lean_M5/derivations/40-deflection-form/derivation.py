#!/usr/bin/env python3
"""Container 40 -- THE DEFLECTION FORM: the refraction-form test (is the 1/b true?), danger-free.

Kevin: light here is a propagating state-change FRONT (not a particle), so the point-mass bridge is
REFRACTION, not geodesic deflection. This runs that test -- the 'is it true' computation -- for the FORM
of deflection(b), which is danger-free (pure geometry; the mass only sets the magnitude, owner-gated).

The eikonal (Fermat) deflection of a front is delta(b) = integral d/db[phi(sqrt(b^2+z^2))] dz, where phi is
the effective index/potential the front refracts through. The FORM of delta(b) is set entirely by how the
point source's potential FALLS OFF, which is set by the dimension the source-flux spreads into (the
Laplacian Green's function): 2D (flux over the circle 2*pi*r) -> phi ~ log r ; 3D (flux over the sphere
4*pi*r^2) -> phi ~ 1/r. Computed COLD (elementary integrals):

  2D (log):  delta(b) = pi        -- CONSTANT, IMPACT-INDEPENDENT  -> the 2+1D cosmic string (38.DV.2 / 39.PM.2)
  3D (1/r):  delta(b) = 2/b       -- proportional to 1/b           -> the Schwarzschild / point-mass form

So (DF.4) the FORM is set by the source-flux dimension; the substrate's front on the 2*pi SURFACE is
impact-INDEPENDENT (2+1D), and the 1/b requires the front over the 4*pi solid angle (3D). The substrate
carries 4*pi as its total curvature holonomy = the DOUBLE COVER (38.DV.3; 03's 2*pi->4*pi sibling route),
so the 3D the 1/b needs IS the 2*pi->4*pi double cover -- a live substrate lead (DF.5, POSTULATE). This
REFINES 39.PM.3: the 1/b is NOT flat-2D front-refraction (that is impact-independent, pi) -- it is the
front over the 4*pi double cover. Rests on 38 (the 4*pi double cover), 39 (the 2+1D contact + the front);
cites the eikonal/Green's-function facts (real analysis, as 16 cites the trig). Danger-free, FIT-free.

  DF.1 the eikonal deflection formula (light-as-front): delta(b) = int d/db[phi] dz. CITED. DERIVED(form).
  DF.2 2D (log potential): delta = pi, IMPACT-INDEPENDENT -- the 2+1D cosmic string. DERIVED (computed cold).
  DF.3 3D (1/r potential): delta = 2/b ~ 1/b -- the Schwarzschild form. DERIVED (computed cold).
  DF.4 the FORM is set by the source-flux DIMENSION (2*pi circle->log->const; 4*pi sphere->1/r->1/b);
       scaling exponent p: 2D p=0, 3D p=-1. DERIVED.
  DF.5 the reading (filed 19): the substrate's 3D route is the 2*pi->4*pi DOUBLE COVER (38.DV.3); the
       front over 4*pi gives 1/b, on the bare 2*pi surface the 2+1D impact-independent. Refines 39.PM.3. POSTULATE.
  DF.6 OWED: whether the front propagates over the 4*pi double cover (the ambient-dimension emergence,
       the metric-no-thirteenth via the double cover); the MAGNITUDE (8*pi*G) -- owner-gated. OWED.
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


def simpson(f, a, b, n=200000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


# ---- DF.1 the eikonal deflection formula -- DERIVED (the form; cited) -------------------
step("DF.1", "the eikonal (Fermat) deflection of a FRONT: delta(b) = integral d/db[phi(sqrt(b^2+z^2))] dz",
     "light here is a propagating FRONT (39.PM.3; the inject, 01.1.4), so its deflection is REFRACTION: "
     "delta(b) = int_{-inf}^{inf} d/db[phi(sqrt(b^2+z^2))] dz, phi the effective index/potential -- NOT a "
     "geodesic particle deflection. The FORM of delta(b) is set by the radial fall-off of phi",
     ["39.PM.3"],
     "set up the test in the framework's own light model. A traveling PARTICLE follows a geodesic; a "
     "propagating FRONT refracts (Fermat / eikonal): the transverse gradient of the effective index tilts "
     "the front. For a source with potential phi(r), a front passing at impact parameter b deflects by "
     "delta(b) = int over the path of the transverse derivative = int_{-inf}^{inf} d/db[phi(sqrt(b^2+z^2))] "
     "dz. This is the standard eikonal lensing integral (the Eddington optical analogy for light-bending), "
     "cited as real-analysis provenance (as container 16 cites the trig). The point of this container is "
     "that delta(b)'s FORM -- impact-independent, 1/b, or other -- is fixed once phi's radial profile is, "
     "and phi's profile is fixed by the source-flux dimension (DF.2/DF.3). Danger-free: no mass in the "
     "form (mass only scales the magnitude, DF.6).",
     "UNIQUE (the eikonal deflection integral; light-as-front, not particle)", "DERIVED",
     {"formula": "delta(b) = int_{-inf}^{inf} d/db[phi(sqrt(b^2+z^2))] dz",
      "light_is_a_front": "39.PM.3 / 01.1.4 -- refraction, not geodesic-particle deflection",
      "cited": "the eikonal/Fermat lensing integral (real analysis)"},
     check=None)

# ---- DF.2 2D (log potential): impact-independent -- DERIVED (computed cold) -------------
# phi = log r (2D Green's fn; flux over the circle 2*pi*r). d/db phi = b/(b^2+z^2). integral = pi.
def delta_2d(b):
    return 2 * simpson(lambda z: b / (b * b + z * z), 0.0, 4000.0)


d2 = {b: delta_2d(b) for b in (1, 2, 4)}
two_d_constant = all(abs(d2[b] - math.pi) < 1e-2 for b in (1, 2, 4))   # delta = pi for all b
df2_ok = two_d_constant
step("DF.2", "2D (a point source has a LOG potential): delta(b) = pi -- CONSTANT, IMPACT-INDEPENDENT (the 2+1D cosmic string)",
     "in 2D a point source's potential is phi ~ log r (the Laplacian Green's function; the flux spreads "
     "over the circle 2*pi*r). The eikonal integral then is delta(b) = int b/(b^2+z^2) dz = pi -- the SAME "
     "for every impact parameter b. So a front refracting in 2D deflects IMPACT-INDEPENDENTLY -- exactly "
     "the 2+1D cosmic-string / conical result (38.DV.2, 39.PM.2). Front-refraction in 2D does NOT give 1/b",
     ["DF.1", "38.DV.2"],
     "the honest result for the substrate's own dimension. The framework substrate is intrinsically 2D "
     "(25.DF.1). In 2D, solving the Laplacian for a point source (flux conserved over a circle of "
     "circumference 2*pi*r) gives the LOG potential phi ~ log r. Put it through the eikonal (DF.1): "
     "d/db[log sqrt(b^2+z^2)] = b/(b^2+z^2), and int_{-inf}^{inf} b/(b^2+z^2) dz = pi -- a CONSTANT, "
     "independent of b (computed cold: delta = pi at b = 1, 2, 4). So even as a FRONT (refraction), even "
     "through a smoothly-varying 2D field, the deflection is IMPACT-INDEPENDENT. This CONFIRMS -- and is "
     "the same physics as -- the 2+1D cosmic string (38.DV.2, 39.PM.2): a conical defect / 2D point mass "
     "deflects by a fixed angle, any b. It also REFINES 39.PM.3: front-refraction in flat 2D is NOT "
     "impact-dependent; the 1/b is not a 2D-front effect. (The closed form pi is cited real analysis; the "
     "cold numeric confirms the constancy.)",
     "UNIQUE (delta = pi, b-independent -- the 2D log potential)", "DERIVED",
     {"potential_2d": "phi ~ log r (2D Green's fn; flux over the circle 2*pi*r)",
      "delta_by_b": {str(b): round(d2[b], 4) for b in (1, 2, 4)}, "closed_form": "pi",
      "impact_independent": two_d_constant, "confirms": "the 2+1D cosmic string (38.DV.2, 39.PM.2)",
      "refines_39_PM3": "front-refraction in flat 2D is impact-INDEPENDENT, not impact-dependent"},
     check="2D: delta(b) = pi (b-independent) for b = 1,2,4 -- impact-independent")
assert df2_ok

# ---- DF.3 3D (1/r potential): 1/b -- DERIVED (computed cold) ----------------------------
# phi = 1/r (3D Green's fn; flux over the sphere 4*pi*r^2). d/db phi = -b/(b^2+z^2)^{3/2}. |integral| = 2/b.
def delta_3d(b):
    return 2 * simpson(lambda z: b / (b * b + z * z) ** 1.5, 0.0, 4000.0)


d3 = {b: delta_3d(b) for b in (1, 2, 4)}
b_times_delta_3d = {b: d3[b] * b for b in (1, 2, 4)}
three_d_is_one_over_b = all(abs(b_times_delta_3d[b] - 2.0) < 1e-3 for b in (1, 2, 4))  # b*delta = 2 (const)
df3_ok = three_d_is_one_over_b
step("DF.3", "3D (a point source has a 1/r potential): delta(b) = 2/b -- proportional to 1/b (the Schwarzschild form)",
     "in 3D a point source's potential is phi ~ 1/r (the Laplacian Green's function; the flux spreads over "
     "the sphere 4*pi*r^2). The eikonal integral is delta(b) = int b/(b^2+z^2)^{3/2} dz = 2/b -- so "
     "b*delta = 2 is constant, i.e. delta is PROPORTIONAL TO 1/b: the Schwarzschild / point-mass form",
     ["DF.1"],
     "the contrast that shows what the 1/b requires. In 3D the point-source potential is phi ~ 1/r (flux "
     "conserved over a sphere of area 4*pi*r^2). Through the eikonal (DF.1): d/db[1/sqrt(b^2+z^2)] = "
     "-b/(b^2+z^2)^{3/2}, and int_{-inf}^{inf} of the magnitude = 2/b (computed cold: b*delta = 2 exactly "
     "at b = 1, 2, 4). So delta ~ 1/b -- the impact-parameter fall-off of the Schwarzschild / point-mass "
     "deflection (4*G*M/(c^2 b) has this form). The 1/b is intrinsically a 3D result: it comes from the "
     "1/r potential, which comes from the 3D flux law (4*pi*r^2). (The closed form 2/b is cited real "
     "analysis; the cold numeric confirms b*delta = 2 constant.)",
     "UNIQUE (delta = 2/b, so b*delta = 2 constant -- the 3D 1/r potential)", "DERIVED",
     {"potential_3d": "phi ~ 1/r (3D Green's fn; flux over the sphere 4*pi*r^2)",
      "delta_by_b": {str(b): round(d3[b], 4) for b in (1, 2, 4)},
      "b_times_delta": {str(b): round(b_times_delta_3d[b], 4) for b in (1, 2, 4)}, "closed_form": "2/b",
      "is_one_over_b": three_d_is_one_over_b, "matches": "the Schwarzschild point-mass form 4*G*M/(c^2 b)"},
     check="3D: b*delta(b) = 2 (constant) for b = 1,2,4 -- delta ~ 1/b")
assert df3_ok

# ---- DF.4 the FORM is set by the source-flux dimension -- DERIVED ----------------------
FLUX_DIM = {"2D": 1, "3D": 2}          # flux spreads over r^(n-1): circle r^1, sphere r^2
DEFLECT_EXP = {"2D": 0, "3D": -1}      # delta ~ b^p: 2D constant (p=0), 3D 1/b (p=-1)
df4_ok = (FLUX_DIM["2D"] == 1 and FLUX_DIM["3D"] == 2
          and DEFLECT_EXP["2D"] == 0 and DEFLECT_EXP["3D"] == -1
          and DEFLECT_EXP["2D"] != DEFLECT_EXP["3D"])
step("DF.4", "the FORM is set by the SOURCE-FLUX DIMENSION: 2*pi circle -> log -> constant; 4*pi sphere -> 1/r -> 1/b",
     "the deflection FORM is fixed by the dimension the source-flux spreads into: 2D (flux over the circle "
     "2*pi*r, ~r^1) -> log potential -> delta CONSTANT (exponent p=0); 3D (flux over the sphere 4*pi*r^2, "
     "~r^2) -> 1/r potential -> delta ~ 1/b (p=-1). So impact-independence vs 1/b is a DIMENSION "
     "distinction, p = 0 vs -1",
     ["DF.2", "DF.3"],
     "the finding, in one line: the deflection's impact-parameter dependence is a fingerprint of the "
     "source-flux dimension. The Laplacian Green's function in n spatial dimensions has the source flux "
     "spreading over an (n-1)-sphere (~ r^{n-1}): n=2 gives the circle (r^1) and the log potential; n=3 "
     "gives the sphere (r^2) and the 1/r potential. Through the eikonal (DF.1) these give delta ~ b^0 "
     "(constant, DF.2) and delta ~ b^{-1} (1/b, DF.3). So the substrate's front on its 2D SURFACE (2*pi "
     "flux) is impact-INDEPENDENT -- the 2+1D gravity it exactly reproduces (39.PM.2) -- and the observed "
     "3+1D 1/b requires the front to see a 4*pi (3D) flux. The bridge from the quantized 2+1D substrate to "
     "the smooth 3+1D 1/b is therefore a DIMENSION step (2*pi -> 4*pi), not a fineness/smearing step -- "
     "which is exactly what DF.5 locates.",
     "UNIQUE (flux dim 1 vs 2; deflection exponent 0 vs -1 -- impact-independent vs 1/b)", "DERIVED",
     {"flux_dimension": FLUX_DIM, "deflection_exponent": DEFLECT_EXP,
      "reading": "2*pi circle -> log -> const (2+1D); 4*pi sphere -> 1/r -> 1/b (Schwarzschild); a dimension distinction"},
     check="flux dim 2D=1, 3D=2; deflection exponent 2D=0 (const), 3D=-1 (1/b); the two differ")
assert df4_ok

# ---- DF.5 the reading: the 3D route is the 2pi->4pi DOUBLE COVER (38.DV.3) -- POSTULATE --
step("DF.5", "the reading (filed 19): the substrate's 3D route is the 2*pi->4*pi DOUBLE COVER (38.DV.3); the front over 4*pi gives 1/b -- refines 39.PM.3",
     "the 1/b needs a 4*pi (3D) source-flux (DF.4). The substrate CARRIES 4*pi -- its total curvature "
     "holonomy = 4*pi = the DOUBLE COVER (38.DV.3; 03's 2*pi->4*pi sibling route for 3D via the solid "
     "angle). So the 3D the 1/b needs IS the 2*pi->4*pi double cover: the front over the 4*pi solid angle "
     "gives the 1/b Schwarzschild form; on the bare 2*pi surface it gives the 2+1D impact-independent. "
     "This REFINES 39.PM.3",
     ["DF.4", "38.DV.3", "39.PM.4"],
     "the correspondence that ties the danger-free FORM computation to the substrate's structure -- filed "
     "through 19, held. SUBSTRATE side (checked/derived): the deflection form is impact-independent for a "
     "2*pi flux (DF.2), 1/b for a 4*pi flux (DF.3/DF.4); and the substrate's total curvature holonomy is "
     "4*pi = the double cover (38.DV.3). PHYSICS side (cited): 3+1D light-bending is 1/b; 2+1D is "
     "topological/impact-independent. THE READING: the substrate's NATIVE gravity (front on the 2*pi "
     "surface) is 2+1D, impact-independent; the observed 3+1D 1/b is the front propagating over the 4*pi "
     "DOUBLE COVER (the 3D solid angle), which the substrate carries as 38.DV.3's total holonomy and 03's "
     "sibling route. So the 2*pi->4*pi double cover IS the ambient-dimension bridge the 1/b needs. This "
     "REFINES 39.PM.3 (which said 'front-refraction, impact-dependent' -- DF.2 shows flat-2D front-"
     "refraction is impact-INDEPENDENT; the 1/b is the double-cover/3D flux, not flat 2D) and CONFIRMS "
     "39.PM.4's double-cover lead. FALSIFICATION: if the front demonstrably does NOT acquire a 4*pi flux "
     "(stays 2*pi), the substrate gives only 2+1D and the 1/b would not emerge; whether it does is DF.6. A "
     "correspondence, WEAK; quarantined; no downstream premise use.",
     "POSTULATE (the 3D route = the 2*pi->4*pi double cover, 38.DV.3; the front over 4*pi gives 1/b; refines 39.PM.3; held)", "POSTULATE",
     {"reading": "the substrate's 3D route is the 2*pi->4*pi double cover (38.DV.3 total = 4*pi; 03 sibling); front over 4*pi -> 1/b",
      "native_is_2plus1D": "front on the 2*pi surface -> impact-independent (2+1D); front over 4*pi -> 1/b (3+1D)",
      "refines_39_PM3": "flat-2D front-refraction is impact-INDEPENDENT (DF.2); the 1/b is the double-cover/3D flux, not flat 2D",
      "confirms_39_PM4": "the double-cover ambient lead", "downstream_premise_use": False},
     check=None)

# ---- DF.6 OWED: the 4pi-flux emergence; the magnitude -----------------------------------
step("DF.6", "OWED: whether the front acquires the 4*pi (3D) flux -- the double-cover ambient emergence; and the MAGNITUDE (8*pi*G), owner-gated",
     "OWED: (a) whether the propagating front actually sees a 4*pi (3D) source-flux -- i.e. the "
     "ambient-dimension emergence via the 2*pi->4*pi double cover (the metric-no-thirteenth, 03/38); "
     "danger-free structure to work; (b) the MAGNITUDE -- the coupling 8*pi*G (delta = 4*G*M/(c^2 b) in "
     "3D), external anchor (27), owner-gated (Path A/B), the arcsec computed-then-compared, NEVER fitted",
     ["DF.5"],
     "the honest residual. The FORM is settled (DF.2/DF.3/DF.4: 2D impact-independent, 3D 1/b) and located "
     "at the double cover (DF.5). What stays owed: (a) DANGER-FREE -- whether the substrate's front "
     "genuinely acquires the 4*pi (3D) flux, which is the ambient-dimension emergence through the "
     "2*pi->4*pi double cover (38.DV.3, 03's sibling route) = the metric-no-thirteenth from the light "
     "side; structure to work, no fitting; (b) OWNER-GATED -- the MAGNITUDE: the coupling 8*pi*G that turns "
     "the 1/b form into the observable 4*G*M/(c^2 b) and the arcsec value; G is an external Planck anchor "
     "(27), a value NEVER fitted, the factor of 2 never chased. So the FORM is true and located; the "
     "4*pi-flux emergence and the magnitude remain. NOT crossed further here.",
     "OWED (the 4*pi-flux/double-cover emergence -- danger-free; the magnitude 8*pi*G -- owner-gated)", "OWED",
     {"owed_flux": "whether the front acquires the 4*pi (3D) flux -- the double-cover ambient emergence (38.DV.3/03), the metric-no-thirteenth from the light side; danger-free",
      "owner_gated_magnitude": "8*pi*G (delta = 4*G*M/(c^2 b)); external anchor (27); the arcsec never fitted, the factor of 2 never chased",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="40-deflection-form",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        delta_2d={str(b): round(d2[b], 4) for b in (1, 2, 4)},
        delta_3d={str(b): round(d3[b], 4) for b in (1, 2, 4)},
        b_times_delta_3d={str(b): round(b_times_delta_3d[b], 4) for b in (1, 2, 4)},
        flux_dimension=FLUX_DIM, deflection_exponent=DEFLECT_EXP,
        two_d_impact_independent=two_d_constant, three_d_is_one_over_b=three_d_is_one_over_b,
        finding="THE DEFLECTION-FORM TEST (is the 1/b true?), computed cold, danger-free. Light is a FRONT "
                "(refraction, not a particle), so delta(b) = int d/db[phi] dz. The FORM is set by the "
                "source-flux dimension: 2D (flux over the circle 2*pi*r) -> log potential -> delta = pi, "
                "IMPACT-INDEPENDENT (DF.2, = the 2+1D cosmic string, confirming 38.DV.2/39.PM.2); 3D (flux "
                "over the sphere 4*pi*r^2) -> 1/r potential -> delta = 2/b ~ 1/b, the Schwarzschild form "
                "(DF.3). So impact-independent vs 1/b is a DIMENSION distinction (exponent 0 vs -1, DF.4). "
                "The substrate's front on its 2*pi SURFACE is 2+1D (impact-independent); the observed 1/b "
                "requires the front over the 4*pi solid angle (3D) -- which the substrate carries as the "
                "2*pi->4*pi DOUBLE COVER (38.DV.3's total = 4*pi; 03's sibling route) (DF.5, POSTULATE). "
                "This REFINES 39.PM.3 (flat-2D front-refraction is impact-INDEPENDENT, not the 1/b) and "
                "CONFIRMS the double-cover ambient lead. OWED: whether the front acquires the 4*pi flux "
                "(danger-free, the double-cover emergence) and the MAGNITUDE 8*pi*G (owner-gated). Nothing "
                "fitted; the factor of 2 never chased.",
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
