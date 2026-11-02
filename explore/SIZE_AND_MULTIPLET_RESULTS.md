# Giving the rings a spin multiplet and a size: the multiplicity, nature's size exponent, and what a chain of nested copies gives (2026-11-02)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `HYPERFINE_SERIES_RESULTS.md` ("Where this points"). Scripts: `spin_multiplet.py`, `e_series_chain.py`, `e_series_chain_spectrum.py` (raw `.out` beside each). Nothing fitted. Sourced as before (hyperfine frequencies secondary; m_e/u recalled, 1e-3 level).

## 1. The multiplicity is exact angular-momentum algebra (`spin_multiplet.out`)
The instrument's co/counter-circulating ring difference is the diagonal energy difference between the electron aligned and anti-aligned with the fully polarised nucleus: E(aligned) − E(anti) = A I. The level splitting between F = I + ½ and F = I − ½ is A(I + ½). Building the electron-spin ⊗ nuclear-spin operator H = A s·I and diagonalising it, the ratio of the true F-splitting to the aligned/anti-aligned difference is 2.00000, 1.50000, 1.33333, 1.25000, 1.20000, 1.14286 for I = ½, 1, 3/2, 2, 5/2, 7/2: exactly (2I+1)/(2I), as the hyperfine note found missing.

With it, the instrument route (splitting linear in the nuclear ring's moment) gives deuterium over hydrogen as (μ_d/μ_p) × 0.75 × 1.000817 (reduced mass) = 0.230447, against 0.230487 measured: 1.7e-4. The multiplicity is no longer a gap.

## 2. The size dependence nature shows
Removing the moment ratio, the multiplicity and the reduced-mass factor from the measured ³He⁺/H ratio (6.100827 against 0.762641) leaves 7.9996 = Z^p with Z = 2: **p = 2.99993**. So the electron-order size dependence of the coupling is an exponent of 3 (the density |ψ(0)|² ∝ (Z/a₀)³), measured to 2e-5 (secondary frequencies; the 2022 Penning-trap value differs by 1.4e-10 and does not matter).

## 3. What a chain of nested copies gives (`e_series_chain.out`, `e_series_chain_spectrum.out`)
Layers 0..K, each the 600-cell link system (face energy μ Σ(1 − cos F), μ = 5.6427), joined by radial links and radial plaquettes with strength μ_r (isotropic when μ_r = μ). A unit current on the decagon of cycle 0 in layer 0 sources the static link field (field propagator only; the matter's own stiffening is left out); M_c is the circulation through the same ring in layer c. If each layer is larger by a factor q, then M_c ∼ q^(−p c); with q = φ (the lab's declared step) the exponent is p = γ/ln φ with γ_c = ln(M_c/M_{c+1}).

Isotropic (μ_r = μ), K = 8: γ_c = 1.2513, 1.0247, 0.8813, 0.7998, 0.7532, 0.7151 for c = 0 to 5, so p = 2.60, 2.13, 1.83, 1.66, 1.57, 1.49 (the last layers are affected by the free end). Not a fixed exponent: the fall slows with separation and tends to an exponential.
- **The far-field rate is exact.** The link lattice's face-energy operator has 119 zero modes (gradients) and lowest nonzero level λ₁ = 0.5278640 = 5 − 2√5 to seven digits, multiplicity 6 (the six invariant 1-forms of S³); the ring source has weight 0.833 of 10 on it, 1.853 on λ = 1.9332, 3.578 on 3.5563. A transverse mode falls across layers with cosh γ = 1 + μλ/(2μ_r): for μ_r = μ and λ₁, γ∞ = 0.71144 (measured 0.7151 at layer 5), p∞(q = φ) = 1.478. The near layers fall faster because higher levels carry most of the source.
- **The exponent depends on the coupling.** For K = 8 the first-pair exponent p₀ (q = φ) is 4.44, 3.90, 3.56, 3.30, 2.95, 2.60 for μ_r/μ = 0.2, 0.3, 0.4, 0.5, 0.7, 1.0; the far-field p∞ is 4.08, 3.08, 2.59, 2.05, 1.48 for μ_r/μ = 0.1, 0.2, 0.3, 0.5, 1.0. Nature's 3 is reached at μ_r/μ ≈ 0.7 for the first pair and ≈ 0.2 in the far field; there is no single coupling at which the chain has p = 3 at every separation.
- **Which step would make p∞ = 3 at the isotropic coupling:** q = exp(γ∞/3) = 1.26763.

**Noticed after computing, not claimed:** √φ = 1.27202 is 0.35% above that q; with q = √φ the isotropic far-field exponent is p∞ = 2.957, 1.4% below 3. Half-integer powers of φ also appeared among the measured adjacent ratios (`E_SERIES_READOUTS_ABLATION_RESULTS.md` §4). The step √φ was looked at after the numbers were seen, the far field is one regime of the exponent, and the two observations may be unrelated. Added to `maps/two_percent_ledger.md` as a near neighbour.

**A geometric remark, with its own uncertainty:** φ − 1 = 1/φ equals the 600-cell's edge chord, so with layers of radii φ^k the radial gap equals the edge length and the isotropic choice μ_r = μ is what the φ step suggests (in the sense of the gap between spheres). In a conformal (log-radius) picture the layer spacing is ln q instead, which would make the isotropic step q = exp(1/φ) = 1.855. Which picture is right is not settled; μ_r/μ was declared, and both readings are declared choices.

## What this says about the pasted plan
- **Spin multiplet:** done as algebra; the instrument contributes the aligned/anti-aligned energy difference, the algebra supplies (2I+1)/(2I) exactly. The multiplicity now reproduces deuterium to 1.7e-4.
- **Size:** giving the second copy a size is not a label. The coupling between rings across layers is computed by the chain and falls with an effective exponent that depends on the separation and on μ_r/μ. At the natural isotropic coupling with φ steps it is 2.60 (first pair) falling to 1.48 (far field), against nature's 3.00. So the Z³ is the one open piece: the lattice gives the right kind of structure (a mode spectrum with an exact golden-field lowest level, six-fold) but not yet p = 3 without a tuned coupling or step.
- **Sphere versus flat space:** the exponential far-field is a property of each layer being a finite sphere (its lowest transverse mode λ₁). A ring much smaller than the layer that contains it, in flat space, would give a power law. The chain of identical layers does not represent a small ring inside a large sphere; that geometry is not built.

## Not done
The inner-ring-in-outer-sphere geometry (the small ring seen from a large one); the layer coupling in the conformal picture; any attempt to make the chain's step or coupling follow from the lattice; sourcing the primary hyperfine papers.

sha256: *spin_multiplet.py 973746ec72bdef949cb3173b61e48865239a49c121ef3ff0dd3f23fe744601d7; *spin_multiplet.out 2f4021f2e3cd25337d76e9d825764528ecf9dfd0490e19d0f3f1474c50abc057; *e_series_chain.py b2f65294054e2776970e97efb7918253ba99ca4528c77d426b1dd5727644506a; *e_series_chain.out c8d38676484f484b14a970678c50b7baa2e32c70513faaa8426c7f8d24ee51d2; *e_series_chain_spectrum.py aedd9b862d50ed389633973c9cfd6c004053fcace7c940fb5796bca3e5d9d6f1; *e_series_chain_spectrum.out 22bca3ba76ff4ce8435d550160ff3329fc2dbd3069c8d462f53532f44d41eb3f.
Commands: `py -3 -I -X utf8 -u explore/<script>.py > explore/<script>.out` for spin_multiplet (seconds), e_series_chain (about 20 s), e_series_chain_spectrum (about 40 s).
