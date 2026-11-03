# The hyperfine splitting along the hydrogen-like series, with no scale step assumed.  New file (2026-11-02); nothing fitted.
# For each ion: measured splitting E, nuclear moment and spin from the saved IAEA table.  Non-relativistic contact form (the one that reproduced H, D, 3He+):
#     E_nr = (8/3) [(2I+1)/(2I)] (mu_X/mu_B) (|mu_e|/mu_B) Z^3 alpha^2 Ry (1 + m_e/M)^-3,
# then r = E / E_nr.  The point-nucleus Dirac (Breit) factor is A(Z alpha) = 1 / (gamma (2 gamma - 1)), gamma = sqrt(1 - (Z alpha)^2); residual r / A holds the finite-size, Bohr-Weisskopf and QED effects.
# The size ratio of the atom's order to the electron's Compton order is s = (a0/Z) / lambda_e = 1 / (Z alpha).  The effective exponent d ln E / d ln R (R the electron-order size a0/Z, so R proportional to 1/Z, at fixed moments) is p_eff = d ln(E_nr A) / d ln Z.
# Sourced: explore/data/moment_benchmark_sourced_values.txt (all hyperfine values secondary), saved IAEA table.  m_e/u recalled (negligible here).
# Run: py -3 -I -X utf8 -u explore/hydrogenlike_series.py > explore/hydrogenlike_series.out
import csv, os, math
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; c = 299792458.0; hc_eVnm = h*c/e*1e9
muB = 9.2740100657e-24; mue = 9.2847646917e-24; ALPHA = 7.2973525643e-3; RY = 13.605693122990; meu = 5.485799090e-4
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
def spin(jp):
    s = jp.rstrip('+-'); a, _, b = s.partition('/'); return float(a)/float(b) if b else float(a)
def Eeff(lam_nm): return hc_eVnm/lam_nm
ions = [('H', 1, 0, h*1420405751.768/e, 1e-10, 'Hellwig (sec.)'), ('D', 1, 1, h*327384352.5222/e, 1e-10, 'Wineland & Ramsey'), ('3He+', 2, 1, h*8665649867.0/e, 1e-9, 'Schuessler et al.'),
        ('165Ho66+', 67, 98, Eeff(572.79), 0.15/572.79, 'Livermore EBIT'), ('187Re74+', 75, 112, Eeff(451.2), 0.2/451.2, 'EBIT; isotope assignment inferred'),
        ('185Re74+', 75, 110, Eeff(455.7), 0.2/455.7, 'EBIT; isotope assignment inferred'), ('207Pb81+', 82, 125, Eeff(1019.7), 0.2/1019.7, 'Seelig 1998'), ('209Bi82+', 83, 126, 5.0840, 0.0008/5.0840, 'ESR (Bi table)')]
print(f'hc = {hc_eVnm:.6f} eV nm')
print(f'{"ion":9s} {"Z":>3s} {"s=1/(Z a)":>9s} {"I":>4s} {"mu(mu_N)":>9s} {"E (eV)":>12s} {"rel.unc":>8s} {"E_nr (eV)":>12s} {"r=E/E_nr":>9s} {"A(Z a)":>8s} {"r/A":>8s}  note')
res = {}
for name, Z, N, E, unc, note in ions:
    r_ = get(Z, N); mu = abs(float(r_['magnetic_dipole'])); I = spin(r_['jp']); M = (float(r_['atomic_mass'])*1e-6 - Z*meu)/meu; muN_over_muB = 1/1836.152673426
    Enr = (8/3)*((2*I+1)/(2*I))*(mu*muN_over_muB)*(mue/muB)*Z**3*ALPHA**2*RY*(1+1/M)**-3
    g = math.sqrt(1-(Z*ALPHA)**2); A = 1/(g*(2*g-1)); res[name] = (Z, E, Enr, A, mu, I, unc)
    print(f'{name:9s} {Z:3d} {1/(Z*ALPHA):9.3f} {I:4.1f} {mu:9.4f} {E:12.6e} {unc:8.1e} {Enr:12.6e} {E/Enr:9.5f} {A:8.5f} {E/Enr/A:8.5f}  {note}')
print('\neffective exponent of the absolute energy in the electron-order size R = a0/Z at fixed moments: p_eff = d ln(E) / d ln Z with E = E_nr x A (Dirac point nucleus)')
print(f'{"Z":>3s} {"s=1/(Z a)":>10s} {"p_eff (Dirac)":>14s}')
for Z in (1, 2, 5, 10, 20, 30, 40, 50, 60, 67, 75, 82, 83):
    def lnE(z): g = math.sqrt(1-(z*ALPHA)**2); return 3*math.log(z) - math.log(g*(2*g-1))
    z1, z2 = Z*0.999, Z*1.001; p = (lnE(z2)-lnE(z1))/(math.log(z2)-math.log(z1))
    print(f'{Z:3d} {1/(Z*ALPHA):10.3f} {p:14.4f}')
print('\nmeasured exponent between pairs of ions (moments and multiplicity divided out, so the Z-dependence only):')
def red(n): Z, E, Enr, A, mu, I, unc = res[n]; return E/(mu*(2*I+1)/(2*I))
for a_, b_ in (('H', '3He+'), ('3He+', '165Ho66+'), ('165Ho66+', '207Pb81+'), ('207Pb81+', '209Bi82+'), ('165Ho66+', '209Bi82+')):
    Za, Zb = res[a_][0], res[b_][0]; p = math.log(red(b_)/red(a_))/math.log(Zb/Za)
    pd = math.log((res[b_][2]*res[b_][3]/ (res[b_][4]*(2*res[b_][5]+1)/(2*res[b_][5])))/(res[a_][2]*res[a_][3]/(res[a_][4]*(2*res[a_][5]+1)/(2*res[a_][5]))))/math.log(Zb/Za)
    print(f'{a_:9s} -> {b_:9s} (Z {Za} -> {Zb}): measured p = {p:.4f}; non-relativistic Z^3 only = 3.0000; Dirac (E_nr A) = {pd:.4f}')
print('\nNote: the Dirac factor is the point-nucleus value; for Ho, Re, Pb, Bi the finite nuclear charge and Bohr-Weisskopf corrections are of order 1% to 10% and are not included, so r/A departs from 1 there.')
