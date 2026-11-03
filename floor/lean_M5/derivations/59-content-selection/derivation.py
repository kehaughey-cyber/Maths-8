#!/usr/bin/env python3
"""Container 59 -- CONTENT SELECTION (K2): is the fermion multiplet content FORCED? Attacked head-on.

The unblock container 57/58 pointed at: the absolute hypercharge levels (58.HC.5) and the fork's mass
numbers ride on WHICH carrier irreps are the fermions -- the fork's open premise K2. Attacked with the five
gates, TARGET OUT OF VIEW (the SM 15-plet, the hypercharge values, and every mass number are kept out of
sight while forcing; they enter only as the cited comparison, sealed). Rederives the fork's R25/R26
structure cold, then asks the honest question and reports where it lands.

THE HONEST LANDING: the substrate FORCES the irrep structure, the gradings, the matter lattice, and the
mass-law spectrum -- but the CONTENT SELECTION (which irreps are the SM fermions, with matching quantum
numbers and count) is NOT forced. A concrete DISCRIMINATING obstruction: the substrate's natural content
sizes are 12 / 14 / 16; the SM chiral generation is 15. So K2 is under-determined, and the fork's mass
numbers (and the nucleon masses) rest on an un-forced, COMPARISON-grade content map. Nothing fitted.

  KS.1  the forced irrep structure: 2I has 9 irreps (dims 1,2,2',3,3',4,4',5,6; sum dim^2 = 120). The
        central character chi(-1)/dim (the duality w, 45/58) splits them into the A5/vector side
        {1,3,3',4,5} (w=0, factors through PSL(2,5)=A5) and the spinor/faithful side {2,2',4',6} (w=1),
        each sum dim^2 = 60 = |A5|. DERIVED (Lean: 120, 60/60).
  KS.2  the natural matter lattice: matter = codim-3 vertex defect (R25); the 2I-conjugation rep on the 12
        icosahedron neighbours decomposes as 1(+)3(+)3'(+)5 (dims 12) -- recomputed cold from A5's
        12-vertex permutation rep (perm character [12,0,0,2,2] over A5's classes). Colour triplet = (3,3'),
        1 and 5 colourless. So the substrate's OWN matter content is a 12-state lattice. DERIVED.
  KS.3  the K2 gap (a SCOPED negative): the SM chiral generation is 15 Weyl states (Q6+u_c3+d_c3+L2+e_c1;
        16 with nu_R). The substrate's natural content SIZES are 12 (matter lattice), 14 (spinor set
        {2,2',4',6}), 16 (vector set {1,3,3',4,5}). NONE equals 15. So the map 'substrate irreps -> SM
        fermion multiplets (with colour/isospin/hypercharge)' is NOT forced -- it is the fork's COMPARISON.
        The 16-with-nu_R coincidence is a NOTICING (allowed), not a forcing, and does not respect the SM's
        SU(3)xSU(2) multiplet structure (an A5 irrep is not an SU(3)xSU(2) multiplet). DERIVED (the counts;
        the scoped negative). SCOPE: tested the counts + the natural sets; REOPENS if a derivation selects
        irreps WITH matching quantum numbers AND count, target out of view.
  KS.4  the consequence (POSTULATE, filed 19): the absolute hypercharge levels (58.HC.5) and the fork's
        mass numbers rest on this un-forced content map. The mass-law spectrum {12,4,4,0} = 12/d over
        {1,3,3',5} is forced GROUP THEORY given the lattice + the mass-law definition -- but its
        IDENTIFICATION with physical masses (and the nucleon masses built on it) inherits the K2 gap. So
        those numbers are COMPARISON, not forced. POSTULATE.
  KS.5  OWED: what would FORCE K2 -- a derivation selecting the irreps WITH their SU(3)xSU(2)xU(1) quantum
        numbers and the correct count, target out of view, respecting 58's fractional grading; the
        generation count (three) stays NOT fished (56.MC.6). The 16=16 noticing is allowed; banking it is
        refused (G3/G5). OWED.

THE HEADLINE: K2 is NOT forced -- the substrate's natural matter content (12/14/16) does not match the SM's
15, so which irreps are the fermions is under-determined (the fork's own COMPARISON grade, confirmed). The
absolute hypercharges (58) and the fork's mass numbers (incl. the nucleon masses) rest on this gap -- they
cannot be forced results while their content foundation is COMPARISON. This answers the standing question:
the fork's mass numbers are NOT forced. Nothing fitted; the count-mismatch is a discriminating negative.
Rests on 45 (central -1), 58 (the w/t gradings), 31 (colour), 09/11 (the twelve), 56 (census). Cites the
fork's R25/R26, the SL(2,5)/A5 irreps, the SM generation content.
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


# ---- KS.1 the forced irrep structure + the central-character split -- DERIVED ----------
DIMS = {"1": 1, "2": 2, "2'": 2, "3": 3, "3'": 3, "4": 4, "4'": 4, "5": 5, "6": 6}
SUM_DIM2 = sum(d * d for d in DIMS.values())                       # 120 = |2I|
A5_SIDE = ["1", "3", "3'", "4", "5"]                              # w=0, factors through PSL(2,5)=A5
SPINOR_SIDE = ["2", "2'", "4'", "6"]                             # w=1, faithful (spinorial)
A5_SUM_DIM2 = sum(DIMS[k] ** 2 for k in A5_SIDE)                  # 60
SPINOR_SUM_DIM2 = sum(DIMS[k] ** 2 for k in SPINOR_SIDE)         # 60
step("KS.1", "the forced irrep structure: 2I has 9 irreps (sum dim^2 = 120); the central character (duality w) splits them A5/vector {1,3,3',4,5} (60) vs spinor {2,2',4',6} (60)",
     "the carrier 2I = SL(2,5) has 9 irreducible representations, dims {1,2,2',3,3',4,4',5,6}, sum dim^2 = "
     "120 = |2I|. The central element -1 acts as chi(-1)/dim = +1 or -1: the +1 (vector) irreps factor "
     "through PSL(2,5) = A5 -- the set {1,3,3',4,5}, sum dim^2 = 60 = |A5|; the -1 (spinor/faithful) irreps "
     "are {2,2',4',6}, sum dim^2 = 60. This central character IS the duality grading w (45's central -1, "
     "58's w in ℤ/2)",
     ["45.SP.2", "58.HC.1", "06.1"],
     "the group-theory floor, forced and target-free. 2I = SL(2,5) is fixed by container 06; its 9 irreps "
     "and their dims are standard (the McKay E8 nodes). The central character chi(-1)/dim in {+1,-1} is the "
     "duality w already used in 58 (from 45's central -1): the w=0 irreps are exactly those factoring "
     "through the A5 = PSL(2,5) quotient (kernel {+-1}), and the w=1 irreps are the genuinely 2-valued "
     "(spinorial) ones. The two sides each carry sum dim^2 = 60 = |A5|. All of this is forced with no "
     "physics target in view.",
     "UNIQUE (9 irreps, sum dim^2=120; w-split A5 {1,3,3',4,5} / spinor {2,2',4',6}, each 60)", "DERIVED",
     {"dims": DIMS, "sum_dim2": SUM_DIM2, "a5_side": A5_SIDE, "spinor_side": SPINOR_SIDE,
      "a5_sum_dim2": A5_SUM_DIM2, "spinor_sum_dim2": SPINOR_SUM_DIM2},
     check="2I: 9 irreps, sum dim^2=120; central-character split A5 {1,3,3',4,5}=60 / spinor {2,2',4',6}=60")
assert SUM_DIM2 == 120 and A5_SUM_DIM2 == 60 and SPINOR_SUM_DIM2 == 60

# ---- KS.2 the natural matter lattice = the 12-vertex A5 perm rep -- DERIVED -------------
# recompute the decomposition of the 12-icosahedron-vertex A5 permutation rep, cold.
def a5_12vertex_decomposition():
    from itertools import permutations
    def sgn(p):
        s = 1
        for i in range(5):
            for j in range(i + 1, 5):
                if p[i] > p[j]:
                    s = -s
        return s
    A5 = [p for p in permutations(range(5)) if sgn(p) == 1]
    idn = tuple(range(5))
    comp = lambda a, b: tuple(a[b[i]] for i in range(5))
    def order(p):
        x, n = p, 1
        while x != idn:
            x = comp(p, x); n += 1
        return n
    c5 = next(p for p in A5 if order(p) == 5)
    C5 = set(); x = idn
    for _ in range(5):
        C5.add(x); x = comp(c5, x)
    cosets, keys = [], []
    for p in A5:
        k = frozenset(comp(h, p) for h in C5)
        if k not in keys:
            keys.append(k); cosets.append(p)
    pt = lambda p: keys.index(frozenset(comp(h, p) for h in C5))
    # class reps in standard order: e, ord2, ord3, ord5a, ord5b
    reps = {}
    for p in A5:
        reps.setdefault((order(p), None), p)
    e = idn
    o2 = next(p for p in A5 if order(p) == 2)
    o3 = next(p for p in A5 if order(p) == 3)
    fives = [p for p in A5 if order(p) == 5]
    # split the 24 order-5 into two classes by conjugacy
    def conj(g, p):
        gi = tuple(sorted(range(5), key=lambda i: g[i]))
        return comp(g, comp(p, gi))
    cl5a = set(conj(g, fives[0]) for g in A5)
    o5a = fives[0]
    o5b = next(p for p in fives if p not in cl5a)
    def permfix(g):
        return sum(1 for i, p in enumerate(cosets) if pt(comp(p, g)) == i)
    perm = [permfix(e), permfix(o2), permfix(o3), permfix(o5a), permfix(o5b)]
    sizes = [1, 15, 20, 12, 12]
    phi = (1 + 5 ** 0.5) / 2
    chars = {"1": [1, 1, 1, 1, 1], "3": [3, -1, 0, phi, 1 - phi],
             "3'": [3, -1, 0, 1 - phi, phi], "4": [4, 0, 1, -1, -1], "5": [5, 1, -1, 0, 0]}
    mult = {n: round(sum(s * a * b for s, a, b in zip(sizes, perm, ch)) / 60) for n, ch in chars.items()}
    return perm, mult

PERM_CHAR, MATTER_MULT = a5_12vertex_decomposition()
MATTER_LATTICE = [k for k in ["1", "3", "3'", "4", "5"] if MATTER_MULT[k] == 1]
MATTER_DIM = sum(DIMS[k] for k in MATTER_LATTICE)                 # 12
step("KS.2", "the natural matter lattice: the 2I-conjugation rep on the 12 icosahedron neighbours = 1(+)3(+)3'(+)5 (dims 12) -- recomputed cold; colour triplet=(3,3'), 1/5 colourless",
     "matter = the codim-3 vertex defect (R25); the carrier acts by conjugation on the 12 icosahedron "
     "neighbours (the twelve, 09/11), and that 12-dim permutation representation decomposes as "
     "1 (+) 3 (+) 3' (+) 5 (each once; dims 1+3+3+5 = 12). Recomputed cold here from A5's 12-vertex perm "
     "rep (permutation character [12,0,0,2,2] over A5's classes -> multiplicities all 1). The colour "
     "triplet is the pair (3,3') (31); 1 and 5 are colourless. So the substrate's OWN matter content is a "
     "12-STATE lattice",
     ["KS.1", "31.CS.1", "09.6.4"],
     "the fork's R25, rederived cold. The 12 neighbours (the kissing twelve, 09/11) carry the "
     "A5-conjugation permutation representation; decomposing it against the A5 character table gives "
     "multiplicities 1,3,3',5 (each unit) and 0 for the 4 -- recomputed here from scratch (build A5, the "
     "C5-coset 12-point action, the perm character [12,0,0,2,2], the inner products). This is the "
     "substrate's native matter lattice {1,3,3',5}, dims summing to 12. The (3,3') pair is the colour "
     "triplet + its Galois partner (31); 1 and 5 are colour singlets. Target-free: no SM multiplet is "
     "invoked here -- this is pure carrier geometry.",
     "UNIQUE (12-vertex conjugation rep = 1+3+3'+5, dims 12; colour triplet (3,3'))", "DERIVED",
     {"perm_character": PERM_CHAR, "multiplicities": MATTER_MULT,
      "matter_lattice": MATTER_LATTICE, "matter_dim": MATTER_DIM},
     check="the 12-neighbour conjugation rep decomposes as 1+3+3'+5 (dims 12); recomputed cold")
assert MATTER_LATTICE == ["1", "3", "3'", "5"] and MATTER_DIM == 12

# ---- KS.3 the K2 gap: none of the natural content sizes is 15 -- DERIVED (scoped neg) ---
SPINOR_DIM = sum(DIMS[k] for k in SPINOR_SIDE)                    # 14
VECTOR_DIM = sum(DIMS[k] for k in A5_SIDE)                        # 16
SM_GEN = {"Q": 6, "u_c": 3, "d_c": 3, "L": 2, "e_c": 1}
SM_STATES = sum(SM_GEN.values())                                 # 15 (16 with nu_R)
SM_WITH_NUR = SM_STATES + 1                                      # 16
mismatches = {"matter_12": MATTER_DIM != SM_STATES,
              "spinor_14": SPINOR_DIM != SM_STATES,
              "vector_16": VECTOR_DIM != SM_STATES}
none_is_15 = all(mismatches.values())
step("KS.3", "the K2 gap (SCOPED negative): the SM generation is 15 (16 w/ nu_R); the substrate's natural sizes are 12/14/16 -- NONE is 15, so the content map is NOT forced (the fork's COMPARISON)",
     "the SM chiral generation is 15 Weyl states (Q:6 + u_c:3 + d_c:3 + L:2 + e_c:1; 16 with a "
     "right-handed neutrino). The substrate's natural content SIZES are: matter lattice 12 (KS.2), spinor "
     "set {2,2',4',6} = 14, vector set {1,3,3',4,5} = 16. NONE equals 15. So the map 'substrate irreps -> "
     "SM fermion multiplets' is NOT forced by the counting -- it is under-determined (the fork's COMPARISON "
     "grade, confirmed). The 16-with-nu_R coincidence is a NOTICING, not a forcing, and it does not respect "
     "the SM's SU(3)xSU(2) multiplet structure (an A5 irrep is not an SU(3)xSU(2) multiplet)",
     ["KS.2", "56.MC.6"],
     "the honest answer to K2, and a SCOPED negative (CORRECTIONS #7). WHAT WAS TESTED: the substrate's "
     "natural content sizes (12 the matter lattice, 14 the spinor/fermion set, 16 the vector set) against "
     "the SM generation count 15 (16 with nu_R). RESULT: none matches 15 -- the content selection is not "
     "fixed by the substrate's counts. The vector set = 16 = a generation WITH nu_R is a real NOTICING and "
     "is recorded as such (leads are admissible), but it is NOT banked: (a) it needs nu_R, a choice; (b) an "
     "A5 irrep carries no SU(3)xSU(2) quantum numbers, so equating {1,3,3',4,5} with (Q,u_c,d_c,L,e_c,nu_R) "
     "would be renaming (G3) -- the dims coincide but the structure does not. So K2 is genuinely "
     "under-determined. SCOPE NOT COVERED: a derivation that selects the irreps together WITH their "
     "colour/isospin/hypercharge quantum numbers and the right count. REOPENS: on any such derivation "
     "(target out of view). This is a discriminating negative -- the substrate's matter content does not, "
     "by counting, deliver the SM generation.",
     "UNIQUE (SM 15 vs natural 12/14/16 -- none matches; content selection NOT forced, scoped)", "DERIVED",
     {"sm_generation": SM_GEN, "sm_states": SM_STATES, "sm_with_nu_r": SM_WITH_NUR,
      "matter_dim": MATTER_DIM, "spinor_dim": SPINOR_DIM, "vector_dim": VECTOR_DIM,
      "mismatches": mismatches, "none_is_15": none_is_15,
      "noticing_not_banked": "vector set 16 = generation with nu_R -- a NOTICING (leads allowed), NOT banked (needs nu_R; A5 irreps carry no SU(3)xSU(2) numbers -> renaming, G3)"},
     check="SM generation 15 (16 w/ nu_R); natural sizes 12/14/16, none = 15 -> content NOT forced (scoped)")
assert none_is_15 and SPINOR_DIM == 14 and VECTOR_DIM == 16 and SM_STATES == 15

# ---- KS.4 the consequence: the mass numbers rest on the un-forced map -- POSTULATE ------
MASS_SPECTRUM = [12 // d if 12 % d == 0 else 0 for d in (1, 3, 3, 5)]   # {12,4,4,0} over {1,3,3',5}
step("KS.4", "the consequence (POSTULATE, filed 19): the absolute hypercharges (58.HC.5) and the fork's mass numbers REST on this un-forced content map -- forced group theory, COMPARISON identification",
     "the absolute hypercharge levels (58.HC.5) and the fork's mass numbers ride on the content selection "
     "(KS.3). The matter-lattice mass spectrum {12,4,4,0} = 12/d over {1,3,3',5} (mass_5 = 0 since 5 does "
     "not divide 12) is forced GROUP THEORY given the lattice (KS.2) + the mass-law definition -- but its "
     "IDENTIFICATION with physical masses, and the nucleon masses built on it, INHERIT the K2 gap (KS.3). "
     "So those numbers are COMPARISON, not forced results",
     ["KS.3", "58.HC.5", "56.MC.6"],
     "the honest consequence, graded POSTULATE. What is EARNED cold: the mass-law SPECTRUM {12,4,4,0} is "
     "forced arithmetic (12/d over the matter lattice, with the 5 vanishing because chi_5 = 0). What is a "
     "READING (filed 19, quarantined): that these ARE the physical masses / that any SM mass ratio follows "
     "-- because that requires the content map (KS.3), which is not forced. Therefore the fork's mass "
     "numbers (the matter-lattice spectrum, and the nucleon masses m_p/m_e etc. that build on it) rest on a "
     "COMPARISON-grade foundation: they cannot be forced results while K2 is open. This is consistent with "
     "the separate assessment of the nucleon chapter (an assembly on an un-forced content map). No "
     "downstream premise rests on this reading.",
     "POSTULATE (mass spectrum {12,4,4,0} forced arithmetic; its physical identification rests on the un-forced K2)", "POSTULATE",
     {"mass_spectrum": MASS_SPECTRUM, "over": ["1", "3", "3'", "5"],
      "forced": "the spectrum 12/d over the matter lattice (arithmetic)",
      "rests_on_K2": "the physical-mass identification + all SM mass ratios (incl. the nucleon masses) need the content map (KS.3), not forced",
      "downstream_premise_use": False},
     check=None)
assert MASS_SPECTRUM == [12, 4, 4, 0]

# ---- KS.5 OWED: what would force K2 -----------------------------------------------------
step("KS.5", "OWED: what would FORCE K2 -- select the irreps WITH their SU(3)xSU(2)xU(1) quantum numbers and the right count, target out of view; generations (3) NOT fished; 16=16 noticing allowed, banking refused",
     "OWED: a derivation that selects which carrier irreps are the fermions TOGETHER WITH their "
     "SU(3)xSU(2)xU(1) quantum numbers and the correct state count (respecting 58's forced fractional "
     "hypercharge), with the SM content out of view -- only that forces K2 and, with it, the absolute "
     "hypercharge levels and the cold sin^2(theta_W) (57). The generation count (three) stays NOT fished "
     "(56.MC.6) -- different 3-folds are not one. The 16-with-nu_R noticing is an admissible lead; banking "
     "it is refused (G3 renaming, G5 no-fit)",
     ["KS.3", "KS.4"],
     "the honest residual, and the discipline. K2 is the load-bearing owed premise beneath the matter "
     "sector: the cold sin^2(theta_W) (57), the absolute hypercharges (58), and any SM mass ratio all wait "
     "on it. Forcing it requires selecting the fermion irreps WITH matching colour/isospin/hypercharge "
     "quantum numbers AND the right count -- not by matching a dimension total (the 12/14/16 vs 15 "
     "mismatch shows counting alone under-determines it), and not by fishing (the 16=16-with-nu_R "
     "coincidence is noticed, not banked; the generation 3 is not fished). Until such a derivation exists, "
     "K2 is genuinely open and the fork's mass numbers stay COMPARISON. This is the truthful state: the "
     "substrate forces the matter STRUCTURE (irreps, gradings, lattice, spectrum) but not the SM CONTENT "
     "MAP.",
     "OWED (force the irreps+quantum-numbers+count with target out of view; generations not fished)", "OWED",
     {"owed": "select fermion irreps WITH SU(3)xSU(2)xU(1) quantum numbers + correct count, target out of view",
      "unblocks": "the cold sin^2(theta_W) (57), the absolute hypercharges (58), SM mass ratios",
      "not_fished": "the generation count (three); the 16=16-with-nu_R coincidence (noticing only)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="59-content-selection",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        dims=DIMS, sum_dim2=SUM_DIM2, a5_side=A5_SIDE, spinor_side=SPINOR_SIDE,
        a5_sum_dim2=A5_SUM_DIM2, spinor_sum_dim2=SPINOR_SUM_DIM2,
        perm_character=PERM_CHAR, matter_multiplicities=MATTER_MULT,
        matter_lattice=MATTER_LATTICE, matter_dim=MATTER_DIM,
        spinor_dim=SPINOR_DIM, vector_dim=VECTOR_DIM,
        sm_states=SM_STATES, sm_with_nu_r=SM_WITH_NUR, none_is_15=none_is_15,
        mass_spectrum=MASS_SPECTRUM,
        finding="CONTENT SELECTION (K2), attacked head-on with the target out of view: the substrate FORCES "
                "the matter STRUCTURE but NOT the SM content map. Forced: 2I's 9 irreps (sum dim^2=120), the "
                "central-character split A5 {1,3,3',4,5} / spinor {2,2',4',6} (each 60, KS.1); the matter "
                "lattice = the 12-vertex conjugation rep 1+3+3'+5 (dims 12, recomputed cold, KS.2); the "
                "mass-law spectrum {12,4,4,0}=12/d over {1,3,3',5} (KS.4). NOT forced (KS.3, scoped "
                "negative): the SM generation is 15 (16 w/ nu_R), but the natural content sizes are 12/14/16 "
                "-- NONE is 15, so which irreps are the fermions (with SU(3)xSU(2)xU(1) quantum numbers) is "
                "under-determined -- the fork's own COMPARISON. The 16=16-with-nu_R coincidence is a "
                "noticing, NOT banked (an A5 irrep carries no SU(3)xSU(2) numbers -> renaming). CONSEQUENCE "
                "(KS.4): the absolute hypercharges (58) and the fork's mass numbers (incl. the nucleon "
                "masses) rest on this un-forced map -- they are NOT forced results while K2 is open. This "
                "answers the standing question: the fork's mass numbers are not forced. OWED (KS.5): force "
                "the irreps+quantum-numbers+count, target out of view; generations not fished. Nothing "
                "fitted; the 12/14/16 vs 15 mismatch is a discriminating negative.",
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
