"""
Susceptibility (flux the matter induces on live links), spin separate from the orbital ring, and the coupling between orders as a splitting.  New file (2026-11-02).  Nothing fitted.
Setup comes from e_series_two_copy.py (definitions only) and e_series_readouts.py (definitions only).  Units kappa = k = 1, mu = M6 value unless stated.
 1. Susceptibility.  (a) static link response: with the matter state fixed, the link field that minimises G + V_spec (a lattice Ampere law: H a* = -g, H the Hessian of G + V at a = 0, g = dG/da the current),
    the flux it puts through the ring, and the frequency shift that flux gives the ring; (b) the same quantity in a live run (time mean of the ring flux against the static value);
    (c) the matter's own flux response with the links held: M(alpha) = -(Area/10) sum omega'(alpha) for one quantum in each circulation sense, and chi = dM/dB.
 2. Spin.  (a) in the existing action the two spinor components of a ring mode are degenerate under flux (U(1) acts on both alike); (b) the Dirac operator D_ij = exp(i k a_ij) gamma_ij of route56 (240 x 240):
    its spectrum, the 28-mode kernel, and the first-order response of the kernel and the first massive multiplets to the same ring flux.
 3. (in e_series_resonance.py)
 4. The coupling between orders as a splitting.  Two rings, one in each copy, coupled only through the plaquette flux mu_r (kappa_r = 0); the equilibrium link field for fixed matter gives the energy
    E* = (1/2) g.x*, and the difference between co- and counter-circulating rings is the instrument's hyperfine-like splitting; compared with the measured hydrogen ratio and with its formula.
Usage:  py -3 -I -X utf8 -u e_series_response.py > e_series_response.out
"""
import numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_two_copy.py'), encoding='utf-8').read().split("rng = np.random.default_rng(20261103)")[0])
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
S_F = np.zeros((len(FACES), NE))
for f in range(len(FACES)):
    for c in range(3): S_F[f, FE[f, c]] += FS[f, c]
HV = MU_N*S_F.T @ S_F                                                   # Hessian of mu sum(1 - cos F) at F = 0
def unit_ring(i, kq, key, sign, rho=1.0):
    ps, vs, _, _ = ring(i, kq, key, sign, rho); Q = rho_h(ps, vs, rho**2).sum(); sc = 1/np.sqrt(abs(Q)); return ps*sc, vs*sc
def HG_diag(psi, key):
    w = np.einsum('hij,hj->hi', Om[key], psi); d = 2*KAP*KK**2*np.real(np.einsum('hi,hi->h', psi[TN].conj(), w)); out = np.zeros(NE); np.add.at(out, eidx, d); return out
def block(c, a, key):
    n = len(c); M = np.zeros((2*n, 2*n), complex)
    for i, h in enumerate(c):
        ph = np.exp(1j*KK*sgn[h]*a[eidx[h]]); j = (i+1) % n
        M[2*i:2*i+2, 2*j:2*j+2] += np.eye(2); M[2*i:2*i+2, 2*i:2*i+2] -= ph*Om[key][h]
    return M
def ringvec(i, kq, key, chi=(1, 0)):
    th = (2*np.pi*kq + (np.pi if key == 'gamma' else 0.0))/10; c = cyc[i]; v = np.zeros((len(c), 2), complex); v[0] = chi
    for n in range(len(c)-1): v[n+1] = np.exp(1j*th)*Om[key][c[n]] @ v[n]
    v = v.reshape(-1); return v/np.linalg.norm(v)
def flux_a(i, alpha):
    a = np.zeros(NE)
    for h in cyc[i]: a[eidx[h]] = alpha*sgn[h]
    return a
def omega_blk(i, kq, key, a, chi=(1, 0)):
    M = block(cyc[i], a, key); v = ringvec(i, kq, key, chi); return np.sqrt(KAP*(v.conj() @ (M.conj().T @ M) @ v).real)
Bsum = sum(sgn[h]*WE[eidx[h]] for h in cyc[0]); AREA = bnorm(Bsum)
KEY = 'q'; far = None
# ======================= 1. susceptibility =======================
print('== 1(a). static link response to a fixed matter state (lattice Ampere law): H a* = -g, H = Hess(G + V_spec) at a = 0, g = dG/da = k j')
p1, v1 = unit_ring(0, 1, KEY, -1); jx = None
for j in range(1, len(cyc)):
    if j == reverse_cycle(0): continue
    pj, vj = unit_ring(j, 1, KEY, +1); d = readouts(p1+pj, v1+vj, np.zeros(NE), KEY)
    if abs(d['j_man']/d['j_exp'] - 2**-0.5) < 1e-6: jx = j; break
pj, vj = unit_ring(jx, 1, KEY, +1); psi = p1+pj; vel = v1+vj
print('state: ring in cycle 0 (charge +1) and ring in cycle', jx, '(charge -1), each normalised to unit charge')
g = currents(psi, np.zeros(NE), KEY); H = np.diag(HG_diag(psi, KEY)) + HV
xs, res, rk, sv = np.linalg.lstsq(H, -g, rcond=1e-10); resid = np.abs(H @ xs + g).max()
Phi = sum(sgn[h]*xs[eidx[h]] for h in cyc[0]); Ir = np.mean([sgn[h]*g[eidx[h]] for h in cyc[0]])
print(f'rank of H {rk} of {NE}; residual of H a* + g: {resid:.2e}; |g| max {np.abs(g).max():.5f}')
print(f'induced circulation through ring 0: Phi = sum a*_e = {Phi:.6f}  (current per ring step g = {Ir:.6f}; ratio Phi/g = {Phi/Ir:.6f})')
print(f'link energy lowering at fixed matter (1/2) g.a* = {0.5*g@xs:.6f}')
a_star = xs.copy(); w0 = omega_blk(0, 1, KEY, np.zeros(NE)); w1 = omega_blk(0, 1, KEY, a_star)
print(f'ring-0 mode kq=1 frequency: bare {w0:.9f}, in its own induced link field {w1:.9f}, shift {w1-w0:+.3e} ({(w1-w0)/w0:+.3e} relative)')
print('induced field also on: faces nonzero', int((np.abs(S_F @ a_star) > 1e-12).sum()), 'of', len(FACES), '; max |F| =', np.abs(S_F @ a_star).max())
print('\n== 1(b). the same flux in a live run (links dynamic, Gauss-prepared, copy B empty and decoupled), T = 40, time mean of the ring-0 circulation')
P = mkP(rho=1.0, kr=0.0, mur=0.0, key=KEY)
Lm = 12*np.eye(N) - (adj*1.0); rhs = -P['kk']*rho_v(psi, vel, 1.0)/P['I'][0]; rhs = rhs - rhs.mean(); ph_ = np.linalg.lstsq(Lm, rhs, rcond=1e-10)[0]
Z = np.zeros((H_ := len(DE), 2), complex)
S0 = ([psi.copy(), Z.copy()], [vel.copy(), Z.copy()], [np.zeros(NE), np.zeros(NE)], [ph_[HEAD]-ph_[TAIL], np.zeros(NE)], np.zeros(N), np.zeros(N))
o = run(S0, P, 4000, 0.02, live=True, snap=10)
phis = np.array([sum(sgn[h]*S[2][0][eidx[h]] for h in cyc[0]) for t, e, S in o['snaps']]); ts = np.array([t for t, e, S in o['snaps']])
print(f'ring-0 circulation over time: mean {phis.mean():.6f}, min {phis.min():.6f}, max {phis.max():.6f}; static value from 1(a): {Phi:.6f}; Gauss drift {o["gd"]:.1e}; max|dE| {o["dEmax"]:.2e}')
print('mean over the first and second half:', phis[:len(phis)//2].mean(), phis[len(phis)//2:].mean())
print('\n== 1(c). the matter\'s own flux response, links held (one quantum in each circulation sense), M(alpha) = -(Area/10)(omega_+\' + omega_-\'), chi = dM/dB, B = 10 alpha / Area')
def dw(i, kq, key, al, e=1e-5): return (omega_blk(i, kq, key, flux_a(i, al+e)) - omega_blk(i, kq, key, flux_a(i, al-e)))/(2*e)
print(f'{"alpha":>8s} {"omega_+":>12s} {"omega_-":>12s} {"M_+":>12s} {"M_-":>12s} {"M total":>12s}')
for al in (0.0, 0.01, 0.05, 0.1, 0.2):
    Mp = -(AREA/10)*dw(0, 1, KEY, al); Mm = -(AREA/10)*dw(0, 9, KEY, al)
    print(f'{al:8.3f} {omega_blk(0, 1, KEY, flux_a(0, al)):12.8f} {omega_blk(0, 9, KEY, flux_a(0, al)):12.8f} {Mp:12.8f} {Mm:12.8f} {Mp+Mm:12.8f}')
e = 1e-4; Mt = lambda al: -(AREA/10)*(dw(0, 1, KEY, al) + dw(0, 9, KEY, al)); chi_a = (Mt(e) - Mt(-e))/(2*e)*(AREA/10)         # dM/dB = dM/dalpha * dalpha/dB, alpha = B Area/10
print(f'chi = dM/dB at 0 for one quantum in each sense = {chi_a:.8f} (positive = paramagnetic); analytic (Area/10)^2 sin(theta/2) = {(AREA/10)**2*np.sin(np.pi/10):.8f}')
# ======================= 2. spin =======================
print('\n== 2(a). the two spinor components of a ring mode under flux in the existing action')
for key in ('q', 'gamma'):
    a_ = flux_a(0, 0.1); wA = omega_blk(0, 1, key, a_, (1, 0)); wB = omega_blk(0, 1, key, a_, (0, 1)); wC = omega_blk(0, 1, key, a_, (1, 1))
    print(f'{key:5s}: omega for spinor (1,0) {wA:.12f}, (0,1) {wB:.12f}, (1,1)/sqrt2-mix {wC:.12f}; spin splitting {wA-wB:+.2e}')
print('\n== 2(b). the Dirac operator D_ij = exp(i k a_ij) gamma_ij (route56) with link phases, 240 x 240')
def Dmat(a):
    D = np.zeros((2*N, 2*N), complex)
    for (i, j) in EDG:
        blk = np.exp(1j*KK*a[eId[(i, j)]])*gam(i, j); D[2*i:2*i+2, 2*j:2*j+2] = blk; D[2*j:2*j+2, 2*i:2*i+2] = blk.conj().T
    return D
D0 = Dmat(np.zeros(NE)); print('Hermitian:', np.abs(D0 - D0.conj().T).max())
ev, U = np.linalg.eigh(D0); print('kernel dimension (|lambda| < 1e-8):', int((np.abs(ev) < 1e-8).sum()), '; spectrum min', ev.min(), 'max', ev.max())
lv, cn = np.unique(np.round(ev, 6), return_counts=True); print('levels (value:multiplicity):', ', '.join(f'{x:.4f}:{c}' for x, c in zip(lv, cn)))
def dD(i_cycle):
    D = np.zeros((2*N, 2*N), complex)
    for h in cyc[i_cycle]:
        e_ = eidx[h]; (i, j) = EDG[e_]; c = sgn[h]
        blk = 1j*KK*c*gam(i, j); D[2*i:2*i+2, 2*j:2*j+2] = blk; D[2*j:2*j+2, 2*i:2*i+2] = blk.conj().T
    return D
dDa = dD(0)
print('first-order response of D to the flux alpha on ring 0 (Hellmann-Feynman within each degenerate level): eigenvalues of P = V^dag (dD/dalpha) V')
order = np.argsort(np.abs(ev)); groups = []; used = np.zeros(2*N, bool)
for idx in order:
    if used[idx]: continue
    grp = np.where(np.abs(ev - ev[idx]) < 1e-6)[0]; used[grp] = True; groups.append(grp)
for grp in groups[:6]:
    Vg = U[:, grp]; Pm = Vg.conj().T @ dDa @ Vg; pe = np.linalg.eigvalsh((Pm+Pm.conj().T)/2)
    print(f'level {ev[grp[0]]:+9.5f} (mult {len(grp):2d}): first-order shifts per unit alpha: ' + ' '.join(f'{x:+.4f}' for x in pe[:12]) + (' ...' if len(pe) > 12 else ''))
e_ = 1e-4; evp = np.linalg.eigvalsh(Dmat(flux_a(0, e_))); evm = np.linalg.eigvalsh(Dmat(flux_a(0, -e_)))
print('finite-difference check: eigenvalues of D(+1e-4) nearest 0 (the 28-kernel):', ' '.join(f'{x:+.2e}' for x in evp[np.argsort(np.abs(evp))[:6]]), '...')
# ======================= 4. coupling between orders as a splitting =======================
print('\n== 4. two rings, one per copy, coupled by the plaquette flux mu_r only (kappa_r = 0): E* = (1/2) g.x*, x* = -H^+ g; splitting = E*(co) - E*(counter)')
MPME = 1836.152673426; RY = 13.605693122990; HFS = 5.8743261841116e-6; ALPHA = 7.2973525643e-3; muB = 9.2740100657e-24; mup = 1.41060679545e-26
R_e = np.zeros((NE, 2*NE+N))
for e_ in range(NE): R_e[e_, e_] = 1; R_e[e_, NE+e_] = -1; R_e[e_, 2*NE+HEAD[e_]] += 1; R_e[e_, 2*NE+TAIL[e_]] -= 1
def split(rho, mur, key=KEY):
    pa, va = unit_ring(0, 1, key, -1, 1.0); out = {}
    for label, kq in (('co', 1), ('counter', 9)):
        pb, vb = unit_ring(0, kq, key, -1, rho)
        gA = currents(pa, np.zeros(NE), key); gB = currents(pb, np.zeros(NE), key)
        HH = np.zeros((2*NE+N, 2*NE+N)); HH[:NE, :NE] = np.diag(HG_diag(pa, key)) + HV; HH[NE:2*NE, NE:2*NE] = np.diag(HG_diag(pb, key)) + HV; HH += mur*R_e.T @ R_e
        g_ = np.concatenate([gA, gB, np.zeros(N)]); x, _, _, _ = np.linalg.lstsq(HH, -g_, rcond=1e-12); out[label] = 0.5*g_ @ x
    return out['co'] - out['counter'], out
w_A = 2*np.sin(np.pi/10)
print(f'ring quantum energy of copy A: omega_A = {w_A:.9f}')
print(f'{"rho_B":>12s} {"mu_r":>10s} {"E*(co)":>14s} {"E*(counter)":>14s} {"splitting":>14s} {"splitting/omega_A":>18s}')
for rho in (1.0, 1.0/MPME):
    for mur in (1e-6, 1e-4, 1e-2, 1.0, MU_N, 100.0):
        d, o_ = split(rho, mur); print(f'{rho:12.5e} {mur:10.3g} {o_["co"]:14.6e} {o_["counter"]:14.6e} {d:14.6e} {d/w_A:18.6e}')
meas = HFS/RY; formula = 16/3*(mup/muB)*ALPHA**2
print(f'\nmeasured hydrogen hyperfine splitting / Rydberg energy = {HFS:.6e} eV / {RY:.9f} eV = {meas:.6e}')
print(f'(16/3)(mu_p/mu_B) alpha^2 = {formula:.6e} (textbook formula from memory; ratio to measured {formula/meas:.6f})')
print('so the measured ratio is the product of the nuclear moment ratio, alpha^2 and a geometric factor of order 1; the instrument carries no alpha (its couplings are declared).')
for rho in (1.0, 1.0/MPME):
    lo, hi = np.log(1e-12), np.log(1e3)
    f = lambda lm: split(rho, np.exp(lm))[0]/w_A - meas
    flo, fhi = f(lo), f(hi)
    if flo*fhi < 0:
        for _ in range(60):
            mid = 0.5*(lo+hi); fm = f(mid)
            if flo*fm <= 0: hi, fhi = mid, fm
            else: lo, flo = mid, fm
        print(f'rho_B = {rho:.5e}: mu_r that gives splitting/omega_A = measured ratio: {np.exp(0.5*(lo+hi)):.4e}')
    else: print(f'rho_B = {rho:.5e}: no mu_r in [1e-12, 1e3] gives the measured ratio (f(lo) = {flo:.3e}, f(hi) = {fhi:.3e}); the splitting is monotone in mu_r?', f(np.log(1e-3)), f(np.log(1.0)))
