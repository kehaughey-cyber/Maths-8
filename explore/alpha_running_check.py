# Does "bare coupling unity at a floor scale" survive the Standard Model running of 1/alpha_em? One-loop arithmetic only; new file; nothing fitted.
# Inputs: 1/alpha_em(m_Z) = 127.951 (PDG, recalled), sin^2 theta_W(m_Z) = 0.23122 (recalled), SM one-loop coefficients b_Y = 41/6 (hypercharge, Q = T3 + Y), b_2 = -19/6 (textbook values), 1/alpha(0) = 137.035999 (CODATA 2022: alpha = 7.2973525643e-3 gives 137.035999177).
# 1/alpha_i(mu) = 1/alpha_i(m_Z) - b_i/(2 pi) ln(mu/m_Z);  1/alpha_em = 1/alpha_Y + 1/alpha_2.  No thresholds other than starting at m_Z; no new physics. m_e -> m_Z is taken from the measured pair 137.036 -> 127.951.
# Run: py -3 -I -X utf8 -u explore/alpha_running_check.py > explore/alpha_running_check.out
from math import log, pi, exp
a0inv = 137.035999177; amz = 127.951; s2 = 0.23122; mZ = 91.1876; mP = 1.220890e19; me = 0.51099895e-3
bY, b2 = 41/6, -19/6
aYinv = (1 - s2)*amz; a2inv = s2*amz
def inv(mu):
    L = log(mu/mZ); y = aYinv - bY/(2*pi)*L; w = a2inv - b2/(2*pi)*L; return y, w, y + w
print('1/alpha_Y(m_Z) = %.4f, 1/alpha_2(m_Z) = %.4f, sum = %.4f' % (aYinv, a2inv, amz))
print('slope of 1/alpha_em above m_Z: d(1/alpha_em)/d ln mu = %.6f per e-fold (hypercharge %.6f, SU(2) %+.6f)' % (-(bY + b2)/(2*pi), -bY/(2*pi), -b2/(2*pi)))
print('fermions only (all three generations, sum N_c Q^2 = 8): -(2/(3 pi)) x 8 = %.6f per e-fold; W and Higgs change the net slope to the line above' % (-(2/(3*pi))*8))
for nm, mu in [('1 TeV', 1e3), ('1e10 GeV', 1e10), ('1e16 GeV', 1e16), ('Planck mass 1.22e19 GeV', mP)]:
    y, w, t = inv(mu); print('  at %-26s 1/alpha_Y = %8.3f  1/alpha_2 = %8.3f  1/alpha_em = %8.3f' % (nm, y, w, t))
y, w, t = inv(mP)
efold_total = log(mP/me)
print('e-folds from m_e to the Planck mass: %.3f (m_e -> m_Z: %.3f, m_Z -> m_P: %.3f)' % (efold_total, log(mZ/me), log(mP/mZ)))
for target, lab in [(1.0, 'alpha = 1 (e = 1 in Gaussian-like units)'), (4*pi, 'alpha = 1/(4 pi) (e = 1 in Heaviside-Lorentz)')]:
    need = a0inv - target
    print('  to reach 1/alpha = %.4f (%s): total drop needed %.3f over %.2f e-folds = %.3f per e-fold' % (target, lab, need, efold_total, need/efold_total))
sup = a0inv - t
print('  supplied by one-loop SM from m_e to the Planck mass: %.3f over %.2f e-folds = %.3f per e-fold (measured 137.036 -> 127.951 below m_Z, one-loop line above)' % (sup, efold_total, sup/efold_total))
for target in (1.0, 4*pi): print('  shortfall factor to reach %.4f: needed / supplied = %.3f' % (target, (a0inv - target)/sup))
Lpole = aYinv/(bY/(2*pi))
print('one-loop Landau pole of alpha_Y: ln(mu/m_Z) = %.2f, mu = %.3e GeV; there 1/alpha_2 = %.3f, so 1/alpha_em = %.3f (never reaches 1 or %.3f)' % (Lpole, mZ*exp(Lpole), a2inv - b2/(2*pi)*Lpole, a2inv - b2/(2*pi)*Lpole, 4*pi))
