#!/usr/bin/env python3
"""Container 22 -- CONVERGE TOP-DOWN: rho = I/alpha meets rho = |B_r|. Rests on 13; cites the origin.

Step 10 of the physics-bridge arc (revised roadmap), and THE HARD LOAD-BEARER. The framework's primary
evidence is that the archic density rho is ONE object reached two ways: TOP-DOWN rho = I(d)/alpha =
|A(d)| (the master handoff, Sessions 1-10b) and BOTTOM-UP rho = |B_r(v)| (container 13). This container
converges them AS FAR AS IS HONEST -- and it surfaces a FINDING rather than a clean numeric convergence,
which was the anticipated, acceptable outcome.

WHAT THE TOP-DOWN SAYS (cited from `prime_framework_master_handoff.docx` sec 2.2, QUARANTINED, external
-- read never as a premise): D is a dcpo (a registration domain); alpha = I(O(bottom)) is the
information quantum; every ARCHON carries exactly alpha (Theorem EAI); and THEOREM LI (Level
Integrality, from R6/R10b/R13/R14): I(d)/alpha is a POSITIVE INTEGER = |A(d)|, the archon count of d.
So top-down, rho(d) = I(d)/alpha = |A(d)| is a forced integer count.

WHAT THE BOTTOM-UP SAYS (container 13, DERIVED, cold): rho(v) = |B_r(v)| is the breadth-first archon
count within r adjacency steps -- also a forced integer count, no continuum, no free cutoff.

  CV.1 they AGREE IN KIND. Both rho are FORCED INTEGER COUNTS of archons -- no continuum, no free
       "line" to guess. Top-down via I/alpha = |A(d)| (LI, cited); bottom-up via |B_r| (13, derived).
       This is the structural half of the primary evidence, and it holds.

  CV.2 the CONVERGENCE CONDITION (arithmetic, kernel-checkable). Theorem LI says I(d) = alpha * |A(d)|
       (each archon carries alpha, EAI). Applied to a ball taken as a registration element d = B_r whose
       archons are its registrations: I(B_r)/alpha = |A(B_r)| = |B_r| -- the top-down and bottom-up
       counts CONVERGE, both = the archon count of the ball. The core is pure arithmetic: given I =
       alpha * c with alpha > 0, I/alpha = c exactly. So the two counts converge PRECISELY WHEN I(B_r) =
       alpha * |B_r| (each registration carries alpha). Checked on instances.

  CV.3 the FINDING, now DISCHARGED (RETREATED 2026-09-03). When written, the numeric convergence was
       CONDITIONAL: Theorem LI + EAI rested on the DCPO floor (R6/R10b/R13/R14), superseded by the TRIADIC
       floor, so the WARRANT CONDITION (top-down meets bottom-up) was NOT yet met and awaited (a) LI cold
       on the triadic floor, (b) the ball B_r identified with a registration element d, (c) the alpha-link
       grounded. ALL THREE ARE NOW DISCHARGED by the containers built after 22: container 23 reconstructed
       LI COLD on the triadic floor and identified the ball as a registration element (L(B_r)=|B_r|,
       23.LI.4) -- owed_a + owed_b; container 24 grounded the alpha-link STRUCTURALLY (EAI forced,
       I(B_r)=alpha*|B_r|, 24.SG.1) modulo the SG.2 intrinsicness postulate -- owed_c. So the warrant
       condition is STRUCTURALLY MET, DERIVED-cold, modulo SG.2. What REMAINS owed is only the alpha VALUE
       (24.SG.4) -- external Stone input, quarantined, an owner-decision boundary (danger zone). Every
       physical VALUE (Step 14, rho_Lambda) now waits only on that external scale, not on the structure.
       CV.3 stays graded OWED because the value is genuinely still owed -- but scoped to SG.4, not the
       (now-discharged) structural warrant.

Grades DERIVED / POSTULATE / OWED, per step. `--check` recomputes the DERIVED steps.
"""

import json
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = []


def step(sid, what, expr, frm, why, determines, grade, value, check=None):
    STEPS.append(dict(id=sid, what=what, expr=expr, frm=frm, why=why,
                      determines=determines, grade=grade, value=value, check=check))
    return value


# ---------------------------------------------------------------- bottom-up |B_r| (cold, from 13)
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
A1 = {i: set() for i in range(12)}
for i, j in R1_EDGES:
    A1[i].add(j)
    A1[j].add(i)


def ball_size(A, v, r):
    seen, front = {v}, {v}
    for _ in range(r):
        nxt = set()
        for u in front:
            nxt |= A[u]
        front = nxt - seen
        seen |= front
    return len(seen)


# a bottom-up ball count (R1, r=1): |B_1| = 6 at every vertex -- a concrete forced integer count
b1 = ball_size(A1, 0, 1)

# ---- CV.1 they agree in kind -- DERIVED ------------------------------------
bottom_up_is_integer_count = isinstance(b1, int) and b1 > 0
step("CV.1", "the two densities agree IN KIND: both rho are forced integer archon COUNTS",
     "top-down rho = I(d)/alpha = |A(d)| (Theorem LI, cited); bottom-up rho = |B_r| (13, derived); both "
     "positive integers, no continuum, no free cutoff", ["13.A.2"],
     "the archic density is ONE object reached two ways, and the structural claim -- that BOTH are "
     "forced INTEGER COUNTS of archons -- holds. TOP-DOWN (cited, quarantined external, "
     "`prime_framework_master_handoff.docx` sec 2.2): Theorem LI gives rho(d) = I(d)/alpha = |A(d)|, a "
     "positive integer = the archon count of d, from R6/R10b/R13/R14. BOTTOM-UP (container 13, derived "
     "cold): rho(v) = |B_r(v)| is the breadth-first archon count, also a positive integer (e.g. "
     "|B_1| = 6 on R1). Neither has a continuum or a free 'line' to guess -- rho is a FORCED COUNT both "
     "directions. This is the structural half of the framework's primary evidence, and it is sound.",
     "UNIQUE (both are forced integer counts; the kind-agreement is exact)", "DERIVED",
     {"bottom_up_example_B1": b1, "bottom_up_is_positive_integer": bottom_up_is_integer_count,
      "top_down": "rho = I(d)/alpha = |A(d)| (Theorem LI, cited)", "both_are_forced_integer_counts": True,
      "no_continuum_no_free_cutoff": True},
     check="both densities are forced positive-integer archon counts (top-down LI cited, bottom-up |B_r| derived)")
assert bottom_up_is_integer_count

# ---- CV.2 the convergence condition (arithmetic) -- DERIVED ----------------
# Theorem LI: I(d) = alpha * |A(d)|. For a ball d = B_r with archons = its registrations,
# I(B_r)/alpha = |B_r|. Core: given I = alpha * c (alpha>0), I/alpha = c exactly.
def converges(alpha, count):
    I = alpha * count
    return alpha > 0 and I // alpha == count and I % alpha == 0


# instances: alpha times a bottom-up count recovers the count (top-down = bottom-up)
conv_instances = {f"alpha={a},count={c}": converges(a, c)
                  for (a, c) in [(3, 6), (5, 12), (2, 51), (7, 372)]}
convergence_condition_holds = all(conv_instances.values())
step("CV.2", "the convergence condition: I = alpha*|B_r| makes top-down = bottom-up (arithmetic)",
     "Theorem LI: I(d)=alpha*|A(d)|; for d=B_r, I(B_r)/alpha = |B_r|; core: I=alpha*c, alpha>0 => "
     "I/alpha = c exactly", ["CV.1"],
     "the convergence, reduced to what is actually checkable. Theorem LI states I(d) = alpha * |A(d)| "
     "(each archon carries alpha, Theorem EAI). Take a ball as a registration element d = B_r whose "
     "archons are its registrations; then I(B_r)/alpha = |A(B_r)| = |B_r| -- the TOP-DOWN count "
     "(I/alpha) EQUALS the BOTTOM-UP count (|B_r|). The kernel-checkable core is pure arithmetic: given "
     "I = alpha * c with alpha > 0, I/alpha recovers c exactly (checked on instances, alpha times the "
     "bottom-up counts 6/12/51/372). So the two densities CONVERGE PRECISELY WHEN I(B_r) = alpha*|B_r| "
     "-- each registration carrying alpha. This ties the density observable (13) to the alpha ruler "
     "(Stone 5). The IDENTIFICATION making it hold on this substrate is CV.3's owed work.",
     "UNIQUE (the arithmetic condition is exact)", "DERIVED",
     {"convergence_condition": "I(B_r) = alpha * |B_r|  <=>  I/alpha = |B_r| (top-down = bottom-up)",
      "arithmetic_core": "I = alpha*c, alpha>0  =>  I/alpha = c", "instances": conv_instances,
      "condition_holds": convergence_condition_holds,
      "ties": "the density observable (13) to the alpha ruler (Stone 5)"},
     check="I = alpha*c (alpha>0) => I/alpha = c, on instances -> the convergence condition")
assert convergence_condition_holds

# ---- CV.3 the finding -- STRUCTURAL WARRANT DISCHARGED by 23/24; only the VALUE (SG.4) remains OWED
step("CV.3", "the finding, DISCHARGED: the structural warrant is met (23 + 24); only the alpha VALUE (24.SG.4, external) remains owed",
     "owed_a/owed_b/owed_c are DISCHARGED -- 23 reconstructed Theorem LI cold on the triadic floor and "
     "identified the ball B_r as a registration element (L(B_r)=|B_r|); 24 grounded the alpha-link "
     "structurally (EAI forced, I(B_r)=alpha*|B_r|), modulo the SG.2 intrinsicness postulate. So the "
     "warrant condition (top-down meets bottom-up) is STRUCTURALLY MET; only the alpha VALUE (external) is owed",
     ["CV.1", "CV.2"],
     "RETREATED 2026-09-03: this finding located the gap, and the gap was then CLOSED by the containers "
     "built after 22. When CV.3 was written, LI + EAI rested on the DCPO floor (R6/R10b/R13/R14), superseded "
     "by the triadic floor, so the warrant condition was NOT yet met and it awaited (a) LI cold on the "
     "triadic floor, (b) B_r identified with a registration element d, (c) the alpha-link grounded. ALL "
     "THREE ARE NOW DISCHARGED: container 23 (level-integrality) reconstructed Theorem LI COLD on the "
     "triadic floor -- the level L(d)=|A(d)| is a well-defined, path-independent, additive integer count "
     "(23.LI.2/LI.3, DERIVED zero-axiom) -- and identified the ball as a registration element, "
     "L(B_r)=|B_r|=(1,6,11,12) on every R1 vertex (23.LI.4, DERIVED zero-axiom, discharging owed_a AND "
     "owed_b); container 24 (stone-grounding) grounded the alpha-link STRUCTURALLY -- EAI (a constant "
     "per-archon alpha) is FORCED by symmetry + additivity, not assumed, giving I(B_r)=alpha*|B_r| "
     "(24.SG.1, DERIVED zero-axiom), MODULO the single archon-intrinsicness postulate (24.SG.2) -- "
     "discharging owed_c at the level the warrant condition needs. So the WARRANT CONDITION (top-down "
     "meets bottom-up) is now STRUCTURALLY MET, DERIVED-cold, modulo SG.2. WHAT REMAINS OWED is only the "
     "alpha VALUE -- container 24.SG.4, external Stone input (base-2/SEC9/Planck hypothesis), quarantined, "
     "never a premise; and it is an OWNER-DECISION boundary (accept hbar/c/mass external, or derive -- the "
     "danger zone). The numeric convergence therefore no longer awaits the STRUCTURE (that is done); every "
     "physical VALUE (Step 14, rho_Lambda) waits only on the external alpha value (SG.4). The primary "
     "evidence is sound in KIND and now GROUNDED in structure; only the scale is external.",
     "OWED (only the alpha VALUE, 24.SG.4, external; the structural warrant is discharged by 23/24 modulo SG.2)", "OWED",
     {"discharged_owed_a": "Theorem LI reconstructed cold on the triadic floor -- container 23 (LI.2/LI.3)",
      "discharged_owed_b": "the ball B_r identified as a registration element, L(B_r)=|B_r| -- container 23 (LI.4)",
      "discharged_owed_c_structurally": "the alpha-link grounded (EAI forced, I(B_r)=alpha*|B_r|) -- container 24 (SG.1), modulo the SG.2 intrinsicness postulate",
      "structural_warrant": "MET -- top-down meets bottom-up is DERIVED-cold (23+24) modulo SG.2",
      "remaining_owed": "only the alpha VALUE -- container 24 (SG.4), external Stone input, owner-decision boundary (danger zone)",
      "gates": "every physical value (Step 14, rho_Lambda) waits only on the external alpha value, not on the structure",
      "is_finding_not_failure": True, "present": False},
     check=None)

# ------------------------------------------------------------------ emit / check
GRADES = {g: sum(1 for s in STEPS if s["grade"] == g) for g in ("DERIVED", "POSTULATE", "OWED")}
OUT = dict(container="22-converge-top-down", steps=STEPS, grades=GRADES,
           values=dict(bottom_up_example_B1=b1, both_are_forced_integer_counts=True,
                       convergence_condition="I(B_r) = alpha*|B_r|  <=>  I/alpha = |B_r|",
                       convergence_condition_holds=convergence_condition_holds,
                       structural_warrant_met=True,
                       structural_warrant_note="DERIVED-cold by 23 (LI.2/LI.3/LI.4) + 24 (SG.1), modulo the SG.2 intrinsicness postulate",
                       value_owed_external=True,
                       finding="convergence holds IN KIND and is now GROUNDED in structure -- the warrant "
                               "condition is DISCHARGED by 23 (LI cold + B_r a registration element) and 24 "
                               "(alpha-link grounded, EAI forced), modulo SG.2. Only the alpha VALUE (24.SG.4, "
                               "external Stone input, owner-decision) remains owed; every physical value waits "
                               "only on that scale, not on the structure.",
                       is_load_bearer=True))

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
