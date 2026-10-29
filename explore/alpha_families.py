# The four untested alpha families, run parameter-free. New file; floor and earlier files untouched.
# F1 T-C beat on the 1,440 histories; F2 propagation dispersion of the 4D icosian lattice (exact + lattice check);
# F3 cross-scale reinjection and mixing of the 144 ten-cycles; F4 recursion-limit sums over the contraction ladder.
# Targets are fixed before running: 1/alpha, 2pi/alpha, pi/alpha, alpha/2pi (tolerance 1e-9 for sweeps; CODATA 2018/2022 spread 6.8e-10).
import numpy as np, math, itertools, os
from fractions import Fraction
from mpmath import mp, mpf, besselj, besseljzero, findroot, nstr
mp.dps = 25
phi = (1+5**.5)/2; pi = math.pi
al = 7.2973525693e-3; T = 1/al; Tmid = 0.5*(T+137.035999177)
targets = {'1/alpha': Tmid, '2pi/alpha': 2*pi*Tmid, 'pi/alpha': pi*Tmid}
print('alpha', al, ' 1/alpha', T, ' alpha/2pi', al/(2*pi), ' 2pi/alpha', 2*pi/al)

# ---------- carrier: 120 unit icosians, quaternion product ----------
def qm(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2, w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2])
verts = []
for i in range(4):
    for s in (1, -1):
        v = np.zeros(4); v[i] = s; verts.append(v)
for sg in itertools.product((.5, -.5), repeat=4): verts.append(np.array(sg))
par = lambda p: sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2
base = [phi/2, .5, 1/(2*phi), 0.0]
for p in itertools.permutations(range(4)):
    if par(p): continue
    for sg in itertools.product((1, -1), repeat=3):
        v = np.zeros(4); k = 0
        for pos in range(4):
            val = base[p[pos]]
            if val != 0.0: v[pos] = val*sg[k]; k += 1
        verts.append(v)
V = np.array(verts); key = lambda v: tuple(np.round(v, 6)+0.0); idx = {key(v): i for i, v in enumerate(V)}
closed = all(key(qm(V[i], V[j])) in idx for i in range(120) for j in range(120))
print('\nCarrier: 120 vertices, closed under quaternion product:', closed)
Gm = V@V.T; A = ((Gm > .8) & (Gm < .82)).astype(float); nbr = [list(np.nonzero(A[i])[0]) for i in range(120)]
H = [(u, s) for u in range(120) for s in nbr[u]]; hid = {h: i for i, h in enumerate(H)}; NH = len(H)
Tn = np.array([hid[(s, idx[key(phi*V[s]-V[u])])] for (u, s) in H])

def order(g):
    x = g.copy(); n = 1
    while not np.allclose(x, [1, 0, 0, 0], atol=1e-6): x = qm(x, g); n += 1
    return n
ords = [order(V[i]) for i in range(120)]
print('element orders:', {o: ords.count(o) for o in sorted(set(ords))})
A5 = [i for i in range(120) if ords[i] == 5]; B6 = [i for i in range(120) if ords[i] == 6]
print('order-5 elements', len(A5), ' order-6 elements', len(B6), ' pairs (a,b):', len(A5)*len(B6))

def cyc_lengths(perm):
    seen = np.zeros(len(perm), bool); L = []
    for i in range(len(perm)):
        if not seen[i]:
            j = i; c = 0
            while not seen[j]: seen[j] = True; j = perm[j]; c += 1
            L.append(c)
    return L
def Cperm(a, b):
    vp = np.array([idx[key(qm(qm(V[a], V[i]), V[b]))] for i in range(120)])
    return vp, np.array([hid[(vp[u], vp[s])] for (u, s) in H])

print('\n=== F1  T-C beat on the 1,440 histories ===')
rng = np.random.default_rng(0)
pairs = [(A5[i], B6[j]) for i in range(len(A5)) for j in range(len(B6))]
commute = 0; clens = set(); c15 = 0; maxL = 0; sample = [pairs[k] for k in rng.choice(len(pairs), 24, replace=False)]
for (a, b) in pairs:
    vp, Cp = Cperm(a, b)
    if np.array_equal(Cp[Tn], Tn[Cp]): commute += 1
for (a, b) in sample:
    vp, Cp = Cperm(a, b)
    clens |= set(cyc_lengths(Cp))
    Cn = np.arange(NH)
    for _ in range(15): Cn = Cp[Cn]
    c15 += int(all(np.allclose(V[vp[i]], V[i]) or True for i in range(1)))
    # max cycle length over all elements T^i C^j of the abelian group
    Ti = np.arange(NH)
    for i in range(10):
        Cj = Ti.copy()
        for j in range(30):
            maxL = max(maxL, max(cyc_lengths(Cj)))
            Cj = Cp[Cj]
        Ti = Tn[Ti]
print('  all 480 C = L_a R_b (a order 5, b order 6) commute with T on histories:', commute, '/', len(pairs))
print('  cycle lengths of C on histories (24 sampled):', sorted(clens), ';  max cycle length over all T^i C^j (24 C sampled):', maxL)
print('  => every eigenphase of any T^i C^j is a multiple of 1/%d cycle; smallest nonzero beat = %.6f cycle; alpha/2pi = %.7f cycle (ratio %.2f)' % (maxL, 1/maxL, al/(2*pi), (1/maxL)/(al/(2*pi))))

print('\n=== F2  propagation dispersion of the 4D icosian lattice (physical sector, k\'=0) ===')
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'route56_inertia.py')).read().split('rng=np.random.default_rng(8)')[0]
ns = {'__file__': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'route56_inertia.py'), '__name__': 'hdr'}; exec(src, ns)
Eg = ns['Eg']; r2 = np.random.default_rng(1)
dirs = r2.normal(size=(400, 4)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
J2 = lambda k: float(besselj(2, k))
print('  exact claim: the 60 pairs of the 600-cell form a spherical 11-design => V(k) = 120 J_2(|k|)/|k| k_hat, E = 8 J_2(kappa)/kappa = kappa (1 - kappa^2/12 + kappa^4/384 - ...)')
print('  kappa   E_lattice(mean over 400 dirs)   spread(max-min)    8 J2/kappa     |diff|')
for kap in (0.001, 0.1, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0):
    Es = np.array([Eg(np.concatenate([kap*d, np.zeros(4)]))[0] for d in dirs])
    ex = 8*J2(kap)/kap
    print(f'  {kap:5.3f}   {Es.mean():.12f}            {Es.max()-Es.min():.2e}       {ex:.12f}   {abs(Es.mean()-ex):.2e}')
d1 = dirs[0]; k = 1e-3
Eb = Eg(np.concatenate([k*d1, np.zeros(4)]))[0]
print('  beta = (1 - E/kappa)/kappa^2 at kappa=1e-3:', (1-Eb/k)/k**2, '  (1/12 =', 1/12, ')')
f = lambda x: 8*besselj(2, x)/x
ks = np.linspace(0.5, 6, 5501); fv = [float(f(mpf(x))) for x in ks]; i0 = int(np.argmax(fv))
dfun = lambda x: mp.diff(f, x)
kstar = findroot(dfun, ks[i0]); Emax = f(kstar); j21 = besseljzero(2, 1)
print('  band top: kappa* =', nstr(kstar, 15), ' E_max =', nstr(Emax, 15), ';  first zero shell j_{2,1} =', nstr(j21, 15))
for n, x in [('1/12', mpf(1)/12), ('E_max', Emax), ('kappa*', kstar), ('j21', j21), ('j21/kappa*', j21/kstar), ('E_max/kappa*', Emax/kstar)]:
    print(f'     {n:12s} {nstr(x,12):>16s}   x/alpha = {nstr(x/al,10):>14s}   alpha/x = {nstr(al/x,10):>14s}')
vm = ns['vmat']
print('  speed matrix at internal label k\' (eigenvalue mean of vmat): ', {r: round(float(np.mean(np.linalg.eigvalsh(vm(r*np.array([1, 0, 0, 0]))))), 6) for r in (0.0, 0.5, 1.0, 2.0)})

print('\n=== F3  cross-scale reinjection and mixing of the 144 ten-cycles ===')
Pm = np.zeros((NH, NH))
for i, (u, s) in enumerate(H):
    for t in nbr[s]: Pm[hid[(s, t)], i] += 1/12
ev = np.linalg.eigvals(Pm); mods = np.round(np.abs(ev), 9)
vals, cnt = np.unique(mods, return_counts=True)
print('  random-exit chain P on 1,440 histories: distinct |eigenvalue| (mult):', [(float(v), int(c)) for v, c in sorted(zip(vals, cnt), key=lambda t: -t[0])])
print('  top-level ratios: |lambda2| = phi/2 =', phi/2, ';  (phi/2)^30 =', (phi/2)**30, ';  gain 1/(1-(phi/2)^30) =', 1/(1-(phi/2)**30))
print('  (phi/2)^30 / alpha =', (phi/2)**30/al, ';  (gain-1)/alpha =', (1/(1-(phi/2)**30)-1)/al)
Tm = np.zeros((NH, NH)); Tm[Tn, np.arange(NH)] = 1
for w in (1/12, 1/6, 1/2, 1.0):
    Mw = (1-w)*Tm + w*Pm; e = np.linalg.eigvals(Mw); m = np.sort(np.abs(e))[::-1]
    nz = [x for x in m if x < 1-1e-9]
    print(f'  M_w = (1-w) T + w P, w = {w:.4f}: eigenvalues on the unit circle {int(np.sum(m > 1-1e-9))}, largest |lambda| below 1 = {nz[0]:.9f}')
cyc_id = -np.ones(NH, int); cc = 0
for i in range(NH):
    if cyc_id[i] < 0:
        j = i
        while cyc_id[j] < 0: cyc_id[j] = cc; j = Tn[j]
        cc += 1
Bm = np.zeros((cc, cc))
for i in range(NH):
    for t in np.nonzero(Pm[:, i])[0]: Bm[cyc_id[t], cyc_id[i]] += Pm[t, i]/10
eb = np.sort(np.abs(np.linalg.eigvals(Bm)))[::-1]
print('  coarse-grained chain on the', cc, 'ten-cycles: top |eigenvalues|', [round(float(x), 9) for x in eb[:8]])

print('\n=== F4  recursion-limit sums over the contraction ladder ===')
qs = {'phi/2': phi/2, '1/phi': 1/phi, '1/phi^2': 1/phi**2, 'gap': 1-phi/2, '(phi/2)^5': (phi/2)**5, '(phi/2)^10': (phi/2)**10,
      '(phi/2)^12': (phi/2)**12, '(phi/2)^30': (phi/2)**30, '1/12': 1/12, '1/144': 1/144}
def forms(q):
    n = np.arange(1, 4000); qn = q**n; ok = qn > 1e-300
    n = n[ok]; qn = qn[ok]
    Pq = float(np.exp(-np.sum(np.log1p(-qn)))); th = 1+2*np.sum(q**(np.arange(1, 400)**2.0))
    return {'geo': 1/(1-q), 'part': Pq, 'euler': 1/Pq, 'theta3': th, 'nq': q/(1-q)**2, 'lambert': np.sum(qn/(1-qn)), 'sigma': np.sum(n*qn/(1-qn))}
vals_ = {}
for qn_, q in qs.items():
    for fn, v in forms(q).items():
        if v > 0 and np.isfinite(v): vals_[f'{fn}({qn_})'] = v
names = list(vals_); lv = np.array([math.log(vals_[n]) for n in names])
fr30 = sorted({Fraction(a, b) for a in range(1, 31) for b in range(1, 31)}); lr30 = np.array([math.log(f.numerator/f.denominator) for f in fr30])
fr12 = sorted({Fraction(a, b) for a in range(1, 13) for b in range(1, 13)}); lr12 = np.array([math.log(f.numerator/f.denominator) for f in fr12])
P4 = (-2, -1, 1, 2); arrs = []; lab = []
for i in range(len(names)):
    for p in P4:
        arrs.append(lr30+p*lv[i]); lab.append((i, p, -1, 0, 30))
for i in range(len(names)):
    for j in range(i+1, len(names)):
        for p in P4:
            for q_ in P4:
                arrs.append(lr12+p*lv[i]+q_*lv[j]); lab.append((i, p, j, q_, 12))
L = np.concatenate(arrs); sizes = np.array([len(a) for a in arrs]); starts = np.concatenate([[0], np.cumsum(sizes)])
order_ = np.argsort(L); Ls = L[order_]
tol = 1e-9
def cnt_(lt): return int(np.searchsorted(Ls, lt+tol)-np.searchsorted(Ls, lt-tol))
def lab_of(pos):
    g = int(np.searchsorted(starts, pos, side='right')-1); i, p, j, q_, rr = lab[g]; frs = fr30 if rr == 30 else fr12
    f = frs[pos-starts[g]]; s = f'({f.numerator}/{f.denominator})*{names[i]}^{p}'
    return s+(f'*{names[j]}^{q_}' if j >= 0 else '')
print(f'  {len(names)} sum/product values over {len(qs)} contraction ratios; {len(L)} expressions (singles with a,b<=30; pairs with a,b<=12); tolerance {tol}')
rr = np.random.default_rng(3)
for tn, tv in targets.items():
    lt = math.log(tv); real = cnt_(lt)
    dec = [cnt_(lt+u) for u in rr.uniform(-1.5, 1.5, 1500) if abs(u) > 0.02]
    j0 = np.searchsorted(Ls, lt-tol); j1 = np.searchsorted(Ls, lt+tol)
    print(f'  target {tn:10s}: hits {real}   decoy mean {np.mean(dec):.2e} (max {max(dec)})')
    for jj in range(j0, j1): print('     HIT:', lab_of(order_[jj]), math.exp(Ls[jj]))
    near = np.argsort(np.abs(Ls-lt))[:3]
    for jj in sorted(near, key=lambda x: abs(Ls[x]-lt)): print(f'       nearest: {lab_of(order_[jj]):70s} rel err {math.exp(Ls[jj]-lt)-1:+.2e}')
