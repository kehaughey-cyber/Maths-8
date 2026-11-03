"""
E-series: the Fermi-contact (spin-magnetization) coupling between the two copies.  New file (2026-11-03).  Nothing fitted; J is a declared parameter, swept.
The existing action couples charge current only (U(1) link phases act on both spinor components alike), so the spin of Psi has no energy in a field (e_series_response.out section 2: spin splitting 0).
Contact term (a vertex-local spin-spin coupling between copy A and copy B, the analogue of (8 pi/3) mu_e . mu_N delta(r)):
    s^c_v = (1/2) sum_{h: end(h) = v} Psi^c_h^dagger sigma Psi^c_h  (3-vector, c = A, B),     E_contact = J sum_v s^A_v . s^B_v.
Gauge properties by construction: invariant under independent U(1) phases of every history in both copies (so Gauss and continuity are untouched), and under any common SU(2) rotation of all histories that end at v
(spinors of both copies rotated together), so no frame choice enters.  It does not involve a, b, or the transport.  Force: F^A_h = -(J/2) (sigma . s^B_{end(h)}) Psi^A_h, and the same for B with s^A.
Mean-field consequence (exact on a cycle, because the term is diagonal in histories): with B fixed, A's quadratic form on a T-cycle c is  M_c = kappa B_c^dagger B_c + K_c,  K_c = (J/2) diag_h (sigma . s^B_{end(h)}).
Checks printed: force against finite differences; invariance under random per-history U(1) phases and per-vertex SU(2) rotations; energy fluctuation of the live dynamics at dt and dt/2 (second order); Gauss conservation with J != 0.
Readouts: the shift of A's ring modes (kq = +-1, spinor up/down) and of its static (kq = 0) modes when B is a ring of unit charge on cycle 22 with spinor (1, 0), as a function of J; the dependence on the spin-density overlap.
Usage:  py -3 -I -X utf8 -u e_series_contact.py > e_series_contact.out
"""
import numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_two_copy.py'), encoding='utf-8').read().split("rng = np.random.default_rng(20261103)")[0])
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)
def svec(psi_c):
    """per-vertex spin density (N, 3): (1/2) sum over histories ending at v of psi^dagger sigma psi"""
    h3 = 0.5*np.real(np.einsum('hi,kij,hj->hk', psi_c.conj(), SIG, psi_c)); out = np.zeros((N, 3))
    for k in range(3): out[:, k] = np.bincount(END, weights=h3[:, k], minlength=N)
    return out
def contact_energy(psi, P): return P.get('J', 0.0)*np.sum(svec(psi[0])*svec(psi[1]))
forces_base, energies_base = forces, energies
def contact_force(psi, P):
    J = P.get('J', 0.0); sA, sB = svec(psi[0]), svec(psi[1])
    GA = 0.5*J*np.einsum('hk,kij,hj->hi', sB[END], SIG, psi[0]); GB = 0.5*J*np.einsum('hk,kij,hj->hi', sA[END], SIG, psi[1])
    return [GA, GB]                                            # dE/dPsi^* for each copy
def forces(psi, a, b, P):
    Fp, Fa, Fb = forces_base(psi, a, b, P)
    if P.get('J', 0.0) != 0.0:
        G = contact_force(psi, P); Fp = [Fp[c] - G[c]/P['m'][c] for c in (0, 1)]
    return Fp, Fa, Fb
def energies(psi, vel, a, adot, b, bdot, P):
    out = energies_base(psi, vel, a, adot, b, bdot, P); out['contact'] = contact_energy(psi, P); out['total'] = out['total'] + out['contact']; return out

print('== contact-term checks')
rng = np.random.default_rng(20261103)
P = mkP(rho=1.0, kr=0.3, mur=0.2, key='q'); P['J'] = 0.7
psi = [rng.normal(size=(H, 2)) + 1j*rng.normal(size=(H, 2)) for _ in (0, 1)]
G = contact_force(psi, P); worst = 0.0
for c in (0, 1):
    dl = rng.normal(size=(H, 2)) + 1j*rng.normal(size=(H, 2)); eps = 1e-6; pp = [x.copy() for x in psi]; pm = [x.copy() for x in psi]; pp[c] = pp[c] + eps*dl; pm[c] = pm[c] - eps*dl
    num = (contact_energy(pp, P) - contact_energy(pm, P))/(2*eps); ana = 2*np.real(np.sum(np.conj(G[c])*dl)); worst = max(worst, abs(num-ana)/abs(ana))
    print(f'  copy {"AB"[c]}: dE/d(eps) numerical {num:.10f}, from force {ana:.10f}')
print(f'  force against finite differences, worst relative error {worst:.2e}')
E0 = contact_energy(psi, P); ph = np.exp(1j*rng.uniform(0, 2*np.pi, size=(2, H)))
E1 = contact_energy([psi[0]*ph[0][:, None], psi[1]*ph[1][:, None]], P); print(f'  per-history U(1) phases: E {E0:.12f} -> {E1:.12f} (difference {E1-E0:+.1e})')
def su2(rng_):
    q = rng_.normal(size=4); q /= np.linalg.norm(q); return np.array([[q[0]+1j*q[3], q[2]+1j*q[1]], [-q[2]+1j*q[1], q[0]-1j*q[3]]])
Us = [su2(rng) for _ in range(N)]; rot = lambda ps: np.array([Us[END[h]] @ ps[h] for h in range(H)])
E2 = contact_energy([rot(psi[0]), rot(psi[1])], P); print(f'  per-vertex common SU(2) rotation of both copies: E {E0:.12f} -> {E2:.12f} (difference {E2-E0:+.1e})')
E3 = contact_energy([rot(psi[0]), psi[1]], P); print(f'  rotating only copy A (not an invariance, for contrast): E -> {E3:.6f}')

print('\n== live dynamics with the contact term (two copies, radial links)')
def rand_state(sc):
    ps = [sc*(rng.normal(size=(H, 2)) + 1j*rng.normal(size=(H, 2))) for _ in (0, 1)]; vl = [sc*(rng.normal(size=(H, 2)) + 1j*rng.normal(size=(H, 2))) for _ in (0, 1)]
    a_ = [sc*rng.normal(size=NE) for _ in (0, 1)]; ad = [sc*rng.normal(size=NE) for _ in (0, 1)]; b_ = sc*rng.normal(size=N); bd = sc*rng.normal(size=N)
    return (ps, vl, a_, ad, b_, bd)
for sc, Jd in ((0.05, 0.7), (0.3, 0.0), (0.3, 0.7)):
    S0 = rand_state(sc); Pd = mkP(rho=1.0, kr=0.3, mur=0.2, key='q'); Pd['J'] = Jd
    for dt, nst in ((0.02, 400), (0.01, 800)):
        with np.errstate(all='ignore'):
            r = run(S0, Pd, nst, dt)
        print(f'  amplitude {sc}, J = {Jd}, dt = {dt}: max |E(t) - E(0)| = {r["dEmax"]:.4e} over t = {nst*dt}; Gauss drift {r["gd"]:.2e}; E0 = {r["e0"]["total"]:.6f} (contact {r["e0"]["contact"]:.6f})')

print('\n== mean-field readout: A on a T-cycle, B a unit-charge ring on cycle 22 with spinor (1, 0)')
def ringvec(i, kq, key, chi=(1, 0)):
    th = (2*np.pi*kq + (np.pi if key == 'gamma' else 0.0))/10; c = cyc[i]; v = np.zeros((len(c), 2), complex); v[0] = chi
    for n in range(len(c)-1): v[n+1] = np.exp(1j*th)*Om[key][c[n]] @ v[n]
    v = v.reshape(-1); return v/np.linalg.norm(v)
def block_c(c, key):
    n = len(c); M = np.zeros((2*n, 2*n), complex)
    for i, h in enumerate(c):
        j = (i+1) % n; M[2*i:2*i+2, 2*j:2*j+2] += np.eye(2); M[2*i:2*i+2, 2*i:2*i+2] -= Om[key][h]
    return M
KEY = 'q'; IB = 22
psiB = np.zeros((H, 2), complex); vB = ringvec(IB, 1, KEY, (1, 0)).reshape(-1, 2)
for n, h in enumerate(cyc[IB]): psiB[h] = vB[n]
sB = svec(psiB); print(f'  B: ring kq = +1 on cycle {IB}, {len(cyc[IB])} histories, total charge density sum |Psi|^2 = {np.sum(np.abs(psiB)**2):.6f}; |s^B_v| per vertex (first 10 vertices of the cycle): ' + ', '.join(f'{np.linalg.norm(sB[DE[h][1]]):.4f}' for h in cyc[IB]))
def link_current_max(i, kq):
    v = ringvec(i, kq, KEY, (1, 0)).reshape(-1, 2); psi_ = np.zeros((H, 2), complex)
    for n, h in enumerate(cyc[i]): psi_[h] = v[n]
    src = np.einsum('hij,hj->hi', Om[KEY], psi_); d = psi_[TN] - src; g = np.zeros(NE); np.add.at(g, eidx, sgn*2*np.imag(np.einsum('hi,hi->h', d.conj(), src)))
    return np.abs(d).max(), np.abs(g).max()
for kq in (0, 1, -1):
    dm, gm = link_current_max(IB, kq); print(f'  ring kq = {kq:+d} on cycle {IB}: max |d_h| (mismatch with the transport) {dm:.3e}, max |link current dG/da| {gm:.3e}')
def cycle_modes(i, J):
    c = cyc[i]; Mb = block_c(c, KEY); Kc = np.zeros((2*len(c), 2*len(c)), complex)
    for n, h in enumerate(c): Kc[2*n:2*n+2, 2*n:2*n+2] = 0.5*J*np.einsum('k,kij->ij', sB[END[h]], SIG)
    w2, U = np.linalg.eigh(Mb.conj().T @ Mb + Kc); return w2, U, Mb
w0, U0, Mb22 = cycle_modes(IB, 0.0)
print('  A on cycle 22, J = 0: eigenvalues of M^dagger M (omega^2):', np.round(w0, 6))
for Jv in (1e-4, 1e-3, 1e-2, 1e-1, 1.0):
    w, U, _ = cycle_modes(IB, Jv); sh = w - w0
    rg = np.where(np.abs(w0 - 0.381966) < 1e-5)[0]; stat = np.where(np.abs(w0) < 1e-9)[0]
    print(f'  J = {Jv:7.0e}: shifts of the kq = +-1 ring modes (omega^2 {w0[rg[0]]:.6f}, 4 modes): ' + ', '.join(f'{x:+.6e}' for x in sh[rg]) + ';  static modes (omega^2 = 0, 2): ' + ', '.join(f'{x:+.6e}' for x in sh[stat]))
print('\n  first-order shifts for A on cycle 22 are linear in J: ratio of shift at J = 1e-3 to shift at J = 1e-2 per unit J, kq = +-1 modes')
wa, _, _ = cycle_modes(IB, 1e-3); wb, _, _ = cycle_modes(IB, 1e-2); rg = np.where(np.abs(w0 - 0.381966) < 1e-5)[0]
print('   ', ((wa-w0)[rg]/1e-3), ((wb-w0)[rg]/1e-2))
print('\n== the same for A on every other cycle: largest ring-mode shift at J = 1e-2 per unit J, against the overlap of A\'s ring density with B\'s (sum_v n^A_v n^B_v for the kq = 1 ring of unit charge)')
nB = np.bincount(END, weights=np.sum(np.abs(psiB)**2, axis=1), minlength=N); rows = []
for i in range(len(cyc)):
    w, U, _ = cycle_modes(i, 1e-2); w00, _, _ = cycle_modes(i, 0.0); ring_i = np.where(np.abs(w00 - 0.381966) < 1e-5)[0]
    vA = ringvec(i, 1, KEY, (1, 0)).reshape(-1, 2); nA = np.zeros(N)
    for n, h in enumerate(cyc[i]): nA[DE[h][1]] += np.sum(np.abs(vA[n])**2)
    rows.append((i, np.max(np.abs(w - w00)[ring_i])/1e-2, float(np.sum(nA*nB))))
rows.sort(key=lambda t: -t[2]); print('  cycle  max |shift|/J   overlap sum n^A n^B   (the 8 largest overlaps, then the median and the smallest nonzero)')
for r_ in rows[:8]: print(f'  {r_[0]:5d}  {r_[1]:12.6e}  {r_[2]:.6e}')
nz = [r_ for r_ in rows if r_[2] > 0]; print(f'  median over cycles with overlap > 0 ({len(nz)} of {len(rows)}): shift/J {np.median([r_[1] for r_ in nz]):.6e}, overlap {np.median([r_[2] for r_ in nz]):.6e}; smallest nonzero overlap {nz[-1][2]:.3e} (shift/J {nz[-1][1]:.3e})')
ov = np.array([r_[2] for r_ in nz]); sh_ = np.array([r_[1] for r_ in nz]); print(f'  correlation of max |shift|/J with the overlap over the {len(nz)} cycles with overlap > 0: {np.corrcoef(ov, sh_)[0, 1]:.6f}')
ID = rows[0]
print('\n== calibration to hydrogen, as an inference to test and not a result: Delta(omega)/omega_A = Delta(omega^2)/(2 omega^2) for the spin-up / spin-down pair of the kq = +1 mode on cycle 22')
w, U, _ = cycle_modes(IB, 1e-3); sh = (w - w0)[rg]
print('  shifts (per unit J):', sh/1e-3, '; omega_A^2 =', w0[rg[0]])
meas = 5.874326e-6/13.605693123; print(f'  measured hydrogen hyperfine / Rydberg = {meas:.6e}')
spl = max(sh) - min(sh); jneeded = meas*2*w0[rg[0]]/(spl/1e-3); print(f'  largest minus smallest ring-mode shift per unit J: {spl/1e-3:.6e}; J that makes Delta(omega)/omega_A equal the measured ratio: {jneeded:.4e}')
