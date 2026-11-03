# SPINE with proofs, Maths 8: from the 00 floor to the current frontier (2026-11-03)

Authored by Claude (Sonnet 5.5). Not independently reviewed. This is one file: the spine of `SPINE_M8_2026-11-03.md` with, under each part, the equations and proofs of that part's claims (copied from `SPINE_M8_PROOFS_2026-11-03.md`; assembled by `explore/build_unified_spine.py` from that file, the spine, and three small hand-written pieces in `explore/unified_spine_*.md`, so the files cannot drift apart silently). Nothing here replaces the files it cites. Where a claim is the floor's it keeps the floor's grade; where it is Maths 8's it is graded by what was actually run. Older words ("archic", "archon") are written "registration" (`notes/terminology.md`); floor files keep the old words.

## How a claim is carried here, and what "proved" means
Each claim sits next to one of four things, and the label says which:
- **LEAN**: the floor's formal statements for nodes 00 to 67, as Lean 4 proofs imported from Maths 5 and compiled in this repository (71 of 71 modules, no `sorry`, no axiom declarations). The kernel accepts each theorem *as stated*; whether the stated theorem is the whole of the node's prose claim is not assessed.
- **PROVED / CHECKED**: a derivation written out in the entry, and its identities verified independently by a script (`explore/spine_proofs_check.py`, 71 PASS; `explore/spine_route56_check.py`, PASS).
- **COMPUTED**: a number from a named script with a committed `.out` and a sha256; reproduces by `explore/reproduce.py`. Computed is a result, not a proof.
- **NOT CARRIED**: the proof is not in this repository; the entry says where the evidence lives. These are listed in one place at the end (Part IX).

**To verify everything that can be verified from this repository** (from the repository root; NumPy, SymPy, mpmath only, Lean 4.33.0-rc1 for the first line):
```bash
py -3 -I -X utf8 -u explore/lean_M5_check.py --pkgs "<Maths 5>/lean/.lake/packages" > explore/lean_M5_check.out
py -3 -I -X utf8 -u explore/spine_proofs_check.py > explore/spine_proofs_check.out
py -3 -I -X utf8 -u explore/spine_route56_check.py > explore/spine_route56_check.out
py -3 -I -X utf8 -u explore/reproduce.py
```
The last line re-runs every explore script that has a committed `.out`, against a fresh export of HEAD.

---

## 0. What this spine serves, and how to read it

**The contract** (`QUESTION.md`, the blockquote only; the rest of that file is commentary the human did not approve): derive how amplitude (Hilbert), geometry (spacetime), probability (the overlap) and the force-gradings each arise as readings of the one recursive act of observation and being, so as to reproduce what has been touched in QIT, QFT and GR, and to yield manipulable handles on mass, space, time and the forces.

**The only two tests:** is the math true, and does it match the universe. SM, GR and QM are comparison surfaces, not the bench. No walls: an archived warning has a scope and is never a general prohibition. No prediction ceremony: state what the math gives and whether it matches.

**What "handles" means** (the human, 2026-11-02): tunable levers on mass, space and time, not mainly exact derived values. Understanding first (a common language, a map of maps), then the applicable understanding that lets others act. Specific engineering (materials, fields in teslas) is not the current work.

**One substance** (the human, 2026-11-02): mass, energy, space, time, clocks, scale and field are readings of one changing substance. Never order them as a chain; never chase one against another. The test is cross-reading consistency under one calibration. Take "both" over a false dichotomy; mark every pre-set choice as open.

**Grades used below.**
- FLOOR: inherited from Maths 5/6, immutable, graded by its own source (DERIVED, POSTULATE, REDUCTION, HELD, OPEN). Cited by node and the sha256 in `floor/PROVENANCE.md`.
- COMPUTED: computed in this repository, script and raw `.out` committed.
- MEASURED: a sourced experimental value, with the source in `explore/data/` or the note. Several are secondary (search summaries); each note says so.
- SCOPED: true under a stated construction only.
- WITHDRAWN: said earlier, found wrong or mis-scoped, corrected append-only (the original is kept).
- OPEN: not done.

---

## I. The floor, rung 0 to 2 (the three containers)

Each carries its own grades; nothing below is stronger than they say. Source: `floor/container_00_distinction.md`, `container_01_recursive_registration.md`, `container_02_registration_event.md`.

**00, the distinction.** DERIVED (zero axioms, kernel-checked): three existential states (defined, undefined-existent, non-existent) are distinct, and undefined is not non-existent; exactly the two existent states are perceivable; a distinction selects its state and its residual positively, so there is no negation on the floor; a distinction needs both a defined and an undefined side. POSTULATE: registration 1 is the existence bound (all-that-is against non-existence, which does not exist); a distinction is registered by three observers, two within and one without, whose live agreement is the registration; that all three are present at registration 1 is the human's working hypothesis and the structure does not force it. OWED at the time: adjacency forces 12, hence the icosahedron. Not claimed: time, space, number, geometry.

**01, recursive registration.** DERIVED: each later registration subdivides the residual of all-that-is; each is a container-00 distinction; the residual nests (what is defined stays defined, the undefined residual only shrinks). POSTULATE: co-definition is by adjacency, live and stepwise (inject spreads one ring at a time); identity is the live web, read off adjacency and never stored; the triad carries up. The owed 12 was largely discharged downstream (nodes 03, 09, 11 force the closed triangular trichotomy and the icosahedron and achieve kissing 12); what remains is the substrate-native metric no-thirteenth, the same single open item as 03.3.7, 09.6.6 and 25.DF.3.

**02, the registration event.** DERIVED: an event turns a potential distinction into a stable one (the first change the floor carries; no time claimed); observer and observed co-emerge; the triad as arithmetic: n rotations vs n! permutations coincide only for n = 1, 2, so a cyclic order turns, and a rotation differs from a permutation, first at n = 3 (proved for n = 1 to 8); the event's stable product is a distinction. POSTULATE: the third observer registers the change (the reading; the arithmetic is the skeleton). OWED: the phase cycle's capacity gives 12.

### Equations and proofs for Part I (container 00 to 02)

The Lean originals of these three containers are among the imported modules (Part II table, rows 00 to 02); the entries below are the same claims proved in elementary form so a reader can check them without Lean.

#### C-A1 (container 00, 0.2) Three existential states; undefined ≠ non-existent; only existent states are perceivable
*Statement.* Let E = {D, U, N} (defined-existent, undefined-existent, non-existent) be a three-element set with distinct elements. Define `perceivable(x) :⇔ x ≠ N`. Then D ≠ U, U ≠ N, D ≠ N; `perceivable(D)`, `perceivable(U)`, ¬`perceivable(N)`.
*Proof.* The three constructors of an inductive type are pairwise distinct (no-confusion). The predicate is the stated definition; the three evaluations follow from the pairwise distinctness. ∎
*Status.* PROVED (trivial). The substantive content of 0.2 is the *definition*: that "undefined" is a third value and not the negation of "defined". That is a modelling choice, stated in the floor as POSTULATE-tier reading.

#### C-A2 (0.3, 0.5) A distinction carries no is-not; both poles are required
*Statement.* Let a base B be a finite set and `status : B → {defined, undefined}` a function. State := {x : status x = defined}; Residual := {x : status x = undefined}. (i) State ∩ Residual = ∅ and State ∪ Residual = B. (ii) The pair (State, Residual) is a distinction in the sense of container 00 iff both are non-empty.
*Proof.* (i) `status` is a function, so no x has both values, which gives disjointness without using negation; the union is B because the codomain has two values. (ii) If Residual = ∅ then every x is defined and there is nothing to distinguish State from; if State = ∅ then no thing is defined and there is no state. The definition of distinction requires a state and a residual to select, so both must be non-empty. ∎
*Status.* PROVED (definitional). The floor's *non-existence* appears only as the bound of registration 1 (a POSTULATE) and is not an element of B.

#### C-A3 (container 01, 1.3) The residual nests
*Statement.* Let status_0, status_1, … be a sequence of status functions on a fixed B with the rule "defined stays defined": status_n(x) = defined ⇒ status_{n+1}(x) = defined. Then Residual_{n+1} ⊆ Residual_n for all n, and State_n ∩ Residual_m = ∅ for m ≥ n.
*Proof.* x ∈ Residual_{n+1} ⇒ status_{n+1}(x) = undefined ⇒ (contrapositive of the rule) status_n(x) = undefined ⇒ x ∈ Residual_n. For the second claim, x ∈ State_n ⇒ x ∈ State_m for m ≥ n (induction on the rule) ⇒ x ∉ Residual_m by C-A2(i). ∎
*Status.* PROVED. The rule itself is the floor's postulate (1.3 "what is defined stays defined").

#### C-A4 (container 02, 2.3) The triad as arithmetic: rotations vs permutations
*Statement.* For n ≥ 1 points: (a) n! = n iff n ∈ {1, 2}; (b) a cyclic order on n distinct labels equals its own reversal as a cyclic order iff n ≤ 2. Hence a cyclic order "turns" (is distinguishable from its mirror) iff n ≥ 3.
*Proof.* (a) n! = n·(n−1)!, so n! = n iff (n−1)! = 1 iff n−1 ∈ {0, 1} (for m ≥ 2, m! ≥ m ≥ 2 by induction). (b) Write the cyclic order as (a_0, …, a_{n−1}); its reversal is b_i = a_{−i mod n}. A rotation by t gives c_i = a_{i+t}. Since labels are distinct, b = c as sequences iff −i ≡ i + t (mod n) for every i, i.e. 2i ≡ −t for all i. Taking i = 0 and i = 1 gives 2 ≡ 0 (mod n), so n divides 2: n ∈ {1, 2}. Conversely for n ≤ 2 the reversal is a rotation. ∎
*Check.* `spine_proofs_check.out` P1 (n! = n for n = 1…12: only 1, 2).
*Status.* PROVED here and checked. The *identification* of the n = 3 rank transition with "the third observer registers change" is the floor's POSTULATE (2.4) and is not claimed proved.

---

## II. The M5 trunk, nodes 03 to 67 (floor; read the node tables in the spine files, not here)

Full node table with grades and current distinctions: `floor/M6_SPINE_2026-10-19.md` (sections I to III) and the original `floor/M5_SPINE_10-9-26.md`. In outline, with the node ranges:

- **03 to 12, geometry from counting.** Dimensional emergence (with retractions and repairs; read 41 to 43), integers, the geometric bridge (Gram form (D/2)(I+J)), the exact golden-field carrier 2I (node 06: 120 units, the binary icosahedral group, the 600-cell vertices), ordinal and metric dynamics, kissing twelve, the icosahedron, the E8 roots from the icosians (240).
- **13 to 27, density, gravity, scale.** Registration density ρ(v) = |B_r(v)| (13); the density deficit 12 − 2d and total 12χ (14); extremal density at twelve (15); the frustration ε = 2π − 5 arccos(1/3) > 0 (16, DERIVED flat geometry, persistence engine POSTULATE); the Stone–Bekenstein–Compton ruler 2πRE/(ħc ln2) (17); the Planck anchor (18, an external bridge); per-edge density gradient as gravity (20, POSTULATE identification); integer levels (23); a common weight I = αL up to scale (24); counting growth exponent 2 (25); base 2 (26); dimensionless substrate with ħ, c, G as the three anchors (27).
- **28 to 45, forces and spin.** Weak SU(2) from quaternion brackets (28); EM U(1) from phase and signed defect, coupling owed (29); strong SU(3) as A2 in E8 (30); colour seating, order-three action 6 fixed + 38 three-cycles (31); one 2π phase cycle (32); the Planck-anchored c is reproduced by construction, so non-discriminating (33); vacuum value open (34, 35); negative curvature, geodesic motion, deflection (36 to 40); the single-SU(2) reduction and the held norm hinge (41 to 43); chirality (44); the spinor sign 2π → −I, 4π → I (45).
- **46 to 67, spacetime, content, tick.** Signature, focusing, CPT (46 to 49); electroweak mixing and the gauge product (50, 51); continuum limit (52, owed analytic bridge); quantum kinematics (53); the Born hinge (55, HELD, strengthened in M6: the unique SO(4)-invariant positive form on quaternionic amplitudes is norm²); matter census (56); Weinberg-angle reduction (57, a naive one-half fails); Z6 hypercharge grading (58); content selection (59, 60); K2 surface tests (61, 62); the Coxeter bridge C = L_aR_b with orders 5 and 6, order 30 (64); four 30-clocks, 288/480 ticks (65); the arbiter seating 13/13/4, lag 81 (66); conjugation and generation census, 24 involutions (67).

The floor's physical contacts are comparison surfaces: counts and isomorphisms need represented dynamics before they are physics (M6 §R).

### Proofs for Part II (nodes 00 to 67): the Lean proofs of record

**Source and provenance.** `floor/lean_M5/lean/` holds byte copies of the Maths 5 Lean sources (`floor/lean_M5/PROVENANCE.md`; `MANIFEST.sha256` lists the sha256 of each of the 210 copied files, compared with the source at copy time, 0 mismatches). Only proofs and derivation scripts were imported; no rules, protocol, grading or prohibitions were.

**How compiled.** `py -3 -I -X utf8 -u explore/lean_M5_check.py --pkgs "<Maths 5>/lean/.lake/packages" [--skip Container05,Container06] > explore/lean_M5_check.out` (and `--only Container05`, `--only Container06` with a long timeout for the two heavy modules, outputs `explore/lean_M5_check_05.out`, `explore/lean_M5_check_06.out`). Toolchain: Lean 4.33.0-rc1 (the version named in the copied `lean-toolchain`), called directly; Mathlib and dependencies from the oleans already built in Maths 5 (read-only). Modules are compiled in import order; each file's messages are scanned for errors and `#print axioms` lines.

**Result.** All 71 modules compile with 0 failures: 68 in the main parallel pass (`explore/lean_M5_check.out`), `Container05.EquidistantDimensionReal` and `Container05.GeometricBridge` (`explore/lean_M5_check_05.out`), and `Container06.Ring` (`explore/lean_M5_check_06.out`; slow by design, it proves the E8 identity of the icosian Gram matrix by kernel `decide` on 8×8 determinants, with `set_option maxHeartbeats 4000000` in the source). No file contains `sorry`, and none declares an `axiom`. The `#print axioms` output shows three footprints: no axioms at all; `[propext, Quot.sound]`; and, for the Mathlib-importing files, `[propext, Classical.choice, Quot.sound]` (the standard Mathlib three). A first attempt that compiled serially with a 900 s limit timed out on `Container05.EquidistantDimensionReal` and `Container06.Ring` and was stopped; the parallel runner replaced it (that serial output was overwritten). In the table, node 05 appears twice (two modules).

**What "compile" means.** The Lean kernel accepts every theorem in these files as stated. The statements are in `floor/lean_M5/DECLARATION_INDEX.md` (signatures, comments omitted) and in the sources. The per-node table below lists, for each node, the claim text from the M6 spine's claim column, the Lean module, how many theorem/lemma declarations it has, the compile result, and the axiom footprint of the theorems that print one.

**Correspondence with the elementary proofs above.** C-A1 (three existential states) is `Container00.undefined_ne_nonexistent`, `defined_perceivable`, `undefined_perceivable`, `nonexistent_not_perceivable`; C-A2 (both poles) is `base_is_distinction`, `all_defined_is_not_a_distinction`, `none_defined_is_not_a_distinction`; C-A3 and C-A4 correspond to the theorems of Containers 01 and 02. C-B1 (the 120 icosians as an E8 Gram of determinant 256) corresponds to `Container06.gram_determinant_is_256`, `halfGram_is_unimodular`, `icosian_ring_is_E8` and the embedding theorems.

<!-- BEGIN LEAN NODE TABLE (generated by explore/lean_M5_nodes.py from explore/lean_M5_check*.out) -->
| node | name | claim (M6 spine claim column) | Lean module | theorems | compile | axiom footprint of the checked theorems |
|---|---|---|---|---|---|---|
| 00 | distinction | Triad: two within, one without; undefined existence differs from nonexistence. | `Container00.Distinction` | 7 | OK | none (zero axioms) |
| 01 | recursive-registration | Recursive subdivision; live adjacent co-definition and cascading changes. | `Container01.RecursiveRegistration` | 5 | OK | none (zero axioms) |
| 02 | registration-event | Actualization through contextual registration and observer roles. | `Container02.RegistrationEvent` | 8 | OK | none (zero axioms) |
| 03 | dimensional-emergence | Triangulation/clique closure and dimensional constraints. | `Container03.DimensionalEmergence` | 7 | OK | {Classical.choice, Quot.sound, propext} (5 theorems axiom-free) |
| 04 | integers | Counts/order give natural numbers and additive inverses. | `Container04.Integers` | 23 | OK | {Quot.sound, propext} (8 theorems axiom-free) |
| 05 | geometric-bridge | Polarization produces Gram form `(D/2)(I+J)`. | `Container05.EquidistantDimensionReal` | 5 | OK | {Classical.choice, Quot.sound, propext} |
| 05 | geometric-bridge | Polarization produces Gram form `(D/2)(I+J)`. | `Container05.GeometricBridge` | 9 | OK | none (zero axioms) |
| 06 | carrier-2i | Exact golden-field construction of 120 units. | `Container06.Ring` | 9 | OK | no `#print axioms` in the file |
| 07 | ordinal-dynamics | Successive changes constitute history. | `Container07.Dynamics` | 6 | OK | none (zero axioms) |
| 08 | metric-dynamics | Ordinal walk gains a metric trajectory through05. | `Container08.MetricDynamics` | 14 | OK | none (zero axioms) |
| 09 | kissing-twelve | Icosahedral kissing witness/field-norm transfer. | `Container09.KissingTwelve` | 6 | OK | none (zero axioms) |
| 09 | kissing-twelve | Icosahedral kissing witness/field-norm transfer. | `Container09.SurfaceSlackReal` | 3 | OK | {Classical.choice, Quot.sound, propext} |
| 10 | why-twelve | Twelvefold angular closure and registration arithmetic. | `Container10.PhaseLedgerReal` | 5 | OK | {Classical.choice, Quot.sound, propext} |
| 10 | why-twelve | Twelvefold angular closure and registration arithmetic. | `Container10.WhyTwelve` | 5 | OK | none (zero axioms) |
| 11 | icosahedron | Icosahedral realization/no-thirteenth in the stated metric. | `Container11.Icosahedron` | 8 | OK | none (zero axioms) |
| 12 | e8-roots | Icosian construction realizes 240 E8 roots. | `Container12.E8Roots` | 4 | OK | none (zero axioms) |
| 13 | archic-density | `ρ(v)=|B_r(v)|`, adjacency-ball count. | `Container13.ArchicDensity` | 6 | OK | none (zero axioms) |
| 14 | density-deficit | Reference `1+3r(r+1)`; angular count `12−2d`, total12χ. | `Container14.DensityDeficit` | 4 | OK | none (zero axioms) |
| 15 | density-extremum | Extremal density directions at twelve/anti-twelve. | `Container15.DensityExtremum` | 4 | OK | none (zero axioms) |
| 16 | frustration-dynamo | `ε=2π−5 arccos(1/3)>0`. | `Container16.FrustrationDynamo` | 3 | OK | none (zero axioms) |
| 17 | stone-bekenstein-compton | Information/energy ruler `2πRE/(ℏc ln2)`. | `Container17.StoneBekensteinCompton` | 3 | OK | none (zero axioms) |
| 18 | stone-planck-anchor | Planck crossover/anchor. | `Container18.StonePlanckAnchor` | 5 | OK | none (zero axioms) |
| 19 | entry-protocol | Provenance and substrate/physics correspondence infrastructure. | `Container19.EntryProtocol` | 2 | OK | none (zero axioms) |
| 20 | density-gradient | Per-edge density/deficit gradient; gravity reading. | `Container20.DensityGradient` | 3 | OK | none (zero axioms) |
| 21 | entry-gravity-curvature | Deficit/curvature comparison and integral count. | `Container21.EntryGravityCurvature` | 2 | OK | none (zero axioms) |
| 22 | converge-top-down | Information and archon-count convergence under a warrant. | `Container22.ConvergeTopDown` | 2 | OK | none (zero axioms) |
| 23 | level-integrality | Registration counts give integer levels on triadic floor. | `Container23.LevelIntegrality` | 8 | OK | none (zero axioms) |
| 24 | stone-grounding | Symmetry/additivity force common weight `I=αL`, up to scale. | `Container24.StoneGrounding` | 8 | OK | none (zero axioms) |
| 25 | dimension-forcing | Intrinsic counting-growth exponent two. | `Container25.DimensionForcing` | 7 | OK | none (zero axioms) |
| 26 | base-2-forcing | Binary registrable alphabet. | `Container26.Base2Forcing` | 6 | OK | none (zero axioms) |
| 27 | dimensional-accounting | Dimensionless substrate and `ℏ,c,G` anchor accounting. | `Container27.DimensionalAccounting` | 7 | OK | none (zero axioms) |
| 28 | weak-su2 | Quaternion brackets and `2I⊂SU(2)`; weak correspondence. | `Container28.WeakSU2` | 6 | OK | none (zero axioms) |
| 29 | em-u1 | Abelian phase and signed-defect charge reading. | `Container29.EmU1` | 5 | OK | none (zero axioms) |
| 30 | strong-su3 | A2/SU(3) in E8. | `Container30.StrongSU3` | 6 | OK | none (zero axioms) |
| 31 | color-seating | Order-three action: 6 fixed + 38 three-cycles. | `Container31.ColorSeating` | 4 | OK | none (zero axioms) |
| 32 | registration-boundary | One 2π phase cycle. | `Container32.RegistrationBoundary` | 3 | OK | none (zero axioms) |
| 33 | planck-anchor-test | Anchored edge/tick/rate reproduces c by construction. | `Container33.PlanckAnchorTest` | 4 | OK | none (zero axioms) |
| 34 | vacuum-value | Minimum density/vacuum and cosmological factor. | `Container34.VacuumValue` | 3 | OK | none (zero axioms) |
| 35 | force-alpha-hat | Naive Planck vacuum fails; alpha-hat=1/N reframe. | `Container35.ForceAlphaHat` | 3 | OK | none (zero axioms) |
| 36 | negative-curvature | d>6 realizes the negative side of degree-six mirror. | `Container36.NegativeCurvature` | 11 | OK | none (zero axioms) |
| 37 | geodesic-motion | Flat versus deficit-bent paths. | `Container37.GeodesicMotion` | 4 | OK | none (zero axioms) |
| 38 | deflection-value | Equilateral deflection/deficit and double-cover geometry. | `Container38.DeflectionValue` | 3 | OK | none (zero axioms) |
| 39 | point-mass-limit | Concentrated curvature;12-cone/coarse-smooth reading. | `Container39.PointMassLimit` | 2 | OK | none (zero axioms) |
| 40 | deflection-form | Front/eikonal1/b argument and geometric4π flux. | `Container40.DeflectionForm` | 3 | OK | none (zero axioms) |
| 41 | metric-no-thirteenth | Single quaternionic spin geometry supplies dimension lever. | `Container41.MetricNoThirteenth` | 3 | OK | none (zero axioms) |
| 42 | single-su2-root | Quaternionic/single-SU(2) structure under composition assumptions. | `Container42.SingleSU2Root` | 3 | OK | none (zero axioms) |
| 43 | composition-norm | Multiplicative norm and measure hinge. | `Container43.CompositionNorm` | 2 | OK | none (zero axioms) |
| 44 | chirality | Orientation-pure casting and distinct mirror. | `Container44.Chirality` | 2 | OK | none (zero axioms) |
| 45 | spinor | Central sign2π→−I,4π→I in spin lift. | `Container45.Spinor` | 2 | OK | none (zero axioms) |
| 46 | spacetime-signature | Ordered time/finite-rate Lorentzian argument. | `Container46.SpacetimeSignature` | 2 | OK | none (zero axioms) |
| 47 | focusing-resolution | Spatial and spacetime focusing are different operators. | `Container47.FocusingResolution` | 2 | OK | none (zero axioms) |
| 48 | closed-left-wing | `V(6−d)=6χ`, genus-two anti-twelve mirror. | `Container48.ClosedLeftWing` | 3 | OK | none (zero axioms) |
| 49 | cpt | Defect mirror, orbit swap, arrow reversal and CPT. | `Container49.CPT` | 2 | OK | none (zero axioms) |
| 50 | electroweak-mixing | Rank-two neutral directions/Z correspondence. | `Container50.ElectroweakMixing` | 2 | OK | none (zero axioms) |
| 51 | gauge-product | Internal gauge product; no forced1+3+8 geometry. | `Container51.GaugeProduct` | 2 | OK | none (zero axioms) |
| 52 | continuum-limit | Refined12-cone/coarse continuum. | `Container52.ContinuumLimit` | 2 | OK | none (zero axioms) |
| 53 | quantum-kinematics | Complex phase/amplitudes and norm-preserving composition. | `Container53.QuantumKinematics` | 3 | OK | none (zero axioms) |
| 54 | deflection-factor | Two metric components/factor-two light-deflection contact. | `Container54.DeflectionFactor` | 2 | OK | none (zero axioms) |
| 55 | born-hinge | Probability/composition norm. | `Container55.BornHinge` | 2 | OK | none (zero axioms) |
| 56 | matter-census | Spinor/color/chiral representation types. | `Container56.MatterCensus` | 2 | OK | none (zero axioms) |
| 57 | weinberg-angle | Normalization reduction; naive one-half fails. | `Container57.WeinbergAngle` | 3 | OK | none (zero axioms) |
| 58 | hypercharge-grading | Z6 quotient/residues. | `Container58.HyperchargeGrading` | 2 | OK | none (zero axioms) |
| 59 | content-selection | Nine irreps,60/60 split, selection problem. | `Container59.ContentSelection` | 3 | OK | none (zero axioms) |
| 60 | content-a-root | Retracts content as an irreducible external root. | `Container60.ContentARoot` | 3 | OK | none (zero axioms) |
| 61 | k2-surface-test | Threefold counts versus generic E8 embeddings. | `Container61.K2SurfaceTest` | 3 | OK | none (zero axioms) |
| 62 | embedding-distinction | Native grading narrows A2/axis choices. | `Container62.EmbeddingDistinction` | 3 | OK | none (zero axioms) |
| 63 | boundary-map | Conditional sector/charge map and mixing fork. | `Container63.BoundaryMap` | 3 | OK | none (zero axioms) |
| 64 | coxeter-bridge | C=L_aR_b, orders5/6, order30, E8 exponent polynomial. | `Container64.CoxeterBridge` | 6 | OK | none (zero axioms) |
| 65 | four-clocks | Four30-clocks; alignment selects288/480 ticks. | `Container65.FourClocks` | 3 | OK | none (zero axioms) |
| 66 |  |  | `Container66.ArbiterSeating` | 4 | OK | none (zero axioms) |
| 67 |  |  | `Container67.ConjugationGeneration` | 5 | OK | none (zero axioms) |
<!-- END LEAN NODE TABLE -->

---

## II-b. The finite carrier, re-derived (supports Parts II, III and IV)

The floor facts that the Maths 8 instrument rests on, proved here directly (independently of the Lean modules above, which cover the same nodes in kernel-checked form where a theorem exists).

#### C-B1 (node 06; spine II, P2) The 120 unit icosians, the 600-cell counts
*Statement and construction.* Let V ⊂ ℍ be the 120 unit quaternions: the 8 elements ±1, ±i, ±j, ±k; the 16 elements (±½, ±½, ±½, ±½); and the 96 elements obtained from ½(±φ, ±1, ±φ⁻¹, 0) by even permutations of the four coordinates (12 even permutations × 8 sign choices of the three non-zero entries). Then: (a) V is a group under quaternion multiplication (order 120, the binary icosahedral group 2I); (b) the relation u·s = φ/2 (inner product on ℝ⁴) holds for exactly 720 unordered pairs, every vertex has exactly 12 such neighbours, and the chord is |u − s| = 1/φ (arc 36°); (c) the triangles (mutually adjacent triples) number 1200 and the tetrahedral cells (4-cliques) 600; (d) 120 − 720 + 1200 − 600 = 0; (e) the number of vertices at graph distance 0, 1, 2, 3, 4, 5 from a vertex is 1, 12, 32, 42, 32, 1.
*Proof of the chord.* |u − s|² = 2 − 2u·s = 2 − φ. From φ² = φ + 1 we get 1/φ = φ − 1, so 1/φ² = (φ − 1)² = φ² − 2φ + 1 = (φ + 1) − 2φ + 1 = 2 − φ. Hence |u − s| = 1/φ (checked in P2: 2 − 2·(φ/2) − 1/φ² = 0), and cos(arc) = φ/2 = cos 36°. Parts (a), (c) to (e) are finite enumerations over 120 elements; they are proved by exhibiting the enumeration, which `spine_proofs_check.py` does from the construction above with no input from any earlier script. ∎
*Check.* `spine_proofs_check.out` P2: 120 distinct, all unit, closed under multiplication, 720 edges, 12 neighbours, 1200 triangles, 600 cells, Euler 0, distance profile [1, 12, 32, 42, 32, 1].
*Status.* PROVED by enumeration and checked. That this *is* the floor's carrier of nodes 06/12 is the floor's DERIVED claim (the golden-field construction); here it is only used as a definition.

#### C-B2 (node 16; P3) Tetrahedral frustration ε = 2π − 5 arccos(1/3) > 0
*Statement.* The dihedral angle of a regular tetrahedron is arccos(1/3) = 70.528779365…°; five tetrahedra around an edge fill 352.64° and leave ε = 2π − 5 arccos(1/3) = 0.128 rad = 7.356°.
*Proof.* For a regular tetrahedron with unit edge, the two face normals at an edge make angle π − δ where cos δ = 1/3 (face-normal dot product −1/3); numeric value in P3. 5·70.5288° = 352.644° < 360° ⇒ ε > 0. ∎
*Check.* P3: `arccos(1/3) = 70.528779365 deg`, `eps = 0.128… rad`.
*Status.* PROVED and checked. The floor's reading of ε as a persistence engine is POSTULATE (node 16); not claimed.

#### C-B3 (spine D2; P4) The native continuation T(u,s) = (s, φs − u) is a permutation of the 1440 directed edges with 144 ten-cycles, and T⁵ is the antipode
*Statement.* Let H = {(u,s) ∈ V × V : u·s = φ/2} (1440 directed edges). Define T(u,s) = (s, φs − u). Then (a) T maps H to H; (b) T is a bijection; (c) T has 144 cycles, each of length 10; (d) T⁵(u,s) = (−u, −s), T¹⁰ = id.
*Proof.* (a) Unit norm: |φs − u|² = φ² + 1 − 2φ(u·s) = φ² + 1 − φ² = 1. Adjacency: (φs − u)·s = φ − u·s = φ − φ/2 = φ/2. Membership of φs − u in V (an icosian): V is closed under the Z[φ]-linear operations that preserve the icosian ring, and this is verified over all 1440 histories in P4 (every image is a vertex of the list). (b) The inverse is T⁻¹(s,w) = (φs − w, s): from w = φs − u we get u = φs − w, and the same norm/adjacency computation applies. (c, d) Let x_0 = u, x_1 = s, x_{n+1} = φx_n − x_{n−1}. Since φ = 2cos(π/5), the recurrence x_{n+1} + x_{n−1} = 2cosθ x_n with θ = π/5 has the general solution x_n = A cos nθ + B sin nθ with A = u, B = (s − u cosθ)/sinθ. Then x_{n+5} = A cos(nθ + π) + B sin(nθ + π) = −x_n and x_{n+10} = x_n. T(x_{n−1}, x_n) = (x_n, x_{n+1}), so T⁵(u,s) = (x_5, x_6) = (−u, −s) and T¹⁰ = id. The period is exactly 10 (not 5) because T⁵ ≠ id. Every cycle thus has length 10 and there are 1440/10 = 144. ∎
*Check.* P4: image all in H; 1440 distinct images; 144 cycles all of length 10; T⁵ antipode for all 1440.
*Status.* PROVED and checked, with one step computational: the membership φs − u ∈ V (checked on all 1440 histories). Twelve incoming contexts and twelve exits follow from each vertex having 12 neighbours (C-B1) and T being injective on them.

#### C-B4 (spine M6 C3/Born hinge; P5) The unique SO(4)-invariant positive quadratic form on ℍ ≅ ℝ⁴ is c·|q|²
*Statement.* If B is a symmetric bilinear form on ℝ⁴ with B(Rx, Ry) = B(x, y) for all R ∈ SO(4), then B = c⟨·,·⟩ for a constant c. If B is positive, c > 0.
*Proof.* SO(4) is transitive on the unit sphere S³. The function x ↦ B(x,x) is SO(4)-invariant, hence constant on S³, equal to c; by homogeneity B(x,x) = c|x|². Polarization recovers B(x,y) = c⟨x,y⟩. ∎ (Equivalent linear-algebra form: the solution space of EᵀM + ME = 0 for M symmetric and the six generators E of so(4) is one-dimensional.)
*Check.* P5: that solution space has dimension 1.
*Status.* PROVED and checked. This is the M6 result "the unique SO(4)-invariant positive form is norm²"; the physical step to the Born rule (probability = this form) is the floor's HELD identification (node 55), not claimed.

#### C-B5 Link-field face operator on the 600-cell (P11) and the S³ spectrum
*Definition.* Orient each edge i→j with i < j. For each triangle i<j<k let (S_F a) = a_ij + a_jk − a_ik (the oriented sum of link phases around the face). The quadratic part of the face energy μ Σ_f (1 − cos F_f) is (μ/2)|S_F a|², so the operator is M = S_Fᵀ S_F (720 × 720).
*Statement.* (a) M has exactly 119 zero modes (the gradients: 120 − 1 = 119 independent gauge functions modulo constants); (b) its lowest non-zero eigenvalue is exactly 5 − 2√5 = 0.52786404500…, a root of x² − 10x + 5, with multiplicity 6; (c) the next three levels are 1.1458980 (16), 1.9331897 (30), 2.8074176 (48); (d) the 70-fold level expected for k = 5 splits under the finite symmetry into 3.5563272 (30) and 3.6972244 (40). The multiplicities 6, 16, 30, 48, 70 are 2k(k+2) for k = 1…5, the multiplicities of the coexact 1-form eigenspaces on the unit S³.
*Proof.* (a) rank(S_F) = 601 = 720 − 119: computed (P11); the kernel is the gradients because the 600-cell boundary complex has H¹ = 0 (Betti numbers (1,0,0,1), cited from M6 §E2) so every closed 1-cochain is exact. (b–d) are eigenvalue computations of an integer matrix, done numerically to 1e-7 for the multiplicity grouping and to 1e-12 for the value 5 − 2√5 (P16). The identification with S³: the coexact 1-forms on the round S³ have curl eigenvalues ±(k+1) with multiplicity k(k+2) each (k ≥ 1), hence Hodge-Laplacian eigenvalues (k+1)² with multiplicity 2k(k+2) (**CITED** from the harmonic analysis of S³, e.g. Ikeda–Taniguchi 1978; not re-derived here). The lattice result is a finite-group approximation to this spectrum: the ratios λ/(k+1)² are 0.1320, 0.1273, 0.1208, 0.1123 for k = 1…4 (from `e_series_chain_origin.out`), a lattice-dispersion factor. ∎
*Check.* P11 and P16; `explore/e_series_chain_origin.out` §1.
*Status.* (a–d) PROVED/COMPUTED and checked. **Correction recorded:** the original `e_series_chain_origin.out` merged the split k = 5 multiplet (tolerance 5e-3) and quoted it as one level at 3.6368399 with multiplicity 70; the claim "exactly 2k(k+2)" holds as a single level for k ≤ 4 and as a sum 30 + 40 for k = 5 (appended to `explore/SIZE_EXPONENT_ORIGIN.md`). The identification with S³ is CITED, not proved.

---

## III. The M6 layer (floor): content, mass, history, representation

Source: `floor/M6_SPINE_2026-10-19.md` sections C1 to F and the explore files it links.

- **C1, content and charge.** Chiral content Q, L, uc, dc, ec of dimensions 6, 2, 3, 3, 1; hypercharge Y = (1/6, −1/2, −2/3, 1/3, 1), Q = T3 + Y; primitive electric weights k = 3Q, physical charge (e/3)k; primitivity fixes the generator, not the measured e/α. Earlier scalar 15-subspace surrogates fail left/right invariance and are excluded under their identifications, not the content.
- **C2, mass and frequency.** Galois mass m(λ) = sqrt(|λσ(λ)|) with shell values 12, 4, 4, 0 is not the current wave frequency. Koide phasor exact zero; δ = 2π/3 − 2π/5 − arcsin(sqrt3/3). Historical numerical contacts are not a certification of every refinement.
- **C3, cosmology and nesting.** K = ln φ/15, base/cover 15/30, ΩΛ = 2/3 and one-leak-tick comparisons, N and horizon capacity, w from the mirror crossing. All retained as leads; this layer was not refit.
- **C4, atoms.** Hydrogen SO(4) gives n²; shell capacities and Mackay numbers are structure, not a finished derivation. Numerical apparatus (the Si/Li MCHF baselines) was repaired and closed; conventional benchmarks validate the apparatus, not a native atomic derivation.
- **D, live history.** Co-definition as a live adjacent web; the native continuation T(u,s) = (s, φs − u): all 1,440 directed-edge histories have unique successors, 144 ten-cycles, T⁵ antipode, T¹⁰ identity; clocks (one-hop T, composite C, mixture, reinjection) are distinct; relaxation (marginal P = A/12 keeps r, random exit erases it); lag survival (φ/2)³⁰ with gain 1/(1 − (φ/2)³⁰); scale has seven distinct meanings and no universal complexity-at-sixty law.
- **E, charged histories and the joint action.** Response phase −(φ/2)Lδθ; flat proper quaternion transport vs nonzero projected holonomy; the F5 spectral law Vspec = μΣfaces(1 − cos F), μ = (48/5) sin(π/5); the incidence operator on 840 vertex+edge components; the associated charged representation (86,400 complex components); an exact canonical wave/branch/field bridge; one joint action evolved with Gauss and second-order energy convergence. Flat field has 4,320 complex cycle-constant zero modes per register.
- **F, statistics and the floor's own frontier (F1 to F6).** Physical interaction mixing cycles, persistent relative particle, open-space field law with units, quantum occupation and admissibility, native atomic operator, nuclear/material/gravity/cosmological joins. These were the open joins when the floor closed.
### Proofs for Part III (M6 layer C1 to F)
**NOT CARRIED here.** The M6 layers are inherited floor material (`floor/M6_SPINE_2026-10-19.md` and the explore files it links); their equations and derivations are in those files and are not re-derived in Maths 8. One value from F is used as an input below and is checked where used: the spectral-law weight μ = (48/5) sin(π/5) (C-E1). The finite-carrier facts that M6 section D uses (1,440 directed edges, unique successors, 144 ten-cycles, T⁵ antipode) are proved in C-B3 above.

---

## IV. Maths 8's own work, with proofs

### IV.1 Route 56 and the lattice Dirac operator (2026-10-25 to 10-28)
Reproduced cold the route-56 connection (phi/psi-branch rebuild); the 28 massless Dirac modes are {1, 2′, 3′} ⊗ spinor and that kernel selection is Galois, not chirality (COMPUTED). The subdivision scale flow: smooth levels converge as θ²; the non-smooth sector and the 28-core do not. Exact icosian shells are Hecke shells; the concurrent 4D icosian lattice Dirac operator has exact E(k, k′), an internal sector flat to order 7 and a 4-dimensional zero manifold; the Hecke T_p is K(120, 720). Internal polynomials of degree ≤ 6 are zero modes of the Weyl block; the exact Z[φ] degree-7 threshold is the first Sym^n(2′) of 2I containing the physical spinor 2 (§28). Internal momentum renormalises the physical velocity (2J1(r)/r for r ≤ 2) and is not a mass term. The joint 2I_L × 2I_R content of the 28-core; the E8 invariant subalgebra under 2I_L × 2I_R is zero (§30); the claim "no route to SU(3)" was **WITHDRAWN** (§31, wrong test: the floor already derives su(3) in E8 and colour Z/3). Mass-fork (§32): static Galois mass and dynamic rate co-vary through a shared form factor, no inversion. Inertia (§33): locked-label inertia is E/v² (exact conical), no rest mass in the band, the nodal manifold is co-definition. k′ dynamics (§34): no relaxation under a physical force; exact Landau–Zener band flips at node passages. The dispersion cap: c is the group-velocity maximum, the band top a rest-mass scale of about one registration per cell. Memory: the "inertia = propagation rate" hypothesis is the PROPAGATION.md thesis; structure got through, the physical-inertia reading and tunability stay OPEN. Ledger: `explore/LIVE_WEB_RESULTS.md` (append-only, with sha256 per section). Floor correction recorded: "static m is not v" and the Hamiltonian/Bloch pictures imported in §33 to 34 were not floor dynamics (the floor is the tick plus the unital channel).
#### Proof entries for IV.1 (route 56)

**C-R1 The degree-7 threshold (§28 of `LIVE_WEB_RESULTS.md`): PROVED / CHECKED.**
*Statement.* Let 2I be the binary icosahedral group (the 120 unit icosians), 2 its defining spinor representation and 2′ the Galois conjugate (√5 → −√5). The internal harmonics of polynomial degree n transform as Sym^n(2′). Then Sym^n(2′) contains no copy of 2 for 0 ≤ n ≤ 6, and n = 7 is the first n for which it does (multiplicity 1; it appears again at n = 13).
*Proof.* The character of Sym^n(V) at a group element with eigenvalues e^{±it} on V is sin((n+1)t)/sin t (n+1 or (−1)^n (n+1) at t = 0, π). For 2 the angle t is given by cos t = Re(u) for the unit icosian u; for 2′ it is given by the Galois conjugate of Re(u), which lies in [−1, 1] for every element of 2I. The multiplicity of 2 in Sym^n(2′) is the group average of χ_Sym^n(2′) · χ_2 over the 120 elements. Orthonormality of the characters is verified first (⟨2,2⟩ = ⟨2′,2′⟩ = 1, ⟨2,2′⟩ = 0). The averages for n = 0 … 13 are 0 except n = 7 and n = 13, which give 1. ∎ (a finite computation over 120 elements, exact up to floating-point rounding.)
*Check.* `explore/spine_route56_check.py` → `explore/spine_route56_check.out` (last line `RESULT PASS`). The same script finds the first icosahedral invariant of the binary form at degree 12, matching Klein.
*Status.* PROVED / CHECKED. It explains why the recorded zero-mode count (§23, §26: polynomials of degree ≤ 6 are zero modes of the Weyl block, the exact ℤ[φ] threshold at 7) has the threshold it has; it does not by itself prove the zero-mode statement for the lattice operator.

**The rest of IV.1: COMPUTED, recorded, not re-proved here.** Each result is in `explore/LIVE_WEB_RESULTS.md` with its script and raw output; the script is the proof. Reproduce status is from `explore/REPRODUCE_REPORT_2026-11-02.md`.

| result | section | script(s) | reproduce |
|---|---|---|---|
| the 28 massless Dirac modes = {1, 2′, 3′} ⊗ spinor; the selection is Galois, not chirality | §9, §10, §12 | `route56_kernel.py`, `route56_chirality.py`, `route56_selection.py` | MATCH |
| subdivision scale flow (smooth levels converge as θ²; the non-smooth sector and the 28-core do not) | §14 | `route56_subdiv.py` | MATCH |
| exact icosian shells are Hecke shells; the Hecke T_p is K(120, 720) | §21 | `route56_hecke.py`, `route56_hecke_check.py` | `route56_hecke_check` DIFFERS (undiagnosed) |
| 4D icosian lattice Dirac operator: exact E(k, k′), internal sector flat to order 7, 4-dimensional zero manifold | §22, §23 | `route56_lattice4d.py`, `route56_window.py`, `route56_internal_poly.py` | MATCH |
| internal momentum renormalises the velocity (2J1(r)/r for r ≤ 2), not a mass term | §24, §25 | `route56_mass_probe*.py`, `route56_velmap.py` | MATCH |
| degree ≤ 6 zero modes, threshold 7 in ℤ[φ] | §26, §28 | `route56_exact_moments.py`, `route56_irrep_content.py` | MATCH (the group-theory half is C-R1) |
| E8 invariant subalgebra under 2I_L × 2I_R is zero (§30); "no route to SU(3)" WITHDRAWN (§31) | §29 to §31 | `route56_core_joint.py`, `route56_e8_a` to `route56_e8_f` | `route56_e8_c` to `_f` ERROR in a fresh export (a probably untracked data file) |
| mass fork; inertia E/v² with no rest mass; k′ dynamics (Landau-Zener band flips) | §32 to §34 | `route56_massfork*.py`, `route56_inertia*.py`, `route56_dynamics.py` | MATCH |
| scale, link, approximants, core (inherited) | §16 to §20 | `route56_core.py`, `route56_link.py`, `route56_approx.py` | DIFFER (undiagnosed) |


### IV.2 The Bekenstein–Compton dictionary and the ladders (2026-10-28 to 10-29)
The premise (the human's): everything is informational change; Bekenstein–Compton (BC) translates information, energy and mass with c built in. Dictionary: I = 2πRE/(ħc) nats; **cycles = R·E/(ħc)**; 1 cycle = 12 radits = 30 ticks = 2π nats; bits = 2π·cycles/ln 2; p12 = log12(R/ℓP). At R = the reduced Compton length, mass cancels and a particle registers exactly one cycle (2π nats); r_s·ƛ_C = 2ℓP²; hydrogen's binding is α/2 cycle at every hydrogenic R (algebra, not BC). Maps (each with script, raw `.out` and sourced inputs): hydrogen, positronium, lithium, periodic-table sample (`maps/ptable_sample.md`, `maps/lithium.md`, `maps/positronium.md`); the lepton-to-atom ladder (`maps/lepton_ladder.md`: e→μ 206.768…, μ→τ 16.817…, steps raw); the full mass ladder, chemical ladder; carbon-12 and one gram (`maps/carbon_one_gram.md`: N = 5.0184506e22 atoms; the gram's BC count 1.16008721e37 cycles; three different bit counts kept apart, atoms, thermodynamic entropy 2.07e22 bits, BC bound 1.05e38 bits); the four languages (energy-size, mass, charge, information); the nucleon row (proton radius = 4 Compton lengths, CODATA 2022 3.9977 ± 0.0030); colour column (α_g1(0) = π); size-versus-energy tables with provenance flags (M measured, C computed, F formal). Known dimensionless ratios in raw values (`maps/known_ratios.md`).

#### Proof entries for IV.2 (the Bekenstein-Compton dictionary)

#### C-C1 Compton rung: a particle registers exactly one cycle, mass cancels (P6)
*Proof.* R = ħ/(mc), E = mc² ⇒ RE/(ħc) = (ħ/(mc))(mc²)/(ħc) = 1; I = 2π nats. ∎ *Check.* P6 (symbolic).

#### C-C2 r_s·ƛ_C = 2ℓ_P² (P6)
*Proof.* r_s = 2Gm/c², ƛ_C = ħ/(mc): product = 2Għ/c³ = 2ℓ_P². ∎

#### C-C3 Hydrogen binding is α/2 cycle at every hydrogenic radius; the Dirac 1s registers tan(θ/2) cycles (P6)
*Proof.* a₀ = ħ/(αmc), E_Ry = α²mc²/2 ⇒ a₀E_Ry/(ħc) = α/2. For the Dirac 1s: E_binding = (1 − γ)mc², γ = √(1 − (Zα)²); define sinθ = Zα (so γ = cosθ, v/c = sinθ), R = a₀/Z = ħ/(Zαmc); then cycles = R·E/(ħc) = [ħ/(Zαmc)]·[(1 − γ)mc²]/(ħc) = (1 − γ)/(Zα) = (1 − cosθ)/sinθ = 2sin²(θ/2)/(2sin(θ/2)cos(θ/2)) = tan(θ/2). ∎ At Zα = 1 (θ = 90°): tan 45° = 1 cycle. At γ = ½ (θ = 60°, Z = sin60°/α = 118.67): tan 30° = 1/√3.
*Check.* P6: the identity is verified symbolically in u = θ/2 and numerically on four angles.
*Status.* PROVED and checked (algebra). Whether 60° and 1/√3 relate to the floor's π/3 cone angle and lean ξ = arcsin(√3/3) is **noticed only** (the number sin ξ = 1/√3 equals tan 30°; no mechanism claimed).

#### C-C4 The tabulated maps (leptons, carbon gram, four languages, size-versus-energy)
*Statement.* Each map is a table whose every row is a closed-form function of sourced inputs through C-C1…C-C3 (cycles, bits, p₁₂, nats).
*Proof / reproduction.* The formulas are those above; the inputs and the scripts are listed in the table of §G (hashes and reproduce-run status). Nothing in these maps is fitted. The gram's three distinct information counts (atoms, thermodynamic entropy, BC bound) are three different formulas and are kept apart.
*Status.* COMPUTED; reproduces byte-for-byte (§G). Source values are from saved files or, where noted in each map, from web search (secondary).


### IV.3 α and what was checked in the floor (2026-10-28 to 10-30)
Alpha candidate map: both rounds **negative within the tested finite single-level structures only** (OPEN: the composition rule across levels). `maps/alpha_mechanism_status.md`: the formula's only content is √α = e/√(4πε₀ħc); one-loop SM running of 1/α_em to the Planck mass gives 104.9, short by 3.9 to 4.2× of reaching the needed slope; the induced-coupling-plus-Kaluza–Klein-tower candidate puts the hypercharge zero at the Planck mass for R = 28.41ℓP, **a fit, not a derivation**; SU(2) under the tower needs 9.7× more levels; above m_Z the floor owes two couplings (α_Y, α₂), or one plus θ_W (K2). Floor claims checked: no common coupling is claimed and 1/φ³ is refuted at m_Z; the lepton Koide-type claim (δ = 2/9) holds for leptons only and misses quarks by 1.5× to 7×; the earlier "no ratio derived from the floor" statement was corrected. Hubble radius correction recorded (`maps/hubble_radius_correction.md`).

#### Proof entries for IV.3 (alpha)

#### C-D1 One-loop running and the induced-coupling candidate
*Statement.* With Standard-Model content, one-loop running of 1/α_em from m_Z (127.951 recalled; sin²θ_W = 0.23122 recalled) gives 1/α_em = 104.9 at the Planck mass, with net slope −0.584 per e-fold above m_Z (fermions alone −1.70); reaching 1/α = 1 or 1/(4π) there would need slopes 2.64 or 2.42 per e-fold, short by 4.2× and 3.9×. With one Kaluza–Klein tower of SM charged content, b̃_Y = 2×20/3 + 1/6 = 27/2 and b̃₂ = −7 + 8 + 1/6 = 7/6; the hypercharge zero sits at the Planck mass for R = 28.41 ℓ_P (a fit, one parameter, not derived).
*Proof.* The one-loop formula 1/α(μ) = 1/α(μ₀) − (b/2π) ln(μ/μ₀) with the SM b-coefficients stated in `maps/alpha_mechanism_status.md`; derivation and numbers in `explore/alpha_running_check.py`, `alpha_tower_check.py`, `alpha_tower_su2.py` (§G).
*Status.* COMPUTED (reproduces byte-identical); the **input values** (1/α(m_Z), sin²θ_W, b-coefficients) are recalled or textbook and are not re-derived here. These notes are negative or blocked results: they say what the candidate cannot do, not that α is derived.


### IV.4 The lab (2026-10-30 to 10-31)
`lab/spine_lab.html` (README: `lab/README.md`): a single-file visual lab: 64-decade zoom, the 600-cell with tick and T transit, rung circles from the maps with provenance, the spine nodes, an amplitude tab (histories, relaxation, reinjection, sag, injection between orders). Declared assumptions: the Planck anchor (non-discriminating, nodes 17/18/33); the φ step per copy is the original visualizer's choice, not a derived scale. Not verified: phones and other browsers; the parser's 49 spine nodes. Not in the lab: the E-series, the 12-cone orbifold sphere, E8, the cosmological N, the periodic-table rows.

**Proofs for IV.4:** none; the lab is a viewer of the maps and the spine nodes. It carries no claim of its own beyond what it displays from them.

### IV.5 The critical path and the carbon gram (2026-11-02)
`maps/critical_path.md`: the openings (scale, clocks, energy, mass, fields, collective) as a critical path with bottom-up and top-down routes; then the six as one change read six ways; the percentage frame as both per-reading percentage of the measured value and share of the whole object's aspects (the coffee-cup test: remove any law and the cup ceases). First whole object: **one gram of carbon**, not the origin epoch, with margins of error on every reference (`maps/carbon_gram_aspects.md`: 36 aspects in 8 groups; `maps/carbon_gram_coarse_pass.md`: 6 of 36 same-kind readouts, 1 compared; `maps/percentage_frame.md`). The instrument audit (`maps/instrument_audit.md`): link phases on T-histories, the joint matter+links+field action, inter-copy flux and the expressed/manifest split were refused earlier and are owed, not hidden.

**Proofs for IV.5:** the critical path, the percentage frame and the carbon-gram aspects are catalogues and framings. The one computed object is the gram's BC count (C-C4 above). The 36-aspect inventory is not proved row by row (Part IX).

### IV.6 The E-series instrument (2026-11-02)
Built and validated (COMPUTED, `explore/e_series_*.py`, `E_SERIES_*_RESULTS.md`): one copy (SU(2) transport, flat "q" holonomy +I or Clifford "gamma" holonomy −I, U(1) link phases, one joint action; gauge covariance, Gauss, continuity, second-order energy); two adjacent nested copies with radial links, plaquette flux and a tick ratio; expressed vs manifest readouts and an ablation record; the Zeeman readout (energy-response moment equals current × area to 3e-10; flux quantum; spectral flow); susceptibility, spin, driven resonance at Ω = Δ = 2μB. Failed first runs are kept under `_run1_` names.

#### Proof entries for IV.6 (the E-series instrument)

#### C-E1 The action, fields and parameters (one copy)
*Fields.* Spinors Ψ_h ∈ ℂ² on the 1440 T-histories h (site = end vertex of h); U(1) link phases a_e on the 720 edges; face fluxes F_f = oriented sum of a_e around face f (1200 faces). Native SU(2) transport Ω_h on each T-step, in two forms run side by side, `q` (the full unit transport of t·s⁻¹) and `gamma` (the Clifford part: the transport of the unit imaginary part).
*Action.* L = Σ_h |Ψ̇_h|² + (I/2) Σ_e ȧ_e² − κ Σ_h |d_h|² − μ Σ_f (1 − cos F_f), with d_h = Ψ_{T(h)} − e^{ik a_h} Ω_h Ψ_h. Parameters used: κ = k = I = 1 and μ = (48/5) sin(π/5) = 5.642738, an **input** from M6 E3, not re-derived (also run at μ = 0).
*Gauge transformations.* For λ: vertices → ℝ, Ψ_h → e^{ikλ_{end(h)}}Ψ_h, a_{s→w} → a_{s→w} + λ_w − λ_s (a discrete gradient along the step). Then d_h → e^{ikλ_{end T(h)}} d_h (so |d_h|² is invariant) and every face flux F_f is invariant (the discrete gradient integrates to zero around a closed loop).
*Integrator.* Velocity Verlet on all fields including links ("live"); frozen-link mode holds a fixed.
*Status.* Definitions. Reproduce: `explore/e_series_one_copy.py` (sha256 `a3268db0df54d426…`, run status MATCH).

#### C-E2 Face-loop values and the ring spectrum (P10, P16)
*Statement (Wilson loops).* The face loop of `gamma` has trace −(8/5) sin(π/5) = −0.940456403668 (std 2.7e-10 over faces), SU(2) angle 236.098°, SO(3) angle 123.90°, and μ = −6 × trace. The face loop of `q` in index order has trace φ (angle 72° = 2π/5) and trace 2 in telescoping order. Around each of the 144 T-cycles the holonomy of `q` is +I and of `gamma` is −I.
*Proof.* The numerical values of the loops come from the explicit transports in `route56_subdiv.py`/`e_series_one_copy.py` (**COMPUTED**; holonomy ±I is observed on all 144 cycles). The numerical relations among the quoted values are proved in P16: sin(π/5) = 0.587785…, −(8/5) sin(π/5) = −0.940456…, 6 × 0.940456 = 5.64274 = (48/5) sin(π/5) ✓; 2·arccos(−0.940456/2) = 236.098° ✓. That μ equals −6× the Wilson trace is an **observed equality** (not derived).
*Statement (spectrum).* On a ten-cycle with holonomy ε = ±1, the matrix M†M of d_h at a = 0 has eigenvalues s² = |λ − 1|² where λ ranges over the roots of λ¹⁰ = ε; hence for `q` s² = 2 − 2cos(2πk/10), with two null modes per cycle (k = 0 doubled by the spinor index: 288 null modes over 144 cycles) and values 0.381966, 1.381966, 2.618034, 3.618034, 4; and for `gamma` s² = 2 − 2cos(π(2k+1)/10) = 0.097887, 0.824430, 2, 3.175570, 3.902113 with no null modes.
*Proof.* Choose a spinor gauge along the cycle that makes all but one transport trivial (a unitary change of basis); the single remaining link carries the holonomy ±I. Then d_h = Ψ_{h+1} − ΩΨ_h becomes (S_ε − 1)Ψ with S_ε the cyclic shift twisted by ε, whose eigenvalues are λ with λ¹⁰ = ε. Therefore s² = |λ − 1|² = 2 − 2cos(arg λ). For ε = +1, arg λ = 2πk/10; for ε = −1, arg λ = π(2k+1)/10. ∎ (P10: the 10×10 twisted shifts reproduce these sets exactly.)
*Status.* The spectrum follows from the holonomy by the proof; the holonomies are COMPUTED. Reproduce: `e_series_one_copy.py` (MATCH).

#### C-E3 Gauge covariance, continuity, Gauss (the structural identities)
*Statement.* (i) The action is invariant under the gauge transformations of C-E1. (ii) Continuity: ρ̇_v = (div j)_v with ρ_v = Σ_{h: end(h)=v} 2 Im(Ψ_h†Ψ̇_h) and j_e = (∂G/∂a_e)/k, where G = κΣ|d_h|². (iii) Gauss: Q_v = I(div ȧ)_v + kρ_v is constant in time.
*Proof.* (i) shown in C-E1. (ii) Gauge invariance of G under a *time-independent* λ gives, for each vertex v (take λ = δ_v), the Noether identity Σ_e (∂G/∂a_e)(dδ_v)_e + [sum over histories ending at v of the Ψ-variation] = 0, i.e. (div ∂G/∂a)_v = −k(Ψ-current at v). The Ψ equation of motion from L, contracted with Ψ_h† and imaginary part taken, turns the Ψ-variation into ρ̇_v. Together they give ρ̇_v = (div ∂G/∂a)_v/k (sign fixed by the conventions of C-E1; the other sign was checked to fail, see below). (iii) The link equation is I ä_e = −∂G/∂a_e − ∂V/∂a_e, V = μΣ(1 − cos F). Gauge invariance of V under every λ gives Σ_e (∂V/∂a_e)(dλ)_e = 0 for all λ, i.e. (div ∂V/∂a)_v = 0 for all v. Hence d/dt Q_v = I (div ä)_v + kρ̇_v = −(div ∂G/∂a)_v + k·(div ∂G/∂a)_v/k = 0. ∎
*Check (numerical, not part of the proof).* Continuity to 1.5e-15 (the other sign: 8); div ∂V/∂a to 7e-15; Gauss conserved to 5e-14 over 2000 steps with random data for both transports and both μ (the other sign drifts 12 to 17); gauge covariance to ~1e-14; second-order energy (fluctuation falls 4.0× on halving the step); finite-difference forces to 8 digits. Output `explore/e_series_one_copy.out`. **Frozen links:** Gauss quantity drifts 2.5 (`q`), 3.7 (`gamma`): with links held fixed the equation I ä = … is not imposed, so (iii) loses its hypothesis; this is expected from the proof and matches the output.
*Status.* (i) and (iii) are PROVED given continuity; (ii) is a derivation at the level of the Noether argument, with the overall sign and factor of 2 in ρ_v fixed by the conventions of C-E1 and **confirmed numerically, not derived line by line here** (the opposite sign fails). The sign (+kρ) is a convention of the action. A line-by-line derivation of (ii) from the Ψ equation of motion is not carried.

#### C-E4 Two copies: Gauss per site, decoupling, tick ratio
*Definition.* Copies A and B on the same 120-vertex carrier; B has tick ρ times longer (kinetic weight ρ², link inertia Iρ², potentials unchanged, so frequencies ×1/ρ). Radial links b_v (120) A→B with gauge shift (λᴮ − λᴬ)/k; matter coupling κ_r Σ_h |Ψᴬ_h − e^{−ikb}Ψᴮ_h|²; radial plaquette flux μ_r Σ_e (1 − cos P_e), P_e = aᴬ_e + b_head − aᴮ_e − b_tail; radial link kinetic energy I_r.
*Statement.* Per-site Gauss quantities (A: I_A div ȧ_A − I_r ḃ_v + kρᴬ; B: I_B div ȧ_B + I_r ḃ_v + kρᴮ) are conserved; with κ_r = μ_r = 0 the copies decouple exactly.
*Proof.* Same argument as C-E3 applied to each copy, with the radial link entering each copy's divergence with opposite sign (a gradient on A is a gradient on B up to the shift); P_e is invariant under the independent gauge transformations. Decoupling is immediate from the action. ∎
*Check.* `explore/e_series_two_copy.out`: Gauss to 5e-14 (ρ = 1, φ), 1.2e-11 (ρ = 12); decoupling difference 0.0; sweep table of arrival times and fractions. **Not explained:** the 3.41 energy-order ratio for `gamma` at ρ = 12. **Failed run kept:** `e_series_two_copy_run1_fdtest_bug.out`.
*Status.* Identities PROVED; the sweep is COMPUTED; the declared couplings (κ_r, μ_r, ρ, identity identification) are choices, not derived.

#### C-E5 Zeeman readout, moment, flux quantum (P10)
*Setup.* Impose a link phase α on every edge of one decagon (forward direction); loop flux Φ = 10α; Area = |bivector| = 5 sin 36° = 2.93892626; B := Φ/Area.
*Statement.* The ring-mode frequencies are ω_k(α) = |e^{iθ_k} − e^{iα}| = 2|sin((θ_k − α)/2)| (θ_k = 2πk/10 for `q`; shifted for `gamma`); the splitting of the two circulation senses is linear in α with slope 2cos 18° = 1.902113; the moment per quantum is μ = |dω/dα|·(1/10)·Area = cos 18°·(5 sin 36°)/10 = cos 18°·sin 36°/2 = 0.2795084969 and equals current × area; ΔE = 2μB; a flux of one quantum (10α = 2π) maps the spectrum onto itself with every level shifted by one.
*Proof.* (ω_k) |e^{ia} − e^{ib}|² = 2 − 2cos(a − b) = 4 sin²((a − b)/2). (Moment) Let E(α) be the mode energy. The imposed phase enters only through a_e = α on the ring, so −dE/dα = Σ_{e∈ring} j_e with j_e = −∂E/∂a_e the (Hellmann–Feynman) edge current; for an eigenmode of the ring all ten j_e are equal, so −dE/dα = 10 j. With B = 10α/Area: μ := −dE/dB = −(dE/dα)(Area/10) = j·Area (current × area) ∎. (Flux quantum) ω_k(α + 2π/10) = |e^{iθ_k} − e^{iα}e^{i2π/10}| = |e^{i(θ_k − 2π/10)} − e^{iα}| = ω_{k−1}(α). ∎
*Check.* P10 (closed forms: slope = cos 18° = 0.95105652; μ = 0.2795084969; 2μ = 0.559017; flux-quantum identity to 1e-15). `explore/e_series_zeeman.out`: energy-response moment 0.2795084969 vs current × area 0.2795084968 (ratio 1.0000000003) for `q`; 0.2618602471 for `gamma`; over tick ratios 5.4e-4 to 1836 the ratio stays 1.0000000003. **Failed run kept:** `e_series_zeeman_run1_analytic_columns.out`.
*Status.* PROVED (closed form) and COMPUTED. The calibration to a measured Larmor frequency is not done; the stated 0.358 ratio (see C-F3) is the proton-order value relative to the measured, not a result.

#### C-E6 Chain of nested layers: decay law and exact couplings (P12)
*Setup.* Layers n = 0…K, each a copy of the link system (face energy μ per layer), joined by radial plaquettes of strength μ_r. Consider a transverse mode of the face operator with eigenvalue λ and amplitude f_n in layer n (radial links can be set to their minimum for a transverse mode).
*Decay law.* The static energy is ½μλΣf_n² + ½μ_rΣ(f_n − f_{n+1})². Stationarity at an interior layer gives μλ f_n + μ_r(2f_n − f_{n+1} − f_{n−1}) = 0, i.e. f_{n+1} + f_{n−1} = (2 + μλ/μ_r) f_n. Solutions f_n ∝ e^{−γ n} with 2cosh γ = 2 + μλ/μ_r, so **cosh γ = 1 + μλ/(2μ_r)**. ∎
*Exponent.* If each layer is larger by a factor q and the mutual inductance falls as M_c ∼ q^{−p c}, then γ = p ln q, so p_M = γ/ln q and the coupling that produces a chosen p_M is **μ_r/μ = λ/(2(cosh(p_M ln q) − 1))**.
*Exact values (P12, symbolic).* cosh(2 ln φ) = (φ² + φ⁻²)/2 = 3/2, so for q = φ and p_M = 2, μ_r/μ = λ₁/(2·½) = λ₁ = 5 − 2√5 = 0.5278640. cosh(3 ln φ) = (φ³ + φ⁻³)/2 = √5, so for p_M = 3, μ_r/μ = λ₁/(2(√5 − 1)) = (3√5 − 5)/8 = (3φ − 4)/4 = 0.2135255. ∎
*Continuum limit (P12).* With the isotropic rule μ_r/μ = (a/Δt)², a² = λ₁/4, Δt = ln q: cosh(p_M Δt) = 1 + λ₁Δt²/(2a²) = 1 + 2Δt², giving p_M = arccosh(1 + 2Δt²)/Δt = 2 − Δt²/3 + O(Δt⁴) → 2 (series verified symbolically); at q = φ the isotropic coupling is a²/Δt² = 0.570 (this is the 8% above λ₁ noted).
*Check.* P12 and `explore/e_series_chain_origin.out` §2 to §3 (solver check at K = 8: at μ_r/μ = λ₁ the layer exponents run 3.243, 2.619, 2.281, 2.124, 2.053, 2.011 toward 2; at (3φ − 4)/4, 4.347, 3.538, 3.190, 3.066, 3.024, 3.007 toward 3).
*Status.* The decay law and the exact couplings are PROVED given that radial links decouple for transverse modes (assumption, verified by the K = 8 solver). The isotropic rule is a hypercubic-lattice rule applied to a 600-cell lattice with a calibrated spacing, stated by the note as approximate at the 8% level. `e_series_chain.py` shows `DIFFERS` in the reproduce run only in an elapsed-time stamp at the first differing line ("4 s" vs "14 s"); the remainder was not compared line by line (open item in the handoff).

#### C-E7 The exponent p_E = p_M + 1 (argument from units)
*Statement.* At fixed physical moments, the absolute coupling energy falls as p_E = p_M + 1.
*Argument.* The current of a ring of radius R carrying fixed physical moment μ is j = μ/(q·c·R·area_lat) ∝ 1/R (tick = R/c, the lab's anchor); the phase it sets on a fixed inner ring is M_lat·j, and the inner ring's energy shift is its own fixed quantum times that phase. So the energy goes as the chain's M_c times 1/R: p_E = p_M + 1.
*Status.* **Argument, not computation** (the note says so). It needs tick ∝ size, an anchor choice that is a declared non-discriminating bridge (floor nodes 17/18/33).

#### C-E8 Subdivision volume and its growth exponent (P13)
*Statement.* The n-fold geodesic subdivision of the 600-cell has V_n = 120 + 720(n−1) + 1200·C(n−1,2) + 600·C(n−1,3) points; V_n ~ 100 n³; the local exponent ln(V_{n+1}/V_n)/ln((n+1)/n) increases to 3.
*Proof.* A point of the n-fold subdivision of a k-simplex with all barycentric coordinates positive is a composition of n into k+1 positive parts: C(n−1, k) of them. Vertices (k=0): 120 · C(n−1,0) = 120; edge-interior points (k=1): 720·C(n−1,1) = 720(n−1); face interior (k=2): 1200·C(n−1,2); cell interior (k=3): 600·C(n−1,3). The sum is V_n. The leading term is 600n³/3! = 100n³. ∎
*Check.* P13: V_1, V_2, V_3 = 120, 840, 2760 (also built and counted by the note); exponents 2.807, 2.934, 2.967, 2.980, 2.987, 2.9905, 2.9929.
*Status.* PROVED and checked. The floor's intrinsic counting dimension is 2 (node 25) and this ambient exponent is 3: both are kept.


### IV.7 The hyperfine arc (2026-11-02): a measured benchmark for the instrument
- Nuclear magneton μ_N = e·c·ƛ_p/2; the 0.358 = ƛ_p/R_mag is a length (0.587 fm), mass 336 MeV (`NUCLEAR_MAGNETON_RESULTS.md`).
- Hydrogen, deuterium, ³He⁺ (MEASURED, secondary): the rung-size form (8/3)[(2I+1)/(2I)]Z³(R_mag/a₀)(ƛ_e/a₀) reproduces them to about 1e-4 with no free parameter, with the electron's actual moment; the μ_r inferred from hydrogen alone does not (`HYPERFINE_SERIES_RESULTS.md`). Multiplicity (2I+1)/(2I) is exact spin algebra; nature's size exponent is p = 2.99993 from ³He⁺/H (`SIZE_AND_MULTIPLET_RESULTS.md`).
- Origin of the exponent 3 (COMPUTED, SCOPED to the construction): the lattice link field is Maxwell on S³; its transverse levels are the coexact 1-form spectrum with multiplicity 2k(k+2) and lowest level λ1 = 5 − 2√5; exponent 3 = 2 (lowest curl eigenvalue) + 1 (fixed-moment source); also the volume-growth exponent 3 of the refined carrier (the floor's intrinsic counting dimension is 2, node 25: both are kept) (`SIZE_EXPONENT_ORIGIN.md`).
- Heavy hydrogen-like ions (Ho, Re, Pb, Bi; secondary values): the exponent rises to 4.0 to 4.2; the chain's profile does not select the φ step and prefers a fine one (`HYDROGENLIKE_AND_STEP_RESULTS.md`; the φ step is an assertion, not used).
- Two groups (`TWO_GROUPS.md`): the light group (H, D, ³He⁺; far-order regime) and the heavy group (adjacent-order regime, atomic order 1.65 to 2× the electron Compton rung). The atomic order registers exactly tan(θ/2) cycles with sin θ = Zα; pole at θ = 60° (1/√3 = the floor's lean sin ξ, noticed not claimed); critical Zα = 1 is one registration.
- Arc exploration (`ARC_EXPLORATION.md`): the nuclear/atomic cycle ratio "plateau near 1/α" is a stay in Z = 70 to 83 and is **WITHDRAWN as a feature**; the electron rung's influence on the exponent is p − 3 ≈ 3(v/c)², an inverse square in the size ratio; mass and size march along the arc and density saturates.
- Finite nuclear charge and magnetization (`NUCLEAR_SIZE_HFS_RESULTS.md`): a Dirac solver validated against γ (5e-14) and the Breit factor (3e-6); finite charge −4.6% to −11.1% and magnetization −1.1% to −3.3% account for the 7 to 15% heavy-ion shortfall to within 1 to 2%; the finite-charge effect goes as R_N^(2 cos θ − 1), an exponent that runs with θ. QED is not computed.
- Ledger of the roughly 2% that recurs across results (`maps/two_percent_ledger.md`): an index only; no common cause asserted.

#### Proof entries for IV.7 (the hyperfine arc)

#### C-F1 The Fermi contact form in rung sizes is the textbook formula (P7)
*Statement.* hfs/Ry = (8/3)[(2I+1)/(2I)] Z³ (R_mag/a₀)(ƛ_e/a₀)(1 + m_e/M)⁻³ equals (8/3)[(2I+1)/(2I)](μ_X/μ_B) Z³ α² (1 + m_e/M)⁻³.
*Proof.* With μ_X = x μ_B (x := μ_X/μ_B), μ_B = eħ/(2m_e): R_mag/a₀ · ƛ_e/a₀ = (2xμ_B/(ec))·ƛ_e/a₀² = (xħ/(m_ec))·ƛ_e/a₀² = x ƛ_e²/a₀² = x α². ∎ (symbolic in P7).
*Status.* PROVED (algebra). The Fermi-contact energy itself, E = (8/3)[(2I+1)/(2I)](μ_X/μ_B) Z³α² Ry (with the reduced-mass factor), is **CITED** textbook (Fermi 1930; Breit 1930 for the relativistic factor); it is not derived in this repository, and the instrument does not contain a spin-magnetization coupling (an open item).
*Check.* `explore/hyperfine_series.out` (sha256 `a73859159e235b37…`, MATCH): form/measured = 0.998898 (H), 0.998727 (D), 0.998947 (³He⁺); with |μ_e| = 1.00115965 μ_B instead of μ_B: 1.000056, 0.999885, 1.000106. Failed run kept: `hyperfine_series_run1_bohr_magneton_only.out`.

#### C-F2 The multiplicity (2I+1)/(2I) is exact spin algebra (P8)
*Statement.* For H = A s·I with s = ½ and nuclear spin I: the splitting between the F = I + ½ and F = I − ½ levels is A(I + ½); the difference between the aligned (m_s = ½, m_I = I) and anti-aligned (m_s = −½, m_I = I) diagonal energies is A I; their ratio is (2I+1)/(2I).
*Proof.* s·I = ½[F(F+1) − I(I+1) − 3/4]. For F = I + ½: ½[(I+½)(I+3/2) − I(I+1) − 3/4] = I/2. For F = I − ½: ½[(I−½)(I+½) − I(I+1) − 3/4] = −(I+1)/2. Difference = I/2 + (I+1)/2 = I + ½. The aligned state has s_zI_z = ½·I, the anti-aligned −½·I: difference A I. Ratio (I + ½)/I = (2I+1)/(2I). ∎
*Check.* P8 (symbolic and the explicit 2(2I+1)-dimensional matrices for I = ½, 1, 3/2, 2, 5/2, 7/2); `spin_multiplet.out`: ratios 2.00000, 1.50000, 1.33333, 1.25000, 1.20000, 1.14286 (MATCH).
*Status.* PROVED and checked.

#### C-F3 The size exponent of nature, p = 2.99993, from ³He⁺/H
*Statement.* Remove the moment ratio, the multiplicity ratio and the reduced-mass factor from the measured ³He⁺/H hyperfine ratio; the remainder is Z^p with Z = 2.
*Derivation (arithmetic).* Measured ratio 6.100827; instrument-route factors: (μ_He/μ_p) = 2.1276253/2.7928474 = 0.761813, multiplicity ratio (2/2) = 1, reduced-mass factor ((1 + m_e/m_p)/(1 + m_e/M_He))³ ≈ 1.001087, product 0.762641. Then 6.100827/0.762641 = 7.9996 = 2^p, p = ln(7.9996)/ln 2 = 2.99993.
*Check.* `explore/spin_multiplet.out` (the line giving 0.762641 and 7.9996) and `hyperfine_series.out`.
*Status.* COMPUTED from secondary frequencies (one factor of 2 in size only: Z = 1 to 2). The exponent is **measured over one doubling**; whether it is constant over a longer range is open (no sourced hydrogen-like data for 3 ≤ Z ≤ 66).

#### C-F4 Where the 3 comes from: two accounts
*Statement and status.* (a) Field propagation: the lowest transverse mode of the carrier (curl eigenvalue 2, the six invariant 1-forms) falls across scale with exponent p_M = 2 (C-E6 at the coupling λ₁, or in the continuum limit with the isotropic rule) and a fixed-moment source contributes +1 (C-E7): 2 + 1 = 3. (b) Volume: a unit-normalised state on a 3-dimensional carrier has density ∝ size⁻³ (C-E8). They coincide for k = 1 (k + 2 = dim S³ = 3); for the mode k = 2 account (a) gives 4. Whether the coincidence has a reason is **not resolved**. Reproduce: `explore/e_series_chain_origin.out`.

#### C-F5 The Dirac 1s hyperfine: Breit factor and exponent excess (P9, P15)
*Statement.* For the point-Coulomb 1s state (κ = −1) in units ħ = c = m = 1, with γ = √(1 − (Zα)²): E = γ; G(r) = N r^γ e^{−Zα r}; F = −√((1 − γ)/(1 + γ)) G; and the point-dipole radial integral normalised by ∫(G² + F²)dr is I = −(Zα)³/(γ(2γ − 1)). The relativistic factor on the non-relativistic hyperfine energy is A(Zα) = 1/(γ(2γ − 1)); the hyperfine energy scales as Z³α²·A, so the local exponent in Z is p = 3 + d ln A/d ln Z = 3 + x·A′/A with x = Zα, which equals p − 3 = (sin²θ/cosθ)(1/cosθ + 2/(2cosθ − 1)) with sinθ = x, and p − 3 = 3x² + … for small x.
*Proof.* Radial Dirac equations (κ = −1): G′ = G/r + (E + 1 − V)F, F′ = −F/r − (E − 1 − V)G with V = −Zα/r. Near r → 0 put G = g r^s, F = f r^s: s g = g + Zα f and s f = −f − Zα g, so f/g = (s − 1)/Zα = −Zα/(s + 1), whence s² = 1 − (Zα)² and s = γ (the consistency is verified in P15). Then F/G = (γ − 1)/(Zα) = −√((1 − γ)/(1 + γ)): the squares agree because (1 − γ)²/(Zα)² = (1 − γ)²/(1 − γ²) = (1 − γ)/(1 + γ), and the sign is negative for γ < 1 (verified in P15). That G = N r^γ e^{−Zαr} solves the full equation with E = γ is the standard point-Coulomb ground state. Normalisation ∫(G² + F²)dr = N²(1 + (1 − γ)/(1 + γ)) ∫r^{2γ}e^{−2Zαr}dr = N²(2/(1 + γ)) Γ(2γ + 1)/(2Zα)^{2γ+1}. Dipole integral ∫GF/r² dr = −√((1 − γ)/(1 + γ)) N² Γ(2γ − 1)/(2Zα)^{2γ−1}. Ratio: −√((1 − γ)/(1 + γ)) · ((1 + γ)/2) · Γ(2γ − 1)(2Zα)²/Γ(2γ + 1) = −(√(1 − γ²)/2)·(2Zα)²/(2γ(2γ − 1)) = −(Zα)³/(γ(2γ − 1)) using Γ(2γ + 1) = 2γ(2γ − 1)Γ(2γ − 1) and √(1 − γ²) = Zα. ∎ For the exponent: d ln γ/d ln x = −x²/γ²; d ln(2γ − 1)/d ln x = −2x²/(γ(2γ − 1)); so p − 3 = x²/γ² + 2x²/(γ(2γ − 1)); with γ = cosθ and x = sinθ this is the stated form; its Taylor series begins 3x² (P9, symbolic).
*Check.* P9, P15 (four values of γ to 1e-12 relative), and the numerical Dirac solver `explore/nuclear_size_hfs.py` (E = γ to 5e-14, I/(−(Zα)³) = Breit factor to 3e-6 at Z = 1, 20, 50, 67, 83; MATCH).
*Status.* PROVED and checked. The statement that the exponent excess is "the influence of the electron's Compton rung" and is ≈ 3(v/c)² is the reading of the leading term 3x².

#### C-F6 Finite nuclear charge (Breit–Rosenthal) and magnetization (Bohr–Weisskopf): method and scaling
*Method (all in `nuclear_size_hfs.py`).* Same radial equations with the potential of a uniformly charged sphere of radius R = √(5/3) R_ch, which is V(r) = −(Zα/2R)(3 − r²/R²) for r < R and −Zα/r outside. **Proof of the potential (P14):** Poisson's equation (1/r²)(r²V′)′ = 3Zα/R³ for constant charge density (satisfied by V_in), V continuous at R (= −Zα/R), V′(R) = Zα/R² continuous; R_ch² = (3/5)R² for a uniform sphere. Solved by shooting in x = ln r (RK4): outward from r₀ = 10⁻⁴R (inside the sphere G₀ = r₀, F₀ = −(E − 1 − V₀)r₀²/3) to a match point 1/(Zα), inward from r_max with G₀ = 10⁻³⁰, F₀ = −√((1 − E)/(1 + E))G₀, root in E by bisection (tolerance 1e-13) on the mismatch. Integrals I_M = ∫GF M(r)/r² dr / ∫(G² + F²)dr with M(r) the fraction of the magnetization inside r: uniform sphere (r/R)³ inside, thin shell 0 inside (both = 1 outside). δ_BR = I(finite charge, point dipole)/I(point charge) − 1; δ_BW = I_M/I(point dipole, same wavefunction) − 1.
*Scaling argument (not a proof of the coefficient).* Near r → 0, G F/r² ∼ r^{2γ−2}; the region r < R contributes ∫₀^R r^{2γ−2}dr = R^{2γ−1}/(2γ − 1) (convergent iff 2γ > 1, which is why the Breit factor has its pole at γ = ½). A finite-charge distortion of order one inside r < R therefore changes I by a fraction ∝ R^{2γ−1}: **δ_BR ∝ R_N^{2cosθ−1}**. At Z = 83, 2γ − 1 = 0.5914 (P9); the computed local exponents are 0.598, 0.600, 0.600, 0.592 (`nuclear_size_hfs_scan.out`, charge radii ×0.25…×4). The scaling is therefore supported to ~1.5% in the exponent, not proved (the O(1) coefficient is computed, not derived).
*Results (COMPUTED, MATCH).* δ_BR = −0.0461, −0.0712, −0.1052, −0.1115 (Ho, Re, Pb, Bi); δ_BW (uniform, shell) −0.0111/−0.0176, −0.0152/−0.0241, −0.0199/−0.0315, −0.0207/−0.0326; Fermi (a = 0.5234 fm) vs uniform differ by 0.0003 to 0.0006; leftover after BR + BW against the measured shortfall: Ho −0.9…−0.3%, Re −0.8…+0.1%, Pb −2.0…−0.8%, Bi +0.6…+1.8%.
*Status.* Method and the potential PROVED; numbers COMPUTED. **Not computed:** QED (self-energy, vacuum polarization), the single-particle magnetization, deformed charge distributions, diamagnetic corrections to the moments. The input hyperfine energies, radii and moments for the ions are secondary (`HYDROGENLIKE_AND_STEP_RESULTS.md`); the Re isotope assignment was inferred.

#### C-F7 The two groups, the arc and the withdrawn plateau
*Statements.* Table of two groups (`TWO_GROUPS.md`): each entry is a closed-form function of the ion's Z, A, R, B, μ, I via C-C1…C-C3 and C-F5 (for example atomic cycles tan(θ/2), size ratio atomic/electron Compton = 1/(Zα) = s). The exponent excess p − 3 ≈ 3/s² (C-F5, since x = 1/s): "+0.7% at s = 13.7, +2.9% at 6.85, +6.8% at 4.57, +21% at 2.74, +46% at 2.05, +95% at 1.65" and the local log-slope −2.000 at s = 68.5 and 27.4. The plateau of the nuclear/atomic cycle ratio was a stay in Z = 70 to 83 where two log-slopes cross (1.206 vs 1.206) and is **withdrawn**.
*Check.* `two_groups.py`, `two_groups_extra.py`, `arc_exploration.py` (MATCH; sha256 in §G).
*Status.* COMPUTED; the plateau correction is in `ARC_EXPLORATION.md` and ledger entry 9.

#### C-F8 Candidates for the ladder that is not a ladder
*Status.* **Candidates only** (`BRAID_CANDIDATES.md`, `dirac_series_vs_chain_weights.py`, MATCH): mode sums, the Dirac series (ratio → 4/3; pole s = 2/√3 ≈ 1.155, i.e. Z = 118.7 by C-C3), odd-mode weights √(3/5) = 0.7746 against Dirac coefficients (two points, unexplained), Binet/Galois alternation. The floor's braid (F18/F19) is untested. No derivation is claimed.


### IV.8 Reproducibility (2026-11-02)
`explore/reproduce.py` re-ran every explore script that has a committed `.out`, against a fresh export of the committed tree: of 89 scripts, 75 are byte-identical (45 also match a hash recorded in a note, 30 have none recorded), 6 DIFFER, 8 ERROR (`explore/REPRODUCE_REPORT_2026-11-02.md`). The ERRORs: four need command-line arguments the runner does not pass; `route56_e8_c` to `_f` probably lack an untracked data file. The DIFFERS: `e_series_chain` and `route56_band2` at first look differ in an elapsed-time stamp only; `route56_core`, `route56_hecke_check`, `route56_link`, `route56_approx` are inherited and undiagnosed. Environment: `explore/ENVIRONMENT.md` (Python 3.14.6, NumPy 2.5.3, SymPy 1.14.0, mpmath 1.3.0). No independent review of any of this has been done.

#### Reproduction table (what to run, what to expect)

Hashes are the first 16 hex digits of the **current** committed file; the *reproduce* column is the status from `explore/REPRODUCE_REPORT_2026-11-02.md`. Run any row as `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` from the repository root.

| claim(s) | script | sha256 (script) | sha256 (out) | reproduce run |
|---|---|---|---|---|
| C-A4, C-B1…C-B5, C-C1…C-C3, C-E2 (arith), C-E5, C-E6 (algebra), C-E8, C-F1, C-F2, C-F5 (P9, P15), C-F6 (potential) | `spine_proofs_check.py` | 6c21b0d8bb4d2a0b | f0ca6fa279e8a26d | new (71 PASS, 2 identical runs) |
| C-E2, C-E3 | `e_series_one_copy.py` | a3268db0df54d426 | 73bf87b47253fd0d | MATCH |
| C-E4 | `e_series_two_copy.py` | bffa8ccf343ef937 | f98fe889798b15b8 | MATCH |
| readouts, ablation | `e_series_readouts.py` | 89b3532f925d2096 | eb65d0551abab8ca | MATCH |
| C-E5 | `e_series_zeeman.py` | 1414e0fff216b012 | d170f3e3f81be11f | MATCH |
| response, resonance | `e_series_response.py` | 4441668fd16e6da7 | 15a5b4874431fc39 | MATCH |
| C-E6 | `e_series_chain.py` | b2f65294054e2776 | c8d38676484f484b | DIFFERS (elapsed-time stamp at first differing line; rest not yet compared) |
| C-E6 | `e_series_chain_spectrum.py` | aedd9b862d50ed38 | 22bca3ba76ff4ce8 | MATCH |
| C-B5, C-E6, C-E8, C-F4 | `e_series_chain_origin.py` | 944c137c687fdcaf | 77a0e5fa85b5b0a7 | MATCH |
| C-F1 | `hyperfine_series.py` | fd387caf92182f29 | a73859159e235b37 | MATCH |
| C-F2, C-F3 | `spin_multiplet.py` | 973746ec72bdef94 | 2f4021f2e3cd2533 | MATCH |
| heavy ions, step | `hydrogenlike_series.py`, `size_exponent_listening.py` | c3915dded268c9a1, cc6cfd7089049642 | 82f38d2e80373f79, 1df1aed189f63621 | MATCH |
| C-F7 | `two_groups.py`, `two_groups_extra.py`, `arc_exploration.py` | 0bb629d2c4b20296, 199561e4bd92cde9, ac9765c52320c277 | a8f80c01d1b1b5bc, dd10976173431c28, fdf9dff38ea6a7ed | MATCH |
| C-F8 | `dirac_series_vs_chain_weights.py` | 03597af4e57f1afb | d2e99b2459a685cc | MATCH |
| C-F5, C-F6 | `nuclear_size_hfs.py`, `nuclear_size_hfs_scan.py` | 1460d21f83186548, 4f8169f527d3dba9 | ff177de7d178d82c, 6715335b28d874bc | MATCH |
| nuclear magneton | `nuclear_magneton_symptoms.py`, `proton_magnetic_scale.py` | d9b3bec9ef78a960, a89efa924a0d9176 | 4cd104965070c73c, 0fdd8c8120988763 | MATCH |
| C-C4 | `carbon_one_gram.py`, `lepton_ladder_map.py`, `four_languages_ladder.py`, `positronium_map.py`, `lattice_physical_map.py` | 90c3480bb1412815, 171191abcbf6fd39, ed031e1101150009, 325c71af25ef7163, f61d384e3d377618 | d948d39b0926bad2, 8656baca9894b50b, 6a1e0aa5f42bd2d4, a7d549e0b547dff6, 0a424268d43aac01 | MATCH |
| C-C4 | `known_ratios.py` | 7d0650096ea99fe2 | writes `maps/known_ratios*.md/csv`; no `.out` | not in report |
| C-D1 | `alpha_running_check.py`, `alpha_tower_check.py`, `alpha_tower_su2.py` | 16bbda845a35b6b5, bbfc51f46d1b62c7, 2d048b65909c018f | 4824fdd75a5429ca, e9399d0381b13d3b, 597418553fecc7d1 | MATCH_UNRECORDED (identical to the committed `.out`; no hash in a note) |

Recorded full-length hashes of each script and output are in the corresponding results note's last lines (for example `HYPERFINE_SERIES_RESULTS.md`, `NUCLEAR_SIZE_HFS_RESULTS.md`). `explore/ENVIRONMENT.md` lists the software versions; `explore/reproduce.py` re-runs everything against a fresh export of the committed tree.

---

## V. The frontier, as it stands

**Closest to the numbers (the hyperfine benchmark).** QED and the single-particle magnetization for the heavy ions; diamagnetically corrected moments; deformed charge distributions for Ho and Re; a measured hyperfine value for hydrogen-like ions with 3 ≤ Z ≤ 66; primary papers behind the secondary values.

**Inside the instrument.** The Fermi-contact (spin-magnetization) coupling is not built (the action couples charge current, not spin); the inner ring inside the outer sphere; geometry scaling inside the dynamics; the second register and conjugate charge content; the size dependence derived inside the instrument rather than read from the chain; a calibration (not forced: "archaeology, not dictation").

**On the floor's own open joins (M6 F1 to F6), now with an instrument and a benchmark.** F1 the interaction mixing cycles, contexts and scales; F2 a persistent relative particle; F3 the open-space field law with units; F4 quantum occupation; F5 a native atomic operator (the hyperfine line is a first measured contact for the nested-copy chain, not a derivation of atoms); F6 nuclear/material/gravity/cosmology.

**Ladder that is not a ladder (the human's question).** Why the heavy ions' exponents do not step regularly: candidates in `BRAID_CANDIDATES.md` (mode sums; the Dirac series with ratio → 4/3 and pole at Z = 118.7; the odd-mode weights √(3/5) against Dirac coefficients, two points, unexplained; Binet/Galois alternation). The floor's braid (F18/F19: two golden rates φ/2 and 1/(2φ), crossing inventory 4:8) is **untested**.

**The whole object.** The carbon gram's 36 aspects: only charge and current-moment readouts exist; the weak, thermal, mechanical, optical, atomic and nuclear sectors have no readout in the instrument yet.

**Handles (the purpose).** None delivered yet. Nothing here is a lever on mass, space or time yet. What exists is a validated instrument whose response (moment, resonance, Zeeman shift, susceptibility) can be varied, and a measured benchmark (hyperfine splittings) it is being compared with.

**Reproducibility clean-up.** Teach the runner the four argument-taking scripts; ignore elapsed-time stamps when comparing; find the data file missing from a fresh clone (the `route56_e8_*` inputs); diagnose the four inherited DIFFERS. Do not edit chained or inherited scripts in place.

**Proofs for Part V:** none exist; these are open items. Nothing in this part is claimed.

---

## VI. Provenance and conventions

- **Floor:** `floor/PROVENANCE.md` carries the source path and sha256 of each inherited file. Three floor files were edited at the human's direction on 2026-11-02; the as-imported copies are in `floor/as_imported/` and the edits are recorded there. Cite floor claims by file and node; never edit it.
- **Commits:** directly to `main`; push only when the human says; verify a push with `git fetch` and `git rev-parse HEAD origin/main`.
- **Runs:** `py -3 -I -X utf8 -u <script> > <script>.out`; NumPy, SymPy, mpmath only. Each result note records sha256 of script and output; failed first runs are kept (`_run1_`); corrections are append-only and name what was wrong.
- **The other worker:** Codex/GPT works through the repository and the human. Record model/client identity in any review; do not imply a review happened without its artifact.
- **Hand-off files:** `HANDOFF_2026-11-02_hyperfine_arc.md` (with its reproducibility addendum), `HANDOFF_BC_2026-10-28.md`.


## VII. Index

| layer | where |
|---|---|
| contract, method | `QUESTION.md`, `CLAUDE.md`, `README.md`, `notes/terminology.md`, `notes/inherited_directions_M4-M7.md` |
| floor | `floor/` (containers 00 to 02, M5 spine, M6 spine, field equations, `PROVENANCE.md`, `as_imported/`) |
| maps | `maps/` (critical path, carbon gram, instrument audit, ledger of the 2%, ladders, alpha, lattice, known ratios) |
| route 56 and the lab | `explore/route56_*.py`, `explore/LIVE_WEB_RESULTS.md`, `lab/` |
| E-series instrument | `explore/e_series_*.py`, `explore/E_SERIES_*_RESULTS.md` |
| hyperfine arc | `explore/NUCLEAR_MAGNETON_RESULTS.md`, `HYPERFINE_SERIES_RESULTS.md`, `SIZE_AND_MULTIPLET_RESULTS.md`, `SIZE_EXPONENT_ORIGIN.md`, `HYDROGENLIKE_AND_STEP_RESULTS.md`, `BRAID_CANDIDATES.md`, `TWO_GROUPS.md`, `ARC_EXPLORATION.md`, `NUCLEAR_SIZE_HFS_RESULTS.md` |
| reproducibility | `explore/reproduce.py`, `explore/ENVIRONMENT.md`, `explore/REPRODUCE_REPORT_2026-11-02.md` |
| measured inputs | `explore/data/` (several secondary; each note says which) |
| guard | `guard/` (`check.py`, run by the pre-commit hook on staged files) |


## VIII. Where each claim's proof is (unified index)

| claim | where its equations and proof are here | status |
|---|---|---|
| Containers 00 to 02 | Part I, C-A1 to C-A4; Lean rows 00 to 02 in Part II | PROVED / CHECKED and LEAN |
| Nodes 03 to 67 (formal statements) | Part II table (71 modules) | LEAN, compiled here |
| 120 icosians, 600-cell counts; frustration ε; native continuation T; unique SO(4) form; S³ link spectrum | II-b, C-B1 to C-B5 | PROVED / CHECKED (S³ harmonic spectrum cited) |
| M6 layers C1 to F | Part III | NOT CARRIED (inherited) |
| Route 56: degree-7 threshold | IV.1, C-R1 | PROVED / CHECKED |
| Route 56: all other results | IV.1 table | COMPUTED, recorded, not re-proved |
| BC dictionary, hydrogen α/2, Dirac tan(θ/2) | IV.2, C-C1 to C-C4 | PROVED / CHECKED; maps COMPUTED |
| α running, induced coupling | IV.3, C-D1 | COMPUTED; negative / blocked |
| E-series instrument | IV.6, C-E1 to C-E8 | PROVED given the equations of motion, CHECKED, COMPUTED; C-E7 is an argument only |
| Hyperfine arc | IV.7, C-F1 to C-F8 | mixed: see each entry's status |
| Frontier | Part V | OPEN |

## IX. What is not carried (be explicit)

1. **Whether each Lean theorem is the whole of its node's prose claim.** The theorems compile; no one has compared statement to prose node by node. Where a node's claim is a computation rather than a theorem, the evidence is the container's `derivation.py` and `derivation.json` in `floor/lean_M5/derivations/`, copied and not re-run here. `Container06.Ring` has no `#print axioms`, so its axiom footprint is not stated.
2. **Route 56 results other than C-R1** (IV.1 table): recorded with scripts and hashes, not re-proved. Four inherited scripts DIFFER and `route56_e8_c` to `_f` ERROR in a fresh export; undiagnosed.
3. **The M6 layers C1 to F** (Part III): inherited, not re-derived.
4. **The Fermi contact formula** (C-F1) and **the S³ harmonic spectrum** (C-B5): cited, not proved.
5. **The 36-aspect carbon-gram inventory:** a sourced catalogue; rows not each proved.
6. **The frontier (Part V):** nothing to carry.
7. **The gauge-continuity sign** in C-E3 is confirmed numerically, not derived line by line; **C-E7** (p_E = p_M + 1) is an argument from units.
8. **Independent review:** none. Every proof here was written and checked by the same worker (Claude); the checkers are independent of the prose, not of the author. The other worker (Codex/GPT) has not reviewed this file.
