#!/usr/bin/env python3
"""Container 61 -- THE K2 SURFACE TEST: do the right surfaces FORCE the SM content? (Kevin: "go")

Run the test container 60 said was owed, TARGET OUT OF VIEW, refused-list at MAXIMUM (E8 GUT-matching is the
single most fitting-prone region in the program). Two surfaces: (A) E8 > A2 x E6; (B) the regular rep C[2I]
under the joint colour x isospin x generation x hypercharge action. The honest question: does either FORCE
3 generations of the specific SM multiplets? Let it land where the truth is -- neither fit nor dismiss.

  ST.1  Surface A -- E8 > A2 x E6 EXISTS and gives a generation structure: 248 = (8,1)+(1,78)+(3,27)+
        (3bar,27bar) [8+78+3*27+3*27]; 240 roots = 6+72+162; the (3,27) is 3 copies of the E6 27, and
        27 = 16+10+1 of SO(10) with the 16 = one SM generation. So E8 -> E6 x SU(3) yields (27,3) = 3
        generations of matter. DERIVED (the branching arithmetic; container 12's roots).
  ST.2  ...but Surface A does NOT FORCE the SM content -- it is a filed PARALLEL, not a forcing:
        (i) GENERIC -- this branching holds for EVERY E8 theory, not this substrate specifically (G3
            renaming: erase 'generation'/'SM' and it is a bare group-theory identity);
        (ii) WEYL-ARBITRARY -- 31 established all A2 subgroups of E8 are Weyl-transitive (1120 checked), so
             there is NO distinguished colour/family A2; the embedding singles out nothing;
        (iii) UNPROJECTED -- the substrate forces neither matter=(3,27) (vs the adjoint or other pieces) nor
              the projection of the 27's EXOTIC states (the 10+1 beyond the 16). G4: no refuter -- every E8
              theory 'works'. So E8 is a promising LEAD, filed POSTULATE, never banked. DERIVED (the
              non-forcing, citing 31).
  ST.3  Surface B -- the regular rep C[2I] (dim = sum d_i^2 = 120) under generation = the OUTER Z/3
        (left-mult by g3, fixed-point-free) gives EXACTLY 3 blocks of 40. The count 3 is SUBSTRATE-SPECIFIC
        (3^1 || 120), NOT generic-E8 -- the one genuine substrate handle on a generation NUMBER. DERIVED.
  ST.4  ...but Surface B does NOT force the CONTENT either: one generation block is 40 states, while one SM
        generation is 15 (16 with nu_R); 40 != 15, 40 != 16, and no substrate principle SELECTS which of the
        40 states are the fermions. So the multiplet content is unforced on B as well. DERIVED.
  ST.5  (reading, POSTULATE) THE VERDICT: neither surface forces the SM CONTENT (the multiplets/
        hypercharges) -- A is generic-E8 (renaming), B has no forced selection. But the generation COUNT (3)
        has a genuine SUBSTRATE-SPECIFIC handle (outer Z/3 + 3^1||120), CONDITIONAL on the identification
        generation = the outer Z/3 (motivated by the triadic floor 00/A3, not proven). So K2 stays OPEN --
        partly structured (the count 3, near-forced), partly open (the content, unforced) -- NOT a root, NOT
        solved, NOT refuted. POSTULATE.
  ST.6  OWED: a substrate principle that SELECTS the multiplet content (would force K2, then cascade or
        refute), OR proof the content needs an external input; the E8 embedding made non-generic (a
        substrate reason to pick THIS A2 and matter=(3,27)); the generation=outer-Z/3 identification made
        rigorous. Generations-count-3 is a REDUCTION to that identification, not fished. OWED.

THE HEADLINE: the K2 surface test, run with discipline -- neither the E8 > A2 x E6 route (generic to every
E8 theory; A2 Weyl-arbitrary; exotics unprojected -> a filed lead, not a forcing) nor the regular rep (no
forced selection of which states are matter) FORCES the SM content. The one genuine substrate-specific
result is the generation COUNT 3 (outer Z/3 + 3^1||120), conditional on generation = the outer Z/3. So K2
is OPEN, partly structured -- content unforced, count-3 near-forced -- neither a root nor solved. Nothing
fitted; the most seductive route (E8 GUT 3-generations) is filed as a lead, not banked. Rests on 60
(the re-examination), 12/30 (E8/A2), 31 (Weyl-transitivity), 58 (hypercharge). Cites E8 > A2 x E6,
E6 > SO(10), the SM generation, the fork R10.
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


# ---- ST.1 Surface A exists and gives a generation structure -- DERIVED ------------------
E8, A2, E6, GEN27, FAM = 248, 8, 78, 27, 3
ROOTS_E8, ROOTS_A2, ROOTS_E6, ROOTS_MATTER = 240, 6, 72, 162
e8_decomp = (A2 + E6 + FAM * GEN27 + FAM * GEN27 == E8)
roots_decomp = (ROOTS_A2 + ROOTS_E6 + ROOTS_MATTER == ROOTS_E8)
so10_27 = (16 + 10 + 1 == GEN27)
step("ST.1", "Surface A -- E8 > A2 x E6 EXISTS: 248 = 8+78+3*27+3*27; 240 = 6+72+162; the (3,27) = 3 copies of the 27; 27 = 16+10+1 (16 = one SM generation) -> 3 generations of matter",
     "E8 branches under A2 x E6 as 248 = (8,1)+(1,78)+(3,27)+(3bar,27bar); on container 12's 240 roots this "
     "is 240 = 6(A2) + 72(E6) + 162((3,27)+(3bar,27bar)). The (3,27) is 3 copies (an A2-triplet) of the E6 "
     "27, and 27 = 16+10+1 of SO(10) with the 16 the SO(10) spinor = one SM generation (with nu_R). So "
     "E8 -> E6 x SU(3) yields (27,3) = 3 GENERATIONS of matter -- a real, celebrated branching",
     ["60.RX.3", "12.RT.1", "30.SS.1"],
     "Surface A engaged honestly and at full strength -- this IS the standard, beautiful E8 route to three "
     "generations, and the substrate HAS E8 (12). The decomposition is exact group theory (Lean checks the "
     "dimension and root bookkeeping). Taken at face value it looks like a derivation of 3 generations of SM "
     "matter. ST.2 asks whether the SUBSTRATE forces it, or whether it is generic.",
     "UNIQUE (E8 > A2 x E6: 248=8+78+3*27+3*27; 240=6+72+162; 27=16+10+1; (27,3)=3 generations)", "DERIVED",
     {"e8": E8, "a2": A2, "e6": E6, "gen27": GEN27, "families": FAM,
      "roots": {"e8": ROOTS_E8, "a2": ROOTS_A2, "e6": ROOTS_E6, "matter": ROOTS_MATTER},
      "e8_decomp": e8_decomp, "roots_decomp": roots_decomp, "so10_27": so10_27},
     check="E8 > A2 x E6: 248=8+78+3*27+3*27; 240=6+72+162; 27=16+10+1; (27,3) = 3 generations")
assert e8_decomp and roots_decomp and so10_27

# ---- ST.2 Surface A does NOT force -- generic, Weyl-arbitrary, unprojected -- DERIVED ----
step("ST.2", "...but Surface A does NOT FORCE the SM content: (i) GENERIC to every E8 theory (G3 renaming); (ii) the A2 is WEYL-ARBITRARY (31, 1120 checked); (iii) the 27's exotics (10+1) are UNPROJECTED. A filed lead, not a forcing",
     "Surface A is a filed PARALLEL, not a forcing: (i) GENERIC -- the branching 248 = (78,1)+(1,8)+(27,3)+ "
     "(27bar,3bar) holds for EVERY theory built on E8; it is a property of E8's representation theory, not "
     "of THIS substrate. Erase 'generation' and 'SM' (G3) and nothing substrate-specific remains. (ii) "
     "WEYL-ARBITRARY -- container 31 established all A2 subgroups of E8 are Weyl-transitive (1120 checked), "
     "so the embedding singles out NO distinguished colour-or-family A2; the choice is arbitrary. (iii) "
     "UNPROJECTED -- the substrate forces neither matter=(3,27) (vs the adjoint (8,1)+(1,78) or the "
     "conjugate) nor the removal of the 27's EXOTIC states (the 10+1 beyond the generation 16). G4: no "
     "refuter -- any E8 theory reproduces this. So E8 is a promising LEAD, never banked",
     ["ST.1", "31.CS.4"],
     "the disciplined verdict on the most seductive route in the whole program -- neither fit nor dismiss. "
     "It is NOT dismissed: E8 -> E6 x SU(3) giving 3 generations is real and the substrate has E8, so it is "
     "a genuine lead, filed as a PARALLEL. It is NOT banked: it fails the gates as a FORCING -- generic to "
     "all E8 (G3 renaming), the A2 Weyl-arbitrary (31, no distinguished embedding), and the exotic states "
     "unprojected by any substrate rule (G4/G5: no refuter, no forced selection). This is exactly where the "
     "refused-list is at maximum: an E8-GUT match is the easiest renaming in physics. So: a lead, held; not "
     "a substrate forcing of the SM content.",
     "UNIQUE (E8 route is generic + Weyl-arbitrary + unprojected -> a filed lead, NOT a forcing)", "DERIVED",
     {"generic_to_all_E8": True, "a2_weyl_arbitrary": "31: 1120 A2's, Weyl-transitive -> no distinguished embedding",
      "exotics_unprojected": "the 27's 10+1 beyond the 16 are not projected by any substrate rule",
      "grade": "filed PARALLEL / lead -- fails G3 (generic/renaming), G4 (no refuter); NOT banked"},
     check="Surface A: generic to all E8 + A2 Weyl-arbitrary (31) + exotics unprojected -> a lead, not a forcing")

# ---- ST.3 Surface B: the outer-Z/3 generation count 3 is substrate-specific -- DERIVED --
REG_DIM = sum(d * d for d in (1, 2, 2, 3, 3, 4, 4, 5, 6))    # 120
GEN_BLOCK = REG_DIM // 3                                      # 40
three_strict = (120 % 3 == 0 and 120 % 9 != 0)               # 3^1 || 120
step("ST.3", "Surface B -- the regular rep C[2I] (dim = sum d_i^2 = 120) under generation = the OUTER Z/3 (left-mult, fixed-point-free) gives EXACTLY 3 blocks of 40; count 3 is substrate-specific (3^1||120), not generic-E8",
     "the regular representation C[2I] has dimension sum d_i^2 = 120 = |2I|. Under generation = the OUTER "
     "Z/3 (left-multiplication by an order-3 element g3, which is fixed-point-free), it splits into EXACTLY "
     "3 equal blocks of 40 (40/40/40). The count 3 is a SUBSTRATE-SPECIFIC divisibility fact -- 3^1 || 120 "
     "(3 divides 120, 9 does not) -- so the generation grading cannot enlarge to Z/9. This is genuinely a "
     "property of 2I (|2I| = 120 = 2^3 * 3 * 5), NOT a generic-E8 statement",
     ["ST.2", "60.RX.2"],
     "Surface B, the substrate-specific one. Unlike the E8 route (generic), the outer-Z/3 generation grading "
     "is a fact about 2I in particular: left-multiplication by an order-3 element is fixed-point-free, giving "
     "3 blocks of 40, and 3^1 || 120 forbids enlargement. So IF generation is the outer Z/3, the count is "
     "exactly 3 -- forced, and forced by this substrate, not by generic E8 group theory. This is the one "
     "piece of K2 with a real substrate handle on a NUMBER.",
     "UNIQUE (regular rep 120; outer-Z/3 generation -> 3 blocks of 40; 3^1||120 forbids Z/9)", "DERIVED",
     {"reg_dim": REG_DIM, "gen_block": GEN_BLOCK, "gen_count": 3, "three_strict": three_strict,
      "substrate_specific": "3^1||120 is a property of |2I|=120, not generic-E8"},
     check="regular rep dim 120; outer-Z/3 -> 3 blocks of 40; 3^1||120 (substrate-specific count 3)")
assert REG_DIM == 120 and GEN_BLOCK == 40 and three_strict

# ---- ST.4 Surface B does NOT force the content -- DERIVED --------------------------------
SM_GEN, SM_NUR = 15, 16
block_ne_gen = (GEN_BLOCK != SM_GEN and GEN_BLOCK != SM_NUR)
step("ST.4", "...but Surface B does NOT force the CONTENT: one generation block is 40 states, one SM generation is 15 (16 w/ nu_R); 40 != 15, 40 != 16, and no substrate principle SELECTS which states are the fermions",
     "the count is not the content. One generation block is 40 states; one SM generation is 15 Weyl fermions "
     "(16 with nu_R). 40 != 15 and 40 != 16 -- the block is LARGER than one generation's fermion content "
     "(it presumably carries gauge and other degrees of freedom too), and NO substrate principle selects "
     "which of the 40 are the matter fermions with which colour/isospin/hypercharge. So Surface B fixes the "
     "generation COUNT but not the multiplet CONTENT",
     ["ST.3"],
     "the honest limit of Surface B. The regular rep gives 3 generation blocks, but a block (40) is not one "
     "SM generation (15/16) -- so the content within a block is not determined by the grading alone, and "
     "there is no forced rule picking 'the fermions' out of the 40. This is the same open selection K2 has "
     "always been: the count is handled, the content is not.",
     "UNIQUE (generation block = 40 != SM 15/16; no forced selection of the fermions within a block)", "DERIVED",
     {"gen_block": GEN_BLOCK, "sm_gen": SM_GEN, "sm_nu_r": SM_NUR, "block_ne_gen": block_ne_gen,
      "content_forced": False},
     check="generation block 40 != SM 15/16; no forced fermion selection -> content unforced on B")
assert block_ne_gen

# ---- ST.5 the verdict -- POSTULATE (filed 19) -------------------------------------------
step("ST.5", "(verdict, POSTULATE) neither surface forces the SM CONTENT (A generic/renaming; B no forced selection); the generation COUNT 3 has a genuine substrate handle (outer Z/3 + 3^1||120), conditional on generation = the outer Z/3. K2 OPEN -- not a root, not solved, not refuted",
     "the honest verdict of the surface test. The CONTENT of K2 (which multiplets, which hypercharges) is "
     "NOT forced by either surface: A is generic to every E8 theory (a renaming, not a substrate forcing) "
     "and the A2 is Weyl-arbitrary; B has no forced selection of the fermions within a 40-block. What DOES "
     "have a genuine, substrate-specific handle is the generation COUNT 3 -- the outer Z/3 (left-mult) + "
     "3^1||120 -- but this is CONDITIONAL on the identification generation = the outer Z/3, motivated by "
     "the triadic floor (00/A3, three roles) yet not proven, and it is a REDUCTION to that identification, "
     "not a cold forcing. So K2 stays OPEN: partly structured (the count 3, near-forced), partly open (the "
     "content, unforced) -- NOT an irreducible root, NOT solved, NOT refuted",
     ["ST.2", "ST.4"],
     "the corrected, disciplined standing after actually running the test. This neither re-declares K2 a "
     "root (the retracted over-claim) nor bangs an E8-GUT match (the over-affirmation twin). The truth in "
     "the middle: the substrate has real handles (a substrate-specific generation count 3; a generic E8 "
     "embedding as a lead) but forces no SM CONTENT. The generation-count 3 is the strongest genuine result "
     "-- and it is a reduction to 'generation = the outer Z/3', which links generations to the triadic "
     "floor, the deepest axiom (00). Whether that identification is forced is the live question. No "
     "downstream premise rests on this reading.",
     "POSTULATE (K2 open: content unforced by either surface; count 3 near-forced via the outer Z/3 identification)", "POSTULATE",
     {"content_forced": False, "count_3_handle": "outer Z/3 + 3^1||120 (substrate-specific), conditional on generation=outer-Z/3",
      "surface_A": "generic-E8 lead, not a forcing (renaming)", "surface_B": "no forced fermion selection",
      "status": "K2 OPEN -- not a root, not solved, not refuted; partly structured",
      "downstream_premise_use": False},
     check=None)

# ---- ST.6 OWED --------------------------------------------------------------------------
step("ST.6", "OWED: a principle that SELECTS the multiplet content (forces K2 -> cascade/refute); a substrate reason to pick THIS A2 + matter=(3,27) (make E8 non-generic); the generation=outer-Z/3 identification made rigorous",
     "OWED: (a) a substrate principle that SELECTS the multiplet content -- which fermions, with which "
     "quantum numbers -- which would force K2 and then cascade (theta_W, hypercharges, masses) or refute; "
     "(b) a substrate reason to pick THIS A2 in E8 and matter = (3,27) (and to project the exotics), which "
     "would make the E8 route non-generic -- a real forcing rather than a lead; (c) the identification "
     "generation = the outer Z/3 made rigorous (currently the count-3 reduces to it). Generations-count-3 "
     "is a REDUCTION to (c), never fished; no content is assembled to the SM (the refused-list binds)",
     ["ST.5"],
     "the honest residual. The test is run; the result is that neither right surface forces the content, "
     "and the E8 route -- the most tempting -- is a generic lead, not a forcing. What would move K2: a "
     "genuine selection principle (content), a non-generic reason for the E8 embedding, or a proof that "
     "generation IS the outer Z/3 (count). Until then K2 is open and partly structured, and the discipline "
     "holds: the E8 3-generations match is filed as a lead, not banked.",
     "OWED (a content-selection principle; a non-generic E8 reason; the generation=outer-Z/3 identification)", "OWED",
     {"owed_content": "a substrate principle selecting the multiplet content (forces K2)",
      "owed_e8": "a substrate reason for THIS A2 + matter=(3,27) + exotic projection (non-generic)",
      "owed_generation": "generation = the outer Z/3 made rigorous (the count-3 reduces to it)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="61-k2-surface-test",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        e8=E8, a2=A2, e6=E6, gen27=GEN27, families=FAM,
        roots_e8=ROOTS_E8, roots_a2=ROOTS_A2, roots_e6=ROOTS_E6, roots_matter=ROOTS_MATTER,
        e8_decomp=e8_decomp, roots_decomp=roots_decomp, so10_27=so10_27,
        reg_dim=REG_DIM, gen_block=GEN_BLOCK, gen_count=3, three_strict=three_strict,
        sm_gen=SM_GEN, sm_nu_r=SM_NUR, block_ne_gen=block_ne_gen, content_forced=False,
        finding="THE K2 SURFACE TEST (Kevin: 'go'), target out of view, refused-list at MAXIMUM. Surface A "
                "(E8 > A2 x E6): 248=8+78+3*27+3*27, 240=6+72+162, (3,27)=3 copies of the 27, 27=16+10+1 -> "
                "3 generations of matter (ST.1) -- a real, celebrated branching. BUT it does NOT FORCE the "
                "SM content (ST.2): GENERIC to every E8 theory (G3 renaming), the A2 WEYL-ARBITRARY (31, "
                "1120 checked -> no distinguished embedding), the 27's exotics (10+1) UNPROJECTED (G4 no "
                "refuter) -- a filed LEAD, never banked. Surface B (regular rep C[2I], dim 120): generation "
                "= the OUTER Z/3 (left-mult) -> EXACTLY 3 blocks of 40; count 3 substrate-specific (3^1||120) "
                "(ST.3); but a block (40) != one SM generation (15/16) and no principle selects the fermions "
                "-> content unforced (ST.4). VERDICT (ST.5): neither surface forces the CONTENT; the "
                "generation COUNT 3 has a genuine substrate handle (outer Z/3 + 3^1||120), conditional on "
                "generation = the outer Z/3 (a reduction, motivated by the triadic floor 00/A3, not proven). "
                "K2 stays OPEN -- partly structured (count 3), partly open (content) -- NOT a root, NOT "
                "solved, NOT refuted. OWED (ST.6): a content-selection principle; a non-generic E8 reason; "
                "the generation=outer-Z/3 identification. Nothing fitted; the E8 GUT match is a lead, held.",
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
