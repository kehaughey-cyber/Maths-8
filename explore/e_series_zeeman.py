"""
Frequency shift of a ring mode under an imposed link flux, read out of the instrument.  New file (2026-11-02).  Nothing fitted.  Links are held fixed ("imposed"); this reads the matter response.
Setup and the ring eigenmodes come from e_series_readouts.py (which executes e_series_one_copy.py's setup).  Units: kappa = k = 1.
Imposed flux: a link phase alpha on every edge of the decagon of cycle C, oriented along the ring, so that history h of C sees a_h = +alpha and the reverse cycle sees -alpha;
the circulation (loop flux) is Phi = sum_e a_e = 10 alpha, and the uniform field through the ring is B = Phi / Area with Area the norm of the oriented bivector sum_e sgn B_e (= 5 sin 36 deg for the unit decagon).
Mode frequency: omega = sqrt(kappa s^2)/rho, s^2 = <psi|M^dag M|psi> for the ring eigenstate psi on the cycle (checked as an eigenvector), M the 20x20 matter operator d = Psi_T - exp(i k a) Omega Psi of the cycle, rho the tick ratio (m = rho^2).
Magnetic moment from the energy response of one quantum: mu = -dE/dB = -(d omega / d alpha) (1/10) Area geo^2 ; compared with the moment per charge from current x area (e_series_readouts.py).
Usage:  py -3 -I -X utf8 -u e_series_zeeman.py > e_series_zeeman.out
"""
import numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
CH = {}
def block(c, a, key):
    n = len(c); M = np.zeros((2*n, 2*n), complex)
    for i, h in enumerate(c):
        ph = np.exp(1j*KK*sgn[h]*a[eidx[h]]); j = (i+1) % n
        M[2*i:2*i+2, 2*j:2*j+2] += np.eye(2); M[2*i:2*i+2, 2*i:2*i+2] -= ph*Om[key][h]
    return M
def ringvec(i, kq, key):
    psi = ring(i, kq, key, -1)[0]; v = np.concatenate([psi[h] for h in cyc[i]]); return v/np.linalg.norm(v)
def flux_a(i, alpha):
    a = np.zeros(NE)
    for h in cyc[i]: a[eidx[h]] = alpha*sgn[h]
    return a
def omega(i, kq, key, alpha, rho=1.0):
    M = block(cyc[i], flux_a(i, alpha), key); v = ringvec(i, kq, key); MM = M.conj().T @ M; s2 = (v.conj() @ MM @ v).real; res = np.linalg.norm(MM @ v - s2*v)
    return np.sqrt(KAP*s2)/rho, res
R0 = reverse_cycle(0)
print('== imposed flux on the decagon of cycle 0')
users = [h for h in range(H) if eidx[h] in set(eidx[x] for x in cyc[0]) and cid[h] not in (0,)]
print('histories outside cycle 0 that use its edges:', len(users), 'all in cycle', sorted(set(cid[h] for h in users)), '(reverse cycle is', R0, ')')
a = flux_a(0, 0.3); print('a_h seen by cycle 0:', sorted(set(np.round([sgn[h]*a[eidx[h]] for h in cyc[0]], 12))), '; by the reverse cycle:', sorted(set(np.round([sgn[h]*a[eidx[h]] for h in cyc[R0]], 12))))
Bsum = sum(sgn[h]*WE[eidx[h]] for h in cyc[0]); AREA = bnorm(Bsum); print('oriented area of the ring (bivector norm) =', repr(AREA), '; 5 sin 36 deg =', repr(5*np.sin(np.pi/5)))
for key in ('q', 'gamma'):
    print(f'\n== transport {key}: frequencies of the two counter-circulating modes (kq = 1 and kq = 9) of cycle 0 against the flux per link alpha (rho = 1)')
    off = 0.0 if key == 'q' else np.pi
    print(f'{"alpha":>10s} {"omega(kq=1)":>14s} {"omega(kq=9)":>14s} {"splitting":>14s} {"2|sin((th1-a)/2)|":>18s} {"2|sin((th9-a)/2)|":>18s} {"eigvec resid":>13s}')
    for al in (0.0, 1e-4, 1e-3, 0.01, 0.05, 0.1, 0.2, 0.3, 0.45, 2*np.pi/10):
        wp, r1 = omega(0, 1, key, al); wm, r2 = omega(0, 9, key, al)
        red = lambda t: (t + np.pi) % (2*np.pi) - np.pi                      # theta reduced to (-pi, pi]
        th = red((2*np.pi*1 + off)/10); thm = red((2*np.pi*9 + off)/10)
        print(f'{al:10.5g} {wp:14.9f} {wm:14.9f} {wp-wm:14.9f} {2*abs(np.sin((th-al)/2)):14.9f} {2*abs(np.sin((thm-al)/2)):14.9f} {max(r1, r2):13.2e}')
    e = 1e-5; wp1, _ = omega(0, 1, key, e); wp2, _ = omega(0, 1, key, -e); dw = (wp1-wp2)/(2*e)
    th = (2*np.pi + off)/10; print('d omega / d alpha at 0 (central difference, kq = 1):', repr(dw), '; analytic -cos(theta/2) =', repr(-np.cos(th/2)), '(eigenvalue |exp(i theta) - exp(i alpha)|, so omega = 2|sin((theta - alpha)/2)|)')
    ps, vs, _, _ = ring(0, 1, key, -1); d = readouts(ps, vs, np.zeros(NE), key); cur = d['j_man']/abs(d['Q']); en = abs(dw)/10*AREA
    print(f'moment per charge: from current x area (readouts) {cur!r}; from -dE/dB = |d omega/d alpha| (1/10) Area {en!r}; ratio {en/cur:.12f}')
print('\n== flux quantum (transport q): one flux quantum per ring is alpha = 2 pi / 10; the levels move to the next ones')
w_at = lambda kq, al: omega(0, kq, 'q', al)[0]
al0 = 0.1; print('with omega = 2|sin((theta - alpha)/2)| a flux quantum moves each level down by one: omega(kq, alpha0 + 2pi/10) should equal omega(kq-1, alpha0)')
for kq in (1, 2, 3, 4):
    print(f'   kq={kq}: omega(kq, alpha0+2pi/10) = {w_at(kq, al0+2*np.pi/10)!r} ; omega(kq-1, alpha0) = {w_at(kq-1, al0)!r}')
M0 = block(cyc[0], flux_a(0, 0.0), 'q'); M1 = block(cyc[0], flux_a(0, 2*np.pi/10), 'q')
s0 = np.sort(np.linalg.eigvalsh(M0.conj().T @ M0)); s1 = np.sort(np.linalg.eigvalsh(M1.conj().T @ M1)); print('spectrum of M^dag M at alpha = 0 and at one flux quantum, max difference of the sorted 20 values:', np.abs(s0-s1).max())
print('\n== order dependence (transport q): energy-response moment against the current x area moment, kq = 1, alpha-derivative by central difference')
print(f'{"rho":>12s} {"d omega/d alpha":>16s} {"mu/q from energy":>18s} {"mu/q from current":>18s} {"ratio":>14s} {"x rho":>10s}')
for rho in (1/1836.152673426, 1/137.035999177, 1.0, (1+5**.5)/2, 12.0, 1836.152673426):
    e = 1e-5; wp1, _ = omega(0, 1, 'q', e, rho); wp2, _ = omega(0, 1, 'q', -e, rho); dw = (wp1-wp2)/(2*e)
    ps, vs, _, _ = ring(0, 1, 'q', -1, rho); d = readouts(ps, vs, np.zeros(NE), 'q', m=rho**2); cur = d['j_man']/abs(d['Q']); en = abs(dw)/10*AREA
    print(f'{rho:12.6e} {dw:16.9e} {en:18.9e} {cur:18.9e} {en/cur:14.10f} {en*rho:10.6f}')
print('\n== uniform flux on every decagon (each undirected edge belongs to exactly one decagon pair; alpha along the forward cycle of each pair)')
fw = []; done = set()
for i in range(len(cyc)):
    if i in done: continue
    j = reverse_cycle(i); done |= {i, j}; fw.append(i)
print('decagon pairs:', len(fw))
for al in (0.05, 0.1, 0.3):
    a = np.zeros(NE); used = np.zeros(NE, int)
    for i in fw:
        for h in cyc[i]: a[eidx[h]] = al*sgn[h]; used[eidx[h]] += 1
    wps = []; wms = []
    for i in range(len(cyc)):
        M = block(cyc[i], a, 'q'); v1 = ringvec(i, 1, 'q'); v9 = ringvec(i, 9, 'q'); MM = M.conj().T @ M
        wps.append(np.sqrt((v1.conj() @ MM @ v1).real)); wms.append(np.sqrt((v9.conj() @ MM @ v9).real))
    wps = np.array(wps); wms = np.array(wms); Fs = (FS*a[FE]).sum(1); Vf = (1-np.cos(Fs)).sum()
    print(f'alpha={al}: each edge assigned once: {bool((used == 1).all())}; omega(kq=1) over the 144 cycles: min {wps.min():.9f} max {wps.max():.9f}; omega(kq=9): min {wms.min():.9f} max {wms.max():.9f}; analytic 2|sin((th-al)/2)| for th = +36 deg, -36 deg: {2*abs(np.sin((2*np.pi/10-al)/2)):.9f} / {2*abs(np.sin((-2*np.pi/10-al)/2)):.9f}')
    print(f'    face flux this imposes: nonzero on {(np.abs(Fs) > 1e-12).sum()} of {len(FACES)} faces, max |F| {np.abs(Fs).max():.4f}, sum(1-cos F) {Vf:.4f} (times mu for the field energy)')
