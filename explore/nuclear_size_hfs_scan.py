"""
Scaling and model dependence of the finite-charge (Breit-Rosenthal) effect.  New file (2026-11-02).  Nothing fitted.  Uses solve() and integrals() of nuclear_size_hfs.py (validated against gamma and the Breit factor there).
A. Z = 83 with the charge radius scaled by 0.25, 0.5, 1, 2, 4: delta_BR and the local exponent d ln|delta_BR| / d ln R_N.
B. Fixed charge radius (that of Bi, 5.5211 fm) with Z = 20, 40, 60, 75, 83: delta_BR and its local exponent in Z.
C. The four heavy ions with a Fermi charge distribution of the same rms radius (diffuseness a = 0.5234 fm, t = 2.3 fm) instead of the uniform sphere: delta_BR(Fermi) against delta_BR(uniform).
Usage:  py -3 -I -X utf8 -u nuclear_size_hfs_scan.py > nuclear_size_hfs_scan.out
"""
import importlib.util, os, math, bisect
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('nsh', os.path.join(here, 'nuclear_size_hfs.py')); nsh = importlib.util.module_from_spec(spec); spec.loader.exec_module(nsh)
ALPHA = nsh.ALPHA; LAM = nsh.LAMBDA_E_FM; one = {'pt': lambda r: 1.0}
def BR(Z, Rch_fm, V=None):
    R = math.sqrt(5/3)*Rch_fm/LAM
    Ept, sp = nsh.solve(Z, None); Ipt = nsh.integrals(sp, one, None)['pt']
    if V is not None:
        old = nsh.make_V; nsh.make_V = lambda Z_, R_: (V, None)
        try: Ef, sf = nsh.solve(Z, R)
        finally: nsh.make_V = old
    else: Ef, sf = nsh.solve(Z, R)
    If = nsh.integrals(sf, one, None)['pt']; return If/Ipt - 1, Ef-Ept
print('== A. Z = 83, charge radius scaled (uniform sphere)')
fs = (0.25, 0.5, 1.0, 2.0, 4.0); resA = []
for f in fs:
    d, dE = BR(83, 5.5211*f); resA.append((f, d)); print(f'  R_ch = {5.5211*f:8.4f} fm (x{f}): delta_BR = {d:+.5f}')
print('  local exponents d ln|delta_BR| / d ln R_N:', ', '.join(f'{math.log(resA[i+1][1]/resA[i][1])/math.log(resA[i+1][0]/resA[i][0]):.3f}' for i in range(len(resA)-1)))
gam83 = math.sqrt(1-(83*ALPHA)**2); print(f'  for comparison: 2 gamma - 1 = {2*gam83-1:.4f}, 2 gamma = {2*gam83:.4f}, 1 (linear in R_N)')
print('\n== B. fixed charge radius 5.5211 fm, Z varied (uniform sphere)')
resB = []
for Z in (20, 40, 60, 75, 83):
    d, dE = BR(Z, 5.5211); resB.append((Z, d)); print(f'  Z = {Z:2d}: delta_BR = {d:+.5f}   delta_BR / (Z alpha R_N/lambda_e) = {d/(Z*ALPHA*5.5211*math.sqrt(5/3)/LAM):.3f}')
print('  local exponents d ln|delta_BR| / d ln Z:', ', '.join(f'{math.log(resB[i+1][1]/resB[i][1])/math.log(resB[i+1][0]/resB[i][0]):.3f}' for i in range(len(resB)-1)))
print('\n== C. Fermi charge distribution (same rms radius) against the uniform sphere')
def fermi_V(Z, rms_fm, a=0.5234):
    c = math.sqrt(5/3*(rms_fm**2 - 7/5*math.pi**2*a**2)); rmax = c + 14*a + 2; n = 30000; rs = [rmax*(k+1)/n for k in range(n)]
    rho = [1.0/(1.0+math.exp((r-c)/a)) for r in rs]; w = rmax/n
    q = []; s = 0.0
    for r, p in zip(rs, rho): s += 4*math.pi*p*r*r*w; q.append(s)
    Ntot = q[-1]; P = [0.0]*n; s = 0.0
    for k in range(n-1, -1, -1): P[k] = s/Ntot; s += 4*math.pi*rho[k]*rs[k]*w
    Q = [x/Ntot for x in q]; za = Z*ALPHA
    def V(r_e):
        r = r_e*LAM
        if r >= rmax: return -za/r_e
        k = bisect.bisect_left(rs, r)
        if k == 0: return -za*LAM*(Q[0]/rs[0]*0 + P[0]) - 0.0
        t = (r-rs[k-1])/(rs[k]-rs[k-1]); Qi = Q[k-1]+t*(Q[k]-Q[k-1]); Pi = P[k-1]+t*(P[k]-P[k-1]); return -za*LAM*(Qi/r + Pi)
    return V, c
print(f'{"ion":9s} {"Z":>3s} {"R_ch (fm)":>9s} {"c (fm)":>7s} {"delta_BR uniform":>17s} {"delta_BR Fermi":>15s} {"Fermi - uniform":>16s}')
for name, Z, Rch in (('165Ho66+', 67, 5.2022), ('187Re74+', 75, 5.3698), ('207Pb81+', 82, 5.4943), ('209Bi82+', 83, 5.5211)):
    du, _ = BR(Z, Rch); V, c = fermi_V(Z, Rch); df, _ = BR(Z, Rch, V)
    print(f'{name:9s} {Z:3d} {Rch:9.4f} {c:7.3f} {du:17.5f} {df:15.5f} {df-du:16.5f}')
