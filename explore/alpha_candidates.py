# Candidate checks for alpha (1/137.036) against the floor's own structure. New file; floor untouched.
# Protocol for the grammar sweep is fixed before running: targets 1/alpha in [137.0359990, 137.0359992] (covers CODATA 2018 and 2022),
# tolerance 1e-9 relative, and a decoy calibration for the look-elsewhere rate. No free parameter is adjusted anywhere.
import numpy as np, math, itertools
from fractions import Fraction
phi = (1+5**.5)/2
al18 = 7.2973525693e-3; T18 = 1/al18; T22 = 137.035999177
Tmid = 0.5*(T18+T22)
pi = math.pi
print('1/alpha CODATA 2018', repr(T18), ' 2022', T22, ' mid', repr(Tmid), ' spread rel', abs(T22-T18)/Tmid)
print()

# ---------- C4/C5 : the floor's finite structure, exact replay ----------
verts = []
for i in range(4):
    for s in (1, -1):
        v = np.zeros(4); v[i] = s; verts.append(v)
for sg in itertools.product((.5, -.5), repeat=4): verts.append(np.array(sg))
def parity(p): return sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2
base = [phi/2, .5, 1/(2*phi), 0.0]
for p in itertools.permutations(range(4)):
    if parity(p): continue
    for sg in itertools.product((1, -1), repeat=3):
        v = np.zeros(4); k = 0
        for pos in range(4):
            val = base[p[pos]]
            if val != 0.0: v[pos] = val*sg[k]; k += 1
        verts.append(v)
V = np.array(verts)
key = lambda v: tuple(np.round(v, 6)+0.0)
idx = {key(v): i for i, v in enumerate(V)}
print('C4 floor carrier: vertices', len(V), ' unique', len(idx), ' all unit', np.allclose((V**2).sum(1), 1))
Gm = V@V.T
A = ((Gm > 0.8) & (Gm < 0.82)).astype(float)
print('   adjacency degree set', set(A.sum(1).astype(int)), ' overlap phi/2 =', phi/2)
nbr = [list(np.nonzero(A[i])[0]) for i in range(120)]
H = [(u, s) for u in range(120) for s in nbr[u]]
hid = {h: i for i, h in enumerate(H)}
def Tmap(h):
    u, s = h
    t = phi*V[s]-V[u]
    return (s, idx[key(t)])
Tn = [hid[Tmap(h)] for h in H]
seen = [False]*len(H); cyc = []
for i in range(len(H)):
    if not seen[i]:
        c = []; j = i
        while not seen[j]: seen[j] = True; c.append(j); j = Tn[j]
        cyc.append(len(c))
print('   histories', len(H), ' T cycles', len(cyc), ' lengths', sorted(set(cyc)))
def Tpow(i, n):
    for _ in range(n): i = Tn[i]
    return i
neg = lambda v: idx[key(-v)]
ok5 = all(H[Tpow(i, 5)] == (neg(V[H[i][0]]), neg(V[H[i][1]])) for i in range(len(H)))
print('   T^5 = antipode on all histories:', ok5, ' T^10 = identity on all:', all(Tpow(i, 10) == i for i in range(len(H))))
print('   => the finite carrier closes EXACTLY (spin doubling 2 pi -> -1, 4 pi -> +1 with zero excess); any alpha/2pi excess is not in the finite carrier.')
print()

# ---------- C5 : spectrum of the random-exit chain on the 120-vertex carrier (A/12) ----------
ev = np.round(np.linalg.eigvalsh(A), 9)
vals, cnt = np.unique(ev, return_counts=True)
print('C5 adjacency spectrum of the 600-cell graph (distinct, multiplicity); /12 = relaxation chain eigenvalues')
for v_, c_ in sorted(zip(vals, cnt), key=lambda t: -t[0]): print(f'   {v_:14.9f}  x{c_:3d}   /12 = {v_/12: .9f}')
mod = sorted(set(np.round(np.abs(vals), 9)), reverse=True)
print('   distinct |eigenvalue| ratios to the top (12):', [round(m/12, 9) for m in mod])
print('   alpha =', al18, ' 1/alpha =', T18, '  any ratio within 1e-6 of alpha or 1/alpha?',
      any(abs(m/12-al18)/al18 < 1e-6 or abs(12/m-T18)/T18 < 1e-6 for m in mod if m > 0))
print()

# ---------- C1/C2/C3/C6 : single-level identities, near-misses, hop counts ----------
eps = 2*pi-5*math.acos(1/3); xi = math.asin(3**.5/3); kap = (pi/3)**2
print('C1 single-level floor quantities in cycles (value/2pi for angles) and ratio to alpha')
q = [('tick 1/30', 1/30), ('radit 1/12', 1/12), ('eps/2pi', eps/(2*pi)), ('delta=2/9 rad /2pi', (2/9)/(2*pi)), ('K=ln(phi)/15 /2pi', math.log(phi)/15/(2*pi)),
     ('kappa=(pi/3)^2', kap), ('gap=1-phi/2', 1-phi/2), ('phi/2', phi/2), ('(phi/2)^30', (phi/2)**30), ('lean xi/2pi', xi/(2*pi)), ('2/15 (=1/3-1/5)', 2/15)]
for n, x in q: print(f'   {n:22s} {x:.10g}   alpha/x = {al18/x:.8g}   x/alpha = {x/al18:.8g}')
print('C2 near-misses (relative error to 1/alpha 2018):')
for n, x in [('exp(2pi)/4', math.exp(2*pi)/4), ('125 kappa', 125*kap), ('144 - 7', 137.0), ('12^2 (full cycle)', 144.0), ('(1-eps/2pi)^2 * 144', (1-eps/(2*pi))**2*144)]:
    print(f'   {n:22s} {x:.9f}   rel err {(x-T18)/T18:+.3e}')
print('C3 closure: 137.036/144 =', T18/144, '; (1-eps/2pi) =', 1-eps/(2*pi), '; (1-eps/2pi)^2 =', (1-eps/(2*pi))**2,
      '; exponent n with (1-eps/2pi)^n = 137.036/144:', math.log(T18/144)/math.log(1-eps/(2*pi)))
print('C6 floor hop counts per cycle (closest to 137.036):', {n: f'{abs(n-T18)/T18:.3f}' for n in (10, 30, 60, 120, 144, 1440)})
print('   alpha/2pi in cycles', al18/(2*pi), ' in ticks', 30*al18/(2*pi), ' ; 2pi/alpha =', 2*pi/al18, '; smallest floor beat is 1/30 cycle =', 1/30,
      ' ; beat F16 delta_nat/2pi =', (4*pi/15-xi)/(2*pi))
print('C9 coupling = (cell/wavelength)^2: EM cell = sqrt(alpha) lam_e =', al18**.5*3.8615926772e-13, 'm ; = sqrt(r_e lam_e):', (2.8179403245e-15*3.8615926772e-13)**.5)
print('   dispersion deviation coefficients from the ledger (lattice B): 0.0517 k^2 and 0.0248 (ka)^2 ; / alpha =', 0.0517/al18, 0.0248/al18)
print()

# ---------- C10 : grammar sweep with decoys ----------
S = {'pi': pi, 'phi': phi, 'sqrt2': 2**.5, 'sqrt3': 3**.5, 'sqrt5': 5**.5, 'e^pi': math.exp(pi), 'ln_phi': math.log(phi), 'acos(1/3)': math.acos(1/3),
     'eps': eps, '1-eps/2pi': 1-eps/(2*pi), 'gap=1-phi/2': 1-phi/2, 'phi/2': phi/2, '(phi/2)^30': (phi/2)**30, 'zeta30': 1/(1-(phi/2)**30),
     'sag=eps*zeta30/(864phi^2)': eps/(1-(phi/2)**30)/(864*phi**2), 'kappa': kap, 'G_nat=2phi^2pi^2/9': 2*phi**2*pi**2/9,
     'delta_nat=4pi/15-xi': 4*pi/15-xi, 'xi=asin(sqrt3/3)': xi, 'K=ln(phi)/15': math.log(phi)/15}
names = list(S); logS = np.array([math.log(S[n]) for n in names])
fr = sorted({Fraction(a, b) for a in range(1, 31) for b in range(1, 31)})
logR = np.array([math.log(f.numerator/f.denominator) for f in fr])
P = (-2, -1, 1, 2)
arrs = []; lab = []
for xi_ in range(len(names)):
    for p in P:
        arrs.append(logR+p*logS[xi_]); lab.append(np.stack([np.full(len(fr), xi_), np.full(len(fr), p), np.full(len(fr), -1), np.zeros(len(fr), int), np.arange(len(fr))], 1))
for xi_ in range(len(names)):
    for yi_ in range(xi_+1, len(names)):
        for p in P:
            for qq in P:
                arrs.append(logR+p*logS[xi_]+qq*logS[yi_]); lab.append(np.stack([np.full(len(fr), xi_), np.full(len(fr), p), np.full(len(fr), yi_), np.full(len(fr), qq), np.arange(len(fr))], 1))
L = np.concatenate(arrs); LB = np.concatenate(lab)
order = np.argsort(L); Ls = L[order]; LBs = LB[order]
N = len(L)
tol = 1e-9; logT = math.log(Tmid)
def count(lt):
    return int(np.searchsorted(Ls, lt+tol)-np.searchsorted(Ls, lt-tol))
def describe(row):
    xi_, p, yi_, qq, ri = row
    f = fr[ri]; s = f'({f.numerator}/{f.denominator})*{names[xi_]}^{p}'
    if yi_ >= 0: s += f'*{names[yi_]}^{qq}'
    return s
real = count(logT)
rng = np.random.default_rng(0)
dec = [count(logT+u) for u in rng.uniform(-1.5, 1.5, 2000) if abs(u) > 0.02]
print(f'C10 grammar sweep: {N} expressions (rationals a/b with a,b<=30; one or two factors from {len(names)} floor constants with exponents in {P}); tolerance {tol}')
print(f'   hits on the real target 1/alpha: {real}   decoy mean hits per target: {np.mean(dec):.3e} over {len(dec)} decoys (max {max(dec)})')
j0 = np.searchsorted(Ls, logT-tol); j1 = np.searchsorted(Ls, logT+tol)
for j in range(j0, j1): print('   HIT:', describe(LBs[j]), ' value', math.exp(Ls[j]))
nearest = np.argsort(np.abs(Ls-logT))[:8]
print('   nearest 8 expressions (relative error):')
for j in sorted(nearest, key=lambda j: abs(Ls[j]-logT)): print(f'     {describe(LBs[j]):60s} {math.exp(Ls[j]):.9f}  {math.exp(Ls[j]-logT)-1:+.2e}')
print('   typical nearest-miss scale = 1/(2 * density) ~', 1/(2*N/(Ls[-1]-Ls[0])))
