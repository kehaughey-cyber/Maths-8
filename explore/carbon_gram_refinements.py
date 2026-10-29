# Refinements to the carbon-gram map (new file; carbon_one_gram.py/.out are left as they are). Same dictionary, no fitting, tabulation only.
# Items: (1) muon rate from the PDG 2020 cosmic-ray review lines (70 m^-2 s^-1 sr^-1, cos^2, 10-15% lower normalization, ~1 cm^-2 min^-1 horizontal)
#        (2) u,d mass spread: PDG 2024 90% CL, mu/md, and a lattice cross-check (FLAG m_ud as quoted in search results, secondary)
#        (3) solar neutrino flux through the gram: Borexino Phase-II Table II (explore/data/borexino_2018_arxiv1707.09279.txt), tree-level nu_e-e cross section
#        (4) which ratios are arithmetic on inputs and which are not
# Run: py -3 -I -u explore/carbon_gram_refinements.py > explore/carbon_gram_refinements.out
from mpmath import mp, mpf, pi, sqrt, nstr, quad, log
mp.dps = 25
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); eV = mpf('1.602176634e-19'); u = mpf('1.66053906660e-27')
hbarc_eVm = mpf('1.973269804e-7'); me_eV = mpf('510998.95')
M = mpf('1e-3'); N = M/(12*u)
a_dia = mpf('3.56683e-10'); V = N*a_dia**3/8
L_cube = V**(mpf(1)/3); R_sph = (3*V/(4*pi))**(mpf(1)/3)
A_face_cm2 = (L_cube*100)**2; A_proj_cm2 = pi*(R_sph*100)**2
print('GEOMETRY  cube side', nstr(L_cube, 8), 'm; face', nstr(A_face_cm2, 8), 'cm^2; sphere projected area pi R^2', nstr(A_proj_cm2, 8), 'cm^2')
print()

print('(1) MUONS  PDG 2020 Cosmic Rays review (explore/data/pdg2020_cosmic_rays.txt lines 308-311):')
print('    vertical integral intensity E>1 GeV/c at sea level ~ 70 m^-2 s^-1 sr^-1 = 0.0070 cm^-2 s^-1 sr^-1; recent measurements favour 10-15% lower; angular law cos^2(theta); "~1 cm^-2 min^-1 for horizontal detectors"')
Iv = mpf('70')/mpf('1e4')
for lab, f in [('PDG 70', 1), ('PDG 70 minus 10%', mpf('0.90')), ('PDG 70 minus 15%', mpf('0.85'))]:
    r = pi/2*Iv*f*A_face_cm2
    print(f'    {lab:18s} (pi/2) I A face: {nstr(r, 6)} s^-1 = {nstr(r*60, 6)} /min = {nstr(r*86400, 6)} /day')
r1 = mpf(1)/60*A_face_cm2
print('    PDG "1 cm^-2 min^-1" (all energies, horizontal) x face:', nstr(r1, 6), 's^-1 =', nstr(r1*60, 6), '/min =', nstr(r1*86400, 6), '/day')
print('    ratio of that to the E>1 GeV cos^2 integral (PDG 70):', nstr(r1/(pi/2*Iv*A_face_cm2), 6), ' -> the rate depends on the energy threshold at the factor 1.5 level, and on a flux normalization at 10-15%')
print('    the cos^2 integral itself: 2 pi I int cos^3 sin d theta = (pi/2) I exactly; a different exponent n gives 2 pi I/(n+2): n=2 -> pi/2 = 1.5708, n=2.0 vs 1.8 changes it by', nstr((2*pi/mpf('3.8'))/(pi/2)-1, 4))
print('    range carried for the gram:', nstr(pi/2*Iv*mpf('0.85')*A_face_cm2*60, 4), '-', nstr(r1*60, 4), 'per minute (a factor', nstr(r1/(pi/2*Iv*mpf('0.85')*A_face_cm2), 3), ')')
print()

print('(2) u, d MASSES  PDG 2024 (pdg2024_quarks.txt): mu = 2.16 +- 0.07 MeV, md = 4.70 +- 0.07 MeV (90% CL), mu/md = 0.462 +- 0.020, (mu+md)/2 = 3.49 +- 0.07 MeV; all MSbar at 2 GeV')
mu, md = mpf('2.16'), mpf('4.70'); dm = mpf('0.07')
Eatom = 12*u*c**2/eV
def frac(mu_, md_): return 18*(mu_+md_)*mpf('1e6')/Eatom
print('    valence 18u+18d at PDG central:', nstr(18*(mu+md), 8), 'MeV =', nstr(frac(mu, md)*100, 6), '% of the atom rest energy')
print('    PDG linear extremes (+-0.07 each, fully correlated):', nstr(18*(mu+md-2*dm), 8), '-', nstr(18*(mu+md+2*dm), 8), 'MeV =', nstr(frac(mu-dm, md-dm)*100, 6), '-', nstr(frac(mu+dm, md+dm)*100, 6), '%')
print('    PDG (mu+md)/2 = 3.49 +- 0.07 -> 36 x that =', nstr(36*mpf('3.49'), 8), 'MeV; consistent with 18(mu+md)')
mud = mpf('3.364'); ratio = mpf('0.462')       # FLAG N_f=2+1 m_ud (quoted in arXiv:2003.11703 as found by search; secondary) with PDG mu/md
md_l = 2*mud/(1+ratio); mu_l = ratio*md_l
print('    lattice cross-check: FLAG m_ud = 3.364(41) MeV (Nf=2+1, via arXiv:2003.11703 as quoted in a search result, secondary) with PDG mu/md=0.462 ->')
print('      mu =', nstr(mu_l, 6), ' md =', nstr(md_l, 6), 'MeV; sum 18(mu+md) =', nstr(18*(mu_l+md_l), 8), 'MeV =', nstr(frac(mu_l, md_l)*100, 6), '% ; difference from PDG central', nstr((18*(mu_l+md_l))/(18*(mu+md))-1, 4))
print('    scale dependence (ILLUSTRATIVE, one-loop, inputs not from a saved file): m(mu) ~ alpha_s(mu)^(4/9) for nf=3; with alpha_s(1,2,3 GeV) = 0.47, 0.30, 0.25 (rough):')
for mu_s, a_s in [(1, mpf('0.47')), (2, mpf('0.30')), (3, mpf('0.25'))]:
    k = (a_s/mpf('0.30'))**(mpf(4)/9)
    print(f'      mu_scale {mu_s} GeV: factor {nstr(k, 5)} -> 18(mu+md) = {nstr(18*(mu+md)*k, 6)} MeV = {nstr(frac(mu*k, md*k)*100, 5)} %')
print('    the quark mass sum is a convention-dependent number; the reading "1.1% of the atom is bare quark mass" is good to about 2-3% of itself (statistical) and moves about 20% with the scale convention; the other ~99% is the proton/neutron mass that is not the bare quark masses')
print()

print('(3) NEUTRINOS THROUGH THE GRAM  (Borexino Phase-II Table II, explore/data/borexino_2018_arxiv1707.09279.txt lines 958-965; fluxes inferred assuming MSW-LMA, cm^-2 s^-1)')
fl = [('pp', mpf('6.1e10'), mpf('0.265'), 'measured (6.1 +-0.5 +0.3/-0.5)e10; SSM HZ 5.98e10, LZ 6.03e10'),
      ('7Be', mpf('4.99e9'), mpf('0.862'), 'measured (4.99 +-0.11 +0.06/-0.08)e9; SSM HZ 4.93e9, LZ 4.50e9'),
      ('pep', mpf('1.27e8'), mpf('1.44'), 'measured (HZ) (1.27 +-0.19 +0.08/-0.12)e8; SSM 1.44e8, 1.46e8'),
      ('CNO', mpf('7.9e8'), mpf('1.0'), 'upper limit <7.9e8 (95% CL) in that paper; SSM HZ 4.88e8, LZ 3.51e8. Energy 1 MeV is a placeholder')]
GF = mpf('1.1663788e-5')            # GeV^-2
hbarc2_cm2GeV2 = mpf('0.3893794e-27')   # (hbar c)^2 in GeV^2 cm^2
s2 = mpf('0.2312')                  # sin^2 theta_W (PDG, recalled, not from a saved file)
gL, gR = mpf(1)/2 + s2, s2          # nu_e e: CC + NC
def sigma_cm2(E_MeV):
    E = E_MeV/mpf('1e3'); m = me_eV/mpf('1e9')   # GeV
    Tmax = 2*E**2/(m+2*E)
    f = lambda T: (2*GF**2*m/pi)*(gL**2 + gR**2*(1-T/E)**2 - gL*gR*m*T/E**2)
    return quad(f, [0, Tmax])*hbarc2_cm2GeV2
nel = 6*N
tot_cross = tot_int = 0
print(f'    {"species":5s} {"flux cm^-2 s^-1":>16s} {"crossings/s":>14s} {"E used MeV":>10s} {"sigma(nu_e e) cm^2":>20s} {"interactions/s":>16s} {"per day":>12s}  note')
for nm, F, E, note in fl:
    s = sigma_cm2(E)
    cr = F*A_proj_cm2; it = F*s*nel
    if nm != 'CNO': tot_cross += cr; tot_int += it
    print(f'    {nm:5s} {nstr(F, 4):>16s} {nstr(cr, 5):>14s} {nstr(E, 4):>10s} {nstr(s, 6):>20s} {nstr(it, 5):>16s} {nstr(it*86400, 5):>12s}  {note}')
print('    pp+7Be+pep crossings through the gram per second:', nstr(tot_cross, 5), '; elastic nu_e-e interactions per second on the 6N electrons (tree level, nu_e only, mean/line energy used for pp, spectrum not integrated; oscillated mu/tau flavour omitted, which lowers it):', nstr(tot_int, 5), '=', nstr(tot_int*86400, 5), 'per day')
print('    pp 0.265 MeV = mean of the pp spectrum (endpoint 0.42 MeV), recalled, not from a saved file; 7Be 0.862 MeV and pep 1.44 MeV are line energies; sin^2 theta_W recalled; so the interaction counts are order-of-magnitude, the crossing counts are flux x area only')
print('    14C antineutrinos made inside the gram (modern 14C, 0.226 Bq/g): 0.226 per second for 1 g of natural carbon, a fraction', nstr(mpf('0.226')/tot_cross, 4), 'of the pp+7Be+pep crossings per second')
print('    crossings per atom of the gram per second (pp):', nstr(fl[0][1]*A_proj_cm2/N, 5), '; the 12C nucleus area pi r_ch^2 =', nstr(pi*(mpf('2.4702e-13'))**2, 5), 'cm^2 -> geometric nuclear crossings/s per gram', nstr(fl[0][1]*pi*(mpf('2.4702e-13'))**2*N, 5), '(only a geometric figure; the weak cross section is ~1e-20 of it)')
print('    not included (no sourced file): 8B, hep, CNO measured value, geo-antineutrinos, reactor, atmospheric, relic')
print()

print('(4) DERIVED RATIOS  None of the ratios in the map is derived from the floor. Which are arithmetic on inputs:')
print('    exact identities of the dictionary: cycles = R E/(hbar c); cycles/(alpha/2) for the valence rung = Z_eff; 2 pi nats per cycle.')
print('    ratios of two sourced numbers, nothing else: B/Mc^2, r_ch/lambda_tau, a0/lambda_e = 1/alpha = 137.035999, level step ratios.')
print('    no ratio here follows from 2I/E8/12/30; 1/alpha, the lepton mass ratios and the nuclear 1.15 cycles are inputs to this map, not outputs of the floor.')
