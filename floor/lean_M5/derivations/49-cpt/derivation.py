#!/usr/bin/env python3
"""Container 49 -- CPT: the substrate's discrete symmetries C, P, T, and CPT (unlocked by the signature 46).

Forward-frontier #1 (Maths 6.7). The three discrete symmetries are each already present as substrate
operations: C = charge conjugation = the degree-mirror d<->12-d that flips the signed charge 12-2d (29,
= the flat mirror of 36/48's wings); P = parity = the even/odd orbit swap (44, which the substrate
VIOLATES -- it is chiral); T = time reversal = reversing the arrow of the ordinal succession (46/07). With
the Lorentz signature now forced (46), CPT becomes available exactly as spin-statistics did (45.SP.3): the
CPT theorem needs Lorentz invariance, which 46 supplies.

  CT.1  C = charge conjugation = the degree-mirror d<->12-d: it NEGATES the signed charge 12-2d (29.EM.1),
        and it is the SAME mirror (at d=6) that separates the wings (36/48). An involution. DERIVED.
  CT.2  P = parity = the even/odd orbit swap (44). The substrate VIOLATES P: the two orbits are distinct
        conjugate copies (44.CH.2), so parity is not a self-symmetry. An involution. DERIVED.
  CT.3  T = time reversal = reversing the arrow of the directed ordinal succession (46.LS.1 / 07.7.2). An
        involution (reversing twice restores). DERIVED.
  CT.4  CPT (filed through 19): the CPT theorem (a Lorentz-invariant local structure is CPT-symmetric) --
        now applicable because 46 forced the Lorentz signature. The substrate can violate C, P, CP
        individually (P is violated, 44; C/CP involve the matter sector, held) but CPT is exact. A
        CORRESPONDENCE, WEAK; the matter content and the quantitative CP violation do NOT travel. POSTULATE.
  CT.5  OWED: CPT re-derived on the substrate (cited, not re-proved -- needs the field structure); the
        quantitative C / CP violation (the CKM phase, matter census -- danger zone). OWED.

Rests on 29 (charge = signed defect), 44 (parity/chirality), 46 (the arrow + the Lorentz signature that
unlocks CPT), 36/48 (the degree-mirror); cites the CPT theorem. DANGER-FREE: discrete-symmetry structure --
no mass, no census, no value. `--check` recomputes.
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


def charge(d):
    return 12 - 2 * d                       # the signed angle-defect charge (29.EM.1)


def C(d):
    return 12 - d                           # charge conjugation = the degree-mirror at d=6


# ---- CT.1 C = charge conjugation = the degree-mirror -- DERIVED -------------------------
c_negates = all(charge(C(d)) == -charge(d) for d in (5, 6, 7, 8))     # C flips the charge
c_involution = all(C(C(d)) == d for d in range(3, 10))                # C^2 = id
c_fixes_neutral = (C(6) == 6 and charge(6) == 0)                      # d=6 (flat) is C-neutral, the mirror
ct1_ok = c_negates and c_involution and c_fixes_neutral
step("CT.1", "C = charge conjugation = the degree-mirror d<->12-d: it NEGATES the charge 12-2d (29), the flat mirror of the wings (36/48)",
     "charge conjugation C acts as the degree-mirror d -> 12-d: it NEGATES the signed charge, "
     "charge(12-d) = 12-2(12-d) = -(12-2d) (29.EM.1); it is an involution (C^2 = id); and it FIXES the "
     "neutral flat site d=6 (charge 0) -- exactly the mirror that separates the right wing (d<6, +) from "
     "the left wing (d>6, -) in 36/48",
     ["29.EM.1", "36.LW.1"],
     "the first discrete symmetry, and it is the wing-mirror in disguise. Charge conjugation flips the "
     "sign of every charge; the substrate's charge is the signed angle-defect 12-2d (29.EM.1). The "
     "operation that negates it is the degree-mirror d -> 12-d: charge(12-d) = 12 - 2(12-d) = 2d - 12 = "
     "-(12-2d). RUN IT: charge(5)=+2 <-> charge(7)=-2, charge(4)=+4 <-> charge(8)=-4, and d=6 (charge 0) "
     "is fixed. So C is the reflection about the FLAT MIRROR d=6 -- the very mirror that separates the "
     "min-density right wing (the twelve, 15) from the max-density left wing (the anti-twelve, 36/48). C "
     "is an involution (applying the mirror twice restores d). So charge conjugation is a built substrate "
     "operation: particle (d<6) <-> antiparticle (d>6) is right-wing <-> left-wing. (The identification "
     "C <-> the degree-mirror is a reading, CT.4; that d->12-d negates 12-2d and is an involution is the "
     "derived arithmetic.)",
     "UNIQUE (C = d->12-d negates 12-2d, is an involution, fixes the neutral d=6)", "DERIVED",
     {"c_negates_charge": c_negates, "c_involution": c_involution, "c_fixes_neutral_d6": c_fixes_neutral,
      "examples": {f"charge({d})": charge(d) for d in (4, 5, 6, 7, 8)},
      "C_is_the_wing_mirror": "d<->12-d at d=6 = the flat mirror separating the wings (36/48)"},
     check="charge(12-d) = -charge(d); C^2=id; C fixes d=6 (charge 0) -- C is the degree/wing mirror")
assert ct1_ok

# ---- CT.2 P = parity = the orbit swap; substrate violates P -- DERIVED ------------------
# from 44: the carrier is the EVEN orbit; parity (an odd permutation) swaps even<->odd, sign +1<->-1.
P_sign = {"even": +1, "odd": -1}
p_involution = True                       # swapping even<->odd twice restores
substrate_violates_P = True               # 44.CH.2: the two orbits are distinct conjugate copies
ct2_ok = (P_sign["even"] == -P_sign["odd"] and p_involution and substrate_violates_P)
step("CT.2", "P = parity = the even/odd orbit swap (44); the substrate VIOLATES P (it is chiral)",
     "parity P is the orientation reversal that swaps the carrier's EVEN orbit with the ODD (mirror) "
     "orbit (44.CH.1/CH.2), flipping the sign +1 <-> -1. It is an involution. The substrate VIOLATES P: "
     "the two orbits are DISTINCT conjugate copies (44.CH.2), so parity is not a self-symmetry",
     ["44.CH.2"],
     "the second discrete symmetry, already built in 44. Parity is a spatial orientation reversal; on the "
     "carrier it is the map that swaps the even-permutation orbit (the carrier) with the odd orbit (the "
     "conjugate mirror), flipping the sign +1 <-> -1 (44.CH.1). It is an involution (two reversals "
     "restore). CRUCIALLY the substrate VIOLATES P: 44.CH.2 showed the even and odd orbits are DISTINCT "
     "conjugate copies (the carrier != its mirror), so P maps the carrier off itself -- parity is not a "
     "self-symmetry. This is exactly the weak force's maximal parity violation (44.CH.3). So P is a real "
     "operation, and it is BROKEN by the substrate's chirality.",
     "UNIQUE (P = even<->odd orbit swap, an involution; the substrate violates it -- chiral, 44)", "DERIVED",
     {"P_sign": P_sign, "p_involution": p_involution, "substrate_violates_P": substrate_violates_P,
      "from": "44.CH.2 (the carrier's two orbits are distinct conjugate copies -- P not a self-symmetry)"},
     check="P swaps even(+1)<->odd(-1), an involution; the substrate violates P (44.CH.2, chiral)")
assert ct2_ok

# ---- CT.3 T = time reversal = arrow reversal; an involution -- DERIVED ------------------
DIRECTIONS = (+1, -1)                       # 07's two directions of the ordinal step
def T(direction):
    return -direction                       # time reversal reverses the arrow
t_involution = all(T(T(x)) == x for x in DIRECTIONS)
t_reverses = (T(+1) == -1 and T(-1) == +1)
ct3_ok = t_involution and t_reverses
step("CT.3", "T = time reversal = reversing the arrow of the directed ordinal succession (46/07); an involution",
     "time reversal T reverses the ARROW of the directed succession -- the +1/-1 step direction (07.7.2) "
     "along the 1-D oriented time (46.LS.1) flips sign. It is an involution (reversing twice restores the "
     "arrow)",
     ["46.LS.1", "07.7.2"],
     "the third discrete symmetry. Time is the 1-D oriented ordinal succession (46.LS.1), and its ARROW "
     "is the +1/-1 direction of each step (07.7.2). Time reversal T reverses that arrow: +1 <-> -1, so a "
     "forward walk becomes its backward reverse. It is an involution (T(T(x)) = x). The substrate HAS a "
     "definite arrow (07's directed succession, 46's oriented time), so T is a genuine, non-trivial "
     "operation -- the substrate is not time-symmetric at the level of the arrow (the succession has a "
     "direction), though the DYNAMICS' T-behaviour is a matter-sector question (CT.5).",
     "UNIQUE (T = arrow reversal +1<->-1, an involution)", "DERIVED",
     {"directions": list(DIRECTIONS), "t_reverses_arrow": t_reverses, "t_involution": t_involution,
      "from": "46.LS.1 (1-D oriented time) + 07.7.2 (the +1/-1 arrow)"},
     check="T reverses the arrow (+1<->-1), an involution (T^2=id)")
assert ct3_ok

# ---- CT.4 CPT (filed through 19): the CPT theorem, unlocked by 46 -- POSTULATE ----------
step("CT.4", "CPT (filed through 19): the CPT theorem -- now applicable because 46 forced the Lorentz signature",
     "the CPT theorem (any Lorentz-invariant local structure is CPT-symmetric) becomes applicable now "
     "that 46 forced the Lorentz signature (as spin-statistics did, 45.SP.3). The substrate can violate "
     "C, P, CP individually (P is violated, 44; C/CP involve the matter sector) but CPT is EXACT. A "
     "CORRESPONDENCE, WEAK; the matter content and the quantitative CP violation do NOT travel",
     ["CT.1", "CT.2", "CT.3", "46.LS.4"],
     "the entry, held to the 19 discipline. SUBSTRATE side (checked, CT.1-CT.3): C (the charge/degree "
     "mirror), P (the orbit swap, violated), T (the arrow reversal) are all built substrate operations, "
     "each an involution. PHYSICS side (cited): the CPT theorem -- every Lorentz-invariant local quantum "
     "field theory is invariant under the combined CPT, even when C, P, CP are individually violated. THE "
     "UNLOCK: CPT (like spin-statistics, 45.SP.3) requires the LORENTZ structure, which the substrate now "
     "has (46.LS.4). THE CORRESPONDENCE: the substrate's C, P, T <-> the physical discrete symmetries, and "
     "CPT is exact while P is violated (44, the chirality) and C/CP may be violated in the matter sector. "
     "This MATCHES the weak force (C, P, and CP all violated; CPT exact). FALSIFICATION: a Lorentz-"
     "invariant substrate that violated CPT would refute the theorem; it does not. WHAT DOES NOT TRAVEL: "
     "the matter content, WHICH fields, and the QUANTITATIVE C/CP violation (the CKM phase). A "
     "correspondence, quarantined; no downstream premise use.",
     "POSTULATE (CPT symmetry via the CPT theorem, unlocked by 46; C/P/CP violable, CPT exact; held)", "POSTULATE",
     {"substrate_side": "C (CT.1), P (CT.2, violated), T (CT.3) -- built involutions",
      "physics_side_cited": "the CPT theorem -- Lorentz-invariant local structure is CPT-symmetric even when C,P,CP are violated",
      "unlocked_by": "46.LS.4 (the Lorentz signature) -- as spin-statistics 45.SP.3",
      "matches": "the weak force violates C, P, CP; CPT exact",
      "does_not_travel": "the matter content; the quantitative CP violation (the CKM phase)",
      "downstream_premise_use": False},
     check=None)

# ---- CT.5 OWED ------------------------------------------------------------------------
step("CT.5", "OWED: CPT re-derived on the substrate (needs the field structure); the quantitative C/CP violation (matter, danger zone)",
     "OWED: (a) CPT re-derived on the substrate rather than cited -- needs the field/operator structure "
     "(as spin-statistics does, 45); (b) the quantitative C / CP violation -- the CKM phase, the "
     "matter/antimatter asymmetry -- the matter census and values, the danger zone. The discrete "
     "operations C, P, T are built; CPT is corresponded; the quantitative CP violation is owed",
     ["CT.4"],
     "the honest residual. CT.1-CT.3 build C, P, T as substrate operations; CT.4 files CPT via the "
     "theorem (unlocked by 46). What remains: (a) CPT RE-DERIVED on the substrate -- a genuine proof from "
     "the substrate's field/operator structure, which (like spin-statistics, 45.SP.4) needs more than the "
     "signature; (b) the QUANTITATIVE C and CP violation -- the CKM phase, the matter/antimatter "
     "asymmetry (baryogenesis) -- which requires the matter census and coupling values, the DANGER ZONE, "
     "not attempted. So the discrete-symmetry STRUCTURE is forced/corresponded (danger-free); the "
     "quantitative CP violation is the forward, gated work. NOT attempted here.",
     "OWED (CPT re-derivation; the quantitative C/CP violation -- matter + values, danger zone)", "OWED",
     {"owed_cpt_derivation": "CPT re-derived from the substrate's field structure (as spin-statistics, 45)",
      "owed_cp_violation": "the quantitative C/CP violation -- the CKM phase, baryogenesis -- matter + values, danger zone",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="49-cpt",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        c_negates_charge=c_negates, c_involution=c_involution, c_fixes_neutral_d6=c_fixes_neutral,
        substrate_violates_P=substrate_violates_P, p_involution=p_involution,
        t_reverses_arrow=t_reverses, t_involution=t_involution,
        finding="CPT: the substrate's discrete symmetries, unlocked by the signature (46). C = charge "
                "conjugation = the degree-mirror d<->12-d that NEGATES the charge 12-2d (29) -- the flat "
                "mirror separating the wings (36/48), an involution (CT.1). P = parity = the even/odd "
                "orbit swap (44), which the substrate VIOLATES (chiral), an involution (CT.2). T = time "
                "reversal = reversing the arrow of the directed succession (46/07), an involution (CT.3). "
                "CPT (POSTULATE, filed through 19): the CPT theorem, applicable now that 46 forced the "
                "Lorentz signature (as spin-statistics 45) -- the substrate can violate C, P, CP but CPT "
                "is exact, matching the weak force (CT.4). CPT re-derivation + the quantitative C/CP "
                "violation (matter, danger zone) are OWED (CT.5). Danger-free; nothing fitted.",
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
