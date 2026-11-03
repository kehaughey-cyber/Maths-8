"""
Does the nested-copy chain reproduce the exponent profile nature shows, and which step does the shape prefer?  New file (2026-11-02).  Nothing assumed about the step.
Nature (hydrogenlike_series.py): the absolute hyperfine energy at fixed moments has the effective exponent p_D(s) = 3 + (1/s^2)/g (1/g + 2/(2g - 1)), g = sqrt(1 - 1/s^2), as a function of the size ratio
s = (a0/Z) / lambda_e = 1/(Z alpha) of the atom's order to the electron's Compton order (point-nucleus Dirac factor; measured values agree for Z = 1, 2 and carry nuclear-size corrections for Z >= 67).
Chain: layers separated by a step q (a ring in layer 0 against the same ring in layer c; size ratio s = q^c), isotropic when mu_r = mu.  Exact for a semi-infinite chain, mode by mode:
   M(c) = - sum_k W_k exp(-gamma_k c) / (mu_r (exp(gamma_k) - 1)),   cosh(gamma_k) = 1 + mu lambda_k / (2 mu_r),
where lambda_k, W_k are the levels of the lattice face-energy operator and the weights of the ring source on them (continued to real c).  Absolute-energy exponent p_E(s) = 1 + (-d ln M / d ln s), the 1 from a source of fixed moment.
Compared over s from 2.5 to 140 (log spacing).  Free parameters: q and m = mu_r/mu.
Usage:  py -3 -I -X utf8 -u size_exponent_listening.py > size_exponent_listening.out
"""
import numpy as np, os, math
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_chain.py'), encoding='utf-8').read().split("phi = (1+5**.5)/2")[0])
phi = (1+5**.5)/2
C = S_F.T @ S_F; w, V = np.linalg.eigh(C); g = np.zeros(NE)
for h in cyc[0]: g[eidx[h]] += sgn[h]
ov = (V.T @ g)**2; nzmask = w > 1e-9
lev = {}
for lam, wt in zip(w[nzmask], ov[nzmask]): lev.setdefault(round(float(lam), 8), 0.0); lev[round(float(lam), 8)] += float(wt)
LAM = np.array(sorted(k for k, v in lev.items() if v > 1e-10)); WK = np.array([lev[k] for k in LAM])
print('levels with source weight:', len(LAM), '; total weight', WK.sum(), '; lowest three', LAM[:3], WK[:3])
def pE(s, q, m):
    c = math.log(s)/math.log(q); gam = np.arccosh(1 + LAM/(2*m)); f = WK/(m*(np.exp(gam)-1)); e = np.exp(-gam*c)
    Mc = (f*e).sum(); dM = (gam*f*e).sum(); return 1 + dM/Mc/math.log(q)
def pD(s):
    gg = math.sqrt(1-1/s**2); return 3 + (1/s**2)/gg*(1/gg + 2/(2*gg-1))
sgrid = np.exp(np.linspace(math.log(2.5), math.log(140), 40)); pdg = np.array([pD(s) for s in sgrid])
def rms(q, m): return math.sqrt(np.mean([(pE(s, q, m)-p)**2 for s, p in zip(sgrid, pdg)]))
print('\n== profile at the step q = phi and the coupling that makes the far field exactly 3 (m = lambda_1)')
print(f'{"s":>8s} {"Dirac p_D":>10s} {"chain p_E":>10s} {"difference":>11s}')
for s in (2.0, 2.5, 3.3, 4.6, 6.9, 10, 14, 20, 40, 70, 137):
    print(f'{s:8.2f} {pD(s):10.4f} {pE(s, phi, LAM[0]):10.4f} {pE(s, phi, LAM[0])-pD(s):11.4f}')
print(f'rms difference over s = 2.5 .. 140: {rms(phi, LAM[0]):.4f}')
print('\n== far field held at 3 (m = lambda_1 / (2 (cosh(2 ln q) - 1)), p_M = 2): rms difference against the Dirac profile for several steps')
print(f'{"q":>10s} {"ln q":>8s} {"m":>10s} {"rms":>8s}')
rows = []
for q in (1.05, 1.1, 1.2, 1.3, math.sqrt(phi), 1.5, phi, 1.8, math.exp(1/phi), 2.0, 2.5, 3.0, 4.0):
    m = LAM[0]/(2*(math.cosh(2*math.log(q))-1)); r = rms(q, m); rows.append((q, m, r)); print(f'{q:10.4f} {math.log(q):8.4f} {m:10.4f} {r:8.4f}')
print('\n== free two-parameter search over q and m = mu_r/mu (grid 80 x 100), rms over the same s')
best = (9, None, None); qs = np.exp(np.linspace(math.log(1.03), math.log(8), 80)); ms = np.exp(np.linspace(math.log(0.01), math.log(100), 100)); grid = np.zeros((len(qs), len(ms)))
for i, q in enumerate(qs):
    for j, m in enumerate(ms):
        r = rms(q, m); grid[i, j] = r
        if r < best[0]: best = (r, q, m)
print(f'best: rms {best[0]:.4f} at q = {best[1]:.4f} (ln q = {math.log(best[1]):.4f}), mu_r/mu = {best[2]:.4f}')
q0, m0 = best[1], best[2]; gam0 = math.acosh(1 + LAM[0]/(2*m0)); print(f'at the best point: far-field p_E = 1 + gamma_1/ln q = {1+gam0/math.log(q0):.4f}')
print('the minimum along q at each tested q (best m for that q):')
for q in (1.05, 1.1, 1.2, 1.3, 1.4, phi, 1.8, 2.0, 2.5, 3.0, 4.0, 6.0):
    i = int(np.argmin(np.abs(np.log(qs)-math.log(q)))); j = int(np.argmin(grid[i])); print(f'  q = {qs[i]:.4f}: best m = {ms[j]:.4f}, rms {grid[i, j]:.4f}')
print('\nrms as a function of the step for the best m, fine grid:')
fine = [(float(qs[i]), float(grid[i].min()), float(ms[np.argmin(grid[i])])) for i in range(len(qs))]
for q, r, m in fine[::6]: print(f'  q = {q:.4f}  rms {r:.4f}  m = {m:.4f}')

print('\n== the chain against the measured pair exponents (ions of hydrogenlike_series.out); E ~ M(s)/s at fixed moments, s = 1/(Z alpha); p = 1 + ln(M(s_b)/M(s_a)) / ln(s_a/s_b)')
ALPHA = 7.2973525643e-3
def Mfun(s, q, m):
    c = math.log(s)/math.log(q); gam = np.arccosh(1 + LAM/(2*m)); f = WK/(m*(np.exp(gam)-1)); return (f*np.exp(-gam*c)).sum()
def pair(Za, Zb, q, m):
    sa, sb = 1/(Za*ALPHA), 1/(Zb*ALPHA); return 1 + math.log(Mfun(sb, q, m)/Mfun(sa, q, m))/math.log(sa/sb)
def dirac_pair(Za, Zb):
    def lnE(z): g = math.sqrt(1-(z*ALPHA)**2); return 3*math.log(z) - math.log(g*(2*g-1))
    return (lnE(Zb)-lnE(Za))/math.log(Zb/Za)
meas = {(1, 2): 3.0015, (2, 67): 3.1034, (67, 82): 4.0379, (67, 83): 4.1958}
print(f'{"pair (Z)":>10s} {"measured":>9s} {"Dirac pt":>9s} {"chain q=phi, m=lambda_1":>24s} {"chain q=1.0571, m=43.29":>24s} {"chain q=1.3009, m=1.831":>24s}')
for (Za, Zb), pm in meas.items():
    print(f'{str(Za)+"->"+str(Zb):>10s} {pm:9.4f} {dirac_pair(Za, Zb):9.4f} {pair(Za, Zb, phi, LAM[0]):24.4f} {pair(Za, Zb, 1.0571, 43.2876):24.4f} {pair(Za, Zb, 1.3009, 1.8307):24.4f}')
print('(the 82 -> 83 pair is not used: neighbouring ions with different nuclear spin and structure; the measured 6.83 is not a Z-dependence.  Measured Z >= 67 values include finite-nuclear-size and Bohr-Weisskopf effects that neither the Dirac point-nucleus factor nor the chain contains.)')
