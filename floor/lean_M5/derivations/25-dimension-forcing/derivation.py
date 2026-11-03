#!/usr/bin/env python3
"""Container 25 -- DIMENSION FORCING: what the counting law forces, and what it does not.
Rests on 13, 14, 03; cites 09, 21.

Step 11 of the physics-bridge arc. The roadmap asked: does the substrate FORCE n=3 and the coefficient
1/(6(n+2)) from the counting law itself? The honest answer UN-CONFLATES three different dimensions the
question ran together (Kevin's scope decision, Maths 6.5):

  - INTRINSIC dimension (the surface's own; the n in V(eps); the ball-growth degree) = 2. FORCED by the
    counting law -- the flat reference flat_ball(r)=1+3r(r+1) is a degree-2 polynomial (ring count 6r
    linear), the signature of an intrinsically 2-D space. The substrate is a closed 2-SPHERE (a surface).
  - The CURVATURE COEFFICIENT 6(n+2) at that n = 24. FORCED at n=2; and its equality with the
    Gauss-Bonnet total 12*chi=24 is a COINCIDENCE of the 2-sphere (chi=2), NOT a structural identity
    (it fails for chi != 2 while the intrinsic n stays 2). Run, not assumed.
  - AMBIENT dimension (the embedding; the kissing/icosahedron dim=3) = 3. NOT forced by the counting
    law -- this is container 03's genuinely-OPEN metric no-thirteenth (3.7). Its levers (separation,
    kissing) are DECIDED-FAILED (CORRECTIONS #6: dim=3 upper bound is a checked negative on three
    counts). NOT re-attempted here; located as the residual OWED.

So "why 3 dimensions" splits into FORCED-2 (intrinsic) + OWED-3 (ambient). That un-conflation is the
result. (A holographic reading -- a 2-D surface substrate, "information on the surface" -- is consonant
but held as a NOTED reading, not a claim; no physics smuggled.)

  DF.1  the counting law forces the INTRINSIC dimension n=2 (ball-growth polynomial degree). DERIVED.
  DF.2  the curvature coefficient 6(n+2)=24 is forced at n=2; 6(n+2)=12*chi is a SPHERE COINCIDENCE,
        not a forced identity (fails for chi != 2). DERIVED.
  DF.3  the AMBIENT dimension 3 is NOT forced -- container 03's metric no-thirteenth (3.7), decided-hard.
        OWED, located, not re-attempted.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
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


# ================================================================ the counting law (consumes 14)
def flatBall(r):
    """Container 14's flat reference: the ball count of a defect-zero (degree-6) neighbourhood."""
    return 1 + 3 * r * (r + 1)


def ring(r):
    """The shell (ring) count = flat_ball(r) - flat_ball(r-1) = 6r, for r >= 1."""
    return flatBall(r) - flatBall(r - 1)


def diff2(f, r):
    return f(r + 2) - 2 * f(r + 1) + f(r)


def diff3(f, r):
    return f(r + 3) - 3 * f(r + 2) + 3 * f(r + 1) - f(r)


# ---- DF.1 the counting law forces the intrinsic dimension n=2 -- DERIVED ---------------
# flat_ball(r)=1+3r(r+1)=1+3r+3r^2 is a DEGREE-2 polynomial. Its second difference is a nonzero
# constant (6) and its third difference is 0 -- the exact signature of degree 2. The ring (shell)
# count 6r is LINEAR (grows as r^{d-1}=r^1), so the intrinsic dimension d = 2. Contrast: a 1-D line
# ball 2r+1 has second difference 0 (degree 1), so the substrate is NOT 1-D; a cubic (3-D volume)
# would have nonzero third difference, and flat_ball's third difference is 0, so it is NOT degree 3.
second_diff_const = all(diff2(flatBall, r) == 6 for r in range(6))     # degree-2: d2 const nonzero
third_diff_zero = all(diff3(flatBall, r) == 0 for r in range(6))       # degree-2: d3 = 0
ring_is_6r = all(ring(r) == 6 * r for r in range(1, 8))                # shell linear -> dim-1 = 1
line1d = lambda r: 2 * r + 1                                            # a 1-D lattice ball, for contrast
line_is_degree1 = all(diff2(line1d, r) == 0 for r in range(6))         # line: d2 = 0 (degree 1)
INTRINSIC_DIM = 2                                                       # = ball-growth polynomial degree
df1_ok = second_diff_const and third_diff_zero and ring_is_6r and line_is_degree1
step("DF.1", "the counting law forces the INTRINSIC dimension n=2 (ball-growth polynomial degree)",
     "flat_ball(r)=1+3r(r+1) is degree 2 (second difference const 6, third difference 0); the ring "
     "count 6r is linear (shell ~ r^{d-1}=r^1), so the intrinsic dimension d=2 -- forced, not chosen",
     ["14.B.1", "13.A.2"],
     "the first, solid half of dimension-forcing. The intrinsic (growth) dimension of a space is the "
     "degree of its ball-growth counting law: |B_r| ~ r^d. Container 14's flat reference flat_ball(r) = "
     "1+3r(r+1) = 1+3r+3r^2 is a DEGREE-2 polynomial -- certified by its finite differences: the second "
     "difference is the nonzero constant 6 (the hallmark of degree exactly 2) and the third difference "
     "is 0. Equivalently the RING (shell) count is 6r, LINEAR in r; a shell grows as r^{d-1}, so 6r ~ "
     "r^1 gives d-1=1, d=2. This is FORCED by the icosahedral/triangular adjacency (6 per ring = the "
     "flat degree-6 triangular tiling, container 14.B.1), not put in by hand. And it is discriminating: "
     "a 1-D lattice ball 2r+1 has second difference 0 (degree 1), so the substrate is NOT 1-D; a 3-D "
     "volume would have a nonzero third difference, and flat_ball's third difference is 0, so it is NOT "
     "degree 3. The substrate is intrinsically a SURFACE -- dimension exactly 2. NOTE: this is the "
     "n in the curvature law V(eps) (container 21, n=2) and is DISTINCT from the ambient dimension 3 "
     "(DF.3); the counting law forces the intrinsic 2, not the ambient 3.",
     "UNIQUE (the intrinsic dimension is the ball-growth polynomial degree = 2)", "DERIVED",
     {"flat_ball": "1+3r(r+1) = 1+3r+3r^2, degree 2",
      "second_difference_constant_6": second_diff_const, "third_difference_zero": third_diff_zero,
      "ring_is_6r_linear": ring_is_6r, "line_1d_is_degree1_contrast": line_is_degree1,
      "intrinsic_dimension": INTRINSIC_DIM,
      "not_1d_not_3d": "line (2r+1) is degree 1; a cubic is degree 3; flat_ball is degree 2",
      "distinct_from_ambient": "this is intrinsic n=2 (surface), NOT the ambient dim=3 (DF.3)"},
     check="flat_ball degree 2 (d2 const 6, d3 = 0); ring 6r linear; line 2r+1 degree 1 -> intrinsic dim 2")
assert df1_ok

# ---- DF.2 the coefficient 6(n+2)=24 forced; =12chi a sphere coincidence -- DERIVED -----
def coeff(n):
    """The curvature coefficient in V(eps)=w_n eps^n [1 - R eps^2 / (6(n+2))] (container 21)."""
    return 6 * (n + 2)


def gaussBonnet(chi):
    """The Gauss-Bonnet total angle deficit = 12*chi radits (container 14.B.4; 12 radits = 2pi)."""
    return 12 * chi


coeff_at_n2 = coeff(INTRINSIC_DIM)                 # 6*(2+2) = 24, FORCED at the intrinsic n=2
gb_sphere = gaussBonnet(2)                          # 12*2 = 24 (chi=2, the sphere)
coeff_forced = (coeff_at_n2 == 24)
# identity or coincidence? The intrinsic n is 2 for ANY surface (genus-independent). So test 6(n+2)
# with n FIXED at 2 against 12*chi for several closed surfaces: it matches ONLY chi=2 (the sphere).
match_by_chi = {chi: (coeff(2) == gaussBonnet(chi)) for chi in (2, 1, 0)}   # sphere / RP2 / torus
is_sphere_coincidence = match_by_chi[2] and not match_by_chi[1] and not match_by_chi[0]
df2_ok = coeff_forced and (gb_sphere == 24) and is_sphere_coincidence
step("DF.2", "the coefficient 6(n+2)=24 is forced at n=2; 6(n+2)=12*chi is a SPHERE COINCIDENCE",
     "6(n+2) at the intrinsic n=2 (DF.1) is 24, forced; it equals the Gauss-Bonnet total 12*chi=24 "
     "for the sphere (chi=2) but NOT for chi != 2 (n stays 2), so the equality is a coincidence, not "
     "a forced identity",
     ["DF.1", "14.B.4"],
     "the coefficient half, and the honest disambiguation the roadmap's question needed. The local "
     "curvature law is V(eps)=w_n eps^n [1 - R eps^2 / (6(n+2))] (container 21, cited). Its coefficient "
     "6(n+2), evaluated at the FORCED intrinsic dimension n=2 (DF.1), is 6*4 = 24 -- so the coefficient "
     "is FORCED by the counting law, not put in by hand. It coincides with the substrate's Gauss-Bonnet "
     "total deficit 12*chi = 24 (chi=2, container 14.B.4). Is that a forced IDENTITY or a COINCIDENCE? "
     "RUN IT: the intrinsic dimension of a surface is 2 REGARDLESS of genus (any closed surface is 2-D), "
     "so hold n=2 and vary the topology. 6(2+2)=24 equals 12*chi only at chi=2 (the sphere); for chi=1 "
     "it is 24 vs 12, for chi=0 (the torus) 24 vs 0 -- NO match. So 6(n+2)=12*chi is SPHERE-SPECIFIC: a "
     "COINCIDENCE of chi=2, NOT a structural identity. This prevents a false-identity claim (the two 24s "
     "have different provenance -- one local/dimensional, one topological -- and agree only here). The "
     "coefficient is forced by n; the Gauss-Bonnet total is forced by chi; they meet at 24 for the "
     "2-sphere alone.",
     "UNIQUE (6(n+2)=24 at n=2; the =12chi equality holds only at chi=2)", "DERIVED",
     {"coefficient_6_n_plus_2_at_n2": coeff_at_n2, "gauss_bonnet_sphere_12chi": gb_sphere,
      "coefficient_forced_at_n2": coeff_forced,
      "match_by_chi_sphere_rp2_torus": match_by_chi,
      "equality_is_sphere_coincidence_not_identity": is_sphere_coincidence,
      "provenance": "6(n+2) is local/dimensional (forced by n=2); 12chi is topological (forced by chi=2)",
      "meets_only_for_2sphere": True},
     check="6(2+2)=24=12*2 (sphere); with n fixed 2, matches 12chi only at chi=2 -> coincidence not identity")
assert df2_ok

# ---- DF.3 the ambient dimension 3 is NOT forced -- OWED (located) -----------------------
step("DF.3", "the AMBIENT dimension 3 is NOT forced by the counting law -- the metric no-thirteenth (OWED)",
     "the '3' of 'why 3 dimensions' is the AMBIENT dimension (the 2-sphere's embedding / the kissing "
     "dim=3), which is container 03's OPEN metric no-thirteenth (3.7) -- the counting law does not "
     "supply it, and its levers are decided-failed",
     ["DF.1", "03.6", "03.7"],
     "the residual, located and NOT re-attempted -- the honest boundary. The counting law forces the "
     "INTRINSIC dimension 2 (DF.1); the '3' of 'why 3 dimensions' is a DIFFERENT dimension -- the AMBIENT "
     "one, in which the closed 2-sphere sits (the twelve kissing, the icosahedron, container 09/03). "
     "Container 03 established dim >= 3 (the tetrahedron minimum / equidistant->dim, 3.5) but showed "
     "dim = 3 is a CHECKED NEGATIVE (3.6): the substrate's no-thirteenth is TOPOLOGICAL (an Euler census "
     "at any d), never METRIC; the sphere is 19.6% uncovered by twelve caps (room exists) and D4 admits "
     "13 at d=4. The one genuinely OPEN thing (03's 3.7) is a substrate-native METRIC no-thirteenth, and "
     "nothing supplies one. Its candidate levers are DECIDED-FAILED (CORRECTIONS #6: the separation "
     "lever passes at d=4 for the 24-cell/600-cell; 'do not re-attempt'). The new ball-growth/density "
     "machinery (13-24) does NOT change this: it measures INTRINSIC structure (counts within the "
     "surface), and a metric no-thirteenth is an AMBIENT embedding fact the intrinsic count cannot see -- "
     "indeed the 19.6%-uncovered fact says the ambient sphere has metric ROOM. So the ambient dim=3 stays "
     "OWED, located precisely: it needs a substrate-native metric obstruction that neither the intrinsic "
     "counting law nor the decided-failed separation/kissing levers provide. NOT re-attempted here.",
     "OWED (the ambient metric no-thirteenth; located, not closed; decided-failed levers named)", "OWED",
     {"ambient_dim_not_forced": True,
      "what_it_is": "container 03's 3.7 metric no-thirteenth (a substrate-native METRIC obstruction)",
      "dim_ge_3_derived": "03.5 (tetrahedron minimum / equidistant -> dim >= 3)",
      "dim_eq_3_is_checked_negative": "03.6 (no-thirteenth is topological census, not metric; sphere 19.6% uncovered; D4 admits 13 at d=4)",
      "decided_failed_levers": "separation + kissing (CORRECTIONS #6: 24-cell/600-cell pass at d=4; do not re-attempt)",
      "counting_law_cannot_supply": "it measures INTRINSIC structure; a metric no-thirteenth is an AMBIENT embedding fact",
      "not_reattempted": True, "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="25-dimension-forcing",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # DF.1 -- guarded by the Lean
        second_difference_constant_6=second_diff_const,
        third_difference_zero=third_diff_zero,
        ring_is_6r_linear=ring_is_6r,
        line_1d_is_degree1=line_is_degree1,
        intrinsic_dimension=INTRINSIC_DIM,
        # DF.2 -- guarded by the Lean
        coefficient_at_n2=coeff_at_n2,
        gauss_bonnet_sphere=gb_sphere,
        match_by_chi=match_by_chi,
        equality_is_sphere_coincidence=is_sphere_coincidence,
        # the un-conflation
        forces_intrinsic_2=True,
        ambient_3_is_owed=True,
        finding="the counting law forces intrinsic n=2 (and the coefficient 6(n+2)=24); ambient dim=3 "
                "(the metric no-thirteenth) is NOT forced -- 'why 3' = forced-2 + owed-3",
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
