# Both electroweak couplings with the Kaluza-Klein tower: does SU(2) screen above 1/R, and where do 1/alpha_Y and 1/alpha_2 reach zero? One-loop, exact threshold counting, one dimension (masses n/R); new file; nothing fitted.
# Content: floor hypercharges (M6 C1.4) for 3 generations of Weyl fermions with SM SU(3)xSU(2) assignments, one Higgs doublet, SU(2) gauge field; inputs recalled: 1/alpha_em(m_Z) = 127.951, sin^2 theta_W = 0.23122.
# b = -(11/3) C_A + (2/3) sum_Weyl T + (1/3) sum_complex scalars T  (SU(2): C_A = 2, T(doublet) = 1/2);  KK level n >= 1: massive vector (gauge + eaten A5 real adjoint scalar), Dirac partners of every fermion, one complex Higgs doublet.
# Run: py -3 -I -X utf8 -u explore/alpha_tower_su2.py > explore/alpha_tower_su2.out
from math import log, pi, lgamma, floor, exp
from fractions import Fraction as Fr
mZ = 91.1876; MP = 1.220890e19; amz = 127.951; s2 = 0.23122
aY0 = (1 - s2)*amz; a20 = s2*amz
CA = 2; Tdoublet = Fr(1, 2)
n_doublets_per_gen = 3 + 1                       # Q_L (3 colours) and L
b2_gauge = Fr(-11, 3)*CA
b2_fermion = Fr(2, 3)*3*n_doublets_per_gen*Tdoublet      # three generations of Weyl doublets
b2_higgs = Fr(1, 3)*Tdoublet
b2 = b2_gauge + b2_fermion + b2_higgs
bt2_gauge = Fr(-11, 3)*CA + Fr(1, 6)*CA          # massive KK vector: gauge + eaten real adjoint scalar (C_A/6)
bt2_fermion = 2*b2_fermion                       # Dirac partners
bt2_higgs = b2_higgs
bt2 = bt2_gauge + bt2_fermion + bt2_higgs
print('SU(2) zero modes: gauge %s + fermions %s + Higgs %s = b_2 = %s (= %.4f)' % (b2_gauge, b2_fermion, b2_higgs, b2, float(b2)))
print('SU(2) per KK level: gauge+A5 %s + doubled fermions %s + Higgs %s = b_tilde_2 = %s (= %.4f)' % (bt2_gauge, bt2_fermion, bt2_higgs, bt2, float(bt2)))
print('so above 1/R each KK level screens SU(2) (b_tilde_2 > 0), but the 1/alpha_2 slope is %.3f vs %.3f for hypercharge (b_tilde_Y = 27/2)' % (float(bt2), 13.5))
bY, bt = 41/6, 13.5; b2f, bt2f = float(b2), float(bt2)
def inv_Y(mu, mu0):
    A = aY0 - bY/(2*pi)*log(mu0/mZ)
    if mu <= mu0: return aY0 - bY/(2*pi)*log(mu/mZ)
    x = mu/mu0; N = floor(x); return A - bY/(2*pi)*log(x) - bt/(2*pi)*(N*log(x) - lgamma(N + 1))
def inv_2(mu, mu0, btx=None):
    bb = bt2f if btx is None else btx
    A = a20 - b2f/(2*pi)*log(mu0/mZ)
    if mu <= mu0: return a20 - b2f/(2*pi)*log(mu/mZ)
    x = mu/mu0; N = floor(x); return A - b2f/(2*pi)*log(x) - bb/(2*pi)*(N*log(x) - lgamma(N + 1))
def zero(f, mu0, target=0.0):
    lo, hi = mu0, mu0*1e40
    if f(lo) <= target: return lo
    for _ in range(400):
        mid = (lo*hi)**0.5
        if f(mid) > target: lo = mid
        else: hi = mid
    return (lo*hi)**0.5
# radius that puts the hypercharge zero exactly at the Planck mass (as in alpha_tower_check)
lo, hi = 1e3, MP
for _ in range(300):
    mid = (lo*hi)**0.5
    if inv_Y(MP, mid) > 0: hi = mid
    else: lo = mid
mu0 = (lo*hi)**0.5
print()
print('tower scale with the hypercharge zero at the Planck mass: mu0 = %.5e GeV, R/l_P = %.3f' % (mu0, MP/mu0))
print('  at mu0: 1/alpha_Y = %.3f, 1/alpha_2 = %.3f, 1/alpha_em = %.3f' % (inv_Y(mu0, mu0), inv_2(mu0, mu0), inv_Y(mu0, mu0) + inv_2(mu0, mu0)))
print('  at the Planck mass: 1/alpha_Y = %.4f, 1/alpha_2 = %.3f, 1/alpha_em = %.3f' % (inv_Y(MP, mu0), inv_2(MP, mu0), inv_Y(MP, mu0) + inv_2(MP, mu0)))
LY = zero(lambda m: inv_Y(m, mu0), mu0); L2 = zero(lambda m: inv_2(m, mu0), mu0)
print('  1/alpha_Y reaches zero at %.4e GeV (Lambda/mu0 = %.2f levels); 1/alpha_2 reaches zero at %.4e GeV (Lambda/mu0 = %.2f levels): the SU(2) zero needs %.1f times as many levels' % (LY, LY/mu0, L2, L2/mu0, (L2/mu0)/(LY/mu0)))
print('  at the SU(2) zero scale 1/alpha_Y is %.3e (hypercharge long past its pole)' % inv_Y(L2, mu0))
# extra SU(2) content needed so that both vanish at the Planck mass for this tower: solve the per-level SU(2) coefficient
x = MP/mu0; N = floor(x); S = N*log(x) - lgamma(N + 1)
need = (a20 - b2f/(2*pi)*log(mu0/mZ) - b2f/(2*pi)*log(x))*2*pi/S
extra_dirac_doublets = (need - bt2f)/(2*float(Tdoublet)*2/3)
print('  per-level SU(2) coefficient needed for 1/alpha_2 = 0 at the Planck mass: b_tilde_2 = %.3f (SM content gives %.3f); the difference is %.2f Dirac SU(2) doublets per level (each adds 2/3 x 2 x 1/2 = 2/3)' % (need, bt2f, extra_dirac_doublets))
print('  and the sin^2 theta_W it would then imply is undetermined: both couplings infinite there, ratio = (limit), not a number')
