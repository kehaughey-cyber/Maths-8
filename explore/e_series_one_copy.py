"""
E-series, one copy: spinors on the 1440 T-histories, native SU(2) transport on the T step, U(1) link phases on the 720 edges, one joint action.
New file (2026-11-02). Nothing fitted. Reuses the carrier and Qmat of route56_subdiv.py. Observation only: every check is printed raw; nothing is tuned to pass.

Fields.   Psi_h in C^2 for each history h=(u,s) (site = the end vertex s).  a_e real on each undirected edge e={i<j}, oriented i->j (a_ji = -a_ij).
T step.   h=(u,s) -> T(h)=(s,t), t = nearest icosian to phi*s - u (the lab's T, spine D2).  The link used is s->t.
Transport Omega_h (two choices, both run, none preferred in advance):
   'q'     full unit transport  Q(t s^-1)   (F5/F6 'q': a coboundary, so proper holonomy of closed vertex paths is I)
   'gamma' Clifford part  Q(unit Im(t s^-1))  (F5 'gamma': carries the face curvature, Wilson trace -(8/5) sin(pi/5) per route56_native)
Action (L = T_kin - U, units set by kappa, k, I, mu):
   L = sum_h |dPsi_h/dt|^2 + (I/2) sum_e (da_e/dt)^2 - kappa sum_h |d_h|^2 - mu sum_faces (1 - cos F_f)
   d_h = Psi_{T(h)} - exp(i k a_h) Omega_h Psi_h,   a_h = +-a_e (sign of the orientation s->t),   F_f = oriented sum of a around the triangle.
   mu = (48/5) sin(pi/5) is M6 E3's V_spec coefficient, used as an input here and not re-derived.
Gauge: Psi_h -> exp(i lam_end(h)) Psi_h,  a_e -> a_e + (lam_head - lam_tail)/k  leaves d_h and F_f invariant (checked below).
Usage:  py -3 -I -X utf8 -u e_series_one_copy.py > e_series_one_copy.out
"""
import numpy as np, importlib.util, os, sys
np.set_printoptions(suppress=True, linewidth=170)
here = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('sd', os.path.join(here, 'route56_subdiv.py')); sd = importlib.util.module_from_spec(sp); sp.loader.exec_module(sd)
phi = sd.phi; Qmat = sd.Qmat
V = sd.carrier(); N = 120
def qmul(a, b):
    return np.array([a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3], a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
                     a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1], a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]])
def qconj(a): return np.array([a[0], -a[1], -a[2], -a[3]])
def nearest(q):
    d = V @ q; i = int(np.argmax(d)); assert np.linalg.norm(V[i]-q) < 1e-9, 'not a vertex'; return i
Gm = V @ V.T; adj = np.abs(Gm - phi/2) < 1e-9
ADJ = [list(np.where(adj[i])[0]) for i in range(N)]
assert all(len(x) == 12 for x in ADJ)
DE = [(u, s) for u in range(N) for s in ADJ[u]]; deId = {e: i for i, e in enumerate(DE)}; H = len(DE)
TN = np.zeros(H, int)
for h, (u, s) in enumerate(DE):
    t = nearest(phi*V[s] - V[u]); TN[h] = deId[(s, t)]
Tinv = np.zeros(H, int); Tinv[TN] = np.arange(H)
assert len(set(TN)) == H
END = np.array([s for u, s in DE])
EDG = [(i, j) for i in range(N) for j in ADJ[i] if i < j]; eId = {e: k for k, e in enumerate(EDG)}; NE = len(EDG)
eidx = np.zeros(H, int); sgn = np.zeros(H)
for h, (u, s) in enumerate(DE):
    t = DE[TN[h]][1]; eidx[h] = eId[(min(s, t), max(s, t))]; sgn[h] = 1.0 if s < t else -1.0
TAIL = np.array([i for i, j in EDG]); HEAD = np.array([j for i, j in EDG])
Dv = np.zeros((N, NE)); Dv[HEAD, np.arange(NE)] += 1; Dv[TAIL, np.arange(NE)] -= 1          # (div f)_v = sum_{head=v} f - sum_{tail=v} f
def edge_term(x, y):
    return eId[(min(x, y), max(x, y))], (1.0 if x < y else -1.0)
FACES = [(i, j, k) for i in range(N) for j in ADJ[i] if j > i for k in ADJ[j] if k > j and adj[i, k]]
FE = np.zeros((len(FACES), 3), int); FS = np.zeros((len(FACES), 3))
for f, (i, j, k) in enumerate(FACES):
    for c, (x, y) in enumerate(((i, j), (j, k), (k, i))): FE[f, c], FS[f, c] = edge_term(x, y)
def q_st(s, t): return qmul(V[t], qconj(V[s]))
Om = {}
Om['q'] = np.array([Qmat(q_st(s, DE[TN[h]][1])) for h, (u, s) in enumerate(DE)])
def gam(x, y):
    q = q_st(x, y); im = q[1:]; n = im/np.linalg.norm(im); return Qmat(np.array([0.0, *n]))
Om['gamma'] = np.array([gam(s, DE[TN[h]][1]) for h, (u, s) in enumerate(DE)])

# ---------------- structure checks ----------------
print('== structure (spine D2 replay, then the new objects)')
print('vertices', N, 'edges', NE, 'directed edges', H, 'faces', len(FACES))
cyc = []; seen = np.zeros(H, bool)
for h0 in range(H):
    if seen[h0]: continue
    c = []; h = h0
    while not seen[h]: seen[h] = True; c.append(h); h = TN[h]
    cyc.append(c)
print('T-cycles', len(cyc), 'lengths', sorted(set(len(c) for c in cyc)))
t5 = 0
for h in range(H):
    x = h
    for _ in range(5): x = TN[x]
    if abs(V[DE[h][0]] @ V[DE[x][0]] + 1) < 1e-9: t5 += 1
print('T^5 antipode', t5, '/', H)
a4 = np.array([0.3, -0.2, 0.5, 0.1]); b4 = np.array([-0.4, 0.2, 0.1, 0.6])
print('Qmat homomorphism, max |Q(ab)-Q(a)Q(b)| =', np.abs(Qmat(qmul(a4, b4)) - Qmat(a4) @ Qmat(b4)).max())
def su2_angle(M):                         # SO(3) rotation angle of an SU(2) matrix, degrees
    tr = np.trace(M).real; return np.degrees(2*np.arccos(np.clip(tr/2, -1, 1)))
print('\n== face Wilson loops')
for name, fn in (('gamma  g_ij g_jk g_ki (route56_native order)', lambda i, j, k: gam(i, j) @ gam(j, k) @ gam(k, i)),
                 ('q  q_ij q_jk q_ki (index order, F6)', lambda i, j, k: Qmat(q_st(i, j)) @ Qmat(q_st(j, k)) @ Qmat(q_st(k, i))),
                 ('q  q_ki q_jk q_ij (telescoping order)', lambda i, j, k: Qmat(q_st(k, i)) @ Qmat(q_st(j, k)) @ Qmat(q_st(i, j)))):
    trs = np.array([np.trace(fn(i, j, k)) for i, j, k in FACES])
    print(name, ': trace mean', repr(trs.real.mean()), 'std', repr(trs.real.std()), 'imag max', abs(trs.imag).max(), 'rot angle', su2_angle(fn(*FACES[0])))
print('reference: -(8/5) sin(pi/5) =', repr(-1.6*np.sin(np.pi/5)))

# ---------------- holonomy and spectrum of the matter operator on the T-cycles (a = 0) ----------------
print('\n== T-cycle holonomy of the transport (later step on the left)')
for key in ('q', 'gamma'):
    ang = []; trs = []
    for c in cyc:
        M = np.eye(2, dtype=complex)
        for h in c: M = Om[key][h] @ M
        ang.append(su2_angle(M)); trs.append(np.trace(M).real)
    u, cnt = np.unique(np.round(trs, 9), return_counts=True)
    print(key, ': traces (value:count)', dict(zip(u.tolist(), cnt.tolist())))
print('\n== matter operator at a = 0, per T-cycle blocks (20x20): singular values^2 of d = Psi_T - Omega Psi, kappa = 1')
def block_spec(key):
    out = []
    for c in cyc:
        n = len(c); M = np.zeros((2*n, 2*n), complex)
        for i, h in enumerate(c):
            M[2*i:2*i+2, 2*((i+1) % n):2*((i+1) % n)+2] += np.eye(2); M[2*i:2*i+2, 2*i:2*i+2] -= Om[key][h]
        out.append(np.linalg.svd(M, compute_uv=False)**2)
    return np.concatenate(out)
for key in ('q', 'gamma'):
    s2 = block_spec(key); nul = int((s2 < 1e-10).sum())
    u, cnt = np.unique(np.round(s2[s2 >= 1e-10], 8), return_counts=True)
    print(key, ': modes', len(s2), 'null modes (s^2<1e-10)', nul, '| nonzero s^2 min', repr(s2[s2 >= 1e-10].min()), 'max', repr(s2.max()), '| distinct nonzero values', len(u))
    print('   first distinct (value:count):', dict(list(zip(u.tolist(), cnt.tolist()))[:8]))

# ---------------- the joint action ----------------
kap = 1.0; kk = 1.0; Ilk = 1.0
MU_N = 48.0/5*np.sin(np.pi/5)
def parts(psi, a, key, mu, kap=kap, kk=kk):
    ah = sgn*a[eidx]; ph = np.exp(1j*kk*ah)
    src = np.einsum('hij,hj->hi', Om[key], psi)*ph[:, None]
    d = psi[TN] - src
    Fs = (FS*a[FE]).sum(1)
    return ph, src, d, Fs
def energy(psi, vel, a, adot, key, mu):
    ph, src, d, Fs = parts(psi, a, key, mu)
    Ek = (np.abs(vel)**2).sum(); Ea = 0.5*Ilk*(adot**2).sum(); Gp = kap*(np.abs(d)**2).sum(); Vf = mu*(1-np.cos(Fs)).sum()
    return Ek + Ea + Gp + Vf, (Ek, Ea, Gp, Vf)
def forces(psi, a, key, mu):
    ph, src, d, Fs = parts(psi, a, key, mu)
    Ompd = np.einsum('hji,hj->hi', Om[key].conj(), d)
    Fpsi = -kap*(d[Tinv] - np.conj(ph)[:, None]*Ompd)                       # Psi'' = -dG/dPsi^dagger
    dGdah = kap*2*kk*np.imag(np.einsum('hi,hi->h', d.conj(), src))          # dG/da_h
    dGda = np.zeros(NE); np.add.at(dGda, eidx, sgn*dGdah)
    dVda = np.zeros(NE)
    for c in range(3): np.add.at(dVda, FE[:, c], FS[:, c]*mu*np.sin(Fs))
    return Fpsi, -(dGda + dVda)/Ilk, dGda, dVda
def step(psi, vel, a, adot, dt, key, mu, live=True):
    Fp, Fa, _, _ = forces(psi, a, key, mu)
    vel_h = vel + 0.5*dt*Fp; adot_h = adot + 0.5*dt*Fa if live else adot
    psi2 = psi + dt*vel_h; a2 = a + dt*adot_h if live else a
    Fp2, Fa2, _, _ = forces(psi2, a2, key, mu)
    return psi2, vel_h + 0.5*dt*Fp2, a2, (adot_h + 0.5*dt*Fa2 if live else adot)
def rho(psi, vel):                          # Noether charge per site
    r = np.zeros(N); np.add.at(r, END, 2*np.imag(np.einsum('hi,hi->h', psi.conj(), vel))); return r
def gauss(psi, vel, adot, s): return Ilk*(Dv @ adot) + s*kk*rho(psi, vel)
rng = np.random.default_rng(20261102)
def rand_state(sc=0.3):
    return (sc*(rng.standard_normal((H, 2))+1j*rng.standard_normal((H, 2))), sc*(rng.standard_normal((H, 2))+1j*rng.standard_normal((H, 2))),
            rng.uniform(-sc, sc, NE), sc*rng.standard_normal(NE))

print('\n== force check against finite differences (random state)')
for key in ('q', 'gamma'):
    psi, vel, a, adot = rand_state()
    Fp, Fa, dGda, dVda = forces(psi, a, key, MU_N)
    def Pot(psi, a): ph, src, d, Fs = parts(psi, a, key, MU_N); return kap*(np.abs(d)**2).sum() + MU_N*(1-np.cos(Fs)).sum()
    e = 1e-6; dir_a = rng.standard_normal(NE); fd_a = (Pot(psi, a+e*dir_a) - Pot(psi, a-e*dir_a))/(2*e)
    dp = rng.standard_normal((H, 2))+1j*rng.standard_normal((H, 2)); fd_p = (Pot(psi+e*dp, a) - Pot(psi-e*dp, a))/(2*e)
    print(key, ': da  analytic', repr(((dGda+dVda)*dir_a).sum()), 'fd', repr(fd_a), '| dPsi analytic', repr(-2*np.real((Fp*dp.conj()).sum())), 'fd', repr(fd_p))

def run(key, mu, nsteps, dt, init, live=True, snap=None):
    psi, vel, a, adot = [x.copy() for x in init]; E0 = energy(psi, vel, a, adot, key, mu)[0]; out = {'E0': E0, 'Emax': 0.0}
    G0 = {s: gauss(psi, vel, adot, s) for s in (1, -1)}; gd = {1: 0.0, -1: 0.0}; snaps = []
    for n in range(1, nsteps+1):
        psi, vel, a, adot = step(psi, vel, a, adot, dt, key, mu, live)
        E = energy(psi, vel, a, adot, key, mu)[0]; out['Emax'] = max(out['Emax'], abs(E-E0))
        for s in (1, -1): gd[s] = max(gd[s], np.abs(gauss(psi, vel, adot, s)-G0[s]).max())
        if snap and n % snap == 0: snaps.append((n*dt, psi.copy(), vel.copy(), a.copy(), adot.copy()))
    out['gauss_drift'] = gd; out['final'] = (psi, vel, a, adot); out['snaps'] = snaps
    return out

print('\n== energy, Gauss and continuity (random initial data, 2000 steps)')
for key in ('q', 'gamma'):
    for mu in (0.0, MU_N):
        init = rand_state()
        o = run(key, mu, 2000, 0.02, init); o2 = run(key, mu, 4000, 0.01, init)
        E0 = o['E0']
        print(f'{key:5s} mu={mu:8.5f}: E0 {E0:.10f} | max|dE| dt=.02: {o["Emax"]:.3e}  dt=.01: {o2["Emax"]:.3e} | Gauss drift (s=+1) {o["gauss_drift"][1]:.3e}  (s=-1) {o["gauss_drift"][-1]:.3e}')
    psi, vel, a, adot = rand_state()
    Fp, Fa, dGda, dVda = forces(psi, a, key, MU_N)
    rdot = np.zeros(N); np.add.at(rdot, END, 2*np.imag(np.einsum('hi,hi->h', psi.conj(), Fp)))
    jedge = dGda/kk
    print(f'   continuity ({key}): max |rho_dot - s*div j|  s=+1: {np.abs(rdot - Dv@jedge).max():.3e}   s=-1: {np.abs(rdot + Dv@jedge).max():.3e}   (j_e = dG/da_e / k);  max|rho_dot| {np.abs(rdot).max():.3e}')
    print(f'   div(dV/da) max (gauge invariance of V_spec): {np.abs(Dv@dVda).max():.3e}')

print('\n== gauge covariance: evolve, and evolve the gauge-transformed state; compare after the transform (500 steps)')
for key in ('q', 'gamma'):
    psi, vel, a, adot = rand_state(); lam = rng.uniform(-np.pi, np.pi, N)
    def gt(psi, vel, a, adot):
        ph = np.exp(1j*lam[END])[:, None]; return psi*ph, vel*ph, a + (lam[HEAD]-lam[TAIL])/kk, adot
    o1 = run(key, MU_N, 500, 0.02, (psi, vel, a, adot)); psiT = gt(psi, vel, a, adot); o2 = run(key, MU_N, 500, 0.02, psiT)
    A1 = gt(*o1['final']); A2 = o2['final']
    print(key, ': max diff Psi', np.abs(A1[0]-A2[0]).max(), ' Psi_dot', np.abs(A1[1]-A2[1]).max(), ' a', np.abs(A1[2]-A2[2]).max(), ' a_dot', np.abs(A1[3]-A2[3]).max())
    e1 = energy(psi, vel, a, adot, key, MU_N)[0]; e2 = energy(*psiT, key, MU_N)[0]; print('   energy before/after gauge transform:', repr(e1), repr(e2))

print('\n== neutral pair, Gauss-prepared; live links versus frozen links (T = 40, dt = 0.02)')
def pair_state(key, v1, v2, amp=0.5, w=0.5, s=None):
    psi = np.zeros((H, 2), complex); vel = np.zeros((H, 2), complex)
    for h in range(H):
        if END[h] == v1: psi[h] = [amp, 0]; vel[h] = -1j*w*psi[h]
        if END[h] == v2: psi[h] = [amp, 0]; vel[h] = +1j*w*psi[h]
    r = rho(psi, vel); Lm = 12*np.eye(N) - (adj*1.0)
    rhs = -s*kk*r/Ilk; rhs = rhs - rhs.mean()                               # total charge is zero on the closed lattice; remove the roundoff
    phiv = np.linalg.lstsq(Lm, rhs, rcond=1e-10)[0]; adot = phiv[HEAD] - phiv[TAIL]
    return psi, vel, np.zeros(NE), adot, r
far = int(np.argmin(V @ V[0]))
for key in ('q', 'gamma'):
    for s in (1, -1):
        psi, vel, a, adot, r = pair_state(key, 0, far, s=s)
        gres = np.abs(gauss(psi, vel, adot, s)).max()
        print(f'{key} prepared for s={s:+d}: total charge {r.sum():.2e}, Gauss residual at t=0 {gres:.2e}, initial field energy {0.5*Ilk*(adot**2).sum():.5f}')
        for live in (True, False):
            o = run(key, MU_N, 2000, 0.02, (psi, vel, a, adot), live=live, snap=500)
            print(f'  live={live}: max|dE| {o["Emax"]:.2e}, Gauss drift (this s) {o["gauss_drift"][s]:.2e} (other s) {o["gauss_drift"][-s]:.2e}')
            for t, P, Vl, A, Ad in o['snaps']:
                rr = rho(P, Vl); print(f'      t={t:4.0f}: rho(v1)={rr[0]:+.4f} rho(v2)={rr[far]:+.4f} Efield={0.5*Ilk*(Ad**2).sum():.4f} max|a|={np.abs(A).max():.4f}')
