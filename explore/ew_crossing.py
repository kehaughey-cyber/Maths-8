# Where do the SM electroweak couplings meet (sin^2 theta_W = 3/8 for alpha_1 = (5/3) alpha_Y = alpha_2)? One loop, no thresholds, recalled inputs: 1/alpha_em(m_Z) = 127.951, sin^2 theta_W = 0.23122, b_Y = 41/6, b_2 = -19/6, 1/alpha_3(m_Z) = 8.47 (alpha_s = 0.1180), b_3 = -7.
# Run: py -3 -I -X utf8 -u explore/ew_crossing.py > explore/ew_crossing.out
from math import log, pi, exp
mZ = 91.1876; amz = 127.951; s2 = 0.23122
aY = (1 - s2)*amz; a2 = s2*amz; a3 = 1/0.1180
bY, b2, b3 = 41/6, -19/6, -7.0
# sin^2 theta_W(mu) = alpha_Y/(alpha_Y + alpha_2) = (1/alpha_2)/(1/alpha_Y + 1/alpha_2); set equal to 3/8
# (a2 - b2 L/2pi) = 3/8 [ (aY - bY L/2pi) + (a2 - b2 L/2pi) ]  ->  solve for L
k = 1/(2*pi); t = 3/8
L = (a2 - t*(aY + a2))/(k*(b2 - t*(bY + b2)))
mu = mZ*exp(L)
iy = aY - bY*k*L; i2 = a2 - b2*k*L; i3 = a3 - b3*k*L
print('sin^2 theta_W = 3/8 at ln(mu/m_Z) = %.3f, mu = %.4e GeV' % (L, mu))
print('there 1/alpha_Y = %.3f, 1/alpha_1 (GUT normalised, = 3/5 x 1/alpha_Y) = %.3f, 1/alpha_2 = %.3f, 1/alpha_3 = %.3f' % (iy, 0.6*iy, i2, i3))
print('at the Planck mass 1.22e19 GeV: sin^2 theta_W = %.4f' % (lambda LL: (a2 - b2*k*LL)/((aY - bY*k*LL) + (a2 - b2*k*LL)))(log(1.22089e19/mZ)))
