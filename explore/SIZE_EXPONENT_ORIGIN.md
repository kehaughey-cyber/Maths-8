# Where the exponent 3 of the size dependence comes from (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `SIZE_AND_MULTIPLET_RESULTS.md`. Script `explore/e_series_chain_origin.py`, raw output `explore/e_series_chain_origin.out`. The human allowed tuning "for understanding as long as we can figure out where it comes from"; the tuned couplings below are tuned openly, to see which exact value each exponent needs. Nature's exponent is p = 2.99993 (³He⁺/H, secondary frequencies).

## A correction to what the previous note compared
The Z³ is an exponent of the **absolute** energy at **fixed** nuclear and electron moments. The chain of the previous note computes a dimensionless mutual inductance between rings that both scale with their layer. Those are different quantities. At a fixed physical moment, the current of a ring of radius R_A in lattice units is j = μ_A / (q c R_A area_lat) ∝ 1/R_A (tick = R/c, the lab's declared anchor). The phase it sets on a fixed inner ring is M_lat · j, and the inner ring's energy shift is its own fixed quantum times that phase. So the absolute energy falls with the exponent **p_E = p_M + 1**, where p_M is the chain's exponent. This is an argument from units, not a lattice computation. On it, nature's p_E = 3 corresponds to a chain exponent p_M = 2, not 3.

## 1. The lattice link field is Maxwell on S³ (`e_series_chain_origin.out` §1)
The face-energy operator S_Fᵀ S_F (119 zero modes, the gradients) has transverse levels at 0.5278640, 1.1458980, 1.9331897, 2.8074176, 3.6368399 with multiplicities 6, 16, 30, 48, 70, which are exactly 2k(k+2) for k = 1 to 5: the multiplicities of the coexact 1-forms on the unit S³, whose curl² eigenvalues are (k+1)². The ratios λ/(k+1)² are 0.1320, 0.1273, 0.1208, 0.1123, 0.1010: a lattice-dispersion factor, falling with k. The lowest level is exactly 5 − 2√5 (0.5278640450), multiplicity 6 (the su(2)_L ⊕ su(2)_R invariant forms). Calibrating the lattice spacing on k = 1 gives a_eff = √(λ₁/4) = 0.3633 (the 600-cell edge chord is 0.6180).

## 2. The exact couplings (§2)
A transverse mode of level λ falls across layers with cosh γ = 1 + μλ/(2μ_r), so the coupling for a far-field exponent p_M with step q is μ_r/μ = λ₁ / (2(cosh(p_M ln q) − 1)).
- q = φ, p_M = 2: **μ_r/μ = λ₁ = 5 − 2√5 = 0.5278640 exactly**, because cosh(2 ln φ) = 3/2. Then γ = 2 ln φ and each layer multiplies the coupling by φ⁻².
- q = φ, p_M = 3: μ_r/μ = (3φ − 4)/4 = 0.2135255, because cosh(3 ln φ) = √5.
- Other steps: √φ gives 2.236 (p_M = 2) and 0.970 (p_M = 3); φ² gives 0.1056 and 0.0330.
Solver check (K = 8): at μ_r/μ = λ₁ the exponent p_M(c) runs 3.243, 2.619, 2.281, 2.124, 2.053, 2.011 (layer 5; the last layers feel the free end) toward 2; at (3φ − 4)/4 it runs 4.347, 3.538, 3.190, 3.066, 3.024, 3.007 toward 3.

## 3. A natural coupling, and the continuum limit (§3)
For an isotropic lattice with spacings a_eff (angular) and Δt = ln q (radial, log-radius), the radial-to-angular plaquette weights are in the ratio (a_eff/Δt)², so μ_r/μ = (a_eff/Δt)², which at q = φ is 0.570 (8% above the exact λ₁ above). The exponent of mode k is then p_M = arccosh(1 + λ_k Δt²/(2a_eff²))/Δt, which tends to √λ_k/a_eff: 2, 3, 4 in the continuum for k = 1, 2, 3 (curl eigenvalues k + 1):

| step q | Δt | μ_r/μ | p_M (k = 1) | **p_E = p_M + 1** | p_M (k = 2) | p_M (k = 3) |
|---|---|---|---|---|---|---|
| φ | 0.4812 | 0.570 | 1.930 | **2.930** | 2.743 | 3.426 |
| √φ | 0.2406 | 2.280 | 1.981 | **2.981** | 2.888 | 3.704 |
| φ^(1/4) | 0.1203 | 9.118 | 1.995 | **2.995** | 2.932 | 3.794 |
| e^0.05 | 0.0500 | 52.79 | 1.999 | **2.999** | 2.944 | 3.822 |

p_M(k = 1) = 2 − Δt²/3 + …. So the lowest mode gives p_E = 3 in the limit of a continuous scale axis, and the φ-step discretization lowers it by 2.3% (2.930) at q = φ. Nature's 2.99993 sits at the continuum value.

## 4. The volume account (§5)
The n-fold geodesic subdivision of the 600-cell has V_n = 120 + 720(n−1) + 1200·C(n−1,2) + 600·C(n−1,3) points (built and counted for n = 1, 2, 3: 120, 840, 2760, equal to the formula). The local growth exponent is 2.807, 2.934, 2.967, 2.980, 2.987, 2.9905, 2.9929 for n = 2 to 8, tending to 3 (V_n ~ 100 n³). A unit-normalised state spread over the carrier has density ∝ 1/V ∝ size⁻³ at a fixed inner point, which is the contact coupling's size dependence. The floor's intrinsic dimension (ball-count growth, spine node 25) is 2; the exponent here is the ambient dimension 3 (nodes 42/43), not that 2.

## Where the 3 comes from
Two accounts give 3 and agree with the measurement:
1. **Field propagation:** the lowest transverse mode of the carrier (the six invariant 1-forms, curl eigenvalue 2) falls across scale with exponent 2 in the chain, and a source of fixed moment contributes one more power through its current (∝ 1/R): 2 + 1 = 3. For the k-th mode the same account gives k + 2.
2. **Volume:** a state normalised over a 3-dimensional carrier has density ∝ size⁻³.
For k = 1 on S³ these coincide (k + 2 = dim S³ = 3). Whether the coincidence has a reason, or is one, is not resolved here: for the k = 2 mode the first account gives 4.

## What this does and does not establish
- **Established by computation:** the lattice spectrum and multiplicities (§1); the exact tuned couplings and their solver checks (§2); the dependence on step size in §3 (given the isotropic rule); the volume growth (§4).
- **Argument, not computation:** the +1 from the fixed-moment source (needs tick ∝ size); the isotropic rule μ_r/μ = (a_eff/Δt)² (a hypercubic-lattice rule applied to a 600-cell lattice with a calibrated spacing; the exact coupling that gives p_M = 2, λ₁, is 8% from it, so the rule is approximate at the 8% level); that the contact coupling is the relevant one (the instrument's action couples charge current, not spin magnetization, so the Fermi contact term itself is not built).
- **The measured exponent was taken over one factor of 2 in size** (Z = 1 to 2, secondary data). A test of constancy over a longer range needs more hydrogen-like hyperfine values (Li²⁺ and beyond), not sourced here. The chain's exponent depends on separation in the near field (3.24 falling to 2.0 at the λ₁ coupling), so a constant 3 over a long range would favour the continuum reading.
- **Tuning:** nothing has been tuned to make the chain give 3 in the sense of a fit. The exact couplings in §2 are the values each exponent requires; the one the lattice's own geometry points to (§3, 0.570) is within 8% of the one that gives 2 exactly.

## Noticed after computing, not claimed
- p_E at φ steps, 2.930, is 2.3% below 3 purely from the discretization of scale (Δt²/3 in p_M). It is added to the 2% ledger (entry 8) with that caveat; the ledger asserts no common cause.
- λ₁ = 5 − 2√5 and the exact couplings are numbers of the golden field (cosh(2 ln φ) = 3/2, cosh(3 ln φ) = √5).

## Not done
A hydrogen-like series beyond Z = 2; the spin-magnetization (contact) coupling in the instrument's action; the inner-ring-in-outer-sphere geometry with a point-like inner ring; a derivation of the radial coupling from the lattice rather than the isotropy rule.

sha256: *e_series_chain_origin.py 944c137c687fdcafa51813ef201bf8f1d9a7316583dcef70a94814714edff4f6; *e_series_chain_origin.out 77a0e5fa85b5b0a788ad704f70edca272eedf27bf366dd32cceac59882d2a9a8.
Command: `py -3 -I -X utf8 -u explore/e_series_chain_origin.py > explore/e_series_chain_origin.out` (about 13 s).
