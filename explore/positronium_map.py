# Positronium translation: Greek (BC cycles) + scale-ladder positions + checks for the floor-vocabulary reading.
# New file; floor untouched. cycles = R E/(hbar c); one cycle = 12 radits = 30 ticks = 2 pi nats = 2 pi/ln2 bits.
from mpmath import mp, mpf, pi, log, sqrt, nstr
mp.dps = 20
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); me = mpf('9.1093837015e-31')
al = mpf('7.2973525693e-3'); eV = mpf('1.602176634e-19'); Mpc = mpf('3.0856775814913673e22')
H0 = mpf('67.4e3')/Mpc
l12 = lambda x: log(x)/log(12)
l10 = lambda x: log(x, 10)
ln2 = log(2)
lam_e = hbar/(me*c); M = 2*me; lam_Ps = hbar/(M*c); a_Ps = 2*lam_e/al; r_e = al*lam_e
lP = sqrt(hbar*G/c**3); tP = sqrt(hbar*G/c**5); mP = sqrt(hbar*c/G); mnu = mpf('0.05')*eV/c**2
RH = c/H0; MH = c**3/(2*G*H0); cyH = RH**2/(2*lP**2); tH = 1/H0
cy = lambda R, E: R*E/(hbar*c)
Eb = al**2*me*c**2/4; w_e = me*c**2/hbar

print('INPUTS: alpha', al, ' m_e', me, ' hbar', hbar, ' G', G, ' H0(s^-1)', H0, ' neutrino 0.05 eV (rough)')
print('lengths: lam_e', lam_e, ' lam_Ps', lam_Ps, ' r_e', r_e, ' a_Ps', a_Ps)
print()

print('PART A  Greek: BC cycles for each positronium row (form = alpha^k x q)')
rows = [('Ps rest @ own Compton cut', lam_Ps, M*c**2, 'alpha^0 x 1'),
        ('Ps rest @ a_Ps', a_Ps, M*c**2, 'alpha^-1 x 4'),
        ('binding E_b = alpha^2 m c^2/4 @ a_Ps', a_Ps, Eb, 'alpha^1 x 1/2'),
        ('1S-2S (3/4 of E_b) @ a_Ps', a_Ps, mpf(3)/4*Eb, 'alpha^1 x 3/8'),
        ('hyperfine (7/12) alpha^4 m c^2 (leading) @ a_Ps', a_Ps, mpf(7)/12*al**4*me*c**2, 'alpha^3 x 7/6'),
        ('annihilation photon 511 keV @ lambda/(2pi)', lam_e, me*c**2, 'alpha^0 x 1')]
print(f'  {"row":52s} {"cycles":>26s} {"radits":>14s} {"ticks":>14s} {"bits":>14s}  form')
for n, R, E, f in rows:
    x = cy(R, E)
    print(f'  {n:52s} {nstr(x,20):>26s} {nstr(12*x,10):>14s} {nstr(30*x,10):>14s} {nstr(2*pi*x/ln2,10):>14s}  {f}')
print('  gravity pair G m_e^2/(hbar c) = (m_e/m_P)^2  ', (me/mP)**2, ' (cycles carried by the 1/R potential)')
print()

print('PART B  rates in electron-Compton-rate units (omega_e = m_e c^2/hbar =', w_e, 'rad/s) and persistence')
G_p = al**5/2
G_o = 2*(pi**2-9)/(9*pi)*al**6
G_om = 1/(mpf('142.05e-9')*w_e)
for n, g in [('para (2 gamma) = alpha^5/2', G_p), ('ortho leading 2(pi^2-9)/(9pi) alpha^6', G_o), ('ortho measured 142.05 ns', G_om)]:
    print(f'  {n:42s} rate/omega_e = {nstr(g,12):>18s}  tau = {nstr(1/(g*w_e)*mpf(10)**9,10):>14s} ns   persistence = {nstr(1/g,10):>16s} electron-Compton cycles   coef of alpha^k: {nstr(g/al**5,8)} (k=5), {nstr(g/al**6,8)} (k=6)')
Psi0 = 1/(pi*a_Ps**3)
print('  |psi(0)|^2 = 1/(pi a_Ps^3) =', Psi0, ' m^-3 ; hydrogen 1/(pi a0^3)/8 =', 1/(pi*(a_Ps/2)**3)/8)
print('  Gamma = c * 4 pi r_e^2 * |psi(0)|^2 =', c*4*pi*r_e**2*Psi0, ' s^-1 ;  alpha^5 omega_e/2 =', G_p*w_e, ' s^-1')
print()

print('PART C  positions on the scale ladders (decades above the anchor, powers of 12 above the anchor)')
print(f'  {"item":34s} {"value":>14s} {"decades":>10s} {"p12":>10s}   ladder')
for n, R in [('lambda_Ps', lam_Ps), ('r_e = alpha lambda_e (inner)', r_e), ('lambda_e', lam_e), ('a_Ps (outer)', a_Ps)]:
    print(f'  {n:34s} {nstr(R,8):>14s} {nstr(l10(R/lP),6):>10s} {nstr(l12(R/lP),6):>10s}   length: Planck length -> Hubble radius (60.93 decades, 56.46 p12)')
for n, m in [('electron mass', me), ('Ps mass 2 m_e', M)]:
    print(f'  {n:34s} {nstr(m,8):>14s} {nstr(l10(m/mnu),6):>10s} {nstr(l12(m/mnu),6):>10s}   mass: 0.05 eV neutrino -> Hubble-sphere mass')
for n, t in [('p-Ps lifetime', 1/(G_p*w_e)), ('o-Ps lifetime (measured)', mpf('142.05e-9')), ('electron Compton time hbar/(m c^2)', 1/w_e)]:
    print(f'  {n:34s} {nstr(t,8):>14s} {nstr(l10(t/tP),6):>10s} {nstr(l12(t/tP),6):>10s}   time: Planck time -> Hubble time (1/H0 =', nstr(tH,6), 's, ', nstr(l10(tH/tP),6), 'decades)')
x = cy(a_Ps, M*c**2)
print(f'  {"Ps cycles across a_Ps":34s} {nstr(x,8):>14s} {nstr(l10(x),6):>10s} {nstr(l12(x),6):>10s}   information: 1 cycle -> Hubble sphere ({nstr(cyH,8)} cycles, {nstr(l10(cyH),6)} decades)')
print('  Ps cycles / Hubble cycles =', x/cyH, '  decades below the horizon count:', l10(cyH/x))
print()

print('PART D  counts and checks used by the floor-vocabulary reading')
d1 = 12-2*5; d2 = 12-2*(12-5)
print('  signed defect (12-2d) for d=5 and its C-mirror d=7:', d1, d2, ' sum =', d1+d2)
print('  two registered bits ->', 2**2, 'spin states = 1 + 3 =', 1+3, ';  12-shell irreps 1+3+3+5 =', 1+3+3+5)
r = a_Ps/lam_Ps
print('  a_Ps / lambda_Ps =', r, '  (= 4/alpha =', 4/al, ')')
print('  flat-ball count 1+3r(r+1) at r = a_Ps/lambda_Ps (ASSUMES one hop = one Compton length) =', 1+3*r*(r+1))
print('  1/alpha =', 1/al, ' log12 =', l12(1/al), ' ; 2/alpha log12 =', l12(2/al), ' ; 4/alpha log12 =', l12(4/al))
