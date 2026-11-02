# The spin multiplicity and the size exponent in the hyperfine splittings, from sourced numbers and exact angular-momentum algebra. New file (2026-11-02); nothing fitted.
# Part 1.  Electron spin 1/2 (s) and nuclear spin I coupled by H = A s.I.  The instrument's co/counter-circulating ring difference is the diagonal energy difference between the electron aligned and anti-aligned with the
#          fully polarised nucleus (m_I = I): E(aligned) - E(anti) = A I.  The true level splitting between F = I + 1/2 and F = I - 1/2 is A (I + 1/2).  The ratio is (2I+1)/(2I).  Built here by diagonalising the (2)(2I+1)-dimensional operator.
# Part 2.  Remove from the measured splittings the moment ratio, the multiplicity and the reduced-mass factor; what is left is the size dependence.  For 3He+ against H it is Z^p, and p is read off (nature's exponent).
# Sourced: explore/data/moment_benchmark_sourced_values.txt (hyperfine frequencies secondary), saved IAEA table.  m_e/u recalled (1e-3 level).
# Run: py -3 -I -X utf8 -u explore/spin_multiplet.py > explore/spin_multiplet.out
import numpy as np, math, os, csv
def spin_ops(j):
    d = int(round(2*j+1)); m = np.array([j-i for i in range(d)]); Jz = np.diag(m).astype(complex); Jp = np.zeros((d, d), complex)
    for i in range(1, d): Jp[i-1, i] = math.sqrt(j*(j+1) - m[i]*(m[i]+1))
    Jm = Jp.conj().T; return (Jp+Jm)/2, (Jp-Jm)/(2j), Jz
print('== Part 1: H = A s.I, electron spin 1/2, nuclear spin I (A = 1)')
print(f'{"I":>4s} {"dim":>4s} {"E(F=I+1/2)":>12s} {"E(F=I-1/2)":>12s} {"F splitting":>12s} {"aligned-anti diag":>18s} {"ratio":>8s} {"(2I+1)/(2I)":>12s}')
for I in (0.5, 1.0, 1.5, 2.0, 2.5, 3.5):
    sx, sy, sz = spin_ops(0.5); Ix, Iy, Iz = spin_ops(I); n = int(round(2*I+1))
    Hm = sum(np.kron(a, b) for a, b in ((sx, Ix), (sy, Iy), (sz, Iz))); ev = np.linalg.eigvalsh(Hm); lv = sorted(set(np.round(ev, 9)))
    # diagonal energies in the product basis |m_s, m_I = I>:  A m_s I
    idx_al = 0*n + 0; idx_an = 1*n + 0                                   # |up, m_I = I>, |down, m_I = I>
    dal = Hm[idx_al, idx_al].real; dan = Hm[idx_an, idx_an].real
    print(f'{I:4.1f} {2*n:4d} {lv[-1]:12.6f} {lv[0]:12.6f} {lv[-1]-lv[0]:12.6f} {dal-dan:18.6f} {(lv[-1]-lv[0])/(dal-dan):8.5f} {(2*I+1)/(2*I):12.5f}')
print('\n== Part 2: what is left after the moment ratio, the multiplicity and the reduced-mass factor')
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
def spin(jp):
    s = jp.rstrip('+-'); a, _, b = s.partition('/'); return float(a)/float(b) if b else float(a)
meu = 5.485799090e-4
sysd = {'H': (1, 0, 1420405751.768), 'D': (1, 1, 327384352.5222), '3He+': (2, 1, 8665649867.0)}
info = {}
for k, (Z, N, nu) in sysd.items():
    r = get(Z, N); mu = abs(float(r['magnetic_dipole'])); I = spin(r['jp']); M = (float(r['atomic_mass'])*1e-6 - Z*meu)/meu
    info[k] = dict(Z=Z, mu=mu, I=I, M=M, nu=nu, mult=(2*I+1)/(2*I), red=(1+1/M)**-3)
H0 = info['H']
for k in ('D', '3He+'):
    X = info[k]; meas = X['nu']/H0['nu']; known = (X['mu']/H0['mu'])*(X['mult']/H0['mult'])*(X['red']/H0['red']); resid = meas/known
    print(f'{k:5s}: measured X/H = {meas:.6f}; moment ratio {X["mu"]/H0["mu"]:.6f} x multiplicity ratio {X["mult"]/H0["mult"]:.5f} x reduced-mass ratio {X["red"]/H0["red"]:.6f} = {known:.6f}; left over {resid:.6f}', end='')
    if X['Z'] > 1: print(f' = Z^p with Z = {X["Z"]}: p = {math.log(resid)/math.log(X["Z"]):.5f}')
    else: print(' (Z = 1: the multiplicity and moments account for the whole ratio to', f'{abs(resid-1):.1e})')
print('\nThe size dependence nature shows is the density of the electron at the nucleus, |psi(0)|^2 proportional to (Z/a0)^3: an exponent p = 3 in the size of the electron order, measured here as above (secondary frequencies).')
print('Instrument route with the multiplicity added: X/H = (mu_X/mu_p)(mult ratio)(reduced-mass ratio); D: %.6f against measured %.6f' % ((info['D']['mu']/H0['mu'])*(info['D']['mult']/H0['mult'])*(info['D']['red']/H0['red']), info['D']['nu']/H0['nu']))
