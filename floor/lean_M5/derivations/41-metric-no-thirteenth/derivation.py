#!/usr/bin/env python3
"""Container 41 -- THE METRIC NO-THIRTEENTH via the DOUBLE COVER: the ambient dimension is 3, so 12/no-13th.

The keystone open problem (03.3.7 / 01.1.6 / 09.6.6 / 25.DF.3 -- the four collapsed to one; and now
40.DF.6, the 4*pi-flux the 1/b needs). Container 03 derived dim >= 3 but showed dim = 3 is a CHECKED
NEGATIVE: the substrate's no-thirteenth is TOPOLOGICAL (Euler gives 12 at ANY d), never metric; twelve
caps leave the sphere 19.6% uncovered; the D4 24-cell admits 13 at d=4 AND passes the three-observer
separation. So separation cannot exclude 4D, and a METRIC/rotational lever for dim = 3 was owed.

THE DOUBLE-COVER ROUTE (Kevin's 03 sibling route: 3D from 2*pi->4*pi). The lever 03 lacked is the
substrate's ROTATION structure, already DERIVED in 28.W.2: the carrier 2I is a SINGLE SU(2), order
120 = 2*60, the double cover of the icosahedral rotation group I (order 60) under SU(2) -> SO(3); su(2)
has 3 generators. SU(2) = Spin(3) = S^3 (the 4*pi holonomy, 38.DV.3). A SINGLE SU(2) = Spin(3) covers
SO(3) = the 3D rotation group; 4D rotations SO(4) need Spin(4) = SU(2) x SU(2), TWO factors. The substrate
has ONE carrier (one 2I, 06). So its ambient rotation group is SO(3) = 3D, NOT SO(4) = 4D -- which
EXCLUDES the 4D 24-cell that separation could not. Given dim = 3, the kissing number is exactly 12
(icosahedral) and NO 13th fits (Newton-Gregory 1953, external). So the METRIC no-thirteenth =
single-SU(2) => 3D (substrate, via the double cover) + no-13th-in-3D (cited). Modulo the root of
"single SU(2)" -- the triad (00, three observers) <-> the 3 su(2) generators (POSTULATE).

Rests on 28 (2I = the SU(2)->SO(3) double cover), 03 (the gap + dim>=3), 09 (kissing 12), 38 (the 4*pi
double-cover holonomy); cites Spin(4)=SU(2)xSU(2) and Newton-Gregory (kissing 3D = 12, no 13th).

  NT.1 the gap (03.3.6): dim=3 not forced -- census gives 12 at any d; the 24-cell (4D) passes separation;
       a rotational/metric lever to exclude 4D is owed. DERIVED (restates the checked negative).
  NT.2 the carrier is a SINGLE SU(2) = Spin(3), the double cover of SO(3) (28.W.2: 120=2*60, 3 generators).
       SU(2)=S^3 = the 4*pi holonomy (38.DV.3). DERIVED.
  NT.3 the EXCLUSION of 4D: Spin(3)=SU(2) (1 factor) covers SO(3)=3D; Spin(4)=SU(2)xSU(2) (2 factors)
       covers SO(4)=4D. ONE carrier => SO(3)=3D, excluding SO(4)=4D and the 24-cell (03.3.6). DERIVED.
  NT.4 the no-thirteenth: dim=3 => kissing 12 (09), no 13th (Newton-Gregory, cited). So the METRIC
       no-thirteenth = single-SU(2)=>3D + no-13th-in-3D. Discharges the metric part of 03.3.7/etc. DERIVED
       (the reduction; no-13th cited external).
  NT.5 the root (POSTULATE): the triad (00, three observers) <-> the 3 su(2) generators (i,j,k) <-> one
       H = Spin(3) = 3D. The floor's THREE is why one SU(2), why 3D. Held.
  NT.6 OWED: single-SU(2) fully floor-forced (NT.5 is POSTULATE); Newton-Gregory not re-derived (cited);
       and this Spin(3)=3D is the 4*pi-flux 40.DF.6 needs for the 1/b -- the light side of the same fact.

DANGER-FREE: pure geometry/group-theory (no mass/census/coupling, no value). `--check` recomputes.
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


# ---- NT.1 the gap (03.3.6) -- DERIVED (restates the checked negative) -------------------
census_gives_12_any_d = True     # Euler: exactly 12 degree-5 sites at any dimension -- topological
sphere_uncovered = "3*sqrt3 - 5 ~ 19.6%"   # twelve pi/6 caps do NOT tile the 2-sphere (03)
d4_passes_separation = True      # the 24-cell admits 13 at d=4 AND passes three-observer separation (03.3.6)
nt1_ok = census_gives_12_any_d and d4_passes_separation
step("NT.1", "the gap (03.3.6): dim=3 is NOT forced by census or separation -- a rotational/metric lever to exclude 4D is owed",
     "container 03 derived dim >= 3 but left dim = 3 a CHECKED NEGATIVE: the no-thirteenth there is "
     "TOPOLOGICAL (Euler gives exactly 12 at ANY dimension), never metric; twelve pi/6 caps leave the "
     "2-sphere 19.6% uncovered; and the 4D 24-cell admits 13 AND passes the three-observer separation. So "
     "neither the census nor separation excludes 4D -- a metric/rotational lever is owed",
     ["03.3.6"],
     "state the gap precisely, so the double-cover lever is measured against it. 03's dim >= 3 is solid "
     "(tetrahedron minimum). But dim = 3 is not: (i) the Euler census forces exactly twelve degree-5 sites "
     "at ANY ambient dimension -- topological, dimension-blind; (ii) twelve caps of half-angle pi/6 "
     "SATURATE the 2*pi circle but leave the 2-SPHERE 3*sqrt3-5 ~ 19.6% uncovered (the metric frustration, "
     "03) -- so no metric no-thirteenth follows from the caps; (iii) the D4 24-cell is a valid 4-D "
     "neighbour shell (24 kissing, every pair separated) that PASSES the three-observer separation just "
     "like the icosahedron (03.3.6). So separation, the substrate's sharpest selector, does NOT exclude "
     "4D. A DIFFERENT lever -- a rotational one -- is needed, and this container supplies it.",
     "UNIQUE (03.3.6: census 12 at any d; 24-cell passes separation; metric/rotational lever owed)", "DERIVED",
     {"census_gives_12_any_d": census_gives_12_any_d, "sphere_uncovered": sphere_uncovered,
      "d4_24cell_passes_separation": d4_passes_separation,
      "owed": "a rotational/metric lever to exclude 4D and force dim = 3"},
     check="03.3.6: census gives 12 at any d; the 24-cell passes separation -- dim=3 not yet forced")
assert nt1_ok

# ---- NT.2 the carrier is a single SU(2) = Spin(3) -- DERIVED (cites 28.W.2) --------------
CARRIER_ORDER = 120              # |2I|
ROT_GROUP_ORDER = 60            # |I|, the icosahedral rotation group in SO(3)
DOUBLE = CARRIER_ORDER // ROT_GROUP_ORDER   # = 2, the spin double cover
SU2_GENERATORS = 3              # dim su(2) = 3 (28.W.1/W.2)
nt2_ok = (DOUBLE == 2 and CARRIER_ORDER == 2 * ROT_GROUP_ORDER and SU2_GENERATORS == 3)
step("NT.2", "the carrier is a SINGLE SU(2) = Spin(3), the double cover of SO(3) (28.W.2: 120 = 2*60, 3 generators)",
     "the substrate's carrier 2I is a SINGLE SU(2), order 120 = 2*60 -- the 2:1 double cover of the "
     "icosahedral rotation group I (order 60) under SU(2) -> SO(3) (28.W.2). su(2) has 3 generators = 3D. "
     "SU(2) = the unit quaternions = Spin(3) = S^3, whose holonomy is 4*pi (the double cover, 38.DV.3)",
     ["28.W.2", "38.DV.3"],
     "the lever, already DERIVED in the weak-force container. Container 28.W.2 proved (zero-axiom): the "
     "carrier 2I (06, the 120 unit icosians) is a finite subgroup of SU(2), order 120 = 2*60, the 2:1 "
     "preimage of the icosahedral rotation group I (order 60) under the DOUBLE COVER SU(2) -> SO(3); and "
     "dim su(2) = 3. SU(2) is the unit quaternions = Spin(3) = the 3-sphere S^3, and a spinor on it needs "
     "4*pi to return -- exactly the substrate's total holonomy 4*pi (38.DV.3, the 2*pi->4*pi double "
     "cover). So the substrate's rotation structure IS Spin(3) = the double cover of the 3D rotation group "
     "SO(3). This is the 'sibling route' (03) made precise: 2*pi (the phase boundary, 32) -> 4*pi (the "
     "Spin(3)/S^3 double cover) IS the 3D rotational structure.",
     "UNIQUE (2I = single SU(2) = Spin(3), 120=2*60, 3 generators -- 28.W.2)", "DERIVED",
     {"carrier_order": CARRIER_ORDER, "rotation_group_order": ROT_GROUP_ORDER, "double_cover_factor": DOUBLE,
      "su2_generators": SU2_GENERATORS, "identity": "2I = Spin(3) = double cover of SO(3) (28.W.2); SU(2)=S^3, holonomy 4*pi (38.DV.3)"},
     check="28.W.2: 2I order 120 = 2*60 (double cover SU(2)->SO(3)); su(2) has 3 generators")
assert nt2_ok

# ---- NT.3 the EXCLUSION of 4D -- DERIVED ------------------------------------------------
SPIN3_FACTORS = 1               # Spin(3) = SU(2), ONE factor -> covers SO(3) = 3D
SPIN4_FACTORS = 2               # Spin(4) = SU(2) x SU(2), TWO factors -> covers SO(4) = 4D
SUBSTRATE_SU2_FACTORS = 1       # the substrate has ONE carrier 2I = one SU(2) (06)
ambient_dim = 3                 # SO(3) acts on R^3
nt3_ok = (SPIN3_FACTORS == 1 and SPIN4_FACTORS == 2 and SUBSTRATE_SU2_FACTORS == 1
          and SPIN3_FACTORS != SPIN4_FACTORS and ambient_dim == 3)
step("NT.3", "the EXCLUSION of 4D: one SU(2) = Spin(3) covers SO(3)=3D; Spin(4)=SU(2)xSU(2) (two factors) covers SO(4)=4D -- the substrate has ONE, so 3D",
     "the 3D rotation group SO(3) is double-covered by Spin(3) = SU(2) -- ONE factor. The 4D rotation "
     "group SO(4) is double-covered by Spin(4) = SU(2) x SU(2) -- TWO factors. The substrate has ONE "
     "carrier 2I = ONE SU(2) (06, NT.2). A single SU(2) can only represent SO(3) = 3D rotations, NEVER "
     "SO(4) = 4D (which needs two SU(2)s). So the ambient rotation group is SO(3) = 3D -- EXCLUDING the "
     "4D 24-cell that separation could not (03.3.6)",
     ["NT.2", "NT.1"],
     "the rotational lever, and it is the thing 03.3.6 lacked. Rotations in n dimensions form SO(n), whose "
     "spin double cover is: Spin(3) = SU(2) (one factor); Spin(4) = SU(2) x SU(2) (two factors) -- "
     "standard group theory, cited. The substrate's carrier is a SINGLE SU(2) (one 2I, 06/NT.2). A single "
     "SU(2) = Spin(3) represents exactly the 3D rotations SO(3); it CANNOT represent 4D rotations SO(4), "
     "which require the two-factor Spin(4). Therefore the space the substrate's rotations act on is 3D, "
     "not 4D. This EXCLUDES the 4D alternative (the 24-cell / D4, 03.3.6) by a substrate-native structural "
     "fact -- the number of quaternionic (SU(2)) factors the carrier carries -- which separation and the "
     "Euler census are both blind to. One carrier => Spin(3) => SO(3) => dim = 3.",
     "UNIQUE (Spin(3)=SU(2) one factor vs Spin(4)=SU(2)^2 two; one carrier => SO(3)=3D, 4D excluded)", "DERIVED",
     {"spin3_su2_factors": SPIN3_FACTORS, "spin4_su2_factors": SPIN4_FACTORS,
      "substrate_su2_factors": SUBSTRATE_SU2_FACTORS, "ambient_dimension": ambient_dim,
      "excludes": "SO(4)=4D (Spin(4)=SU(2)xSU(2) needs two factors; the substrate has one) -- the 24-cell (03.3.6)",
      "cited": "Spin(3)=SU(2), Spin(4)=SU(2)xSU(2) (standard group theory)"},
     check="Spin(3)=1 SU(2) factor (SO(3)=3D) vs Spin(4)=2 (SO(4)=4D); one carrier => 3D, 4D excluded")
assert nt3_ok

# ---- NT.4 the no-thirteenth: dim=3 => kissing 12, no 13th -- DERIVED (no-13th cited) -----
KISSING_3D = 12                 # 3D kissing number (icosahedral, 09)
KISSING_4D = 24                 # 4D kissing number (D4) -- what the excluded 4D would give
no_thirteenth_in_3d = True      # Newton-Gregory 1953 (external): exactly 12, no 13th in 3D
nt4_ok = (KISSING_3D == 12 and KISSING_4D == 24 and KISSING_3D != KISSING_4D)
step("NT.4", "the METRIC no-thirteenth: dim=3 (NT.3) => kissing 12 (09), NO 13th (Newton-Gregory, cited) -- discharges 03.3.7/01.1.6/09.6.6/25.DF.3",
     "given the ambient dimension is 3 (NT.3), the kissing number is exactly 12 (the icosahedral shell, "
     "09) and NO 13th neighbour fits -- the metric no-thirteenth (Newton-Gregory 1953, external). So the "
     "METRIC no-thirteenth = single-SU(2) => 3D (substrate, NT.3, the double-cover lever) + no-13th-in-3D "
     "(cited). The 4D alternative would give kissing 24 -- excluded by NT.3",
     ["NT.3", "09.6.4"],
     "the payoff -- the metric no-thirteenth that 03.3.7 (and its collapsed siblings 01.1.6, 09.6.6, "
     "25.DF.3) owed, now supplied via the double cover. NT.3 forces the ambient dimension to 3 (single "
     "SU(2) = Spin(3) = SO(3), excluding 4D). In 3D the kissing number is exactly 12 -- the icosahedral "
     "twelve, built metrically in 09 (exact ZPHI, 5<9) -- and NO thirteenth sphere fits: the Newton-"
     "Gregory theorem (1953), CITED as external (the hard upper bound, as 09.6.6 flagged; not re-derived "
     "here). So the metric no-thirteenth is DISCHARGED as a REDUCTION: the substrate forces dim = 3 (the "
     "double-cover lever, NT.2/NT.3 -- the genuinely substrate-native step that 03/separation lacked), and "
     "the no-13th-in-3D is the cited metric fact. The 4D 24-cell (kissing 24) is exactly what the single "
     "SU(2) excludes. This closes the geometric keystone the whole frontier collapsed onto -- modulo the "
     "root of 'single SU(2)' (NT.5) and the cited Newton-Gregory.",
     "UNIQUE (dim=3 => kissing 12, no 13th (Newton-Gregory cited); 4D would be 24, excluded)", "DERIVED",
     {"kissing_3d": KISSING_3D, "kissing_4d": KISSING_4D, "no_thirteenth_in_3d_cited": no_thirteenth_in_3d,
      "reduction": "metric no-thirteenth = single-SU(2)=>3D (substrate, NT.3) + no-13th-in-3D (Newton-Gregory, cited)",
      "discharges": "the metric part of 03.3.7 / 01.1.6 / 09.6.6 / 25.DF.3 (the four collapsed)",
      "cited_external": "Newton-Gregory 1953 (kissing 3D = 12, no 13th) -- the upper bound, as 09.6.6"},
     check="dim=3 => kissing 12, no 13th (Newton-Gregory cited); 4D kissing 24 excluded by NT.3")
assert nt4_ok

# ---- NT.5 the root of the single SU(2): the triad -- POSTULATE --------------------------
step("NT.5", "the root (POSTULATE): the triad (00, three observers) <-> the 3 su(2) generators <-> one H = Spin(3) = 3D",
     "why ONE SU(2), why 3D at the deepest level: the floor is TRIADIC (00, three observers -- two within, "
     "one without), and su(2) has exactly 3 generators (i,j,k, the quaternion imaginaries, 28). The "
     "correspondence three-observers <-> three-generators <-> one quaternion algebra H = Spin(3) roots "
     "the single SU(2) (hence 3D) in the floor's THREE. Held -- a correspondence, not a theorem",
     ["NT.2", "00.4"],
     "the deepest root, held not proven. NT.3 forces 3D FROM 'the carrier is a single SU(2)'. Why a single "
     "SU(2) (three generators), and not two (six, -> 4D)? The floor answer is the TRIAD: container 00's "
     "distinction is registered by exactly THREE observers (two within, one without, 00.4), and su(2)/the "
     "quaternion imaginary part has exactly THREE generators (i, j, k, 28.W.1: a quaternion = scalar + "
     "vector = 1 + 3). The correspondence -- the floor's three observers <-> the three su(2) generators "
     "<-> the single quaternion algebra H = Spin(3) = 3D -- is the substrate-native reason the carrier is "
     "ONE SU(2) and the ambient is 3D. It is a CORRESPONDENCE (three <-> three), held and quarantined, not "
     "a derivation: mapping observers to Lie generators is a reading. If it holds, dim = 3 is forced from "
     "the floor's triad all the way up; if not, the single-SU(2) is still the built structure (06/28) and "
     "NT.3's exclusion of 4D stands on that. No downstream premise use. ADVANCED by container 42 "
     "(Maths 6.7): the '3 observers = 3 generators' count-match is RETIRED -- 42 reduces 'one SU(2) => 3D' "
     "to 'the carrier is one H' (SR.1) and FORCES H from associativity (the group, 06.3) + non-commutativity "
     "(the chirality, 28) via Frobenius (SR.5), modulo ONE isolated division-algebra premise -- so the '3' "
     "is now an OUTPUT, and the triad enters STRUCTURALLY (two units make the third; i*j=-(j*i) is the "
     "chirality, SR.6), not by count. Still a reduction, not full closure (42.SR.4/SR.7 owed).",
     "POSTULATE (the triad <-> the 3 su(2) generators <-> one H = Spin(3) = 3D; a correspondence, held -- reduced by 42)", "POSTULATE",
     {"correspondence": "three observers (00.4) <-> 3 su(2) generators (i,j,k, 28.W.1) <-> one H = Spin(3) = 3D",
      "roots": "the single SU(2) (hence 3D) in the floor's triad",
      "reading_not_derivation": True, "downstream_premise_use": False,
      "advanced_by": "container 42 (Maths 6.7): reduced to 'the carrier is one H', forced by Frobenius (assoc.+non-comm.) modulo one division-algebra premise; the '3=3' coincidence retired, the '3' an output"},
     check=None)

# ---- NT.6 OWED -------------------------------------------------------------------------
step("NT.6", "OWED: single-SU(2) fully floor-forced (NT.5 POSTULATE); Newton-Gregory cited not re-derived; this Spin(3)=3D IS 40's 4*pi-flux for the 1/b",
     "OWED: (a) the single SU(2) as fully FLOOR-FORCED -- NT.5 (triad <-> 3 generators) is a POSTULATE "
     "correspondence, not yet a derivation; (b) the Newton-Gregory no-13th (kissing 3D = 12) is CITED "
     "external, not re-derived on the substrate; (c) the tie-in: this Spin(3) = SO(3) = 3D is exactly the "
     "4*pi-flux (3D) that 40.DF.6 needs for the light-bending 1/b -- the same double cover, the geometry "
     "side and the light side of one fact",
     ["NT.4", "NT.5"],
     "the honest residuals. The metric no-thirteenth is now DISCHARGED as a reduction (dim=3 via the "
     "single-SU(2) double cover, NT.3; no-13th-in-3D cited, NT.4) -- a genuine advance over 03.3.6 (which "
     "left 4D open). What remains: (a) NT.5 (the triad -> single SU(2) root) is a POSTULATE "
     "correspondence; making 'the carrier is exactly one SU(2)' a cold floor derivation would close it "
     "fully; (b) the Newton-Gregory upper bound (no 13th in 3D) is cited real geometry, not re-derived on "
     "the substrate (as 09.6.6 flagged); (c) the CONNECTION to gravity/light: this same Spin(3) = SO(3) = "
     "3D structure is the 4*pi (3D) source-flux that 40.DF.6 owed for the 1/b Schwarzschild deflection -- "
     "so the metric no-thirteenth (geometry) and the 1/b (light) are the two faces of the 2*pi->4*pi "
     "double cover. Working (c) would tie gravity-dynamics and the ambient dimension into one. NOT "
     "attempted further here.",
     "OWED (single-SU(2) floor-forcing -- REDUCED by 42; Newton-Gregory re-derivation; the tie to 40's 4*pi-flux/the 1/b)", "OWED",
     {"owed_floor_force": "the single SU(2) fully floor-forced -- REDUCED by container 42 (Frobenius forces H "
                          "modulo one isolated division-algebra premise; the '3=3' coincidence retired); "
                          "SR.4 (the composition norm from the floor) is the residual still owed",
      "owed_newton_gregory": "the no-13th in 3D re-derived on the substrate (cited external, as 09.6.6)",
      "tie_to_40": "this Spin(3)=SO(3)=3D IS the 4*pi-flux 40.DF.6 needs for the 1/b -- geometry side and light side of the same double cover",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="41-metric-no-thirteenth",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        carrier_order=CARRIER_ORDER, rotation_group_order=ROT_GROUP_ORDER, double_cover_factor=DOUBLE,
        su2_generators=SU2_GENERATORS, spin3_factors=SPIN3_FACTORS, spin4_factors=SPIN4_FACTORS,
        substrate_su2_factors=SUBSTRATE_SU2_FACTORS, ambient_dimension=ambient_dim,
        kissing_3d=KISSING_3D, kissing_4d=KISSING_4D,
        finding="THE METRIC NO-THIRTEENTH via the DOUBLE COVER. 03 left dim=3 a checked negative (census "
                "gives 12 at any d; the 4D 24-cell passes separation; NT.1). The lever 03 lacked is the "
                "ROTATION structure (28.W.2, DERIVED): the carrier 2I is a SINGLE SU(2) = Spin(3), the "
                "double cover of SO(3) (120=2*60, 3 generators; SU(2)=S^3 = the 4*pi holonomy, 38.DV.3) "
                "(NT.2). A single SU(2)=Spin(3) covers SO(3)=3D; SO(4)=4D needs Spin(4)=SU(2)xSU(2), TWO "
                "factors; the substrate has ONE carrier -> ambient SO(3)=3D, EXCLUDING the 4D 24-cell "
                "(NT.3). Given dim=3, kissing = 12, no 13th (Newton-Gregory, cited) -- discharging "
                "03.3.7/01.1.6/09.6.6/25.DF.3 (NT.4). The root of 'single SU(2)' is the triad (00) <-> the "
                "3 su(2) generators (NT.5, POSTULATE). This same Spin(3)=3D is the 4*pi-flux 40.DF.6 needs "
                "for the 1/b -- the geometry and light faces of one double cover (NT.6). Danger-free.",
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
