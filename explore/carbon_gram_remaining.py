# Carbon gram: the items listed as not done in carbon_gram_refinements.md. New file; nothing fitted, tabulation only.
#  A heat content and phonons (diamond), B graphite vs diamond, C polyatomic geometry, D nuclear matter radius, E neutrinos (8B, hep, geo, relic; atmospheric not obtained)
# Inputs: explore/data/carbon_remaining_sourced_values.txt (list of sources), nist_webbook_*.html, cccbdb_enthalpy_formation_0K.html, pdg2024_baryons.txt, pdg2024_rev_bbang-cosmology.txt, solar_neutrinos_review_arxiv2501.09971.txt, geonu_borexino_arxiv1909.02257.txt.
# Run: py -3 -I -u explore/carbon_gram_remaining.py > explore/carbon_gram_remaining.out
import html, os, re
from mpmath import mp, mpf, pi, sqrt, log, exp, nstr, quad, findroot, zeta
mp.dps = 25
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data')
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); eV = mpf('1.602176634e-19'); kB = mpf('1.380649e-23'); u = mpf('1.66053906660e-27')
Rg = mpf('8.314462618'); hbarc = mpf('1.973269804e-7'); al = mpf('7.2973525693e-3'); a0 = mpf('5.29177210903e-11')
lP = sqrt(hbar*G/c**3); l12 = lambda x: log(x)/log(12); l10 = lambda x: log(x, 10)
M = mpf('1e-3'); N = M/(12*u); Erest = M*c**2/eV
a_dia = mpf('3.56683e-10'); V_dia = N*a_dia**3/8; R_dia = (3*V_dia/(4*pi))**(mpf(1)/3)
Ec = mpf('711.2')/mpf('96.485332')          # eV per atom, Hfg(C atom, 0 K), CCCBDB
T = mpf('298.15')
cyc = lambda R, E: R*E/hbarc

print('=== A. HEAT CONTENT AND PHONONS (diamond)')
D3 = lambda x: 3/x**3*quad(lambda t: t**3/(exp(t)-1), [0, x])
CvD = lambda x: 3/x**3*quad(lambda t: t**4*exp(t)/(exp(t)-1)**2, [0, x])      # Cv/(3R), x = Theta/T
SD = lambda x: mpf(4)/3*D3(x) - log(1-exp(-x))                              # S/(3R)
xCp = findroot(lambda x: 3*Rg*CvD(x) - mpf('6.1149'), 7)
xS = findroot(lambda x: 3*Rg*SD(x) - mpf('2.3782'), 7)
Th_Cp = xCp*mpf('298.16'); Th_S = xS*T
print('  Debye temperature solved from the measured value, not fitted to anything else:')
print('    from Cp(298.16 K) = 6.1149 J/(mol K) [DeSorbo 1953, NIST WebBook], taking Cp = Cv:  Theta_D =', nstr(Th_Cp, 8), 'K')
print('    from S(298.15 K) = 2.3782 J/(mol K) [DeSorbo 1953]:                                  Theta_D =', nstr(Th_S, 8), 'K')
print('    the two differ by', nstr((Th_S/Th_Cp-1)*100, 4), '% : the Debye model is not exact for diamond (one optical branch at 1332.7 cm^-1); both are model-defined numbers')
for lab, Th in [('Cp', Th_Cp), ('S', Th_S)]:
    xD = Th/T
    U = 3*Rg*T*D3(xD)          # J/mol, U(T)-U(0)
    kTh = kB*Th/eV
    print(f'  [{lab}] k Theta_D = {nstr(kTh, 8)} eV; heat content U(298.15)-U(0) per gram = {nstr(U/12, 8)} J (per mol {nstr(U, 8)}); fraction of M c^2 = {nstr(U/12/(M*c**2), 6)}; zero-point (9/8) k Theta per atom = {nstr(mpf(9)/8*kTh, 8)} eV, per gram {nstr(mpf(9)/8*kTh*eV*N, 8)} J')
    print(f'      cycles of one phonon quantum at the lattice constant: a k Theta/(hbar c) = {nstr(cyc(a_dia, kTh), 8)} ; at the C-C bond: {nstr(cyc(a_dia*sqrt(3)/4, kTh), 8)}')
Eraman = mpf('1332.7')*mpf('1.239841984e-4')
print('  Raman zone-centre optical phonon 1332.7 +- 0.2 cm^-1 (0 K) =', nstr(Eraman, 8), 'eV (secondary source); cycles at the C-C bond:', nstr(cyc(a_dia*sqrt(3)/4, Eraman), 8), '; Raman energy / k Theta_D(Cp):', nstr(Eraman/(kB*Th_Cp/eV), 6), '; Raman energy / kT(298.15 K):', nstr(Eraman/(kB*T/eV), 6))
print('  modes in the gram: 3 N =', nstr(3*N, 10), '; cycles of one Debye quantum at the C-C bond:', nstr(cyc(a_dia*sqrt(3)/4, kB*Th_Cp/eV), 6), '; Debye thermal energy per mode at 298.15 K:', nstr(3*Rg*T*D3(Th_Cp/T)/(3*mpf('6.02214076e23'))/eV, 6), 'eV')
print('  hbar c / k Theta_D (Cp) wavelength-scale of the cutoff phonon:', nstr(hbarc/(kB*Th_Cp/eV), 8), 'm = ', nstr(l12(hbarc/(kB*Th_Cp/eV)/lP), 6), 'p12')
print()

print('=== B. GRAPHITE vs DIAMOND (graphite density, in-plane bond and interlayer are search-result quotations; entropies from the saved NIST page)')
rho_g = mpf('2267'); V_g = M/rho_g; R_g = (3*V_g/(4*pi))**(mpf(1)/3)
print('  diamond: V', nstr(V_dia, 8), 'm^3, R_sph', nstr(R_dia, 8), 'm, p12', nstr(l12(R_dia/lP), 7), ', BC cycles', nstr(cyc(R_dia, Erest), 8), ', bits', nstr(2*pi*cyc(R_dia, Erest)/log(2), 8))
print('  graphite (2.267 g/cm^3): V', nstr(V_g, 8), 'm^3, R_sph', nstr(R_g, 8), 'm, p12', nstr(l12(R_g/lP), 7), ', BC cycles', nstr(cyc(R_g, Erest), 8), ', bits', nstr(2*pi*cyc(R_g, Erest)/log(2), 8), '; radius ratio g/d', nstr(R_g/R_dia, 8))
S_gr = [('Takahashi-Westrum 1970 (amorphous label)', mpf('5.833')), ('Lutcov et al. 1970', mpf('6.201'))]
S_d = mpf('2.3782')
for nm, S in S_gr:
    bits = S/12/kB/log(2)
    print(f'  graphite-like entropy {nm}: {nstr(S, 6)} J/(mol K) -> per gram {nstr(S/12/kB/log(2), 8)} bits ; ratio to diamond {nstr(S/S_d, 6)} ; BC bits / thermodynamic bits {nstr(2*pi*cyc(R_g, Erest)/log(2)/bits, 6)} (decades {nstr(l10(2*pi*cyc(R_g, Erest)/log(2)/bits), 6)})')
print('  diamond: thermodynamic bits', nstr(S_d/12/kB/log(2), 8), '; decades gap', nstr(l10(2*pi*cyc(R_dia, Erest)/log(2)/(S_d/12/kB/log(2))), 6))
Rb_d = a_dia*sqrt(3)/4; Rb_g = mpf('1.42e-10'); Rl = mpf('3.35e-10')
print('  bond cycles: diamond C-C', nstr(Rb_d, 6), 'm with E = Ec/2 =', nstr(Ec/2, 6), 'eV (2 bonds per atom, 4 neighbours) ->', nstr(cyc(Rb_d, Ec/2), 8), '; graphite in-plane C-C 1.42e-10 with E = Ec/1.5 =', nstr(Ec/mpf('1.5'), 6), 'eV (3 neighbours, 1.5 bonds per atom) ->', nstr(cyc(Rb_g, Ec/mpf('1.5')), 8))
print('  (Ec is the 0 K atomic enthalpy of formation, one number for both: the difference between graphite and diamond cohesion, ~2 kJ/mol, is below the printed digits and is not applied)')
print('  graphite interlayer 3.35e-10 m ->', nstr(l12(Rl/lP), 6), 'p12; in-plane/interlayer =', nstr(Rb_g/Rl, 6))
print()

print('=== C. POLYATOMIC GEOMETRY (CCCBDB experimental geometries, no uncertainties on most; atomization energies from the saved 0 K enthalpies)')
raw = open(os.path.join(DATA, 'cccbdb_enthalpy_formation_0K.html'), encoding='utf-8', errors='replace').read()
def txt(s): return html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<sub>(.*?)</sub>', r'\1', s, flags=re.I))).strip()
Hf = {}
for row in re.findall(r'<TR>(.*?)</TR>', raw, flags=re.S | re.I):
    cells = re.findall(r'<TD[^>]*>(.*?)</TD>', row, flags=re.S | re.I)
    if len(cells) >= 4:
        try: Hf[txt(cells[0])] = mpf(txt(cells[2]))
        except Exception: pass
kJ = mpf('96.485332')
# name, formula, atoms, edges [(length A, count)], note
mols = [
 ('carbon monoxide', 'CO',   {'C': 1, 'O': 1}, [(mpf('1.128'), 1)], 'one C-O edge (triple bond counted once)'),
 ('methane',         'CH4',  {'C': 1, 'H': 4}, [(mpf('1.087'), 4)], '4 C-H edges'),
 ('carbon dioxide',  'CO2',  {'C': 1, 'O': 2}, [(mpf('1.162'), 2)], '2 C=O edges'),
 ('acetylene',       'C2H2', {'C': 2, 'H': 2}, [(mpf('1.203'), 1), (mpf('1.063'), 2)], '1 C-C, 2 C-H edges'),
 ('ethylene',        'C2H4', {'C': 2, 'H': 4}, [(mpf('1.339'), 1), (mpf('1.086'), 4)], '1 C-C, 4 C-H edges'),
 ('ethane',          'C2H6', {'C': 2, 'H': 6}, [(mpf('1.536'), 1), (mpf('1.091'), 6)], '1 C-C, 6 C-H edges'),
 ('benzene',         'C6H6', {'C': 6, 'H': 6}, [(mpf('1.397'), 6), (mpf('1.084'), 6)], '6 C-C (Kekule averaged), 6 C-H edges'),
]
print(f'  {"molecule":16s} {"formula":6s} {"D0 eV":>10s} {"edges":>5s} {"mean edge length m":>20s} {"mean edge E eV":>14s} {"cycles (R_mean, E/edge)":>24s} {"/(alpha/2)":>11s} {"D0/atom/Ry":>11s}   note')
for nm, f, at, edges, note in mols:
    if f not in Hf or any(a not in Hf for a in at): print('  missing enthalpy for', f); continue
    D0 = (sum(n*Hf[a] for a, n in at.items()) - Hf[f])/kJ
    ne = sum(n for _, n in edges); Rm = sum(L*n for L, n in edges)/ne*mpf('1e-10'); Ee = D0/ne
    cc = cyc(Rm, Ee)
    print(f'  {nm:16s} {f:6s} {nstr(D0, 8):>10s} {ne:>5d} {nstr(Rm, 8):>20s} {nstr(Ee, 6):>14s} {nstr(cc, 8):>24s} {nstr(cc/(al/2), 6):>11s} {nstr(D0/sum(at.values())/mpf("13.605693123"), 5):>11s}   {note}')
print('  Edge energy is D0 divided by the number of structural edges; it is not a measured bond energy. Whole-molecule cycles with R = mean edge length are shown only to put the polyatomics on the same axis as the diatomics.')
print()

print('=== D. NUCLEAR MATTER RADIUS from the charge radius (arithmetic with PDG 2024 inputs)')
rch = mpf('2.4702'); rp = mpf('0.8409'); rn2 = mpf('-0.1155'); lam_p = hbarc/mpf('938.27208816e6')*mpf('1e15')
DF = mpf(3)/4*lam_p**2          # Darwin-Foldy term, fm^2
print('  inputs: r_ch(12C) = 2.4702 fm (secondary), r_p = 0.8409 fm (PDG 2024), <r_n^2> = -0.1155(17) fm^2 (PDG 2024), Darwin-Foldy 3/4 (hbar/m_p c)^2 =', nstr(DF, 6), 'fm^2')
rpp2 = rch**2 - rp**2 - (mpf(6)/6)*rn2 - DF
print('  point-proton r_pp^2 = r_ch^2 - r_p^2 - (N/Z)<r_n^2> - DF =', nstr(rpp2, 8), 'fm^2 -> r_pp =', nstr(sqrt(rpp2), 8), 'fm')
print('  with N = Z and isospin symmetry (Coulomb and the spin-orbit term for 12C neglected) the point-matter radius equals r_pp: ', nstr(sqrt(rpp2), 6), 'fm  (ratio to r_ch', nstr(sqrt(rpp2)/rch, 6), ')')
B12 = mpf('92161735.2')
for lab, rr in [('r_ch', rch), ('r_pp (matter, point)', sqrt(rpp2))]:
    print(f'  nucleus cycles B r/(hbar c) with {lab:22s}: {nstr(B12*rr*mpf("1e-15")/hbarc, 10)} ; p12 of the radius {nstr(l12(rr*mpf("1e-15")/lP), 6)}')
dp = sqrt(rpp2)
print('  nuclear matter radius shifts the nucleus cycles by', nstr((dp/rch-1)*100, 4), '% (the comparison with the nucleon r_p/lambda_p = 3.9977 and the A^(4/3) growth is unchanged in kind)')
print()

print('=== E. NEUTRINOS through the gram: 8B, hep, geo, relic (atmospheric: no number extracted, see sources note)')
A_proj = pi*(R_dia*100)**2
print('  gram projected area pi R^2 =', nstr(A_proj, 8), 'cm^2')
fl = [('8B solar, SNO three-phase NC total', mpf('5.25e6'), '(5.25 +-0.16 +0.11/-0.13)e6, measured'),
      ('hep solar, SSM B16-GS98', mpf('7.98e3'), 'not observed; SSM +-30%'),
      ('hep solar, SSM B16-AGSS09', mpf('8.25e3'), 'not observed'),
      ('geo nu_e-bar, 238U', mpf('2.8e6'), 'Borexino 1909.02257, first column of first table; heading lost in pdftotext'),
      ('geo nu_e-bar, 232Th', mpf('2.5e6'), 'same, Th'),
      ]
for nm, F, note in fl:
    print(f'  {nm:38s} flux {nstr(F, 4):>10s} cm^-2 s^-1 ; crossings per second {nstr(F*A_proj, 5):>12s} ; per day {nstr(F*A_proj*86400, 5):>12s}   {note}')
print('  geo total (U + Th as listed) =', nstr(mpf('2.8e6')+mpf('2.5e6'), 4), 'cm^-2 s^-1 ; crossings', nstr((mpf('2.8e6')+mpf('2.5e6'))*A_proj, 5), 's^-1 (40K is not included in that table row; reactor not included)')
print('  solar so far (pp+7Be+pep from carbon_gram_refinements.out): 3.459e10 s^-1; adding 8B', nstr(mpf('5.25e6')*A_proj, 5), ' hep', nstr(mpf('7.98e3')*A_proj, 5))
# relic neutrinos
Tcmb = mpf('2.7255'); kTeV = kB*Tcmb/eV
ng = 2*zeta(3)/pi**2*(kTeV/hbarc)**3 * mpf('1e-6')      # photons per cm^3  ((eV/(eV m))^3 = m^-3 -> 1e-6 cm^-3)
n_nu_one = mpf(3)/22*ng      # one flavour, neutrino or antineutrino separately
n_tot = 6*n_nu_one           # 3 flavours x (nu + nubar)
print('  CMB photon density n_gamma =', nstr(ng, 8), 'cm^-3 (T =', nstr(Tcmb, 5), 'K); relic density per neutrino or antineutrino of one flavour 3/22 n_gamma =', nstr(n_nu_one, 6), 'cm^-3; per flavour (nu + nubar)', nstr(2*n_nu_one, 6), '; all species', nstr(n_tot, 6), 'cm^-3')
Tnu = (mpf(4)/11)**(mpf(1)/3)*Tcmb; kTnu = kB*Tnu/eV
pmean = mpf('3.151')*kTnu       # mean momentum of a relativistic Fermi-Dirac distribution, eV/c
print('  T_nu =', nstr(Tnu, 6), 'K, k T_nu =', nstr(kTnu, 6), 'eV ; mean momentum 3.151 k T_nu =', nstr(pmean, 6), 'eV/c (mean of the F-D spectrum; recalled coefficient)')
for m in [mpf('0.0503021'), mpf('0.0086776')]:
    v = pmean/m if pmean < m else mpf(1)
    flux = n_tot*v*c*mpf('100')            # cm^-2 s^-1 if all species had this mass (non-relativistic p/m)
    print(f'  if every species had m = {nstr(m, 6)} eV (the oscillation minima, masses unmeasured): v/c = {nstr(v, 5)} ; flux n v = {nstr(flux, 6)} cm^-2 s^-1 ; crossings of the gram {nstr(flux*A_proj, 6)} s^-1  (isotropic, no gravitational clustering, no Earth motion)')
print('  atmospheric neutrinos: the PDG neutrino review (sec 14.6.2) gives the flux only as a figure; no integral number was extracted, none is quoted here.')
print('  all of these are crossings; interaction rates are many orders smaller and are not computed (low-energy relic cross sections are not sourced).')
