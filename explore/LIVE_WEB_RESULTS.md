# Live web, energy = registration rate, and the effective-mass probe — results

Cold anchors for the mass/energy investigation (2026-10-25). Reproduce each with
`py -3 -I -u explore/<script>`. All build the carrier (120 icosians, 720 edges) from scratch.
See also `maps/mass_requirements.md` and `maps/degrees_of_freedom.md`.

## Scripts
- `registration_rate.py` — energy = registration rate, on the carrier.
- `live_web_push.py` — the live relational web (D-arc joint action) kicked, web engagement.
- `effective_mass.py` — ring-down frequency shift → effective mass & damping vs amplitude and κ.
- `link_laws.py` — the two floor-grounded link laws (adiabatic w(ψ) with full variational force; first-order relaxational).
- `pentagon_frustration.py` — the pentagonal vertex-figure (5 triangles) and the frustration ε, grounded in the carrier.
- `pentagon_driver.py` — co-definition driven by the pentagonal 5-cycle circulation carrying ε.
- `pentagon_flux.py` — ε threaded as flux (Peierls phase) per pentagon; the frustration gaps the vacuum mode (∝ ε²).
- `route56_repro.py` — cold reproduction of the F5/F6 Clifford connection (γ, Dirac D=Aγ, faces, μ).
- `route56_massgap.py` — connects the reproduced operator to the mass gap via the pentagon-ε frustration flux.
- `route56_native.py` — the fully-native non-abelian curvature: uniform per-face Wilson holonomy + the native Dirac spectrum.
- `route56_kernel.py` — the 28 massless Dirac modes resolved onto the carrier irreps ({1, 2′, 3′}⊗spinor).
- `route56_chirality.py` — parity test showing the kernel's {1,2′,3′} selection is algebraic (Galois), not geometric chirality.
- `route56_galois.py` — rebuilds the connection on the φ- and ψ-branch graphs and reports each kernel (see §11 caveat).
- `route56_selection.py` — kernel selection rule (ρ⊗2 irreducible), flip-vs-relabel test, L×R content, D^tr energies.
- `route56_shells.py` — the connection on all 7 class-shell graphs, both spinor transports, every level labelled by channel.
- `route56_formula.py` — tests the closed spectrum formula on all 14 operators (run from any directory; needs `route56_shells.py` beside it).
- `route56_meaning.py` — weighted-mix kernel test; shell-meaning tests T1 (hop layers), T2 (flatness, first attempt FAILED — see §13), T3 (continuum limit).
- `route56_meaning2.py` — corrected flatness test with the pull-back transport; pure-gauge identity; layer polynomials; order6+order3 mixes.

## 1. energy = registration rate  [cold, verified]
On the 120-icosian adjacency, the committed 2nd-order wave `ψ_{t+1}=2ψ_t−ψ_{t−1}−c²Lψ_t` has,
for every eigenmode, a per-tick phase advance **measured from the running lattice** equal to
`ω(μ)=arccos(1−(c²/2)μ)` (μ=12−λ) to 6 decimals. Spectrum reproduces the floor set
{12,6φ,4φ,3,0,−2,−4/φ,−3,6ψ} with multiplicities = d² {1,4,9,16,25,36,9,16,4} (massless irrep-5
block = 25 = the kernel). At c≈0.5 the matter-lattice rates land exactly on the torsion
developments 2π/5 (irrep 3, period 5 ticks), 2π/3 (irrep 5). **Scope:** this measures the
*dynamics* face on a *frozen* adjacency — one of three clocks (radit/walk/propagation). The
registration rate is inverted from, and distinct from, the Galois mass {12,4,4,0} (static invariant
vs dynamic rate; the Galois pair 3/3′ share mass 4 but have rates 2π/5 vs 4π/5).

## 2. Live web engagement ∝ μ  [cold, this constitutive model]
Brought the adjacency alive with the D-arc joint action: field ψ on vertices, log-strength `y_e`
on edges, `w_e=exp(y_e)`, stiffness κ; `ψ̈=−L[y]ψ`, `ÿ_e=−κy_e−½w_e|Δψ|²` (reused verbatim).
Sound (energy conserved ~1e-3; **frozen control inert**). Kicking a mode drives the web in
proportion to μ: **corr(web-kinetic, μ)=+0.95**, and the **uniform mode (Galois mass 12) drives it
at 7e-56 = zero**. So at the engagement level the live web orders by μ (registration rate), not the
Galois mass. The coupling is through |Δψ|², so the effect is **nonlinear — it vanishes at linear
order** (small excitations don't re-co-define the web).

## 3. Effective mass: dissipative resistance + stiffness softening, nonlinear, κ-tunable  [cold, MODEL-DEPENDENT]
Ring-down of each mode at amplitude A, comparing bare (w=1) / frozen-static (edges balanced to A,
held) / live (edges moving); `m_eff=(ω_static/ω_live)²`.
- **Nonlinear onset:** at small A, m_eff→1.000, γ→0 (bare). Effects switch on with amplitude.
- **Reactive effect = stiffness softening, not inertial mass:** the live web weakens edges where the
  field has gradients, pulling ω below bare (μ=12, A=2: 3.464→3.309, −4.5%; scales with A² and μ);
  the dynamic residual m_eff stays 0.94–1.0 (slightly < 1) — no clean inertial-mass increase.
- **Resistive effect = damping γ:** mode energy leaks into web re-co-definition (total H conserved),
  growing with A and strongly with μ (μ=12, A=2: γ=0.031, ~20× the static control).
- **κ tunes it:** stiff κ (=4) → frozen limit (m_eff→0.99, γ→4e-5); soft κ (=0.25) → large effect
  (m_eff 0.95), damping peaks near κ=0.5.
- **Reading:** "resistance to acceleration" here is **dissipative** (the web resists change by
  dissipating it into re-co-definition) **plus a stiffness softening** — NOT a reactive stored
  inertial mass — and it is κ-tunable. Matches the native phrasing "resistance = the cost of changing
  the rate of propagation through the matrix."

## The crux — the constitutive link law is not derived
The `exp(y)/κ` response is the D-arc's **modeling choice, not forced by the floor** (its own report
flags "derive or constrain the link response from the floor's registration/phase/lag rules" as the
open task). So the magnitudes above (m_eff, γ, the κ-scaling) are **model-dependent**. The next move
is the constitutive law, not more measurement in this model. Candidate decomposition to test against
the floor: (i) the state-dependence form (co-definition weakens with |Δψ|²); (ii) the response RATE
(floor's stepwise co-definition, container 01 → rate fixed by the tick/hop, not a free κ);
(iii) the ORDER — 1st-order relaxational (dissipative, = the structural arrow F2/F3 toward Haar) vs
the D-arc's 2nd-order conservative. If co-definition is relaxational, the dissipative resistance is
native, not an artifact.

## 4. Floor-grounded link laws (`link_laws.py`)  [cold]
Built the two laws the exp/κ decomposition pointed to, with the variational force done correctly
(verified analytic gradV vs finite-diff, err 1.2e-8 — `ψ̈=−L[w]ψ` drops the ∂w/∂ψ term, which matters).
- **Law A (adiabatic w(ψ), conservative):** a genuine REACTIVE effective-mass *increase* — m_eff=(ω_bare/ω_live)²
  up to **1.22** (μ=12, A=2), scaling with amplitude² and μ. (The earlier "softening/lighter" was the
  dropped-term artifact; done correctly, co-definition makes the mode genuinely heavier.)
- **Law B (first-order relaxational, rate Γ):** adds genuine DISSIPATION (the structural arrow), damping
  rate rising with Γ.
So **fast co-definition → reactive inertia; lagging co-definition → dissipative resistance; the tick rate Γ
sets the balance.** Remaining knobs: β (co-definition strength) and Γ (to be pinned to the tick).

## 5. Pentagonal vertex-figure & frustration (`pentagon_frustration.py`, `pentagon_driver.py`)  [cold structure; additive driver near-null]
The generative unit is the **pentagonal vertex-figure** (5 triangles around a point), not the bare triad;
the out-of-plane apex gives the frustration **ε = 2π − 5·arccos(1/3) = 7.356°** (container 16) — the same ε
that set the electron mass (m_e = 2π/120 − ε/10). Confirmed cold: **every one of the 720 edges has exactly 5
common neighbours forming a clean 5-cycle** (the 5 tetrahedra around the edge, the {3,3,5} edge-figure). A
circulation operator C_e(ψ)=Im Σ conj(ψ)ψ around each pentagon is 0 for a uniform-phase field, nonzero for a
chiral one ("change needs the loop + phase"). **Driving co-definition by Φ=ε+C_e (additive) is near-null:**
C_e (~0.01) ≪ ε (0.128), so additive ε is a uniform, trivial rescale. **Lesson:** a frustration entering as
an additive *scalar* is uniform and trivial; **ε must enter as a FLUX / geometric phase** (holonomy ε threaded
through each pentagon, ungaugeable because pentagons share edges), which gaps the spectrum = rest mass — the
Koide-δ geometric-phase mechanism. Next: the ε-as-flux spectral test.

## 6. ε as FLUX gaps the vacuum mode (`pentagon_flux.py`)  [cold]
Threading holonomy ε through each of the 720 pentagons as Peierls phases **opens a mass gap**. The
Laplacian's zero mode — the **constant/uniform (dispersion-massless) mode, multiplicity 1** (not the
adjacency-λ=0 irrep-5, which is the Laplacian *top*, μ=12) — lifts from 0 to **0.011 at native ε**,
scaling **exactly as flux²** (gap ∝ ε²): f=0.25→0.00069, 0.5→0.00275, 1→0.01099, 2→0.04389. So a
uniform *scalar* frustration is trivial (it rescales), but a uniform *flux* frustration is
**ungaugeable** (a genuine holonomy) and **removes the zero-energy state → the field is massive**.
**Frustration flux → rest mass, with ε the source** (the same ε that set the electron mass). Since the
eigenvalue reads as a frequency², the mass-frequency ω ∝ √gap ∝ **ε (linear)** — the same linear-in-ε
dependence as the electron-mass δ-displacement. Caveats: the least-squares connection realizes ε on
the pentagons exactly but also loads other cycles; the carrier's intrinsic connection is **SU(2)**
(F5/F6 torsion), so the faithful frustration is non-abelian and this U(1) flux is an abelian model;
the gap is dimensionless (unit bridge owed for an absolute MeV number).

## 7. route56 reproduced cold + connected to the mass gap (`route56_repro.py`, `route56_massgap.py`)  [cold]
Before building a new SU(2) connection, checked the spine: it is already in route56 (2026-10-19). Independent
cold rebuild of the F5/F6 Clifford connection reproduces **every banked number**: γ (γ²=−I, γ†=−γ,
γ_ji=−γ_ij); the Dirac operator **D=Aγ** (Hermitian on 240 components, spectrum −7.60845…4.12915, **28 zero
modes** at tol 1e-7 — float γ noise ~1e-8); Tr(D²)=2880; **1200 faces** with Clifford trace
−(8/5)sin(π/5)=−0.940456; Ω=cI−sγ; and the pinned **μ=(48/5)sin(π/5)=5.642738**.
**Connection to the mass gap:** threading the pentagon-ε frustration flux (holonomy ε per pentagon) onto the
banked operator gaps, all ∝ ε² (flux²): the **scalar vacuum mode** (0→0.011 at native ε), the **Dirac zero
modes** (0→0.000165), at energy **V_spec = μ·Σ_faces(1−cosF) = 17.76** with **μ PINNED** (derived, not fitted).
So the frustration-mass carries a non-arbitrary energy coefficient — the constant the pure-U(1) flux lacked.
Caveats: least-squares flux realization (exact gap/V_spec realization-dependent; μ pinned regardless;
ε²-scaling robust); this threads an *abelian* flux on the non-abelian D (route56's own D_a=e^{ia}D) — the
28 zero modes already exist *with* γ, so the fully-native step is the non-abelian *curvature* itself; MeV
bridge owed.

## 8. The native non-abelian curvature (`route56_native.py`)  [cold structure; physical-mass bridge open]
Going fully native (the curvature *in* γ, not an abelian flux on top): the per-face Wilson holonomy
`W = γ_ij γ_jk γ_ki` is **uniform across all 1200 faces** — SU(2), det 1, Tr = −(8/5)sin(π/5) = −0.940456
(std 1.4e-9), SO(3) rotation angle **123.90°**. So the native frustration is a **homogeneous non-abelian
field strength**, already present in γ, not fitted. The native Dirac spectrum `D=Aγ` splits into **28 massless
+ 212 massive** over 12 levels (mults {6,2,12,20,30,24,28,18,8,30,30,12,20}), asymmetric −7.6085…4.1291 — a
real massless/massive split from the pure geometry. **Honest gap:** the native spectrum does *not* obviously
map to the physical mass ladder {12,4,4,0} (mults aren't d²; the endpoints and the 123.90° face angle aren't
recognizable golden/torsion values). So fully-native gives a clean uniform curvature and a real
massless/massive split, but the bridge to physical masses is open; the pinned-μ abelian-flux route (§6–7,
V_spec) stays the controllable handle. Next: identify the 28 massless modes (which carrier sector/irreps).

## 9. The 28 massless Dirac modes = {1, 2′, 3′} ⊗ spinor (`route56_kernel.py`)  [cold]
Projecting ker D onto the carrier irreps (the adjacency eigenspaces = the mass sectors): the 28 are **the
full spinor-doubled content of exactly three irreps** — irrep **1** (λ=12, weight 2), irrep **2′** (λ=6ψ,
weight 8), irrep **3′** (λ=−4/φ, weight 18); 2+8+18 = 28 = 2·(1²+2²+3²), each the *entire* d²×2 block, all
other irreps weight 0. The modes are **spin-unpolarized** (spinor density 14/14). **Key facts:** (i) this is
**NOT the Galois-massless irrep 5** (weight 0) — the algebraic (Galois-readout) and dynamical (Dirac-kernel)
notions of "massless" pick *different* carrier sectors; (ii) the selected irreps are the trivial singlet plus
the **Galois-conjugate (primed)** members 2′,3′ of the d≤3 pairs — suggesting a **chirality/Galois selection**
by the γ-connection (the φ vs ψ branch). Open: the selection mechanism, and whether {1,2′,3′}⊗spinor reads
as a physical multiplet.

## 10. Why {1,2′,3′}: algebraic Galois, not geometric chirality (`route56_chirality.py`)  [cold]
Tested the chirality reading with a **parity** operation — an orientation-reversing reflection (q3→−q3,
det −1) that permutes the 120 icosians. The kernel is **unchanged** (still {1,2′,3′}, weights 2/8/18): the
massless sector is **parity-robust**, so the selection is **not** a geometric chirality/orientation effect
(correcting an earlier guess). It is a **Galois-branch** feature: the kernel eigenvalues {12, **6ψ**, **−4/φ**}
are precisely the Galois conjugates (√5→−√5) of the *excluded* {6φ, 4φ} (6ψ=σ(6φ); −4/φ=4ψ=σ(4φ)). The
γ-connection built on **c=φ/2=cos(π/5)** — one branch of ℚ(√5) — selects the opposite (ψ) branch irreps;
only the field automorphism √5→−√5, not any rotation or reflection, would flip it to {1,2,3}. So all the
"splits" in this arc (Galois-readout vs Dirac-kernel masslessness; the kernel's branch) are algebraic ℚ(√5)
features tied to the φ in γ.

## 11. Galois-branch rebuild (`route56_galois.py`)  [cold observation; interpretation corrected in §12]
The 120-icosian set is Galois-invariant (√5→−√5 permutes it), so on the same points either branch can be
built: **φ-branch** (neighbours at overlap φ/2 = cos π/5, c = φ/2) and **ψ-branch** (overlap ψ/2 =
−1/(2φ) = cos 3π/5, c = ψ/2). Both are 12-regular, γ²=−I to ~1e-9, kernel dim 28. Labelling each branch's
kernel by that branch's *own* adjacency eigenvalues: φ-branch {1,2′,3′} (weights 2/8/18), ψ-branch {1,2,3}
(weights 2/8/18) — the labels swap 2′↔2, 3′↔3, singlet fixed. **Caveat recorded at commit time:** those labels
come from each graph's own eigenvalues. Both graphs are built from the same group, so their eigenspaces may be
the same isotypic blocks under different names. This script does not test whether the kernel *subspace* flips
or only its labels; that is tested in §12.

## 12. Selection rule, correction of §11, and the whole-shell spectrum (`route56_selection.py`, `route56_shells.py`, `route56_formula.py`)  [cold]
**Correction of §11.** The φ-graph and ψ-graph kernels are the **same subspace** (overlap tr(Π_aΠ_b)/28 = 1.0000):
both graphs come from one group, so they share the isotypic blocks V_ρ, and the §11 "flip" was a relabeling by each
graph's own eigenvalues. The two graphs are nevertheless **different operators** (same kernel, different massive
spectra: e.g. channel 2→1 is −7.0534 on the φ-shell and −11.4127 on the ψ-shell).
**Selection rule (derived, verified on all 9 irreps × 3 connections).** ker D = ⊕ V_ρ⊗C² over {ρ : ρ⊗2 irreducible}. For f in V_ρ,
D(f⊗χ)=0 ∀χ ⇔ A(fQ)=cλ_ρ(fQ); fQ lies in the blocks of ρ⊗2; λ_σ = |C|χ_σ(h)/d_σ and χ_2(h)=2c, so irreducible ρ⊗2=σ gives
λ_σ=cλ_ρ identically; reducible → components with different λ → not in the kernel. Only ρ ∈ {1,2′,3′} qualify (1⊗2=2, 2′⊗2=4, 3′⊗2=6).
**The genuine Galois flip** is swapping the *spinor transport* 2→2′ (Q′ = Q∘σ, a homomorphism, character χ_2′; σ(2I) is the mirror
copy, so Q′ is not indexed by vertices): the kernel becomes {1,2,3}, overlap with the original 2/28 (the shared singlet).
**Content.** Kernel = (σ_L,ρ_R) = (2,1)⊕(4,2′)⊕(6,3′), 2+8+18 = 28 modes; left-fold-odd (spinor-like) 20, even 8. Each block is an irreducible,
mutually inequivalent L×R rep, so any L×R-invariant perturbation lifts the 28 into three levels (Schur; argued, not run). D^tr = cD + sA⊗I
(checked 1.8e-9) acts on the kernel as s·λ_ρ: 7.0534(×2), −2.1796(×8), −1.4531(×18) (ratios 12 : 6/φ : 4/φ), and D has the exact shadow at −sλ_ρ.
**All seven class-shell graphs** (overlap cos(nπ/5), n=1..4, plus 1/2, 0, −1/2; the antipode c=−1 is degenerate), transports 2 and 2′ (14 operators):
(i) **closed spectrum formula, exact on all 14:** level(ρ→σ) = (c′λ_ρ − λ_σ)/s′, multiplicity d_ρ d_σ, over σ ⊂ ρ⊗τ (max diff ≤2e-8);
(ii) the **core kernel (1→2, 2′→4, 3′→6) is identical on all 7 shells**; extra zero channels only at order 6/3 (+18, kernel 46) and order 4 (+124, kernel 152);
(iii) **antipodal shells** c ↔ −c: level₋c = ε_σ·level_c (ε = fold parity of the left irrep), 16/16 channels in all three pairs; the Galois-conjugate
shell pairs are n=1↔3 and n=2↔4; (iv) channel 2→1 has level −|C| sinθ_n.
**Limits.** The route56 assembly is one choice (not unique); no MeV scale; the ε-flux breaks L×R and its effect on the three levels is untested.

## 13. Weighted mixes keep the core; what the shell family means (`route56_meaning.py`, `route56_meaning2.py`)  [cold]
**Weighted mixes.** 180 random mixes Σ w_c D_c of the 7 shell connections (positive, signed, sparse; transport 2): kernel dimension **exactly 28 every
time**, core intact to 1e-9. Mixes of only the special shells (order 6, 4, 3): 28. Order 6 + order 3 with generic weights: **46** (the extra 6→3′
channel survives). Order 6 + order 3 with **equal weights: 146 = 120 + 8 + 18** — by level₋c = ε_σ·level_c every left-fold-odd channel (120 modes)
cancels, and the core channel 2′→4 (8) and 6→3′ (18) are already zero (count worked out after seeing 146). Mixing the two spinor transports,
a·D⁽²⁾ + b·D⁽²′⁾ on the n=1 shell: kernel **2** (the singlet block only).
**T1 — hop layers.** The shells are the hop-distance layers of the 600-cell graph (sizes 1, 12, 32, 42, 32, 1): d1 = n1; d2 = n2 + order 6 (12+20);
d3 = order 4 + n3 (30+12); d4 = order 3 + n4 (20+12); d5 = antipode.
**T2 — flatness. The first attempt FAILED (errors 1.6, 15, 190 for n=2,3,4), and the cause was my test design, not the physics:** I built the
twisted adjacency with push-forward blocks Q_jQ_i†, whose matrix products compose the transports in the wrong order. With the pull-back transport
Ω_ij = Q_iQ_j† = c − sγ_ij (route56's "full return transport"): TO(A) = W(A⊗I)W† with W = diag(Q_i), **exact to 1e-16 — the transport is pure
gauge (flat, F6)**; TO(A₁)ⁿ = Σ m_n(c) TO(A_c) with the same walk counts as A₁ⁿ (relative error ~3e-9, float); and
**D_c = (c·A_c⊗I − W(A_c⊗I)W†)/s_c, exact to 3e-9** — D_c is the frame-twist difference of the shell sum (flat connection, frame Q: teleparallel),
which is why the channel formula is (cλ_ρ − λ_σ)/s. **The shells are not graded n-th powers:** the distance-2…5 layers are degree-8 polynomials in
A₁ (the 600-cell graph is not distance-regular); A₁² = 12I + 5A_{n1} + 1A_{n2} + 3A_{order6}, so literal walk-powers are specific weighted
*mixes* of shells (which keep the core).
**T3 — continuum limit.** On the six irreps that are restrictions of SU(2) irreps (d = 1,2,3,4′,5,6) the lattice eigenvalue equals the SU(2) shell
formula |C| sin(dθ)/(d sinθ) to 5e-14. Its small-angle limit, level/(|C|θ/3) → (d−1) for d→d+1 and −(d+1) for d→d−1 (closed form evaluated down to
θ = 0.01), are the eigenvalues of 2σ·J: the teleparallel (left-invariant-frame) Dirac operator on S³; the Riemannian Dirac operator is that plus 3/2
(analytic, standard). The continuum operator's only zero is the constant spinor (channel 1→2); the core channels 2′→4 and 3′→6 have no SU(2)
analogue. The lattice at its smallest angle (36°) is coarse: 6% (d=2), 24% (d=3), 45% (d=4), 66% (d=5) below the continuum value, so the
identification rests on the exact chain formula, not on lattice convergence.
**Not tested / no basis to test:** any comparison with observation; any identification of these levels as physical masses; whether shell weights carry meaning.

## 14. Scale flow under geodesic subdivision (`route56_subdiv.py`, raw output `route56_subdiv_all.out`)  [cold]
**Setup.** Each of the 600 tetrahedral cells is cut into the barycentric lattice at frequency n and projected to S³ (n=1: the inherited 120-vertex n=1 shell
graph; n=2: 840 vertices; n=3: 2760). Edges = the 12 FCC-type neighbours. Operator **A** is the route56 rule on the refined edges, unit weight, per-edge overlap
c_ij = p_i·p_j: D_ij = (Q_jQ_i† − c_ij)/s_ij = −i n_ij·σ (Hermitian to 0). The only scale is geometric, κ = mean_i(Σ_j θ_ij)/3 (0.6283·4 = 2.5133, 1.2915, 0.8665
for n=1,2,3), not fitted. Control **B**: least-squares first-order discretisation of the same teleparallel operator on the same mesh (scale 1 by construction).
Test functions: the sampled SU(2) matrix elements D^(d)_{mm'}(p), d ≤ K, ⊗ C²; Ritz values of the compressed operator. The continuum targets are the
teleparallel levels (d−1) ×d(d+1) and −(d+1) ×d(d−1) (branch fixed by the data: this frame gives +(d−1), −(d+1)).
A first version calibrated on a "6-fold level" and found none — the lattice splits the continuum multiplets by 2I, and I had asked for the wrong thing; the
geometric κ replaced the calibration.

**Result (A/κ Ritz levels; B agrees to 3 digits).**
| target (mult) | n=1 (θ=36°) | n=2 (18.50°) | n=3 (12.41°) | err/θ² at n=1,2,3 |
|---|---|---|---|---|
| +1 (6) | 0.9355 | 0.983 | 0.992 | 0.163, 0.163, 0.170 |
| −3 (2) | −2.806 | −2.948 | −2.977 | 0.49, 0.50, 0.49 |
| +2 (12) | 1.514 | 1.864 | 1.938 | 1.23, 1.30, 1.32 |
| −4 (6) | −3.027 | −3.728 | −3.876 | 2.46, 2.61, 2.64 |
| +3 (20) | 1.643 | 2.592 | 2.811 | 3.44, 3.91, 4.03 |
| −5 (12) | −2.738 | −4.319 | −4.686 | 5.73, 6.53, 6.69 |
The constant spinor stays an exact 2-fold zero at every n. **In the smooth (SU(2)-chain) sector the lattice levels approach the continuum integers with error ∝ θ²**
(err/θ² flat to ~5–15% over a factor 2.9 in θ). The 6/24/45/66% gaps of §13 are the first rung of this flow, not a defect of the identification; the
"too coarse to confirm the continuum" and "the identification is exact on the chain" statements are the two ends of one scale flow.

**What this does NOT show (read before citing).**
1. *Strong convergence is not shown.* Leakage ||(1−P)DP|| does not vanish: A 0.256/0.232 (d≤3, n=2/3), B 0.215/0.334. The mesh is not uniform (local
   anisotropy up to 1.19; at n=3 the new vertices have neighbour-direction imbalance 0.13, an O(1) first-order inconsistency there). Ritz values converge;
   the operator norm on the smooth subspace does not (yet). A mesh with consistent weights or a regular refinement is needed to close this.
2. *The non-smooth sector does not flow to the continuum.* Only 2 modes below |λ|<0.5 belong to the continuum, but the lattice has 52, 202, 312 (n=1,2,3):
   lattice levels below 1 in |λ|: 108, 382(A)/364(B), 704(A)/734(B). Most low-lying modes are not SU(2) harmonics and their levels go *down* with n
   (lowest nonzero: 0.289, 0.101, 0.0055–0.0071). They are the Galois-conjugate / non-chain irreps (2′, 3′, 4 …) plus mesh modes; I did not separate them.
3. *The 28-mode massless core is not refinement-stable.* Kernel dimension: 28 (n=1), 30 (n=2), **4** (n=3; mesh imbalance). The smooth sector contributes exactly
   the constant spinor (2); the remaining 26/28/2 are non-smooth. Whether the core is a lattice (doubler-like) object, or survives on a refinement that
   keeps full L×R balance, is open; at n=3 it did not.
4. A and B share the mesh and (for B) the answer assumed; their agreement shows A is the teleparallel operator to leading order, not that the mesh is good.
5. Frequencies 1–3 only; the quasicrystal inflation (the other refinement the corpus has) is untested, and the user's view is that it is not an either/or with
   subdivision. No MeV scale, no observation, no identification of levels as masses.
Command: `py -3 -I -u route56_subdiv.py 1 2 3 > route56_subdiv_all.out` (~70 s). sha256: route56_subdiv.py 7d2a7a4f4905c4bb57caec44427ad0059d9074d22d499381bf559e47371f67c1; route56_subdiv_all.out 690eaa5c8e74d4d744a380fcb71ba27226f7545aa0b40ca5a59cb1418ead4899.

## 15. The quasicrystal refinement; clues from Skull Candy (`route56_quasi.py`, `route56_quasi2.py`)  [cold, dispersion only]
**Source read (C:\Users\Dad\OneDrive\Desktop\Active\skull candy, repo HEAD 2bfaf0b "v20 quasicrystal DOS on the carrier").** What bears on the scalar
interactions: `SESSION_HANDOFF.md` §0 ("scale-up is one continuous geometry talking across the seams … harmonics, scalars, scalar walks and pathing");
`silicon/coresident/interferometer/seam_loops.py` (the seam is the *scalar alphabet* — the overlap values — carried by each tick-loop; Q8-loops vs φ-loops
carry distinguishable alphabets, with a random-partition negative control); `sim/distinguish/RESULTS_v4_scale.md` + `rtl/web_engine_scale.sv` (S scaled copies of the
carrier, each node coupled to its own direction at the neighbouring scale by an exact ×φ^{±2} (or ×φ^{±1}) in ℤ[φ]; 1,561,680/1,561,680 lines bit-exact;
the walk climbs one scale per tick; per-scale shape of the dominant eigenvector is scale-invariant); `RESULTS_v15_nested.md` (tick and seam commute,
[T,M]=0; ×φ^{-2} then ×φ^{2} is lossless); `RESULTS_v20_dos.md` + `dos_web.py` (the walk is tight-binding; kissing-12 motif spectrum
{−√5×3, −1×5, √5×3, …}; dominant pseudogap at filling 12/13, e/a = 24/13 = 1.846; the stated ceiling is KPM on the φ-inflated extended quasilattice).
My reading, to be corrected if wrong: the "scalar interactions" are (a) the shell scalars c (the alphabet) and their class-sum eigenvalues λ_X, which
are exactly what enter my channel formula (c′λ_ρ − λ_σ)/s′, and (b) the radial φ^{±2} dilation. I tested (b): the S=6 dilation chain M (hops φ² out,
φ^{-2} in) is a diagonal similarity of the plain path graph, max|M − D P D⁻¹| = 4.4e-16, spectrum 2cos(kπ/7) to 5.6e-15. **The scalar dilation seam is pure
gauge (flat, product around every in-shell square = φ²·φ^{-2} = 1), like the SU(2) transport (§13).** It adds the path spectrum to the shell spectrum
and nothing else; the ×φ growth seen in the raw amplitudes is the gauge factor, which is why only the shape is scale-invariant.

**Quasicrystal refinement.** The inherited Maths 6 6D→3D icosahedral cut-and-project (`explore/scale.py`, triacontahedron window, first shell 0.78,
19588 vertices at K=6) is a refinement of the *local icosahedral motif in R³*, not a refinement of S³; the connection transfers because the per-edge
object is γ_ij = −i n_ij·σ (§14), whose continuum limit in flat R³ is the Weyl operator σ·p (levels ±|k|, no curvature shift).
- **FAILED first test (`route56_quasi.py`, output `route56_quasi.out`): open-ball state counting.** The simple-cubic control gave 42 zero modes and a
  count slope of 0.08 against Weyl's 3; the quasicrystal gave slope ≈ 0.8–1.0 with hundreds of modes at L = 0.15. Cause: truncated stencils at the
  surface of a small ball (interior imbalance and anisotropy also large: 3.9 and 1.7 for the quasilattice) create O(1) boundary modes; the pipeline was not a valid
  Weyl counter, so **this test shows nothing about the quasicrystal either way.** (Also: interior degree is ~18, not 12–13.)
- **Replacement (`route56_quasi2.py`, `route56_quasi2.out`): Gaussian wave packets, no eigen-decomposition, no boundary.** ψ = g e^{ik·x} u_±(k) at the centre
  of a ball of radius 4.2 widths; E = ⟨ψ|D|ψ⟩/⟨ψ|ψ⟩ against ±|k|. Control (simple cubic): E/|k| = 0.9257 for every |k| ≤ 1 — exactly the analytic envelope
  factor e^{−1/(4w²)} = 0.9257 for w = 1.8 (central-difference sin averaged over the packet), so the machinery is validated. Quasicrystal (N = 8386, w = 1.8):
  B 0.9595, 0.9434, 0.9189, 0.8741 and A/κ 1.0278, 1.0109, 0.9853, 0.9383 at |k| = 0.4, 0.7, 1.0, 1.4; w = 2.4 (N = 18258): B 0.9727, 0.9563, 0.9314; A/κ 1.0044,
  0.9878, 0.9626 at |k| = 0.4, 0.7, 1.0. **The Weyl dispersion E = ±|k| holds to 1–4% at low k with no fit (κ geometric), and is isotropic:** over 8 random directions × 2 helicities
  min = max to 1e-4 (e.g. A/κ 0.9852–0.9853 at |k| = 1) against 0.9246–0.9255 for the cubic control (icosahedral symmetry has no l = 4 invariant). The
  shortfall shrinks with a wider packet, as the envelope-plus-lattice-curvature account predicts (A/κ at |k|=0.4: +2.8% → +0.4%).
**Not shown.** (1) Residuals ‖(D−E)ψ‖/‖ψ‖/|k| are 1.2–2.5, but the continuum value for this packet is √(3/2)/(w|k|) (1.7 at w = 1.8, |k| = 0.4): the residual is the envelope's, not
the lattice's; A has visibly more (2.47 vs B 1.55 at |k| = 0.4), consistent with unit weights on an uneven mesh. (2) This is a dispersion check on the smooth sector; it says
nothing about doublers or the non-smooth low modes of §14 (not probed; high-k and zero-mode content of the quasicrystal is untested), nor about the 28-mode core. (3) Spherical region around
a vertex-free origin, one realisation, no inflation sequence: the φ³-self-similarity of the quasilattice has not been used as the refinement parameter.
(4) No link yet from the R³ quasicrystal to the S³ carrier (how the orbifold/double-cone relates), no observation, no mass identification.
Commands: `py -3 -I -u route56_quasi.py > route56_quasi.out`; `py -3 -I -u route56_quasi2.py > route56_quasi2.out`. sha256: route56_quasi.py 23f48650…739a3f; route56_quasi.out 94bbb33f…540522; route56_quasi2.py baa9634e…343238; route56_quasi2.out ffc45e4a…df8cb (full values: `sha256sum explore/route56_quasi*`).

## 16. Self-similarity, doublers, deviation floor, and the R³↔S³ link (`route56_scale.py`, `route56_link.py`; raw `route56_scale.out`, `route56_link.out`)  [cold]
**1. The inflation unit is φ³, exactly.** For the 19589-point cut-and-project set: φ³·Λ ⊂ Λ with fraction **1.0000** whenever the image lies inside the generated
region (|x|<1, 1.5, 2.0: 13/13, 103/103, 213/213), 0.965 at |x|<2.5 only because the images reach the box edge (10.59 of 10.91 available); φ·Λ and φ²·Λ
are *not* subsets (0.077–0.568, identical for φ and φ²). (The internal coordinate shrinks by (−1/φ)³.) So the lattice contains a coarse copy of itself at every φ³.
**2. Doublers (packet scan, 1<|k|<9; `E(k)` sign change and ‖Dψ‖/‖ψ‖ against the k=0 envelope floor 0.680).** Control, simple cubic: E changes sign at
k = 3.20, 4.48, 5.52 along x, (110), (111) = π, π√2, π√3 (to the 0.08 step) and ‖Dψ‖ falls to the floor (0.63): the detector works. Quasicrystal: E(k)
changes sign at |k| = 6.1–7.1 in **every** direction tested (5-,3-,2-fold axes + 4 random; a = 0.69, so |k|a ≈ 4.4–4.9). Operator B (LS-consistent) never reaches the floor
(min ‖Dψ‖ 0.87 on the 5-fold axis, 0.97–1.05 elsewhere): a sign change of the helicity-projected energy but no zero-energy state in the sampled directions. Operator A (route56's
raw rule, κ geometric) reaches 0.67 on the 5-fold axis and 0.81–0.89 in four others, E ≈ 0.00–0.15: **A has near-zero-energy high-k states (doubler-like); B does not.** Directions
sampled coarsely (step 0.12, 7 directions); a packet cannot resolve a gap below ~1/w.
**3. Deviation law (B, packets of width 1.5/1.8/2.4, |k| = 0.3–1.4, 4 directions, 15 points).** 1 − E/|k| = α/w² + βk² + γk⁴ with α = 0.103 (envelope), **β = 0.0517**, γ = −0.0019,
max |fit−data| = 0.0021. With mean edge a = 0.693: **δ_lattice = 0.0248 (ka)²**. For A the same fit is poor (max error 0.029, α < 0) — the unit-weight rule is not consistent on this uneven mesh.
**4. Where the smooth-sector deviation reaches a floor (my reading of "sigma": the lattice-vs-continuum deviation of the smooth sector; if you meant the Galois σ or a statistical σ, say so).**
| floor | k·a | λ/a | φ³ steps above the lattice | φ steps |
|---|---|---|---|---|
| 1e-2 | 0.63 | 9.9 | 1.6 | 4.8 |
| 1e-6 | 6.3e-3 | 9.9e2 | 4.8 | 14.3 |
| 1e-9 | 2.0e-4 | 3.1e4 | 7.2 | 21.5 |
| 1e-12 | 6.3e-6 | 9.9e5 | 9.6 | 28.7 |
| 1e-16 | 6.3e-8 | 9.9e7 | 12.8 | 38.3 |
One decade of length = 1.595 φ³ steps. So **in the smooth sector the lattice signature is below 1e-12 about ten φ³-inflations above the lattice spacing and below double precision at ~13**;
a tower of ~97 φ³ steps spans 61 decades. Caveats: (i) the k² law was measured only for ka ≈ 0.2–1 and is extrapolated ~8 decades; (ii) it is the smooth sector only — the
non-smooth/high-k sector (§14, item 2; doubler-like states above) sits at fixed ka ≈ 4–5 at every scale and does not flow down; the structure that survives below a smooth-sector noise floor
is that lattice-scale sector; (iii) no lattice constant in metres is established (hop↔metre owed), so no physical scale is claimed.
**5. The link R³ ↔ S³ (`route56_link.py`).**
(a) *Local chart.* The 600-cell star in the log chart has shells 12 (36°), 20 (60°), 12 (72°), 30 (90°) with radius ratios 1, 1.667, 2.000, 2.500; the quasicrystal around its
icosahedral origin has 12 (0.707), 30 (1.203), 60, 20 (1.686), 60, 30 … with ratios 1, 1.701, 1.973, 2.384. **Only the first shell (the kissing-12 icosahedron) coincides**; beyond it the
orbit sequences differ. Both are unions of icosahedral-group orbits, nothing more is identified.
(b) *The exact link is algebraic.* The 120 units are the unit shell of the 4D icosian quasicrystal (the icosian ring is the E8 cut-and-project with Galois conjugation as the internal space);
the S³ refinement is the set of directions of icosians of larger norm. For a pair at overlap class c, u+v has |q|² = 2+2c and internal norm |σ(q)|² = 2+2σ(c); norm product 1 ⇒ existing vertex
(classes 1/(2φ), −1/2, −φ/2), otherwise a **new direction with norm product 5 (classes φ/2, −1/(2φ): the edge midpoints, √5), 9 (class 1/2: 3²), 4 (class 0: 2²)** — the refinement ladder runs along the
primes 2, 3, √5 of ℤ[φ]. One rung (all pair sums): 2520 new points, 2640 on S³.
(c) *The route56 rule on that set* (kNN-14 edges symmetrised; mean edge 13.28°; counting-measure Ritz on SU(2) harmonics, d≤4): A/κ levels +0.983–0.992 (target 1, ×6 split by the set's symmetry), 1.86–1.97 (2), 2.59–2.93 (3), −2.968 (−3), −3.83 (−4), −4.46…−4.69 (−5); B similar.
At comparable angle the geodesic subdivision gave 0.992, 1.938, 2.811, −2.977, −3.876, −4.686 at 12.41°: **the two refinements flow to the same continuum integers with comparable θ² coefficients** (e.g. level +1: err/θ² ≈ 0.17 in both).
(d) *Zero modes / the 28-core on this set (full spectrum, 5280 modes).* Kernel = **2** for both A and B (the constant spinor only); modes below |λ|<0.5: 712 (A), 678 (B) against 2 in the continuum; lowest nonzero |λ| 0.0017/0.0025.
**The 28-mode core does not appear on this refinement, nor on the n=3 subdivision, nor on a non-group R³ set** — it is a feature of the exact 2I×2I-symmetric 120-vertex (and its symmetric n=2) graph; the kNN construction here is irregular, so this is "not seen on this
graph" rather than "excluded" (a regular, symmetric icosian refinement graph is the clean test). The 28-core is defined by the 2I irreps and has no direct R³ analogue; on R³ I tested the doubler content instead (item 2).
**Not done.** Window-restricted icosian ladders beyond one rung (sums of three units); an exactly symmetric edge rule for the icosian set; periodic approximants of the R³ set (the only way to get a boundary-free spectrum there); relating the 2D orbifold; any observation.
Commands: `py -3 -I -u route56_scale.py > route56_scale.out` (~3 min), `py -3 -I -u route56_link.py > route56_link.out` (~1 min). sha256 route56_scale.py 89cf67f7…18e33; route56_scale.out 02da7acf…f08ba; route56_link.py f898a421…ac14; route56_link.out f6ee9dac…5e44 (full values: `sha256sum explore/route56_scale* explore/route56_link*`).

## 17. Bandwidth and dispersion cap (`route56_band.py`, raw `route56_band.out`)  [cold, packet part ±10%]
Units ħ = c = 1, a = mean edge length (S³: arc angle). **E_max·a is the band top in units of ħc/a.**
**Full spectra (exact).** Geodesically refined 600-cell, A/κ and B agree: n=1 (120 pts, a = 0.6283): E_max = 3.0273, **E_max·a = 1.9021**; n=2 (840, a = 0.3229): 4.8476/4.8367 (A/B), **1.5652/1.5617**;
n=3 (2760, a = 0.2166): 6.8465/6.7939, **1.4832/1.4718**. Top 10% of the spectrum holds 20, 142, 474 modes. Quasicrystal ball, A/κ: E_max·a = 1.436 (N=700), **1.552** (N=1300), top six eigenvectors with 0.84/0.99 of their weight in
the interior (bulk edge). B's top eigenvectors have 0.00–0.01 interior weight: **surface modes, so B's 2.29 (E_max·a 1.56) is not a bulk edge.** Simple cubic (analytic): E_max·a = 1 at k = π/2.
**Dispersion from packets (w = 2.4; |d|_est = √(‖Dψ‖² − 1.5/w²)).** *Validation on the cubic control:* the estimator is ~10% low (|d|max 0.905 vs 1; 0.76/0.82 vs 0.841/0.909 at k = 1, 2; (111): 0.85/1.45 vs 0.945/1.584),
v_g(0) reads 1.10–1.12 vs 1, m*/E_top reads 1.19–1.20 vs 1. *Quasicrystal, operator B (7 directions agree to 1%):* v_g(k→0) = 1.04; max v_g = 1.22; band top |d| = 1.78 (est.) at k = 3.0, i.e. **ka ≈ 2.07**, E_top·a ≈ 1.23–1.24;
m*/E_top = 1.27–1.29. Applying the cubic bias, v_g max ≈ v_g(0) ≈ 1 and m*/E_top ≈ 1.06 ± 0.1. |d|(k = 1, 2, 4, 6) = 0.90, 1.55, 1.58, 0.77: linear to ka ≈ 0.7, saturating by k ≈ 2 (ka ≈ 1.4), top at ka ≈ 2.1, falling after.
Operator A: the estimator is contaminated (v_g(0) reads 0.58 vs E/|k| ≈ 1.0 from §15) because A's packet residual carries an extra non-envelope term; its band-top 1.91 (est.) is not reliable. **A's exact bulk edge is E_max·a = 1.55 (above).**
**Reading.** (1) *c is the top of the group-velocity saturation:* v_g is maximal at k → 0 (= the speed in the continuum limit, 1) and falls monotonically to 0 at the band top; within the ±10% estimator, no mode is faster (B max 1.22 est. vs cubic control reading 1.14–1.16 for a true 1).
(2) *The band top is a rest-mass scale:* v_g = 0 at E_top, and the band-top effective mass obeys m* ≈ E_top (cubic exactly 1; quasicrystal ≈ 1.06 ± 0.1): the lattice's heaviest mode has m*c² ≈ E_max and Compton wavelength ħ/(m*c) = a/(E_top·a) ≈ a/1.2…a/1.5, i.e. **≈ one lattice spacing**.
This is the Compton–Bekenstein statement at the cap: at R = ƛ_C the bound is 2π nats = one registration, here one per cell. (3) The cap in units of ħc/a is lattice-dependent (cubic 1.0; quasicrystal 1.2–1.55; refined S³ 1.90 → 1.57 → 1.48 and still falling), so its refinement limit is not established.
**Consequence for scale (a hypothesis, not a result):** if the cap E_max is the Planck energy E_P = √(ħc⁵/G), then a = (E_max·a)·ħc/E_P = (E_max·a)·ℓ_P ≈ 1.5 ℓ_P. The Bekenstein–Hawking handle (one nat per cell of area a²) gives a = 2 ℓ_P up to the O(1) cell-area geometry: the two handles agree to ~25% before geometry is fixed.
Observation bounds (not calibrations): the highest-energy cosmic rays (~3×10²⁰ eV) require E_max ≥ that, so a ≲ 1.5 ħc/(3×10²⁰ eV) ≈ 9×10⁻²⁸ m. **Not done:** the refinement limit of E_max·a on S³ (n ≥ 4); a bulk (surface-free) band edge for B; an unbiased |d|(k) (periodic approximant); whether the cap is Planck's — this is where G enters and nothing here derives it.
sha256: route56_band.py and route56_band.out as printed by `sha256sum explore/route56_band*`. Command: `py -3 -I -u route56_band.py > route56_band.out` (~3 min).

## 18. The cap examined: refinement limit, closed form, bulk band, unbiased dispersion (`route56_band2.py`, `route56_fcc.py`, `route56_approx.py`; raw `.out`)  [cold]
Follow-up to §17's four open items. All exact spectra or exact Bloch matrices; no fit.
**(a) Refined S³ to n = 5** (sparse build, Lanczos with full reorthogonalisation; validated against dense `eigvalsh` at n = 2, 3 to 6 digits). max|λ|·a, a = mean edge angle:
| n | N | a | A/κ (E_min, E_max) | max|λ|·a (A) | max|λ|·a (B) | (E_max−E_min)/2·a (A) |
|---|---|---|---|---|---|---|
| 2 | 840 | 0.32288 | −4.8476, +3.7093 | 1.5652 | 1.5617 | 1.3814 |
| 3 | 2760 | 0.21664 | −6.8465, +5.6070 | 1.4832 | 1.4718 | 1.3490 |
| 4 | 6480 | 0.16286 | −8.8350, +7.7119 | 1.4389 | 1.4412 | 1.3475 |
| 5 | 12600 | 0.13043 | −10.8986, +9.7844 | 1.4215 | 1.4216 | 1.3489 |
The spectrum is not symmetric (continuum levels d−1 and −(d+1)); the negative edge carries the cap. max|λ|·a falls toward 1.4142 from above (excess over √2: A .1510, .0690, .0247, .0073; B .1475, .0576, .0270, .0074); n = 5 is 0.5% above. The half-bandwidth·a sits at 1.349 ± 0.002 for n ≥ 3 and is the less clean measure (the −1 shift of the positive branch).
**(b) Closed form (`route56_fcc.py`).** The refined lattice is locally FCC (A3, kissing-12). There Σ n nᵀ = 4I, the LS weights are n/(4a), κ = 4a, and A/κ = B on the Hermitised operator: E(k) = |Σ_j n_j sin(k·d_j)|/(4a). Max over k: **E_max·a = √2 = 1.414213562373** (to 12 digits),
at k a = π/√2 along (100) (the sine argument k·d = π/2 per hop); (110) 1.299038, (111) 1.224745. Small k: E/|k| = 1 − O(1e−9). Along (100): E = √2 sin(ka/√2)/a = sin(kℓ)/ℓ with ℓ = a/√2, so **E_max = 1/ℓ exactly.** The S³ sequence (a) approaches this value; that it reaches it is not proved (n ≤ 5).
**(c) Bulk band of the quasicrystal, exact (periodic approximants, φ → τ = 3/2, 5/3, 8/5; kernel lattices saturated, 136 / 576 / 1220 points per cell; mean degree 11.9 / 13.2 / 13.2).** Top eigenvalue over 40 random K (|K| < 4.5; a lower bound on the max): operator B **E_max·a = 1.468 / 1.404 / 1.403** (surface-free, so this removes §17's caveat); operator A (unit weights) 1.562 / 1.465 / 1.499 (not converged between approximants). 5/3 and 8/5 B agree to 0.1%, and sit at √2 within the sampling (1.403 vs 1.414).
**(d) Unbiased dispersion** (exact plane wave u₊(K) in the position gauge, mean E = ⟨ψ|H(K)|ψ⟩; the spread √(⟨H²⟩−⟨H⟩²) ≈ 0.33 is local disorder, not an error bar on the mean). B, τ = 5/3, mean of four directions agreeing to <0.5%: E(K) = 0.2986, 0.5889, 0.9490, 1.332, 1.616, 1.82 at K = 0.3, 0.6, 1.0, 1.5, 2.0, 3.0 (E/K = 0.995 at 0.3). §17's packet estimator read 0.90 and 1.55 at K = 1, 2: low by ~5%, a smaller bias than the cubic-control value I applied (10%).
**Not done / not shown:** the S³ limit at n ≥ 6; the K-maximum of the approximant is sampled, not optimised; A on the approximants disagrees across τ (A is not the consistent operator on an irregular graph); the 28-core and non-smooth sector are untouched.
**The 2π question.** §17 wrote "Compton wavelength ≈ one lattice spacing". Corrected: with ħ = c = 1, ƛ = 1/m* is the *reduced* Compton wavelength, and m* ≈ E_max gives ƛ = 1/E_max = ℓ = a/√2 (FCC), by the sine form alone: E = sin(kℓ)/ℓ has E_max ℓ = 1 for any nearest-neighbour first-difference operator, so that part is not evidence of 2π. The full λ_C = 2πℓ ≈ 4.44a is one sine wave (phase 2π); it is itself a lattice wave (kℓ = 1, E = 0.84 E_max), and the band-top wave has wavelength 4ℓ (a quarter wave per hop). The 2π of the Bekenstein bound S ≤ 2π E R/ħc at R = ƛ is imported with that bound; the lattice supplies E_max ℓ = 1 and the bound turns it into exactly 2π nats. This is the Compton–Bekenstein identity the earlier runs used, now with the lattice supplying the E_max·ℓ = 1; the link between the 2π of the bound and the 2π of the 4π double cover is not derived here.
sha256: route56_band2.py a7b00814022d1c6611a21c0e7b9dde5ab60f52e2a9a38b083c8118a950a91aea; route56_band2.out 25c8d9c0c4a526fc90b6346f9ac7c8b809847bd7559a7768b9af201b88a787a9; route56_approx.py e841d7c26ad120d75c6a00b8e22e2c22ce03e948e92c8fd2d80be760ebdeb329; route56_approx.out aad90b8288a4bba5a36a8be4f4b291505ebf5e7a534addd57e0cdd3ef8b8549d; route56_fcc.py 34f9a4a921a9fe7a554aba101b2a4aec04a3f7b47c9a16164b4e3b3343e21abf; route56_fcc.out fad995ff82501af39abe7cc2c33412199fcc18c127e3e106bd81e5aa756b2937.
Commands: `py -3 -I -u route56_band2.py 2 3 4 5 > route56_band2.out` (~10 min); `py -3 -I -u route56_approx.py 3/2 5/3 8/5 > route56_approx.out`; `py -3 -I -u route56_fcc.py > route56_fcc.out`. (route56_approx.out was re-encoded cp1252 to UTF-8 after the run, content unchanged; hash is of the UTF-8 file.)

## 19. Cap limit, optimised approximants, FCC species, the 28-core by irrep, spin-lift holonomy (`route56_band2.py` n=6,7; `route56_approx2/3.py`; `route56_fcc_nodes.py`, `route56_fcc_dos.py`; `route56_core.py`; `route56_holonomy.py`)  [cold]
**CORRECTION to §18(a)/(b).** §18 said the S³ max|λ|·a "approaches √2 from above". n = 6, 7 falsify the last step. Raw (`route56_band2_n67.out`): n=6 (N=21720, a=0.10876) A/κ: E = −12.9859 … +11.8909, max|λ|·a = **1.41232**; B 1.41680. n=7 (N=34440, a=0.09325) A/κ: −15.0890 … +13.9792, **1.40712**; B **1.41077**.
Full A sequence n=2..7: 1.5652, 1.4832, 1.4389, 1.4215, 1.4123, 1.4071: it crosses √2 = 1.41421 between n=5 and 6 and keeps falling. The half-bandwidth·a ((E_max − E_min)/2·a) runs 1.3814, 1.3490, 1.3475, 1.3489, 1.3528, 1.3553 (n=2..7) and is rising, so the two measures close on one limit
(their gap is a·|(E_max+E_min)/2| ≈ 0.55·a → 0). Linear extrapolation in a of the half-bandwidth gives ≈ 1.37 (n=5..7 slopes −0.16…−0.18); this is an estimate from three points. **The refined 600-cell does not reach the homogeneous FCC value √2; its limit is ~3% lower and unexplained** (candidates, untested: the 5-cell disclination edges and the 12-valent icosahedral vertices of the 600-cell are not FCC).

**Optimised approximant band tops** (random starts then pattern search on K, five refined maxima agree to 4 digits; dense `eigvalsh` for 3/2 and 5/3 in `route56_approx2.out`, Lanczos in `route56_approx3.out` for all three, checked against `eigvalsh`: 5/3 B differs 3e−6, 8/5 B 7e−5):

| τ | N/cell | a | B E_max·a | at K | A E_max·a |
|---|---|---|---|---|---|
| 3/2 | 136 | 0.6981 | 1.46959 | (1.23, −1.11, −0.75) | 1.56385 |
| 5/3 | 576 | 0.7067 | 1.40446 | (0.48, 0.12, −3.58) | 1.46393 |
| 8/5 | 1220 | 0.7070 | 1.40364 | (1.97, 0.01, 1.96) | 1.49931 |

B converges between the last two approximants (1.4045 → 1.4036) to **≈ 1.404, 0.7% below √2**; the §18 sampled values were 0.0003–0.001 low. A does not converge across τ (1.564, 1.464, 1.499): it is the unit-weight rule, and its band top moves with the degree distribution (mean degree 11.9, 13.2, 13.2; max 16, 18, 19).

**What "no surface" meant.** A finite ball of N points has a boundary where the lattice stops; operators on it have boundary-localised eigenstates (§17: B's top six eigenvectors had 0.00–0.01 weight in the interior). A periodic approximant has its boundary glued to itself (a 3-torus), so every state is a Bloch wave, there is no boundary, and the top eigenvalue is the bulk band edge.

**Species (doublers) of the FCC operator** (`route56_fcc_nodes.py`; the first two scripts I wrote for this had scaling errors and were overwritten; the file is the third). E(k) = |F(k)|, F = Σ n sin(k·d)/(4a). Zeros of F: **Γ (chirality +, isotropic velocity c)**, **four L-type points (chirality −, velocity-matrix singular values (1, ½, ½)·c: c along the (111) axis and c/2 across)**, and **nodal lines** (velocity matrix rank 1, through the X-type points κ = (±2,0,0)…).
Raw: 297 distinct roots found, 9 isolated (Γ and the 8 points (±1,±1,±1), which pair to 4 modulo (2,2,2)), 288 on nodal sets. The sum of isolated chiralities, counting the 4 L points, is 1 − 4 = −3, not 0; the compensation is on the nodal lines (not checked).
Low-mode count (`route56_fcc_dos.py`, 4e6 Monte Carlo k-points): expected #|λ|<1 = 2N·P(|F|<a) = **171, 279, 545** at n=2, 3, 5 (of which ≈ 1 near Γ), against measured **382 (A), 364 (B) at n=2 and 704 (A), 734 (B) at n=3** (§14). Same order, trend ∝ 1/a, a factor 2.2–2.5 low; the rest is defect/mesh structure. **The non-smooth low modes are in large part the FCC nodal-line and L-cone states, and their number grows as 1/a with refinement: they do not flow away.** (Not measured at n = 5; the prediction 545 is untested.)

**The 28-core by symmetry** (`route56_core.py`: A commutes with left multiplication T_g (spinor rotated by Q_g) and right multiplication R_g, residuals 1e−9; 9 irreps of 2I with orthonormal characters asserted; 4g = 2⊗2′).
n=1 (N=120): kernel 28; **R-content 1×2, 2′×4, 3′×6; L-content 2×1, 6×3, 4g×2** (the {1,2′,3′} selection with 1→2, 2′→4, 3′→6). n=2 (N=840): kernel 30 = the same Galois core (R: 1×4, 2′×4, 3′×6; L: 2×2, 6×3, 4g×2) plus two extra R-singlet modes. n=3 (N=2760): kernel **4**, R-content 1×4 only, L-content 2×2: **the Galois-conjugate part of the core (2′ and 3′, 26 modes) is no longer zero; the 2 smooth constant-spinor modes persist (plus 2 extra singlet modes).**
Where it went: modes 0 < |λ| < 0.02 at n=3 (22) have R-content 4s×4, 6×1 (not the primed irreps); the primed R-irreps appear in 0 < |λ| < 0.5 (2′×5, 3′×14, 4g×6 of dim 308) and 0.5–1. So the core is exactly zero on the 120-point set and at n=2, and is lifted by n=3; it is not found just above zero.
Window 0 < |λ| < 0.5 at n=2 (172 modes) has R-content only in the chain (2,3,4s,5,6): no Galois irreps. At n=3 the same window has both.

**2π and the 4π cover** (`route56_holonomy.py`): along the decagon g^k (g at 36° from 1) the transport per hop Q_g is a 72° rotation; the spin lift after 5 hops (arc 180°, rotation 360° = 2π) is **−I**, after 10 hops (arc 360°, rotation 720° = 4π) **+I** (raw tr/2 per k=1..10: +0.809, +0.309, −0.309, −0.809, −1.000, −0.809, −0.309, +0.309, +0.809, +1.000). This is floor container 45 (2π ↦ −I, 4π ↦ +I) seen on the carrier; it holds for any element of order 10.
What it does not show: that the Bekenstein-bound 2π is that rotation. The lattice gives E_max·ℓ = 1 (§18), and a stationary state advances its phase by 2π per Compton cycle with spinor sign +1 (e^{−iEt} carries no sign), so −I appears only for a spatial 2π rotation, not for one Compton cycle in time. The standard-physics route to the identification is the Unruh/Rindler one:
the 2π in S ≤ 2πER/ħc is the Euclidean angle around a horizon, and a spinor taken once round that angle returns −1, which is the antiperiodicity of a fermionic thermal state. I have not derived or checked that here; it is the comparison-surface statement of the claim, and it would make the Bekenstein 2π the first half of the 4π. A lattice-internal version needs a defined horizon/boost on the carrier.

**Still open:** S³ at n ≥ 8 and the cause of the ~3% deficit from FCC; a certificate (not a search) for the approximant maximum; nodal-line charge compensation; why n=3 lifts the core; the 28-core on a refinement that preserves 2I_L × 2I_R and the φ³ ladder.

sha256: route56_band2_n67.out 43c5f5e4076c849cc9eabcf834e7571502e0632c107f5b5360e89cc982a409e0; route56_approx2.py ed790333acf84c889ea7d6c62b72beaea440a2ee0b069af20c6b325cda6733b4; route56_approx2.out 46ddf5572ee1efee350a14719a1d17a81090faa8bf3c85f4cf9dcefeb7cfa42f; route56_approx3.py b3f25f7ad633e808c8852cc7f841e5692f3147ba0f98adf3a6c85d36fcb9abda; route56_approx3.out 990fd131d493f93047d02f7a1e32e72f01ff2c5b08735bb2fbafcc2e20f5bdbc;
route56_core.py 092037d853cae620743f3a2835e53df73d6bee831d7aadb92ff99906b4e41fbb; route56_core.out (n=1,2) 1cc0f4b5a9100e09ff650f66e55bf68a909e87bd3034c22bafb8972cd5f28be4; route56_core_n3b.out 888dd61d3a80b21bd753d022f4fa329a5b51ba7881f9a259aec111a537f915ae (route56_core_n3.out is the first n=3 run, before two small windows were added); route56_holonomy.py 8212b039debc264a7a43e4ceaf00b0221cf8181664c8da038ec1bbad855b4cdd; route56_holonomy.out 9b017c8f2ea28a9e9688a1ad58df124bd0abd19bd8403e4183f530b6780fc142;
route56_fcc_nodes.py ad2978eaf448442b513a89c8598b13ad05a968f97a65b508b04e6842a51960b1; route56_fcc_nodes.out 02c4bb3c2af1bb6bf33e68f17502c23ac715d5fdeecdada3981aa9c862600462; route56_fcc_dos.py cfebfd25210c17c69dc4faaa9ebf7a2bdc20a154e079534ebbd10c2fdaa7250b; route56_fcc_dos.out aecde115a63bf0719bcc1420aba378d684da9c972720b91c0e76d93ae0cbfbd0.
Commands: `py -3 -I -u route56_band2.py 6 7 > route56_band2_n67.out`; `py -3 -I -u route56_approx2.py 3/2 24` and `5/3 24` (dense, 30+ min each); `py -3 -I -u route56_approx3.py {3/2,5/3,8/5} 24 > route56_approx3.out`; `py -3 -I -u route56_core.py 1 2 > route56_core.out`, `... 3 > route56_core_n3b.out`; `route56_holonomy.py`; `route56_fcc_nodes.py`; `route56_fcc_dos.py`.

## 20. S³ to n = 10, grid check of the approximant maximum, nodal-line charge balance, where the 28-core goes (`route56_band2.py` n=8–10; `route56_cert.py`; `route56_fcc_charge.py`; `route56_core_embed.py`, `route56_core_levels.py`)  [cold]
**Wording corrections to §19, per the human's notes.** (1) "Every state is a wave that wraps around" on a periodic cell is kept as the plain statement: the cell is a torus and all states are Bloch waves. (2) §19 called the additional low-lying states "extra"/"doubler"; that was a reading, not a result. What is established: the operator has more low-|λ| states than the single Weyl cone predicts, their count tracks the FCC zero set (Γ cone, four L cones, nodal lines) at the right order, and they do not thin out as n grows. Whether they are artifacts, or part of what the structure actually contains, is **not understood** and I do not claim either.

**S³, n = 8, 9, 10** (raw `route56_band2_n8910.out`; Lanczos, 300 steps, full reorthogonalisation; at these sizes the extreme Ritz values are lower bounds that may still be 1e−3 low, validated only to n=3 against dense):
| n | N | a | A/κ: E_min, E_max | max|λ|·a (A) | max|λ|·a (B) |
|---|---|---|---|---|---|
| 8 | 51360 | 0.08162 | −17.1758, +16.0820 | 1.40185 | 1.40739 |
| 9 | 73080 | 0.07256 | −19.2814, +18.2151 | 1.39907 | 1.40465 |
| 10 | 100200 | 0.06531 | −21.4078, +20.3454 | 1.39820 | 1.40386 |
Half-bandwidth·a (A): 1.3572, 1.3604, 1.3635 (rising; the gap to max|λ|·a is a·|(E_max+E_min)/2| = 0.0348 at n=10). **max|λ|·a (B) at n = 10, 1.4039, equals the approximants' bulk value for B, 1.4036–1.4045 (§19), to 0.1%; A is 0.006 lower at n = 10.** Both sit ≈ 1% below √2 = 1.4142. I read the S³ limit as 1.40 ± 0.01; the step-to-step differences (−.0053, −.0028, −.0009 for A) are not regular enough to extrapolate further, and the missing 1% from the homogeneous FCC value is unexplained.

**Grid-and-curvature check of the approximant maximum, operator B** (`route56_cert.py`). Lambda(K) = top eigenvalue on an n³ grid over the Brillouin zone (sparse matvec + Lanczos 80, checked against dense: 3/2 exact, 5/3 1.3e−6, 8/5 5e−4); every zone point is within r of a grid point; with M the bound on ∂²H (row/column sums of ‖blk‖|d|²), Lambda* ≤ Lambda_grid + ½Mr², **under the assumption that the maximiser is stationary for an active branch**; it is not a floating-point-proof certificate.
| τ | grid | max Λ | M | r | margin ½Mr² | E_max·a ∈ |
|---|---|---|---|---|---|---|
| 3/2 | 24³ | 2.105182 | 2.630 | 0.0723 | 0.00687 | [1.46956, 1.47436] |
| 5/3 | 24³ | 1.987181 | 2.547 | 0.0445 | 0.00252 | [1.40444, 1.40622] |
| 8/5 | 18³ | 1.985245 | 2.615 | 0.0423 | 0.00234 | [1.40362, 1.40528] |
The pattern-search values (1.46959, 1.40446, 1.40364) are inside these intervals. For 5/3 and 8/5 the upper end is below √2 (8/5 would need +5e−4·a added for the Lanczos error; still below). The B maximum on the quasicrystal approximants is **1.404–1.405, not √2.**

**Charge balance of the FCC nodal set** (`route56_fcc_charge.py`; Poincaré–Hopf on the 3-torus: the indices of the isolated zeros of a generic vector field sum to χ(T³) = 0). Unperturbed: 5 isolated nondegenerate zeros (Γ +1, four L −1), total −3; the three X-type points are degenerate (rank-1 velocity matrix).
A first perturbation, ε·u·sin(k·e) along one lattice axis, gave 11 zeros with total **−1**: it left the X points degenerate and was an insufficient test (recorded, superseded). With a generic periodic perturbation ε Σ_i u_i sin(k·e_i) over the three cubic axes (e_i = √2 × axis) the zero set resolves to **26 isolated Weyl points, 13 of chirality + and 13 of −, total 0** (ε = 0.01 and 0.03; at ε = 0.1 a pair has annihilated: 12 + / 12 −, total 0). The Γ cone (+1) and four L cones (−1) are unchanged; the X points are replaced by clusters carrying the compensating **net +3**.
So the nodal set carries total index +3 and the charge balances; the three X points keep det M ≈ 0 to 1e−3 at ε = 0.03 (they are near-degenerate, not generic points).

**The 28-core, where it goes** (`route56_core_embed.py`, `route56_core_levels.py`). All geodesic refinements here are 2I_L × 2I_R invariant (commutator residual 1e−9 at n = 1, 2, 3, §19); the core nevertheless dies at n = 3, so **symmetry of the point set does not protect it.**
(a) The n = 1 kernel does **not** embed: zero-padding its 28 vectors onto the refined set gives ‖D v‖/‖v‖ = 3.48–3.82 at n = 2 and exactly √12 = 3.4641 at n = 3 (each of a vertex's 12 new neighbours receives the vertex value); overlap of the padded vectors with the n=2 kernel 0.54–0.59, with the n=3 kernel 0.08–0.17.
(b) The n = 2 kernel (30) has the same irreps as n = 1 (right: 1, 2′, 3′) but different states: weight on the 120 original vertices 0.324 (uniform 0.143). Its survival is by the structure of the isotypic blocks, not by being the same vectors.
(c) Lowest clusters with (left, right) irreps (raw `route56_core_levels.out`, |λ|/κ units where the smooth levels are integers): n=1: 0 (×28; R 1×2, 2′×4, 3′×6), 0.289 (×24; L 6×4, R 4g×6), 0.578 (×18; R 6×3), 0.867 (×8; R 4g×2) …; n=2: 0 (×30), 0.101 (×24, R 6×4), 0.154 (×12, R 3×4), 0.238 (×10, R 5×2) …;
n=3: 0 (×4, R 1×4), 0.0071 (×16, L 4g×4, R 4s×4), 0.0115 (×6, L 1×6, R 6), 0.0686 (×24, R 4g×6), 0.0716 (×30, R 5×6), 0.136 (×18, L 6×3, **R 3′×6**), 0.181 (×18, R 3×6), 0.306 (×18, **R 3′×6**), … The Galois R-block 3′ that was exactly zero at n=1, 2 sits at **0.136 and 0.306** at n=3: lifted by 14% and 31% of the first smooth level (1), not by a small amount.
**Not done: a refinement that keeps the full 2I_L × 2I_R symmetry together with the φ³ ladder.** What blocks it: (i) the norm-1 icosians are only the 120 (the algebra is definite at both infinite places), so there is no larger unit group on S³ to build refined vertices from; (ii) multiplying by φ³ scales a quaternion and leaves its direction on S³ unchanged, so the φ³ ladder lives in the 4D/8D icosian lattice, not on S³; (iii) every new point on S³ is a normalised quaternion q/|q| with |q|² ∉ ℤ[φ] in general, so the Galois conjugation σ is not defined on it, and the core is a Galois-covariant object. A test needs the operator built on the 4D icosian quasicrystal itself (pair-sum sets, §16) with a regular symmetric edge rule, and a definition of what plays the role of Q_j Q_iᵀ there. I have not built that.
sha256: route56_band2_n8910.out 6462934d543e83bf6cfe200c50cbfb8cb29dd1b24ef6c2287236ba97584ca7b5; route56_fcc_charge.py 35e5826a174f9a3a1aa7395c69e534d6a8d9e26a92290c94bb0aa72768b0cd02; route56_fcc_charge.out 49d10fae83c0eee8d079f6ba855d6ced82d41049f409bcd18f2e77e8206c22ca; route56_cert.py d3bea02da88a53370cdd98dd8a3ef75029484bc3527b93b7e50a3bbd7c4429fd; route56_cert_32.out 89d95bcdbade50f7e4bb27dea05f67aae047c9209faf83b230beda9979166c15; route56_cert_53.out 1df3341abec8fc6a9ea18c208b57e099338db9fc20d4a9d4c3393e1de7975bec; route56_cert_85.out 9dd381141ee713e4d7e622ed8821b98762b7d3db57ce3b8e4937dbc25e5cc58c;
route56_core_embed.py 8253b5e86c424c6763df62b289cf0b51c0395ef71870a53320ac32392b1d8909; route56_core_embed.out 5df126c224dff8fad8f526b0effffa9cd6dbf23645f7975ebd1648b0d628e5e8; route56_core_levels.py 31e75f7a0bd08ddebd2a0693cbdf8f02f23280420464ce7baaf8607acbf3f752; route56_core_levels.out 454993139fb9dff0eeaa27d988e81ee6ba7dd830d9c82a408aa265cdfdabcb5b.
Commands: `py -3 -I -u route56_band2.py 8 9 10 > route56_band2_n8910.out` (~35 min); `py -3 -I -u route56_cert.py {3/2 24, 5/3 24, 8/5 18}`; `py -3 -I -u route56_fcc_charge.py`; `py -3 -I -u route56_core_embed.py`; `py -3 -I -u route56_core_levels.py 1 2 3`.
