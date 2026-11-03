# The two groups of hydrogen-like ions side by side: energy, mass, information, and what else differs. New file (2026-11-02); nothing fitted.
# Light group: H, D, 3He+ (Z = 1, 2).  Heavy group: 165Ho66+, 187Re74+, 207Pb81+, 209Bi82+ (Z = 67 to 83).
# Dictionary of the repo: cycles = R E / (hbar c), 1 cycle = 2 pi nats; bits = 2 pi cycles / ln 2; p12 = log_12 (R / l_P).  Atomic order: R = a0/Z, E = binding energy of the 1s state.  Nuclear order: R = charge radius.
# Sourced: explore/data/moment_benchmark_sourced_values.txt (hyperfine energies secondary), saved IAEA table (radii, binding, moments, quadrupole, masses).  Recalled: G (Planck mass, log scale only), u c^2 via m_e/u.
# The 1s radial density of the Dirac point-nucleus problem is P(r) ~ r^(2g) exp(-2 Z r / a0), g = sqrt(1 - (Z alpha)^2): used for the fraction of the electron inside the nucleus (point-nucleus wavefunction, no finite-size feedback).
# Run: py -3 -I -X utf8 -u explore/two_groups.py > explore/two_groups.out
import csv, os, math, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0; hbarc = hbar*c/e                 # eV m
ALPHA = 7.2973525643e-3; RY = 13.605693122990; meu = 5.485799090e-4; MPME = 1836.152673426; muB = 9.2740100657e-24
mec2 = hbar*c*ALPHA/ (hbarc/ (hbarc))  # placeholder, replaced below
me = e*hbar/(2*muB); mec2 = me*c**2/e; lam_e = hbarc/mec2; a0 = lam_e/ALPHA; uc2 = mec2/meu/1e6                    # u c^2 in MeV
G = 6.67430e-11; mP_c2 = math.sqrt(hbar*c**5/G)/e; lP = math.sqrt(hbar*G/c**3); muN = muB/MPME
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
def spin(jp):
    s = jp.rstrip('+-'); a, _, b = s.partition('/'); return float(a)/float(b) if b else float(a)
ions = [('H', 1, 0, 5.874326e-6, 0.84075), ('D', 1, 1, 1.353953e-6, None), ('3He+', 2, 1, 3.583825e-5, None), ('165Ho66+', 67, 98, 2.164566, None), ('187Re74+', 75, 112, 2.747877, None), ('207Pb81+', 82, 125, 1.215889, None), ('209Bi82+', 83, 126, 5.0840, None)]
D = {}
for name, Z, N, Ehfs, rN in ions:
    r = get(Z, N); A = Z+N; mu = abs(float(r['magnetic_dipole'])); I = spin(r['jp']); Rn = (rN if rN else float(r['radius']))*1e-15; Q = r['electric_quadrupole']
    M_MeV = float(r['atomic_mass'])*1e-6*uc2 - Z*mec2/1e6; Mc2 = M_MeV*1e6; lamN = hbarc/Mc2; Bt = float(r['binding'])*1e-3*A if r['binding'] else 0.0
    g = math.sqrt(1-(Z*ALPHA)**2); ED = mec2*(1-g); Re = a0/Z; Enr = Z**2*RY
    cyc_nr = Z*ALPHA/2; cyc_D = (1-g)/(Z*ALPHA); lam_ph = h*c/(Ehfs*e); Rm = 2*mu*muN/(e*c)
    x = 2*Z*Rn/a0; Pin = float(mp.gammainc(2*g+1, 0, x, regularized=True)); Pin_nr = float(mp.gammainc(3, 0, x, regularized=True))
    D[name] = dict(Z=Z, A=A, I=I, mu=mu, Q=Q, Rn=Rn, M=M_MeV, lamN=lamN, Bt=Bt, g=g, ED=ED, Enr=Enr, Re=Re, cyc_nr=cyc_nr, cyc_D=cyc_D, Ehfs=Ehfs, lam_ph=lam_ph, Rm=Rm, Pin=Pin, Pin_nr=Pin_nr, s=1/(Z*ALPHA))
print(f'hbar c = {hbarc:.6e} eV m ; a0 = {a0:.6e} m ; lambda_e = {lam_e:.6e} m ; m_P c^2 = {mP_c2/1e9:.4e} GeV (G recalled) ; u c^2 = {uc2:.5f} MeV')
names = [n for n, *_ in ions]
def row(label, key, fmt='{:12.4e}', f=lambda v: v):
    print(f'{label:46s}' + ''.join(fmt.format(f(D[n][key])).rjust(13) for n in names))
print('\n' + ' '*46 + ''.join(n.rjust(13) for n in names) + '\n' + ' '*46 + 'light'.rjust(13)*3 + 'heavy'.rjust(13)*4)
print('--- ENERGY')
row('1s binding, non-relativistic Z^2 Ry (eV)', 'Enr'); row('1s binding, Dirac point nucleus (eV)', 'ED'); print(f'{"  Dirac / non-relativistic":46s}' + ''.join(f'{D[n]["ED"]/D[n]["Enr"]:13.5f}' for n in names))
row('orbital speed v/c = Z alpha', 'g', '{:13.5f}', lambda g: math.sqrt(1-g**2)); row('hyperfine splitting (eV)', 'Ehfs'); print(f'{"  hyperfine / 1s binding":46s}' + ''.join(f'{D[n]["Ehfs"]/D[n]["ED"]:13.3e}' for n in names))
row('hyperfine photon wavelength (m)', 'lam_ph')
print('--- INFORMATION (cycles = R E / hbar c, bits = 2 pi cycles / ln 2)')
row('atomic order, cycles (R = a0/Z, E = Dirac 1s)', 'cyc_D', '{:13.6f}'); print(f'{"  atomic order, bits":46s}' + ''.join(f'{D[n]["cyc_D"]*2*math.pi/math.log(2):13.4f}' for n in names))
print(f'{"  atomic order, cycles, non-relativistic Z a/2":46s}' + ''.join(f'{D[n]["cyc_nr"]:13.6f}' for n in names))
print(f'{"  fraction of one full registration":46s}' + ''.join(f'{D[n]["cyc_D"]:13.5f}' for n in names) + '   (1.0 at Z alpha = 1, where a0/Z = lambda_e and E_1s = m_e c^2)')
print(f'{"nuclear order, cycles R_N B / hbar c":46s}' + ''.join(f'{D[n]["Rn"]*D[n]["Bt"]*1e6/hbarc:13.4f}' if D[n]['Bt'] > 0 else '            -' for n in names))
print(f'{"  nuclear order, bits":46s}' + ''.join(f'{D[n]["Rn"]*D[n]["Bt"]*1e6/hbarc*2*math.pi/math.log(2):13.2f}' if D[n]['Bt'] > 0 else '            -' for n in names))
print(f'{"nuclear size in its own Compton lengths R_N/lambda_N":46s}' + ''.join(f'{D[n]["Rn"]/D[n]["lamN"]:13.2f}' for n in names))
print('--- MASS AND SIZE')
row('nuclear mass (MeV)', 'M'); print(f'{"  nuclear mass / m_e":46s}' + ''.join(f'{D[n]["M"]*1e6/mec2:13.1f}' for n in names)); print(f'{"  gravitational coupling (M/m_P)^2":46s}' + ''.join(f'{(D[n]["M"]*1e6/mP_c2)**2:13.3e}' for n in names))
row('nuclear charge radius (m)', 'Rn'); row('electron order size a0/Z (m)', 'Re'); print(f'{"  size ratio atomic / nuclear order R_e/R_N":46s}' + ''.join(f'{D[n]["Re"]/D[n]["Rn"]:13.1f}' for n in names))
print(f'{"  p12 above l_P, nuclear order":46s}' + ''.join(f'{math.log(D[n]["Rn"]/lP)/math.log(12):13.3f}' for n in names)); print(f'{"  p12 above l_P, atomic order":46s}' + ''.join(f'{math.log(D[n]["Re"]/lP)/math.log(12):13.3f}' for n in names))
print(f'{"  size ratio atomic order / electron Compton s":46s}' + ''.join(f'{D[n]["s"]:13.3f}' for n in names))
print('--- OVERLAP AND STRUCTURE')
print(f'{"fraction of the 1s electron inside the nucleus (Dirac)":46s}' + ''.join(f'{D[n]["Pin"]:13.3e}' for n in names)); print(f'{"  same, non-relativistic radial density":46s}' + ''.join(f'{D[n]["Pin_nr"]:13.3e}' for n in names))
row('nuclear spin I', 'I', '{:13.1f}'); print(f'{"  multiplicity (2I+1)/(2I)":46s}' + ''.join(f'{(2*D[n]["I"]+1)/(2*D[n]["I"]):13.4f}' for n in names))
row('nuclear moment (mu_N)', 'mu', '{:13.4f}'); print(f'{"quadrupole moment (barn; blank = none)":46s}' + ''.join(f'{(D[n]["Q"] or "-"):>13s}' for n in names))
row('moment-equivalent ring radius R_mag (m)', 'Rm'); print(f'{"  R_mag / R_N":46s}' + ''.join(f'{D[n]["Rm"]/D[n]["Rn"]:13.4f}' for n in names))
print('\n--- group ranges (heavy / light) ---')
L = ['H', 'D', '3He+']; Hh = ['165Ho66+', '187Re74+', '207Pb81+', '209Bi82+']
def span(vals): return min(vals), max(vals)
for label, key in (('1s Dirac energy (eV)', 'ED'), ('hyperfine energy (eV)', 'Ehfs'), ('atomic cycles', 'cyc_D'), ('nuclear mass (MeV)', 'M'), ('hyperfine wavelength (m)', 'lam_ph')):
    a, b = span([D[n][key] for n in L]); c_, d = span([D[n][key] for n in Hh]); print(f'{label:28s} light {a:.3e} to {b:.3e}; heavy {c_:.3e} to {d:.3e}; heavy over light {c_/b:.2e} to {d/a:.2e}')
a, b = span([D[n]['Re']/D[n]['Rn'] for n in L]); c_, d = span([D[n]['Re']/D[n]['Rn'] for n in Hh]); print(f'{"size ratio R_e/R_N":28s} light {a:.3e} to {b:.3e}; heavy {c_:.3e} to {d:.3e}')
a, b = span([D[n]['Pin'] for n in L]); c_, d = span([D[n]['Pin'] for n in Hh]); print(f'{"fraction inside nucleus":28s} light {a:.3e} to {b:.3e}; heavy {c_:.3e} to {d:.3e}; heavy over light {c_/b:.2e} to {d/a:.2e}')
