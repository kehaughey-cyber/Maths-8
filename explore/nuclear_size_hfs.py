"""
Finite nuclear charge (Breit-Rosenthal) and magnetization (Bohr-Weisskopf) corrections to the 1s hyperfine splitting of the heavy hydrogen-like ions.  New file (2026-11-02).  Nothing fitted.
Units hbar = c = m_e = 1 (lengths in the electron reduced Compton length, energies in m_e c^2).  Radial Dirac equations, kappa = -1, G = r g, F = r f:
    G' = G/r + (E + 1 - V) F ,     F' = -F/r - (E - 1 - V) G .
Point-nucleus V = -Z alpha / r; uniform charged sphere of radius R (R = sqrt(5/3) R_ch, matching the rms charge radius): V = -(Z alpha/(2R))(3 - r^2/R^2) inside.  Shooting in x = ln r (RK4), outward from a small radius to the match point,
inward from a large radius, root in E by bisection on the mismatch.  The point-dipole hyperfine radial integral is I = int G F / r^2 dr (normalised int (G^2 + F^2) dr = 1); with a magnetization distribution it is I_M = int G F M(r) / r^2 dr,
M(r) the fraction of the magnetization inside r (uniform sphere: (r/R)^3 inside; thin shell: 0 inside).  Checks: E(point) = sqrt(1 - (Z alpha)^2) and I(point)/(-(Z alpha)^3) = 1/(gamma (2 gamma - 1)).
  delta_BR = I(finite charge, point dipole) / I(point nucleus) - 1 ;  delta_BW = I_M / I(point dipole, same wavefunction) - 1.
Measured: E / (E_nr A) = r/A from hydrogenlike_series.out (A = the Dirac point-nucleus factor); the shortfall is 1 - r/A.  QED corrections (self-energy and vacuum polarization) are not computed here.
Usage:  py -3 -I -X utf8 -u nuclear_size_hfs.py > nuclear_size_hfs.out
"""
import math, sys
ALPHA = 7.2973525643e-3; LAMBDA_E_FM = 386.15926796          # electron reduced Compton length in fm (hbar c / m_e c^2 = 1.973269804e-7 eV m / 510998.95 eV)
def rk4_run(f, x0, y0, x1, n):
    h = (x1-x0)/n; x = x0; y = list(y0); out = [(x, y[0], y[1])]
    for _ in range(n):
        k1 = f(x, y); k2 = f(x+h/2, [y[0]+h/2*k1[0], y[1]+h/2*k1[1]]); k3 = f(x+h/2, [y[0]+h/2*k2[0], y[1]+h/2*k2[1]]); k4 = f(x+h, [y[0]+h*k3[0], y[1]+h*k3[1]])
        y = [y[0]+h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), y[1]+h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]; x += h; out.append((x, y[0], y[1]))
    return out
def make_V(Z, R):
    za = Z*ALPHA
    if R is None: return lambda r: -za/r, 0.0
    return (lambda r: (-za*(3-(r/R)**2)/(2*R)) if r < R else -za/r), None
def solve(Z, R, nout=4000, nin=4000, tol=1e-13):
    za = Z*ALPHA; V, _ = make_V(Z, R); gam = math.sqrt(1-za**2)
    rm = 1.0/za                                               # match near the bulk of the wavefunction
    def run_out(E):
        if R is None:
            r0 = 1e-10; G0 = r0**gam; F0 = (gam-1)/za*G0
        else:
            r0 = 1e-4*R; V0 = V(r0); G0 = r0; F0 = -(E-1-V0)/3*r0**2
        f = lambda x, y: (lambda r: [r*(y[0]/r + (E+1-V(r))*y[1]), r*(-y[1]/r - (E-1-V(r))*y[0])])(math.exp(x))
        return rk4_run(f, math.log(r0), [G0, F0], math.log(rm), nout)
    def run_in(E):
        lam = math.sqrt(1-E*E); rmax = rm + 45.0/lam; G0 = 1e-30; F0 = -math.sqrt((1-E)/(1+E))*G0
        f = lambda x, y: (lambda r: [r*(y[0]/r + (E+1-V(r))*y[1]), r*(-y[1]/r - (E-1-V(r))*y[0])])(math.exp(x))
        return rk4_run(f, math.log(rmax), [G0, F0], math.log(rm), nin)
    def mism(E):
        o = run_out(E)[-1]; i = run_in(E)[-1]; return (o[1]*i[2] - o[2]*i[1])/math.hypot(o[1], o[2])/math.hypot(i[1], i[2])
    lo, hi = gam-0.06*gam, min(gam+0.06*gam, 0.99999); flo = mism(lo); fhi = mism(hi); n = 0
    # bracket: scan if the endpoints do not change sign
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
def integrals(sol, models, R_m):
    xs = [s[0] for s in sol]; Gs = [s[1] for s in sol]; Fs = [s[2] for s in sol]
    norm = 0.0; I = {k: 0.0 for k in models}
    for k in range(len(sol)-1):
        r1, r2 = math.exp(xs[k]), math.exp(xs[k+1]); dx = xs[k+1]-xs[k]
        n1 = (Gs[k]**2+Fs[k]**2)*r1; n2 = (Gs[k+1]**2+Fs[k+1]**2)*r2; norm += 0.5*(n1+n2)*dx
        for name, Mf in models.items():
            a = Gs[k]*Fs[k]/r1**2*Mf(r1)*r1; b = Gs[k+1]*Fs[k+1]/r2**2*Mf(r2)*r2; I[name] += 0.5*(a+b)*dx
    return {k: v/norm for k, v in I.items()}
if __name__ == '__main__':
    print('== checks of the solver on the point nucleus: E against gamma, and I(point) / (-(Z alpha)^3) against the Breit factor 1/(gamma (2 gamma - 1))')
    one = {'pt': lambda r: 1.0}
    for Z in (1, 20, 50, 67, 83):
        za = Z*ALPHA; gam = math.sqrt(1-za**2)
        E, sol = solve(Z, None); I = integrals(sol, one, None)['pt']
        print(f'  Z = {Z:2d}: E = {E:.10f}, gamma = {gam:.10f} (diff {E-gam:+.1e}); I/(-(Z a)^3) = {I/(-(za**3)):.8f}, Breit factor = {1/(gam*(2*gam-1)):.8f} (ratio {I/(-(za**3))*gam*(2*gam-1):.8f})')
    # measured shortfall from hydrogenlike_series.out
    ions = [('H', 1, 0.84075, None), ('3He+', 2, 1.9661, 0.99957), ('165Ho66+', 67, 5.2022, 0.93344), ('187Re74+', 75, 5.3698, 0.90557), ('207Pb81+', 82, 5.4943, 0.85539), ('209Bi82+', 83, 5.5211, 0.87360)]
    print('\n== finite charge (uniform sphere, R = sqrt(5/3) R_ch) and magnetization (uniform sphere and thin shell at the same R), point-dipole integral ratios')
    print(f'{"ion":9s} {"Z":>3s} {"R (fm)":>8s} {"E_fin - E_pt":>13s} {"delta_BR":>10s} {"delta_BW unif":>14s} {"delta_BW shell":>15s} {"BR+BW(unif)":>12s} {"BR+BW(shell)":>13s} {"measured r/A - 1":>17s}')
    rows = []
    for name, Z, Rch, rA in ions:
        R = math.sqrt(5/3)*Rch/LAMBDA_E_FM; za = Z*ALPHA
        Ept, solp = solve(Z, None); Ipt = integrals(solp, one, None)['pt']
        Ef, solf = solve(Z, R)
        models = {'pt': lambda r: 1.0, 'unif': lambda r, R=R: (r/R)**3 if r < R else 1.0, 'shell': lambda r, R=R: 0.0 if r < R else 1.0}
        If = integrals(solf, models, R)
        dBR = If['pt']/Ipt - 1; dU = If['unif']/If['pt'] - 1; dS = If['shell']/If['pt'] - 1
        meas = (rA-1) if rA else float('nan'); rows.append((name, Z, dBR, dU, dS, meas))
        print(f'{name:9s} {Z:3d} {R*LAMBDA_E_FM:8.3f} {Ef-Ept:13.3e} {dBR:10.5f} {dU:14.5f} {dS:15.5f} {dBR+dU:12.5f} {dBR+dS:13.5f} {meas:17.5f}')
    print('\nwhat is left of the measured shortfall after the computed corrections (QED not included; its size for Bi is of order -0.3% by recollection, not computed here):')
    for name, Z, dBR, dU, dS, meas in rows:
        if meas == meas: print(f'  {name:9s} measured {meas:+.5f}; after BR {meas-dBR:+.5f}; after BR + BW(uniform) {meas-dBR-dU:+.5f}; after BR + BW(shell) {meas-dBR-dS:+.5f}')
