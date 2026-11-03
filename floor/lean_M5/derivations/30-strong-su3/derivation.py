#!/usr/bin/env python3
"""Container 30 -- STRONG / SU(3) VIA THE CARRIER'S E8: the third filed FORCE entry.
Rests on 12 (the carrier's E8 root system); cites 00 (the triadic floor / three-observer 3-fold), 27
(the coupling is an alpha_hat). Filed through the 19 gate. Runs Kevin's four-step pipeline for the STRONG
force (2026-08-29, Maths 6.5) -- and grades the location HONESTLY, because SU(3) is NOT quaternionic like
the carrier, so it is LESS NATIVE than weak (2I subset SU(2)) or EM (charge built).

THE REFRAME (Kevin): forces = INTERNAL/carrier gauge symmetry; gravity = the geometry (13-24). With weak
SU(2) (28) and EM U(1) (29), the electroweak pair is located in the carrier's quaternion. The strong
SU(3) completes the SM gauge trio -- but its home is the carrier's LARGER structure, E8 (container 12),
not the quaternionic 2I: E8 contains A2 = su(3).

  STEP 1 REQUIREMENT: the strong force is an SU(3) gauge symmetry -- 8 generators (dim su(3)=8, the 8
    gluons), rank 2, center Z/3 (color TRIALITY, 3 colors), confining.
  STEP 2 LOCATION: su(3) = the A2 root system (6 roots + rank 2 = 8), and A2 sits inside the carrier's E8
    (container 12: E8's inner products are {-2,-1,0,1,2}, so two roots at -1 generate A2). The triality
    Z/3 resonates with the substrate's native 3-fold (the triadic floor 00 / the order-3 face sector of
    2I).
  STEP 3 CONDITION: 8 = 6 roots + 2 rank; the A2 Cartan det = 3 = |Z/3| = the triality; a Z/3 symmetry
    must permute the roots (order 3). AND -- honestly -- the location is via E8 subset (a CHOICE of
    embedding), less native than 2I subset SU(2); this must be flagged, not hidden.
  STEP 4 CHECK: the 6 A2 roots {e_i-e_j} all have norm 2; 6+2=8=dim su(3) -- CHECKED; det[[2,-1],[-1,2]]
    = 3 = the triality -- CHECKED; the cyclic coordinate permutation Z/3 permutes the 6 roots (order 3)
    -- CHECKED; A2 subset E8 via inner-product -1 -- cited (12.E.3).

  S.1  su(3) = A2, located in the carrier's E8: 8 = 6 roots + 2 rank; A2 subset E8 (inner product -1,
       12.E.3). DERIVED.
  S.2  the triality Z/3 = det(A2 Cartan) = 3; the cyclic Z/3 permutes the roots (order 3); resonates with
       the substrate's native 3-fold (triadic floor 00 / order-3 faces). DERIVED.
  S.3  THE FILED ENTRY (through 19): su(3) <-> A2 subset E8; color triality Z/3 <-> the 3-fold; 8 gluons
       <-> the 8-dim adjoint. Correspondence -- and LESS NATIVE than weak/EM (the E8 embedding is a
       choice). With 28+29 the SM trio is located; 1+3+8=12 is a NOTED check vs the substrate's 12, NOT a
       claim. POSTULATE.
  S.4  the strong DYNAMICS: confinement, asymptotic freedom, the coupling alpha_s (a dimensionless
       alpha_hat), the color assignments of matter (danger zone). OWED, located.

A CORRESPONDENCE (entry-protocol tier), WEAK -- consistency, not discrimination. It does NOT build SU(3)
gauge theory (no smuggling); it files that E8 contains A2=su(3) and that the triality is det=3. The
1+3+8=12 arithmetic is NOTED, refused-list discipline applies. Grades per step. `--check` recomputes.
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


# ================================================================ the A2 root system (su(3))
# A2 = {e_i - e_j : i != j, i,j in {1,2,3}}: 6 roots in the sum-zero plane of Z^3, all norm 2.
A2_ROOTS = [(1, -1, 0), (-1, 1, 0), (0, 1, -1), (0, -1, 1), (1, 0, -1), (-1, 0, 1)]


def norm(r):
    return r[0] * r[0] + r[1] * r[1] + r[2] * r[2]


def det2(m):
    """Determinant of a 2x2 matrix [[a,b],[c,d]]."""
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def cyc(r):
    """The cyclic coordinate permutation (a,b,c) -> (c,a,b) -- the Z/3 (triality)."""
    return (r[2], r[0], r[1])


# ---- S.1 su(3) = A2, located in the carrier's E8 -- DERIVED -----------------------------
# dim su(3) = 8 = 6 roots (the A2 hexagon) + 2 rank. The 6 A2 roots {e_i-e_j} all have norm 2. A2 sits
# inside the carrier's E8 (container 12: inner products {-2,-1,0,1,2}, so two roots at -1 generate A2).
all_norm_two = all(norm(r) == 2 for r in A2_ROOTS)
N_ROOTS, RANK = len(A2_ROOTS), 2                         # 6 roots + rank 2
DIM_SU3 = N_ROOTS + RANK                                 # = 8 = the 8 gluons
dim_is_eight = (DIM_SU3 == 8)
s1_ok = all_norm_two and dim_is_eight and N_ROOTS == 6
step("S.1", "su(3) = A2, located in the carrier's E8: 8 = 6 roots + 2 rank; A2 subset E8 (inner product -1)",
     "dim su(3) = 8 = 6 roots (the A2 hexagon {e_i-e_j}, all norm 2) + 2 rank; and A2 sits inside the "
     "carrier's E8 (container 12: E8's inner products are {-2,-1,0,1,2}, so two roots at -1 generate A2 = "
     "su(3))",
     ["12.E.3"],
     "the pipeline's location for the strong force, graded honestly. STEP 1 REQUIREMENT: the strong force "
     "is an SU(3) gauge symmetry -- 8 generators (the 8 gluons), i.e. dim su(3) = 8, rank 2. STEP 2 "
     "LOCATION: su(3)'s root system is A2 -- 6 roots + 2 Cartan (rank) = 8. The 6 A2 roots are {e_i - e_j "
     ": i != j} in the sum-zero plane of Z^3, a hexagon, all of norm 2. Where is A2 in the architecture? "
     "NOT in the quaternionic 2I (that is SU(2), container 28) -- SU(3) is not quaternionic. It is in the "
     "carrier's LARGER structure, E8 (container 12): E8's 240 roots have inner products in {-2,-1,0,1,2} "
     "(12.E.3), and any two roots at inner product -1 (both norm 2) generate an A2 root system, hence an "
     "su(3). So su(3) subset e8 = the carrier. STEP 3/4 CHECK: the 6 A2 roots all have norm 2, and "
     "6 + 2 = 8 = dim su(3) = the gluon count -- kernel-checked; A2 subset E8 via the inner-product -1 "
     "that 12.E.3 proved occurs -- cited. HONESTY (carried into S.3): this location is LESS NATIVE than "
     "weak's (2I IS the carrier, exactly SU(2)) -- E8 contains MANY A2 subsystems, so the embedding is a "
     "CHOICE, not forced. The su(3) is located in the carrier, but not singled out by it. That caveat is "
     "flagged, not hidden.",
     "UNIQUE (A2 = su(3): 6 norm-2 roots + rank 2 = 8; A2 subset E8 via inner-product -1)", "DERIVED",
     {"a2_roots": [list(r) for r in A2_ROOTS], "all_norm_two": all_norm_two,
      "n_roots": N_ROOTS, "rank": RANK, "dim_su3": DIM_SU3, "dim_is_eight": dim_is_eight,
      "a2_subset_e8": "E8's inner products {-2,-1,0,1,2} (12.E.3) include -1; two roots at -1 generate A2",
      "less_native_caveat": "E8 contains many A2's -- the embedding is a CHOICE, less native than 2I subset SU(2)"},
     check="the 6 A2 roots {e_i-e_j} all norm 2; 6+2=8=dim su(3); A2 subset E8 via inner-product -1 (12.E.3)")
assert s1_ok

# ---- S.2 the triality Z/3 = det(A2 Cartan) = 3; resonates with the 3-fold -- DERIVED ----
# The A2 Cartan matrix [[2,-1],[-1,2]] has determinant 3 = |Z(SU(3))| = the color TRIALITY. And the
# cyclic coordinate permutation (a,b,c)->(c,a,b) is a Z/3 that permutes the 6 roots (order 3) -- the
# triality realized on the roots. This 3-fold resonates with the substrate's NATIVE 3-fold: the triadic
# floor (three observers, 00) and the order-3 face sector of 2I (maths-4).
A2_CARTAN = [[2, -1], [-1, 2]]
cartan_det = det2(A2_CARTAN)                             # = 3 = |Z/3| = triality
det_is_three = (cartan_det == 3)
cyc_images = [cyc(r) for r in A2_ROOTS]
cyc_is_permutation = (sorted(cyc_images) == sorted(A2_ROOTS))          # Z/3 maps roots -> roots
cyc_order_three = (all(cyc(cyc(cyc(r))) == r for r in A2_ROOTS)
                   and any(cyc(r) != r for r in A2_ROOTS))              # sigma^3 = id, sigma != id
s2_ok = det_is_three and cyc_is_permutation and cyc_order_three
step("S.2", "the triality Z/3 = det(A2 Cartan) = 3; the cyclic Z/3 permutes the roots (order 3)",
     "the A2 Cartan [[2,-1],[-1,2]] has determinant 3 = |Z(SU(3))| = the color TRIALITY; and the cyclic "
     "coordinate permutation (a,b,c)->(c,a,b) is a Z/3 that permutes the 6 roots (order 3) -- the triality "
     "on the roots; this 3-fold resonates with the substrate's native 3-fold (triadic floor 00 / order-3 "
     "faces of 2I)",
     ["S.1"],
     "the triality, the strong force's most distinctive requirement, and where it touches the substrate's "
     "own 3-fold. STEP 1 REQUIREMENT: SU(3) has a center Z/3 -- the color TRIALITY (3 colors; reps carry "
     "triality 0, +1, -1). STEP 3/4 CHECK: (a) the A2 Cartan matrix [[2,-1],[-1,2]] has determinant 3, "
     "and for SU(n) the Cartan determinant = n = |center| -- so det = 3 = |Z/3| = the triality, "
     "kernel-checked; (b) the triality is realized concretely on the roots by the cyclic permutation of "
     "the three coordinates (a,b,c)->(c,a,b): it maps the 6 A2 roots onto themselves (a permutation) and "
     "has order 3 (sigma^3 = identity, sigma != identity) -- the Z/3, kernel-checked. STEP 2 LOCATION of "
     "the triality: this Z/3 RESONATES with the substrate's NATIVE 3-fold -- the triadic floor (a "
     "distinction is registered by THREE observers, 00) and the order-3 sector of 2I (the 20 triangular "
     "faces, order-3 rotations; maths-4's 'phase requires three'). So the strong force's triality is not "
     "foreign to the substrate: the substrate is 3-fold at its floor. (The det=3 and the Z/3 permutation "
     "are the DERIVED facts; the IDENTIFICATION of this Z/3 with the substrate's specific 3-fold is the "
     "correspondence, S.3 -- resonance, cited in prose, not a premise here.)",
     "UNIQUE (det A2 Cartan = 3 = |Z/3| = triality; the cyclic Z/3 permutes the 6 roots, order 3)",
     "DERIVED",
     {"a2_cartan": A2_CARTAN, "cartan_det": cartan_det, "det_is_three_is_triality": det_is_three,
      "cyclic_permutes_roots": cyc_is_permutation, "cyclic_order_three": cyc_order_three,
      "triality": "det(A2 Cartan) = 3 = |Z(SU(3))| = the color triality (3 colors)",
      "native_3fold_resonance": "resonates with the triadic floor (00, three observers) / the order-3 faces of 2I"},
     check="det[[2,-1],[-1,2]]=3=|Z/3|=triality; the cyclic Z/3 permutes the 6 roots (order 3)")
assert s2_ok

# ---- S.3 the filed entry (through 19): su(3) <-> A2 subset E8 -- POSTULATE ---------------
SM_GAUGE_DIM = 1 + 3 + 8                                 # U(1)+SU(2)+SU(3) = 12 gauge bosons
sm_is_twelve = (SM_GAUGE_DIM == 12)
step("S.3", "THE FILED ENTRY: su(3) <-> A2 subset E8 (correspondence, LESS NATIVE); the SM trio located",
     "filed through the 19 gate: su(3) <-> the A2 root system inside the carrier's E8 (S.1); color "
     "triality Z/3 <-> the substrate's native 3-fold (S.2); 8 gluons <-> the 8-dim adjoint. A "
     "CORRESPONDENCE -- and LESS NATIVE than weak/EM (the E8 embedding is a choice). With 28 (SU(2)) and "
     "29 (U(1)) the SM gauge trio U(1)xSU(2)xSU(3) is now located; 1+3+8=12 is a NOTED check vs the "
     "substrate's 12, NOT a claim",
     ["S.1", "S.2", "12.E.1"],
     "the entry itself, the four parts (19's format), and the HONEST close of the forces trio. SUBSTRATE "
     "SIDE (checked): su(3) = A2 subset E8 (S.1); the triality = det = 3, the Z/3 on the roots (S.2). "
     "PHYSICS SIDE (cited): the strong force is an SU(3) gauge symmetry, 8 gluons, color triality Z/3, "
     "confining. THE CORRESPONDENCE: su(3) <-> A2 subset the carrier's E8; color triality <-> the "
     "substrate's native 3-fold (triadic floor / order-3 faces); 8 gluons <-> the 8-dim adjoint. WHAT "
     "DOES NOT TRAVEL: confinement and asymptotic freedom (the DYNAMICS, S.4), the coupling alpha_s "
     "(S.4), the color REPRESENTATIONS of matter, AND -- the honest caveat -- the SPECIFIC EMBEDDING (E8 "
     "contains many A2 subsystems; this location is a choice, LESS NATIVE than weak's 2I subset SU(2), "
     "which IS the carrier). FALSIFICATION SURFACE: the carrier's E8 must contain A2 = su(3) (it does, "
     "12.E.3) and a Z/3 triality (it does, S.2); if su(3) were not a subalgebra of the carrier, the "
     "correspondence would fail. It PASSES the consistency it asserts, at the E8 (not the quaternion) "
     "level. A CORRESPONDENCE, not a resolution -- WEAK (consistency, not discrimination), like 21/28/29; "
     "quarantined. THE SM TRIO: with 28 (SU(2), the non-abelian vector) and 29 (U(1), the abelian "
     "scalar), the full SM gauge group U(1)xSU(2)xSU(3) is now located in the carrier. A NOTED READING "
     "(not a claim): its dimension 1+3+8 = 12 matches the substrate's central 12 (kissing/icosahedron) -- "
     "but whether that is a FORCED decomposition of the 12 or a coincidence is an OPEN check, and the "
     "refused-list discipline applies (do not fit). Held as a lead, not asserted.",
     "POSTULATE (the filed correspondence su(3) <-> A2 subset E8; less native; the SM trio located)",
     "POSTULATE",
     {"substrate_side": "su(3) = A2 subset E8 (S.1); triality = det = 3, Z/3 on roots (S.2)",
      "physics_side_cited": "the strong force is an SU(3) gauge symmetry, 8 gluons, triality Z/3, confining",
      "correspondence": "su(3) <-> A2 subset E8; triality <-> the native 3-fold; 8 gluons <-> the 8-dim adjoint",
      "what_does_not_travel": "confinement; asymptotic freedom; alpha_s; color reps; AND the specific E8 embedding (a choice)",
      "less_native_than_weak": "E8 has many A2's -- less native than 2I subset SU(2) (which IS the carrier); flagged",
      "falsification_surface": "the carrier's E8 must contain A2=su(3) (12.E.3) and a Z/3 triality (S.2)",
      "sm_trio_located": "with 28 (SU(2)) + 29 (U(1)), the SM group U(1)xSU(2)xSU(3) is located in the carrier",
      "sm_gauge_dim": SM_GAUGE_DIM, "one_plus_three_plus_eight_is_twelve": sm_is_twelve,
      "twelve_is_a_noted_check_not_a_claim": "1+3+8=12 matches the substrate's 12 -- OPEN check, refused-list applies, NOT asserted",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "downstream_premise_use": False},
     check=None)

# ---- S.4 the strong dynamics -- OWED (located) -----------------------------------------
step("S.4", "the strong DYNAMICS (confinement, asymptotic freedom, alpha_s, color reps) is OWED",
     "confinement and asymptotic freedom (the strong DYNAMICS), the coupling alpha_s (a dimensionless "
     "alpha_hat, 27), and the color representations of matter (danger zone) are OWED; located, not closed",
     ["S.3", "27.DA.4"],
     "the residual, located and NOT attempted -- the honest boundary. S.1-S.3 locate the strong gauge "
     "GROUP (SU(3)) and its triality in the carrier's E8, as a correspondence. What remains: (i) "
     "CONFINEMENT and ASYMPTOTIC FREEDOM -- the strong DYNAMICS (the running coupling, the non-abelian "
     "gauge dynamics); (ii) the coupling alpha_s -- a dimensionless coupling, so per container 27 an "
     "alpha_hat quantity the substrate must FORCE not fit, respecting the refused-list; (iii) the color "
     "REPRESENTATIONS of matter -- which substrate objects carry which color -- involving the matter "
     "census, the DANGER ZONE, not attempted. So the strong GROUP and TRIALITY are located (checked, "
     "correspondence, at the E8 level); its DYNAMICS and COUPLING are the forward work, located precisely. "
     "NOT attempted here.",
     "OWED (the strong dynamics: confinement, asymptotic freedom, alpha_s, color reps; located)", "OWED",
     {"present": False,
      "owed": "confinement; asymptotic freedom; the coupling alpha_s; the color representations of matter",
      "alpha_s_is_alpha_hat_type": "a dimensionless coupling -> an alpha_hat to FORCE not fit (27), refused-list",
      "danger_zone": "the color assignments involve the matter census -- NOT attempted",
      "located": "the strong GROUP + TRIALITY are checked (S.1-S.3); the DYNAMICS + COUPLING are forward work",
      "not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="30-strong-su3",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # S.1 -- guarded by the Lean
        a2_roots=[list(r) for r in A2_ROOTS], all_norm_two=all_norm_two,
        n_roots=N_ROOTS, rank=RANK, dim_su3=DIM_SU3, dim_is_eight=dim_is_eight,
        # S.2 -- guarded by the Lean
        cartan_det=cartan_det, det_is_three=det_is_three,
        cyclic_permutes_roots=cyc_is_permutation, cyclic_order_three=cyc_order_three,
        # the SM trio
        sm_gauge_dim=SM_GAUGE_DIM, sm_is_twelve=sm_is_twelve,
        third_force_entry=True,
        finding="the STRONG force located in the carrier's E8 (less native than weak/EM): su(3) = A2 (8 = "
                "6 roots + 2 rank), A2 subset E8 via inner-product -1 (S.1); the triality Z/3 = det(A2 "
                "Cartan) = 3, the cyclic Z/3 permutes the roots, resonating with the substrate's native "
                "3-fold (S.2); the correspondence su(3) <-> A2 subset E8 is filed through 19 (S.3, "
                "POSTULATE, WEAK, embedding is a choice); dynamics + alpha_s OWED (S.4). With 28+29, the SM "
                "trio U(1)xSU(2)xSU(3) is located; 1+3+8=12 vs the substrate's 12 is a NOTED check, not a claim.",
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
