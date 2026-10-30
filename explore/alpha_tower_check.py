# Induced-hypercharge test with a Kaluza-Klein tower: where does 1/alpha_Y reach 0 if all Standard-Model charged content (3 generations of Weyl fermions + one Higgs doublet) sits in one compact extra dimension?
# One-loop arithmetic; new file; nothing fitted. The tower is exact threshold counting: each KK level n (mass n mu0) adds b_tilde to the Y beta coefficient above its mass.
#   zero modes: b_Y = 41/6 (3 x 20/9 fermions + 1/6 Higgs doublet), recomputed below from the hypercharges;  KK level: Dirac partners of every fermion (2 x 20/3) + one complex Higgs doublet (1/6) = 27/2.
#   1/alpha_Y(mu) = 1/alpha_Y(mu0) - (b_Y/2pi) ln(mu/mu0) - (b_tilde/2pi) sum_{n=1..floor(mu/mu0)} ln(mu/(n mu0))      for mu >= mu0 (one dimension, masses n/R).
# Inputs recalled (not a saved file): 1/alpha_em(m_Z) = 127.951, sin^2 theta_W = 0.23122. Hypercharges are the floor's (M6 C1.4): Y = (1/6, -1/2, -2/3, 1/3, 1) for (Q_L, L, u_R^c, d_R^c, e_R^c) up to the conjugation convention used for squares.
# Run: py -3 -I -X utf8 -u explore/alpha_tower_check.py > explore/alpha_tower_check.out
from math import log, pi, lgamma, exp, floor
from fractions import Fraction as Fr
mZ = 91.1876; MP = 1.220890e19; amz = 127.951; s2 = 0.23122
aYinv_mz = (1 - s2)*amz
# beta coefficient from content: Weyl fermion multiplets with (dimension of colour x weak, Y)
mult = [(6, Fr(1, 6)), (2, Fr(-1, 2)), (3, Fr(-2, 3)), (3, Fr(1, 3)), (1, Fr(1))]    # components, Y  (Q_L: 3x2, L: 2, u_R: 3, d_R: 3, e_R: 1)
sumY2 = sum(n*y*y for n, y in mult)
bf = Fr(2, 3)*sumY2*3                      # three generations, Weyl fermions
bH = Fr(1, 3)*(2*Fr(1, 4))                 # one complex Higgs doublet (Y = 1/2)
bY = bf + bH; bt = 2*bf/1 + bH             # KK level: fermions become Dirac (twice the Weyl value), Higgs doublet once
print('sum Y^2 per generation = %s; fermion b_Y (3 gen) = %s; Higgs = %s; zero-mode b_Y = %s (= %.4f); KK-level b_tilde = %s (= %.4f)' % (sumY2, bf, bH, bY, float(bY), bt, float(bt)))
bY, bt = float(bY), float(bt)
def inv_zero(mu): return aYinv_mz - bY/(2*pi)*log(mu/mZ)
def inv_tower(mu, mu0):
    A = inv_zero(mu0)
    if mu <= mu0: return inv_zero(mu)
    x = mu/mu0; N = floor(x)
    return A - bY/(2*pi)*log(x) - bt/(2*pi)*(N*log(x) - lgamma(N + 1))
def zero_at(mu0, target=0.0):
    lo, hi = mu0, MP*1e30
    f = lambda m: inv_tower(m, mu0) - target
    if f(lo) <= 0: return lo
    for _ in range(300):
        mid = (lo*hi)**0.5
        if f(mid) > 0: lo = mid
        else: hi = mid
    return (lo*hi)**0.5
print('no tower: 1/alpha_Y = 0 at mu = %.3e GeV (= %.3e M_P)' % (mZ*exp(aYinv_mz/(bY/(2*pi))), mZ*exp(aYinv_mz/(bY/(2*pi)))/MP))
print()
print('tower starting at mu0 = M_P/N: scale Lambda* where 1/alpha_Y = 0, and 1/alpha_Y at the Planck mass')
print('%-22s %-14s %-14s %-16s %-12s' % ('N (mu0 = M_P/N)', 'mu0 (GeV)', 'Lambda* (GeV)', 'Lambda*/M_P', '1/aY(M_P)'))
for lab, N in [('12', 12), ('30', 30), ('120', 120), ('600', 600), ('12^3', 12**3), ('12^5', 12**5), ('12^7', 12**7), ('12^9', 12**9), ('12^11', 12**11), ('12^13', 12**13), ('1e15 (mu0 = 12 TeV)', 1e15), ('2.4e15 (mu0 = 5 TeV)', 2.4e15)]:
    mu0 = MP/N
    print('%-22s %-14.4e %-14.4e %-16.4e %-12.3f' % (lab, mu0, zero_at(mu0), zero_at(mu0)/MP, inv_tower(MP, mu0)))
print()
print('mu0 needed so that 1/alpha_Y = 0 exactly at the Planck mass (the one free parameter, solved, not chosen):')
lo, hi = 1e3, MP
for _ in range(300):
    mid = (lo*hi)**0.5
    if inv_tower(MP, mid) > 0: hi = mid        # 1/aY still positive at M_P -> tower must start lower
    else: lo = mid
mu0 = (lo*hi)**0.5
print('  mu0 = %.6e GeV  -> R / l_P = M_P/mu0 = %.6e ; at that mu0 the check 1/alpha_Y(M_P) = %.3e' % (mu0, MP/mu0, inv_tower(MP, mu0)))
print('  same with 1/alpha_Y(M_P) = 1 (bare unity in these units):', end=' ')
lo, hi = 1e3, MP
for _ in range(300):
    mid = (lo*hi)**0.5
    if inv_tower(MP, mid) > 1: hi = mid
    else: lo = mid
mu1 = (lo*hi)**0.5
print('mu0 = %.6e GeV, R / l_P = %.6e' % (mu1, MP/mu1))
print()
print('what the chain still needs: alpha_2. With 1/alpha_Y(Lambda) = 0 and sin^2 theta_W(Lambda) = 3/8 (alpha_Y/alpha_2 = 3/5) one gets 1/alpha_2(Lambda) = 0 as well (the ratio of two infinite couplings), which SU(2) cannot do because it is asymptotically free; the pair (alpha_Y, alpha_2) therefore needs a finite floor value or a separate input for alpha_2.')

print()
print('sensitivity of the solved R / l_P (hypercharge zero exactly at the Planck mass) to conventions and inputs:')
def solveR(bt_factor, aY0=None):
    A0 = aYinv_mz if aY0 is None else aY0
    def inv(mu, mu0):
        A = A0 - bY/(2*pi)*log(mu0/mZ)
        if mu <= mu0: return A
        x = mu/mu0; N = floor(x)
        return A - bY/(2*pi)*log(x) - (bt*bt_factor)/(2*pi)*(N*log(x) - lgamma(N + 1))
    lo, hi = 1e3, MP
    for _ in range(300):
        mid = (lo*hi)**0.5
        if inv(MP, mid) > 0: hi = mid
        else: lo = mid
    return MP/((lo*hi)**0.5)
for f, lab in [(1, 'orbifold, one tower (b_tilde = 27/2)'), (2, 'circle without orbifold (two towers, b_tilde x 2)'), (0.5, 'half the KK content (b_tilde x 1/2)')]:
    print('  %-52s R / l_P = %.3f' % (lab, solveR(f)))
for d in (-0.002, 0.002):
    print('  1/alpha_Y(m_Z) shifted by %+.1f%%: R / l_P = %.3f' % (d*100, solveR(1, aYinv_mz*(1 + d))))
print('  named floor numbers for comparison: Coxeter number / tick order 30, |2I| = 120, 600-cell vertices 120 and cells 600, 12^k; the closest to the solved 28.4 is 30 (5.6% away), but the solved value moves by a factor 2 with a counting convention')
