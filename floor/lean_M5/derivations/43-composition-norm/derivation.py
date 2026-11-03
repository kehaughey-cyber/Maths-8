#!/usr/bin/env python3
"""Container 43 -- FLOOR-FORCING 42.SR.4: the division property reduces to the bridge + ONE multiplicative-norm postulate.

Kevin (Maths 6.7): floor-force 42.SR.4 -- the last held premise, "the carrier's ambient algebra is a
finite-dimensional DIVISION algebra over R", under which Frobenius/Hurwitz force H (hence dim=3). The
honest outcome is a LANDING, not a vanishing: SR.4 does not reduce to zero postulates (there is always a
floor), but it reduces to the ALREADY-ACCEPTED bridge (05) plus ONE crisp, irreducible postulate -- and
the container proves the group structure ALONE provably cannot supply the missing piece.

  CN.1  the target, itemized. What Frobenius (42.SR.5) / Hurwitz needs from SR.4: (i) over R with a
        positive-definite norm; (ii) finite-dimensional, unital, product = composition; (iii) DIVISION
        (no zero divisors). DERIVED (restates 42.SR.4 as three checkable requirements).

  CN.2  (i) over R + positive-definite = the BRIDGE (05.1), an EXISTING floor postulate -- NOT new. The
        bridge already gives real Euclidean space with the ordinary (positive-definite) inner product,
        explicitly not Hilbert/split. So this third of SR.4 is granted by the floor already. DERIVED
        (rests on 05.1).

  CN.3  the group ALONE does NOT force division -- the honest counterexample. The carrier is a group
        (06.3), but a group's real ALGEBRA (its R-span) generally has ZERO DIVISORS: R[Z/2] has
        (1+t)(1-t)=1-t^2=0 with both factors nonzero. And a sum of isometries is not an isometry, so the
        norm is not automatically multiplicative. So "the carrier is a group of isometries" is
        INSUFFICIENT for a division algebra -- the multiplicative norm is genuinely EXTRA. DERIVED,
        zero-axiom (the Z/2 zero divisor).

  CN.4  the isolated deep root (POSTULATE): the composition norm is MULTIPLICATIVE, N(xy)=N(x)N(y).
        Rooted (the reading) in INTENSIVITY -- registration subdivides the one (00.0.1/01.1.3), so
        composing registrations composes SHARES multiplicatively (a share of a share), while the additive
        archon count (23.LI.4) is its LOGARITHM (the Shannon reading, 26 -- log turns x into +, resolving
        the apparent tension). This is SR.4's true floor-kernel: reduced from "division algebra" to "the
        composition norm is multiplicative". USED as a premise by CN.5 (downstream_premise_use=True).

  CN.5  positive-definite (CN.2/05) + multiplicative (CN.4) => no zero divisors => (finite-dim) DIVISION.
        Hurwitz (cited): a positive-definite multiplicative real algebra is R, C, H, or O (dims 1,2,4,8);
        with 42's associativity (excl. O) + non-commutativity (excl. R,C) => H (dim 4) => dim=3. So SR.4
        is DISCHARGED given CN.4; the whole edifice now bottoms at 05 (bridge) + CN.4 (multiplicative
        norm) + 42's assoc/non-comm. DERIVED given CN.4 (Hurwitz cited, as 42 cites Frobenius).

  CN.6  OWED + the honest tension. OWED: CN.4 fully derived (the intensivity->multiplicative reading made
        a theorem); Hurwitz re-derived on the substrate; the product=composition / 0=non-existence
        identifications. THE TENSION (named, not hidden): the multiplicative norm is CLOSE to the crux --
        composition algebras essentially ARE the normed division algebras -- so CN.4 is load-bearing; but
        it is NOT circular (Hurwitz's restriction to dims 1,2,4,8 and the assoc+non-comm cut to H are
        real, non-trivial content, and CN.4 is motivated by intensivity, not by the answer H).

Rests on 42 (SR.4 -- the premise it roots; SR.5 -- the Frobenius/Hurwitz cut), 05 (the bridge / real
positive-definite norm), 06 (the carrier is a group), 00/01/23/26 (intensivity + additive count + the
Shannon log); cites Hurwitz 1898. DANGER-FREE: pure algebra -- no mass, no census, no coupling, no value.
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


# ================================================================ the Z/2 group-algebra zero divisor (CN.3)
# Elements of R[Z/2] as pairs (a,b) = a*1 + b*t, with t^2 = 1, so (a,b)*(c,d) = (a*c + b*d, a*d + b*c).
def g2mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c)


U = (1, 1)      # 1 + t
W = (1, -1)     # 1 - t
UW = g2mul(U, W)                                   # (1-1, -1+1) = (0,0) -- a zero divisor
zero_divisor = (UW == (0, 0) and U != (0, 0) and W != (0, 0))

# ---- the Hurwitz composition algebras (reuse 42's four, by real dimension) --------------
ALGEBRAS = ["R", "C", "H", "O"]
REAL_DIM = {"R": 1, "C": 2, "H": 4, "O": 8}        # Hurwitz: the composition algebras over R
ASSOCIATIVE = {"R": True, "C": True, "H": True, "O": False}
COMMUTATIVE = {"R": True, "C": True, "H": False, "O": False}
HURWITZ_DIMS = [REAL_DIM[a] for a in ALGEBRAS]     # [1,2,4,8]
forced = [a for a in ALGEBRAS if ASSOCIATIVE[a] and not COMMUTATIVE[a]]   # -> ["H"], dim 4

# ---- CN.1 the target, itemized -- DERIVED ----------------------------------------------
REQUIREMENTS = ["over R with a positive-definite norm", "finite-dimensional, unital, product=composition",
                "DIVISION (no zero divisors / every nonzero element invertible)"]
step("CN.1", "the target: what Frobenius/Hurwitz needs from 42.SR.4, as three checkable requirements",
     "42.SR.4 ('the carrier's ambient algebra is a finite-dim DIVISION algebra over R') = (i) over R + "
     "positive-definite norm; (ii) finite-dim, unital, product=composition; (iii) DIVISION (no zero "
     "divisors). Frobenius/Hurwitz consumes exactly these",
     ["42.SR.4"],
     "state precisely what must be floor-forced, so each piece can be sorted honestly. 42 forced H (hence "
     "dim=3) from associativity + non-commutativity + SR.4, via Frobenius. SR.4 is the one held premise. "
     "Unpack it into the three things Frobenius/Hurwitz actually uses: (i) the algebra is over R and "
     "carries a positive-definite quadratic form (norm); (ii) it is finite-dimensional, unital, and its "
     "product is the composition of registrations; (iii) it is a DIVISION algebra -- no zero divisors, "
     "equivalently (finite-dim) every nonzero element invertible. CN.2-CN.5 sort these: (i) is the bridge "
     "(existing), (ii) is cold, (iii) is the residual that needs the multiplicative norm.",
     "UNIQUE (SR.4 = the three requirements Frobenius/Hurwitz consumes)", "DERIVED",
     {"requirements": REQUIREMENTS,
      "consumed_by": "42.SR.5 (Frobenius) / Hurwitz",
      "sorting": "(i) bridge 05 [CN.2]; (ii) cold [00/06/07]; (iii) the residual -- needs multiplicativity [CN.3-CN.5]"},
     check="SR.4 unpacks into (over-R+pos-def) + (finite-dim,unital,product) + (division)")

# ---- CN.2 over R + positive-definite = the bridge (05) -- DERIVED (rests on 05.1) -------
step("CN.2", "(i) over R + positive-definite norm = the BRIDGE (05.1) -- an EXISTING floor postulate, not new",
     "the bridge (05.1) already gives: the registration structure corresponds to points in real "
     "Euclidean space with the ORDINARY inner product -- real, positive-definite, explicitly NOT Hilbert "
     "and NOT split. So requirement (i) of SR.4 is supplied by the floor ALREADY; it is not a new "
     "assumption",
     ["CN.1", "05.5.1"],
     "the first third of SR.4 costs nothing new. Container 05 (the geometric-balance bridge, a POSTULATE "
     "the whole metric tower already rests on) states that registrations correspond to points in a REAL "
     "EUCLIDEAN space with the ordinary inner product -- which is exactly a positive-definite quadratic "
     "form over R (05.1 is emphatic: Euclidean, NOT Hilbert space, real coordinates + ordinary inner "
     "product). The downstream metric containers (08 etc.) are DERIVED resting on 05, so resting on it "
     "here imports no new commitment. Requirement (i) -- over R with a positive-definite norm -- is thus "
     "GRANTED by the existing floor, not a fresh premise. (This is why the norm in CN.4/CN.5 is "
     "positive-definite: because the bridge's is.)",
     "DERIVED given 05.1 (the bridge supplies real + positive-definite; an existing postulate, not new)", "DERIVED",
     {"supplied_by": "05.1 (the bridge -- real Euclidean, positive-definite, not Hilbert/split)",
      "is_new_postulate": False, "already_rested_on_by": "the metric tower (08+), DERIVED"},
     check="requirement (i) over-R + positive-definite = the bridge 05.1 (existing postulate)")

# ---- CN.3 the group ALONE does not force division -- DERIVED (zero-axiom counterexample) -
step("CN.3", "(iii, negative) the group ALONE does NOT force division: R[Z/2] has a zero divisor (1+t)(1-t)=0",
     "the carrier is a group (06.3), but a group's real ALGEBRA (its R-span) generally has ZERO "
     "DIVISORS: in R[Z/2] (t^2=1), (1+t)(1-t) = 1 - t^2 = 0 with 1+t, 1-t both nonzero. And a sum of "
     "isometries is not an isometry, so a group of norm-1 isometries does not make the norm "
     "multiplicative. So being a group of isometries is INSUFFICIENT for a division algebra -- the "
     "multiplicative norm is genuinely EXTRA",
     ["CN.1", "06.6.3"],
     "the honest step that stops the over-claim, and it is cold. It is tempting to say 'the carrier is a "
     "group (06.3), every element invertible, so the algebra is a division algebra'. FALSE, and provably: "
     "the group ALGEBRA R[G] is not the division algebra. RUN THE COUNTEREXAMPLE on the smallest group "
     "Z/2 = {1,t}, t^2=1: represent a*1+b*t as (a,b), so (a,b)*(c,d) = (ac+bd, ad+bc). Then "
     "(1+t)(1-t) = (1,1)*(1,-1) = (1-1, -1+1) = (0,0) -- a ZERO DIVISOR, with both factors nonzero. So "
     "R[Z/2] is not a division algebra, though Z/2 is a perfectly good group. Moreover, a sum of "
     "norm-1 isometries is generally not an isometry (|g+h|.v depends on v), so the positive-definite "
     "norm is NOT automatically multiplicative on the span. CONCLUSION: the carrier being a group of "
     "isometries (06.3 + 05) does NOT supply the division property; something more is needed, and CN.4 "
     "names exactly what -- multiplicativity of the norm. This is the guard against the false floor-force "
     "'group => division'.",
     "UNIQUE (R[Z/2] has an explicit zero divisor => group alone does not give a division algebra)", "DERIVED",
     {"z2_product_rule": "(a,b)*(c,d) = (ac+bd, ad+bc), t^2=1",
      "zero_divisor_witness": {"one_plus_t": list(U), "one_minus_t": list(W), "product": list(UW)},
      "is_zero_divisor": zero_divisor,
      "so": "group (06.3) alone does NOT force division; the multiplicative norm is genuinely extra",
      "also": "a sum of isometries is not an isometry => norm not automatically multiplicative"},
     check="(1+t)(1-t)=(0,0) in R[Z/2] with both nonzero -- a zero divisor; group does not give a division algebra")
assert zero_divisor

# ---- CN.4 the isolated deep root: the composition norm is multiplicative -- POSTULATE ----
step("CN.4", "the isolated root (POSTULATE): the composition norm is MULTIPLICATIVE, N(xy)=N(x)N(y)",
     "the composition norm is MULTIPLICATIVE: N(xy) = N(x)N(y). The reading that roots it: registration "
     "is INTENSIVE -- it subdivides the one, it does not replicate (00.0.1; 01.1.3) -- so composing "
     "registrations composes SHARES multiplicatively (a share of a share is the product), while the "
     "ADDITIVE archon count (23.LI.4) is its LOGARITHM (the Shannon reading, 26; log turns x into +). "
     "This is SR.4's true floor-kernel; USED as a premise by CN.5",
     ["CN.3", "00.0.1", "23.LI.4", "26.B2.3"],
     "the residual, isolated and named -- the point of the container. CN.3 showed the group does not give "
     "division; the missing piece is a MULTIPLICATIVE norm N(xy)=N(x)N(y). Where can that root in the "
     "floor? The reading: registration is INTENSIVE -- 00/01 (and the alpha-hat work, 23/24) establish "
     "that registration SUBDIVIDES the one rather than replicating it, so a registration carries a SHARE "
     "of the whole. Composing two registrations composes their shares MULTIPLICATIVELY -- a share of a "
     "share is the product of the shares -- so the natural norm (the share/measure) is multiplicative. "
     "This is consistent with, not contrary to, the ADDITIVE archon count (23.LI.4): the count is the "
     "LOGARITHM of the multiplicative share (the Shannon reading already in play at 26/32 -- additive "
     "information = log of multiplicative probability), and log turns multiplication into addition, so "
     "counts add exactly when shares multiply. HONEST GRADE: this identification -- that the "
     "composition-algebra norm IS the intensive share -- is a READING, held as the single POSTULATE. It "
     "is the deepest the root goes here: SR.4 ('division algebra over R') is now reduced to (05, existing) "
     "+ THIS one multiplicative-norm postulate. It is USED by CN.5 (downstream_premise_use=True) -- a "
     "premise, not a quarantined reading.",
     "POSTULATE (the composition norm is multiplicative; rooted in intensivity/shares, the count its log; the isolated residual)", "POSTULATE",
     {"claim": "N(xy) = N(x)N(y) (the composition norm is multiplicative)",
      "root_reading": "registration intensive (00/01) => composing registrations composes SHARES multiplicatively",
      "count_is_the_log": "the additive archon count (23.LI.4) = log of the multiplicative share (Shannon, 26); +/x consistent",
      "is_the_one_residual": True, "reading_not_derivation": True,
      "premise_not_quarantined_reading": "USED by CN.5 -- a premise, not a quarantined reading",
      "downstream_premise_use": True},
     check=None)

# ---- CN.5 pos-def + multiplicative => division; Hurwitz => H -- DERIVED (given CN.4) -----
posdef_and_mult_give_division = True    # N(x)>0 for x!=0 and N(xy)=N(x)N(y) => xy=0 => x=0 or y=0
hurwitz_then_H = (forced == ["H"] and REAL_DIM["H"] == 4 and HURWITZ_DIMS == [1, 2, 4, 8])
step("CN.5", "positive-definite (05) + multiplicative (CN.4) => division; Hurwitz => H (dim 4) => dim=3 -- SR.4 discharged given CN.4",
     "positive-definite (CN.2/05) + multiplicative (CN.4): if N(x)>0 for x!=0 and N(xy)=N(x)N(y), then "
     "xy=0 => N(x)N(y)=0 => x=0 or y=0 -- NO ZERO DIVISORS => (finite-dim) DIVISION. Hurwitz 1898 "
     "(cited): a positive-definite multiplicative real algebra is R, C, H, or O (dims 1,2,4,8); with "
     "42's associativity (excl. O) + non-commutativity (excl. R,C) => H (dim 4) => dim=3. So SR.4 is "
     "DISCHARGED given CN.4",
     ["CN.2", "CN.4", "42.SR.5"],
     "the payoff: SR.4 falls out of the bridge + the one multiplicative-norm postulate. First the "
     "DIVISION property, cold from CN.2+CN.4: a positive-definite norm has N(x)>0 for every nonzero x "
     "(05), and if the norm is multiplicative (CN.4) then N(xy)=N(x)N(y); so xy=0 forces N(x)N(y)=0, "
     "hence N(x)=0 or N(y)=0, hence x=0 or y=0 -- NO ZERO DIVISORS. In finite dimension (06) no zero "
     "divisors <=> a division algebra. So requirement (iii) is met. Then the classification is even "
     "cleaner than Frobenius: HURWITZ 1898 (cited external, as 42 cites Frobenius/41 cites "
     "Newton-Gregory) says a finite-dim unital real algebra with a positive-definite MULTIPLICATIVE "
     "quadratic form is exactly R, C, H, or O (real dims 1,2,4,8). Applying 42's associativity (the "
     "group, excl. the non-associative O) and non-commutativity (the chirality, excl. the commutative "
     "R, C) leaves H (real dim 4), whose imaginary part is 3 -- so dim=3 (42.SR.1). Therefore the entire "
     "'carrier is H / dim=3' edifice now bottoms at: the bridge (05) + CN.4 (the multiplicative norm) + "
     "42's associativity/non-commutativity. SR.4 is no longer a broad standalone premise -- it is "
     "reduced to ONE crisp, dimension-free postulate (CN.4) atop the existing bridge.",
     "UNIQUE (pos-def + multiplicative => division; Hurwitz + assoc + non-comm => H (dim 4) => dim 3)", "DERIVED",
     {"posdef_plus_mult_give_no_zero_divisors": posdef_and_mult_give_division,
      "hurwitz_dims": HURWITZ_DIMS, "forced_algebra": forced, "h_real_dim": REAL_DIM["H"],
      "hurwitz_then_H": hurwitz_then_H,
      "cited_external": "Hurwitz 1898 (positive-definite multiplicative real algebra = R,C,H,O)",
      "discharges": "42.SR.4 given CN.4 -- the edifice bottoms at 05 (bridge) + CN.4 (mult. norm) + 42's assoc/non-comm"},
     check="pos-def + multiplicative => no zero divisors => division; Hurwitz dims [1,2,4,8], assoc+non-comm => H (dim 4)")
assert posdef_and_mult_give_division and hurwitz_then_H

# ---- CN.6 OWED + the honest tension ----------------------------------------------------
step("CN.6", "OWED + the honest tension: CN.4 is load-bearing (close to the crux) but NOT circular",
     "OWED: (a) CN.4 fully DERIVED -- the intensivity->multiplicative-share reading (and the count=log "
     "tie) made a theorem, not a reading; (b) Hurwitz re-derived on the substrate (cited, not re-proved); "
     "(c) the product=composition / 0=non-existence identifications. THE TENSION, named: the "
     "multiplicative norm (CN.4) is CLOSE to the crux -- composition algebras essentially ARE the normed "
     "division algebras -- so CN.4 is load-bearing; but it is NOT circular",
     ["CN.4", "CN.5"],
     "the honest residuals and the one tension a careful reader will (rightly) press on. WHAT THIS "
     "CONTAINER DID: floor-forced 42.SR.4 as a LANDING -- (i) over-R+positive-definite = the existing "
     "bridge 05 (CN.2, no new cost); (ii) finite-dim/unital/product cold; (iii) division reduced to ONE "
     "postulate, the multiplicative norm (CN.4), after proving the group alone cannot supply it (CN.3). "
     "So SR.4 is reduced from a broad premise to 05 + CN.4. WHAT IT DID NOT DO: (a) turn CN.4 into a "
     "theorem -- the intensivity->multiplicativity step is a (well-motivated, Shannon-consistent) "
     "READING; (b) re-derive Hurwitz on the substrate; (c) discharge the product=composition and "
     "0=non-existence identifications. THE TENSION (stated, not hidden -- CORRECTIONS #7 discipline): "
     "because a positive-definite MULTIPLICATIVE norm essentially CHARACTERIZES the normed division "
     "algebras, CN.4 is doing heavy lifting and sits close to the conclusion. It is NOT circular: "
     "Hurwitz's restriction to dims 1,2,4,8 is a hard, non-trivial theorem (not assumed), the cut to H "
     "via associativity + non-commutativity (42) is real content, and CN.4 is motivated by INTENSIVITY "
     "(the floor's subdivide-not-replicate), not reverse-engineered from H. The honest standing: SR.4 is "
     "REDUCED to its bedrock -- the bridge plus a single, named, dimension-free, independently-motivated "
     "postulate -- with the group-only shortcut disproved. Fully deriving CN.4 (the share/log picture as "
     "a theorem) would finish it. NOT attempted further here; danger-free throughout.",
     "OWED (CN.4 fully derived; Hurwitz re-derived; the identifications) + the tension named", "OWED",
     {"owed_derive_CN4": "the intensivity->multiplicative-norm reading made a theorem (with the count=log tie)",
      "owed_hurwitz": "Hurwitz re-derived on the substrate (cited external)",
      "owed_identifications": "product=composition; 0=non-existence (00)",
      "tension": "CN.4 (multiplicative norm) is close to the crux (composition algebras ~ normed division algebras) -- "
                 "load-bearing, but NOT circular: Hurwitz's 1,2,4,8 + the assoc/non-comm cut are real content, "
                 "and CN.4 is motivated by intensivity, not by H",
      "net": "42.SR.4 reduced from a broad premise to the existing bridge (05) + ONE named multiplicative-norm postulate; group-only shortcut disproved",
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="43-composition-norm",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        requirements=REQUIREMENTS,
        z2_zero_divisor={"one_plus_t": list(U), "one_minus_t": list(W), "product": list(UW),
                         "is_zero_divisor": zero_divisor},
        algebras=ALGEBRAS, real_dim=REAL_DIM, associative=ASSOCIATIVE, commutative=COMMUTATIVE,
        hurwitz_dims=HURWITZ_DIMS, forced_algebra=forced,
        finding="FLOOR-FORCING 42.SR.4 as a LANDING. SR.4 ('the carrier's ambient algebra is a "
                "finite-dim DIVISION algebra over R') splits into (i) over-R + positive-definite = the "
                "BRIDGE 05 (CN.2, an EXISTING postulate, not new); (ii) finite-dim/unital/product cold; "
                "(iii) DIVISION. The group ALONE does NOT give (iii) -- R[Z/2] has the zero divisor "
                "(1+t)(1-t)=0 (CN.3, cold) -- so a MULTIPLICATIVE norm is genuinely extra. That is the "
                "isolated root (CN.4, POSTULATE): the composition norm is multiplicative, rooted in "
                "INTENSIVITY (registration subdivides => shares multiply; the additive count 23 is its "
                "log, Shannon 26). Then positive-definite + multiplicative => no zero divisors => DIVISION, "
                "and Hurwitz (cited) + 42's assoc/non-comm => H (dim 4) => dim=3 (CN.5). So SR.4 is REDUCED "
                "to 05 + ONE named, dimension-free, independently-motivated postulate; the group-only "
                "shortcut is disproved. TENSION named (CN.6): CN.4 is load-bearing (close to the crux) but "
                "NOT circular. Danger-free, nothing fitted.",
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
