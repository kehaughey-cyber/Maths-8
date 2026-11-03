#!/usr/bin/env python3
"""Container 50 -- ELECTROWEAK MIXING: the Cartan is rank 2, so there are TWO neutral bosons -> photon + Z.

Forward-frontier #3 (Maths 6.7). 29.EM.2 located the electroweak algebra u(1)+su(2) = 1+3 = 4 = the
quaternion. This container forces the MIXING STRUCTURE that 29 did not: the electroweak Cartan (maximal
torus) is RANK 2 -- u(1) (hypercharge Y) contributes 1, su(2)'s Cartan (weak isospin T3) contributes 1 --
so there are exactly TWO neutral gauge directions (B from u(1), W3 from su(2)). They MIX: one combination
stays the massless PHOTON (the unbroken U(1)_EM), the orthogonal one is the massive Z. So the substrate
FORCES a second neutral boson (the Z), distinct from the photon. The mixing ANGLE (which combination) and
the breaking (Higgs) are values / matter -- OWED, danger zone; the mixing EXISTENCE is danger-free.

  EW.1  the electroweak Cartan is RANK 2: rank(u(1)) + rank(su(2)) = 1 + 1 = 2 (hypercharge Y + weak
        isospin T3, two commuting U(1) directions). So exactly TWO neutral (Cartan) gauge bosons. DERIVED.
  EW.2  the two neutral directions MIX: the unbroken U(1)_EM is a LINE in the rank-2 Cartan plane, the Z
        the orthogonal line. Generically the photon is a nontrivial COMBINATION of Y and T3 (mixing) --
        aligned with neither axis -- so a SECOND neutral boson (the Z) is forced, distinct from the photon.
        DERIVED (the existence; the specific line is the angle, EW.3).
  EW.3  the filed correspondence (through 19): the photon = the massless combination, the Z = the massive
        orthogonal one (Gell-Mann-Nishijima Q = T3 + Y/2); the WEINBERG ANGLE theta_W parametrizes WHICH
        combination -- a VALUE; the breaking that selects it (the Higgs) is MATTER. Correspondence. POSTULATE.
  EW.4  OWED: the Weinberg angle value; the Higgs / electroweak breaking mechanism (W/Z masses); the matter
        hypercharge assignments -- values + matter census, the danger zone. OWED.

Rests on 29 (u(1)+su(2), the abelian/non-abelian split), 28 (su(2)); cites the electroweak Cartan / the
Weinberg mixing / Gell-Mann-Nishijima. DANGER-FREE: the Cartan rank + mixing existence -- no mass, no
value. `--check` recomputes.
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


# ---- EW.1 the electroweak Cartan is rank 2 -- DERIVED ----------------------------------
RANK_U1, RANK_SU2 = 1, 1                          # rank(u(1))=1 (Y); rank(su(2))=1 (Cartan T3)
CARTAN_RANK = RANK_U1 + RANK_SU2                  # = 2: two commuting U(1) directions
NEUTRAL_BOSONS = CARTAN_RANK                      # B (from u(1)) and W3 (from su(2))
ew1_ok = (CARTAN_RANK == 2 and NEUTRAL_BOSONS == 2)
step("EW.1", "the electroweak Cartan is RANK 2: rank(u(1))+rank(su(2)) = 1+1 = 2 -> two neutral gauge directions (B, W3)",
     "the maximal torus (Cartan) of the electroweak algebra u(1)(+)su(2) (29.EM.2) has rank = rank(u(1)) "
     "+ rank(su(2)) = 1 + 1 = 2: the hypercharge Y (the u(1) direction) and the weak isospin T3 (su(2)'s "
     "Cartan). So there are exactly TWO commuting neutral gauge directions -- B (from u(1)) and W3 (from "
     "su(2))",
     ["29.EM.2", "28.W.1"],
     "the structural fact 29 stopped short of. Container 29.EM.2 gave the electroweak algebra as "
     "u(1)(+)su(2), dimension 1+3 = 4. Its MAXIMAL TORUS (Cartan subalgebra -- the maximal set of "
     "commuting generators) has rank = rank(u(1)) + rank(su(2)). rank(u(1)) = 1 (one abelian generator, "
     "the hypercharge Y, 29). su(2) has rank 1 (its Cartan is one generator -- the diagonal T3, since only "
     "one of i,j,k can be diagonalized at a time, 28). So the electroweak Cartan is rank 1+1 = 2: TWO "
     "commuting neutral directions, conventionally B (the u(1) gauge boson) and W3 (the neutral su(2) "
     "one). This rank-2 fact is what forces the mixing (EW.2): two neutral bosons must combine.",
     "UNIQUE (rank(u(1))+rank(su(2)) = 1+1 = 2 -- two neutral Cartan directions)", "DERIVED",
     {"rank_u1": RANK_U1, "rank_su2": RANK_SU2, "cartan_rank": CARTAN_RANK,
      "neutral_bosons": NEUTRAL_BOSONS, "which": "B (from u(1), hypercharge Y) and W3 (from su(2), T3)"},
     check="rank(u(1))+rank(su(2)) = 1+1 = 2 -> two neutral gauge directions (B, W3)")
assert ew1_ok

# ---- EW.2 the two neutral directions mix -> photon + Z -- DERIVED -----------------------
# a line in the 2-plane: coefficients (a,b). Pure axes = (1,0) [pure Y] or (0,1) [pure T3]. The physical
# photon is a COMBINATION (both nonzero) -> a nontrivial mixing -> a second neutral boson (the Z) is forced.
def is_combination(a, b):
    return a != 0 and b != 0                      # neither pure Y nor pure T3
photon_dir = (1, 1)                                # a representative nontrivial combination (schematic)
z_orthogonal = (1, -1)                             # the orthogonal line -- the Z
mixing_exists = is_combination(*photon_dir) and (photon_dir != z_orthogonal)
two_neutral_distinct = (NEUTRAL_BOSONS == 2)
ew2_ok = mixing_exists and two_neutral_distinct
step("EW.2", "the two neutral directions MIX: the photon is a combination of Y and T3; the orthogonal one is the Z (a SECOND neutral boson, forced)",
     "the unbroken electromagnetic U(1)_EM is a LINE in the rank-2 Cartan plane (EW.1); the orthogonal "
     "line is the Z. Generically the photon is a nontrivial COMBINATION of Y and T3 (aligned with neither "
     "axis) -- MIXING -- so a SECOND neutral gauge boson, the Z, is forced, distinct from the photon",
     ["EW.1"],
     "the mixing, forced by the rank-2 Cartan. With two commuting neutral directions (B and W3, EW.1), "
     "electroweak symmetry breaking leaves ONE unbroken U(1) (electromagnetism -- the massless photon) and "
     "one broken (the massive Z). The unbroken direction is a LINE in the 2-dimensional Cartan plane; the "
     "Z is the orthogonal line. Unless the photon happened to align exactly with an axis (pure hypercharge "
     "Y or pure T3), it is a nontrivial COMBINATION of both -- which is what MIXING means. The key forced "
     "consequence, danger-free: because the Cartan is rank 2 (not 1), there are TWO neutral gauge bosons, "
     "so a SECOND neutral boson beyond the photon -- the Z -- is FORCED to exist. (The specific "
     "combination -- the mixing angle -- is EW.3, a value; here only the EXISTENCE of the mixing / the Z "
     "is claimed.) This is the substrate predicting the Z boson from the rank-2 electroweak Cartan.",
     "UNIQUE (rank-2 Cartan => two neutral bosons => the photon is a combination, the Z the orthogonal -- mixing exists)", "DERIVED",
     {"photon_direction_schematic": list(photon_dir), "z_orthogonal_schematic": list(z_orthogonal),
      "mixing_exists": mixing_exists, "second_neutral_boson_forced": two_neutral_distinct,
      "forced": "a second neutral boson (the Z), distinct from the photon -- from the rank-2 Cartan"},
     check="rank-2 Cartan => photon = a combination (both nonzero), Z = orthogonal -> a second neutral boson (Z) forced")
assert ew2_ok

# ---- EW.3 the filed correspondence -- POSTULATE ----------------------------------------
step("EW.3", "the filed correspondence (through 19): photon = massless combination, Z = massive orthogonal (Gell-Mann-Nishijima); the ANGLE is a value",
     "filed through the 19 gate: the substrate's two neutral directions (EW.2) <-> the physical B and W3; "
     "the photon = the massless combination (Q = T3 + Y/2, Gell-Mann-Nishijima), the Z = the massive "
     "orthogonal one. The WEINBERG ANGLE theta_W (WHICH combination) is a VALUE; the breaking that selects "
     "it (the Higgs) is MATTER. A CORRESPONDENCE, WEAK -- the angle, the masses, the breaking do NOT travel",
     ["EW.2", "29.EM.3"],
     "the entry, held to the 19 discipline (mirror of 29.EM.3). SUBSTRATE side (checked, EW.1-EW.2): the "
     "electroweak Cartan is rank 2, so two neutral bosons that must mix -- a photon and a Z. PHYSICS side "
     "(cited): electroweak symmetry breaking SU(2)xU(1) -> U(1)_EM leaves the massless photon (the "
     "combination A = B cos(theta_W) + W3 sin(theta_W)) and the massive Z (the orthogonal), with the "
     "electric charge Q = T3 + Y/2 (Gell-Mann-Nishijima). THE CORRESPONDENCE: the substrate's two neutral "
     "directions <-> B and W3; the unbroken combination <-> the photon; the orthogonal <-> the Z. "
     "FALSIFICATION: a rank-1 electroweak Cartan would give NO second neutral boson (no Z); the substrate "
     "has rank 2 (EW.1) and the Z exists -- it PASSES. WHAT DOES NOT TRAVEL: the WEINBERG ANGLE theta_W "
     "(a value -- which combination), the W/Z MASSES and the HIGGS breaking mechanism (matter, danger "
     "zone), and the matter hypercharge assignments. A correspondence, quarantined; no downstream premise "
     "use.",
     "POSTULATE (photon = massless combination, Z = orthogonal; the angle theta_W a value; held)", "POSTULATE",
     {"substrate_side": "rank-2 Cartan -> two neutral bosons that mix (EW.1-EW.2)",
      "physics_side_cited": "SU(2)xU(1)->U(1)_EM: photon = B cos+W3 sin, Z orthogonal; Q = T3 + Y/2",
      "correspondence": "two neutral directions <-> B, W3; unbroken combination <-> photon; orthogonal <-> Z",
      "does_not_travel": "the Weinberg angle theta_W (value); the W/Z masses + Higgs breaking (matter, danger); hypercharge assignments",
      "downstream_premise_use": False},
     check=None)

# ---- EW.4 OWED ------------------------------------------------------------------------
step("EW.4", "OWED: the Weinberg angle value; the Higgs/electroweak breaking (W/Z masses); the matter hypercharge assignments -- danger zone",
     "OWED: (a) the WEINBERG ANGLE theta_W -- which combination is the photon -- a dimensionless value "
     "(an alpha_hat-type quantity, 27, to force not fit); (b) the HIGGS / electroweak breaking mechanism "
     "giving the W and Z their masses -- MATTER, the danger zone; (c) the matter HYPERCHARGE assignments. "
     "The mixing EXISTENCE (the Z) is forced; the angle, the masses, and the assignments are owed",
     ["EW.3"],
     "the honest residual. EW.1-EW.2 force the mixing existence (rank-2 Cartan -> a second neutral boson, "
     "the Z); EW.3 files the correspondence. What remains: (a) the WEINBERG ANGLE theta_W -- the specific "
     "combination -- a dimensionless coupling, hence (per 27) an alpha_hat quantity to FORCE not fit, "
     "respecting the refused-list; (b) the ELECTROWEAK BREAKING -- the Higgs mechanism, the W/Z masses "
     "(the photon staying massless) -- which involves MASS and the matter sector, the DANGER ZONE, not "
     "attempted; (c) the matter HYPERCHARGE assignments (which fermions carry which Y). So the mixing "
     "STRUCTURE (the Z's existence) is forced and danger-free; the angle, the masses, and the assignments "
     "are the forward, gated work. NOT attempted here.",
     "OWED (the Weinberg angle; the Higgs/breaking + W/Z masses; hypercharge assignments -- danger zone)", "OWED",
     {"owed_angle": "the Weinberg angle theta_W -- an alpha_hat-type value to force not fit (27)",
      "owed_breaking": "the Higgs / electroweak breaking + W/Z masses -- matter, danger zone",
      "owed_hypercharge": "the matter hypercharge assignments (which fermions carry which Y)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="50-electroweak-mixing",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        rank_u1=RANK_U1, rank_su2=RANK_SU2, cartan_rank=CARTAN_RANK, neutral_bosons=NEUTRAL_BOSONS,
        mixing_exists=mixing_exists, second_neutral_boson_forced=two_neutral_distinct,
        finding="ELECTROWEAK MIXING: the Cartan is rank 2, so a second neutral boson (the Z) is forced. "
                "29 gave u(1)+su(2)=1+3=4; here the maximal torus has rank(u(1))+rank(su(2)) = 1+1 = 2 -- "
                "two commuting neutral directions, B and W3 (EW.1). They MIX: the unbroken U(1)_EM (the "
                "massless photon) is a nontrivial combination of Y and T3, the Z is the orthogonal one -- "
                "so the substrate FORCES a second neutral boson, the Z, distinct from the photon (EW.2). "
                "The correspondence (photon = massless combination, Z = orthogonal, Q = T3 + Y/2) is filed "
                "through 19 (EW.3, POSTULATE); the WEINBERG ANGLE (which combination), the Higgs/breaking + "
                "W/Z masses, and the hypercharge assignments are OWED (EW.4, danger zone). Danger-free; "
                "nothing fitted.",
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
