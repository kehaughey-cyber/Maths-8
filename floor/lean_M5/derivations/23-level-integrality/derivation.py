#!/usr/bin/env python3
"""Container 23 -- LEVEL INTEGRALITY, cold on the triadic floor. Rests on 00, 01, 13.

Discharges container 22's owed_a (and owed_b): reconstruct Theorem LI -- the dcpo-floor
result rho(d) = I(d)/alpha = |A(d)|, "no element has a fractional level" -- on the TRIADIC
floor (container 00), where the substrate actually stands. This is the load-bearing leg of
Step 10's warrant condition (top-down meets bottom-up).

WHAT LI IS ON THE DCPO FLOOR (cited from `prime_framework_master_handoff.docx` sec 2-3.1,
QUARANTINED, read never as a premise): D is a directed-complete partial order with a real,
strictly-monotone, Scott-continuous information measure I (axiom R6). Theorem LI (from R13
atomisticity, R14 countable additivity, R10b valuation, R6) FORCES that real measure onto
integer multiples of alpha: I(d)/alpha is a positive integer = |A(d)|. It is a QUANTIZATION
theorem -- the work is dragging a continuum onto the integers. (Below a dcpo element of
"dimension >= 2" sits a continuum of order-atoms, so |A(d)| there means the cardinality of a
MAXIMAL ORTHOGONAL archon family -- a basis -- and "no fractional level" is "dimension is
well-defined".)

WHAT CHANGES ON THE TRIADIC FLOOR -- and it is the framework's own thesis made rigorous: the
triadic floor NEVER introduces a continuum. A registration element d is built by container
01's stepwise, POSITIVE, DISJOINT residual subdivision (01.1, 01.3): each step registers one
archon into the still-`undefined` residual. So A(d) is FINITE BY CONSTRUCTION, and the level
is its CARDINALITY from the start. Integrality stops being a theorem forcing reals onto Z and
becomes STRUCTURAL -- a count. The non-trivial content MOVES to where the triadic floor does
real work: well-definedness (path-independence of the count) and additivity. alpha stays OFF
the derived core (Stone 5's quarantined reading 17.S.3, Step 12).

  LI.1  the archon and the registration element on the triadic floor (atomisticity-cold).
  LI.2  the level L(d) := |A(d)| is well-defined, path-independent, an integer -- THE HEART.
        Integrality is free: a cardinality is a Nat, no continuum anywhere.
  LI.3  additivity L(a (+) b) = L(a) + L(b) on ORTHOGONAL (disjoint-residual) a, b -- with the
        overlapping case a CHECKED NEGATIVE (additivity needs orthogonality, is not vacuous).
  LI.4  the ball B_r is a registration element; L(B_r) = |B_r| (consumes container 13). The
        top-down level MEETS the bottom-up count -- discharges container 22's owed_b.
  LI.5  POSTULATE (quarantined): EAI-cold + the alpha-valuation. IF I(archon)=alpha and I is
        additive on orthogonal joins THEN I(d)=alpha*L(d), so I(d)/alpha=|A(d)| -- recovering
        the dcpo Theorem LI. Held off the derived core: EAI rests on the triad postulate and
        alpha is 17.S.3, Step 12 (container 22's owed_c, which stays owed).

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import itertools
import json
import sys
from itertools import combinations, permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ================================================================ the archon-set model
# The triadic floor's stepwise registration (container 01): a registration element is the
# set of archons registered into it. `insNew` is the positive, disjoint step (01.3): an
# archon is added only if it is fresh (still in the residual) -- never re-covering a defined
# thing. This is EXACTLY container 13's `insNew`/`union` idiom (one home for the operation).
def insNew(p, s):
    return s if p in s else s + [p]


def union(a, b):
    acc = list(a)
    for x in b:
        acc = insNew(x, acc)
    return acc


def L(s):                       # the level = the archon count = the cardinality of A(d)
    return len(s)


def build_from(order):          # build a registration element by a propagation sequence
    s = []
    for p in order:
        s = insNew(p, s)
    return s


# ---- LI.1 the archon / registration element (atomisticity-cold) -- DERIVED --------------
# A registration element is a finite join of archons; A(d) is its archon set. On the triadic
# floor the archon is container 00's level-0 primitive (the registration produced by the
# three-observer act), and container 01 builds every element by registering archons into the
# residual. So A(d) is a finite set by construction -- atomisticity holds without a lattice.
demo_elt = build_from([10, 20, 30, 40])
li1_ok = (L(demo_elt) == 4 and set(demo_elt) == {10, 20, 30, 40})
step("LI.1", "the archon and the registration element (atomisticity-cold, from 00 + 01)",
     "archon = container 00's level-0 registration primitive; a registration element d is a "
     "FINITE join of archons A(d), each registered into the residual (container 01)",
     ["00.2", "00.3", "01.1"],
     "the dcpo floor's Archon (an order-atom of D, p with nothing strictly between bottom and p) "
     "and its atomisticity axiom R13 (every d is the join of the archons below it) are recovered "
     "COLD, without a lattice or a measure. On the triadic floor the archon IS container 00's "
     "level-0 primitive -- the live registration produced by the three-observer act -- and "
     "container 01 builds every registration element by stepwise POSITIVE subdivision of the "
     "residual (01.1). So A(d), the set of archons composing d, is FINITE BY CONSTRUCTION: there "
     "is no continuum of sub-atoms as there is below a Hilbert-space projection. Atomisticity is "
     "structural here, not an axiom imposed on an abstract order.",
     "UNIQUE (A(d) is the set of archons registered into d)", "DERIVED",
     {"archon": "container 00 level-0 primitive (registration by three observers)",
      "registration_element": "a finite join of archons, built by 01's residual subdivision",
      "A(d)": "the archon set of d -- finite by construction (no continuum of sub-atoms)",
      "demo_element": demo_elt, "demo_level": L(demo_elt), "atomisticity_is_structural": True},
     check="a registration element is a finite archon set built by 01's stepwise subdivision")
assert li1_ok

# ---- LI.2 the level is a well-defined path-independent integer -- DERIVED (THE HEART) ---
# Build the SAME archon set by every propagation order; the level (and the set) must not depend
# on the order. This is the triadic "dimension is well-defined" -- where the dcpo floor's
# R13/R14/R10b did their labor. Integrality is then FREE: len(...) is a non-negative integer.
archs = [10, 20, 30, 40]
all_orders = list(permutations(archs))
built_lengths = {L(build_from(o)) for o in all_orders}
built_sets = {frozenset(build_from(o)) for o in all_orders}
path_independent = (built_lengths == {4} and len(built_sets) == 1)
# covering-cold: a FRESH step raises the level by exactly 1; re-adding a present archon does not
# (the covering property needs disjointness p meet d = bottom -- 01.3's disjoint residual).
cover_fresh = (L(insNew(99, archs)) == L(archs) + 1)
cover_idempotent = (L(insNew(10, archs)) == L(archs))     # 10 already present -> no increase
# integrality: the level is a Python int >= 0 -- a cardinality, not a real forced onto Z.
level_is_nonneg_int = isinstance(L(archs), int) and L(archs) >= 0
li2_ok = path_independent and cover_fresh and cover_idempotent and level_is_nonneg_int
step("LI.2", "the level L(d) := |A(d)| is well-defined, path-independent, an integer (THE HEART)",
     "L(d) = |A(d)|; every propagation sequence building d gives the same count (each fresh step "
     "+1, covering-cold); a cardinality is a Nat -- integrality is structural, no continuum",
     ["LI.1", "01.3"],
     "the reconstruction's heart, and where the dcpo floor's real-analysis machinery is NOT "
     "needed. WELL-DEFINEDNESS: all 24 propagation orders of a 4-archon element yield the same "
     "level 4 and the same set -- the level does not depend on the build order. This is the "
     "triadic analog of 'dimension is well-defined' (all maximal orthogonal families have equal "
     "cardinality), which is exactly what R13 + R14 + R10b bought on the dcpo floor. COVERING-COLD: "
     "a fresh archon raises the level by exactly 1 (01.3's positive disjoint residual), while "
     "re-adding a present archon does not -- so the covering property holds and needs disjointness. "
     "INTEGRALITY: L(d) is a CARDINALITY, a non-negative integer BY CONSTRUCTION. The dcpo LI had "
     "to force a real Scott-continuous measure I onto integer multiples of alpha; the triadic floor "
     "never introduced the continuum, so integrality is free. 'No element has a fractional level' "
     "becomes 'the level is a count' -- the framework's 'rho is a forced COUNT, no continuum, no "
     "free cutoff' thesis, made rigorous.",
     "UNIQUE (the level is the cardinality of A(d); path-independent)", "DERIVED",
     {"path_independent": path_independent, "orders_tried": len(all_orders),
      "all_orders_give_level": sorted(built_lengths), "distinct_sets_built": len(built_sets),
      "covering_fresh_plus_one": cover_fresh, "covering_idempotent_on_present": cover_idempotent,
      "level_is_nonneg_integer": level_is_nonneg_int,
      "integrality_is_structural_not_forced": True,
      "dcpo_needed": "R6 (real measure) + R10b + R14 to FORCE integrality; triadic needs none of it"},
     check="all propagation orders give one level (path-independent); fresh step +1; level is a Nat")
assert li2_ok

# ---- LI.3 additivity on orthogonal elements (+ overlap checked-negative) -- DERIVED -----
A = [1, 2, 3]
B = [4, 5, 6]                       # orthogonal (disjoint residual): additive
C = [1, 2, 3]
Dov = [3, 4]                        # overlapping: additivity FAILS (checked negative)
add_orthogonal = (L(union(A, B)) == L(A) + L(B))          # 6 == 3 + 3
add_overlap_fails = (L(union(C, Dov)) != L(C) + L(Dov))   # 4 != 3 + 2
li3_ok = add_orthogonal and add_overlap_fails
step("LI.3", "additivity L(a (+) b) = L(a) + L(b) on ORTHOGONAL a, b (overlap = checked negative)",
     "for disjoint-residual a, b: |A(a) union A(b)| = |A(a)| + |A(b)|; for overlapping a, b it "
     "FAILS -- so additivity is exactly the orthogonal case (R10b/R14 on the dcpo floor)",
     ["LI.2"],
     "the triadic recovery of R10b (valuation: I(a join b) = I(a) + I(b) for orthogonal a, b) and "
     "R14 (countable additivity over orthogonal families). Here it is pure cardinality of a "
     "DISJOINT union: two orthogonal registration elements (disjoint archon sets -- their residuals "
     "do not overlap, 01.3) compose with levels that ADD. The overlapping case is kept as a CHECKED "
     "NEGATIVE (the protocol's discipline): elements sharing an archon do NOT add (|{1,2,3} union "
     "{3,4}| = 4, not 5) -- so additivity is not vacuous; it holds PRECISELY on orthogonal pairs, "
     "which is what the dcpo valuation axiom also restricts to. This is the additivity leg the "
     "convergence condition (container 22, CV.2) needs, now cold on the triadic floor.",
     "UNIQUE (additivity holds exactly on orthogonal pairs)", "DERIVED",
     {"orthogonal_example": {"a": A, "b": B, "L(a|+|b)": L(union(A, B)), "L(a)+L(b)": L(A) + L(B),
                             "additive": add_orthogonal},
      "overlap_checked_negative": {"a": C, "b": Dov, "L(a|+|b)": L(union(C, Dov)),
                                   "L(a)+L(b)": L(C) + L(Dov), "additive": not add_overlap_fails},
      "additivity_needs_orthogonality": True},
     check="orthogonal levels add (disjoint union); overlapping levels do not (checked negative)")
assert li3_ok

# ---- LI.4 the ball is a registration element: L(B_r) = |B_r| -- DERIVED (owed_b) --------
# Recompute container 13's R1 icosahedron adjacency COLD (same construction as 13/22): edges =
# the pairs at the minimal squared distance 4 in Z[phi]. The ball B_r(v) is a registration
# element whose archons are the registrations within r adjacency steps; its LEVEL is |B_r|.
def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def sqdist(u, v):
    acc = (0, 0)
    for cu, cv in zip(u, v):
        dd = zsub(cu, cv)
        acc = zadd(acc, zmul(dd, dd))
    return acc


VERTS = []
for a in (1, -1):
    for b in (1, -1):
        VERTS.append(((0, 0), (a, 0), (0, b)))
        VERTS.append(((0, b), (0, 0), (a, 0)))
        VERTS.append(((a, 0), (0, b), (0, 0)))
VERTS = list(dict.fromkeys(VERTS))
R1_EDGES = sorted((i, j) for i, j in combinations(range(12), 2)
                  if sqdist(VERTS[i], VERTS[j]) == (4, 0))
ADJ = {i: set() for i in range(12)}
for i, j in R1_EDGES:
    ADJ[i].add(j)
    ADJ[j].add(i)


def ball_set(v, r):
    """The registration element B_r(v): archons within r adjacency steps, as a set (monotone
    growth -- container 13's `ballSet`/`expand`). Its LEVEL is its cardinality."""
    seen = {v}
    front = {v}
    for _ in range(r):
        nxt = set()
        for u in front:
            nxt |= ADJ[u]
        front = nxt - seen
        seen |= front
    return seen


ball_profiles = {v: [L(ball_set(v, r)) for r in range(4)] for v in range(12)}
# every vertex: L(B_r) = (1,6,11,12) -- the level of the ball IS container 13's |B_r|.
ball_is_level = all(p == [1, 6, 11, 12] for p in ball_profiles.values())
# and the level grows by the covering rule: each radius adds the fresh ring (disjoint front).
step("LI.4", "the ball B_r is a registration element; L(B_r) = |B_r| (consumes 13; owed_b)",
     "A(B_r(v)) = the registrations within r adjacency steps; L(B_r) = |A(B_r)| = |B_r(v)| -- the "
     "top-down level equals container 13's bottom-up count, on every R1 vertex",
     ["LI.2", "13.A.2"],
     "the identification container 22 named owed_b, now made. Container 13's ball-growth |B_r(v)| "
     "is a breadth-first archon COUNT over adjacency. Read the ball as a REGISTRATION ELEMENT "
     "d = B_r whose archons A(d) are exactly those registrations within r adjacency steps of v. "
     "Then LI.2 applies: L(B_r) = |A(B_r)| = |B_r| -- the level of the ball (top-down, I/alpha in "
     "the dcpo language) IS the bottom-up count (container 13). Recomputed cold on the R1 "
     "icosahedron (the same Z[phi] minimal-distance adjacency as 13), every vertex gives the "
     "profile (1, 6, 11, 12): L(B_0)=1, L(B_1)=6, L(B_2)=11, L(B_3)=12. Each radius adds the fresh "
     "ring (the disjoint front -- covering-cold, LI.2). So on this substrate the top-down level and "
     "the bottom-up count are the SAME integer, per vertex. This closes the identification leg of "
     "Step 10's warrant condition; only the alpha-link (LI.5) remains, quarantined.",
     "UNIQUE (the ball's level is its archon count = |B_r|)", "DERIVED",
     {"r1_ball_profiles_are_level": ball_is_level,
      "profile_every_vertex": [1, 6, 11, 12],
      "L(B_r)=|B_r|": "the ball read as a registration element; its level is container 13's count",
      "discharges": "container 22 owed_b (identify B_r with a registration element d)"},
     check="on the R1 icosahedron, every vertex has L(B_r) = (1,6,11,12) = container 13's |B_r|")
assert ball_is_level

# ---- LI.5 EAI-cold + the alpha-valuation -- POSTULATE (quarantined) ---------------------
step("LI.5", "EAI-cold + the alpha-valuation recovers the dcpo Theorem LI (POSTULATE, quarantined)",
     "IF every archon carries a common quantum alpha (EAI-cold) and I is additive on orthogonal "
     "joins, THEN I(d) = alpha * L(d), so I(d)/alpha = |A(d)| -- the dcpo Theorem LI, recovered",
     ["LI.2", "LI.3", "00.4", "17.S.3"],
     "the bridge from the count (derived, cold) to the dcpo floor's rho = I(d)/alpha -- kept OFF "
     "the derived core and graded POSTULATE, quarantined. On the dcpo floor Theorem EAI (all "
     "archons carry equal information alpha) was proved from R3/R8'/R6/R15, and R15 was itself "
     "under repair (R15a 'maybe provable' / R15b a NEW axiom). Cold on the triadic floor, EAI's "
     "content is: every archon is the SAME act -- one registered distinction by three observers, "
     "the identical local rule applied at every site (container 01's self-similar subdivision). So "
     "no archon can carry more than another; each carries one common quantum alpha. But this rests "
     "on the TRIAD POSTULATE (00.4/00.6, held not proven), and alpha itself is Stone 5's QUARANTINED "
     "reading (17.S.3), which cannot be a premise until grounded (Step 12, container 22's owed_c). "
     "GIVEN both, additivity (LI.3) gives I(d) = alpha * L(d), hence I(d)/alpha = |A(d)| = L(d) -- "
     "the dcpo Theorem LI recovered, now with its integrality leg DERIVED-cold (LI.2) and only the "
     "alpha-valuation held. This is the honest boundary: the count is proven; the ruler is owed.",
     "POSTULATE (EAI rests on the triad postulate; alpha is quarantined, Step 12)", "POSTULATE",
     {"eai_cold": "every archon = the same three-observer act (01's self-similar rule) -> equal quantum",
      "rests_on": "the triad postulate 00.4/00.6 (held, not proven)",
      "alpha_status": "Stone 5's quarantined reading 17.S.3 -- not a premise until Step 12",
      "if_granted": "I(d) = alpha * L(d) => I(d)/alpha = |A(d)| = L(d) (the dcpo Theorem LI)",
      "owed_c_remains": "the alpha grounding stays owed to Step 12 (stone-grounding)",
      # a HELD reading: it imports the quarantined alpha (17.S.3), so it is itself quarantined --
      # container 19's global check must see that NO derived step ever rests on it (none does).
      "downstream_premise_use": False,
      "present": False},
     check=None)

# ================================================================ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(
    container="23-level-integrality",
    steps=STEPS,
    grades=GRADES,
    values=dict(
        # LI.2 witnesses (the heart) -- guarded by the Lean
        path_independent=path_independent,
        all_orders_give_level=sorted(built_lengths),
        covering_fresh_plus_one=cover_fresh,
        covering_idempotent_on_present=cover_idempotent,
        level_is_nonneg_integer=level_is_nonneg_int,
        # LI.3 additivity witnesses
        additivity_orthogonal={"a": A, "b": B, "sum": L(union(A, B))},
        additivity_overlap_fails={"a": C, "b": Dov, "count": L(union(C, Dov)),
                                  "naive_sum": L(C) + L(Dov)},
        # LI.4 the ball tie (consumes 13) -- guarded by the Lean
        r1_ball_profile=[1, 6, 11, 12],
        r1_ball_is_level=ball_is_level,
        r1_edges=[list(e) for e in R1_EDGES],
        # the headline
        integrality_is_structural=True,
        warrant_leg_discharged="owed_a (LI cold on the triadic floor) + owed_b (B_r <-> d)",
        alpha_still_owed="owed_c (alpha grounding, Step 12) -- LI.5 POSTULATE, quarantined",
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
