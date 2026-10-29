# Full mass ladder: neutrino scale, leptons, quarks, W/Z/H, hadrons, nuclei, binding energies. Raw successive steps.
# New file; floor untouched. No fitting, no search: tabulate ratios between sourced quantities, print logs, stop.
# cycles = R E/(hbar c); one cycle = 12 radits = 30 ticks = 2 pi nats.
# Inputs: explore/data/pdg2024_*.txt (PDG 2024 summary tables, pdftotext), explore/data/ame2020_mass_1.mas20.txt (AME2020, IAEA AMDC).
from mpmath import mp, mpf, pi, log, sqrt, nstr, nint
import os
mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); eV = mpf('1.602176634e-19')
me_kg = mpf('9.1093837015e-31'); mp_kg = mpf('1.67262192369e-27'); mn_kg = mpf('1.67492749804e-27')
u_kg = mpf('1.66053906660e-27'); al = mpf('7.2973525693e-3')
phi = (1+sqrt(5))/2
lP = sqrt(hbar*G/c**3); mP_eV = sqrt(hbar*c/G)*c**2/eV
l12 = lambda x: log(x)/log(12); l10 = lambda x: log(x, 10); lphi = lambda x: log(x)/log(phi); l2 = lambda x: log(x, 2)
lam = lambda m_eV: hbar/((m_eV*eV/c**2)*c)          # reduced Compton wavelength in m from a mass in eV

# ---- neutrino scale from PDG 2024 oscillation splittings (normal order, lightest mass set to 0 = minimum possible masses)
d21 = mpf('7.53e-5'); d32 = mpf('2.455e-3'); d31 = d32 + d21
nu2_min = sqrt(d21); nu3_min = sqrt(d31)
print('NEUTRINO (PDG 2024 summary: dm21^2 = 7.53e-5 eV^2, dm32^2 = 2.455e-3 eV^2 normal order; tritium m_nu_e < 0.8 eV (90% CL); DESI+CMB LCDM sum < 0.072 eV (95%), arXiv:2404.03002)')
print('  minimum masses if lightest = 0 (lower bounds on m2, m3, not measured masses): m2 >=', nu2_min, 'eV   m3 >=', nu3_min, 'eV   sum >=', nu2_min+nu3_min, 'eV')
print('  old rough anchor 0.05 eV; m3_min / 0.05 =', nu3_min/mpf('0.05'))
print()

# ---- master mass list (eV). (name, mass_eV, unc_eV or None, source/scheme)
mev = mpf(10)**6; gev = mpf(10)**9
M = [
 ('nu2_min', nu2_min, None, 'lower bound from dm21^2 (lightest=0)'),
 ('nu3_min', nu3_min, None, 'lower bound from dm31^2 (lightest=0)'),
 ('e',  me_kg*c**2/eV, None, 'CODATA 2018'),
 ('u',  mpf('2.16')*mev, mpf('0.07')*mev, 'PDG24 MSbar 2 GeV'),
 ('d',  mpf('4.70')*mev, mpf('0.07')*mev, 'PDG24 MSbar 2 GeV'),
 ('s',  mpf('93.5')*mev, mpf('0.8')*mev, 'PDG24 MSbar 2 GeV'),
 ('mu', mpf('105.6583755')*mev, mpf('0.0000023')*mev, 'PDG24'),
 ('c',  mpf('1.2730')*gev, mpf('0.0046')*gev, 'PDG24 MSbar m_c(m_c)'),
 ('tau', mpf('1776.93')*mev, mpf('0.09')*mev, 'PDG24'),
 ('b',  mpf('4.183')*gev, mpf('0.007')*gev, 'PDG24 MSbar m_b(m_b)'),
 ('p',  mp_kg*c**2/eV, None, 'CODATA 2018'),
 ('n',  mn_kg*c**2/eV, None, 'CODATA 2018'),
 ('W',  mpf('80.3692')*gev, mpf('0.0133')*gev, 'PDG24'),
 ('Z',  mpf('91.1880')*gev, mpf('0.0020')*gev, 'PDG24'),
 ('H',  mpf('125.20')*gev, mpf('0.11')*gev, 'PDG24'),
 ('t',  mpf('172.57')*gev, mpf('0.29')*gev, 'PDG24 direct measurement'),
]
M.sort(key=lambda t: t[1])
me_eV = me_kg*c**2/eV
print('PART A  sorted mass list, positions, Compton length (1 cycle each at own cut), gravitational (m/m_P)^2')
print(f'  {"name":8s} {"mass eV":>22s} {"rel unc":>10s} {"m/m_e":>22s} {"mass dec":>10s} {"mass p12":>10s} {"lam_C m":>14s} {"len dec":>9s} {"len p12":>9s} {"(m/mP)^2":>12s}  source')
for n, m, u, s in M:
    L = lam(m)
    ru = '-' if u is None else nstr(u/m, 3)
    print(f'  {n:8s} {nstr(m,16):>22s} {ru:>10s} {nstr(m/me_eV,16):>22s} {nstr(l10(m/nu3_min),6):>10s} {nstr(l12(m/nu3_min),6):>10s} {nstr(L,8):>14s} {nstr(l10(L/lP),6):>9s} {nstr(l12(L/lP),6):>9s} {nstr((m/mP_eV)**2,6):>12s}  {s}')
print('  mass dec / p12 are above nu3_min (the heavier minimum neutrino mass); length dec / p12 above the Planck length; m_P =', nstr(mP_eV,10), 'eV')
print()

print('PART B  raw successive steps in mass order (ratio, ln, log10, log12, logphi, distance of logphi and log12 to nearest integer)')
print(f'  {"step":12s} {"ratio":>22s} {"ln":>12s} {"log10":>10s} {"log12":>10s} {"logphi":>10s} {"phi-res":>9s} {"12-res":>9s}')
for i in range(1, len(M)):
    a = M[i-1]; b = M[i]; r = b[1]/a[1]
    lp = lphi(r); l1 = l12(r)
    print(f'  {a[0]+">"+b[0]:12s} {nstr(r,16):>22s} {nstr(log(r),8):>12s} {nstr(l10(r),6):>10s} {nstr(l1,6):>10s} {nstr(lp,6):>10s} {nstr(lp-nint(lp),4):>9s} {nstr(l1-nint(l1),4):>9s}')
top = M[-1]; bot = M[0]
print('  full span nu2_min -> t: ratio', nstr(top[1]/bot[1],12), ' log10', nstr(l10(top[1]/bot[1]),8), ' log12', nstr(l12(top[1]/bot[1]),8), ' logphi', nstr(lphi(top[1]/bot[1]),8))
print('  e -> t: ratio', nstr(top[1]/me_eV,12), ' log10', nstr(l10(top[1]/me_eV),8), ' log12', nstr(l12(top[1]/me_eV),8), ' logphi', nstr(lphi(top[1]/me_eV),8))
print('  count of steps:', len(M)-1, ' mean log12 step:', nstr(l12(top[1]/bot[1])/(len(M)-1),8), ' mean ln step:', nstr(log(top[1]/bot[1])/(len(M)-1),8))
print()

print('PART C  uncertainty bracket on each step ratio (propagated relative uncertainty from the PDG 1-sigma values; PDG quark uncertainties are 90% CL, so not 1-sigma)')
for i in range(1, len(M)):
    a = M[i-1]; b = M[i]
    ua = 0 if a[2] is None else a[2]/a[1]; ub = 0 if b[2] is None else b[2]/b[1]
    ru = sqrt(ua**2+ub**2)
    print(f'  {a[0]+">"+b[0]:12s} rel unc of ratio {nstr(ru,3):>10s}  -> logphi unc {nstr(ru/log(phi),3):>10s}  log12 unc {nstr(ru/log(12),3):>10s}')
print()

print('PART D  Koide quantity Q = (sum m)/(sum sqrt m)^2 for several triples, raw (2/3 for comparison). Quark masses are scheme-dependent: mixed-scheme triples are listed as is, not endorsed.')
mm = {n: m for n, m, u, s in M}
def Q(a, b, c_): return (mm[a]+mm[b]+mm[c_])/(sqrt(mm[a])+sqrt(mm[b])+sqrt(mm[c_]))**2
for tr in [('e','mu','tau'), ('u','c','t'), ('d','s','b'), ('s','c','b'), ('c','b','t'), ('u','d','s')]:
    q = Q(*tr)
    print(f'  {"".join(x+" " for x in tr):12s} Q = {nstr(q,16)}   Q - 2/3 = {nstr(q-mpf(2)/3,6)}')
print()

# ---- nuclei from AME2020
amu = {}; rows = []
for line in open(os.path.join(HERE, 'data', 'ame2020_mass_1.mas20.txt')).read().split('\n'):
    if len(line) < 120 or not line[4:19].strip().replace(' ', '').isdigit(): continue
    try:
        N = int(line[4:9]); Z = int(line[9:14]); A = int(line[14:19]); el = line[20:23].strip()
    except ValueError: continue
    ba = line[54:67].strip(); me_ = line[28:42].strip()
    if '#' in line[28:67] or '*' in line[28:67]: continue
    try:
        ba = mpf(ba); mex = mpf(me_)
    except Exception: continue
    t = line.split()
    try: am = mpf(t[-3] + t[-2])    # atomic mass in micro-u: "integer part" + "fraction group"
    except Exception: am = None
    rows.append((A, Z, el, ba, mex, am))
print('PART E  AME2020 (', len(rows), 'nuclides with measured, non-estimated binding energy per nucleon parsed )')
best = max(rows, key=lambda r: r[3]); print('  largest B/A in table:', best[0], best[2], nstr(best[3],12), 'keV  (Z =', best[1], ')')
want = [(1,0),(1,1),(2,1),(3,1),(3,2),(4,2),(6,3),(7,3),(12,6),(14,7),(16,8),(20,10),(28,14),(40,20),(56,26),(58,26),(62,28),(120,50),(208,82),(238,92)]
print(f'  {"nuclide":8s} {"A":>4s} {"Z":>3s} {"B/A keV":>18s} {"B total MeV":>16s} {"M_atom (u*1e-6)":>20s} {"B/(M c^2)":>14s} {"B/(m_p c^2)":>14s} {"lam_nuc m":>12s} {"len p12":>9s}')
for A, Z in want:
    r = [x for x in rows if x[0] == A and x[1] == Z]
    if not r: print('  missing', A, Z); continue
    A_, Z_, el, ba, mex, am = r[0]
    Btot = ba*A/1000
    Mnuc_u = (am/mpf(10)**6 - Z*me_kg/u_kg) if am else None   # nuclear mass ~ atomic - Z m_e (electron binding ignored)
    Mnuc_eV = Mnuc_u*u_kg*c**2/eV if Mnuc_u else None
    bm = (Btot*mev)/Mnuc_eV if Mnuc_eV else None
    bp = (Btot*mev)/(mp_kg*c**2/eV)
    Ln = lam(Mnuc_eV) if Mnuc_eV else None
    print(f'  {str(A)+el:8s} {A:>4d} {Z:>3d} {nstr(ba,12):>18s} {nstr(Btot,12):>16s} {nstr(am,14) if am else "-":>20s} {nstr(bm,8) if bm else "-":>14s} {nstr(bp,8):>14s} {nstr(Ln,6) if Ln else "-":>12s} {nstr(l12(Ln/lP),6) if Ln else "-":>9s}')
print('  nuclear mass = atomic mass - Z m_e; electron binding energy (<~1 MeV for U) ignored; for A=1,Z=0 (neutron) no electrons removed.')
print()

print('PART F  binding energies against alpha and the lepton scale (raw)')
print('  alpha/2 =', al/2, ' alpha =', al, ' alpha^2 =', al**2)
for A, Z, nm in [(2,1,'2H'),(4,2,'4He'),(12,6,'12C'),(56,26,'56Fe'),(62,28,'62Ni')]:
    r = [x for x in rows if x[0] == A and x[1] == Z][0]
    ba = r[3]
    print(f'  {nm:5s} B/A = {nstr(ba,12)} keV  B/A / m_e c^2 = {nstr(ba*1000/me_eV,10)}  B/A /(m_p c^2) = {nstr(ba*1000/(mp_kg*c**2/eV),10)}  B/A/(m_e c^2)/alpha = {nstr(ba*1000/me_eV/al,10)}')
print()

print('PART G  reference powers of phi for reading the residual columns: phi^n for n = 5..20')
for k in range(5, 21):
    print(f'  phi^{k:<3d} = {nstr(phi**k,15):>20s}')
