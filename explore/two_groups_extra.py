# Follow-ups to two_groups.py.  New file (2026-11-02); nothing fitted.  Exploratory; the look-elsewhere caveat applies to every coincidence noticed here.
# 1. The ratio of the nuclear order's registration cycles (R_N B / hbar c) to the atomic order's (R = a0/Z, E = Dirac 1s binding: (1 - g)/(Z alpha)) for every stable nuclide in the saved IAEA table with a charge radius and a binding energy,
#    and where that ratio crosses 1/alpha.
# 2. The Lorentz angle theta = arcsin(Z alpha) of the 1s electron (v/c = sin theta, gamma = cos theta) for both groups, the position of the Dirac hyperfine pole (gamma = 1/2, theta = 60 deg), the atomic cycles there, and the
#    framework's angles for comparison (36 deg = pi/5, the 600-cell edge arc; 60 deg = pi/3, the cone angle; the lean xi = arcsin(sqrt3/3)).
# Run: py -3 -I -X utf8 -u explore/two_groups_extra.py > explore/two_groups_extra.out
import csv, os, math
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0; hbarc = hbar*c/e; ALPHA = 7.2973525643e-3
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def cyc_atomic(Z):
    g = math.sqrt(1-(Z*ALPHA)**2); return (1-g)/(Z*ALPHA)
data = []
for r in rows:
    try:
        Z = int(r['z']); N = int(r['n'])
        if Z < 3 or Z > 100 or r['half_life'] != 'STABLE' or not r['radius'] or not r['binding']: continue
        Rn = float(r['radius'])*1e-15; A = Z+N; B = float(r['binding'])*1e-3*A*1e6
        data.append((Z, A, Rn*B/hbarc, cyc_atomic(Z), Rn*B/hbarc/cyc_atomic(Z)))
    except ValueError: continue
data.sort()
print(f'stable nuclides with a radius and a binding energy: {len(data)}; 1/alpha = {1/ALPHA:.4f}')
print(f'{"Z":>4s} {"A":>4s} {"nuclear cycles":>15s} {"atomic cycles":>14s} {"ratio":>9s} {"ratio x alpha":>14s}')
shown = set()
for Z, A, cn, ca, ra in data:
    if Z in (3, 6, 8, 14, 20, 26, 30, 40, 50, 60, 67, 75, 79, 82, 83, 90, 92) and Z not in shown:
        shown.add(Z); print(f'{Z:4d} {A:4d} {cn:15.4f} {ca:14.5f} {ra:9.2f} {ra*ALPHA:14.4f}')
within = [(Z, A, ra) for Z, A, cn, ca, ra in data if abs(ra*ALPHA-1) < 0.02]
print('stable nuclides with ratio within 2% of 1/alpha: Z, A =', ', '.join(f'{Z}/{A}' for Z, A, ra in within))
lo = [(Z, A, ra) for Z, A, cn, ca, ra in data if Z >= 60]
print('Z >= 60: ratio min %.2f max %.2f mean %.2f' % (min(r for *_, r in lo), max(r for *_, r in lo), sum(r for *_, r in lo)/len(lo)))
print('\nLorentz angle of the 1s electron, theta = arcsin(Z alpha):')
for name, Z in (('H, D', 1), ('3He+', 2), ('165Ho66+', 67), ('187Re74+', 75), ('207Pb81+', 82), ('209Bi82+', 83)):
    th = math.degrees(math.asin(Z*ALPHA)); print(f'  {name:9s} Z = {Z:2d}  Z alpha = {Z*ALPHA:.5f}  theta = {th:7.3f} deg   atomic cycles (1 - cos theta)/sin theta = {(1-math.cos(math.radians(th)))/math.sin(math.radians(th)):.5f}  = tan(theta/2) = {math.tan(math.radians(th)/2):.5f}')
print('  the atomic cycles of the 1s state are exactly tan(theta/2): (1 - cos t)/sin t = tan(t/2).')
print(f'  Dirac hyperfine pole: gamma = 1/2, theta = 60 deg, Z alpha = sqrt3/2 = {math.sqrt(3)/2:.5f}, Z = {math.sqrt(3)/2/ALPHA:.2f}; atomic cycles there = tan 30 deg = 1/sqrt3 = {1/math.sqrt(3):.5f}')
xi = math.asin(1/math.sqrt(3)); print(f'  the lean xi = arcsin(sqrt3/3) = {xi:.5f} rad = {math.degrees(xi):.4f} deg ; sin xi = 1/sqrt3 = {math.sin(xi):.5f}  (equal to the atomic cycles at the pole)')
print(f'  critical charge: theta = 90 deg at Z alpha = 1, Z = {1/ALPHA:.3f}; atomic cycles there = tan 45 deg = 1')
print(f'  Z alpha = sin 36 deg ({math.pi/5:.5f} rad = pi/5, the 600-cell edge arc): Z = {math.sin(math.pi/5)/ALPHA:.2f}; Z alpha = sin 30 deg: Z = {0.5/ALPHA:.2f}; heavy group theta = 29.3, 33.2, 36.8, 37.3 deg')
print('\nthe atomic order registers tan(theta/2) cycles; the exponent excess of the hyperfine energy in terms of theta:')
def pexc(th):
    g = math.cos(th); x = math.sin(th)**2; return x/g*(1/g + 2/(2*g-1))
for d in (0.5, 5, 15, 29.27, 33.18, 36.76, 37.28, 45, 55, 59, 59.9):
    print(f'  theta = {d:6.2f} deg: p - 3 = {pexc(math.radians(d)):10.4f}   atomic cycles {math.tan(math.radians(d)/2):.5f}')
