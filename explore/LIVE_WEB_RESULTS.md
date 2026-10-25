# Live web, energy = registration rate, and the effective-mass probe — results

Cold anchors for the mass/energy investigation (2026-10-25). Reproduce each with
`py -3 -I -u explore/<script>`. All build the carrier (120 icosians, 720 edges) from scratch.
See also `maps/mass_requirements.md` and `maps/degrees_of_freedom.md`.

## Scripts
- `registration_rate.py` — energy = registration rate, on the carrier.
- `live_web_push.py` — the live relational web (D-arc joint action) kicked, web engagement.
- `effective_mass.py` — ring-down frequency shift → effective mass & damping vs amplitude and κ.

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
