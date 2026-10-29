# Hydrogen map under BC. Replays to new files only; floor untouched.
# Map = the touches of mass (maps/mass_requirements.md) and coordinates/clocks
# (maps/degrees_of_freedom.md) evaluated for hydrogen with measured values.
# BC: I = 2 pi R E/(hbar c) nats, so cycles = I/(2 pi) = R E/(hbar c).
# One cycle = 12 radits = 30 ticks = 2 pi nats = 2 pi/ln2 bits (floor 32, 64).
from mpmath import mp, mpf, pi, log, sqrt, acos, nstr, nint
mp.dps = 20
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); e = mpf('1.602176634e-19'); h = 2*pi*hbar
al = mpf('7.2973525693e-3'); me = mpf('9.1093837015e-31'); mpr = mpf('1.67262192369e-27')
u = mpf('1.66053906660e-27'); mH = mpf('1.00782503223')*u
a0 = mpf('5.29177210903e-11'); Ry = mpf('13.605693122994')*e
G = mpf('6.67430e-11'); GF_GeV = mpf('1.1663788e-5'); mp_GeV = mpf('0.93827208816')
mec2 = me*c**2
ln2 = log(2)
def cyc(R, E): return R*E/(hbar*c)
lam = lambda m: hbar/(m*c)

print('INPUTS (CODATA 2018 / measured), unrounded as typed')
for n, v in [('alpha', al), ('m_e', me), ('m_p', mpr), ('m_H', mH), ('a0', a0), ('Ry (J)', Ry), ('hbar', hbar), ('G', G)]:
    print(f'  {n:8s} {v}')
print()

print('PART A  hydrogen map -> BC (R, E) pairs.  cycles = R E/(hbar c)')
print('  rate = E/(m_e c^2) = frequency in electron-Compton-cycle units (energy = registration rate)')
print('  coef = cycles / (alpha^k (m_e/m_p)^j) for the stated (k, j)')
rows = []
def add(name, touch, R, E, k, j):
    cy = cyc(R, E)
    rows.append((name, touch, R, E, cy, k, j))
add('e rest @ lambda_e', 'Compton/inertia', lam(me), mec2, -99, 0)
add('p rest @ lambda_p', 'Compton/inertia', lam(mpr), mpr*c**2, -99, 0)
add('H rest @ lambda_H', 'Compton/inertia', lam(mH), mH*c**2, -99, 0)
add('e rest @ a0', 'E=mc^2, relational cfg', a0, mec2, -1, 0)
add('p rest @ a0', 'E=mc^2, relational cfg', a0, mpr*c**2, -1, -1)
add('H rest @ a0', 'E=mc^2, relational cfg', a0, mH*c**2, -1, -1)
add('Rydberg binding @ a0', 'binding energy', a0, Ry, 1, 0)
add('1S-2S (nu=2466061413187035 Hz) @ a0', 'spectrum', a0, h*mpf('2466061413187035'), 1, 0)
add('2P3/2-2P1/2 (10969.04 MHz) @ a0', 'fine structure', a0, h*mpf('10969.04e6'), 3, 0)
add('Lamb 2S-2P (1057.845 MHz) @ a0', 'QED', a0, h*mpf('1057.845e6'), 3, 0)
add('hyperfine 1S (1420.405751768 MHz) @ a0', 'spin-spin', a0, h*mpf('1420.405751768e6'), 3, 1)
print(f'  {"entry":42s} {"cycles":>26s} {"radits":>16s} {"ticks":>16s} {"bits":>16s} {"rate":>14s} {"coef":>14s}')
for name, touch, R, E, cy, k, j in rows:
    coef = '-' if k == -99 else nstr(cy/(al**k*(me/mpr)**j), 10)
    print(f'  {name:42s} {nstr(cy,20):>26s} {nstr(12*cy,12):>16s} {nstr(30*cy,12):>16s} {nstr(2*pi*cy/ln2,12):>16s} {nstr(E/mec2,10):>14s} {coef:>14s}')
print()

print('PART A2  pure numbers in the map')
print('  m_p/m_e          ', mpr/me)
print('  1/alpha          ', 1/al)
print('  Ry/(m_H c^2)     ', Ry/(mH*c**2), ' (binding fraction of H mass; = (alpha^2/2)(m_e/m_H) =', al**2/2*me/mH, ')')
print('  Compton cycles per Bohr radian  1/alpha^2 =', 1/al**2)
print('  G m_p m_e/(hbar c)  gravity pair      ', G*mpr*me/(hbar*c))
print('  G_F m_p^2 (natural units, conv. caveat)', GF_GeV*mp_GeV**2)
print('  hyperfine coef theory-ish (4/3) g_p, g_p = 5.5856946893 ->', mpf(4)/3*mpf('5.5856946893'))
print()

print('PART B  common denominators: the map in alpha-powers')
print('  every R=a0 entry is  E/(m_e c^2)/alpha ; E/(m_e c^2) in {1, m_p/m_e, alpha^2/2, 3 alpha^2/8, alpha^4/16-ish, ...}')
print('  independent pure numbers needed by the hydrogen map:  alpha,  m_p/m_e  (plus g_p for hyperfine, plus QED logs for Lamb)')
print()

print('PART C  framework quantities with BC applied (cycles = value/2pi for angles)')
phi = (1+sqrt(5))/2
eps = 2*pi - 5*acos(mpf(1)/3)
fw = [('1 tick (2pi/30)', 2*pi/30), ('1 radit (2pi/12)', 2*pi/12), ('epsilon = 2pi-5 arccos(1/3)', eps), ('epsilon/10', eps/10),
      ('delta = 2/9 rad', mpf(2)/9), ('K = ln(phi)/15', log(phi)/15), ('2pi/5', 2*pi/5), ('2pi/3', 2*pi/3),
      ('arcsin(sqrt3/3) lean', mp.asin(sqrt(3)/3)), ('pi/6 (kappa/Lambda)', pi/6)]
print(f'  {"quantity":32s} {"rad":>18s} {"cycles":>18s} {"ticks":>14s} {"radits":>14s}')
for n, v in fw:
    print(f'  {n:32s} {nstr(v,14):>18s} {nstr(v/(2*pi),14):>18s} {nstr(30*v/(2*pi),10):>14s} {nstr(12*v/(2*pi),10):>14s}')
print('  gap = 1-phi/2     ', 1-phi/2, ' ; phi/2 =', phi/2)
print('  exp(2pi)/4        ', mp.e**(2*pi)/4, ' vs 1/alpha', 1/al, ' ratio', (1/al)/(mp.e**(2*pi)/4))
print()

print('PART D  integrality of hydrogen cycles in floor units (no search; two tests only)')
for name, touch, R, E, cy, k, j in rows:
    if cy > 1:
        print(f'  {name:42s} ticks={nstr(30*cy,14):>20s} frac={nstr(30*cy-nint(30*cy),6):>10s}   radits={nstr(12*cy,14):>20s} frac={nstr(12*cy-nint(12*cy),6):>10s}')
print()
print('PART E  alpha-ladder ratios (alpha, hydrogen binding, in floor units)')
print('  alpha in ticks  (30 alpha)   ', 30*al, '   alpha/2 in ticks (15 alpha)', 15*al)
print('  alpha/(eps/2pi)              ', al/(eps/(2*pi)))
print('  (alpha/2)/(K/2pi)            ', (al/2)/(log(phi)/15/(2*pi)))
