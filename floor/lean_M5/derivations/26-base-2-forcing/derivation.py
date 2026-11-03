#!/usr/bin/env python3
"""Container 26 -- BASE-2 FORCING: is registration base-2, or is ln2 a convention?
Rests on 00 (the floor's existential states + the distinction); cites 17 (the Stone's ln2),
23/24 (the count L, alpha per archon). Physics-bridge Step 13, and Step 1 of the alpha-value plan.

The question (Stone 17 S.3b/S.4ii, the "Shannon-vs-registration reconciliation"): the Bekenstein
ruler is BC = 2*pi/ln2. Is the ln2 -- the base-2 -- FORCED by the registration substrate, or is it a
units convention (nats->bits) carrying no content beyond 2*pi? This is the danger-FREE opener of the
alpha-value plan: it touches NO mass (Path A / Path B fork does not bite here).

The honest answer is graded, and it is CONDITIONAL:

  - B2.1 DERIVED: the REGISTRABLE ALPHABET is exactly 2. Container 00 has three existential states
    (defined / undefined / non-existent) but non-existence CANNOT be perceived or registered (00.2), and
    a distinction is a positive TWO-valued partition (defined / undefined-existent, 00.3). So the number
    of states a registration can distinguish is 2. Two CHECKED NEGATIVES keep this from being smuggled:
    base-3 is REFUTED (the third state is unregistrable, so the alphabet is 2 not 3), and the triad's
    3 (OBSERVERS, 00.4 -- the machinery that PRODUCES a registration) is TYPED APART from the 2
    (the alphabet of what is registered). "Triadic floor" does NOT mean "base 3".

  - B2.2 DERIVED: the per-registration BRANCHING FACTOR is 2 -- base-2. One registration = one binary
    distinction = one base-2 digit (a bit); a configuration space grows as 2^k (each registration
    doubles it), so the substrate's native count L (containers 23/24) is a BIT-count. Pure arithmetic
    on the alphabet 2; no continuum.

  - B2.3 POSTULATE: the Shannon reconciliation (the READING). GIVEN that registration information =
    distinguishing among registrable configurations (identifying the substrate's count with Shannon's
    H), base-2 is the FORCED information unit and ln2 = log_e(2) gains CONTENT: it is the nat-size of
    one forced registration bit, so BC's "2*pi/ln2" reads "2*pi nats = 2*pi/ln2 registration-bits". The
    compatible, separate fact (physics is right about this): the base of a CONTINUOUS entropy is a free
    convention -- nats or bits, nothing physical changes. Both are true at different levels; the
    substrate has a PREFERRED discrete unit (the bit = one registration) while continuous entropy does
    not. This identification is a correspondence, held POSTULATE, not proven.

  - B2.4 OWED: that the ln2 in the SPECIFIC Bekenstein/Compton ruler (BC=2*pi/ln2) is THIS registration
    bit -- i.e. the black-hole-entropy bit = the registration bit -- is the SEC9 / Compton-boundary
    correspondence (alpha-value plan Step 2, a later container). Located, not closed here. So base-2 is
    grounded as the substrate's native unit and reconciled with Shannon, but its identification with
    Stone 17's ln2 waits on SEC9.

Either outcome was admissible on entry (base-2 forced, OR ln2 a bare convention). What recomputes is:
the alphabet is 2 (not 3), the branching is base-2 -- DERIVED; the identification that makes ln2
contentful is a named POSTULATE; the tie to the ruler's ln2 is OWED. NO mass, NO census, danger-free.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
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


# ================================================================ the floor (consumes 00)
# Container 00's three existential states and its perceivable predicate, re-exhibited cold.
STATES = ["definedExistent", "undefinedExistent", "nonExistent"]


def perceivable(s):
    """Container 00.2: only what EXISTS can be perceived or registered. Non-existence cannot."""
    return s in ("definedExistent", "undefinedExistent")


# ---- B2.1 the registrable alphabet is exactly 2 -- DERIVED -----------------------------
# Of the three existential states, exactly two are perceivable/registrable (00.2); a distinction is a
# positive two-valued partition, defined vs undefined-existent (00.3). So the alphabet of what a single
# registration can distinguish has cardinality 2. Checked negatives: base-3 is refused (the third state
# is unregistrable), and the triad's 3 (OBSERVERS -- the machinery, 00.4) is a DIFFERENT quantity, kept
# typed apart from the 2 (the alphabet of the registered content).
registrable = [s for s in STATES if perceivable(s)]
ALPHABET = len(registrable)                              # = 2 (defined-existent, undefined-existent)
TOTAL_STATES = len(STATES)                               # = 3 (the third is non-existent, unregistrable)
OBSERVER_COUNT = 3                                       # the triad (00.4) -- machinery, NOT the alphabet
alphabet_is_two = (ALPHABET == 2)
base3_refuted = (ALPHABET != 3) and (TOTAL_STATES == 3)  # 3 states but only 2 registrable -> not base 3
typed_apart_from_triad = (OBSERVER_COUNT != ALPHABET)    # 3 observers != 2 registrable states (00.4 vs 00.2/3)
b21_ok = alphabet_is_two and base3_refuted and typed_apart_from_triad
step("B2.1", "the REGISTRABLE ALPHABET is exactly 2 (not 3; the triad's 3 is observers, typed apart)",
     "of container 00's three existential states, exactly two are perceivable/registrable (00.2), and a "
     "distinction is a positive two-valued partition defined/undefined-existent (00.3); so the alphabet "
     "of a single registration = 2. Base-3 refuted (the third state is unregistrable); the triad's 3 "
     "(observers, 00.4) is a distinct quantity, typed apart.",
     ["00.2", "00.3", "00.4"],
     "the solid floor of base-2, consuming container 00 cold. The information-theoretic BASE of a "
     "substrate is the size of its elemental alphabet -- how many states one registration distinguishes. "
     "Container 00 gives three existential states (defined-existent, undefined-existent, non-existent), "
     "but 00.2 proves non-existence CANNOT be perceived or registered, and 00.3 builds a distinction as a "
     "POSITIVE two-valued partition (a defined thing AND an undefined-existent residual, both existent, "
     "no is-not). So exactly TWO states are registrable: the alphabet is 2. Two checked negatives keep "
     "this honest and prevent the two easy conflations. (a) BASE-3 IS REFUTED: there are three existential "
     "states but only two are registrable, so the base is 2, not 3 -- the third (non-existence) is the "
     "counterpoint, not a symbol. (b) THE TRIAD IS NOT THE ALPHABET: container 00.4's THREE is the count "
     "of OBSERVERS (two within, one without) -- the machinery that PRODUCES a registration, explicitly "
     "'not the registration' (00.4) -- while the 2 here is the alphabet of the registered CONTENT. These "
     "are different quantities (like 14.B.4 != 14.B.5), kept typed apart: 'triadic floor' does NOT license "
     "'base 3'. What recomputes: |registrable states| = 2, |all states| = 3, and 3 (observers) != 2 "
     "(alphabet).",
     "UNIQUE (the registrable alphabet is the count of perceivable existential states = 2)", "DERIVED",
     {"registrable_states": registrable, "alphabet": ALPHABET, "total_existential_states": TOTAL_STATES,
      "alphabet_is_two": alphabet_is_two, "base3_refuted_third_state_unregistrable": base3_refuted,
      "observer_count_triad": OBSERVER_COUNT, "observers_typed_apart_from_alphabet": typed_apart_from_triad,
      "not_base3": "3 existential states but only 2 registrable; non-existence is the counterpoint, not a symbol",
      "triad_is_machinery": "the 3 is OBSERVERS (00.4, produce the registration), NOT the 2-state alphabet"},
     check="of 3 existential states exactly 2 are registrable (00.2/00.3) -> alphabet 2; 3 (observers) != 2 (alphabet); base-3 refuted")
assert b21_ok

# ---- B2.2 the per-registration branching factor is 2 -- base-2 -- DERIVED ---------------
# One registration = one binary distinction = one base-2 digit (a bit). A configuration space over k
# registrations grows as alphabet^k = 2^k: each registration MULTIPLIES the count by the alphabet size,
# so the branching factor is 2 and the substrate's native count L (containers 23/24) is a BIT-count. The
# base-2 branching is the doubling 2^{k+1} = 2 * 2^k; log2(2^k) = k recovers the count (exact on powers).
K_RANGE = list(range(0, 7))
def configs(k):
    """Free configuration count over k independent binary registrations = alphabet^k = 2^k."""
    return ALPHABET ** k
doubling = all(configs(k + 1) == 2 * configs(k) for k in K_RANGE)        # base-2 branching (x2 per reg.)
base_at_zero = (configs(0) == 1)                                          # empty config: one state
def log2_exact(n):
    """log2 of a power of two, exact (bit_length-1); this is the bit-count of an alphabet-2 config."""
    return n.bit_length() - 1
bitcount_is_k = all(log2_exact(configs(k)) == k for k in K_RANGE)        # bits(2^k) = k = the count L
b22_ok = doubling and base_at_zero and bitcount_is_k
step("B2.2", "the per-registration BRANCHING FACTOR is 2 -- base-2; the count L is a bit-count",
     "one registration = one binary distinction = one base-2 digit (a bit); a configuration space grows "
     "as alphabet^k = 2^k (each registration doubles it: 2^{k+1}=2*2^k), so the branching factor is 2 "
     "and the substrate's native count L is a BIT-count -- log2(2^k)=k",
     ["B2.1", "23.LI.2"],
     "the base-2 structure itself, arithmetic on the alphabet 2 (B2.1), no continuum. The BASE of a "
     "counting system is its per-symbol branching factor. With the registrable alphabet = 2 (B2.1), each "
     "registration is a single binary distinction -- one base-2 digit, a BIT. A configuration space over "
     "k registrations has alphabet^k = 2^k states: each added registration MULTIPLIES the count by 2 (the "
     "doubling 2^{k+1} = 2*2^k), which IS what 'base 2' means. So the substrate's native information count "
     "-- container 23's level L(d)=|A(d)|, the archon count, and container 24's I=alpha*L -- is a BIT-count "
     "(base 2): L archons carry L bits, and log2(2^L)=L recovers the count exactly. NOTE this is the "
     "BRANCHING factor of ONE registration (=2), which does not assume the archons are independent (they "
     "are co-defined by adjacency, 01.4); the 2^k free join is the illustration, the branching factor 2 is "
     "the claim. What recomputes: 2^{k+1}=2*2^k (base-2 doubling), 2^0=1, and log2(2^k)=k, all exact "
     "integer.",
     "UNIQUE (the branching factor is the alphabet size = 2; the count in that base is log2 = the archon count)",
     "DERIVED",
     {"branching_factor": ALPHABET, "base": 2, "doubling_2pow_k": doubling, "base_at_zero": base_at_zero,
      "bitcount_log2_is_k": bitcount_is_k, "k_range": K_RANGE,
      "L_is_a_bit_count": "container 23's L(d)=|A(d)| archon count IS the information in bits (base 2)",
      "not_assuming_independence": "the branching factor of ONE registration is 2; 2^k is the illustrative free join"},
     check="branching factor = alphabet 2; 2^{k+1}=2*2^k (base-2 doubling); log2(2^k)=k -> L is a bit-count")
assert b22_ok

# ---- B2.3 the Shannon reconciliation (the reading) -- POSTULATE -------------------------
# The identification that turns the DERIVED alphabet-2 into a claim about INFORMATION and gives ln2
# content. GIVEN registration-information = distinguishing among registrable configurations (the
# substrate's count IS Shannon's H with W=2), base-2 is the forced unit and ln2 = log_e(2) is the
# nat-size of one registration bit. Separately and compatibly: the base of a CONTINUOUS entropy is a
# free convention (physics is right -- nats or bits, nothing physical changes). Both true at different
# levels; the substrate has a preferred DISCRETE unit, continuous entropy does not. Held, not proven.
step("B2.3", "the Shannon reconciliation (READING): base-2 forced GIVEN info=distinguishing configs; ln2 gains content",
     "GIVEN that registration information = distinguishing among registrable configurations (the "
     "substrate's count is Shannon's H with W=2), base-2 is the FORCED information unit and ln2=log_e(2) "
     "is the nat-size of one registration bit, so BC=2*pi/ln2 reads '2*pi nats = 2*pi/ln2 bits'. The "
     "base-freedom of CONTINUOUS entropy is a separate, compatible fact. A correspondence, held.",
     ["B2.2", "17.S.3", "17.S.4"],
     "the honest reading, and the one place the danger of injection lives -- so it is graded POSTULATE, "
     "not DERIVED. B2.1/B2.2 establish, cold, that the registrable alphabet is 2 and the branching is "
     "base-2. To turn that into 'base-2 is the forced INFORMATION base, and ln2 has physical content' "
     "requires one identification: that registration information IS the distinguishing of registrable "
     "configurations -- i.e. the substrate's archon count L is Shannon's H with alphabet W=2. This is the "
     "Shannon-vs-registration reconciliation Stone 17 (S.3b/S.4ii) left owed. UNDER it, ln2 = log_e(2) "
     "acquires content: it is the size, in the analytically-natural nats, of ONE forced binary "
     "registration, so 'BC = 2*pi/ln2' says '2*pi nats = 2*pi/ln2 registration-bits' and the bit is the "
     "archon, not a unit convention. The steelman for the OTHER side is admitted and RECONCILED, not "
     "dismissed: for a CONTINUOUS entropy the log base is a free convention (you may count in nats and "
     "drop the ln2; nothing physical changes) -- physics is right about this. The reconciliation: base is "
     "free for a continuum but FIXED for this discrete substrate, whose elemental act is a 2-valued "
     "distinction, so it has a preferred unit (the bit = one registration) a continuum lacks. Both facts "
     "hold, at different levels. The identification (substrate count = Shannon H) is a CORRESPONDENCE, "
     "quarantined and held POSTULATE -- it is a reading, not proven; downstream may not rest on it.",
     "POSTULATE (the identification substrate-count = Shannon information; held, not proven)", "POSTULATE",
     {"reading_not_derived": True,
      "given": "registration information = distinguishing among registrable configurations (count = Shannon H, W=2)",
      "then_base2_forced": "the forced information unit is base-2; the bit = one archon",
      "ln2_gains_content": "ln2 = log_e(2) = the nat-size of one registration bit; BC=2*pi/ln2 => 2*pi nats in bits",
      "compatible_separate_fact": "the base of a CONTINUOUS entropy is a free convention (nats or bits); physics is right",
      "reconciliation": "base is free for a continuum but FIXED for this discrete substrate (elemental 2-valued act)",
      "quarantined": True, "downstream_premise_use": False},
     check=None)

# ---- B2.4 the tie to the ruler's ln2 needs SEC9 -- OWED ---------------------------------
# base-2 is grounded as the substrate's native unit (B2.1/B2.2) and reconciled with Shannon (B2.3), but
# that the ln2 in the SPECIFIC Bekenstein/Compton ruler BC=2*pi/ln2 is THIS registration bit -- the
# black-hole-entropy bit = the registration bit -- is the SEC9 / Compton-boundary correspondence
# (alpha-value plan Step 2, a later container). Located, not closed; NO mass touched here.
step("B2.4", "tying the ruler's ln2 to the registration bit is the SEC9 / Compton-boundary correspondence (OWED)",
     "that the ln2 in the specific ruler BC=2*pi/ln2 (Stone 17) is THIS registration bit -- i.e. the "
     "Bekenstein/black-hole-entropy bit = the registration bit -- is the SEC9 (Compton = registration "
     "boundary) correspondence, the alpha-value plan's Step 2, a later container. Located, not closed here.",
     ["B2.3", "17.S.4"],
     "the residual, located and NOT attempted here -- the honest boundary of the danger-free opener. "
     "B2.1/B2.2 ground base-2 as the substrate's native counting unit; B2.3 reconciles it with Shannon "
     "and gives ln2 content AS the nat-size of a registration bit. What remains for base-2 to fully "
     "discharge Stone 17's S.4(ii) is the identification of that registration bit with the ln2 in the "
     "SPECIFIC Bekenstein/Compton ruler -- that the entropy bit counted by the Bekenstein bound at the "
     "Compton scale IS one registration. That identification is exactly the SEC9 / Compton = "
     "registration-boundary correspondence (Stone 17 S.3a, OPEN), which is the alpha-value plan's Step 2 "
     "and a container of its own. It is NOT attempted here (this container is Step 1, deliberately "
     "mass-free): SEC9 touches the Compton scale R=hbar/mc and so the mass, which is the Path-A/Path-B "
     "owner-decision boundary. So base-2 is grounded and reconciled; its tie to the ruler's ln2 is "
     "located as SEC9's, and waits. present=False.",
     "OWED (the registration-bit = Bekenstein-bit identification; located at SEC9, not closed)", "OWED",
     {"present": False, "what_it_is": "registration bit = Bekenstein/Compton entropy bit (the ln2 in BC=2*pi/ln2)",
      "located_at": "SEC9 / Compton = registration-boundary (Stone 17 S.3a, OPEN) -- alpha-value plan Step 2",
      "why_deferred": "SEC9 touches the Compton scale R=hbar/mc and thus the mass -- the Path-A/Path-B boundary",
      "grounded_so_far": "base-2 as the substrate's native unit (B2.1/B2.2) + the Shannon reconciliation (B2.3)",
      "not_attempted": True, "danger_free": "this container touches NO mass"},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="26-base-2-forcing",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # B2.1 -- guarded by the Lean
        alphabet=ALPHABET,
        total_existential_states=TOTAL_STATES,
        observer_count=OBSERVER_COUNT,
        alphabet_is_two=alphabet_is_two,
        base3_refuted=base3_refuted,
        observers_typed_apart=typed_apart_from_triad,
        # B2.2 -- guarded by the Lean
        base=2,
        doubling_2pow_k=doubling,
        base_at_zero=base_at_zero,
        bitcount_log2_is_k=bitcount_is_k,
        # the reconciliation
        base2_forced_given_shannon=True,
        ln2_has_content_given_shannon=True,
        ruler_ln2_tie_is_owed_sec9=True,
        finding="the registrable alphabet is 2 (not 3; the triad's 3 is observers, typed apart) and the "
                "branching is base-2 -- DERIVED; base-2 as the forced INFORMATION unit (ln2 contentful) "
                "holds GIVEN the Shannon identification -- POSTULATE; tying it to the ruler's specific ln2 "
                "is SEC9's -- OWED. Danger-free: no mass touched.",
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
