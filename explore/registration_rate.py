"""
energy = registration rate, made computable on the carrier (2I / 600-cell).

Claim under test: for the committed 2nd-order wave on the lattice, the phase a
mode actually REGISTERS per tick (measured from the dynamics, not assumed) equals
its energy omega(mu) = arccos(1 - (c^2/2) mu), mu = 12 - lambda the Laplacian
eigenvalue.  Then: one full registration = 2pi phase = one period; E*T = 2pi (h).
Also tabulate the dynamical rate against the Galois mass readout {12,4,4,0} and
report honestly whether they agree or invert.

Cold, no fitting: the only inputs are the carrier geometry and the wave update.
"""
import numpy as np, itertools
from itertools import permutations

phi = (1 + 5**0.5) / 2
psi = -1/phi

# ---- 1. the 120 icosians (unit quaternions = 600-cell vertices) -------------
V = []
# 8 units: (+-1,0,0,0) and perms
for i in range(4):
    for s in (1, -1):
        v = [0,0,0,0]; v[i] = s; V.append(v)
# 16: (+-1/2)^4
for s in itertools.product((0.5,-0.5), repeat=4):
    V.append(list(s))
# 96: even perms of (0, 1/2, phi/2, 1/(2phi)) with independent signs on the 3 nonzero
base = [0.0, 0.5, phi/2, 1/(2*phi)]
def parity(p):
    p=list(p); seen=[False]*len(p); par=0
    for i in range(len(p)):
        if seen[i]: continue
        j=i; cl=0
        while not seen[j]:
            seen[j]=True; j=p[j]; cl+=1
        par += cl-1
    return par % 2
even = [p for p in permutations(range(4)) if parity(p)==0]   # 12
for p in even:
    vals = [base[p[i]] for i in range(4)]
    nz = [i for i in range(4) if vals[i] != 0.0]              # 3 nonzero slots
    for ss in itertools.product((1,-1), repeat=3):
        v = list(vals)
        for k, idx in enumerate(nz):
            v[idx] = vals[idx]*ss[k]
        V.append(v)
V = np.array(V)
# dedupe defensively
Vu = np.unique(np.round(V, 9), axis=0)
print(f"[carrier] icosians built: {len(V)} raw, {len(Vu)} unique (expect 120)")
V = Vu

# ---- 2. adjacency: neighbours when overlap = phi/2 --------------------------
G = V @ V.T
A = (np.abs(G - phi/2) < 1e-6).astype(float)
np.fill_diagonal(A, 0.0)
deg = A.sum(1)
print(f"[carrier] degree: min {deg.min():.0f} max {deg.max():.0f} (expect 12 regular)")

# ---- 3. adjacency spectrum (should be the native tick/mass eigenvalues) -----
w = np.linalg.eigvalsh(A)
vals, cnts = np.unique(np.round(w, 6), return_counts=True)
named = {12:"12", round(6*phi,6):"6phi", round(4*phi,6):"4phi", 3:"3", 0:"0",
         -2:"-2", round(-4/phi,6):"-4/phi", -3:"-3", round(6*psi,6):"6psi"}
print("\n[spectrum] adjacency eigenvalue  (mult)   name")
for v,c in sorted(zip(vals,cnts), reverse=True):
    print(f"   lambda = {v:9.5f}   x{c:<3d}   {named.get(round(v,6),'?')}")

# ---- 4. Galois mass readout on the matter lattice {1,3,3',5} ----------------
# lambda_d = 12 * U_{d-1}(cos pi/5)/d ; mass = sqrt|lambda_d * sigma(lambda_d)|
def U(n, x):            # Chebyshev U_n
    if n==0: return 1.0
    if n==1: return 2*x
    Um1, Un = 1.0, 2*x
    for _ in range(2, n+1):
        Um1, Un = Un, 2*x*Un - Um1
    return Un
x = phi/2  # cos(pi/5)
lam = {1: 12*U(0,x)/1, 3: 12*U(2,x)/3, "3'": -4/phi, 5: 12*U(4,x)/5}
# sigma swaps sqrt5 -> -sqrt5, i.e. phi<->psi; mass = sqrt|lam * lam_gal|
galmass = {1: (12, 12), 3: (4*phi, 4*psi), "3'": (-4/phi, -4*phi), 5: (0.0, 0.0)}
print("\n[Galois mass]  irrep   adj-lambda    m = sqrt|lam*sigma(lam)|")
massrow = {}
for d,(l,lg) in galmass.items():
    m = (abs(l*lg))**0.5
    massrow[d] = (l, m)
    print(f"   {str(d):>3}      {l:8.4f}       {m:6.3f}")

# ---- 5. the dynamics: 2nd-order wave, measure registration rate -------------
# scalar per-mode recurrence (modes decouple): a_{t+1} = (2 - c^2 mu) a_t - a_{t-1}
mu_max = 12 - w.min()
c = 0.5                      # stable: c^2 * mu_max <= 4
assert c*c*mu_max <= 4+1e-9, "unstable c"
def omega_formula(mu):
    val = 1 - 0.5*c*c*mu
    return float(np.arccos(np.clip(val,-1,1)))

# verify "energy = registration rate" ON THE FULL LATTICE for each distinct mode:
# init the lattice in a real eigenmode (standing start), run the full 120-dim
# update, and RECOVER omega from the realized trajectory (not assumed).
evec = {}
wA, UA = np.linalg.eigh(A)
for target in vals:
    idx = np.argmin(np.abs(wA - target))
    evec[round(target,6)] = UA[:, idx]

def measure_rate(u, steps=400):
    u = u/np.linalg.norm(u)
    mu = 12 - float(u @ (A @ u))              # Laplacian eigenvalue of this mode
    prev = u.copy(); cur = u.copy()           # standing start (zero velocity)
    coss = []
    for t in range(steps):
        nxt = (2.0)*cur - prev - c*c*(12*cur - A@cur)
        a_p = prev @ u; a_c = cur @ u; a_n = nxt @ u
        if abs(a_c) > 1e-9:
            coss.append((a_n + a_p)/(2*a_c))   # = cos(omega), realized by the run
        prev, cur = cur, nxt
    cosw = np.median(coss)
    return mu, float(np.arccos(np.clip(cosw,-1,1)))

print("\n[registration rate]  measured from the lattice dynamics (c=%.2f)" % c)
print("  adj-lambda   mu=12-lambda    omega_measured   omega_formula    period 2pi/omega (ticks)")
rate = {}
for target in sorted(vals, reverse=True):
    u = evec[round(target,6)]
    mu, om = measure_rate(u)
    omf = omega_formula(mu)
    per = (2*np.pi/om) if om > 1e-9 else float('inf')
    rate[round(target,6)] = om
    print(f"   {target:8.4f}    {mu:8.4f}    {om:12.6f}    {omf:12.6f}    {per:10.3f}")

# ---- 6. rate vs Galois mass: agree or invert? -------------------------------
print("\n[rate vs Galois mass] on the matter lattice {1,3,3',5}")
print("  irrep   adj-lambda   Galois m   dispersion omega(=energy=reg.rate)")
for d,(l,m) in massrow.items():
    om = rate.get(round(l,6), None)
    oms = f"{om:.6f}" if om is not None else "n/a"
    print(f"   {str(d):>3}     {l:8.4f}    {m:6.3f}      {oms}")

# ---- 7. the 2pi / informational closure -------------------------------------
print("\n[2pi closure] one registration = one period = 2pi phase")
print("  For any mode: E*T = (hbar*omega)*(2pi/omega) = 2*pi*hbar = h  (one quantum of action).")
print("  Compton-Bekenstein: at R = Compton wavelength, R*E = hbar*c, so Bekenstein")
print(f"  bound = 2*pi nats = 2*pi/ln2 = {2*np.pi/np.log(2):.4f} bits  (floor BC = 9.06).")
print("  => registration rate omega = information per tick (nats/tick); one 2pi = one registration.")
