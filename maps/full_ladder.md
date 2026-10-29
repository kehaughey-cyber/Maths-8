# Map — the full mass ladder: neutrino scale to top quark, hadrons, nuclei and binding energies (2026-10-29)

Completes `lepton_ladder.md`. Same dictionary (cycles = R·E/ħc; 1 cycle = 12 radits = 30 ticks = 2π nats). Tabulation only: sourced numbers, ratios between neighbours, logs. No rule proposed, nothing fitted.
Run: `py -3 -I -u explore/full_ladder_map.py > explore/full_ladder_map.out`. Raw output: `explore/full_ladder_map.out`.

## Sources (all persisted in `explore/data/`)
| file | what | source | sha256 |
|---|---|---|---|
| `pdg2024_leptons.txt` | e, μ, τ masses; neutrino limits and oscillation parameters | PDG 2024 summary tables (S. Navas et al., Phys. Rev. D 110, 030001), `rpp2024-sum-leptons.pdf` through pdftotext | de2a057e43f89d7179ed3e3ffaa9d588e6dbb9e717908aa93d19cc5fe277b1fb |
| `pdg2024_quarks.txt` | u d s c b t | PDG 2024 `rpp2024-sum-quarks.pdf` | 1e33287c96b681f657011bcc96da4b88cc025d3d3adbd5b60a13d2a51cb4e447 |
| `pdg2024_gauge_higgs.txt` | W, Z, H | PDG 2024 `rpp2024-sum-gauge-higgs-bosons.pdf` | af85251d38bde0c676e514f51b66a464a25f9055de4eae6ee3907903073b9b27 |
| `ame2020_mass_1.mas20.txt` | atomic masses, binding energy per nucleon, 2550 measured nuclides parsed | AME2020 (Huang et al., Chin. Phys. C 45, 030002), IAEA AMDC `mass_1.mas20.txt`, 472,648 bytes, fetched 2026-10-29 | e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307 |

Also used: DESI+CMB flat ΛCDM Σm_ν < 0.072 eV (95%), arXiv:2404.03002 abstract; CODATA 2018 for ħ, c, G, α, m_e, m_p, m_n, u. The PDF-to-text conversion mangles "±" to "�", and the numbers above were read from the converted text, not from memory.

## Correction to `lepton_ladder.md` (append-only)
That map used the CODATA 2018 τ mass, 3.16754(21)e-27 kg = 1776.86 MeV. PDG 2024 gives 1776.93 ± 0.09 MeV. The τ rows there are 4e-5 relative low (e→τ 3477.2276 there, 3477.3653 here), inside both uncertainties. Its neutrino anchor 0.05 eV is replaced below by a number from the oscillation data.

## The neutrino end (the anchor, now sourced)
Measured: Δm²₂₁ = (7.53 ± 0.18)e-5 eV², Δm²₃₂ = (2.455 ± 0.028)e-3 eV² (normal order). Direct limit m(ν_e) < 0.8 eV (90% CL). Cosmology: Σm_ν < 0.072 eV (95%, ΛCDM, DESI+CMB). No neutrino absolute mass is measured.
Minimum masses if the lightest is zero (lower bounds, not measurements): m₂ ≥ 0.008677557259966655 eV, m₃ ≥ 0.05030208743183527 eV, sum ≥ 0.05897964469180193 eV. The ladder anchor is now m₃_min (the old 0.05 eV is 0.6% below it). Oscillations require Σ ≥ 0.0590 eV and DESI+CMB gives ≤ 0.072 eV, so the allowed window for the sum under that cosmology is narrow.

## Sorted masses and steps (full table: Part A–C of the output)
| particle | mass | ratio to previous | log₁₂ | log_φ | mass source |
|---|---|---|---|---|---|
| ν₂ (min) | 0.008677557 eV | – | – | – | oscillation lower bound |
| ν₃ (min) | 0.0503020874 eV | 5.796802709 | 0.707192 | 3.65184 | oscillation lower bound |
| e | 510998.9499961642 eV | 10158603.27245 | 6.49273 | 33.5275 | CODATA |
| u | 2.16 MeV | 4.227014557 | 0.580101 | 2.99555 | MS-bar 2 GeV |
| d | 4.70 MeV | 2.175925926 | 0.312871 | 1.61562 | MS-bar 2 GeV |
| s | 93.5 MeV | 19.89361702 | 1.20343 | 6.21431 | MS-bar 2 GeV |
| μ | 105.6583755 MeV | 1.130036102 | 0.0491969 | 0.254045 | PDG |
| p | 938.2720881605 MeV | 8.880243367 | 0.878837 | 4.53819 | CODATA |
| n | 939.5654205204 MeV | 1.001378419 | 0.000554335 | 0.0028625 | CODATA |
| c | 1.2730 GeV | 1.354881706 | 0.122224 | 0.631144 | MS-bar m_c(m_c) |
| τ | 1776.93 MeV | 1.395860173 | 0.134215 | 0.693065 | PDG |
| b | 4.183 GeV | 2.354060092 | 0.344537 | 1.77914 | MS-bar m_b(m_b) |
| W | 80.3692 GeV | 19.21329190 | 1.18942 | 6.14200 | PDG |
| Z | 91.1880 GeV | 1.134613758 | 0.0508238 | 0.262446 | PDG |
| H | 125.20 GeV | 1.372987674 | 0.127566 | 0.658731 | PDG |
| t | 172.57 GeV | 1.378354633 | 0.129136 | 0.666838 | direct measurement |

Spans: ν₂_min→t ratio 1.98869330193e13 (log₁₀ 13.2986, log₁₂ 12.3228, log_φ 63.633); e→t ratio 337711.0657 (log₁₂ 5.1229, log_φ 26.454). Fifteen steps over ν₂_min→t, mean ln step 2.0414.

## What the steps show, stated plainly
- The largest single step is ν₃_min→e (10158603, log₁₂ 6.49): the neutrino scale sits about seven decades below the charged leptons, and it is set only by bounds, not measurements.
- Four neighbouring heavy steps are close to each other: n→c 1.3549, c→τ 1.3959, Z→H 1.3730, H→t 1.3784. Their propagated uncertainties are 0.36%, 0.36%, 0.09% and 0.19%, and they differ from one another by more than that, so they are not equal. The charm row is scheme-dependent (MS-bar m_c(m_c)), and that ordering depends on the scheme.
- Phase-residual columns (distance of log_φ and log₁₂ to the nearest integer) are printed for every step. The only residual that looks small is e→u (−0.0044 in log_φ), and the u uncertainty (3.2% on the ratio) makes it 0.067 in log_φ. It carries no information. Part C of the output gives the uncertainty for every step.
- Koide, raw: Q(e,μ,τ) = 0.6666644634 with PDG τ, so Q − 2/3 = −2.20e-6 (the τ relative uncertainty is 5.06e-5; its effect on Q was not propagated). Quark triples are scheme-mixed and listed for completeness only: (c,b,t) 0.66922 (Q − 2/3 = +0.00256), (u,d,s) 0.56675, (d,s,b) 0.73129, (s,c,b) 0.45843, (u,c,t) 0.84879.

## Nuclei and binding energies (Parts E–F)
Largest binding energy per nucleon among the 2550 measured nuclides parsed: ⁶²Ni, 8794.5555 keV (⁵⁶Fe 8790.3563, ⁵⁸Fe 8792.2534). Selected rows (B total from B/A × A; nuclear mass = atomic mass − Z·m_e, electron binding ignored):
| nuclide | B/A keV | B total MeV | B/(M c²) | B/(m_p c²) |
|---|---|---|---|---|
| ²H | 1112.2831 | 2.2245662 | 0.0011860476 | 0.002370918 |
| ³H | 2827.2654 | 8.4817962 | 0.0030195922 | 0.0090398045 |
| ⁴He | 7073.9156 | 28.2956624 | 0.0075913021 | 0.030157204 |
| ¹²C | 7680.1446 | 92.1617352 | 0.0082472361 | 0.098224957 |
| ⁵⁶Fe | 8790.3563 | 492.2599528 | 0.009450222 | 0.52464521 |
| ⁶²Ni | 8794.5555 | 545.262441 | 0.0094546125 | 0.58113467 |
| ²⁰⁸Pb | 7867.453 | 1636.430224 | 0.0084488334 | 1.7440892 |
| ²³⁸U | 7570.1262 | 1801.6900356 | 0.0081268535 | 1.9202213 |

Nuclear Compton lengths run from 2.10e-16 m (p, n) to 8.90e-19 m (²³⁸U): 17.71 down to 15.51 powers of 12 above the Planck length. For comparison the atom's a₀ sits at 22.72 p12, ƛ_e at 20.74, ƛ_t at 15.61 (Part A). B/(M c²) across ²H to ²³⁸U spans 0.0012 to 0.0095, i.e. 0.3 to 2.6 times α/2 = 0.00364868; the ratios are in the output, and no relation is claimed.

## Not done / flags
- Hadrons beyond p and n (π, K, other mesons and baryons), nuclear charge radii, atomic ionization energies and molecular binding are not in this map. Hydrogen, positronium, lithium and the periodic-table sample are in their own maps.
- Quark masses are PDG scheme values with 90% CL ranges. Light quarks are MS-bar at 2 GeV, c and b at their own mass, t from direct measurement. Their order in the sorted list is scheme-dependent. The confined quarks have no pole mass.
- Neutrino rows are lower bounds. The largest gap on the ladder is the one least constrained by measurement.
- The AME parse takes measured values only (skips # and *). Atomic masses used for nuclei subtract Z·m_e and ignore electron binding.
- The previous map's τ row is corrected above; its other rows stand.

sha256: *full_ladder_map.py 59786d1174975cb5b2bd9d8859b811e911ae1fd676acb52df0aae403e698d14e; *full_ladder_map.out 7791c1d1a42504687f16cfb22985df3dfe23d70da5fdf660146ab9ada08fdf31.
