# Carbon gram — refinements: muons, u/d masses, neutrinos, what is derived (2026-10-29)

Follows `maps/carbon_one_gram.md` (append-only; that file and its .out are not changed). Tabulation only; nothing fitted.
Run: `py -3 -I -u explore/carbon_gram_refinements.py > explore/carbon_gram_refinements.out`. Raw output: `explore/carbon_gram_refinements.out`.

## Sources added (persisted in `explore/data/`)
| file | content | sha256 |
|---|---|---|
| `pdg2020_cosmic_rays.txt` | PDG Review 30, Cosmic Rays (rev. Oct 2019, 1 June 2020): muon intensity, cos² law, 10–15% lower normalization | 9da43de77976d31f5b5bf5b1fc3fefcdac78f3da0df0529bff88e6304263898b |
| `pdg2024_quarks.txt` | u, d, mu/md, (mu+md)/2 (already in the repo) | see `full_ladder.md` |
| `borexino_2018_arxiv1707.09279.pdf` / `.txt` | Borexino Phase-II, pp-chain solar neutrinos, Table II: measured fluxes and SSM predictions (pdftotext of the arXiv PDF) | pdf 5c656c8da7569b33513c3e95e439d5f574287898739074b1588bc7e5a9dc3d3e; txt e95985aa4038ba3e67b34ce32a1dab4a07b34fc69676122ae30d124a24340aab |

Still secondary: FLAG m_ud = 3.364(41) MeV (via a search result quoting arXiv:2003.11703). Recalled, not in a saved file: sin²θ_W = 0.2312, G_F, pp mean energy 0.265 MeV, the one-loop α_s values in the scale illustration.

## 1. Muons (the cos² law and the quoted intensity)
PDG: vertical integral intensity above 1 GeV/c at sea level ≈ 70 m⁻² s⁻¹ sr⁻¹, recent measurements favour 10–15% lower, angular law cos²θ, and "I ≈ 1 cm⁻² min⁻¹ for horizontal detectors". The rate through a horizontal face is ∫ I cos²θ cosθ dΩ = (π/2) I exactly. On the gram's cube face (0.4327 cm²):
| case | per minute | per day |
|---|---|---|
| 70, E > 1 GeV | 0.2855 | 411 |
| 70 minus 10% | 0.2569 | 370 |
| 70 minus 15% | 0.2427 | 349 |
| PDG "1 cm⁻² min⁻¹" (all energies) | 0.4327 | 623 |
The two PDG statements differ by 1.52 because of the energy threshold, so the carried range is 0.24–0.43 per minute (factor 1.78). The previous map's 0.2855 sits at the top of the E > 1 GeV group; neither value is "the" rate, the cos² law and the quoted intensity are as good as the PDG statement, and the energy threshold is a convention. A cos^n exponent of 1.8 instead of 2 would change it by 5%.

## 2. u and d masses
PDG 2024 (MS-bar, 2 GeV, 90% CL): mu = 2.16 ± 0.07, md = 4.70 ± 0.07 MeV. Valence 18u + 18d = 123.48 MeV = 1.1047% of the atom's rest energy; fully correlated ±0.07 gives 120.96–126.0 MeV (1.082–1.127%). With the FLAG average m_ud = 3.364(41) MeV and PDG mu/md = 0.462: 121.10 MeV (1.083%), 1.9% below the PDG central, within the PDG span. The scale convention is the larger effect: a one-loop illustration (rough α_s, not a saved source) moves the sum to 150.7 MeV (1.35%) at 1 GeV and 113.9 MeV (1.02%) at 3 GeV. So the statistical uncertainty is 2–3%; the scale convention is 20% or so. The bare-mass share of the atom is ~1% on any of them; the other ~99% is nucleon mass, not bare quark mass.

## 3. Neutrinos through the gram (solar)
Borexino Phase-II Table II (fluxes inferred assuming MSW-LMA), cm⁻² s⁻¹: pp (6.1 ± 0.5 +0.3/−0.5)e10 [SSM 5.98e10 HZ, 6.03e10 LZ]; ⁷Be (4.99 ± 0.11 +0.06/−0.08)e9 [4.93e9, 4.50e9]; pep (HZ) (1.27 ± 0.19 +0.08/−0.12)e8 [1.44e8, 1.46e8]; CNO < 7.9e8 at 95% CL [4.88e8, 3.51e8].
Through the gram (projected sphere area 0.5232 cm²): pp 3.19e10 s⁻¹, ⁷Be 2.61e9, pep 6.6e7; together 3.46e10 crossings per second. Interactions are far rarer: tree-level elastic ν_e–e scattering on the gram's 6N electrons gives about 3e-11 per second (2.6e-6 per day), order of magnitude only (σ ~ 1e-45–1e-44 cm²; pp spectrum not integrated; νμ/ντ components omitted). For scale, the gram's own ¹⁴C decays (natural carbon, 0.226 Bq) make 0.226 antineutrinos per second, which is 6.5e-12 of the solar crossings. Not included: ⁸B, hep, measured CNO, geo-, reactor, atmospheric and relic neutrinos (no saved sources).

## 4. Derived ratios
None. Every ratio in the carbon maps is arithmetic on sourced inputs or a dictionary identity (cycles = RE/ħc; valence rung = Z_eff·α/2; a₀/ƛ_e = 1/α). 1/α, the lepton mass ratios, the 1.15 nuclear cycles and the 15.7-decade information gap are inputs or observations here, not outputs of the floor. The map therefore gives the pattern to be explained, not an explanation of it.

## Verdict on the four items
Muons: range 0.24–0.43/min, threshold-dependent. u/d: 1.1% ± 0.03% statistical, ±20% by scale convention. Neutrinos: 3.5e10 crossings/s, ~1e-11 interactions/s, one-sided. No result from this file changes an order-of-magnitude statement in `carbon_one_gram.md`.

sha256: *carbon_gram_refinements.py 5a41823f16de7a0ea8953544ad45923b0a2bdad4a4e7e8e359d9ed30e159700b; *carbon_gram_refinements.out 87c77bddec713b1970e42c8640772051d3d93898ec80b99508b28043bfc04b61.
