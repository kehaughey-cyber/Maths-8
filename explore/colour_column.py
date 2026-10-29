# Colour column for the four-languages ladder: the strong force written the way alpha Q^2 writes EM. New file; nothing fitted.
# Sources (saved in explore/data/):
#   deur_brodsky_teramond_2016_arxiv1604.08082.pdf/.txt : Prog. Part. Nucl. Phys. 90 (2016) 1; eq. (4.4) alpha_g1(Q^2=0) = pi (Bjorken sum rule effective charge; JLab data fill 0 < Q^2 < ~1e1 GeV^2; slope eq. (4.3) is small:
#       "decrease by only 1% over the Q^2-span of 0.1 GeV^2"); alpha_V(0) = 0.42 +- 0.03 (V-scheme freezing value quoted in sec. 4.9); many models freeze anywhere from ~0.4 to ~3.5 (scheme/observable dependent).
#   pdg2024_qcd_review.pdf/.txt : alpha_s(m_Z^2) = 0.1180 +- 0.0009 (PDG 2023/2024 average, eq. 9.25).
# Colour factor: C_F = 4/3 (quark colour Casimir in SU(3); the floor has su(3) inside E8 and the colour Z/3, see floor/). Not fitted.
# Run: py -3 -I -u explore/colour_column.py > explore/colour_column.out
from mpmath import mp, mpf, pi, nstr
mp.dps = 25
hbarc = mpf('1.973269804e-7')              # eV m
r_ch = mpf('2.4702e-15'); B12 = mpf('92161735.2')   # m ; eV  (carbon_one_gram.out)
CF = mpf(4)/3
cyc_nuc = r_ch*B12/hbarc
print('INPUTS  alpha_g1(0) = pi = ', nstr(pi, 12), ';  alpha_V(0) = 0.42 +- 0.03 ;  alpha_s(m_Z^2) = 0.1180 +- 0.0009 ;  C_F = 4/3')
print('12C nucleus: R = r_ch =', nstr(r_ch, 8), 'm, E = B =', nstr(B12, 10), 'eV, cycles R E/(hbar c) =', nstr(cyc_nuc, 12))
Qscale = hbarc/r_ch
print('momentum scale hbar c / r_ch =', nstr(Qscale/mpf('1e6'), 8), 'MeV ; Q^2 =', nstr((Qscale/mpf('1e9'))**2, 6), 'GeV^2  (inside the near-flat region of alpha_g1: slope bound ~1% per 0.1 GeV^2)')
print()
print('COLOUR CYCLES  C_F alpha  (the strong analogue of alpha Q^2, pair-binding cycles at any R, if the coupling is the frozen one)')
for nm, a, u in [('alpha_g1(0)', pi, 'exact, eq 4.4'), ('alpha_V(0) central', mpf('0.42'), '+-0.03'), ('alpha_V(0) low', mpf('0.39'), ''), ('alpha_V(0) high', mpf('0.45'), '')]:
    cc = CF*a
    print(f'  {nm:20s} alpha = {nstr(a, 8):>12s} {u:14s} C_F alpha = {nstr(cc, 10):>12s}   nucleus cycles / (C_F alpha) = {nstr(cyc_nuc/cc, 10)}')
print()
print('FOR COMPARISON (four_languages_ladder.out, same quantity E/E_C = cycles/(coupling cycles)):')
print('  H atom 0.5 ; C valence 0.27479962 ; Compton rungs 137.036 (= 1/alpha) ; 12C nucleus vs EM alpha Q^2 (Q = 6) 4.3916575')
print('  12C nucleus vs C_F alpha_g1(0):', nstr(cyc_nuc/(CF*pi), 10), ' (ratio to C valence 0.27479962:', nstr(cyc_nuc/(CF*pi)/mpf('0.27479962'), 8), ')')
print('  12C nucleus vs C_F alpha_V(0) = 0.56 :', nstr(cyc_nuc/(CF*mpf('0.42')), 10))
print()
print('READING  the 0.2754 vs 0.2748 closeness was noticed after the numbers were computed; it uses three free choices (the rung, C_F, the g1 scheme). With the V scheme the same ratio is 2.06. One data point, scheme dependent: noted, not claimed.')
print('         alpha_s(m_Z) = 0.1180 would give C_F alpha = ', nstr(CF*mpf('0.1180'), 8), 'at 91.19 GeV (hbar c / 91.19 GeV = ', nstr(hbarc/mpf('91.1880e9'), 6), 'm): not a nuclear-size quantity; shown for the range of the coupling (factor', nstr(pi/mpf('0.1180'), 6), 'from m_Z to Q=0 in the g1 scheme).')
