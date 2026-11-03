#!/usr/bin/env python3
"""Container 58 -- the NATIVE HYPERCHARGE GRADING (SU(3)xSU(2)xU(1))/Z6, from the collaborator's fork.

Kevin handed over the collaborator's fork (PrimeFramework docs, 2026-09-10): "these should answer your
questions on the fork ... you may have to rederive some of this to integrate it at the project's standard."
This container REDERIVES the fork's hypercharge result (its R27 / F14) cold, on OUR substrate, at OUR
standard (derivation.py + Lean + verify, honest grades). It upgrades container 51's HELD joint (the SM
gauge product with the joint deferred) and is the concrete structure container 57 said the Weinberg angle
was owed to.

The fork's route abandons the mass-founded Gell-Mann-Nishijima Q = T3 + Y (flagged contaminated) and uses
two NATIVE gradings of the carrier instead:
  - t = colour triality, Z/3 (our container 31: the order-3 element g3, 6 fixed + 38 three-cycles);
  - w = duality, Z/2 (our container 45: the central -1 of 2I; spinor 1 / vector 0 -- the central character).
Their product is Z/3 x Z/2 = Z/6 -- exactly the centralizer <g3,-1> = Z/6 already found in 31.CS.2.

  HC.1  the two native gradings: t in Z/3 (31) and w in Z/2 (45). DERIVED.
  HC.2  they combine to Z/6: Z/3 x Z/2 = Z/6 (CRT); Y6 = -(2t+3w) mod 6 is a BIJECTION to Z/6 (coeffs
        2 = 6/3, 3 = 6/2 -- the prime coefficients). So the SM gauge group is (SU(3)xSU(2)xU(1))/Z6 from two
        native gradings -- upgrading 51's held joint. DERIVED (Lean: the 6 residues are all distinct).
  HC.3  the fractional hypercharge grading Y = -(t/3 + w/2) is FORCED (its fractional/mod-6 part); the SM
        pieces (Q,L,u_c,d_c,e_c) carry residues -(2t+3w) mod 6 = {1,3,2,2,0}. DERIVED (the fractional part).
  HC.4  anomaly-freedom: on the SM chiral content Y6 = {+1,-3,-4,+2,+6} with multiplicities {6,2,3,3,1}
        (colour x isospin), both anomaly sums vanish: sum m*Y6 = 0 (grav/mixed) and sum m*Y6^3 = 0 (U(1)^3).
        DERIVED (Lean, split +/- in Nat). This certifies the grading is CONSISTENT with the SM content.
  HC.5  the absolute levels are CONDITIONAL (K2): the fractional part is forced (HC.3), but the integer
        levels 6n -- which distinguish e.g. u_c (Y6=-4) from d_c (Y6=+2), same (t,w)=(2,0) -- need the
        multiplet CONTENT selection (which irreps are the fermions), NOT yet derived (fork's K2, open). The
        correspondence to SM hypercharges. POSTULATE (filed 19).
  HC.6  OWED: the content selection K2 (the representation assignment); and the bearing on 57 -- the fork's
        sin^2(theta_W) = 1/phi^3 ~ 0.2361 is a FENCED candidate (the fork grades it CONSISTENCY / OBSERVATION,
        inversion-then-match, representation UNFORCED, 2.1% off measured 0.23122) -- NOT banked. So 57's cold
        theta_W remains owed to K2. OWED.

THE HONEST HEADLINE: the SM gauge group (SU(3)xSU(2)xU(1))/Z6 and the FRACTIONAL hypercharge grading
Y = -(t/3+w/2) are FORCED from two native gradings (colour Z/3, 31; duality Z/2, 45); the SM content is
anomaly-free under it (Lean). The ABSOLUTE levels (K2) and the sin^2(theta_W) value stay owed; 1/phi^3 is a
fenced candidate, not banked. Rests on 31 (colour Z/3), 45 (central -1 / Z/2), 30 (su(3)), 28 (su(2)),
29 (u(1)), 51 (the product/joint). Cites the fork's R27/F14, the SM hypercharges, the anomaly conditions.
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


# ---- HC.1 the two native gradings -- DERIVED -------------------------------------------
Z3 = 3    # colour triality (31)
Z2 = 2    # duality / central character (45)
step("HC.1", "the two native gradings: colour triality t in Z/3 (31) and duality w in Z/2 (45, the central -1)",
     "the substrate carries two native discrete gradings: (i) colour TRIALITY t in Z/3 -- container 31's "
     "order-3 element g3 partitions the 120 into 6 fixed + 38 three-cycles, the ℤ/3 colour seating; (ii) "
     "DUALITY w in Z/2 -- container 45's central -1 of 2I (2π ↦ -1 on spinors, 4π ↦ +1), the central "
     "character splitting the irreps into vector (w=0) and spinor (w=1). Both are FORCED carrier structure, "
     "not chosen",
     ["31.CS.1", "45.SP.2"],
     "the two ingredients, both already DERIVED in the corpus. Triality is 31's cold ℤ/3 (the order-3 "
     "element, exhaustive on the 120). Duality is 45's central -1 -- the ℤ/2 central character of 2I "
     "(spinor vs vector). 31.CS.2 already noted the colour element's centralizer is <g3,-1> = ℤ/6 = "
     "ℤ/3 × ℤ/2 -- so the two gradings live together natively. No mass, no Nishijima Q, no chosen embedding.",
     "UNIQUE (t in Z/3 from 31; w in Z/2 from 45)", "DERIVED",
     {"triality_order": Z3, "duality_order": Z2,
      "t_source": "31.CS.1 (order-3 element g3, colour ℤ/3)", "w_source": "45.SP.2 (central -1, spinor/vector)"},
     check="two native gradings: colour triality t in Z/3 (31), duality w in Z/2 (45)")
assert Z3 == 3 and Z2 == 2

# ---- HC.2 they combine to Z/6 -- DERIVED (Lean) ----------------------------------------
# residues -(2t+3w) mod 6 over (t,w) in Z3 x Z2, computed as Nat: (6 - (2t+3w) % 6) % 6
def y6(t, w):
    return (6 - ((2 * t + 3 * w) % 6)) % 6
RESIDUES = [y6(t, w) for t in range(3) for w in range(2)]   # order (0,0)(0,1)(1,0)(1,1)(2,0)(2,1)
z6_bijection = (sorted(RESIDUES) == [0, 1, 2, 3, 4, 5])      # all of Z/6 -> a bijection
step("HC.2", "they combine to Z/6: Z/3 x Z/2 = Z/6 (CRT); Y6 = -(2t+3w) is a bijection to Z/6 -- the SM group is (SU(3)xSU(2)xU(1))/Z6",
     "the two gradings combine by CRT: Z/3 x Z/2 = Z/6. The hypercharge in x6 units, Y6 = -(2t+3w) mod 6, "
     "is a BIJECTION (t,w) -> Z/6 (coefficients 2 = 6/3 and 3 = 6/2, the prime coefficients): over the six "
     "(t,w) the residues are {0,1,2,3,4,5}, all of Z/6. So the shared centre is Z/6 (= the colour element's "
     "centralizer <g3,-1>, 31.CS.2) and the SM gauge group is (SU(3) x SU(2) x U(1)) / Z6 -- realised from "
     "two NATIVE gradings, upgrading 51's held joint",
     ["HC.1", "31.CS.2", "51.GP.2"],
     "the joint, native. Container 51 located the product U(1)xSU(2)xSU(3) but DEFERRED the joint (the "
     "shared centre / embedding) to this fork. Here it closes natively: the colour ℤ/3 (31) and the duality "
     "ℤ/2 (45) are exactly the two factors of ℤ/6, and their combined character Y6 = -(2t+3w) runs bijectively "
     "over ℤ/6. The quotient group (SU(3)xSU(2)xU(1))/ℤ6 is the true SM gauge group (the ℤ6 identifies the "
     "shared centre so that integer electric charges come out) -- and here the ℤ6 is not imposed, it IS the "
     "centralizer 31 already found. Lean certifies the six residues are all distinct (a bijection to ℤ/6).",
     "UNIQUE (Y6 = -(2t+3w) bijects Z3xZ2 -> Z/6; the SM group is (SU(3)xSU(2)xU(1))/Z6)", "DERIVED",
     {"residues": RESIDUES, "z6_bijection": z6_bijection,
      "gauge_group": "(SU(3) x SU(2) x U(1)) / Z6", "coefficients": [2, 3],
      "note": "Z6 = <g3,-1> = the colour element's centralizer (31.CS.2)"},
     check="Y6 = -(2t+3w) bijects Z/3 x Z/2 -> Z/6 (residues = {0..5}); SM group (SU(3)xSU(2)xU(1))/Z6")
assert z6_bijection

# ---- HC.3 the fractional grading is forced -- DERIVED ----------------------------------
# SM pieces (Q, L, u_c, d_c, e_c): Y6 (x6 units, with the integer 6n shift) and their mod-6 residues
SM_PIECES = ["Q", "L", "u_c", "d_c", "e_c"]
Y6_SM = [1, -3, -4, 2, 6]                          # -(2t+3w) + 6n, x6 units (the SM hypercharges x6)
RESID_SM = [y % 6 for y in Y6_SM]                  # the FORCED fractional part = -(2t+3w) mod 6
step("HC.3", "the fractional hypercharge grading Y = -(t/3 + w/2) is FORCED; the SM pieces carry residues -(2t+3w) mod 6 = {1,3,2,2,0}",
     "the native grading is Y = -(t/3 + w/2) (mod 1); its FRACTIONAL part is forced by the two gradings "
     "(HC.2). For the SM chiral pieces (Q, L, u_c, d_c, e_c) the x6 hypercharges are Y6 = {+1,-3,-4,+2,+6}, "
     "whose forced fractional (mod-6) residues are {1,3,2,2,0} -- matching Q=1/6, L=-1/2, u_c=-2/3, d_c=1/3, "
     "e_c=1. The fractional grading is native and forced; only the integer level (the 6n) is open (HC.5)",
     ["HC.2"],
     "the forced content, stated honestly. The fractional part of each hypercharge is fixed by (t,w) via "
     "Y6 = -(2t+3w) mod 6 -- e.g. the quark doublet Q (colour t=1, spinor w=1) -> residue 1 = 6*(1/6); the "
     "lepton doublet L (t=0,w=1) -> 3 = 6*(-1/2 mod 1); e_c (t=0,w=0) -> 0 = 6*1. This is the FORCED, "
     "native, mass-free grading (no Gell-Mann-Nishijima Q). What it does NOT fix by itself: u_c and d_c "
     "share (t,w)=(2,0) (residue 2) and are distinguished only by the integer level (Y6 -4 vs +2, differing "
     "by 6) -- that is the absolute-level question K2 (HC.5).",
     "UNIQUE (fractional Y = -(t/3+w/2) forced; SM residues = {1,3,2,2,0})", "DERIVED",
     {"sm_pieces": SM_PIECES, "Y6_sm": Y6_SM, "residues_sm": RESID_SM,
      "forced": "the fractional part -(2t+3w) mod 6", "not_forced_here": "the integer level 6n (K2, HC.5)"},
     check="fractional grading Y = -(t/3+w/2) forced; SM residues -(2t+3w) mod 6 = {1,3,2,2,0}")
assert RESID_SM == [1, 3, 2, 2, 0]

# ---- HC.4 anomaly-freedom -- DERIVED (Lean) --------------------------------------------
MULT_SM = [6, 2, 3, 3, 1]                           # colour x isospin: Q=3x2, L=2, u_c=3, d_c=3, e_c=1
anomaly1 = sum(m * y for m, y in zip(MULT_SM, Y6_SM))            # sum m*Y6  (grav/mixed) -> 0
anomaly3 = sum(m * y ** 3 for m, y in zip(MULT_SM, Y6_SM))       # sum m*Y6^3 (U(1)^3)   -> 0
# split +/- for the Nat-decidable Lean certification
anom1_pos = 6 * 1 + 3 * 2 + 1 * 6                   # Q, d_c, e_c
anom1_neg = 2 * 3 + 3 * 4                           # L, u_c
anom3_pos = 6 * 1 + 3 * 8 + 1 * 216                 # 6*1^3 + 3*2^3 + 1*6^3
anom3_neg = 2 * 27 + 3 * 64                         # 2*3^3 + 3*4^3
step("HC.4", "anomaly-freedom: on the SM content Y6={+1,-3,-4,+2,+6}, mult={6,2,3,3,1}, both sum m*Y6 = 0 and sum m*Y6^3 = 0",
     "under the grading, the SM chiral content is anomaly-free: with multiplicities {6,2,3,3,1} (colour x "
     "isospin) and Y6 = {+1,-3,-4,+2,+6}, sum m*Y6 = 0 (the gravitational / mixed gauge-gravitational "
     "anomaly, Tr Y = 0) and sum m*Y6^3 = 0 (the U(1)^3 anomaly, Tr Y^3 = 0). Both vanish exactly -- the "
     "grading is CONSISTENT with the SM matter content",
     ["HC.3"],
     "the consistency check, cold and exact. The two U(1)_Y anomaly conditions are Tr Y = 0 and Tr Y^3 = 0 "
     "over a generation. On the SM content they vanish: sum m*Y6 = 6(1)+2(-3)+3(-4)+3(2)+1(6) = 0, and "
     "sum m*Y6^3 = 6(1)+2(-27)+3(-64)+3(8)+1(216) = 0. Lean certifies both by splitting into positive and "
     "negative parts in Nat (18 = 18 and 246 = 246). This is a genuine cold fact about the grading + the SM "
     "content; it does NOT by itself SELECT that content (that is K2, HC.5) -- Tr Y = Tr Y^3 = 0 over 2I's "
     "irreps does not fix which irreps are the fermions (31/51 note the same). So: the grading is "
     "anomaly-consistent with the SM content, content selection owed.",
     "UNIQUE (sum m*Y6 = 0 and sum m*Y6^3 = 0 on the SM content -- anomaly-free)", "DERIVED",
     {"mult_sm": MULT_SM, "anomaly1": anomaly1, "anomaly3": anomaly3,
      "anom1_pos": anom1_pos, "anom1_neg": anom1_neg, "anom3_pos": anom3_pos, "anom3_neg": anom3_neg,
      "reading": "Tr Y = 0 (grav/mixed) and Tr Y^3 = 0 (U(1)^3); content selection is K2 (HC.5)"},
     check="anomaly-free on SM content: sum m*Y6 = 0 (18=18) and sum m*Y6^3 = 0 (246=246)")
assert anomaly1 == 0 and anomaly3 == 0
assert anom1_pos == anom1_neg and anom3_pos == anom3_neg

# ---- HC.5 the absolute levels are conditional (K2) -- POSTULATE (filed 19) --------------
step("HC.5", "the absolute levels are CONDITIONAL (K2): the fractional part is forced, but the integer levels 6n need the multiplet CONTENT selection -- not yet derived",
     "the fractional hypercharge is forced (HC.3), but the ABSOLUTE integer levels (the 6n shift) are "
     "CONDITIONAL on the multiplet CONTENT -- which carrier irreps constitute the fermions and their (t,w) "
     "embedding. Example: u_c and d_c share (t,w)=(2,0) (residue 2) and are distinguished ONLY by the "
     "integer level (Y6 = -4 vs +2). Tr Y = Tr Y^3 = 0 over 2I's irreps does not by itself fix the content "
     "(31/51). This is the fork's open premise K2. The correspondence to the SM hypercharges is filed here",
     ["HC.4", "51.GP.4", "56.MC.6"],
     "the honest boundary. What is EARNED cold: the SM gauge group is (SU(3)xSU(2)xU(1))/Z6 (HC.2), the "
     "fractional hypercharge grading Y = -(t/3+w/2) is forced (HC.3), and the SM content is anomaly-free "
     "under it (HC.4). What is a READING (filed through 19, quarantined): that the fermions ARE exactly the "
     "SM multiplet content with these absolute levels -- i.e. selecting which carrier irreps are the "
     "fermions (the representation assignment, the fork's K2, and our 56.MC.6 census hypercharges). The "
     "fractional part is forced; the absolute levels ride on the content selection, which is NOT yet "
     "derived. So the correspondence 'native grading <-> SM hypercharges' is POSTULATE; the absolute levels "
     "are conditional. No downstream premise rests on this reading.",
     "POSTULATE (absolute levels conditional on content K2; the fractional part forced, HC.3)", "POSTULATE",
     {"forced": "the fractional grading (HC.3) + the Z6 group (HC.2) + anomaly-freedom (HC.4)",
      "conditional": "the integer levels 6n -- need the multiplet content selection (K2 / 56.MC.6)",
      "example": "u_c and d_c share (t,w)=(2,0); distinguished only by the absolute level",
      "downstream_premise_use": False},
     check=None)

# ---- HC.6 OWED: the content K2, and the bearing on 57 (sin^2 theta_W) -------------------
step("HC.6", "OWED: the content selection K2 (representation assignment); and 57's theta_W -- the fork's 1/phi^3 is a FENCED candidate (OBSERVATION, 2.1% off), NOT banked",
     "OWED: (a) the multiplet CONTENT selection (K2) -- which carrier irreps are the fermions, the "
     "representation assignment that would fix the absolute levels and the generations (56.MC.6); (b) the "
     "bearing on container 57 (the Weinberg angle): the fork's candidate sin^2(theta_W) = 1/phi^3 ~ 0.2361 "
     "is a FENCED near-miss -- the fork itself grades it CONSISTENCY / OBSERVATION (inversion-then-match, "
     "NOT a derivation; the representation behind it UNFORCED), 2.1% off the measured 0.23122 (MS-bar) and "
     "more off on-shell. It is NOT banked (rule 17: resemblance != result; the refused-list discipline). So "
     "57's cold theta_W value remains OWED -- now located precisely at K2 (the representation assignment), "
     "with 1/phi^3 carried only as the frontier's stated target",
     ["HC.5", "56.MC.6"],
     "the honest residual, and the disciplined handling of the fork's near-miss. This container banks the "
     "FORCED structure -- the Z6 gauge group and the fractional grading. It does NOT bank: (a) the content "
     "selection K2 (owed); (b) the fork's sin^2(theta_W) = 1/phi^3. On (b): the collaborator found the "
     "native closed form 1/phi^3 = 0.2360679... and matched it to the measured weak-mixing angle by "
     "inversion (2.1% off MS-bar), grading it CONSISTENCY / OBSERVATION and explicitly NOT upgrading it -- "
     "the representation assignment that would FORCE the identification is open. Under our discipline this is "
     "a fenced candidate, not a result: noticing the coincidence and stating the discrepancy is allowed; "
     "banking it is not (the refused-list ethos -- 1/144 at 4.84% off 137 was refused; 1/phi^3 at 2.1% with "
     "the rep unforced is a near-miss, reported as such). So container 57's crossing B stands: theta_W "
     "reduces to a normalization the abelian algebra cannot supply, the naive U(2) shortcut is refuted, and "
     "the true value is owed to K2 -- with 1/phi^3 the fork's fenced target, not banked.",
     "OWED (content selection K2; 1/phi^3 fenced not banked -- 57's theta_W owed to the representation assignment)", "OWED",
     {"owed_content": "K2 -- the multiplet content / representation assignment (56.MC.6)",
      "fork_theta_w_candidate": "sin^2(theta_W) = 1/phi^3 ~ 0.2360679 -- FENCED (OBSERVATION, inversion-match, rep unforced, 2.1% off 0.23122); NOT banked",
      "bearing_on_57": "57's cold theta_W remains owed, now located at K2; 1/phi^3 carried as target only",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="58-hypercharge-grading",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        triality_order=Z3, duality_order=Z2, residues=RESIDUES, z6_bijection=z6_bijection,
        sm_pieces=SM_PIECES, Y6_sm=Y6_SM, residues_sm=RESID_SM, mult_sm=MULT_SM,
        anomaly1=anomaly1, anomaly3=anomaly3,
        anom1_pos=anom1_pos, anom1_neg=anom1_neg, anom3_pos=anom3_pos, anom3_neg=anom3_neg,
        finding="the NATIVE HYPERCHARGE GRADING (rederiving the fork's R27/F14 at our standard): the SM "
                "gauge group (SU(3)xSU(2)xU(1))/Z6 and the FRACTIONAL hypercharge Y = -(t/3+w/2) are FORCED "
                "from two native gradings -- colour triality Z/3 (31) x duality Z/2 (45) = Z/6 (= the colour "
                "element's centralizer <g3,-1>, 31.CS.2); Y6 = -(2t+3w) bijects to Z/6 (HC.2). The SM pieces "
                "(Q,L,u_c,d_c,e_c) carry forced residues {1,3,2,2,0} (HC.3), and the SM content is "
                "anomaly-free (sum m*Y6 = 0, sum m*Y6^3 = 0; HC.4, Lean). The mass-founded Gell-Mann-Nishijima "
                "Q=T3+Y is abandoned. OWED: the ABSOLUTE levels (K2 -- the multiplet content selection, HC.5 "
                "POSTULATE) and 57's theta_W value; the fork's sin^2(theta_W) = 1/phi^3 ~ 0.2361 is a FENCED "
                "candidate (OBSERVATION, inversion-match, 2.1% off), NOT banked (HC.6). Upgrades 51's held "
                "joint; the structure 57 was owed. Nothing fitted.",
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
