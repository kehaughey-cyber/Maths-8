"""
Expressed / manifest readouts of the E-series state (one copy, and the order dependence of the moment).  New file (2026-11-02).  Nothing fitted.
Setup is executed unchanged from e_series_one_copy.py (carrier, T-histories, edges, faces, transports).

Readouts, each as an expressed quantity (what is present) and a manifest quantity (the net effect), all evaluated at one instant on a state:
  Expressed is counted on the histories h (the finest elements: each carries its own charge rho_h and its own step current g_h); manifest is what survives when they are
  combined at the vertex or edge, where the fields couple.  (First run counted expressed after combining and could not show anything; kept as a failed run.)
  charge   : rho_h = 2 m Im(Psi_h^dag Psi_h') ;  expressed = sum_h |rho_h| ;  manifest = |net charge| and the charge dipole |sum_v rho_v X_v|  (X_v the vertex as a point of R^4)
  current  : g_h = (dG/da_h)/k, the current along history h's own T step; j_e = sum_h sgn_h g_h (flows tail -> head, the continuity current of e_series_one_copy.py);
             expressed = sum_h |g_h| |B_e(h)| ;  manifest = | sum_e j_e B_e |  with B_e = (1/2) X_tail ^ X_head, the bivector of the triangle swept from the origin
             (the magnetic moment of the current, I x Area, as a bivector; norm = sqrt(sum_{i<j} B_ij^2))
  flux     : expressed = sum_f |F_f| |A_f| ;  manifest = | sum_f F_f A_f |,  A_f = (1/2)(X_j-X_i) ^ (X_k-X_i)
States are the exact eigenmodes of the T-cycles (flat transport 'q'; 'gamma' has the half-step shift), prepared at a = 0:  Psi_{T h} = exp(i theta) Omega_h Psi_h,
theta = (2 pi kq [+ pi for gamma]) / 10,  Psi' = -+ i omega Psi,  omega = s sqrt(kappa/m),  s^2 = 2 - 2 cos(theta).  Tick ratio rho enters as m = rho^2 (omega = s/rho).
Usage:  py -3 -I -X utf8 -u e_series_readouts.py > e_series_readouts.out
"""
import numpy as np, importlib.util, os, sys
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e_series_one_copy.py'), encoding='utf-8').read().split('# ---------------- structure checks')[0])
KAP = 1.0; KK = 1.0
def wedge(x, y): return 0.5*(np.outer(x, y) - np.outer(y, x))
def bnorm(B): return float(np.sqrt(0.5*(B**2).sum()))
WE = np.array([wedge(V[TAIL[e]], V[HEAD[e]]) for e in range(NE)]); WEn = np.sqrt(0.5*(WE**2).sum(axis=(1, 2)))
AF = np.array([wedge(V[j]-V[i], V[k]-V[i]) for (i, j, k) in FACES]); AFn = np.sqrt(0.5*(AF**2).sum(axis=(1, 2)))
def hist_currents(psi, a, key):
    ph = np.exp(1j*KK*sgn*a[eidx]); src = np.einsum('hij,hj->hi', Om[key], psi)*ph[:, None]; d = psi[TN] - src
    return KAP*2*np.imag(np.einsum('hi,hi->h', d.conj(), src))                      # g_h = (dG/da_h)/k along the history's own step
def currents(psi, a, key):
    g = hist_currents(psi, a, key); j = np.zeros(NE); np.add.at(j, eidx, sgn*g); return j
def rho_h(psi, vel, m): return 2*m*np.imag(np.einsum('hi,hi->h', psi.conj(), vel))
def rho_v(psi, vel, m): return np.bincount(END, weights=rho_h(psi, vel, m), minlength=N)
def readouts(psi, vel, a, key, m=1.0, geo=1.0):
    r = rho_v(psi, vel, m); rh = rho_h(psi, vel, m); g = hist_currents(psi, a, key); j = currents(psi, a, key); Fs = (FS*a[FE]).sum(1)
    Mj = np.einsum('e,eij->ij', j, WE)*geo**2; MF = np.einsum('f,fij->ij', Fs, AF)*geo**2
    return dict(Q=r.sum(), abs_rho=np.abs(rh).sum(), dip=np.linalg.norm((r[:, None]*V).sum(0))*geo,
                j_exp=(np.abs(g)*WEn[eidx]).sum()*geo**2, j_man=bnorm(Mj), F_exp=(np.abs(Fs)*AFn).sum()*geo**2, F_man=bnorm(MF))
cyc = []; seen = np.zeros(H, bool)
for h0 in range(H):
    if seen[h0]: continue
    c = []; h = h0
    while not seen[h]: seen[h] = True; c.append(h); h = TN[h]
    cyc.append(c)
cid = np.zeros(H, int)
for i, c in enumerate(cyc):
    for h in c: cid[h] = i
def reverse_cycle(i): return cid[deId[(DE[cyc[i][0]][1], DE[cyc[i][0]][0])]]
def ring(i, kq, key, sign, rho=1.0):
    th = (2*np.pi*kq + (np.pi if key == 'gamma' else 0.0))/10; c = cyc[i]; psi = np.zeros((H, 2), complex); psi[c[0]] = [1, 0]
    for n in range(len(c)-1): psi[c[n+1]] = np.exp(1j*th)*Om[key][c[n]] @ psi[c[n]]
    close = np.abs(np.exp(1j*th)*Om[key][c[-1]] @ psi[c[-1]] - psi[c[0]]).max()
    s = np.sqrt(KAP*(2-2*np.cos(th))); om = s/rho
    return psi, sign*(-1j)*om*psi, close, s
print('== check: ring states are eigenmodes of the matter operator (q and gamma)')
for key in ('q', 'gamma'):
    psi, vel, close, s = ring(0, 1, key, -1); ph = np.ones(H); d = psi[TN] - np.einsum('hij,hj->hi', Om[key], psi)
    res = (d[Tinv] - np.einsum('hji,hj->hi', Om[key].conj(), d)) - s**2*psi
    print(key, ': closure residual', close, ' eigen-equation residual', np.abs(res).max(), ' s^2 =', repr(s**2), '(2-2cos theta)')
a0 = np.zeros(NE); R0 = reverse_cycle(0); print('cycle 0 reversed is cycle', R0, '; reverse of that is', reverse_cycle(R0))

def show(name, d):
    print(f'{name:50s} charge: expressed {d["abs_rho"]:9.4f} net Q {d["Q"]:+9.4f} dipole {d["dip"]:7.4f} | current: expressed {d["j_exp"]:9.4f} manifest {d["j_man"]:9.4f} (man/exp {(d["j_man"]/d["j_exp"] if d["j_exp"]>1e-9 else 0):.4f})')
for key in ('q', 'gamma'):
    print(f'\n== expressed / manifest readouts at one instant, transport {key}, rho = 1, kq = 1')
    ps, vs, _, _ = ring(0, 1, key, -1); pr, vr, _, _ = ring(R0, 1, key, +1); pr2, vr2, _, _ = ring(R0, 1, key, -1)
    show('one ring (Q>0)', readouts(ps, vs, a0, key))
    show('ring + its reverse ring, opposite charges (neutral)', readouts(ps+pr, vs+vr, a0, key))
    show('ring + its reverse ring, same charge sign', readouts(ps+pr2, vs+vr2, a0, key))
    mans = []
    for jx in range(1, len(cyc)):
        if jx == R0: continue
        pj, vj, _, _ = ring(jx, 1, key, +1); d = readouts(ps+pj, vs+vj, a0, key); mans.append(d['j_man']/d['j_exp'])
    mans = np.array(mans); print(f'{"ring + any other cycle, opposite charges":50s} manifest/expressed current over the 142 other cycles: min {mans.min():.4f} median {np.median(mans):.4f} max {mans.max():.4f}')
    # all rings: each decagon pair neutral
    P = np.zeros((H, 2), complex); Vv = np.zeros((H, 2), complex); done = set()
    for i in range(len(cyc)):
        if i in done: continue
        j = reverse_cycle(i); done |= {i, j}; a1, b1, _, _ = ring(i, 1, key, -1); a2, b2, _, _ = ring(j, 1, key, +1); P += a1+a2; Vv += b1+b2
    show('all 144 rings, each decagon pair neutral', readouts(P, Vv, a0, key))
    ref_P = P
    rng = np.random.default_rng(7); P = np.zeros((H, 2), complex); Vv = np.zeros((H, 2), complex)
    for i in range(len(cyc)):
        sg = rng.choice([-1, 1]); a1, b1, _, _ = ring(i, 1, key, sg); P += a1; Vv += b1
    show('all 144 rings, random charge signs (seed 7)', readouts(P, Vv, a0, key))
    P = np.zeros((H, 2), complex); Vv = np.zeros((H, 2), complex)
    for i in range(len(cyc)): a1, b1, _, _ = ring(i, 1, key, -1); P += a1; Vv += b1
    show('all 144 rings, same charge sign', readouts(P, Vv, a0, key))
print('\n== one ring, charge -, by mode index kq (transport q): moment per charge')
for kq in range(1, 6):
    ps, vs, _, s = ring(0, kq, 'q', -1); d = readouts(ps, vs, a0, 'q')
    print(f'kq={kq}: omega={s:.6f}  Q={d["Q"]:+.5f}  manifest moment={d["j_man"]:.6f}  moment/|Q|={d["j_man"]/abs(d["Q"]):.6f}')

print('\n== order dependence: one ring, kq = 1, in a copy whose tick is rho times longer (m = rho^2, omega = s/rho); geometry unscaled and scaled by geo = rho')
CODATA_MP_ME = 1836.152673426; ALPHA_INV = 137.035999177
mu_B = 9.2740100657e-24; mu_e = 9.2847646917e-24; mu_p = 1.41060679545e-26
base = None
print(f'{"rho":>12s} {"|Q|":>12s} {"moment (geo=1)":>16s} {"moment/|Q| (geo=1)":>20s} {"x rho":>10s} {"moment/|Q| (geo=rho)":>22s} {"/ rho":>10s}')
for rho in (1.0/CODATA_MP_ME, 1.0/ALPHA_INV, 1.0, 12.0, CODATA_MP_ME):
    ps, vs, _, s = ring(0, 1, 'q', -1, rho); d = readouts(ps, vs, a0, 'q', m=rho**2); d2 = readouts(ps, vs, a0, 'q', m=rho**2, geo=rho)
    r1 = d['j_man']/abs(d['Q']); r2 = d2['j_man']/abs(d2['Q'])
    print(f'{rho:12.6e} {abs(d["Q"]):12.5e} {d["j_man"]:16.6e} {r1:20.6e} {r1*rho:10.6f} {r2:22.6e} {r2/rho:10.6f}')
print('\n== measured comparison (CODATA 2022, moment_benchmark_sourced_values.txt)')
print('model, geometry scaled with the tick (size and tick together): moment per charge in an order whose tick is 1/(m_p/m_e) of the electron order, over the electron order:', repr(1.0/CODATA_MP_ME))
print('measured |mu_p / mu_e| =', repr(mu_p/mu_e), '; mu_N/mu_B = m_e/m_p =', repr(1.0/CODATA_MP_ME), '; mu_e/mu_B =', repr(mu_e/mu_B))
print('model / measured (proton over electron) =', repr((1.0/CODATA_MP_ME)/(mu_p/mu_e)), '= 1/(mu_p/mu_N) up to mu_e/mu_B =', repr(1.0/((mu_p/mu_B)*CODATA_MP_ME)))
print('measured mu_p in nuclear magnetons (table value 2.792847351) -> mu_N/mu_p-order factor the instrument does not produce:', repr(mu_p/(mu_B/CODATA_MP_ME)))
