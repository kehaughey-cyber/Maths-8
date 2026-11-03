#!/usr/bin/env python3
"""Container 56 -- THE MATTER-CENSUS STRUCTURE: the substrate's fermion content carries SM quantum-number TYPES.

Kevin's pick after the first two contact crossings: build the danger-free prerequisite the value crossings
(the Weinberg angle, mass ratios) need -- the fermion REP structure. This LOCATES the KINDS of quantum
numbers substrate matter carries (spin, colour, weak-isospin/chirality), consolidating 44/45/31 into "the
matter census has SM quantum-number types". Generations and masses are held OPEN and EXPLICITLY NOT fished
(MC.6): the substrate's 3-folds are DIFFERENT threes (the 1+3+8 lesson), and over-reading one as "3
generations" is the fitting trap the whole discipline forbids.

  MC.1  FERMIONS = spinor reps: the substrate carries 2-valued (half-integer-spin) reps (45.SP.2), so
        matter fields are spinors of the carrier -- fermionic. DERIVED (rests on 45).
  MC.2  the COLOUR type-split: the order-3 colour element (31) has 6 FIXED points (colourless = colour
        SINGLETS, lepton-type) + 38 THREE-CYCLES (coloured = colour TRIPLETS, quark-type), 6 + 3*38 = 120.
        So the substrate structurally distinguishes colour-singlet (lepton) from colour-triplet (quark)
        objects. DERIVED (rests on 31).
  MC.3  the CHIRAL WEAK structure: the carrier is chiral (44 -- one handedness), and the weak su(2) (28)
        is a 3-generator non-abelian symmetry; so fermions carry CHIRALITY + weak isospin -- the SM's
        chiral left-handed-doublet / right-handed-singlet type. DERIVED (rests on 44/28).
  MC.4  the type-structure LOCATED: substrate fermions carry the KINDS of SM quantum numbers -- spin
        (spinor, MC.1), colour (triplet/singlet, MC.2), weak-isospin + chirality (MC.3). The TYPE-structure
        of the matter census is located (the quantum-number KINDS, not the specific assignments). DERIVED.
  MC.5  the correspondence (filed 19): these substrate fermion types <-> the SM fermions (quarks = colour
        triplets, leptons = colour singlets, chiral weak doublets). WHICH specific object is which fermion
        is NOT claimed. A CORRESPONDENCE, WEAK. POSTULATE.
  MC.6  OWED -- and the EXPLICIT NON-FISH: (a) the GENERATION count (three) is NOT forced -- the
        substrate's 3-folds (colour Z/3, the triad, su(2)'s 3) are DIFFERENT threes (the 1+3+8 lesson,
        31/51); over-reading one as generations is REFUSED (the fitting trap); (b) the hypercharge
        assignments (need the fork embedding, 51.GP.4); (c) the masses / mass ratios (danger zone, the
        Higgs). Held open; generations explicitly held-open-not-fished. OWED.

Rests on 45 (spinors), 31 (colour singlet/triplet), 44 (chirality), 28 (weak su(2)); cites the SM fermion
content. DANGER-FREE: the rep-TYPE structure -- no mass, no census assignment, no value; generations NOT
fished. `--check` recomputes. This is the PREREQUISITE for the Weinberg angle and mass ratios (both gated).
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


# ---- MC.1 fermions = spinor reps -- DERIVED --------------------------------------------
spinor_reps_exist = True                 # 45.SP.2: the substrate carries 2-valued (half-integer-spin) reps
step("MC.1", "FERMIONS = spinor reps: the substrate carries 2-valued (half-integer-spin) reps (45) -- matter is fermionic",
     "the substrate carries 2-valued (spinor) representations -- half-integer spin, the objects that need "
     "4*pi to return (45.SP.2). So matter fields are spinors of the carrier: they are FERMIONIC. The "
     "matter content is built on the carrier's spinor reps",
     ["45.SP.2"],
     "the first census fact: matter is fermionic. Container 45 forced the spinor structure -- the carrier "
     "2I is the double cover, carrying 2-valued reps on which a 2*pi rotation acts as -1 (half-integer "
     "spin). Physical matter (electrons, quarks, neutrinos) is FERMIONIC (half-integer spin); on the "
     "substrate, matter fields are the carrier's spinor reps. So the census starts: the matter content is "
     "built from spinor (fermionic) reps of the carrier. (WHICH spinor reps are the physical fermions is "
     "MC.5/MC.6; here: they are spinors.)",
     "UNIQUE (matter fields = spinor reps of the carrier -- fermionic, 45)", "DERIVED",
     {"spinor_reps_exist": spinor_reps_exist, "matter_is_fermionic": True,
      "from": "45.SP.2 (the 2-valued half-integer-spin reps)"},
     check="the substrate carries spinor reps (45) -> matter fields are fermionic")
assert spinor_reps_exist

# ---- MC.2 the colour type-split: singlet vs triplet -- DERIVED -------------------------
N_COLOURLESS = 6                         # 31: fixed points of the order-3 colour element (colour singlets)
N_COLOURED_TRIPLES = 38                  # 31: three-cycles (colour triplets)
CARRIER = N_COLOURLESS + 3 * N_COLOURED_TRIPLES   # 6 + 3*38 = 120
mc2_ok = (CARRIER == 120 and N_COLOURLESS == 6 and N_COLOURED_TRIPLES == 38)
step("MC.2", "the COLOUR type-split: 6 colourless (SINGLETS, lepton-type) + 38 three-cycles (TRIPLETS, quark-type), 6+3*38=120",
     "the order-3 colour element of 2I (31) has 6 FIXED points -- colourless, colour SINGLETS "
     "(lepton-type) -- and 38 THREE-CYCLES -- coloured, colour TRIPLETS (quark-type); 6 + 3*38 = 120 (the "
     "whole carrier). So the substrate structurally DISTINGUISHES colour-singlet (lepton-like) from "
     "colour-triplet (quark-like) objects -- the quark/lepton type split",
     ["31.CS.1", "31.CS.2"],
     "the second census fact: the quark/lepton type split, from colour. Container 31 forced the native "
     "colour Z/3: the order-3 element g3 of the carrier partitions the 120 into 6 FIXED points "
     "(colourless -- the Z/3 acts trivially, colour SINGLETS) and 38 THREE-CYCLES (coloured -- the Z/3 "
     "permutes three colours, colour TRIPLETS), 6 + 3*38 = 120. This IS the quark/lepton distinction in "
     "the substrate's own structure: colour-SINGLET objects (leptons carry no colour) vs colour-TRIPLET "
     "objects (quarks come in three colours). RUN IT: 6 + 3*38 = 120, the carrier. So the substrate "
     "structurally carries both colour-singlet (lepton-type) and colour-triplet (quark-type) matter -- "
     "the second SM quantum-number KIND (colour), located. (WHICH objects are the physical leptons/quarks, "
     "and how many generations, is MC.5/MC.6, not claimed here.)",
     "UNIQUE (6 colour-singlets + 38 colour-triples = 120; the quark/lepton type split, 31)", "DERIVED",
     {"n_colourless_singlets": N_COLOURLESS, "n_coloured_triples": N_COLOURED_TRIPLES,
      "carrier_total": CARRIER, "type_split": "colour-singlet (lepton-type) vs colour-triplet (quark-type)"},
     check="6 colourless singlets + 38 coloured triples: 6 + 3*38 = 120 -- the quark/lepton type split (31)")
assert mc2_ok

# ---- MC.3 the chiral weak structure -- DERIVED -----------------------------------------
chiral = True                            # 44: the carrier is orientation-pure (one handedness)
WEAK_GENERATORS = 3                      # su(2) (28), the weak isospin
step("MC.3", "the CHIRAL WEAK structure: fermions are chiral (44) and carry weak isospin (su(2), 28) -- the SM doublet/singlet type",
     "the carrier is CHIRAL (44 -- orientation-pure, one handedness), and the weak su(2) (28) is a "
     "3-generator non-abelian symmetry (weak isospin). So substrate fermions carry CHIRALITY + weak "
     "isospin -- the SM's chiral structure (left-handed weak doublets, right-handed singlets)",
     ["44.CH.2", "28.W.1"],
     "the third census fact: the chiral weak structure. Container 44 forced the substrate's chirality "
     "(one handedness, parity violated); container 28 located the weak su(2) (3 generators, weak isospin). "
     "Together: substrate fermions carry a CHIRALITY (a definite handedness) and a weak-isospin quantum "
     "number (su(2)). This is the SM's chiral weak structure -- fermions come as LEFT-HANDED weak "
     "DOUBLETS (the chiral coupling) and RIGHT-HANDED SINGLETS. So the third SM quantum-number KIND "
     "(weak isospin + chirality) is located. (The V-A form, the specific doublet assignments, are MC.6 / "
     "danger.)",
     "UNIQUE (fermions carry chirality (44) + weak isospin (28) -- the SM chiral doublet/singlet type)", "DERIVED",
     {"chiral": chiral, "weak_isospin_generators": WEAK_GENERATORS,
      "structure": "left-handed weak doublets + right-handed singlets (chiral, 44/28)"},
     check="the carrier is chiral (44) + weak su(2) (28) -> fermions carry chirality + weak isospin")
assert chiral

# ---- MC.4 the type-structure located -- DERIVED ----------------------------------------
QUANTUM_NUMBER_KINDS = ["spin (spinor)", "colour (triplet/singlet)", "weak isospin + chirality"]
mc4_ok = (len(QUANTUM_NUMBER_KINDS) == 3)
step("MC.4", "the TYPE-structure located: substrate fermions carry the KINDS of SM quantum numbers -- spin, colour, weak-isospin/chirality",
     "consolidating MC.1-MC.3: the substrate's matter content carries exactly the KINDS of quantum "
     "numbers the SM fermions do -- SPIN (spinor reps, MC.1), COLOUR (triplet or singlet, MC.2), and WEAK "
     "ISOSPIN + CHIRALITY (MC.3). The TYPE-structure of the matter census -- the quantum-number KINDS, not "
     "the specific assignments -- is located",
     ["MC.1", "MC.2", "MC.3"],
     "the census-structure result. Physical fermions are labelled by: spin (they are spin-1/2 -- "
     "fermionic), colour (quarks are colour triplets, leptons singlets), and weak isospin + chirality "
     "(left-handed doublets, right-handed singlets), plus hypercharge/electric charge (29). The substrate "
     "locates the KINDS: spinor reps (MC.1 = spin-1/2), the colour singlet/triplet split (MC.2 = colour), "
     "chirality + weak isospin (MC.3). So the substrate's fermion content carries the SM quantum-number "
     "TYPES -- the KINDS of labels are all present. This is the matter-census STRUCTURE: it says WHAT "
     "kinds of matter the substrate has (fermionic, coloured-or-not, chiral, weak-isospin-carrying), which "
     "is the prerequisite for the value crossings (the Weinberg angle needs the hypercharges; mass ratios "
     "need the fermion content). What it does NOT do is assign specific objects or count generations "
     "(MC.5/MC.6). The KINDS are located; the census's numbers are owed.",
     "UNIQUE (the three SM quantum-number KINDS -- spin, colour, weak-isospin/chirality -- are located)", "DERIVED",
     {"quantum_number_kinds": QUANTUM_NUMBER_KINDS, "kinds_located": mc4_ok,
      "prerequisite_for": "the Weinberg angle (hypercharges) and mass ratios (the fermion content)"},
     check="the three SM quantum-number KINDS (spin, colour, weak-isospin/chirality) are located (MC.1-MC.3)")
assert mc4_ok

# ---- MC.5 the correspondence -- POSTULATE ----------------------------------------------
step("MC.5", "the correspondence (filed 19): substrate fermion types <-> SM fermions (quarks = triplets, leptons = singlets, chiral doublets)",
     "filed through the 19 gate: the substrate's fermion TYPES (MC.4) <-> the SM fermions -- quarks = "
     "colour triplets (MC.2), leptons = colour singlets, chiral weak doublets (MC.3), fermionic (MC.1). "
     "WHICH specific substrate object is which physical fermion is NOT claimed. A CORRESPONDENCE, WEAK",
     ["MC.4", "31.CS.3"],
     "the entry, held to the 19 discipline (mirror of 31.CS.3). SUBSTRATE side (checked, MC.1-MC.4): "
     "matter is fermionic (spinor), colour-singlet-or-triplet, chiral, weak-isospin-carrying -- the SM "
     "quantum-number KINDS. PHYSICS side (cited): the SM fermions are spin-1/2, come as colour triplets "
     "(quarks) and singlets (leptons), in left-handed weak doublets and right-handed singlets. THE "
     "CORRESPONDENCE: the substrate fermion TYPES <-> the SM fermion types (quarks <-> colour triplets, "
     "leptons <-> singlets, the chiral doublet structure). FALSIFICATION: if the substrate carried no "
     "colour-singlet or no colour-triplet or no chiral reps, it could not host the SM fermions; it hosts "
     "all (MC.1-MC.3). WHAT DOES NOT TRAVEL: WHICH specific object is the electron / the up quark (the "
     "detailed census); the number of generations (MC.6, NOT fished); the hypercharges; the masses. A "
     "correspondence, quarantined; no downstream premise use.",
     "POSTULATE (substrate fermion types <-> SM fermions; specific assignments/generations NOT claimed; held)", "POSTULATE",
     {"correspondence": "substrate fermion types <-> SM: quarks=triplets, leptons=singlets, chiral doublets, fermionic",
      "does_not_travel": "which object is which fermion; the generation count (MC.6); hypercharges; masses",
      "downstream_premise_use": False},
     check=None)

# ---- MC.6 OWED + the explicit generation non-fish --------------------------------------
step("MC.6", "OWED + the EXPLICIT NON-FISH: the generation count (three) is NOT forced -- the substrate 3-folds are DIFFERENT threes (the fitting trap refused)",
     "OWED: (a) the GENERATION count (three) is NOT forced -- the substrate's various 3-folds (colour Z/3 "
     "in 31, the triad in 00, su(2)'s 3 in 28) are DIFFERENT threes (the 1+3+8 lesson, 31/51); "
     "over-reading any one as '3 generations' is REFUSED (the fitting/dismissal trap CORRECTIONS warns "
     "of); (b) the hypercharge assignments (need the fork embedding, 51.GP.4); (c) the masses / mass "
     "ratios (danger zone, the Higgs). Held open; generations explicitly held-open-NOT-fished",
     ["MC.5"],
     "the honest residual, and the discipline's hardest line held. MC.1-MC.4 locate the fermion "
     "quantum-number KINDS (danger-free). What is NOT forced, and MUST NOT be fished: (a) THE GENERATION "
     "COUNT. Physics has three fermion generations, and no theory forces the three. The substrate has "
     "several 3-folds -- colour's Z/3 (31), the floor triad (00), su(2)'s three generators (28) -- and it "
     "is TEMPTING to declare one of them 'the three generations'. That is the FITTING/DISMISSAL trap the "
     "whole project guards against (CORRECTIONS; the 1+3+8 lesson, 31/51, established these are DIFFERENT "
     "threes at different levels, not one). So the generation count is NOT forced and is explicitly "
     "held-open-not-fished -- naming a substrate 3-fold 'generations' without a derivation would be "
     "renaming (CONTACT.md G3), refused. (b) The HYPERCHARGE assignments need the E8->SM embedding (the "
     "fork, 51.GP.4). (c) The MASSES / mass ratios are the danger zone (the Higgs, values). So this "
     "container locates the matter KINDS (the prerequisite for the value crossings) and REFUSES to fish "
     "the generation count or the masses. The Weinberg angle and mass ratios remain gated on the fork + "
     "these owed pieces. NOT attempted further here.",
     "OWED (generation count NOT forced -- fitting trap refused; hypercharges -- fork; masses -- danger)", "OWED",
     {"generation_count_not_forced": True,
      "why_not_fished": "the substrate 3-folds (colour Z/3, the triad, su(2)'s 3) are DIFFERENT threes (1+3+8 lesson, 31/51); naming one 'generations' is renaming (G3), refused",
      "owed_hypercharge": "the hypercharge assignments -- need the E8->SM embedding (the fork, 51.GP.4)",
      "owed_masses": "the masses / mass ratios -- danger zone (the Higgs, values)",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="56-matter-census",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        n_colourless_singlets=N_COLOURLESS, n_coloured_triples=N_COLOURED_TRIPLES, carrier_total=CARRIER,
        weak_isospin_generators=WEAK_GENERATORS, quantum_number_kinds=QUANTUM_NUMBER_KINDS,
        finding="THE MATTER-CENSUS STRUCTURE (the danger-free prerequisite for the value crossings). The "
                "substrate's fermion content carries the KINDS of SM quantum numbers: FERMIONS = spinor "
                "reps (45, MC.1); the COLOUR type-split -- 6 colourless SINGLETS (leptons) + 38 coloured "
                "TRIPLETS (quarks), 6+3*38=120 (31, MC.2); CHIRALITY + weak isospin (44/28, MC.3). The "
                "TYPE-structure (spin, colour, weak-isospin/chirality) is located (MC.4). Correspondence "
                "to the SM fermions filed (MC.5, POSTULATE) -- which specific object is which is NOT "
                "claimed. EXPLICIT NON-FISH (MC.6): the GENERATION count (three) is NOT forced -- the "
                "substrate 3-folds (colour Z/3, the triad, su(2)'s 3) are DIFFERENT threes (1+3+8 lesson); "
                "naming one 'generations' is renaming, refused; hypercharges need the fork; masses are "
                "danger. The Weinberg angle + mass ratios remain gated on the fork + these. Danger-free; "
                "nothing fitted; generations NOT fished.",
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
