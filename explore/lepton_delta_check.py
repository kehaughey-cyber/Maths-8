# Floor F15/F16 (floor/field_equations_v3.txt lines 242, 270-272): charged-lepton masses from the Q = 2/3 amplitude family sqrt(m_k) proportional to 1 + sqrt(2) cos(2 pi k/3 + delta),
# with delta = 2/9 rad claimed from the floor (numerator 2 = the double cover's doubling, denominator 9 = the extremal winding's lag budget; metering step = the single priced IDENTIFICATION).
# This script only does the arithmetic of that claim: ratios at delta = 2/9, the delta that each measured ratio would need, and the comparison with PDG 2024. New file; nothing fitted (delta = 2/9 is the floor's number, not tuned here).
# Run: py -3 -I -X utf8 -u explore/lepton_delta_check.py > explore/lepton_delta_check.out
from math import cos, sqrt, pi
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
dmu, dtau = 0.0000024, 0.09                       # PDG 2024 uncertainties (MeV) as read from the saved leptons table: mu +-0.0000023..., tau +-0.09
def masses(delta):
    s = sorted((1 + sqrt(2)*cos(2*pi*k/3 + delta))**2 for k in range(3)); return s
def ratios(delta):
    s = masses(delta); return s[1]/s[0], s[2]/s[0]
def Q(delta):
    s = masses(delta); return sum(s)/sum(sqrt(x) for x in s)**2
d0 = 2/9
r = ratios(d0)
print('delta = 2/9 = %.10f rad;  Koide Q(delta) = %.12f (2/3 = %.12f)' % (d0, Q(d0), 2/3))
print('predicted  m_mu/m_e = %.6f   m_tau/m_e = %.5f   m_tau/m_mu = %.6f' % (r[0], r[1], r[1]/r[0]))
print('measured   m_mu/m_e = %.6f   m_tau/m_e = %.5f   m_tau/m_mu = %.6f   (PDG 2024, saved)' % (mmu/me, mtau/me, mtau/mmu))
print('difference m_mu/m_e: %+.3e relative;  m_tau/m_e: %+.3e relative;  tau uncertainty alone: %.3e relative (%.2f sigma)' % (r[0]/(mmu/me) - 1, r[1]/(mtau/me) - 1, dtau/mtau, (r[1]/(mtau/me) - 1)/(dtau/mtau)))
print()
# which delta does each measured ratio require?
def solve(target, which):
    lo, hi = 0.0, 0.5
    f = lambda d: ratios(d)[which] - target
    for _ in range(200):
        mid = (lo + hi)/2
        if f(lo)*f(mid) <= 0: hi = mid
        else: lo = mid
    return (lo + hi)/2
dm = solve(mmu/me, 0); dt = solve(mtau/me, 1)
print('delta required by m_mu/m_e   = %.10f  (2/9 = %.10f; difference %+.3e rad)' % (dm, d0, dm - d0))
print('delta required by m_tau/m_e  = %.10f  (2/9 = %.10f; difference %+.3e rad)' % (dt, d0, dt - d0))
print('delta required by m_tau/m_e from the +-0.09 MeV tau uncertainty: %.10f to %.10f' % (solve((mtau + dtau)/me, 1), solve((mtau - dtau)/me, 1)))
print()
print('what this is: with delta left free, the family (Q = 2/3 plus an overall mass M and one phase delta) has two parameters for three masses; it predicts the Koide relation Q = 2/3 and nothing else.')
print('measured Koide Q(e, mu, tau) = %.10f ; 2/3 = %.10f ; difference %+.3e' % ((me + mmu + mtau)/(sqrt(me) + sqrt(mmu) + sqrt(mtau))**2, 2/3, (me + mmu + mtau)/(sqrt(me) + sqrt(mmu) + sqrt(mtau))**2 - 2/3))
print('with delta = 2/9 supplied by the floor and M anchored on m_e, the family gives m_mu/m_e and m_tau/m_e with no free parameter; the numerator 2 / denominator 9 argument and the metering step are not reproduced here.')

print()
print('the floor\'s refined phase (F16): delta = delta_nat - sigma = 12.7323526 degrees (quoted, not re-derived here; delta_nat = 4 pi/15 - arccos(1/3)/2 = 12.7356103 degrees)')
from math import acos, degrees, radians
dnat = 4*pi/15 - 0.5*acos(1/3)
print('  delta_nat recomputed: %.7f degrees = %.10f rad' % (degrees(dnat), dnat))
for lab, d in [('delta_nat', dnat), ('delta = 12.7323526 deg (floor, with the sag)', radians(12.7323526)), ('delta = 2/9 rad', 2/9)]:
    r = ratios(d)
    print('  %-46s m_mu/m_e = %.6f (%+.2e relative)   m_tau/m_e = %.5f (%+.2e relative, %.2f sigma_tau)' % (lab, r[0], r[0]/(mmu/me) - 1, r[1], r[1]/(mtau/me) - 1, (r[1]/(mtau/me) - 1)/(dtau/mtau)))
print('  measured m_mu/m_e is known to about 2e-8 relative, so any deviation above 1e-7 in that ratio is many sigma; m_tau/m_e is known to 5.1e-5 relative.')
