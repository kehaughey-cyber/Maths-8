"""
A driven transition between the two Zeeman levels of a ring (the resonance NMR measures).  New file (2026-11-02).  Nothing fitted.  Links are imposed, not dynamic; the matter obeys the action's equation
Psi'' = -kappa M^dag M Psi on the 10 histories of cycle 0 (transport q, spinor component (1,0)).
Static flux alpha0 on every ring edge splits the counter-circulating modes kq = 1 and kq = 9 by Delta = omega_9 - omega_1.  A drive couples them: a second harmonic around the ring (pattern cos(2 * 2 pi n / 10),
changing kq by 2) modulated at frequency Omega with amplitude alpha1:  a_n(t) = alpha0 + alpha1 cos(Omega t) cos(4 pi n / 10).
Start in mode kq = 1 (Psi = psi_1, Psi' = -i omega_1 psi_1), integrate with velocity Verlet, record the largest fraction of the mode energy found in kq = 9 over the run, for a scan of Omega.
Mode energy of mode k: |<psi_k|Psi'>|^2 + omega_k^2 |<psi_k|Psi>|^2 with the static omega_k(alpha0); fraction = E_9 / (sum over modes).
Usage:  py -3 -I -X utf8 -u e_series_resonance.py > e_series_resonance.out
"""
import numpy as np, os, sys, time
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
def ringvec(i, kq, key, chi=(1, 0)):
    th = (2*np.pi*kq + (np.pi if key == 'gamma' else 0.0))/10; c = cyc[i]; v = np.zeros((len(c), 2), complex); v[0] = chi
    for m in range(len(c)-1): v[m+1] = np.exp(1j*th)*Om[key][c[m]] @ v[m]
    v = v.reshape(-1); return v/np.linalg.norm(v)
c0 = cyc[0]; n = len(c0); Om_r = np.array([Om['q'][h] for h in c0]); Omd = np.conj(np.transpose(Om_r, (0, 2, 1))); nxt = (np.arange(n)+1) % n; prv = (np.arange(n)-1) % n
def force(P, ah):
    ph = np.exp(1j*ah); d = P[nxt] - ph[:, None]*np.einsum('nij,nj->ni', Om_r, P)
    return -KAP*(d[prv] - np.conj(ph)[:, None]*np.einsum('nij,nj->ni', Omd, d))
def static_modes(alpha0):
    out = []; a = np.zeros(NE)
    for h in c0: a[eidx[h]] = alpha0*sgn[h]
    M = np.zeros((2*n, 2*n), complex)
    for i, h in enumerate(c0):
        ph = np.exp(1j*sgn[h]*a[eidx[h]]); j = (i+1) % n; M[2*i:2*i+2, 2*j:2*j+2] += np.eye(2); M[2*i:2*i+2, 2*i:2*i+2] -= ph*Om['q'][h]
    MM = M.conj().T @ M; ev, U = np.linalg.eigh(MM); return ev, U
def run_drive(alpha0, alpha1, Omega, T, dt, ev, U, v1, k9sel):
    ph0 = np.full(n, alpha0); pat = np.cos(4*np.pi*np.arange(n)/n)
    om1 = np.sqrt(KAP*(v1.conj() @ (U*ev) @ U.conj().T @ v1).real)
    P = v1.reshape(n, 2).copy(); V = -1j*om1*P; best = 0.0; steps = int(T/dt)
    om = np.sqrt(np.maximum(ev, 0)); t = 0.0
    for s in range(steps):
        F = force(P, ph0 + alpha1*np.cos(Omega*t)*pat); Vh = V + 0.5*dt*F; P = P + dt*Vh; t += dt
        F2 = force(P, ph0 + alpha1*np.cos(Omega*t)*pat); V = Vh + 0.5*dt*F2
        if s % 20 == 0:
            cp = U.conj().T @ P.reshape(-1); cv = U.conj().T @ V.reshape(-1); En = np.abs(cv)**2 + ev*np.abs(cp)**2
            fr = En[k9sel].sum()/En.sum(); best = max(best, fr)
    return best
if __name__ == '__main__':
    alpha1 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.06; T = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0; npts = int(sys.argv[3]) if len(sys.argv) > 3 else 41
    print(f'drive amplitude alpha1 = {alpha1}, run length T = {T}, dt = 0.02, second-harmonic pattern cos(4 pi n/10)')
    for alpha0 in (0.05, 0.1):
        ev, U = static_modes(alpha0); v1 = ringvec(0, 1, 'q'); v9 = ringvec(0, 9, 'q')
        w1 = np.sqrt((v1.conj() @ (U*ev) @ U.conj().T @ v1).real); w9 = np.sqrt((v9.conj() @ (U*ev) @ U.conj().T @ v9).real); Delta = abs(w9 - w1)
        # eigenvectors belonging to mode 9: the eigenspace containing v9 (spinor-degenerate pair)
        k9 = np.where(np.abs(ev - w9**2) < 1e-9)[0]; proj = np.abs(U.conj().T @ v9)**2     # the whole (spinor-degenerate) eigenspace of mode 9
        print(f'\nalpha0 = {alpha0}: omega_1 = {w1:.9f}, omega_9 = {w9:.9f}, Delta = {Delta:.9f}; eigen-index of mode 9: {k9.tolist()} (weight {proj[k9].sum():.6f})')
        print(f'{"Omega":>10s} {"Omega/Delta":>12s} {"max fraction in kq=9":>22s}')
        res = []
        for x in np.linspace(0.85, 1.15, npts):
            Om_ = x*Delta; f = run_drive(alpha0, alpha1, Om_, T, 0.02, ev, U, v1, k9); res.append((Om_, x, f)); print(f'{Om_:10.6f} {x:12.4f} {f:22.6f}', flush=True)
        r = np.array(res); ip = int(np.argmax(r[:, 2])); print(f'peak at Omega = {r[ip, 0]:.6f} (Omega/Delta = {r[ip, 1]:.4f}), fraction {r[ip, 2]:.4f}; half-height width (Omega/Delta) from the scan ~', end=' ')
        half = r[:, 2] >= 0.5*r[ip, 2]; print(f'{r[half, 1].min():.3f} to {r[half, 1].max():.3f}')
