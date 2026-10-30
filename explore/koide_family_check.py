# Run quarks and neutrinos through the same family the floor uses for leptons: sqrt(m_k) proportional to a_k = 1 + A cos(2 pi k/3 + delta), Q = 1/3 + A^2/6 (floor F9, F15-F17, field_equations_v3.txt).
# Floor parameters as stated there: leptons A = sqrt(2), delta = 2/9 rad; down-type A = (sqrt2 + sqrt3)/2 (Q_down = (13 + 2 sqrt6)/24), delta_f = 2/(9k) with k = colocated channel count (down 2, up 3; IDENTIFICATION grade; the floor itself says the one-phase quark snapshot is REJECTED, running owed);
# up-type A^2_up = A^2_down + (7 - 2 sqrt6)/4 = 3 (the floor gives the isospin splitting of A^2; A_up = sqrt3 follows); neutrinos delta_nu = 12 deg + 21 eps/10 = 27.447817 deg, eps = 2 pi - 5 arccos(1/3) (A not stated for neutrinos; sqrt2 assumed here and flagged).
# Masses: PDG 2024 (saved in explore/data): quarks MS-bar (u, d, s at 2 GeV; c, b at their own mass; t direct) - scheme-mixed, so quark comparisons are good to tens of percent at best.
# Run: py -3 -I -X utf8 -u explore/koide_family_check.py > explore/koide_family_check.out
from math import cos, sqrt, pi, acos, radians, degrees
def fam(A, delta):
    return sorted((1 + A*cos(2*pi*k/3 + delta))**2 for k in range(3))
def Qof(m): return sum(m)/sum(sqrt(x) for x in m)**2
def solve_delta(A, target, which):
    # delta in (0, pi/3) range scan then bisection on ratio m[which]/m[0]
    best = None
    N = 20000
    prev = None
    for i in range(N + 1):
        d = i*(2*pi/3)/N
        m = fam(A, d); r = m[which]/m[0] if m[0] > 0 else float('inf')
        if prev is not None and (prev[1] - target)*(r - target) <= 0:
            lo, hi = prev[0], d
            for _ in range(100):
                mid = (lo + hi)/2; mm = fam(A, mid); rm = mm[which]/mm[0]
                if (mm[which]/mm[0] - target)*(fam(A, lo)[which]/fam(A, lo)[0] - target) <= 0: hi = mid
                else: lo = mid
            return (lo + hi)/2
        prev = (d, r)
    return None
PDG = dict(e=0.51099895, mu=105.6583755, tau=1776.93, u=2.16, d=4.70, s=93.5, c=1273.0, b=4183.0, t=172570.0)
print('LEPTONS (reference): A = sqrt2, delta = 2/9')
m = fam(sqrt(2), 2/9); print('  predicted m_mu/m_e = %.6f, m_tau/m_e = %.4f ; measured %.6f, %.4f ; Q = %.12f' % (m[1]/m[0], m[2]/m[0], PDG['mu']/PDG['e'], PDG['tau']/PDG['e'], Qof(m)))
print()
print('DOWN-TYPE: A = (sqrt2 + sqrt3)/2 = %.6f, Q_down = (13 + 2 sqrt6)/24 = %.6f' % ((sqrt(2) + sqrt(3))/2, (13 + 2*sqrt(6))/24))
Ad = (sqrt(2) + sqrt(3))/2
md = [PDG['d'], PDG['s'], PDG['b']]
print('  measured (d, s, b): m_s/m_d = %.3f, m_b/m_d = %.2f, Koide Q = %.5f' % (md[1]/md[0], md[2]/md[0], Qof(md)))
for lab, d in [('delta_f = 2/(9 k), k = 2  -> 1/9', 1/9)]:
    m = fam(Ad, d); print('  floor delta = %.6f: m_s/m_d = %.3f, m_b/m_d = %.2f, Q = %.5f' % (d, m[1]/m[0], m[2]/m[0], Qof(m)))
ds = solve_delta(Ad, md[1]/md[0], 1)
if ds is not None:
    m = fam(Ad, ds); print('  delta fitted to m_s/m_d = %.6f rad: then m_b/m_d = %.2f (measured %.2f)' % (ds, m[2]/m[0], md[2]/md[0]))
else: print('  no delta reproduces m_s/m_d = %.3f within this A' % (md[1]/md[0]))
db = solve_delta(Ad, md[2]/md[0], 2)
print('  delta fitted to m_b/m_d: %s' % ('%.6f rad -> m_s/m_d = %.3f' % (db, fam(Ad, db)[1]/fam(Ad, db)[0]) if db is not None else 'none'))
print()
Au = sqrt(3)
mu_ = [PDG['u'], PDG['c'], PDG['t']]
print('UP-TYPE: A_up = sqrt3 = %.6f (A^2_up - A^2_down = (7 - 2 sqrt6)/4 = %.6f), Q_up = 1/3 + 3/6 = %.6f' % (Au, (7 - 2*sqrt(6))/4, 1/3 + 3/6))
print('  measured (u, c, t): m_c/m_u = %.1f, m_t/m_u = %.0f, Koide Q = %.5f' % (mu_[1]/mu_[0], mu_[2]/mu_[0], Qof(mu_)))
m = fam(Au, 2/27); print('  floor delta = 2/27 = %.6f: m_c/m_u = %.1f, m_t/m_u = %.0f, Q = %.5f' % (2/27, m[1]/m[0], m[2]/m[0], Qof(m)))
du = solve_delta(Au, mu_[1]/mu_[0], 1)
if du is not None:
    m = fam(Au, du); print('  delta fitted to m_c/m_u = %.6f rad: then m_t/m_u = %.0f (measured %.0f)' % (du, m[2]/m[0], mu_[2]/mu_[0]))
else: print('  no delta reproduces m_c/m_u = %.1f within this A' % (mu_[1]/mu_[0]))
print('  quark masses are scheme- and scale-mixed (u, d, s at 2 GeV; c, b at their own mass; t direct): treat agreement better than ~30% as not meaningful and disagreement above a factor 2 as a clear miss')
print()
eps = 2*pi - 5*acos(1/3); dnu = radians(12.0) + 2.1*eps
print('NEUTRINOS: delta_nu = 12 deg + 21 eps/10 = %.6f deg (eps = %.8f rad); A = sqrt2 assumed (the floor row does not state A for neutrinos)' % (degrees(dnu), eps))
m = fam(sqrt(2), dnu)
r = (m[1]**2 - m[0]**2)/(m[2]**2 - m[1]**2)
dm21, dm32 = 7.53e-5, 2.455e-3
print('  family masses (arbitrary scale): %s ; m_2/m_1 = %.3f, m_3/m_1 = %.3f' % (['%.5f' % x for x in m], m[1]/m[0], m[2]/m[0]))
print('  predicted Delta m^2_21 / Delta m^2_32 = %.5f ; measured %.5f (7.53e-5 / 2.455e-3, PDG 2024 saved)' % (r, dm21/dm32))
s = sqrt(dm32/(m[2]**2 - m[1]**2))
mv = [s*x for x in m]
print('  anchoring the scale on Delta m^2_32: m1 = %.3e eV, m2 = %.4e eV, m3 = %.5f eV ; sum = %.5f eV (oscillation minimum 0.05898, cosmology bound 0.072 eV at 95%%)' % (mv[0], mv[1], mv[2], sum(mv)))
print('  with delta_nu stated as matched to a measured ratio (floor F17: inversion-then-match) the ratio above is not a test; the sum and the lightest mass are what the family would add.')
