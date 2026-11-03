# The two groups of hydrogen-like ions: energy, mass, information, and what else differs (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. The human's request: look at the properties of the light group (H, D, ³He⁺; Z = 1, 2) and the heavy group (¹⁶⁵Ho⁶⁶⁺, ¹⁸⁷Re⁷⁴⁺, ²⁰⁷Pb⁸¹⁺, ²⁰⁹Bi⁸²⁺; Z = 67 to 83), find the commonalities and differences, in energy, mass and information, and add anything else relevant. Scripts: `two_groups.py`, `two_groups_extra.py` (raw `.out` beside each). Nothing fitted. Hyperfine energies are secondary (`HYDROGENLIKE_AND_STEP_RESULTS.md`); radii, binding energies, moments, quadrupole moments and masses are from the saved IAEA table (the proton radius is the CODATA 2022 value); G (Planck mass, used on a log scale only) and m_e/u are recalled. Dictionary of the repo: cycles = R E/ħc, bits = 2π·cycles/ln 2, p12 = log₁₂(R/ℓ_P). Atomic order: R = a₀/Z, E = the Dirac 1s binding energy. Nuclear order: R = the charge radius.

## The two groups, side by side (`two_groups.out`)
| | H | D | ³He⁺ | ¹⁶⁵Ho⁶⁶⁺ | ¹⁸⁷Re⁷⁴⁺ | ²⁰⁷Pb⁸¹⁺ | ²⁰⁹Bi⁸²⁺ |
|---|---|---|---|---|---|---|---|
| **Energy** | | | | | | | |
| 1s binding, Dirac (eV) | 13.606 | 13.606 | 54.43 | 6.524e4 | 8.333e4 | 1.016e5 | 1.044e5 |
| Dirac / non-relativistic | 1.00001 | 1.00001 | 1.00005 | 1.068 | 1.089 | 1.110 | 1.114 |
| orbital speed v/c = Zα | 0.0073 | 0.0073 | 0.0146 | 0.489 | 0.547 | 0.598 | 0.606 |
| hyperfine splitting (eV) | 5.874e-6 | 1.354e-6 | 3.584e-5 | 2.165 | 2.748 | 1.216 | 5.084 |
| hyperfine / 1s binding | 4.3e-7 | 1.0e-7 | 6.6e-7 | 3.3e-5 | 3.3e-5 | 1.2e-5 | 4.9e-5 |
| hyperfine photon wavelength | 21.1 cm | 91.6 cm | 3.46 cm | 573 nm | 451 nm | 1020 nm | 244 nm |
| **Information** (cycles; bits) | | | | | | | |
| atomic order, cycles | 0.00365 | 0.00365 | 0.00730 | 0.2611 | 0.2979 | 0.3322 | 0.3373 |
| atomic order, bits | 0.033 | 0.033 | 0.066 | 2.37 | 2.70 | 3.01 | 3.06 |
| nuclear order, cycles R_N B/ħc | – | 0.0241 | 0.0769 | 35.4 | 40.6 | 45.4 | 45.9 |
| nuclear order, bits | – | 0.22 | 0.70 | 321 | 368 | 411 | 416 |
| nuclear size in its own Compton lengths | 4.0 | 20.4 | 28.0 | 4049 | 4738 | 5367 | 5445 |
| **Mass and size** | | | | | | | |
| nuclear mass (MeV) | 938 | 1876 | 2808 | 1.536e5 | 1.741e5 | 1.927e5 | 1.946e5 |
| nuclear mass / m_e | 1836 | 3670 | 5496 | 3.01e5 | 3.41e5 | 3.77e5 | 3.81e5 |
| gravitational coupling (M/m_P)² | 5.9e-39 | 2.4e-38 | 5.3e-38 | 1.6e-34 | 2.0e-34 | 2.5e-34 | 2.5e-34 |
| p12 of the nuclear order | 18.27 | 18.65 | 18.61 | 19.00 | 19.02 | 19.03 | 19.03 |
| p12 of the atomic order | 22.72 | 22.72 | 22.44 | 21.02 | 20.98 | 20.94 | 20.94 |
| size ratio atomic / nuclear order | 62941 | 24704 | 13458 | 151.8 | 131.4 | 117.5 | 115.5 |
| size ratio atomic order / electron Compton, s | 137.04 | 137.04 | 68.52 | 2.045 | 1.827 | 1.671 | 1.651 |
| **Overlap and structure** | | | | | | | |
| fraction of the 1s electron inside the nucleus (Dirac) | 5.4e-15 | 8.8e-14 | 5.5e-13 | 1.6e-6 | 3.4e-6 | 6.6e-6 | 7.3e-6 |
| nuclear spin I; (2I+1)/(2I) | ½; 2 | 1; 1.5 | ½; 2 | 7/2; 1.14 | 5/2; 1.2 | ½; 2 | 9/2; 1.11 |
| quadrupole moment (barn) | none | 0.0029 | none | 3.58 | 1.94 | none | −0.52 |
| moment-equivalent ring radius / nuclear radius | 0.699 | 0.084 | 0.228 | 0.168 | 0.126 | 0.023 | 0.156 |

## Common to both groups
- One electron in a 1s state, so one spin-½ fermion of the same moment, and a contact (s-wave) coupling to a nuclear moment: the hyperfine energy is E = (8/3)[(2I+1)/(2I)](μ_X/μ_B) Z³α² Ry × A(Zα), with the same Dirac factor A for both (r = E/E_nr = 1.00 at Z = 1, 2; r/A = 0.93 to 0.86 at Z ≥ 67 because of nuclear structure).
- Every ion lies on **one curve**, parametrised by the Lorentz angle θ = arcsin(Zα) (v/c = sin θ, γ = cos θ). The atomic order registers exactly **tan(θ/2)** cycles ((1−cos θ)/sin θ), and the exponent excess of the hyperfine energy is p − 3 = (sin²θ/cos θ)(1/cos θ + 2/(2cos θ − 1)). The light group is at θ = 0.42° and 0.84°, the heavy group at 29.3°, 33.2°, 36.8°, 37.3°.
- The electron is the light particle throughout (M/m_e ≥ 1836), and gravity is negligible in both ((M/m_P)² below 3e-34).
- Both nuclei carry a magnetic moment and a spin; all hyperfine transitions are M1.

## What differs
- **Regime.** v/c ≤ 0.015 against 0.49 to 0.61; Dirac/non-relativistic 1.00001 against 1.07 to 1.11.
- **Energy.** Binding 14 to 54 eV against 65 to 104 keV (1.2e3 to 7.7e3 times); hyperfine 1.4 to 36 μeV against 1.2 to 5.1 eV (3.4e4 to 3.7e6 times); the nuclear moment's share of the binding rises from 1e-7–7e-7 to 1.2e-5–4.9e-5. The hyperfine photon moves from radio (3.5 to 92 cm) to optical (244 nm to 1.02 μm).
- **Information.** The atomic order carries 0.0037 to 0.0073 cycles (0.033 to 0.066 bits) against 0.26 to 0.34 cycles (2.4 to 3.1 bits), a third of one registration. The nuclear order carries 0.02 to 0.08 cycles for D and ³He (0.2 to 0.7 bits; the proton has 3.998 cycles by its rest energy) against 35 to 46 cycles (321 to 416 bits).
- **Mass and size.** A = 1 to 3, 0.9 to 2.8 GeV, a nucleus 4 to 28 of its own Compton lengths across, against A = 165 to 209, 154 to 195 GeV, 4000 to 5400 Compton lengths across (composite, many-nucleon). The atomic and nuclear orders are 1.3e4 to 6.3e4 apart in size for the light group and 115 to 152 apart for the heavy. The atomic order sits 68 to 137 times the electron's Compton length for the light group and only 1.65 to 2.05 times for the heavy, i.e. next to the electron Compton rung (p12 20.74): at p12 20.94 to 21.02 against 22.4 to 22.7.
- **Overlap.** The fraction of the electron inside the nucleus is 5e-15 to 5.5e-13 against 1.6e-6 to 7.3e-6 (3e6 to 1e9 times; the Dirac cusp raises it by about 4 in the heavy group and by 1.000 in the light). This is the property that separates "the moment alone" from "the moment and the nuclear structure".
- **Nuclear structure.** The light nuclei have I = ½, 1, ½ and almost no quadrupole moment. The heavy ones are Ho (I = 7/2, Q = 3.58 b, strongly deformed), Re (I = 5/2, Q = 1.94 to 2.07 b), Bi (I = 9/2, Q = −0.52 b) and Pb (I = ½, no quadrupole moment). Pb has the light group's spin and the largest shortfall from the point-nucleus form (r/A = 0.855), so the shortfall is not the spin multiplicity. The proton is unique in having a moment-equivalent ring (0.587 fm) comparable to its radius (0.70); every other nucleus has 0.02 to 0.23.
- **Exponent.** Exactly 3 (3.0015, secondary data) against 4.0 to 4.2 (rising toward the pole).

## Noticed after computing, not claimed
- **A plateau in the ratio of nuclear to atomic cycles** (`two_groups_extra.out`). Over 239 stable nuclides with a radius and a binding energy, R_N B/ħc divided by the atomic cycles rises smoothly with Z (38 at Li, 53 at C, 82 at Ca, 100 at Z = 30, 114 at 40, 118 at 50, 128 at 60) and flattens at 135 to 136 for Z = 67 to 83 (Ho 135.7, Re 136.3, Pb 136.5, Bi 136.1; 1/α = 137.04). Times α the four values are 0.990, 0.983, 0.988, 0.992: 0.8% to 1.7% below 1. It is not the coincidence of four points; it is a plateau at about 0.99/α for the heavy stable nuclei (within 2% of 1/α from Z = 60 to the end), and the light nuclei sit far below it (D 6.6, ³He 10.5). The plateau is partly produced by mild slopes (nuclear cycles ∝ A^(4/3), atomic cycles growing faster than Z), so its height may be an accident. The value 1/α is the electron and atom rung ratio.
- **The Dirac pole in registration terms.** The atomic cycles are tan(θ/2). The hyperfine factor has its pole at γ = ½, θ = 60° (Z = 118.7), where the atomic order registers tan 30° = 1/√3 = 0.57735 cycles, which equals sin ξ for the floor's lean ξ = arcsin(√3/3) = 35.26°; the critical charge (Zα = 1, Z = 137.04) is exactly one registration (tan 45°). The heavy group (θ = 29° to 37°) is about half-way to the pole; p − 3 is 1.05, 1.49, 2.04, 2.14 for the four ions and would be 4.4 at 45°, 18 at 55°, 98 at 59°. Whether 60° and 1/√3 here relate to the floor's π/3 cone angle and lean is not established.
- **θ near 36°.** Pb and Bi are at 36.75° and 37.28°; Zα = sin 36° (π/5, the 600-cell edge arc) would be Z = 80.55. Two points against the framework angle, chosen after seeing them.
Ledger entry 9 records the plateau's 1% to 1.7% as a near neighbour.

## What this suggests, as reading and not result
- The light group is the **far-order regime**: the atomic order is 10⁴ to 10⁵ from the nucleus in size, 10² to 10³ in registration cycles, 70 to 137 times the electron Compton rung. The coupling is the weak far-field one (1e-7), scale-free, and the exponent is the integer 3.
- The heavy group is the **adjacent-order regime**: the atomic order is 1.65 to 2 times the electron Compton rung, a third of a registration, 115 to 152 times the nuclear size (cycles 136 times). The exponent runs, the nuclear order's internal structure (a magnetization distribution, deformation) enters, and the electron's own rung is a neighbour.
- So the exponent's running is a measure of how near the atomic order is to its neighbouring rungs, and the heavy ions are the ones where it is adjacent to two of them (the electron Compton rung and the nuclear order). The earlier chain (adjacent orders exchange and couple strongly; far orders decouple) is the same statement in the instrument.

## Not done
The finite-size and Bohr–Weisskopf corrections that would turn the heavy group's r/A into a measurement of the nuclear order's structure; any measurement between Z = 3 and 66; the radiative lifetimes of the M1 transitions (not sourced); a test of the plateau against the nuclear liquid-drop saturation values to see whether 0.99/α is an accident; the relation (if any) of 36° and 60° to the floor's angles.

sha256: *two_groups.py 0bb629d2c4b20296e41243315dd211f08036780b8bfc8a1cf1d02b2a49922d3e; *two_groups.out a8f80c01d1b1b5bc9c4220d6dbe552632fbabe4d23910e1077d36226f9205d75; *two_groups_extra.py 199561e4bd92cde99c343f681eaccaf3f3ff8eb6f2a1b84f697e5272bca923fe; *two_groups_extra.out dd10976173431c28eb4979281b9d354fe69f7a47a5a5e076ee4267e0964cd7c0.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` (a few seconds each).
