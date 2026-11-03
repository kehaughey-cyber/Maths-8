"""
Is the chain's mode structure the Dirac series in disguise?  New file (2026-11-02).  Nothing fitted; this only compares two exact structures.
1. The point-nucleus Dirac hyperfine factor A(Z alpha) = 1 / (g (2 g - 1)), g = sqrt(1 - x), x = (Z alpha)^2 = 1/s^2, as a series in x (sympy): A = sum c_j x^j.
2. If the field of a ring falls across scale as M(s) = sum_k a_k s^-(k+1) (continuum limit of the chain: one power per transverse mode of S^3, exponent k + 1), and the absolute energy is M/s, then M(s) ~ s^-2 A(1/s^2)
   needs a_{2j+1} / a_1 = c_j: the odd modes k = 1, 3, 5, ... with weights equal to the series coefficients.  (The ring couples only to odd k; the Dirac series has only even powers of 1/s.)
3. The lattice ring's weights: levels of the face-energy operator S_F^T S_F, assigned to k by the continuum multiplicities 2k(k+2); a_k = W_k f_k with f_k = 1/gamma_k, gamma_k proportional to sqrt(lambda_k) in the continuum limit.
4. The Galois-conjugate (Binet) alternation of a golden ladder, for comparison: F_n sqrt5 = phi^n - psi^n, L_n = phi^n + psi^n, psi = -1/phi.
Usage:  py -3 -I -X utf8 -u dirac_series_vs_chain_weights.py > dirac_series_vs_chain_weights.out
"""
import numpy as np, os, math
import sympy as sp
here = os.path.dirname(os.path.abspath(__file__))
x = sp.symbols('x'); gam = sp.sqrt(1 - x); A = 1/(gam*(2*gam - 1)); ser = sp.series(A, x, 0, 8).removeO()
dirac_c = [sp.nsimplify(ser.coeff(x, j)) for j in range(8)]
print('== 1. Dirac factor A(x) = 1/(g(2g-1)) = sum c_j x^j, x = (Z alpha)^2 = 1/s^2:', ', '.join(str(ci) for ci in dirac_c))
print('   as decimals:', ', '.join(f'{float(ci):.6f}' for ci in dirac_c))
pser = sp.series(2*x*sp.diff(sp.log(A), x), x, 0, 6).removeO()
print('   exponent excess p_D - 3 = d ln A / d ln Z =', sp.expand(pser), '  (series in 1/s^2)')
exec(open(os.path.join(here, 'e_series_chain.py'), encoding='utf-8').read().split("phi = (1+5**.5)/2")[0])
Cc = S_F.T @ S_F; w, V = np.linalg.eigh(Cc); g = np.zeros(NE)
for h in cyc[0]: g[eidx[h]] += sgn[h]
ov = (V.T @ g)**2; nz = np.where(w > 1e-9)[0]; order = nz[np.argsort(w[nz])]
print('\n== 3. the lattice ring against the continuum S^3 coexact 1-form levels (levels assigned by cumulative multiplicity 2k(k+2))')
acc = 0; k = 1; need = 2*k*(k+2); Wk = 0.0; lamsum = 0.0; mult = 0; rows = []
for i in order:
    acc += 1; Wk += ov[i]; lamsum += w[i]
    if acc == need:
        rows.append((k, lamsum/acc, acc, Wk)); k += 1; need = 2*k*(k+2); acc = 0; Wk = 0.0; lamsum = 0.0
if acc: rows.append((k, lamsum/acc, acc, Wk, 'partial'))
print(f'{"k":>3s} {"lambda_k":>10s} {"modes":>6s} {"W_k (ring weight)":>18s} {"a_k = W_k/sqrt(lambda_k), over a_1":>36s} {"c_j (Dirac), j=(k-1)/2":>24s} {"ratio a_k/(a_1 c_j)":>20s}')
a1 = None
for r in rows:
    kk, lam, mm, W = r[0], r[1], r[2], r[3]; a = W/math.sqrt(lam)
    if kk == 1: a1 = a
    if kk % 2 == 1:
        j = (kk-1)//2; cj = float(dirac_c[j]) if j < len(dirac_c) else float('nan'); print(f'{kk:3d} {lam:10.5f} {mm:6d} {W:18.6f} {a/a1:36.6f} {cj:24.6f} {a/a1/cj:20.6f}' + ('  (partial)' if len(r) > 4 else ''))
    else: print(f'{kk:3d} {lam:10.5f} {mm:6d} {W:18.6f}   (even k: ring weight {W:.2e})')
print('total ring weight on the listed levels:', sum(r[3] for r in rows))
print('\n== 4. the Galois-conjugate alternation of a golden ladder (Binet): values above and below the pure exponential')
phi = (1+5**.5)/2; psi = -1/phi
print(f'{"n":>3s} {"phi^n":>12s} {"F_n":>10s} {"phi^n/sqrt5":>12s} {"F_n/(phi^n/sqrt5)":>18s} {"L_n":>9s} {"L_n/phi^n":>11s}')
F = [0, 1]
for n in range(2, 16): F.append(F[-1]+F[-2])
for n in range(1, 13):
    Ln = phi**n + psi**n; print(f'{n:3d} {phi**n:12.5f} {F[n]:10d} {phi**n/5**.5:12.5f} {F[n]/(phi**n/5**.5):18.6f} {Ln:9.3f} {Ln/phi**n:11.6f}')
print('F_n is below phi^n/sqrt5 for even n and above for odd n (psi^n alternates in sign): a ladder that looks exponential and lands alternately below and above it.')
