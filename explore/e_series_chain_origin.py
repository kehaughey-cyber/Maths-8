"""
Where the exponent of the size dependence comes from.  New file (2026-11-02).  Nothing fitted; the couplings that are tuned are tuned openly, to see which exact value each exponent needs.
Uses the definitions of e_series_chain.py (link system, chain_M) and route56_subdiv.py (refinement).
1. The lattice's face-energy spectrum (S_F^T S_F) against the continuum spectrum of coexact 1-forms on the unit S^3: curl^2 = (k+1)^2, multiplicity 2k(k+2), k = 1, 2, ...
2. Per-mode fall across layers: cosh(gamma_k) = 1 + mu lambda_k / (2 mu_r).  The exact mu_r/mu that gives a chosen far-field exponent p_M = gamma/ln q  is  lambda_1 / (2 (cosh(p_M ln q) - 1)).
3. What a fixed-moment source adds.  A ring of fixed physical moment mu_A at radius R_A carries a current in lattice units j = mu_A / (q c R_A area_lat) proportional to 1/R_A (tick = R/c, the lab's declared anchor); the phase it sets on a fixed
   inner ring is M_lat * j, and the inner ring's energy shift is its own (fixed) quantum times that phase.  So the exponent of the absolute energy in R_A is p_E = p_M + 1.  (An argument from units, not a lattice computation.)
4. The chain at the coupling that makes the far-field p_M exactly 2 for q = phi, checked on the solver.
5. The volume growth of the refined carrier: number of points of the n-fold geodesic subdivision of the 600-cell.
Usage:  py -3 -I -X utf8 -u e_series_chain_origin.py > e_series_chain_origin.out
"""
import numpy as np, os, sys, math, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_chain.py'), encoding='utf-8').read().split("phi = (1+5**.5)/2")[0])
phi = (1+5**.5)/2; lnphi = math.log(phi)
C = S_F.T @ S_F; w = np.linalg.eigvalsh(C); nz = w[w > 1e-9]
# group into levels (tolerance 5e-3 relative merges the icosahedral splitting of the higher levels)
levels = []
for x in nz:
    if levels and abs(x - np.mean(levels[-1])) < 2e-2: levels[-1].append(x)
    else: levels.append([x])
print('== 1. spectrum of the lattice face-energy operator against the continuum S^3 coexact 1-forms')
print(f'{"lattice level":>14s} {"mult":>5s}   {"k":>2s} {"(k+1)^2":>8s} {"2k(k+2)":>8s} {"lambda/(k+1)^2":>15s}')
cum = 0; k = 1; i = 0
rowsk = []
for lv in levels[:8]:
    lam = np.mean(lv); m = len(lv); cum += m
    rowsk.append((lam, m))
# match levels to k by cumulative multiplicity 6, 16, 30, 48, 70
k = 1; need = 2*k*(k+2); acc = 0; accl = 0.0
for lam, m in rowsk:
    acc += m; accl += lam*m
    if acc == need:
        print(f'{accl/acc:14.7f} {acc:5d}   {k:2d} {(k+1)**2:8d} {need:8d} {accl/acc/(k+1)**2:15.6f}')
        k += 1; need = 2*k*(k+2); acc = 0; accl = 0.0
    elif acc > need: print('  (levels do not align with the multiplicities from here)'); break
lam1 = nz.min(); print(f'lowest level lambda_1 = {lam1:.10f} ; 5 - 2 sqrt 5 = {5-2*5**.5:.10f}')
a_eff = math.sqrt(lam1/4); print(f'lattice spacing a_eff defined by lambda_1 = 4 a_eff^2 (k = 1): {a_eff:.5f} (the 600-cell edge chord is {1/phi:.5f}, arc {math.pi/5:.5f})')
print('\n== 2. exact couplings for a chosen far-field exponent p_M (q = step per layer): mu_r/mu = lambda_1 / (2 (cosh(p_M ln q) - 1))')
print(f'{"q":>14s} {"p_M":>5s} {"mu_r/mu":>14s}   note')
for qn, q in (('phi', phi), ('sqrt(phi)', math.sqrt(phi)), ('phi^2', phi**2)):
    for p in (2.0, 3.0):
        m = lam1/(2*(math.cosh(p*math.log(q)) - 1)); note = ''
        if qn == 'phi' and p == 2.0: note = f'= lambda_1 exactly (cosh(2 ln phi) = 3/2): {abs(m-lam1):.1e}'
        if qn == 'phi' and p == 3.0: note = f'= (3 phi - 4)/4 = {(3*phi-4)/4:.8f} (cosh(3 ln phi) = sqrt 5)'
        print(f'{qn:>14s} {p:5.1f} {m:14.8f}   {note}')
print('\n== 3. the continuum limit of the per-mode exponent under the isotropic rule mu_r/mu = (a_eff/dt)^2 (dt = ln q, the log-radius spacing): p_M = arccosh(1 + lambda dt^2 / (2 a_eff^2)) / dt')
print(f'{"q":>12s} {"dt":>8s} {"mu_r/mu":>9s}  p_M(k=1) {"p_E = p_M + 1":>14s} {"p_M(k=2)":>9s} {"p_M(k=3)":>9s}   [continuum: 2, 3, 4]')
lamk = [np.mean(l) for l in [[x for x in nz if abs(x-r[0]) < 0.3*r[0]] for r in rowsk]][:3]
lamk = [rowsk[0][0], None, None]
# lambda for k = 2, 3 from the level groups by multiplicity accumulation
accs = []; acc = 0; accl = 0.0; kk = 1; need = 6
for lam, m in rowsk:
    acc += m; accl += lam*m
    if acc == need: accs.append(accl/acc); kk += 1; need = 2*kk*(kk+2); acc = 0; accl = 0.0
for qn, q in (('phi', phi), ('sqrt(phi)', math.sqrt(phi)), ('phi^(1/4)', phi**.25), ('e^0.05', math.exp(0.05))):
    dt = math.log(q); mm = (a_eff/dt)**2
    pm = [math.acosh(1 + l*dt**2/(2*a_eff**2))/dt for l in accs[:3]]
    print(f'{qn:>12s} {dt:8.4f} {mm:9.4f}  {pm[0]:8.4f} {pm[0]+1:14.4f} {pm[1]:9.4f} {pm[2]:9.4f}')
print('series: p_M(k=1) = 2 - dt^2/3 + ...; nature (3He+/H) gives p_E = 2.99993.')
print('\n== 4. the chain on the solver at mu_r/mu = lambda_1 (q = phi): far-field p_M should be exactly 2 (gamma = 2 ln phi = %.8f)' % (2*lnphi))
M, res = chain_M(8, lam1*MU); gm = np.log(M[:-1]/M[1:])
print('residual', f'{res:.1e}', '; gamma_c =', ' '.join(f'{x:.5f}' for x in gm), '; p_M(c) =', ' '.join(f'{x/lnphi:.4f}' for x in gm))
M, res = chain_M(8, ((3*phi-4)/4)*MU); gm = np.log(M[:-1]/M[1:])
print('at mu_r/mu = (3 phi - 4)/4: gamma_c =', ' '.join(f'{x:.5f}' for x in gm), '; p_M(c) =', ' '.join(f'{x/lnphi:.4f}' for x in gm), '(far-field target 3)')
print('\n== 5. volume growth of the refined carrier (points of the n-fold geodesic subdivision of the 600-cell)')
spec = importlib.util.spec_from_file_location('sd2', os.path.join(here, 'route56_subdiv.py')); sd2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(sd2)
from math import comb
Vc = sd2.carrier(); print(f'{"n":>3s} {"points (formula)":>17s} {"points (built)":>15s} {"ratio to n=1":>13s} {"local exponent ln(V_n/V_{n-1})/ln(n/(n-1))":>44s}')
prev = None
for n in range(1, 9):
    f = 120 + 720*(n-1) + 1200*comb(n-1, 2) + 600*comb(n-1, 3); built = '-'
    if n <= 3:
        P, E = sd2.subdivide(Vc, n); built = str(len(P))
    ex = '' if prev is None else f'{math.log(f/prev)/math.log(n/(n-1)):.4f}'
    print(f'{n:3d} {f:17d} {built:>15s} {f/120:13.3f} {ex:>44s}'); prev = f
print('large-n limit: V_n ~ 100 n^3 (the 600 cells each contribute n^3/6): exponent 3 = the ambient dimension of the carrier; the floor\'s intrinsic dimension (ball-count growth, node 25) is 2.')
