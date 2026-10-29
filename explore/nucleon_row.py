# Nucleon row for the four-languages / colour ladder. New file; nothing fitted.
# Inputs: r_p = 0.84075(64) fm (CODATA 2022, explore/data/codata2022_proton_radius.txt); m_p c^2 = 938.27208816 MeV (CODATA 2018, as in four_languages_ladder.py);
#         alpha_g1(0) = pi and the near-flat slope (Deur, Brodsky, de Teramond 2016, eq 4.4, 4.3; explore/data/); C_F = 4/3.
# Run: py -3 -I -u explore/nucleon_row.py > explore/nucleon_row.out
from mpmath import mp, mpf, pi, nstr
mp.dps = 25
hbarc = mpf('1.973269804e-7'); mp_eV = mpf('938.27208816e6')
lam_p = hbarc/mp_eV
CF = mpf(4)/3
print('proton Compton length hbar/(m_p c) =', nstr(lam_p, 12), 'm')
for lab, r, u in [('CODATA 2022', mpf('0.84075e-15'), mpf('0.00064e-15')), ('CODATA 2018 (recalled)', mpf('0.8414e-15'), mpf('0.0019e-15'))]:
    x = r*mp_eV/hbarc
    print(f'{lab:24s} r_p = {nstr(r, 8)} +- {nstr(u, 3)} m ; cycles r_p m_p c^2/(hbar c) = r_p/lambda_p = {nstr(x, 10)} +- {nstr(u/lam_p, 3)} ; minus 4 = {nstr(x-4, 6)} ({nstr((x-4)/(u/lam_p), 3)} sigma)')
    Q = hbarc/r
    print(f'{"":24s} momentum scale hbar c/r_p = {nstr(Q/mpf("1e6"), 8)} MeV, Q^2 = {nstr((Q/mpf("1e9"))**2, 6)} GeV^2 ; C_F alpha_g1(0) = {nstr(CF*pi, 10)} ; ratio cycles/(C_F alpha_g1) = {nstr(x/(CF*pi), 8)}')
print('alpha_g1 at that Q^2: not tabulated here; Deur: slope near 0 gives ~1% decrease per 0.1 GeV^2, so within ~0.5% of pi at Q^2 = 0.055 GeV^2.')
print('the 4 is an observation, not derived; the 4.7% difference between 4.0 and C_F pi = 4.19 is a comparison, not a match.')
