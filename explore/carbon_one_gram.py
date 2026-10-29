# One gram of carbon-12 (as diamond), from information to energy to leptons. Same dictionary: cycles = R E/(hbar c); 1 cycle = 2 pi nats = 12 radits = 30 ticks.
# New file; floor untouched. No fitting: every number is a sourced input or an arithmetic consequence of sourced inputs; the script prints and stops.
# Inputs: explore/data/ame2020_mass_1.mas20.txt (12C, 14C, 14N), nubase2020_nubase_4.mas20.txt (14C half-life, abundances), PeriodicTableJSON.json (ionization energies),
# pdg2024_quarks.txt (u, d masses as read there), nist_webbook_diamond_condensed.html (S, Cp), carbon_sourced_values.txt (radius, lattice constant, muon flux, 14C activity).
import json, os, re
from mpmath import mp, mpf, pi, log, sqrt, nstr, exp
mp.dps = 25
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data')
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); eV = mpf('1.602176634e-19'); kB = mpf('1.380649e-23')
NA = mpf('6.02214076e23'); u = mpf('1.66053906660e-27'); me_kg = mpf('9.1093837015e-31'); mp_kg = mpf('1.67262192369e-27'); mn_kg = mpf('1.67492749804e-27')
al = mpf('7.2973525693e-3'); Ry = mpf('13.605693123'); a0 = mpf('5.29177210903e-11'); hbarc = mpf('1.973269804e-7')   # eV m
mmu_eV = mpf('105.6583755e6'); mtau_eV = mpf('1776.93e6'); me_eV = me_kg*c**2/eV
l10 = lambda x: log(x, 10); l12 = lambda x: log(x)/log(12); l2 = lambda x: log(x, 2)
lP = sqrt(hbar*G/c**3); mP = sqrt(hbar*c/G)
cyc = lambda R, E_eV: R*E_eV/hbarc
T = mpf('298.15')

# ---- sourced inputs
r_ch = mpf('2.4702e-15'); r_ch_u = mpf('0.0022e-15')                 # 12C rms charge radius (IAEA / Angeli-Marinova, via search result)
a_dia = mpf('3.56683e-10')                                            # diamond cubic lattice constant (Straumanis & Aka 1951, via search result)
S_dia = mpf('2.3782'); Cp_dia = mpf('6.1149')                          # J/(mol K) at 298.15 K, NIST WebBook (DeSorbo 1953)
I_v = mpf('0.70e-2')                                                   # cm^-2 s^-1 sr^-1, vertical, E > 1 GeV, sea level (Cosmic ray recipes)
A14_modern = mpf('0.226')                                              # Bq per gram of carbon, modern 14C specific activity
mu_u = mpf('2.16e6'); md_u = mpf('4.70e6')                             # u, d MSbar masses at 2 GeV in eV, PDG 2024 as read in pdg2024_quarks.txt
ame = {}
for line in open(os.path.join(DATA, 'ame2020_mass_1.mas20.txt')).read().split('\n'):
    if len(line) > 100 and line[14:19].strip().isdigit():
        try: ame[(int(line[14:19]), line[20:23].strip())] = (mpf(line[28:42]), mpf(line[54:67]))
        except Exception: pass
mex12, ba12 = ame[(12, 'C')]; mex14C, _ = ame[(14, 'C')]; mex14N, _ = ame[(14, 'N')]
line14 = next(l for l in open(os.path.join(DATA, 'nubase2020_nubase_4.mas20.txt')).read().split('\n') if re.match(r'014 0060\s+14C\s', l))
mh = re.search(r'(\d+\.\d+)\s+ky\s+(\d+\.\d+)', line14); hl_ky = mpf(mh.group(1)); hl_unc = mpf(mh.group(2))
print('NUBASE2020 line for 14C:', line14[:130].rstrip())
EL = {e['symbol']: e for e in json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']}
IE = [mpf(x)/mpf('96.485332') for x in EL['C']['ionization_energies']]      # eV
M_nat = mpf(str(EL['C']['atomic_mass']))

print('INPUTS')
print('  12C: AME2020 mass excess', mex12, 'keV (= 0 by definition), B/A', ba12, 'keV')
print('  14C - 14N mass excess difference (AME2020):', mex14C - mex14N, 'keV  = Q(beta-) of 14C (nuclear Q from atomic masses)')
print('  14C half-life (NUBASE2020):', hl_ky, '+-', hl_unc, 'ky; 12C abundance 98.94(6)%, 13C 1.06(6)% (NUBASE2020 IS field)')
print('  12C rms charge radius', r_ch, '+-', r_ch_u, 'm (IAEA / Angeli-Marinova via search result); diamond a', a_dia, 'm (Straumanis-Aka via search result)')
print('  diamond S(298.15) =', S_dia, ' Cp =', Cp_dia, ' J/(mol K) (NIST WebBook, DeSorbo 1953)')
print('  muon vertical intensity (E>1 GeV, sea level)', I_v, 'cm^-2 s^-1 sr^-1, cos^2 law (Cosmic ray recipes, via search result); 14C modern activity', A14_modern, 'Bq/g C')
print('  PeriodicTableJSON C ionization energies (kJ/mol):', EL['C']['ionization_energies'])
print()

# =========================== the gram
M = mpf('1e-3'); m_atom = 12*u
N = M/m_atom                 # atoms of 12C in one gram
print('THE GRAM: 1 g of 12C (atomic mass 12 u exactly) -> N = M/(12 u) =', nstr(N, 15), 'atoms  (= 1/12 mol with N_A exact)')
print('  natural carbon (M = 12.011 u from PeriodicTableJSON): N_nat =', nstr(M/(M_nat*u), 15), ' ; 1 g of natural carbon holds', nstr(M/(M_nat*u)*mpf('0.9894'), 12), '12C and', nstr(M/(M_nat*u)*mpf('0.0106'), 12), '13C')
print('  per atom: 6 protons, 6 neutrons, 6 electrons; valence quarks 18 u + 18 d')
print('  per gram: protons', nstr(6*N, 12), ' neutrons', nstr(6*N, 12), ' electrons', nstr(6*N, 12), ' u quarks', nstr(18*N, 12), ' d quarks', nstr(18*N, 12), ' (total valence quarks', nstr(36*N, 12), ')')
print()

# =========================== PART 1: information
print('PART 1  INFORMATION')
Erest = M*c**2
V_dia = N*a_dia**3/8            # 8 atoms per cubic cell
rho_dia = M/V_dia
R_sph = (3*V_dia/(4*pi))**(mpf(1)/3); L_cube = V_dia**(mpf(1)/3)
print('  diamond volume of the gram (8 atoms per cell, a =', a_dia, ') V =', nstr(V_dia, 10), 'm^3; density', nstr(rho_dia, 8), 'kg/m^3; cube side', nstr(L_cube, 8), 'm; equal-volume sphere radius', nstr(R_sph, 8), 'm')
print('  gram rest energy M c^2 =', nstr(Erest, 15), 'J =', nstr(Erest/eV, 15), 'eV')
cy_gram = R_sph*Erest/eV/hbarc
print('  Bekenstein-Compton count for the whole gram: cycles = R E/(hbar c) =', nstr(cy_gram, 12), ' -> nats', nstr(2*pi*cy_gram, 12), ' bits', nstr(2*pi*cy_gram/log(2), 12), '  (log10 of bits', nstr(l10(2*pi*cy_gram/log(2)), 8), ')')
S_gram = S_dia*(M/(12*mpf('1e-3')))            # J/K for 1 g of 12C diamond: S per mol (12 g) -> per gram /12
S_gram = S_dia/12
print('  thermodynamic entropy of the gram at 298.15 K (diamond): S =', nstr(S_gram, 10), 'J/K =', nstr(S_gram/kB, 12), 'nats =', nstr(S_gram/kB/log(2), 12), 'bits;  per atom', nstr(S_gram/kB/N, 8), 'nats')
print('  Landauer energy to erase those bits at 298.15 K: T S =', nstr(T*S_gram, 10), 'J ;  kT ln2 =', nstr(kB*T*log(2), 10), 'J per bit')
print('  counting the atoms: log2 N =', nstr(l2(N), 8), 'bits;  Bekenstein bits / thermodynamic bits =', nstr(2*pi*cy_gram/log(2)/(S_gram/kB/log(2)), 8), ' (gap in decades', nstr(l10(2*pi*cy_gram/log(2)/(S_gram/kB/log(2))), 6), ')')
print('  Compton wavelength of the whole gram hbar/(M c) =', nstr(hbar/(M*c), 10), 'm; Planck mass', nstr(mP, 10), 'kg; M/m_P =', nstr(M/mP, 10), ';  that wavelength / l_P =', nstr(hbar/(M*c)/lP, 10), ' (log12', nstr(l12(hbar/(M*c)/lP), 8), ')')
print()

# =========================== PART 2: energy budget of the atom and the gram
print('PART 2  ENERGY  (per atom in eV, per gram in J, fraction of the gram rest energy)')
Mnuc_u = 12 - 6*me_kg/u                                    # nuclear mass in u (electron binding ignored)
Mnuc_eV = Mnuc_u*u*c**2/eV
B12 = 12*ba12*mpf('1e3')                                  # eV, total binding of the nucleus from AME B/A
Eatom = 12*u*c**2/eV
SIE = sum(IE)
Ec = mpf('711.2')/mpf('96.485332')                         # eV, Hfg(C atom, 0 K) from the CCCBDB table (cohesion of graphite)
q_u = 18*mu_u + 18*md_u
items = [
 ('atom rest energy 12 u c^2', Eatom),
 ('nuclear rest energy (12 u - 6 m_e) c^2', Mnuc_eV),
 ('6 protons + 6 neutrons rest (free nucleons)', 6*(mp_kg+mn_kg)*c**2/eV),
 ('nuclear binding energy B (AME2020 B/A x 12)', B12),
 ('valence quark masses 18 u + 18 d (MSbar 2 GeV, PDG 2024)', q_u),
 ('6 electrons rest energy', 6*me_eV),
 ('sum of all six ionization energies', SIE),
 ('cohesion Ec = Hfg(C atom, 0 K)', Ec),
 ('thermal: kT at 298.15 K', kB*T/eV),
]
print(f'  {"item":62s} {"eV per atom":>18s} {"J per gram":>16s} {"fraction of M c^2":>18s} {"log10 eV":>9s} {"log12 eV":>9s}')
for n, e in items:
    print(f'  {n:62s} {nstr(e, 14):>18s} {nstr(e*eV*N, 10):>16s} {nstr(e*eV*N/Erest, 10):>18s} {nstr(l10(e), 6):>9s} {nstr(l12(e), 6):>9s}')
print('  check: atom rest = nuclear rest + 6 m_e c^2 (electron binding <1 keV ignored):', nstr(Eatom - Mnuc_eV - 6*me_eV, 10), 'eV residual')
print('  nuclear rest = 6 m_p + 6 m_n - B:', nstr(Mnuc_eV - (6*(mp_kg+mn_kg)*c**2/eV - B12), 10), 'eV residual (m_e binding of AME atomic masses ~ electron binding ignored)')
print('  of the rest energy of one atom: electrons', nstr(6*me_eV/Eatom, 10), ' valence quark masses', nstr(q_u/Eatom, 10), ' nuclear binding', nstr(B12/Eatom, 10), ' remainder (nucleon mass not from bare quark masses, net of binding)',
      nstr((Eatom - 6*me_eV - q_u + 0)/Eatom, 10))
pr = mp_kg*c**2/eV; nr = mn_kg*c**2/eV
print('  one proton: 2 u + 1 d bare', nstr(2*mu_u+md_u, 8), 'eV =', nstr((2*mu_u+md_u)/pr, 6), 'of m_p c^2;  one neutron: 1 u + 2 d bare', nstr(mu_u+2*md_u, 8), 'eV =', nstr((mu_u+2*md_u)/nr, 6), 'of m_n c^2')
print('  quark-mass uncertainties (PDG 90% CL): u +-0.07 MeV, d +-0.07 MeV -> sum +-', nstr(18*mpf('0.07e6')*2, 8), 'eV per atom if linear')
print('  hydrogen-like check: C5+ ionization energy is the sixth IE =', nstr(IE[5], 10), 'eV vs Z^2 Ry =', nstr(36*Ry, 10), 'eV; ratio', nstr(IE[5]/(36*Ry), 8))
print('  ionization energies (eV):', ' '.join(nstr(x, 8) for x in IE))
print()

# =========================== PART 3: sizes
print('PART 3  SIZES  (m, and position in powers of 12 above the Planck length)')
r_bond = a_dia*sqrt(3)/4
sizes = [('Planck length', lP), ('1 g Compton wavelength hbar/(Mc)', hbar/(M*c)), ('tau Compton wavelength', hbar*c/(mtau_eV*eV)),
         ('12C rms charge radius', r_ch), ('muon Compton wavelength', hbar*c/(mmu_eV*eV)), ('1s radius of the hydrogenic muon in C (nonrel., point nucleus)', hbar*c/(mmu_eV*eV)/(6*al)),
         ('electron Compton wavelength', hbar*c/(me_eV*eV)), ('C5+ 1s radius a0/6', a0/6), ('diamond C-C bond a sqrt3/4', r_bond), ('diamond cubic a', a_dia),
         ('Wigner-Seitz radius of the gram lattice', (3*V_dia/(4*pi*N))**(mpf(1)/3)), ('cube side of the gram', L_cube), ('equal-volume sphere radius of the gram', R_sph)]
print(f'  {"item":62s} {"size m":>14s} {"decades above l_P":>18s} {"p12 above l_P":>14s}')
for n, s in sizes:
    print(f'  {n:62s} {nstr(s, 8):>14s} {nstr(l10(s/lP), 8):>18s} {nstr(l12(s/lP), 8):>14s}')
print('  ratios: R_sph / C-C bond =', nstr(R_sph/r_bond, 10), ' ; C-C bond / r_ch =', nstr(r_bond/r_ch, 10), ' ; r_ch / lambda_tau =', nstr(r_ch/(hbar*c/(mtau_eV*eV)), 10), ' ; lambda_e / r_ch =', nstr(hbar*c/(me_eV*eV)/r_ch, 10))
print()

# =========================== PART 4: levels in the dictionary, with object counts in the gram
print('PART 4  LEVELS: cycles = R E/(hbar c) for one object, count in the gram, total cycles in the gram')
bond_E = Ec/2                                                # 2 bonds per atom in the diamond lattice (4 neighbours, each bond shared)
lv = [
 ('nucleus: R = r_ch, E = B (total binding)', r_ch, B12, N),
 ('nucleus: R = r_ch, E = nuclear rest energy', r_ch, Mnuc_eV, N),
 ('per nucleon: R = r_ch, E = B/12', r_ch, B12/12, 12*N),
 ('C5+ (1s electron): R = a0/6, E = IE6', a0/6, IE[5], N),
 ('valence electron: R = n^2 a0/Z_eff, E = IE1', 4*a0/(2*sqrt(IE[0]/Ry)), IE[0], N),
 ('diamond bond: R = C-C, E = Ec/2', r_bond, bond_E, 2*N),
 ('cohesion: R = r_ws, E = Ec', (3*V_dia/(4*pi*N))**(mpf(1)/3), Ec, N),
 ('thermal: R = a, E = kT (298.15 K)', a_dia, kB*T/eV, N),
 ('the gram: R = sphere radius, E = M c^2', R_sph, Erest/eV, 1),
]
print(f'  {"level":48s} {"cycles / object":>16s} {"/(alpha/2)":>12s} {"count":>12s} {"total cycles":>16s} {"log10 total":>11s}')
for n, R, E, k in lv:
    cc = cyc(R, E)
    print(f'  {n:48s} {nstr(cc, 10):>16s} {nstr(cc/(al/2), 10):>12s} {nstr(k, 6):>12s} {nstr(cc*k, 10):>16s} {nstr(l10(cc*k), 8):>11s}')
print()

# =========================== PART 5: leptons
print('PART 5  LEPTONS in and through the gram')
print('  electrons held:', nstr(6*N, 12), ' ; electron rest-mass fraction of the gram:', nstr(6*me_kg/(12*u), 10), ' ; their binding (sum IE) per atom', nstr(SIE, 8), 'eV')
lam14 = log(2)/(hl_ky*mpf('1e3')*mpf('365.25')*mpf('86400'))
N14_gram = A14_modern/lam14                                   # 14C atoms per gram of modern carbon, derived from activity and half-life
N_nat = M/(M_nat*u)
print('  14C: lambda = ln2/T_half =', nstr(lam14, 10), 's^-1  (T_half', hl_ky, 'ky);  modern activity', A14_modern, 'Bq/g -> 14C atoms per gram of carbon', nstr(N14_gram, 8), ' ; 14C/C atom ratio', nstr(N14_gram/N_nat, 8))
Q = (mex14C - mex14N)*mpf('1e3')
print('  each 14C decay emits one electron and one antineutrino: Q =', nstr(Q, 10), 'eV; leptons made per second per gram of modern carbon: electrons', A14_modern, ' antineutrinos', A14_modern, ' ; per year', nstr(A14_modern*mpf('365.25')*86400, 8), 'of each')
print('  power if every decay deposited Q (upper bound; the antineutrino leaves with part of it):', nstr(A14_modern*Q*eV, 8), 'W')
print('  Q / (electron rest energy) =', nstr(Q/me_eV, 8))
area_cm2 = (L_cube*100)**2
rate = pi/2*I_v*area_cm2                                       # integral of I_v cos^2 theta cos theta dOmega over a horizontal face = (pi/2) I_v A
print('  cosmic-ray muons (sea level): horizontal face of the cube', nstr(area_cm2, 8), 'cm^2; rate through it = (pi/2) I_v A =', nstr(rate, 8), 's^-1 =', nstr(rate*60, 8), 'per minute =', nstr(rate*86400, 8), 'per day (cos^2 law, E > 1 GeV)')
Mnuc_kg = Mnuc_u*u
for nm, m_eV, in [('muon', mmu_eV), ('tau', mtau_eV), ('electron', me_eV)]:
    mred = m_eV*(Mnuc_eV)/(m_eV + Mnuc_eV)
    rB = hbar*c/(mred*eV)/(6*al)       # hydrogenic Bohr radius for Z = 6 with the reduced mass
    EB = (6*al)**2*mred/2
    print(f'  hydrogenic {nm:8s} on a point 12C nucleus (Z = 6, reduced mass): 1s radius {nstr(rB, 8)} m = {nstr(rB/r_ch, 8)} nuclear radii; E_1s = (Z alpha)^2 mu c^2/2 = {nstr(EB, 8)} eV (nonrelativistic, no finite-size effect: for the muon and tau this is not a measured level)')
print('  neutrinos through the gram: not sourced here (solar, atmospheric and 14C-antineutrino fluxes), no number given')
print()

# =========================== PART 6: step ratios along the energy ladder per atom
print('PART 6  RAW STEP RATIOS along the per-atom energy ladder (descending)')
ladder = sorted([(n, e) for n, e in items], key=lambda t: -t[1])
print(f'  {"from":62s} {"to":40s} {"ratio":>14s} {"log10":>8s} {"log12":>8s}')
for i in range(len(ladder)-1):
    a, b = ladder[i], ladder[i+1]
    r = a[1]/b[1]
    print(f'  {a[0]:62s} {b[0]:40s} {nstr(r, 8):>14s} {nstr(l10(r), 6):>8s} {nstr(l12(r), 6):>8s}')
print('  span first to last:', nstr(ladder[0][1]/ladder[-1][1], 8), ' log10', nstr(l10(ladder[0][1]/ladder[-1][1]), 8), ' log12', nstr(l12(ladder[0][1]/ladder[-1][1]), 8))
print('  gram total energy / Landauer-erasure energy of its entropy:', nstr(Erest/(T*S_gram), 8), ' ; gram rest energy / nuclear binding of the gram:', nstr(Erest/(B12*eV*N), 8))
