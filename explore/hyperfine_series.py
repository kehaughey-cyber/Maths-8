# The hyperfine inference examined: hydrogen, deuterium, 3He+.  New file (2026-11-02); nothing fitted.
# Two routes are compared with the measured splittings:
#  (A) the geometric / rung-size form, no free coupling:  hfs / Ry = (8/3) [(2I+1)/(2I)] Z^3 (R_mag,X / a0)(lambda_e / a0) x (1 + m_e/M)^-3,  R_mag,X = 2|mu_X|/(e c)  (the radius at which a charge circling at c has the nuclear moment),
#      lambda_e = hbar/(m_e c), a0 = lambda_e/alpha (the rung ratio a0/lambda_e = 1/alpha).  Equivalent to (8/3)[(2I+1)/(2I)] (mu_X/mu_B) Z^3 alpha^2 Ry (1+m_e/M)^-3.
#  (B) the instrument route as calibrated on hydrogen: the splitting is linear in the moment of the nuclear ring (weak coupling), so X/H = mu_X / mu_p, with the same coupling and nothing else.
# Sourced: explore/data/moment_benchmark_sourced_values.txt (CODATA 2022 mu_B, alpha, Ry, m_p/m_e; hyperfine frequencies, secondary), saved IAEA table (moments, spins, atomic masses).  m_e/u recalled (1e-3-level correction only).
# Run: py -3 -I -X utf8 -u explore/hyperfine_series.py > explore/hyperfine_series.out
import csv, os, math
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0
muB = 9.2740100657e-24; mue = 9.2847646917e-24; MPME = 1836.152673426; ALPHA = 7.2973525643e-3; RY = 13.605693122990; meu = 5.485799090e-4
me = e*hbar/(2*muB); muN = muB/MPME; lam_e = hbar/(me*c); a0 = lam_e/ALPHA
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
def spin(jp):
    s = jp.rstrip('+-'); a, _, b = s.partition('/'); return float(a)/float(b) if b else float(a)
systems = [('H', 1, 0, 1420405751.768, 'Hellwig 1970 (as cited on the hydrogen-line page)'), ('D', 1, 1, 327384352.5222, 'Wineland & Ramsey 1972'),
           ('3He+ (1969)', 2, 1, 8665649867.0, 'Schuessler, Fortson & Dehmelt 1969'), ('3He+ (2022)', 2, 1, 8665649865.77, 'Schneider et al. 2022')]
print('rung ratio a0 / lambda_e =', repr(a0/lam_e), ' = 1/alpha =', repr(1/ALPHA), '(by definition; carries no new information)')
print('lambda_e =', lam_e, 'm ; a0 =', a0, 'm\n')
print("(Ap) is (A) with the electron measured moment |mu_e| = 1.00115965 mu_B in place of mu_B (CODATA 2022, sourced).")
print(f'{"system":12s} {"Z":>2s} {"I":>4s} {"mu (mu_N)":>11s} {"(2I+1)/(2I)":>11s} {"M/m_e":>10s} {"measured hfs/Ry":>16s} {"(A) prediction":>16s} {"A/measured":>11s} {"Ap/measured":>12s} {"R_mag/a0":>11s}')
res = {}
for name, Z, N, nu, ref in systems:
    r = get(Z, N); mu = abs(float(r['magnetic_dipole'])); I = spin(r['jp']); m_atom_u = float(r['atomic_mass'])*1e-6; M = (m_atom_u - Z*meu)/meu
    meas = h*nu/e/RY; Rm = 2*mu*muN/(e*c); fac = (2*I+1)/(2*I)
    pred = (8/3)*fac*Z**3*(Rm/a0)*(lam_e/a0)*(1+1/M)**-3
    res[name] = (meas, pred, mu, I, Z, M, nu)
    print(f'{name:12s} {Z:2d} {I:4.1f} {mu:11.7f} {fac:11.4f} {M:10.2f} {meas:16.6e} {pred:16.6e} {pred/meas:11.6f} {pred*mue/muB/meas:12.6f} {Rm/a0:11.4e}')
print('\n(A) check without the reduced-mass factor, hydrogen: ', (8/3)*2*(res['H'][2]*muN*2/(e*c)/a0)*(lam_e/a0), 'against measured', res['H'][0])
print('\nratios to hydrogen:')
mH, pH, muH, IH, ZH, MH, nuH = res['H']
print(f'{"system":12s} {"measured X/H":>14s} {"(A) X/H":>12s} {"A/measured":>11s} {"(B) mu_X/mu_p":>14s} {"B/measured":>11s}  what (B) is missing')
for name in ('D', '3He+ (1969)', '3He+ (2022)'):
    meas, pred, mu, I, Z, M, nu = res[name]
    B = mu/muH
    print(f'{name:12s} {meas/mH:14.6f} {pred/pH:12.6f} {(pred/pH)/(meas/mH):11.6f} {B:14.6f} {B/(meas/mH):11.6f}  factor needed {(meas/mH)/B:.4f} = (2I+1)/(2I) ratio {((2*I+1)/(2*I))/2:.4f} x Z^3 {Z**3} x reduced mass')
print('\nthe two 3He+ values differ by', (8665649867.0-8665649865.77), 'Hz =', (8665649867.0-8665649865.77)/8665649867.0, 'relative; the formula-versus-measured gaps are 1e-4 to 1e-3, set by QED, Breit and nuclear-structure corrections that (A) does not include.')
print('\nthe instrument-calibrated coupling mu_r from hydrogen (e_series_response.out: 1.2531e-4 at rho_B = 1, 1.2098e-6 at rho_B = 1/1836.15) enters (B) only through the common factor, which cancels in X/H.')
