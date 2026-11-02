"""
E-series, two adjacent nested copies, with radial links and inter-copy flux.  New file (2026-11-02).  Nothing fitted; every declared choice is a parameter and is swept, not tuned.
Builds on e_series_one_copy.py (setup section is executed from that file unchanged: carrier, T histories, edges, faces, transports Om['q'] / Om['gamma']).

Copies c = 0 (A) and 1 (B), each exactly the one-copy system, sharing the vertex set.  B is the next order up: its own tick is rho times longer, implemented as
kinetic weight m_B = rho^2 and link inertia I_B = I rho^2 (so every B frequency is 1/rho of A's), potentials unchanged.  rho is a declared choice (swept: 1, phi, 12).
Radial links b_v (120 of them), oriented A -> B, gauge shift  b_v -> b_v + (lam^B_v - lam^A_v)/k.  Two inter-copy terms, each with its own strength (each can be set to 0):
   matter:      kappa_r sum_h | Psi^A_h - exp(-i k b_end(h)) Psi^B_h |^2      (the same history in the two copies; identity identification, a declared choice)
   plaquette:   mu_r sum_e (1 - cos P_e),  P_e = a^A_e + b_head(e) - a^B_e - b_tail(e)     (flux through each radial square, e = lattice edge tail<head)
   radial link kinetic energy (I_r/2) sum_v (db_v/dt)^2.
L = sum_c [ m_c sum_h |Psi_c'|^2 + (I_c/2) sum_e (a_c')^2 - kappa sum_h |d_c,h|^2 - mu sum_f (1 - cos F_c,f) ] + (I_r/2) sum_v b'^2 - kappa_r(...) - mu_r(...).
Per-site Gauss quantities:  A: I_A div a_A' - I_r b'_v + k rho^A_v ;  B: I_B div a_B' + I_r b'_v + k rho^B_v,   rho^c_v = sum_{end(h)=v} 2 m_c Im(Psi^dag Psi').
Usage:  py -3 -I -X utf8 -u e_series_two_copy.py > e_series_two_copy.out
"""
import numpy as np, importlib.util, os, sys
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e_series_one_copy.py'), encoding='utf-8').read().split('# ---------------- structure checks')[0])
MU_N = 48.0/5*np.sin(np.pi/5)
def mkP(rho=1.0, kr=0.0, mur=0.0, Ir=1.0, key='q', mu=MU_N):
    return dict(key=key, mu=mu, kap=1.0, kk=1.0, I=[1.0, rho**2], m=[1.0, rho**2], kr=kr, mur=mur, Ir=Ir, rho=rho)
def forces(psi, a, b, P):
    kap, kk, mu, Om_ = P['kap'], P['kk'], P['mu'], Om[P['key']]
    Fp = [None, None]; dGda = [None, None]
    for c in (0, 1):
        ph = np.exp(1j*kk*sgn*a[c][eidx]); src = np.einsum('hij,hj->hi', Om_, psi[c])*ph[:, None]; d = psi[c][TN] - src
        Fs = (FS*a[c][FE]).sum(1)
        Fp[c] = -kap*(d[Tinv] - np.conj(ph)[:, None]*np.einsum('hji,hj->hi', Om_.conj(), d))
        g = np.zeros(NE); np.add.at(g, eidx, sgn*kap*2*kk*np.imag(np.einsum('hi,hi->h', d.conj(), src)))
        for q in range(3): np.add.at(g, FE[:, q], FS[:, q]*mu*np.sin(Fs))
        dGda[c] = g
    pb = np.exp(-1j*kk*b[END]); z = pb[:, None]*psi[1]; dr = psi[0] - z
    Fp[0] = Fp[0] - P['kr']*dr; Fp[1] = Fp[1] + P['kr']*np.conj(pb)[:, None]*dr
    dGdb = np.zeros(N); np.add.at(dGdb, END, -P['kr']*2*kk*np.imag(np.einsum('hi,hi->h', dr.conj(), z)))
    Pf = a[0] + b[HEAD] - a[1] - b[TAIL]; sp_ = P['mur']*np.sin(Pf)
    Fa = [-(dGda[0] + sp_)/P['I'][0], -(dGda[1] - sp_)/P['I'][1]]
    Fb = -(dGdb + Dv @ sp_)/P['Ir']
    return [Fp[0]/P['m'][0], Fp[1]/P['m'][1]], Fa, Fb
def energies(psi, vel, a, adot, b, bdot, P):
    kap, kk, mu, Om_ = P['kap'], P['kk'], P['mu'], Om[P['key']]; out = {}
    for c in (0, 1):
        ph = np.exp(1j*kk*sgn*a[c][eidx]); d = psi[c][TN] - np.einsum('hij,hj->hi', Om_, psi[c])*ph[:, None]; Fs = (FS*a[c][FE]).sum(1)
        out['matter%d' % c] = P['m'][c]*(np.abs(vel[c])**2).sum() + kap*(np.abs(d)**2).sum()
        out['link%d' % c] = 0.5*P['I'][c]*(adot[c]**2).sum() + mu*(1-np.cos(Fs)).sum()
    dr = psi[0] - np.exp(-1j*kk*b[END])[:, None]*psi[1]; Pf = a[0] + b[HEAD] - a[1] - b[TAIL]
    out['inter'] = P['kr']*(np.abs(dr)**2).sum() + P['mur']*(1-np.cos(Pf)).sum() + 0.5*P['Ir']*(bdot**2).sum()
    out['total'] = out['matter0'] + out['link0'] + out['matter1'] + out['link1'] + out['inter']; return out
def rho_c(psi, vel, P):
    return [np.bincount(END, weights=2*P['m'][c]*np.imag(np.einsum('hi,hi->h', psi[c].conj(), vel[c])), minlength=N) for c in (0, 1)]
def gaussq(psi, vel, adot, bdot, P):
    r = rho_c(psi, vel, P); kk = P['kk']
    return [P['I'][0]*(Dv @ adot[0]) - P['Ir']*bdot + kk*r[0], P['I'][1]*(Dv @ adot[1]) + P['Ir']*bdot + kk*r[1]]
def step(S, dt, P, live=True):
    psi, vel, a, adot, b, bdot = S
    Fp, Fa, Fb = forces(psi, a, b, P)
    vel_h = [vel[c] + 0.5*dt*Fp[c] for c in (0, 1)]
    adot_h = [adot[c] + 0.5*dt*Fa[c] for c in (0, 1)] if live else adot; bdot_h = bdot + 0.5*dt*Fb if live else bdot
    psi2 = [psi[c] + dt*vel_h[c] for c in (0, 1)]
    a2 = [a[c] + dt*adot_h[c] for c in (0, 1)] if live else a; b2 = b + dt*bdot_h if live else b
    Fp2, Fa2, Fb2 = forces(psi2, a2, b2, P)
    return (psi2, [vel_h[c] + 0.5*dt*Fp2[c] for c in (0, 1)], a2, [adot_h[c] + 0.5*dt*Fa2[c] for c in (0, 1)] if live else adot, b2, bdot_h + 0.5*dt*Fb2 if live else bdot)
def copyS(S): return tuple([x.copy() for x in v] if isinstance(v, list) else v.copy() for v in S)
def run(S0, P, nsteps, dt, live=True, snap=None, thr=1e-3):
    S = copyS(S0); e0 = energies(*S, P); G0 = gaussq(S[0], S[1], S[3], S[5], P); out = dict(e0=e0, dEmax=0.0, gd=0.0, snaps=[], tarr=None, fracB=[])
    for n in range(1, nsteps+1):
        S = step(S, dt, P, live); e = energies(*S, P); out['dEmax'] = max(out['dEmax'], abs(e['total']-e0['total']))
        G = gaussq(S[0], S[1], S[3], S[5], P); out['gd'] = max(out['gd'], max(np.abs(G[c]-G0[c]).max() for c in (0, 1)))
        fB = (e['matter1'] + e['link1'])/e0['total']; out['fracB'].append(fB)
        if out['tarr'] is None and fB > thr: out['tarr'] = n*dt
        if snap and n % snap == 0: out['snaps'].append((n*dt, e, S))
    out['final'] = S; return out
rng = np.random.default_rng(20261103)
def rand_S(sc=0.3):
    c = lambda: sc*(rng.standard_normal((H, 2)) + 1j*rng.standard_normal((H, 2)))
    return ([c(), c()], [c(), c()], [rng.uniform(-sc, sc, NE), rng.uniform(-sc, sc, NE)], [sc*rng.standard_normal(NE), sc*rng.standard_normal(NE)],
            rng.uniform(-sc, sc, N), sc*rng.standard_normal(N))
print('== declared parameters: kappa = k = I = I_r = 1, mu = M6 E3 value', repr(MU_N), '(input, not derived); identity identification of histories between copies')

print('\n== force check against finite differences (random state, rho = phi, kappa_r = 0.7, mu_r = 0.9)')
for key in ('q', 'gamma'):
    P = mkP(rho=phi, kr=0.7, mur=0.9, key=key); S = rand_S()
    def Pot(psi, a, b):
        e = energies(psi, [0*psi[0], 0*psi[1]], a, [0*a[0], 0*a[1]], b, 0*b, P); return e['total']
    # potential = total energy at zero velocities (the kinetic terms vanish)
    Fp, Fa, Fb = forces(S[0], S[2], S[4], P); e = 1e-6
    for name, which in (('a_A', 0), ('a_B', 1)):
        dirn = rng.standard_normal(NE); a_p = [x.copy() for x in S[2]]; a_m = [x.copy() for x in S[2]]; a_p[which] += e*dirn; a_m[which] -= e*dirn
        fd = (Pot(S[0], a_p, S[4]) - Pot(S[0], a_m, S[4]))/(2*e); an = -(P['I'][which]*Fa[which]*dirn).sum()
        print(key, name, ': analytic', repr(an), 'fd', repr(fd))
    dirn = rng.standard_normal(N); fd = (Pot(S[0], S[2], S[4]+e*dirn) - Pot(S[0], S[2], S[4]-e*dirn))/(2*e); print(key, 'b  : analytic', repr(-(P['Ir']*Fb*dirn).sum()), 'fd', repr(fd))
    for c in (0, 1):
        dp = rng.standard_normal((H, 2)) + 1j*rng.standard_normal((H, 2)); pp = [x.copy() for x in S[0]]; pm = [x.copy() for x in S[0]]; pp[c] += e*dp; pm[c] -= e*dp
        fd = (Pot(pp, S[2], S[4]) - Pot(pm, S[2], S[4]))/(2*e); an = -2*P['m'][c]*np.real((Fp[c]*dp.conj()).sum()); print(key, 'Psi_%s: analytic' % 'AB'[c], repr(an), 'fd', repr(fd))

print('\n== gauge covariance with independent gauge transformations in each copy (500 steps, rho = phi, kappa_r = 0.7, mu_r = 0.9)')
for key in ('q', 'gamma'):
    P = mkP(rho=phi, kr=0.7, mur=0.9, key=key); S = rand_S(); lam = [rng.uniform(-np.pi, np.pi, N), rng.uniform(-np.pi, np.pi, N)]
    def gt(S):
        psi, vel, a, adot, b, bdot = S; f = [np.exp(1j*lam[c][END])[:, None] for c in (0, 1)]
        return ([psi[c]*f[c] for c in (0, 1)], [vel[c]*f[c] for c in (0, 1)], [a[c] + (lam[c][HEAD]-lam[c][TAIL])/P['kk'] for c in (0, 1)], adot, b + (lam[1]-lam[0])/P['kk'], bdot)
    o1 = run(S, P, 500, 0.02); o2 = run(gt(S), P, 500, 0.02); A1 = gt(o1['final']); A2 = o2['final']
    diffs = [max(np.abs(A1[i][c]-A2[i][c]).max() for c in (0, 1)) if isinstance(A1[i], list) else np.abs(A1[i]-A2[i]).max() for i in range(6)]
    print(key, ': max diff Psi, Psi_dot, a, a_dot, b, b_dot =', ['%.2e' % x for x in diffs], '| energy before/after', repr(energies(*S, P)['total']), repr(energies(*gt(S), P)['total']))

print('\n== energy order, per-site Gauss in both copies (random data, 2000 steps dt .02 and 4000 steps dt .01)')
for key in ('q', 'gamma'):
    for rho in (1.0, phi, 12.0):
        P = mkP(rho=rho, kr=0.7, mur=0.9, key=key); S = rand_S(); o = run(S, P, 2000, 0.02); o2 = run(S, P, 4000, 0.01)
        print(f'{key:5s} rho={rho:7.4f}: E0 {o["e0"]["total"]:.8f} | max|dE| dt=.02 {o["dEmax"]:.3e} dt=.01 {o2["dEmax"]:.3e} ratio {o["dEmax"]/o2["dEmax"]:.2f} | Gauss drift (A and B, all sites) {o["gd"]:.2e}')

print('\n== decoupling: kappa_r = mu_r = 0 and rho = 1; copy A with copy B random equals copy A with copy B zero')
P = mkP(rho=1.0, kr=0.0, mur=0.0, key='q'); S = rand_S(); Z = copyS(S)
Z[0][1][:] = 0; Z[1][1][:] = 0; Z[2][1][:] = 0; Z[3][1][:] = 0
o1 = run(S, P, 500, 0.02); o2 = run(Z, P, 500, 0.02)
print('max diff of copy A (Psi, a) after 500 steps between the two runs:', np.abs(o1['final'][0][0]-o2['final'][0][0]).max(), np.abs(o1['final'][2][0]-o2['final'][2][0]).max())

print('\n== listening: neutral pair in copy A (vertex 0 and its antipode), Gauss-prepared with the links; copy B empty; links live; T = 40, dt = 0.02')
far = int(np.argmin(V @ V[0]))
def pair_S(P, amp=0.5, w=0.5):
    psi = [np.zeros((H, 2), complex), np.zeros((H, 2), complex)]; vel = [np.zeros((H, 2), complex), np.zeros((H, 2), complex)]
    for h in range(H):
        if END[h] == 0: psi[0][h] = [amp, 0]; vel[0][h] = -1j*w*psi[0][h]
        if END[h] == far: psi[0][h] = [amp, 0]; vel[0][h] = +1j*w*psi[0][h]
    r = rho_c(psi, vel, P)[0]; Lm = 12*np.eye(N) - (adj*1.0); rhs = -P['kk']*r/P['I'][0]; rhs = rhs - rhs.mean()
    phiv = np.linalg.lstsq(Lm, rhs, rcond=1e-10)[0]
    return (psi, vel, [np.zeros(NE), np.zeros(NE)], [phiv[HEAD]-phiv[TAIL], np.zeros(NE)], np.zeros(N), np.zeros(N))
print('columns: rho kappa_r mu_r | t_arrive (B energy > 1e-3 of total) | fraction of total energy in B at t=10,20,30,40 | max fraction | Gauss drift | max|dE|')
for key in ('q', 'gamma'):
    print('--', key)
    for rho in (1.0, phi, 12.0):
        for kr, mur in ((0.0, 0.0), (0.1, 0.0), (1.0, 0.0), (0.0, MU_N), (1.0, MU_N)):
            P = mkP(rho=rho, kr=kr, mur=mur, key=key); S = pair_S(P); o = run(S, P, 2000, 0.02)
            fb = np.array(o['fracB']); at = lambda t: fb[int(round(t/0.02))-1]
            print(f'rho={rho:7.4f} kr={kr:4.1f} mur={mur:7.4f} | t_arr {("%.2f" % o["tarr"]) if o["tarr"] is not None else "none":>6} | {at(10):.4f} {at(20):.4f} {at(30):.4f} {at(40):.4f} | max {fb.max():.4f} | gauss {o["gd"]:.1e} | dE {o["dEmax"]:.1e}')
print('\n== frozen-link control (links held fixed), q, rho = phi, kappa_r = 1, mu_r = M6 value')
P = mkP(rho=phi, kr=1.0, mur=MU_N, key='q'); S = pair_S(P)
for live in (True, False):
    o = run(S, P, 2000, 0.02, live=live); fb = np.array(o['fracB']); print('live' if live else 'frozen', ': max fraction in B', f'{fb.max():.4f}', '| fraction at t=40', f'{fb[-1]:.4f}', '| Gauss drift', f'{o["gd"]:.2e}', '| max|dE|', f'{o["dEmax"]:.2e}')
