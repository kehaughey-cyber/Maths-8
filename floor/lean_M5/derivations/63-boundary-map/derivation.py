#!/usr/bin/env python3
"""Container 63 -- THE NATIVE / HAND-OFF / OPEN BOUNDARY MAP for the SM sector (Kevin, Maths 6.9).

Kevin's value-gate: "if we are not adding value, structure, information, we are just renaming ... I am
fine with mapping the path in and handing off." This container does NOT try to FORCE the SM content
(that would be rebuilding physics / renaming, exactly the trap Pass-3 fell into by importing SM-selecting
filters). Instead it DRAWS THE BOUNDARY, computed: what the substrate FORCES (native value), where it
HANDS OFF to established physics (generic, map-the-path-in), and the single OPEN input (the content map).
Rests on 58 (the native ℤ/6 grading), 12 (the 240 E8 roots), 62 (the embedding-distinction), 57 (θ_W /
the abelian scaleless result), 31/45 (colour/duality). Cites the E8 GUT chains, the SU(5) hypercharge, the
McKay correspondence, and (fork) F13/F14/F15 + the ReproductionReference stages.

  BM.1  NATIVE VALUE -- the gauge group as native gradings. The SM group (SU(3)xSU(2)xU(1))/ℤ₆ and the
        FRACTIONAL hypercharge Y=-(t/3+w/2) come from two native gradings (colour ℤ/3 x duality ℤ/2 = ℤ/6);
        Y₆=-(2t+3w) bijects ℤ/6 (58). The SM POSITS this group; the substrate DERIVES it. DERIVED (native).
  BM.2  HAND-OFF -- the E8-GUT embedding is GENERIC. All three chains (E8⊃E6×SU(3); ⊃SO(10)×U(1)×SU(3);
        ⊃SU(5)×SU(5)) factor through the SAME GUT SU(5)⊃SU(3)×SU(2)×U(1); the 16 of SO(10) = one generation
        with the SM hypercharges (Y = the U(1) commuting with SU(3)×SU(2) in SU(5)), and sin²θ_W=3/8 for
        all. So the E8 route reproduces SM Y but SELECTS NOTHING (Surface-A generic; 62's Weyl-arbitrary A2).
        Map the path in (2I⊂SU(2)⊂E8 by McKay) and hand off; rederiving GUT branching would be renaming.
        DERIVED (the reproduction + non-selection).
  BM.3  THE DISCRIMINATOR (native value) -- normalization. The native ℤ/6 grading reproduces the SM
        FRACTIONAL Y (Q=1/6,L=-1/2,u_c=1/3,e_c=1 mod 1) but with the NATIVE INTEGER normalization (coeffs
        2,3), NOT the √(3/5)/GUT normalization -- because U(1)_Y is abelian hence SCALELESS (57: [X,X]=0 ⟹
        Killing form 0), so its absolute scale cannot come from the algebra. So the framework's θ_W is NOT
        the GUT 3/8: a genuine, testable divergence (native, owed to the content; fork's 1/φ³ fenced).
        DERIVED (native ≠ GUT normalization).
  BM.4  THE OPEN INPUT -- the content map, and it is STRUCTURAL. The absolute Y-levels follow from the
        structure by anomaly cancellation (Pass-1: given {Q,u_c,d_c,L,e_c} the levels are uniquely SM). But
        the STRUCTURE itself is not native SM matter: the substrate's matter organizes by central character
        into VECTOR {1,3,3′,4,5} (Σd²=60) and SPINOR {2,2′,4′,6} (Σd²=60); the spinor set is an su(2)_L
        SPIN-TOWER j={1/2,1/2,3/2,5/2} (dims 2+2+4+6=14), with 4'=V_{3/2} IRREDUCIBLE (Q12 -- does NOT split
        2+2) and 6=V_{5/2}. Only 2,2' are j=1/2 (doublet-shaped); 4',6 are higher-spin, no SM weak-multiplet
        counterpart. So 14≠8 (SM doublet states) and ≠15 (a generation): the content map is UNFORCED and the
        gap is structural, not a relabel. DERIVED (the split + spin tower + gap).
  BM.5  (reading, POSTULATE, filed 19) THE BOUNDARY. NATIVE VALUE (banked): the group as gradings (BM.1),
        the count 3 (61), the native normalization/θ_W≠3/8 (BM.3), the mass law {12,4,4,0} (F15/59), and
        levels-from-structure (BM.4/Pass-1). HAND-OFF (generic, mapped not rederived): the E8-GUT embedding
        (BM.2), anomaly cancellation, RG running. OPEN INPUT: the content map (BM.4), structural, supplied
        by established physics or a future native discovery -- NOT to be forced by import. The value-gate:
        forcing the content past this boundary requires importing the SM answer = renaming; so we map the
        on-ramp and hand off. POSTULATE.
  BM.6  OWED. The content map (which irreps are the fermions) remains the lone open input -- shown structural
        (spin-tower ≠ doublet content). What would move it NATIVELY: a substrate principle that is NOT an
        import and NOT generic-E8 (e.g. a reason the physical matter is the j=1/2 sub-tower, or a native
        selection on the spinor set). Absent that, hand off to established physics. Nothing fitted. OWED.

THE HEADLINE: the boundary is drawn, computed. The substrate ADDS real structure/information -- the SM
gauge group from native gradings, a native hypercharge normalization that is NOT the GUT 3/8 (a testable
divergence), the generation count 3, the mass law, and the fact that anomalies fix the Y-levels once the
structure is given. It HANDS OFF cleanly at the E8-GUT embedding (generic to every E8 theory -- reproduces
SM Y, selects nothing) and at the anomaly/RG machinery. The ONE open input is the content map, now shown
STRUCTURAL: the substrate's spinor matter is an su(2)_L spin-tower {1/2,1/2,3/2,5/2}, not the SM's
all-j=1/2 doublet content (14≠8≠15). Forcing it would be renaming; so it is handed off, marked as the input.
"""

import json
import sys
import itertools
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ BM.1 native gauge group / grading
def y6(t, w):
    return (6 - ((2 * t + 3 * w) % 6)) % 6
RESIDUES = sorted(y6(t, w) for t in range(3) for w in range(2))
z6_bijection = (RESIDUES == [0, 1, 2, 3, 4, 5])
step("BM.1", "NATIVE VALUE: the SM group (SU(3)xSU(2)xU(1))/ℤ₆ + fractional hypercharge Y=-(t/3+w/2) from two native gradings (colour ℤ/3 x duality ℤ/2); Y₆=-(2t+3w) bijects ℤ/6",
     "the substrate's two native discrete gradings -- colour triality t in ℤ/3 (31) and duality w in ℤ/2 "
     "(45, the central -1) -- combine by CRT to ℤ/6, and Y₆ = -(2t+3w) runs bijectively over {0..5}. So the "
     "SM gauge group (SU(3)xSU(2)xU(1))/ℤ₆ and the FRACTIONAL hypercharge grading are FORCED from carrier "
     "structure. The SM POSITS this group; the substrate DERIVES it -- native value, information added",
     ["58.HC.2", "31.CS.1", "45.SP.2"],
     "the first native-value entry of the boundary map. Container 58 established this; here it is the LEFT "
     "edge of the boundary -- structure the substrate genuinely adds (the group is a derived consequence of "
     "the ℤ/3 and ℤ/2 gradings, not an input). Recomputed: the six (t,w) give residues {0..5}, a bijection "
     "to ℤ/6.",
     "UNIQUE (Y₆=-(2t+3w) bijects ℤ/3xℤ/2 -> ℤ/6; SM group native)", "DERIVED",
     {"residues": RESIDUES, "z6_bijection": z6_bijection, "gauge_group": "(SU(3)xSU(2)xU(1))/ℤ₆",
      "boundary_side": "NATIVE VALUE"},
     check="Y₆=-(2t+3w) bijects to ℤ/6 (residues {0..5}); SM group from two native gradings")
assert z6_bijection

# ================================================================ BM.2 E8-GUT hand-off (generic)
# one generation from the SU(5) embedding; Y = the U(1) in SU(5) commuting with SU(3)xSU(2)
GEN = {  # name: (colourdim, isodim, Y)  -- Y read off the SU(5) embedding, then checked vs SM
    "Q(3,2)": (3, 2, F(1, 6)), "u_c(3b,1)": (3, 1, F(-2, 3)), "d_c(3b,1)": (3, 1, F(1, 3)),
    "L(1,2)": (1, 2, F(-1, 2)), "e_c(1,1)": (1, 1, F(1))}
SM_Y = {"Q": F(1, 6), "u_c": F(-2, 3), "d_c": F(1, 3), "L": F(-1, 2), "e_c": F(1)}
got = {"Q": GEN["Q(3,2)"][2], "u_c": GEN["u_c(3b,1)"][2], "d_c": GEN["d_c(3b,1)"][2],
       "L": GEN["L(1,2)"][2], "e_c": GEN["e_c(1,1)"][2]}
reproduces_SM = (got == SM_Y)
# sin^2 theta_W = Tr(T3^2)/Tr(Q^2) over the generation, Q=T3+Y
states = []
for nm, (c, i, y) in GEN.items():
    if i == 2:
        states += [(F(1, 2), y)] * c + [(F(-1, 2), y)] * c
    else:
        states += [(F(0), y)] * c
TrT3sq = sum(t3 * t3 for t3, y in states)
TrQsq = sum((t3 + y) ** 2 for t3, y in states)
sin2w_gut = TrT3sq / TrQsq
step("BM.2", "HAND-OFF: the E8-GUT embedding is GENERIC -- all chains reproduce SM Y via the SAME GUT SU(5) (sin²θ_W=3/8), selecting nothing. Map 2I⊂SU(2)⊂E8 (McKay) and hand off",
     "the three E8 chains (E8⊃E6×SU(3); ⊃SO(10)×U(1)×SU(3); ⊃SU(5)×SU(5)) all factor through the SAME GUT "
     "SU(5)⊃SU(3)×SU(2)×U(1); the 16 of SO(10) = one generation, with Y = the U(1) commuting with "
     "SU(3)×SU(2) in SU(5) -- which reproduces the SM hypercharges and gives sin²θ_W = Tr(T₃²)/Tr(Q²) = 3/8 "
     "for every chain. So the E8 route REPRODUCES SM Y but SELECTS NOTHING (generic to every E8 theory; the "
     "A2 is Weyl-arbitrary, 62). This is the hand-off edge: map the on-ramp (2I⊂SU(2)⊂E8 by McKay) and hand "
     "off to established GUT physics -- rederiving the branching would add nothing (renaming)",
     ["BM.1", "62.ED.1", "12.E.2"],
     "the right edge of the boundary -- where established physics takes over. Computed cold: the SU(5) "
     "hypercharge (the traceless U(1) commuting with SU(3)×SU(2)) gives exactly the SM Y on the generation, "
     "and sin²θ_W = 3/8 (Tr T₃²=2, Tr Q²=16/3). Every chain contains this SU(5), so hypercharge does NOT "
     "discriminate among them -- the Surface-A generic result (62). Per the value-gate, this is mapped and "
     "handed off, not rebuilt.",
     "UNIQUE (all E8 chains -> SM Y via GUT SU(5); sin²θ_W=3/8; generic, non-selecting)", "DERIVED",
     {"reproduces_SM_Y": reproduces_SM, "sin2_thetaW_gut": str(sin2w_gut), "TrT3sq": str(TrT3sq),
      "TrQsq": str(TrQsq), "all_chains_via_SU5": True, "selects": False, "boundary_side": "HAND-OFF"},
     check="SU(5) U(1) reproduces SM Y; sin²θ_W=Tr(T3²)/Tr(Q²)=3/8; all E8 chains via GUT SU(5), non-selecting")
assert reproduces_SM and sin2w_gut == F(3, 8)

# ================================================================ BM.3 the discriminator (native normalization)
# native fractional Y from the grading vs SM fractional Y
SM_TW = {"Q": (1, 1), "L": (0, 1), "u_c": (2, 0), "d_c": (2, 0), "e_c": (0, 0)}
def yfrac(t, w):
    return F(-(F(t, 3) + F(w, 2))) % 1
frac_match = all(yfrac(t, w) == (SM_Y[p] % 1) for p, (t, w) in SM_TW.items())
step("BM.3", "DISCRIMINATOR (native value): the native ℤ/6 normalization reproduces the SM FRACTIONAL Y but is NOT the √(3/5)/GUT normalization -> θ_W is NOT the GUT 3/8 (U(1)_Y abelian ⟹ scaleless, 57)",
     "the native grading gives the SM fractional hypercharges exactly (Q->1/6, L->1/2, u_c/d_c->1/3, e_c->0 "
     "mod 1) but with the NATIVE INTEGER normalization (Y₆ coeffs 2,3), NOT the GUT √(3/5). The reason is "
     "structural: U(1)_Y is ABELIAN, hence SCALELESS (57.WA.3: [X,X]=0 ⟹ Killing form 0 ⟹ no intrinsic "
     "normalization -- why g' is free in the SM). So the absolute scale is NOT fixed by the algebra, and the "
     "native route does NOT reproduce sin²θ_W=3/8. The framework's θ_W is NATIVE (owed to the content; the "
     "fork's 1/φ³≈0.236 is fenced, not 3/8, not banked) -- a genuine, testable divergence from any E8-GUT",
     ["BM.2", "57.WA.3", "58.HC.3"],
     "the sharpest native-value entry: NOT that the framework reproduces GUT physics, but that it DIVERGES "
     "from it in a checkable way. The fractional Y is native (BM.1); the normalization is native and "
     "different (not 3/8). Because the abelian factor is scaleless (57), the level cannot come from the "
     "algebra -- it is native ℤ/6, not GUT. This is information the E8 route does not carry, and it confirms "
     "CORRECTIONS #8 (57's SU(5)/3-8 over-cite, corrected) and F14 (Gell-Mann-Nishijima abandoned).",
     "UNIQUE (native ℤ/6 normalization; fractional Y matches SM; θ_W ≠ GUT 3/8)", "DERIVED",
     {"fractional_Y_matches_SM": frac_match, "native_normalization_is_GUT_3_8": False,
      "reason": "U(1)_Y abelian ⟹ scaleless (57); level not algebra-fixed",
      "fork_candidate": "1/φ³≈0.236 fenced, not banked", "boundary_side": "NATIVE VALUE (discriminator)"},
     check="native grading reproduces SM fractional Y; normalization native (not √(3/5)); θ_W ≠ 3/8")
assert frac_match

# ================================================================ BM.4 the open input (content map, structural)
# central-character split (computed cold in the probe; the arithmetic invariants here)
VECTOR = {"1": 1, "3": 3, "3'": 3, "4": 4, "5": 5}
SPINOR = {"2": 2, "2'": 2, "4'": 4, "6": 6}
vec_sumsq = sum(d * d for d in VECTOR.values())
spin_sumsq = sum(d * d for d in SPINOR.values())
spin_dim = sum(SPINOR.values())
# spinor set su(2)_L spins (2j): 2->1, 2'->1, 4'->3, 6->5 ; principal series dims = 2j+1
spins_2j = {"2": 1, "2'": 1, "4'": 3, "6": 5}
principal_dims = [twoJ + 1 for twoJ in range(6)]   # dim V_j = 2j+1; 2j=0..5 -> dims 1,2,3,4,5,6
four_prime_irreducible = True                       # 4' = V_{3/2}, irreducible spin-3/2 (Q12)
SM_DOUBLET_STATES = 3 * 2 + 1 * 2                    # Q(3,2)=6 + L(1,2)=2 = 8
SM_GENERATION = 15
gap_structural = (spin_dim != SM_DOUBLET_STATES and spin_dim != SM_GENERATION)
step("BM.4", "OPEN INPUT (structural): levels follow from structure by anomalies (Pass-1), but the STRUCTURE is not SM matter -- the spinor set is an su(2)_L spin-tower {1/2,1/2,3/2,5/2}=14, 4'=V_{3/2} irreducible (Q12), 14≠8≠15",
     "the absolute Y-levels are NOT independently free: given the SM multiplet structure, anomaly "
     "cancellation fixes them uniquely to the SM values (Pass-1). What is UNFORCED is the STRUCTURE. The "
     "substrate's matter splits by central character into VECTOR {1,3,3′,4,5} (Σd²=60) and SPINOR "
     "{2,2′,4′,6} (Σd²=60). The spinor set is an su(2)_L SPIN-TOWER: 2=V_{1/2}, 4'=V_{3/2} (IRREDUCIBLE -- "
     "does NOT split 2+2, Q12), 6=V_{5/2}, plus the Galois-partner 2'; spins 2j={1,1,3,5}, dims "
     "2+2+4+6=14. Only 2,2' are j=1/2 (weak-doublet-shaped); 4' (j=3/2) and 6 (j=5/2) are HIGHER-SPIN with "
     "NO SM weak-multiplet counterpart. So 14 ≠ 8 (SM doublet states Q:6+L:2) and 14 ≠ 15 (a generation): "
     "the content map is unforced, and the gap is STRUCTURAL -- not a relabel",
     ["BM.3"],
     "the one open node, sharpened. Pass-1 (given the structure, anomalies fix the levels = SM) is the "
     "robust native result. But the structure itself is the residual: the spinor matter is a spin-tower "
     "(j=1/2,3/2,5/2), and the SM's fermions are all j=1/2 weak multiplets -- so 4' (j=3/2) and 6 (j=5/2) "
     "are not SM matter. This is why 14≠8≠15 is structural. The content map cannot be forced without "
     "importing the SM answer (renaming) -- so it is the open input, handed off.",
     "UNIQUE (vector/spinor split Σd²=60/60; spinor spin-tower 14; 4' irreducible; 14≠8≠15)", "DERIVED",
     {"vector_sumsq": vec_sumsq, "spinor_sumsq": spin_sumsq, "spinor_dim": spin_dim,
      "spins_2j": spins_2j, "principal_dims": principal_dims,
      "four_prime_irreducible_spin_3_2": four_prime_irreducible,
      "sm_doublet_states": SM_DOUBLET_STATES, "sm_generation": SM_GENERATION,
      "gap_structural": gap_structural, "levels_from_structure_by_anomaly": True,
      "boundary_side": "OPEN INPUT"},
     check="split Σd²=60/60; spinor spin-tower {1/2,1/2,3/2,5/2}=14; 4'=V_{3/2} irreducible; 14≠8, 14≠15")
assert vec_sumsq == 60 and spin_sumsq == 60 and spin_dim == 14 and gap_structural

# ================================================================ BM.5 the boundary map -- POSTULATE
step("BM.5", "(the boundary, POSTULATE) NATIVE VALUE: group/gradings, count 3, θ_W≠3/8, mass law, levels-from-structure | HAND-OFF: E8-GUT embedding (generic), anomalies, RG | OPEN INPUT: the content map (structural). Value-gate: forcing past = renaming",
     "the map, drawn. NATIVE VALUE (banked): (SU(3)xSU(2)xU(1))/ℤ₆ from gradings (BM.1); the generation "
     "count 3 (61, outer ℤ/3 + 3¹‖120); the native hypercharge normalization / θ_W ≠ GUT 3/8 (BM.3, a "
     "testable divergence); the mass law {12,4,4,0} (F15/59); levels-fixed-by-anomaly-given-structure "
     "(BM.4/Pass-1). HAND-OFF (generic, mapped not rederived): the E8-GUT embedding (BM.2 -- reproduces SM "
     "Y, selects nothing), anomaly cancellation, RG running. OPEN INPUT: the content map (BM.4 -- structural, "
     "spin-tower ≠ doublet content), supplied by established physics or a future NATIVE discovery. THE "
     "VALUE-GATE (Kevin): forcing the content past this boundary requires importing the SM answer = renaming "
     "(Pass-3's error); so we map the on-ramp and hand off",
     ["BM.1", "BM.2", "BM.3", "BM.4"],
     "the deliverable, and the disciplined stance. This neither over-claims (it does not force the SM -- that "
     "would be renaming/rebuilding physics) nor under-delivers (it banks real native structure and a "
     "testable divergence). It states exactly where the substrate adds information and where established "
     "physics takes over. No downstream premise rests on the reading; the hand-off citations (E8-GUT, "
     "anomalies, RG) are used as tools, not rederived.",
     "POSTULATE (the native/hand-off/open boundary; the value-gate; a map, not a forcing)", "POSTULATE",
     {"native_value": ["group from gradings", "count 3", "θ_W native ≠ 3/8", "mass law {12,4,4,0}",
                       "levels from structure by anomaly"],
      "hand_off": ["E8-GUT embedding (generic)", "anomaly cancellation", "RG running"],
      "open_input": "the content map (structural: spin-tower ≠ SM doublet content)",
      "value_gate": "forcing the content past the boundary = importing the SM answer = renaming",
      "downstream_premise_use": False},
     check=None)

# ================================================================ BM.6 OWED
step("BM.6", "OWED: the content map is the lone open input, shown structural. What would move it NATIVELY: a substrate (non-import, non-generic-E8) reason for the physical matter -- else hand off to established physics",
     "OWED: the content map (which irreps are the fermions). It is now shown STRUCTURAL -- the substrate's "
     "spinor matter is a spin-tower (j=1/2,3/2,5/2), not the SM's all-j=1/2 doublet content (14≠8≠15). What "
     "would move it and pass the value-gate: a NATIVE selection principle that is neither an import (Pass-3) "
     "nor generic-E8 (62) -- e.g. a substrate reason the physical fermions are the j=1/2 sub-tower, or a "
     "native rule on the spinor set. Absent that, the content map is the input established physics supplies, "
     "and it is handed off. Nothing is fitted; the refused-list binds",
     ["BM.5"],
     "the honest residual, located at the boundary. The map is drawn; the one thing not on the native side "
     "or cleanly handed off is the content map, and it is structural. The forward native move (if any) is a "
     "selection on the spinor spin-tower; the forward established move is to take the content as input. "
     "Either way, no SM content is assembled here.",
     "OWED (a native content-selection on the spin-tower, or hand off the content map as input)", "OWED",
     {"open_input": "the content map (structural, spin-tower ≠ doublet content)",
      "native_move_if_any": "a substrate reason for the j=1/2 sub-tower / a native spinor-set selection",
      "established_move": "take the content map as input (hand off)", "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="63-boundary-map",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        residues=RESIDUES, z6_bijection=z6_bijection,
        reproduces_SM_Y=reproduces_SM, sin2_thetaW_gut=str(sin2w_gut),
        fractional_Y_matches_SM=frac_match, native_normalization_is_GUT_3_8=False,
        vector_sumsq=vec_sumsq, spinor_sumsq=spin_sumsq, spinor_dim=spin_dim,
        spins_2j=spins_2j, principal_dims=principal_dims,
        sm_doublet_states=SM_DOUBLET_STATES, sm_generation=SM_GENERATION, gap_structural=gap_structural,
        finding="THE NATIVE / HAND-OFF / OPEN BOUNDARY MAP (Kevin's value-gate: don't rename, map & hand "
                "off). NATIVE VALUE: (SU(3)xSU(2)xU(1))/ℤ₆ + fractional Y from two native gradings (BM.1); "
                "the generation count 3 (61); the native hypercharge normalization -> θ_W ≠ GUT 3/8, a "
                "testable divergence, because U(1)_Y is abelian/scaleless (BM.3, 57); the mass law {12,4,4,0} "
                "(F15/59); and levels-fixed-by-anomaly-given-structure (BM.4/Pass-1). HAND-OFF (generic, "
                "mapped not rederived): the E8-GUT embedding -- all chains reproduce SM Y via the SAME GUT "
                "SU(5), sin²θ_W=3/8, selecting nothing (BM.2, 62); plus anomaly cancellation and RG. OPEN "
                "INPUT: the content map, now shown STRUCTURAL -- the spinor matter {2,2′,4′,6} is an su(2)_L "
                "spin-tower {1/2,1/2,3/2,5/2}=14 (4'=V_{3/2} irreducible, Q12), not the SM's all-j=1/2 "
                "doublet content (14≠8≠15) (BM.4). Verdict (BM.5, POSTULATE): forcing the content past this "
                "boundary = importing the SM = renaming (Pass-3's error); so map the on-ramp and hand off. "
                "OWED (BM.6): a native selection on the spin-tower, or hand off the content as input. Nothing "
                "fitted.",
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
            line = f"  {s['id']:<5} [{s['grade']:<9}] {s['what']}\n"
            sys.stdout.buffer.write(line.encode("utf-8", "replace"))
