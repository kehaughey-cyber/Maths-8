# Map — the same rungs in four languages: energy and size, mass, charge, information (2026-10-29)

Nine rungs written four ways. Tabulation only; nothing fitted, no rule proposed. Inputs as in `carbon_one_gram.md` and `full_ladder.md`.
Run: `py -3 -I -u explore/four_languages_ladder.py > explore/four_languages_ladder.out`. Raw output: `explore/four_languages_ladder.out`.
Stated in the output: the gram's cycle count differs between the energy-size form (1.16008721205e37) and R/ƛ_C (1.16008721242e37) in the 10th digit, because ħc is entered as the rounded literal 1.973269804e-7 eV m. Not a physical difference.

## Rungs (R, E)
Compton rungs: R = ħ/(mc), E = mc² (τ, μ, e, p). Nucleus: R = r_ch, E = total binding. H atom: a₀, Ry. C valence: R = n²a₀/Z_eff (n = 2, Z_eff 1.8195), E = IE₁. C–C bond: R = a√3/4, E = Ec/2. Gram: R = equal-volume sphere, E = Mc².

## 1. Energy and size (cycles = R·E/ħc)
| rung | p12 | E eV | cycles |
|---|---|---|---|
| τ | 17.4549 | 1.77693e9 | 1 |
| μ | 18.5907 | 1.0565838e8 | 1 |
| e | 20.7363 | 510998.95 | 1 |
| p | 17.7119 | 9.3827209e8 | 1 |
| ¹²C nucleus | 18.7033 | 9.2161735e7 | 1.153709026 |
| H atom | 22.7164 | 13.605693 | 0.003648676 |
| C valence | 23.0334 | 11.260779 | 0.006638794 |
| C–C bond | 23.1474 | 3.6855343 | 0.002884676 |
| gram | 30.0248 | 5.6095886e32 | 1.160087212e37 |

## 2. Mass (m, gravitational coupling (m/m_P)², Compton length, Schwarzschild radius)
| rung | m/m_e | log₁₂(m/m_P) | (m/m_P)² | ƛ p12 | r_s p12 |
|---|---|---|---|---|---|
| τ | 3477.3653 | −17.4549 | 2.1183e-38 | 17.4549 | −17.176 |
| μ | 206.76828 | −18.5907 | 7.48953e-41 | 18.5907 | −18.3118 |
| e | 1 | −20.7363 | 1.75181e-45 | 20.7363 | −20.4574 |
| p | 1836.1527 | −17.7119 | 5.90615e-39 | 17.7119 | −17.433 |
| ¹²C nucleus | 21868.662 | −16.7149 | 8.37782e-37 | 16.7149 | −16.436 |
| H atom | 1837.1527 | −17.7117 | 5.91258e-39 | 17.7117 | −17.4327 |
| C valence / bond (atom) | 21874.662 | −16.7148 | 8.38242e-37 | 16.7148 | −16.4359 |
| gram | 1.0977691e27 | 4.32018 | 2.1111e9 | −4.32018 | 4.59912 |

## 3. Charge (Q felt, Coulomb cycles αQ² = R·E_C/ħc, E/E_C)
| rung | Q | αQ² | E/E_C |
|---|---|---|---|
| τ, μ, e, p (Compton) | 1 | 0.0072973526 | 137.036 |
| ¹²C nucleus | 6 | 0.26270469 | 4.3916575 |
| H atom | 1 | 0.0072973526 | 0.5 |
| C valence | 1.8195 | 0.024158674 | 0.27479962 |
| C–C bond, gram | 0 (neutral) | – | – |

Gram: positive charge 6N e = 48242.666 C; all charges 12N e = 96485.332 C, which is the Faraday constant, because 12N = 1 mol. Net 0. Unscreened Coulomb energy of the positive charge alone at the gram's radius: 3.199e40 eV = 5.70e7 × Mc².

## 4. Information (bits = 2π cycles / ln 2)
| rung | bits per object | count in gram | total bits |
|---|---|---|---|
| τ, μ, e, p | 9.064720284 | e, p: 3.0111e23 each | 2.7294511e24 each |
| ¹²C nucleus | 10.45804961 | 5.0185e22 | 5.2483206e23 |
| H atom | 0.03307423 | – | – |
| C valence | 0.06017881 | 5.0185e22 | 3.020044e21 |
| C–C bond | 0.02614878 | 1.0037e23 | 2.6245273e21 |
| gram | 1.051586608e38 | 1 | 1.0515866e38 |
Other counts of the same gram: thermodynamic entropy 2.0708965e22 bits; atoms 5.0184506e22; log₂ N = 75.41 bits to label one atom.

## What the columns do and do not show
- Identities, not findings: cycles = 1 at every Compton rung; E/E_C = 1/α = 137.036 at every Compton rung (E = mc², E_C = αmc²); E/E_C = ½ for the H atom (virial); bits = 2π·cycles/ln 2.
- Non-identity numbers: the nucleus at 1.1537 cycles, E/E_C = 4.39 for Q = 6; C valence E/E_C = 0.275; the gram's (M/m_P)² = 2.11e9; unscreened charge energy 5.7e7 × Mc².
- The gravitational coupling (m/m_P)² is the mass-language analogue of αQ²: both are cycles of a pair's binding at any R. It runs from 1.75e-45 (e) through 5.9e-39 (p) to 2.11e9 (gram) and passes 1 at the Planck mass, between the nucleus and the gram.
- The gram is the only rung where the mass column has an order-one or larger coupling, and the only rung where the charge column is cancelled (net 0 against 5.7e7 unscreened).

sha256: *four_languages_ladder.py ed031e110115000981d7b4546ad2806e4156ab6381adfd0fc3530b1241c4615b; *four_languages_ladder.out 6a1e0aa5f42bd2d489490a82e11c5ad2248da6beda487ad75af8d83d93587605.
