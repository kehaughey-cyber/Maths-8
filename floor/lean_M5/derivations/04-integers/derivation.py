#!/usr/bin/env python3
"""Container 04 -- the integers / the additive inverse. Rung 4, rests on container 01.

Mines the CRITERION of maths-4's RUNG4-INTEGERS-ADDITIVE-INVERSE (LIVE / THEOREM /
zero-axiom -- the Grothendieck completion of N), never its literals. The floor reading is
Kevin's, finally earned:

  - Rung 1 gives a COUNT -- a Nat, the length of a registration chain. A count has no
    inverse: there is no n with n+1 = 0 (you cannot un-register). That is the LACK.
  - An integer is a SIGNED DISPLACEMENT: a pair (a, b) read as "a one way, b the other" --
    a DIRECTION with magnitude, never a located thing. Two pairs are the same integer when
    they encode the same net displacement, compared by CROSS-ADD (a+d = c+b) so Nat's
    truncated subtraction -- the "is-not" operation -- is never invoked. The positive form.
  - "0" is the COUNTERPOINT, not a thing: the class of the balanced pairs (n, n), the
    diagonal a = b, where the two directions cancel. It names balance, not an object
    (CORRECTIONS.md #2: 0 is non-existence/counterpoint; it does not exist).
  - +1 and -1 are the two unit DIRECTIONS off the counterpoint: +1 = class of (1, 0),
    -1 = class of (0, 1). Directions, not is/is-not.
  - THE HEADLINE: every integer has an additive inverse -- its REVERSED direction,
    negPair(a,b) = (b,a) -- and (a,b) + (b,a) ~ 0. The one thing Nat lacks, now supplied
    for EVERY element. The inverse of a direction is the opposite direction; they meet at
    the counterpoint.

Everything is computed here from its own criteria (exact Nat arithmetic, cross-add only;
no subtraction is used to DEFINE anything -- min-normalisation only names a class's
canonical representative). Grades, first-class: DERIVED (recomputed/kernel-checked here),
POSTULATE (the identification with the floor, held/capped), OWED (the ring and the order,
deferred -- not smuggled).
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNG1_DERIV = HERE.parent / "01-recursive-registration" / "derivation.json"

STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- the objects
# An integer is a pair of Nats (a, b), read "a against b" -- a signed displacement.
# Every operation below stays inside Nat's addition; subtraction is NEVER invoked.
def int_equiv(p, q):
    """(a,b) ~ (c,d)  iff  a + d = c + b  (cross-add form of 'a-b = c-d')."""
    return p[0] + q[1] == q[0] + p[1]


def add_pair(p, q):
    return (p[0] + q[0], p[1] + q[1])


def neg_pair(p):
    """Reverse the direction: 'a against b' negated is 'b against a'."""
    return (p[1], p[0])


def mul_pair(p, q):
    """(a-b)(c-d) = (ac+bd) - (ad+bc), kept in Nat -- no subtraction is invoked."""
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c)


def le_pair(p, q):
    """(a,b) <= (c,d)  iff  a+d <= c+b  (cross-add form of 'a-b <= c-d')."""
    return p[0] + q[1] <= q[0] + p[1]


def is_pos(p):
    """Orientation: the +1 direction. (a,b) is positive iff its net leans defined-ward,
    i.e. b < a -- WHICH direction is positive, decided without subtraction."""
    return p[1] < p[0]


def of_nat_pair(n):
    """The count n embeds as pure defined-direction displacement: (n, 0)."""
    return (n, 0)


def canonical(p):
    """The class representative: subtract the common (balanced) part. m = min(a,b) is the
    amount that cancels; (a-m, b-m) lands on (k,0) | (0,k) | (0,0). This NAMES the class
    (it does not define the equivalence -- int_equiv does)."""
    m = min(p[0], p[1])
    return (p[0] - m, p[1] - m)


ZERO = (0, 0)
PLUS_ONE = (1, 0)
MINUS_ONE = (0, 1)

# a sample of pairs -- exhaustive over a small coordinate range; exact throughout.
R = 6
SAMPLE = [(a, b) for a in range(R) for b in range(R)]


# ---- 4.1 the count has no inverse -- the LACK -- DERIVED --------------------
N41 = 200
no_succ_is_zero = all((n + 1) != 0 for n in range(N41))
step("4.1", "the count has no additive inverse -- the lack rung 4 repairs",
     "for all n:Nat, n + 1 != 0", [],
     "rung 1 hands up a COUNT (a chain length): a Nat. A count cannot be undone -- there is "
     "no n with n+1 = 0, because n+1 >= 1 > 0 always. This missing inverse is exactly what "
     "'algebra' adds beyond 'number', and it is added below, not assumed.",
     "UNIQUE (a property of Nat)", "DERIVED",
     {"checked_range": N41, "any_n_with_succ_zero": (not no_succ_is_zero),
      "reason": "n+1 >= 1 > 0 for every n:Nat"},
     check="no n:Nat satisfies n+1 = 0")
assert no_succ_is_zero

# ---- 4.2 integer = signed displacement; cross-add is an equivalence -- DERIVED
refl_ok = all(int_equiv(p, p) for p in SAMPLE)
symm_ok = all((not int_equiv(p, q)) or int_equiv(q, p) for p in SAMPLE for q in SAMPLE)
trans_ok = all((not (int_equiv(p, q) and int_equiv(q, r))) or int_equiv(p, r)
               for p in SAMPLE for q in SAMPLE for r in SAMPLE)
classes = {}
for p in SAMPLE:
    classes.setdefault(canonical(p), []).append(list(p))
step("4.2", "an integer is a signed displacement; cross-add is an equivalence relation",
     "(a,b) ~ (c,d) iff a+d = c+b -- reflexive, symmetric, transitive", ["4.1"],
     "the pair (a,b) is a DIRECTION with magnitude ('a one way, b the other'), never a "
     "located thing. Sameness is same NET displacement, tested by cross-ADD so Nat's "
     "truncated subtraction (the is-not operation) is never invoked -- the positive form. "
     "Reflexive/symmetric/transitive make 'the integer' a genuine class, not an accident of "
     "the chosen pair.",
     "the integer is UNIQUE (as a class); its representative is CHOSEN", "DERIVED",
     {"sample_size": len(SAMPLE), "refl": refl_ok, "symm": symm_ok, "trans": trans_ok,
      "distinct_classes": len(classes)},
     check="cross-add relation is refl/symm/trans over the sample")
assert refl_ok and symm_ok and trans_ok

# ---- 4.3 "0" is the counterpoint, not a thing -- DERIVED --------------------
diagonal_all_zero = all(int_equiv((n, n), ZERO) for n in range(R + R))
zero_iff_balanced = all(int_equiv(p, ZERO) == (p[0] == p[1]) for p in SAMPLE)
step("4.3", "'0' is the counterpoint -- the balanced (diagonal) class, not a thing",
     "the class of ZERO = { (n,n) : n:Nat } ; and (a,b) ~ 0 iff a = b", ["4.2"],
     "zero is not an object among the counts. It is the class of the BALANCED pairs (n,n) -- "
     "the diagonal a=b, where the two directions cancel to null displacement. It names "
     "BALANCE, the counterpoint, not a located thing (CORRECTIONS #2: 0 does not exist; it "
     "is the counterpoint). A pair sits at 0 exactly when its two directions are equal.",
     "UNIQUE (the zero class is the whole diagonal)", "DERIVED",
     {"diagonal_is_zero": diagonal_all_zero, "zero_iff_balanced": zero_iff_balanced,
      "canonical_of_zero": list(canonical(ZERO)),
      "note": "0 names balance, not an object -- the counterpoint"},
     check="the (n,n) diagonal is exactly the class of 0")
assert diagonal_all_zero and zero_iff_balanced

# ---- 4.4 +1 and -1 are the two unit directions -- DERIVED ------------------
plus_minus_distinct = not int_equiv(PLUS_ONE, MINUS_ONE)
plus_minus_inverse = int_equiv(add_pair(PLUS_ONE, MINUS_ONE), ZERO)
# reachability: every class with |net| <= K is reached from 0 by iterating +1 or -1.
K = 8
reached = set()
p = ZERO
for _ in range(K + 1):                       # 0, +1, +2, ... +K
    reached.add(canonical(p)); p = add_pair(p, PLUS_ONE)
p = ZERO
for _ in range(K + 1):                       # 0, -1, -2, ... -K
    reached.add(canonical(p)); p = add_pair(p, MINUS_ONE)
want = {canonical((k, 0)) for k in range(K + 1)} | {canonical((0, k)) for k in range(K + 1)}
all_reached = want.issubset(reached)
step("4.4", "+1 and -1 are the two unit directions off the counterpoint",
     "+1 := class(1,0) ; -1 := class(0,1) ; distinct, mutually inverse, and generating",
     ["4.3"],
     "+1 is one net step the defined way, -1 one net step the opposite way -- DIRECTIONS, not "
     "is/is-not. They are distinct (1+1 != 0+0), each other's inverse, and every integer is "
     "reached from the counterpoint 0 by iterating one direction or the other. This is what "
     "earns 'the number line': an origin and two directions.",
     "UNIQUE (the two unit-direction classes)", "DERIVED",
     {"plus_one": list(PLUS_ONE), "minus_one": list(MINUS_ONE),
      "distinct": plus_minus_distinct, "plus_minus_inverse": plus_minus_inverse,
      "reach_bound": K, "all_reached_from_zero": all_reached},
     check="+1,-1 distinct, inverse, and generate every class from 0")
assert plus_minus_distinct and plus_minus_inverse and all_reached

# ---- 4.5 THE HEADLINE: every integer has an additive inverse -- DERIVED -----
all_have_inverse = all(int_equiv(add_pair(p, neg_pair(p)), ZERO) for p in SAMPLE)
witnesses = [{"p": list(p), "neg": list(neg_pair(p)),
              "sum": list(add_pair(p, neg_pair(p))), "at_zero": int_equiv(add_pair(p, neg_pair(p)), ZERO)}
             for p in [(1, 0), (0, 1), (3, 1), (2, 5)]]
step("4.5", "THE HEADLINE -- every integer has an additive inverse (its reversed direction)",
     "negPair(a,b) = (b,a) ; (a,b) + (b,a) ~ 0 for every pair", ["4.1", "4.4"],
     "the one thing Nat lacked (4.1) is now supplied for EVERY element: reverse the direction "
     "(swap the components) and the sum balances to the counterpoint. The inverse of a "
     "direction IS the opposite direction; the two meet at 0. This is the whole content of "
     "'algebra beyond counting', proved -- not assumed.",
     "UNIQUE (each class has one inverse class)", "DERIVED",
     {"all_have_inverse": all_have_inverse, "sample_size": len(SAMPLE),
      "inverse_is": "the reversed direction (swap the two components)",
      "witnesses": witnesses},
     check="(a,b)+(b,a) ~ 0 for every pair in the sample")
assert all_have_inverse

# ---- 4.6 operations well-defined on the class; the count embeds -- DERIVED --
# pairs of ~-equivalent pairs, over the sample -- the representatives to test congruence on.
eqv = [(p, q) for p in SAMPLE for q in SAMPLE if int_equiv(p, q)]
# a few equivalent (q ~ q2) addends to compose against every equivalent (p ~ p2).
Q_PAIRS = [((1, 0), (3, 2)), ((0, 2), (2, 4)), ((2, 2), (0, 0)), ((5, 1), (4, 0))]
add_congr_ok = all(int_equiv(add_pair(p, q), add_pair(p2, q2))
                   for (p, p2) in eqv for (q, q2) in Q_PAIRS)
neg_congr_ok = all(int_equiv(neg_pair(p), neg_pair(p2)) for (p, p2) in eqv)
embed_preserves_add = all(of_nat_pair(a + b) == add_pair(of_nat_pair(a), of_nat_pair(b))
                          for a in range(R) for b in range(R))
# the thin, honest tie to rung 1: its own derivation's chain length is a genuine Nat.
rung1 = json.loads(RUNG1_DERIV.read_text(encoding="utf-8"))
rung1_count = rung1["values"]["length"]
step("4.6", "the operations are well-defined on the class; the count embeds, preserving +",
     "addPair_congr, negPair_congr ; ofNatPair(a+b) = ofNatPair a + ofNatPair b (outright)",
     ["4.2", "4.5"],
     "addition and negation do not depend on which representative is chosen -- the direction "
     "is a genuine property of the CLASS, so these are operations on integers, not on pairs. "
     "And counting sits inside as pure defined-direction displacement: n -> (n,0) preserves "
     "addition OUTRIGHT (definitionally, not merely up to ~). The tie to rung 1 is deliberately "
     "thin and honest: rung 1 produces a real Nat (a chain length) and that Nat embeds as "
     "(n,0) -- no rich structural correspondence is claimed.",
     "UNIQUE (well-definedness makes the class operation unique)", "DERIVED",
     {"add_congr": add_congr_ok, "neg_congr": neg_congr_ok,
      "embed_preserves_add": embed_preserves_add,
      "rung1_chain_length": rung1_count, "embed_of_rung1": list(of_nat_pair(rung1_count)),
      "tie": "thin, honest -- an available Nat, not a structural correspondence"},
     check="add/neg representative-independent; embedding preserves +; rung-1 Nat embeds")
assert add_congr_ok and neg_congr_ok and embed_preserves_add

# ---- 4.7 the identification with the registration floor -- POSTULATE --------
step("4.7", "the reading: this signed-displacement structure IS the floor's number line",
     "identify(class(a,b)) := the net registration displacement; +1/-1 the two directions, "
     "0 the counterpoint", ["4.3", "4.4", "4.5"],
     "the mathematics above is unconditional. THIS step is the reading, held not proven: that "
     "the signed displacements ARE the floor's number line -- +1 and -1 the two directions a "
     "registration count can be extended in, 0 the counterpoint (not a thing). Kevin's floor "
     "note, now earned by the algebra but not derived from it. Capped as a postulate.",
     "the reading (identification), held", "POSTULATE",
     {"held": True, "reading": "+1/-1 are the registration directions; 0 is the counterpoint",
      "proven": False},
     check=None)

# ---- 4.8 multiplication -- the ring core -- DERIVED -------------------------
# (a-b)(c-d) = (ac+bd) - (ad+bc); the product stays inside Nat, no subtraction invoked.
mul_congr_ok = all(int_equiv(mul_pair(p, r), mul_pair(p2, r))
                   for (p, p2) in eqv for r in [(1, 0), (0, 1), (3, 2), (2, 5)])
mul_one_ok = all(int_equiv(mul_pair(p, PLUS_ONE), p) for p in SAMPLE)
mul_comm_ok = all(mul_pair(p, q) == mul_pair(q, p) for p in SAMPLE for q in SAMPLE)
left_distrib_ok = all(int_equiv(mul_pair(p, add_pair(q, r)),
                                add_pair(mul_pair(p, q), mul_pair(p, r)))
                      for p in [(2, 0), (0, 3), (3, 1)] for q in SAMPLE for r in SAMPLE)
step("4.8", "multiplication -- the ring core: a well-defined, commutative, distributive product",
     "(a,b)*(c,d) = (ac+bd, ad+bc) ; representative-independent ; 1=(1,0) ; distributes over +",
     ["4.2", "4.6"],
     "the product of two signed displacements, kept in Nat ((ac+bd)-(ad+bc), no subtraction). "
     "Its HEADLINE is well-definedness -- multiplication is genuinely an operation on the "
     "CLASSES, not on pairs (mul_congr). With +1=(1,0) as the unit, commutativity, and "
     "distribution over addition, the integers become a commutative RING -- multiplication is "
     "real, derived from the same construction as the sum.",
     "UNIQUE (well-definedness makes the class product unique)", "DERIVED",
     {"mul_congr": mul_congr_ok, "mul_one": mul_one_ok, "mul_comm": mul_comm_ok,
      "left_distrib": left_distrib_ok, "unit": list(PLUS_ONE)},
     check="product representative-independent, unit (1,0), commutative, left-distributive")
assert mul_congr_ok and mul_one_ok and mul_comm_ok and left_distrib_ok

# ---- 4.9 the order and the orientation -- DERIVED --------------------------
le_refl_ok = all(le_pair(p, p) for p in SAMPLE)
le_total_ok = all(le_pair(p, q) or le_pair(q, p) for p in SAMPLE for q in SAMPLE)
le_congr_ok = all((not (int_equiv(p, p2) and int_equiv(q, q2))) or (le_pair(p, q) == le_pair(p2, q2))
                  for (p, p2) in eqv for (q, q2) in eqv[:64])
# orientation: exactly one of  +positive | ~0 | -positive  holds for every integer.
def _tri(p):
    return (is_pos(p), int_equiv(p, ZERO), is_pos(neg_pair(p)))
trichotomy_ok = all(sum(_tri(p)) == 1 for p in SAMPLE)
pos_is_plus_dir = is_pos(PLUS_ONE) and (not is_pos(MINUS_ONE)) and (not is_pos(ZERO))
step("4.9", "the order and the ORIENTATION -- which direction is positive (trichotomy)",
     "(a,b) <= (c,d) iff a+d <= c+b ; isPos(a,b) := b < a ; exactly one of +,0,- per integer",
     ["4.3", "4.4"],
     "the order is a total order on the classes (reflexive, total, representative-independent). "
     "Its content for the floor is the ORIENTATION: isPos says which of the two directions is "
     "positive (the +1 direction), and the TRICHOTOMY -- every integer is positive, the "
     "counterpoint 0, or negative, exactly one -- is precisely how the two directions and the "
     "counterpoint partition the number line. This is the orientation OWED by step 4.4's "
     "'directions', now supplied.",
     "UNIQUE (a total order; the trichotomy is exhaustive and exclusive)", "DERIVED",
     {"le_refl": le_refl_ok, "le_total": le_total_ok, "le_congr": le_congr_ok,
      "trichotomy_exactly_one": trichotomy_ok, "positive_is_the_plus_direction": pos_is_plus_dir,
      "exclusivity_in_kernel": True},
     check="order total & representative-independent; +/0/- trichotomy is EXACTLY one per integer")
assert le_refl_ok and le_total_ok and le_congr_ok and trichotomy_ok and pos_is_plus_dir

# ---- 4.10 associativity of the product -- DERIVED --------------------------
assoc_ok = all(int_equiv(mul_pair(mul_pair(p, q), r), mul_pair(p, mul_pair(q, r)))
               for p in SAMPLE for q in [(1, 0), (2, 1), (0, 3), (3, 2)]
               for r in [(1, 0), (0, 2), (3, 1)])
step("4.10", "associativity of the product -- the last ring axiom, now mechanised -- DERIVED",
     "(p*q)*r ~ p*(q*r)", ["4.8"],
     "the product is associative: distributing and reassociating the triple products puts both "
     "sides over the same eight degree-3 monomials, a linear identity. Verified exactly over the "
     "sample here, and PROVED in the kernel (mulPair_assoc) -- the commutative-ring structure is "
     "now complete, no ring axiom left owed.",
     "UNIQUE (associativity is an identity)", "DERIVED",
     {"assoc_holds": assoc_ok, "built_in_kernel": True},
     check="(p*q)*r ~ p*(q*r) over the sample; kernel proof mulPair_assoc")
assert assoc_ok

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="04-integers", steps=STEPS, grades=GRADES,
           values=dict(sample_range=R, sample_size=len(SAMPLE),
                       distinct_classes=len(classes),
                       zero=list(ZERO), plus_one=list(PLUS_ONE), minus_one=list(MINUS_ONE),
                       all_have_inverse=all_have_inverse,
                       rung1_chain_length=rung1_count))

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
