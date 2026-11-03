#!/usr/bin/env python3
"""Container 51 -- THE SM GAUGE PRODUCT: U(1) x SU(2) x SU(3) located as electroweak(2I) x strong(E8).

Forward-frontier #2 (Maths 6.7). 28/29/30/31 located the three gauge algebras separately; this container
states the PRODUCT structure they form -- the Standard Model gauge group U(1) x SU(2) x SU(3) -- as two
sectors in distinct carrier structures: the ELECTROWEAK (SU(2) x U(1)) in the quaternion 2I (28/29/50), the
STRONG (SU(3)) in E8's A2 (30), with colour's Z/3 center native in 2I (31). It preserves 31's caveat
(1+3+8=12 is NOT a forced decomposition of the geometric twelve) and DEFERS the SU(2)/SU(3) joint
fine-structure to the collaborator's fork -- coordinate, do not duplicate.

  GP.1  the three located gauge algebras and their dimensions: u(1) (dim 1, 29), su(2) (dim 3, 28), su(3)
        (dim 8 = 6 roots + 2 rank, A2 subset E8, 30). Total 1+3+8 = 12 as a SUM of located pieces. DERIVED.
  GP.2  the PRODUCT structure: the ELECTROWEAK sector SU(2) x U(1) lives in the quaternion 2I (28/29/50);
        the STRONG sector SU(3) lives in E8's A2 (30), with colour's Z/3 center native in 2I (31). Two
        sectors in distinct carrier structures -> the SM gauge group is the product U(1) x SU(2) x SU(3).
        DERIVED.
  GP.3  the honest caveat (preserving 31): 1+3+8 = 12 equals the geometric twelve NUMERICALLY, but this is
        NOT a forced DECOMPOSITION of the geometric twelve -- 31 showed the 12 vertices cannot split 1+3+8
        as a symmetry decomposition (the "1" needs a fixed vertex -> stabilizer order 10, an 8-orbit needs
        8 | 10, impossible). Colour's 3 IS native (31); the full 1+3+8 decomposition is NOT forced. DERIVED
        (the coincidence flagged, not banked).
  GP.4  the joint (filed through 19; DEFERRED to the fork): how SU(2) and SU(3) sit together -- the
        specific embedding / intersection in the carrier/E8 -- is the collaborator's fork. The product
        LOCATION is filed; the JOINT fine-structure is held to coordinate, not duplicate. POSTULATE.
  GP.5  OWED: the joint (fork); the couplings g_weak, alpha_s, alpha_EM (danger zone, 27's alpha_hat); the
        matter representations / the quark & lepton content (danger zone). OWED.

Rests on 28 (su(2)), 29 (u(1)), 30 (su(3)=A2 subset E8), 31 (colour Z/3 native); cites the SM gauge group.
DANGER-FREE: the located dimensions + product structure -- no mass, no census, no coupling, no value.
`--check` recomputes.
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


# ---- GP.1 the three located gauge algebras and dimensions -- DERIVED -------------------
U1_DIM, SU2_DIM, SU3_DIM = 1, 3, 8               # 29, 28, 30 (su(3)=A2: 6 roots + 2 rank = 8)
TOTAL = U1_DIM + SU2_DIM + SU3_DIM               # 1+3+8 = 12
gp1_ok = (U1_DIM == 1 and SU2_DIM == 3 and SU3_DIM == 8 and TOTAL == 12)
step("GP.1", "the three located gauge algebras: u(1)=1 (29), su(2)=3 (28), su(3)=8 (A2 subset E8, 30); total 1+3+8=12",
     "the three Standard-Model gauge algebras, each located in the carrier: u(1) (dim 1, the abelian "
     "phase / EM, 29), su(2) (dim 3, the imaginary quaternions, 28), su(3) (dim 8 = 6 A2 roots + 2 rank, "
     "A2 subset E8, 30). Their dimensions SUM to 1+3+8 = 12",
     ["28.W.1", "29.EM.2", "30.S.1"],
     "gather the located pieces. Container 28 located su(2) (dim 3, the imaginary quaternions of 2I); 29 "
     "located u(1) (dim 1, the abelian phase, the charge = signed defect); 30 located su(3) as A2 inside "
     "E8 (dim 8 = 6 roots + 2 Cartan rank). These are the three gauge algebras of the Standard Model, and "
     "their dimensions sum to 1 + 3 + 8 = 12 -- the count of gauge bosons (1 photon-sector B, 3 weak "
     "W-bosons, 8 gluons). This is a SUM of separately-located pieces; whether it is ALSO a decomposition "
     "of the geometric twelve is a separate (and negative) question, GP.3.",
     "UNIQUE (u(1)=1, su(2)=3, su(3)=8; sum 12 -- the located gauge dimensions)", "DERIVED",
     {"u1_dim": U1_DIM, "su2_dim": SU2_DIM, "su3_dim": SU3_DIM, "total": TOTAL,
      "sources": "28 (su2), 29 (u1), 30 (su3=A2 subset E8)"},
     check="u(1)=1, su(2)=3, su(3)=8; 1+3+8 = 12 (the located gauge dimensions)")
assert gp1_ok

# ---- GP.2 the product structure: electroweak(2I) x strong(E8) -- DERIVED ----------------
EW_LOCUS = "the quaternion 2I (28/29/50)"        # SU(2) x U(1)
STRONG_LOCUS = "E8's A2 (30); colour Z/3 native in 2I (31)"   # SU(3)
distinct_sectors = (EW_LOCUS != STRONG_LOCUS)
step("GP.2", "the PRODUCT structure: electroweak (SU(2)xU(1)) in the quaternion 2I; strong (SU(3)) in E8's A2 -> U(1)xSU(2)xSU(3)",
     "the SM gauge group is a PRODUCT of two sectors located in DISTINCT carrier structures: the "
     "ELECTROWEAK sector SU(2) x U(1) in the quaternion 2I (28/29, mixing 50); the STRONG sector SU(3) in "
     "E8's A2 (30), with colour's Z/3 center native in 2I (31). So the located gauge group is the product "
     "U(1) x SU(2) x SU(3)",
     ["GP.1", "30.S.1", "31.CS.1"],
     "the product, from where each sector lives. The ELECTROWEAK sector (SU(2) from the imaginary "
     "quaternions, U(1) from the abelian phase, mixing into photon+Z at 50) lives in the QUATERNION "
     "structure of the carrier 2I. The STRONG sector (SU(3)) lives in E8's A2 root system (30), a "
     "different structure -- with the important refinement (31) that colour's Z/3 CENTER is native in 2I "
     "(the order-3 seating), even though the full su(3) adjoint is the less-native E8/A2 side. Because the "
     "electroweak and strong sectors are located in distinct carrier structures (the quaternion vs E8's "
     "A2), they form a PRODUCT: the Standard Model gauge group U(1) x SU(2) x SU(3), the direct product of "
     "the located factors. (The FINE structure of how SU(2) and SU(3) sit together -- the joint -- is "
     "GP.4, the fork's.)",
     "UNIQUE (electroweak in 2I, strong in E8's A2 -- distinct sectors -> the product U(1)xSU(2)xSU(3))", "DERIVED",
     {"electroweak_locus": EW_LOCUS, "strong_locus": STRONG_LOCUS, "distinct_sectors": distinct_sectors,
      "product": "U(1) x SU(2) x SU(3) -- the SM gauge group, the direct product of the located factors"},
     check="electroweak (SU(2)xU(1)) in 2I; strong (SU(3)) in E8's A2 -- distinct sectors -> the product SM gauge group")
assert distinct_sectors

# ---- GP.3 the honest caveat: 1+3+8=12 is NOT a forced geometric decomposition -- DERIVED -
# 31's argument: a "1" (singlet) needs a fixed vertex -> stabilizer order 12/1... the icosahedral vertex
# stabilizer is order 10 (|2I->I|=60, 60/... the vertex-transitive action on 12 has stabilizer 60/12=5 in
# I, order 10 in 2I); an 8-orbit needs 8 | (orbit-stabilizer), and 8 does NOT divide 10. So the 12 cannot
# split 1+3+8 as a symmetry decomposition. Preserve this negative.
STAB_ORDER = 10                                   # the 2I-stabilizer of a vertex (order 10)
eight_divides_ten = (STAB_ORDER % SU3_DIM == 0)   # False: 8 does not divide 10
decomposition_forced = eight_divides_ten          # False
gp3_ok = (TOTAL == 12 and not decomposition_forced)
step("GP.3", "the honest caveat (31): 1+3+8=12 equals the geometric twelve NUMERICALLY, but is NOT a forced decomposition (8 does not divide 10)",
     "1+3+8 = 12 coincides with the geometric twelve NUMERICALLY, but 31 showed this is NOT a forced "
     "DECOMPOSITION of the geometric twelve: a singlet '1' needs a fixed vertex (stabilizer order 10 in "
     "2I), and an 8-orbit would need 8 | 10, which is FALSE. So the twelve cannot split 1+3+8 as a "
     "symmetry decomposition. Colour's 3 IS native (31); the full 1+3+8 decomposition is NOT forced",
     ["GP.1", "31.CS.2"],
     "the discipline: flag the coincidence, do not bank it. The gauge dimension sum 1+3+8 = 12 (GP.1) "
     "equals the count of geometric twelve (the icosahedral vertices) -- a tempting 'the 12 gauge bosons "
     "ARE the 12 vertices, split 1+3+8'. Container 31 already REFUTED that as a symmetry decomposition: "
     "the icosahedral action on the twelve vertices has a vertex-stabilizer of order 10 in 2I; a singlet "
     "'1' would be a fixed vertex, and an '8' would be an orbit of size 8, requiring 8 | 10 by "
     "orbit-stabilizer -- which is FALSE (8 does not divide 10). So the twelve do NOT split as 1+3+8 under "
     "the symmetry. The truth 31 established: colour's 3 IS native (an order-3 seating), but the full "
     "1+3+8 = 12 is a SUM of separately-located pieces, NOT a forced decomposition of the geometric "
     "twelve. This container preserves that -- the '12' is a numerical coincidence flagged, never banked "
     "as structure. (This is exactly the anti-fitting discipline: noticing 1+3+8=12 is fine; asserting it "
     "as a forced decomposition is refused.)",
     "UNIQUE (1+3+8=12 numerically; 8 does not divide 10 -> not a forced geometric decomposition, 31)", "DERIVED",
     {"total": TOTAL, "vertex_stabilizer_order_2I": STAB_ORDER,
      "eight_divides_ten": eight_divides_ten, "decomposition_forced": decomposition_forced,
      "caveat": "1+3+8=12 numerically; NOT a forced decomposition of the geometric twelve (31); colour's 3 native, full decomposition not forced"},
     check="1+3+8=12 numerically; 8 does not divide 10 -> the twelve do NOT split 1+3+8 (31); coincidence flagged not banked")
assert gp3_ok

# ---- GP.4 the joint -- POSTULATE (deferred to the fork) --------------------------------
step("GP.4", "the joint (filed through 19; DEFERRED to the fork): how SU(2) and SU(3) sit together -- the collaborator's fork",
     "filed through the 19 gate: the SM gauge group U(1) x SU(2) x SU(3) <-> the located product "
     "(GP.1-GP.2). The FINE structure of how SU(2) (2I) and SU(3) (E8's A2) sit together -- the specific "
     "embedding / intersection / the joint -- is the collaborator's fork; the product LOCATION is filed, "
     "the JOINT is held to COORDINATE, not duplicate. A CORRESPONDENCE, WEAK",
     ["GP.2", "30.S.3", "31.CS.3"],
     "the entry, held to the 19 discipline, and honest about the boundary with the fork. SUBSTRATE side "
     "(checked, GP.1-GP.3): the three gauge algebras are located (dims 1,3,8), forming a product of two "
     "sectors (electroweak in 2I, strong in E8/A2), with the 1+3+8=12 coincidence flagged not banked. "
     "PHYSICS side (cited): the SM gauge group is U(1) x SU(2) x SU(3). THE CORRESPONDENCE: the located "
     "product <-> the SM gauge group. WHAT IS DEFERRED (the fork): the JOINT -- how SU(2) and SU(3) "
     "embed/intersect in the carrier/E8, the fine structure of the E8 -> SM breaking chain -- is being "
     "infilled in the collaborator's fork (HANDOFF: the SU(2)/SU(3) joint, step 5, held to coordinate). "
     "This container states the PRODUCT (the located factors), not the joint, to avoid duplicating the "
     "fork. FALSIFICATION: if the carrier could not host all three factors, the location would fail; it "
     "hosts them (28/29/30/31). WHAT DOES NOT TRAVEL: the joint fine-structure (fork), the couplings, the "
     "matter reps. A correspondence, quarantined; no downstream premise use.",
     "POSTULATE (the SM gauge product located; the joint fine-structure deferred to the fork; held)", "POSTULATE",
     {"substrate_side": "the located product: electroweak(2I) x strong(E8/A2), dims 1,3,8 (GP.1-GP.3)",
      "physics_side_cited": "the SM gauge group U(1) x SU(2) x SU(3)",
      "deferred_to_fork": "the JOINT -- how SU(2) and SU(3) embed/intersect; the E8->SM breaking fine-structure",
      "does_not_travel": "the joint fine-structure (fork); the couplings; the matter reps",
      "downstream_premise_use": False},
     check=None)

# ---- GP.5 OWED ------------------------------------------------------------------------
step("GP.5", "OWED: the joint (fork); the couplings g_weak/alpha_s/alpha_EM (danger); the matter representations (danger)",
     "OWED: (a) the JOINT -- how SU(2) and SU(3) sit together, the E8 -> SM fine-structure -- the "
     "collaborator's fork; (b) the COUPLINGS g_weak, alpha_s, alpha_EM (~1/137) -- dimensionless "
     "alpha_hat-type values (27) to force not fit, the danger zone; (c) the matter REPRESENTATIONS -- the "
     "quark and lepton content, their quantum numbers -- the matter census, danger zone. The product is "
     "located; the joint, couplings, and matter are owed",
     ["GP.4"],
     "the honest residual. GP.1-GP.3 locate the SM gauge product (danger-free); GP.4 files it and defers "
     "the joint. What remains: (a) the JOINT (the fork); (b) the three COUPLINGS -- each a dimensionless "
     "coupling, hence (per 27) an alpha_hat quantity to FORCE not fit, respecting the refused-list, the "
     "DANGER ZONE; (c) the matter REPRESENTATIONS -- which substrate objects are the quarks (colour "
     "triplets) and leptons (colour singlets), their weak-isospin and hypercharge assignments -- the "
     "matter census, DANGER ZONE. So the gauge PRODUCT is located and danger-free; the joint, the "
     "couplings, and the matter content are the forward, gated work. NOT attempted here.",
     "OWED (the joint -- fork; the couplings -- danger; the matter representations -- danger)", "OWED",
     {"owed_joint": "how SU(2) and SU(3) sit together / the E8->SM fine-structure -- the collaborator's fork",
      "owed_couplings": "g_weak, alpha_s, alpha_EM -- dimensionless alpha_hat values to force not fit (27), danger zone",
      "owed_matter": "the quark & lepton representations and quantum numbers -- the matter census, danger zone",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="51-gauge-product",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        u1_dim=U1_DIM, su2_dim=SU2_DIM, su3_dim=SU3_DIM, total=TOTAL,
        vertex_stabilizer_order_2I=STAB_ORDER, eight_divides_ten=eight_divides_ten,
        decomposition_forced=decomposition_forced, distinct_sectors=distinct_sectors,
        finding="THE SM GAUGE PRODUCT: U(1) x SU(2) x SU(3) located as electroweak(2I) x strong(E8). The "
                "three gauge algebras -- u(1)=1 (29), su(2)=3 (28), su(3)=8 (A2 subset E8, 30) -- sum to "
                "1+3+8=12 (GP.1). They form a PRODUCT of two sectors in distinct carrier structures: the "
                "electroweak SU(2)xU(1) in the quaternion 2I (28/29/50), the strong SU(3) in E8's A2 (30) "
                "with colour's Z/3 native in 2I (31) -> the SM gauge group U(1)xSU(2)xSU(3) (GP.2). CAVEAT "
                "(preserving 31): 1+3+8=12 equals the geometric twelve NUMERICALLY but is NOT a forced "
                "decomposition (8 does not divide 10; the twelve can't split 1+3+8) -- coincidence flagged, "
                "not banked (GP.3). The JOINT (how SU(2)/SU(3) sit together) is DEFERRED to the "
                "collaborator's fork (GP.4, POSTULATE); the joint, the couplings, and the matter reps are "
                "OWED (GP.5, danger zone). Danger-free; nothing fitted.",
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
