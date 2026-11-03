#!/usr/bin/env python3
"""Container 31 -- COLOR AS THREE SEATINGS: the native Z/3 of the strong force.
Rests on 06 (the carrier 2I) and 30 (su(3)=A2, the triality det=3); cites 00 (the three-observer 3-fold).
Filed through the 19 gate. The cold Z/3 color-seating check (2026-08-29, Maths 6.5).

CONTEXT (Kevin): container 30 located su(3) as A2 subset E8 -- but that embedding is a CHOICE (LESS
NATIVE). Going to the clues (PrimeFramework_BeltComplete_QuarkSeating.docx -- DANGER-ZONE material, the
'quark seating' that caused the restart; mined as a LEAD ONLY, criterion not literals), the framework
locates COLOUR NATIVELY: as THREE SEATINGS under conjugation by an order-3 element g3 of 2I (colour =
which of the three seatings you sit in; C(g3) cycles P0->P1->P2). This container RE-DERIVES that COLD on
the 120 vertices of 2I -- the Z/3, not the belt's quark census (which stays danger-zone, not imported).

  CS.1 an order-3 element of 2I forces a Z/3 COLOUR SEATING. g3=(-1/2,1/2,1/2,1/2) has order 3;
       conjugation by it has order EXACTLY 3 (perm^3=id), partitioning 2I into fixed points (the
       centralizer) + 3-cycles -- 6 + 38 exactly. Every non-centralizing element sits in a 3-cycle = three
       colour positions cyclically permuted. The three colours = the order of g3 = 3, FORCED. DERIVED.
  CS.2 the THREE is the substrate's NATIVE 3-fold; the centralizer is the colourless part. Z/3 = order of
       g3 = 3 = native (2I's order-3 elements = 3-fold face rotations; the triality det(A2 Cartan)=3, 30;
       the three-observer floor, 00). The 6 fixed = C(g3) = <g3,-1> = Z/6 (|class|=20). DERIVED.
  CS.3 THE FILED ENTRY (through 19): the three g3-seatings <-> QCD's 3 colours (SU(3) fundamental + center
       Z/3); the colourless centralizer <-> colour-singlets (confinement flavour). REFINES 30: the
       colour-3/Z/3 is NATIVE now (order-3 element of 2I), improving on 30's chosen A2 subset E8. WEAK. POSTULATE.
  CS.4 the full su(3) ADJOINT (8 gluons) natively; the quark seating / mass map (DANGER ZONE, a lead to
       re-derive cold if pursued, NOT imported); alpha_s. Located. OWED.

HONEST on the 1+3+8=12 question: this shows colour=3 is NATIVE (correcting the earlier over-quick
'coincidence' dismissal -- colour IS 3-fold in the substrate). It does NOT resurrect 1+3+8=12: the three
seatings give the CENTER / fundamental-3, NOT the 8-generator adjoint or a 12-sum. So the native reach is
the Z/3 and the 3 colours; the 8 stays the less-native E8 side (30) and owed.

Grades per step. `--check` recomputes the DERIVED steps (the exact Z[phi] cycle structure).
"""

import json
import sys
import itertools
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ 2I in exact Z[phi] (component=(a+b*phi)/2)
def cmul_num(A, B):
    """(a+b*phi)(c+d*phi) = (ac+bd)+(ad+bc+bd)*phi   [phi^2=phi+1]; returns the /4 numerator of a /2 x /2 product."""
    a, b = A
    c, d = B
    return (a * c + b * d, a * d + b * c + b * d)


def qmul(A, B):
    aw, ax, ay, az = A
    bw, bx, by, bz = B

    def s(*terms):
        P = Q = 0
        for sign, X, Y in terms:
            p, q = cmul_num(X, Y)
            P += sign * p
            Q += sign * q
        assert P % 2 == 0 and Q % 2 == 0
        return (P // 2, Q // 2)
    return (s((1, aw, bw), (-1, ax, bx), (-1, ay, by), (-1, az, bz)),
            s((1, aw, bx), (1, ax, bw), (1, ay, bz), (-1, az, by)),
            s((1, aw, by), (-1, ax, bz), (1, ay, bw), (1, az, bx)),
            s((1, aw, bz), (1, ax, by), (-1, ay, bx), (1, az, bw)))


def neg(c):
    return (-c[0], -c[1])


def qconj(A):
    return (A[0], neg(A[1]), neg(A[2]), neg(A[3]))


Z, HALF, ONE, PHI2, INV2 = (0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)   # 0, 1/2, 1, phi/2, 1/(2phi)
NHALF, NONE = neg(HALF), neg(ONE)


def build_2I():
    els = set()
    for i in range(4):
        for s_ in (ONE, NONE):
            v = [Z, Z, Z, Z]
            v[i] = s_
            els.add(tuple(v))
    for signs in itertools.product((HALF, NHALF), repeat=4):
        els.add(tuple(signs))
    base = [Z, HALF, PHI2, INV2]
    for p in itertools.permutations(range(4)):
        if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2:
            continue                                        # even permutations only
        for sgn in itertools.product((1, -1), repeat=3):
            vals = [base[0], base[1] if sgn[0] > 0 else neg(base[1]),
                    base[2] if sgn[1] > 0 else neg(base[2]), base[3] if sgn[2] > 0 else neg(base[3])]
            v = [Z, Z, Z, Z]
            for slot, pos in enumerate(p):
                v[pos] = vals[slot]
            els.add(tuple(v))
    return list(els)


ELS = build_2I()
IDENT = (ONE, Z, Z, Z)
IDX = {e: i for i, e in enumerate(ELS)}
ORDER_2I = len(ELS)

# order-3 element and its conjugation cycle structure
G3 = (NHALF, HALF, HALF, HALF)
def elem_order(q):
    p = q
    o = 1
    while p != IDENT:
        p = qmul(p, q)
        o += 1
        if o > 30:
            return -1
    return o
G3_ORDER = elem_order(G3)
G3I = qconj(G3)
PERM = [IDX[qmul(qmul(G3, ELS[i]), G3I)] for i in range(ORDER_2I)]
# cycle structure
seen = [False] * ORDER_2I
CYC = {}
for i in range(ORDER_2I):
    if seen[i]:
        continue
    L = 0
    j = i
    while not seen[j]:
        seen[j] = True
        j = PERM[j]
        L += 1
    CYC[L] = CYC.get(L, 0) + 1
PERM3_IS_ID = all(PERM[PERM[PERM[i]]] == i for i in range(ORDER_2I))
N_FIXED = CYC.get(1, 0)
N_TRIPLES = CYC.get(3, 0)
CLASS_SIZE = ORDER_2I // N_FIXED           # |class(g3)| = |2I| / |centralizer|

# the KERNEL witness: g3 doubled = integer quaternion (-1,1,1,1); its cube = (8,0,0,0) => unit order 3
def iqmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw * bw - ax * bx - ay * by - az * bz, aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx, aw * bz + ax * by - ay * bx + az * bw)
GI = (-1, 1, 1, 1)
CUBE = iqmul(iqmul(GI, GI), GI)            # = (8,0,0,0)

# ---- CS.1 an order-3 element forces a Z/3 colour seating -- DERIVED ---------------------
cs1_ok = (ORDER_2I == 120 and G3_ORDER == 3 and PERM3_IS_ID
          and sorted(CYC.items()) == [(1, 6), (3, 38)] and CUBE == (8, 0, 0, 0))
step("CS.1", "an order-3 element of 2I forces a Z/3 COLOUR SEATING (6 fixed + 38 three-cycles, cold)",
     "g3=(-1/2,1/2,1/2,1/2) in 2I (06) has order 3; conjugation by it has order EXACTLY 3 (perm^3=id), "
     "partitioning the 120 into fixed points + 3-cycles -- 6 + 38 exactly; every non-centralizing element "
     "sits in a 3-cycle = three colour positions cyclically permuted P0->P1->P2->P0 (the Z/3). The three "
     "colours = the order of g3 = 3, forced",
     ["06.2"],
     "the cold re-derivation of the framework's 'colour = three seatings' criterion (mined from the "
     "danger-zone belt/quark clue as a LEAD, derived here from scratch -- no census imported). Built cold "
     "on the 120 vertices of 2I (container 06's carrier), exact in Z[phi]: pick an order-3 element "
     "g3=(-1/2,1/2,1/2,1/2) (one of the 16 Hurwitz-type units; verified order 3). Conjugation c(x)=g3.x.g3^-1 "
     "is an inner automorphism, and since g3^3=1 it has order dividing 3; it is exactly 3 (perm^3=identity, "
     "checked). So its cycles have length 1 or 3: the length-1 cycles are the FIXED points (elements "
     "commuting with g3, the centralizer) and the length-3 cycles are COLOUR TRIPLES -- each an object in "
     "three colour seatings, cyclically permuted, the exact Z/3 the framework calls colour. Exhaustive on "
     "the 120: 6 fixed + 38 three-cycles (6 + 3*38 = 120). The 'three colours' is not chosen -- it is the "
     "ORDER of g3 (=3), so any order-3 element gives a three-fold seating. CERTIFICATION SPLIT: the "
     "kernel proves g3 has order 3 via the INTEGER quaternion (-1,1,1,1) (=2*g3, no phi) whose cube is "
     "exactly (8,0,0,0) = 8*identity, so the unit g3 cubes to 1 -- zero-axiom, integer; the full "
     "120-element cycle structure (6+38) is EXACT-INTEGER in Z[phi] (verify-guarded, this derivation "
     "recomputes it), as container 06/13's larger computations are.",
     "UNIQUE (an order-3 element's conjugation has order 3; cycles 1 or 3; 6 fixed + 38 triples on the 120)",
     "DERIVED",
     {"order_2I": ORDER_2I, "g3": [list(c) for c in G3], "g3_order": G3_ORDER,
      "conjugation_perm3_is_identity": PERM3_IS_ID,
      "cycle_structure": {str(k): v for k, v in sorted(CYC.items())},
      "n_fixed": N_FIXED, "n_three_cycles": N_TRIPLES,
      "kernel_cube_of_doubled_g3": list(CUBE),
      "three_colours_is_forced": "the seating count = the order of g3 = 3; any order-3 element gives Z/3",
      "colour_triples": "the 38 three-cycles = objects in three colour seatings, cyclically permuted P0->P1->P2"},
     check="g3 order 3 (kernel: (-1,1,1,1)^3=(8,0,0,0)); conjugation perm^3=id; 6 fixed + 38 three-cycles on the 120")
assert cs1_ok

# ---- CS.2 the three is the native 3-fold; the centralizer is colourless -- DERIVED -----
CENTRALIZER = N_FIXED                                    # = 6 = |<g3,-1>| = Z/6
cs2_ok = (CENTRALIZER == 6 and CLASS_SIZE == 20 and CENTRALIZER * CLASS_SIZE == ORDER_2I)
step("CS.2", "the THREE is the substrate's NATIVE 3-fold; the centralizer (6) is the colourless part",
     "the Z/3 = order of g3 = 3 = the substrate's native 3-fold (2I's order-3 elements are 3-fold "
     "rotations; the triality det(A2 Cartan)=3 of container 30; the three-observer floor 00). The 6 fixed "
     "points = the centralizer C(g3) = <g3,-1> = Z/6, |class(g3)|=20, 6*20=120 -- the colourless "
     "(commuting) part",
     ["CS.1", "30.S.2"],
     "the meaning of the three, and where it is native. The seating count is 3 because g3 has order 3 -- "
     "and 'three' is the substrate's OWN number, not an import: (a) 2I's order-3 elements are exactly the "
     "3-fold face rotations of the icosahedron (through the 20 triangular faces); (b) container 30's "
     "triality is det(A2 Cartan)=3=|Z(SU(3))|, the same three; (c) the floor is TRIADIC -- a distinction "
     "takes three observers (container 00, two within one without). So colour's three-ness reduces to the "
     "substrate's native 3-fold, not to a chosen structure. The FIXED points -- the 6 elements commuting "
     "with g3 -- are the centralizer C(g3): it is <g3, -1> (the order-3 g3 together with the center -1), "
     "of order 6 = Z/6, and its conjugacy class has size |2I|/|C| = 120/6 = 20 (one of 2I's two size-20 "
     "classes). These 6 are the 'colourless' seats -- invariant under the colour-cycling g3 -- the "
     "singlet-flavoured part (confinement resonance, made precise only in the correspondence CS.3). "
     "EXACT-INTEGER (verify-guarded); the count 6*20=120 is the orbit-counting check.",
     "UNIQUE (centralizer order 6 = Z/6, class size 20, 6*20=120; three = the native 3-fold)", "DERIVED",
     {"centralizer_order": CENTRALIZER, "class_size": CLASS_SIZE,
      "centralizer_times_class": CENTRALIZER * CLASS_SIZE, "structure": "C(g3) = <g3,-1> = Z/6",
      "three_is_native": "2I's order-3 = 3-fold face rotations; triality det=3 (30); the triadic floor (00)",
      "colourless_part": "the 6 fixed = the centralizer = the singlet-flavoured (commuting) seats"},
     check="centralizer C(g3)=Z/6 order 6, class size 20, 6*20=120; the three = the substrate's native 3-fold")
assert cs2_ok

# ---- CS.3 the filed entry (through 19): colour <-> three seatings -- POSTULATE ----------
step("CS.3", "THE FILED ENTRY: the three g3-seatings <-> QCD's 3 colours (SU(3) center Z/3 + fundamental)",
     "filed through the 19 gate: the three g3-colour-seatings <-> QCD's 3 colours (the SU(3) fundamental + "
     "center Z/3, CS.1); the colourless centralizer <-> colour-singlets (confinement flavour, CS.2). "
     "REFINES container 30: the colour-3/Z/3 is NATIVE now (an order-3 element of 2I), improving on 30's "
     "CHOSEN A2 subset E8. A correspondence; the full su(3) adjoint / quark census do NOT travel",
     ["CS.1", "CS.2", "06.2"],
     "the entry, the four parts, and the honest refinement of the strong-force location. SUBSTRATE SIDE "
     "(checked): an order-3 element of 2I forces a Z/3 colour seating (CS.1); the three is the native "
     "3-fold, the centralizer the colourless part (CS.2). PHYSICS SIDE (cited): QCD has 3 colours, the "
     "SU(3) center is Z/3 (triality), colour-singlet states are confined. THE CORRESPONDENCE: the three "
     "g3-seatings <-> the 3 colours (SU(3) fundamental) and the Z/3 center; the colourless centralizer "
     "<-> colour-singlets. This REFINES container 30: 30 located su(3) as A2 subset E8 -- but that "
     "embedding is a CHOICE (E8 has many A2's), flagged less-native. HERE the colour-3 and its Z/3 are "
     "NATIVE -- forced by an order-3 element of the carrier itself, tied to the substrate's own 3-fold "
     "(the triadic floor). So the strong force's FUNDAMENTAL (3 colours) and CENTER (Z/3) are now located "
     "natively; the ADJOINT (8 gluons) remains the less-native E8 side (30) and owed. WHAT DOES NOT "
     "TRAVEL: the full su(3) adjoint (three DISCRETE seatings give the center/fundamental, NOT the "
     "continuous 8-generator SU(3)); the belt-trichotomy QUARK SEATING and mass-map "
     "(PrimeFramework_BeltComplete_QuarkSeating -- DANGER ZONE, a lead mined for the Z/3 CRITERION only, "
     "its census NOT imported); the coupling alpha_s. FALSIFICATION SURFACE: an order-3 element must give "
     "exactly a three-fold seating (it does, CS.1) tied to the native 3-fold (CS.2); if colour's three "
     "were not the substrate's own three, this would fail. HONEST on 1+3+8=12: this makes colour=3 NATIVE "
     "(correcting the earlier too-quick 'coincidence' -- colour IS 3-fold here), but does NOT resurrect "
     "1+3+8=12: the seatings give the center/fundamental-3, never an 8 or a 12-sum. A CORRESPONDENCE, WEAK "
     "(consistency, not discrimination); quarantined.",
     "POSTULATE (the filed correspondence colour <-> three g3-seatings; a reading, held, quarantined)",
     "POSTULATE",
     {"substrate_side": "an order-3 element forces a Z/3 colour seating (CS.1); native 3-fold, colourless centralizer (CS.2)",
      "physics_side_cited": "QCD: 3 colours, SU(3) center Z/3 (triality), colour-singlets confined",
      "correspondence": "three g3-seatings <-> 3 colours (SU(3) fundamental + center Z/3); centralizer <-> colour-singlets",
      "refines_30": "the colour-3/Z/3 is NATIVE (order-3 element of 2I), improving on 30's CHOSEN A2 subset E8",
      "what_does_not_travel": "the full su(3) adjoint (8 gluons -- discrete seatings give center/fundamental, not continuous SU(3)); the quark seating / mass map (DANGER ZONE); alpha_s",
      "one_plus_three_plus_eight_note": "colour=3 native corrects the 'coincidence' dismissal; but does NOT resurrect 1+3+8=12 (seatings give center/fundamental-3, not the 8 or a 12-sum)",
      "correspondence_not_resolution": True, "weak_consistency_not_discrimination": True,
      "downstream_premise_use": False},
     check=None)

# ---- CS.4 the full su(3) adjoint + the quark census -- OWED (located) -------------------
step("CS.4", "the full su(3) ADJOINT (8) natively + the quark seating/mass (danger zone) + alpha_s -- OWED",
     "the full su(3) ADJOINT (8 gluons) natively (the three discrete seatings give only the center/"
     "fundamental); the quark seating / mass map (DANGER ZONE, a lead to re-derive cold, NOT imported); "
     "the coupling alpha_s. Located, not closed",
     ["CS.3", "30.S.4"],
     "the residual, located and NOT attempted -- the honest boundary. CS.1-CS.3 locate colour's 3 and Z/3 "
     "NATIVELY (an order-3 element of 2I). What remains: (i) the full su(3) ADJOINT -- the 8 gluons, the "
     "CONTINUOUS SU(3) -- which the three discrete seatings do NOT supply (they give the center Z/3 and "
     "the fundamental 3); the 8 is container 30's A2 subset E8, less native, and a NATIVE 8 (if one "
     "exists) is owed; (ii) the QUARK SEATING and mass-map -- the framework's belt trichotomy (6 dark "
     "baryonic + 6 shared mesonic + 18 = 6 flavours x 3 colours) -- which is the DANGER ZONE (the census "
     "assembly that caused the restart); mined here ONLY for the Z/3 colour CRITERION, its quark/mass "
     "census NOT imported, to be re-derived cold if ever pursued; (iii) the coupling alpha_s (a "
     "dimensionless alpha_hat to FORCE not fit, per 27/29-30). So colour's fundamental/center is native "
     "(CS.1-3); the adjoint, the quark census, and the coupling are the forward work. NOT attempted here.",
     "OWED (native su(3) adjoint; the quark seating/mass census -- danger zone; alpha_s; located)", "OWED",
     {"present": False,
      "owed_native_adjoint": "the 8-generator su(3) natively -- the discrete Z/3 seatings give only center/fundamental; the 8 is 30's less-native A2 subset E8",
      "quark_census_danger_zone": "the belt trichotomy (6 dark + 6 shared + 18 quark) -- census that caused the restart; mined for the Z/3 CRITERION only, NOT imported",
      "coupling": "alpha_s -- a dimensionless alpha_hat to force not fit (27)",
      "located_not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="31-color-seating",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # CS.1 -- kernel guards the order-3 cube; the cycle structure is exact-integer here
        order_2I=ORDER_2I, g3_order=G3_ORDER, perm3_is_identity=PERM3_IS_ID,
        n_fixed=N_FIXED, n_three_cycles=N_TRIPLES, kernel_cube=list(CUBE),
        # CS.2
        centralizer_order=CENTRALIZER, class_size=CLASS_SIZE,
        # the finding
        color_three_is_native=True,
        finding="COLOUR is NATIVELY three seatings: an order-3 element g3 of 2I acts by conjugation with "
                "order exactly 3 (perm^3=id), partitioning the 120 into 6 fixed (the colourless centralizer "
                "Z/6) + 38 three-cycles (colour triples, the Z/3) -- CS.1/CS.2; the correspondence colour "
                "<-> three g3-seatings is filed through 19 (CS.3, POSTULATE, REFINES 30's chosen A2 subset E8 "
                "with a NATIVE colour-3/Z/3); the full su(3) adjoint (8) + quark census (danger zone) + "
                "alpha_s are OWED (CS.4). Corrects the '1+3+8=12 coincidence' dismissal: colour IS native "
                "3-fold -- but this gives the center/fundamental, NOT the 8 or a 12-sum.",
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
