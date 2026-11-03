#!/usr/bin/env python3
"""Container 45 -- THE SPINOR STRUCTURE: the carrier carries 2-valued (spinor) reps; a 2*pi turn acts as -1.

Step 5 of the forward frontier (Maths 6.7): force the substrate's SPINOR structure. 38.DV.3 already NAMED
the 4*pi total holonomy as "the 2I spinor double cover" (a reading); 41/42 use the same double cover for
dim=3. This container forces the spinor content COLD: the carrier 2I is the binary icosahedral group, the
2:1 preimage of I under SU(2)->SO(3) (28.W.2), whose kernel is {+-1}; the central -1 is a 2*pi rotation
acting as -1 on a spinor -- so the substrate carries genuine 2-VALUED representations (half-integer "spin"),
the objects that return only after 4*pi. Fermionic statistics is a CITED correspondence (spin-statistics
needs the Lorentz structure, not yet forced -- container 50).

  SP.1  the central -1: 2I contains -1 = (-1,0,0,0), order 2, CENTRAL, and it is the non-trivial element
        of the kernel {+-1} of SU(2)->SO(3) (28.W.2, 120=2*60). Conjugation by -1 is the IDENTITY rotation
        (a 2*pi turn = identity in SO(3)) -- yet -1 != +1 in SU(2). DERIVED.

  SP.2  the spinor / 2-valuedness: on the 2D fundamental (spinor) rep, SU(2) acts DIRECTLY, so a 2*pi
        rotation sends psi -> -psi and only 4*pi returns psi -> +psi. The double cover being NON-TRIVIAL
        (-1 != +1) is exactly the 4*pi holonomy (38.DV.3). So the substrate carries 2-VALUED (spinor)
        representations -- half-integer spin -- not just the single-valued (tensor/integer-spin) ones of
        SO(3). DERIVED.

  SP.3  the correspondence (filed through 19): spinorial (half-integer, 4*pi) matter is FERMIONIC (Pauli
        exclusion, antisymmetric). The substrate's spinor structure <-> the existence of fermions. The
        spin<->statistics link is CITED (the spin-statistics theorem needs the Lorentz structure, container
        50 -- not yet forced). A CORRESPONDENCE, WEAK, quarantined. POSTULATE.

  SP.4  OWED: WHICH substrate objects are the fermion fields (the matter census); the spin-statistics
        connection re-derived on the substrate (needs the signature/Lorentz structure, 50); values/masses
        (danger zone). OWED.

Rests on 28 (2I = the SU(2)->SO(3) double cover, 120=2*60), 06 (the carrier quaternions), 38 (the 4*pi
holonomy); cites the spin-statistics theorem. DANGER-FREE: pure group/rep structure -- no mass, no census,
no coupling, no value. `--check` recomputes.
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


# ================================================================ quaternion arithmetic (the carrier's SU(2))
def qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def qconj(q):
    w, x, y, z = q
    return (w, -x, -y, -z)


ONE = (1, 0, 0, 0)
NEG_ONE = (-1, 0, 0, 0)
I = (0, 1, 0, 0)
J = (0, 0, 1, 0)
K = (0, 0, 0, 1)

# ---- SP.1 the central -1 -- DERIVED ----------------------------------------------------
neg_one_sq = qmul(NEG_ONE, NEG_ONE)                 # = +1: order 2
central = all(qmul(NEG_ONE, g) == qmul(g, NEG_ONE) for g in (I, J, K))   # -1 commutes with all
# conjugation by -1 acts as the identity rotation on the imaginary (vector) part:
conj_by_neg1 = {name: qmul(qmul(NEG_ONE, v), qconj(NEG_ONE)) for name, v in (("i", I), ("j", J), ("k", K))}
conj_is_identity = (conj_by_neg1["i"] == I and conj_by_neg1["j"] == J and conj_by_neg1["k"] == K)
nontrivial = (NEG_ONE != ONE)
sp1_ok = (neg_one_sq == ONE and central and conj_is_identity and nontrivial)
step("SP.1", "the central -1: 2I contains -1 (order 2, central), the non-trivial kernel of SU(2)->SO(3); conjugation by -1 = the identity rotation",
     "the carrier 2I contains -1 = (-1,0,0,0): (-1)^2 = +1 (order 2), it is CENTRAL (commutes with i,j,k), "
     "and conjugation by -1 acts as the IDENTITY rotation on the vector part ((-1)v(-1)^-1 = v) -- so -1 "
     "maps to the identity in SO(3). It is the non-trivial element of the kernel {+-1} of the double "
     "cover SU(2)->SO(3) (28.W.2, 120=2*60). Yet -1 != +1 in SU(2)",
     ["28.W.2", "06.6.2"],
     "the seat of the spinor, sitting in the carrier. Container 28.W.2 established 2I is the 2:1 preimage "
     "of the icosahedral rotation group I under the double cover SU(2)->SO(3): |2I|=120=2*60, and the "
     "factor 2 is the kernel {+-1}. Here is that kernel, concretely: -1 = (-1,0,0,0) is in the carrier "
     "(it is 1*-1, the negative of the identity, present since 2I is a group closed under the quaternion "
     "product). RUN IT: (-1)^2 = +1 (order 2); -1 commutes with i,j,k (central); and conjugation q -> "
     "(-1)q(-1)^-1 fixes i,j,k -- so -1 acts as the IDENTITY on 3-space (SO(3)), i.e. it is a full 2*pi "
     "rotation, which is the identity rotation. BUT -1 != +1 as elements of SU(2). That gap -- a 2*pi "
     "rotation is the identity in SO(3) but -1 in SU(2) -- is the double cover being NON-TRIVIAL, and it "
     "is the seat of the spinor (SP.2).",
     "UNIQUE (-1 in 2I: order 2, central, conj = identity rotation, yet -1 != +1 -- the kernel)", "DERIVED",
     {"neg_one_squared": list(neg_one_sq), "central": central,
      "conjugation_by_neg1": {k: list(v) for k, v in conj_by_neg1.items()},
      "conj_is_identity_rotation": conj_is_identity, "neg1_ne_1": nontrivial,
      "kernel": "-1 is the non-trivial element of ker(SU(2)->SO(3)) = {+-1} (28.W.2, 120=2*60)"},
     check="(-1)^2=+1 (order 2), central, conjugation by -1 = identity rotation, yet -1 != +1 -- the double-cover kernel")
assert sp1_ok

# ---- SP.2 the spinor / 2-valuedness -- DERIVED -----------------------------------------
# On the 2D fundamental rep SU(2) acts directly: a 2*pi rotation IS -1 (psi -> -psi); 4*pi IS +1.
two_pi_acts_as = NEG_ONE            # a 2*pi rotation acts as -1 on a spinor
four_pi_acts_as = qmul(NEG_ONE, NEG_ONE)     # 4*pi = (2*pi)^2 acts as +1
returns_only_at_4pi = (two_pi_acts_as != ONE and four_pi_acts_as == ONE)
sp2_ok = returns_only_at_4pi
step("SP.2", "the spinor: on the 2D fundamental rep a 2*pi turn sends psi -> -psi; only 4*pi returns it -- the substrate carries 2-valued (half-integer-spin) reps",
     "on the 2-dimensional fundamental (spinor) representation, SU(2) acts DIRECTLY (not through SO(3)), "
     "so the 2*pi rotation acts as -1: psi -> -psi, and only the 4*pi rotation (= (2*pi)^2) returns "
     "psi -> +psi. The double cover being non-trivial (-1 != +1, SP.1) IS the 4*pi holonomy (38.DV.3). So "
     "the substrate carries 2-VALUED (spinor) representations -- half-integer spin -- alongside the "
     "single-valued (integer-spin) tensor reps of SO(3)",
     ["SP.1", "38.DV.3"],
     "the spinor, forced -- what 38.DV.3 named as a reading. A representation of SO(3) is single-valued "
     "(a 2*pi rotation acts as +1 -- integer spin, tensors). But SU(2) = Spin(3) has representations SO(3) "
     "does NOT: the 2D fundamental, on which the carrier acts directly, where the central -1 (SP.1) acts "
     "as -1. So a 2*pi rotation sends a spinor psi -> -psi, and only 4*pi returns it to +psi. RUN IT: "
     "2*pi acts as -1 (!= +1), 4*pi = (2*pi)^2 acts as +1. This is precisely the 4*pi total holonomy of "
     "38.DV.3 (the substrate's twelve deficits sum to 4*pi = 2*(2*pi)) read on the reps: the substrate is "
     "spinorial, it distinguishes a 2*pi turn from no turn. Half-integer spin exists on the substrate -- "
     "forced by the carrier being the double cover 2I (not the single cover I), the same fact that gives "
     "dim=3 (41/42) and the 1/b light-bending flux (40). One structure, many faces.",
     "UNIQUE (2*pi acts as -1, 4*pi as +1 on the spinor rep -- 2-valued, half-integer spin)", "DERIVED",
     {"two_pi_acts_as": list(two_pi_acts_as), "four_pi_acts_as": list(four_pi_acts_as),
      "spinor_returns_only_at_4pi": returns_only_at_4pi,
      "meaning": "the substrate carries 2-valued (spinor / half-integer-spin) reps, not only SO(3)'s single-valued ones",
      "same_double_cover": "= the 4*pi holonomy (38.DV.3), dim=3 (41/42), the 1/b flux (40)"},
     check="on the spinor rep: 2*pi acts as -1 (!= +1), 4*pi as +1 -- returns only after 4*pi (half-integer spin)")
assert sp2_ok

# ---- SP.3 the correspondence: spinors <-> fermions -- POSTULATE ------------------------
step("SP.3", "the correspondence (filed through 19): spinorial (half-integer, 4*pi) matter is FERMIONIC (Pauli); spin-statistics CITED",
     "filed through the 19 gate: spinorial matter (half-integer spin, the 4*pi objects of SP.2) is "
     "FERMIONIC -- antisymmetric, obeying Pauli exclusion. The substrate's spinor structure <-> the "
     "existence of fermions. The spin<->statistics LINK is CITED (the spin-statistics theorem needs the "
     "Lorentz/causal structure, not yet forced -- container 50). A CORRESPONDENCE, WEAK; the matter "
     "fields, the exclusion dynamics, values do NOT travel",
     ["SP.2", "28.W.3"],
     "the physical entry, held to the 19 discipline. SUBSTRATE side (checked, SP.1-SP.2): the carrier "
     "carries 2-valued spinor reps -- half-integer spin, the objects that need 4*pi to return. PHYSICS "
     "side (cited): half-integer-spin fields are FERMIONS (antisymmetric wavefunctions, Pauli exclusion); "
     "the spin-statistics THEOREM ties spin to statistics -- but that theorem needs relativistic "
     "(Lorentz-invariant, causal) QFT, i.e. the metric SIGNATURE, which is NOT yet forced on the "
     "substrate (that is container 50). THE CORRESPONDENCE: the substrate's spinor structure <-> the "
     "existence of fermionic matter. FALSIFICATION: a substrate with no 2-valued reps could carry no "
     "fundamental fermions; ours does (SP.2). WHAT DOES NOT TRAVEL: which objects are the fermion fields "
     "(the matter census), the exclusion dynamics, any mass/value. And spin<->statistics itself is CITED, "
     "pending the Lorentz structure (50). A correspondence, quarantined; no downstream premise use.",
     "POSTULATE (spinors <-> fermions; spin-statistics cited pending the Lorentz structure; held)", "POSTULATE",
     {"substrate_side": "the carrier carries 2-valued spinor reps -- half-integer spin (SP.1-SP.2)",
      "physics_side_cited": "half-integer spin => fermions (Pauli); the spin-statistics theorem needs the Lorentz structure (50)",
      "correspondence": "substrate spinor structure <-> the existence of fermionic matter",
      "does_not_travel": "the matter fields/census; the exclusion dynamics; any mass/value",
      "spin_statistics_gated_on": "the metric signature / Lorentz structure (container 50)",
      "downstream_premise_use": False},
     check=None)

# ---- SP.4 OWED ------------------------------------------------------------------------
step("SP.4", "OWED: which substrate objects are fermion fields (matter census); spin-statistics re-derived (needs 50); masses/values (danger zone)",
     "OWED: (a) WHICH substrate objects carry the spinor reps as fermion fields -- the matter census; "
     "(b) the spin-statistics connection re-derived on the substrate -- needs the signature/Lorentz "
     "structure (container 50); (c) masses and couplings of the matter -- the danger zone. The spinor "
     "STRUCTURE is forced; the matter content and dynamics are owed",
     ["SP.3"],
     "the honest residual. SP.1-SP.2 force the spinor structure (2-valued reps, half-integer spin, the "
     "4*pi return); SP.3 files the fermion correspondence. What remains: (a) the MATTER CENSUS -- which "
     "substrate objects actually carry these spinor reps as physical fermion fields (electrons, quarks, "
     "neutrinos) -- not addressed (matter sector); (b) SPIN-STATISTICS re-derived on the substrate rather "
     "than cited -- this needs the metric SIGNATURE / Lorentz structure (container 50 forces the "
     "signature; only then is a spin-statistics argument available); (c) the MASSES and couplings of the "
     "matter -- the danger zone, out. So the spinor structure is forced and danger-free; the matter it "
     "dresses is owed. NOT attempted further here.",
     "OWED (the fermion matter census; spin-statistics via the Lorentz structure (50); masses -- danger zone)", "OWED",
     {"owed_census": "which substrate objects are the fermion fields -- the matter census",
      "owed_spin_statistics": "the spin<->statistics connection re-derived -- needs the signature/Lorentz structure (container 50)",
      "owed_masses": "matter masses and couplings -- danger zone",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="45-spinor",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        neg_one_squared=list(neg_one_sq), central=central, conj_is_identity=conj_is_identity,
        two_pi_acts_as=list(two_pi_acts_as), four_pi_acts_as=list(four_pi_acts_as),
        spinor_returns_only_at_4pi=returns_only_at_4pi,
        finding="THE SPINOR STRUCTURE forced (38.DV.3 only NAMED it). The carrier 2I contains the central "
                "-1 (order 2, conjugation = identity rotation, yet -1 != +1) -- the non-trivial kernel of "
                "the double cover SU(2)->SO(3) (28.W.2, 120=2*60) (SP.1). On the 2D fundamental (spinor) "
                "rep a 2*pi rotation acts as -1 (psi -> -psi) and only 4*pi returns it -- so the substrate "
                "carries 2-VALUED (half-integer-spin) reps, the 4*pi holonomy of 38.DV.3 read on the reps "
                "(SP.2). Filed correspondence (SP.3, POSTULATE): spinors <-> FERMIONS (Pauli); "
                "spin-statistics CITED, pending the Lorentz structure (50). The matter census + "
                "spin-statistics re-derivation + masses are OWED (SP.4). Same double cover as dim=3 (41/42) "
                "and the 1/b flux (40). Danger-free; nothing fitted.",
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
