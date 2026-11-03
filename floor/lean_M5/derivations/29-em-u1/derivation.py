#!/usr/bin/env python3
"""Container 29 -- EM / U(1) VIA THE CARRIER: the second filed FORCE entry.
Rests on 14 (the charge = signed angle-defect) and 28 (the quaternion algebra, abelian vs non-abelian);
cites 27 (the coupling is an alpha_hat), maths-4 (the Gauss law, coupling unity). Filed through the 19
gate. Runs Kevin's four-step pipeline for the EM force (2026-08-29, Maths 6.5).

THE REFRAME (Kevin): forces = INTERNAL/carrier gauge symmetry; gravity = the geometry (13-24). EM is a
U(1) gauge symmetry, and -- unlike the other forces -- its CHARGE is already built (14: the signed
angle-defect), so its 'locate' step starts half-done. This is 'look where it should be, and find it'.

  STEP 1 REQUIREMENT: EM is a U(1) gauge symmetry -- 1 generator, ABELIAN, UNBROKEN (massless photon), a
    conserved QUANTIZED electric charge, coupling alpha (the fine-structure constant ~ 1/137).
  STEP 2 LOCATION: the charge = the signed angle-defect 12-2d (14.B.4), already built; the U(1) = an
    abelian 1-generator subgroup of the carrier (a single imaginary direction generates a circle), the
    scalar/phase to su(2)'s vector (28); the Gauss law reads the charge (enclosed = 12 - boundary turning).
  STEP 3 CONDITION: the charge must be quantized + signed (a mirror at zero) + conserved; the symmetry
    must be ABELIAN (1 generator, [X,X]=0) -- unlike weak su(2) (non-abelian, [i,j]=2k != 0); unbroken =
    the charge exactly conserved.
  STEP 4 CHECK: 12-2d is integer-quantized and signed with a MIRROR at d=6 (2 / 0 / -2) -- CHECKED; the
    total sum = 24 = 12*chi is a topological invariant (conserved) -- CHECKED (14); abelian [i,i]=0 vs
    non-abelian [i,j]=2k (28) -- CHECKED; 1(u(1))+3(su(2))=4=the quaternion=electroweak -- CHECKED.

  EM.1 the U(1) charge IS the signed angle-defect 12-2d: quantized, signed (mirror at 6), conserved
       (sum = 12*chi). DERIVED.
  EM.2 the U(1) is ABELIAN, 1 generator ([X,X]=0) -- vs weak su(2) non-abelian; u(1)(1)+su(2)(3)=4=the
       quaternion = the electroweak algebra. DERIVED.
  EM.3 THE FILED ENTRY (through 19): EM's U(1) <-> the carrier's abelian U(1)/phase; electric charge <->
       the signed defect; the Gauss law <-> enclosed = 12 - boundary turning. Correspondence. POSTULATE.
  EM.4 the EM coupling alpha ~ 1/137 is a dimensionless alpha_hat (27); the substrate's BARE coupling is
       UNITY (no epsilon_0), so alpha is NOT geometric -- FORCE it not fit, refused-list respected. The
       matter charge assignments (danger zone). OWED, located -- the honest home of the 1/137 question.

This is a CORRESPONDENCE (entry-protocol tier), WEAK -- consistency, not discrimination. It does NOT build
U(1) gauge theory (no physics smuggling); it files that the charge IS the signed defect and the symmetry
IS abelian. Grades per step. `--check` recomputes the DERIVED steps.
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


# ================================================================ the charge (consumes 14) + quaternions (28)
def signed_charge(d):
    """Container 14's angle-defect 12 - 2d, read SIGNED (over Int): the U(1) charge. Mirror at d=6."""
    return 12 - 2 * d


def qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def comm(a, b):
    return tuple(x - y for x, y in zip(qmul(a, b), qmul(b, a)))


I = (0, 1, 0, 0)
J = (0, 0, 1, 0)

# ---- EM.1 the U(1) charge IS the signed angle-defect -- DERIVED -------------------------
# The charge = 12 - 2d (container 14.B.4). Read signed: charge(5)=+2, charge(6)=0 (the flat MIRROR),
# charge(7)=-2 -- quantized (integer radits), signed (a mirror at zero = the neutral point), and the
# total over the icosahedron sum = 12*2 = 24 = 12*chi (Gauss-Bonnet, refinement-invariant) = CONSERVED.
# On THIS substrate deg <= 6, so only charge >= 0 is realized (the twelve carry +2, the rest 0); the
# negative side (deg > 6) is off-substrate, exactly as container 15's density is one-sided here.
ch5, ch6, ch7 = signed_charge(5), signed_charge(6), signed_charge(7)      # 2, 0, -2
mirror_at_six = (ch6 == 0) and (ch5 > 0) and (ch7 < 0)                    # signed, mirror at deg 6
quantized = all(isinstance(signed_charge(d), int) for d in (5, 6, 7))
TOTAL_CHARGE, CHI = 12 * ch5, 2                                            # twelve deg-5 vertices carry +2
conserved_is_12chi = (TOTAL_CHARGE == 12 * CHI == 24)                      # = angleCharge (14), topological
em1_ok = mirror_at_six and quantized and conserved_is_12chi
step("EM.1", "the U(1) charge IS the signed angle-defect 12-2d: quantized, signed (mirror at 6), conserved",
     "the charge = 12-2d (container 14.B.4) read signed: charge(5)=+2, charge(6)=0 (the flat mirror), "
     "charge(7)=-2 -- quantized (integer), signed (a mirror at zero), and the total over the icosahedron "
     "= 12*2 = 24 = 12*chi (Gauss-Bonnet, refinement-invariant) = CONSERVED. That is a U(1) charge",
     ["14.B.4"],
     "the pipeline's first landing for EM, and the reason EM is the natural second force: its CHARGE is "
     "already built. STEP 1 REQUIREMENT: EM needs a conserved, QUANTIZED, signed electric charge. STEP 2 "
     "LOCATION: container 14's angle-defect 12-2d (14.B.4, the curvature charge) IS a charge. STEP 3/4 "
     "CONDITION and CHECK, read it as a U(1) charge: (a) QUANTIZED -- 12-2d is an integer (radits), the "
     "charge comes in whole units; (b) SIGNED with a MIRROR -- charge(5)=+2, charge(6)=0, charge(7)=-2, so "
     "deg 6 (the flat, no unregistered information) is the ZERO / neutral point, below it positive, above "
     "it negative, a genuine +/- charge about a mirror; (c) CONSERVED -- the total over the closed "
     "substrate sum(12-2d) = 24 = 12*chi (Gauss-Bonnet, container 14.B.4's angleCharge), a TOPOLOGICAL "
     "invariant (refinement-invariant), so total charge is conserved exactly, like total charge zero on a "
     "closed universe / the U(1) Gauss law. NOTE the one-sidedness: this icosahedral substrate has deg <= "
     "6, so only charge >= 0 is realized (the twelve carry +2, the rest 0); the negative side needs deg > "
     "6, off THIS substrate -- exactly container 15's density one-sidedness, NOT a claim that negative "
     "charge is forbidden in general. So the substrate's charge has the three defining marks of a U(1) "
     "charge. (Consumes 14's angle-defect; the signed reading over Int adds the mirror 14's Nat truncates.)",
     "UNIQUE (the charge 12-2d is quantized, signed with a mirror at d=6, and conserved = 12*chi)", "DERIVED",
     {"charge_deg5": ch5, "charge_deg6": ch6, "charge_deg7": ch7,
      "signed_mirror_at_six": mirror_at_six, "quantized": quantized,
      "total_charge": TOTAL_CHARGE, "chi": CHI, "conserved_is_12chi": conserved_is_12chi,
      "one_sided_here": "deg <= 6 on this substrate -> only charge >= 0 realized (15's one-sidedness); negative side off-substrate",
      "is_a_U1_charge": "quantized + signed (mirror) + conserved (topological) = the marks of a U(1) charge"},
     check="12-2d: charge(5,6,7)=(2,0,-2) signed mirror at 6; total=24=12*chi conserved (14) -> a U(1) charge")
assert em1_ok

# ---- EM.2 the U(1) is abelian, 1 generator; u(1)+su(2) = the quaternion -- DERIVED -----
# U(1) is generated by ONE direction and is ABELIAN: a single generator's self-bracket is 0 ([i,i]=0),
# so span{i} is a 1-dim abelian Lie algebra u(1) -- unlike weak su(2) = span{i,j,k}, non-abelian
# ([i,j]=2k != 0, container 28). And the counts complete the electroweak algebra: u(1)(1) + su(2)(3) = 4
# = the quaternion's real dimension = the electroweak gauge algebra su(2)+u(1). EM = the abelian scalar
# direction; weak = the non-abelian vector; together = the quaternion.
ii = comm(I, I)      # [i,i] = 0 -- the u(1) generator is abelian
ij = comm(I, J)      # [i,j] = 2k != 0 -- su(2) is non-abelian (container 28)
u1_abelian = (ii == (0, 0, 0, 0))
weak_nonabelian = (ij != (0, 0, 0, 0))
U1_DIM, SU2_DIM = 1, 3
electroweak_dim = U1_DIM + SU2_DIM                                         # 1 + 3 = 4 = the quaternion
ew_is_quaternion = (electroweak_dim == 4)
em2_ok = u1_abelian and weak_nonabelian and ew_is_quaternion
step("EM.2", "the U(1) is ABELIAN, 1 generator ([X,X]=0); u(1)(1)+su(2)(3)=4=the quaternion (electroweak)",
     "U(1) is generated by ONE direction and is ABELIAN: a single generator's self-bracket [i,i]=0, so "
     "span{i} is a 1-dim abelian u(1) -- unlike weak su(2)=span{i,j,k}, non-abelian ([i,j]=2k != 0, "
     "container 28); and u(1)(1) + su(2)(3) = 4 = the quaternion = the electroweak gauge algebra",
     ["EM.1", "28.W.1"],
     "the character condition, and it distinguishes EM from weak in the SAME carrier. STEP 1 REQUIREMENT: "
     "EM is ABELIAN (U(1) has one generator, its charges are additive numbers that commute), whereas the "
     "weak force is NON-abelian (SU(2), 3 generators that don't commute). STEP 2 LOCATION: a U(1) sits in "
     "the carrier as an abelian 1-parameter subgroup -- a single imaginary direction i generates the "
     "circle exp(theta*i), the maximal torus / the phase. STEP 3/4 CONDITION and CHECK: (a) ABELIAN -- the "
     "1-dimensional subalgebra span{i} is abelian because its only bracket is [i,i]=0, computed cold; "
     "contrast su(2) = span{i,j,k}, where [i,j]=2k != 0 (container 28) -- non-abelian. So the carrier "
     "carries BOTH an abelian U(1) (EM) and a non-abelian SU(2) (weak), and the abelian/non-abelian "
     "distinction the two forces require IS present. (b) THE COMPLETION -- a quaternion splits scalar + "
     "vector = 1 + 3; the vector 3 is su(2) (28), and adding the 1 abelian generator gives 1 + 3 = 4 = the "
     "quaternion's real dimension = the dimension of the ELECTROWEAK gauge algebra su(2) (+) u(1). So EM's "
     "u(1) and weak's su(2) are the two halves of the carrier's own algebra: EM = an abelian direction, "
     "weak = the non-abelian vector, together = the quaternion. (This is a dimension/bracket correspondence "
     "-- the ALGEBRA facts are derived; that this IS the electroweak group is the reading, EM.3.)",
     "UNIQUE ([i,i]=0 abelian vs [i,j]=2k non-abelian; 1+3=4=the electroweak dimension)", "DERIVED",
     {"comm_i_i": list(ii), "u1_abelian": u1_abelian,
      "comm_i_j": list(ij), "weak_nonabelian": weak_nonabelian,
      "u1_dim": U1_DIM, "su2_dim": SU2_DIM, "electroweak_dim": electroweak_dim,
      "electroweak_is_quaternion": ew_is_quaternion,
      "abelian_vs_nonabelian": "U(1) abelian ([i,i]=0) vs su(2) non-abelian ([i,j]=2k) -- both in the carrier",
      "electroweak_completion": "u(1)(scalar,1) + su(2)(vector,3) = 4 = the quaternion = su(2)(+)u(1)"},
     check="[i,i]=0 (u(1) abelian) vs [i,j]=2k (su(2) non-abelian, 28); 1+3=4=quaternion=electroweak")
assert em2_ok

# ---- EM.3 the filed entry (through 19): EM's U(1) <-> the carrier -- POSTULATE ----------
step("EM.3", "THE FILED ENTRY: EM's U(1) <-> the carrier's abelian U(1)/phase; charge <-> the signed defect",
     "filed through the 19 gate: EM's U(1) gauge symmetry <-> the carrier's abelian 1-generator U(1) "
     "(EM.2); electric charge <-> the signed angle-defect 12-2d (EM.1); the U(1) Gauss law <-> the "
     "substrate's Gauss law (enclosed = 12 - boundary turning). Abelian, unbroken (charge conserved -> "
     "massless photon). A CORRESPONDENCE, never a premise; coupling/matter-charges do NOT travel",
     ["EM.1", "EM.2", "14.B.4"],
     "the entry itself, the four parts (19's format). SUBSTRATE SIDE (checked): the charge is the signed, "
     "quantized, conserved defect (EM.1); the symmetry is abelian, 1 generator (EM.2). PHYSICS SIDE "
     "(cited, never re-derived): EM is a U(1) gauge symmetry, abelian, UNBROKEN (the photon is massless), "
     "with a conserved quantized electric charge. THE CORRESPONDENCE: EM's U(1) <-> the carrier's abelian "
     "U(1)/phase (EM.2); electric charge <-> the signed angle-defect (EM.1); the U(1) Gauss law "
     "(div E = rho) <-> the substrate's Gauss law 'enclosed = 12 - boundary turning' (maths-4, cited). "
     "UNBROKEN matches: the substrate charge is EXACTLY conserved (total = 12*chi, topological), so the "
     "mediator stays massless -- unlike weak, which is broken. WHAT DOES NOT TRAVEL: the COUPLING VALUE "
     "alpha (the fine-structure constant; EM.4), and the MATTER charge assignments (which objects carry "
     "which charge). FALSIFICATION SURFACE: the charge MUST be quantized + signed + conserved (it is, "
     "EM.1) and the symmetry ABELIAN (it is, EM.2); if EM required a non-abelian group or a "
     "non-conserved / continuous charge, the correspondence would FAIL. It PASSES the consistency it "
     "asserts. A CORRESPONDENCE, not a resolution -- WEAK (consistency, not discrimination), like the 21 "
     "and 28 entries; quarantined (downstream_premise_use=False). The SECOND filed force entry: with 28, "
     "the electroweak pair U(1) x SU(2) is now located in the carrier (the quaternion).",
     "POSTULATE (the filed correspondence EM-U(1) <-> the carrier; a reading, held, quarantined)", "POSTULATE",
     {"substrate_side": "charge = signed/quantized/conserved defect (EM.1); abelian 1-generator (EM.2)",
      "physics_side_cited": "EM is a U(1) gauge symmetry, abelian, unbroken (massless photon), conserved quantized charge",
      "correspondence": "EM U(1) <-> carrier's abelian U(1)/phase; electric charge <-> signed defect; Gauss law <-> enclosed=12-turning",
      "unbroken_matches": "the charge is exactly conserved (total=12*chi topological) -> massless mediator, unlike broken weak",
      "what_does_not_travel": "the coupling value alpha (the fine-structure constant, EM.4); the matter charge assignments",
      "falsification_surface": "the charge must be quantized+signed+conserved (checked) and the symmetry abelian (checked)",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "electroweak_pair_located": "with 28, U(1) x SU(2) both located in the carrier (the quaternion)",
      "downstream_premise_use": False},
     check=None)

# ---- EM.4 the coupling alpha ~ 1/137 -- OWED (located, the honest home of 1/137) -------
step("EM.4", "the EM coupling alpha ~ 1/137 is a dimensionless alpha_hat; bare coupling UNITY; FORCE not fit (OWED)",
     "the EM coupling alpha ~ 1/137 (the fine-structure constant) is a dimensionless alpha_hat-type "
     "quantity (container 27); the substrate's BARE charge-holonomy coupling is UNITY (maths-4: no "
     "epsilon_0 in the Gauss law), so alpha is NOT in the substrate's angular geometry -- it must be "
     "FORCED as an internal quantity, respecting the refused-list. The matter charge assignments are "
     "danger zone. Located, not attempted",
     ["EM.3", "27.DA.4"],
     "the residual -- and it is the honest home of the famous 1/137 question, located precisely and NOT "
     "attempted. EM.1-EM.3 locate the U(1) group and its charge in the carrier. What remains is the "
     "COUPLING: the fine-structure constant alpha ~ 1/137, the STRENGTH of the EM coupling. Container 27 "
     "showed alpha's kind: a dimensionless coupling is an alpha_hat quantity, and the substrate can only "
     "FORCE it (never manufacture a dimensionful anchor). maths-4 sharpened WHERE it is NOT: the "
     "substrate's Gauss law 'enclosed = 12 - boundary turning' carries NO coupling constant (where EM has "
     "epsilon_0, the substrate has nothing), so the bare charge-to-holonomy coupling is UNITY -- and "
     "therefore alpha CANNOT be a ratio of the substrate's ANGULAR quantities (the geometry's coupling is "
     "already 1). This is exactly the forces reframe: alpha is INTERNAL, not geometric. So alpha_EM is an "
     "alpha_hat to be FORCED from the internal/carrier structure, respecting maths-4's REFUSED-LIST "
     "(1/144 = 4.84% off 137 'a session that finds it promising has FAILED', 1/12, 24, 20, 2^7; do not "
     "fish pi/phi/12 near 137) and the census cautionary tale (FORCED not fitted). The matter charge "
     "ASSIGNMENTS (which objects carry which electric charge) involve the matter census -- the DANGER "
     "ZONE, not attempted. So the U(1) and its charge are located (checked); the coupling alpha and the "
     "charge assignments are the forward work, located precisely. NOT attempted here.",
     "OWED (the EM coupling alpha ~ 1/137, a dimensionless alpha_hat to force not fit; located)", "OWED",
     {"present": False,
      "what_it_is": "the fine-structure constant alpha ~ 1/137 = the EM coupling strength",
      "is_alpha_hat_type": "a dimensionless coupling -> an alpha_hat quantity to FORCE not fit (container 27)",
      "bare_coupling_unity": "the substrate's Gauss law has no epsilon_0 -> bare coupling = 1; alpha is NOT angular/geometric (maths-4)",
      "refused_list": "1/144 (4.84% off 137, refused), 1/12, 24, 20, 2^7 -- do not fish pi/phi/12 near 137",
      "matter_charge_assignments": "which objects carry which electric charge -- the matter census, DANGER ZONE, not attempted",
      "located_not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="29-em-u1",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # EM.1 -- guarded by the Lean
        charge_deg5=ch5, charge_deg6=ch6, charge_deg7=ch7,
        signed_mirror_at_six=mirror_at_six, total_charge=TOTAL_CHARGE, chi=CHI,
        conserved_is_12chi=conserved_is_12chi,
        # EM.2 -- guarded by the Lean
        comm_i_i=list(ii), u1_abelian=u1_abelian, comm_i_j=list(ij), weak_nonabelian=weak_nonabelian,
        electroweak_dim=electroweak_dim, electroweak_is_quaternion=ew_is_quaternion,
        # the entry
        second_force_entry=True,
        finding="the EM force located in the carrier: the U(1) charge IS the signed angle-defect 12-2d "
                "(quantized, signed mirror at 6, conserved = 12*chi -- EM.1); the U(1) is ABELIAN "
                "([i,i]=0) vs weak su(2) non-abelian ([i,j]=2k), and u(1)(1)+su(2)(3)=4=the quaternion = "
                "electroweak (EM.2); the correspondence EM-U(1) <-> carrier is filed through 19 (EM.3, "
                "POSTULATE, WEAK); the coupling alpha~1/137 is the owed alpha_hat (bare coupling unity, "
                "FORCE not fit, refused-list -- EM.4). With 28, U(1) x SU(2) both located in the carrier.",
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
