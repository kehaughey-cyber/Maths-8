"""
Vacuum polarization (Uehling) correction to the 1s hyperfine splitting of hydrogen-like ions.  New file (2026-11-03).  Nothing fitted.  Self-energy is NOT computed here.
Units hbar = c = m_e = 1.  Same Dirac radial equations and shooting as nuclear_size_hfs.py (copied here with the potential as a table, because that file is chained evidence and is not edited).
Two first-order pieces, each computed non-perturbatively where possible:
  (wf)  the Uehling potential added to the nuclear potential:  V_U(r) = -(2 alpha/(3 pi)) Z alpha int_1^inf dt w(t) S(r; 2t),  w(t) = (1 + 1/(2 t^2)) sqrt(t^2 - 1)/t^2,
        S(r; kappa) = the angular average of exp(-kappa d)/d over the nuclear charge (uniform sphere of radius R; point nucleus: exp(-kappa r)/r).  delta_wf = I(V + V_U)/I(V) - 1, I = int G F / r^2 dr (normalised).
  (ml)  the magnetic loop: the same photon-propagator correction acts on the nuclear vector potential, 1/r^2 -> (1/r^2)[1 + (2 alpha/(3 pi)) int_1^inf dt w(t) exp(-2 t r)(1 + 2 t r)]  (point dipole;
        the nuclear size inside this small term is neglected).  delta_ml = (2 alpha/(3 pi)) int G F / r^2 [int w(t) exp(-2tr)(1 + 2tr) dt] dr / I.
Low-Z check: the leading small-(Z alpha) behaviour of the total should be delta_VP / (alpha (Z alpha)) -> 3/4 (the Kroll-Pollock vacuum-polarization coefficient; recalled, not sourced here); the analytic leading
value of the magnetic loop alone from this formula is (2/(3 pi)) * 2 * (9 pi/32) = 3/8 (shown below as a number computed by the script, not assumed).
Usage:  py -3 -I -X utf8 -u explore/vp_hfs.py > explore/vp_hfs.out
"""
import math, sys
import numpy as np
ALPHA = 7.2973525643e-3; LAMBDA_E_FM = 386.15926796

# ---------- Uehling kernel: t = cosh s
SG, WG = np.polynomial.legendre.leggauss(700)
SMAX = math.acosh(5e8); S_NODES = 0.5*SMAX*(SG+1); S_W = 0.5*SMAX*WG
T_NODES = np.cosh(S_NODES); WT = (1+1/(2*T_NODES**2))*np.sinh(S_NODES)/T_NODES**2*np.sinh(S_NODES)*S_W      # w(t) dt = w(t) sinh(s) ds
def S_kernel(r, kap, R):
    """angular and charge average of exp(-kap d)/d ; kap array, r scalar"""
    if R is None or R == 0: return np.exp(-kap*r)/r
    if r >= R:
        I1 = np.exp(-kap*(r-R))*(R*(1+np.exp(-2*kap*R))/kap - (1-np.exp(-2*kap*R))/kap**2)
        return 3/(2*r*kap*R**3)*I1
    P1 = r*(1+np.exp(-2*kap*r))/kap - (1-np.exp(-2*kap*r))/kap**2
    P2 = ((r+1/kap)*(1-np.exp(-2*kap*r)) - (R+1/kap)*(np.exp(-kap*(R-r)) - np.exp(-kap*(R+r))))/kap
    return 3/(2*r*kap*R**3)*(P1+P2)
def VU_over_Za(r, R):
    """V_U(r)/(Z alpha) (negative)"""
    kap = 2*T_NODES
    return -(2*ALPHA/(3*math.pi))*np.sum(WT*S_kernel(r, kap, R))
def loop_factor(r):
    kap = 2*T_NODES
    return (2*ALPHA/(3*math.pi))*np.sum(WT*np.exp(-kap*r)*(1+kap*r))

# ---------- Dirac solver with a tabulated extra potential
def rk4_run(f, x0, y0, x1, n):
    h = (x1-x0)/n; x = x0; y = list(y0); out = [(x, y[0], y[1])]
    for _ in range(n):
        k1 = f(x, y); k2 = f(x+h/2, [y[0]+h/2*k1[0], y[1]+h/2*k1[1]]); k3 = f(x+h/2, [y[0]+h/2*k2[0], y[1]+h/2*k2[1]]); k4 = f(x+h, [y[0]+h*k3[0], y[1]+h*k3[1]])
        y = [y[0]+h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), y[1]+h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]; x += h; out.append((x, y[0], y[1]))
    return out
def solve(Z, R, tab=None, nout=4000, nin=4000, tol=1e-13):
    """tab = (x0, dx, list of V_U values per unit Z alpha) or None"""
    za = Z*ALPHA; gam = math.sqrt(1-za**2)
    if R is None: Vc = lambda r: -za/r
    else: Vc = lambda r: (-za*(3-(r/R)**2)/(2*R)) if r < R else -za/r
    if tab is None: V = lambda x, r: Vc(r)
    else:
        x0t, dxt, tabv = tab; nt = len(tabv)
        def V(x, r):
            u = (x-x0t)/dxt; i = int(u)
            if i < 0: i = 0; u = 0.0
            if i >= nt-1: i = nt-2; u = float(nt-1)
            fr = u-i; return Vc(r) + za*(tabv[i]*(1-fr)+tabv[i+1]*fr)
    rm = 1.0/za
    def run_out(E):
        if R is None: r0 = 1e-10; G0 = r0**gam; F0 = (gam-1)/za*G0
        else: r0 = 1e-4*R; V0 = Vc(r0); G0 = r0; F0 = -(E-1-V0)/3*r0**2
        f = lambda x, y: (lambda r, v: [r*(y[0]/r + (E+1-v)*y[1]), r*(-y[1]/r - (E-1-v)*y[0])])(math.exp(x), V(x, math.exp(x)))
        return rk4_run(f, math.log(r0), [G0, F0], math.log(rm), nout)
    def run_in(E):
        lam = math.sqrt(1-E*E); rmax = rm + 45.0/lam; G0 = 1e-30; F0 = -math.sqrt((1-E)/(1+E))*G0
        f = lambda x, y: (lambda r, v: [r*(y[0]/r + (E+1-v)*y[1]), r*(-y[1]/r - (E-1-v)*y[0])])(math.exp(x), V(x, math.exp(x)))
        return rk4_run(f, math.log(rmax), [G0, F0], math.log(rm), nin)
    def mism(E):
        o = run_out(E)[-1]; i = run_in(E)[-1]; return (o[1]*i[2] - o[2]*i[1])/math.hypot(o[1], o[2])/math.hypot(i[1], i[2])
    lo, hi = gam-0.06*gam, min(gam+0.06*gam, 0.99999); flo = mism(lo); fhi = mism(hi); n = 0
    if flo*fhi > 0:
        grid = [lo + (hi-lo)*k/24 for k in range(25)]; vals = [mism(E) for E in grid]
        for k in range(24):
            if vals[k]*vals[k+1] < 0: lo, hi, flo, fhi = grid[k], grid[k+1], vals[k], vals[k+1]; break
    while hi-lo > tol and n < 60:
        mid = 0.5*(lo+hi); fm = mism(mid)
        if flo*fm <= 0: hi, fhi = mid, fm
        else: lo, flo = mid, fm
        n += 1
    E = 0.5*(lo+hi); o = run_out(E); i = run_in(E)
    sc = o[-1][1]/i[-1][1]; sol = [(x, g, f) for x, g, f in o[:-1]] + [(x, g*sc, f*sc) for x, g, f in reversed(i)]
    return E, sol
def hfs_integral(sol, weight=None):
    xs = np.array([s[0] for s in sol]); G = np.array([s[1] for s in sol]); F = np.array([s[2] for s in sol]); r = np.exp(xs)
    norm = np.trapezoid((G**2+F**2)*r, xs); c = G*F/r**2/norm
    I = np.trapezoid(c*r, xs)
    return I, xs, r, c

def make_table(R, rmin, rmax, n=2600):
    x0 = math.log(rmin); x1 = math.log(rmax); dx = (x1-x0)/(n-1); vals = [VU_over_Za(math.exp(x0+k*dx), R) for k in range(n)]
    return (x0, dx, vals)

if __name__ == '__main__':
    print('== sanity of the kernels.  Uehling potential of a point nucleus at r = 0.1, 1, 10 (units lambda_e) per unit Z alpha:')
    for r in (0.1, 1.0, 10.0): print(f'  r = {r}: V_U/(Z alpha) = {VU_over_Za(r, None):.10e};  (Coulomb is {-1/r:.6e}; ratio {VU_over_Za(r, None)/(-1/r):.6e});  finite sphere R = 0.0184: {VU_over_Za(r, 0.0184):.10e}')
    print('  inside a sphere of radius R = 0.0184: V_U(r)/(Z alpha) at r = 0.001, 0.01, 0.0184, 0.02:', ', '.join(f'{VU_over_Za(r, 0.0184):.8e}' for r in (0.001, 0.01, 0.0184, 0.02)))
    print('  continuity at r = R (from inside, from outside):', f'{S_kernel(0.0184*(1-1e-9), 2*T_NODES, 0.0184)[:3]}', f'{S_kernel(0.0184*(1+1e-9), 2*T_NODES, 0.0184)[:3]}')
    ml_analytic = (2*ALPHA/(3*math.pi))*2*(9*math.pi/32)/ALPHA
    print(f'  analytic leading magnetic-loop coefficient (2/(3 pi)) * 2 * (9 pi/32) = {ml_analytic:.10f} (= 3/8 = {3/8})')
    print('\n== low Z, point nucleus: total and parts of the vacuum-polarization correction in units of alpha (Z alpha)')
    print(f'{"Z":>3s} {"delta_wf":>13s} {"delta_ml":>13s} {"total":>13s} {"wf/(a Za)":>10s} {"ml/(a Za)":>10s} {"total/(a Za)":>13s}')
    low = []
    for Z in (1, 2, 4, 8, 16):
        za = Z*ALPHA; tab = make_table(None, 1e-11, 46.0/za+10)
        E0, s0 = solve(Z, None); E1, s1 = solve(Z, None, tab); I0, xs, r, c = hfs_integral(s0); I1, _, _, _ = hfs_integral(s1)
        L = np.array([loop_factor(rr) for rr in r]); dml = np.trapezoid(c*L*r, xs)/I0; dwf = I1/I0-1; tot = dwf+dml
        low.append((Z, dwf, dml, tot)); print(f'{Z:3d} {dwf:13.6e} {dml:13.6e} {tot:13.6e} {dwf/(ALPHA*za):10.5f} {dml/(ALPHA*za):10.5f} {tot/(ALPHA*za):13.5f}   (E shift {E1-E0:+.3e})', flush=True)
    print('\n== the heavy ions, uniform charged sphere R = sqrt(5/3) R_ch (R_ch from hydrogenlike_series ion table), first-order VP pieces')
    print(f'{"ion":9s} {"Z":>3s} {"delta_wf":>12s} {"delta_ml":>12s} {"total VP":>12s}   {"E shift (m c^2)":>16s}')
    ions = [('165Ho66+', 67, 5.2022), ('187Re74+', 75, 5.3698), ('207Pb81+', 82, 5.4943), ('209Bi82+', 83, 5.5211)]
    for name, Z, Rch in ions:
        R = math.sqrt(5/3)*Rch/LAMBDA_E_FM; za = Z*ALPHA
        tab = make_table(R, 1e-4*R*0.99, 46.0/za+10, n=3200)
        E0, s0 = solve(Z, R); E1, s1 = solve(Z, R, tab); I0, xs, r, c = hfs_integral(s0); I1, _, _, _ = hfs_integral(s1)
        L = np.array([loop_factor(rr) for rr in r]); dml = np.trapezoid(c*L*r, xs)/I0; dwf = I1/I0-1
        print(f'{name:9s} {Z:3d} {dwf:12.6e} {dml:12.6e} {dwf+dml:12.6e}   {E1-E0:+16.9e}', flush=True)
