# Map — positronium, the first atom translated (2026-10-28)

Translation, not derivation. Greek = BC cycles (cycles = R·E/ħc; 1 cycle = 12 radits = 30 ticks = 2π nats = 9.0647 bits). Hieroglyph = the floor's vocabulary (`floor/`, `maps/degrees_of_freedom.md`). Scale = position on the ladders in `maps/mass_requirements.md` terms (length Planck → Hubble radius 60.93 decades / 56.46 powers of 12; time the same; mass 0.05 eV neutrino → Hubble-sphere mass 90.0 / 83.4; information 1 cycle → Hubble sphere 3.6056e121 cycles, 121.56 / 112.64).
Run: `py -3 -I -u explore/positronium_map.py > explore/positronium_map.out`. Raw values: `explore/positronium_map.out`.
Sourced inputs: CODATA 2018 constants; p-Ps formula t₀ = 2ħ/(mₑc²α⁵) and o-Ps 142.05 ± 0.02 ns, 7.040 μs⁻¹ (Wikipedia "Positronium", citing Karshenboim 2003, Badertscher 2007, Adkins 2000). The 0.05 eV neutrino is rough. Hyperfine (7/12)α⁴mₑc² and a_Ps = 2ƛ_e/α are my leading-order derivations; the page gives only "≈0.001 eV".

## The table
| Row | Greek (cycles) | Scale position | Hieroglyph (floor) | Grade |
|---|---|---|---|---|
| e⁻, e⁺ at own cut | 1 each (12 radits, 30 ticks) | ƛ_e 22.378 dec / 20.736 p12 above l_P; m_e 7.009 dec / 6.495 p12 above 0.05 eV | a defect d and its C-mirror 12−d; signed defects 2 + (−2) = 0 | arithmetic exact; electron↔d is a reading (nodes 29, 49) |
| Pair at its extent | rest 4/α = 548.14399633 cycles | a_Ps 24.816 dec / 22.995 p12 (ƛ_Ps 22.077, r_e 20.241) | coordinate 2, the outer end of the ladder; r_e = αƛ_e is the inner end | exact algebra |
| Binding | α/2 = 0.00364867628 (0.10946 ticks) | – | coordinate 3, the pair's bound; same as hydrogen | exact |
| 1S–2S | 3α/8 = 0.00273651 | – | levels n, 4n² states with spin | exact (leading) |
| Hyperfine | 7α³/6 = 4.5336e-7 | – | two registered bits = 4 states = 1 ⊕ 3; the 12-shell is 1⊕3⊕3′⊕5 (dims 1+3+3+5 = 12) | dims exact; Ps spin ↔ 2I irreps is a reading |
| Para decay | rate α⁵/2 of ω_e; τ = 0.12449 ns | time 33.364 dec / 30.916 p12 | Γ = c·4π r_e²·\|ψ(0)\|² = inner-sphere area × outer density, equal to α⁵ω_e/2 to every printed digit (8.0325e9 s⁻¹); fold +1 (even photons) | algebra exact; fold reading (nodes 49, 64) |
| Ortho decay | measured 0.060050 α⁶ (leading 0.061512 α⁶); τ = 142.05 ns | time 36.421 dec / 33.749 p12 | fold −1 (odd photons, 3) | reading |
| Persistence | p-Ps 9.665e10, o-Ps 1.1028e14 electron-Compton cycles | – | registrations survived before re-co-defining into propagation | reading |
| Annihilation photon | 1 cycle each; 2γ = 2 cycles in, 2 out; 3γ shares 2 | – | standing registrations → propagation quanta, count conserved | reading |
| Gravity pair | (m_e/m_P)² = 1.7518e-45 | log12 = −41.47 | deficit reading (node 20) | nothing to compare |
| Total information across a_Ps | 548.14 cycles | 2.739 dec of 121.56 (2.3%); 1.52e-119 of the horizon's count | – | – |

Positronium sits 33–41% along the length ladder, 8% along the mass ladder, 55–60% along the time ladder, and 2.3% along the information ladder.

## Common denominator
α only. Every row is α^k × a rational (4, 1/2, 3/8, 7/6, 1/2) with one π in the ortho coefficient. Compare hydrogen: same binding (α/2), rest row (m_H/mₑ)/α instead of 4/α, and the extra mass step m_p/mₑ.

## What does not line up
- α itself (1/α = 137.036). Floor node 29 gives bare coupling 1, node 35 gives α̂ = 1/N only for the cosmological scale; exp(2π)/4 = 133.87 is 2.4% off. Current reading: α is a resolution of the recursion at this extent, not on the floor.
- The ortho coefficient 0.06005 (contains π); the 4, 3/8, 7/6 coefficients (QED leading terms; no floor counterpart found).
- 12-power test: 1/α, 2/α, 4/α have log₁₂ = 1.980, 2.259, 2.538; only the hydrogen-style step is near an integer, and it depends on the reduced-mass factor.
- Registrations per extent: with the floor's flat-ball law 1+3r(r+1) at r = a_Ps/ƛ_Ps = 548.14 the count is 903,030.95, assuming one hop = one Compton length (an assumption, not a floor fact). No comparison available.

sha256: *positronium_map.py 325c71af25ef7163503e7a9bef6768474eed9694a66a638cb44b69329ad7c1be; *positronium_map.out a7d549e0b547dff67aef0b36dae6e19ef99450c738518827f68566cc57bee0d6.
