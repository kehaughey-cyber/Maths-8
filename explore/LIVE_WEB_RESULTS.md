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
