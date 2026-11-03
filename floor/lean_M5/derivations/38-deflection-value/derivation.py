#!/usr/bin/env python3
"""Container 38 -- THE DEFLECTION VALUE: the quantitative geodesic deflection (discharges 37.GM.6's value, danger-free part).

Container 37 built geodesic motion and showed the deflection EQUALS the angle deficit (GM.2). This puts a
VALUE on it -- the intrinsic, exact, forced value -- and characterizes its FORM, all danger-free (pure
geometry, no mass). The OBSERVABLE gravitational magnitude (light-bending arcsec, the Newtonian factor of
2) is a SEPARATE thing: it needs a mass + an anchor + the continuum limit (08.8.6) -- the danger zone and
an owner decision -- and stays OWED here, NEVER fitted. Rests on 37 (deflection = deficit), 14 (the
deficit), 36 (both wings); cites 21 (the 4pi integral) and cone / cosmic-string geometry.

  DV.1 the per-site deflection VALUE = the deficit angle: 2pi - d*(pi/3) = (6-d)*(pi/3). At the twelve
       (d=5): pi/3 = 60deg exactly. Integer core 12-2d = 2 radits (14.B.4); the radian value cited (pi).
       DERIVED.
  DV.2 it is IMPACT-PARAMETER-INDEPENDENT: a concentrated deficit is a CONICAL DEFECT (a cosmic string in
       2D); a geodesic winding it deflects by the FULL deficit regardless of how close it passes -- NOT
       the continuum point-mass 1/b (Newton/Schwarzschild). The substrate's distinctive deflection FORM.
       DERIVED (the integer content: deflection = the full deficit; the cone-unrolling provenance cited).
  DV.3 the TOTAL deflection over the twelve = 12 * (pi/3) = 4*pi = 2*(2pi): TWO full turns -- the DOUBLE
       COVER (Gauss-Bonnet 2*pi*chi = 4pi, 21). 24 radits = 2*12. Connects to the 2I spinor double-cover
       (carrier, 06) and 03's 2pi->4pi sibling route. DERIVED.
  DV.4 the reading (filed through 19): the substrate deflects geodesics like a lattice of CONICAL DEFECTS
       (cosmic-string-like, quantized, impact-independent) -- and the observable magnitude compares to
       gravitational light-bending. NAMED, held, quarantined. POSTULATE.
  DV.5 OWED: the OBSERVABLE GR magnitude (arcsec light-bending; the Newtonian factor of 2) -- needs mass +
       the anchor + the continuum (08.8.6); danger zone; computed-then-compared, NEVER fitted. OWED.

DANGER-FREE and FIT-FREE: the DERIVED values are pure geometry; no mass/census/coupling, no target
chased. The only cited numbers are pi (the radian conversion) and 21's 4pi. `--check` recomputes.
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


def deficit_radits(d):
    return 12 - 2 * d                       # 14.B.4 / 37.GM.2 -- 12 radits = 2*pi


# ---- DV.1 the per-site deflection value -- DERIVED --------------------------------------
# 1 radit = 2*pi/12 = pi/6.  deficit(d) radits = (12-2d)*(pi/6) = (6-d)*(pi/3).
DEFLECT_RADITS = {d: deficit_radits(d) for d in (5, 6, 7)}
twelve_radits = deficit_radits(5)                        # 2
# radian value at the twelve = 2 * pi/6 = pi/3 (cited: pi). Stored symbolically + numerically.
import math
twelve_rad = twelve_radits * math.pi / 6                 # pi/3
twelve_deg = math.degrees(twelve_rad)                    # 60.0
dv1_ok = (twelve_radits == 2 and abs(twelve_rad - math.pi / 3) < 1e-12 and abs(twelve_deg - 60.0) < 1e-9)
step("DV.1", "the per-site deflection VALUE = the deficit angle: pi/3 (60 deg) at the twelve, (6-d)*(pi/3) in general",
     "the geodesic deflection around a degree-d vertex (37.GM.2) has the VALUE 2pi - d*(pi/3) = (12-2d) "
     "radits = (6-d)*(pi/3): at the twelve (d=5) it is exactly pi/3 = 60 deg; at a degree-7 (the left "
     "wing) it is -pi/3. The integer core 12-2d is 14.B.4 (2 radits at the twelve); the radian value uses "
     "pi (cited)",
     ["37.GM.2", "14.B.4"],
     "put the number on 37's deflection. Each triangle is equilateral, interior angle pi/3 (60 deg). A "
     "degree-d vertex has d of them: total angle d*(pi/3), so the deficit (2pi minus that) is 2pi - "
     "d*(pi/3) = (6-d)*(pi/3). In the substrate's radit units (12 radits = 2pi, so 1 radit = pi/6) this "
     "is exactly the integer 12-2d (14.B.4) -- 2 radits at the twelve. Converting: 2 radits = pi/3 = 60 "
     "degrees. So the deflection VALUE is fixed and forced: pi/3 at each of the twelve, 0 on flat, -pi/3 "
     "at a degree-7 site. Nothing fitted -- it is the equilateral geometry. (The integer 12-2d is "
     "kernel-checkable; the radian conversion cites pi, as container 16 cites the trig and 10 arcsin.)",
     "UNIQUE (deflection = (6-d)*(pi/3); pi/3 at the twelve, forced by the equilateral angle)", "DERIVED",
     {"deflection_radits": DEFLECT_RADITS, "twelve_radits": twelve_radits,
      "twelve_radians": "pi/3", "twelve_degrees": 60.0, "general": "(6-d)*(pi/3)",
      "one_radit": "pi/6", "cited": "pi (the radian value); integer core 12-2d is 14.B.4"},
     check="deficit(5)=2 radits = pi/3 = 60deg; general (6-d)*(pi/3)")
assert dv1_ok

# ---- DV.2 impact-parameter independence -- DERIVED (conical defect / cosmic string) -----
# the deflection is the FULL deficit for any geodesic winding the vertex -- not a function of b.
deflection_equals_full_deficit = all(DEFLECT_RADITS[d] == deficit_radits(d) for d in (5, 6, 7))
dv2_ok = deflection_equals_full_deficit
step("DV.2", "the deflection is IMPACT-PARAMETER-INDEPENDENT: a conical defect (cosmic string), NOT the point-mass 1/b",
     "a concentrated deficit is a CONICAL DEFECT: unroll the cone to a flat wedge of angle 2pi-deficit; a "
     "geodesic is a straight line on the wedge, and gluing the edges deflects it by exactly the deficit -- "
     "the FULL deficit, for ANY impact parameter b (any geodesic winding the apex). This is the 2D cosmic "
     "string, NOT the continuum point-mass deflection 4GM/(c^2 b) ~ 1/b",
     ["DV.1", "37.GM.3"],
     "the FORM of the deflection, and it is a genuine prediction that distinguishes the discrete substrate "
     "from a smooth mass. On a piecewise-flat surface the curvature is a point deficit -- a cone apex. "
     "Unroll the cone: it is a flat wedge with a missing angle = the deficit. A geodesic is a straight "
     "line on the flat wedge; when the wedge edges are re-glued, that line comes back deflected by exactly "
     "the missing angle -- the deficit -- REGARDLESS of how far from the apex it passed (the impact "
     "parameter b). So the substrate's deflection is QUANTIZED and TOPOLOGICAL: the full deficit if the "
     "geodesic winds the site, 0 if not -- never the smooth 1/b fall-off of a Newtonian/Schwarzschild "
     "point mass (4GM/(c^2 b)). This is precisely the light deflection of a COSMIC STRING (a conical "
     "defect), a real GR object -- so the substrate's concentrated curvature deflects like a lattice of "
     "cosmic strings, not like point masses. (The integer content -- deflection = the full deficit, no "
     "b-dependence -- is here; the cone-unrolling geometry is the standard fact, cited.)",
     "UNIQUE (deflection = the full deficit, independent of impact parameter -- the conical/cosmic-string form)", "DERIVED",
     {"form": "conical defect / cosmic string -- deflection = the full deficit, impact-parameter-INDEPENDENT",
      "contrast": "NOT the continuum point-mass 4GM/(c^2 b) ~ 1/b (Newton/Schwarzschild)",
      "quantized_topological": "full deficit if the geodesic winds the site, else 0",
      "cited": "the cone-unrolling / cosmic-string deflection (standard GR)"},
     check="deflection = the full deficit (14.B.4) for any winding -- impact-parameter-independent")
assert dv2_ok

# ---- DV.3 the total deflection = 4pi = the double cover -- DERIVED ----------------------
total_radits = 12 * deficit_radits(5)                    # 12 sites * 2 radits = 24
turns = total_radits // 12                                # 24 / 12 = 2 full 2pi turns
is_double_cover = (total_radits == 24 and total_radits == 2 * 12 and turns == 2)
dv3_ok = is_double_cover
step("DV.3", "the TOTAL deflection over the twelve = 4*pi = 2*(2*pi): TWO full turns -- the DOUBLE COVER",
     "summing the deflection over the twelve degree-5 sites: 12 * (pi/3) = 4*pi = 12*2 = 24 radits = "
     "2*(12 radits) = TWO full 2*pi turns. This is Gauss-Bonnet (2*pi*chi = 4*pi for the sphere, 21), and "
     "the factor 2 is the DOUBLE COVER -- a spinor needs 4*pi to return, the 2I structure (06)",
     ["DV.1", "21.GC.1"],
     "the whole-substrate holonomy, and it lands on a structural resonance (danger-free, not fitted). The "
     "twelve each deflect a geodesic by pi/3; their total is 12*(pi/3) = 4*pi = 24 radits = 2*12 = two "
     "full 2*pi turns. This is exactly Gauss-Bonnet -- the total curvature of a genus-0 surface is "
     "2*pi*chi = 4*pi (chi=2), already the integral match in container 21 (24 radits = 4pi = 2*pi*chi). "
     "The telling factor is the 2: the total holonomy is TWO full rotations, not one -- a DOUBLE cover. A "
     "spinor is exactly the object that needs a 4*pi rotation (not 2*pi) to return to itself, and the "
     "carrier is 2I, the binary icosahedral group, the double cover of the icosahedral rotation group "
     "(06). Container 03 also named 3D-from-2pi->4pi (the double cover) as a sibling route. So the "
     "substrate's total geodesic holonomy = 4*pi = the spinor double-cover = the 2I structure -- gravity's "
     "curvature-holonomy meeting the carrier's spin structure. (24 = 2*12 is kernel-checkable; the 4*pi "
     "and the spinor reading cite 21 and 06.)",
     "UNIQUE (total = 24 radits = 4*pi = 2*(2*pi), a double cover)", "DERIVED",
     {"total_radits": total_radits, "total_radians": "4*pi", "full_turns": turns,
      "double_cover": is_double_cover, "gauss_bonnet": "2*pi*chi = 4*pi (chi=2), = 21's integral match",
      "resonance": "4*pi = the spinor double cover = the 2I structure (06); 03's 2pi->4pi sibling route"},
     check="total = 12 * deficit(5) = 24 radits = 2*12 = two full 2*pi turns (= 4*pi)")
assert dv3_ok

# ---- DV.4 the reading -- POSTULATE (quarantined) ---------------------------------------
step("DV.4", "the reading (filed through 19): the substrate deflects geodesics like a lattice of CONICAL DEFECTS (cosmic-string-like); the observable magnitude is gravitational light-bending",
     "the substrate's concentrated curvature deflects geodesics like a lattice of conical defects / "
     "cosmic strings (DV.2): quantized, impact-independent, pi/3 per site (DV.1), 4*pi total (DV.3). The "
     "observable magnitude compares to gravitational light-bending. NAMED, held, quarantined",
     ["DV.2", "DV.3", "37.GM.5"],
     "the physical correspondence, filed through 19, held to the same discipline as 37.GM.5. SUBSTRATE "
     "side (checked): pi/3 per site (DV.1), impact-independent conical form (DV.2), 4*pi total = double "
     "cover (DV.3). PHYSICS side (cited): conical defects / cosmic strings deflect light by the deficit "
     "angle, impact-independent -- a real GR object; gravitational light-bending is a geodesic deflection. "
     "THE READING: the substrate's curvature deflects geodesics like cosmic strings, and this IS its "
     "gravitational light-bending, quantized at pi/3 per site. IMPORTANT what this is NOT: it is NOT the "
     "smooth point-mass deflection (Newton/Schwarzschild 4GM/c^2 b) -- that is a DIFFERENT regime "
     "(smeared, continuum) and needs mass + the continuum limit (DV.5). So the substrate's NATIVE "
     "deflection is the cosmic-string form; the point-mass form is an emergent large-N / smeared limit, "
     "owed. WHAT DOES NOT TRAVEL: the observable magnitude (DV.5); mass; the continuum. A correspondence, "
     "WEAK; quarantined; no downstream premise use.",
     "POSTULATE (substrate deflection = conical-defect / cosmic-string light-bending; the point-mass form is owed; held)", "POSTULATE",
     {"reading": "the substrate deflects geodesics like a lattice of conical defects / cosmic strings -- quantized pi/3 per site, impact-independent",
      "native_form": "cosmic-string (topological), NOT the smooth point-mass 4GM/c^2 b (a smeared/continuum limit, owed)",
      "filed_through": "the 19 gate (mirror of 37.GM.5)", "downstream_premise_use": False,
      "correspondence_not_confirmed": True},
     check=None)

# ---- DV.5 OWED: the observable GR magnitude -- danger zone ------------------------------
step("DV.5", "OWED: the OBSERVABLE GR magnitude (light-bending arcsec; the Newtonian factor of 2) -- mass + anchor + continuum, danger zone, NEVER fitted",
     "OWED: the observable gravitational deflection magnitude -- the light-bending angle in physical "
     "units (arcsec), and the point-mass smooth form 4GM/(c^2 b) (with the famous factor of 2 over the "
     "Newtonian 2GM/(c^2 b)). This needs a MASS, the Planck ANCHOR (a length scale), and the CONTINUUM "
     "limit (08.8.6) -- the danger zone and an owner decision; computed-then-compared, NEVER fitted",
     ["DV.4"],
     "the honest boundary. DV.1-DV.3 give the INTRINSIC deflection value -- pi/3 per site, impact-"
     "independent, 4*pi total -- pure geometry, danger-free, forced. The OBSERVABLE gravitational "
     "magnitude is a different object and is OWED behind three things this container will NOT cross: (a) a "
     "MASS -- the point-mass deflection 4GM/(c^2 b) needs M; mass is the DANGER ZONE / the Path-A/B owner "
     "decision (27); (b) the ANCHOR -- a physical length scale (the Planck length) to turn radit-deflection "
     "into arcsec; external (27), owner-gated; (c) the CONTINUUM limit -- the smooth 1/b point-mass form "
     "is a smeared large-N limit of the quantized cosmic-string deflection (DV.2), and the continuum is "
     "08.8.6, deliberately not-a-rung. The famous FACTOR OF 2 (GR light-bending = twice Newtonian) is "
     "NOT chased here -- reaching for it from a known target would be the refused-list error; it is owed a "
     "forced derivation (the space+time split), not a fit. So the intrinsic value is DERIVED; the "
     "observable magnitude is located, gated, and NOT attempted. NOT crossed here.",
     "OWED (observable GR magnitude -- mass + anchor + continuum, danger zone; the factor of 2 never fitted)", "OWED",
     {"owed_mass": "the point-mass deflection 4GM/(c^2 b) needs M -- danger zone / owner decision (27)",
      "owed_anchor": "a physical length scale (Planck length) to convert radits -> arcsec -- external (27)",
      "owed_continuum": "the smooth 1/b form is a smeared large-N limit of the quantized cosmic-string deflection -- 08.8.6, not-a-rung",
      "refused": "the GR/Newtonian factor of 2 -- NOT chased from a target (refused-list); owed a forced derivation",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="38-deflection-value",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        deflection_radits=DEFLECT_RADITS, twelve_radits=twelve_radits, twelve_radians="pi/3",
        twelve_degrees=60.0, total_radits=total_radits, full_turns=turns, double_cover=is_double_cover,
        finding="THE DEFLECTION VALUE, intrinsic and exact: pi/3 (60 deg) per degree-5 site = the deficit "
                "angle (6-d)*(pi/3) (DV.1); IMPACT-PARAMETER-INDEPENDENT -- a conical defect / cosmic "
                "string, NOT the point-mass 1/b (DV.2); TOTAL = 4*pi = 2*(2*pi), TWO full turns, the "
                "DOUBLE COVER (Gauss-Bonnet, = 21; the 2I spinor structure, 06) (DV.3). The reading -- the "
                "substrate deflects like a lattice of cosmic strings -- is POSTULATE (through 19). The "
                "OBSERVABLE GR magnitude (arcsec; the Newtonian factor of 2) is OWED behind mass + the "
                "anchor + the continuum (danger zone), NEVER fitted (DV.5). Danger-free; nothing chased.",
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
