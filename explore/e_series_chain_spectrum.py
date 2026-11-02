"""
Why the chain falls the way it does, and where p = 3 would sit.  New file (2026-11-02).  Nothing fitted.  Uses the definitions of e_series_chain.py.
Far field: a transverse mode of the link lattice with face-energy eigenvalue lambda (eigenvalue of S_F^T S_F) falls across layers as exp(-gamma c) with cosh(gamma) = 1 + mu lambda / (2 mu_r).
The ring source projects onto such modes; the lowest one with nonzero weight sets the far-field rate.  Then a scan of mu_r / mu with K = 8 for the effective exponent p = gamma_c / ln(phi) at the first layers.
Usage:  py -3 -I -X utf8 -u e_series_chain_spectrum.py > e_series_chain_spectrum.out
"""
import numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_chain.py'), encoding='utf-8').read().split("phi = (1+5**.5)/2")[0])
phi = (1+5**.5)/2
C = S_F.T @ S_F; w, V = np.linalg.eigh(C)
g = np.zeros(NE)
for h in cyc[0]: g[eidx[h]] += sgn[h]
ov = (V.T @ g)**2
print('face-energy operator S_F^T S_F (720 x 720): zero modes', int((w < 1e-9).sum()), '(gradients), lowest nonzero eigenvalues of the lattice and the weight of the ring source on each distinct level:')
lv = []; i = 0
nz = np.where(w > 1e-9)[0]
vals = np.round(w[nz], 7); order = sorted(set(vals))
for v in order[:10]:
    sel = nz[vals == v]; lv.append((v, len(sel), ov[sel].sum()))
    print(f'  lambda = {v:.7f}  multiplicity {len(sel):3d}  weight of the ring source {ov[sel].sum():.6f}')
tot = ov[nz].sum(); print('total weight of the ring source on nonzero modes', tot, '; on zero modes', ov[w < 1e-9].sum())
lam1 = next(v for v, m, wt in lv if wt > 1e-8); print('lowest level with nonzero source weight: lambda =', lam1)
print('\nfar-field rate predicted for mu_r / mu:')
for fr in (0.1, 0.2, 0.3, 0.5, 1.0, 10.0):
    gam = np.arccosh(1 + lam1/(2*fr)); print(f'  mu_r/mu = {fr:5.1f}: gamma_inf = arccosh(1 + lambda/(2 mu_r/mu)) = {gam:.5f} ; p (q = phi) = {gam/np.log(phi):.4f} ; q for p = 3: {np.exp(gam/3):.5f}')
print('\nscan, K = 8: gamma_c and p (q = phi) at the first layers')
print(f'{"mu_r/mu":>8s}   gamma_0 {"p_0":>8s}   gamma_1 {"p_1":>8s}   gamma_2 {"p_2":>8s}   gamma_3 {"p_3":>8s}')
for fr in (0.2, 0.3, 0.4, 0.5, 0.7, 1.0):
    M, res = chain_M(8, fr*MU); gm = np.log(M[:-1]/M[1:])
    print(f'{fr:8.2f}   ' + '   '.join(f'{gm[c]:7.4f} {gm[c]/np.log(phi):8.4f}' for c in range(4)))
