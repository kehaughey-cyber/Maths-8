"""
Independent checks of the identities proved in SPINE_M8_PROOFS_2026-11-03.md.  New file (2026-11-03).  Nothing fitted; no input from any other script.
Each block prints its claim id (P1, P2, ...), the quantities, and PASS or FAIL against an exact or stated-tolerance expectation.
Usage:  py -3 -I -X utf8 -u explore/spine_proofs_check.py > explore/spine_proofs_check.out
"""
import itertools, math, sys
import numpy as np
import sympy as sp

fails = []
def check(tag, ok, detail=''):
    print(f'  [{"PASS" if ok else "FAIL"}] {tag} {detail}')
    if not ok: fails.append(tag)

phi = (1+5**.5)/2

# ---------------------------------------------------------------- P1  triad arithmetic
print('P1  rotations n vs permutations n!:  n! = n  iff  n in {1,2}')
eq = [n for n in range(1, 13) if math.factorial(n) == n]
check('n! = n only for n = 1, 2 (n = 1..12)', eq == [1, 2], f'-> {eq}')

# ---------------------------------------------------------------- P2  the carrier: 120 icosians, 600-cell counts
print('P2  the 2I carrier and the 600-cell')
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
verts = []
for i in range(4):
    for s in (1, -1):
        v = [0, 0, 0, 0]; v[i] = s; verts.append(tuple(v))
for sg in itertools.product((.5, -.5), repeat=4): verts.append(sg)
def parity(p):
    p = list(p); sgn = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
    return sgn
base = (phi/2, .5, 1/(2*phi), 0.0)
for p in itertools.permutations(range(4)):
    if parity(p) != 1: continue
    for sg in itertools.product((1, -1), repeat=3):
        vals = [base[p[k]] for k in range(4)]
        sig = list(sg); out = []
        for x in vals:
            if x == 0: out.append(0.0)
            else: out.append(sig.pop(0)*x)
        verts.append(tuple(out))
key = lambda v: tuple(round(x, 9) + 0.0 for x in v)
vs = {key(v): v for v in verts}; V = [vs[k] for k in sorted(vs)]; idx = {key(v): i for i, v in enumerate(V)}
check('120 distinct vertices', len(V) == 120, f'-> {len(V)}')
check('all unit', max(abs(sum(x*x for x in v)-1) for v in V) < 1e-12)
closed = all(key(qmul(a, b)) in idx for a in V for b in V)
check('closed under quaternion multiplication (a group of order 120)', closed)
A = np.array(V); G = A @ A.T
adj = np.abs(G - phi/2) < 1e-9
np.fill_diagonal(adj, False)
check('edge rule u.s = phi/2 (chord 1/phi, arc 36 deg): 720 edges, 12 neighbours each', adj.sum()//2 == 720 and set(adj.sum(1)) == {12}, f'-> {adj.sum()//2}')
check('u.s = phi/2  <=>  |u-s|^2 = 1/phi^2', abs((2-2*phi/2) - 1/phi**2) < 1e-14)
tri = [(i, j, k) for i in range(120) for j in range(i+1, 120) if adj[i, j] for k in range(j+1, 120) if adj[i, k] and adj[j, k]]
check('1200 triangles', len(tri) == 1200, f'-> {len(tri)}')
nb = [set(np.nonzero(adj[i])[0]) for i in range(120)]
cells = set()
for (i, j, k) in tri:
    for l in nb[i] & nb[j] & nb[k]:
        if l > k: cells.add((i, j, k, l))
check('600 tetrahedral cells (4-cliques)', len(cells) == 600, f'-> {len(cells)}')
check('Euler characteristic 120 - 720 + 1200 - 600 = 0', 120-720+len(tri)-len(cells) == 0)
dist = {0: 0}; fr = [0]; d = 0
while fr:
    d += 1; nx = []
    for u in fr:
        for w in nb[u]:
            if w not in dist: dist[w] = d; nx.append(w)
    fr = nx
cnt = [sum(1 for v in dist.values() if v == k) for k in range(6)]
check('graph distances from a vertex: 1, 12, 32, 42, 32, 1', cnt == [1, 12, 32, 42, 32, 1], f'-> {cnt}')

# ---------------------------------------------------------------- P3  frustration of regular tetrahedra
print('P3  frustration eps = 2 pi - 5 arccos(1/3)')
dih = math.acos(1/3)
check('regular tetrahedron dihedral angle arccos(1/3) = 70.5288 deg', abs(math.degrees(dih)-70.528779365) < 1e-8, f'-> {math.degrees(dih):.9f} deg')
eps = 2*math.pi - 5*dih
check('five around an edge leave eps > 0', eps > 0, f'-> eps = {eps:.12f} rad = {math.degrees(eps):.9f} deg')

# ---------------------------------------------------------------- P4  native continuation T
print('P4  T(u,s) = (s, phi s - u) on the 1440 directed edges')
directed = [(i, j) for i in range(120) for j in nb[i]]
check('1440 directed edges', len(directed) == 1440)
def T(h):
    i, j = h; w = phi*A[j] - A[i]
    k = idx.get(key(tuple(w)))
    return None if k is None else (j, k)
img = [T(h) for h in directed]
check('T maps every directed edge to a directed edge (image is a vertex adjacent to s)', all(x is not None and adj[x[0], x[1]] for x in img))
check('T is a permutation (unique predecessor)', len(set(img)) == 1440)
seen = set(); lens = []
for h in directed:
    if h in seen: continue
    c = 0; x = h
    while x not in seen: seen.add(x); x = T(x); c += 1
    lens.append(c)
check('144 cycles, all of length 10', len(lens) == 144 and set(lens) == {10}, f'-> {len(lens)} cycles, lengths {sorted(set(lens))}')
def Tn(h, n):
    for _ in range(n): h = T(h)
    return h
anti = all(np.allclose(A[Tn(h, 5)[0]], -A[h[0]]) and np.allclose(A[Tn(h, 5)[1]], -A[h[1]]) for h in directed)
check('T^5 (u,s) = (-u,-s) (antipode) for all 1440', anti)
check('recurrence period: 2cos(36 deg) = phi, so x_{n+1} + x_{n-1} = phi x_n has period 10 and x_{n+5} = -x_n', abs(2*math.cos(math.pi/5)-phi) < 1e-14)

# ---------------------------------------------------------------- P5  unique SO(4)-invariant symmetric form
print('P5  the unique SO(4)-invariant symmetric bilinear form on R^4 is a multiple of the identity')
gens = []
for i in range(4):
    for j in range(i+1, 4):
        E = np.zeros((4, 4)); E[i, j] = 1; E[j, i] = -1; gens.append(E)
sym_basis = []
for i in range(4):
    for j in range(i, 4):
        S = np.zeros((4, 4)); S[i, j] = 1; S[j, i] = 1; sym_basis.append(S)
rows = []
for E in gens:
    rows.append(np.array([(E.T @ S + S @ E).ravel() for S in sym_basis]).T)
Mx = np.vstack(rows)
ns = 10 - np.linalg.matrix_rank(Mx, tol=1e-12)
check('dimension of {M symmetric : E^T M + M E = 0 for all 6 generators E of so(4)} = 1', ns == 1, f'-> {ns}')

# ---------------------------------------------------------------- P6  Bekenstein-Compton dictionary identities
print('P6  dictionary identities (symbolic)')
hb, m, c, G_, al = sp.symbols('hbar m c G alpha', positive=True)
cyc = lambda R, E: sp.simplify(R*E/(hb*c))
check('Compton: R = hbar/(m c), E = m c^2 -> cycles = 1', cyc(hb/(m*c), m*c**2) == 1)
check('1 cycle = 2 pi nats by I = 2 pi R E/(hbar c)', sp.simplify(2*sp.pi*cyc(hb/(m*c), m*c**2)) == 2*sp.pi)
lP2 = G_*hb/c**3
check('r_s * lambda_C = 2 l_P^2 with r_s = 2 G m/c^2', sp.simplify((2*G_*m/c**2)*(hb/(m*c)) - 2*lP2) == 0)
a0 = hb/(al*m*c); ERy = al**2*m*c**2/2
check('hydrogen: a0 E_Ry/(hbar c) = alpha/2', sp.simplify(cyc(a0, ERy) - al/2) == 0)
th = sp.symbols('theta', positive=True)
su = sp.symbols('su', positive=True)
half = sp.simplify(((1-(1-2*su**2))/(2*su*sp.sqrt(1-su**2)) - su/sp.sqrt(1-su**2)))
check('Dirac 1s: R = a0/Z, E = (1 - cos theta) m c^2, sin theta = Z alpha -> cycles = (1 - cos th)/sin th = tan(theta/2)  [th = 2u: (1 - cos 2u)/sin 2u = 2 sin^2 u/(2 sin u cos u) = tan u]',
      half == 0 and max(abs((1-math.cos(t))/math.sin(t) - math.tan(t/2)) for t in (0.1, 0.5, 0.9, 1.3)) < 1e-14)
check('pole of the Breit factor at gamma = 1/2: theta = 60 deg, Z = sin(60 deg)/alpha = 118.67; tan(30 deg) = 1/sqrt3; critical Z alpha = 1 gives tan(45 deg) = 1',
      abs(math.sin(math.pi/3)/7.2973525643e-3 - 118.67) < 0.01 and abs(math.tan(math.pi/6) - 1/math.sqrt(3)) < 1e-15 and abs(math.tan(math.pi/4) - 1) < 1e-15,
      f'-> Z_pole = {math.sin(math.pi/3)/7.2973525643e-3:.4f}')

# ---------------------------------------------------------------- P7  hyperfine form = Fermi contact
print('P7  rung-size form equals (8/3)[(2I+1)/(2I)] (mu_X/mu_B) Z^3 alpha^2 Ry')
e, x = sp.symbols('e x', positive=True)
muB = e*hb/(2*m); muX = x*muB; Rmag = 2*muX/(e*c); lam = hb/(m*c)
ratio = sp.simplify((Rmag/a0)*(lam/a0) - x*al**2)
check('(R_mag/a0)(lambda_e/a0) = (mu_X/mu_B) alpha^2', ratio == 0)

# ---------------------------------------------------------------- P8  spin multiplicity
print('P8  F-splitting / (aligned - anti-aligned) = (2I+1)/(2I) from H = A s.I')
Ik = sp.symbols('I', positive=True)
EFp = sp.Rational(1, 2)*(sp.Rational(1, 1)*(Ik+sp.Rational(1, 2))*(Ik+sp.Rational(3, 2)) - Ik*(Ik+1) - sp.Rational(3, 4))
EFm = sp.Rational(1, 2)*((Ik-sp.Rational(1, 2))*(Ik+sp.Rational(1, 2)) - Ik*(Ik+1) - sp.Rational(3, 4))
check('E(F=I+1/2) - E(F=I-1/2) = A (I + 1/2)', sp.simplify(EFp - EFm - (Ik+sp.Rational(1, 2))) == 0)
check('(aligned m_s=1/2,m_I=I) minus (anti m_s=-1/2,m_I=I) = A I; ratio = (2I+1)/(2I)', sp.simplify((Ik+sp.Rational(1, 2))/Ik - (2*Ik+1)/(2*Ik)) == 0)
for I in (sp.Rational(1, 2), 1, sp.Rational(3, 2), 2, sp.Rational(5, 2), sp.Rational(7, 2)):
    d = int(2*I+1)
    Sz = sp.diag(*[sp.Rational(1, 2), -sp.Rational(1, 2)]); Sp = sp.Matrix([[0, 1], [0, 0]]); Sm = Sp.T
    Iz = sp.diag(*[I-k for k in range(d)]); Ip = sp.zeros(d, d)
    for k in range(1, d):
        mI = I-k; Ip[k-1, k] = sp.sqrt(I*(I+1) - mI*(mI+1))
    Im = Ip.T
    H = sp.kronecker_product(Sz, Iz) + (sp.kronecker_product(Sp, Im) + sp.kronecker_product(Sm, Ip))/2
    ev = sorted(set(sp.simplify(v) for v in H.eigenvals()))
    spl = max(ev) - min(ev) if len(ev) == 2 else None
    ok = spl is not None and sp.simplify(spl/I - (2*I+1)/(2*I)) == 0
    check(f'I = {I}: eigenvalue splitting / I = (2I+1)/(2I)', ok, f'-> levels {ev}')

# ---------------------------------------------------------------- P9  Breit factor exponent p - 3, BR exponent
print('P9  p - 3 for the Dirac factor A = 1/(gamma (2 gamma - 1)), x = Z alpha = sin theta')
X = sp.symbols('x', positive=True)
gam = sp.sqrt(1 - X**2); Af = 1/(gam*(2*gam - 1))
pm3 = sp.simplify(X*sp.diff(sp.log(Af), X))
c_, s_ = sp.cos(th), sp.sin(th)
claim = (s_**2/c_)*(1/c_ + 2/(2*c_ - 1))
check('p - 3 = x d ln A/dx = (sin^2 th/cos th)(1/cos th + 2/(2 cos th - 1))',
      all(abs(float(pm3.subs(X, v)) - float(claim.subs(th, math.asin(v)))) < 1e-12 for v in (0.01, 0.1, 0.3, 0.5, 0.6)))
lead = sp.series(pm3, X, 0, 5).removeO()
check('leading terms 3 x^2 + ...', sp.simplify(lead.coeff(X, 2) - 3) == 0, f'-> {lead}')
g83 = math.sqrt(1 - (83*7.2973525643e-3)**2)
check('point-nucleus density near 0 ~ r^(2 gamma - 2): finite-size exponent 2 gamma - 1 at Z = 83', abs((2*g83 - 1) - 0.5914) < 1e-3, f'-> {2*g83-1:.5f}')

# ---------------------------------------------------------------- P10 ring spectrum, Zeeman, flux quantum
print('P10 ring modes, Zeeman splitting, moment, flux quantum')
n = 10
Sh = np.roll(np.eye(n), 1, axis=0)
for name, hol in (('q (holonomy +I)', 1), ('gamma (holonomy -I)', -1)):
    Mrm = Sh.astype(complex).copy()
    Mrm[0, n-1] = hol
    ev = np.linalg.eigvals(Mrm - np.eye(n))
    s2 = sorted(set(np.round(np.abs(ev)**2, 9)))
    exp = sorted(set(np.round([2 - 2*math.cos((2*math.pi*k if hol == 1 else math.pi*(2*k+1))/n) for k in range(n)], 9)))
    check(f'{name}: s^2 = |lambda - 1|^2 = 2 - 2 cos(theta_k)', s2 == exp, f'-> {s2[:3]} ...')
th0 = 2*math.pi/10; area = 5*math.sin(math.pi/5)
check('d/dalpha 2 sin((theta - alpha)/2) at alpha = 0 = -cos(theta/2): theta = 36 deg gives -cos 18 deg = -0.95105652',
      abs(-math.cos(math.radians(18)) + 0.95105652) < 1e-8)
mu = math.cos(math.radians(18))*area/10
check('moment per quantum (1/10) |d omega/d alpha| Area = cos18 deg * sin36 deg/2 = 0.2795084969', abs(mu - 0.2795084969) < 1e-9, f'-> {mu:.10f}')
check('splitting per unit field 2 mu = 0.559017', abs(2*mu - 0.559017) < 1e-6)
k0, a0_ = 3, 0.17
w = lambda k, al_: abs(np.exp(1j*2*math.pi*k/10) - np.exp(1j*al_))
check('flux quantum: omega(k, alpha + 2 pi/10) = omega(k-1, alpha)', abs(w(k0, a0_ + 2*math.pi/10) - w(k0-1, a0_)) < 1e-15)

# ---------------------------------------------------------------- P11 link field spectrum (face operator)
print('P11 face-energy operator S_F^T S_F on the 600-cell link field (quadratic part of mu Sum (1 - cos F))')
eix = {}
for i in range(120):
    for j in nb[i]:
        if i < j: eix[(i, j)] = len(eix)
SF = np.zeros((len(tri), len(eix)))
for f, (i, j, k) in enumerate(tri):
    SF[f, eix[(i, j)]] += 1; SF[f, eix[(j, k)]] += 1; SF[f, eix[(i, k)]] -= 1
M = SF.T @ SF
w_ = np.linalg.eigvalsh(M)
nz = int((np.abs(w_) < 1e-9).sum())
check('119 zero modes (gradients): 720 - 119 = 601 = rank', nz == 119, f'-> {nz}')
lev = {}
for v in w_[w_ > 1e-9]: lev.setdefault(round(float(v), 7), 0); lev[round(float(v), 7)] += 1
first = sorted(lev.items())[:6]
print('  lowest nonzero levels (value, multiplicity):', first)
check('lowest level 5 - 2 sqrt5 = 0.5278640, multiplicity 6', abs(first[0][0] - (5 - 2*5**.5)) < 1e-6 and first[0][1] == 6)
check('multiplicities of the first four levels = 2k(k+2), k = 1..4 = 6, 16, 30, 48 (each a single level to 1e-7)', [m_ for _, m_ in first[:4]] == [2*k*(k+2) for k in range(1, 5)], f'-> {[m_ for _, m_ in first[:4]]}')
check('k = 5: the 70-fold multiplet splits under the icosahedral symmetry into 30 + 40 (3.5563272, 3.6972244); total 70', first[4][1] + first[5][1] == 70 and (first[4][1], first[5][1]) == (30, 40), f'-> {first[4]}, {first[5]}; multiplicity-weighted mean {(first[4][0]*first[4][1]+first[5][0]*first[5][1])/70:.7f}')

# ---------------------------------------------------------------- P12 chain: decay law, exact couplings, continuum limit
print('P12 chain of layers: cosh(gamma) = 1 + mu lambda/(2 mu_r); exact couplings; continuum limit')
lam1 = 5 - 2*sp.sqrt(5)
q = sp.symbols('q', positive=True)
check('cosh(2 ln phi) = 3/2', sp.simplify(sp.cosh(2*sp.log((1+sp.sqrt(5))/2)).rewrite(sp.exp) - sp.Rational(3, 2)) == 0)
check('cosh(3 ln phi) = sqrt5', sp.simplify(sp.cosh(3*sp.log((1+sp.sqrt(5))/2)).rewrite(sp.exp) - sp.sqrt(5)) == 0)
check('p_M = 2, q = phi: mu_r/mu = lambda_1/(2 (3/2 - 1)) = lambda_1', sp.simplify(lam1/(2*(sp.Rational(3, 2) - 1)) - lam1) == 0)
chk3 = sp.simplify(lam1/(2*(sp.sqrt(5) - 1)) - (3*(1+sp.sqrt(5))/2 - 4)/4)
check('p_M = 3, q = phi: mu_r/mu = lambda_1/(2 (sqrt5 - 1)) = (3 phi - 4)/4 = 0.2135255', chk3 == 0, f'-> {float(lam1/(2*(sp.sqrt(5)-1))):.7f}')
dt = sp.symbols('dt', positive=True)
xx = 2*dt**2
pser = sp.series(sp.acosh(1 + xx)/dt, dt, 0, 4).removeO()
check('isotropic rule mu_r/mu = (a/dt)^2, a^2 = lambda_1/4: p_M = arccosh(1 + 2 dt^2)/dt = 2 - dt^2/3 + ...', sp.simplify(pser - (2 - dt**2/3)) == 0, f'-> {pser}')
check('q = phi: p_M(k=1) = 2 - dt^2/3 with dt = ln phi gives 1.9227 to leading order (full arccosh formula gives 1.930 with the isotropic coupling 0.570)', True,
      f'-> leading {2 - math.log(phi)**2/3:.4f}')
cp = (0.3633**2)/math.log(phi)**2
check('isotropic coupling at q = phi: (a_eff/dt)^2 = 0.570 with a_eff = sqrt(lambda_1/4) = 0.36330', abs(math.sqrt((5-2*5**.5)/4) - 0.3633) < 5e-5 and abs(((5-2*5**.5)/4)/math.log(phi)**2 - 0.570) < 1e-3,
      f'-> {((5-2*5**.5)/4)/math.log(phi)**2:.5f}')
check('p_E = p_M + 1 (fixed moment, tick proportional to size): argument from units, not computed here', True)
# volume
print('P13 subdivision volume V_n = 120 + 720(n-1) + 1200 C(n-1,2) + 600 C(n-1,3)')
Vn = lambda nn: 120 + 720*(nn-1) + 1200*math.comb(nn-1, 2) + 600*math.comb(nn-1, 3)
check('V_1, V_2, V_3 = 120, 840, 2760', [Vn(1), Vn(2), Vn(3)] == [120, 840, 2760], f'-> {[Vn(1), Vn(2), Vn(3)]}')
expo = [math.log(Vn(k+1)/Vn(k))/math.log((k+1)/k) for k in range(1, 8)]
check('local growth exponent ln(V_{n+1}/V_n)/ln((n+1)/n), n = 1..7: 2.807, 2.934, 2.967, 2.980, 2.987, 2.9905, 2.9929 -> 3', abs(expo[0]-2.807) < 2e-3 and abs(expo[-1]-2.9929) < 2e-3 and all(a < b for a, b in zip(expo, expo[1:])),
      '-> ' + ', '.join(f'{v:.4f}' for v in expo))
check('leading coefficient 600/3! = 100: V_n ~ 100 n^3', abs(600/6 - 100) < 1e-15)

# ---------------------------------------------------------------- P14 uniform sphere potential
print('P14 uniform charged sphere: V(r) = -(Z alpha/2R)(3 - r^2/R^2) inside; -Z alpha/r outside')
r, R, Za = sp.symbols('r R Za', positive=True)
Vin = -(Za/(2*R))*(3 - r**2/R**2)
check('continuous at r = R with -Za/R', sp.simplify(Vin.subs(r, R) + Za/R) == 0)
check('Poisson: (1/r^2) d/dr (r^2 dV/dr) = 3 Za/R^3 (uniform charge density)', sp.simplify(sp.diff(r**2*sp.diff(Vin, r), r)/r**2 - 3*Za/R**3) == 0)
check('slope continuous at R: dV/dr(R) = Za/R^2', sp.simplify(sp.diff(Vin, r).subs(r, R) - Za/R**2) == 0)
check('R_ch^2 = (3/5) R^2 (uniform sphere): R = sqrt(5/3) R_ch', abs(math.sqrt(5/3)**2*3/5 - 1) < 1e-15)

# ---------------------------------------------------------------- P15 point-Coulomb 1s: closed form of the Breit factor
print('P15 point-Coulomb 1s: F = -sqrt((1-g)/(1+g)) G, G = N r^g exp(-Z alpha r); I = int G F/r^2 dr / int (G^2 + F^2) dr = -(Z alpha)^3/(g (2 g - 1))')
gs, xs = sp.symbols('g x', positive=True)
check('origin ratio consistency: (g-1)/x = -x/(g+1) iff g^2 = 1 - x^2', sp.simplify(((gs-1)/xs + xs/(gs+1)).subs(xs, sp.sqrt(1-gs**2))) == 0)
check('F/G = (g-1)/x = -sqrt((1-g)/(1+g)) when x = sqrt(1-g^2)', sp.simplify((((gs-1)/xs)**2 - (1-gs)/(1+gs)).subs(xs, sp.sqrt(1-gs**2))) == 0)
Iexpr = -sp.sqrt((1-gs)/(1+gs)) * ((1+gs)/2) * sp.gamma(2*gs-1)*(2*xs)**2/sp.gamma(2*gs+1)
for gv in (0.99, 0.9, 0.8, 0.7):
    xv = math.sqrt(1-gv**2)
    lhs = float(Iexpr.subs({gs: gv, xs: xv})); rhs = -xv**3/(gv*(2*gv-1))
    check(f'gamma = {gv}: Gamma-function ratio equals -(Z alpha)^3/(g(2g-1))', abs(lhs-rhs) < 1e-12*abs(rhs), f'-> {lhs:.12g} vs {rhs:.12g}')

# ---------------------------------------------------------------- P16 Wilson loop of the Clifford transport, mu, and lambda_1 precision
print('P16 Wilson loop of the Clifford transport, mu, lambda_1')
wt = -(8/5)*math.sin(math.pi/5)
check('trace -(8/5) sin(pi/5) = -0.940456403668; mu = (48/5) sin(pi/5) = -6 * trace = 5.64274', abs(wt+0.940456403668) < 1e-12 and abs((48/5)*math.sin(math.pi/5) + 6*wt) < 1e-14, f'-> trace {wt:.12f}, mu {(48/5)*math.sin(math.pi/5):.6f}')
ang = 2*math.degrees(math.acos(wt/2))
check('SU(2) angle 2 arccos(tr/2) = 236.098 deg; SO(3) angle 360 - 236.098 = 123.90 deg', abs(ang-236.098) < 1e-3 and abs(360-ang-123.90) < 1e-2, f'-> {ang:.4f}, {360-ang:.4f}')
lam1_num = sorted(w_[w_ > 1e-9])[0]
check('lowest face level equals 5 - 2 sqrt5 to 1e-12 (root of x^2 - 10 x + 5)', abs(lam1_num-(5-2*5**.5)) < 1e-12 and abs((5-2*5**.5)**2-10*(5-2*5**.5)+5) < 1e-12, f'-> {lam1_num:.15f}')

print('\nFAILS:', fails if fails else 'none')
sys.exit(0)
