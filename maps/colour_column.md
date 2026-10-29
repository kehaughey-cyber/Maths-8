# Colour column: the strong coupling written like alpha Q^2 (2026-10-29)

Adds the strong force to `four_languages_ladder.md`. Run: `py -3 -I -u explore/colour_column.py > explore/colour_column.out`. Raw output: `explore/colour_column.out`.

## Sources (saved in `explore/data/`)
- `deur_brodsky_teramond_2016_arxiv1604.08082.pdf/.txt` (Prog. Part. Nucl. Phys. 90, 1): eq. (4.4) alpha_g1(Q^2=0) = pi, the Bjorken-sum-rule effective charge, measured by JLab and others across 0 < Q^2; slope near 0 about 1% per 0.1 GeV^2. V-scheme freezing value 0.42 +- 0.03. Models freeze anywhere from about 0.4 to 3.5 (scheme/observable dependent). pdftotext drops the pi glyph in the default layout; confirmed with `-enc UTF-8` ("alpha_g1 (0) = pi").
- `pdg2024_qcd_review.pdf/.txt`: alpha_s(m_Z^2) = 0.1180 +- 0.0009 (eq. 9.25).
- sha256 pdf: deur d14351349b433fa38f9ad6f2de0ce1553bad6b8841019df7ce6f7bf062006854; pdg d06948c331663c2341c3f922e48cd29b4aac83f3bbff71fe3ac8d70cb4f40c51.

## Result (12C, r_ch = 2.4702 fm, B = 92.1617352 MeV, cycles 1.15370902565, scale hbar c/r_ch = 79.88 MeV, Q^2 = 0.00638 GeV^2)
Strong pair-binding cycles C_F alpha with C_F = 4/3: g1 scheme 4.188790205 (nucleus cycles / that = 0.2754277); V scheme 0.56 (0.52 to 0.60) (ratio 2.060, range 1.92 to 2.22). The g1 ratio 0.27543 is 0.23% from the carbon valence electron's EM ratio E/E_C = 0.27480; noticed after computing, three free choices, V scheme gives 2.06.

## Correction (append-only): second nucleus
The closeness above is not a shared ratio. B ~ a_v A and r ~ r0 A^(1/3) give cycles ~ A^(4/3). Using AME2020 B (full_ladder.md) and charge radii recalled from memory, NOT from a saved source (4He 1.6755, 56Fe 3.7377, 208Pb 5.5012 fm; Angeli-Marinova table was blocked by a bot check and should replace these):
| nucleus | cycles R B / hbar c | / (C_F alpha_g1(0)) |
|---|---|---|
| 4He | 0.2403 | 0.0574 |
| 12C | 1.1537 | 0.2754 |
| 56Fe | 9.3242 | 2.226 |
| 208Pb | 45.6214 | 10.891 |
The carbon value is a crossing of a rising curve. What is constant across nuclei is B/A (about 8 MeV) times r0 (about 1.2 fm) / hbar c, about 0.05 cycles per nucleon, i.e. saturation.

sha256: *colour_column.py 573348aae7f912c7f0dbe65fb5a07a4da8ac46e3e4b8af2c5cbc16cda779b598; *colour_column.out 65dc4ea10524470767ca5c3aa3ba0d5d70d371e34ef0284d47d65718312c267a.
