# Self-energy: sourced, not computed; and what is left of the heavy-ion hyperfine splittings (2026-11-03)

Authored by Claude (Sonnet 5.5); no independent review claimed. Follows `QED_BW_HFS_RESULTS.md`. **The bound-state self-energy was not computed in this repository.** It is a one-loop all-order calculation (Dirac–Coulomb Green function, renormalization, partial-wave sum); writing it in NumPy/mpmath is a project of its own, and an approximate version would have been an assertion dressed as a computation. Instead the published all-order values were looked up and used as **sourced inputs**, clearly marked as such. `se_combine.py` / `se_combine.out` do the arithmetic; the numbers are in `data/qed_hfs_sourced_values.txt`.

## Sourcing and its limits
Both papers were read through ar5iv HTML pages by a web-fetch tool whose small model summarised the tables; the PDFs could not be decoded (a minimal local text extraction recovered only fragments). So the numbers are **secondary**, not read from the papers directly. The two sources agree with each other: α·X_total from the all-order table (arXiv physics/9705029) gives −0.01316 (Z = 67), −0.01711 (75), −0.02255 (83); the self-energy column of PRA 56, 252 (arXiv physics/9706031, Table 2) gives −0.0132, −0.0171, −0.0226, and −0.0218 for Z = 82 (interpolated by the authors). Defined relative to the Fermi energy: E_SE = x_SE·E_nr. Open convention question, inferred and not checked against the PDFs: the tabulated self-energy contains the free-electron Schwinger term α/(2π) (F(0) = 1/2), which this repository's E_nr already includes through the measured electron moment; both versions are printed, (a) as tabulated and (b) with α/(2π) removed. The difference is 0.07 to 0.08 percentage points.

## Check of this repository's vacuum polarization against the literature
Converting the first-order Uehling result of `vp_hfs.out` to the literature convention (× A (1 + BR)(1 + BW)), it is 0.00632, 0.00881, 0.01199, 0.01254 (Ho, Re, Pb, Bi) against the literature's Uehling electric + magnetic loops 0.0064, 0.0090, 0.0122, 0.0128: ratios 0.988, 0.979, 0.983, 0.980. Agreement to about 1–2% (the literature numbers are quoted to two significant figures; the Wichmann–Kroll term, −0.0001 to −0.0003, is not in either). This is an independent check of the vacuum-polarization computation, not of the self-energy.

## What is left (`se_combine.out`)
left = measured r/A ÷ [(1 + BR)(1 + BW)(1 + VP) + x_SE/A] − 1. (a) = x_SE as tabulated; (b) with α/(2π) removed; "no SE" repeats the previous note.
| ion | Bohr–Weisskopf model | (a) | (b) | no SE |
|---|---|---|---|---|
| Ho | uniform … shell bounds | −0.0058 … +0.0009 | −0.0050 … +0.0017 | −0.0148 … −0.0082 |
| Re | single particle (3 variants) | −0.0061 … −0.0076 | −0.0053 … −0.0069 | −0.0165 … −0.0180 |
| Re | uniform … shell bounds | −0.0048 … +0.0043 | −0.0041 … +0.0051 | −0.0153 … −0.0063 |
| Pb | single particle (all three) | −0.0073 | −0.0067 | −0.0193 |
| Pb | uniform … shell bounds | −0.0193 … −0.0075 | −0.0187 … −0.0068 | −0.0310 … −0.0194 |
| Bi | single particle (3 variants) | −0.0092 … −0.0002 | −0.0086 … +0.0005 | −0.0210 … −0.0122 |
| Bi | uniform … shell bounds | +0.0094 … +0.0221 | +0.0101 … +0.0227 | −0.0028 … +0.0095 |

**Reading.** With the sourced self-energy included, the remainder for the single-particle models is **−0.7% (Pb), −0.5% to −0.8% (Re), −0.0% to −0.9% (Bi)**, down from −1.2% to −2.1% without it; the self-energy (−0.85% Ho to −1.06% Bi of the point-Dirac value, of the size and sign of the earlier leftover) accounts for roughly 60% (Pb, Re) to nearly all (Bi, scaled-moment variant) of the previous gap. What remains is inside the spread of the nuclear-magnetization models (Bi moves by 0.9 percentage points with the spin g-factor alone; Re/Pb/Ho are deformed or have the moment-split uncertainty) but is **negative in every single-particle variant for Re and Pb**, so it is not clearly noise: candidates are the magnetization model, the nuclear charge-radius and moment inputs (secondary), the Wichmann–Kroll and higher-order terms, and the two uncertain conventions above. The measured splittings carry relative uncertainties of 1.6e-4 to 4.4e-4, so the measurement itself does not explain it. The Re isotope assignment and the Pb/Re/Ho wavelengths are themselves secondary.

## Not done
The self-energy is still not computed here; the PDFs were not read; the (a)/(b) convention was not settled; the magnetic Wichmann–Kroll loop is in neither source; no screening, no deformed nuclear model for Ho and Re. The result is arithmetic on sourced numbers plus this repository's own finite-charge, magnetization and vacuum-polarization computations.

sha256: *se_combine.py f070bdd654389a7711de44228c0da7f12410a5a2ffc50841464d49e784c9b754; *se_combine.out eacb5e0b66d8a310f83ca3d25ac2a42c8741f14f7c5b5be02afc80f930a52896; *qed_hfs_sourced_values.txt b60baab5ef7b33d3d7e3f081786215a39e95fcadd82809a7a7e85c12511ca800.
Command: `py -3 -I -X utf8 -u explore/se_combine.py > explore/se_combine.out` (instant).
