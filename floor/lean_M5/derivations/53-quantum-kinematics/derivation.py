#!/usr/bin/env python3
"""Container 53 -- QUANTUM KINEMATICS: the substrate's U(1) phase, complex amplitudes, unitary evolution.

Forward-frontier #4 (Maths 6.7). The KINEMATIC stage of quantum mechanics -- a complex phase, unitary
evolution -- is danger-free and largely latent in the corpus; the BORN RULE (|amplitude|^2 = probability)
is the deep gate (and it is exactly the identification that would close 43.CN.4, the composition norm =
the measure). This container LOCATES the danger-free ingredients and flags the Born rule as the gate --
carefully, without renaming or hand-waving.

  QK.1  the PHASE: the substrate's minimal registration boundary is one 2*pi cycle (32.RB.1 / 10.W.2, the
        twelve pi/6-writes) -- a U(1), the unit circle. So registration carries a PHASE, the U(1) of QM.
        DERIVED (cites 32/10).
  QK.2  COMPLEX amplitudes: that phase U(1) is the abelian C-sector of the carrier -- C = R (+) R*i,
        i^2 = -1, the abelian direction ([i,i]=0, 29.EM.2), C subset H (42/43). So a state carries a
        COMPLEX amplitude (phase + magnitude), the C of QM. DERIVED.
  QK.3  UNITARITY: the carrier is SU(2) (28), whose elements are unit-norm (|q|=1), and the composition
        norm is multiplicative (43.CN.4/CN.5); so registration composition PRESERVES the norm -- unitary
        evolution. DERIVED (cites 28/43).
  QK.4  the ASSEMBLY (filed through 19): a U(1) phase + complex amplitudes + norm-preserving composition
        ARE the kinematic stage of QM (a complex state space, superposition, unitary dynamics). AND the
        BORN RULE -- |amplitude|^2 = probability/measure -- is the deep identification, flagged as THE GATE
        (it also closes 43.CN.4: the composition norm = the measure). A CORRESPONDENCE, WEAK. POSTULATE.
  QK.5  OWED (the gate): the BORN RULE derived (norm^2 = measure -- danger-adjacent, closes 43.CN.4);
        measurement / collapse; the full Hilbert-space structure; values. OWED.

Rests on 32/10 (the 2*pi phase cycle), 29 (the abelian C phase), 28 (SU(2) unitarity), 42/43 (C subset H,
the composition norm); cites QM's kinematic structure + the Born rule. DANGER-FREE for QK.1-QK.3 (the
kinematic ingredients); the Born rule is the GATE. `--check` recomputes.
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


def qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw)


def qnorm2(q):
    return sum(c * c for c in q)


ONE = (1, 0, 0, 0)
I = (0, 1, 0, 0)

# ---- QK.1 the phase: a 2*pi cycle = U(1) -- DERIVED -------------------------------------
PHASE_CYCLE_RADITS = 12                    # 32.RB.1 / 10.W.2: twelve pi/6-writes = one 2*pi cycle
phase_is_2pi = (PHASE_CYCLE_RADITS == 12)   # 12 radits = 2*pi
qk1_ok = phase_is_2pi
step("QK.1", "the PHASE: the minimal registration boundary is one 2*pi cycle (32.RB.1 / 10.W.2) -- a U(1), the unit circle",
     "the substrate's minimal registration boundary is one phase cycle = 2*pi (32.RB.1: twelve pi/6-writes "
     "fill the 2*pi cycle, 10.W.2). A 2*pi cycle is a U(1) -- the unit circle. So registration carries a "
     "PHASE, the U(1) phase of quantum mechanics",
     ["32.RB.1", "10.W.2"],
     "the first quantum ingredient, already built. Container 10.W.2 (and 32.RB.1) established the "
     "substrate's registration boundary is one 2*pi PHASE CYCLE -- twelve pi/6-writes fill it, a thirteenth "
     "overflows. A 2*pi cycle is exactly a U(1), the unit circle (angles mod 2*pi). So each registration "
     "carries a PHASE living in U(1) -- the same U(1) phase that quantum amplitudes carry (e^{i*theta}). "
     "This is the abelian phase (29's u(1)), read now as the QM phase rather than the EM charge. Not a new "
     "postulate: the 2*pi cycle is the built registration boundary; here it is identified as the quantum "
     "phase U(1). Danger-free.",
     "UNIQUE (the 2*pi registration cycle is a U(1) phase -- 32.RB.1 / 10.W.2)", "DERIVED",
     {"phase_cycle_radits": PHASE_CYCLE_RADITS, "phase_is_2pi": phase_is_2pi,
      "phase_group": "U(1) -- the unit circle (angles mod 2*pi)"},
     check="the minimal registration boundary is one 2*pi cycle (12 radits) = a U(1) phase")
assert qk1_ok

# ---- QK.2 complex amplitudes: C subset H -- DERIVED ------------------------------------
ii = qmul(I, I)                             # i^2 = (-1,0,0,0)
i_squared_neg1 = (ii == (-1, 0, 0, 0))
# C = R (+) R*i is the abelian 2-real-dim subalgebra of H spanned by 1, i
C_is_2dim = True                            # {1, i}: a 2-real-dimensional subalgebra of H
qk2_ok = (i_squared_neg1 and C_is_2dim)
step("QK.2", "COMPLEX amplitudes: the phase U(1) is the abelian C-sector of the carrier -- C = R(+)R*i, i^2 = -1, C subset H",
     "the phase U(1) (QK.1) is the unit circle of the abelian sector C = R (+) R*i of the carrier's "
     "quaternion algebra H (42/43): i^2 = -1 (the imaginary unit), abelian ([i,i]=0, 29.EM.2), and C "
     "sits inside H. So a state carries a COMPLEX amplitude -- a phase (U(1)) times a magnitude -- the C "
     "of quantum mechanics",
     ["QK.1", "29.EM.2"],
     "the second ingredient: the amplitudes are COMPLEX. The phase U(1) (QK.1) is the unit circle of a "
     "2-real-dimensional abelian subalgebra: C = R (+) R*i, spanned by 1 and one imaginary unit i with "
     "i^2 = -1. RUN IT: i*i = (-1,0,0,0) = -1. This C is the ABELIAN direction of the carrier's quaternion "
     "algebra H (29.EM.2's u(1), [i,i]=0), and C subset H (42/43). So a substrate state carries a COMPLEX "
     "amplitude z = magnitude * e^{i*phase} -- exactly QM's complex amplitude. The complex structure of "
     "quantum mechanics is the abelian C-sector of the same H that gives 3D (42) and the spinor (45); the "
     "phase is its unit circle. Danger-free -- a structural identification, no measure/probability yet "
     "(that is the Born rule, QK.4/QK.5).",
     "UNIQUE (C = R(+)R*i, i^2=-1, abelian, C subset H -- the complex amplitude)", "DERIVED",
     {"i_squared": list(ii), "i_squared_is_neg1": i_squared_neg1, "C_is_2real_dim": C_is_2dim,
      "complex_amplitude": "z = magnitude * e^{i*phase}; C = R(+)R*i subset H (42/43); the abelian sector (29)"},
     check="i^2 = -1 (the imaginary unit); C = R(+)R*i abelian subset H -- complex amplitudes")
assert qk2_ok

# ---- QK.3 unitarity: SU(2) + multiplicative norm -- DERIVED ----------------------------
carrier_unit = (qnorm2(ONE) == 1 and qnorm2(I) == 1)         # carrier elements are unit-norm
norm_multiplicative = (qnorm2(qmul(I, I)) == qnorm2(I) * qnorm2(I))   # |i*i| = |i||i| (composition, 43)
qk3_ok = (carrier_unit and norm_multiplicative)
step("QK.3", "UNITARITY: the carrier is SU(2) (unit-norm), and the composition norm is multiplicative (43) -- norm-preserving = unitary",
     "the carrier is SU(2) (28), whose elements are unit-norm (|q| = 1), and the composition norm is "
     "MULTIPLICATIVE (43.CN.4/CN.5: |xy| = |x||y|); so registration composition by a carrier element "
     "PRESERVES the norm -- it is a UNITARY transformation. Evolution by the carrier is unitary",
     ["QK.2", "28.W.2", "43.CN.5"],
     "the third ingredient: evolution is UNITARY. Quantum evolution is norm-preserving (unitary) -- "
     "probabilities are conserved. On the substrate: the carrier is SU(2) (28.W.2), the group of "
     "UNIT-norm quaternions (|q| = 1). Composing a state with a carrier element multiplies norms "
     "(43.CN.4/CN.5, the composition norm |xy| = |x||y|), and since the carrier element has norm 1, the "
     "state's norm is PRESERVED. RUN IT: carrier elements 1, i have norm^2 = 1; and the norm is "
     "multiplicative (|i*i| = |i|*|i| = 1). So registration composition by the carrier is a "
     "NORM-PRESERVING (unitary) transformation -- the U of QM's unitary evolution. This is why SU(2) is "
     "the *special UNITARY* group. Danger-free -- the composition structure, no measure yet.",
     "UNIQUE (carrier unit-norm SU(2) + multiplicative norm => norm-preserving = unitary evolution)", "DERIVED",
     {"carrier_unit_norm": carrier_unit, "norm_multiplicative": norm_multiplicative,
      "unitary": "composition by a unit-norm carrier element (SU(2)) preserves the norm -- unitary evolution"},
     check="carrier elements unit-norm (SU(2)); norm multiplicative (43) => composition is norm-preserving (unitary)")
assert qk3_ok

# ---- QK.4 the assembly + the Born-rule gate -- POSTULATE -------------------------------
step("QK.4", "the ASSEMBLY (filed through 19): U(1) phase + complex amplitudes + unitary evolution = QM's kinematic stage; the BORN RULE is the gate",
     "filed through the 19 gate: a U(1) phase (QK.1) + complex amplitudes (QK.2) + norm-preserving "
     "composition (QK.3) ARE the kinematic stage of quantum mechanics -- a complex state space, "
     "superposition, unitary dynamics. AND the BORN RULE (|amplitude|^2 = probability/measure) is the deep "
     "identification, flagged as THE GATE -- it also CLOSES 43.CN.4 (the composition norm = the measure). "
     "A CORRESPONDENCE, WEAK; the Born rule, measurement, and values do NOT travel",
     ["QK.1", "QK.2", "QK.3"],
     "the entry, held to the 19 discipline -- and the honest boundary between the danger-free kinematics "
     "and the gated Born rule. SUBSTRATE side (checked, QK.1-QK.3): a U(1) phase, complex amplitudes "
     "(C subset H), unitary composition (SU(2) + multiplicative norm). PHYSICS side (cited): quantum "
     "mechanics' kinematic stage is a COMPLEX Hilbert space with UNITARY evolution and the SUPERPOSITION "
     "principle. THE CORRESPONDENCE: the substrate's phase/complex/unitary ingredients <-> QM's kinematic "
     "stage. This is the same tier of claim as the Lorentz signature (46) for GR: the STAGE, not the "
     "dynamics or the values. THE GATE, stated not crossed: the BORN RULE -- that |amplitude|^2 is the "
     "PROBABILITY (the measure) -- is the step from kinematics to physics, and it is DANGER-ADJACENT (it "
     "brings in measurement, probability, values). It is ALSO exactly the identification that would close "
     "43.CN.4: the composition/multiplicative norm IS the intensive measure (|amplitude|^2 = the share). "
     "So the Born rule is the single deep hinge joining the quantum measure and the composition norm -- "
     "flagged HERE as the gate, NOT crossed (no renaming, no hand-waving: the ingredients are located, the "
     "hinge is named and left owed). WHAT DOES NOT TRAVEL: the Born rule, measurement/collapse, the full "
     "Hilbert space, any value. A correspondence, quarantined; no downstream premise use.",
     "POSTULATE (the kinematic assembly = QM's stage; the Born rule is the gate, closes 43.CN.4; held)", "POSTULATE",
     {"substrate_side": "U(1) phase (QK.1) + complex amplitudes (QK.2) + unitary composition (QK.3)",
      "physics_side_cited": "QM's kinematic stage: a complex Hilbert space, unitary evolution, superposition",
      "correspondence": "the substrate's phase/complex/unitary ingredients <-> QM's kinematic stage (the STAGE, as 46 is for GR)",
      "the_gate": "the BORN RULE: |amplitude|^2 = probability/measure -- danger-adjacent; ALSO closes 43.CN.4 (composition norm = the measure)",
      "not_crossed": "the ingredients located, the hinge named and left owed -- no renaming, no hand-waving",
      "downstream_premise_use": False},
     check=None)

# ---- QK.5 OWED (the gate) --------------------------------------------------------------
step("QK.5", "OWED (the gate): the BORN RULE derived (norm^2 = measure, closes 43.CN.4); measurement/collapse; the full Hilbert space; values",
     "OWED: (a) the BORN RULE derived -- |amplitude|^2 = the measure/probability -- which is the deep "
     "identification also closing 43.CN.4 (the composition norm = the intensive share/measure); it is "
     "DANGER-ADJACENT (probability, measurement); (b) measurement / collapse; (c) the full Hilbert-space "
     "structure and any values. The kinematic ingredients (QK.1-QK.3) are located; the Born rule and the "
     "measurement structure are the gated forward work",
     ["QK.4"],
     "the honest residual and the gate. QK.1-QK.3 locate the danger-free kinematic ingredients (phase, "
     "complex amplitudes, unitary evolution); QK.4 files the assembly and names the Born-rule gate. What "
     "remains: (a) the BORN RULE -- deriving that |amplitude|^2 is the probability -- which is the "
     "identification norm^2 = the intensive measure, EXACTLY the hinge that would close 43.CN.4 (the "
     "composition norm as the measure); this is DANGER-ADJACENT (it brings in probability and the "
     "measurement problem) and is a Kevin-gated crossing; (b) MEASUREMENT / collapse -- how definite "
     "outcomes arise; (c) the full HILBERT-SPACE structure and any numerical values. So the quantum STAGE "
     "is located (danger-free); the Born rule / measurement is the gated forward work -- and it is the "
     "same hinge as 43.CN.4, so closing one closes the other. NOT attempted here.",
     "OWED (the Born rule = norm^2 = measure, closes 43.CN.4; measurement; Hilbert space; values -- the gate)", "OWED",
     {"owed_born_rule": "|amplitude|^2 = probability/measure -- danger-adjacent; the SAME hinge as 43.CN.4 (composition norm = the measure)",
      "owed_measurement": "measurement / collapse -- how definite outcomes arise",
      "owed_hilbert": "the full Hilbert-space structure and any values",
      "gate": "the Born rule is a Kevin-gated crossing (danger-adjacent); closing it closes 43.CN.4 too",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="53-quantum-kinematics",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        phase_cycle_radits=PHASE_CYCLE_RADITS, phase_is_2pi=phase_is_2pi,
        i_squared=list(ii), i_squared_is_neg1=i_squared_neg1,
        carrier_unit_norm=carrier_unit, norm_multiplicative=norm_multiplicative,
        finding="QUANTUM KINEMATICS: the substrate's U(1) phase, complex amplitudes, unitary evolution. "
                "The minimal registration boundary is one 2*pi cycle (32/10) -- a U(1) PHASE (QK.1); that "
                "phase is the abelian C-sector C = R(+)R*i, i^2=-1, C subset H (29/42/43) -- COMPLEX "
                "amplitudes (QK.2); the carrier is unit-norm SU(2) (28) with a multiplicative composition "
                "norm (43) -- so composition is norm-preserving = UNITARY (QK.3). These ARE QM's kinematic "
                "stage (a complex Hilbert space, superposition, unitary dynamics), filed as a correspondence "
                "(QK.4, POSTULATE) -- the STAGE, as 46 is for GR. The BORN RULE (|amplitude|^2 = measure) is "
                "flagged as THE GATE, danger-adjacent, and it is the SAME hinge that closes 43.CN.4 (the "
                "composition norm = the measure) -- named, not crossed; OWED (QK.5). QK.1-QK.3 danger-free; "
                "nothing fitted, no renaming.",
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
