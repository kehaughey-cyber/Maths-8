# Map — the chemical level: atoms, molecules, atomization, solids (2026-10-29)

Third map of the ladder (after `lepton_ladder.md` and `full_ladder.md`). Same dictionary: cycles = R·E/ħc, α/2 = the hydrogen rung, positions in powers of 12 above the Planck length (p12). Tabulation only: sourced numbers, ratios, ranges. No rule proposed, nothing fitted.
Run: `py -3 -I -u explore/chemical_ladder_map.py > explore/chemical_ladder_map.out`. Raw output (all 104 atoms, 89 diatomics, 401 molecule rows, 17 solids): `explore/chemical_ladder_map.out`.

## Sources (persisted in `explore/data/`)
| file | content | sha256 |
|---|---|---|
| `PeriodicTableJSON.json` | 119 elements: ionization energies, shells, density, phase, atomic mass (Bowserinator, github raw; values trace to Wikipedia, not independently checked against NIST; same hash as the earlier ptable map) | 05e478cb1192c5bbfad8d9600fd3b4c7902c0966ad5d0408bfcc4d5092424c0d |
| `cccbdb_diatomic_exp_bondlengths.html` | experimental diatomic bond lengths r_e in Å, 318 cells, NIST CCCBDB Release 22 (cccbdb.nist.gov/diatomicexpbondx.asp) | 416af651d8ae2e4908c2aefda71d54ed8edf526d533ec7251b33e93d5fab1f2c |
| `cccbdb_enthalpy_formation_0K.html` | enthalpy of formation at 0 K, 450 species (CODATA, JANAF, Gurvich, TRC and others), NIST CCCBDB (cccbdb.nist.gov/hf0kx.asp) | 7afa4324b91989a66f0413e2bd81bd6846e94c4ae2e4c23939269a25315d28fb |
| `cccbdb_exp_diatomic_constants.html` | ωe, Be etc. for diatomics (fetched, not used by the script yet) | c9086c766db9fe7a0f9a9c5a0f33d2d12cd5a4ae387119f6524736393949e3ba |

Atomization energy D0 = Σ Hfg(atoms, 0 K) − Hfg(molecule, 0 K), in eV (÷ 96.485332 kJ/mol per eV). It uses the CCCBDB atoms (24 tabulated, so heavy-element molecules are missing). Solid cohesion Ec = Hfg of the gas atom at 0 K from the element's reference state; for H, N, O, F, Cl the reference state is a diatomic gas, so Ec is half the bond energy and those are left out of the solids.

## The three levels on one scale (cycles/(α/2); R positions in p12)
| level | members | R (m) | R in p12 | E | cycles/(α/2) range (median) |
|---|---|---|---|---|---|
| atoms, valence rung (R = n²a₀/Z_eff, E = IE₁) | 104 | 3.94e-11 (He) … 6.89e-10 (Fr) | 22.597 … 23.749 | 3.89 eV (Cs) … 24.59 eV (He) | Z_eff 0.9997 (H) … 5.3327 (Rn); identity, no new information |
| diatomic molecules (R = r_e, E = D0) | 89 | 0.741 Å (H₂) … 3.891 Å (Mg₂) | 22.85 … 23.52 | 0.037 eV (Mg₂) … 11.108 eV (CO) | 0.0202 (Mg₂) … 1.7404 (CO) (median 0.8965) |
| atomization of 401 molecule rows (energy only, no size in these data) | 401 | – | – | 0.0373 (Mg₂) … 83.6946 eV (C₇H₁₄) | D0/atom/Ry 0.0014 (Mg₂) … 0.4154 (C₃O₂) |
| solids (R = r_ws, E = Ec) | 17 | 1.245e-10 (Be) … 2.620e-10 (K) | 23.06 … 23.36 | 0.93 eV (K) … 7.37 eV (C) | 0.2874 (Zn) … 1.4104 (C) (median 0.6327) |

Whole chemical level: every R sits within 22.60 … 23.75 p12, i.e. 1.15 powers of 12 (1.24 decades), and every cycles/(α/2) from the atoms, molecules and solids sits within 0.02 … 5.3 (diatomics and solids within 0.02 … 1.74). Nuclear Compton lengths (from `full_ladder.md`) are 15.51 … 17.71 p12 and the top quark's is 15.61, so the chemical level is a separate shelf 5 to 8 powers of 12 above the nuclear one, and ƛ_e (20.74 p12) is 2 powers of 12 below it.

## Representatives (Part E; cycles = R·E/ħc)
| level | R m | E eV | cycles | cycles/(α/2) |
|---|---|---|---|---|
| H atom (a₀, Ry) | 5.2918e-11 | 13.6057 | 3.648676e-03 | 1.0000 |
| He valence | 3.9365e-11 | 24.5872 | 4.904889e-03 | 1.3443 |
| Fe valence | 2.7774e-10 | 7.9028 | 1.112306e-02 | 3.0485 |
| Cs valence | 5.9350e-10 | 3.8939 | 1.171160e-02 | 3.2098 |
| H₂ (r_e = 0.741 Å, D0 = 4.4774 eV) | 7.4100e-11 | 4.4774 | 1.681335e-03 | 0.4608 |
| N₂ (1.098 Å, 9.7590 eV) | 1.0980e-10 | 9.7590 | 5.430265e-03 | 1.4883 |
| CO (1.128 Å, 11.1084 eV) | 1.1280e-10 | 11.1084 | 6.350020e-03 | 1.7404 |
| NaCl (2.361 Å, 4.2224 eV) | 2.3610e-10 | 4.2224 | 5.052069e-03 | 1.3846 |
| Li solid (r_ws 1.727e-10 m, Ec 1.6344 eV) | 1.7271e-10 | 1.6344 | 1.430573e-03 | 0.3921 |
| C solid (r_ws 1.378e-10 m, Ec 7.3711 eV) | 1.3777e-10 | 7.3711 | 5.146207e-03 | 1.4104 |
| Si solid (1.685e-10 m, 4.6194 eV) | 1.6846e-10 | 4.6194 | 3.943514e-03 | 1.0808 |

## What the table shows, stated plainly
- Raw, level to level: H₂ has r_e/a₀ = 1.40028706 and D0/Ry = 0.32908022; Li solid has r_ws/a₀ = 3.263812 and Ec/Ry = 0.12012952; a₀/ƛ_e = 137.035999.
- In the sample, the cycles of a bond or a cohesion fall in the same band as the cycles of an atom's own binding: diatomics at 0.02 … 1.74 times α/2, solids at 0.29 … 1.41, atoms at 1.0 … 5.3 (that last range is the identity Z_eff·α/2). The three levels overlap on the same scale rather than separating.
- The extremes are the weakest systems: Mg₂ (0.0202), Be₂ (0.0301), Na₂ and Li₂ (0.31–0.38) at the low end, which are van der Waals or alkali dimers; CO (1.7404), SiO (1.7261), SiS (1.7102) at the high end.
- The 401-row atomization table (Part C) is energy only. D0 per atom in Ry runs 0.0014 … 0.4154; hydrocarbon rows (C₆H₁₄, C₇H₁₄) are near 0.28–0.29.

## What it does not show / flags
- Atoms: the Z_eff column is an identity (cycles = Z_eff·α/2), so it adds no information; it is shown to put the atom on the same axis.
- Diatomics: 89 of the 318 bond-length cells matched a tabulated 0 K enthalpy and all atoms. Excited-state and ion cells are not used. Bond lengths are r_e, atomization energies are D0 (0 K), so the cycles use r_e·D0 and not r_e·De.
- Solids: only 17 elements have both a 0 K atomic enthalpy and density ≥ 0.5 g/cm³ in the files. r_ws is a volume per atom, not a bond length. Hfg(atom) is the enthalpy of atomization from the reference state, which is the cohesive energy for monatomic solids.
- The molecule table has no sizes beyond diatomics; polyatomic geometries, ionic and metallic bonding, liquids and condensed-molecule cohesion are not here.
- Single sources: Wikipedia-derived element data; CCCBDB compiled from several originals. The unrounded values in the .out are the inputs' digits.
- Not done: nuclear sizes (not in the sourced set), so the nuclear shelf is placed at ƛ only and the cycles of a nucleus at its own radius are not computed.

sha256: *chemical_ladder_map.py 32695aac8927dbbcdaabbc796cb696e594ab29a965d59799c1fa241bd6ef212f; *chemical_ladder_map.out 3157b5766314cec258aa876ce69920e0320c496404265b08f06fc458ce8742aa.
