# Map — functions that produce known products (2026-10-28)

Frame (the human's): the work is building algebra, i.e. functions that do things and produce known products. Parameters (α, m_p/mₑ) are allowed as inputs; a result is how many independent products a function set gives per parameter. Translation, not derivation.
Supporting scripts and raw outputs for the numbers below are in `explore/` (`positronium_map`, `hydrogen_map_bc`, `lithium_map`, `ptable_sample`, `ptable_solids`, `alpha_candidates`, `alpha_families`) and were uncommitted when this file was committed.

## The core function: BC
cycles(R, E) = R·E/ħc (1 cycle = 2π nats = 12 radits = 30 ticks). Evaluated at different arguments and couplings g, it reproduces known products:
| Product | Argument | Value |
|---|---|---|
| Compton registration | R = ƛ | 1 cycle (2π nats = 9.0647 bits), mass-independent |
| 511 keV annihilation photon | R = λ/2π | 1 cycle each; 2γ: 2 in, 2 out |
| Bound-state delta | R_n E_n for any Coulomb level | π·Zα nats = Zα/2 cycle; hydrogen 0.0229253092 nats; n-independent |
| Bekenstein–Hawking entropy | R = r_s, E = Mc² | 4πGM²/ħc nats (exact) |
| Hawking quantum | R = r_s, E = k_B T_H | E_H·r_s = ħc/4π: 1/(4π) cycle = 0.5 nat for every mass (solar-mass hole T_H = 6.1700738e-8 K) |
| de Sitter horizon entropy | R = c/H₀ (67.4), critical density | (R/ℓ_P)²/2 = 3.6055617e121 cycles = π(R/ℓ_P)² = 2.2654412e122 nats |
| Cosmological-constant ratio | same | ρ_Λ/ρ_P = (3Ω_Λ/8π)(ℓ_P/R)², factor 0.0818 against 1/N for Ω_Λ = 0.685 |
| Positronium rest energy, binding, 1S–2S | a_Ps = 2ƛ_e/α = 1.0583544e-10 m | 4/α = 548.14399633, α/2 = 0.00364867628, 3α/8 = 0.00273651 cycles |
| Para-positronium decay | Γ = c·4π r_e²·\|ψ(0)\|² | α⁵ω_e/2 = 8.0325029e9 s⁻¹, τ = 0.12449 ns (rule assumed, equality exact) |
| Ortho-positronium | measured 142.05 ns | 0.060050 α⁶ (leading 0.061512 α⁶) |

Other functions: inner gƛ, outer ƛ/g with inner × outer = ƛ² (EM electron: r_e = 2.8179403e-15, ƛ_e = 3.8615927e-13, a₀ = 5.2917721e-11 m; gravity proton: 1.2421158e-54 m, 2.1030891e-16 m, 3.5608464e22 m); the exponent rule k = 3 + N (3 = dimension of the overlap |ψ(0)|² ∝ α³, N = number of photon crossings: hyperfine and virtual annihilation α⁴, 2γ α⁵, 3γ α⁶).

## Products sort by what they need
1. Anchors only (ħ, c, G): Compton, photon, Hawking quantum, S_BH, S_dS, the 10¹²² ratio.
2. A coupling g (α): the atomic rows, the Z_eff·α/2 rungs of every element.
3. Imported counts (not yet from the algebra): the QED coefficients 1/3 + 1/4 = 7/12 (hyperfine), 1/2 (para), 2(π²−9)/(9π) (ortho), and the 4π r² in the rate rule.

## Corrections made while reviewing
- The −κ²/12 in the lattice dispersion E = 8J₂(κ)/κ comes from the Bessel expansion, 12 = 4(ν+1) with ν = D/2 = 2 in four dimensions (2(D+2) = 12). It does not need the 12 neighbours. The earlier claim that the static count 12 enters as the first correction was wrong.
- The three appearances of 4π are not one sphere-flux factor. In e²/(4πε₀) it is the solid angle of Gauss's law (a convention about where it sits: absent in Gaussian units). In Hawking, 1/(4π) = (1/2π)(1/2): 2π is the thermal period (Unruh) and ½ comes from κ = c²/(2r_s). In the singlet decay rate, 4π = 4·π: 4 is the spin multiplicity (1 of 4 states annihilates to 2γ; spin-averaged σv = πr_e²c) and π is the Dirac cross-section. Only the first is a solid angle.

## Target for a screening function (products waiting for a function)
Z_eff,k = n√(E_k/Ry) with n the outermost occupied shell (shell-level assumption). Successive ratios:
- Alkali Z₂/Z₁ (core removal): Li 1.8728, Na 2.0222, K 2.0247, Rb 2.0449, Cs 2.0322 (Fr: one stage in the file). Z₃/Z₂: 1.2308 (Na), 1.2034 (K), 1.2108 (Rb), 1.2336 (Cs).
- Alkaline earth Z₂/Z₁ (second valence electron): Be 1.3976, Mg 1.4023, Ca 1.3936, Sr 1.3916, Ba 1.3854, Ra 1.3865 (√2 = 1.4142). Z₃/Z₂ (core removal): 1.4535, 1.5392, 1.5532, 1.5775, 1.6094.
The alkali ratio is about 2.02–2.05 for n ≥ 3 and not monotone; the alkaline-earth ratio is flat near 1.39. Data source: PeriodicTableJSON.json (Wikipedia-derived, not checked against NIST).

## Open
The value of g at the electron step (α), the proton step (1836.15), the per-level composition rule, and functions for the imported coefficients in class 3.
