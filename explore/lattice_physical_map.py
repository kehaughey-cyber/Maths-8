# Put physical units on the lattice(1).html machine and place it on the size axis of our maps. New file; nothing fitted; no lattice feature is adjusted to a rung.
# Lattice (rebuilt cold here as the html does): 600-cell vertices (120) on the unit S^3, edges where dot = phi/2, tick q -> g5 q g6 with an order-5 and an order-6 unit
# (the html uses V[8], V[73] in its own ordering; here the first pair of units of those orders whose tick has four 30-cycles is used), clocks, shells by w.
# Anchor (floor nodes 17/18/33, a declared non-discriminating bridge): the edge at tower scale k = 0 is the Planck length, tick = edge/c; scale k multiplies lengths by phi^k (the html's tower).
# Everything after the anchor line is arithmetic on that assumption.
# Run: py -3 -I -X utf8 -u explore/lattice_physical_map.py > explore/lattice_physical_map.out
import functools, itertools, math, random
from math import sqrt, pi, log, acos
PHI = (1 + sqrt(5))/2; PSI = PHI - 1
def evenperms(n):
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        if inv % 2 == 0: yield p
def gen_vertices():
    V = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0]*4; v[i] = float(s); V.append(v)
    for m in range(16): V.append([(-.5 if m & 1 else .5), (-.5 if m & 2 else .5), (-.5 if m & 4 else .5), (-.5 if m & 8 else .5)])
    base = [0, .5, PHI/2, PSI/2]
    for p in evenperms(4):
        for m in range(8):
            v = [0.0]*4; bit = 0
            for i in range(4):
                mag = base[p[i]]
                if mag == 0: v[i] = 0.0
                else:
                    v[i] = -mag if (m >> bit) & 1 else mag; bit += 1
            V.append(v)
    out = []
    for v in V:
        if not any(sum((a - b)**2 for a, b in zip(v, u)) < 1e-12 for u in out): out.append(v)
    return out
dot = lambda a, b: sum(x*y for x, y in zip(a, b))
V = gen_vertices()
E = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V)) if abs(dot(V[i], V[j]) - PHI/2) < 1e-9]
print('LATTICE (cold): vertices %d, edges %d, edge chord %.6f (= 1/phi on the unit sphere), edge arc %.4f deg (= 36), S^3 radius / chord = %.6f (= phi)' % (len(V), len(E), sqrt(2 - PHI), math.degrees(acos(PHI/2)), 1/sqrt(2 - PHI)))
ADJ = [[] for _ in V]
for i, j in E:
    ADJ[i].append(j); ADJ[j].append(i)
def bfs(s):
    d = {s: 0}; q = [s]
    for u in q:
        for w in ADJ[u]:
            if w not in d:
                d[w] = d[u] + 1; q.append(w)
    return d
dd = bfs(0)
print('  neighbours per vertex: %s ; graph diameter %d ; vertices at graph distance 0..%d from a vertex: %s' % (sorted(set(len(a) for a in ADJ)), max(dd.values()), max(dd.values()), [sum(1 for x in dd.values() if x == k) for k in range(max(dd.values()) + 1)]))
shells = {}
for v in V:
    key = round(v[0], 6); shells[key] = shells.get(key, 0) + 1
print('  w-shells (w: count): ' + ', '.join('%.4f:%d' % (w, n) for w, n in sorted(shells.items(), reverse=True)))
qmul = lambda a, b: [a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3], a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2], a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1], a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]]
def idx(q):
    for i, v in enumerate(V):
        if sum((a - b)**2 for a, b in zip(q, v)) < 1e-9: return i
    return -1
def order(g):
    x = list(g); n = 1
    while n < 200:
        if abs(x[0] - 1) < 1e-9 and all(abs(c) < 1e-9 for c in x[1:]): return n
        x = qmul(x, g); n += 1
    return None
orders = [order(v) for v in V]
g5s = [i for i, o in enumerate(orders) if o == 5]; g6s = [i for i, o in enumerate(orders) if o == 6]
found = None
for a in g5s[:40]:
    for b in g6s[:40]:
        T = [idx(qmul(qmul(V[a], v), V[b])) for v in V]
        if -1 in T: continue
        seen = [False]*len(V); lens = []
        for s in range(len(V)):
            if seen[s]: continue
            i = s; n = 0
            while not seen[i]:
                seen[i] = True; i = T[i]; n += 1
            lens.append(n)
        if sorted(lens) == [30, 30, 30, 30]:
            found = (a, b, T, lens); break
    if found: break
a, b, T, lens = found
t15 = functools.reduce(lambda x, _: T[x], range(15), 0)
print('  tick q -> g5 q g6 with g5 of order %s and g6 of order %s: cycle lengths %s ; after 15 ticks vertex 0 sits at dot %.6f with its start (the fold: -1 = antipode)' % (orders[a], orders[b], lens, dot(V[0], V[t15])))
print()
c = 299792458.0; hbar = 1.054571817e-34; G = 6.67430e-11; lP = sqrt(hbar*G/c**3); tP = lP/c      # full precision (CODATA 2018 constants; G = 6.67430(15)e-11)
print('ANCHOR (assumption, non-discriminating): edge at scale k = 0 is l_P = %.6e m, tick = l_P/c = %.6e s, front speed c (the wave advances one edge per tick by construction)' % (lP, tP))
print('  at scale k: edge = l_P phi^k; S^3 radius = phi x chord edge; tick = edge/c; 30-tick cycle = 30 ticks; fold = 15 ticks; the antipode is reached after 5 ticks (graph diameter)')
print('  w-shell heights at scale k in units of the S^3 radius: 1, phi/2 = %.6f, 1/2, psi/2 = %.6f, 0 (counts 1, 12, 20, 12, 30, 12, 20, 12, 1)' % (PHI/2, PSI/2))
print()
hc = 1.973269804e-7
a_dia = 3.56683e-10
rungs = [('tau Compton length', hc/1776.93e6), ('proton Compton length', hc/938.27208816e6), ('nucleon charge radius r_p (CODATA 2022)', 0.84075e-15), ('muon Compton length', hc/105.6583755e6), ('12C charge radius (IAEA)', 2.4702e-15),
         ('electron Compton length', hc/0.51099895e6), ('C5+ 1s radius a0/6', 5.29177210903e-11/6), ('Bohr radius a0', 5.29177210903e-11), ('diamond C-C bond', a_dia*sqrt(3)/4), ('diamond lattice constant', a_dia),
         ('radius of 1 g of diamond (sphere)', 4.0808074e-3), ('Hubble radius c/H0 (order of magnitude, recalled)', 4.4e26)]
print('RUNGS on the tower: k = log_phi(R / l_P) if the rung is read as one lattice edge (subtract 1 to read it as the S^3 radius; same fractional part). Nearest integer scale, offset, and the factor the rung is off from that scale.')
print('%-52s %-11s %-10s %-8s %-8s %-8s %-14s %-12s' % ('rung', 'R (m)', 'k_edge', 'nearest', 'offset', 'factor', 'tick if edge s', '30 ticks s'))
fr = []
for nm, R in rungs:
    k = log(R/lP)/log(PHI); kn = round(k); f = k - kn; fr.append(k - math.floor(k))
    print('%-52s %-11.4e %-10.4f %-8d %+8.4f %-8.4f %-14.4e %-12.4e' % (nm, R, k, kn, f, PHI**f, R/c, 30*R/c))
print()
print('Fractional parts of k_edge (raw): ' + ' '.join('%.3f' % x for x in fr))
n = len(fr); rbar = abs(sum(complex(math.cos(2*pi*x), math.sin(2*pi*x)) for x in fr))/n
random.seed(1); ge = 0; N = 100000
for _ in range(N):
    z = abs(sum(complex(math.cos(2*pi*u), math.sin(2*pi*u)) for u in (random.random() for _ in range(n))))/n
    if z >= rbar: ge += 1
print('  mean resultant length of the fractional parts = %.4f (1 = identical offsets, 0 = evenly spread); %d independent uniform values reach %.4f or more with probability %.3f (Monte Carlo, %d draws)' % (rbar, n, rbar, ge/N, N))
print('  a different anchor (l_P times s) shifts every k by the same log_phi(s) and leaves this statistic unchanged: it asks only whether the rungs sit at one common offset in the tower.')
print('  the rungs are not independent (three Compton lengths are masses; a0 = lambda_e/alpha), so the probability overstates the significance of any clustering.')
print()
print('Between neighbouring rungs, raw tower steps: ' + '; '.join('%s -> %s: %.3f' % (rungs[i][0].split(' (')[0], rungs[i + 1][0].split(' (')[0], log(rungs[i + 1][1]/rungs[i][1])/log(PHI)) for i in range(len(rungs) - 1)))
print('Planck length to Hubble radius: %.3f tower steps; Planck length to the radius of 1 g: %.3f' % (log(4.4e26/lP)/log(PHI), log(4.0808e-3/lP)/log(PHI)))

km = log(rungs[3][1]/lP)/log(PHI)
print()
print('PRECISION OF THE ONE NEAR-INTEGER ENTRY: muon Compton length k_edge = %.6f (offset from 96: %+.6f). Uncertainty on k from G = 6.67430(15)e-11: l_P changes by 1.1e-5 relative, so k by %.1e; from the muon mass (2.2e-8 relative): %.1e.' % (km, km - 96, 0.5*2.2e-5/log(PHI), 2.2e-8/log(PHI)))
print('  the offset is %.1f sigma_G from an exact integer. Reading the muon length instead as the unreduced Compton wavelength 2 pi x lambda-bar shifts k by log_phi(2 pi) = %.4f, so the near-integer position belongs to the reduced length with the Planck length l_P = sqrt(hbar G/c^3) as anchor.' % (abs(km - 96)/(0.5*2.2e-5/log(PHI)), log(2*pi)/log(PHI)))
print('  chance of landing within +-%.4f of an integer for one rung: %.4f; for any of %d rungs: %.3f; with the five anchors l_P, 2 pi l_P, l_P/sqrt(8 pi), l_P sqrt(4 pi), l_P/(2 pi) tried, about %.2f.' % (abs(km - 96), 2*abs(km - 96), len(rungs), 1 - (1 - 2*abs(km - 96))**len(rungs), 1 - (1 - 2*abs(km - 96))**(5*len(rungs))))
