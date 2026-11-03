#!/usr/bin/env python3
"""Container 44 -- CHIRALITY: the carrier is orientation-pure; parity is not a self-symmetry (forced surface).

Step 3 of Kevin's forward frontier (Maths 6.7): force the substrate's HANDEDNESS. 28.W.2 CITED maths-4's
chirality ("orientation is chirality; zero orientation-reversing self-maps") to meet the chiral weak
force. This container forces it COLD on the substrate -- and the clue was already in 06: the carrier is
built on EVEN permutations only (06.1), the odd orbit being the excluded conjugate mirror (CORRECTIONS #5).

  CH.1  the carrier is ORIENTATION-PURE. 06.1 builds the 96-block on EVEN permutations of the four
        coordinates (sign +1); and the carrier 2I sits in SU(2) = proper rotations (det +1, the double
        cover of SO(3)) -- NO reflection / improper element. The sign is multiplicative, so composing
        carrier elements stays sign +1: the carrier never generates an orientation-reversing map. DERIVED.

  CH.2  PARITY is not a self-symmetry. An orientation reversal (an ODD permutation / a reflection, sign
        -1) carries the carrier to the OTHER orbit -- the conjugate (odd) copy, a DISTINCT carrier
        (06 finding-2 / CORRECTIONS #5). So the mirror image of the carrier is not the carrier: the
        substrate is CHIRAL (has a definite handedness). DERIVED (the two orbits are distinct; parity
        swaps them).

  CH.3  the correspondence (filed through 19): substrate chirality <-> WEAK PARITY VIOLATION. The one
        chiral force (the weak SU(2), 28) couples to a single handedness; the carrier having a single
        handedness (no parity self-map) is exactly the structure that force requires. A CORRESPONDENCE,
        WEAK, quarantined -- reps/couplings/the V-A form do NOT travel. POSTULATE.

  CH.4  OWED: WHICH handedness maps to physical left (a convention until matter is oriented); the
        quantitative parity violation (the V-A structure, maximal violation) -- values/matter, danger
        zone. OWED.

Rests on 06 (the even-permutation carrier; the conjugate mirror), 28 (the chiral weak force it meets);
cites SU(2) = proper rotations (det +1). DANGER-FREE: pure orientation/group structure -- no mass, no
census, no coupling, no value. `--check` recomputes.
"""

import json
import sys
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ permutation parity (06.1's even orbit)
def inversions(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])


def parity(p):
    return inversions(p) % 2                 # 0 even (orientation-preserving), 1 odd (reversing)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))     # (p after q)


ALL_PERMS = [tuple(p) for p in permutations(range(4))]
EVEN = [p for p in ALL_PERMS if parity(p) == 0]      # A4, the carrier's orbit (06.1)
ODD = [p for p in ALL_PERMS if parity(p) == 1]       # the conjugate mirror (excluded)
IDENT = (0, 1, 2, 3)
TRANSPOSITION = (1, 0, 2, 3)                          # a reflection: sign -1

# ---- CH.1 the carrier is orientation-pure -- DERIVED -----------------------------------
even_count = len(EVEN)
even_closed = all(parity(compose(a, b)) == 0 for a in EVEN for b in EVEN)   # even . even = even
sign_is_plus = all(parity(p) == 0 for p in EVEN)
ch1_ok = (even_count == 12 and even_closed and sign_is_plus)
step("CH.1", "the carrier is ORIENTATION-PURE: 06.1's even permutations (sign +1) are closed under composition; 2I subset SU(2) = proper rotations (det +1)",
     "06.1 builds the carrier's 96-block on the EVEN permutations of four coordinates -- sign +1, "
     "orientation-preserving. The 12 even permutations (A4) are CLOSED under composition (even.even=even, "
     "the sign homomorphism is multiplicative), so the carrier never generates an orientation-reversing "
     "map. And 2I sits in SU(2) = the proper rotations (det +1, the double cover of SO(3)) -- it contains "
     "no reflection / improper element",
     ["06.6.1"],
     "the handedness, sitting in plain sight in 06. Container 06.1 is literally 'the even permutations of "
     "four coordinates', and its own note records that 'taking the odd orbit instead gives a conjugate "
     "copy' -- the carrier is one orbit, the EVEN one. Even permutations have sign +1 (orientation-"
     "preserving); the sign is a homomorphism to {+1,-1}, so a product of even permutations is even -- the "
     "12 even permutations (A4) are closed under composition. RUN IT: |EVEN| = 12, and even.even = even "
     "for all pairs. So nothing the carrier does reverses orientation. This matches the quaternionic "
     "picture: 2I is a finite subgroup of SU(2), and SU(2) double-covers SO(3) = the PROPER rotations "
     "(det +1); there is no reflection (det -1, an improper element) anywhere in the carrier. The carrier "
     "is orientation-PURE -- one handedness, built in.",
     "UNIQUE (the even orbit is closed under composition, sign +1; the carrier is orientation-pure)", "DERIVED",
     {"even_count": even_count, "odd_count": len(ODD), "even_closed_under_composition": even_closed,
      "all_even_sign_plus": sign_is_plus,
      "carrier_in_SU2": "2I subset SU(2) = proper rotations (det +1), the double cover of SO(3) -- no reflection",
      "clue": "06.1 builds the 96-block on EVEN permutations only; the odd orbit is the conjugate mirror"},
     check="the 12 even permutations (A4) are closed under composition (even.even=even), all sign +1")
assert ch1_ok

# ---- CH.2 parity is not a self-symmetry -- DERIVED -------------------------------------
# An odd permutation (a reflection) carries an even one OUT of the even orbit, into the odd orbit.
mirror_leaves_orbit = all(parity(compose(TRANSPOSITION, e)) == 1 for e in EVEN)   # odd . even = odd
orbits_disjoint = (set(EVEN) & set(ODD) == set())
ch2_ok = (parity(TRANSPOSITION) == 1 and mirror_leaves_orbit and orbits_disjoint and len(ODD) == 12)
step("CH.2", "PARITY is not a self-symmetry: an orientation reversal carries the carrier to the DISTINCT conjugate (mirror) copy",
     "an orientation reversal is an ODD permutation / a reflection (sign -1). Composing it with any "
     "carrier (even) element gives an ODD map (odd.even=odd) -- it lands in the OTHER orbit, the "
     "conjugate (odd) copy, which is a DISTINCT carrier (06 finding-2 / CORRECTIONS #5), disjoint from "
     "the even one. So the mirror image of the carrier is NOT the carrier: the substrate is CHIRAL",
     ["CH.1", "06.6.2"],
     "the chirality itself: the carrier is not equal to its own mirror image. Parity (a reflection, an "
     "orientation reversal) is an ODD permutation, sign -1. Apply it to the carrier's even orbit: "
     "odd.even = odd (the sign flips), so every carrier element is sent OUT of the even orbit into the "
     "odd one. The odd orbit is the CONJUGATE copy of the carrier -- 06's finding 2 / CORRECTIONS #5: "
     "the base (0,1/2,phi^-1/2,phi/2) on the even orbit vs the odd orbit are conjugate copies differing "
     "in 96 of 120 elements, the same abstract 2I in a mirror embedding. The two orbits are DISJOINT (a "
     "permutation is even or odd, never both). So parity maps the carrier to a DIFFERENT carrier -- it is "
     "not a self-symmetry. The substrate has a definite HANDEDNESS. (This is why 06 had to CHOOSE the "
     "even orbit and record the odd as the conjugate: the choice IS the chirality.)",
     "UNIQUE (parity sends the even carrier to the disjoint odd conjugate copy -- not a self-map)", "DERIVED",
     {"transposition_parity": parity(TRANSPOSITION), "mirror_leaves_even_orbit": mirror_leaves_orbit,
      "orbits_disjoint": orbits_disjoint, "odd_count": len(ODD),
      "chirality": "the carrier != its mirror image (the conjugate odd copy, 06 finding-2 / CORRECTIONS #5)",
      "choice_is_the_chirality": "06 chose the even orbit; the choice is the handedness"},
     check="a transposition (sign -1) sends every even carrier element into the disjoint odd orbit -- parity is not a self-map")
assert ch2_ok

# ---- CH.3 the correspondence: chirality <-> weak parity violation -- POSTULATE ----------
step("CH.3", "the correspondence (filed through 19): substrate chirality <-> WEAK PARITY VIOLATION",
     "filed through the 19 gate: the substrate's single handedness (no parity self-map, CH.2) <-> the "
     "WEAK force's parity violation (the one chiral force, SU(2), 28, couples to a single handedness). "
     "The carrier having exactly one handedness is the structure the chiral weak force requires. A "
     "CORRESPONDENCE, WEAK; reps / the coupling / the V-A form do NOT travel",
     ["CH.2", "28.W.2"],
     "the physical entry, held to the 19 discipline (mirror of 28.W.3). SUBSTRATE side (checked, "
     "CH.1-CH.2): the carrier is orientation-pure and parity carries it to a distinct mirror copy -- one "
     "handedness, built in. PHYSICS side (cited, never re-derived): the WEAK force is the one force that "
     "VIOLATES PARITY -- it couples only to left-handed fermions (and right-handed antifermions), maximal "
     "violation (Wu 1957); the other three forces are parity-symmetric. THE CORRESPONDENCE: the "
     "substrate's chirality (the carrier's single handedness, which 28.W.2 already needed and cited from "
     "maths-4) <-> the weak force's coupling to a single handedness. It is now forced on the substrate "
     "(CH.1-CH.2), not merely cited. FALSIFICATION SURFACE: if the fundamental interactions were ALL "
     "parity-symmetric, a chiral substrate would be wrong; but the weak force is maximally parity-"
     "violating -- the correspondence PASSES the consistency it asserts. WHAT DOES NOT TRAVEL: the matter "
     "REPRESENTATIONS (which fermions are left-handed doublets), the V-A structure, the coupling. A "
     "correspondence, quarantined (downstream_premise_use=False); no DERIVED step rests on it.",
     "POSTULATE (chirality <-> weak parity violation; a filed correspondence, WEAK, held)", "POSTULATE",
     {"substrate_side": "the carrier is orientation-pure; parity maps it to a distinct mirror copy (CH.1-CH.2)",
      "physics_side_cited": "the weak force violates parity maximally -- couples to one handedness (Wu 1957); the other forces do not",
      "correspondence": "substrate chirality <-> weak parity violation (forced here, was cited in 28.W.2)",
      "falsification": "all-parity-symmetric interactions would refute; the weak force is maximally chiral -- PASSES",
      "does_not_travel": "the matter representations; the V-A structure; the coupling",
      "downstream_premise_use": False},
     check=None)

# ---- CH.4 OWED ------------------------------------------------------------------------
step("CH.4", "OWED: which handedness is physical-left (a convention until matter is oriented); the quantitative V-A parity violation (danger zone)",
     "OWED: (a) WHICH of the two orbits maps to physical LEFT -- a convention/reading until matter is "
     "oriented on the substrate; (b) the QUANTITATIVE parity violation -- the V-A structure, maximal "
     "violation, the specific chiral couplings -- which needs matter representations and values (the "
     "danger zone). The substrate's chirality is forced; its orientation labelling and quantitative "
     "content are owed",
     ["CH.3"],
     "the honest residual. CH.1-CH.2 force that the substrate is chiral (one handedness, parity not a "
     "self-map); CH.3 files the correspondence to weak parity violation. What remains: (a) which orbit is "
     "'left' -- the substrate distinguishes its two mirror copies but nothing here labels one as the "
     "physical left-handed sector; that is a convention until matter fields are oriented on the carrier "
     "(a later, matter-sector question); (b) the QUANTITATIVE parity violation -- the V-A (vector minus "
     "axial) structure, the maximal-violation coupling -- which requires the matter representations and "
     "coupling values, the DANGER ZONE, not attempted. So the handedness is forced; the labelling and the "
     "numbers are owed. NOT attempted further here.",
     "OWED (the left/right labelling convention; the quantitative V-A parity violation -- danger zone)", "OWED",
     {"owed_labelling": "which orbit is physical-left -- a convention until matter is oriented on the carrier",
      "owed_quantitative": "the V-A structure / maximal violation / chiral couplings -- matter + values, danger zone",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="44-chirality",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        even_count=even_count, odd_count=len(ODD), even_closed=even_closed,
        transposition_parity=parity(TRANSPOSITION), orbits_disjoint=orbits_disjoint,
        finding="CHIRALITY forced on the substrate (28.W.2 only CITED it). The clue was in 06: the carrier "
                "is built on EVEN permutations (06.1, sign +1), the 12 of which are closed under "
                "composition -- so the carrier is ORIENTATION-PURE (CH.1); 2I subset SU(2) = proper "
                "rotations (det +1), no reflection. PARITY (an odd permutation / reflection, sign -1) "
                "carries the carrier into the DISJOINT odd orbit -- the conjugate mirror copy (06 "
                "finding-2 / CORRECTIONS #5), a distinct carrier -- so the substrate is CHIRAL, parity is "
                "not a self-symmetry (CH.2). Filed correspondence (CH.3, POSTULATE): substrate chirality "
                "<-> WEAK PARITY VIOLATION (the one chiral force, 28). The left/right labelling + the "
                "quantitative V-A violation are OWED (CH.4, danger zone). Danger-free; nothing fitted.",
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
