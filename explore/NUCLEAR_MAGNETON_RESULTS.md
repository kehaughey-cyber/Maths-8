# The nuclear magneton: what it is, what it does, its symptoms (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Computed from sourced numbers only (`explore/data/moment_benchmark_sourced_values.txt`, the saved IAEA table, exact SI constants); textbook relations used from memory are marked in the output. Script `explore/nuclear_magneton_symptoms.py`, raw output `explore/nuclear_magneton_symptoms.out`. Nothing fitted.

## What it is
μ_N = eħ/(2 m_p) = 5.0507837392e-27 J/T, equal to μ_B divided by m_p/m_e = 1836.152673426. It equals e·c·ƛ_p/2 with ƛ_p = ħ/(m_p c) = 2.1030891e-16 m (ratio 0.9999999999999999): the magnetic moment of one charge e circling at the speed of light on the proton's reduced Compton radius (current e c/(2πr) times area πr²). It is the unit moment of the proton's order, as the Bohr magneton is for the electron's. Dirac's point proton (g = 2, spin 1/2) would have exactly 1 μ_N.

## What it does: precession in a field
A nuclear moment μ in a field B precesses at ν = |μ|B/(Ih) and has two energy levels split by hν (spin 1/2). From the table: proton 42.577479 MHz/T (the CODATA value gives 42.5774785), neutron 29.164693, deuteron 6.535903, ³He 32.436045, ¹³C 10.707746, ¹⁴N 3.076273, ¹⁵N 4.315255, ¹⁹F 40.069244 MHz/T. At 1 T the proton splitting is 1.76e-7 eV, 1.5e5 times smaller than kT at 298 K.

## Symptoms that the nucleus is not a point particle
- Proton: measured 2.792847351 μ_N against 1 for a point Dirac particle (g_p = 5.5856947).
- Neutron: no charge, yet −1.9130427 μ_N. A neutral particle with a moment has charged parts that do not cancel.
- Ratio μ_n/μ_p = −0.68498. The textbook quark picture (from memory, constituent quark mass m_p/3) gives μ_p = 3, μ_n = −2, ratio −2/3: the measured values are 6.9% and 4.3% below it.

## Symptoms in the gram (¹³C, taken as 1.06% of the atoms)
5.32e20 ¹³C nuclei, each 3.5475e-27 J/T. All aligned would give 1.887e-6 J/T (the expressed ceiling). In 1 T at 298.15 K the net moment is 1.626e-12 J/T, a fraction 8.6e-7 (at 4.2 K, 6.1e-5). The weak-field nuclear Curie susceptibility is 1.63e-13 emu/g, about 3.3e-7 of the diamond orbital diamagnetism (−4.9e-7 cm³/g, a secondary unverified value). The nuclear moments are present and measurable (NMR resolves them) and their bulk effect in the gram is a millionth of an already tiny one.

## Ablating the size scaling against the measured moment ratio
The instrument gives moment per charge ∝ ρ^(2g−1) when the geometry scales as ρ^g (g = 0: size independent of the tick; g = 1: size follows the tick). For proton over electron (ρ = 1/1836.152673426) the table in the output gives model/measured |μ_p/μ_e| = 1.2e6 (g = 0), 658 (g = 0.5), 15.4 (g = 0.75), **0.358 (g = 1)**, 8.4e-3 (g = 1.25), 2e-4 (g = 1.5). The exponent that reproduces μ_N/μ_B exactly is g = 1.0000 (by construction of the anchor); the one that reproduces |μ_p/μ_e| is g = 0.9317, the difference being ln(μ_p/μ_N)/(2 ln(m_p/m_e)) (0.06833, and 0.06825 with μ_e/μ_B). So among scalings of this form, only size following the tick reproduces the magneton; nature's measured moment sits 6.8% in the exponent from it, which is the proton's internal structure (the factor 2.79).

## Not done
The instrument's moment is defined as current × area. The physical definition is the energy response, μ = −∂E/∂B. The precession frequency and the splitting hν are that response, and reading them out of the instrument (the frequency shift of a ring mode under an imposed uniform link flux) is the natural internal check and the route to a Larmor readout. Not built. The hyperfine splitting (a nuclear moment acting on its own electron) is the measured counterpart for the inter-order coupling κ_r; not sourced or run.

sha256: *nuclear_magneton_symptoms.py d9b3bec9ef78a960e03e6c1c8fff7a1bc004dbda8d842a8e24caab31ed31a6a7; *nuclear_magneton_symptoms.out 4cd104965070c73c72379626d2335d1c6f51306f75d960cc93ea062b6d89991a.
Command: `py -3 -I -X utf8 -u explore/nuclear_magneton_symptoms.py > explore/nuclear_magneton_symptoms.out`.
