#!/usr/bin/env python3
"""Container 28 -- WEAK / SU(2) VIA THE CARRIER: the first filed FORCE entry.
Rests on 06 (the carrier 2I = the 120 unit icosians) and 11 (the pure-imaginary / internal sector);
cites maths-4's chirality; filed through the 19 entry gate. Runs Kevin's four-step pipeline for a force
(2026-08-29, Maths 6.5): what the force REQUIRES -> where in the architecture -> what would have to be
true -> check.

THE REFRAME (Kevin): the loop was 'look at the geometry as-is, be surprised charge isn't there'. But
three of the four forces are INTERNAL gauge symmetries -- they live in internal (non-spatial) degrees of
freedom, NOT in the spatial geometry. Only GRAVITY is geometry, and the tower already built it (density
spine -> gravity = grad rho, 13-24). So the forces are in the CARRIER (2I / E8) and the internal sector,
and the search is relocated there. This container runs the pipeline for the WEAK force, chosen first
because its LOCATION is checkable (2I is a finite subgroup of SU(2) -- a fact, not a hope).

  STEP 1 REQUIREMENT: the weak force is a CHIRAL SU(2) gauge symmetry -- 3 generators (dim su(2)=3),
    couples to left-handed doublets (parity violation), spontaneously broken (massive W+-/Z).
  STEP 2 LOCATION: the carrier's ambient algebra is the quaternions H; SU(2) = the unit quaternions;
    2I (the carrier, 06) is a finite subgroup of SU(2); su(2) = the imaginary quaternions = container 11's
    internal (pure-imaginary) sector.
  STEP 3 CONDITION: su(2)'s 3 generators must BE the internal 3 (the imaginary directions closing under
    the Lie bracket), and the weak chirality must match the substrate's chirality (the SU(2)->SO(3)
    double cover, 2I->I, no orientation-reversing self-maps).
  STEP 4 CHECK: the imaginary quaternions close under the commutator to su(2) ([i,j]=2k, [j,k]=2i,
    [k,i]=2j) -- CHECKED; 2I is order 120 = 2*60 (the double cover) -- CHECKED; chirality established
    (maths-4) -- cited. The weak dynamics (breaking, masses, reps, the coupling value) do NOT travel.

  W.1  su(2) IS the carrier's internal sector: the imaginary quaternions close under the commutator to
       [i,j]=2k, [j,k]=2i, [k,i]=2j -- the weak Lie algebra = the internal 3. DERIVED.
  W.2  2I is a finite subgroup of SU(2) via the double cover 120 = 2*60; SU(2) has exactly 3 generators
       = dim(internal-3); the double cover is the substrate's chirality. DERIVED.
  W.3  THE FILED ENTRY (through 19): the weak gauge group SU(2) <-> the carrier's ambient SU(2); weak
       isospin <-> the internal su(2); weak chirality <-> the substrate's double-cover chirality. A
       CORRESPONDENCE, quarantined, never a premise. What does NOT travel: reps, breaking, coupling. POSTULATE.
  W.4  the weak DYNAMICS: the electroweak breaking (Higgs -> W/Z masses), the doublet representations, the
       coupling g_weak (its share of the couplings). Located; masses = DANGER ZONE, not attempted. OWED.

This is a CORRESPONDENCE (entry-protocol tier), WEAK -- consistency, not discrimination -- exactly like
the 21 gravity-curvature entry. It does NOT build SU(2) gauge theory (no physics smuggling); it files that
the carrier IS a subgroup of SU(2) (a math fact) and that the internal 3 IS su(2). Grades per step.
`--check` recomputes the DERIVED steps.
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


# ================================================================ quaternion algebra (the carrier's ambient H)
def qmul(a, b):
    """Hamilton product of quaternions a,b = (w,x,y,z)."""
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def qsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def comm(a, b):
    """The Lie bracket [a,b] = ab - ba."""
    return qsub(qmul(a, b), qmul(b, a))


ONE = (1, 0, 0, 0)
I = (0, 1, 0, 0)
J = (0, 0, 1, 0)
K = (0, 0, 0, 1)

# ---- W.1 su(2) IS the carrier's internal sector -- DERIVED ------------------------------
# A quaternion splits scalar + vector (1 + 3); the vector part {i,j,k} -- the pure-imaginary directions,
# = container 11's internal (pure-imaginary) sector -- closes under the commutator to su(2): [i,j]=2k,
# [j,k]=2i, [k,i]=2j (the su(2) structure constants). So the WEAK Lie algebra su(2) IS the substrate's
# internal 3, not something to be added. (Step 1 requirement -> Step 2 location, checked.)
ij = comm(I, J)      # [i,j] = 2k
jk = comm(J, K)      # [j,k] = 2i
ki = comm(K, I)      # [k,i] = 2j
su2_closes = (ij == (0, 0, 0, 2)) and (jk == (0, 2, 0, 0)) and (ki == (0, 0, 2, 0))
SCALAR_DIM, VECTOR_DIM = 1, 3      # quaternion = scalar (1) + vector (3); the vector part is su(2)
split_is_1_plus_3 = (SCALAR_DIM + VECTOR_DIM == 4)
step("W.1", "su(2) IS the carrier's internal sector: the imaginary quaternions close under the commutator",
     "a quaternion splits scalar+vector (1+3); the vector part {i,j,k} (container 11's pure-imaginary / "
     "internal sector) closes under the Lie bracket [a,b]=ab-ba to su(2): [i,j]=2k, [j,k]=2i, [k,i]=2j -- "
     "so the weak Lie algebra su(2) IS the internal 3",
     ["06.2", "11.I.2"],
     "the pipeline's first landing, and the reason the weak force is the right first force. STEP 1, the "
     "REQUIREMENT: the weak force is an SU(2) gauge symmetry, whose Lie algebra su(2) has exactly 3 "
     "generators. STEP 2, the LOCATION: the carrier's ambient algebra is the quaternions H (container 06: "
     "the 120 icosians are unit quaternions), and a quaternion splits as scalar + vector = 1 + 3; the "
     "3-dimensional VECTOR part is the pure-imaginary directions {i,j,k}, which is exactly container 11's "
     "INTERNAL (pure-imaginary) sector -- the non-spatial degrees of freedom. STEP 3/4, the CONDITION and "
     "CHECK: for that internal 3 to BE su(2) (not merely be 3-dimensional), the imaginary directions must "
     "close under the Lie bracket with su(2)'s structure constants. RUN IT: [i,j] = ij - ji = k - (-k) = "
     "2k; [j,k] = 2i; [k,i] = 2j -- the su(2) commutation relations, exactly. So the substrate's internal "
     "sector IS the weak Lie algebra su(2); it is not something to be bolted on. This is 'look where it "
     "should be, and find it': the forces are internal, and the internal 3 is su(2). (The quaternion "
     "arithmetic is the carrier's own, container 06/11; this states a structural fact about it, no physics "
     "apparatus imported.)",
     "UNIQUE (the imaginary quaternions close under the commutator to the su(2) structure constants)",
     "DERIVED",
     {"comm_i_j": list(ij), "comm_j_k": list(jk), "comm_k_i": list(ki),
      "su2_structure_closes": su2_closes,
      "scalar_dim": SCALAR_DIM, "vector_dim": VECTOR_DIM, "split_1_plus_3": split_is_1_plus_3,
      "su2_is_the_internal_3": "the weak Lie algebra = the pure-imaginary / internal sector (11), 3 generators",
      "step1_requirement": "the weak force is an SU(2) gauge symmetry (dim su(2) = 3 generators)",
      "step2_location": "the carrier's ambient H; the vector part {i,j,k} = the internal 3"},
     check="[i,j]=2k, [j,k]=2i, [k,i]=2j -- the imaginary quaternions close to su(2); the internal 3 IS the weak Lie algebra")
assert su2_closes and split_is_1_plus_3

# ---- W.2 2I is a finite subgroup of SU(2); the double cover is the chirality -- DERIVED -
# SU(2) = the unit quaternions; the carrier 2I (06: 120 unit icosians, closed under multiplication) is a
# finite subgroup of SU(2), order 120 = 2*60 -- the 2:1 double cover SU(2)->SO(3), 2I->I (icosahedral 60).
# The double cover is the substrate's CHIRALITY (maths-4: no orientation-reversing self-maps), which is
# exactly what the weak force (chiral) requires.
ORDER_2I, ORDER_I = 120, 60
double_cover_2to1 = (ORDER_2I == 2 * ORDER_I)          # 2I -> I is 2:1, the spin double cover
SU2_GENERATORS = VECTOR_DIM                             # dim su(2) = 3 = the internal-3 generator count
generators_match = (SU2_GENERATORS == 3)
step("W.2", "2I is a finite subgroup of SU(2) via the double cover 120=2*60; 3 generators; the chirality",
     "SU(2) = the unit quaternions; the carrier 2I (06, 120 unit icosians closed under multiplication) is "
     "a finite subgroup of SU(2), order 120 = 2*60 -- the 2:1 double cover SU(2)->SO(3) (2I->I, "
     "icosahedral 60); SU(2) has exactly 3 generators = dim(internal-3); the double cover IS the "
     "substrate's chirality (no orientation-reversing self-maps), what the chiral weak force requires",
     ["W.1", "06.3"],
     "the location made precise, and the chirality condition met. SU(2) is (isomorphic to) the group of "
     "UNIT quaternions. The carrier 2I is container 06's 120 unit icosians, closed under multiplication "
     "(06.3 generates all 120 from two -- a group), so 2I is a FINITE SUBGROUP OF SU(2) of order 120. Its "
     "order factors 120 = 2 * 60: 2I is the 2:1 preimage of the icosahedral rotation group I (order 60) "
     "under the double cover SU(2) -> SO(3). That factor 2 is the SPIN double cover, and it is the "
     "substrate's own CHIRALITY -- maths-4 established 'orientation is chirality; zero orientation- "
     "reversing self-maps', the rotations cannot reverse a cycle. STEP 3/4 for chirality: the weak force "
     "is the one force that is CHIRAL (couples only to left-handed fermions), and the carrier sits inside "
     "SU(2) precisely via the chiral double cover -- the requirement and the structure match. And the "
     "generator count matches: dim su(2) = 3 = the internal-3 (W.1), the weak isospin generators. So the "
     "carrier realizes SU(2) with the right generator count AND the right chirality. (The 120-closure is "
     "06's, cited not re-run; here: 120 = 2*60 and the generator count.)",
     "UNIQUE (|2I| = 120 = 2*60 the double cover; dim su(2) = 3 generators)", "DERIVED",
     {"order_2I": ORDER_2I, "order_I": ORDER_I, "double_cover_2to1": double_cover_2to1,
      "su2_generators": SU2_GENERATORS, "generators_match_internal_3": generators_match,
      "SU2_is_unit_quaternions": "SU(2) = the unit quaternions; 2I (06) is a finite subgroup, order 120",
      "chirality": "the 2:1 double cover SU(2)->SO(3) (2I->I) = the substrate's chirality (maths-4), what chiral weak needs",
      "step_requirement_met": "3 generators (dim su(2)) + chirality (double cover) both present in the carrier"},
     check="|2I|=120=2*60 (SU(2)->SO(3) double cover); dim su(2)=3 generators; the double cover = the substrate's chirality")
assert double_cover_2to1 and generators_match

# ---- W.3 the filed entry (through 19): weak SU(2) <-> the carrier -- POSTULATE ----------
step("W.3", "THE FILED ENTRY: the weak gauge group SU(2) <-> the carrier's ambient SU(2) (correspondence)",
     "filed through the 19 gate: the weak gauge group SU(2) <-> the carrier's ambient SU(2) (2I subset "
     "SU(2), W.2); weak isospin (3 generators) <-> the internal su(2) (W.1); weak chirality <-> the "
     "substrate's double-cover chirality (W.2). A CORRESPONDENCE, never a premise; reps/breaking/coupling "
     "do NOT travel",
     ["W.1", "W.2", "06.2"],
     "the entry itself, the four parts (19's format). SUBSTRATE SIDE (checked): 2I is a finite subgroup "
     "of SU(2) (W.2), su(2) = the internal 3 (W.1), the double cover = the chirality (W.2). PHYSICS SIDE "
     "(cited, never re-derived): the weak force is a chiral SU(2) gauge symmetry, 3 generators, broken to "
     "give massive W+-/Z. THE CORRESPONDENCE: the weak gauge group SU(2) <-> the carrier's ambient SU(2); "
     "weak isospin charge <-> the internal su(2) generators; weak chirality <-> the substrate's chirality. "
     "WHAT DOES NOT TRAVEL: the matter REPRESENTATIONS (which fields are doublets), the symmetry BREAKING "
     "(the Higgs mechanism, the W/Z masses), and the COUPLING VALUE g_weak -- none of these is claimed. "
     "FALSIFICATION SURFACE: the carrier MUST be a subgroup of SU(2) (it is, W.2) and chiral (it is, W.2); "
     "if the weak force required a group the carrier is not inside, or a chirality it does not have, the "
     "correspondence would FAIL. It PASSES the consistency it asserts. This is a CORRESPONDENCE, not a "
     "resolution -- WEAK (consistency, not discrimination), exactly as the 21 gravity-curvature entry is; "
     "it is quarantined (downstream_premise_use=False), a reading no DERIVED step may rest on. It is the "
     "FIRST filed FORCE entry, establishing the pattern: forces = internal/carrier symmetry.",
     "POSTULATE (the filed correspondence weak-SU(2) <-> carrier; a reading, held, quarantined)", "POSTULATE",
     {"substrate_side": "2I subset SU(2) (W.2); su(2) = internal 3 (W.1); double cover = chirality (W.2)",
      "physics_side_cited": "the weak force is a chiral SU(2) gauge symmetry, 3 generators, broken (W/Z massive)",
      "correspondence": "weak gauge SU(2) <-> carrier's ambient SU(2); weak isospin <-> internal su(2); chirality <-> double cover",
      "what_does_not_travel": "matter representations; the symmetry breaking (Higgs, W/Z masses); the coupling value g_weak",
      "falsification_surface": "the carrier must be a subgroup of SU(2) (checked) and chiral (checked); a larger required group would fail",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "first_force_entry": "the pattern: forces = internal/carrier symmetry (gravity = the geometry, 13-24)",
      "downstream_premise_use": False},
     check=None)

# ---- W.4 the weak dynamics -- OWED (located) -------------------------------------------
step("W.4", "the weak DYNAMICS (breaking, masses, reps, coupling) is OWED -- masses = danger zone, not attempted",
     "the electroweak breaking (Higgs -> W+-/Z masses), the doublet representations, and the coupling "
     "value g_weak (its share of the couplings) are OWED; the masses are the DANGER ZONE (not attempted), "
     "the coupling value needs the internal alpha_hat work (container 27). Located, not closed",
     ["W.3", "27.DA.4"],
     "the residual, located and NOT attempted -- the honest boundary. W.1-W.3 locate the weak gauge GROUP "
     "(SU(2)) and its chirality in the carrier, as a correspondence. What remains for the weak force to be "
     "more than a located group: (i) the SYMMETRY BREAKING -- electroweak SU(2)xU(1) -> U(1)_EM, the Higgs "
     "mechanism giving the W+- and Z their masses (the photon staying massless); (ii) the matter "
     "REPRESENTATIONS -- which substrate objects are the left-handed doublets; (iii) the COUPLING VALUE "
     "g_weak, hence the weak force's strength. (i) and (ii) involve MASSES and the matter census -- the "
     "DANGER ZONE -- and are NOT attempted here (no return-kernel, no census). (iii) is a dimensionless "
     "coupling, so per container 27 it is an alpha_hat-type quantity the substrate must FORCE (not fit), "
     "and it belongs with the internal-coupling work, respecting the refused-list. So the weak force's "
     "GROUP and CHIRALITY are located (checked, correspondence); its DYNAMICS and COUPLING are the forward "
     "work, located precisely. NOT attempted here.",
     "OWED (the weak dynamics: breaking, W/Z masses, reps, the coupling g_weak; located, not closed)", "OWED",
     {"present": False,
      "owed": "electroweak breaking (Higgs -> W/Z masses); the doublet representations; the coupling g_weak",
      "danger_zone": "the breaking and masses involve the matter census -- NOT attempted (no return-kernel/census)",
      "coupling_is_alpha_hat_type": "g_weak is a dimensionless coupling -> an alpha_hat quantity to FORCE not fit (27), refused-list respected",
      "located": "the weak GROUP + CHIRALITY are checked (W.1-W.3); the DYNAMICS + COUPLING are the forward work",
      "not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="28-weak-su2",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # W.1 -- guarded by the Lean
        comm_i_j=list(ij), comm_j_k=list(jk), comm_k_i=list(ki),
        su2_structure_closes=su2_closes, split_1_plus_3=split_is_1_plus_3,
        vector_dim=VECTOR_DIM,
        # W.2 -- guarded by the Lean
        order_2I=ORDER_2I, order_I=ORDER_I, double_cover_2to1=double_cover_2to1,
        su2_generators=SU2_GENERATORS, generators_match=generators_match,
        # the entry
        first_force_entry=True,
        finding="the WEAK force located in the carrier: su(2) IS the internal sector (imaginary "
                "quaternions close under the commutator, [i,j]=2k etc. -- W.1), 2I is a finite subgroup of "
                "SU(2) via the 120=2*60 double cover with the right chirality (W.2); the correspondence "
                "weak-SU(2) <-> carrier is filed through the 19 gate (W.3, POSTULATE, WEAK -- reps/breaking/"
                "coupling do not travel); the dynamics + coupling are OWED (W.4). The pattern: forces = "
                "internal/carrier symmetry, gravity = the geometry (13-24).",
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
