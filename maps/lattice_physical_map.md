# The lattice, with physical units, on our size axis (2026-10-30)

Source: `C:\Users\Dad\OneDrive\Desktop\Optimus Prime\lattice(1).html` (the 600-cell, live: 120 vertices, 720 edges, nine w-shells, the tick q → g₅·q·g₆ with four 30-clocks and the fold at t = 15, a tower of scales at radii φ^k, a BFS wave from a vertex). Run: `py -3 -I -X utf8 -u explore/lattice_physical_map.py > explore/lattice_physical_map.out` (raw output there; sha256 below). Nothing is fitted and no lattice feature is adjusted to a rung.

## The lattice, rebuilt cold (matches the html's own header)
120 vertices, 720 edges, 12 neighbours per vertex, edge chord 1/φ = 0.618034 and edge arc 36° on the unit S³ (S³ radius / chord = φ). Graph distance from a vertex: 1, 12, 32, 42, 32, 1 (diameter 5). w-shells: 1 (w = ±1), 12 (±φ/2), 20 (±½), 12 (±ψ/2), 30 (0), total 120. The tick q → g₅·q·g₆ (orders 5 and 6) has four cycles of length 30; after 15 ticks a vertex sits at its antipode (dot = −1), the fold.

## The physical assumption (declared, non-discriminating)
Floor nodes 17/18/33: anchor edge, tick and rate to the Planck scale. Here the edge at tower scale k = 0 is ℓ_P = 1.616255×10⁻³⁵ m and one tick is ℓ_P/c = 5.391×10⁻⁴⁴ s, so the wave advances one edge per tick at c by construction (node 33 says this reproduces c by construction). At scale k: edge = ℓ_P φ^k, S³ radius = φ × chord edge, tick = edge/c, the 30-tick cycle = 30 ticks, the fold = 15 ticks, the antipode is reached after 5 ticks. The step φ per scale is the html's choice (the floor's D6 keeps several meanings of "scale" distinct: updates, accumulated phase, causal lag, harmonic order, organization depth, carrier extent, mesh).

## Rungs from our maps placed on the tower (k = log_φ(R/ℓ_P), rung read as one edge; subtract 1 to read it as the S³ radius)
| rung | R (m) | k | nearest scale, offset | tick if edge (s) | 30 ticks (s) |
|---|---|---|---|---|---|
| τ Compton length | 1.1105e-16 | 90.1345 | 90, +0.1345 | 3.704e-25 | 1.111e-23 |
| proton Compton length | 2.1031e-16 | 91.4616 | 91, +0.4616 | 7.015e-25 | 2.105e-23 |
| nucleon r_p (CODATA 2022) | 8.4075e-16 | 94.3413 | 94, +0.3413 | 2.804e-24 | 8.413e-23 |
| muon Compton length | 1.8676e-15 | 95.9998 | 96, −0.0002 | 6.230e-24 | 1.869e-22 |
| ¹²C charge radius (IAEA) | 2.4702e-15 | 96.5809 | 97, −0.4191 | 8.240e-24 | 2.472e-22 |
| electron Compton length | 3.8616e-13 | 107.0793 | 107, +0.0793 | 1.288e-21 | 3.864e-20 |
| C⁵⁺ 1s radius a₀/6 | 8.8196e-12 | 113.5806 | 114, −0.4194 | 2.942e-20 | 8.826e-19 |
| Bohr radius a₀ | 5.2918e-11 | 117.3040 | 117, +0.3040 | 1.765e-19 | 5.295e-18 |
| diamond C–C bond | 1.5445e-10 | 119.5299 | 120, −0.4701 | 5.152e-19 | 1.546e-17 |
| diamond lattice constant | 3.5668e-10 | 121.2692 | 121, +0.2692 | 1.190e-18 | 3.569e-17 |
| radius of 1 g of diamond | 4.0808e-3 | 155.0438 | 155, +0.0438 | 1.361e-11 | 4.084e-10 |
| Hubble radius c/H₀ (order of magnitude, recalled) | 4.4e26 | 293.9645 | 294, −0.0355 | 1.468e18 | 4.403e19 |

Planck length to the Hubble radius: 293.964 tower steps; to the radius of 1 g: 155.044.

## What the placement shows
- **No common offset.** The fractional parts of k are 0.135, 0.462, 0.341, 1.000, 0.581, 0.079, 0.581, 0.304, 0.530, 0.269, 0.044, 0.964. Their mean resultant length is 0.262 (1 = identical offsets); twelve independent uniform values reach that or more with probability 0.45 (Monte Carlo). The rungs do not sit at a common offset in the tower, and a different anchor (ℓ_P × s) would not change that. The rungs are not independent (three are masses; a₀ = ƛ_e/α), so the probability overstates any clustering.
- **One near-integer entry, noticed and not claimed.** The muon Compton length is at k = 95.999805, offset −1.95×10⁻⁴ from 96 (the uncertainty on k from G is 2.3×10⁻⁵, so it is 8.5σ from exactly integer; from the muon mass 5×10⁻⁸). It belongs to the reduced Compton length with ℓ_P = √(ħG/c³) as anchor; the unreduced 2πƛ shifts k by 3.819. The chance that one rung lands within ±0.0002 of an integer is 0.0004; for any of 12 rungs 0.005; allowing five natural anchors (ℓ_P, 2πℓ_P, ℓ_P/√(8π), ℓ_P√(4π), ℓ_P/2π) about 0.02. This is the only near-integer entry in the table.
- **The ends.** The Hubble radius is at k = 293.96 and the gram at 155.04, both near integers, but the Hubble radius is known only to ~8% (±0.16 in k) and the gram's radius depends on the crystal phase (+0.06 for graphite), so neither is significant.
- **Tick scales (raw).** The tick at the nucleon rung is 2.80×10⁻²⁴ s, and 30 ticks there are 8.41×10⁻²³ s; ħ/(m_p c²) is 7.0×10⁻²⁵ s. At the Bohr radius, one tick is 1.77×10⁻¹⁹ s and 30 ticks are 5.30×10⁻¹⁸ s. No physical process is identified with them here.

## Status
A placement, not a derivation. The anchor is an assumption (non-discriminating); the φ step per scale is the html's; the lattice's internal structure (counts, clocks, fold) is exact mathematics. The map shows that, on this anchor, the known rungs do not fall on one lattice offset, and that the lattice supplies no length beyond ℓ_P φ^k.

sha256: *lattice_physical_map.py f61d384e3d377618400303a818def88fe6caa5598684433e5a797b38cfdbca59; *lattice_physical_map.out 0a424268d43aac012f4648aaf4854503d5dfa5715d49a1953a748655279dca49.
