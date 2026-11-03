#!/usr/bin/env python3
"""Container 60 -- CONTENT SELECTION (K2): THE RE-EXAMINATION. The 'root' verdict is RETRACTED.

  *** RETRACTION (2026-09-11, Kevin's re-examination; CORRECTIONS #9). ***
The ORIGINAL version of this container concluded "K2 is a genuine irreducible ROOT." THAT VERDICT IS
RETRACTED. It rested on CATEGORY ERRORS -- it tested the WRONG surfaces and mistook basis structure for
contradiction, then (eager for a root, per the roots north-star) declared irreducibility prematurely. The
directory slug ("content-a-root") is kept as a visible scar (the project's "scars are the map" discipline);
this container now records the honest re-examination.

WHAT K2 ACTUALLY IS: the SM fermion content is a set of gauge-group reps (colour x isospin x hypercharge)
with a generation multiplicity. Forcing it means the substrate's matter objects, organized by their GAUGE +
FAMILY quantum numbers, reproduce the SM multiplets -- NOT "which of 2I's 9 abstract irreps sum to 15".

  RX.1  the narrow fact that IS true (kept from the original), and why it is nearly vacuous: the
        2I-irrep-DIMENSION surface alone does not force the SM content -- the sums {1,3,3',5}=12,
        {2,2',4',6}=14, {1,3,3',4,5}=16 do not equal the SM's 15. But this compares irrep DIMENSIONS to a
        WEYL-FERMION COUNT (a category error, RX.2a) -- the wrong surface -- so it establishes nothing about
        irreducibility. DERIVED (the counts) + flagged as the wrong comparison.
  RX.2  the CATEGORY ERRORS that invalidated the 'root' verdict:
        (a) WRONG SURFACE -- compared irrep dimensions to a Weyl count (RX.1);
        (b) MASS/WEAK-BASIS CONFLATION -- the original 'sharp obstruction' set the vertex-defect MASS
            lattice (all w=0, even-Y) against the weak/hypercharge matter (needs w=1, odd-Y) and called them
            'irreconcilable'. But mass-eigenbasis != weak-eigenbasis is EXACTLY the SM (the CKM/PMNS mixing);
            they are complementary ASPECTS of the same fermions, not rival contents. No contradiction.
        (c) GENERATIONS DISMISSED -- repeatedly (56/59/60) called generations 'just another of the
            substrate's threes' and refused to engage. But generation = the OUTER Z/3 (LEFT-mult by g3,
            fixed-point-free -> 40/40/40) is genuinely DISTINCT from colour = the INNER Z/3 (conjugation ->
            6 fixed + 38 triples), they COMMUTE (9 joint labels), and the count 3 is forced by 3^1 || 120 --
            a real, motivated structure, not a dismissible coincidence.
        (d) PREMATURE ROOT -- declared 'irreducible' from wrong-surface failure, against the earned-root
            criterion (push on the RIGHT surfaces first). DERIVED (the (c) facts are Lean-checked).
  RX.3  the RIGHT surfaces -- UNTESTED in the original attack: (i) the REGULAR REP C[2I] (dim 120) under the
        joint commuting action colour(inner Z/3) x isospin(su(2)_L on H=C^2) x generation(outer Z/3) x
        hypercharge(Z/6); (ii) E8 > A2 x E6 (248 = (8,1)+(1,78)+(3,27)+(3bar,27bar); the 27 of E6 is one
        generation). Every SM label has a located substrate handle (colour 30/31, isospin fork, hypercharge
        58, generation the outer Z/3). DERIVED (the surfaces exist; the E8 decomposition dims check).
  RX.4  (reading, POSTULATE) K2 is RE-OPENED. It is NOT an irreducible root -- it is a partially-structured,
        genuinely-OPEN problem: the substrate has real handles for every SM label (RX.3), but the
        content-selection on the RIGHT surface is untested. The 'root' verdict (original KA.5) is withdrawn.
  RX.5  OWED: the real test -- decompose the right surfaces (RX.3) and see whether 3 generations of SM
        multiplets emerge, TARGET OUT OF VIEW, refused-list at MAXIMUM (the most fitting-prone region in the
        program). Paused before the test (Kevin: 'step back further first'). OWED.

THE HEADLINE: the earlier 'K2 is a root' is WRONG -- a category error (wrong surface + mass/weak conflation
+ generations dismissed). K2 is RE-OPENED as a partially-structured open problem with real substrate handles
(colour, isospin, hypercharge, and generation = the outer Z/3, count 3 via 3^1||120). The honest test on the
right surfaces (regular rep joint action; E8 > A2 x E6) is OWED, and deliberately paused. Nothing fitted.
Rests on 59 (the forced structure), 31 (inner Z/3 colour), 58 (hypercharge), 12/30 (E8/A2); cites the fork
R10 (generation = outer Z/3), the SM content, E8 > A2 x E6.
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


# ---- RX.1 the narrow true fact, flagged as the wrong surface -- DERIVED -----------------
VDEF_DIM, SPINOR_DIM, VECTOR_DIM, SM_GEN = 12, 14, 16, 15
none_is_15 = (VDEF_DIM != SM_GEN and SPINOR_DIM != SM_GEN and VECTOR_DIM != SM_GEN)
step("RX.1", "the narrow true fact (kept), and why it is nearly vacuous: the 2I-irrep-DIMENSION surface alone does not force the SM content (12/14/16 != 15) -- but that is the WRONG comparison",
     "the one fact worth keeping from the original attack: sums of 2I irrep DIMENSIONS -- {1,3,3',5}=12, "
     "{2,2',4',6}=14, {1,3,3',4,5}=16 -- do not equal the SM generation's 15. TRUE, but it compares irrep "
     "dimensions to a WEYL-FERMION COUNT (RX.2a): the wrong surface. The SM content is not a subset of 2I's "
     "9 irreps summing to a number; it is gauge-group reps with a generation multiplicity. So this fact "
     "establishes NOTHING about whether K2 is forced or irreducible",
     ["59.KS.2"],
     "kept for the record, and immediately quarantined as the wrong comparison. It was the backbone of the "
     "original 'K2 is a root' argument, and it is a category error: dimensions of representations of 2I are "
     "not counts of Standard-Model Weyl fermions. RX.2-RX.3 give the right surfaces.",
     "UNIQUE (2I-irrep-dimension sums 12/14/16 != 15 -- true but the wrong surface)", "DERIVED",
     {"vdef_dim": VDEF_DIM, "spinor_dim": SPINOR_DIM, "vector_dim": VECTOR_DIM, "sm_gen": SM_GEN,
      "none_is_15": none_is_15, "flag": "WRONG SURFACE -- irrep dimensions vs a Weyl count (RX.2a)"},
     check="2I-irrep-dimension sums 12/14/16 != 15 -- true but the wrong surface (category error RX.2a)")
assert none_is_15

# ---- RX.2 the category errors -- DERIVED (the generation facts are the Lean core) --------
# generation = OUTER Z/3 (left-mult, fixed-point-free): 40/40/40. colour = INNER Z/3 (conj): 6 fixed + 38 triples.
GEN_BLOCKS = 120 // 3            # 40 -- left-mult by g3 is fixed-point-free -> 3 blocks of 40
GEN_FIXED = 0                    # left translation by g!=e has NO fixed points
GEN_COUNT = 3
COLOUR_FIXED = 6                 # conjugation by g3: 6 fixed (31.CS.1)
COLOUR_TRIPLES = 38             # + 38 three-cycles; 6 + 3*38 = 120
three_exactly_divides_120 = (120 % 3 == 0 and 120 % 9 != 0)   # 3^1 || 120 -> count cannot enlarge to Z/9
gen_ne_colour = (GEN_FIXED != COLOUR_FIXED)                    # outer (0 fixed) != inner (6 fixed)
step("RX.2", "the CATEGORY ERRORS: (a) wrong surface; (b) mass/weak-basis conflation (CKM/PMNS is normal); (c) generations = OUTER Z/3 (40/40/40) != colour = INNER Z/3 (6 fixed), a real structure dismissed; (d) premature root",
     "the four category errors that make the original 'K2 is a root' verdict WRONG: (a) WRONG SURFACE -- "
     "irrep dimensions vs a Weyl count (RX.1). (b) MASS/WEAK-BASIS CONFLATION -- the original 'sharp "
     "obstruction' pitted the vertex-defect MASS lattice (all w=0, even-Y) against the weak matter (w=1, "
     "odd-Y) as 'irreconcilable'; but mass-eigenbasis != weak-eigenbasis IS the SM (CKM/PMNS mixing) -- "
     "complementary aspects, not rival contents. (c) GENERATIONS DISMISSED -- generation is the OUTER Z/3 "
     "(left-mult by g3, FIXED-POINT-FREE -> 40/40/40), genuinely DISTINCT from colour = the INNER Z/3 "
     "(conjugation -> 6 fixed + 38 triples); they commute (9 joint labels); count 3 forced by 3^1||120. A "
     "real structure, wrongly waved off as 'just another three'. (d) PREMATURE ROOT -- irreducibility "
     "declared from wrong-surface failure",
     ["RX.1", "31.CS.1"],
     "the correction, with (c) carrying the Lean-checked facts. The decisive ones are (b) and (c). (b): I "
     "manufactured a contradiction out of the ordinary two-basis structure of the SM -- the mass basis and "
     "the weak basis differ, and that difference is physical (the mixing matrices), not a defect. (c): I "
     "repeatedly refused to engage generations as 'a dismissible three', but the fork (R10) distinguishes "
     "them exactly -- generation is left-multiplication (fixed-point-free, 40/40/40), colour is conjugation "
     "(6 fixed + 38 triples); they are different actions of the SAME order-3 element, they commute, and the "
     "count 3 is a divisibility fact (3^1 || 120), not a fit. Lean certifies: 40*3 = 120; 3 | 120 but 9 does "
     "not; and the outer action has 0 fixed points while the inner has 6 -- so they are genuinely different "
     "threes, and generation is a located structure, not a coincidence.",
     "UNIQUE (four category errors; generation=outer Z/3 (40/40/40, 0 fixed) != colour=inner Z/3 (6 fixed); 3^1||120)", "DERIVED",
     {"gen_blocks": GEN_BLOCKS, "gen_fixed": GEN_FIXED, "gen_count": GEN_COUNT,
      "colour_fixed": COLOUR_FIXED, "colour_triples": COLOUR_TRIPLES,
      "three_strictly_divides_120": three_exactly_divides_120, "gen_ne_colour": gen_ne_colour,
      "errors": ["a wrong surface", "b mass/weak-basis conflation", "c generations dismissed", "d premature root"]},
     check="generation=outer Z/3 (40/40/40, 0 fixed) != colour=inner Z/3 (6 fixed); 3^1||120; 4 category errors named")
assert three_exactly_divides_120 and gen_ne_colour and GEN_BLOCKS == 40

# ---- RX.3 the right surfaces, untested -- DERIVED ---------------------------------------
E8, A2, E6, GEN27, FAMILIES = 248, 8, 78, 27, 3
e8_decomp_ok = (A2 + E6 + FAMILIES * GEN27 + FAMILIES * GEN27 == E8)   # (8,1)+(1,78)+(3,27)+(3bar,27bar)
step("RX.3", "the RIGHT surfaces (UNTESTED in the original): (i) the regular rep C[2I] under joint colour x isospin x generation x hypercharge; (ii) E8 > A2 x E6 (248 = 8+78+3*27+3*27; the 27 = one generation)",
     "the surfaces that actually carry the SM matter content, none tested in the original attack: (i) the "
     "REGULAR REPRESENTATION C[2I] (dim 120) under the joint COMMUTING action -- colour = inner Z/3 (31), "
     "isospin = su(2)_L on H=C^2 (fork), generation = outer Z/3 (RX.2), hypercharge = Z/6 (58); the SM "
     "multiplets, if forced, live here. (ii) E8 > A2 x E6 (already touched in 31's scoped negative): "
     "248 = (8,1)+(1,78)+(3,27)+(3bar,27bar), and the 27 of E6 is one generation (16 of SO(10) + 10 + 1). "
     "Every SM label has a located substrate handle -- so K2 is a structured problem, not a bare input",
     ["RX.2", "58.HC.2", "30.SS.1", "12.RT.1"],
     "the honest map of where K2 must be tested. The substrate is not silent on the matter content -- it "
     "has a home for every SM label: colour (inner Z/3, 31 / A2 in E8, 30), isospin (su(2)_L, left-mult on "
     "H), hypercharge (the Z/6 grading, 58), generation (the outer Z/3, 40/40/40, count 3). The two natural "
     "surfaces are the regular rep under the joint action, and the E8 > A2 x E6 decomposition (Lean checks "
     "the E8 dimension bookkeeping 8+78+81+81=248). Whether either FORCES the SM content is the genuine open "
     "test -- and it is the most fitting-prone region in the program, so it is approached with maximal G5, "
     "target out of view.",
     "UNIQUE (two untested surfaces: regular rep joint action; E8 > A2 x E6, 248 = 8+78+3*27+3*27)", "DERIVED",
     {"e8": E8, "a2": A2, "e6": E6, "gen27": GEN27, "families": FAMILIES, "e8_decomp_ok": e8_decomp_ok,
      "surfaces": ["regular rep C[2I] under colour x isospin x generation x hypercharge", "E8 > A2 x E6"],
      "handles": {"colour": "inner Z/3 (31) / A2 (30)", "isospin": "su(2)_L on H=C^2",
                  "hypercharge": "Z/6 (58)", "generation": "outer Z/3 (40/40/40, count 3 via 3^1||120)"}},
     check="right surfaces exist: regular rep joint action; E8 > A2 x E6 (8+78+3*27+3*27 = 248)")
assert e8_decomp_ok

# ---- RX.4 K2 re-opened, the root verdict withdrawn -- POSTULATE (filed 19) --------------
step("RX.4", "(reading, POSTULATE) K2 is RE-OPENED -- NOT an irreducible root, but a partially-structured OPEN problem with real handles; the original 'root' verdict is withdrawn",
     "the corrected reading, filed through 19. K2 is NOT an irreducible root: the original verdict rested on "
     "category errors (RX.2). It is a PARTIALLY-STRUCTURED, genuinely-OPEN problem -- the substrate provides "
     "a located handle for every SM label (RX.3), but whether the right surfaces FORCE the SM content "
     "(3 generations of the specific multiplets, anomaly-free) is untested. The 'K2 is a root' claim (the "
     "original KA.5) is WITHDRAWN",
     ["RX.2", "RX.3"],
     "the honest standing after the re-examination. What is retracted: 'K2 is an irreducible root'. What "
     "replaces it: K2 is an open, structured problem. The roots ledger (FRONTIER) accordingly drops K2 from "
     "the earned-root set -- the only earned root remains the 3 Planck anchors (27). This is the correction "
     "of an over-correction: hunting the true bottom, I banked a root that was not earned. No downstream "
     "premise rests on this reading.",
     "POSTULATE (K2 re-opened, not a root; a partially-structured open problem; the root verdict withdrawn)", "POSTULATE",
     {"retracted": "the original 'K2 is a genuine root' verdict (KA.5)",
      "now": "K2 is a partially-structured, genuinely-open problem with located handles (RX.3)",
      "earned_root_set_now": "the 3 Planck anchors only (K2 removed)",
      "downstream_premise_use": False},
     check=None)

# ---- RX.5 OWED: the real test, paused -----------------------------------------------------
step("RX.5", "OWED: the real test -- decompose the right surfaces (regular rep joint action; E8 > A2 x E6) for 3 generations of SM multiplets, target out of view, refused-list at MAXIMUM. Paused (Kevin: step back first)",
     "OWED: the genuine K2 test -- decompose (i) the regular rep C[2I] under the joint colour x isospin x "
     "generation x hypercharge action, and/or (ii) E8 > A2 x E6, and see whether 3 generations of the "
     "specific SM multiplets emerge, anomaly-free -- TARGET OUT OF VIEW, with the refused-list at MAXIMUM "
     "(this is the single most fitting-prone region in the program; E8 GUT-matching is exactly where "
     "renaming is most tempting). Deliberately PAUSED before the test (Kevin: 'step back further first')",
     ["RX.3", "RX.4"],
     "the honest residual and the pause. The re-examination is the deliverable of this pass; the surface "
     "test is the next crossing, and it is gated by discipline, not by a wall: computed-then-compared, "
     "name-erased (G3), refuter-first (G4), no assembling to the SM (G5). Until it is run, K2 stands as an "
     "open, structured problem -- neither a forced result nor an irreducible root.",
     "OWED (the surface test -- regular rep / E8 > A2 x E6 -- target out of view, refused-list maximum; paused)", "OWED",
     {"owed_test": "decompose the regular rep (joint action) and/or E8 > A2 x E6 for 3 generations of SM multiplets",
      "discipline": "target out of view; refused-list at maximum (most fitting-prone region)",
      "status": "PAUSED (step back further first)", "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="60-content-a-root",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        vdef_dim=VDEF_DIM, spinor_dim=SPINOR_DIM, vector_dim=VECTOR_DIM, sm_gen=SM_GEN, none_is_15=none_is_15,
        gen_blocks=GEN_BLOCKS, gen_fixed=GEN_FIXED, gen_count=GEN_COUNT,
        colour_fixed=COLOUR_FIXED, colour_triples=COLOUR_TRIPLES,
        three_strictly_divides_120=three_exactly_divides_120, gen_ne_colour=gen_ne_colour,
        e8=E8, a2=A2, e6=E6, gen27=GEN27, families=FAMILIES, e8_decomp_ok=e8_decomp_ok,
        retraction="the original 'K2 is a genuine root' verdict is RETRACTED (Kevin's re-examination, "
                   "2026-09-11; CORRECTIONS #9) -- it rested on category errors",
        finding="CONTENT SELECTION (K2): THE RE-EXAMINATION. The original 'K2 is a root' verdict is "
                "RETRACTED -- category errors: (a) it compared 2I-irrep DIMENSIONS (12/14/16) to a "
                "WEYL-FERMION count (15) -- the wrong surface (RX.1); (b) it mistook mass-basis vs "
                "weak-basis (the normal SM CKM/PMNS two-basis structure) for an 'irreconcilable' "
                "contradiction; (c) it dismissed generations, which are actually the OUTER Z/3 (left-mult, "
                "fixed-point-free -> 40/40/40), genuinely DISTINCT from colour = the INNER Z/3 (conjugation "
                "-> 6 fixed + 38 triples), commuting (9 joint labels), count 3 forced by 3^1||120; (d) it "
                "declared 'root' from wrong-surface failure (RX.2). The RIGHT surfaces were UNTESTED: the "
                "regular rep C[2I] under joint colour(inner Z/3) x isospin(su(2)_L) x generation(outer Z/3) "
                "x hypercharge(Z/6), and E8 > A2 x E6 (248 = 8+78+3*27+3*27; the 27 = one generation) "
                "(RX.3). So K2 is RE-OPENED (RX.4): NOT an irreducible root, but a partially-structured "
                "OPEN problem with a located handle for every SM label. The real test on the right surfaces "
                "is OWED and deliberately PAUSED (RX.5). The earned-root set drops back to the 3 Planck "
                "anchors only. Nothing fitted; an over-correction corrected.",
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
