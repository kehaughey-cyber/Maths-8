# Map — the aspects of one gram of carbon (draft inventory, 2026-11-02)

Authored by Claude (Sonnet 5.5) from the repo's carbon maps and saved sources, plus recall where marked. No independent review. This is the denominator for the whole-object share in `maps/critical_path.md` (second update): the list of aspects that must hold together for the gram to exist. It is a list, not a count; no share has been computed. Open for additions.

## Conditions (the human's, 2026-11-02)
- **The mature state, not the origin.** The change has been running a long time. This is the gram as observed now; nothing here reads the Planck anchor or the bottom of the lab as what it was at the start.
- **Every reference has a margin of error.** Values below carry the repo's recorded uncertainty or scheme; where none is recorded the cell says so. Never compare a bare number.
- **A measurement is not a neutral view** (compare the double slit). Every value here is the result of an act of examining, and the framework's readouts will be too. How we examine it is part of what we see.
- **The aspects are mutually necessary.** Remove any law (gravity, electromagnetism, the strong or weak force) and the gram ceases to exist, so the list is not a checklist of separate items.

Status key: **S** saved source in `explore/data/`; **M** in a repo map from a named source (some secondary, see the named map); **R** recalled, no saved source, to be sourced before use; **–** not in the repo.
Scale columns: *expressed* is where the property is present in the structure, *manifest* is where its effect shows. The two can differ (a property can be present long before its effect appears).

## A. Mass and gravity
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| rest mass: 12 u per atom, N = 5.0184506350676e22 atoms per gram | nucleus → bulk | `carbon_one_gram.md` | S/M, N_A exact, u exact in the 12C definition |
| where the mass sits: nucleons about 99%, bare quark masses about 1%, electrons 0.027%, binding 0.82% | quarks, gluon field → nucleon → atom | `carbon_complete_stack.md` §2 | quark masses ±2% statistical, ±20% with the scale (scheme-dependent) |
| gravitational coupling (m/m_P)² on each rung; the gram 2.111e9 | every rung → bulk | `carbon_complete_stack.md` §1, §4 | depends on G, the least well known anchor; its uncertainty must be carried |
| weight and field of the gram | bulk | – | not tabulated |
| inertial = gravitational mass | all | `mass_requirements.md` | tested to about 1e-15 (MICROSCOPE), per that map |

## B. Strong force and the nucleus
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| nuclear binding B = 92.1617352 MeV, B/A = 7.6801446 MeV | nucleus | `full_ladder.md` | S AME2020 (measured values only; electron binding ignored in nuclear mass) |
| nuclear size, charge radius 2.4702(22) fm | nucleus | `carbon_one_gram.md` | S (IAEA ground-state table saved); matter radius differs by 5.3% |
| nucleon size, r_p = 0.84075(64) fm = 3.9977(30) Compton lengths | nucleon | `colour_column.md` | S CODATA 2022 |
| ground-state spin and parity 0+ | nucleus | `explore/data/iaea_livechart_ground_states.csv` | S, not tabulated in the stack |
| excited levels of 12C | nucleus | `explore/data/iaea_livechart_12C_levels.csv` | S saved, not tabulated |
| strong coupling and confinement scale | nucleon → nucleus | `colour_column.md` | scheme ambiguity (factor 7.5) exceeds the gaps, so those comparisons are undetermined |

## C. Weak force
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| 14C beta decay, 0.226 Bq per gram of natural carbon, half-life 5700(30) y, Q(β−) = 156.4765(37) keV | nucleus → bulk | `carbon_one_gram.md`, `explore/data/carbon_aspect_sourced_values.txt` §1 | S NUBASE2020 and IAEA table (half-life, Q); activity secondary; 0.53% from the 5700 vs 5730 convention |
| neutrinos through the gram (solar, geo, relic) | cosmic → bulk | `carbon_complete_stack.md` §6 | rates from saved reviews; atmospheric not obtained |
| neutrino interaction rate in the gram, about 3e-11 per second | – | `carbon_gram_refinements.md` | order of magnitude only |
| neutrino mass scale (oscillation lower bounds; no absolute mass measured) | – | `full_ladder.md` | S PDG 2024 |
| weak column of the unified table | – | `carbon_complete_stack.md` §4 | "not expressed": a gap |

## D. Electromagnetism, electric side
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| charge content: 6N positive, 6N negative, net zero (12N e = the Faraday constant) | nucleus, electrons → bulk | `carbon_complete_stack.md` §5 | exact counts |
| the six electrons and their ionization energies, sum 1030.1079 eV | atom | `carbon_one_gram.md` | S (NIST ASD CI to CVI saved, PeriodicTableJSON) |
| bonds and molecules: C–C 3.6855 eV (Ec/2), CH4, C2H6, CO2, C6H6, CO | atom → molecule → lattice | `carbon_gram_remaining.md`, `chemical_ladder.md` | CCCBDB geometries are secondary (page text not saved) |
| the lattice: a = 3.56683 Å, density 3512.9591 kg/m³, cohesion 7.3711 eV per atom | lattice → bulk | `carbon_one_gram.md` | secondary quotation for a; graphite quantities also secondary |
| electronic band structure: diamond gap 5.47 eV, resistivity 1e11–1e18 Ω m; graphite a semimetal | lattice → bulk | `carbon_aspect_sourced_values.txt` §4 | W secondary (Wikipedia; resistivity from Fromentin 2004; gap has no reference shown) |
| optical response: refractive index 2.417 at 589.3 nm | lattice → bulk | `carbon_aspect_sourced_values.txt` §4 | W secondary; footnote not clearly attached to the value |

## E. Electromagnetism, magnetic side
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| nuclear spin zero for 12C: no nuclear magnetic moment | nucleus | IAEA table (above) | S |
| ground term 3P, J = 0 for the free atom (2s2 2p2): no net atomic moment in the ground level | atom | `explore/data/nist_asd_CI.txt` | S (level energy uncertainty 1.6e-7 eV) |
| electron magnetic moment μ_e = −9.2847646917(29)e−24 J/T | electron | `carbon_aspect_sourced_values.txt` §2 | W NIST CODATA 2022 |
| collective magnetic response | lattice → bulk | `carbon_aspect_sourced_values.txt` §3 | W review arXiv cond-mat/0207368: graphite c-axis χ = −(22–50)e−6 emu/g (varies tens of percent between samples); in-plane −5e−7 emu/g usually quoted but +2e−6 reported (misalignment can mimic the sign); diamond −4.9e−7 cm³/g from a secondary table, unverified |

Reading of section E: the gram has many magnetic ingredients present (spins, orbital currents, moments) and its manifest magnetism is weak. This is the expressed-versus-manifest difference the human described: having the properties of magnetism is not the same as manifesting its effects.

## F. Quantum statistics and spin
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| fermion exclusion and shell filling, 1s2 2s2 2p2 | electrons → atom → chemistry | NIST ASD CI saved | S (configuration); exclusion itself is not derived by the floor (M6 F4) |
| nuclear pairing in 12C (6 protons, 6 neutrons, spin 0) | nucleons → nucleus | – | – |

## G. Thermal and statistical
| aspect | expressed → manifest | in repo | status and uncertainty |
|---|---|---|---|
| entropy of diamond, S = 2.3782 J/(mol K) at 298.15 K | lattice → bulk | `carbon_one_gram.md` | S NIST WebBook (DeSorbo 1953); graphite-like values are a range |
| heat capacity Cp = 6.1149 J/(mol K); Debye temperature 1861 K (Cp) or 1865 K (S) | phonons → bulk | `carbon_gram_remaining.md` | the two Debye values differ by 0.20%, so they are model-defined |
| phonons: Raman zone-centre mode 1332.7(2) cm-1 | lattice | `carbon_gram_remaining.md` | secondary |
| thermal conduction ≈2200 W/(m K) natural, 3320 for 12C-enriched at room temperature (Anthony 1990); burns above 700 °C in air, graphitises ≈1700 °C in argon; Mohs 10 | lattice → bulk | `carbon_aspect_sourced_values.txt` §4 | W secondary (Wikipedia, with primary references where shown); bulk and Young's moduli and Debye value not obtained |
| information counts: atoms (log2 N = 75.41), thermodynamic bits 2.0709e22, Bekenstein–Compton bits 1.0516e38 (gap 15.7 decades) | all | `carbon_complete_stack.md` §3 | gap depends on phase (diamond versus graphite, radius ×1.157) |

## H. Context of the gram (not modelled; the mature state)
| aspect | in repo | status |
|---|---|---|
| isotopic make-up: 98.94% 12C, 1.06% 13C, trace 14C | IAEA table (S), `carbon_one_gram.md` | S/M |
| cosmic muons through the gram, 0.243 to 0.433 per minute for the 0.4327 cm² face (threshold-dependent, factor 1.78) | `carbon_gram_refinements.md` | secondary |
| origin of the carbon (stellar synthesis) | – | not modelled; the gram is taken as observed |

## What this draft shows
- **Well covered in the repo:** mass budget, nuclear binding and size, charge, atomic and molecular energies, the lattice, entropy and heat, the neutrino and ¹⁴C flows.
- **Updated 2026-11-02:** the rows for weak decay energy, electron moment, susceptibility, electronic, optical, thermal conduction and thermal limits now carry sourced values (secondary where marked).
- **Still gaps:** the weak column of the unified table, elastic moduli, and a primary source for the diamond susceptibility and the diamond table values.
- **Stands out:** every row is a measurement with a scheme or margin attached. Several (strong coupling, quark masses, G) carry uncertainties larger than the gaps one would want to resolve. Those rows can mark where the instrument can say something and where it cannot yet.
