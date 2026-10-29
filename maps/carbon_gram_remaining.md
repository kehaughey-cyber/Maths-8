# Carbon gram — the items listed as not done (2026-10-29)

Closes the "not done" list in `carbon_gram_refinements.md`: heat content and phonons, graphite, polyatomic geometry, nuclear matter radius, ⁸B/hep/geo/relic neutrinos. Atmospheric neutrinos were not obtained as a number. Tabulation only; nothing fitted.
Run: `py -3 -I -u explore/carbon_gram_remaining.py > explore/carbon_gram_remaining.out`. Raw output: `explore/carbon_gram_remaining.out`. Sources and which are secondary: `explore/data/carbon_remaining_sourced_values.txt`.
New saved sources: `pdg2024_baryons.pdf/.txt`, `pdg2024_rev_bbang-cosmology.pdf/.txt`, `pdg2024_rev_neutrino-mixing.pdf/.txt`, `solar_neutrinos_review_arxiv2501.09971.pdf/.txt`, `geonu_borexino_arxiv1909.02257.pdf/.txt`.

## A. Heat content and phonons (diamond)
Debye temperature, solved from the measured value (defined by it, not fitted to anything else): 1861.04 K from Cp(298.16 K) = 6.1149 J/(mol K); 1864.75 K from S(298.15 K) = 2.3782 J/(mol K). They differ by 0.20%, so the Debye model is not exact for diamond; both numbers are model-defined.
- k·Θ_D = 0.16037 eV (Cp) or 0.16069 eV (S). The Raman zone-centre optical phonon, 1332.7 ± 0.2 cm⁻¹ (secondary), is 0.16523 eV = 1.030 k·Θ_D = 6.43 kT at 298.15 K.
- Heat content U(298.15) − U(0): 43.64 J per gram (Cp) or 43.42 J (S) = 4.9e-13 of Mc². Zero-point energy 1450.6 J per gram (Cp), 3.3 times the heat content at room temperature.
- 3N = 1.5055e23 modes. Cycles of one Debye quantum across the C–C bond: 1.2552e-4 (0.0344 × α/2); across the lattice constant: 2.8988e-4. ħc/(kΘ_D) = 1.230 µm = 26.76 p12 above the Planck length.

## B. Graphite vs diamond (density 2.267 g/cm³, in-plane 1.42 Å, interlayer 3.35 Å are search-result quotations)
| | diamond | graphite |
|---|---|---|
| sphere radius of the gram | 0.0040808 m, 30.0248 p12 | 0.0047223 m, 30.0836 p12 (×1.1572) |
| Bekenstein–Compton bits | 1.0516e38 | 1.2169e38 |
| thermodynamic bits | 2.0709e22 (S = 2.3782) | 5.079e22 (S = 5.833, labelled amorphous) to 5.400e22 (S = 6.201) |
| gap | 15.706 decades | 15.380 to 15.353 decades |
| bond cycles (E = Ec/2 vs Ec/1.5) | 0.0028847 | 0.0035362 (in-plane 1.42 Å) |
Graphite's interlayer distance is 23.459 p12, and in-plane/interlayer = 0.4239. The entropy values on the saved NIST page are not both graphite-labelled; the graphite-like entropy is a range, not a number. Ec is one number for both phases; the ≈2 kJ/mol difference is not applied.

## C. Polyatomic geometry (CCCBDB experimental; D0 from the saved 0 K enthalpies; "edge" = structural bond, not a measured bond energy)
| molecule | D0 (eV) | edges | mean edge (m) | cycles / (α/2) | D0/atom/Ry |
|---|---|---|---|---|---|
| CO | 11.108 | 1 | 1.128e-10 | 1.740 | 0.408 |
| CH₄ | 17.016 | 4 | 1.087e-10 | 0.642 | 0.250 |
| CO₂ | 16.561 | 2 | 1.162e-10 | 1.336 | 0.406 |
| C₂H₂ | 16.856 | 3 | 1.1097e-10 | 0.866 | 0.310 |
| C₂H₄ | 23.065 | 5 | 1.1366e-10 | 0.728 | 0.283 |
| C₂H₆ | 28.883 | 7 | 1.1546e-10 | 0.662 | 0.265 |
| C₆H₆ | 56.618 | 12 | 1.2405e-10 | 0.813 | 0.347 |
They fall in the same band as the diatomics (0.02–1.74 × α/2), at 0.64–1.74 × α/2. Most geometries carry no listed uncertainty.

## D. Nuclear matter radius
From the charge radius (2.4702 fm, secondary), r_p = 0.8409 fm and ⟨r_n²⟩ = −0.1155(17) fm² (PDG 2024), and the Darwin–Foldy term 0.03317 fm²: r_pp² = 5.4771 fm², r_pp = 2.3403 fm (0.9474 × r_ch). With N = Z and isospin symmetry (Coulomb and the 12C spin-orbit term neglected) this is the point-matter radius. Nucleus cycles B·r/ħc: 1.15371 with r_ch, 1.09305 with r_pp (−5.26%). The 4.0 in the nucleon row and the A^(4/3) growth are unaffected in kind.

## E. Neutrinos through the gram (projected area 0.52317 cm²; crossings, not interactions)
| species | flux (cm⁻² s⁻¹) | crossings per second | note |
|---|---|---|---|
| ⁸B solar | 5.25e6 | 2.75e6 | SNO three-phase NC total (5.25 ± 0.16 +0.11/−0.13)e6, via the 2025 review |
| hep solar | 7.98e3 / 8.25e3 | 4.2e3 / 4.3e3 | SSM only (not observed), ±30% |
| geo (U, Th as listed) | 2.8e6 + 2.5e6 | 1.46e6 + 1.31e6 | Borexino; first column of a table whose headings were lost; ⁴⁰K and reactor not included |
| relic, all species at m₃(min) 0.0503 eV | 1.06e11 | 5.5e10 | n = 336.05 cm⁻³ (3/22 n_γ per species), mean momentum 3.151 kT_ν, v = 0.0105 c |
| relic, all at m₂(min) 0.0087 eV | 6.13e11 | 3.2e11 | v = 0.0609 c |
Relic numbers assume isotropy, no gravitational clustering and no Earth motion; masses are unmeasured, so the two rows bracket an assumption. Compare solar pp+⁷Be+pep: 3.46e10 s⁻¹. Atmospheric: the PDG review gives only a figure; no integral flux was extracted and none is quoted. Interactions are not computed (relic cross sections not sourced).

## What this does and does not say
- Nothing here changes an order-of-magnitude statement in the earlier maps. The graphite choice narrows the information gap from 15.71 to ≈15.35–15.38 decades; it does not close it.
- Phonons put one more energy scale in the ladder (0.160 eV, 1.2 µm), between the thermal kT (0.0257 eV) and the bond energies; the Debye quantum is 0.034 × α/2 in cycles at the bond.
- Open after this: atmospheric flux; the 12C spin-orbit term in the matter radius; the weak force as a column; phonon dispersion beyond Debye; polyatomics beyond seven carbon-containing molecules; and sources still secondary (12C radius, diamond a, graphite structure, Raman frequency, geo table headings).

sha256: *carbon_gram_remaining.py 32f38f7721649f09618d3226fdd7c6984c6c18a146d0b1d87b4b4a6af4c2bcd8; *carbon_gram_remaining.out f8aa6ee30b2ef8b8a52fb3f5f6627195307bd0079c497612f18d117d51fd65b7; carbon_remaining_sourced_values.txt f79dceec58db0e6b76811c6689c498d24eecad2af1b92bbab353657155c55cfe.
