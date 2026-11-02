# Instrument audit: what the repo already has for the joint object (2026-11-02)

Authored by Claude (Sonnet 5.5). Scope: step 2 of the plan in `maps/critical_path.md`. Read in full: `explore/LIVE_WEB_RESULTS.md` §1–6 and §29–34, the headers of the scripts named below, `lab/spine_lab_src.html`. Seen by heading or header only: §7–28 of that results file and most `route56_*` scripts. The M6 `explore/periodic_table/` E-series code is not in this repo. Nothing was run in this step; every statement about a result is quoted from the repo's own text.

## What the joint object needs
The E-series action (floor M6 E6: matter, field and links in one action) on adjacent nested copies, with:
1. the carrier and the tick/continuation structure (C, T);
2. a link layer with phases (holonomy, not scalars);
3. one action in which matter, links and field all have kinetic terms, giving current, continuity, Gauss and energy transfer;
4. a flux term between adjacent nested copies, copies left open in number;
5. readouts for rate, frequency, persistence, flux, tick per order, metric, each recorded as expressed and manifest;
6. switches to remove one layer at a time (ablation);
7. a raw record (command, unrounded output, sha256, failures included).

## What exists
| piece | where | what it does (from the repo's text) | limits stated there |
|---|---|---|---|
| carrier, T on 1440 histories, random exit K, reinjection, sag | `lab/spine_lab_src.html` (JS); independent Python replay `explore/amplitude_histories_check.py` | first moment of the vertex marginal shrinks by φ/2 per tick; T returns after 10; reinjection gain 1/(1−(φ/2)³⁰); sag; arrival times along the order chain | amplitudes only, real, no link phases |
| propagation clock | `explore/registration_rate.py`, results §1 | measured phase per tick equals arccos(1−(c²/2)μ) to 6 decimals; distinct from the Galois mass {12,4,4,0} | frozen adjacency; one of three clocks |
| live web (co-definition) | `explore/link_laws.py`, `effective_mass.py`, §2–4 | field plus edge weights that move; reactive effective mass up to 1.22 for an adiabatic law, dissipation for a relaxational one; knobs β and Γ | §3: the constitutive link law is a modelling choice, not derived |
| flux as holonomy | `explore/pentagon_flux.py`, §5–6 | a scalar frustration is trivial; threading ε as Peierls phases through the 720 pentagons lifts the uniform zero mode from 0 to 0.011, gap ∝ flux² | abelian U(1) model; the carrier's connection is SU(2); gap is dimensionless |
| native SU(2) connection | `explore/route56_native.py`, `route56_subdiv.py` (`carrier`, `Qmat`, `subdivide`) | Dirac operator D = Aγ, per-face Wilson holonomy, the 28 massless modes {1,2′,3′}⊗spinor | physical-mass bridge open |
| inertia, dynamics | `explore/route56_inertia*.py`, `route56_dynamics.py`, §33–34 | locked-label inertia M = E/v² exactly; no rest-mass band minimum (standing states are saddles); packet sweeps ergodically; node passage is an exact Landau–Zener crossing | no mechanism for relaxation in the Hamiltonian alone; mode-by-mode mass inversion untested (§32) |
| mass fork | `explore/route56_massfork*.py`, §32 | static Galois mass and dynamic rate are the same shell form factor at small momentum (corr +0.923) | does not decide whether either is inertia |
| force-grading tests | `explore/route56_core_joint.py`, `route56_e8_*.py`, §29–31 | 28-core = (2,1)⊕(4g,2′)⊕(6,3′), abelian commutant; fixed subalgebras of cyclic subgroups are large | §31 withdraws the "no route to SU(3)" conclusion of §29–30 |
| scale and anchor | `explore/anchor_investigation.py`, `lattice_physical_map.py`, `hubble_radius_correction.py`, `ratios_128_137.py` | tower of copies, Planck anchor choice tested, rungs placed | anchor and φ step are declared choices |

## What a keyword search did not find
A search of the `.py` files for "link phase", "continuity", "Verlet", "Berry" returned nothing; "Gauss" appears only in three unrelated files, "Peierls" only in `pentagon_flux.py`. This is a search, not a reading, so the E-series pieces could exist under other names. As far as it shows, missing are:
- link phases on the T-history layer;
- a single action with matter, link and field kinetic terms (M6 E6), with current, continuity and Gauss;
- flux between adjacent nested copies (the lab's order chain handles arrival times only);
- any expressed/manifest split in a readout;
- ablation switches.

## Findings that constrain the design (from the repo's own results)
- Scalar frustration is trivial and flux is not (§5–6), so phases enter as holonomy.
- The link response is a modelling choice (§3, §4), so it is a swept parameter and not a fixed law.
- A persistence readout cannot look for a band minimum: there is none (§33). It has to look at organised, standing states.
- Nothing relaxes in the Hamiltonian by itself (§34). In the lab, relaxation comes from the random exit K and from reinjection (D4, D5), the dissipative parts. That correspondence is my reading, not stated in the repo.
- Mass has three readings that do not yet agree (§32, `maps/mass_requirements.md`), so each mass readout carries its protocol.

## Reuse and rebuild
- **Reuse:** the carrier and `Qmat` builders in `route56_subdiv.py`; the connection and holonomy in `route56_native.py`; the T/K replay in `amplitude_histories_check.py`; the Peierls machinery in `pentagon_flux.py`; the verified variational force in `link_laws.py` (gradient checked against finite differences, error 1.2e-8 per §4).
- **Rebuild:** the joint action with Gauss and continuity (M6 E6, code absent here), SU(2) link phases on the T-history layer, and the coupling between adjacent nested copies.

## Not confirmed
`route56_repro.py` and `route56_massgap.py` contain 48/5 or sin(π/5) expressions; I did not confirm they are the frustration-flux energy V_spec = μΣ(1−cos F) with μ = (48/5) sin(π/5) of M6 E3.
