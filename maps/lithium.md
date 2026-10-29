# Map — lithium through the positronium/hydrogen dictionary (2026-10-28)

Second entry of the map of maps. Same dictionary: cycles = R·E/ħc (1 cycle = 12 radits = 30 ticks = 2π nats), position on the length ladder (Planck length → Hubble radius, 60.93 decades / 56.46 powers of 12), floor reading. Run: `py -3 -I -u explore/lithium_map.py > explore/lithium_map.out`.
Sourced inputs only: Wikipedia "Lithium" infobox (ionization energies 520.2 / 7298.1 / 11815.0 kJ/mol, lattice constant 350.93 pm per Arblaster 2018, heats of fusion 3.00 and vaporization 136 kJ/mol, melting point 453.65 K); CRC work function 2.9 eV (via Wikipedia "Work function", no uncertainty); cohesive energy 1.66 eV (experimental, ZPE-corrected, arXiv 2602.16679); Fermi energy 4.74 eV (Ashcroft–Mermin free-electron, via HyperPhysics). Ionic and valence radii come from the measured ionization energy through a hydrogenic effective charge Z_eff = n√(IE/Ry); nothing is fitted to another quantity.

| Row | R (m) | Cycles | In units of α/2 | R position (decades / p12 above l_P) |
|---|---|---|---|---|
| Li²⁺ 1s (IE3, R = a₀/3) | 1.7639e-11 | 0.0109462620 | 3.000064 | 24.038 / 22.274 |
| Li⁺ 1s (IE2, Z_eff = 2.3578) | 2.2443e-11 | 0.0086029868 | 2.357838 | 24.143 / 22.371 |
| Li 2s (IE1, Z_eff = 1.2590) | 1.6813e-10 | 0.0045936671 | 1.258996 | 25.017 / 23.182 |
| Solid, cohesive 1.66 eV | 3.0391e-10 (nearest neighbour) | 0.0025566586 | 0.700709 | 25.274 / 23.420 |
| Solid, work function 2.9 eV | 3.0391e-10 | 0.0044664518 | 1.224129 | same |
| Solid, Fermi energy 4.74 eV | 3.0391e-10 | 0.0073003385 | 2.000818 | same |
| Solid, heat of vaporization | 3.0391e-10 | 0.0021709123 | 0.594986 | same |
| Solid, heat of fusion | 3.0391e-10 | 4.7888e-05 | 0.013125 | same |
| Solid, kT at melting point | 3.0391e-10 | 6.0209e-05 | 0.016501 | same |
| Solid, kT at 300 K | 3.0391e-10 | 3.9816e-05 | 0.010912 | same |

## Reading
- The dictionary carries over unchanged. Every rung is a number times hydrogen's α/2: the three ionization stages are 3.000, 2.358, 1.259 times α/2 (Z_eff·α/2), and the solid's energies sit between 0.011 and 2.0 times α/2 at the nearest-neighbour distance. The Li²⁺ check (IE3 = 1.000021 × 9 Ry) shows the hydrogenic core is exact.
- Lengths: the atom-to-lattice step from the 2s radius to the nearest neighbour is a factor 1.808 (0.257 decades); nn/a₀ = 5.743.
- Floor reading (reading only): shell capacity 2n² (hydrogen SO(4), spine C4.1), so Li is a closed 1s² core plus one open registered state in the 2s shell, a spin-1/2 doublet (the spinor 2 of 2I).
- The thermal row is small: kT at 300 K is 0.011 of α/2 at the same radius, about 1% of the binding.

## Coincidences, not claims
- Fermi energy at nn is 2.0008 × α/2, i.e. E_F·nn/ħc ≈ α, 0.04% off. It follows from the lattice constant being 6.63 a₀ and the electron-gas k_F = 3.898/a (the product reduces to 13.16·a₀/a = 1.984); it is a geometry accident of lithium's lattice, not a relation.
- IE3/IE2 = 1.618915, 0.055% above φ. Screening-dependent, no mechanism, one of three ratios.

## Not done
- No line spectrum, hyperfine or Li-7 rest-mass row (not in the sourced set).
- Solid values beyond the Wikipedia infobox are a single source each.
- The hieroglyph column for lithium is only the shell reading above.
sha256: *lithium_map.py 64a2862960875fafb2a014ee5f0645c3c85398c8dd258c8729d293ac5e19a563; *lithium_map.out 6a677756aa67526a10031673631e1273b4005910d8e56c4a4272f2820e5e6d14.
