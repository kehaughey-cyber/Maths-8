# Map — the openings as a critical path, with bottom-up and top-down routes (2026-11-02)

Authored by Claude (Sonnet 5.5) from a read of the repo with the human; no independent review claimed. The dependency order is a judgement from the files, open to correction. Nothing here was computed; it is a plan of the map, not a result.

## Purpose this serves (the human's words, 2026-11-02)
"Handles" means **tunable levers on mass, space and time** (and through them the forces), not mainly exact derived values such as masses or α. Understanding comes first, then the applicable understanding, so that people with interest and means can apply it in their own area (the human's example: plastic "magnets" for the Pacific garbage patch). Specific engineering (which material, how many teslas) is not the current work. The current work is completing the map: a common language in which any quantity is written in terms of another and the relation is known.

Scale is central: lower orders do not stop while higher orders are observed. All orders are live at once, each with its own tick.

## What is in hand
Carrier 2I and the 600-cell; tick C and native continuation T (C and T commute; T¹⁰ = id, C¹⁵ = −I); relaxation φ/2 per tick and reinjection gain 1/(1−(φ/2)³⁰) (D4, D5); density deficit ↔ curvature ↔ charge; gradings ↔ forces; Born invariant form; the E-series charged-history actions at one scale; the size–energy ladder with 1 cycle = 12 radits = 30 ticks = 2π (`maps/full_ladder.md`, `maps/degrees_of_freedom.md`); the lab (`lab/`).

## Critical path
```
P1 scale: how orders couple, all live at once
 └─ P2 clocks joined (radit · walk · propagation)
     └─ P3 energy (which clock, or the clock-invariant)
         ├─ P4 mass / inertia
         └─ P5 field law + units (EM)
              └─ P6 persistent particle / collective
```
Scale is the root: if every order has its own tick, "time", "rate" and "energy" are undefined until the coupling between orders is known.

## Each opening
| opening | needs | bottom-up (from the act) | top-down (from the observed) |
|---|---|---|---|
| **P1 scale** | the law for crossing between orders. Only inter-order mechanism derived so far: reinjection (D5). The φ step per copy and the radial-hop cost are declared in the lab, not derived. | Registration is recursive by construction (floor 01), so nesting is built in; the question is what ratio the recursion forces. ℤ[φ] has φ as a unit, so golden inflation is a candidate (not derived). Compute the inner-copy structure. | Causality bounds the radial-hop cost from below: if a hop cost the starting copy's tick, Planck-to-atom would be ~10²² faster than light (lab, Amplitude tab), so the cost is at least the larger copy's tick. The rungs show no common offset in the φ tower (`maps/lattice_physical_map.md`), consistent with orders being a continuum and rungs being readings of it. |
| **P2 clocks** | the relation of 12 radits, the 10-cycle of T and the 30-cycle of C. | Mostly exact finite computation: C and T commute (M6 D3). Field equations F3 call the order-30 beat the cross-scale one, so the walk clock may be the inter-order clock and propagation the intra-order one. To be checked. | 1 cycle = 12 radits = 30 ticks = 2π (ladder maps). |
| **P3 energy** | a named clock for each rate. `registration_rate.py` measured the propagation clock only. | Repeat for the walk and radit clocks and compare. | At R = Compton length, R·E/ħc = 1 cycle with mass cancelling (Compton–Bekenstein 2π): energy as registration rate. |
| **P4 mass** | reconcile three readings: Galois mass {12,4,4,0}, propagation rate (inertia), Compton. M6 C2 says these are not identified. | Compute the vertex-wave frequency and √\|λσ(λ)\| per irrep and look for a relation. | The measured ladder (neutrino to top); the lepton Koide structure is the one working contact (A = √2 asserted; quarks miss, `maps/alpha_mechanism_status.md` Update 3). |
| **P5 fields** | open-space flux across orders, the coupling, calibrated units (M6 F2, F3). | Extend the E-series joint action to nested copies, with flux through the boundary between copies as "open space". | Known relations such as μ = g(q/2m)S as translation targets. |
| **P6 collective** | P4 and P5, plus admissibility (M6 F4). | Find which structure gives one persistent pattern. | Atoms and shell closure as the target. |

## Readings of the table
- **Magnetism as a test of the path** (not as the work): μ = g(q/2m)S needs charge (signed defect, k = 3Q), mass (P4) and spin (spinor, 4π). Charge and spin have floor entries; mass is the missing one, so the route to magnetism runs through P4 and, behind it, P1–P3.
- **Where the directions meet:** both ends are anchored externally, Planck at the bottom and c/H₀ at the top (k = 291.54, see `maps/hubble_radius_correction.md`). A calibration at one rung, tested against the others, is the allowed route.
- **P1 is the lever on time:** the radial-hop cost is the one parameter the lab declares rather than derives; it sets how fast a disturbance crosses orders.

## Suggested start
P1 and P2 together. P2 is mostly exact finite computation, so quickest; it would say whether the walk clock is the inter-order clock, which would fix P1.
