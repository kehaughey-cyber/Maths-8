#!/usr/bin/env python3
"""Container 27 -- DIMENSIONAL ACCOUNTING: how much of alpha's value is irreducibly external?
Rests on 13/23/26 (the substrate's dimensionless quantities) and cites 17/18 (the Stones, where the
dimensionful constants enter). Physics-bridge / alpha-value plan Path B, Step 1 (Kevin's decision,
Maths 6.5): the honest, de-risking first move of Path B -- account for where UNITS enter before touching
any census number.

Path B was 'derive hbar/c/G/mass from the substrate'. Read literally that is a CATEGORY error, and the
project already hit it: the substrate is DIMENSIONLESS (counts + angles, exact Q(sqrt5)); hbar/c/G are
DIMENSIONFUL; a dimensionless substrate cannot emit a dimensionful number without an external anchor.
maths-4 established the same thing physically ('the substrate's coupling is UNITY... alpha must enter
where the substrate meets MEASUREMENT'). So this container makes that wall a FIRST-CLASS CHECKED RESULT,
and turns 'alpha may be irreducibly external' from a hand-wave into a derived structural finding:

  DA.1 (DERIVED): the substrate is DIMENSIONLESS. Every quantity the tower computes -- ball growth |B_r|
       (13), the archon count L (23), degrees / Euler chi / the 240 / the 12, radits and deficits (14/16),
       BC=2pi/ln2 (17, already a pure number), the base-2 alphabet (26) -- is a COUNT or a dimensionless
       RATIO. No length, time, mass, or energy is native. (Represent a dimension as an integer triple of
       (L,T,M) exponents; the substrate quantities all carry (0,0,0).)

  DA.2 (DERIVED): {hbar, c, G} is a DIMENSIONAL BASIS. Their (L,T,M) exponent matrix has determinant 2
       (!= 0), so the three span the whole dimension space -- ANY dimensionful quantity's units are a
       unique (rational-exponent) monomial in hbar,c,G. This is exactly why Planck units are well-defined.
       Consequence: EXACTLY THREE dimensionful anchors fix ALL units, and a dimensionless substrate
       supplies NONE of them, so >= 3 dimensionful inputs are IRREDUCIBLY EXTERNAL. The headline.

  DA.3 (DERIVED): the per-archon alpha FACTORIZES as alpha = alpha_hat (dimensionless) x (Planck-unit
       anchor monomial). The source reads alpha two ways -- 'energy per archon' (Stone 17) with dimension
       (2,-2,1)=energy, and the 'edge' in c=alpha/tau (Kevin's Planck hypothesis) with dimension
       (1,0,0)=length. These are DIMENSIONALLY DISTINCT (so 'alpha' names two objects), but COMPTON-DUAL:
       their product carries dimension (3,-2,1) = that of hbar*c, i.e. E*R=hbar*c -- exactly Stone 17's
       cold algebra. Each reading's units ARE a Planck monomial (2*energy = hbar+5c-G = Planck energy;
       2*length = hbar+G-3c = Planck length). So alpha's ABSOLUTE value carries units and needs the
       anchor; only the dimensionless alpha_hat is the substrate's to force.

  DA.4 (OWED): forcing alpha_hat (the dimensionless part) is the FORWARD Path B work -- the transfer rule
       at F2 (the packing frustration = container 16's eps=7.356deg, maths-4's 'first quantity with SLACK,
       unpinned'), computed-then-compared NEVER fitted, respecting maths-4's REFUSED-LIST (1/144, 1/12,
       24, 20, 2^7 -- 'a session that finds these promising has failed'). The reading-disambiguation
       (energy vs length alpha) awaits the Planck hypothesis (18.P.3) / SEC9. The three Planck anchors are
       the located irreducible external input.

This introduces NO specific dimensionless value (no 137, no 864), touches NO census, derives NO mass -- it
is pure dimensional bookkeeping (the Buckingham-Pi accounting), the honest ledger of what Path B can and
cannot buy. Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
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


# ================================================================ dimension algebra (L, T, M) exponents
def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def smul(k, a):
    return (k * a[0], k * a[1], k * a[2])


def det3(r1, r2, r3):
    """Determinant of the 3x3 matrix whose rows are the three (L,T,M) exponent triples."""
    return (r1[0] * (r2[1] * r3[2] - r2[2] * r3[1])
            - r1[1] * (r2[0] * r3[2] - r2[2] * r3[0])
            + r1[2] * (r2[0] * r3[1] - r2[1] * r3[0]))


ZERO = (0, 0, 0)
# The three base anchors, (L, T, M) exponents:
HBAR = (2, -1, 1)    # action = energy*time = M L^2 T^-1
CLIGHT = (1, -1, 0)  # speed = L T^-1
GNEWTON = (3, -2, -1)  # G: L^3 M^-1 T^-2

# ---- DA.1 the substrate is dimensionless -- DERIVED ------------------------------------
# Every quantity the tower computes is a count or a dimensionless ratio: it carries dimension (0,0,0).
# Represented here by tagging the tower's paradigmatic outputs; NONE has length/time/mass/energy.
SUBSTRATE_QUANTITIES = {
    "ball_growth_|B_r|_(13)": ZERO,
    "archon_count_L_(23)": ZERO,
    "degree_/_Euler_chi_/_240_/_12": ZERO,
    "radits_/_deficits_(14/16)": ZERO,
    "BC=2pi/ln2_(17)": ZERO,
    "base-2_alphabet_(26)": ZERO,
}
substrate_all_dimensionless = all(d == ZERO for d in SUBSTRATE_QUANTITIES.values())
step("DA.1", "the substrate is DIMENSIONLESS -- every tower quantity carries dimension (0,0,0)",
     "every quantity the tower computes (|B_r| 13, archon count L 23, degree/chi/240/12, radits/deficits "
     "14/16, BC=2pi/ln2 17, the base-2 alphabet 26) is a COUNT or a dimensionless RATIO -- (L,T,M) "
     "exponents (0,0,0); no length, time, mass, or energy is native",
     ["13.A.2", "23.LI.2", "26.B2.1"],
     "the floor of the accounting, and it is a census of the whole tower. A 'dimension' is a vector of "
     "exponents over the base units -- here (L,T,M) for length, time, mass; a quantity is DIMENSIONLESS "
     "when that vector is (0,0,0). Run down what the substrate actually produces: ball-growth counts "
     "|B_r| (13), the archon count L=|A(d)| (23), vertex degrees and the Euler characteristic and the "
     "240 and the 12, angle radits and deficits (14/16), the pure number BC=2pi/ln2 (17), the base-2 "
     "alphabet size (26). Every one is a COUNT (an integer) or a dimensionless RATIO of counts/angles. "
     "NONE carries a length, a time, a mass, or an energy -- there is no metre, second, kilogram, or "
     "joule anywhere in the substrate; the geometry is relational and exact-arithmetic (Q(sqrt5)), never "
     "metric-with-units. So the substrate lives entirely at dimension (0,0,0). This is not a limitation "
     "to apologise for; it is the precise fact that makes DA.2's accounting exact.",
     "UNIQUE (the substrate's quantities are counts/ratios; their (L,T,M) dimension is (0,0,0))", "DERIVED",
     {"substrate_quantities": {k: list(v) for k, v in SUBSTRATE_QUANTITIES.items()},
      "all_dimensionless": substrate_all_dimensionless,
      "base_dimensions": "(L, T, M) -- length, time, mass",
      "no_native_units": "no metre/second/kilogram/joule; relational, exact Q(sqrt5), never metric-with-units"},
     check="every tower quantity (|B_r|,L,chi,radits,BC,alphabet) has (L,T,M) dimension (0,0,0) -- dimensionless")
assert substrate_all_dimensionless

# ---- DA.2 {hbar, c, G} is a dimensional basis (det=2) -- DERIVED ------------------------
# The 3x3 matrix of (L,T,M) exponents for hbar, c, G has determinant 2 != 0, so the three are linearly
# independent and SPAN the dimension space: any dimensionful quantity's units are a unique monomial in
# them (why Planck units exist). So exactly THREE dimensionful anchors fix ALL units; the dimensionless
# substrate supplies none, so >= 3 dimensionful inputs are IRREDUCIBLY EXTERNAL.
anchor_det = det3(HBAR, CLIGHT, GNEWTON)              # = 2
anchors_independent = (anchor_det != 0)
DIM_RANK = 3                                          # rank of (L, T, M)
step("DA.2", "{hbar, c, G} is a DIMENSIONAL BASIS (det=2 != 0) -- exactly 3 anchors are irreducibly external",
     "the (L,T,M) exponent matrix of {hbar=(2,-1,1), c=(1,-1,0), G=(3,-2,-1)} has determinant 2 != 0, so "
     "the three SPAN the dimension space -- any dimensionful quantity's units are a unique monomial in "
     "hbar,c,G (Planck units). So exactly 3 dimensionful anchors fix ALL units; a dimensionless substrate "
     "supplies none -> >= 3 dimensionful inputs are IRREDUCIBLY EXTERNAL",
     ["DA.1"],
     "the headline, and it is what makes Path B honest instead of a category error. Path B asked to "
     "'derive hbar/c/G'. But dimension space (L,T,M) is a 3-dimensional vector space over the exponents, "
     "and {hbar, c, G} is a BASIS for it: their exponent matrix "
     "[[2,-1,1],[1,-1,0],[3,-2,-1]] has determinant 2, nonzero, so the three are independent and span. "
     "That is precisely why Planck units (l_P, t_P, m_P) exist and are unique -- every physical unit is a "
     "unique monomial hbar^a c^b G^d. Two consequences, both forced. (i) EXACTLY THREE dimensionful "
     "numbers are needed to fix every unit -- no fewer (the rank is 3), no more (three already span). "
     "(ii) The substrate is dimensionless (DA.1), so it supplies NONE of the three: a count times a count "
     "is a count, forever at (0,0,0); you cannot manufacture a metre from integers. Therefore >= 3 "
     "dimensionful inputs are IRREDUCIBLY EXTERNAL to the substrate -- they enter at MEASUREMENT (the "
     "Stones 17/18), exactly as maths-4 found ('the substrate's coupling is unity; alpha must enter where "
     "the substrate meets measurement'). This is not defeat: it is an exact ACCOUNTING -- it says how much "
     "is external (three numbers, the Planck scale) and, by DA.1, that everything else is the substrate's "
     "dimensionless business.",
     "UNIQUE (det of the {hbar,c,G} exponent matrix = 2; the three span (L,T,M), rank 3)", "DERIVED",
     {"hbar_dim": list(HBAR), "c_dim": list(CLIGHT), "G_dim": list(GNEWTON),
      "determinant": anchor_det, "anchors_independent": anchors_independent, "dimension_rank": DIM_RANK,
      "exactly_three_anchors": "rank(L,T,M)=3 and {hbar,c,G} realize it (det=2) -> exactly 3 fix all units",
      "irreducibly_external": ">= 3 dimensionful inputs; the dimensionless substrate supplies none",
      "why_planck_units_exist": "a basis for dimension space -> unique monomial hbar^a c^b G^d for any unit"},
     check="det[[2,-1,1],[1,-1,0],[3,-2,-1]] = 2 != 0 -> {hbar,c,G} a dimensional basis; exactly 3 anchors external")
assert anchors_independent and anchor_det == 2

# ---- DA.3 the per-archon alpha factorizes; the two readings are Compton-dual -- DERIVED -
# alpha = alpha_hat (dimensionless) x (Planck-unit anchor). The source reads alpha two ways, dimensionally
# distinct but Compton-dual (their product ~ hbar*c = Stone 17's R*E=hbar*c). Each reading's units are a
# Planck monomial. So alpha's ABSOLUTE value needs the anchor; only alpha_hat is the substrate's to force.
ALPHA_ENERGY = (2, -2, 1)   # 'energy per archon' (Stone 17): M L^2 T^-2
ALPHA_LENGTH = (1, 0, 0)    # the 'edge' in c=alpha/tau (Planck hypothesis 18.P.3): L
HBARC = add(HBAR, CLIGHT)   # dimension of hbar*c = (3,-2,1)
readings_differ = (ALPHA_ENERGY != ALPHA_LENGTH)
compton_dual = (add(ALPHA_ENERGY, ALPHA_LENGTH) == HBARC)          # E*R has hbar*c's dimension (Stone 17)
energy_is_planck_energy = (smul(2, ALPHA_ENERGY) == add(add(HBAR, smul(5, CLIGHT)), smul(-1, GNEWTON)))  # 2E = hbar+5c-G
length_is_planck_length = (smul(2, ALPHA_LENGTH) == add(add(HBAR, GNEWTON), smul(-3, CLIGHT)))            # 2L = hbar+G-3c
da3_ok = readings_differ and compton_dual and energy_is_planck_energy and length_is_planck_length
step("DA.3", "the per-archon alpha FACTORIZES as alpha_hat x (Planck anchor); its two readings are Compton-dual",
     "alpha = alpha_hat (dimensionless) x (Planck-unit anchor); the source reads alpha as 'energy per "
     "archon' (dim (2,-2,1), Stone 17) AND as the 'edge' in c=alpha/tau (dim (1,0,0), 18.P.3) -- "
     "dimensionally DISTINCT but COMPTON-DUAL (their sum = (3,-2,1) = dim(hbar*c), i.e. E*R=hbar*c). Each "
     "reading's units are a Planck monomial (2*energy=hbar+5c-G; 2*length=hbar+G-3c)",
     ["DA.2", "17.S.1"],   # 18.P.3 (Planck hypothesis) is CITED in prose only, NOT a premise -- the
     "the per-archon alpha, put on the ledger -- and it surfaces a conflation the source carries. alpha "
     "is read TWO ways in the corpus: 'energy per archon' (Stone 17, dimension energy (2,-2,1)) and the "
     "registration EDGE in c=alpha/tau (Kevin's Planck hypothesis 18.P.3: c a speed L/T, tau the tick T, "
     "so alpha=c*tau=length (1,0,0)). Those dimension vectors are DIFFERENT, so 'alpha' names two "
     "different objects unless one reading is wrong -- a real overload, exactly the kind the container "
     "discipline exists to catch. RUN IT: are they unrelated, or dual? Their dimensions SUM to (3,-2,1), "
     "which is the dimension of hbar*c -- so (energy alpha)*(length alpha) ~ hbar*c, i.e. E*R=hbar*c, "
     "which is LITERALLY Stone 17's cold algebra (17.S.1). The two readings are COMPTON-DUAL, not "
     "contradictory: the energy-alpha and the length-alpha are Compton conjugates, linked by hbar*c. And "
     "each one's units ARE a Planck monomial: 2*(energy alpha)=hbar+5c-G (the Planck energy sqrt(hbar "
     "c^5/G)), 2*(length alpha)=hbar+G-3c (the Planck length sqrt(hbar G/c^3)) -- both checked as integer "
     "exponent identities (the factor 2 clears the square roots). CONCLUSION: under either reading alpha "
     "= alpha_hat (dimensionless) x (a fixed Planck-unit anchor), so alpha's ABSOLUTE value carries units "
     "and needs the anchor; ONLY the dimensionless alpha_hat is the substrate's to force. The physical "
     "READING (which alpha, and that E*R=hbar*c is the registration boundary) stays Stone-quarantined; "
     "the DIMENSIONAL arithmetic here is what is derived.",
     "UNIQUE (the two alpha readings' dimension vectors, their Compton-dual sum, and their Planck monomials)",
     "DERIVED",
     {"alpha_energy_dim": list(ALPHA_ENERGY), "alpha_length_dim": list(ALPHA_LENGTH),
      "readings_dimensionally_differ": readings_differ,
      "compton_dual_sum_is_hbarc": compton_dual, "hbarc_dim": list(HBARC),
      "energy_reading_is_planck_energy_2E_eq_hbar_5c_minus_G": energy_is_planck_energy,
      "length_reading_is_planck_length_2L_eq_hbar_G_minus_3c": length_is_planck_length,
      "factorization": "alpha = alpha_hat (dimensionless, substrate-forcible) x (Planck-unit anchor)",
      "reading_quarantined": "which alpha, and E*R=hbar*c as the registration boundary, is Stone 17/18's, held"},
     check="alpha readings (2,-2,1)!=(1,0,0) but sum=(3,-2,1)=dim(hbar*c) (Compton dual); each = a Planck monomial")
assert da3_ok

# ---- DA.4 forcing alpha_hat + disambiguating the reading -- OWED (located) --------------
step("DA.4", "forcing the dimensionless alpha_hat is the forward Path B work; the reading awaits Planck/SEC9 (OWED)",
     "alpha's value = alpha_hat (dimensionless) x (3 Planck anchors, irreducibly external, DA.2). Forcing "
     "alpha_hat from the substrate is the FORWARD Path B work -- the transfer rule at F2 (container 16's "
     "eps), computed-then-compared NEVER fitted, respecting maths-4's refused-list; the energy-vs-length "
     "reading awaits the Planck hypothesis (18.P.3) / SEC9. Located, not closed.",
     ["DA.2", "DA.3", "16.D.1"],
     "the residual, located precisely and NOT attempted here -- the honest boundary, and the map for what "
     "Path B does next. The accounting closes the dimensionful question: EXACTLY the three Planck anchors "
     "(hbar, c, G -- equivalently l_P, t_P, m_P) are irreducibly external (DA.2), and alpha's absolute "
     "value = alpha_hat x (a Planck-unit anchor) (DA.3). So the ONLY thing the substrate can, or must, "
     "supply for alpha is the DIMENSIONLESS factor alpha_hat. Forcing alpha_hat is the real forward Path "
     "B work, and the accounting already constrains HOW to look: (i) it must be FORCED, not assembled -- "
     "the 864/standing-lag census 'stays failing' precisely because it was fitted, not forced; (ii) it "
     "must respect maths-4's REFUSED-LIST (1/144, 1/12, 24, 20, 2^7 -- recorded as refused; do not fish "
     "pi/phi/12 near a target); (iii) the one PRINCIPLED opening is F2, the packing frustration = "
     "container 16's eps=7.356deg, maths-4's 'first quantity with SLACK, unpinned', and the owed object "
     "there is the TRANSFER RULE (how a frustration at one level enters the next), NOT composing "
     "frustrations to hit a number. Separately, the energy-vs-length reading of alpha (DA.3) is a "
     "disambiguation that touches the Planck hypothesis (18.P.3, l_P=edge/t_P=tick) and SEC9 (Compton = "
     "registration boundary), both OPEN. So: the irreducible external input is the 3 Planck anchors "
     "(located); alpha_hat and the reading are the forward Path B agenda. NOT attempted here.",
     "OWED (force alpha_hat via the F2 transfer rule; disambiguate the reading via Planck/SEC9; located)",
     "OWED",
     {"present": False,
      "irreducible_external": "exactly the 3 Planck anchors {hbar,c,G} = {l_P,t_P,m_P} (DA.2, det=2)",
      "substrate_must_force": "only the dimensionless alpha_hat (DA.3)",
      "how_constrained": "FORCED not fitted (census 'stays failing' when fitted); respect refused-list (1/144,1/12,24,20,2^7)",
      "principled_opening": "F2 = the packing frustration = container 16's eps=7.356deg (maths-4: first quantity with SLACK, unpinned)",
      "owed_object": "the TRANSFER RULE (how frustration at one level enters the next) -- NOT composing to hit a number",
      "reading_disambiguation": "energy-vs-length alpha awaits the Planck hypothesis (18.P.3) / SEC9 (both OPEN)",
      "not_attempted": True},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="27-dimensional-accounting",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # DA.1
        substrate_all_dimensionless=substrate_all_dimensionless,
        # DA.2 -- guarded by the Lean
        anchor_determinant=anchor_det,
        anchors_independent=anchors_independent,
        dimension_rank=DIM_RANK,
        hbar_dim=list(HBAR), c_dim=list(CLIGHT), G_dim=list(GNEWTON),
        # DA.3 -- guarded by the Lean
        alpha_energy_dim=list(ALPHA_ENERGY), alpha_length_dim=list(ALPHA_LENGTH),
        readings_differ=readings_differ, compton_dual=compton_dual,
        energy_is_planck_energy=energy_is_planck_energy, length_is_planck_length=length_is_planck_length,
        # the accounting
        exactly_three_anchors_external=True,
        substrate_forces_only_alpha_hat=True,
        finding="the substrate is dimensionless (DA.1); {hbar,c,G} is a dimensional basis (det=2), so "
                "EXACTLY 3 dimensionful anchors are irreducibly external (DA.2); the per-archon alpha = "
                "alpha_hat (dimensionless, the substrate's to force) x a Planck anchor, its energy/length "
                "readings Compton-dual via E*R=hbar*c (DA.3); forcing alpha_hat (the F2 transfer rule, "
                "forced-not-fitted, refused-list respected) is the forward Path B work (DA.4). Path B's "
                "honest content: derive the dimensionless alpha_hat; exactly three Planck numbers stay external.",
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
