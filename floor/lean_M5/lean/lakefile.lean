import Lake
open Lake DSL

package «maths5» where

-- MATHLIB (added 2026-08-21, the Mathlib-setup session). The revision is PINNED by
-- lake-manifest.json (mathlib @ 7d6261f2dc0f, matching maths 4's pins so its 418 theorems
-- compile unchanged); this line only makes Mathlib AVAILABLE. It does NOT make any existing
-- container depend on it: a container's axiom footprint is decided by its `import`s, so the
-- zero-axiom cores (00-04, 06-10) stay zero-axiom precisely because they import no Mathlib.
-- ONLY containers whose modules `import Mathlib` widen to Mathlib's three axioms (propext,
-- Classical.choice, Quot.sound), and their Lean must `#print axioms` to confirm exactly those.
require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

-- Container 00 (the distinction / rung 0) imports nothing -- pure core-Lean logic
-- (Prop, Not, Exists), and its deliverable is a ZERO-axiom report, stronger than the
-- lattice containers' [propext]. No Mathlib, no decide.
lean_lib Container00 where
  globs := #[.submodules `Container00]

-- Container 01 (recursive registration / rung 1) imports Container00 and nothing else --
-- the floor-up spine in the kernel. Also zero axioms.
lean_lib Container01 where
  globs := #[.submodules `Container01]

-- Container 06 (the carrier / E8) imports nothing -- pure integer arithmetic decided
-- by the kernel, the zero-axiom standard. Later containers that need real numbers or
-- Euclidean geometry will `require mathlib`; this one does not, and must not.
lean_lib Container06 where
  -- The container's modules live in `Container06/` (e.g. `Container06.Ring`), with no
  -- `Container06.lean` root. The default glob `.one Container06` looks for that missing
  -- root and reports "bad imports"; `.submodules` globs everything under the directory,
  -- so `lake build Container06` builds `Container06.Ring` directly.
  globs := #[.submodules `Container06]

-- Container 02 (the registration event / rung 2) imports Container00.
lean_lib Container02 where
  globs := #[.submodules `Container02]

-- Container 03 (dimensional emergence / rung 3, OPEN) imports nothing -- combinatorics.
lean_lib Container03 where
  globs := #[.submodules `Container03]

-- Container 04 (the integers / additive inverse / rung 4) imports Container01 -- the
-- floor-up dependency in the kernel. Pure Nat arithmetic, zero axioms (no Quotient, so no
-- Quot.sound; cancellation hand-proved to dodge propext). No Mathlib, no decide.
lean_lib Container04 where
  globs := #[.submodules `Container04]

-- Container 07 (ordinal / relational dynamics / rung 4.5) imports Container02 (change) and
-- Container04 (order & direction) -- the dependency position is by import, not the number.
-- Pure integer arithmetic (the directed walk); no Mathlib.
lean_lib Container07 where
  globs := #[.submodules `Container07]

-- Container 05 (the geometric-balance bridge / rung 5, equidistant dimension). Mathlib-FREE: the
-- affine-independence content is exact integer Gram determinants the kernel decides. The general
-- all-N theorem is maths 4's Mathlib result (cited); the port is OWED. (Dir 05-geometric-bridge;
-- the 05-icosahedron stub has no derivation.py and is not built.)
lean_lib Container05 where
  globs := #[.submodules `Container05]

-- Container 08 (metric dynamics) imports Container07 (the ordinal walk); rests conceptually on
-- Container05 (the bridge, which licenses the metric). Exact integer 2-D geometry; no Mathlib.
lean_lib Container08 where
  globs := #[.submodules `Container08]

-- Container 09 (kissing-twelve / rung 6). Mathlib-FREE: exact Z[phi] arithmetic (Int x Int,
-- phi^2 = phi+1); the kissing gap bottoms out at 5 < 9. Rests conceptually on Container05 (the
-- bridge / Euclidean 3-space). The upper bound (no 13th) is external, cited.
lean_lib Container09 where
  globs := #[.submodules `Container09]

-- Container 10 (why-12, the consolidation). Mathlib-FREE, pure Nat by `decide` (zero-axiom): the
-- phase-ledger counting core (12 pi/6-writes fill the 2pi cycle, a 13th overflows), the cap's
-- dimension-independence, and the conditional selection of d=3. The HEADLINE is a POSTULATE (the
-- phase cycle is the adjacency ledger), not a theorem; the trig provenance is cited from maths-4.
lean_lib Container10 where
  globs := #[.submodules `Container10]

-- Container 11 (the icosahedron interior / the rank-6 icosahedral module). Number is a build-order
-- label (the 05 slot went to the geometric-balance bridge). Mathlib-FREE, exact Z[phi] (Int x Int),
-- ZERO-axiom by `decide` with structural recursion only: the rank obstruction (six-direction det 8),
-- the three overlaps (norms 9,16,5), the cuboctahedron non-triangulation, the 12+20 minimal shell.
lean_lib Container11 where
  globs := #[.submodules `Container11]

-- Container 12 (the E8 root system / rung 7). Number is a build-order label; positioned above the
-- carrier (06), whose E8 Gram it consumes. Mathlib-FREE, exact integer `decide`, ZERO-axiom: the 240
-- minimal (norm-2) vectors, verified against the norm-2 criterion (count 240, all norm 2, distinct,
-- negation-closed). The 240-witness list is large, so the module raises maxHeartbeats / maxRecDepth.
lean_lib Container12 where
  globs := #[.submodules `Container12]

-- Container 13 (archic density / physics-bridge Step 1). Number is a build-order label; positioned
-- on the icosahedron (03). Mathlib-FREE, ZERO-axiom by `decide`: the R1 icosahedron is a closed
-- degree-5 triangular mesh (30 edges, 20 faces, Euler 2), the ball-growth observable |B_r(v)| =
-- (1,6,11,12) for every vertex, and |B_1(v)| = deg(v)+1 (the relabelling identity). BFS is monotone
-- set-growth, so the kernel work is linear in the radius. The strict finer-than-degree separation
-- (R3, 162 vertices) is exact-integer computation in the derivation/model, not the kernel.
lean_lib Container13 where
  globs := #[.submodules `Container13]

-- Container 14 (density deficit / physics-bridge Step 2). IMPORTS Container13 (14 rests on 13 --
-- the floor-up dependency; reuses its ball-growth observable). Mathlib-FREE, ZERO-axiom by `decide`:
-- the flat reference flat_ball(r)=1+3r(r+1), the curvature charge (angle deficit = 24 = 12*chi on
-- R1), and the primordial law at r=1 (flat_ball(1)-|B_1|=1=tri(1)). The r>=2 primordial law and the
-- ball-deficit-total conservation span 162+ vertices and are exact-integer in the derivation/model.
lean_lib Container14 where
  globs := #[.submodules `Container14]

-- Container 15 (density extremum / physics-bridge Step 3). IMPORTS Container14 (15 rests on 14).
-- Mathlib-FREE, ZERO-axiom by `decide`: the density extrema values (rho_min = flat-tri at the twelve,
-- rho_max = flat at the mirror, rho_min < rho_max), net positive curvature (12*chi=24>0), and no
-- hyperbolic vertex on R1. The spatial extremum (R4, 642 vtx) is exact-integer in the derivation/model.
-- C.3 (the vacuum/black-hole naming) is a POSTULATE -- possible, NOT confirmed -- so it has no Lean.
lean_lib Container15 where
  globs := #[.submodules `Container15]

-- Container 16 (frustration dynamo / physics-bridge Step 4). Mathlib-FREE, ZERO-axiom by `decide`:
-- the tetrahedral gap eps = 2pi - 5*arccos(1/3) > 0 reduces exactly to the integer core 45 < 49 (the
-- trig provenance cos(2pi/5)=(sqrt5-1)/4 needs R and is CITED, as container 10 cites arcsin(1/2)=pi/6).
-- D.3 (eps as a dynamo, NOT the vacuum) is a POSTULATE -- no Lean.
lean_lib Container16 where
  globs := #[.submodules `Container16]

-- Container 17 (Bekenstein-Compton Stone / physics-bridge Step 5). EXTERNAL, QUARANTINED physics
-- re-derived COLD (our own proof, not an import of maths-4's MassCancellation.lean). Mathlib-FREE,
-- ZERO-axiom: the mass cancellation R*E = hbar*c (m absent) for all Nat -- so BC = 2*pi/ln2. The
-- scalar 2*pi/ln2 needs R and is cited/numeric. Nat assoc hand-proved to dodge propext.
lean_lib Container17 where
  globs := #[.submodules `Container17]

-- Container 18 (Planck-anchor Stone / physics-bridge Step 6). EXTERNAL, QUARANTINED physics re-derived
-- COLD (our own proof, not maths-4's PlanckAnchor.lean, which used Mathlib `ring` at bridge tier).
-- Mathlib-FREE, ZERO-axiom: the crossover hbar*c = 2 G m^2 (Compton = Schwarzschild) and its cleared
-- Planck form, with Nat comm/assoc HAND-PROVED. div-by-G and sqrt (m = m_P/sqrt2) routine/cited.
lean_lib Container18 where
  globs := #[.submodules `Container18]

-- Container 19 (entry protocol / physics-bridge Step 7). INFRASTRUCTURE: the gate for physics
-- correspondences. Mathlib-FREE, ZERO-axiom by `decide`: the QUARANTINE invariant on the concrete
-- bridge dependency graph -- "an entry is never a premise", no DERIVED result rests on a quarantined
-- physics reading; and the crux (18.P.2 rests on the Stone's algebra 17.S.2, not its reading 17.S.3).
lean_lib Container19 where
  globs := #[.submodules `Container19]

-- Container 20 (density gradient / physics-bridge Step 8). Mathlib-FREE, ZERO-axiom by `decide` over
-- Int: the discrete GAUSS LAW (sum_v L(v) = 0, gravity sources sum to zero on a closed graph) and the
-- source sign (a local minimum is a positive source). Full R3/R4/R5 localization is exact-Python.
lean_lib Container20 where
  globs := #[.submodules `Container20]

-- Container 21 (entry: gravity <-> curvature / physics-bridge Step 9). The first FILED correspondence
-- entry. Mathlib-FREE, ZERO-axiom by `decide`: the integral match (substrate deficit 24 = 4*pi =
-- 2*pi*chi, Gauss-Bonnet) and the V(eps) coefficient 6(n+2)=24 for n=2. Gate + routing exact-Python.
lean_lib Container21 where
  globs := #[.submodules `Container21]

-- Container 22 (converge top-down / physics-bridge Step 10, the load-bearer). Mathlib-FREE, ZERO-axiom
-- by `decide`: the CONVERGENCE CONDITION -- given I = alpha*c (alpha>0), the top-down count I/alpha
-- recovers the bottom-up count c. CV.3 (the finding: LI rests on the superseded dcpo floor; the warrant
-- condition awaits the triadic-floor reconstruction + alpha grounding) is OWED, no Lean.
lean_lib Container22 where
  globs := #[.submodules `Container22]

-- Container 23 (level integrality / discharges container 22's owed_a + owed_b). IMPORTS Container13
-- (LI.4: the ball B_r is a registration element and its level is container 13's |B_r|). Mathlib-FREE,
-- ZERO-axiom by `decide`: Theorem LI reconstructed COLD on the triadic floor -- the level L(d)=|A(d)|
-- is a well-defined, path-independent, ADDITIVE integer count of archons. Integrality is STRUCTURAL
-- (a cardinality, no continuum), not a real measure forced onto Z as on the superseded dcpo floor;
-- the non-trivial content is well-definedness + additivity. LI.5 (the alpha-valuation) is a POSTULATE,
-- quarantined (alpha is Stone 5's reading 17.S.3, Step 12) -- no Lean.
lean_lib Container23 where
  globs := #[.submodules `Container23]

-- Container 24 (stone grounding / physics-bridge Step 12). IMPORTS Container23 (hence Container13):
-- grounds the STRUCTURAL alpha. Mathlib-FREE, ZERO-axiom by `decide`: the representation theorem
-- (a constant/symmetric weight alpha gives I=alpha*L; a non-constant weight breaks it -- EAI forced,
-- not assumed; the scale alpha the only freedom), the payoff I(B_r)=alpha*|B_r|, and the c=alpha/tau
-- structural constancy (each registration step contributes exactly alpha). SG.2 (intrinsicness) is a
-- POSTULATE; SG.4 (alpha's VALUE -- base-2/SEC9/Planck, external Stone input) is OWED, quarantined -- no Lean.
lean_lib Container24 where
  globs := #[.submodules `Container24]

-- Container 25 (dimension forcing / physics-bridge Step 11). IMPORTS Container14 (reuses flatBall,
-- angleCharge). Mathlib-FREE, ZERO-axiom by `decide`: the counting law forces the INTRINSIC dimension
-- n=2 (flat_ball degree 2 -- second difference const 6, third difference 0; ring linear; a 1-D line is
-- degree 1), and the curvature coefficient 6(n+2)=24 at n=2 -- whose equality with 12*chi=24 is a SPHERE
-- COINCIDENCE (fails for chi != 2), not a forced identity. DF.3 (the ambient dim=3, container 03's
-- metric no-thirteenth) is OWED, located, decided-failed levers not re-attempted -- no Lean.
lean_lib Container25 where
  globs := #[.submodules `Container25]

-- Container 26 (base-2 forcing / physics-bridge Step 13; alpha-value plan Step 1). IMPORTS Container00
-- (reuses Existential + perceivable). Mathlib-FREE, ZERO-axiom by `decide`: the registrable alphabet is
-- exactly 2 (of 00's three existential states only two are perceivable; base-3 refused; the triad's 3 is
-- OBSERVERS, typed apart from the 2), and the per-registration branching factor is 2 -- base-2 (a config
-- space doubles per registration, 2^(k+1)=2*2^k). B2.3 (the Shannon reading giving ln2 content) is
-- POSTULATE; B2.4 (the ruler's ln2 = the registration bit, SEC9) is OWED -- no Lean. Danger-free: no mass.
lean_lib Container26 where
  globs := #[.submodules `Container26]

-- Container 27 (dimensional accounting / alpha-value plan Path B Step 1). Imports NOTHING -- self-contained
-- dimensional bookkeeping over (L,T,M) exponent triples. Mathlib-FREE, ZERO-axiom by `decide`: the
-- substrate is dimensionless (DA.1), {hbar,c,G} is a dimensional basis (DA.2, det=2 != 0 -> exactly 3
-- anchors irreducibly external), and the per-archon alpha's energy/length readings are Compton-dual
-- (DA.3, sum = dim(hbar*c) = E*R=hbar*c), each a Planck monomial. DA.4 (forcing the dimensionless
-- alpha_hat; disambiguating the reading) is OWED -- no Lean. Introduces no value, touches no census.
lean_lib Container27 where
  globs := #[.submodules `Container27]

-- Container 28 (weak / SU(2) via the carrier -- the first filed FORCE entry). Imports NOTHING --
-- self-contained quaternion algebra (the carrier's ambient H). Mathlib-FREE, ZERO-axiom by `decide`:
-- the imaginary quaternions close under the commutator to su(2) ([i,j]=2k, [j,k]=2i, [k,i]=2j), so the
-- weak Lie algebra IS the internal sector (11); and |2I|=120=2*60 is the SU(2)->SO(3) double cover (the
-- chirality), dim su(2)=3 generators. W.3 (the filed correspondence weak-SU(2) <-> carrier) is
-- POSTULATE; W.4 (the weak dynamics: breaking/masses/reps/coupling -- danger zone) is OWED -- no Lean.
lean_lib Container28 where
  globs := #[.submodules `Container28]

-- Container 29 (EM / U(1) via the carrier -- the second filed FORCE entry). IMPORTS Container14
-- (angleCharge -- the charge) and Container28 (the quaternion comm -- abelian vs non-abelian). Mathlib-
-- FREE, ZERO-axiom by `decide`: the U(1) charge IS the signed angle-defect 12-2d (quantized, signed with
-- a mirror at deg 6: +2/0/-2, total 24 = angleCharge = 12*chi conserved); the U(1) is abelian ([i,i]=0)
-- vs weak su(2) non-abelian ([i,j]=2k), and u(1)(1)+su(2)(3)=4=the quaternion=electroweak. EM.3 (the
-- filed correspondence) is POSTULATE; EM.4 (alpha ~ 1/137, bare coupling unity, an alpha_hat to force not
-- fit) is OWED -- no Lean.
lean_lib Container29 where
  globs := #[.submodules `Container29]

-- Container 30 (strong / SU(3) via the carrier's E8 -- the third filed FORCE entry). Imports NOTHING --
-- self-contained A2 root-system arithmetic. Mathlib-FREE, ZERO-axiom by `decide`: the 6 A2 roots
-- {e_i-e_j} all have norm 2, 6+2=8=dim su(3) (the 8 gluons); the A2 Cartan det = 3 = |Z/3| = the color
-- triality; the cyclic Z/3 (a,b,c)->(c,a,b) permutes the 6 roots (order 3). A2 subset E8 is cited
-- (12.E.3, inner products include -1) -- LESS NATIVE than weak's 2I subset SU(2) (an embedding choice).
-- S.3 (the filed correspondence) is POSTULATE; S.4 (the strong dynamics -- danger zone) is OWED -- no Lean.
lean_lib Container30 where
  globs := #[.submodules `Container30]

-- Container 31 (colour as three seatings -- the native Z/3 of the strong force). Imports NOTHING --
-- self-contained integer-quaternion arithmetic. Mathlib-FREE, ZERO-axiom by `decide`: g3 has order 3 via
-- the integer quaternion (-1,1,1,1)=2*g3 whose cube is (8,0,0,0), so conjugation by g3 gives a Z/3 colour
-- seating (cycles of length 1 or 3); plus the orbit-counting consistency 6+3*38=120 and centralizer
-- 6*class 20=120. The full 120-element Z[phi] cycle structure (6 fixed + 38 three-cycles) is EXACT-INTEGER
-- (verify-guarded). CS.3 (the correspondence, REFINES 30's chosen A2 subset E8 with a NATIVE colour-3) is
-- POSTULATE; CS.4 (the native adjoint / quark census -- danger zone / alpha_s) is OWED -- no Lean.
lean_lib Container31 where
  globs := #[.submodules `Container31]

-- Container 32 (the registration boundary is 2*pi / SEC9 -- the alpha-value chain's load-bearer). Imports
-- NOTHING -- self-contained integer phase-ledger arithmetic. Mathlib-FREE, ZERO-axiom by `decide`: 12
-- writes of 1 radit fill the capacity-12 cycle (= 2*pi, container 10), a 13th overflows -- so the minimal
-- registration boundary is 2*pi, corresponding to the Compton 2*pi (Stone 17 S.3a, discharged as a
-- correspondence). The real 12*(pi/6)=2*pi is cited from container 10; BC=2*pi/ln2 from Stone 17. The mass
-- stays external (27). RB.3 (the filed SEC9 correspondence) is POSTULATE; RB.4 (mass/anchor/value) OWED -- no Lean.
lean_lib Container32 where
  globs := #[.submodules `Container32]

-- Container 33 (the Planck-anchor test -- alpha-value plan Step 3). Imports NOTHING -- self-contained
-- integer + dimension-triple arithmetic. Mathlib-FREE, ZERO-axiom by `decide`: the substrate has a
-- constant edge/tick rate (edges after k ticks = k; edge = minimal adjacency sq dist 4, container 13),
-- and edge/tick = (1,-1,0) = speed = c = l_P/t_P (same KIND, container 27's dimensions). Kevin's Planck
-- hypothesis (edge=l_P, tick=t_P) is filed as a held correspondence (PA.3, POSTULATE) -- STRUCTURALLY
-- CONSISTENT but not discriminating (reproduces c by construction); PA.4 (discrimination / external
-- values / the value) is OWED -- no Lean.
lean_lib Container33 where
  globs := #[.submodules `Container33]

-- Container 34 (the vacuum value / rho_Lambda -- alpha-value plan Step 4, the FLAGSHIP; configuration
-- landed, value OWED). IMPORTS Container14 (flat_ball, tri -> the min density). Mathlib-FREE, ZERO-axiom
-- by `decide`: the vacuum = the minimum archic density (rho_min = flat_ball - tri at the twelve =
-- [6,16,31,51], deficit = tri = [1,3,6,10]); rho_Lambda = alpha x rho_vac is dimensionally an energy
-- density ((2,-2,1)+(-3,0,0)=(-1,-2,1), container 27). VV.3 (vacuum = min density; rho_Lambda=alpha*rho_vac)
-- is POSTULATE; VV.4 (the VALUE = alpha_hat x anchor x count, gated on alpha_hat + 3 external anchors,
-- computed-then-compared NEVER fitted) is OWED -- no Lean.
lean_lib Container34 where
  globs := #[.submodules `Container34]

-- Container 35 (forcing alpha_hat -- the last unknown). Imports NOTHING -- self-contained integer
-- arithmetic. Mathlib-FREE, ZERO-axiom by `decide`: the naive forced value alpha_hat=1 (given the Planck
-- hypothesis, 33); it is REFUTED (predicts rho_Lambda ~ Planck density, order 0; measured cosmological
-- constant ~10^-122, order -122; gap 122, predicted != measured -- the cosmological constant problem).
-- alpha_hat is NOT substrate-forceable; ~10^-122 is the external cosmological scale (the cc problem).
-- NOT a fit (10^-122 is the MEASURED value, cited to falsify). AH.3 (the reading) POSTULATE; AH.4 (the
-- honest end -- alpha_hat irreducibly external) OWED -- no Lean.
lean_lib Container35 where
  globs := #[.submodules `Container35]

-- Container 36 (negative curvature / the LEFT WING of the mirror -- the max-density direction 15
-- deferred). IMPORTS Container14 (flatBall -- the flat reference, one home). Mathlib-FREE, ZERO-axiom by
-- `decide`: the signed curvature D_1 = 6-d (angle deficit 12-2d) across the mirror, negative for d>6
-- (LW.1); the degree-7 star is denser than flat (|B_1|=8 > flatBall 1 = 7, D_1=-1, LW.2); the {3,7}
-- tiling grows faster than flat (validated cold: the recurrence reproduces flat {3,6}; at d=7 the deficit
-- [0,-1,-10,-48,-171,-526] is negative and growing, LW.3); Gauss-Bonnet sum(12-2d)=12*chi puts the wings
-- on different surfaces (right chi=2 genus-0; all-deg>6 chi<0, LW.4). LW.5 (max density <-> black-hole)
-- POSTULATE; LW.6 (closed realization / value / does the substrate go left -- the metric-no-thirteenth) OWED.
lean_lib Container36 where
  globs := #[.submodules `Container36]

-- Container 37 (geodesic motion / the walk accelerating in the curvature field -- free-fall). IMPORTS
-- Container36 (angleDeficit -- the signed deficit 12-2d, one home). Mathlib-FREE, ZERO-axiom by `decide`:
-- flat region => geodesic straight (08's free walk, GM.1); deflection = the angle deficit, the Regge
-- holonomy (GM.2); the sign sets focusing -- twelve (positive) focus, left wing (negative) defocus (GM.3);
-- the discrete acceleration Delta^2 (08.8.7) localizes at the deficit, a ~ curvature (GM.4). GM.5
-- (geodesic = gravitational free-fall; the focusing-sign a test on the vacuum/black-hole readings)
-- POSTULATE; GM.6 (continuum equation / value / mass -- danger zone) OWED. Danger-free geometry.
lean_lib Container37 where
  globs := #[.submodules `Container37]

-- Container 38 (the deflection value / the quantitative geodesic deflection). IMPORTS Container37
-- (deflection) and Container36 (angleDeficit) -- one home each. Mathlib-FREE, ZERO-axiom by `decide`:
-- the per-site deflection = the deficit, 2 radits = pi/3 = 60deg at the twelve (DV.1, pi cited); it is
-- the FULL deficit -- impact-parameter-independent, a conical defect / cosmic string (DV.2, cone
-- geometry cited); the total = 12*2 = 24 radits = 2*12 = TWO full 2pi turns, the DOUBLE COVER (DV.3,
-- Gauss-Bonnet 4pi = 2*pi*chi from 21, the 2I spinor structure from 06). DV.4 (the cosmic-string
-- reading) POSTULATE; DV.5 (the observable GR magnitude -- mass/anchor/continuum, danger zone) OWED.
lean_lib Container38 where
  globs := #[.submodules `Container38]

-- Container 39 (the point-mass limit / opening the continuum door -- the first MASS contact). Imports
-- NOTHING (self-contained integer facts; cites 14/38/25). Mathlib-FREE, ZERO-axiom by `decide`: refining
-- does NOT smear -- the deficit stays 24 radits at 12 cone points (14.B.4/B.5), so the intrinsic continuum
-- is a 12-cone ORBIFOLD, not a smooth sphere (0 concentrated points) -- vindicating 08.8.6 (PM.1). PM.2
-- the 2+1D contact (a conical defect = a 2+1D point mass, deficit = 8*pi*G*m, Deser-Jackiw-'t Hooft;
-- MASS enters as a filed correspondence, quarantined, G owed) is POSTULATE, filed through 19; PM.3 (the
-- 3+1D 1/b is NOT reached by refining -- it needs the ambient dimension, 25.DF.3, the metric-no-thirteenth)
-- DERIVED, rests on PM.1 + 38.DV.2 + 25.DF.3; PM.4/PM.5 (preserve 2+1D, locate the 3+1D hole / OWED) no Lean.
lean_lib Container39 where
  globs := #[.submodules `Container39]

-- Container 40 (the deflection form / the refraction-form test -- is the 1/b true?). Imports NOTHING
-- (self-contained integer facts; cites 38/39 + the eikonal/Green's-fn real analysis). Mathlib-FREE,
-- ZERO-axiom by `decide`: light is a FRONT (refraction), so the deflection FORM is set by the source-flux
-- dimension -- 2D (circle 2*pi*r, dim 1) -> log -> delta = pi CONSTANT (exponent 0, impact-independent,
-- the 2+1D cosmic string); 3D (sphere 4*pi*r^2, dim 2) -> 1/r -> delta = 2/b (exponent -1, b*delta = 2,
-- the Schwarzschild form). The kernel checks the flux-dims (1,2), exponents (0,-1) and the 3D invariant
-- b*delta = 2; pi and 2/b are cited real analysis. DF.5 (the 2*pi->4*pi double-cover route to 3D, 38.DV.3;
-- refines 39.PM.3) POSTULATE, filed through 19; DF.6 (the 4*pi-flux emergence; the magnitude 8*pi*G) OWED.
lean_lib Container40 where
  globs := #[.submodules `Container40]

-- Container 41 (the metric no-thirteenth via the double cover / the ambient dimension is 3). Imports
-- NOTHING (self-contained integer group-theory; cites 28/09/03/38 + Newton-Gregory). Mathlib-FREE,
-- ZERO-axiom by `decide`: 03 left dim=3 a checked negative (census 12 at any d; the 4D 24-cell passes
-- separation). The lever: the carrier 2I is a SINGLE SU(2)=Spin(3), the double cover of SO(3) (28.W.2,
-- 120=2*60, 3 generators; SU(2)=S^3 = the 4*pi holonomy, 38.DV.3). One SU(2)=Spin(3) covers SO(3)=3D;
-- SO(4)=4D needs Spin(4)=SU(2)xSU(2), TWO factors; one carrier => ambient dim 3, EXCLUDING the 24-cell.
-- Then dim=3 => kissing 12 (09.6.4), no 13th (Newton-Gregory, cited) -- discharging the metric part of
-- 03.3.7/01.1.6/09.6.6/25.DF.3. NT.5 (the triad <-> 3 su(2) generators root) POSTULATE; NT.6 OWED (the
-- floor-forcing, Newton-Gregory re-derivation, and the tie to 40's 4*pi-flux for the 1/b).
lean_lib Container41 where
  globs := #[.submodules `Container41]

-- Container 42 (the root of the single SU(2): why the carrier is one H, hence 3D). Imports NOTHING
-- (self-contained integer / Bool algebra; cites 41/06/28 + Frobenius). Mathlib-FREE, ZERO-axiom by
-- `decide`: 41 forced dim=3 from "one SU(2)=Spin(3)" but left the root (why ONE) the numerical POSTULATE
-- "3 observers <-> 3 generators". This roots it as a REDUCTION: (SR.1) "one SU(2) => 3D" IS "the carrier
-- is one H" (ambient 3 = dim Im H, one factor vs Spin(4)'s two); (SR.2/3/5) among the four real normed
-- division algebras {R,C,H,O} the UNIQUE associative (excl. O) + non-commutative (excl. R,C) one is H
-- (Frobenius, cited) -- so the 3 is an OUTPUT; (SR.6) H's imaginary units close "two make the third",
-- i*j=-(j*i) is the chirality. SR.4 (the division-algebra premise) POSTULATE; SR.7 OWED -- no Lean.
lean_lib Container42 where
  globs := #[.submodules `Container42]

-- Container 43 (floor-forcing 42.SR.4: the division property reduces to the bridge + one multiplicative
-- norm). Imports NOTHING (self-contained integer / Bool algebra; cites 05/06/42 + Hurwitz). Mathlib-FREE,
-- ZERO-axiom by `decide`: the group ALONE does NOT force division -- R[Z/2] has the zero divisor
-- (1+t)(1-t)=(0,0) (CN.3) -- so a MULTIPLICATIVE norm is genuinely extra (CN.4, POSTULATE, the isolated
-- root, rooted in intensivity/shares). Given it, positive-definite (bridge 05) + multiplicative => no zero
-- divisors => division, and Hurwitz (cited) + 42's assoc/non-comm => H (real dim 4) => dim=3 (CN.5). So
-- SR.4 is reduced from a broad premise to 05 + ONE named postulate; the group-only shortcut is disproved.
-- CN.6 OWED + the honest tension (CN.4 is load-bearing, close to the crux, but not circular).
lean_lib Container43 where
  globs := #[.submodules `Container43]

-- Container 44 (chirality: the carrier is orientation-pure; parity is not a self-symmetry). Imports
-- NOTHING (self-contained permutation-parity arithmetic; cites 06/28). Mathlib-FREE, ZERO-axiom by
-- `decide`: 06.1's even permutations (sign +1) are closed under composition (even.even=even) -- the
-- carrier is orientation-pure, 2I subset SU(2)=proper rotations (CH.1); a transposition (reflection,
-- sign -1) composed with an even one is odd (odd.even=odd) -- parity carries the carrier into the
-- disjoint conjugate mirror, so the substrate is CHIRAL (CH.2). CH.3 (chirality <-> weak parity
-- violation) POSTULATE; CH.4 OWED. Forces what 28.W.2 only cited. Danger-free.
lean_lib Container44 where
  globs := #[.submodules `Container44]

-- Container 45 (the spinor structure: the carrier carries 2-valued reps; a 2*pi turn acts as -1). Imports
-- NOTHING (self-contained integer quaternion arithmetic; cites 28/06/38). Mathlib-FREE, ZERO-axiom by
-- `decide`: 2I contains the central -1 (order 2, conjugation = identity rotation, yet -1 != +1) -- the
-- non-trivial kernel of SU(2)->SO(3) (SP.1); on the 2D spinor rep 2*pi acts as -1, 4*pi as +1 -- 2-valued,
-- half-integer spin, the 4*pi holonomy of 38.DV.3 (SP.2). SP.3 (spinors <-> fermions; spin-statistics
-- cited, pending the signature/50) POSTULATE; SP.4 OWED. Danger-free.
lean_lib Container45 where
  globs := #[.submodules `Container45]

-- Container 46 (the spacetime signature: time is 1-D, and causality forces Lorentzian (3,1)). Imports
-- NOTHING (self-contained integer arithmetic; cites 07/25/41/33). Mathlib-FREE, ZERO-axiom by `decide`:
-- time is 1-D directed (07's total order = a line, the +/- arrow) + the (3+1) split (LS.1/LS.2); the
-- finite rate c is a causal cone (LS.3); a Euclidean (4,0) metric has NO null cone, so a causal substrate
-- needs one timelike direction (time, opposite sign) + three spacelike = signature (3,1) (LS.4, forced).
-- LS.5 (the pseudo-Riemannian metric identification, filed through 19) POSTULATE; LS.6 OWED. Forces the
-- other half of the dimension result (space was 25/41/42). Unlocks 45.SP.3 (spin-statistics). Danger-free.
lean_lib Container46 where
  globs := #[.submodules `Container46]

-- Container 47 (the focusing resolution: the 37-vs-15 tension is a spatial/spacetime type error). Imports
-- NOTHING (self-contained integer arithmetic; cites 37/15/46 + Raychaudhuri). Mathlib-FREE, ZERO-axiom by
-- `decide`: the twelve carry positive spatial deficit (37 focusing, FR.1); the SPACETIME focusing sign is
-- rho+3p -- vacuum (w=-1) -2rho<0 repulsive, matter (w=0) +rho>0 attractive -- independent of the spatial
-- curvature, so positive spatial K and vacuum repulsion coexist: NO contradiction (FR.3). Resolution (b),
-- forced by 46's timelike direction. FR.4 (which the twelve are) POSTULATE; FR.5 OWED. Danger-free.
lean_lib Container47 where
  globs := #[.submodules `Container47]

-- Container 48 (the closed left wing: closure forces the negative-curvature mirror -- 12 degree-7 at genus
-- 2). Imports NOTHING (self-contained integer closure arithmetic; cites 03/36/14 + {3,7} regular maps).
-- Mathlib-FREE, ZERO-axiom by `decide`: the closure law V(6-d)=6*chi (03) gives the sphere (3,4),(4,6),
-- (5,12) at chi=2 (CW.1); at chi=-2 (genus 2) it forces d>6: (7,12),(8,6),(9,4) -- the mirror under
-- d<->12-d, same V (CW.2); the icosahedron's mirror is 12 degree-7 at genus 2, total deficit -24=12chi,
-- the negative-curvature 'anti-twelve' (CW.3). Realizability held (CW.4, the counting is necessary; the
-- minimal {3,7} regular map is Klein's genus-3/56-vertex); CW.5 OWED. Forces 36.LW.6.a. Danger-free.
lean_lib Container48 where
  globs := #[.submodules `Container48]

-- Container 49 (CPT: the substrate's discrete symmetries C, P, T, unlocked by the signature 46). Imports
-- NOTHING (self-contained integer arithmetic; cites 29/44/46 + the CPT theorem). Mathlib-FREE, ZERO-axiom
-- by `decide`: C = charge conjugation = the degree-mirror d->12-d, negating the charge 12-2d (29), the
-- flat mirror of the wings (36/48), an involution fixing the neutral d=6 (CT.1); P (even/odd orbit swap,
-- 44, violated) and T (arrow reversal, 46/07) are involutions (CT.2/CT.3). CPT (CT.4) via the CPT theorem,
-- unlocked by 46's Lorentz signature (as spin-statistics 45) -- POSTULATE; CT.5 OWED. Danger-free.
lean_lib Container49 where
  globs := #[.submodules `Container49]

-- Container 50 (electroweak mixing: the Cartan is rank 2, so two neutral bosons -> photon + Z). Imports
-- NOTHING (self-contained integer arithmetic; cites 29/28 + the electroweak Cartan). Mathlib-FREE,
-- ZERO-axiom by `decide`: rank(u(1))+rank(su(2)) = 1+1 = 2 (Y + T3), two neutral directions B,W3 (EW.1);
-- the photon is a nontrivial combination (both nonzero), the Z the orthogonal -- a SECOND neutral boson
-- forced (EW.2). EW.3 (photon/Z correspondence, Gell-Mann-Nishijima; the Weinberg angle a value) POSTULATE;
-- EW.4 OWED (angle/Higgs/masses/hypercharge -- danger zone). Danger-free.
lean_lib Container50 where
  globs := #[.submodules `Container50]

-- Container 51 (the SM gauge product: U(1)xSU(2)xSU(3) as electroweak(2I) x strong(E8)). Imports NOTHING
-- (self-contained integer arithmetic; cites 28/29/30/31 + the SM gauge group). Mathlib-FREE, ZERO-axiom by
-- `decide`: the located gauge dims u(1)=1, su(2)=3, su(3)=8 sum to 12 (GP.1); the product structure
-- electroweak(2I) x strong(E8/A2) (GP.2); the caveat (31) that 1+3+8=12 is NUMERICAL not a forced
-- decomposition (8 does not divide the vertex-stabilizer 10) (GP.3). GP.4 (the joint, deferred to the
-- collaborator's fork) POSTULATE; GP.5 OWED (joint/couplings/matter -- danger zone). Danger-free.
lean_lib Container51 where
  globs := #[.submodules `Container51]

-- Container 52 (the continuum limit: the emergent smooth manifold is a 12-cone orbifold sphere). Imports
-- NOTHING (self-contained integer arithmetic; cites 25/38/39/40/08). Mathlib-FREE, ZERO-axiom by `decide`:
-- flat_ball(r)=1+3r+3r^2 -- leading 3r^2 (continuum area-growth), remainder 1+3r lower order, second
-- difference const 6 (degree 2) -> flat 2D coarse limit (CL.1); the 12 cones persist (39.PM.1's orbifold),
-- each pi/3 (2 radits, 38.DV.1), total 12*2 = 24 radits = 4*pi = 2*pi*chi (38.DV.3) -- a 12-cone orbifold
-- (CL.2). CL.3 (GR's smooth manifold = the emergent coarse image, 40/08.8.6) POSTULATE; CL.4 OWED. Danger-free.
lean_lib Container52 where
  globs := #[.submodules `Container52]

-- Container 53 (quantum kinematics: the substrate's U(1) phase, complex amplitudes, unitary evolution).
-- Imports NOTHING (self-contained integer quaternion arithmetic; cites 32/10/29/28/43). Mathlib-FREE,
-- ZERO-axiom by `decide`: the minimal registration boundary is one 2*pi cycle -- a U(1) phase (QK.1);
-- i^2=-1, the complex sector C=R(+)R*i subset H (QK.2); carrier unit-norm SU(2) + multiplicative norm
-- => composition norm-preserving = unitary (QK.3). QK.4 (the assembly = QM's kinematic stage; the BORN
-- RULE the gate, danger-adjacent, closing 43.CN.4) POSTULATE; QK.5 OWED. QK.1-QK.3 danger-free.
lean_lib Container53 where
  globs := #[.submodules `Container53]

-- Container 54 (FIRST CONTACT, Rung 0 crossing A: the light-bending factor of 2, GR vs Newton). Imports
-- NOTHING (self-contained integer arithmetic; cites 40/46/20/14/21 + Eddington 1919). Mathlib-FREE,
-- ZERO-axiom by `decide`: the light FRONT (40) feels BOTH the temporal (g_tt/potential) and spatial
-- (g_ii/curvature) metric parts via the null condition (46), a Newtonian particle feels only the temporal
-- (FC.2); the two parts are locked equal (gamma=1) because potential (rho, 20) and curvature (deficit,
-- 14/21) are one field (grad rho = -grad deficit, 20.G.3) -> ratio = 1+1 = 2, discriminated from Newton's
-- 1 (Eddington 1919 measured 2x Newton) (FC.4). FC.3 the equality POSTULATE (metric correspondence); FC.5
-- OWED (the magnitude 4GM/c^2 b -- G+mass, DANGER ZONE). The first danger-line crossing, on the owner's
-- go, dimensionless-only; passes the CONTACT.md five gates.
lean_lib Container54 where
  globs := #[.submodules `Container54]

-- Container 55 (THE BORN HINGE, Rung 0: |amplitude|^2 = the composition norm = the intensive measure).
-- Imports NOTHING (self-contained integer quaternion arithmetic; cites 06/43/53/05 + the Born rule).
-- Mathlib-FREE, ZERO-axiom by `decide`: N(q)=q*conj(q)=|q|^2 (06.6, quadratic), multiplicative (43), so
-- N(amp)=|amp|^2 (BR.1); the SQUARE is forced -- the quadratic norm is additive over orthogonal (Pythagoras)
-- while the linear modulus is not (BR.2). BR.3 the measure<->probability hinge (closes 43.CN.4 = the Born
-- rule as ONE hinge) POSTULATE; BR.4 the gate ledger (structure passes); BR.5 OWED (Gleason-uniqueness;
-- measurement NOT solved). The highest-leverage non-value crossing; the square forced, probability the held
-- hinge -- NOT a derivation of probability, NOT a solution to measurement.
lean_lib Container55 where
  globs := #[.submodules `Container55]

-- Container 56 (the matter-census structure: substrate fermions carry SM quantum-number TYPES). Imports
-- NOTHING (self-contained integer arithmetic; cites 45/31/44/28). Mathlib-FREE, ZERO-axiom by `decide`:
-- matter is fermionic (spinor reps, 45; MC.1); the colour type-split is 6 colourless SINGLETS (leptons) +
-- 38 coloured TRIPLETS (quarks), 6+3*38=120 (31; MC.2); fermions are chiral (44) with weak isospin (28;
-- MC.3); the three SM quantum-number KINDS are located (MC.4). MC.5 (correspondence) POSTULATE; MC.6 OWED
-- -- the generation count is NOT forced (the substrate 3-folds are DIFFERENT threes, 1+3+8 lesson; naming
-- one 'generations' is renaming, refused), hypercharges need the fork, masses are danger. The danger-free
-- prerequisite for the (gated) Weinberg angle + mass ratios. Nothing fitted; generations NOT fished.
lean_lib Container56 where
  globs := #[.submodules `Container56]

-- Container 57 (CROSSING B, Rung 0: the Weinberg angle sin^2(theta_W)). Imports NOTHING (self-contained
-- integer arithmetic; cites 50/29/28/51/30/56 + the U(2) sin^2=1/2, the SU(5) 3/8, meas 0.23122).
-- Mathlib-FREE, ZERO-axiom by `decide`. theta_W REDUCES to the U(1)_Y-vs-su(2) normalization (WA.2; su(2)
-- carrier-fixed by 28); the abelian factor is SCALELESS ([X,X]=0, 29 => Killing form 0 => g' free in the
-- SM, WA.3); the minimal carrier normalization (quaternion/u(2) trace form) makes T0,T3 equal-norm and
-- gives sin^2=Tr(T3^2)/Tr(Q^2)=2/4=1/2 on the doublet -- REFUTED (1/2 != 3/8; measured ~0.231), a
-- discriminating negative, WA.4. u(2) omits COLOUR; the true value needs the E8->SM embedding (the fork,
-- 51) folding the strong sector (30) in -- SU(5) gives 3/8, cited (WA.5, POSTULATE); the cold value + the
-- RG running are OWED (WA.6). A reduction + a refutation; nothing fitted; the fork is the next unblock.
lean_lib Container57 where
  globs := #[.submodules `Container57]

-- Container 58 (the native hypercharge grading (SU(3)xSU(2)xU(1))/Z6; fork R27/F14 rederived). Imports
-- NOTHING (self-contained Nat arithmetic; cites 31/45/30/28/29/51 + the fork, SM hypercharges, anomaly
-- conditions). Mathlib-FREE, ZERO-axiom by decide. Two native gradings -- colour triality Z/3 (31) and
-- duality Z/2 (45, central -1) -- combine to Z/6 (= the colour element's centralizer <g3,-1>, 31.CS.2);
-- Y6 = -(2t+3w) bijects Z/3 x Z/2 -> Z/6 (HC.2), so the SM group is (SU(3)xSU(2)xU(1))/Z6. The fractional
-- hypercharge Y = -(t/3+w/2) is forced (HC.3); the SM content {Q,L,u_c,d_c,e_c} is anomaly-free
-- (sum m*Y6 = 0, sum m*Y6^3 = 0; HC.4, Lean). Gell-Mann-Nishijima Q=T3+Y abandoned as mass-founded.
-- Absolute levels CONDITIONAL (K2, HC.5 POSTULATE); content selection + 57's theta_W OWED (HC.6); the
-- fork's sin^2(theta_W)=1/phi^3 is a fenced candidate, NOT banked. Upgrades 51's held joint.
lean_lib Container58 where
  globs := #[.submodules `Container58]

-- Container 59 (content selection K2: is the fermion multiplet content forced?). Imports NOTHING
-- (self-contained Nat arithmetic; cites 45/58/31/09/11/56 + the fork R25/R26, the SL(2,5)/A5 irreps, the
-- SM generation). Mathlib-FREE, ZERO-axiom by decide. Forces the matter STRUCTURE -- 2I's 9 irreps (sum
-- dim^2=120), the central-character split A5 {1,3,3',4,5} / spinor {2,2',4',6} (each 60, KS.1); the matter
-- lattice = the 12-vertex conjugation rep 1+3+3'+5 (dim 12, KS.2); the mass spectrum 12/d over {1,3,3',5} =
-- {12,4,4,0} (KS.4). Does NOT force the CONTENT MAP (KS.3, scoped negative): the SM generation is 15 (16
-- w/ nu_R), natural sizes are 12/14/16 -- none is 15 -> which irreps are the fermions is under-determined
-- (the fork's COMPARISON). Consequence (KS.4 POSTULATE): the absolute hypercharges (58) and the fork's mass
-- numbers rest on this un-forced map -- not forced results while K2 is open. Nothing fitted.
lean_lib Container59 where
  globs := #[.submodules `Container59]

-- Container 60 (content selection K2: THE RE-EXAMINATION -- the 'K2 is a root' verdict RETRACTED,
-- CORRECTIONS #9). Imports NOTHING (self-contained Nat arithmetic; cites 59/31/58/12/30 + fork R10, SM
-- content, E8>A2xE6). Mathlib-FREE, ZERO-axiom by decide. The original verdict rested on category errors:
-- (a) irrep DIMENSIONS vs a Weyl COUNT (wrong surface); (b) mass-basis vs weak-basis mistaken for a
-- contradiction (that difference IS the SM's CKM/PMNS mixing); (c) generations dismissed -- they are the
-- OUTER Z/3 (left-mult, fixed-point-free, 40/40/40), distinct from colour = the INNER Z/3 (6 fixed + 38
-- triples), count 3 via 3^1||120; (d) premature root. The Lean now certifies the CORRECTED facts
-- (generation != colour; 3^1||120; E8 = 8+78+3*27+3*27) + the kept-but-vacuous 12/14/16 != 15. The RIGHT
-- surfaces (regular rep C[2I] joint action; E8>A2xE6) are UNTESTED -> K2 RE-OPENED as a partially-structured
-- open problem (RX.4 POSTULATE); the real test OWED and paused (RX.5). An over-correction, corrected.
lean_lib Container60 where
  globs := #[.submodules `Container60]

-- Container 61 (the K2 surface test: do the right surfaces force the SM content? -- answer: no). Imports
-- NOTHING (self-contained Nat arithmetic; cites 60/12/30/31/58 + E8 branchings, the SM generation).
-- Mathlib-FREE, ZERO-axiom by decide. Surface A (E8 = A2 x E6): 248=8+78+3*27+3*27, 240=6+72+162,
-- 27=16+10+1, (3,27)=3 generations (ST.1) -- but generic to every E8 theory, A2 Weyl-arbitrary (31),
-- exotics unprojected -> a filed LEAD not a forcing (ST.2). Surface B (regular rep C[2I], dim 120): the
-- outer-Z/3 generation gives 3 blocks of 40 (3^1||120, substrate-specific count 3, ST.3) -- but a block
-- (40) != one SM generation (15/16), no forced fermion selection (ST.4). VERDICT: K2 OPEN -- content
-- unforced by either surface; count 3 near-forced via generation = the outer Z/3 (ST.5 POSTULATE). The E8
-- GUT 3-generations match is a lead, not banked. Nothing fitted.
lean_lib Container61 where
  globs := #[.submodules `Container61]

-- Container 62 (the K2 embedding-distinction test: does a substrate-native invariant single out an A2 in
-- E8? -- answer: it CUTS but does not FORCE). Imports NOTHING (self-contained Nat arithmetic; cites
-- 12/06/31/61 + E8 A2-subsystem count). Mathlib-FREE, ZERO-axiom by decide. Xi = conjugation by an order-3
-- element g3 of 2I (31's colour operator; the Galois sigma is NOT an isometry). BASELINE: E8 has 1120 A2
-- subsystems, W-transitive (ED.1, computed -- the prose-only claim now checked). g3's fixed locus is an
-- A2 x A2 (12 roots, ED.2); it leaves 4 of 1120 invariant (2 fixed + 2 triality), 372 three-cycles
-- (4+3*372=1120, ED.3); 20 order-3 elements (one class) -> 10 conjugate loci (ED.4). VERDICT: a REDUCTION
-- 'which A2' -> 'which order-3 axis' -- eliminative (opt 2) + residual arbitrary (opt 1), NOT a forcing
-- (opt 3, POSTULATE). A twin of 61's count-3.
lean_lib Container62 where
  globs := #[.submodules `Container62]

-- Container 63 (the native/hand-off/open boundary map for the SM sector). Imports NOTHING (self-contained
-- Nat arithmetic; cites 58/62/57/12 + the E8 GUT chains, SU(5) hypercharge, McKay, fork F13/F14/F15).
-- Mathlib-FREE, ZERO-axiom by decide. NATIVE VALUE: SM group from two native gradings (BM.1); native
-- normalization -> theta_W != GUT 3/8 (BM.3, testable; U(1)_Y abelian/scaleless, 57); mass law (F15);
-- levels-from-structure (BM.4). HAND-OFF: E8-GUT embedding reproduces SM Y via the SAME GUT SU(5),
-- sin^2thetaW=3/8, selecting nothing (BM.2, generic; 62). OPEN: the content map, STRUCTURAL -- spinor
-- matter is an su(2)_L spin-tower {1/2,1/2,3/2,5/2}=14, not SM doublet content (14!=8!=15) (BM.4).
-- Value-gate (BM.5, POSTULATE): forcing past the boundary = importing the SM = renaming; map & hand off.
lean_lib Container63 where
  globs := #[.submodules `Container63]

-- Container 64 (the Coxeter-30 bridge: the substrate's tick IS the E8 Coxeter element). Imports NOTHING
-- (self-contained Nat/Int arithmetic; cites 06/12/61/62/45 + the E8 Coxeter data). Mathlib-FREE, ZERO-axiom
-- by decide. The tick C = L_a . R_b (a order-5, b order-6 icosians) is an order-30 E8 isometry whose char
-- poly is EXACTLY Phi_30 -- eigenvalue angles = the E8 exponents {1,7,11,13,17,19,23,29}, so C IS the E8
-- Coxeter element (CX.1/CX.2, 8 helices of 30 on 240, 4 loops of 30 on 120). Generation = C^10 (pure
-- right-mult, order-3 fixed-point-free, 40/40/40 on 120, grounds 61; CX.3); colour = conj b^2 (fixed locus
-- A2 x A2, 62's cut; CX.4); the fold = C^15 = -I (45's central -1; CX.4); the +phi/2 mass-law walk commutes
-- with the tick (CX.5). The Lean banks the integer bookkeeping (helix counts, Phi_30 degree + exponents
-- coprime to 30, generation 40*3/80*3, A2xA2 signature 12+12+24+24+72=144, C^15 half-turn 15*2=30); the
-- eigenvalue-angle equality and the 120x120 commutation are exact-Python. CX.6 (verdict: the E8 mechanism
-- is DYNAMICAL -- a unification, not a forcing; all Coxeter elements W-conjugate) POSTULATE; CX.7 (a
-- canonical tick, or the impossibility proof; the content selection K2) OWED -- no Lean.
lean_lib Container64 where
  globs := #[.submodules `Container64]

-- Container 65 (the four clocks and the frame-alignment rule -- the owed piece of 64.CX.7). Imports NOTHING
-- (self-contained Nat arithmetic; cites 64/06/12 + the corpus). Mathlib-FREE, ZERO-axiom by decide. The
-- tick's four 30-clocks on the 120 (FC.1) are canonically the four quaternion axes {1,i,j,k} of the
-- Galois-fixed canonical frame (FC.2: 24 Hurwitz units, 8 axis = the Q8 seam): each clock owns exactly one
-- antipodal axis pair, the antipode C^15=-I fixes each clock, and frame-alignment is a SELECTOR -- 288 of
-- 480 ticks align, 6 labelings, 48 each (FC.3), a real cut 480 -> 288 (CORRECTIONS #12's canonicalizer,
-- built). The four clock-origins read 120-4 = 116 = 4x29, the fork's n-p-splitting meter (FC.4, POSTULATE:
-- the origin=+axis is the parity bit; the fork's mass numbers stay CANDIDATE). The Lean banks the integer
-- bookkeeping (seat 4*30=120, 116=4x29; frame 24/8/4; selector 288<480=6*48). VERDICT (FC.5, POSTULATE): a
-- REDUCTION toward canonicalizing the tick, not a forcing (a unique tick needs the arbiter seating, FC.6
-- OWED). Rests on 64. Nothing fitted.
lean_lib Container65 where
  globs := #[.submodules `Container65]

-- Container 66 (the arbiter seating -- does the fork's arbiter lean cut 65's 288 aligned ticks to a unique
-- tick? the piece that would turn the reduction chain 61->62->64->65 into a FORCING). Imports NOTHING
-- (self-contained Nat/Int arithmetic; cites 64/65/06 + the corpus). Mathlib-FREE, ZERO-axiom by decide. Run
-- target out of view, the arbiter census reproduces the fork EXACTLY and unfitted: the arbiter (servicing)
-- clock -- the identity's tick-clock -- has seats 13/13/4 by latitude (universal over the 288, AS.1), total
-- registration-distance lag 81 = 9^2 (universal, AS.2), lean 18-51 = -33 (AS.3); the four-clock total -93 is
-- a TICK-INDEPENDENT substrate constant (the clocks partition all 120). As a SELECTOR the 4-clock lean
-- multiset takes exactly 2 values over the 288 -- (-33,-26,-22,-12) [144] and (-26,-25,-22,-20) [144] -- so
-- it CUTS 288 -> 2 classes of 144 (the max-lean -33 class holds the canonical tick + the proton's -33), NOT
-- -> 1 (AS.4). The Lean banks the integer bookkeeping (shells 120, seats 13/13/4; lag 81=9^2; lean -33,
-- totals -93; selector 2*144=288). VERDICT (AS.5, POSTULATE): a genuine further REDUCTION, NOT the forcing --
-- 144 remain; a unique tick up to parity is OWED (AS.6). Parity = the global carrier-reflection (-93<->+93).
-- Does not touch K2; fork mass numbers stay CANDIDATE. Rests on 64/65. Nothing fitted.
lean_lib Container66 where
  globs := #[.submodules `Container66]

-- Container 67 (conjugation on generation -- how do charge-conjugation-like (colour-flipping) involutions of
-- the 120 act on the outer Z/3? the convention-free SALVAGE from the REFUTED Maths-6 P1 "C = the improper
-- half => preserves the outer Z/3 => generation stands"). Imports NOTHING (self-contained Nat/Int arithmetic;
-- cites 64/49/44/06 + the corpus). Mathlib-FREE, ZERO-axiom by decide. EXHAUSTIVELY over the 120's full
-- isometry group (14400 = |H4|; v->pvq det+1, v->p vbar q det-1), the colour-flipping involutions number 24 =
-- 18 proper + 6 improper; on the outer Z/3 = <R_{b^4}> (64) the 18 proper ALL INVERT, the 6 improper ALL
-- SCRAMBLE, 0 PRESERVE -- identical under 61's left L_{g3} reading (convention-independent). So NO colour-
-- flipping involution leaves the outer Z/3 invariant => charge conjugation C acts NON-TRIVIALLY on it (P1's
-- "improper preserve" had the sign BACKWARDS: improper SCRAMBLE; the P1 bug was a binary flip-vs-not test on
-- a three-way question). C != P (the improper colour-flipper is a carrier self-map; parity is not). The Lean
-- banks the integer bookkeeping (14400; 24 = 18+6; trichotomy 18 invert + 6 scramble + 0 preserve; convention
-- independence; 0 preserve => C non-trivial; 6 improper self-maps). The SM comparison is OPEN/two-sided
-- (CG.6, POSTULATE): test against the universe, not the SM convention -- "divergence" retired. OWED (CG.7):
-- C's orientation (49's d->12-d realization), the outer-Z/3 charge-vs-family identity. Rests on 64/49/44.
-- Nothing fitted.
lean_lib Container67 where
  globs := #[.submodules `Container67]
