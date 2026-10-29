# Map — one gram of carbon-12, from information to energy to leptons (2026-10-29)

One element, examined through every level the sourced data reach, with the gram as the object. Same dictionary as the other ladder maps (cycles = R·E/ħc, α/2 = the hydrogen rung, positions in powers of 12 above the Planck length). Tabulation of sourced inputs and arithmetic on them; no rule proposed, nothing fitted.
Run: `py -3 -I -u explore/carbon_one_gram.py > explore/carbon_one_gram.out`. Raw output: `explore/carbon_one_gram.out`.

## Why carbon-12
It is the one element where every level has a measured number: the nucleus (12 u exactly, a measured charge radius, B/A from AME2020), all six electrons (the complete ionization sequence down to the bare nucleus; C⁵⁺ is hydrogen-like), a molecule (C₂), a solid (diamond, one lattice constant, 8 atoms per cell), a thermal state (NIST S and Cp), and a radioactive sibling (¹⁴C) that makes leptons inside the gram. Hydrogen is simpler but has one electron and no solid with a simple cell. The gram is taken as pure ¹²C in the diamond structure; natural carbon differs by 0.1% in atom count and carries ¹³C (1.06%) and ¹⁴C.

## Sources
Saved in `explore/data/`: AME2020 mass table; NUBASE2020 (14C half-life 5.70 ± 0.03 ky read from line 014 0060 of the saved file); PeriodicTableJSON (C ionization energies); PDG 2024 quark text (u 2.16, d 4.70 MeV, MS-bar 2 GeV); NIST WebBook diamond page (S° = 2.3782 J/(mol·K), DeSorbo 1953) and `carbon_sourced_values.txt` (the values below that came by web search and not from a saved file: ¹²C rms charge radius 2.4702 ± 0.0022 fm [IAEA / Angeli–Marinova 2013, the IAEA page itself blocked a bot check and was not opened]; diamond a = 3.56683 Å [Straumanis & Aka 1951]; sea-level vertical muon intensity 0.70e-2 cm⁻² s⁻¹ sr⁻¹ for E > 1 GeV, cos² law [Cosmic ray recipes, arXiv:astro-ph/0601158]; modern ¹⁴C activity 0.226 Bq/g C). These are secondary quotations from search results; the primary papers were not opened.

## The gram
N = M/(12 u) = 5.0184506350676e22 atoms (1/12 mol, N_A exact). Per gram: protons, neutrons and electrons 3.01107038104e23 each; valence quarks 9.03321114312e23 u and 9.03321114312e23 d. Diamond volume 2.846602994e-7 m³ (density 3512.9591 kg/m³); cube side 6.5782287 mm; equal-volume sphere radius 4.0808074 mm. Rest energy M c² = 8.98755178737e13 J = 5.60958860380e32 eV.

## 1. Information (three different bit counts)
| count | value | what it is |
|---|---|---|
| atoms | N = 5.0184506e22 (log₂ N = 75.41) | counting the objects |
| thermodynamic entropy | 0.1981833 J/K = 1.4354360e22 nats = 2.0708965e22 bits (0.28603 nats/atom) | diamond at 298.15 K, S° = 2.3782 J/(mol·K) |
| Bekenstein–Compton, R = sphere radius, E = M c² | 1.16008721e37 cycles = 7.28904e37 nats = 1.0515866e38 bits | upper bound for that region |
Gap between the Bekenstein and thermodynamic bit counts: 5.0779e15 (15.71 decades). Landauer cost of the entropy at 298.15 K: T S = 59.088 J; kT ln 2 = 2.853e-21 J per bit. The gram's own Compton wavelength is 3.5177e-40 m = 2.1764e-5 Planck lengths (M/m_P = 45946.7), at −4.32 powers of 12, i.e. below the Planck length.

## 2. Energy (per atom, and the share of the gram's rest energy)
| item | eV per atom | J per gram | fraction of M c² |
|---|---|---|---|
| atom rest energy 12 u c² | 1.1177929229e10 | 8.987551787e13 | 1 |
| nuclear rest energy (12 u − 6 mₑ) c² | 1.1174863235e10 | 8.985086592e13 | 0.99972571 |
| 6 p + 6 n (free nucleons) | 1.1267025052e10 | 9.059188788e13 | 1.007970691 |
| nuclear binding B (AME B/A × 12) | 92161735.2 | 7.410213027e11 | 0.00824497 |
| 18 u + 18 d bare quark masses (MS-bar 2 GeV) | 123480000 | 9.928340679e11 | 0.01104677 |
| 6 electrons rest | 3065993.70 | 2.465195171e10 | 2.742900e-4 |
| all six ionization energies | 1030.1078717 | 8282525.0 | 9.21555e-8 |
| cohesion Ec = Hfg(C atom, 0 K) | 7.371068589 | 59266.67 | 6.5943e-10 |
| kT at 298.15 K | 0.025692579 | 206.58 | 2.2985e-12 |
Per proton, the bare 2u + 1d masses are 9.02 MeV = 0.961% of m_p c²; per neutron 11.56 MeV = 1.230% of m_n c². The u, d uncertainties (PDG 90% CL, ±0.07 MeV each) give about ±2.5 MeV on the 123.48 MeV sum. Step ratios along the per-atom list (Part 6 of the output): nuclear rest → bare quark masses 90.499; quark masses → B 1.3398; B → electron rest 30.059; electron rest → ΣIE 2976.4; ΣIE → Ec 139.75; Ec → kT 286.89; first to last 4.3853e11 (log₁₂ 10.788).
Checks printed: atom = nuclear + 6 mₑ to 2e-17 eV; 6 mₚ + 6 mₙ − B differs from nuclear rest by −81.58 eV, which is the six hydrogen-atom binding energies in the AME definition of B (6 × 13.606 = 81.63 eV; the 0.05 eV gap is below the ±0.6 eV precision of B/A × 12). C⁵⁺: IE₆ = 489.9915772 eV against Z²Ry = 489.8049524 eV, ratio 1.000381.

## 3. Sizes (m; powers of 12 above the Planck length)
τ Compton wavelength 1.1105e-16 (17.455); ¹²C rms charge radius 2.4702e-15 (18.703); μ Compton 1.8676e-15 (18.591); electron Compton 3.8616e-13 (20.736); C⁵⁺ 1s a₀/6 = 8.8196e-12 (21.995); Wigner–Seitz radius 1.1063e-10 (23.013); diamond C–C 1.5445e-10 (23.147); a = 3.5668e-10 (23.484); cube side 6.5782e-3 (30.217); sphere radius 4.0808e-3 (30.025). Ratios: R_sph / C–C = 2.6422e7; C–C / r_ch = 62524.6; ƛ_e / r_ch = 156.327; r_ch / ƛ_τ = 22.244.

## 4. The levels in the dictionary (cycles = R·E/ħc; count in the gram)
| level | cycles / object | /(α/2) | count | total cycles |
|---|---|---|---|---|
| nucleus, R = r_ch, E = B | 1.153709026 | 316.199 | 5.0185e22 | 5.7898e22 |
| nucleus, R = r_ch, E = nuclear rest energy | 139.8903845 | 38340.04 | 5.0185e22 | 7.0203e24 |
| per nucleon, R = r_ch, E = B/12 | 0.0961424188 | 26.350 | 6.0221e23 | 5.7898e22 |
| C⁵⁺ 1s electron, R = a₀/6, E = IE₆ | 0.02190039899 | 6.00229 | 5.0185e22 | 1.0991e21 |
| valence electron, R = n²a₀/Z_eff (n = 2), E = IE₁ | 0.006638794288 | 1.81951 | 5.0185e22 | 3.3316e20 |
| diamond bond, R = C–C, E = Ec/2 | 0.002884675947 | 0.79061 | 1.0037e23 | 2.8953e20 |
| cohesion, R = r_ws, E = Ec | 0.004132696644 | 1.13266 | 5.0185e22 | 2.0740e20 |
| thermal, R = a, E = kT | 4.644122e-5 | 0.012728 | 5.0185e22 | 2.3306e18 |
| the gram, R = sphere radius, E = M c² | 1.160087212e37 | 3.1795e39 | 1 | 1.1601e37 |
The C⁵⁺ row is Z·α/2 with Z = 6 (identity); the valence, bond and cohesion rows sit between 0.79 and 1.82 times α/2; the nuclear rows sit at 316 and 38340 times α/2, with B at R = r_ch giving 1.153709 cycles.

## 5. Leptons in and through the gram
- **Held:** 3.01107e23 electrons, 2.7429e-4 of the mass, bound at 1030.108 eV per atom in total.
- **Made inside it (¹⁴C):** with T½ = 5.70 ky, λ = 3.853423e-12 s⁻¹; a modern activity of 0.226 Bq/g C needs 5.8649e10 ¹⁴C atoms per gram of carbon, a ¹⁴C/C ratio of 1.169742e-12 (derived from activity and half-life, not assumed). Each decay emits one electron and one antineutrino; Q = 156.47645 keV (AME2020 ¹⁴C − ¹⁴N mass excess); 0.226 of each per second per gram, 7.132e6 per year; at most 5.666e-15 W if each decay deposited all of Q.
- **Passing through (cosmic muons):** the horizontal face of the 6.578 mm cube is 0.43273 cm²; with I_v = 0.70e-2 cm⁻² s⁻¹ sr⁻¹ and a cos² angular law the rate is (π/2) I_v A = 4.758e-3 s⁻¹ = 0.2855 per minute = 411 per day (E > 1 GeV). This number rests on the assumed angular law and on a single quoted intensity.
- **Where each charged lepton would sit if it were bound to the ¹²C nucleus (hydrogenic model, Z = 6, reduced mass, point nucleus, nonrelativistic; the μ and τ values are not measured levels and the τ one is inside the nuclear size, so it is not valid there):** electron 8.8200e-12 m = 3570.57 r_ch, E = 489.78 eV; muon 4.3058e-14 m = 17.431 r_ch, E = 100327.5 eV; tau 2.9396e-15 m = 1.1900 r_ch, E = 1469554.8 eV. The e/μ radius ratio is 204.8 and the μ/τ ratio is 14.65 (the mass ratios 206.77 and 16.82 reduced by the nucleus-mass correction).
- **Not given:** neutrino fluxes through the gram (solar, atmospheric, 14C antineutrinos reaching other matter); not sourced here.

## What this puts side by side (no claim beyond the numbers)
1. One gram spans, in a single object: a count of 75 bits, an entropy of 2.07e22 bits, and a bound of 1.05e38 bits; and per atom an energy ladder from 1.12e10 eV down to 0.0257 eV (10.79 powers of 12), with the nuclear binding at 0.824%, the bare quark masses at 1.105%, and the electrons at 0.0274% of the rest energy.
2. The sizes inside the gram run from r_ch = 2.47 fm to the sphere radius 4.08 mm, 18.70 to 30.03 powers of 12; the chemical shelf (23.0 to 23.5) is the one where bond length, cohesion and valence electrons all sit, and the nuclear binding and the lepton Compton wavelengths all sit between 17.45 and 20.74.
3. In the hydrogenic picture the three charged leptons sample the gap between the nuclear surface and the atomic scale: electron far outside (3570 r_ch), muon at 17 r_ch, tau at about one r_ch.

## Flags and what is not done
- All sizes assume the diamond lattice for the gram; graphite or amorphous carbon would change volume, entropy and the Bekenstein bound's radius.
- The ¹²C radius, diamond lattice constant, muon intensity and ¹⁴C activity are secondary quotations (see Sources). The muon rate rests on the assumed cos² law.
- Quark masses are scheme-dependent (MS-bar at 2 GeV for u, d); they enter only the 1.105% line and carry about ±2.5 MeV.
- NIST Cp (6.1149 J/(mol·K)) was loaded but not used; heat capacity enters no row. The heat content H(298) − H(0), the phonon spectrum, and C₂/graphite comparisons are not included.
- The "levels" table uses r_ch for the nuclear rows; a matter radius or a different convention would change them. It does not claim a nuclear registration.
- No derivation is attempted here of any of these ratios.

sha256: *carbon_one_gram.py 90c3480bb1412815cdefae9d04b1ed84d82b3cee1d55d3cb46cc4754c8e7e6ed; *carbon_one_gram.out d948d39b0926bad2c0cf2ad1f4d1cdc9d67023a1f7140078de65604606ce8721. Inputs added to `explore/data/`: nubase2020_nubase_4.mas20.txt 1585a5eea86c5e17e90307c7e6e786d060049c4039e392a261ff6db977df9859; nist_webbook_diamond_condensed.html 1f1be042b1b543a5a2f5f0cb4a0ce3fdb10451c4b0e466b1ef3a639163416c1e; nist_webbook_carbon_graphite_condensed.html e9b4d17511a2e6b6df02625a9609b29de49a6733c69665e4483d614320a6de7f; carbon_sourced_values.txt 9c9de7832b6c987c0608afa7fdb762c9c2c11a9e083c0ce52025a818c3c2f521.
