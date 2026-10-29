# Map — the lepton-to-atom ladder, raw successive steps (2026-10-29)

Purpose (the human's): read what a level does from known data across decades, approaching the atomic level from the leptons. Same dictionary as `positronium.md` (cycles = R·E/ħc; 1 cycle = 12 radits = 30 ticks = 2π nats). This map tabulates ratios between known quantities and their logs; it proposes no rule and fits nothing.
Run: `py -3 -I -u explore/lepton_ladder_map.py > explore/lepton_ladder_map.out`. Raw output: `explore/lepton_ladder_map.out`.
Inputs (CODATA 2018): ħ, c, G, α = 7.2973525693e-3, m_e, m_μ = 1.883531627e-28 kg, m_p, m_n; m_τ = 3.16754(21)e-27 kg (relative uncertainty 6.6e-5, so every τ row carries it). Anchors for ladder positions as in positronium: Planck length, 0.05 eV neutrino (rough).

## Mass steps (raw)
| step | ratio | log₁₂ | log_φ | log_φ − nearest int |
|---|---|---|---|---|
| e→μ | 206.768282983825522 | 2.14559318 | 11.07952565 | +0.0795 |
| μ→τ | 16.8170258178521151 | 1.135814021 | 5.865175517 | −0.1348 |
| e→τ | 3477.22755325194598 | 3.281407201 | 16.94470117 | −0.0553 |
| e→p | 1836.15267344000132 | 3.024430605 | 15.61771206 | −0.3823 |
| μ→p | 8.88024336683994529 | 0.8788374255 | 4.538186406 | −0.4618 |
| p→τ | 1.89375731307648743 | 0.2569765959 | 1.326989111 | +0.3270 |
| p→n | 1.00137841930525078 | 0.0005543347705 | 0.002862502719 | +0.0029 |

Mass order is e < μ < p ≈ n < τ, so the proton and neutron sit between the muon and the tau. Every particle has exactly 1 cycle at its own Compton cut (Part A).

## The EM triple for each lepton (r = αƛ, ƛ, a = ƛ/α)
e: 2.81794032449e-15, 3.86159267724e-13, 5.2917721058e-11 m. μ: 1.36284940989e-17, 1.86759430485e-15, 2.55927651448e-13 m. τ: 8.1039859524e-19, 1.11053781155e-16, 1.52183658526e-14 m. The binding row is α/2 cycle = 0.00364867628465 at every R (hydrogen-like). Within each triple the steps are 1/α = 137.035999083695801 by definition (log₁₂ 1.98005, log_φ 10.22469, log₂ 7.09841).

## All nine lengths sorted ascending (Part D, raw step from previous)
r_τ → r_μ 16.8170258 → ƛ_τ 8.14864653 → ƛ_μ 16.8170258 → r_e 1.50886106 → a_τ 5.40052808 → a_μ 16.8170258 → ƛ_e 1.50886106 → a_e 137.035999.
The interleaving is fixed by two numbers only: m_μ/m_e ≈ 206.77 and 1/α. The steps repeat in pattern (16.817, 1.50886, 16.817, 1.50886, …) because each lepton's triple is a scaled copy of the others.

## Hadron step and the real atom
m_p/m_e = 1836.15267344000132 (ln 7.51542772, log₁₂ 3.02443061, log_φ 15.61771206). a₀/ƛ_p = (m_p/m_e)/α = 251619.016075049617. Reduced-mass hydrogen a₀ is 1.00054461702 times the infinite-mass a₀. Muonic-hydrogen Bohr radius (reduced mass) 2.84747543074570e-13 m.

## Koide (floor C2.2 touches it)
Q = (m_e+m_μ+m_τ)/(√m_e+√m_μ+√m_τ)² = 0.666660490512092, Q − 2/3 = −6.176e-6. The τ input uncertainty is 6.6e-5 relative; whether the offset sits inside that was not propagated here.

## What the table shows, without reading it
- Seen directly: two independent step sizes organise the lepton lengths: m_μ/m_e = 206.77 between charged leptons' scales and 1/α = 137.036 between each lepton's own r, ƛ, a. The τ's triple overlaps the μ's and e's: a_τ (1.52e-14 m) lies between ƛ_μ and a_μ, and a_μ (2.56e-13 m) lies below ƛ_e (3.86e-13 m).
- The base-12 and base-φ residuals above are printed so the reader can see how far each step is from an integer power. The smallest log_φ residuals among the lepton steps are e→μ (+0.080) and e→τ (−0.055); μ→τ is −0.135, and the proton rows are near half-integers. The p→n step is 1.0014 and not a ladder step. Residuals this size are not evidence of anything on their own: with spacing 1 in log_φ, a residual under 0.1 occurs for about one step in five by chance, and the τ rows carry a 6.6e-5 input uncertainty (0.00014 in log_φ).
- Not tested: whether any step ratio is a function of the others; whether the same two numbers (206.77, 137.04) appear as steps between non-lepton scales (W/Z, Higgs, quarks, nuclei). Those extensions need sourced inputs not in this repo.

## Not done / flags
- τ mass and the neutrino anchor are the weakest inputs; neutrino masses are not on the ladder.
- Quarks, W/Z, Higgs, nuclear masses and binding energies are not included.
- The proton/neutron/τ ordering shows p→n and p→τ as separate rows only because the sort is by mass.

sha256: *lepton_ladder_map.py 171191abcbf6fd39ed30d91fdd27f52db1f8167fb66e627a17cfeeaff3b13b7e; *lepton_ladder_map.out 8656baca9894b50b9973d0380e73039e67f57f7ff884eba64ee6ac00c32f6a9f.
