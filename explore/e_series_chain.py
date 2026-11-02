"""
How the coupling between two rings falls with their separation across a chain of nested copies.  New file (2026-11-02).  Nothing fitted.
Copies c = 0..K, each the 600-cell link system (720 edge phases, face energy mu sum(1 - cos F)), joined layer to layer by radial links b^c (120, oriented c -> c+1) and radial plaquettes
P^c_e = a^c_e - a^{c+1}_e + b^c_head - b^c_tail with energy mu_r sum(1 - cos P).  Isotropic when mu_r = mu.  (Matter enters only as the source current; its own stiffening is left out so that this is the field propagator.)
Static response: a unit circulating current on the decagon of cycle 0 in layer 0 sources the quadratic form  H x = -g  (H = Hessian of all link energies at zero field, g the current on the ring edges);
the circulation M_c = sum over the ring's edges of x in layer c is the mutual inductance between the layer-0 ring and the same ring in layer c.
If each layer is a copy larger by a factor q (the lab's declared step is q = phi), the fall M_c ~ exp(-gamma c) = (size ratio)^-p with p = gamma / ln q.  Nature's exponent (the Z^3 of the hyperfine structure) is p = 3.
Reported: M_c, the step ratio gamma_c = ln(M_c / M_{c+1}), p for q = phi, and the step q3 = exp(gamma/3) that would make p = 3.
Usage:  py -3 -I -X utf8 -u e_series_chain.py > e_series_chain.out
"""
import numpy as np, os, sys, time
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
MU = 48.0/5*np.sin(np.pi/5)
S_F = np.zeros((len(FACES), NE))
for f in range(len(FACES)):
    for c in range(3): S_F[f, FE[f, c]] += FS[f, c]
HV = MU*S_F.T @ S_F
def chain_M(K, mur, ring_cycle=0):
    L = K+1; D = L*NE + K*N; Hm = np.zeros((D, D))
    for c in range(L): Hm[c*NE:(c+1)*NE, c*NE:(c+1)*NE] += HV
    for c in range(K):
        for e in range(NE):
            idx = np.array([c*NE+e, (c+1)*NE+e, L*NE + c*N + HEAD[e], L*NE + c*N + TAIL[e]]); r = np.array([1.0, -1.0, 1.0, -1.0])
            Hm[np.ix_(idx, idx)] += mur*np.outer(r, r)
    g = np.zeros(D)
    for h in cyc[ring_cycle]: g[eidx[h]] += sgn[h]
    x = np.linalg.solve(Hm + 1e-10*np.eye(D), -g)
    M = np.array([sum(sgn[h]*x[c*NE+eidx[h]] for h in cyc[ring_cycle]) for c in range(L)])
    return M, np.abs(Hm @ x + g).max()
phi = (1+5**.5)/2
print('mu =', repr(MU), '(M6 E3 value, an input)')
for K in (6, 8):
    for fr in ((0.1, 1.0, 10.0) if K == 6 else (1.0,)):
        t0 = time.time(); M, res = chain_M(K, fr*MU)
        print(f'\n== K = {K} (layers 0..{K}), mu_r / mu = {fr}, residual {res:.1e}, {time.time()-t0:.0f} s')
        print('layer c   M_c (circulation per unit source current)   gamma_c = ln(M_c/M_{c+1})   p (q = phi)   q for p = 3')
        for c in range(K+1):
            if c < K and M[c+1] != 0 and M[c]/M[c+1] > 0:
                gm = np.log(M[c]/M[c+1]); print(f'{c:6d}   {M[c]:+.10e}   {gm:+.6f}   {gm/np.log(phi):+.4f}   {np.exp(gm/3):.5f}')
            else: print(f'{c:6d}   {M[c]:+.10e}')
