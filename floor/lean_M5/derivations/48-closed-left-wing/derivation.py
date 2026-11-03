#!/usr/bin/env python3
"""Container 48 -- THE CLOSED LEFT WING: closure forces the negative-curvature mirror -- 12 degree-7 at genus 2.

Step 8 of the forward frontier (Maths 6.7): force what 36.LW.6 owed -- the CLOSED negative-curvature
realization (36 built only a patch / the open plane). The clue is 03's own closure forcing, read across the
mirror: the counting law V(6-d) = 6*chi (Euler + 3F=2E + uniform degree) that gave the sphere (d,V) =
(3,4),(4,6),(5,12) at chi=2 gives, at chi=-2 (genus 2), (d,V) = (7,12),(8,6),(9,4) -- the EXACT mirror
under d <-> 12-d, same V. The icosahedron's mirror is 12 degree-7 vertices on a genus-2 surface: the
negative-curvature sibling of the twelve.

  CW.1  the closure law V(6-d) = 6*chi (03's REFRAME-CLOSURE-FORCING generalized to any chi). Euler
        V-E+F=chi with 3F=2E (triangulation) and uniform degree d (E=dV/2, F=dV/3) gives V(6-d)=6*chi.
        DERIVED.

  CW.2  the mirror spectrum. chi=+2 (sphere) forces 6-d>0, i.e. d<6: (d,V) = (3,4),(4,6),(5,12) (= 03).
        chi=-2 (genus 2) forces 6-d<0, i.e. d>6: (d,V) = (7,12),(8,6),(9,4) -- the MIRROR under d<->12-d,
        with the SAME V. Positive curvature needs d<6; negative needs d>6; the mirror is at d=6 (flat).
        DERIVED.

  CW.3  the icosahedron's mirror is 12 degree-7 vertices at genus 2 (chi=-2). d=7 => V=12, the exact
        vertex-count mirror of the sphere's 12 degree-5 (d=5, V=12). Total angle deficit sum(12-2d) =
        12*(-2) = -24 = 12*chi (Gauss-Bonnet) -- the sign-mirror of the sphere's +24. The negative-
        curvature sibling of the twelve. DERIVED.

  CW.4  REALIZABILITY (held): the counting (CW.1-CW.3) is a NECESSARY condition; whether a simplicial
        7-regular triangulation of genus 2 with exactly 12 vertices EXISTS as a regular map is NOT asserted
        here (the {3,7} regular maps exist -- the minimal is Klein's genus-3, 56 vertices -- but the
        12-vertex genus-2 case is the counting mirror, realizability uncertain). Held / cited. POSTULATE.

  CW.5  OWED: realizability confirmed or refuted; the max-density / Schwarzschild VALUE (danger zone);
        and whether the SUBSTRATE ever realizes degree>6 -- the metric-no-thirteenth (41/42/43) from the
        other side (a 13th neighbour IS a degree-7 site). OWED.

Rests on 03 (the closure forcing), 36 (the left wing / the deficit across the mirror), 14 (Gauss-Bonnet);
cites the {3,7} regular-map literature. DANGER-FREE: pure closure counting -- no mass, no value. `--check`
recomputes.
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


# ================================================================ the closure law (03 generalized)
def closure_V(d, chi):
    """Euler + 3F=2E (triangulation) + uniform degree d => V(6-d) = 6*chi. Returns V if a positive
    integer solution exists, else None."""
    denom = 6 - d
    if denom == 0:
        return None                       # d=6: flat, V*0 = 6chi -> no finite closed count
    if (6 * chi) % denom != 0:
        return None
    V = (6 * chi) // denom
    return V if V > 0 else None


# ---- CW.1 the closure law -- DERIVED ----------------------------------------------------
# Certify the derivation V(6-d)=6chi on the known sphere cases (03): (3,4),(4,6),(5,12) at chi=2.
sphere_spectrum = {d: closure_V(d, 2) for d in (3, 4, 5)}
cw1_ok = (sphere_spectrum == {3: 4, 4: 6, 5: 12})
step("CW.1", "the closure law V(6-d) = 6*chi (03's REFRAME-CLOSURE-FORCING generalized to any chi)",
     "for a closed triangulation (3F=2E) with uniform degree d: E = dV/2, F = dV/3, so Euler V-E+F=chi "
     "gives V - dV/2 + dV/3 = chi, i.e. V(6-d) = 6*chi. At chi=2 this reproduces 03's sphere spectrum "
     "(3,4),(4,6),(5,12)",
     ["03.3.3", "14.B.4"],
     "the lever, 03's own closure forcing, written for any Euler characteristic. Container 03 "
     "(REFRAME-CLOSURE-FORCING) forced the sphere's degree/vertex pairs from closure alone: Euler "
     "V-E+F=chi, plus the triangulation identity 3F=2E (each face a triangle, each edge in two faces), "
     "plus a UNIFORM vertex degree d (so E=dV/2, F=2E/3=dV/3). Substituting: V - dV/2 + dV/3 = V(6-d)/6 "
     "= chi, hence V(6-d) = 6*chi. RUN IT at chi=2 (the sphere): d=3 -> V=4 (tetrahedron), d=4 -> V=6 "
     "(octahedron), d=5 -> V=12 (icosahedron) -- exactly 03's forced spectrum, and d>=6 impossible "
     "(6-d<=0 gives no positive V). So the law is 03's, certified here on the sphere; CW.2 reads it across "
     "the mirror to the negative-curvature side.",
     "UNIQUE (V(6-d)=6chi from Euler + 3F=2E + uniform degree; reproduces 03 at chi=2)", "DERIVED",
     {"law": "V(6-d) = 6*chi", "sphere_spectrum_chi2": sphere_spectrum,
      "derivation": "Euler V-E+F=chi; 3F=2E; uniform degree d (E=dV/2, F=dV/3)"},
     check="V(6-d)=6chi at chi=2 gives (3,4),(4,6),(5,12) -- 03's sphere spectrum")
assert cw1_ok

# ---- CW.2 the mirror spectrum -- DERIVED -----------------------------------------------
genus2_spectrum = {d: closure_V(d, -2) for d in (7, 8, 9)}
# the mirror map d <-> 12-d takes the sphere spectrum to the genus-2 spectrum with the SAME V
mirror_ok = all(closure_V(d, 2) == closure_V(12 - d, -2) for d in (3, 4, 5))
cw2_ok = (genus2_spectrum == {7: 12, 8: 6, 9: 4} and mirror_ok)
step("CW.2", "the mirror spectrum: chi=-2 (genus 2) forces d>6, (d,V)=(7,12),(8,6),(9,4) -- the mirror of the sphere under d<->12-d",
     "at chi=-2 (genus 2) the law V(6-d)=6*chi=-12 forces 6-d<0, i.e. d>6: (d,V) = (7,12),(8,6),(9,4). "
     "Under the mirror map d <-> 12-d this is EXACTLY the sphere's (5,12),(4,6),(3,4) with the SAME V: "
     "positive curvature needs d<6, negative needs d>6, the mirror at d=6 (flat)",
     ["CW.1", "36.LW.4"],
     "the payoff -- the closed left wing, forced by the same closure math. The sphere spectrum sits at "
     "chi=2, d<6 (positive deficit 12-2d>0). The genus-2 surface has chi = 2-2*genus = -2, so the law "
     "gives V(6-d) = -12, which needs 6-d<0, i.e. d>6 -- negative deficit, exactly 36's left wing. RUN "
     "IT: d=7 -> V=12, d=8 -> V=6, d=9 -> V=4 (d>=10 degenerate). Now the mirror: reflect the degree "
     "about the flat mirror d=6, d <-> 12-d, so 5<->7, 4<->8, 3<->9. The sphere's (5,12),(4,6),(3,4) maps "
     "to the genus-2 (7,12),(8,6),(9,4) -- SAME vertex counts, mirrored degrees, mirrored curvature sign. "
     "The three positive-curvature closed triangulations (tetra/octa/icosa) have three exact negative-"
     "curvature mirrors at genus 2. This is 36.LW.4's 'chi<0 surface' made precise and closed -- not a "
     "patch, a specific closed spectrum.",
     "UNIQUE (chi=-2 forces d>6: (7,12),(8,6),(9,4); the mirror of the sphere under d<->12-d)", "DERIVED",
     {"genus2_spectrum_chi_minus2": genus2_spectrum, "mirror_map": "d <-> 12-d (about the flat mirror d=6)",
      "same_V_under_mirror": mirror_ok,
      "correspondence": "(5,12)<->(7,12), (4,6)<->(8,6), (3,4)<->(9,4) -- icosa/octa/tetra and their negative-curvature mirrors"},
     check="chi=-2 gives (7,12),(8,6),(9,4); equals the sphere spectrum under d<->12-d with the same V")
assert cw2_ok

# ---- CW.3 the icosahedron's mirror: 12 degree-7 at genus 2 -- DERIVED -------------------
ICOSA_V, ICOSA_D, ICOSA_CHI = 12, 5, 2
MIRROR_V, MIRROR_D, MIRROR_CHI = closure_V(7, -2), 7, -2
sphere_total_deficit = ICOSA_V * (12 - 2 * ICOSA_D)          # 12*(+2) = +24 = 12*chi
mirror_total_deficit = MIRROR_V * (12 - 2 * MIRROR_D)        # 12*(-2) = -24 = 12*chi
cw3_ok = (MIRROR_V == 12 and MIRROR_V == ICOSA_V
          and sphere_total_deficit == 24 and mirror_total_deficit == -24
          and sphere_total_deficit == 12 * ICOSA_CHI and mirror_total_deficit == 12 * MIRROR_CHI)
step("CW.3", "the icosahedron's mirror: 12 degree-7 vertices at genus 2 (chi=-2), total deficit -24 = 12*chi -- the sibling of the twelve",
     "d=7 => V=12: the closed left wing is 12 degree-7 vertices on a genus-2 surface (chi=-2), the EXACT "
     "vertex-count mirror of the sphere's 12 degree-5 (the twelve). Total angle deficit sum(12-2d) = "
     "12*(-2) = -24 = 12*chi (Gauss-Bonnet) -- the sign-mirror of the sphere's +24. The negative-curvature "
     "sibling of the twelve",
     ["CW.2", "14.B.4"],
     "the headline mirror. The icosahedron is the d=5 closed triangulation: 12 vertices, chi=2 (genus 0), "
     "each vertex deficit +2, total +24 = 12*chi (Gauss-Bonnet, 14.B.4). Its mirror under d<->12-d is "
     "d=7, and CW.2 gives V=12 again: a closed genus-2 (chi=-2) surface with 12 degree-7 vertices, each "
     "deficit 12-14 = -2, total -24 = 12*(-2) = 12*chi. So the twelve have an exact negative-curvature "
     "sibling: same COUNT (12), mirrored DEGREE (7 vs 5), mirrored SIGN (-2 vs +2), mirrored TOPOLOGY "
     "(genus 2 vs 0), mirrored total deficit (-24 vs +24). This is what 36.LW.6 owed -- the closed "
     "realization -- as a forced counting fact: IF the closed left wing exists, it is these 12 degree-7 "
     "sites at genus 2. (Realizability as a simplicial regular map is CW.4, held.) The max-density "
     "'anti-twelve' mirrors the min-density twelve.",
     "UNIQUE (d=7 => 12 degree-7 vertices at genus 2, chi=-2, total deficit -24 = 12*chi)", "DERIVED",
     {"icosahedron": {"V": ICOSA_V, "d": ICOSA_D, "chi": ICOSA_CHI, "total_deficit": sphere_total_deficit},
      "mirror": {"V": MIRROR_V, "d": MIRROR_D, "chi": MIRROR_CHI, "genus": 2, "total_deficit": mirror_total_deficit},
      "same_vertex_count": MIRROR_V == ICOSA_V,
      "the_anti_twelve": "12 degree-7 sites, deficit -2 each, total -24 = 12*chi -- the max-density mirror of the twelve"},
     check="d=7 => V=12 (= icosa's 12); total deficit -24 = 12*(-2) = 12*chi (mirror of +24)")
assert cw3_ok

# ---- CW.4 realizability -- POSTULATE (held) --------------------------------------------
step("CW.4", "REALIZABILITY (held): the counting is NECESSARY; a simplicial 12-vertex 7-regular genus-2 surface is NOT asserted to exist",
     "the closure counting (CW.1-CW.3) is a NECESSARY condition; whether a simplicial 7-regular "
     "triangulation of genus 2 with exactly 12 vertices EXISTS as a regular map is NOT asserted here (the "
     "{3,7} regular maps exist -- the minimal is Klein's genus-3, 56 vertices -- but the 12-vertex genus-2 "
     "case is the counting mirror; realizability uncertain). Held / cited",
     ["CW.3"],
     "the honest boundary -- the counting mirror is exact, but existence is a further question. Euler + "
     "3F=2E + uniform degree is NECESSARY, not sufficient: it fixed the sphere's (5,12) AND the "
     "icosahedron is genuinely realizable (a real polytope), but for genus 2 the same count (12 degree-7) "
     "may or may not be realizable as an actual simplicial surface / regular map. The {3,7} regular maps "
     "DO exist on some genera -- the smallest is the Klein quartic, genus 3, 56 vertices (the Hurwitz "
     "surface) -- but a 12-vertex genus-2 7-regular triangulation is the COUNTING mirror, and its "
     "existence as a regular map is not established here (it may be a non-regular triangulation, or not "
     "exist). So this container claims the COUNTING (what the closed left wing must be IF it exists: 12 "
     "degree-7 at genus 2), not the geometric realization. Held, quarantined; no downstream premise use. "
     "This is the same discipline 03 uses (the closure count is forced; the polytope realization is a "
     "separate fact).",
     "POSTULATE (realizability of the 12-vertex genus-2 7-regular surface -- necessary count holds; no SYMMETRIC realization; general existence undetermined)", "POSTULATE",
     {"counting_is_necessary_not_sufficient": True,
      "known_37_regular_map": "Klein quartic (the dual {3,7} has 24 vertices, genus 3) -- the minimal {3,7} regular map",
      "twelve_vertex_genus2": "the counting mirror; realizability as a regular map not asserted",
      "claims": "the counting (12 degree-7 at genus 2 IF it exists), not the geometric realization",
      "realizability_check_2026_09_08": "CHECKED (Maths 6.7): necessary counts hold (V=12,E=42,F=28,chi=-2; "
          "Heawood min 9<=12). NO SYMMETRIC realization: a vertex-transitive Z12 regular Cayley map gives NO "
          "7-regular triangulation at any genus (7200 rotation systems searched; the face-tracer validated on "
          "the Csaszar torus Z7 {3,6} genus 1) -- consistent with genus 2 admitting NO {3,7} REGULAR map (no "
          "genus-2 Hurwitz group; the minimal is Klein's genus 3). GENERAL (non-symmetric) existence "
          "UNDETERMINED here -- needs an isomorphism-free surface-triangulation enumerator (surftri/plantri). "
          "No clean obstruction found (the 'each edge in exactly 2 triangles => complement is K5's' argument "
          "FAILS: triangulations admit non-facial empty triangles, so edges may share >2 neighbours).",
      "downstream_premise_use": False},
     check=None)

# ---- CW.5 OWED ------------------------------------------------------------------------
step("CW.5", "OWED: realizability confirmed/refuted; the max-density value (danger); whether the substrate goes LEFT (the metric-no-thirteenth)",
     "OWED: (a) realizability of the 12-vertex genus-2 7-regular surface CONFIRMED or REFUTED (an "
     "explicit construction or an obstruction); (b) the max-density / Schwarzschild VALUE (danger zone); "
     "(c) whether the SUBSTRATE ever realizes degree>6 -- the metric-no-thirteenth (41/42/43) from the "
     "other side, since a 13th neighbour IS a degree-7 site. The counting mirror is forced; realization, "
     "value, and substrate-realization are owed",
     ["CW.3", "CW.4"],
     "the honest residual, tying back to the frontier. CW.1-CW.3 force the closed left wing's counting "
     "(12 degree-7 at genus 2, the exact mirror of the icosahedron); CW.4 holds realizability. What "
     "remains: (a) REALIZABILITY -- build the simplicial genus-2 surface explicitly, or find the "
     "obstruction (a bounded, danger-free combinatorial search, a good next step); (b) the max-density / "
     "Schwarzschild VALUE (36.LW.6.b) -- computed-then-compared, never fitted, the danger zone (mass); "
     "(c) whether the SUBSTRATE goes LEFT of the mirror at all -- and this is the same metric-no-thirteenth "
     "that 41/42/43 addressed for the RIGHT wing (a 13th neighbour = a degree-7 site = going left). So the "
     "left wing's realization and the metric-no-thirteenth are one problem, now with the closed target "
     "specified (12 degree-7, genus 2). NOT attempted further here.",
     "OWED (realizability; the max-density value -- danger; whether the substrate goes left = the metric-no-thirteenth)", "OWED",
     {"owed_realizability": "an explicit 12-vertex genus-2 7-regular surface, or an obstruction -- the SYMMETRIC "
          "case is settled NEGATIVE (CW.4: no vertex-transitive Z12 realization; no genus-2 {3,7} regular map); "
          "the general (non-symmetric) case needs surftri/plantri (not available here)",
      "owed_value": "the max-density / Schwarzschild value (36.LW.6) -- computed-then-compared, danger zone",
      "owed_substrate": "whether the substrate realizes degree>6 = the metric-no-thirteenth (41/42/43) from the other side",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="48-closed-left-wing",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        sphere_spectrum_chi2=sphere_spectrum, genus2_spectrum_chi_minus2=genus2_spectrum,
        mirror_same_V=mirror_ok,
        icosa={"V": ICOSA_V, "d": ICOSA_D, "chi": ICOSA_CHI, "total_deficit": sphere_total_deficit},
        mirror={"V": MIRROR_V, "d": MIRROR_D, "chi": MIRROR_CHI, "genus": 2, "total_deficit": mirror_total_deficit},
        finding="THE CLOSED LEFT WING forced by closure (36.LW.6.a). The law V(6-d)=6*chi (03's closure "
                "forcing generalized -- Euler + 3F=2E + uniform degree, CW.1) at chi=-2 (genus 2) forces "
                "d>6: (d,V)=(7,12),(8,6),(9,4), the EXACT mirror of the sphere's (5,12),(4,6),(3,4) under "
                "d<->12-d with the SAME V (CW.2). The icosahedron's mirror is 12 degree-7 vertices at "
                "genus 2, total deficit -24 = 12*chi -- the negative-curvature 'anti-twelve', sibling of "
                "the twelve (CW.3). Realizability CHECKED (CW.4, Maths 6.7): the counts hold, but NO "
                "symmetric realization exists (no vertex-transitive Z12 map -- 7200 rotation systems, tracer "
                "validated on Csaszar; no genus-2 {3,7} regular map), and the general non-symmetric case is "
                "undetermined (needs surftri). General realizability, the value, and whether the substrate "
                "goes left (the metric-no-thirteenth, 41/42/43) are OWED (CW.5). Danger-free; nothing fitted.",
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
