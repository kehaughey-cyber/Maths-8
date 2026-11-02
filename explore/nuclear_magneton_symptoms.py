# The nuclear magneton: what it is, what it does, and its symptoms, computed only from sourced numbers. New file (2026-11-02); nothing fitted.
# Exact SI constants: e, h, c, k_B.  Sourced (explore/data/moment_benchmark_sourced_values.txt, CODATA 2022): mu_B, mu_e, mu_p, m_p/m_e.  Sourced (saved IAEA table): nuclear moments, spins, abundances.
# Textbook relations used and not sourced here are marked "(textbook, from memory)".
# Run: py -3 -I -X utf8 -u explore/nuclear_magneton_symptoms.py > explore/nuclear_magneton_symptoms.out
import csv, os, math
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0; kB = 1.380649e-23; mu0 = 4e-7*math.pi   # mu0 = 4 pi e-7 (the pre-2019 definition; the 2019 SI value differs by about 5e-10)
muB = 9.2740100657e-24; mue = 9.2847646917e-24; mup = 1.41060679545e-26; MPME = 1836.152673426
me = e*hbar/(2*muB); mp = me*MPME; muN = e*hbar/(2*mp)
print('== what the nuclear magneton is')
print('m_e from mu_B = e hbar / (2 m_e):', repr(me), 'kg ; m_p = m_e x (m_p/m_e):', repr(mp), 'kg')
print('mu_N = e hbar / (2 m_p) =', repr(muN), 'J/T ;  mu_B / (m_p/m_e) =', repr(muB/MPME), ' (equal)')
lam_p = hbar/(mp*c); print('proton reduced Compton length hbar/(m_p c) =', repr(lam_p), 'm (the stack lists 2.1030891e-16)')
print('e c lambda_p / 2 =', repr(e*c*lam_p/2), 'J/T ; ratio to mu_N =', repr(e*c*lam_p/2/muN), ' i.e. mu_N is the moment of one charge e circling at c on the radius lambda_p (current e c/(2 pi r) times area pi r^2)')
print('mu_N / h =', repr(muN/h/1e6), 'MHz/T')
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
def spin(jp):
    s = jp.rstrip('+-'); a, _, b = s.partition('/'); return float(a)/float(b) if b else float(a)
print('\n== what it does: the precession (Larmor) frequency of a nuclear moment in a field, nu = |mu| B / (I h); and the g-factor g = mu / (I mu_N)')
print('nuclide   Jpi    I    mu (mu_N)     g = mu/(I mu_N)   |mu_N-units|   nu per tesla (MHz/T)   splitting h nu at 1 T (eV)   kT at 298.15 K / that')
for (z, n) in [(1, 0), (0, 1), (1, 1), (2, 1), (6, 7), (7, 7), (7, 8), (9, 10)]:
    r = get(z, n); mu = float(r['magnetic_dipole']); I = spin(r['jp']); g = mu/(I)
    nu = abs(mu)*muN/(I*h)/1e6; dE = h*nu*1e6/e
    print(f'{r["symbol"]+str(z+n):8s} {r["jp"]:>6s} {I:4.1f} {mu:12.7f} {g:16.7f} {abs(mu):12.7f} {nu:18.6f} {dE:24.4e} {kB*298.15/e/dE:20.4g}')
print('check on the proton: 2 mu_p / h from the CODATA value =', repr(2*mup/h/1e6), 'MHz/T (the table row gives the line above)')
print('\n== symptoms: how the nucleus is not a point particle')
mp_t = float(get(1, 0)['magnetic_dipole']); mn_t = float(get(0, 1)['magnetic_dipole'])
print('Dirac point proton (g = 2, spin 1/2): mu = 1.0000 mu_N; measured', repr(mp_t), '-> factor', repr(mp_t), ' (g_p = %.7f)' % (2*mp_t))
print('Dirac point neutron (no charge): mu = 0; measured', repr(mn_t), 'mu_N : a neutral particle with a moment must have charged parts that do not cancel')
print('measured ratio mu_n / mu_p =', repr(mn_t/mp_t))
print('quark picture (textbook, from memory): mu_p = (4 mu_u - mu_d)/3, mu_n = (4 mu_d - mu_u)/3, mu_q = e_q hbar/(2 m_q), m_q = m_p/3 gives mu_u = 2, mu_d = -1 (units mu_N): mu_p = 3.0000, mu_n = -2.0000, ratio -2/3 = -0.66667')
print('   against measured 2.7928 (%+.1f%%), -1.9130 (%+.1f%%), ratio %.5f' % ((mp_t/3-1)*100, (mn_t/(-2)-1)*100, mn_t/mp_t))
print('\n== symptoms in the gram: carbon-13 (natural abundance from the table row for carbon-12 = 98.94%, so 13C taken as 1.06%)')
mu13 = float(get(6, 7)['magnetic_dipole']); I13 = spin(get(6, 7)['jp']); N = 5.0184506350676e22; f13 = 1 - float(get(6, 6)['abundance'])/100
N13 = N*f13; m_gram = 1.0e-3
print('13C nuclei in one gram:', repr(N13), ' moment each', repr(mu13*muN), 'J/T')
M_all = N13*mu13*muN
print('all 13C moments aligned (expressed ceiling): M =', repr(M_all), 'J/T')
for T in (298.15, 4.2):
    for B in (1.0,):
        x = mu13*muN*B/(kB*T)   # spin-1/2: M = N mu tanh(mu B / kT)
        print(f'   in B = {B} T at T = {T} K: M = {N13*mu13*muN*math.tanh(x):.4e} J/T ; manifest/expressed = tanh({x:.3e}) = {math.tanh(x):.4e}')
chi_vol_per_gram = mu0*N13*(mu13*muN)**2/(kB*298.15)          # SI volume susceptibility times the volume of one gram: m^3 ; M = chi H V, chi per kg below
chi_mass_SI = chi_vol_per_gram/m_gram                         # m^3/kg (weak-field Curie law, spin 1/2)
print('nuclear Curie mass susceptibility of the 13C moments, 298.15 K: %.4e m^3/kg = %.4e emu/g (cgs: x 1e3/(4 pi))' % (chi_mass_SI, chi_mass_SI*1e3/(4*math.pi)))
print('compare the diamond orbital (diamagnetic) susceptibility -4.9e-7 cm^3/g (secondary table value, unverified, carbon_aspect_sourced_values.txt section 3): ratio nuclear/diamagnetic = %.2e' % (chi_mass_SI*1e3/(4*math.pi)/4.9e-7))
print('\n== ablating the size scaling in the instrument against the measured moment ratio (proton order over electron order)')
print('instrument: moment per charge ratio = rho_p^(2g-1), rho_p = 1/(m_p/m_e), edge scaling geo = rho^g (g = 0: size does not follow the tick; g = 1: size follows the tick, the lab anchor)')
rp = 1.0/MPME; meas = mup/mue
print(f'{"g":>8s} {"model ratio":>14s} {"model/measured |mu_p/mu_e|":>28s} {"model/(mu_N/mu_B)":>20s}')
for g in (0.0, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0):
    r = rp**(2*g-1); print(f'{g:8.3f} {r:14.6e} {r/meas:28.6e} {r/(muN/muB):20.6e}')
g_p = 0.5*(1 + math.log(meas)/math.log(rp)); g_N = 0.5*(1 + math.log(muN/muB)/math.log(rp))
print('exponent that reproduces the measured |mu_p/mu_e| exactly: g =', repr(g_p), '; the one that reproduces mu_N/mu_B: g =', repr(g_N))
print('the difference 1 - g =', repr(1 - g_p), ' is ln(mu_p/mu_N) / (2 ln(m_p/m_e)) = ', repr(math.log(mup/muN)/(2*math.log(MPME))))
