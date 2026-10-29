# The same rungs written in four languages: energy-and-size, mass, charge, information. New file; nothing fitted, no rule proposed.
# Rungs: tau, mu, e (Compton), proton (Compton), 12C nucleus (r_ch, B), H atom, C valence electron, C-C bond, the gram.
# Inputs are the ones already used in carbon_one_gram.py / full_ladder.md (CODATA 2018 constants, PDG 2024 masses, AME2020 B/A, r_ch, diamond a, Ec from CCCBDB, IE1 from PeriodicTableJSON).
# Run: py -3 -I -u explore/four_languages_ladder.py > explore/four_languages_ladder.out
from mpmath import mp, mpf, pi, sqrt, log, nstr
mp.dps = 25
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); eV = mpf('1.602176634e-19'); u = mpf('1.66053906660e-27')
al = mpf('7.2973525693e-3'); hbarc = mpf('1.973269804e-7'); Ry = mpf('13.605693123'); a0 = mpf('5.29177210903e-11')
me = mpf('510998.95'); mmu = mpf('105.6583755e6'); mtau = mpf('1776.93e6'); mproton = mpf('938.27208816e6')
lP = sqrt(hbar*G/c**3); mP_eV = sqrt(hbar*c/G)*c**2/eV
l12 = lambda x: log(x)/log(12); l10 = lambda x: log(x, 10)
M = mpf('1e-3'); N = M/(12*u)
a_dia = mpf('3.56683e-10'); V = N*a_dia**3/8; R_sph = (3*V/(4*pi))**(mpf(1)/3)
r_ch = mpf('2.4702e-15'); B12 = 12*mpf('7680.1446e3'); Mnuc = (12*u - 6*mpf('9.1093837015e-31'))*c**2/eV
IE1 = mpf('1086.5')/mpf('96.485332'); Ec = mpf('711.2')/mpf('96.485332')
Zeff = 2*sqrt(IE1/Ry); R_val = 4*a0/Zeff
# name, R (m), E (eV), mass (eV), Q felt (e), count in gram, note
rows = [
 ('tau (Compton)',       hbarc/mtau, mtau, mtau, 1, 0, 'R = hbar/(m c), E = m c^2'),
 ('muon (Compton)',      hbarc/mmu,  mmu,  mmu,  1, 0, 'R = hbar/(m c), E = m c^2'),
 ('electron (Compton)',  hbarc/me,   me,   me,   1, 6*N, 'R = hbar/(m c), E = m c^2'),
 ('proton (Compton)',    hbarc/mproton, mproton, mproton, 1, 6*N, 'R = hbar/(m c), E = m c^2'),
 ('12C nucleus (r_ch, B)', r_ch, B12, Mnuc, 6, N, 'R = rms charge radius, E = total binding'),
 ('H atom (a0, Ry)',     a0, Ry, mproton + me, 1, 0, 'reference rung, not in the gram'),
 ('C valence (n=2)',     R_val, IE1, 12*u*c**2/eV, Zeff, N, 'R = n^2 a0/Z_eff, E = IE1; Q felt = Z_eff; mass = atom'),
 ('C-C bond (diamond)',  a_dia*sqrt(3)/4, Ec/2, 12*u*c**2/eV, 0, 2*N, 'R = bond length, E = Ec/2; mass = atom share; Q felt 0 (neutral)'),
 ('the gram',            R_sph, M*c**2/eV, M*c**2/eV, 0, 1, 'R = equal-volume sphere, E = M c^2; charge content below'),
]
print('LANGUAGE 1  ENERGY AND SIZE   cycles = R E/(hbar c)')
print(f'  {"rung":24s} {"R m":>13s} {"p12":>8s} {"E eV":>14s} {"log12 E":>8s} {"cycles":>14s}')
cy = {}
for n, R, E, m, Q, k, note in rows:
    cy[n] = R*E/hbarc
    print(f'  {n:24s} {nstr(R, 6):>13s} {nstr(l12(R/lP), 6):>8s} {nstr(E, 8):>14s} {nstr(l12(E), 5):>8s} {nstr(cy[n], 10):>14s}')
print()
print('LANGUAGE 2  MASS   m (eV), m/m_e, log12(m/m_P), gravitational coupling (m/m_P)^2, Compton length in p12, Schwarzschild radius 2Gm/c^2 in p12')
print(f'  {"rung":24s} {"m eV":>14s} {"m/m_e":>13s} {"log12 m/mP":>11s} {"(m/mP)^2":>12s} {"lambda p12":>10s} {"r_s p12":>9s}')
for n, R, E, m, Q, k, note in rows:
    mk = m*eV/c**2; rs = 2*G*mk/c**2
    print(f'  {n:24s} {nstr(m, 8):>14s} {nstr(m/me, 8):>13s} {nstr(l12(m/mP_eV), 6):>11s} {nstr((m/mP_eV)**2, 6):>12s} {nstr(l12(hbarc/m/lP), 6):>10s} {nstr(l12(rs/lP), 6):>9s}')
print()
print('LANGUAGE 3  CHARGE   Q felt (units of e); Coulomb cycles alpha Q^2 (= R E_C/hbar c at any R); E_C at the rung R; row E / E_C')
print(f'  {"rung":24s} {"Q":>9s} {"alpha Q^2":>13s} {"E_C eV":>14s} {"E/E_C":>12s}')
for n, R, E, m, Q, k, note in rows:
    if Q == 0:
        print(f'  {n:24s} {"0":>9s} {"-":>13s} {"-":>14s} {"-":>12s}   ({note})'); continue
    aQ2 = al*Q**2; EC = aQ2*hbarc/R
    print(f'  {n:24s} {nstr(Q, 6):>9s} {nstr(aQ2, 8):>13s} {nstr(EC, 8):>14s} {nstr(E/EC, 8):>12s}')
Qp = 6*N
EC_g = al*Qp**2*hbarc/R_sph
print(f'  gram, charge content: positive charge {nstr(Qp, 10)} e = {nstr(Qp*eV, 10)} C; all charges |Q| = 12 N e = {nstr(12*N*eV, 10)} C (Faraday constant 96485.33212 C/mol, since 12N = 1 mol); net 0')
print(f'  gram, unscreened: alpha Q^2 with Q = 6N = {nstr(al*Qp**2, 8)}; Coulomb energy of the positive charge alone at R_sph = {nstr(EC_g, 8)} eV = {nstr(EC_g/(M*c**2/eV), 8)} x M c^2')
print()
print('LANGUAGE 4  INFORMATION   bits per object = 2 pi cycles / ln 2; count in the gram; total bits')
print(f'  {"rung":24s} {"cycles":>14s} {"nats":>14s} {"bits/object":>14s} {"count in gram":>14s} {"total bits":>14s}')
for n, R, E, m, Q, k, note in rows:
    nats = 2*pi*cy[n]; bits = nats/log(2)
    print(f'  {n:24s} {nstr(cy[n], 10):>14s} {nstr(nats, 10):>14s} {nstr(bits, 10):>14s} {nstr(k, 5) if k else "-":>14s} {nstr(bits*k, 8) if k else "-":>14s}')
S_th = mpf('2.3782')/12/mpf('1.380649e-23')
print(f'  other counts for the same gram: thermodynamic entropy {nstr(S_th/log(2), 8)} bits; atoms {nstr(N, 8)} (log2 {nstr(log(N, 2), 6)} bits to label one); Bekenstein-Compton {nstr(2*pi*cy["the gram"]/log(2), 8)} bits')
print()
print('CROSS-CHECK  one gram, same cycle count in each language: cycles(R E) vs (R/lambda_C)(m/m_P-style) forms')
Mkg = M
lamC = hbar/(Mkg*c)
print(f'  cycles via energy-size: {nstr(cy["the gram"], 12)}; via R/lambda_C(gram): {nstr(R_sph/lamC, 12)} (same number: lambda_C = hbar/(M c))')
print(f'  gravitational: (M/m_P)^2 = {nstr((M*c**2/eV/mP_eV)**2, 8)}; gram R_sph / r_s = {nstr(R_sph/(2*G*Mkg/c**2), 8)}')
