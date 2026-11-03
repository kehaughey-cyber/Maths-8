# Map — candidates for α (1/137.036), and what each check found (2026-10-28)

Frame: translation, not derivation. α is read as a ratio between adjacent orders (extent ratio ƛ_e/r_e = a₀/ƛ_e = 1/α; spectral ratio; phase excess per cycle). Target 1/α in [137.0359991, 137.0359992] (CODATA 2018 and 2022 differ by 6.8e-10 relative). A candidate counts only if it matches to about 1e-9; anything looser is noise at this precision (see A10).
Run: `py -3 -I -u explore/alpha_candidates.py > explore/alpha_candidates.out` (2.5 s). Raw output: `explore/alpha_candidates.out`.

| # | Candidate (where α could be) | Check | Result |
|---|---|---|---|
| A1 | α equals a single-level floor count or angle (tick, radit, ε, δ, K, κ, gap, φ/2, (φ/2)³⁰, lean, 2/15) | ratio of each in cycles to α | no. α/x = 0.219, 0.0876, 0.357, 0.206, 1.429, 0.00665, 0.0382, 0.00902, 4.21, 0.0745, 0.0547. Only ε/2π = 2.8001 α (5e-5 off, one of 11 comparisons) is close to a simple ratio; not an identity |
| A2 | noticed near-misses | relative error to 1/α | exp(2π)/4 −2.3e-2; 125κ +3.05e-4; 144−7 −2.6e-4. All ≫ 1e-9, so none is an identity. 125κ is also ~15× worse than the typical nearest miss in A10 (2e-5) |
| A3 | 1/α is a near-complete 144 = 12², deficit = floor non-closure | (1−ε/2π)^n vs 137.036/144 = 0.95164 | n = 2.401, not an integer; n = 2 gives 0.95955, 0.83% off |
| A4 | 137 hops per cycle; hop counts in the floor | 10, 30, 60, 120, 144, 1440 vs 137.036 | nearest is 144 (5.1% off). 144 is in the floor (1,440 histories = 144 ten-cycles of T) |
| A5 | α/2π is an excess in the 4π double cover (g−2) | replay of the native transit T on the 1,440 histories | 144 ten-cycles; T⁵ = antipode and T¹⁰ = identity on all 1,440. The finite carrier closes exactly, so α/2π is not a finite-carrier effect |
| A6 | α is a ratio in the relaxation (A/12) spectrum of the 600-cell graph | eigenvalues of A | 12, 9.7082(×4), 6.4721(×9), 3(×16), 0(×25), −2(×36), −2.4721(×9), −3(×16), −3.7082(×4): all in Q(√5). No ratio within 1e-6 of α or 1/α |
| A7 | α/2π is a beat of two clocks (F16-style) | smallest floor beat | 1/30 cycle = 0.0333; F16 beat 0.0354; α/2π = 0.0011614 cycle (1/861.02), 29× smaller than any single-level beat |
| A8 | coupling = (cell/wavelength)²: EM cell | cell = √α ƛ_e | 3.2987e-14 m = √(r_e ƛ_e); no floor scale equals it (lattice cell ≈ 1.5 ℓ_P) |
| A9 | dispersion deviation of the propagation wave | ledger coefficients 0.0517 k², 0.0248 (ka)² | ratios to α 7.08 and 3.40; lattice-dependent; no |
| A10 | grammar sweep (look-elsewhere calibrated) | 1,731,600 expressions: rational a/b (a,b ≤ 30) × one or two of 20 floor constants with exponents ±1, ±2; tolerance 1e-9; 1,976 decoy targets | 0 hits on α; 0 on every decoy; nearest miss 1.4e-5; typical nearest-miss scale 2e-5. No expression of that grammar equals 1/α |

## Not testable yet
- T–C beat on composite propagation waves, and propagation dispersion at higher complexity (needs an operator the repo does not hold).
- Cross-scale reinjection operator (D5) spectrum, and mixing of the 144 cycles (the floor gives no mixing weight).
- A recursion-limit sum over levels (finite carriers give algebraic numbers; a ten-digit α needs a limit).
- The alpha/photon arc of M6 (`alpha_photon.py`, `alpha_spacelike.py`): the files are not in this repo.

## Reading
Every candidate that can be checked with what the repo holds came back negative. The finite carrier is exact (A5, A6), and the two untested families both need a recursive structure.
sha256: *alpha_candidates.py dca1ea770dfd2c06f646ef0825469aecd9fb1f9099e7278445686dec3bb40494; *alpha_candidates.out 6f57191e611d09d5f536dc22baaf8693b40c2f52782c75b38b27333bfdef040e.

## Round 2 — the four families (run 2026-10-28)
Run: `py -3 -I -u explore/alpha_families.py > explore/alpha_families.out` (22 s). All parameter-free; targets 1/α, 2π/α, π/α, α/2π.

| Family | Check | Result |
|---|---|---|
| F1 T–C beat | joint action of T and all 480 C = L_a R_b (a order 5, b order 6) on the 1,440 histories | all 480 commute with T; every C has cycle length 30 on histories; max cycle length over all T^i C^j is 30, so every beat is a multiple of 1/30 cycle. Smallest beat 0.03333 cycle vs α/2π = 0.0011614 (ratio 28.70). Negative |
| F2 propagation dispersion | 4D icosian lattice, physical sector (k'=0), 400 directions | the 60 pairs form a spherical 11-design, so E = 8 J₂(κ)/κ = κ(1 − κ²/12 + κ⁴/384 − …); lattice agrees to 1e-13 at κ ≤ 1, 4e-10 at κ=2, 6e-6 at κ=5. β = 1/12 (numerically 0.0833333307). Band top κ* = 2.29991033, E_max = 1.43970293 (the §33 top stationary energy 1.4397); first zero shell j₂,₁ = 5.1356223. None of these ratios is α-related (x/α = 11.42, 197.3, 315.2, 703.8, 306.0, 85.78). Speed (mean eigenvalue of vmat) at internal label \|k'\| = 0, 0.5, 1, 2: 1.0, 0.969, 0.880, 0.577. Negative |
| F3 reinjection and mixing | random-exit chain P on the 1,440 histories; M_w = (1−w)T + wP; chain coarse-grained onto the 144 ten-cycles | P moduli 1, 0.809(×4), 0.5393(×9), 0.3090(×4), 0.25(×32), 0.2060(×9), 0.1667(×36), 0; (φ/2)³⁰ = 1.7327e-3, gain 1.0017357 (ratio to α 0.237). Largest \|λ\| below 1 of M_w is √(1−w) for w < 1 (0.957427 = √(11/12) at w = 1/12; 0.912871 at 1/6; 0.707107 at 1/2) and φ/2 at w = 1. Coarse-grained chain on the 144 cycles: second eigenvalue exactly 1/3 (at least 7-fold). No α. The floor gives no mixing weight, so w is not fixed. Negative |
| F4 recursion limits | 70 sums/products (geometric, partition, Euler, θ₃, Lambert, σ) over 10 contraction ratios (φ/2, 1/φ, 1/φ², gap, (φ/2)^5,10,12,30, 1/12, 1/144); 3,671,640 expressions; 1,500 decoys per target | 0 hits for 1/α, 2π/α and π/α; decoy mean 0; nearest misses 1e-6 to 1e-5. Negative |

sha256: *alpha_families.py 4d8eed2d9bc5a645d30ae0692a9ae99b4ad4a4e43a7abaee8cde45cc7315769d; *alpha_families.out 1d64d7c56d94c3027b7557b52c0fddbe0cfa8819171f224fdf53757eadaf3914.
**Not covered:** the internal-momentum sector of F2 (only its speed was sampled); the rule for what one recursion level does to a coupling (composition across levels), which is a property of the universe still to be found, not an input from anyone; the M6 alpha/photon arc (files not in this repo).
